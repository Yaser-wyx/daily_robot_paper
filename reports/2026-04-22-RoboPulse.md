# RoboPulse | 2026-04-22

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 64 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线很清晰：VLA 与机器人世界模型正在从“会看会说会生成”转向“能记、能验、能执行、能迁移”的具身闭环。最终精选覆盖了四个最关键瓶颈：部署期物理学习、统一训练基础设施、世界模型的可执行评测与控制导向表征，以及用记忆与 RL 改造长期操控和 sim2real 数据供给。它们入选不是因为单点性能口号，而是因为都在重写机器人基础模型真正落地所需的接口、评价标准或数据生产方式。今天直接命中的核心 VIP 作者是 Hao Su 与 Shuran Song，优先级最高；其余 VIP 名单在本批最终精选中未明显出现，但仍建议持续跟踪其合作网络中的 VLA/世界模型新作。

## 今日信号

- 今天最值得记住的研究信号是：机器人世界模型的评判标准正在从视觉逼真度转向物理可执行性与控制有效性。
- 今天最值得记住的研究信号是：长历史不再被默认当作更多上下文，记忆正被重构为可门控、可验证、可跨 trial 积累的能力模块。
- 今天最值得记住的研究信号是：VLA 研究开始同时补齐训练栈、评测协议与自动专家数据生产，说明领域正从模型展示转向工程化扩张。

## Editor's Picks

### [1]. PhysMem: Scaling Test-time Physical Memory for Robot Manipulation [[VIP]] [[HTML]](https://arxiv.org/html/2602.20323) [[PDF]](https://arxiv.org/pdf/2602.20323) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2602.20323`
* **Authors**: Haoyang Li, Yang You, Hao Su, Leonidas Guibas
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，它把 VLM 机器人规划里最难落地的“物理常识缺乏实例化”问题，转成了可验证的测试时记忆循环。
* **问题与切口**: 这篇工作针对 VLM 规划器懂物理概念、却不懂当前场景具体物理参数的核心断层，提出一种不改参数的测试时物理记忆框架。它不把失败简单当作更多上下文，而是把交互经验组织成可提出、可验证、可晋升的“原则”。相对直接微调或长上下文堆叠，这条路线更像部署期科学实验：先形成关于摩擦、稳定性等具体假设，再用针对性交互确认哪些知识值得保留。
* **核心方法与证据**: 方法上，PhysMem 用一个 scientific memory loop 串起经验记录、假设生成、定向验证与原则晋升，并把物理操控写成 options 框架：高层 VLM 根据当前观测、任务文本和记忆中激活的原则选取 option，低层执行器负责落地。证据来自真实机器人评估与 Reflect-VLM 插砖基准；后者在 MuJoCo 中可扩展到 500+ episodes，并按 2-8 块砖的难度分层测试不同 VLM 的物理学习能力。
* **正文要点**:
  - 把物理操控写成 options 框架，高层 VLM 依据任务、观测与记忆中的有效原则选动作。
  - 记忆不是原始轨迹缓存，而是经过假设生成、定向验证后才晋升的原则性知识。
  - 实验同时含真实机器人与 Reflect-VLM 插砖基准，且后者可扩到 500+ episode 的受控评测。
* **为什么值得跟**:
  - 它把 VLM 的物理落地问题从参数更新转为部署期可审计的记忆与实验设计问题。
  - 对接任意低层执行器的表述很通用，兼容运动规划器、VLA 或其他控制器。
  - 如果这类机制成立，机器人在陌生物体和表面上的适应将更接近真正的在场学习。
* **风险 / 保留意见**:
  - 当前证据主要依赖视觉观测与结果反馈，触觉、力觉和声音等关键物理信号尚未纳入主实验。
  - 假设生成与验证策略若设计不稳，记忆中错误原则可能仍会影响后续长链规划。
* **建议先看**: 先读问题定义和 scientific memory loop，判断作者如何把“经验”压缩成可调用原则；再看插砖基准与真实机器人案例，确认这种记忆是否真的提升了物理决策，而不只是任务特化缓存。
* **关键词**: `test-time memory` `VLM planner` `physical grounding` `robot manipulation` `option framework`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 原则从单次或少量交互中被提炼出来时，作者如何避免把偶然成功误写成通用物理规律？
  - 当记忆检索出的原则彼此冲突时，高层 VLM 选择 option 的机制如何处理优先级与失效回退？
  - 如果换成含触觉或力反馈的执行器，PhysMem 的记忆单元是否仍保持同样的抽象粒度？
* **上传 PDF 后优先看**:
  - 方法章节里 scientific memory loop 与原则晋升条件
  - 受控插砖基准的难度分层、episode 设计与跨 VLM 对比
  - 真实机器人案例中记忆带来行为改变的定性分析

### [2]. VLA Foundry: A Unified Framework for Training Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2604.19728) [[PDF]](https://arxiv.org/pdf/2604.19728) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.19728`
* **Authors**: Jean Mercat, Sedrick Keh, Kushal Arora, Isabella Huang, Paarth Shah, Haruki Nishimura, Shun Iwase, Katherine Liu
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它不是又一个 VLA 模型，而是把 LLM、VLM、VLA 训练链条真正打通的研究基础设施。
* **问题与切口**: 这篇工作的核心价值在于把当前割裂的语言预训练、视觉语言建模和动作微调流程统一进一个开源代码栈，使研究者能系统地研究“从语料到动作”各阶段的耦合关系。相对只发布动作头或单一 checkpoint 的项目，它更强调端到端可控性、模块一致性和可复现实验，这对比较数据配比、骨干选择与训练策略尤其关键。
* **核心方法与证据**: 作者提供同一框架下的两条演示路径：一条从头完成 LLM→VLM→VLA 训练，另一条接入 Hugging Face 预训练骨干，并以 Qwen3-VL 为代表做动作阶段扩展。证据主要来自 LBM Eval 开源模拟基准：49 个桌面双臂任务、Docker 化环境、可视化 dashboard，以及结合 STEP 与 CLD 的统计比较流程，明显强调社区可复用的评测闭环。
* **正文要点**:
  - 统一抽象覆盖数据、配置、训练与评测，目标是把 LLM、VLM、VLA 放到同一实验闭环。
  - 既支持从零训练，也支持在现成视觉语言骨干上继续做动作专家微调。
  - 评测侧不仅给 checkpoint，还补齐开源模拟器、Docker 分发与统计分析工具链。
* **为什么值得跟**:
  - 它降低了研究 VLA 数据规模律和预训练路径依赖的工程门槛。
  - 对社区来说，统一训练栈比单次模型结果更能沉淀可复用的比较协议。
  - 如果后续很多开源 VLA 工作复用这套栈，模型差异和训练差异会更容易被拆开讨论。
* **风险 / 保留意见**:
  - 论文更偏系统与平台贡献，算法新意主要体现在整合而非全新学习机制。
  - 当前主要证据来自开源模拟评测，真实机器人闭环迁移能力在摘录里还看不充分。
* **建议先看**: 先看作者如何定义统一训练栈的边界，再看两条模型路径分别证明了哪些研究自由度。评测部分重点关注它如何把统计显著性和可复现实验流程产品化。
* **关键词**: `VLA training stack` `LLM-VLM-VLA` `open-source framework` `LBM Eval` `evaluation tooling`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 统一代码栈是否真的减少了阶段间数据格式与 tokenizer 失配，还是主要解决了工程组织问题？
  - 从零训练路线与预训练骨干路线在同一协议下暴露出哪些最关键的性能瓶颈？
  - STEP 与 CLD 的统计接口是否足以支持社区做稳定的跨模型比较，尤其在 rollout 方差较大时？
* **上传 PDF 后优先看**:
  - 系统架构与训练阶段接口设计
  - 从零训练模型与 Qwen3-VL 扩展模型的实验设置
  - LBM Eval 开源评测、dashboard 与统计分析章节

### [3]. RoboWM-Bench: A Benchmark for Evaluating World Models in Robotic Manipulation [[HTML]](https://arxiv.org/html/2604.19092) [[PDF]](https://arxiv.org/pdf/2604.19092) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.19092`
* **Authors**: Feng Jiang, Yang Chen, Kyle Xu, Yuchen Liu, Haifeng Wang, Zhenhao Shen, Jasper Lu, Shengze Huang, Yuanfei Wang, Chen Xie, Ruihai Wu
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把“世界模型视频看起来像不像”升级成“生成行为能不能被机器人真正执行”。
* **问题与切口**: 这篇 benchmark 直指当前机器人世界模型评估的失真：视频预测越来越逼真，但视觉逼真并不等于物理可执行。作者提出的 RoboWM-Bench 不停留在感知打分或物理诊断，而是把生成的人手或机器人操控视频转成具身动作序列，再检查这些动作能否在统一环境中完成任务。这个切口对 World Model 和 World Action Model 都更贴近机器人真正关心的终点。
* **核心方法与证据**: 方法上，RoboWM-Bench 完全建立在开源仿真中，覆盖纯模拟任务和 real-to-sim 重建任务两类场景，以保证可复现性。它基于 LeHome 框架做具身执行评测；真实场景重建采用模块化流程，背景用 4D Gaussian 表示保留视觉与空间一致性，交互物体则单独建模，再把模型生成行为还原成机器人动作并验证任务是否完成。
* **正文要点**:
  - 核心评价对象不是视频质量本身，而是由预测行为导出的物理可执行性与任务完成度。
  - 同时支持人手视频和机器人视频，使 benchmark 不局限于单一数据来源。
  - real-to-sim 设计试图在开放复现与真实场景贴近度之间做折中。
* **为什么值得跟**:
  - 它为机器人世界模型提供了比 FVD 或感知指标更接近下游控制价值的评测目标。
  - 统一协议有助于比较不同视频生成路线是否真能支持动作决策。
  - 如果社区接受这类标准，未来世界模型论文必须回答“能否执行”而不仅是“能否生成”。
* **风险 / 保留意见**:
  - 执行结果仍依赖场景重建质量与动作恢复链路，误差可能混入世界模型评价。
  - benchmark 能验证 executability，但未必完整覆盖规划、探索或长时信用分配价值。
* **建议先看**: 先抓住 benchmark 的评价哲学：作者到底如何把生成视频映射为具身动作。随后重点核查 real-to-sim 重建链条，因为这决定了执行失败究竟来自世界模型还是评测管线。
* **关键词**: `world model benchmark` `embodied evaluation` `robot manipulation` `executability` `real-to-sim`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 从生成视频恢复动作序列时，作者如何隔离动作恢复误差与世界模型本身的误差？
  - 人手操控视频与机器人操控视频在执行映射上是否采用同一协议，公平性如何保证？
  - benchmark 中哪些任务最能暴露“视频合理但动力学错误”的失败模式？
* **上传 PDF 后优先看**:
  - 评价协议与动作恢复流程
  - real-to-sim 场景重建与 LeHome 仿真设置
  - 不同世界模型的失败案例与任务分布分析

### [4]. Mask World Model: Predicting What Matters for Robust Robot Policy Learning [[HTML]](https://arxiv.org/html/2604.19683) [[PDF]](https://arxiv.org/pdf/2604.19683) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.19683`
* **Authors**: Yunfan Lou, Xiaowei Chi, Xiaojie Zhang, Zezhong Qian, Chengxuan Li, Rongyu Zhang, Yaoxu Lyu, Guoyu Song, Chuyao Fu, Haoxuan Xu, Pengwei Wang, Shanghang Zhang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把世界模型从追求像素逼真，转向直接服务控制所需的几何与接触结构。
* **问题与切口**: MWM 的切口很清楚：机器人策略需要的是可控动力学线索，而不是把光照、纹理和背景运动都预测得很像。作者因此改为预测语义 mask 的时序演化，而非 RGB 像素，希望用几何信息瓶颈逼迫模型只保留与物理动态、接触关系和任务推进有关的因素。相对 RGB 世界模型，这是一条更明显面向控制目标重写表征空间的路线。
* **核心方法与证据**: 方法上，作者沿用视频 diffusion 架构，但把预测对象替换为 mask，并将 mask 动力学骨干与 diffusion policy head 直接耦合成闭环控制框架。证据主要来自 LIBERO 与 RLBench：前者覆盖 Spatial、Object、Goal 和 LIBERO-10 套件，后者报告 6 个代表性任务且每任务 20 次评测；对比对象包含 OpenVLA、CogACT 及多种 RGB 或 latent 世界模型管线。
* **正文要点**:
  - 训练时使用语义监督学习 mask 动力学，测试时仍只依赖原始多视角 RGB 输入。
  - 作者把“预测什么”视为控制泛化的核心，而不是默认继承视频生成中的 RGB 目标。
  - 实验同时比较 RGB-centric 基线、世界模型组合路线和作者自己的多种 mask 版本。
* **为什么值得跟**:
  - 它为世界模型服务机器人控制提供了更明确的表征偏置设计原则。
  - 若 mask 表征真的更稳，sim2real 和视觉扰动鲁棒性都可能因此受益。
  - 这篇工作也提醒社区，世界模型的好坏不该只由生成画面质量决定。
* **风险 / 保留意见**:
  - mask supervision 带来额外标注或离线语义管线依赖，训练成本与泛化边界需要细看。
  - 过强的几何瓶颈也可能丢失某些对操作关键但不易被 mask 表达的细粒度信息。
* **建议先看**: 先看作者为何断定 RGB 目标与控制目标错位，再看 mask dynamics 与 policy head 的耦合方式。实验部分重点核查视觉扰动、跨基准一致性，以及 mask 版本到底比哪些 RGB 路线更稳。
* **关键词**: `mask world model` `video diffusion` `robot policy learning` `semantic masks` `robust control`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - mask 表征是否足以覆盖接触前兆、遮挡恢复等需要细粒度视觉线索的情形？
  - 离线语义监督如果出现域偏差，会不会把世界模型的鲁棒性收益部分抵消？
  - 作者的优势更多来自预测目标改变，还是来自与 diffusion policy head 的联合设计？
* **上传 PDF 后优先看**:
  - 方法章节中 mask dynamics backbone 与 policy head 的接口
  - LIBERO 与 RLBench 对比实验及消融设置
  - 真实机器人评测与视觉干扰鲁棒性分析

### [5]. Gated Memory Policy [[VIP]] [[HTML]](https://arxiv.org/html/2604.18933) [[PDF]](https://arxiv.org/pdf/2604.18933) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.18933`
* **Authors**: Yihuai Gao, Jinyun Liu, Shuang Li, Shuran Song
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，它把机器人记忆问题从“喂更长历史”改写成“何时回忆、回忆什么”的可学习机制。
* **问题与切口**: GMP 解决的是操控策略里经常被粗暴处理的记忆需求差异：有些任务近似 Markov，有些则需要单次执行内回忆，最难的还要跨 trial 累积对摩擦等隐变量的认识。作者认为简单拉长观测历史会引入分布偏移与过拟合，于是提出带记忆门的 visuomotor policy，让策略按需召回历史上下文，而不是默认始终背着长序列输入。
* **核心方法与证据**: 作者以 Transformer-based Diffusion Policy 为骨干，引入针对 history tokens 的 cross-attention、经校准的二值 memory gate，以及对历史动作注入 diffusion noise 的训练设计，目标是在保留 Markov 任务性能的同时获得 in-trial 和 cross-trial 记忆能力。证据来自自建 MemMimic 仿真与真实任务、RoboMimic Markov 基准，以及与多类 VLA 基线相关的记忆型 benchmark 对比。
* **正文要点**:
  - 论文明确区分 Markovian、in-trial memory 与 cross-trial memory 三类操控需求。
  - 作者不把长历史直接拼接进输入，而是用门控与跨注意力做选择性检索。
  - 评测既覆盖记忆密集任务，也回测 RoboMimic，以验证记忆机制不会拖垮普通任务。
* **为什么值得跟**:
  - 它给 VLA 或 visuomotor policy 的长期上下文处理提供了比“加长窗口”更可控的方案。
  - 跨 trial 记忆能力直接关系到对摩擦、稳定性等隐含物理属性的在场适应。
  - 如果门控有效，计算量与泛化性能的折中可能比全历史 Transformer 更健康。
* **风险 / 保留意见**:
  - memory gate 的校准质量可能强依赖任务分布，跨平台迁移时是否稳定还需核查。
  - 真实世界长时任务中的记忆污染、错误召回和恢复机制在摘录里证据仍有限。
* **建议先看**: 先看作者如何形式化三类记忆需求，再看 gate、cross-attention 和 history noise 各自解决了什么失败模式。实验上优先比较它在非 Markov 任务提升与 Markov 任务保性能之间的平衡。
* **关键词**: `robot memory` `diffusion policy` `gated retrieval` `non-Markovian manipulation` `Shuran Song`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 二值 memory gate 的监督或校准信号来自哪里，是否容易过拟合到训练任务的触发模式？
  - cross-trial 记忆在多次失败后如何避免错误经验被持续放大？
  - history action 加噪带来的收益，究竟来自正则化还是更贴近测试时记忆不完美的分布？
* **上传 PDF 后优先看**:
  - 方法章节中 gate、cross-attention 与 noise 设计
  - MemMimic 任务定义及 in-trial 与 cross-trial 评测
  - RoboMimic 与其他基线的性能保真和计算开销比较

### [6]. ExpertGen: Scalable Sim-to-Real Expert Policy Learning from Imperfect Behavior Priors [[HTML]](https://arxiv.org/html/2603.15956) [[PDF]](https://arxiv.org/pdf/2603.15956) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.15956`
* **Authors**: Zifan Xu, Ran Gong, Maria Vittoria Minniti, Ahmet Salih Gundogdu, Eric Rosen, Kausik Sivakumar, Riedana Yan, Zixing Wang, Di Deng, Peter Stone, Xiaohan Zhang, Karl Schmeckpeper
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把 RL 放回 VLA 数据问题的上游，用仿真里自动变强的专家来补高质量示教稀缺。
* **问题与切口**: ExpertGen 面对的是一个很现实的瓶颈：高质量机器人示教太贵，而 VLA 与行为克隆又强依赖这类数据。作者提出先用不完美行为先验初始化 diffusion policy，这些先验既可以来自人，也可以来自调用技能库的 LLM 脚本；随后在仿真中用强化学习把先验打磨成更强的专家，再把自动生成的高质量行为用于 sim-to-real 学习。它不是直接替代 BC，而是重构专家数据的生产方式。
* **核心方法与证据**: 从摘录可见，方法主线是“imperfect prior → diffusion policy 初始化 → simulation RL 提升专家性 → 规模化生成训练数据”。实验覆盖 AnyTask 的 8 个桌面操作任务与 AutoMate 的工业装配场景；前者的先验来自 LLM 调用技能库生成的脚本策略，每个任务收集 1000 条演示，后者则强调高精度插接这类接触敏感操作。证据边界上，摘录未展开更多算法细节。
* **正文要点**:
  - 论文把不完美先验视为可启动资源，而不是必须先拿到人工专家示教。
  - AnyTask 基准覆盖 lifting、pushing、stacking、pick-and-place、drawer opening 等多样操作。
  - AutoMate 场景强调工业装配与紧公差插接，能检验方法在高精度接触任务上的价值。
* **为什么值得跟**:
  - 它把 RL 与 VLA 或 BC 的关系从竞争改成协作：RL 负责造更好的专家，BC 负责稳定吸收。
  - 如果成立，机器人高质量数据的扩展路径将更接近自动化生产而非人工采集。
  - 对 sim2real 而言，这条路线尤其适合先在仿真中补齐失败恢复和稀有状态覆盖。
* **风险 / 保留意见**:
  - 整体效果会强依赖仿真保真度与任务生成器质量，sim-to-real 缺口可能仍是主风险。
  - 摘录对 RL 细节、奖励设计和真实机器人验证展开有限，复现实操难度暂时难估。
* **建议先看**: 先看作者如何定义 imperfect behavior prior，以及 RL 在其中究竟优化了哪些专家能力。随后重点核查两类基准上的 transfer 证据，尤其是高精度装配任务是否真正体现了自动专家生成的价值。
* **关键词**: `sim2real` `expert policy learning` `imperfect priors` `reinforcement learning` `diffusion policy`
* **证据来源**: arXiv HTML (Introduction, Experiments)
* **读 PDF 先核查**:
  - LLM 合成脚本先验的失败模式是什么，RL 是否主要在补状态覆盖还是补失败恢复？
  - 自动生成的专家数据与原始不完美演示混合训练时，作者如何控制分布偏差与质量权重？
  - 在 AutoMate 这类接触敏感任务上，性能提升更多来自更强专家数据还是来自 diffusion policy 初始化本身？
* **上传 PDF 后优先看**:
  - 方法章节中 prior 初始化与 RL 改进流程
  - AnyTask 的数据生成、任务分布与 sim2real 评测
  - AutoMate 装配任务上的迁移与失败案例分析

## Watchlist

### [W1]. UniT: Toward a Unified Physical Language for Human-to-Humanoid Policy Learning and World Modeling [[HTML]](https://arxiv.org/html/2604.19734) [[PDF]](https://arxiv.org/pdf/2604.19734)
* **Paper ID**: `2604.19734`
* **Authors**: Boyu Chen, Yi Chen, Lu Qiu, Jerry Bai, Yuying Ge, Yixiao Ge
* **Author Priority**: Standard
* **为什么还值得留意**: UniT 进入 shortlist，是因为它把 human-to-humanoid transfer、policy learning 和 world modeling 放进同一个“统一物理语言”叙事里，且通过视觉锚定的 latent action tokenizer 处理跨 embodiment 映射，方向很新。真实 humanoid 任务、OOD 设定和 human+robot 混合预训练也让它具备后续追踪价值。没有进入最终精选，主要因为它更偏 humanoid 迁移专线，和今天聚焦的操控型 VLA 与 world model 主线相比，通用机器人操控的外溢性还需要更多证据。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

### [W2]. Assessing VLM-Driven Semantic-Affordance Inference for Non-Humanoid Robot Morphologies [[HTML]](https://arxiv.org/html/2604.19509) [[PDF]](https://arxiv.org/pdf/2604.19509)
* **Paper ID**: `2604.19509`
* **Authors**: Jess Jones, Raul Santos-Rodriguez, Sabine Hauert
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇进入 watchlist，是因为它切到了一个常被忽略的问题：VLM 对非 humanoid 形态的 affordance 推理是否仍然成立。作者还提供了真实加合成的混合数据集与人工标注评估，作为问题定义很有价值。没有进入最终精选，是因为从摘录看它更像一篇探索性评测与数据贡献，离可执行控制、VLA 训练或世界模型方法推进还有一层距离。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. AeroBridge-TTA: Test-Time Adaptive Language-Conditioned Control for UAVs [[HTML]](https://arxiv.org/html/2604.19059) [[PDF]](https://arxiv.org/pdf/2604.19059)
* **Paper ID**: `2604.19059`
* **Authors**: Lingxue Lyu
* **Author Priority**: Standard
* **为什么还值得留意**: AeroBridge-TTA 值得保留在 watchlist，因为它把语言条件控制与 test-time adaptation 结合，明确瞄准 UAV 在真实动力学失配下的执行落差。在线 latent 适应、OOD 干扰设定和“执行不匹配而非理解失败”的 framing 都很清晰。没有进入最终精选，主要因为它更偏无人机控制栈，且摘录证据基本来自仿真，和今天以操作型 VLA 与 world model 为核心的关注面相比略偏支线。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. GenerativeMPC: VLM-RAG-guided Whole-Body MPC with Virtual Impedance for Bimanual Mobile Manipulation [[HTML]](https://arxiv.org/html/2604.19522) [[PDF]](https://arxiv.org/pdf/2604.19522)
* **Paper ID**: `2604.19522`
* **Authors**: Marcelino Julio Fernando, Miguel Altamirano Cabrera, Jeffrin Sam, Yara Mahmoud, Konstantin Gubernatorov, Dzmitry Tsetserukou
* **Author Priority**: Standard
* **为什么还值得留意**: GenerativeMPC 进入 shortlist，是因为它尝试把 VLM-RAG 的语义理解直接落到 whole-body MPC 与阻抗参数上，桥接了高层语义和低层合规控制。对于双臂移动操作，这种“语义直接调物理约束”的系统设计有现实意义。没有进入最终精选，是因为它更像层级控制系统整合，通用学习机制与大规模验证范围在摘录中还不够强，作为方向信号强于作为主线论文入选。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
