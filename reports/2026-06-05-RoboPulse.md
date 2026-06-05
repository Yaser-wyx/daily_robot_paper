# RoboPulse | 2026-06-05

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 82 papers scanned · 10 shortlisted · 5 editor's picks

今天的主线非常集中：VLA 后训练、闭环世界模型评估、世界-语言-动作统一建模，以及把推理、affordance、速度或医疗数据先验接入机器人策略。最终精选的五篇都直接触到 VLA 可部署性的关键瓶颈：失败样本如何利用、闭环 rollout 如何替代昂贵真机测试、世界模型如何服务动作生成、VLM 语义空间如何落到可执行 affordance，以及测试时计算如何提升长程鲁棒性。它们未必都有 VIP 作者背书，但议题密度高，和 VLA/RL/world model 的后续系统设计关系更直接。VIP 作者里今天最值得优先跟踪的是 LadderMan 的 Pieter Abbeel 与 Yue Wang，以及 Open-H-Embodiment 的 Chelsea Finn；前者偏真实 humanoid sim2real 与全身控制，后者偏医疗机器人 foundation dataset 和 VLA 迁移。

## 今日信号

- VLA 研究正在从“直接模仿动作”转向“后训练、偏好、affordance、latent reasoning 等中间机制”，目标是把失败模式显式纳入优化。
- World model / WAM 不再只是开放环视频预测，而开始服务闭环 policy-in-the-loop 评估、动作生成加速和测试时 scaling。
- Sim2Real 的重点正在从单纯 domain randomization 扩展到数据可执行性、感知几何校正、真实部署闭环验证和安全/速度可控。

## Historical Rediscovery

- **Paper**: See Less, Specify More: Visual Evidence Budgets for Generalizable VLAs [[HTML]](https://arxiv.org/html/2606.02735) [[PDF]](https://arxiv.org/pdf/2606.02735)
  - **Paper ID**: `2606.02735`
  - **来源日期**: 2026-06-03
  - **当时可能被低估的信号**: “Specify More”用更细的轨迹/子任务语言降低执行歧义，“See Less”用 visual evidence budget 抑制无关视觉干扰；这不是泛泛的 VLA 改进，而是直接针对泛化失败时的输入与指令接口。
  - **为什么现在值得再看**: 现在值得再看，因为 VLA 真实部署越来越依赖可控的语言粒度、视觉证据选择和跨任务泛化；它可作为 VLA policy 接口设计和 World Action Model 输入约束的参考。
  - **建议动作**: 加入精读
  - **关键词**: `VLA` `generalization` `visual evidence budget` `instruction interface` `OpenPI`
- **Paper**: AirDreamer: Generalist Drone Navigation with World Models [[HTML]](https://arxiv.org/html/2606.03252) [[PDF]](https://arxiv.org/pdf/2606.03252)
  - **Paper ID**: `2606.03252`
  - **来源日期**: 2026-06-03
  - **当时可能被低估的信号**: 历史记录里明确提到 Dreamer V3 world model 与 RL policy 用于未知杂乱环境导航，并报告仿真到真实 drone transfer；这类真实迁移信号容易被“非操作任务”标签低估。
  - **为什么现在值得再看**: 值得今天再看，因为它能补 World Model 在真实闭环控制中的证据，尤其是从仿真学习到真实平台执行的链路；对 Sim2Real 和长时程导航式 World Action Model 有参考价值。
  - **建议动作**: 加入精读
  - **关键词**: `World Model` `Dreamer V3` `RL` `Sim2Real` `real drone transfer`
- **Paper**: AsyncShield: A Plug-and-Play Edge Adapter for Asynchronous Cloud-based VLA Navigation [[HTML]](https://arxiv.org/html/2604.24086) [[PDF]](https://arxiv.org/pdf/2604.24086)
  - **Paper ID**: `2604.24086`
  - **来源日期**: 2026-04-28
  - **当时可能被低估的信号**: 历史 note 里提到它把云端 VLA 导航延迟拆成几何映射、约束优化和 RL 适配三部分；这个组合说明它不是单纯系统工程，而是在处理 VLA action 滞后下的闭环安全问题。
  - **为什么现在值得再看**: 现在值得再看，因为真实部署评测不能只看离线成功率，还要看网络延迟、异步动作和边缘安全适配；它与 VLA 实机部署、RL 适配和 closed-loop action reliability 强相关。
  - **建议动作**: 快速浏览
  - **关键词**: `VLA deployment` `asynchronous control` `edge adapter` `RL adaptation` `navigation`
- **Paper**: RopeDreamer: A Kinematic Recurrent State Space Model for Dynamics of Flexible Deformable Linear Objects [[HTML]](https://arxiv.org/html/2604.28161) [[PDF]](https://arxiv.org/pdf/2604.28161)
  - **Paper ID**: `2604.28161`
  - **来源日期**: 2026-05-01
  - **当时可能被低估的信号**: 历史 note 里强调 recurrent state space model、quaternion kinematic chain 和长时预测中的拓扑保持；这说明它关注的不是短视感知，而是物理一致的长期 dynamics。
  - **为什么现在值得再看**: 值得再看，因为 World Model 和 World Action Model 若要进入 contact-rich manipulation，必须处理可变形物体的稳定预测与状态表示；这篇可作为窄域但扎实的物理 world model 参照。
  - **建议动作**: 快速浏览
  - **关键词**: `World Model` `deformable object` `long-horizon prediction` `RSSM` `robot manipulation`
- **Paper**: BifrostUMI: Bridging Robot-Free Demonstrations and Humanoid Whole-Body Manipulation [[HTML]](https://arxiv.org/html/2605.03452) [[PDF]](https://arxiv.org/pdf/2605.03452)
  - **Paper ID**: `2605.03452`
  - **来源日期**: 2026-05-06
  - **当时可能被低估的信号**: 历史 note 里提到便携 VR、稀疏关键点、wrist-view 视觉和 whole-body coordination 的联动；这些是把 robot-free demonstrations 转成 humanoid 操作数据时非常具体的可复用信号。
  - **为什么现在值得再看**: 现在值得再看，因为真实部署和长时程操作越来越依赖低成本、高覆盖的数据采集；它与 humanoid VLA、跨 embodiment 数据、Sim2Real 训练管线都有直接关系。
  - **建议动作**: 继续跟踪
  - **关键词**: `humanoid manipulation` `robot-free demonstrations` `whole-body coordination` `VLA data` `Sim2Real`

## Editor's Picks

### [1]. FlowPRO: Reward-Free Reinforced Fine-Tuning of Flow-Matching VLAs via Proximalized Preference Optimization [[HTML]](https://arxiv.org/html/2606.05468) [[PDF]](https://arxiv.org/pdf/2606.05468) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.05468`
* **Authors**: Yihao Wu, He Zhang, Junbo Tan, Xueqian Wang, Zhengyou Zhang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为 FlowPRO 直接瞄准 flow-matching VLA 的真实机器人后训练瓶颈，用 reward-free preference optimization 处理失败信号。
* **关键词**: `VLA 后训练` `flow matching` `preference optimization` `reward-free RL` `real robot bimanual`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

这篇的核心问题是：VLA 已经能把视觉、语言和低层动作接在一起，但把一个 SFT 得到的模型后训练到真实机器人可部署水平仍然很难。摘要和引言明确指出，SFT 与 DAgger 类方法虽然能利用人类示范或纠正，但对失败信号的利用偏间接；reward-based RL 又依赖真实世界奖励设计和稳定 critic，成本与风险都高。对 flow-matching VLA 来说，这个问题更尖锐，因为动作头不是普通离散语言策略，直接套 RLHF/DPO 的假设可能导致 likelihood underdetermination 或 reward hacking 式退化。FlowPRO 的动机因此很清楚：在没有显式 reward model、也不依赖在线 RL 的情况下，从真实机器人干预数据里构造偏好监督，让模型专门修复困难失败模式。

#### ⚙️ 核心方法

FlowPRO 是一个 reward-free offline reinforced fine-tuning 框架，核心算法是 RPRO，即 Robotic Flow-matching Proximalized Preference Optimization。当前摘录可以确认它从 RLHF、DPO、PRO 的理论线索出发，把偏好优化改写到 flow-matching action head 上：一方面保留 preferred 与 dispreferred action pair 的 contrastive optimizer，用相对偏好推动策略远离失败动作；另一方面加入显式 proximal regularizer，避免普通 Flow-DPO 中只约束相对似然而导致正负样本似然一起下降的病理。方法部分还提到 teleoperated intervention-and-rollback 数据收集范式和数据处理管线，这意味着偏好对不是抽象标注，而是来自真实执行中的失败、人工介入、回滚和修正。实验问题里出现 state-wise Smooth Interpolation 与 trajectory-wise preference contrast 的比较，说明它不是只比较整条轨迹优劣，而试图把纠偏信号更细粒度地对齐到状态层面。相对已有后训练路线的新意在于：既绕开显式 reward/critic，又针对 flow-matching VLA 的动作分布形式设计了 proximalized preference loss。

#### 📊 实验与结果

摘录显示实验覆盖四个轴：整体性能、数据构造、loss 设计和组件归因。硬件是 Dobot XTrainer bimanual platform，任务包括 Pack、Cap、USB、Case 四个长程双臂任务，分别涉及亚厘米插入、空中协调、亚毫米精度和可变形长程打包等困难因素。训练流程是先用 SFT 得到 base policy 和 reference policy，再进行多轮 RPRO fine-tuning。评估为了控制训练随机性，每个表项来自 3 个独立训练 seed，并报告跨 seed 的均值和标准差。结论声称 FlowPRO 在四个长程真实机器人任务和两个 π-family base policies 上取得最高 success rate 与最短 completion time，并优于四个代表性 baseline 及 loss 组合。摘录没有给出具体表格数字，因此只能把“最高”和“最短”作为作者结论引用，不能进一步比较幅度。

#### ⚠️ 风险 / 保留意见

- 真实任务数量为四个，虽然难度高，但跨平台、跨对象和跨语言泛化证据仍需看完整实验。
- 偏好数据依赖 teleoperation intervention-and-rollback，部署成本和标注一致性可能是复现风险。
- RPRO 对 flow-matching action head 定制较强，迁移到 diffusion、autoregressive 或离散动作 VLA 时未必直接成立。

#### 💭 结论与启发

这篇对后续选题的启发在于，VLA 后训练可以绕开显式奖励，但不能绕开“失败信号如何结构化”的问题。值得重点学习它如何把真实机器人干预转成 state-wise preference pair，以及 proximal regularizer 如何在 flow-matching 目标里防止偏好优化漂移。如果要复现，优先不应追求完整双臂硬件，而应先在现有 VLA action head 上实现 Flow-DPO/RPRO 对照，验证是否真的能消除负样本偏好优化带来的分布坍缩。

#### 🔎 读 PDF 先核查

- RPRO 的 proximal regularizer 在 flow-matching loss 中具体约束的是路径、噪声时间步还是动作分布似然？
- state-wise Smooth Interpolation 如何从 intervention-and-rollback 轨迹中构造 preferred/dispreferred action pair？
- FlowPRO 对两个 π-family base policies 的提升是否来自同一类失败模式，还是任务相关性很强？

#### 📌 上传 PDF 后优先看

- RPRO loss 推导与 Flow-DPO 对比章节
- teleoperated intervention-and-rollback 数据构造流程
- 四个真实双臂任务的 baseline、ablation 和 failure mode 分析

### [2]. PiL-World: A Chunk-Wise World Model for VLA Policy-in-the-Loop Evaluation [[HTML]](https://arxiv.org/html/2606.05773) [[PDF]](https://arxiv.org/pdf/2606.05773) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.05773`
* **Authors**: Chong Ma, Taiyi Su, Jian Zhu, Jianjun Zhang, Zitai Huang, Yi Xu, Hanli Wang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为 PiL-World 把 world model 从开放环预测推进到 VLA policy-in-the-loop 闭环评估。
* **关键词**: `policy-in-the-loop` `world model` `closed-loop evaluation` `VLA benchmark` `dual-arm manipulation`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

这篇抓住了 VLA 评估中的一个现实落差：真实机器人部署时，策略不是一次性输出完整动作序列，而是在观察、执行 action chunk、再观察的闭环里不断改变状态分布。许多机器人 world model 或视频预测方法可以沿着预收集轨迹做开放环预测，但这不足以评价一个 VLA 在自己动作造成的新状态下会如何继续决策。真实机器人闭环测试又受限于硬件安全、场景重置和吞吐量，难以大规模筛选策略。PiL-World 的动机因此是构造一个能和 VLA 策略交替运行的 chunk-wise world model，用生成的未来观察喂回策略，让 imagined rollout 更接近真实部署的反馈环。对 VLA、world model 和 sim2real 方向来说，这类评估工具可能比单纯提升视频预测指标更有系统价值。

#### ⚙️ 核心方法

当前摘录只能确认 PiL-World 的总体机制，方法细节不足以展开具体架构。它被定义为 policy-in-the-loop VLA evaluation 的 chunk-wise world model：输入当前 observation 和 VLA policy 预测出的 action chunk，生成与该动作执行一致的 multi-view future observations，并且这些生成观察要匹配 VLA 下一次推理所需的图像输入格式。随后系统交替执行两步：VLA 根据当前或生成观察输出下一段动作，PiL-World 根据该动作段预测执行后的多视角观察。这样多个 action chunks 被组合成闭环 imagined rollout。相对开放环 world model，关键接口变化是“动作来自被评估策略本身”，而不是预录数据；“下一步输入来自模型生成结果”，而不是 ground-truth trajectory。摘录未给出具体视频生成 backbone、状态表示、训练损失或多视角一致性约束，因此这些只能作为待核查内容，不能假设它使用某种扩散、Transformer 或显式动力学模块。

#### 📊 实验与结果

摘录显示 PiL-World 在三个真实 dual-arm manipulation tasks 上做验证，并声称能提升 policy-in-the-loop evaluation 的有效性。引言与结论强调，它生成每个 chunk 结束后的 final observation，再作为下一次 policy query 的输入，因此实验应重点关注 imagined closed-loop rollout 是否能区分不同 VLA 策略、是否与真实机器人结果相关，以及是否优于开放环预测式评估。当前 HTML 摘录的 Experiments 部分基本回退到摘要内容，没有提供 benchmark 名称、任务细节、量化指标、对比方法或具体数字。因此结果只能保守表述为：作者报告了三项真实双臂任务上的闭环评估改进，但改进幅度和统计证据需要打开 PDF 后核查。

#### ⚠️ 风险 / 保留意见

- HTML 摘录缺少具体模型结构和量化结果，当前只能确认研究目标与闭环接口。
- 闭环 imagined rollout 容易累积视觉生成误差，生成观察是否会误导 VLA 是核心风险。
- 如果只在三个真实双臂任务上验证，评估相关性对更多任务和策略族的泛化仍不确定。

#### 💭 结论与启发

这篇的价值不在于又做一个视频预测模型，而在于把 world model 的评估对象从 dataset trajectory 改成 VLA 策略本身。后续如果做 VLA benchmark，可以借鉴它的接口设计：评估器必须吃 policy action chunk，并返回 policy 下一步真实会使用的观测模态。复现时应优先验证 imagined rollout 与真实 rollout 的排名相关性，而不是只看生成图像质量；否则 world model 可能看起来逼真，却不能帮助选择更可靠的机器人策略。

#### 🔎 读 PDF 先核查

- PiL-World 的训练目标如何保证生成的 multi-view observation 与 VLA action chunk 因果一致？
- 作者如何量化 imagined closed-loop evaluation 与真实机器人成功率之间的相关性？
- 生成误差跨多个 action chunks 累积时，PiL-World 是否有重置、校正或不确定性估计机制？

#### 📌 上传 PDF 后优先看

- world model 架构与训练损失章节
- policy-in-the-loop rollout 协议与接口定义
- 真实双臂任务上的评估相关性和开放环 baseline 对比

### [3]. World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis [[HTML]](https://arxiv.org/html/2606.05979) [[PDF]](https://arxiv.org/pdf/2606.05979) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.05979`
* **Authors**: Yi Yang, Zhihong Liu, Siqi Kou, Yiyang Chen, Yanzhe Hu, Jianbo Zhou, Boyuan Zhao, Zhijie Wei, Xiao Xia, Xueqi Li, Pengfei Liu, Zhijie Deng
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为 WLA 试图把 world modeling、language reasoning 和 action synthesis 合成一个 embodied foundation model 接口。
* **关键词**: `world-language-action` `WAM` `VLA` `autoregressive transformer` `test-time scaling`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

WLA 的出发点是当前 WAM 与 VLA 各有短板。WAM 通过预测未来视觉状态学习物理动态，能从大规模 egocentric videos 中受益，并为动作预测提供未来状态先验；但如果只预测低层视觉细节，模型会被像素级变化牵制，语义推理和长程外推能力不足。VLA 则擅长语言指令和任务语义，但很多方法仍直接把观察与语言映射到动作，世界动态建模不够显式。论文提出的关键判断是，机器人的“下一状态”不应只是图像，也应包含高层 textual intention 或 subtask 表征。这样，语义层能提供紧凑、可泛化的规划线索，物理层提供细粒度动态约束，两者共同服务动作生成。这个问题对长程任务尤其重要，因为长程控制既需要知道下一步应该做什么，也需要知道物体和机器人状态会怎么变。

#### ⚙️ 核心方法

WLA 被定义为 world-language-action model，输入 textual instructions、images 和 robot states，联合预测 textual subtasks、subgoal images 和 robot actions。核心是 autoregressive Transformer backbone，而不是 WAM 中常见的 bidirectional diffusion Transformer。模型把下一状态拆成两类互补输出：语义层的 textual intention，以及细粒度 physical dynamics。实现上，WLA-0 使用 RynnBrain-2B 作为 backbone，SANA-600M 作为 World Expert，flow-matching head 作为 Action Expert，总参数量 3.4B；每个 expert 有 28 层，meta-queries 数量为 64。World Expert 通过 world modeling objective 监督物理动态，Action Expert 利用这些动态先验降低 state-action correlation 的建模难度。meta-queries 是重要接口：它们让 world prediction 隐式影响 action generation，因此推理时可以关闭显式 world prediction 以维持效率，也可以在测试时打开 world prediction 做 test-time scaling。相对已有 VLA/WAM，新意在于不是把语言推理和世界预测作为两个外部模块串联，而是在同一 AR embodied backbone 中共同训练并通过 meta-query 影响动作头。

#### 📊 实验与结果

摘录给出较多实现和部分实验设置信息。WLA-0 在 LIBERO 上 action chunk size 为 8，在其他设置中为 32。RoboTwin 2.0 是包含 50 个任务的双臂 manipulation benchmark，作者按既有多任务训练协议，用 2,500 条 clean-scene trajectories 和 25,000 条 strongly randomized trajectories 混合训练 100k steps。摘录还提到 memory 相关 benchmark 和 real-time robot control，但具体表格数字没有完整呈现。结论声称 WLA-0 在多任务表现、memory benchmark 和长程推理/实时控制上取得强结果或 state-of-the-art 结果。能明确引用的证据主要是模型规模、组件配置、训练数据规模和 benchmark 类型；关于成功率提升幅度、SOTA 差距和真实机器人任务细节，需要 PDF 中表格和消融进一步核查。

#### ⚠️ 风险 / 保留意见

- 3.4B 参数与多 expert 结构复现成本高，训练数据、算力和工程细节都会影响结论可迁移性。
- world prediction 推理时可关闭这一点很有吸引力，但其对动作提升的因果贡献需要强消融支持。
- 摘要级证据显示统一建模很强，但不同 benchmark 的数据配比和任务难度可能掩盖模块真实贡献。

#### 💭 结论与启发

这篇值得作为“下一代 VLA 接口设计”的参考：动作头前不只是塞更多视觉语言 token，而是让模型同时学习 subtask、subgoal image 和 action，并用 meta-query 把世界预测转成动作条件。后续选题可以围绕两个问题展开：一是世界预测是否必须生成可视化图像，还是只需要 latent dynamics；二是 test-time scaling 在机器人控制中应当花在语言计划、世界 rollout 还是动作假设上。复现时应先做小模型版本，验证 meta-query 与 world loss 对 action success 的边际收益。

#### 🔎 读 PDF 先核查

- meta-queries 如何把 World Expert 的预测信息传递给 Action Expert，是否有显式 cross-attention 或共享 latent 接口？
- 推理时关闭 world prediction 后，动作性能相比开启 world prediction 和完全移除 world loss 分别如何变化？
- WLA-0 在 RoboTwin、LIBERO 和 memory benchmark 上的提升是否来自语义 subtask 预测、subgoal image 预测，还是更大的 backbone 容量？

#### 📌 上传 PDF 后优先看

- WLA 架构图与 meta-query 机制章节
- world / language / action 多任务损失和推理开关消融
- RoboTwin 2.0、LIBERO、memory benchmark 的表格与 ablation

### [4]. AffordanceVLA: A Vision-Language-Action Model Empowering Action Generation through Affordance-Aware Understanding [[HTML]](https://arxiv.org/html/2606.06155) [[PDF]](https://arxiv.org/pdf/2606.06155) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.06155`
* **Authors**: Qize Yu, Jiadi You, Yuran Wang, Jiaqi Liang, Bowen Ping, Yang Tian, Yue Chen, Minghong Cai, Zeying Gong, Ruihai Wu, Yinchuan Li, Junwei Liang, Yingcong Chen
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为 AffordanceVLA 用 which/where/how affordance 中间表征缓解 VLM 语义空间到机器人动作空间的错配。
* **关键词**: `affordance forecasting` `VLA` `Mixture-of-Transformer` `2D/3D grounding` `manipulation policy`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

这篇的动机非常典型但重要：VLA 常借助 pretrained VLM 的世界知识来做 instruction-following manipulation，但 VLM 的预训练目标主要是视觉-语言语义对齐，而机器人动作存在于 3D 物理空间。直接从自然语言和图像端到端预测动作，容易让模型知道“是什么”，却不知道“该接触哪里、如何接触、以什么几何方式执行”。已有路线包括视频预测、轨迹预测或直接 policy learning，但中间表示如果不够 task-oriented，就难以稳定桥接 perception 与 action。AffordanceVLA 的核心判断是，affordance forecasting 可以作为更精确的中间接口：先定位与任务相关的对象和交互区域，再进行 3D 几何推理，最后指导动作生成。对 VLA 来说，这相当于把语义理解拆成可执行的 manipulation prior。

#### ⚙️ 核心方法

AffordanceVLA 引入 structured affordance forecasting，逐步建模三类互补先验：Which2Act 用 object-centric grounding 和 visual latent prediction 抑制视觉干扰；Where2Act 估计 2D affordance map，给出交互位置；How2Act 做 3D geometric reasoning，用于指导 manipulation policy。摘录显示这些 affordance cues 是 spatially grounded、semantically conditioned 且 action-coupled 的中间表示。架构上，实验问题提到 Mixture-of-Transformer 设计，包含 Understanding、Affordance Generation 和 Action experts，目标是避免 unified network structures 中的 representation collapse。训练范式是 three-stage progressive training，用来从广义视觉语言预训练逐步过渡到任务相关 embodied control。当前摘录能确认上述模块和训练设计，但没有提供每个 expert 的精确网络结构、affordance supervision 来源、2D/3D 标签构造方式或动作头细节。因此方法解读应保守：它的核心贡献是把 VLA 的感知-动作映射拆成 which/where/how 三个 affordance 子问题，并用专门 expert 维护这些表征，而不是假设单一 VLM latent 可以自动对齐控制空间。

#### 📊 实验与结果

实验覆盖 simulation benchmarks 和 real-world tasks。摘录明确提到在 LIBERO 与 CALVIN 上比较大量 baseline，并报告两个模型变体，以隔离架构和训练范式贡献。实验问题围绕三点：structured affordance forecasting 是否是有效中间表示，MoT 的解耦 expert 是否避免 representation collapse，三阶段 progressive training 是否帮助弥合 VLM 预训练与 embodied control 的差距。结论片段还给出一个定性 failure mode：在 Toaster 任务中，Pi0 的失败集中于 button-pressing step，常把“按按钮”误执行成夹爪闭合式 pick-and-place，说明 instruction following 和动作 affordance 对齐不足。摘录中的数值占位不完整，因此不能引用具体成功率，只能说明作者用仿真与真实任务、baseline、变体和失败案例来支撑主张。

#### ⚠️ 风险 / 保留意见

- affordance 标签或伪标签的来源若成本高，会限制规模化复现。
- which/where/how 分解对接触型 manipulation 很自然，但对非刚体、工具使用或双臂协调的充分性需要验证。
- MoT 和三阶段训练引入较多组件，真实收益需要看严格 ablation，而不能只看最终模型胜出。

#### 💭 结论与启发

这篇对系统设计的启发是，不要把 VLA 的所有能力都压进一个动作 decoder；对精细操作，显式 affordance 中间层可能比更大 backbone 更有效。后续复现可以从最小版本开始：保留原 VLA action head，只加入 2D affordance map 或 object-centric latent，观察是否能减少“语义理解正确但接触动作错误”的失败。读 PDF 时应特别关注 affordance supervision 是否可自动生成，因为这决定了方法是工程上可扩展，还是主要依赖昂贵标注。

#### 🔎 读 PDF 先核查

- Which2Act、Where2Act、How2Act 的监督信号分别来自人工标注、仿真标签、轨迹反推还是模型伪标签？
- MoT 的 Understanding、Affordance Generation、Action experts 如何通信，是否存在共享 token 或 gating 机制？
- Toaster/button-pressing 这类 failure mode 的改善是否能由 affordance map 直接解释，还是来自整体模型容量增加？

#### 📌 上传 PDF 后优先看

- which/where/how affordance 表征定义与标签构造章节
- MoT 架构和 representation collapse 消融
- LIBERO、CALVIN 与真实任务 failure mode 对比

### [5]. MPCoT: Reward-Guided Multi-Path Latent Reasoning for Test-Time Scalable Vision-Language-Action [[HTML]](https://arxiv.org/html/2606.06245) [[PDF]](https://arxiv.org/pdf/2606.06245) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.06245`
* **Authors**: Boyang Zhang, Lianlei Shan
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为 MPCoT 把 VLA 的测试时计算做成 latent multi-path refinement，而不是生成显式 CoT token。
* **关键词**: `latent reasoning` `test-time scaling` `OpenVLA-OFT` `path preference` `CALVIN`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

MPCoT 关注 VLA 在长程和高不确定性控制中的脆弱性。传统 one-pass action decoding 很高效，但面对组合指令、连续子任务和早期误差累积时，策略缺少推理时 deliberation。显式 chain-of-thought 可以增加推理深度，但在机器人控制中会带来 token latency、内存开销，以及文本 rationale 到连续动作之间的间接接口。论文的动机是寻找一种更贴近控制的测试时 scaling：让模型在连续 latent space 中初始化多条假设、迭代细化、评分聚合，再输出动作 chunk。这样既保留原始 action interface，又避免输出解释性 token。对 VLA/RL 结合方向来说，它把 reward-guided training 和 reward-free inference 连接起来，试图用训练期奖励监督换取测试期轻量选择能力。

#### ⚙️ 核心方法

MPCoT 被插入 OpenVLA-OFT，在每个 control step 中先初始化多个 latent hypotheses，再用共享权重的 refinement steps 对这些分支进行迭代更新，随后根据 confidence-aware soft weights 聚合分支，最后交给同一个 action decoder 输出动作。论文强调它不是 multi-policy ensemble，也不是 inference-time search，而是在单一 policy head 前加入轻量 latent reasoning module。训练期，candidate branches 会接受 path-preference supervision，奖励来源包括 expert-action consistency、world-model/VLM-based progress 和 success feedback 等；这些信号训练 scorer，使推理期无需再访问 reward。接口上，MPCoT 保持 OpenVLA-OFT 的 8-step action interface 不变，显式把提升归因到 action head 前的 latent reasoning。它还支持通过增加 latent refinement depth 和 hypothesis width 来扩展测试时计算。摘录没有给出 scorer 的精确公式、world-model/VLM progress 的实现或 reward 归一化细节，因此这些应作为 PDF 核查重点。

#### 📊 实验与结果

实验使用 OpenVLA-OFT 官方 evaluation code 和 splits。主结果固定 inference 设置；depth/width ablation 只改变 latent steps 和 hypotheses，不改变 backbone、decoder、action horizon、splits 或 observations。LIBERO 被定位为 near-ceiling compatibility benchmark，CALVIN ABCD 和机制消融是检验 sequential robustness、depth/width scaling 与 reward-guided path supervision 的主要证据。指标上，LIBERO 报告 suite-level 和 average success rates；CALVIN ABCD 报告 1-5 step success rate 和 average successful sequence length，用于反映长程指令链中的误差累积。论文还用 Path Consistency 衡量 scorer-preferred path 与 highest-return path 的一致性。结论声称在 LIBERO 和 CALVIN 上优于强 baseline，并且消融支持 depth/width scaling、soft aggregation 与 reward-guided supervision 的作用；摘录未提供具体数值，因此不能陈述提升幅度。

#### ⚠️ 风险 / 保留意见

- 训练期 path reward 依赖 expert consistency、world-model/VLM progress 和 success feedback，其可靠性会直接影响 scorer。
- 测试时增加 depth/width 会带来 latency，是否适合真实机器人闭环频率需看完整延迟表。
- 目前证据主要来自 LIBERO 与 CALVIN，真实机器人部署和分布外任务仍是缺口。

#### 💭 结论与启发

这篇提供了一个很实用的 VLA test-time scaling 模板：不用让机器人策略说出 CoT，而是在动作头前做多假设 latent 推理。后续如果做 OpenVLA/OFT 系统，可以把 MPCoT 当作可插拔模块评估，重点看同一 action head 下是否能用少量额外计算提升长程稳定性。更重要的是，它提示 reward 不一定要在推理时在线搜索使用，也可以在训练期教会一个路径 scorer，再让策略在部署时做快速 latent aggregation。

#### 🔎 读 PDF 先核查

- 训练期 path-preference objective 中 expert consistency、world-model/VLM progress 和 success feedback 的权重如何设定？
- depth 和 width 增加时，成功率提升与推理延迟之间的拐点在哪里？
- Path Consistency 与实际 long-horizon success 是否强相关，还是只解释部分机制？

#### 📌 上传 PDF 后优先看

- MPCoT latent hypothesis refinement 与 scorer 训练章节
- LIBERO/CALVIN 主结果和 depth-width ablation
- 延迟、path consistency、soft aggregation 的机制消融

## Watchlist

### [W1]. TempoVLA: Learning Speed-Controllable Vision-Language-Action Policies [[HTML]](https://arxiv.org/html/2606.06491) [[PDF]](https://arxiv.org/pdf/2606.06491)
* **Paper ID**: `2606.06491`
* **Authors**: Dong Jing, Jingchen Nie, Tianqi Zhang, Jiaqi Liu, Huaxiu Yao, Zhiwu Lu, Mingyu Ding
* **Author Priority**: Standard
* **为什么还值得留意**: TempoVLA 进入 watchlist 是因为速度可控 VLA 很贴近真实部署：低风险 transit 需要快，高风险 contact 需要慢，而现有 VLA 通常继承示范数据的固定速度。它没有进入最终精选，主要是因为相对今天的 reward-free 后训练、闭环 world model 和统一 WLA，议题更偏执行控制层与数据增强；需要看 PDF 确认真实世界动态速度控制和高速度饱和边界。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

### [W2]. Flash-WAM: Modality-Aware Distillation for World Action Models [[HTML]](https://arxiv.org/html/2606.05254) [[PDF]](https://arxiv.org/pdf/2606.05254)
* **Paper ID**: `2606.05254`
* **Authors**: Arman Akbari, Ci Zhang, Arash Akbari, Lin Zhao, Yixiao Chen, Weiwei Chen, Xuan Zhang, Geng Yuan, Yanzhi Wang
* **Author Priority**: Standard
* **为什么还值得留意**: Flash-WAM 值得跟踪，因为 WAM 的多步 diffusion 推理成本确实阻碍实时控制，modality-aware distillation 针对 joint video-action streams 的噪声日程不对称提出了专门解法。它未进最终精选，是因为它更像 WAM 推理加速与蒸馏工程突破，而不是今天最核心的 VLA 后训练、闭环评估或动作推理框架；摘录中的部分速度和成功率数字缺失，也需要 PDF 核查。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

### [W3]. VISTA: Vision-Grounded and Physics-Validated Adaptation of UMI data for VLA Training [[HTML]](https://arxiv.org/html/2606.04708) [[PDF]](https://arxiv.org/pdf/2606.04708)
* **Paper ID**: `2606.04708`
* **Authors**: Siyuan Yang, Linzheng Guo, Ouyang Lu, Zhaxizhuoma, Daoran Zhang, Xinmiao Wang, Ting Xiao, Fangzheng Yan, Zhijun Chen, Yan Ding, Chao Yu, Chenjia Bai, Xuelong Li
* **Author Priority**: Standard
* **为什么还值得留意**: VISTA 进入 watchlist 是因为 UMI 数据到 VLA 训练之间的两个 mismatch 很关键：fisheye wrist view 对 VLM 不友好，human-collected trajectory 也可能物理不可执行。它没有进入最终精选，是因为它主要是数据适配与验证框架，和今天最终五篇相比，对 VLA policy 内部推理、world model 或后训练目标的直接方法贡献稍弱。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. LadderMan: Learning Humanoid Perceptive Ladder Climbing [[VIP]] [[HTML]](https://arxiv.org/html/2606.05873) [[PDF]](https://arxiv.org/pdf/2606.05873)
* **Paper ID**: `2606.05873`
* **Authors**: Siheng Zhao, Yuanhang Zhang, Ziqi Lu, Pieter Abbeel, Rocky Duan, Koushil Sreenath, Yue Wang, C. Karen Liu, Guanya Shi
* **Author Priority**: Core VIP
* **为什么还值得留意**: LadderMan 因 Pieter Abbeel 与 Yue Wang 进入 VIP 优先跟踪，同时其 humanoid ladder climbing 涉及 whole-body coordination、vision foundation model sim2real 和真实 Unitree G1 部署，工程价值很高。它没有进入最终精选，是因为主题更偏 humanoid locomotion/manipulation 系统，而不是 VLA、world action model 或 VLA+RL 的主线。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W5]. Open-H-Embodiment: A Large-Scale Dataset for Enabling Foundation Models in Medical Robotics [[VIP]] [[HTML]](https://arxiv.org/html/2604.21017) [[PDF]](https://arxiv.org/pdf/2604.21017)
* **Paper ID**: `2604.21017`
* **Authors**: Open-H-Embodiment Consortium: Nigel Nelson, Juo-Tung Chen, Jesse Haworth, Xinhao Chen, Lukas Zbinden, Dianye Huang, Alaa Eldin Abdelaal, Alberto Arezzo, Ayberk Acar, Farshid Alambeigi, Carlo Alberto Ammirati, Yunke Ao, Pablo David Aranda Rodriguez, Soofiyan Atar, Mattia Ballo, Noah Barnes, Federica Barontini, Filip Binkiewicz, Peter Black, Sebastian Bodenstedt, Leonardo Borgioli, Nikola Budjak, Benjamin Calmé, Fabio Carrillo, Nicola Cavalcanti, Changwei Chen, Haoxin Chen, Sihang Chen, Qihan Chen, Zhongyu Chen, Ziyang Chen, Shing Shin Cheng, Meiqing Cheng, Min Cheng, Zih-Yun Sarah Chiu, Xiangyu Chu, Camilo Correa-Gallego, Giulio Dagnino, Anton Deguet, Jacob Delgado, Jonathan C. DeLong, Kaizhong Deng, Alexander Dimitrakakis, Qingpeng Ding, Hao Ding, Giovanni Distefano, Daniel Donoho, Anqing Duan, Marco Esposito, Shane Farritor, Jad Fayad, Zahi Fayad, Mario Ferradosa, Filippo Filicori, Chelsea Finn, Philipp Fürnstahl, Jiawei Ge, Stamatia Giannarou, Xavier Giralt Ludevid, Frederic Giraud, Aditya Amit Godbole, Ken Goldberg, Antony Goldenberg, Diego Granero Marana, Xiaoqing Guo, Tamás Haidegger, Evan Hailey, Pascal Hansen, Ziyi Hao, Kush Hari, Kengo Hayashi, Jonathon Hawkins, Shelby Haworth, Ortrun Hellig, S. Duke Herrell, Zhouyang Hong, Andrew Howe, Junlei Hu, Zhaoyang Jacopo Hu, Ria Jain, Mohammad Rafiee Javazm, Howard Ji, Rui Ji, Jianmin Ji, Zhongliang Jiang, Dominic Jones, Jeffrey Jopling, Britton Jordan, Ran Ju, Michael Kam, Luoyao Kang, Fausto Kang, Siddhartha Kapuria, Peter Kazanzides, Sonika Kiehler, Ethan Kilmer, Ji Woong Kim, Przemysław Korzeniowski, Chandra Kuchi
* **Author Priority**: Core VIP
* **为什么还值得留意**: Open-H-Embodiment 因 Chelsea Finn 和大规模医疗机器人数据集进入 watchlist；摘录明确给出 119 个数据集、780 小时 paired video/kinematics、50 多个机构和 20 个平台，数据规模本身值得长期跟踪。它没有进入最终精选，是因为论文更偏医疗机器人 foundation dataset 与 GR00T-H 迁移验证，和今天 VLA/world model 方法创新主线相比更像重要资源型论文。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
