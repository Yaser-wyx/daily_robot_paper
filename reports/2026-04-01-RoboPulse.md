# RoboPulse | 2026-04-01

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 73 papers scanned · 9 shortlisted · 6 editor's picks

今天的主线很明确：VLA 与世界模型研究正在从“直接把视觉语言特征映射成动作”转向“先形成可检验的未来表征，再把它落到控制”的路线，latent foresight、simulation-in-the-loop 和 cross-modal dynamics 是最集中的三个切口。进入最终精选的六篇覆盖了端到端 VLA 架构重构、离散动作迭代修正、测试时物理仿真规划、视角泛化的一次性适配、跨模态潜动力学规划，以及 learned dynamics 加 MPC 的真实机器人闭环执行，因此组合起来能较完整反映今天的研究版图。相比之下，watchlist 几篇更像重要补充：失败推理数据、multi-view world model 和 3D 视角增强都值得继续跟，但基于当前摘录，证据密度或方向代表性还略弱于精选组。作者层面，今天没有命中你给出的核心 VIP 名单，但扩展名单里的 Jiajun Wu 出现在 IMPASTO 中，属于今天最值得优先追踪的作者线索。

## 今日信号

- 今天最值得记住的研究信号是：VLA 正在从“VLM 只做编码器”转向“VLM 负责意图或未来预测，控制器只负责把意图落地”的解耦式设计。
- 今天最值得记住的研究信号是：不少泛化问题未必首先卡在物理建模，视角变化与视觉表征失配可能是当前 VLA 更便宜、也更有效的修复入口。
- 今天最值得记住的研究信号是：world model 正在从离线表征工具变成决策时真正可调用的模块，包括测试时仿真、跨模态潜变量 rollout 和 learned dynamics 下的 MPC。

## Editor's Picks

### [1]. DIAL: Decoupling Intent and Action via Latent World Modeling for End-to-End VLA [[HTML]](https://arxiv.org/html/2603.29844) [[PDF]](https://arxiv.org/pdf/2603.29844) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.29844`
* **Authors**: Yi Chen, Yuying Ge, Hui Zhou, Mingyu Ding, Yixiao Ge, Xihui Liu
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把 end-to-end VLA 里最常见的语义退化与控制耦合问题，明确改写成“意图预测 + 反应式执行”的可训练接口。
* **问题与切口**: DIAL 针对的是当前端到端 VLA 常把预训练 VLM 当成多模态编码器、再直接回归低层动作的路线。作者认为这种做法既浪费了 VLM 的高层决策能力，也容易在训练中破坏原有语义表征。它的核心新意，是把高层 intent 与低层 action 之间插入一个可微的 latent intent bottleneck：先让 VLM 预测未来子目标的潜在视觉前瞻，再由独立的反应式策略把“当前状态和目标差距”翻译成高频控制。
* **核心方法与证据**: 方法上，DIAL 采用双系统结构：System-2 用预训练 VLM 处理语言、视觉和本体状态，不直接出动作，而是做 latent world modeling，生成未来子目标的潜在 intent；System-1 则是基于 flow matching 的 reactive policy，对照当前观测与 intent 解码动作 chunk。证据方面，HTML 摘录明确给出了 RoboCasa GR1 Tabletop 与真实 IRON-R01-1.11 机器人实验，并描述了两项类 EgoDex 真实任务、每项 120 条轨迹采集，以及混合数据预训练再微调的两阶段 protocol；但具体增益幅度仍需 PDF 进一步核查。
* **正文要点**:
  - 作者把 VLM 从“动作条件编码器”改成“未来子目标的潜在世界模型”，强调高层认知与低层执行的结构性解耦。
  - 低层控制器不是再做纯回归，而是用 flow-matching 式 reactive policy，把 intent 与当前观测的偏差转成动作 chunk。
  - 真实机器人部分至少覆盖 Pick & Place 与 Pouring 两类任务，且使用预训练加任务微调的统一训练范式。
* **为什么值得跟**:
  - 它提供了一条比传统层级规划更可微、又比直接端到端出动作更稳的 VLA 中间路线。
  - 如果 latent intent 真能稳定承载高层目标，VLM 的语义能力就更可能在机器人训练中保留下来。
  - 这类“先预测未来、再执行控制”的接口也更容易和 world model、planner 或安全约束继续拼接。
* **风险 / 保留意见**:
  - 当前摘录只说明作者在 benchmark 和真实机上有效，但没有给出失败模式分解，因此尚不清楚收益主要来自结构改动还是训练配方。
  - 真实机器人微调数据量看起来不大，跨任务、跨场景和跨机器人迁移是否稳健，仍需要看 PDF 中更完整的泛化实验。
* **建议先看**: 先抓住它的核心命题：latent intent 是否真的成为高层语义与低层动作之间的有效接口。随后重点看真实机器人实验与消融，判断收益到底来自 decoupling、本体状态融合，还是 flow-matching 控制器本身。
* **关键词**: `VLA` `latent world model` `intent-action decoupling` `flow matching` `real-world manipulation`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - latent visual foresight 在训练中是如何被约束为“可执行意图”而不是仅仅可重建的表征？
  - System-1 相比直接 action head 的优势，主要体现为稳定性、精度还是长时程可组合性？
  - 预训练 warmup 与端到端训练各自承担什么作用，若去掉其中一段性能会如何变化？
* **上传 PDF 后优先看**:
  - 方法章节里关于 dual-system 架构与 latent intent 定义的部分
  - 实验章节里真实机器人 protocol、数据组成与对比设置
  - 消融或分析章节里 decoupling、flow matching 与 latent foresight 的贡献拆分

### [2]. DFM-VLA: Iterative Action Refinement for Robot Manipulation via Discrete Flow Matching [[HTML]](https://arxiv.org/html/2603.26320) [[PDF]](https://arxiv.org/pdf/2603.26320) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.26320`
* **Authors**: Jiayi Chen, Wenxuan Song, Shuai Chen, Jingbo Wang, Zhijun Li, Haoang Li
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它直击离散 VLA 的一个真实痛点：动作 token 一旦生成就难以反悔，而这篇把“可回改”做成了显式解码机制。
* **问题与切口**: DFM-VLA 关注的是离散动作 VLA 的解码局限。无论是自回归还是离散扩散，现有方法通常都难以在后续步骤修正先前错误 token，导致早期误差被放大到整段动作序列。作者提出 discrete flow matching，把动作生成改写为对整段 token 序列的迭代更新，而不是单向吐 token。相对已有路线，它的关键新意不在换 backbone，而在把动作序列 refinement 变成建模 token-level probability velocity field 的问题。
* **核心方法与证据**: 架构上，DFM-VLA 维持类似 UniVLA 的统一离散 token 范式：文本用 Emu3 tokenizer，图像用 VQ tokenizer，连续动作经 FAST 离散后再做 BPE 压缩，并显式加入模态边界标记。方法部分给出两种 velocity-field 构造，一种是 auxiliary velocity head，一种是 embedding-guided 方案，并配合 two-stage inference 做解码分配。证据方面，HTML 摘录明确列出 CALVIN、LIBERO 与真实机器人 manipulation 实验，以及关于超参数、解码行为和效率权衡的分析问题设置，但具体改进幅度仍需看 PDF。
* **正文要点**:
  - 论文的核心主张是让整段 action tokens 在推理过程中可被反复修正，而不是一次性定稿。
  - 作者没有放弃离散 token 体系，而是在统一 token 化框架内引入 velocity-field 建模与两阶段解码。
  - 实验设计不仅比较任务成功率，还专门关注 schedule、两阶段分配、解码行为与效率取舍。
* **为什么值得跟**:
  - 它切中了离散 VLA 当前很现实的工程问题，即错误一旦进入前缀就很难挽回。
  - 如果 refinement 机制成立，离散动作建模就不再只能在自回归和离散扩散之间二选一。
  - 这类全序列可修正的解码方式，对长动作 chunk 或高维离散控制尤其有潜在价值。
* **风险 / 保留意见**:
  - 当前摘录没有给出推理开销和实时性结论，实际机器人部署时 iterative refinement 的延迟可能成为约束。
  - 收益是否稳定来自 flow matching 本身，还是部分来自更强 tokenizer/预训练初始化，仍需依赖消融确认。
* **建议先看**: 先看方法章节里两种 velocity-field 构造和 two-stage inference 的关系，搞清楚它究竟如何实现“能改前面 token”。再看分析实验，判断 refinement 带来的是真正更优的控制一致性，还是只是增加了采样预算。
* **关键词**: `VLA` `discrete flow matching` `iterative refinement` `action tokenization` `robot manipulation`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 两种 velocity-field 构造分别更适合什么场景，性能差异来自表达能力还是优化稳定性？
  - two-stage decoder 的预算分配如何影响成功率与时延，是否存在明显的收益饱和点？
  - 动作 token 被回改后，最终执行质量提升主要来自纠错、平滑性提升，还是跨模态对齐更好？
* **上传 PDF 后优先看**:
  - 方法章节里 auxiliary velocity head 与 embedding-guided 设计
  - 实验章节里 CALVIN、LIBERO 和真实机对比结果
  - 分析章节里解码行为、效率权衡与 schedule 消融

### [3]. SIMPACT: Simulation-Enabled Action Planning using Vision-Language Models [[PDF]](https://arxiv.org/pdf/2512.05955) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2512.05955`
* **Authors**: Haowen Liu, Shaoxiong Yao, Haonan Chen, Jiawei Gao, Jiayuan Mao, Jia-Bin Huang, Yilun Du
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，但要带着证据边界去读，因为从现有材料看，它最吸引人的地方是“训练外仿真增强 VLM 物理推理”，而不是已被充分证明的系统完成度。
* **问题与切口**: SIMPACT 试图解决 VLM 擅长语义常识、却缺乏物理因果理解的问题，目标场景是需要细粒度物理推理与动作规划的机器人操作。它的切口很直接：不额外训练模型，而是在测试时把物理仿真拉进决策回路。根据摘要，系统能从单帧 RGB-D 观测快速构建仿真环境，让 VLM 提议动作、观察仿真 rollout，再迭代修正计划。相较常见的端到端 policy 学习，这更像是把 VLM 变成高层 planner，再用 simulator 补齐其缺失的 dynamics grounding。
* **核心方法与证据**: 基于当前材料，方法证据只来自摘要，因此必须保守表达。可以确定的是，SIMPACT 是 simulation-enabled、test-time、training-free 的 action planning 框架，核心循环包含从单帧 RGB-D 建模环境、提出动作、执行仿真 rollout、再根据结果迭代改进。但摘要没有展开仿真构建细节、搜索或优化策略、动作空间定义，也没有给出实验设置与增益边界；因此目前更适合把它看成一个很强的方向信号，而不是已经完成证实的标准答案。
* **正文要点**:
  - 核心卖点是测试时把 physics simulation 接入 VLM 决策，而不是再训练一个新的物理世界模型。
  - 系统输入被描述为单帧 RGB-D 观测，这意味着作者强调低观测成本下的 planning 可行性。
  - 现有证据仅来自摘要，关于 simulator fidelity、rollout 开销和真实机器人落地能力都还无法定论。
* **为什么值得跟**:
  - 它代表了一条很重要的路线：用外部 simulator 补足 foundation model 的物理短板，而不是全靠数据和参数规模硬学。
  - 如果构建成本足够低，这类 test-time planning 对低数据、零训练迁移任务会很有吸引力。
  - 它也把 world model 的讨论从“模型内部学到什么”扩展到了“推理时调用什么外部物理工具”。
* **风险 / 保留意见**:
  - 没有 HTML 正文，现阶段无法判断其仿真构建是否足够快、足够稳，也无法判断是否真的优于学习式 planner。
  - 单帧 RGB-D 到可用物理场景的转换可能非常依赖工程假设，真实场景中的遮挡、材质和接触误差可能显著影响结果。
* **建议先看**: 这篇先不要急着看结果，先确认系统闭环到底如何运作：单帧观测如何变成 simulator，VLM 如何基于 rollout 改动作。等 PDF 到手后，优先核查实验是否真正证明了 training-free 物理规划的优势，而不只是展示可运行原型。
* **关键词**: `simulation-in-the-loop` `VLM planning` `RGB-D` `physical reasoning` `test-time planning`
* **证据来源**: Abstract fallback
* **读 PDF 先核查**:
  - 从单帧 RGB-D 构建物理仿真的假设有哪些，哪些对象属性是显式估计、哪些是默认设定？
  - VLM 在规划循环中扮演的是提出候选动作、评价 rollout，还是同时承担搜索策略控制？
  - 该方法的优势主要出现在哪类任务上：接触敏感操作、长时程规划，还是语义与物理共同约束的任务？
* **上传 PDF 后优先看**:
  - 系统总览章节里 test-time planning 闭环的定义
  - 方法章节里单帧 RGB-D 到 simulator 的构建流程
  - 实验章节里与 training-free 或 learning-based planner 的对比设置

### [4]. VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling [[HTML]](https://arxiv.org/html/2512.02902) [[PDF]](https://arxiv.org/pdf/2512.02902) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2512.02902`
* **Authors**: Weiqi Li, Quande Zhang, Ruifeng Zhai, Liang Lin, Guangrun Wang
* **Author Priority**: Standard
* **一句话结论**: 非常值得优先看，它提出了一个对当前 VLA 泛化讨论很有杀伤力的判断：问题可能首先不是“不会物理”，而是“视觉表征没对齐”。
* **问题与切口**: 这篇论文重审了 VLA 在新视角和视觉扰动下的失效来源。作者的核心判断是，性能骤降主要由 Spatial Modeling 的失配造成，而不是很多人直觉上更担心的 Physical Modeling 不足。基于这一点，论文没有走重训练大模型的路，而是提出一次性、轻量的视觉适配框架，用极少参数重新校准视觉 token 与 VLM 头之间的配合。相对已有路线，它最有价值的地方是把一个看似“模型能力不够”的问题，转化成了“表征对齐可修复”的问题。
* **核心方法与证据**: 方法上，作者明确反对全局微调，认为视觉扰动主要引起 embedding 空间的系统性漂移，因此只需适配视觉模块即可。具体给出两种机制：Feature Token Modulation，用全局 affine 变换调制视觉 tokens；以及进一步的 Feature Linear Adaptation，用更强但仍轻量的更新方式做校准。证据方面，HTML 摘录给出 Libero-V benchmark，覆盖新视角、光照、背景纹理和传感器噪声四类扰动，并强调每个任务只需一次人类 demonstration 做 one-shot adaptation；摘要中还直接给出了 FTM 在 viewpoint 上的显著提升与 4K 参数规模。
* **正文要点**:
  - 论文把鲁棒性问题定位为视觉表征与语言动作头之间的系统性失配，而不是整体 visuomotor 能力缺失。
  - Libero-V 将新视角、光照、纹理和传感器噪声统一纳入评测，是对分布偏移更系统的设置。
  - 方法要求每个任务只用单条人类示范做 one-shot adaptation，强调低成本部署价值。
* **为什么值得跟**:
  - 它挑战了一个常见前提：VLA 的 OOD 失效未必需要更强物理世界模型才能修复。
  - 如果轻量视觉校准已经能恢复大部分性能，那么很多现实部署问题会比想象中更便宜。
  - 这篇也为 Sim2Real 与 view generalization 提供了更精确的诊断框架，而不是笼统地谈“泛化差”。
* **风险 / 保留意见**:
  - 论文的“主要是 spatial 而非 physical”这一判断依赖其任务与扰动分布，是否能外推到更强接触动力学任务仍需谨慎。
  - one-shot adaptation 虽然很省数据，但也可能依赖 demonstration 质量与扰动类型匹配，稳定性需要更细分析。
* **建议先看**: 先看作者如何论证“问题主要出在 spatial misalignment”，这是整篇最关键的论点。再看 FTM 和 FLA 的成本与收益边界，判断它们更像通用修复模块，还是只在特定视觉偏移上有效。
* **关键词**: `VLA generalization` `viewpoint robustness` `one-shot adaptation` `feature modulation` `spatial modeling`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 作者区分 spatial modeling 与 physical modeling 的证据链是什么，是否有专门针对物理扰动的反证实验？
  - FTM 与 FLA 分别在什么扰动类型下更有效，它们是否对应不同程度的表征漂移？
  - 一次示范的适配信息主要来自新视角几何、颜色统计，还是任务级动作先验的重对齐？
* **上传 PDF 后优先看**:
  - 方法章节里 FTM 与 FLA 的具体参数化形式
  - 实验章节里 Libero-V 的扰动构造与 one-shot adaptation protocol
  - 分析章节里关于 spatial 与 physical 建模失配的归因证据

### [5]. CLaD: Planning with Grounded Foresight via Cross-Modal Latent Dynamics [[HTML]](https://arxiv.org/html/2603.29409) [[PDF]](https://arxiv.org/pdf/2603.29409) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.29409`
* **Authors**: Andrew Jeong, Jaemin Kim, Sebin Lee, Sung-Eui Yoon
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它不是泛泛谈多模态对齐，而是把“语义变化和本体运动如何在动作下共同演化”明确建模成规划对象。
* **问题与切口**: CLaD 关注长时程操作中一个常被忽略的问题：机器人运动状态变化与场景语义变化本来是被同一动作耦合驱动的，但许多方法只在语义空间或 latent 空间单独规划，没有显式约束二者的共同演化。作者提出 cross-modal latent dynamics，用非对称 cross-attention 让 kinematic transition 去查询 semantic transition，从而在潜空间里预测 grounded foresight。相较只做静态对齐或纯 latent rollout 的方法，它的创新点在于把“跨模态转移动力学”当成规划核心。
* **核心方法与证据**: 方法上，CLaD 用自监督方式学习未来潜状态，借助 EMA target encoders 预测未来 latent，并加辅助重建损失避免表征塌缩、维持与可观测状态的锚定；控制侧则接入 diffusion policy。HTML 摘录还给出了较完整实验设定：在 LIBERO-LONG 的 10 个长时程任务上验证三点假设，即跨模态动力学可带来参数效率、语义与本体必须共同 grounding、以及“运动查询语义”的非对称注意力是更优归纳偏置。作者也明确给出 0.66B 参数规模与训练配置，但具体结果幅度仍需 PDF 核实。
* **正文要点**:
  - 论文区分的不是静态多模态对齐，而是动作条件下语义状态与本体状态的共同转移。
  - 作者强调 asymmetric cross-attention 的方向性很重要，即由 kinematic transition 去查询 semantic transition。
  - 实验目标不只比性能，还专门验证参数效率、双模态 grounding 必要性与注意力归纳偏置。
* **为什么值得跟**:
  - 它把 world model 与 policy 的接口前移到了“跨模态未来状态”层面，适合长时程操作任务。
  - 如果跨模态转移动力学确实可学，规划就不必在昂贵语义生成和无约束 latent rollout 之间摇摆。
  - 相对大规模 VLA 暴力扩参，这篇更像是在探索更结构化、更参数高效的长时程规划路线。
* **风险 / 保留意见**:
  - 摘要与 HTML 强调的是机制合理性，但跨模态 latent 是否真的对应可解释的物理语义状态，还需要更多可视化或失败案例支撑。
  - 在更开放、视觉变化更剧烈的场景中，非对称注意力的归纳偏置是否仍成立，目前证据主要限于给定 benchmark。
* **建议先看**: 阅读时先围绕一个问题展开：CLaD 学到的是不是“动作下的跨模态转移规律”，而不是普通融合特征。然后重点检查三类假设验证实验，尤其是 asymmetric cross-attention 与双模态 grounding 的消融。
* **关键词**: `cross-modal latent dynamics` `grounded foresight` `long-horizon planning` `diffusion policy` `LIBERO-LONG`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - EMA 目标预测和辅助重建各自在避免表征塌缩、提升规划有效性上承担什么角色？
  - 为何必须由 kinematic transition 查询 semantic transition，反过来或对称设计为什么不如当前方案？
  - CLaD 的收益主要体现在长时程信用分配、动作连贯性，还是语义状态预测更准？
* **上传 PDF 后优先看**:
  - 方法章节里 cross-modal latent dynamics 与 asymmetric cross-attention 的设计
  - 训练章节里 EMA 目标学习与辅助重建损失的配合
  - 实验章节里 LIBERO-LONG 上的三类假设验证与消融

### [6]. IMPASTO: Integrating Model-Based Planning with Learned Dynamics Models for Robotic Oil Painting Reproduction [[VIP]] [[HTML]](https://arxiv.org/html/2603.29315) [[PDF]](https://arxiv.org/pdf/2603.29315) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.29315`
* **Authors**: Yingke Wang, Hao Li, Yifeng Zhu, Hong-Xing Yu, Ken Goldberg, Li Fei-Fei, Jiajun Wu, Yunzhu Li, Ruohan Zhang
* **Author Priority**: Extended VIP
* **一句话结论**: 值得优先看，它把 learned dynamics、MPC 与真实力控执行严密接上，虽然任务特殊，但系统完整度和研究含金量都很高。
* **问题与切口**: IMPASTO 处理的是一个很不标准、但极能检验模型与控制结合能力的任务：机器人用软毛笔和颜料复现油画。难点不只是视觉目标匹配，还包括可变形工具、力敏接触、笔触效果预测和多步 stroke planning。作者的核心切口，是只给目标油画图像序列，不依赖人工逐步示教或高保真模拟器，而是学习像素级 canvas dynamics，再用 receding-horizon MPC 去规划轨迹、力度和颜色。相比常规 manipulation 论文，它更像一套真实世界 closed-loop system 论文，而不是单一模块改进。
* **核心方法与证据**: 方法上，IMPASTO 由三层组成：学习式 pixel dynamics model 预测笔触后画布变化，基于模型的 receding-horizon optimizer 做多步规划，力敏控制器在 7-DoF 机械臂上执行。数据来源被明确描述为 robot self-play，而不是人类逐步演示。实验部分围绕四个问题展开：数据量对 dynamics 训练的影响、单笔触复现质量、闭环多步规划是否能逼近目标油画、以及像素 dynamics 的预测保真度。摘录还说明作者比较了单笔触 baselines，并强调控制 brush state 与颜料条件以减少随机性；但具体指标数值在当前材料中不完整。
* **正文要点**:
  - 这篇不是单纯做艺术机器人，而是把 learned dynamics、MPC 和 force-sensitive execution 连接成完整闭环。
  - 系统学习 solely from robot self-play，说明作者试图减少对昂贵专家示教和精确模拟器的依赖。
  - 实验明确区分了单笔触建模、数据需求和多步闭环规划三个层面，而不只展示最终作品。
* **为什么值得跟**:
  - 它证明 learned dynamics 不只适合标准抓取堆叠，也能进入接触复杂、材料变化显著的真实任务。
  - 对 world model 社区来说，这是一篇很好的“模型如何真正驱动决策与执行”的案例。
  - 作者名单里有 Jiajun Wu，且整篇体现出强烈的物理建模与系统整合取向，值得持续跟踪。
* **风险 / 保留意见**:
  - 任务很有辨识度，但也较专用，方法中的一部分收益可能依赖油画场景特有的低速闭环与视觉反馈结构。
  - 真实笔刷与颜料交互具有随机性，尽管作者控制了实验条件，模型泛化到不同耗材和环境的稳定性仍需进一步确认。
* **建议先看**: 先把它当成 learned dynamics + MPC 的真实系统论文来读，而不是“机器人画画”的展示。优先看 dynamics model 如何支撑多步规划，以及作者如何处理执行中的随机性与力控闭环。
* **关键词**: `learned dynamics` `model predictive control` `force-sensitive manipulation` `robot painting` `self-play`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)
* **读 PDF 先核查**:
  - pixel dynamics model 的预测对象和时域边界是什么，它如何支撑多步 stroke 规划而非仅单步视觉预测？
  - MPC 优化的动作变量里，轨迹、力度和颜色是联合搜索还是分阶段确定？
  - 自博弈数据覆盖的笔触分布是否足以支持风格或材质变化，还是主要服务于特定工作空间与颜料条件？
* **上传 PDF 后优先看**:
  - 方法章节里 dynamics model、MPC 与力控执行器的接口定义
  - 实验章节里单笔触复现与多步闭环规划的分离评测
  - 分析章节里数据量、随机性控制与 baseline 对比设置

## Watchlist

### [W1]. Scaling Cross-Environment Failure Reasoning Data for Vision-Language Robotic Manipulation [[HTML]](https://arxiv.org/html/2512.01946) [[PDF]](https://arxiv.org/pdf/2512.01946)
* **Paper ID**: `2512.01946`
* **Authors**: Paul Pacaud, Ricardo Garcia, Shizhe Chen, Cordelia Schmid
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇进入 shortlist，是因为它抓住了机器人系统里很现实但经常被低估的问题：失败检测、失败归因和恢复需要跨环境、跨失败模式的数据支持。摘要与 HTML 显示它不仅构建了合成失败数据，还让 VLM 生成显式 reasoning traces，并且验证了合成失败分布与真实策略失败有一定相似性。之所以没进最终精选，是因为当前贡献更偏数据与 failure reasoning 基础设施，而不是直接推进今天主线中的 VLA/world model/planning 核心算法。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)

### [W2]. Towards High-Consistency Embodied World Model with Multi-View Trajectory Videos [[HTML]](https://arxiv.org/html/2511.12882) [[PDF]](https://arxiv.org/pdf/2511.12882)
* **Paper ID**: `2511.12882`
* **Authors**: Taiyi Su, Jian Zhu, Yaxuan Li, Chong Ma, Jianjun Zhang, Zitai Huang, Hanli Wang, Yi Xu
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇值得保留在观察名单，因为它把 embodied world model 的控制信号从低层动作改写成 multi-view trajectory videos，并且试图用 object-aware priors 和新的交互一致性评测来补齐“生成好看但不可控”的缺口。方向上它很贴近今天的 world model 主题，也有比较明确的方法新意。没有进入最终精选，主要是基于当前摘录可验证的下游决策价值还不如 DIAL、CLaD 或 IMPASTO 那么清晰，且我们对其关键实验边界仍缺少足够正文证据。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. Efficient Camera Pose Augmentation for View Generalization in Robotic Policy Learning [[HTML]](https://arxiv.org/html/2603.29192) [[PDF]](https://arxiv.org/pdf/2603.29192)
* **Paper ID**: `2603.29192`
* **Authors**: Sen Wang, Huaiyi Dong, Jingyi Tian, Jiayi Li, Zhuo Yang, Tongtong Cao, Anlin Chen, Shuang Wu, Le Wang, Sanping Zhou
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇进入 shortlist，是因为 novel view generalization 的确是当前机器人策略学习的高频痛点，而它用 feed-forward 3D Gaussian Splatting 做稀疏、未标定输入下的视角增强，思路很有吸引力。它和 2512.02902 一起构成了“视觉几何修复比重训练 policy 更关键”的强信号。之所以停在 watchlist，一是当前只有接近摘要级别的 body excerpt，方法与实验证据不足；二是同一主题下，2512.02902 对问题诊断与适配收益的论证更完整、更适合进最终精选。
* **证据来源**: arXiv HTML
