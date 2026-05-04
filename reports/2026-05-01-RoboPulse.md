# RoboPulse | 2026-05-01

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 52 papers scanned · 10 shortlisted · 5 editor's picks

今天的主线很清楚：VLA 正从以模仿学习为核心的“看图出动作”，转向把世界动态、潜在推理、目标可达性和接触物理显式纳入决策回路。最终精选的五篇分别覆盖统一 World Action Model、RL 驱动的 latent reasoning、以 goal-conditioned RL 重写 VLA 预训练、WAM 对 VLA 的稳健性比较，以及触觉引导的推理时控制，组合起来比单点提分更能代表接下来一段时间的研究方向。它们入选的共同原因，不是都给出同一种 SOTA 叙事，而是都在回答“VLA 下一步该如何补足时间结构、物理结构和泛化能力”这个核心问题。就 VIP 作者跟踪优先级看，这批最终精选里最值得优先盯的是 Hao Su 参与的 TouchGuide；其余入选更像是方法趋势领先于作者光环，说明这一波热点正在向更广泛团队扩散。

## 今日信号

- 今天最值得记住的研究信号：VLA 的竞争点正在从静态语义对齐，转向对未来视觉后果、接触约束和目标可达性的内部建模。
- 今天最值得记住的研究信号：RL 在 VLA 里的作用不再只是微调动作头，而是开始直接塑造 latent reasoning、value representation 和规划先验。
- 今天最值得记住的研究信号：world model / world action model 的价值判断，已经从“能不能生成未来”转向“能不能在分布偏移和真实部署中带来更稳健的控制收益”。

## Editor's Picks

### [1]. MotuBrain: An Advanced World Action Model for Robot Control [[HTML]](https://arxiv.org/html/2604.27792) [[PDF]](https://arxiv.org/pdf/2604.27792) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.27792`
* **Authors**: MotuBrain Team, Chendong Xiang, Fan Bao, Haitian Liu, Hengkai Tan, Hongzhe Bi, James Li, Jiabao Liu, Jingrui Pang, Kiro Jing, Louis Liu, Mengchen Cai, Rongxu Cui, Ruowen Zhao, Runqing Wang, Shuhe Huang, Yao Feng, Yinze Rong, Zeyuan Wang, Jun Zhu
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把 World Action Model 从概念拼装推进成了一个统一生成式系统，并且在统一评测里给出很强的控制结果。
* **问题与切口**: 这篇工作瞄准 VLA 的一个核心短板：模型继承了很强的视觉语义先验，却常常缺少对细粒度世界动态的建模，因此更像表层模仿而不是时序理解。MotuBrain 的切口是把 video 与 action 放进同一个统一生成框架里，做成既能当 policy、又能当 world model、还能做 inverse dynamics 和联合预测的 World Action Model。相较于把视频预测、动作生成和机器人适配拆成多模块路线，它更强调“一套模型、多种推理模式”的统一性。
* **核心方法与证据**: 从可见 HTML 看，MotuBrain 建立在 UniDiffuser formulation 之上，并采用 three-stream Mixture-of-Transformers 来联合建模多模态视频与动作序列。作者强调同一模型支持 policy learning、world modeling、video generation、inverse dynamics 等多种推理模式，再通过大规模预训练加轻量机器人适配落地到控制。证据层面，正文给出了 RoboTwin 2.0 协议下的多任务训练、clean 与 heavily randomized 场景评测，以及不同 policy architecture 的消融；可见摘录中它在平均成功率和 randomized setting 上表现很强，但更细的误差来源和模块贡献仍需 PDF 核查。
* **正文要点**:
  - 将 video 与 action 放进统一 UniDiffuser 框架，并声明支持 policy、world model、inverse dynamics 等多种推理模式。
  - RoboTwin 2.0 采用 clean 与 heavily randomized 的多任务训练设置，明显把场景随机化适应能力作为主验证面。
  - 结论部分强调“大规模预训练 + 轻量机器人适配”的组合，而不是完全依赖纯机器人数据端到端重训。
* **为什么值得跟**:
  - 它把 VLA 的语义先验和显式世界动态建模更紧地捆在一起。
  - 如果统一模型真能兼顾多推理模式，训练与部署复用成本都有机会下降。
  - 它为 WAM 是否能成为 VLA 下一阶段主干提供了强正面样例。
* **风险 / 保留意见**:
  - 当前强证据主要来自 RoboTwin 与作者汇总结果，跨平台真实机器人细节还不够充分。
  - 多能力统一在一个模型里是否存在模式间干扰，HTML 摘录里暂时看不清。
* **建议先看**: 先看方法部分如何把 video 与 action 放进同一生成式框架，再看 RoboTwin 主结果与架构消融，判断性能提升究竟来自统一建模本身，还是主要来自训练配方与数据规模。
* **关键词**: `World Action Model` `VLA` `UniDiffuser` `Mixture-of-Transformers` `RoboTwin`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 三流架构里各模态和动作流如何分工，哪些共享参数决定了多推理模式的兼容性？
  - 性能提升主要来自大规模预训练、统一生成目标，还是机器人适配阶段的具体设计？
  - 在随机化场景之外，模型对长时序误差累积和真实接触动力学的鲁棒性如何？
* **上传 PDF 后优先看**:
  - 方法章节中的统一生成目标与三流架构说明
  - 主基准实验与 randomized setting 对比结果
  - 消融实验里不同 policy architecture 的比较

### [2]. LaST-R1: Reinforcing Action via Adaptive Physical Latent Reasoning for VLA Models [[HTML]](https://arxiv.org/html/2604.28192) [[PDF]](https://arxiv.org/pdf/2604.28192) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.28192`
* **Authors**: Hao Chen, Jiaming Liu, Zhonghao Yan, Nuowei Han, Renrui Zhang, Chenyang Gu, Jialin Gao, Ziyu Guo, Siyuan Qian, Yinxi Wang, Peng Jia, Chi-Wing Fu, Shanghang Zhang, Pheng-Ann Heng
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把 VLA 里的“先推理再动作”真正接到了在线 RL 上，而不是停留在静态模仿学习。
* **问题与切口**: LaST-R1 抓住了当前 reasoning-style VLA 的一个关键空缺：无论是显式语言推理还是连续潜变量推理，很多方法最终仍停留在 imitation learning 框架里，适应性和泛化能力受限；而已有 RL+VLA 又往往只优化原始动作空间，绕开了物理推理本身。它的核心新意，是把 latent reasoning 与 action generation 放进同一个 VLA 结构里，并用 RL 去直接塑造从潜在推理到动作执行的耦合过程。
* **核心方法与证据**: 根据可见方法摘录，LaST-R1 建在 Qwen3-VL-4B 上，视觉编码器为 SigLIP2-Large；视觉 token 与语言 token 一起送入 LLM backbone，模型先自回归生成 latent reasoning tokens，再生成离散化后的 action tokens。作者进一步提出 Latent-to-Action Policy Optimization（LAPO），试图让在线 RL 不只修动作输出，而是联动优化潜在物理推理与行动。证据层面，HTML 明确给出两阶段训练流程：先做预训练与 SFT warm-up，再在 LIBERO 四套任务上做在线 RL，并报告真实机器人部署与泛化分析，但具体奖励设计和收益分解仍需 PDF 支撑。
* **正文要点**:
  - 模型先生成 latent reasoning tokens，再生成离散化 action tokens，把推理与执行放在同一自回归框架内。
  - 在线 RL 不是只调原始动作，而是围绕 Latent-to-Action Policy Optimization 去塑造潜在推理到动作的耦合。
  - 实验设计把 SFT warm-up 压到每任务单条 expert 轨迹，意在更清晰地暴露 RL post-training 的贡献。
* **为什么值得跟**:
  - 它把 VLA 中最热的 reasoning 叙事，从离线演示学习推进到可适应的在线改进。
  - 如果 latent reasoning 真承载了物理结构，它可能比文字 CoT 更适合低时延控制。
  - 它为 RL+VLA 提供了更细粒度的优化接口，不再只是给动作头做后训练。
* **风险 / 保留意见**:
  - HTML 摘录还不足以判断 latent token 学到的是真实物理因果，还是仅仅提供了更大容量。
  - LIBERO 与定制预训练数据的收益分解不够透明，真实部署泛化强度仍需看 PDF 细节。
* **建议先看**: 先抓住 latent token 的构造和 LAPO 的优化接口，再看 LIBERO 四套任务与 real-world/generalization 部分是否真正证明“推理被 RL 塑形”，而不仅是模型变大或训练更久。
* **关键词**: `VLA` `Reinforcement Learning` `Latent Reasoning` `LAPO` `LIBERO`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - latent reasoning token 到底编码了哪些可验证的物理信息，是否有可视化或 probing 证据？
  - LAPO 的优化目标如何把推理质量与最终任务回报关联起来，而不是间接提升动作采样？
  - 在极低数据 warm-up 设定下，方法对探索稳定性和训练成本的敏感性有多强？
* **上传 PDF 后优先看**:
  - 方法章节中 latent representation 与 token 生成流程
  - RL post-training / LAPO 目标与训练算法说明
  - LIBERO 主结果、泛化实验与真实机器人部署

### [3]. PRTS: A Primitive Reasoning and Tasking System via Contrastive Representations [[HTML]](https://arxiv.org/html/2604.27472) [[PDF]](https://arxiv.org/pdf/2604.27472) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.27472`
* **Authors**: Yang Zhang, Jiangyuan Zhao, Chenyou Fan, Fangzheng Yan, Tian Li, Haitong Tang, Sen Fu, Xuan'er Wu, Qizhen Weng, Weinan Zhang, Xiu Li, Chi Zhang, Chenjia Bai, Xuelong Li
* **Author Priority**: Standard
* **一句话结论**: 非常值得看，它不是给 VLA 再加一个 value head，而是试图从预训练目标本身重写 VLA。
* **问题与切口**: PRTS 的出发点很直接：机器人轨迹本质上是一个随时间推进的 goal-reaching 过程，但现有 VLA 预训练大多仍按 supervised behavior cloning 来做，难以在表征里显式编码任务进度。它因此把 VLA 预训练重述为 goal-conditioned reinforcement learning：把语言指令视作目标，用 contrastive RL 去学习一个统一嵌入空间，使状态-动作表征能够对应“是否更接近完成该目标”的可达性信号。相较于依赖奖励标签或单独 value 网络的路线，这个切口更基础。
* **核心方法与证据**: 从可见正文看，作者明确把监督来源放在离线轨迹结构本身，而不是人工奖励或进度标注上。其核心主张是：通过 language-conditioned 的 contrastive objective，在 backbone 里直接塑造 goal-reachability-aware representations，而不是先训练一个行为克隆模型，再外挂 value 模块。实验部分的可见摘录没有把所有数据和数值展开，但已清楚列出验证面：仿真与真实部署、分布偏移、零样本指令泛化、人类干预恢复、值分析与预训练效率。这说明论文重点不是单点分数，而是验证这种预训练目标是否真的带来更稳健的表征。
* **正文要点**:
  - 把语言指令视为 goal，用 state-action 与 goal 的内积去表达 reachability，而不是只做行为克隆。
  - 训练监督来自离线轨迹结构本身，作者明确强调不依赖奖励标签、进度标注或独立 value network。
  - 实验问题设置覆盖分布偏移、零样本指令跟随、人类干预恢复和值分析，明显把“鲁棒性”作为主评价面。
* **为什么值得跟**:
  - 如果预训练表征自带 goal-progress 语义，VLA 的泛化上限可能高于纯 BC 路线。
  - 它把 RL 的思想前移到 foundation pretraining，而不是只在下游微调阶段使用。
  - 对长时序操作和失败恢复而言，这类 reachability-aware 表征更有吸引力。
* **风险 / 保留意见**:
  - HTML 摘录未给出关键对比的量化幅度，当前更像强命题而非完全坐实的结论。
  - contrastive reachability 是否能稳定泛化到开放世界任务，仍可能强依赖数据覆盖与负样本构造。
* **建议先看**: 优先读问题定义与 contrastive RL 目标，确认它如何把“目标可达性”嵌进 backbone；随后直接看分布偏移、零样本指令和干预恢复实验，这些最能检验这条路线是否真优于行为克隆。
* **关键词**: `VLA Pretraining` `Goal-Conditioned RL` `Contrastive RL` `Goal Reachability` `Robustness`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 对比学习里的正负样本和时序配对是如何构造的，是否会隐式泄漏任务进度先验？
  - reachability 表征在下游策略头之外能否被独立 probing，证明它不是普通语义嵌入的副产品？
  - 当任务目标包含多阶段子目标时，单一内积式目标是否足够表达复杂进度结构？
* **上传 PDF 后优先看**:
  - 预训练目标与 contrastive RL 公式化章节
  - 值分析与表征分析相关实验
  - 分布偏移、零样本指令和人类干预恢复实验

### [4]. Do World Action Models Generalize Better than VLAs? A Robustness Study [[HTML]](https://arxiv.org/html/2603.22078) [[PDF]](https://arxiv.org/pdf/2603.22078) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.22078`
* **Authors**: Zhanguang Zhang, Zhiyuan Li, Behnam Rahmati, Rui Heng Yang, Yintao Ma, Amir Rasouli, Sajjad Pakdamansavoji, Yangzheng Wu, Lingfeng Zhang, Tongtong Cao, Feng Wen, Xinyu Wang, Xingyue Quan, Yingxue Zhang
* **Author Priority**: Standard
* **一句话结论**: 值得放进最终精选，因为它不是再造一个模型，而是正面回答了 WAM 相比 VLA 是否真的更泛化。
* **问题与切口**: 这篇论文的重要性在于它把问题提得很对：当 world action model / world model 在机器人里重新升温时，社区真正需要的不是更多口号式“更会想象未来”，而是明确比较这类方法与标准 VLA 在泛化和鲁棒性上到底谁更强。从标题、摘要与可见引言看，作者核心切口不是追求某个单一 benchmark 的绝对分数，而是围绕未见场景、上下文扰动与真实动作规划难题，检验 WAM 是否比 VLA 更具稳健优势。
* **核心方法与证据**: 可见 HTML 中，方法部分先对 robotics 里的 world model 用法做了结构化梳理：它既可以作为 learned simulator，也可以作为规划辅助模块，或在一定适配后直接充当策略本身。这种分类本身就很有价值，因为它把不同“world model 叙事”拆开来讨论。证据边界也必须说清：当前摘录没有展开具体 benchmark、扰动构造和最终谁赢多少，因此这里更应把它视作一篇检验研究叙事成立与否的比较论文，而不是一篇已被摘要数字完全坐实的性能宣言。
* **正文要点**:
  - 论文明确把比较对象设为 WAM 与 VLA 的 generalization / robustness，而非单一任务上的平均成功率。
  - 方法部分先把 robotics 中 world model 的角色分成 learned simulator、planning auxiliary 和 adapted policy 三类。
  - 从可见摘录看，作者重点在构建比较视角；具体扰动设计与定量结论仍需 PDF 核查。
* **为什么值得跟**:
  - 当前领域需要这种“范式对范式”的证伪型论文，而不只是新模型堆叠。
  - 它能帮助判断 WAM 热潮究竟来自预测未来的真实收益，还是主要来自训练规模和评测选择。
  - 如果稳健性优势成立，world model 更可能成为主线，而不是仅仅充当配件。
* **风险 / 保留意见**:
  - HTML 证据不足，暂时无法确认实验覆盖面是否足以支撑强结论。
  - 比较研究很容易受到训练数据、模型规模和评测协议不对齐的影响。
* **建议先看**: 这篇最适合带着“评测公平性”去读。先看比较框架和扰动维度是否对齐，再看作者如何控制数据规模、模型容量和任务设置，否则所谓范式差异很可能被实验设计本身主导。
* **关键词**: `World Action Model` `VLA` `Robustness` `Generalization` `Comparative Study`
* **证据来源**: arXiv HTML (Introduction, Method)
* **读 PDF 先核查**:
  - 作者如何保证 WAM 与 VLA 在数据、规模和训练预算上的对比公平？
  - 鲁棒性测试具体覆盖哪些扰动，是否区分语义泛化、物理泛化和感知干扰？
  - 如果 WAM 更强，优势主要来自预测未来状态本身，还是来自更好的规划接口？
* **上传 PDF 后优先看**:
  - 实验设置中的对比协议与公平性说明
  - 鲁棒性/泛化评测章节
  - 结果讨论中对 WAM 优势来源的归因分析

### [5]. TouchGuide: Inference-Time Steering of Visuomotor Policies via Touch Guidance [[VIP]] [[HTML]](https://arxiv.org/html/2601.20239) [[PDF]](https://arxiv.org/pdf/2601.20239) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2601.20239`
* **Authors**: Zhemeng Zhang, Jiahua Ma, Xincheng Yang, Xin Wen, Yuzhi Zhang, Boyan Li, Yiran Qin, Jin Liu, Can Zhao, Li Kang, Haoqin Hong, Zhenfei Yin, Philip Torr, Hao Su, Ruimao Zhang, Daolin Ma
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，尤其因为它把触觉真正做成了推理时控制信号，而不是再训练一个更重的多模态策略。
* **问题与切口**: TouchGuide 对准的是精细、接触密集操作里一个长期被低估的问题：视觉能给全局场景理解，但真正决定动作成败的往往是局部接触物理。它没有沿着常见的 feature-level 或 policy-level 融合继续堆模型，而是提出一种 cross-policy 的 visuo-tactile 融合范式，在低维动作空间里对预训练 diffusion 或 flow-matching visuomotor policy 做 inference-time steering。这个切口的价值，在于它把触觉从“训练时一起喂进去”改成“执行时用于修正动作”。
* **核心方法与证据**: 从可见方法部分看，TouchGuide 采用两阶段机制：前期采样阶段仅依赖视觉生成一个粗粒度、视觉上可行的动作；后期则引入任务特定的 Contact Physical Model（CPM），用 feasibility score 对动作进行触觉引导和修正。作者把这一过程与 classifier guidance 联系起来，并且还专门讨论了 flow matching 场景下的指导形式。实验上，论文通过 TacUMI 数据采集系统在五个接触密集任务上验证方法，并覆盖双臂 Bi-ARX5、单臂 Flexiv Rizon4、不同传感器与不同策略，证据方向是对的，但每类收益的来源仍需 PDF 细拆。
* **正文要点**:
  - 推理分两阶段：先由纯视觉策略给出粗动作，再由 Contact Physical Model 在后期采样中做触觉引导。
  - 方法明确兼容 diffusion-based 与 flow-matching-based visuomotor policy，而不是绑定单一策略族。
  - 实验覆盖五个接触密集任务，并专门追问跨机器人、跨触觉传感器、跨策略的泛化能力。
* **为什么值得跟**:
  - 它把触觉从训练时特征拼接，改成了测试时可插拔的物理约束。
  - 对现有大量视觉主导的 VLA/visuomotor policy，这提供了一条低侵入升级路径。
  - 在精细操作和脆弱物体交互上，这类推理时校正比纯视觉更有现实价值。
* **风险 / 保留意见**:
  - 任务特定 CPM 的构建成本与可迁移性，可能决定方法真实可扩展性。
  - 如果基础视觉策略本身误差过大，后期 guidance 能纠正到什么程度还需要更细证据。
* **建议先看**: 先看 IV-A 到 IV-C，弄清 classifier guidance 如何被改造成 visuo-tactile action steering；然后重点看五类任务里哪些收益真正来自触觉，哪些可能只是更好的采样或后处理。
* **关键词**: `Visuo-Tactile` `Inference-Time Steering` `Diffusion Policy` `Flow Matching` `Hao Su`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - CPM 的 feasibility score 如何定义和训练，是否会对不同任务重复大量工程化建模？
  - TouchGuide 在 diffusion 与 flow-matching 两类基础策略上的收益是否一致，还是强依赖其中一类？
  - 触觉 guidance 介入的时机和强度对最终稳定性有多敏感？
* **上传 PDF 后优先看**:
  - 方法章节中 classifier guidance 与 flow-matching 推导
  - CPM 构建与触觉可行性评分说明
  - 跨机器人/传感器/策略泛化实验

## Watchlist

### [W1]. GazeVLA: Learning Human Intention for Robotic Manipulation [[HTML]](https://arxiv.org/html/2604.22615) [[PDF]](https://arxiv.org/pdf/2604.22615)
* **Paper ID**: `2604.22615`
* **Authors**: Chengyang Li, Kaiyi Xiong, Yuan Xu, Lei Qian, Yizhou Wang, Wentao Zhu
* **Author Priority**: Standard
* **为什么还值得留意**: GazeVLA 进入 shortlist 的原因很充分：它抓住了“用人类意图而不是直接动作桥接 human-to-robot gap”这个很有潜力的方向，并且人类预训练数据规模、gaze 监督和 VLIA 框架都很有辨识度。没有进最终精选，主要是因为它更偏 human intention transfer 与 active perception，和今天最核心的 world model / world action model / RL-driven VLA 主线相比还是次一级；现有摘录也更强调意图预测与 AV-ALOHA 验证，还不足以压过最终入选那几篇对范式演进更直接的论文。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. DOT-Sim: Differentiable Optical Tactile Simulation with Precise Real-to-Sim Physical Calibration [[HTML]](https://arxiv.org/html/2604.27367) [[PDF]](https://arxiv.org/pdf/2604.27367)
* **Paper ID**: `2604.27367`
* **Authors**: Yang You, Won Kyung Do, Aiden Swann, Rika Antonova, Monroe Kennedy, Leonidas Guibas
* **Author Priority**: Standard
* **为什么还值得留意**: DOT-Sim 是今天 shortlist 里最强的 Sim2Real 基础设施候选之一：用 MPM 做软传感器形变建模，再配合可微校准和光学渲染，路线很扎实，且明确面向真实触觉传感器的快速 real-to-sim 校准。之所以留在 watchlist，而没有进最终精选，是因为它更像触觉仿真平台论文，和今天聚焦的 VLA / WAM / RL 主线是间接相关；它的重要性更多体现在上游数据与仿真可信度，而不是直接重写当前机器人 foundation model 的决策范式。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. ExoActor: Exocentric Video Generation as Generalizable Interactive Humanoid Control [[HTML]](https://arxiv.org/html/2604.27711) [[PDF]](https://arxiv.org/pdf/2604.27711)
* **Paper ID**: `2604.27711`
* **Authors**: Yanghao Zhou, Jingyu Ma, Yibo Peng, Zhenguo Sun, Yu Bai, Börje F. Karlsson
* **Author Priority**: Standard
* **为什么还值得留意**: ExoActor 很有想象力：它把第三人称视频生成当作类人机器人控制的统一中间接口，和今天的 world-model 化趋势高度同频，因此进入 shortlist 没问题。没有进最终精选，主要因为从可见摘录看，论文更像一个由 video generation、motion estimation、motion execution 串起来的系统可行性展示，作者自己在结论里也强调了多环节限制；相比之下，MotuBrain 和那篇 WAM-vs-VLA robustness study 对“world model 是否更好”这个核心问题给出的命题更集中。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. RAY-TOLD: Ray-Based Latent Dynamics for Dense Dynamic Obstacle Avoidance with TDMPC [[HTML]](https://arxiv.org/html/2604.27450) [[PDF]](https://arxiv.org/pdf/2604.27450)
* **Paper ID**: `2604.27450`
* **Authors**: Seungho Han, Seokju Lee, Jeonguk Kang
* **Author Priority**: Standard
* **为什么还值得留意**: RAY-TOLD 值得保留在 watchlist，因为它把 latent dynamics、value modeling、TDMPC/MPPI 式长短期结合讲得很清楚，而且在高密动态障碍规避里确实击中了 world model 的实用价值。没有进最终精选，原因在于它更偏移动机器人导航与混合规划控制，和今天明确聚焦的 manipulation-oriented VLA / WAM 主线有距离；同时其贡献更像特定任务域的强系统整合，而不是对通用 embodied foundation model 方向的直接推进。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W5]. RopeDreamer: A Kinematic Recurrent State Space Model for Dynamics of Flexible Deformable Linear Objects [[HTML]](https://arxiv.org/html/2604.28161) [[PDF]](https://arxiv.org/pdf/2604.28161)
* **Paper ID**: `2604.28161`
* **Authors**: Tim Missal, Lucas Domingues, Berk Guler, Simon Manschitz, Jan Peters, Paula Dornhofer Paro Costa
* **Author Priority**: Standard
* **为什么还值得留意**: RopeDreamer 入围 shortlist，主要因为它代表了 world model 在可变形体操控上的一个扎实分支：用 recurrent state space model 结合 quaternion kinematic chain，专门解决长时预测中的拓扑保持问题。没有进最终精选，是因为它的任务边界明显更窄，重点在 DLO dynamics 建模本身，而不是与 VLA、RL 后训练或统一 action/world modeling 的主线直接汇合；从可见摘录看，控制闭环和更广泛泛化证据也不如最终入选论文那么突出。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
