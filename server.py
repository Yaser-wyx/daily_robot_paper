from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
import re
import time
import json
import feedparser
import httpx
import uvicorn
import aiosqlite
import asyncio
from datetime import datetime, timedelta
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("RoboPulse")

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_PATH = "robopulse.db"

@app.get("/")
async def read_root():
    return FileResponse("paper.html")

# --- LLM Configuration ---
LLM_API_KEY = "AIzaSyBGcJiobPSJ33_a1ZeBsKP7Py9FAsU26z4"
GEMINI_MODEL = "gemini-3-pro-preview"
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com"
PROXY = "http://127.0.0.1:7890"
# PROXY = None
GEMINI_API_URL = f"{GEMINI_BASE_URL}/v1beta/models/{GEMINI_MODEL}:generateContent"

# --- Database & Models ---
class SummarizeRequest(BaseModel):
    title: str
    abstract: str
    paper_id: Optional[str] = None

async def init_db():
    logger.info(f"正在初始化数据库: {DB_PATH}")
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS papers (
                id TEXT PRIMARY KEY,
                title TEXT,
                abstract TEXT,
                authors TEXT,
                published_date TEXT,
                pdf_link TEXT,
                vlm_analysis TEXT,
                tags TEXT
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS briefings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                type TEXT,
                title TEXT,
                summary_content TEXT,
                selected_ids TEXT
            )
        """)
        await db.commit()

@app.on_event("startup")
async def startup_event():
    await init_db()
    asyncio.create_task(sync_arxiv_data())

# --- ArXiv Sync Engine ---
ARXIV_API_URL = "https://export.arxiv.org/api/query"

async def sync_arxiv_data(limit: int = 100):
    logger.info(f"开始同步 ArXiv 数据 (limit: {limit})...")
    params = {
        "search_query": "cat:cs.RO",
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "max_results": limit
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(ARXIV_API_URL, params=params, timeout=30.0)
            if response.status_code != 200:
                logger.error(f"ArXiv API 请求失败: {response.status_code}")
                return []
            
            feed = feedparser.parse(response.content)
            new_papers = []
            async with aiosqlite.connect(DB_PATH) as db:
                for entry in feed.entries:
                    paper_id = entry.id.split('/abs/')[-1].split('v')[0]
                    title = entry.title.replace('\n', ' ').strip()
                    abstract = entry.summary.replace('\n', ' ').strip()
                    author_list = [author.name for author in entry.authors]
                    published = entry.published[:10]
                    pdf_link = next((link.href for link in entry.links if link.type == 'application/pdf'), f"https://arxiv.org/pdf/{paper_id}.pdf")
                    
                    tags = []
                    text = (title + " " + abstract).lower()
                    if "humanoid" in text: tags.append("Humanoid")
                    if "vla" in text or "vision-language" in text: tags.append("VLA")
                    if "world model" in text: tags.append("World Model")
                    if "manipulation" in text: tags.append("Manipulation")
                    if "navigation" in text: tags.append("Nav")
                    if not tags: tags.append("General")

                    await db.execute("""
                        INSERT INTO papers (id, title, abstract, authors, published_date, pdf_link, tags)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                        ON CONFLICT(id) DO UPDATE SET
                        published_date=excluded.published_date
                    """, (paper_id, title, abstract, json.dumps(author_list), published, pdf_link, json.dumps(tags)))
                    
                    new_papers.append({"id": paper_id, "title": title})
                await db.commit()
            logger.info(f"ArXiv 同步成功，处理了 {len(new_papers)} 篇论文")
            return new_papers
        except Exception as e:
            logger.exception(f"同步过程中发生异常: {str(e)}")
            return []

@app.post("/api/sync")
async def manual_sync():
    """手动触发同步"""
    papers = await sync_arxiv_data(limit=50)
    return {"message": f"Sync complete. {len(papers)} papers updated.", "papers": papers}

# --- AI Pulse Engine ---
async def call_gemini(prompt: str):
    if LLM_API_KEY == "YOUR_GEMINI_API_KEY" or not LLM_API_KEY:
        return "⚠️ 请配置 API Key"
    
    logger.info(f"正在调用 Gemini API...")
    try:
        async with httpx.AsyncClient(proxy=PROXY) as client:
            response = await client.post(
                f"{GEMINI_API_URL}?key={LLM_API_KEY}",
                headers={"Content-Type": "application/json"},
                json={
                    "contents": [{"parts": [{"text": prompt}]}],
                    "generationConfig": {"temperature": 0.3}
                },
                timeout=120.0
            )
            if response.status_code == 200:
                return response.json()['candidates'][0]['content']['parts'][0]['text']
            else:
                logger.error(f"Gemini 响应错误: {response.text}")
                return f"Error: {response.text}"
    except Exception as e:
        logger.exception("Gemini 调用异常")
        return f"Exception: {str(e)}"

# --- API Endpoints ---

async def get_papers_by_ids(db, paper_ids: List[str]):
    papers = []
    for pid in paper_ids:
        cursor = await db.execute("SELECT * FROM papers WHERE id = ?", (pid,))
        row = await cursor.fetchone()
        if row:
            p = dict(row)
            p['authors'] = json.loads(p['authors'])
            p['tags'] = json.loads(p['tags'])
            papers.append(p)
    return papers

async def generate_briefing(db, briefing_type: str, date_str: str, days_limit: int = 1):
    # 确定时间跨度
    end_date = datetime.strptime(date_str, "%Y-%m-%d")
    start_date = end_date - timedelta(days=days_limit)
    start_date_str = start_date.strftime("%Y-%m-%d")

    logger.info(f"正在生成 {briefing_type} 简报 ({start_date_str} 至 {date_str})...")
    
    # 提取该时间段内的论文（或者最近的 X 篇）
    query = "SELECT * FROM papers WHERE published_date >= ? AND published_date <= ? ORDER BY published_date DESC LIMIT 50"
    cursor = await db.execute(query, (start_date_str, date_str))
    rows = await cursor.fetchall()
    
    if not rows:
        return False

    papers_context = ""
    for i, r in enumerate(rows):
        papers_context += f"[{i}] ID: {r['id']} | Title: {r['title']}\nAbstract: {r['abstract'][:300]}...\n\n"
    
    scale_name = "每日" if briefing_type == 'daily' else "每周" if briefing_type == 'weekly' else "每月"
    
    # 构建日期范围字符串
    date_range_str = date_str
    if briefing_type == 'weekly':
        date_range_str = f"{start_date_str} 至 {date_str}"
    elif briefing_type == 'monthly':
        date_range_str = f"{start_date_str} 至 {date_str}"

    prompt = f"""你是一个机器人学领域的顶级学术编辑，正在为专业研究人员撰写一份 Notion 风格的“RoboPulse 机器人学学术脉动”{scale_name}简报。
时间跨度：{date_range_str}

**输入数据**（最新的论文列表）：
{papers_context}

**任务要求：**
1. **主编精选 Top 10 (Editor's Choice)**：从输入中选出 10 篇最具影响力的论文，并按重要性从 1 到 10 排序。
2. **深度综述 (Trend Analysis)**：用 Markdown 撰写综述（约 800字）。
   - **关键：** 在综述中引用论文时，必须使用你在 Top 10 中给出的排名序号，格式为 [1], [2] ... [10]。
   - **严禁**引用不在 Top 10 列表中的论文。
   - 提炼核心技术趋势，并在趋势描述中嵌入这些序号。
3. **输出格式**：仅输出一个合法 JSON 对象，严禁代码块包裹。结构：
{{
  "title": "简报标题",
  "summary_content": "Markdown 综述内容 (引用格式 [1]-[10])",
  "selected_ids": ["与序号1对应的ID", "与序号2对应的ID", ..., "与序号10对应的ID"]
}}
"""
    raw_ai_res = await call_gemini(prompt)
    try:
        json_str = raw_ai_res.strip()
        if "```" in json_str: json_str = re.sub(r"```(?:json)?\s*|\s*```", "", json_str, flags=re.DOTALL)
        start, end = json_str.find('{'), json_str.rfind('}')
        if start != -1 and end != -1: json_str = json_str[start:end+1]
        
        ai_data = json.loads(json_str)
        title = ai_data.get('title') or f"RoboPulse {scale_name}简报"
        summary = ai_data.get('summary_content') or ai_data.get('summary')
        s_ids = ai_data.get('selected_ids') or []
        s_ids = [str(i) for i in s_ids] if isinstance(s_ids, list) else []

        await db.execute("""
            INSERT INTO briefings (date, type, title, summary_content, selected_ids)
            VALUES (?, ?, ?, ?, ?)
        """, (date_str, briefing_type, title, summary, json.dumps(s_ids)))
        await db.commit()
        return True
    except Exception as e:
        logger.error(f"解析失败: {e}")
        return False

@app.get("/api/pulse/{scale}")
async def get_pulse(scale: str, date: str = None):
    if scale not in ['daily', 'weekly', 'monthly']:
        raise HTTPException(status_code=400, detail="Invalid scale")
    
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        
        target_date = date or datetime.now().strftime("%Y-%m-%d")
        
        # 校验：不能查看未来
        today_str = datetime.now().strftime("%Y-%m-%d")
        if target_date > today_str:
             return {
                "empty": True,
                "title": "Future is Loading...",
                "date": target_date,
                "date_range": target_date,
                "summary_content": "### ⏳ 尚未发生\n\n我们无法预测未来，但您可以回顾过去。请选择今天或之前的日期。",
                "selected_papers": []
            }

        # 计算辅助信息：日期范围
        try:
            dt = datetime.strptime(target_date, "%Y-%m-%d")
        except ValueError:
             raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD")

        date_range_label = target_date
        if scale == 'weekly':
            start = dt - timedelta(days=6) # Weekly includes today, so -6 days
            date_range_label = f"{start.strftime('%Y-%m-%d')} ~ {target_date}"
        elif scale == 'monthly':
            start = dt - timedelta(days=29)
            date_range_label = f"{start.strftime('%Y-%m-%d')} ~ {target_date}"

        # 1. 查找是否存在指定日期的简报
        cursor = await db.execute("SELECT * FROM briefings WHERE type = ? AND date = ?", (scale, target_date))
        briefing_row = await cursor.fetchone()
        
        if briefing_row:
            res = dict(briefing_row)
            res['selected_papers'] = await get_papers_by_ids(db, json.loads(res['selected_ids']))
            res['date_range'] = date_range_label
            return res

        # 2. 不存在则生成
        days_map = {'daily': 2, 'weekly': 7, 'monthly': 30}
        success = await generate_briefing(db, scale, target_date, days_map[scale])
        
        if success:
            cursor = await db.execute("SELECT * FROM briefings WHERE type = ? AND date = ?", (scale, target_date))
            new_row = await cursor.fetchone()
            if new_row:
                res = dict(new_row)
                res['selected_papers'] = await get_papers_by_ids(db, json.loads(res['selected_ids']))
                res['date_range'] = date_range_label
                return res
        
        # 3. 生成失败（通常是因为没有论文），返回空状态
        return {
            "empty": True, 
            "title": "No Papers Found", 
            "date": target_date,
            "date_range": date_range_label,
            "summary_content": f"No papers were found for the period **{date_range_label}**. Try syncing ArXiv manually or checking another date.",
            "selected_papers": []
        }

@app.get("/api/stream")
async def get_stream(page: int = 0, size: int = 20):
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        cursor = await db.execute("""
            SELECT * FROM papers ORDER BY published_date DESC, id DESC LIMIT ? OFFSET ?
        """, (size, page * size))
        rows = await cursor.fetchall()
        papers = []
        for row in rows:
            p = dict(row)
            p['authors'] = json.loads(p['authors'])
            p['tags'] = json.loads(p['tags'])
            papers.append(p)
        return papers

@app.post("/api/analyze/{paper_id}")
async def analyze_paper(paper_id: str):
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        cursor = await db.execute("SELECT * FROM papers WHERE id = ?", (paper_id,))
        paper = await cursor.fetchone()
        if not paper: raise HTTPException(status_code=404, detail="Paper not found")
        if paper['vlm_analysis']: return {"analysis": paper['vlm_analysis']}
        
        prompt = f"""你是一个高级算法工程师。请对论文《{paper['title']}》进行类似 Notion 笔记风格的深度拆解。
        
摘要内容：{paper['abstract']}

**请按照以下 Markdown 格式输出（不要包含其他废话）：**

### 💡 一句话总结 (TL;DR)
> 用**粗体**写一句话，直击痛点和贡献。

### ✨ 核心亮点 (Key Highlights)
- **亮点 1**：...
- **亮点 2**：...
- **亮点 3**：...

### 📖 背景与意义
简要描述该工作解决了什么长期存在的问题，或者相比 SOTA 有什么提升。

### 🏷️ 核心标签
`Methodology Tag` `Application Tag`
"""
        analysis = await call_gemini(prompt)
        await db.execute("UPDATE papers SET vlm_analysis = ? WHERE id = ?", (analysis, paper_id))
        await db.commit()
        return {"analysis": analysis}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
