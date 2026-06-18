# RoboPulse | 2026-06-18

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 81 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线非常集中：VLA 评测、动作分块的闭环化、sim-to-real residual RL，以及面向机器人操作的多视角 world model 都在试图把“看起来会做”推进到“可评估、可纠错、可迁移”。最终精选保留了两类最值得跟踪的工作：一类把 world/action model 直接用于策略评估或执行时选择，另一类把人类视频、对象中心状态、几何一致性等外部结构注入 VLA 数据和控制闭环。VIP 作者里，Sergey Levine 参与的 SC3-Eval 和 Pieter Abbeel 参与的 Do as I Do 最值得优先读，因为它们分别卡在机器人基础模型的可扩展评测和灵巧手数据规模化两个关键瓶颈上。PAIWorld 与 Cosmos 3 虽然一个有 HTML、一个只有摘要回退，但共同提示大模型化 world model 正在从视频生成走向物理 AI 的统一底座。

## 今日信号

- VLA 研究的评测范式正在从真实机器人全量 rollout 转向 action-conditioned world model，但可信评估的核心难点变成多视角一致性、分布外行为检测和长时误差控制。
- sim-to-real 的新信号不是单纯缩小视觉域差距，而是通过对象中心 6-DoF 状态、动作残差、几何记忆等可跨域接口，把需要迁移的部分压缩到更稳定的表示空间。
- 动作分块和 world/action model 正在融合：策略不再只是一次性吐出 chunk，而是在测试时用 latent rollout、视频 rollout 或 reward/value 预测来重新选择、终止或修正执行。

## Historical Rediscovery

- **Paper**: Uncertainty Quantification for Flow-Based Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2606.18043) [[PDF]](https://arxiv.org/pdf/2606.18043)
  - **Paper ID**: `2606.18043`
  - **来源日期**: 2026-06-17
  - **当时可能被低估的信号**: 当时可能低估了 VFD 的 epistemic uncertainty 估计和 SAVE 主动微调组合；历史备注里还明确提到相比 uncertainty baseline 减少数据收集量的信号。
  - **为什么现在值得再看**: 现在值得再看，因为 VLA 从 benchmark 走向真实部署时，不确定性估计、主动数据采集和安全筛选会变成核心能力；它和你的 VLA、真实部署评测、RL/VLA 后训练数据效率兴趣高度相关。
  - **建议动作**: 加入精读
  - **关键词**: `VLA` `uncertainty` `active fine-tuning` `deployment reliability` `data efficiency`
- **Paper**: ACE-Ego-0: Unifying Egocentric Human and Robotic Data for VLA Pretraining [[HTML]](https://arxiv.org/html/2606.17200) [[PDF]](https://arxiv.org/pdf/2606.17200)
  - **Paper ID**: `2606.17200`
  - **来源日期**: 2026-06-17
  - **当时可能被低估的信号**: 当时可能低估了 camera-space actions、cross-embodiment morphology tokens、time-aligned action chunking 这些接口设计；这些不是普通数据拼接，而是在定义异构动作数据如何进入 VLA 预训练。
  - **为什么现在值得再看**: 现在值得再看，因为 VLA 的瓶颈越来越像是统一动作表示和跨来源数据预训练，而不是单一 benchmark 上调参；它和你的 VLA、长时程操作、人类视频到机器人学习方向直接相关。
  - **建议动作**: 加入精读
  - **关键词**: `VLA pretraining` `egocentric video` `cross-embodiment` `action representation` `robot data`
- **Paper**: EgoInfinity: A Web-Scale 4D Hand-Object Interaction Data Engine for Any-View Robot Retargeting and Video-to-Action Robot Learning [[HTML]](https://arxiv.org/html/2606.17385) [[PDF]](https://arxiv.org/pdf/2606.17385)
  - **Paper ID**: `2606.17385`
  - **来源日期**: 2026-06-17
  - **当时可能被低估的信号**: 当时可能低估了“纯 RGB 互联网视频到可 retarget robot data”的路线价值；即使机器人闭环证据仍需核查，4D hand-object interaction data engine 本身就是重要基础设施信号。
  - **为什么现在值得再看**: 现在值得再看，因为 video-to-action、human demonstration retargeting 和大规模操作数据生成正是 VLA/World Action Model 的上游供给问题；它也可能服务于 Sim2Real 数据扩展。
  - **建议动作**: 快速浏览
  - **关键词**: `video-to-action` `retargeting` `4D hand-object interaction` `VLA data` `Sim2Real`
- **Paper**: RopeDreamer: A Kinematic Recurrent State Space Model for Dynamics of Flexible Deformable Linear Objects [[HTML]](https://arxiv.org/html/2604.28161) [[PDF]](https://arxiv.org/pdf/2604.28161)
  - **Paper ID**: `2604.28161`
  - **来源日期**: 2026-05-01
  - **当时可能被低估的信号**: 当时可能因为任务边界窄而低估了 kinematic recurrent state space model 对长时可控预测的价值；历史备注里的 quaternion kinematic chain 和拓扑保持是明确的技术信号。
  - **为什么现在值得再看**: 现在值得再看，因为 World Model/World Action Model 要进入真实操作，必须处理非刚体、长时状态演化和物理一致性；这篇可作为 deformable manipulation world model 的参考分支。
  - **建议动作**: 快速浏览
  - **关键词**: `world model` `deformable object` `long-horizon prediction` `state space model` `manipulation`
- **Paper**: Visual-Tactile Peg-in-Hole Assembly Learning from Peg-out-of-Hole Disassembly [[HTML]](https://arxiv.org/html/2604.20712) [[PDF]](https://arxiv.org/pdf/2604.20712)
  - **Paper ID**: `2604.20712`
  - **来源日期**: 2026-04-23
  - **当时可能被低估的信号**: 当时可能低估了从 peg-out-of-hole disassembly 反向辅助 peg-in-hole assembly 的数据与任务设计信号；这类反向任务构造可能比表面上更有外溢性。
  - **为什么现在值得再看**: 现在值得再看，因为 VLA 和 WAM 在接触丰富操作中仍需要可靠的低层技能、触觉反馈和 Sim2Real 闭环；它可补足视觉语言策略在精密装配上的落地短板。
  - **建议动作**: 继续跟踪
  - **关键词**: `Sim2Real` `visual-tactile` `contact-rich manipulation` `POMDP` `assembly`

## Editor's Picks

### [1]. SC3-Eval: Evaluating Robot Foundation Models via Self-Consistent Video Generation [[VIP]] [[HTML]](https://arxiv.org/html/2606.18610) [[PDF]](https://arxiv.org/pdf/2606.18610) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.18610`
* **Authors**: Wei-Cheng Tseng, Gashon Hussein, Yuzhu Dong, Allen Z. Ren, Lucy X. Shi, XuDong Wang, Sergey Levine, Zhaoshuo Li, Jinwei Gu, Florian Shkurti, Ming-Yu Liu, Quan Vuong
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看：SC3-Eval 把视频 world model 从“生成未来画面”推进到“可扩展评测真实 VLA 策略”，且由 Sergey Levine 参与，方向命中今天主线。
* **关键词**: `VLA evaluation` `action-conditioned world model` `self-consistency` `uncertainty termination` `Sergey Levine`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

通用机器人操作策略的真实评测成本很高：每个策略都需要机器人时间、环境复位和人工监督，跨任务、跨场景评测更难扩展。action-conditioned video world model 提供了一条替代路线，即给定初始多视角观测和动作序列，在模型中模拟 rollout，再用模拟结果估计策略表现。但这条路线有三个硬问题：自回归误差会累积，多摄像头视角必须彼此一致，评测器还要面对策略产生的分布外行为。SC3-Eval 的重要性在于，它不是把视频模型当作漂亮的可视化工具，而是把它改造成机器人基础模型的评测器。

#### ⚙️ 核心方法

当前摘录可以确认，SC3-Eval 的核心是把一个预训练的统一动力学模型改造成策略评估器，并利用该模型内部的 forward/inverse dynamics 结构约束 rollout。论文强调 inverse dynamics objective 能把生成轨迹锚定在物理上更合理的动作流形上，从而缓解自回归漂移；同一套 forward-inverse consistency 信号还被用作 per-chunk uncertainty，用来在模型认为 rollout 已经偏离可信区域时提前终止。它和传统 model-based RL 中的 ensemble uncertainty、MOReL、MOPO 有相似动机，都是识别 off-manifold 查询，但区别是 SC3-Eval 不训练额外 ensemble，也不是把不确定性用于离线 RL 奖励惩罚，而是在策略评测阶段阻止不可靠 rollout 继续污染分数。摘要还提到 self-consistent video generation 和多视角观测一致性，但摘录没有完整展开三种 self-consistency 的所有实现细节，因此应把它理解为一个利用模型内部一致性信号增强评测可靠性的 recipe。

#### 📊 实验与结果

实验部分把真实机器人 rollout 视为 gold standard，并将 SC3-Eval 放在三类替代评测方案中定位：physics simulator 如 SIMPLER、RoboLab，real-to-sim 如 PolaRiS，以及 video-model-based evaluator。结论摘录显示，SC3-Eval 在七个真实世界 VLA 策略上评测，并与三个强视频模型评测 baseline 对比；还声称能泛化到 held-out task。HTML 摘录中 Pearson correlation 与 MMRV 的具体数值缺失，不能引用数字，只能保守表述为作者报告在闭环相关性和排序类指标上优于强基线。证据边界在于，摘录没有给出任务组成、策略列表、显著性或失败样例细节。

#### ⚠️ 风险 / 保留意见

- HTML 摘录缺失关键数值，无法判断相关性提升的幅度和统计稳定性。
- 评测器本身依赖预训练视频/动力学模型，若真实策略进入模型未覆盖的接触模式，提前终止可能过度保守或误判。
- 视频生成评测仍可能捕捉视觉合理性而非真实接触动力学，真实机器人对照细节需要重点核查。

#### 💭 结论与启发

这篇对后续系统设计的启发是：world model 做机器人评测时，不应只追求更长、更清晰的视频，而要显式输出“我是否还可信”的信号。forward-inverse consistency 是一个很实用的接口，因为它把动作可解释性、分布外检测和 rollout 终止统一到同一模型内部。复现时我会优先关注它如何把评测分数从视频 rollout 转换成策略级排序，以及 early termination 对低质量策略和高质量策略是否有不同偏置。

#### 🔎 读 PDF 先核查

- forward-inverse consistency 的不确定性阈值如何设定，是否对不同任务、不同 VLA 策略需要重新校准？
- SC3-Eval 的评测分数如何从多视角视频 rollout 聚合到策略级 performance，是否依赖任务特定成功检测器？
- held-out task 泛化主要来自预训练视频 foundation model，还是来自 inverse dynamics/self-consistency 适配过程？

#### 📌 上传 PDF 后优先看

- 方法章节中的 self-consistency 设计与 forward/inverse dynamics 训练目标
- 实验章节中的七个真实 VLA 策略、三个视频评测 baseline 和 held-out task 设置
- 消融与失败案例，尤其是 early termination、多视角一致性和 inverse objective 的单独贡献

### [2]. Do as I Do: Dexterous Manipulation Data from Everyday Human Videos [[VIP]] [[HTML]](https://arxiv.org/html/2606.19333) [[PDF]](https://arxiv.org/pdf/2606.19333) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.19333`
* **Authors**: Bhawna Paliwal, Haritheja Etukuru, William Liang, Pieter Abbeel, Nur Muhammad Mahi Shafiullah, Jitendra Malik
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看：Do as I Do 正面处理“从日常人类视频生成灵巧手操作数据”，对 dexterous manipulation 数据规模化有直接启发。
* **关键词**: `dexterous manipulation` `human videos` `retargeting` `SAM 3D` `Pieter Abbeel`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

灵巧手机器人最缺的是可规模化、可迁移的操作数据。真实遥操作受限于操作者技能、设备透明性和成本，仿真探索又受限于环境、奖励和接触建模复杂度。人类日常视频天然包含大量手物交互，但单目 RGB 视频没有机器人动作标签，且人手到多指机械手存在明显 embodiment gap，因此过去很难直接作为机器人操作数据。Do as I Do 的动机是把“看人做”变成“机器人可执行轨迹”，让互联网、第一视角和外部视角视频都成为灵巧手学习的数据来源。Pieter Abbeel 参与也使它在机器人学习数据路线中值得优先跟踪。

#### ⚙️ 核心方法

方法由两段组成：先从单目 RGB 视频重建并跟踪 3D 手和物体，再把重建结果 retarget 到多指机器人手，生成动态上可行、可在真实世界执行的轨迹。手部跟踪部分直接利用现有模型 HawoR，因为作者认为它对 noisy internet videos 有足够鲁棒性；物体部分则是难点，尤其是开放集合刚体在手部遮挡下容易丢失 pose lock、漂移或无法重新捕获。为此论文开发了基于 SAM 3D 的物体跟踪方法，利用带遮挡训练的 3D generative foundation model 来提升手物交互场景中的目标保持能力。摘录还显示，重建后的 3D 手、物体和相机会被组合成一致的近场表示，再进入机器人 embodiment 的 retargeting 流程。当前摘录没有完整给出 retargeting 的优化目标、动力学约束或控制接口细节，因此对“动态可行”的具体实现需要上传 PDF 后核查。

#### 📊 实验与结果

实验覆盖两个层面。第一，手物重建在标准 benchmark 上评估：DexYCB 的 160 个标注视频和 HOI4D 的 12 个标注视频，并通过提供 ground-truth hands 来隔离物体重建与跟踪性能；对比对象包括 joint hand-object reconstruction 方法和 object tracker。第二，为贴近日常视频分布，作者额外收集了 150 个来自网络、egocentric datasets 和生成视频的样本；由于没有 ground-truth pose，采用每个视频 3 名志愿者的人类偏好比较 SAM 3D tracking 与当前 SOTA。结论称方法适用于 egocentric、exocentric 和在线视频源，但摘录没有给出真实机器人成功率或偏好比例，需保守看待部署证据。

#### ⚠️ 风险 / 保留意见

- 方法明确假设刚体物体，软物体、铰接物体和可变形接触可能不在能力范围内。
- 单目视频的尺度、相机运动和遮挡会影响重建质量，retargeting 可能放大这些误差。
- 人类偏好评估能说明视觉跟踪质量，但不等价于机器人执行成功率。

#### 💭 结论与启发

这篇最值得借鉴的是数据管线视角：与其等待大规模灵巧手遥操作数据，不如先把人类视频转成可筛选、可 retarget、可验证的轨迹候选。对后续选题来说，关键不是单点重建精度，而是如何让重建误差不破坏接触时序和抓取意图。若要复现，我会把它拆成三步验证：物体 pose 稳定性、retarget 后关节/接触可行性、以及真实机器人闭环执行是否能承受前两步的残差。

#### 🔎 读 PDF 先核查

- SAM 3D-based object tracking 在手部严重遮挡和物体离手再接触时如何重新获得 pose lock？
- retargeting 阶段如何处理人手接触点与机器人多指手接触能力不匹配的问题？
- 生成的轨迹是直接用于执行、用于 imitation learning，还是作为可筛选的数据扩增源，三者证据分别如何？

#### 📌 上传 PDF 后优先看

- 重建方法章节，尤其是 HawoR、SAM 3D tracking 与近场一致表示的接口
- retargeting 章节中的动力学可行性、接触约束和机器人手参数化
- 真实机器人或下游学习实验，以及 DexYCB/HOI4D/150 in-the-wild 视频的定量与偏好评估

### [3]. Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement [[HTML]](https://arxiv.org/html/2606.18953) [[PDF]](https://arxiv.org/pdf/2606.18953) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.18953`
* **Authors**: Kinam Kim, Namiko Saito, Heecheol Kim, Katsushi Ikeuchi, Jaegul Choo, Yasuyuki Matsushita
* **Author Priority**: Standard
* **一句话结论**: 值得优先看：它把 residual RL、对象中心状态和零样本 sim-to-real 结合，用很工程化的接口增强冻结 VLA。
* **关键词**: `residual RL` `zero-shot sim-to-real` `VLA enhancement` `object-centric observation` `6-DoF pose`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

VLA 模型依赖大规模预训练和机器人示范，已经能覆盖多样操作任务，但 imitation learning 在精细接触中容易因小误差累积而失败。直接用 RL 改进现代 VLA 又不简单，因为不少 VLA 使用 diffusion 或 flow matching 生成动作，标准策略梯度不容易穿过迭代生成过程。Residual RL 是自然折中：冻结原 VLA，只训练一个轻量纠错策略。但已有路线存在 sim-to-real 两难：特权状态方法部署时要蒸馏，图像方法受视觉域差距影响，真实 RL 又昂贵且风险高。本文的关键问题是：纯仿真训练的 residual policy 能否零样本提升真实 VLA？

#### ⚙️ 核心方法

框架分三阶段。第一，通过 teleoperation replay 为真实机器人 VLA 构建仿真 counterpart，使冻结 VLA 能在仿真中产生基础动作。第二，在仿真里训练一个 object-centric residual policy，它不直接依赖渲染图像，而是读取 6-DoF object poses、机器人 proprioception 和 base VLA action 等对象中心观测。第三，部署到真实机器人时，VLA 与 residual 都冻结，最终动作为基础动作加上残差；摘录明确说明位置和夹爪用加法组合，旋转用 quaternion multiplication。这个设计的核心新意是把 residual 的输入接口选成仿真和真实都能恢复的对象中心表示，从而避开图像域差距，也不需要把特权状态策略再蒸馏成可部署策略。论文还提到 residual-corrected policy 可用于重新训练 base VLA，让单任务 residual 行为进一步转化为多任务 VLA 自改进数据，但摘录没有展开训练细节。

#### 📊 实验与结果

实验围绕五个问题展开：真实机器人零样本提升、观测与鲁棒性设计、residual 何时介入、以及 residual-corrected rollout 是否能 bootstrap VLA。主结果在五个任务上评估，作者称仿真中 residual 改善所有任务，真实机器人上 sim-trained residual 零样本迁移到全部五个任务，并提高平均成功率；但 HTML 摘录中的具体成功率数值为空，不能引用。论文还声称在另一种 VLA 架构上也有提升，说明 object-centric observation interface 不绑定单一 VLA。证据边界是任务难度、物体 pose 获取方式、失败统计和 residual 干预分布都需要看完整实验。

#### ⚠️ 风险 / 保留意见

- 强依赖真实部署时可获得可靠 6-DoF object poses，感知失败会直接影响 residual。
- 对象中心接口适合刚体操作，但对 deformable object、遮挡严重或多物体接触可能不足。
- 零样本 sim-to-real 的说服力取决于仿真 counterpart 与真实 VLA rollout 的匹配程度。

#### 💭 结论与启发

这篇给我的最大启发是：增强 VLA 不一定要改大模型本体，可以在动作输出之后加一个跨域稳定的小接口。对象中心 residual 很适合做工程复现，因为它把难问题分解为 VLA 负责语义和粗动作，RL 负责局部纠错与恢复。后续如果做 sim-to-real VLA，我会优先比较三种接口：图像 residual、特权状态 residual、对象中心 residual，并重点检查对象 pose 噪声下的退化曲线。

#### 🔎 读 PDF 先核查

- object-centric residual 的输入中 base VLA action 占多大作用，去掉动作条件后是否还能稳定提升？
- 真实机器人上的 6-DoF object pose 是如何获得的，是否使用了人工标定或任务特定检测器？
- residual-corrected rollout 用于 retrain base VLA 时，如何避免把 per-task residual 的窄行为过拟合进多任务模型？

#### 📌 上传 PDF 后优先看

- 三阶段方法图与 object-centric observation 定义
- 五个真实机器人任务的主结果、跨 VLA 架构实验和具体成功率表
- 消融实验：观测设计、pose 噪声、residual 干预时刻和 VLA self-improvement

### [4]. DREAM-Chunk: Reactive Action Chunking with Latent World Model [[HTML]](https://arxiv.org/html/2606.18589) [[PDF]](https://arxiv.org/pdf/2606.18589) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.18589`
* **Authors**: Wenxi Chen, Kaidi Zhang, Chi Lin, Zhiyuan Zhang, Yu She, Yuejiang Liu, Raymond A. Yeh, Shaoshuai Mou, Yan Gu
* **Author Priority**: Standard
* **一句话结论**: 值得优先看：DREAM-Chunk 针对 VLA 常用 action chunking 的开环脆弱性，提出了无需微调策略的测试时 world-model 选择机制。
* **关键词**: `action chunking` `latent world model` `test-time scaling` `VLA execution` `reactive control`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

action chunking 已经成为很多 VLA 和机器人策略的常用接口：低频模型推理输出一段动作，高频控制器执行，从而降低推理压力并提升动作平滑性。但 chunk 一旦提交，执行过程通常偏开环，遇到随机动力学、硬件误差、部分可观测状态或外界扰动时很容易偏离。World model 能预测未来状态，但如果把它和 VLA 重训练在一起，成本和复杂度都会提高。DREAM-Chunk 的动机是做一种 test-time scaling：不改已有 chunking policy，只在测试时多采样、多想象、多选择，让动作分块获得反应性。

#### ⚙️ 核心方法

当前摘录能确认，DREAM-Chunk 在测试时从 chunking policy 采样多个候选 action chunks，用轻量 latent world model 对每个候选的未来 latent state 进行 rollout，然后根据“dreamed”状态与实际观测 rollout 的匹配程度，从更合适的 chunk 中选择动作。它的关键不是生成可视化视频，而是在 latent 空间中覆盖多个可能的随机未来，并在长 horizon chunk 执行中持续进行在线校正。方法不要求额外 policy fine-tuning，因此适合作为已有 VLA/action-chunking 策略的外接模块。摘录还提到其收益依赖 demonstration 中存在 corrective behaviors，以及辅助 world model 的 latent representation 设计会影响性能。由于 HTML 的 Method 部分摘录主要重复摘要，尚不能确认 latent matching 的具体距离函数、chunk 重采样频率、候选数量调度或 world model 训练损失。

#### 📊 实验与结果

实验分为受控仿真和真实硬件。仿真使用 Kinetix，一个覆盖 locomotion、manipulation 和 Atari-like control 的 2D agentic benchmark，并按照 RTC evaluation setting，从 RL expert demonstrations 训练 flow-matching action-chunking imitation policy。作者重点研究动作噪声下样本数、示范中的纠错行为以及 latent world model 设计对效果的影响。真实机器人部分用于检验硬件执行误差、部分可观测性和外部扰动下的鲁棒性。结论称在 Kinetix 中收益随 stochasticity 和 sample count 增加而增强，但摘录未提供具体数字或任务成功率，需保守表达。

#### ⚠️ 风险 / 保留意见

- 测试时多采样会增加推理计算量，真实机器人闭环频率是否足够需要核查。
- 方法依赖示范数据中存在纠错行为，纯专家顺滑轨迹可能不给 world model 提供可选择的恢复模式。
- latent matching 的可靠性取决于表示是否捕捉任务相关状态，而非视觉或动力学无关变化。

#### 💭 结论与启发

这篇适合作为 action chunking 系统的实用增强思路：保留 chunk 的低频推理优势，同时用 world model 在执行中恢复部分闭环性。对复现来说，它比端到端训练大 VLA 更轻，因为主要改测试时控制逻辑。后续我会重点比较 DREAM-Chunk 与简单 receding-horizon replan、ensemble chunk sampling、以及 value-based chunk selection 的差异，判断 latent world model 是否真的提供了额外信息。

#### 🔎 读 PDF 先核查

- dreamed latent state 与 observed rollout 的匹配具体如何计算，是否需要任务特定 reward 或 success signal？
- 候选 chunk 数量增加带来的收益何时饱和，真实硬件延迟是否限制 sample count？
- 为什么 corrective behaviors 是有效条件，它们在训练数据中如何被定义、检测或控制？

#### 📌 上传 PDF 后优先看

- 方法章节中的 latent world model、candidate chunk sampling 和 latent matching 细节
- Kinetix 噪声实验中的 sample count、stochasticity 和 corrective behavior 消融
- 真实机器人扰动实验，尤其是执行频率、延迟和与普通 chunking policy 的对比

### [5]. PAIWorld: A 3D-Consistent World Foundation Model for Robotic Manipulation [[HTML]](https://arxiv.org/html/2606.18375) [[PDF]](https://arxiv.org/pdf/2606.18375) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.18375`
* **Authors**: Yuhang Huang, Xuan Lv, Junyan Xu, Zhiyuan Yu, Jiazhao Zhang, Ruizhen Hu, Wancheng Feng, Shilong Zou, Hewen Xiao, Ziqiao Zhou, Kaiyun Huang, Zhiyu Peng, Juzhan Xu, Hang Zhao, Chenyang Zhu, Renjiao Yi, Yifei Huang, Douhui Wu, Yan Zhang, Kexu Cheng, Chunhe Song, Yunzhi Xue, Xiuhong Zhang, Leitao Guo, Yunji Chen, Bin Wu, Haibin Yu, Kai Xu
* **Author Priority**: Standard
* **一句话结论**: 值得优先看：PAIWorld 把机器人 world foundation model 的关键矛盾明确推到多视角 3D 一致性，并给出大规模几何增强方案。
* **关键词**: `world foundation model` `multi-view generation` `3D consistency` `Geo-RoPE` `robotic manipulation`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

当前 world foundation model 在视频生成和物理场景模拟上进展很快，但机器人操作天然不是单视角问题。真实系统通常同时依赖 egocentric、eye-to-hand、wrist-mounted 等多摄像头视角，不同视角提供全局场景、局部接触和手眼细节。如果 multi-view world model 只是拼接 view tokens，而缺少几何推理，就会出现跨视角物体漂移、深度不一致、纹理错位等问题，这些错误会进一步污染下游规划和控制。PAIWorld 的价值在于把“生成好看视频”转成“生成几何一致的多视角机器人未来”，这正是 manipulation world model 走向实用评估和规划的前提。

#### ⚙️ 核心方法

PAIWorld 的核心判断是，多视角 3D 一致性需要两个互补条件：视角之间必须有显式信息通路，且训练目标必须给出几何一致性的信号。为此，论文在预训练 backbone 中插入 Geometry-Aware Cross-View Attention，让不同 camera view 能互相通信；同时使用 Geometric Rotary Position Embedding，也就是 Geo-RoPE，把几何位置信息注入注意力过程，使 cross-view attention 不只是全局 token 混合，而是受空间关系约束。摘录还提到 REPA projection heads 随机初始化，并称这些模块被插入 Cosmos-Predict2.5 这样的 flow-matching DiT latent world model。模型用 Cosmos-Reason1 作为 text embedder，提供物理 grounded 的文本条件。当前摘录可以确认其目标覆盖 action-conditioned video generation 和 text-conditioned multi-view generation，但下游规划或策略控制接口没有在摘录中充分展开。

#### 📊 实验与结果

实验评估两个生成范式：action-conditioned video generation 和 text-conditioned multi-view generation，并在三个 benchmark 上与 SOTA baseline 做定量比较。实现细节里有较明确规模信息：full model 约 14B 参数，训练数据约 2.5M 多视角机器人操作视频 clips，来源包括 AgiBot-World 35%、RoboMIND 20%、Galaxea 15%、RoboTwin 15% 和 RoboCOIN 15%。这些数据提供多摄像头视频流，并伴随文本描述或动作相关信息。结论称 Geometry-Aware Cross-View Attention、Geo-RoPE 和几何一致性训练信号共同改善 3D-consistent multi-view generation。摘录未给出具体指标数值、benchmark 名称细节或真实机器人闭环验证，因此现阶段主要把它视作强 world model 基座工作。

#### ⚠️ 风险 / 保留意见

- 14B 级模型和 2.5M clips 数据规模带来很高复现门槛，普通实验室难以完整复刻。
- 摘录主要证明生成一致性，尚不能确认对真实策略评估、规划或控制的直接收益。
- 多源机器人数据的相机标定、动作格式和文本质量差异可能影响几何监督的一致性。

#### 💭 结论与启发

PAIWorld 提醒我，多视角机器人 world model 的瓶颈不是简单扩大视频模型，而是让视角通信被几何约束。对后续阅读，我会把它和 WEAVER、Mem-World、SC3-Eval 放在一起比较：一个强调几何 cross-view attention，一个强调效率/奖励预测，一个强调记忆持久性，一个强调评测一致性。系统设计上，如果目标是 manipulation 评测或数据生成，几何编码和相机标定质量可能比单纯视频分辨率更关键。

#### 🔎 读 PDF 先核查

- Geometry-Aware Cross-View Attention 是否显式使用相机内外参，还是通过 learned geometric embedding 间接建模？
- Geo-RoPE 与普通 RoPE 或 view-token concatenation 的消融差距主要体现在深度、纹理还是动作一致性？
- action-conditioned generation 是否被用于策略评估或规划，还是主要停留在视频预测指标？

#### 📌 上传 PDF 后优先看

- 架构章节中的 Geometry-Aware Cross-View Attention 与 Geo-RoPE 公式/接口
- 数据与训练章节，尤其是 2.5M clips 多源数据的相机、动作和文本对齐方式
- 实验章节中的三类 benchmark、3D consistency 指标、消融和跨视角失败案例

### [6]. Cosmos 3: Omnimodal World Models for Physical AI [[PDF]](https://arxiv.org/pdf/2606.02800) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.02800`
* **Authors**: NVIDIA: Aditi, Niket Agarwal, Arslan Ali, Jon Allen, Martin Antolini, Adeline Aubame, Alisson Azzolini, Junjie Bai, Maciej Bala, Yogesh Balaji, Josh Bapst, Aarti Basant, Mukesh Beladiya, Mohammad Qazim Bhat, Zaid Pervaiz Bhat, Dan Blick, Vanni Brighella, Han Cai, Tiffany Cai, Eric Cameracci, Jiaxin Cao, Yulong Cao, Mark Carlson, Carlos Casanova, Ting-Yun Chang, Yan Chang, Yu-Wei Chao, Prithvijit Chattopadhyay, Roshan Chaudhari, Chieh-Yun Chen, Junyu Chen, Ke Chen, Qizhi Chen, Wenkai Chen, Xiaotong Chen, Yu Chen, An-Chieh Cheng, Click Cheng, Xiu Chia, Jeana Choi, Chaeyeon Chung, Wenyan Cong, Yin Cui, Magdalena Dadela, Nalin Dadhich, Wenliang Dai, Joyjit Daw, Alperen Degirmenci, Rodrigo Vieira Del Monte, Robert Denomme, Sameer Dharur, Marco Di Lucca, Ke Ding, Wenhao Ding, Yifan Ding, Yuzhu Dong, Nicole Drumheller, Yilun Du, Aigul Dzhumamuratova, Aleksandr Efitorov, Hamid Eghbalzadeh, Naomi Eigbe, Imad El Hanafi, Hassan Eslami, Benedikt Falk, Jiaojiao Fan, Jim Fan, Amol Fasale, Sergiy Fefilatyev, Liang Feng, Francesco Ferroni, Sanja Fidler, Xiao Fu, Vikram Fugro, Prashant Gaikwad, TJ Galda, Katelyn Gao, Yihuai Gao, Wenhang Ge, Sreyan Ghosh, Arushi Goel, Vivek Goel, Akash Gokul, Rama Govindaraju, Jinwei Gu, Miguel Guerrero, Elfie Guo, Aryaman Gupta, Siddharth Gururani, Hugo Hadfield, Song Han, Ankur Handa, Zekun Hao, Mohammad Harrim, Ali Hassani, Nathan Hayes-Roth, Yufan He, Chris Helvig, Cyrus Hogg
* **Author Priority**: Standard
* **一句话结论**: 值得优先看但需等全文：Cosmos 3 只有摘要回退信息，仍因其 omnimodal world/action model 定位对 Physical AI 底座方向很关键。
* **关键词**: `omnimodal world model` `Physical AI` `world-action model` `mixture-of-transformers` `Cosmos 3`
* **证据来源**: Abstract fallback

#### 📖 背景与动机

机器人和 Physical AI 需要同时处理语言、图像、视频、音频和动作序列。传统路线往往把 VLM、视频生成器、world simulator、policy model 或 world-action model 分开训练，再在系统层面拼接，这会带来接口复杂、表示不统一和跨模态迁移受限的问题。Cosmos 3 的摘要把目标定得很大：用统一的 omnimodal world model 同时支持理解与生成，试图把多种 embodied agent 所需能力放进同一类 scalable backbone。由于目前只有摘要回退，不能确认具体架构细节和机器人实验设置，但它代表工业界把 world model 大规模统一化的方向。

#### ⚙️ 核心方法

当前摘录只能确认 Cosmos 3 是一族 omnimodal world models，设计为在 unified mixture-of-transformers architecture 中联合处理并生成 language、image、video、audio 和 action sequences。它支持灵活的 input-output configuration，因此摘要声称可以把 vision-language model、video generator、world simulator 和 world-action model 都纳入同一框架。这里最值得注意的是 action sequence 被列为一等模态，说明 Cosmos 3 不只是文本到图像/视频模型，而是面向 Physical AI 的生成与控制底座。摘要还提到 post-trained Cosmos 3 models 在 Artificial Analysis 的开源 Text-to-Image 和 Image-to-Video 排名，以及 RoboArena 的 policy model 排名中表现领先；但由于没有 HTML 方法摘录，不能描述 mixture-of-transformers 的路由机制、训练阶段、action tokenization 或机器人 policy head。

#### 📊 实验与结果

摘要称 Cosmos 3 在多样 understanding 和 generation tasks 上达到新的 state-of-the-art，并在发布时被 Artificial Analysis 评为最佳开源 Text-to-Image 与 Image-to-Video 模型、被 RoboArena 评为最佳 policy model。由于提供内容只有摘要回退，不能引用具体 benchmark、分数、模型尺寸、数据规模或机器人任务成功率。对本文的实验判断应非常保守：它至少表明作者把 omnimodal world model 同时放到生成质量和策略能力两个评估维度中，但是否能支撑真实机器人 long-horizon manipulation、sim-to-real 或闭环规划，需要等完整 PDF 核查。

#### ⚠️ 风险 / 保留意见

- 只有摘要回退，无法核查架构、训练数据、评估协议和机器人部署细节。
- omnimodal 统一模型可能在接口上很强，但不同模态任务的能力是否互相促进需要实验证明。
- 工业级大模型通常复现门槛高，开源权重、数据透明度和动作接口开放程度决定研究可用性。

#### 💭 结论与启发

Cosmos 3 对我更像方向锚点而不是可立即复现的论文：它提示 world model、VLM、policy model 和 action model 正在收敛到统一架构。后续阅读时我会特别关注它如何表示 action，以及 action 与 video/audio/language 是否共享 token 空间或通过专门专家路由。若它的 policy capability 真的来自同一 omnimodal backbone，而不是额外后训练堆叠，就会对 VLA 系统架构产生很大影响。

#### 🔎 读 PDF 先核查

- action sequences 在 Cosmos 3 中如何 tokenized，是否与语言/视频 token 共享表示或使用专门专家？
- RoboArena policy model 排名对应哪些机器人任务、输入输出接口和真实/仿真评测协议？
- omnimodal 训练是否证明语言、视频、音频和动作之间存在正迁移，还是主要依赖后训练分任务优化？

#### 📌 上传 PDF 后优先看

- 模型架构章节中的 mixture-of-transformers、模态路由和 action 表示
- 训练与 post-training 章节，尤其是多模态数据配比和 Physical AI 数据来源
- 评估章节中的 RoboArena policy 结果、world-action generation 任务和真实机器人证据

## Watchlist

### [W1]. Qwen-RobotManip Technical Report: Alignment Unlocks Scale for Robotic Manipulation Foundation Models [[PDF]](https://arxiv.org/pdf/2606.17846)
* **Paper ID**: `2606.17846`
* **Authors**: Haoqi Yuan, Zhixuan Liang, Anzhe Chen, Ye Wang, Haoyang Li, Pei Lin, Yiyang Huang, Zixing Lei, Tong Zhang, Jiazhao Zhang, Jie Zhang, Jingyang Fan, Gengze Zhou, Qihang Peng, Chenxu Lv, Xiaoyue Chen, An Yang, Fei Huang, Junyang Lin, Dayiheng Liu, Jingren Zhou, Chenfei Wu, Xiong-Hui Chen
* **Author Priority**: Standard
* **为什么还值得留意**: Qwen-RobotManip 命中 VLA foundation model scale-up 与多源机器人数据对齐主题，摘要提出 representation、motion、behavior 三个维度的统一 alignment，方向重要。它没有进入最终精选，主要因为当前只有摘要回退，无法核查具体模型接口、数据规模、对齐损失和真实机器人评估证据；相比 SC3-Eval、Residual RL 和 DREAM-Chunk，它对今天“评测/闭环/Sim2Real”的可操作细节暂时不足。
* **证据来源**: Abstract fallback

### [W2]. WEAVER, Better, Faster, Longer: An Effective World Model for Robotic Manipulation [[HTML]](https://arxiv.org/html/2606.13672) [[PDF]](https://arxiv.org/pdf/2606.13672)
* **Paper ID**: `2606.13672`
* **Authors**: Arnav Kumar Jain, Yilin Wu, Jesse Farebrother, Gokul Swamy, Andrea Bajcsy
* **Author Priority**: Standard
* **为什么还值得留意**: WEAVER 很接近最终精选：它明确把机器人 world model 的 fidelity、consistency、efficiency 三个 desiderata 放在一起，并覆盖 policy evaluation、policy improvement 和 planning。没有进入最终精选，是因为今天已选 SC3-Eval、DREAM-Chunk、PAIWorld 和 Cosmos 3 分别覆盖评测、chunk 执行、多视角几何和大模型底座；WEAVER 更适合作为 world model 评估与规划方向的重点后续阅读，而非本轮主线中的唯一代表。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)

### [W3]. Mem-World: Memory-Augmented Action-Conditioned World Models for Persistent Robot Manipulation [[HTML]](https://arxiv.org/html/2606.18960) [[PDF]](https://arxiv.org/pdf/2606.18960)
* **Paper ID**: `2606.18960`
* **Authors**: Zirui Zheng, Jiaqian Yu, Xiongfeng Peng, jun shi, Mingyi Li, Chao Zhang, Weiming Li, Dong Wang, Huchuan Lu, Xu Jia
* **Author Priority**: Standard
* **为什么还值得留意**: Mem-World 关注长期操作中的记忆持久性，尤其是 wrist camera 快速运动和末端遮挡导致 world model 遗忘或幻觉的问题，和机器人真实部署非常相关。它没有进入最终精选，是因为方法更聚焦在 memory retrieval 与 persistent rollout，相比 PAIWorld 的 3D consistency 和 SC3-Eval 的策略评测，本轮主线优先级略低；但若后续研究长时 manipulation world model，它应与 PAIWorld/WEAVER 一起读。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. Motion-Focused Latent Action Enables Cross-Embodiment VLA Training from Human EgoVideos [[HTML]](https://arxiv.org/html/2606.18955) [[PDF]](https://arxiv.org/pdf/2606.18955)
* **Paper ID**: `2606.18955`
* **Authors**: Runze Xu, Yiluo Zhang, Jian Wang, Yu Wang, Jincheng Yu
* **Author Priority**: Standard
* **为什么还值得留意**: Motion-Focused Latent Action 试图从无动作标签的人类 ego videos 中抽取跨 embodiment 的离散动作先验，和 Do as I Do 同属“人类视频转机器人数据”路线。它没有进入最终精选，是因为当前摘录显示的方法偏 latent action pretraining 与 downstream fine-tuning，真实可执行轨迹和灵巧操作证据不如 Do as I Do 直接；但其 Hybrid Disentangled VQ-VAE 和 motion/background 解耦值得列入后续数据预训练 watchlist。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
