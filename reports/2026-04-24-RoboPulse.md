# RoboPulse | 2026-04-24

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 56 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线很清楚：VLA 正从“直接生成动作”转向“带显式中间结构的闭环系统”，其中任务管理、世界模型后训练、过程级评测，以及 foundation priors 驱动的自主学习开始汇合。最终精选之所以成立，是因为这 6 篇分别覆盖了长程操作管理、world model 作为纠错基础设施、open-world 评测重构、视频模型转世界交互模型、跨 embodiment 预训练，以及 RL 与基础模型结合这几条最关键的推进线。落在 VIP 名单里且今天最值得优先跟踪的是 Xiaolong Wang、Pieter Abbeel 和 Jiangmiao Pang，其中前两位已进入最终精选，后者在 watchlist 里提供了更底层但很重要的 action-space 设计视角。若后续你上传 PDF，我建议先核查这些工作在真实机器人、长程失败恢复和跨场景泛化上的证据强度。

## 今日信号

- 今天最值得记住的研究信号是：VLA 的竞争焦点正在从单体 backbone 转向显式中间表示与层级闭环，任务进度、空间锚点、视觉轨迹和意图先验都被重新拉回控制回路。
- 今天最值得记住的研究信号是：world model 的角色正在从“离线想象器”升级为“交互式后训练平台”，其关键价值不只是合成数据，而是支持回滚、分叉和失败态复用的人类纠错。
- 今天最值得记住的研究信号是：open-world 机器人评测开始从终态成功率转向过程可靠性与安全性，这会直接改变长程 household VLA 的研究排序。

## Editor's Picks

### [1]. Long-Horizon Manipulation via Trace-Conditioned VLA Planning [[VIP]] [[HTML]](https://arxiv.org/html/2604.21924) [[PDF]](https://arxiv.org/pdf/2604.21924) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.21924`
* **Authors**: Isabella Liu, An-Chieh Cheng, Rui Yan, Geng Chen, Ri-Zhao Qiu, Xueyan Zou, Sha Yi, Hongxu Yin, Xiaolong Wang, Sifei Liu
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，它把长程操作里最难的“进度管理”从执行器里拆出来，用显式剩余计划和视觉轨迹把短程 VLA 拼成可回溯的长程系统。
* **问题与切口**: 这篇工作瞄准长程操作中最现实的断点：任务往往是多步、依赖进度、且会因局部失误连续崩塌。LoHo-Manip 的新意不在于再训练一个更大的端到端 VLA，而是把“任务管理”单独交给一个高层 VLM，并让它在每个阶段根据当前观测重写剩余计划。它输出的不只是子任务序列，还包含 done/remaining 的语言式进度记忆，以及一个紧凑的视觉轨迹，用来把长时程问题压缩成一连串可执行、可纠偏的短时程片段。
* **核心方法与证据**: 正文摘录给出的主线很完整：系统被明确拆成 task manager 与 low-level executor 两层，前者依据指令和当前观测预测 remaining task structure，后者只负责局部短程控制。作者强调采用 receding-horizon 调用方式，以显式 progress signal 缓解长时程 credit assignment 和 rollout distribution shift。证据链覆盖四层：先验证推理与轨迹预测能力，再测 embodied benchmark 上的子任务规划，再到仿真闭环操控，最后是非受限真实环境实验。由于摘录没有给出数值结果，当前更适合把它判断为“结构上很对、强度待 PDF 核查”的优先稿。
* **正文要点**:
  - 管理器只预测“剩余计划”，而不是直接输出整段长动作序列。
  - 显式 done/remaining 划分被当作轻量语言记忆，用来跟踪任务进度。
  - 实验设计从推理与规划逐步推进到仿真闭环和真实环境长程执行。
* **为什么值得跟**:
  - 它正面回答了长程 VLA 为什么常在中途失控，而不是只在终端动作头上继续堆容量。
  - 分层拆分让失败恢复和重规划天然可插入，更接近真实家居任务的执行逻辑。
  - Xiaolong Wang 这条线值得跟，因为它把 long-horizon VLA 从“会做动作”推进到“会管任务”。
* **风险 / 保留意见**:
  - 管理器输出质量若不稳定，错误会以“高层计划偏差”形式持续传给执行器。
  - 摘录未给出真实机器人成功率、失败模式分解或与强基线的定量差距，证据强度仍需 PDF 核查。
* **建议先看**: 先看系统总览和 manager 输出接口，判断 done/remaining 记忆与 visual trace 是否真在承担进度管理。然后直接看闭环仿真与真实机器人部分，确认收益究竟来自高层重规划还是底层执行器本身。
* **关键词**: `长程操作` `分层VLA` `任务管理` `视觉轨迹` `进度感知规划`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)
* **读 PDF 先核查**:
  - visual trace 的具体表示、监督来源和更新频率是什么，它与语言式剩余计划各自承担什么功能？
  - receding-horizon 重规划是在固定步频触发，还是由失败/不确定性触发；不同触发机制会怎样影响稳定性？
  - 端到端收益主要来自 manager 的子任务分解能力，还是来自它对执行失败后的重写与恢复能力？
* **上传 PDF 后优先看**:
  - 系统总览与 manager/executor 接口定义
  - 子任务规划与轨迹预测评测
  - 仿真闭环和真实机器人失败案例分析

### [2]. Hi-WM: Human-in-the-World-Model for Scalable Robot Post-Training [[HTML]](https://arxiv.org/html/2604.21741) [[PDF]](https://arxiv.org/pdf/2604.21741) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.21741`
* **Authors**: Yaxuan Li, Zhongyi Zhou, Yefei Chen, Yanjiang Guo, Jiaming Liu, Shanghang Zhang, Jianyu Chen, Yichen Zhu
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把昂贵的真实机器人纠错环路迁到可回滚、可分叉的世界模型里，直击后训练扩展性的核心瓶颈。
* **问题与切口**: Hi-WM 关注的不是从零学一个机器人策略，而是如何把已经预训练好的 generalist policy 真正打磨成可部署的 task-specific controller。它的核心切口很实用：现有 human-in-the-loop post-training 之所以难扩展，不是因为没有人类监督，而是每次纠错都要占用真实机器人、真实场景和人工复位。作者因此把纠错操作移入一个 learned world model，让人类在模型里直接接管失败状态，围绕难点行为进行低成本、可复用的 targeted correction。
* **核心方法与证据**: 摘录显示，Hi-WM 的流程是先让当前策略在 action-conditioned world model 中闭环 rollout；一旦轨迹错误或接近失败，人类就在模型内部给出短时 corrective actions。其关键工程点不是单次演示，而是缓存中间状态，并支持 rollback 与 branching，从而把一个失败态复用成多条修正分支，形成围绕薄弱行为的密集监督。实验部分围绕四个研究问题组织：世界模型与真实执行的对齐性、作为 policy-agnostic post-training 框架的有效性、随场景覆盖扩展的成本优势，以及对新场景真实泛化的帮助。摘录明确写到真实机器人实验，但未提供量化幅度。
* **正文要点**:
  - 人类干预发生在世界模型内部，而不是物理机器人执行现场。
  - 系统支持状态缓存、回滚和分叉，能围绕单个失败态生成多条修正轨迹。
  - 实验问题设置明确覆盖对齐性、有效性、扩展性与真实泛化四个维度。
* **为什么值得跟**:
  - 它把 world model 从“做想象”推进到“做后训练基础设施”，用途明显更接近真实研发流程。
  - 失败态复用机制如果成立，会显著改变机器人 post-training 的边际成本结构。
  - 这条线兼容已有策略而非替换全部堆栈，更容易被工业或实验室现有流程采纳。
* **风险 / 保留意见**:
  - 若世界模型对接触、形变或长时程误差的拟合不足，虚拟纠错可能会向真实部署传递系统性偏差。
  - 摘录虽说明有真实机器人验证，但没有给出具体任务提升幅度、失效案例或人工成本统计。
* **建议先看**: 先看方法部分关于 rollback、branching 和 corrective trajectory 生成的具体接口，这决定它是否真能规模化。再看实验中的 RQ1 与 RQ3，优先判断世界模型对齐性和成本扩展性是否足够支撑这套叙事。
* **关键词**: `world model` `后训练` `human-in-the-loop` `失败态复用` `机器人纠错`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 人类在世界模型里施加的 corrective actions 是直接动作级编辑，还是更高层的轨迹/子目标修正？
  - 世界模型闭环 rollout 的失真会如何影响纠错数据分布，作者是否设计了筛选或校准机制？
  - policy-agnostic 的说法具体覆盖哪些基座策略，收益是否依赖特定策略架构或任务类型？
* **上传 PDF 后优先看**:
  - Hi-WM 交互流程与状态缓存机制
  - 真实机器人对齐性与成本扩展实验
  - 新场景泛化与失败案例分析

### [3]. How VLAs (Really) Work In Open-World Environments [[HTML]](https://arxiv.org/html/2604.21192) [[PDF]](https://arxiv.org/pdf/2604.21192) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.21192`
* **Authors**: Amir Rasouli, Yangzheng Wu, Zhiyuan Li, Rui Heng Yang, Xuan Zhao, Charles Eret, Sajjad Pakdamansavoji
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它不是再造一个 VLA，而是指出现有 open-world 评测把“做成了”错当成“做对了且做安全了”。
* **问题与切口**: 这篇工作的价值在于把视角从“模型会不会完成任务”转向“模型是如何完成任务、过程中是否可靠”。作者质疑当前长程 household benchmark 常用的 success rate 或 partial score 过度依赖终态物体状态，忽略了执行过程中是否出现危险行为、无效试探或与指令不一致的操作。相较于继续堆更大模型，它更像是在给 open-world VLA 研究补一块被长期忽视的评测地基：如果评测仍然 progress-agnostic，那么很多真实部署中最关键的风险就不会被看见。
* **核心方法与证据**: 从摘录可见，论文选择了 BEHAVIOR-1K challenge 的设置，并对其中两套获胜策略进行分析，目标不是构造一个新 benchmark，而是在现有 open-world household 环境上重新审视 SOTA VLA 的能力边界。引言强调机器人评测缺少类似自动驾驶中过程安全导向的度量，结论则指出现有策略虽然能完成不少复杂子任务，但整体成功率仍低，在真实而复杂的 open-world 条件下离可靠部署还有明显距离。摘录没有展开其全部评测指标，因此“过程级安全分析”这一点应视为由引言与结论支持的保守判断。
* **正文要点**:
  - 论文直接质疑仅看终态的 progress-agnostic 评测协议。
  - 实验采用 B1K challenge 的 50 个代表任务设置，并分析两套顶尖策略。
  - 结论强调当前 VLA 具备部分复杂子任务能力，但整体可靠性仍不足。
* **为什么值得跟**:
  - 它提醒研究社区，错误的评测目标会系统性高估 open-world VLA 的实际可用性。
  - 对长程家务任务来说，过程中的混乱、危险和无效动作往往比最终是否侥幸完成更关键。
  - 这类工作能直接影响后续 benchmark、reward 设计与安全评测标准的走向。
* **风险 / 保留意见**:
  - 摘录没有给出完整指标体系和标注流程，评测是否可大规模复现还需要 PDF 验证。
  - 结论建立在特定 benchmark 与两套策略之上，外推到更广泛 VLA 家族时需要谨慎。
* **建议先看**: 先看评测协议与指标定义，确认作者到底把哪些“过程问题”系统化了。然后看两套顶尖策略的失败归因，判断问题主要来自长程规划、感知歧义，还是执行过程中的安全缺口。
* **关键词**: `open-world VLA` `评测协议` `过程安全` `BEHAVIOR-1K` `长程家务任务`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 作者新增或强调的过程级指标具体如何定义，它们与传统 success rate 的相关性如何？
  - 两套获胜策略的主要失败模式是否一致，还是分别暴露出不同类型的长程缺陷？
  - 在 B1K 这类开放环境里，哪些任务类别最容易被 progress-agnostic 终态评分误判为“可部署”？
* **上传 PDF 后优先看**:
  - 评测协议与指标定义部分
  - B1K challenge 设置与策略比较实验
  - 失败归因与部署风险讨论

### [4]. Learning Physics from Pretrained Video Models: A Multimodal Continuous and Sequential World Interaction Models for Robotic Manipulation [[HTML]](https://arxiv.org/html/2603.00110) [[PDF]](https://arxiv.org/pdf/2603.00110) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.00110`
* **Authors**: Zijian Song, Qichang Li, Sihan Qin, Yuhao Chen, Tianshui Chen, Liang Lin, Guangrun Wang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，但要带着验证意识读：它试图把预训练视频生成器直接改造成可交互世界模型，这是高杠杆方向，证据细节仍需 PDF 核查。
* **问题与切口**: PhysGen 的核心企图非常大胆：既然机器人数据稀缺，就不要只把预训练基础模型当作感知编码器，而是把视频生成模型直接当成 physics simulator 的替代近似，用来建模机器人动作与外部环境之间的连续交互。它提出一个 multimodal continuous and sequential world interaction framework，把视频与动作统一到共享的 physical token 表示中，希望把视频模型里已有的动态规律迁移到操控场景。相较于主要从语言或 demonstration 侧迁移的路线，这更像是在借视频生成模型补机器人对物理演化的先验。
* **核心方法与证据**: 摘录中能确定的方法线索主要集中在建模层。作者以 NOVA 这类连续、非量化空间中的自回归视频生成模型为基础，把时间维上的 autoregressive 生成、帧内 token set 的空间自回归，以及连续 token 概率估计的 diffusion loss 结合起来。论文强调它是一个 continuous 与 sequential 的 world interaction model，而不是单纯 future frame prediction。问题在于，当前提供的摘要与 HTML 片段没有展开实验章节内容、任务范围或关键对比，因此我们能较有把握地判断其建模方向很前沿，但暂时不能对闭环操控效果做强结论。
* **正文要点**:
  - 作者把预训练视频生成模型视为 physics simulator 的代理近似。
  - 视频与动作被统一进共享的连续 physical token 表示。
  - 方法依托连续空间中的时序自回归、空间自回归和 diffusion-style 训练信号。
* **为什么值得跟**:
  - 如果这条路线成立，机器人世界模型就不必完全依赖昂贵的专用机器人交互数据起步。
  - 它把“视频会生成动态”进一步推进到“视频能否支持可操作的物理交互建模”这一更高价值问题。
  - 对 world model 和 world action model 方向而言，这是从感知迁移走向动力学迁移的重要尝试。
* **风险 / 保留意见**:
  - 当前摘录缺少实验细节，无法判断它是否真的支撑闭环操控而非只擅长预测外观变化。
  - 连续 token 与动作统一后的训练稳定性、长时程误差累积和真实物理一致性都存在复现风险。
* **建议先看**: 先抓住它如何把视频 token 与动作 token 放进同一个连续交互建模框架，这是理解全文的主轴。上传 PDF 后优先核查实验部分，确认它到底是在预测上好看，还是在控制上真的有用。
* **关键词**: `视频生成模型` `世界模型` `物理先验` `连续表示` `机器人操控`
* **证据来源**: arXiv HTML (Introduction, Method)
* **读 PDF 先核查**:
  - shared physical token 的构造是否真正保留了动作可控性，而不是只让视频预测更顺滑？
  - 该框架在闭环控制中如何使用生成结果，是直接规划、模型预测控制，还是用于训练策略？
  - 与传统 simulator-based world model 相比，作者如何界定“学到 physics”而不只是学到视觉时序相关性？
* **上传 PDF 后优先看**:
  - 表示学习与 token 统一方式
  - 基于 NOVA 的时空自回归建模细节
  - 闭环操控评测与 world-model 基线比较

### [5]. JoyAI-RA 0.1: A Foundation Model for Robotic Autonomy [[PDF]](https://arxiv.org/pdf/2604.20100) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.20100`
* **Authors**: Tianle Zhang, Zhihao Yuan, Dafeng Chi, Peidong Liu, Dongwei Li, Kejun Hu, Likui Zhang, Junnan Nie, Ziming Wei, Zengjue Chen, Yili Tang, Jiayi Li, Zhiyuan Xiang, Mingyang Li, Tianci Luo, Hanwen Wan, Ao Li, Linbo Zhai, Zhihao Zhan, Xiaodong Bai, Jiakun Cai, Peng Cao, Kangliang Chen, Siang Chen, Yixiang Dai, Shuai Di, Yicheng Gong, Chenguang Gui, Yucheng Guo, Peng Hao, Qingrong He, Haoyang Huang, Kunrui Huang, Zhixuan Huang, Shibo Jin, Yixiang Jin, Anson Li, Dongjiang Li, Jiawei Li, Ruodai Li, Yihang Li, Yuzhen Li, Jiaming Liang, Fangsheng Liu, Jing Long, Mingxi Luo, Xing Pan, Hui Shen, Xiaomeng Tian, Daming Wang, Song Wang, Junwu Xiong, Hang Xu, Wanting Xu, Zhengcheng Yu, He Zhang, Jiyao Zhang, Lin Zhao, Chen Zhou, Nan Duan, Yuzheng Zhuang, Liang Lin
* **Author Priority**: Standard
* **一句话结论**: 值得纳入最终精选，但当前只能做方向性优先跟踪；是否真正站得住，取决于 PDF 里跨 embodiment 证据和真实机器人结果是否扎实。
* **问题与切口**: 从摘要看，JoyAI-RA 试图回答两个基础而顽固的问题：开放世界机器人数据覆盖不足，以及不同 embodiment 之间行为知识难以迁移。它提出的是一个面向 generalizable robotic manipulation 的 VLA foundation model，并采用 multi-source、multi-level 的预训练框架，把 web data、第一视角人类操作视频、仿真轨迹与真实机器人数据放进同一套训练体系。相对已有路线，它最值得关注的点是明确强调 action-space unification，希望把人类操作知识更直接地桥接到机器人控制上。
* **核心方法与证据**: 这篇目前只有摘要回退信息，因此所有判断都必须保守。摘要明确给出的证据仅包括：训练数据源是异构混合的，方法层面有 explicit action-space unification，目标是增强跨 embodiment 泛化，尤其缓解 human manipulation 与 robot control 之间的鸿沟。基于这些信息，可以合理推断它更像一篇“数据与预训练体系”型 foundation model 论文，而不是一个单点模块创新稿。但在没有 HTML 正文和实验摘录的情况下，我们不能判断各数据源的贡献拆分、真实机器人覆盖范围，或其开放世界泛化是否超越同类大模型。
* **正文要点**:
  - 摘要明确提出 multi-source、multi-level 的预训练框架。
  - 它把 web、egocentric human video、simulation 和 real-robot data 放在同一训练体系内。
  - 跨 embodiment 迁移依赖显式 action-space unification。
* **为什么值得跟**:
  - 这条路线正面对准 VLA 扩展到开放世界时最现实的数据瓶颈。
  - 若 human-to-robot 的动作桥接有效，机器人预训练的数据上限会被明显抬高。
  - 大规模 foundation model 叙事若缺少 embodiment 对齐，这类工作提供了更务实的补口。
* **风险 / 保留意见**:
  - 当前只有摘要，缺少正文证据，任何关于效果强度的判断都只能视为趋势推断。
  - 异构多源训练通常伴随对齐噪声、数据配比敏感性和评测选择偏差，复现门槛可能很高。
* **建议先看**: 上传 PDF 后先看数据配方与 action-space unification，这是决定其技术含金量的核心。其次优先检查跨 embodiment 与真实机器人实验，因为摘要中的主要主张几乎都落在这两块。
* **关键词**: `VLA foundation model` `跨 embodiment` `多源预训练` `动作空间统一` `机器人自主性`
* **证据来源**: Abstract fallback
* **读 PDF 先核查**:
  - 作者如何把 egocentric human manipulation video 映射到机器人可执行的动作空间，这一桥接是否需要额外标注或拟合器？
  - 不同数据源在训练中是统一混训、分阶段课程式训练，还是有显式层级设计？
  - 跨 embodiment 泛化是通过哪些平台和任务来验证的，是否区分了形态差异与任务差异的贡献？
* **上传 PDF 后优先看**:
  - 预训练数据混合与课程设计
  - action-space unification 与 embodiment bridge 机制
  - 跨 embodiment 和真实机器人泛化实验

### [6]. Reinforcement Learning with Foundation Priors: Let the Embodied Agent Efficiently Learn on Its Own [[VIP]] [[HTML]](https://arxiv.org/html/2310.02635) [[PDF]](https://arxiv.org/pdf/2310.02635) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2310.02635`
* **Authors**: Weirui Ye, Yunsheng Zhang, Haoyang Weng, Xianfan Gu, Shengjie Wang, Tong Zhang, Mengchen Wang, Pieter Abbeel, Yang Gao
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，它把强化学习最难落地的两个问题——样本效率和奖励设计——都交给 foundation priors 来缓解，而且给出了真实机器人学习设置。
* **问题与切口**: RLFP 的目标非常明确：让 embodied agent 能更高效、更少人工奖励工程地自己学会操作任务。它不是简单把基础模型当成 imitation teacher，而是把 policy、value 与 success-reward 三类 foundation priors 一起并入 RL 框架，形成可在 Goal-Conditioned MDP 中使用的统一先验体系。相较于“预训练后直接部署”或“纯 RL 从零探索”，这条路线的创新点在于把基础模型变成 RL 的结构化引导与反馈源，再让 agent 通过交互自行补足任务能力。
* **核心方法与证据**: 论文先形式化提出 RLFP，再基于 actor-critic 实现 FAC，并单独说明三类 foundation models 如何获得。摘录给出的实验证据边界相对清楚：作者同时做了真实机器人与仿真评估，并专门考察样本效率、每类 prior 的贡献，以及 foundation model 质量的影响。真实平台使用 Franka Panda，观测来自固定外部相机与腕部相机，任务共五个，其中大多数任务训练一小时，Pick Place 训练三十分钟。虽然没有摘录到具体成绩，但至少能确认它不是只停留在模拟器层面的概念验证。
* **正文要点**:
  - RLFP 同时利用 policy prior、value prior 和 success-reward prior。
  - FAC 把这些先验注入 actor-critic，而不是替代 RL 交互本身。
  - 实验同时覆盖真实机器人、仿真环境和先验质量/组成的消融。
* **为什么值得跟**:
  - 它为 RL 与基础模型结合提供了比“拿 VLA 直接当策略”更细粒度的接口设计。
  - 真实机器人一小时级学习设置，使其对样本效率问题具有直接现实意义。
  - Pieter Abbeel 这条线值得持续跟，因为它把 foundation models 从模仿学习扩展到自主学习范式。
* **风险 / 保留意见**:
  - 先验质量若不足，RL 可能被错误的 policy/value/reward 引导，导致探索与收敛同时受损。
  - 摘录未提供与哪些强基线比较、真实任务成功曲线如何变化，因此实际优势幅度仍需核对 PDF。
* **建议先看**: 先看 RLFP 的先验形式化，判断三类 prior 是如何进入 Bellman 更新与策略优化的。再直接读真实机器人实验和消融，确认它到底是靠哪个 prior 真正提高了学习效率。
* **关键词**: `强化学习` `foundation priors` `actor-critic` `真实机器人学习` `样本效率`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - policy、value 和 success-reward 三类 priors 分别以何种损失或约束形式进入 FAC，它们之间是否存在冲突权重？
  - foundation model 质量变化对 RL 收敛最敏感的是哪一种 prior，是否存在某类 prior 反而拖累学习？
  - 在真实机器人一小时级训练中，性能提升来自更快探索、奖励塑形改善，还是更稳的 credit assignment？
* **上传 PDF 后优先看**:
  - RLFP 形式化与 FAC 算法部分
  - 真实机器人设置与学习曲线
  - 三类 priors 的消融与质量分析

## Watchlist

### [W1]. Demystifying Action Space Design for Robotic Manipulation Policies [[VIP]] [[HTML]](https://arxiv.org/html/2602.23408) [[PDF]](https://arxiv.org/pdf/2602.23408)
* **Paper ID**: `2602.23408`
* **Authors**: Yuchun Feng, Jinliang Zheng, Zhihao Wang, Dongxiu Liu, Jianxiong Li, Jiangmiao Pang, Tai Wang, Xianyuan Zhan
* **Author Priority**: Core VIP
* **为什么还值得留意**: 这篇进入 shortlist 很合理，因为它系统性追问 action space 这个经常被 VLA 论文一笔带过、但实际上深刻影响优化与部署稳定性的底层问题，而且作者名单里有 Jiangmiao Pang。它覆盖多种硬件平台、真实机器人与仿真，并比较不同生成式策略范式，研究设计看起来扎实。之所以没进最终精选，是因为它更像“底层设计准则”论文，和今天主线中的 long-horizon VLA、world model、RL+VLA 相比，系统层推进感稍弱。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)

### [W2]. CorridorVLA: Explicit Spatial Constraints for Generative Action Heads via Sparse Anchors [[HTML]](https://arxiv.org/html/2604.21241) [[PDF]](https://arxiv.org/pdf/2604.21241)
* **Paper ID**: `2604.21241`
* **Authors**: Dachong Li, ZhuangZhuang Chen, Jin Zhang, Jianqiang Li
* **Author Priority**: Standard
* **为什么还值得留意**: CorridorVLA 有明确技术切口：用 sparse anchors 给 generative action head 加显式空间约束，这比把空间信息隐含塞进 latent 更可解释，也更贴近控制目标。它在 SmolVLA 和 GR00T 两类 backbone 上验证，说明方法具备一定通用性。没有进入最终精选，主要因为当前证据集中在标准 benchmark，作者也明确承认没有 real-robot 实验，因此更适合作为值得跟踪的结构化改进，而不是今天的核心代表作。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. From Noise to Intent: Anchoring Generative VLA Policies with Residual Bridges [[HTML]](https://arxiv.org/html/2604.21391) [[PDF]](https://arxiv.org/pdf/2604.21391)
* **Paper ID**: `2604.21391`
* **Authors**: Yiming Zhong, Yaoyu He, Zemin Yang, Pengfei Tian, Yifan Huang, Qingqiu Huang, Xinge Zhu, Yuexin Ma
* **Author Priority**: Standard
* **为什么还值得留意**: ResVLA 的问题意识很强，直接挑战 generative VLA 的“from noise”范式，改走“from intent”的 residual bridge 路线，并把语义意图与局部执行分开建模，这和今天的显式中间结构趋势高度一致。它还声称覆盖鲁棒性、效率、跨 embodiment 与真实机器人，方向上相当有野心。之所以暂留 watchlist，是因为当前摘录更像方法主张和实验假设框架，真正决定分量的还是 PDF 里对 gains、失败模式和训练稳定性的实证细节。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. VistaBot: View-Robust Robot Manipulation via Spatiotemporal-Aware View Synthesis [[HTML]](https://arxiv.org/html/2604.21914) [[PDF]](https://arxiv.org/pdf/2604.21914)
* **Paper ID**: `2604.21914`
* **Authors**: Songen Gu, Yuhang Zheng, Weize Li, Yupeng Zheng, Yating Feng, Xiang Li, Yilun Chen, Pengfei Li, Wenchao Ding
* **Author Priority**: Standard
* **为什么还值得留意**: VistaBot 解决的是一个非常实际却常被低估的问题：固定视角训练的操控策略对相机视角变化很脆弱，而这恰恰卡住了端到端系统的可扩展性。它把 4D geometry estimation、view synthesis latent 和 latent action learning 串起来，并且同时做了仿真与真实实验，还提出了 View Generalization Score，完成度不低。没进最终精选的原因是它更偏“视角鲁棒性感知与表示增强”模块，和今天更核心的 VLA 任务管理、world model 后训练、RL 自主学习相比，主线贴合度略弱。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
