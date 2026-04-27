# RoboPulse | 2026-04-23

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 59 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线很清晰：VLA 正从“看当前就出动作”的反应式范式，转向带未来评估的 world model 规划、带几何瓶颈的控制表征，以及更可靠的校准与安全执行。最终精选覆盖了这条链路上的六个关键切口：跨具身预训练、工业部署中的计划执行、面向控制的 world model 表征、小模型 VLA 的知识注入、顺序决策校准，以及医疗场景中的 world-model RL。它们入选的共同原因不是单点指标，而是都在回答“怎样让机器人在长时程、分布变化和高风险场景下更稳地做对事”。VIP 作者里，今天最值得持续跟踪的是 watchlist 中 Pieter Abbeel 参与的 2506.02618；这次最终精选本身并未被 VIP 名单主导，更多体现的是主题贴合度而非作者光环。

## 今日信号

- 今天最值得记住的研究信号是：world model 在机器人里不再只是生成未来画面，而是在越来越多工作中直接承担候选轨迹评估、风险过滤和测试时决策支持。
- 今天最值得记住的研究信号是：面向控制的表示学习正在主动背离高保真 RGB 预测，转向语义掩码、几何约束和任务相关语义，以减少视觉噪声对策略的误导。
- 今天最值得记住的研究信号是：VLA 的下一阶段竞争力不仅取决于模型规模，还取决于跨具身动作统一、校准能力和在真实部署链路中闭环验证的工程完整度。

## Editor's Picks

### [1]. JoyAI-RA 0.1: A Foundation Model for Robotic Autonomy [[PDF]](https://arxiv.org/pdf/2604.20100) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.20100`
* **Authors**: Tianle Zhang, Zhihao Yuan, Dafeng Chi, Peidong Liu, Dongwei Li, Kejun Hu, Likui Zhang, Junnan Nie, Ziming Wei, Zengjue Chen, Yili Tang, Jiayi Li, Zhiyuan Xiang, Mingyang Li, Tianci Luo, Hanwen Wan, Ao Li, Linbo Zhai, Zhihao Zhan, Yuzheng Zhuang, Liang Lin, Xiaodong Bai, Jiakun Cai, Peng Cao, Kangliang Chen, Siang Chen, Yixiang Dai, Shuai Di, Nan Duan, Yicheng Gong, Chenguang Gui, Yucheng Guo, Peng Hao, Qingrong He, Haoyang Huang, Kunrui Huang, Zhixuan Huang, Shibo Jin, Yixiang Jin, Anson Li, Dongjiang Li, Jiawei Li, Ruodai Li, Yihang Li, Yuzhen Li, Jiaming Liang, Fangsheng Liu, Jing Long, Mingxi Luo, Xing Pan, Hui Shen, Xiaomeng Tian, Daming Wang, Song Wang, Junwu Xiong, Hang Xu, Wanting Xu, Zhengcheng Yu, He Zhang, Jiyao Zhang, Lin Zhao, Chen Zhou
* **Author Priority**: Standard
* **一句话结论**: 如果你关心通用机器人基础模型的数据来源与跨具身泛化，这篇值得优先看，但目前证据主要来自摘要，结论应保守吸收。
* **问题与切口**: 这篇工作把问题直接对准开放世界机器人自治的两大瓶颈：数据多样性不足，以及人类操作、仿真轨迹和真实机器人之间难以迁移。JoyAI-RA 的核心切口不是只扩大单一机器人数据，而是提出多源、多层级预训练框架，把网页数据、自我中心人类操作视频、仿真生成轨迹和真实机器人数据并入同一训练管线，再通过显式动作空间统一去缩小具身差异。相较常见只在机器人数据上扩量的路线，它更像是在搭一套“跨人类到机器人”的动作知识底座。
* **核心方法与证据**: 可确认的信息主要来自摘要回退：作者强调使用异构多源数据联合训练，并通过动作空间统一来桥接人类操作与机器人控制，目标是提升跨具身泛化，尤其是从人类操作到机器人执行的迁移。由于 arXiv HTML 不可用，正文中的具体模块设计、数据配比、训练阶段划分和评测协议都无法从当前材料中核实，因此这篇更适合作为“方向性强、证据待 PDF 落实”的基础模型候选，而不是现在就下细节判断。
* **正文要点**:
  - 工作主张用多源、多层级预训练统一整合网页数据、人类操作视频、仿真轨迹与真实机器人数据。
  - 论文明确把“显式动作空间统一”当成跨具身迁移的关键机制，而不是仅靠共享视觉语言表征。
  - 当前可见证据仅来自摘要，正文实验规模、对比对象和失败案例都还无法从 HTML 摘录确认。
* **为什么值得跟**:
  - 它直接回应了 VLA 领域最现实的数据瓶颈：真实机器人数据贵且覆盖窄。
  - 如果人类操作与机器人控制真能被统一到可迁移动作表征，跨具身学习会明显提速。
  - 它把机器人基础模型的竞争点从“谁的数据更多”推进到“谁能统一更多来源的动作知识”。
* **风险 / 保留意见**:
  - 只有摘要证据，当前无法判断性能提升究竟来自动作统一还是单纯来自数据规模扩张。
  - 跨具身泛化的边界不清楚，尚不能确认对新机器人形态和新任务的真实稳健性。
* **建议先看**: 拿到 PDF 后先看预训练数据组织方式和动作空间统一方案，再看跨具身评测是否真的覆盖人到机、仿真到真机和不同机器人之间的迁移。
* **关键词**: `VLA` `基础模型` `跨具身泛化` `多源预训练` `动作空间统一`
* **证据来源**: Abstract fallback
* **读 PDF 先核查**:
  - 动作空间统一具体怎样兼容人类操作、仿真控制和真实机器人控制信号？
  - 性能提升主要来自多源数据规模，还是来自统一后的表示与训练目标？
  - 跨具身泛化是否在未见机器人形态和未见任务组合上仍然成立？
* **上传 PDF 后优先看**:
  - 预训练数据构建与多阶段训练设计
  - 动作表示统一与跨具身对齐机制
  - 跨具身泛化评测与消融实验

### [2]. Cortex 2.0: Grounding World Models in Real-World Industrial Deployment [[HTML]](https://arxiv.org/html/2604.20246) [[PDF]](https://arxiv.org/pdf/2604.20246) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.20246`
* **Authors**: Adriana Aida, Walida Amer, Katarina Bankovic, Dhruv Behl, Fabian Busch, Annie Bhalla, Minh Duong, Florian Gienger, Rohan Godse, Denis Grachev, Ralf Gulde, Elisa Hagensieker, Junpeng Hu, Shivam Joshi, Tobias Knoblauch, Likith Kumar, Damien LaRocque, Keerthana Lokesh, Omar Moured, Khiem Nguyen, Christian Preyss, Ranjith Sriganesan, Vikram Singh, Carsten Sponner, Anh Tong, Dominik Tuscher, Marc Tuscher, Pavan Upputuri
* **Author Priority**: Standard
* **一句话结论**: 这是今天最值得优先通读的工业向论文之一，因为它把 VLA 从反应式控制明确推进到可部署的 plan-and-act 框架。
* **问题与切口**: Cortex 2.0 针对工业操作中的长时程脆弱性开刀。作者的判断很明确：现有 VLA 即便泛化不错，本质上仍是基于当前观测做下一步动作的反应式系统，一旦早期动作失误，长链条任务就容易连锁失败。它的新意在于把 world model 直接接到部署链路中，在视觉潜空间里生成多个未来候选轨迹，再用一个同时考虑任务进展、风险和完成可能性的评分模块做筛选，让策略先“看未来”再执行，而不是只在当前帧上贪心决策。
* **核心方法与证据**: 从 HTML 可确认的主方法是：world model 通过 flow matching 学习视觉潜空间动力学；推理时从不同噪声初始化生成候选未来潜变量序列，PRO 对每条候选按任务推进、风险概率和完成概率进行稠密评分，再选择最高分轨迹执行。正文还给出了一个重要工程取舍：作者认为 PRO 更依赖运动与物理合理性，而非高保真重建，因此粗粒度潜变量也足以做有效筛选。实验在单臂与双臂平台上进行，使用腕部相机、30Hz 控制，并以等价 200 GPU 小时预算比较多类基线；结论部分声称四个基准上都取得更高成功率和更短执行时间，且是唯一无需人工介入完成任务的方法。
* **正文要点**:
  - 论文把问题定义为“长时程工业操作中的复合失败”，并明确批评纯反应式 VLA 缺乏未来结果评估。
  - 核心机制是潜空间候选未来生成加 PRO 稠密评分，其中评分维度包含进展、风险和完成可能性。
  - 实验覆盖单臂与双臂平台，比较时强调等算力预算，这使部署层面的结论更有参考价值。
* **为什么值得跟**:
  - 它展示了 world model 在 VLA 中的一个务实角色：不是做漂亮预测，而是做测试时轨迹筛选器。
  - 对工业场景而言，缩短执行时间并减少人工介入，往往比单次子任务成功更有系统价值。
  - 这条路线为“生成多个未来再选最优”提供了可部署范式，可能成为长时程机器人控制的重要模板。
* **风险 / 保留意见**:
  - PRO 的评分质量可能成为系统上限；如果奖励代理与真实成功不一致，规划会被系统性带偏。
  - 当前证据集中在特定工业平台和任务集合上，跨工位、跨夹具和更强分布漂移下的泛化边界仍待确认。
* **建议先看**: 先看 method 里 world model 与 PRO 的接口，理解候选未来是怎样被生成和筛掉的；再看实验是否真正证明它比强反应式基线更适合长时程闭环执行。
* **关键词**: `VLA` `World Model` `工业部署` `规划执行` `潜空间预测`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - PRO 的训练信号来自人工设计、离线标注，还是可从执行结果自动回推？
  - 候选轨迹数量、ODE 步数和执行延迟之间的折中在真实部署里有多敏感？
  - 性能提升主要来自未来评估本身，还是来自更强的预训练视频先验？
* **上传 PDF 后优先看**:
  - world model 与 PRO 的方法章节
  - 部署设置与基线公平性说明
  - 长时程任务成功率、耗时和人工干预相关结果

### [3]. Mask World Model: Predicting What Matters for Robust Robot Policy Learning [[HTML]](https://arxiv.org/html/2604.19683) [[PDF]](https://arxiv.org/pdf/2604.19683) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.19683`
* **Authors**: Yunfan Lou, Xiaowei Chi, Xiaojie Zhang, Zezhong Qian, Chengxuan Li, Rongyu Zhang, Yaoxu Lyu, Guoyu Song, Chuyao Fu, Haoxuan Xu, Pengwei Wang, Shanghang Zhang
* **Author Priority**: Standard
* **一句话结论**: 如果你只想先挑一篇真正体现“控制导向 world model”思路的论文，这篇应列入最高优先级。
* **问题与切口**: Mask World Model 的切口非常锋利：它认为机器人 world model 若以高保真 RGB 预测为目标，模型容量会被光照、背景、纹理和反射等与动作决策弱相关的因素消耗，最终让策略学到脆弱的控制表示。为此，作者把预测对象从像素改成语义掩码，让 world model 学的是物体与接触关系的演化，而不是画面细节本身。这个“几何信息瓶颈”路线，本质上是在把视频生成的能力改造成更贴近控制的动态抽象。
* **核心方法与证据**: 从 HTML 可确认的结构是：作者用视频扩散架构预测未来语义掩码，再把这个 mask dynamics backbone 与 diffusion policy head 结合做闭环控制。一个很关键的工程点是，语义监督只在线下训练时使用，测试时系统仍只吃原始多视角 RGB，因此作者试图避免部署时额外依赖分割输入。实验覆盖 LIBERO 与 RLBench 两个语言条件操作基准，RLBench 部分在六个任务上各跑 20 次随机化评测；对比对象包括 RGB 中心的一般ist policy 与 world-model 管线。摘要与结论声称其在模拟和真实机器人上都表现更强，但从当前摘录无法读取更细的失效模式。
* **正文要点**:
  - 论文明确把 RGB 预测与控制目标之间的错配定义为核心问题，目标是过滤光照和动态背景等干扰因素。
  - 方法上预测的是未来语义掩码而非像素，并将该预测骨干与扩散策略头直接耦合。
  - 训练时使用语义监督，测试时只依赖原始 RGB，这一点对真实部署可行性很关键。
* **为什么值得跟**:
  - 它为机器人 world model 提供了一个更贴近控制的表征方向，而不是继续追逐视频重建质量。
  - 如果语义瓶颈确实更稳健，这对 sim2real 和多环境泛化会比单纯提升像素保真更有价值。
  - 它说明“减少模型看到的信息”有时比“让模型看到更多细节”更适合机器人决策。
* **风险 / 保留意见**:
  - 训练阶段如何获得稳定且足够准确的语义掩码，可能会决定方法能否扩展到更多真实场景。
  - 当前摘录没有展开失败案例，尚不清楚在遮挡重、语义边界模糊时是否会出现新的误判。
* **建议先看**: 先抓住作者提出的核心论点：控制需要的是几何与交互动态，而不是像素保真；再重点检查语义监督来源和测试时只用 RGB 的实现是否真的闭环成立。
* **关键词**: `World Model` `语义掩码` `控制表征` `扩散策略` `鲁棒操作`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 训练用的语义掩码来自人工标注、自动分割，还是仿真真值，不同来源会不会显著影响结论？
  - 性能收益到底来自“掩码瓶颈”本身，还是来自额外监督带来的表征增强？
  - 当任务成功依赖细粒度材质或接触纹理时，mask 表示会不会丢掉必要信息？
* **上传 PDF 后优先看**:
  - 语义掩码构建与监督来源说明
  - world model 与 policy head 的耦合方式
  - LIBERO、RLBench 及真实机器人泛化结果

### [4]. PokeVLA: Empowering Pocket-Sized Vision-Language-Action Model with Comprehensive World Knowledge Guidance [[HTML]](https://arxiv.org/html/2604.20834) [[PDF]](https://arxiv.org/pdf/2604.20834) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.20834`
* **Authors**: Yupeng Zheng, Xiang Li, Songen Gu, Yuhang Zheng, Shuai Tian, Weize Li, Linbo Wang, Senyu Fei, Pengfei Li, Yinfeng Gao, Zebin Xing, Yilun Chen, Qichao Zhang, Haoran Li, Wenchao Ding
* **Author Priority**: Standard
* **一句话结论**: 这篇值得优先看，因为它提供了一个不靠大模型堆规模、而靠知识注入与空间对齐做强 VLA 的小模型路线。
* **问题与切口**: PokeVLA 想解决的不是“VLA 能不能做任务”，而是“在模型很小的情况下，怎样让它同时具备高层知识、空间感知和可操作的动作表示”。作者认为现有做法往往直接把通用 VLM 的隐状态拿去喂动作学习，缺少对操作相关表征的精细化塑形，因此在学习效率、空间一致性和任务指导上都有缺口。它提出两阶段方案：先用 240 万样本的多模态数据把一个紧凑型 PokeVLM 预训练成更懂空间指向、affordance 和 embodied reasoning 的模型，再把这些与操作强相关的表征通过目标感知语义、多视角几何对齐和 action expert 注入动作学习。
* **核心方法与证据**: 从 HTML 可确认的证据包括：第一阶段的数据覆盖空间定位、可供性和具身推理任务；第二阶段强调多视角 goal-aware semantics learning、geometry alignment 和一个新的 action expert。实验主要放在 LIBERO 与更强调扰动鲁棒性的 LIBERO-Plus 上，后者显式包含视角、机器人初始位姿、语言指令、光照、背景纹理、传感器噪声和物体布局等七类变化。正文还给出了评测协议差异，例如 LIBERO 中每个测试样本重复执行多次，而 LIBERO-Plus 更接近一次性鲁棒评估。不过从当前摘录仍无法确认 action expert 的具体结构及其计算代价。
* **正文要点**:
  - 核心训练范式是“两阶段”：先做紧凑 VLM 预训练，再把操作相关表征系统性注入动作端。
  - PokeVLM 的预训练数据被明确设计为覆盖空间 grounding、affordance 和 embodied reasoning，而非一般视觉语言任务。
  - LIBERO-Plus 的七类扰动设置使这篇论文的重点更偏向鲁棒泛化，而不只是静态基准分数。
* **为什么值得跟**:
  - 它为小模型 VLA 提供了一个可行命题：能力增强不一定只靠更大参数量，也可以靠更好的知识组织。
  - 如果空间对齐和目标感知语义注入有效，VLA 的数据效率和扰动鲁棒性都可能受益。
  - 这条路线对资源受限部署很重要，因为很多机器人场景根本容不下大体量模型。
* **风险 / 保留意见**:
  - 模型增益可能高度依赖那套 240 万样本的人工策划数据分布，跨域迁移能力仍需谨慎评估。
  - 当前摘录没有提供真实机器人部署证据，也看不出轻量化是否真的转化为端到端时延优势。
* **建议先看**: 先看两阶段方案里表征学习和动作学习的分工是否清晰，再重点检查 LIBERO-Plus 上对七类扰动的鲁棒性证据是否支持“小模型也能稳”的主张。
* **关键词**: `VLA` `轻量模型` `空间 grounding` `affordance` `鲁棒泛化`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - PokeVLM 相比通用 VLM 到底新增了哪些对操作最关键的监督与数据筛选规则？
  - geometry alignment 在多视角条件下是如何约束到动作空间的？
  - 所谓 tiny-scale 的优势主要体现为训练效率、推理时延，还是更好的泛化效率？
* **上传 PDF 后优先看**:
  - 两阶段训练与 240 万样本数据组织
  - 语义注入、几何对齐与 action expert 设计
  - LIBERO-Plus 扰动鲁棒性与消融实验

### [5]. Temporal Difference Calibration in Sequential Tasks: Application to Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2604.20472) [[PDF]](https://arxiv.org/pdf/2604.20472) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.20472`
* **Authors**: Shelly Francis-Meretzki, Mirco Mutti, Yaniv Romano, Aviv Tamar
* **Author Priority**: Standard
* **一句话结论**: 如果你的关注点是 VLA 的可靠性而不是单纯成功率，这篇应当高优先级阅读。
* **问题与切口**: 这篇论文处理的是一个很少被严肃定义的问题：在序列决策里，任务成败往往只有回合结束时才能知道，但系统却需要在执行途中持续给出“我会不会成功”的可信置信度。作者把这个问题形式化为 episodic sequential calibration，提出顺序版 Brier score，并指出在二元结果设置下，它的风险最优解正好对应策略的价值函数。这个切口很重要，因为它把“VLA 置信度是否可信”从经验校准问题，转成了可以和 RL 价值估计正面打通的学习问题。
* **核心方法与证据**: 从 HTML 可确认的主线是：顺序校准通过未来奖励预测来实现，而 Theorem 5.1 给出了关键连接，即最小化 Sequential Brier Score 等价于学习值函数。基于这个联系，作者提出 TDQC，把时序差分式价值估计引入成功概率校准。实验明确围绕三个问题展开：TD 损失是否改善校准与失败检测，黑盒校准是否有竞争力，以及校准后的成功预测器能否在测试时指导动作搜索。评测覆盖四类 VLA 策略，且作者特别强调其方法只需要动作概率，因此理论上适用于只能经 API 访问的黑盒模型。摘录未给出更细粒度的泛化边界。
* **正文要点**:
  - 论文提出顺序版 Brier score，用部分轨迹上的置信度去对应最终任务成功。
  - Theorem 5.1 把“校准成功预测器”与“学习值函数”直接连在一起，这是全文最重要的理论支点。
  - 方法只依赖动作概率这一点，使其具备服务黑盒或专有模型的现实吸引力。
* **为什么值得跟**:
  - VLA 在真实世界里不仅要会做，还要知道自己什么时候大概率会做错。
  - 把校准问题并入 RL 价值估计工具箱，是一个概念上很干净、也很可能可扩展的统一视角。
  - 如果测试时动作搜索能被校准后的成功预测器有效引导，可靠性就不再只是评测指标，而会反过来提升控制。
* **风险 / 保留意见**:
  - 方法对动作概率可得性的依赖，可能让某些连续控制或封闭系统难以直接接入。
  - 当前摘录没有展开分布外任务、奖励设计偏差和长时程信用分配对校准稳定性的影响。
* **建议先看**: 先读问题定义和 Theorem 5.1，确认作者为什么能把校准问题改写成值函数学习；然后再看 TDQC 在失败检测和测试时搜索中的作用是否真的超出传统后处理校准。
* **关键词**: `VLA` `校准` `值函数` `时序差分` `可靠性`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 顺序成功标签依赖的奖励阈值设定对校准结果有多敏感？
  - 与常见黑盒后处理校准方法相比，TDQC 的优势主要来自时序结构还是来自更多训练信号？
  - 校准改善在多大程度上真正转化为更高任务成功率，而不是只提升置信度排序？
* **上传 PDF 后优先看**:
  - 顺序校准问题定义与指标设计
  - Theorem 5.1 与 TDQC 方法章节
  - 失败检测与测试时引导动作搜索实验

### [6]. Toward Safe Autonomous Robotic Endovascular Interventions using World Models [[HTML]](https://arxiv.org/html/2604.20151) [[PDF]](https://arxiv.org/pdf/2604.20151) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.20151`
* **Authors**: Harry Robertshaw, Nikola Fischer, Han-Ru Wu, Andrea Walker Perez, Weiyuan Deng, Benjamin Jackson, Christos Bergeles, Alejandro Granados, Thomas C Booth
* **Author Priority**: Standard
* **一句话结论**: 这篇值得入选，因为它把 world-model RL 放进了高风险医疗操作场景，研究价值高于当前可见实验篇幅本身。
* **问题与切口**: 论文关注机械取栓中的血管内导航自动化，这是一类典型长时程、高安全约束、强个体差异的机器人问题。作者没有继续沿用纯 model-free 强化学习，而是把 TD-MPC2 这种结合规划与学习动力学的方法引入 endovascular navigation，希望在多种血管几何和更长导航链路下提升鲁棒性。相对一般操作任务，这篇最重要的新意不是 world model 本身，而是把它放进一个临床可解释性和安全性都更敏感的应用域，并明确把 sim-to-real 与风险监测一并纳入评估。
* **核心方法与证据**: 从 HTML 可确认的实验设计较有信息量：作者实现了导丝尖端碰撞监测器，记录接触力，并统计最大值和均值；同时记录尖端速度，用来辅助分析训练流程与安全性。评测指标除成功率与程序时间外，还包含在失败情形下反映接近目标程度的 path ratio，以及达到某结果所需的 exploration steps。论文还做了数据增强的 ablation，专门考察从 in silico 到 in vitro 的迁移效果。结论声称这是首次在五个留出真实患者血管几何的仿真环境和一个体外平台上，针对多导航任务、工业标准器械和透视追踪进行此类 RL 评估；但从摘录看，临床级闭环安全性仍显然只是早期探索。
* **正文要点**:
  - 方法核心是把 TD-MPC2 作为 world-model RL 框架，用于多任务血管内导航而非一般桌面操作。
  - 实验不仅看成功率，也显式监测导丝尖端接触力和速度，体现出安全导向评估。
  - 作者把 sim-to-real 迁移作为正文问题处理，并用数据增强消融去分析体内外落差。
* **为什么值得跟**:
  - 它说明 world model 的价值不只在工业装配，也可能进入医疗机器人这类高风险长时程场景。
  - 引入力与速度等安全相关量，让 RL 评测开始接近临床可用性的讨论方式。
  - 多患者血管几何的设置抓住了这类任务最核心的泛化来源：解剖结构差异。
* **风险 / 保留意见**:
  - 从仿真和体外测试到真实临床部署之间仍有巨大鸿沟，当前证据远不足以支持自主介入落地。
  - 摘录没有给出更完整的对比基线与失败模式分析，尚难判断 world model 相比其他 RL 路线的优势有多稳。
* **建议先看**: 先看训练与数据增强管线，判断作者如何应对患者几何差异；再重点读安全相关指标和 in silico 到 in vitro 的迁移结果，而不要只盯成功率。
* **关键词**: `World Model` `TD-MPC2` `医疗机器人` `机械取栓` `Sim2Real`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 学习到的动力学模型如何处理不同患者血管几何带来的显著分布变化？
  - 哪类数据增强对 in silico 到 in vitro 迁移最关键，是否会牺牲控制精度？
  - 接触力监测是仅用于离线评估，还是在规划与动作选择中也发挥了约束作用？
* **上传 PDF 后优先看**:
  - TD-MPC2 训练流程与数据增强设计
  - 安全指标采集与碰撞监测设置
  - 留出患者血管几何评测与体外迁移实验

## Watchlist

### [W1]. OmniUMI: Towards Physically Grounded Robot Learning via Human-Aligned Multimodal Interaction [[HTML]](https://arxiv.org/html/2604.10647) [[PDF]](https://arxiv.org/pdf/2604.10647)
* **Paper ID**: `2604.10647`
* **Authors**: Shaqi Luo, Yuanyuan Li, Youhao Hu, Chenhao Yu, Chaoran Xu, Jiachen Zhang, Guocai Yao, Tiejun Huang, Ran He, Zhongyuan Wang
* **Author Priority**: Standard
* **为什么还值得留意**: OmniUMI 进入 shortlist，主要因为它把 UMI 风格机器人学习从纯 visuomotor 采集推进到触觉、抓取内力和外部 wrench 的统一交互采集，这对接触丰富操作和未来 physically grounded VLA 都很关键。它没进最终精选，是因为当前重心更偏向数据采集接口与人类对齐交互流程，而不是今天主线里的 VLA/world model/plan-and-act 本体。换言之，它更像上游数据基础设施论文，重要但不在今天最核心的一层。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. ETac: A Lightweight and Efficient Tactile Simulation Framework for Learning Dexterous Manipulation [[HTML]](https://arxiv.org/html/2604.20295) [[PDF]](https://arxiv.org/pdf/2604.20295)
* **Paper ID**: `2604.20295`
* **Authors**: Zhe Xu, Feiyu Zhao, Xiyan Huang, Chenxi Xiao
* **Author Priority**: Standard
* **为什么还值得留意**: ETac 进入 watchlist 的理由很充分：它同时强调触觉仿真的保真度与并行 RL 训练效率，且摘录里给出了较强的吞吐和形变误差证据，对 dexterous manipulation 很有现实吸引力。之所以没有进入最终精选，是因为它更像 tactile simulation backend，而不是面向 VLA、world model 或跨具身规划的主线工作。对于今天的主题，它更偏支撑层而非中心叙事。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)

### [W3]. Visual-Tactile Peg-in-Hole Assembly Learning from Peg-out-of-Hole Disassembly [[HTML]](https://arxiv.org/html/2604.20712) [[PDF]](https://arxiv.org/pdf/2604.20712)
* **Paper ID**: `2604.20712`
* **Authors**: Yongqiang Zhao, Xuyang Zhang, Zhuo Chen, Matteo Leonetti, Emmanouil Spyrakos-Papastavridis, Shan Luo
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇用 peg-out-of-hole 反向任务去帮助 peg-in-hole 学习，思路相当聪明，而且视觉-触觉结合、POMDP 建模和 sim-to-real 都使它具备研究含金量。没有进入最终精选，主要是因为它的问题设置仍然比较窄，核心贡献更偏装配技能学习，而非通用 VLA、world model 或大范围泛化框架。它适合持续关注，但优先级略低于那些在方法范式上更具外溢性的论文。
* **证据来源**: arXiv HTML (Introduction, Experiments)

### [W4]. Rodrigues Network for Learning Robot Actions [[VIP]] [[HTML]](https://arxiv.org/html/2506.02618) [[PDF]](https://arxiv.org/pdf/2506.02618)
* **Paper ID**: `2506.02618`
* **Authors**: Jialiang Zhang, Haoran Geng, Yang You, Congyue Deng, Pieter Abbeel, Jitendra Malik, Leonidas Guibas
* **Author Priority**: Core VIP
* **为什么还值得留意**: RodriNet 进入 shortlist，一方面因为它确实抓住了动作学习里常被忽略的关节运动学归纳偏置，另一方面因为作者名单里有核心 VIP 作者 Pieter Abbeel，值得持续跟踪。它没有进入最终精选，是因为当前摘录显示它更偏通用动作表示与架构层创新，离今天的重点方向 VLA、world model、sim2real 闭环部署还有一层距离。若后续你要扩展“动作表征如何反哺 VLA”这条线，它会是非常值得补读的旁支。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)
