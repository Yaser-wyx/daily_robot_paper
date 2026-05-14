import os

ARXIV_URL = "https://arxiv.org/list/cs.RO/new"
ARXIV_ABS_URL = "https://arxiv.org/abs/{paper_id}"
ARXIV_HTML_URL = "https://arxiv.org/html/{paper_id}"
ARXIV_PDF_URL = "https://arxiv.org/pdf/{paper_id}"
REQUEST_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
}
CODEX_MODEL = os.environ.get("CODEX_MODEL", "").strip()
CHATGPT_WEB_URL = os.environ.get("CHATGPT_WEB_URL", "https://chatgpt.com/").strip()
INTERESTS = (
    "VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, "
    "World Model, World Action Model"
)
# Biased toward robot learning / manipulation / VLA / world-model authors who are
# active in embodied AI and likely to appear on cs.RO papers relevant to this brief.
CORE_VIP_AUTHORS = [
    "Sergey Levine",
    "Chelsea Finn",
    "Pieter Abbeel",
    "Dorsa Sadigh",
    "Shuran Song",
    "Yuke Zhu",
    "Jeannette Bohg",
    "Xiaolong Wang",
    "Huazhe Xu",
    "Hao Su",
    "Cewu Lu",
    "Jiangmiao Pang",
    "He Wang",
    "Donglin Wang",
    "Yue Wang",
]
EXTENDED_VIP_AUTHORS = [
    "Fei Xia",
    "Ted Xiao",
    "Karol Hausman",
    "Pierre Sermanet",
    "Dieter Fox",
    "Lerrel Pinto",
    "Pulkit Agrawal",
    "Deepak Pathak",
    "Abhinav Gupta",
    "Danfei Xu",
    "Jiajun Wu",
    "Siddharth Karamcheti",
    "Dhruv Shah",
    "Mohit Shridhar",
    "Daniela Rus",
    "Russ Tedrake",
]
VIP_AUTHORS = list(dict.fromkeys(CORE_VIP_AUTHORS + EXTENDED_VIP_AUTHORS))
OUTPUT_DIR = "./reports"
CODEX_BIN = None
ARXIV_NOT_UPDATED_EXIT_CODE = 75
GENERAL_FAILURE_EXIT_CODE = 1
SHORTLIST_TARGET = 10
SELECTED_TARGET = 6
SHORTLIST_CONTEXT_LIMIT = 4600
WATCHLIST_PREFIX = "W"
SECTION_PATTERNS = {
    "Abstract": [r"\babstract\b"],
    "Introduction": [r"\bintroduction\b", r"\boverview\b"],
    "Method": [r"\bmethod\b", r"\bapproach\b", r"\bframework\b", r"\bmodel\b", r"\balgorithm\b"],
    "Experiments": [r"\bexperiments?\b", r"\bevaluation\b", r"\bresults?\b", r"\bbenchmark\b"],
    "Conclusion": [r"\bconclusion\b", r"\bdiscussion\b", r"\blimitation\b", r"\bfinal remarks\b"],
}
