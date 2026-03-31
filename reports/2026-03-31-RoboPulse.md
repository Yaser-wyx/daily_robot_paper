# RoboPulse | 2026-03-31

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 154 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线很清楚：VLA 正在从“学动作”扩展到“学世界、学奖励、学部署期适应”，而 Sim2Real 重新回到中心位置。最终精选的 6 篇之所以胜出，是因为它们分别卡住了这个闭环里的关键环节：生成式 3D 世界驱动的 RL 微调、可用于在线 RL 的触觉仿真、仅靠视频语言推理的奖励建模、真实世界标准化评测、目标状态生成式 world model，以及测试时物理记忆。相比单点模型改进，这一组论文更像是在重构 VLA 的训练基础设施与评测标尺。VIP 作者里，Jiangmiao Pang 与 Hao Su 所在工作最值得优先跟踪；在候补中，Cewu Lu 也值得继续盯住，因为他对应的是“意图而非轨迹”这条很可能继续升温的泛化路线。

## 今日信号

- 今天最值得记住的研究信号是：VLA 的关键瓶颈正从动作建模本身转向奖励、进度、记忆等更高层训练信号的可靠性。
- 今天最值得记住的趋势判断是：Sim2Real 的新焦点不再只是随机化，而是能否廉价生成、对齐并高吞吐运行训练世界与传感器世界。
- 今天最值得记住的研究信号是：真实世界评测正在从“能不能做粗粒度成功”转向“能不能稳定完成精细末端步骤”，这会重新洗牌 VLA 与 world action model 的比较方式。

## Editor's Picks

### [1]. Scaling Sim-to-Real Reinforcement Learning for Robot VLAs with Generative 3D Worlds [[PDF]](https://arxiv.org/pdf/2603.18532) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.18532`
* **Authors**: Andrew Choi, Xinjie Wang, Zhizhong Su, Wei Xu
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把 VLA 的 RL 微调重新搬回仿真，并把场景多样性而不是单纯策略结构当成核心问题。
* **问题与切口**: 这篇抓住了一个很尖锐的矛盾：真实机器人上的 RL 微调虽然绕开了 sim2real，却可能把原本泛化较强的 VLA 压缩成对少量场景过拟合的策略。作者把切口放在“可扩展的世界多样性”上，主张用生成式 3D 世界补足仿真中的场景与物体分布，让 RL 微调既保留开放世界先验，又减少人工搭建仿真内容的劳动。
* **核心方法与证据**: 从摘要能确认的方法主线是：在预训练 VLA 之上做 RL 微调，但训练环境不主要来自手工设计场景，而来自生成式 3D 世界提供的大规模多样环境。作者的核心主张有两点，一是这种做法不会明显牺牲泛化性，二是能降低构建仿真训练世界的人力成本。由于这里只有摘要回退，具体 world generation 流程、RL 目标、真实部署设置与消融证据都还需要 PDF 核查。
* **正文要点**:
  - 论文反过来检验了“真实 RL 更安全于泛化”这一常见直觉，指出它可能把广泛预训练的 VLA 变成场景特化策略。
  - 核心方案不是继续手工扩展仿真库，而是引入生成式 3D 世界来扩大场景与物体多样性。
  - 当前可见证据仅来自摘要，尚不足以判断生成世界的物理真实性与真实部署收益分别贡献了多少。
* **为什么值得跟**:
  - 它把 VLA 的 RL 扩展瓶颈从“算法行不行”转成“训练世界能否廉价扩容”。
  - 如果结论成立，sim2real 不再只是必须付出的代价，而会重新成为保留泛化能力的手段。
  - 这条路线天然连接世界生成、离线预训练与在线策略优化三条研究线。
* **风险 / 保留意见**:
  - 仅凭摘要无法确认生成世界是否覆盖了真实接触、遮挡和材质变化等关键误差源。
  - 若奖励设计或真实评测范围较窄，所谓“保留 generality”可能仍局限于相近任务分布。
* **建议先看**: 先看作者如何定义“泛化没有被 RL 微调破坏”，再看生成式 3D 世界是在扩充几何外观，还是连交互分布也一起扩充。若这两点站得住，这篇就有方法论价值。
* **关键词**: `VLA` `Sim2Real` `Reinforcement Learning` `Generative 3D Worlds` `World Generation`
* **证据来源**: Abstract fallback
* **读 PDF 先核查**:
  - 生成式 3D 世界到底参与了场景布局、物体资产，还是也影响动力学与交互随机化？
  - 作者如何证明 RL 微调后的提升不是靠记住训练场景，而是真正保留了跨场景泛化？
  - 真实部署中的收益主要来自世界多样性，还是来自 RL 本身对动作策略的再优化？
* **上传 PDF 后优先看**:
  - 方法章节里关于生成式 3D 世界构建与采样策略的部分
  - 真实机器人评测与跨场景泛化实验
  - 对人工仿真设计成本、世界多样性和 RL 收益关系的消融分析

### [2]. Tac2Real: Reliable and GPU Visuotactile Simulation for Online Reinforcement Learning and Zero-Shot Real-World Deployment [[VIP]] [[HTML]](https://arxiv.org/html/2603.28475) [[PDF]](https://arxiv.org/pdf/2603.28475) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.28475`
* **Authors**: Ningyu Yan, Shuai Wang, Xing Shen, Hui Wang, Hanqing Wang, Yang Xiang, Jiangmiao Pang
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，它把“触觉仿真够真”和“在线 RL 跑得动”这两个通常互斥的目标拉到了一起。
* **问题与切口**: Tac2Real 面向的是接触密集操作里一个很现实的卡点：视觉触觉仿真若追求物理可信度，往往难以支撑在线 RL 的吞吐；若只追求速度，又会把关键接触细节抹掉。作者的切口不是再做一个离线可视化仿真器，而是做一个能直接喂给在线 RL 的轻量级 visuotactile framework，并把零样本真实部署作为明确目标。
* **核心方法与证据**: 方法上，Tac2Real 以 PNCG-IPC 为核心，将标准 IPC 中昂贵且不易并行的 Newton 管线换成非线性共轭梯度求解，避免 Hessian 装配与分解，把计算压到梯度、对角 Hessian 与点积这类 GPU 友好操作上。实验摘录给出两类证据：在 cube indenter rotation 中，其形变更接近真实且在大旋转与滑移下比 Tacchi 稳定；在 16 张 RTX 4090、4096 环境上达到高吞吐。结论里还补上了 TacAlign，用于系统性缩小 sim2real gap，但真实部署细节仍需全文核查。
* **正文要点**:
  - PNCG-IPC 用非线性共轭梯度替代 Newton 求解，避免 Hessian 级别的代价，从设计上更适合 GPU 并行。
  - 在 cube indenter rotation 对比里，Tac2Real 比基于 penalty 的 TacSL 更物理一致，也比 Tacchi 在大形变下更稳定。
  - 框架显式支持多节点、多 GPU 高吞吐仿真，并在结论中加入 TacAlign 作为可复现的 sim2real 对齐层。
* **为什么值得跟**:
  - 如果触觉仿真终于能兼顾可信度与吞吐，接触密集 manipulation 的在线 RL 才真正有机会规模化。
  - 这篇把触觉 Sim2Real 从“传感器建模问题”推进成“训练基础设施问题”。
  - Jiangmiao Pang 参与的这条线值得持续跟踪，因为它可能外溢到更广的多模态操作学习。
* **风险 / 保留意见**:
  - 摘录里对零样本真实部署的任务覆盖与失败案例交代不够，迁移强度还不能高估。
  - 高并行结果依赖多 GPU 集群，单机成本与工程复杂度是否可接受仍需看完整实验。
* **建议先看**: 先看 PNCG-IPC 为什么能同时保住接触稳定性与 GPU 并行性，再看 TacAlign 是否真的把仿真中的触觉分布和真实传感器对齐。若这两段证据都扎实，这篇会很有工程牵引力。
* **关键词**: `Visuotactile Simulation` `Online RL` `Sim2Real` `PNCG-IPC` `Tactile Manipulation`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - PNCG-IPC 的稳定性收益主要来自求解器替换，还是来自对接触与摩擦项的具体近似处理？
  - TacAlign 到底在校准几何、光学、材料参数，还是同时覆盖结构化与随机扰动？
  - 高吞吐并行带来的收益在真实 RL 学习曲线上是否转化为更快、更稳的策略提升？
* **上传 PDF 后优先看**:
  - 求解器设计与 PNCG-IPC 细节
  - 仿真可靠性对比与大形变失败案例
  - 真实部署与 TacAlign 对齐实验

### [3]. SOLE-R1: Video-Language Reasoning as the Sole Reward for On-Robot Reinforcement Learning [[PDF]](https://arxiv.org/pdf/2603.28730) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.28730`
* **Authors**: Philip Schroeder, Thomas Weng, Karl Schmeckpeper, Eric Rosen, Stephen Hart, Ondrej Biza
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它尝试把视频语言推理模型直接做成 on-robot RL 的唯一奖励源，这个命题本身就很前沿。
* **问题与切口**: 这篇不是简单把 VLM 拿来做成败打分器，而是直面一个更难的问题：当策略在线学习时，现有强模型在部分可观测和分布偏移下会被策略钻空子，导致“看起来像成功”的奖励幻觉。SOLE-R1 的新意在于把 reward model 升级成一个专门面向机器人的视频语言推理器，只给原始视频和自然语言目标，就输出逐时刻的任务进展信号。
* **核心方法与证据**: 从摘要看，SOLE-R1 的核心机制是 per-timestep 的时空 chain-of-thought 推理：模型接收视频观测和文本目标，进行时序与空间上的显式推理，再生成可直接作为奖励使用的 dense progress estimates。训练上，作者建立了大规模视频轨迹与 reasoning synthesis pipeline，用合成推理监督来让模型学会作为 reward 使用。当前证据边界也很明确：我们能确认问题设置和方法方向，但看不到 reward 稳定性、抗 exploitation 细节和真实机器人样本效率的完整拆解。
* **正文要点**:
  - 作者明确指出现有强 VLM 作为 RL evaluator 时，会在 partial observability 和 distribution shift 下被策略利用。
  - SOLE-R1 用原始视频与语言目标做逐时刻时空推理，并输出 dense task progress 作为奖励。
  - 训练依赖大规模 trajectory 与 reasoning synthesis pipeline，但摘要尚未展示 reward 校准与真实部署边界。
* **为什么值得跟**:
  - 它把机器人 RL 的奖励建模从稀疏成功判断推进到可连续驱动学习的 reasoning signal。
  - 如果 reward 真能只靠视频和语言工作，许多任务就不必再依赖专门仪器化的奖励工程。
  - 这条路线直接连接 VLM 推理可靠性与 policy exploitability，研究价值很高。
* **风险 / 保留意见**:
  - 摘要不足以判断 chain-of-thought 是否稳定可控，还是会引入新的偏差和幻觉。
  - 若 dense progress 主要靠合成推理数据学得，分布外真实任务上的奖励错判仍可能被策略放大。
* **建议先看**: 先核查作者如何构造 reasoning supervision 和 reward calibration，再看 on-robot RL 中是否真的把外部 reward 全部拿掉。核心不是“会不会推理”，而是“奖励能否长期不被 exploit”。
* **关键词**: `Vision-Language-Action` `Reward Modeling` `Online RL` `Video-Language Reasoning` `Dense Progress`
* **证据来源**: Abstract fallback
* **读 PDF 先核查**:
  - 时空 chain-of-thought 的中间推理是否被约束为可验证结构，还是完全自由生成？
  - dense progress reward 如何避免把表面视觉变化误当成任务推进，从而被策略钻空子？
  - synthetic reasoning supervision 与真实机器人视频之间的分布差是如何缓解的？
* **上传 PDF 后优先看**:
  - reward model 训练数据与 reasoning synthesis 流程
  - on-robot RL 主实验与 reward-only 设定
  - reward exploitation、partial observability 与分布偏移分析

### [4]. ManipArena: Comprehensive Real-world Evaluation of Reasoning-Oriented Generalist Robot Manipulation [[HTML]](https://arxiv.org/html/2603.28545) [[PDF]](https://arxiv.org/pdf/2603.28545) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.28545`
* **Authors**: Yu Sun, Meng Cao, Ping Yang, Rongtao Xu, Yunxiao Yan, Runze Xu, Liang Ma, Roy Gan, Andy Zhai, Qingxuan Chen, Zunnan Xu, Hao Wang, Jincheng Yu, Lucy Liang, Qian Wang, Ivan Laptev, Ian D Reid, Xiaodan Liang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它可能是近期少数真正把 VLA 与 world action model 拉到同一真实执行标尺上的评测工作。
* **问题与切口**: ManipArena 解决的不是“再做一个模型”，而是给 VLA 和 world model 一类系统建立一个真实世界、可复现、可比较的统一评测基座。作者强调现有基准过于 simulator-centric，难以反映感知噪声、接触复杂性、硬件约束和系统时延。相比泛泛地说“真实评测更重要”，这篇进一步把 reasoning-oriented manipulation、OOD 泛化和长程执行放到一个标准化框架里，并尝试直接诊断不同范式的能力边界。
* **核心方法与证据**: 从摘录可见，ManipArena 包含 20 个任务、10,812 条专家轨迹，并支持受控 OOD 设置。作者没有停留在排行榜式比较，而是让代表性 VLA OneModel 与 world action model DreamZero 正面对照，发现二者跨任务相关性较低，暗示策略风格确实不同。方法段给出的证据尤其有价值：DreamZero 在粗粒度 pick-and-place 上非常强，但在 insert_wireline、sort_headphone 这类精细末端步骤上出现固定式卡点，说明“粗成功、细失败”是可结构化分析的。
* **正文要点**:
  - 框架覆盖 20 个任务与 10,812 条专家轨迹，突出 reasoning-oriented 操作与受控 OOD 泛化。
  - OneModel 与 DreamZero 的跨任务相关性较低，支持“VLA 与 world action model 学到的是不同策略偏好”这一判断。
  - DreamZero 在粗粒度搬运任务上很强，但在精细末端子步骤上常出现稳定卡点，暴露出细操作短板。
* **为什么值得跟**:
  - 没有像样的真实评测，VLA 与 world model 的比较就很容易被 simulator artifact 误导。
  - 这篇提供的不只是 benchmark，更是理解两类范式互补性的诊断工具。
  - 如果社区接受这套标尺，后续工作会被迫更认真地处理接触、延迟和长程失败链条。
* **风险 / 保留意见**:
  - 摘录没有完整展开硬件标准化、执行协议与评分一致性，评测公正性仍需全文确认。
  - 目前对比主要围绕一个代表性 VLA 和一个代表性 world action model，能否外推到整个范式还要谨慎。
* **建议先看**: 先读任务设计、评分规则和 OOD 设置，再看 OneModel 与 DreamZero 的失败剖面。真正有价值的不是单个分数，而是作者如何把“为什么失败”拆成可比较的子阶段。
* **关键词**: `Real-World Evaluation` `VLA` `World Action Model` `Benchmark` `Reasoning Manipulation`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)
* **读 PDF 先核查**:
  - ManipArena 如何控制不同机器人平台、感知栈和系统时延带来的额外方差？
  - 低跨任务相关性是范式层面的稳定现象，还是主要由 OneModel 与 DreamZero 的具体实现决定？
  - DreamZero 的细粒度失败究竟更多来自感知、接触控制，还是规划 horizon 不足？
* **上传 PDF 后优先看**:
  - 基准任务与评分协议章节
  - OOD 泛化与长程任务设置
  - VLA 对 world action model 的失败分析与案例拆解

### [5]. Goal-VLA: Image-Generative VLMs as Object-Centric World Models Empowering Zero-shot Robot Manipulation [[HTML]](https://arxiv.org/html/2506.23919) [[PDF]](https://arxiv.org/pdf/2506.23919) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2506.23919`
* **Authors**: Haonan Chen, Jingxiang Guo, Bangjun Wang, Tianrui Zhang, Xuchuan Huang, Boren Zheng, Yiwen Hou, Chenrui Tie, Jiajun Deng, Lin Shao
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把图像生成式 VLM 从“会描述目标”推进到“直接产出可落到 3D 操作目标的世界模型”。
* **问题与切口**: Goal-VLA 面对的是 zero-shot manipulation 的老难题：基础 VLM 有开放世界语义，但一到动作层就受限于稀缺的 instruction-vision-action 数据，泛化能力明显掉档。作者的切口很清楚，不让策略直接从当前观测跳到动作，而是先让图像生成式 VLM 作为 object-centric world model 想出“任务完成后的目标状态”，再把这个视觉目标落到可执行的 3D 物体位姿与操作。
* **核心方法与证据**: 方法是一个分层流水线。Goal State Reasoning 读入单视角 RGBD 和自然语言任务，生成 goal image、goal depth 以及初始/目标物体 mask；Spatial Grounding 再把这些视觉结果转成精确 3D 变换；Low-level Policy 负责执行。作者还加入 Reflection-through-Synthesis，用迭代式合成来修正高层推理输出。实验摘录给出的证据边界较清楚：仿真在 RLBench 8 个任务上、按 10 个随机种子和多次 trial 评估，并专门追问跨环境、跨任务、跨物体、跨 embodiment 的泛化。
* **正文要点**:
  - 输入是单视角 RGBD 与自然语言；高层模块输出 goal image、goal depth 和初始/目标物体 masks。
  - Spatial Grounding 将视觉目标转成精确 3D 变换，再交给低层策略执行具体操作。
  - 实验问题明确围绕基线对比、Reflection-through-Synthesis 的作用，以及跨环境与跨 embodiment 泛化展开。
* **为什么值得跟**:
  - 它把 world model 的价值落在“先想出目标状态，再做空间落地”这个更可解释的接口上。
  - 层次化分解减少了端到端 action 数据不足对 zero-shot 能力的直接限制。
  - object-centric 的目标表示更有机会跨场景、跨物体甚至跨机器人复用。
* **风险 / 保留意见**:
  - 目标图像生成得再合理，也可能在遮挡、多物体交互或单视角歧义下给出错误 3D 目标。
  - 当前摘录以仿真设定和方法接口为主，真实机器人泛化强度还需要完整正文验证。
* **建议先看**: 先看 Goal State Reasoning 与 Spatial Grounding 的接口定义，再核查 Reflection-through-Synthesis 到底是在修正语义错误、几何错误，还是两者都修。若接口清晰，这篇很适合作为 world-model 式 manipulation pipeline 参考。
* **关键词**: `Zero-shot Manipulation` `Generative VLM` `Object-Centric World Model` `Spatial Grounding` `Goal State Reasoning`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 生成式 VLM 输出的 goal image 与 goal depth 是一次生成还是迭代优化，失败模式分别是什么？
  - Spatial Grounding 如何处理遮挡、同类物体混淆与单视角带来的 3D 不适定性？
  - Reflection-through-Synthesis 的收益主要来自更准的目标状态，还是来自更利于位姿估计的视觉结果？
* **上传 PDF 后优先看**:
  - 系统总览与模块接口定义章节
  - Reflection-through-Synthesis 的消融实验
  - 跨环境、跨物体、跨 embodiment 的泛化评测

### [6]. PhysMem: Scaling Test-time Physical Memory for Robot Manipulation [[VIP]] [[HTML]](https://arxiv.org/html/2602.20323) [[PDF]](https://arxiv.org/pdf/2602.20323) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2602.20323`
* **Authors**: Haoyang Li, Yang You, Hao Su, Leonidas Guibas
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，它把 VLM 物理常识不足的问题转成可在部署期持续积累的“验证过的物理记忆”。
* **问题与切口**: PhysMem 处理的是一个很具体但经常被忽视的缺口：VLM 也许知道摩擦、稳定性、动量这些概念，却很难判断“这颗球在这张桌面上会滚多远”“这块石头在这里稳不稳”。作者没有去更新模型参数，而是提出一个测试时记忆框架，让机器人在执行过程中记录经验、提出物理假设、做定向验证，再把通过验证的原则供后续规划检索使用。
* **核心方法与证据**: 方法核心是 scientific memory loop。系统把物理操作建模为 options 框架下的序列决策，高层 VLM policy 在决策时显式条件于当前从记忆中检索出的 active principles，再选 temporally-extended options。更关键的是，记忆不是原始经验堆积，而是“先提出假设、再实验验证、最后晋升原则”。实验上，作者除真实机器人外，还用 MuJoCo 的 Reflect-VLM brick insertion 基准做 500+ episodes、跨多种 VLM、按 2 到 8 块砖逐级加难，给出了比较可扩展的受控评测。
* **正文要点**:
  - 框架核心是 scientific memory loop：从经验生成假设、做定向验证、只把通过验证的原则写入可检索记忆。
  - 高层 VLM policy 在决策时显式条件于当前 active principles，再选择 temporally-extended options。
  - 除真实机器人外，作者还在 MuJoCo brick insertion 上做 500+ episodes、跨多 VLM、按砖块数分难度的控制实验。
* **为什么值得跟**:
  - 它提供了不用微调大模型参数、却能在测试时获得物理适应性的可行路线。
  - 把经验提升为“原则”而不是直接记住轨迹，更有机会跨任务复用。
  - 这套架构天然能接入触觉、音频和主动感知，向多模态物理推理扩展。
* **风险 / 保留意见**:
  - 原则抽取与验证流程如果成本过高，部署期学习收益可能会被交互预算吞掉。
  - 记忆里形成的“原则”是否真正可迁移，仍取决于归纳粒度与检索机制是否合适。
* **建议先看**: 先看 scientific memory loop 的晋升机制，再看 brick insertion 难度升级是否真的测到了原则迁移而非经验缓存。对研究者来说，关键不是记忆库本身，而是“验证后再使用”的机制是否成立。
* **关键词**: `Test-time Adaptation` `Physical Memory` `VLM Planner` `Robot Manipulation` `Scientific Memory Loop`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 候选 physical principles 是由 VLM 自由生成，还是受模板或程序结构约束？
  - targeted experiments 如何平衡验证成本与信息增益，是否会出现探索过度？
  - active principles 的检索失败或相互冲突时，系统如何影响 option selection？
* **上传 PDF 后优先看**:
  - scientific memory loop 与 memory schema 设计
  - brick insertion benchmark 的难度设置与跨模型实验
  - 真实机器人案例与多模态扩展讨论

## Watchlist

### [W1]. Mimic Intent, Not Just Trajectories [[VIP]] [[HTML]](https://arxiv.org/html/2602.08602) [[PDF]](https://arxiv.org/pdf/2602.08602)
* **Paper ID**: `2602.08602`
* **Authors**: Renming Huang, Chendong Zeng, Wenjing Tang, Jintian Cai, Cewu Lu, Panpan Cai
* **Author Priority**: Core VIP
* **为什么还值得留意**: 这篇进入 shortlist 的理由很充分：它直接攻击 VLA/IL 泛化差的根因，提出把行为意图和执行细节解耦，且 Cewu Lu 在今天的 VIP 名单里值得继续跟踪。之所以没进最终精选，是因为它更偏 imitation learning 表征路线，而今天主线更集中在 RL、Sim2Real、world model 与部署期适应；另外从现有摘录看，机制亮点主要停留在频域 action tokenization 与 benchmark 表现，意图表征是否真正形成可迁移因果结构，还需要 PDF 细看。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. ViPRA: Video Prediction for Robot Actions [[VIP]] [[PDF]](https://arxiv.org/pdf/2511.07732)
* **Paper ID**: `2511.07732`
* **Authors**: Sandeep Routray, Hengkai Pan, Unnat Jain, Shikhar Bahl, Deepak Pathak
* **Author Priority**: Extended VIP
* **为什么还值得留意**: ViPRA 值得放进观察名单，因为它把 actionless video 通过 latent actions 和 video prediction 接到机器人连续控制上，和 world model 式预训练高度相关，且 Deepak Pathak 是必须跟的扩展作者。没有进入最终精选，主要因为当前只有摘要回退，可见证据不足；同时它更像一种通用预训练到控制的桥接框架，和今天更聚焦的 VLA-RL、真实评测、部署期物理适应相比，落点稍偏上游表示学习。
* **证据来源**: Abstract fallback

### [W3]. ProgressVLA: Progress-Guided Diffusion Policy for Vision-Language Robotic Manipulation [[HTML]](https://arxiv.org/html/2603.27670) [[PDF]](https://arxiv.org/pdf/2603.27670)
* **Paper ID**: `2603.27670`
* **Authors**: Hongyu Yan, Qiwei Li, Jiaolong Yang, Yadong Mu
* **Author Priority**: Standard
* **为什么还值得留意**: ProgressVLA 入围 shortlist，是因为它把 task progress 作为显式可学习信号引入 diffusion VLA，对长程 manipulation 的停止判定和子目标推进都很关键。没有进最终精选，主要是因为今天已经有 SOLE-R1 这类更激进的 reward/progress 方案，以及 ManipArena 这类更基础设施级的评测工作；从现有摘录看，它更像一条扎实但相对增量的控制改良线，完整说服力还要等全文里的失败模式和泛化拆解。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. Uni-World VLA: Interleaved World Modeling and Planning for Autonomous Driving [[HTML]](https://arxiv.org/html/2603.27287) [[PDF]](https://arxiv.org/pdf/2603.27287)
* **Paper ID**: `2603.27287`
* **Authors**: Qiqi Liu, Huan Xu, Jingyu Li, Bin Sun, Zhihui Hao, Dangen She, Xiatian Zhu, Li Zhang
* **Author Priority**: Standard
* **为什么还值得留意**: Uni-World VLA 进入 shortlist 的原因在于它很好地体现了“交错式世界建模与规划”这条 World Action Model 主线，不再先开环想象整段未来、再独立规划，而是逐步交替预测与决策。之所以没有进入最终精选，是因为它的主战场是自动驾驶而非机器人操作，和今天的 manipulation 主线有明显域差；因此它更适合作为方法信号跟踪，而不是今天最终精选里的核心代表。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
