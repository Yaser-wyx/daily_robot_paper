# RoboPulse | 2026-06-11

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 86 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线很清晰：VLA 正在从“视觉-语言到动作”的端到端模仿，转向更强的物理闭环、动态先验、测试时计算调度和 RL 后训练。最终精选保留了触觉 Sim2Real、去中心化多机器人 VLA、动作专家预训练、具身 planner 路由、World-Action prior 以及生成式控制策略 RL 微调这六条互补路线。VIP 作者上，Hao Su 的 TacCoRL、Chelsea Finn/Jeannette Bohg 的 CHORUS、Yue Wang 的 APT、Chelsea Finn/Jiajun Wu 的 DIRECT、Sergey Levine 的 OGPO 都值得优先跟踪；扩展名单里的 Russ Tedrake 对应 Ambient Diffusion Policy，虽未入精选但应继续观察。整体看，今天更像是 VLA 工程化落地的一组关键补丁：补触觉、补协作、补语言泛化、补动态模型、补算力分配、补 RL 微调。

## 今日信号

- VLA 的下一阶段竞争点不只是更大 backbone，而是如何把触觉、力觉、世界模型和动作先验可靠接入决策链。
- World Action Model 正从“生成未来视频是否合理”转向“未来表征是否真的能改善动作解码”，接口对齐会成为核心问题。
- RL 与测试时计算在机器人中都开始强调成本约束：更高成功率必须同时回答样本效率、推理延迟和真实部署代价。

## Historical Rediscovery

- **Paper**: HiMem-WAM: Hierarchical Memory-Gated World Action Models for Robotic Manipulation [[HTML]](https://arxiv.org/html/2606.10363) [[PDF]](https://arxiv.org/pdf/2606.10363)
  - **Paper ID**: `2606.10363`
  - **来源日期**: 2026-06-10
  - **当时可能被低估的信号**: 当时可能因为 Efficient-WAM 已代表 WAM 部署效率方向而被压低优先级，但它的 LIBERO、LIBERO-PLUS、RMBench 与真实机器人部署信号说明它不是纯概念模型。
  - **为什么现在值得再看**: 你的兴趣里包含 World Action Model、长时程操作和真实部署评测；这篇正好连接 WAM 结构设计、记忆机制与机器人操作落地，值得重新核查其机制和增益是否足够扎实。
  - **建议动作**: 加入精读
  - **关键词**: `World Action Model` `long-horizon manipulation` `memory-gated policy` `real robot deployment` `LIBERO`
- **Paper**: MIND-V: Hierarchical World Model for Long-Horizon Robotic Manipulation with RL-based Physical Alignment [[HTML]](https://arxiv.org/html/2512.06628) [[PDF]](https://arxiv.org/pdf/2512.06628)
  - **Paper ID**: `2512.06628`
  - **来源日期**: 2026-06-10
  - **当时可能被低估的信号**: 当时被视为偏数据合成/视频世界模型、离闭环控制还有距离，但 GRPO 与 Physical Foresight Coherence reward 这类物理对齐信号可能低估了它对机器人世界模型训练的价值。
  - **为什么现在值得再看**: 现在如果关注 VLA/WAM 的预测式训练、长时程任务分解和物理一致性约束，这篇可作为视频 world model 如何服务操作任务的参考。
  - **建议动作**: 加入精读
  - **关键词**: `world model` `RL alignment` `long-horizon manipulation` `video generation` `physical consistency`
- **Paper**: VeriSpace: Spatially Grounded Action Verification for Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2606.10568) [[PDF]](https://arxiv.org/pdf/2606.10568)
  - **Paper ID**: `2606.10568`
  - **来源日期**: 2026-06-10
  - **当时可能被低估的信号**: 当时它被归为测试时校验模块而非训练主线，但 SimplerEnv-WidowX、LIBERO 和真实机器人实验的信号说明它可能直接影响部署可靠性。
  - **为什么现在值得再看**: 对真实 VLA 系统而言，动作验证、空间 grounding 和失败前筛选会越来越重要；它与 VLA、Sim2Real 评测和真实机器人部署高度相关。
  - **建议动作**: 加入精读
  - **关键词**: `VLA` `action verification` `3D spatial grounding` `test-time selection` `real robot evaluation`
- **Paper**: VistaBot: View-Robust Robot Manipulation via Spatiotemporal-Aware View Synthesis [[HTML]](https://arxiv.org/html/2604.21914) [[PDF]](https://arxiv.org/pdf/2604.21914)
  - **Paper ID**: `2604.21914`
  - **来源日期**: 2026-04-24
  - **当时可能被低估的信号**: 当时它被看作视角鲁棒性感知模块，但同时覆盖仿真与真实实验，并提出 View Generalization Score，说明它对部署泛化的评测价值可能被低估。
  - **为什么现在值得再看**: VLA 和 visuomotor policy 的真实部署常被视角变化卡住；这篇与 Sim2Real、真实评测、latent action 表示和稳健操作策略都有交集。
  - **建议动作**: 快速浏览
  - **关键词**: `view robustness` `Sim2Real` `latent action learning` `robot manipulation` `real experiment`
- **Paper**: VEGA: Visual Encoder Grounding Alignment for Spatially-Aware Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2605.10485) [[PDF]](https://arxiv.org/pdf/2605.10485)
  - **Paper ID**: `2605.10485`
  - **来源日期**: 2026-05-12
  - **当时可能被低估的信号**: 当时因其偏视觉 backbone grounding 而未被置于主线，但直接处理 spatially-aware VLA 表征，可能比 LLM-token 层经验搜索更接近底层瓶颈。
  - **为什么现在值得再看**: 如果接下来关注 3D-aware VLA、RoboTwin 2.0、ALOHA 或空间推理失败模式，这篇可以补上 VLA 表征层面的关键线索。
  - **建议动作**: 快速浏览
  - **关键词**: `VLA` `spatial reasoning` `visual encoder grounding` `3D-aware representation` `ALOHA`

## Editor's Picks

### [1]. TacCoRL: Integrating Tactile Feedback into VLA via Simulation [[VIP]] [[HTML]](https://arxiv.org/html/2606.11743) [[PDF]](https://arxiv.org/pdf/2606.11743) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.11743`
* **Authors**: Siyu Ma, Yuqi Liang, Chang Yu, Yunuo Chen, Hao Su, Yixin Zhu, Yin Yang, Chenfanfu Jiang
* **Author Priority**: Core VIP
* **一句话结论**: 优先看：TacCoRL 是今天最贴近 contact-rich VLA 落地的一篇，把触觉、Sim2Real 和模拟 RL 串成了可操作的后训练流程。
* **关键词**: `Tactile VLA` `Sim2Real` `Sparse-reward RL` `Contact-rich manipulation` `Real-data anchoring`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

VLA 模型能利用大规模视觉、语言和动作先验，但在插入、装配、双手操作这类接触密集任务中，视觉常常看不到最关键的局部状态：是否对齐、哪里接触、压力如何分布。单纯把视觉策略扩大，无法稳定解决近失败状态下的纠偏问题；而大规模触觉预训练或真实世界探索又成本高、风险大。TacCoRL 的动机正是在不依赖海量真实触觉数据的前提下，让已有 VLA 学会用触觉改变动作响应。它的重要性在于把 tactile feedback 从“额外传感器输入”提升为 contact-conditioned corrective action 的训练信号。

#### ⚙️ 核心方法

当前摘录可以确认，TacCoRL 采用两阶段 sim-to-real pipeline 来改造预训练 VLA。第一阶段是混合 sim-real co-training：用仿真与真实专家 rollout 共同初始化一个带触觉条件的动作先验，使策略在语言、图像、本体和触觉读数下输出 n-step action chunk。第二阶段是在交互式仿真中做 sparse-reward RL，用闭环接触环境训练近失败状态下的纠偏能力，同时用真实数据监督作为 anchor，约束策略不要偏离真实分布。方法还强调仿真并非离线数据源，而是 closed-loop contact environment；因此先对 policy-facing interfaces 做对齐，包括控制器响应和触觉读数。仿真侧额外有 privileged state，可用于 reward 和 critic learning，而策略推理时只使用真实机器人可获得的观测。新意在于，它不是简单拼接触觉 token，而是通过 sim-real co-training、simulation RL 与 real-data anchoring 组合，让触觉在动作层面产生可迁移的纠偏效果。

#### 📊 实验与结果

实验围绕四个问题展开：控制器与触觉信号是否足够对齐、sim-real co-training 是否能为仿真 RL 提供好初始化、加入触觉是否提升仿真 refined policy，以及真实机器人成功率是否优于 vision-only 和 imitation-only baseline。摘录明确提到，作者先做单关节 sweep 的 SysID，匹配真实与仿真的目标跟踪误差；触觉校准则通过 matched contact trajectories 比较 normalized active-taxel readings。真实评估覆盖四个双臂 contact-rich tasks，结论称 TacCoRL 在真实机器人上相对视觉-only 和 imitation-only baseline 提升成功率。但当前摘录没有给出具体成功率数值、任务名称细节或统计显著性，因此只能保守认为证据方向支持方法有效，具体幅度需要查 PDF 表格。

#### ⚠️ 风险 / 保留意见

- 依赖仿真控制器响应和触觉读数对齐，若传感器、材料或接触模型变化较大，迁移风险会升高。
- 真实数据 anchor 的权重选择会影响 RL 改进与分布偏移之间的平衡，可能需要任务级调参。
- 摘录未提供具体成功率和方差，真实机器人证据强度需要核查完整实验表。

#### 💭 结论与启发

对后续选题最有启发的是，触觉 VLA 不一定要从大规模 tactile-language-action 预训练开始，也可以作为预训练 VLA 的后训练补丁来做。系统设计上，应把触觉看成触发纠偏动作的局部状态估计，而不是被动附加模态；训练上，真实演示负责分布约束，仿真 RL 负责探索稀有接触失败状态。这给 contact-rich manipulation 的复现路线提供了较清楚的工程拆分：先做接口对齐，再做混合监督初始化，最后做受真实数据约束的模拟 RL。

#### 🔎 读 PDF 先核查

- 触觉读数是以何种 token、特征或时序窗口接入 VLA action head 的？
- real-data anchoring 的损失权重如何设置，不同权重下真实成功率是否稳定？
- 四个双臂 contact-rich tasks 中，触觉带来的收益是否主要集中在插入/装配等高接触不确定性任务？

#### 📌 上传 PDF 后优先看

- 方法章节中的触觉条件化策略结构与 action chunk 预测接口
- 仿真控制器 SysID、触觉校准和 sim-real alignment 实验
- 真实机器人四任务成功率表、消融表和 anchor weight 分析

### [2]. CHORUS: Decentralized Multi-Embodiment Collaboration with One VLA Policy [[VIP]] [[HTML]](https://arxiv.org/html/2606.12352) [[PDF]](https://arxiv.org/pdf/2606.12352) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.12352`
* **Authors**: Ria Doshi, Tian Gao, Annie Chen, Chelsea Finn, Jeannette Bohg
* **Author Priority**: Core VIP
* **一句话结论**: 优先看：CHORUS 把单个 VLA policy 用到去中心化异构多机器人协作，是 VLA 从单体操作走向 team behavior 的关键尝试。
* **关键词**: `Multi-robot collaboration` `Decentralized VLA` `Weight sharing` `Multi-embodiment` `Collaborative manipulation`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

多机器人协作在搬运、清洁、装配和建筑等任务中很自然，但移动多机器人场景同时面临异构 embodiment、局部可观测、通信开销和团队规模扩展问题。集中式策略虽然能看全队观测并一次输出所有动作，但随着机器人数量增加，输入上下文和动作空间迅速膨胀，也会远离单机器人 VLA 的预训练分布。传统去中心化方法常为每个机器人训练独立策略，推理时又可能需要显式对齐或信息共享。CHORUS 的核心动机是利用预训练 VLA 的视觉-动作先验和对队友视觉线索的反应能力，让一个共享权重策略在每个机器人本地运行，从而兼顾协作、扩展性和训练效率。

#### ⚙️ 核心方法

当前摘录显示，CHORUS 的关键设计是 decentralized inference 加 weight sharing：同一个 VLA policy 被部署到不同机器人上，每个实例只接收该机器人的局部观测并输出本体动作，而不是汇总全队观测。作者构造了一个 centralized VLA baseline，输入为两个机器人的 concatenated observations，并联合输出两个机器人的动作；理论上它信息更多，可作为上界，但实际因为输入维度增加、控制频率共享、camera slot 与预训练单移动操作臂分布不匹配，未必能达到上界。CHORUS 的方法新意不在于显式通信协议，而在于把共享 VLA backbone 作为隐式协作先验：机器人通过本地视觉观察队友行为并即时响应。摘录还提到中心化 baseline 需要共享控制率，附录分析了 resampling，这说明 CHORUS 在异构团队中避免了部分同步约束。完整架构细节、观测格式和动作空间映射仍需 PDF 核查。

#### 📊 实验与结果

实验问题包括：预训练 backbone 是否优于从零训练的模仿学习方法，跨机器人共享权重是否提升对队友行为的反应性，CHORUS 与集中式全队观测策略相比如何，以及能否扩展到三机器人团队。摘录明确说在三个任务中，CHORUS 匹配或超过 centralized baseline，尽管推理时只使用本地观测；结论还称框架能较平滑地扩展到更大和异构团队。当前摘录没有给出具体任务名称、成功率数值、机器人硬件配置或统计区间，因此不能夸大结果幅度。可确认的证据是，作者至少系统比较了去中心化共享权重、集中式共享权重和从零训练 baseline，并用实验支持共享 VLA backbone 对协作 manipulation 有帮助。

#### ⚠️ 风险 / 保留意见

- 去中心化策略依赖本地视觉观察队友，遮挡、视角受限或队友不可见时可能退化。
- 一个共享策略跨 embodiment 工作需要动作空间和观测接口设计，硬件差异过大时复现难度会上升。
- 摘录未说明是否有真实机器人长时程失败分析，协作稳定性和安全性仍需核查。

#### 💭 结论与启发

CHORUS 给我的启发是，多机器人 VLA 不一定从通信、图搜索或 centralized transformer 开始，也可以先验证“共享单体 VLA 是否已包含足够的视觉协作先验”。如果这个假设成立，系统设计可更轻：每台机器人只跑本地策略，用视觉感知队友，而不是搭建复杂团队状态服务器。后续复现应重点关注任务是否真的需要协作、队友行为变化是否会触发反应，以及共享权重相对 per-robot policy 的泛化收益。

#### 🔎 读 PDF 先核查

- CHORUS 如何把不同 embodiment 的动作空间统一到同一个 VLA policy 输出接口？
- 共享权重带来的 reactivity benefit 是通过哪些对照实验量化的？
- 三机器人扩展中，性能下降主要来自局部可观测、碰撞协调还是控制频率不一致？

#### 📌 上传 PDF 后优先看

- 方法章节中的 decentralized inference 与多 embodiment action mapping
- baseline design 表，尤其是 centralized VLA、per-robot policy 和 from-scratch IL 对照
- 三机器人扩展实验、异构团队实验和失败案例分析

### [3]. APT: Action Expert Pretraining Improves Instruction Generalization of Vision-Language-Action Policies [[VIP]] [[HTML]](https://arxiv.org/html/2606.12366) [[PDF]](https://arxiv.org/pdf/2606.12366) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.12366`
* **Authors**: Kechun Xu, Zhenjie Zhu, Anzhe Chen, Rong Xiong, Yue Wang
* **Author Priority**: Core VIP
* **一句话结论**: 优先看：APT 针对连续动作 VLA 的语言泛化短板提出 action expert pretraining，是理解 VLA OOD instruction failure 的重要论文。
* **关键词**: `Instruction generalization` `Action expert pretraining` `Continuous-action VLA` `Visual shortcuts` `OOD language`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

当前连续动作 VLA 通常把预训练 VLM 接到随机初始化的 action expert，再用机器人数据联合训练。问题在于机器人数据存在结构性不平衡：一段轨迹包含大量视觉-动作变化，却只对应一条语言指令，导致 action expert 很容易学习视觉捷径，而不真正依赖语言。这样模型在 seen task 上可能表现不错，但遇到 paraphrase、新物体引用或组合指令时就失败。离散动作路线可通过 vision-language co-training 缓解这一问题，但连续动作专家缺乏类似保护。APT 的动机是先让 action expert 在更平衡的 vision-action 数据上学到稳定动作先验，再与 VLA likelihood 结合，以改善 OOD instruction generalization。

#### ⚙️ 核心方法

APT 将 VLA 策略表述为从视觉观测和语言指令到连续动作的映射，并指出瓶颈来自随机初始化 action expert 在不平衡 VLA 数据上产生 noisy gradients 和 language bypass。当前摘录可以确认，方法把策略分解为 VA prior 和 VLA likelihood，并由此形成两阶段预训练流程：先在 balanced vision-action data 上预训练 action expert，使其获得较稳健的动作生成能力；再引入语言条件，让模型学习语言如何修正或选择动作分布。这样的设计意图是降低 action expert 对视觉位置、物体布局等捷径的依赖，让语言在 OOD 指令、替换目标和组合任务中真正参与决策。摘录没有展开具体网络结构、损失公式和训练日程，因此不能断言其实现细节；但可以确认其方法核心不是换更大 VLM，而是重新安排 action expert 的初始化和训练分解，解决连续动作 VLA 中语言监督稀疏的问题。

#### 📊 实验与结果

实验覆盖两类语言泛化 benchmark。LIBERO-PRO 在 LIBERO 上引入 Pos 和 Task 两类扰动：Pos 交换物体位置但固定指令，用来测试是否依赖语言而非位置先验；Task 替换指令中的操作对象，形成 OOD language generalization。另一个 rigid object pick-place benchmark 包含 Seen Object、Unseen Object、Unseen Container、Unseen Object & Unseen Environment 四个 suite，并随机化布局、相机视角和指令。结论称 APT 在 instruction generalization 上有一致提升，并适用于多种架构。摘录没有给出具体成功率、均值方差或 ablation 数字，因此当前只能确认实验设计对语言泛化问题是针对性的，结果幅度要等 PDF 表格核查。

#### ⚠️ 风险 / 保留意见

- 依赖 balanced vision-action pretraining 数据，数据构造方式会直接影响方法收益。
- 当前设计不显式建模长时程记忆，长任务或多阶段组合指令可能仍受限。
- 若 OOD 失败来自感知或语义 grounding 而非 action expert 初始化，APT 的提升可能有限。

#### 💭 结论与启发

APT 对后续 VLA 研究的价值在于，它把 OOD instruction failure 从“语言模型不够强”转向“动作专家训练动态不对”来解释。复现时不应只看最终成功率，还要设计能排除位置捷径的数据扰动，例如目标交换、容器交换和组合指令。系统上，如果已有连续动作 VLA 在 seen task 好但语言替换差，可以优先尝试 action expert 的 VA pretraining 或分阶段冻结/解冻，而不是盲目扩大机器人数据。

#### 🔎 读 PDF 先核查

- VA prior 与 VLA likelihood 在训练和推理时如何组合，是否增加推理成本？
- balanced vision-action data 的定义和采样策略是什么，是否需要人工重标注？
- APT 的改进是否主要来自 action expert 初始化，还是来自后续训练中的语言梯度更稳定？

#### 📌 上传 PDF 后优先看

- 方法章节中的 VA prior/VLA likelihood 分解和两阶段训练算法
- LIBERO-PRO Pos/Task 结果表与语言泛化消融
- 不同 VLA 架构上的迁移实验和长时程限制讨论

### [4]. DIRECT: When and Where Should You Allocate Test-Time Compute in Embodied Planners? [[VIP]] [[HTML]](https://arxiv.org/html/2606.12402) [[PDF]](https://arxiv.org/pdf/2606.12402) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.12402`
* **Authors**: Jadelynn Dao, Milan Ganai, Yasmina Abukhadra, Ajay Sridhar, Mozhgan Nasr Azadani, Katie Luo, Clark Barrett, Jiajun Wu, Chelsea Finn, Marco Pavone
* **Author Priority**: Core VIP
* **一句话结论**: 优先看：DIRECT 把 test-time compute routing 引入具身 planner，回答什么时候该用更贵 VLM、什么时候便宜模型足够。
* **关键词**: `Test-time compute` `Embodied planning` `VLM routing` `Quality-cost Pareto` `Franka DROID`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

VLM 正被大量用作具身 agent 的高层 planner，将抽象指令拆成可执行 skill plan，再交给低层策略执行。一个直观趋势是增加 test-time compute，例如使用更大模型、更深 reasoning 或更多历史上下文，但机器人场景对延迟、token、FLOPs 和部署成本非常敏感。摘录指出，在 Franka 实验中 Thinking model 更慢但成功率与非 thinking counterpart 相同，说明额外计算并非均匀有效。DIRECT 的问题意识很实际：具身任务难度由语言、视觉场景和轨迹可行性共同决定，因此需要根据 prompt 与 multimodal scene context 动态分配 planner 计算，而不是一律使用最贵配置。

#### ⚙️ 核心方法

DIRECT 是一个面向 embodied planner 的 routing framework。它借鉴 FrugalGPT、RouteLLM 等模型路由思想，但区别在于传统路由主要依赖文本特征，而机器人任务的难度还取决于物理场景、对象布局、可达性和低层执行约束。当前摘录可以确认，DIRECT 使用 multimodal scene context 对每个 prompt 分配计算，把任务路由到 capability profile 更匹配的 planner 配置。候选维度包括 reasoning depth、model size 和 memory history；这些轴带来的能力增益不同，因此 router 不是简单在大小模型之间二选一，而是在多种成本-能力配置之间选择。作者将其定位在高层规划栈，而非低层 diffusion controller 的 integration-step routing。评估时，每个 router configuration 对应 quality-cost 平面上的一个点，并用受 LLM/VLM routing benchmark 启发的 harmonic-mean efficiency score 比较 success 与 cost 的折中。具体 router head、输入编码、训练标签和成本定义需要 PDF 核查。

#### 📊 实验与结果

摘录显示，DIRECT 在 VLABench、RoboMME 和 Franka DROID hardware experiments 上评估，并声称能以更低成本恢复接近 frontier 的成功率。实验分析了 reasoning depth、model size 和 memory history 三个 test-time compute 轴，结论是收益具有 task-contingent 特征：便宜配置已经足以完成大量任务，而某些任务才需要更高能力模型。方法评价采用质量和成本归一化后的 harmonic-mean efficiency score，并与 oracle quality ceiling 及不同 router/baseline 比较。当前摘录没有给出成功率、成本降低比例或硬件任务细节，除了 Franka 上 thinking/non-thinking 成功率相同这一现象描述外，不能引用具体数字。

#### ⚠️ 风险 / 保留意见

- router 本身需要可靠预测任务难度，若场景分布变化，可能把困难任务路由给低能力 planner。
- 高层 planner 成功率还受低层 skill policy 影响，路由收益可能被执行误差掩盖。
- 成本指标包含 latency、token 和 FLOPs 等多维因素，实际部署权重需按硬件和任务重新校准。

#### 💭 结论与启发

DIRECT 的启发是，机器人中的 test-time scaling 不能只用“更会推理”叙事来评价，必须把成功率和延迟/成本放在同一张图上。对构建 VLA/VLM planner 系统来说，一个实用路线是准备多个 planner 配置，再训练轻量 router 识别哪些任务真的需要复杂推理、长历史或大模型。后续读 PDF 时应重点看 router 是否能从视觉场景中学到物理难度，而不是仅按指令长度或语义类别做近似分类。

#### 🔎 读 PDF 先核查

- DIRECT 的 router 输入包含哪些视觉、语言和历史特征，是否使用低层执行反馈？
- 不同 compute 轴中，reasoning depth、model size、memory history 分别解决哪类失败？
- 在真实 Franka DROID 实验中，成本降低是否伴随失败模式变化或安全风险上升？

#### 📌 上传 PDF 后优先看

- router 架构、训练目标和 quality-cost metric 定义
- VLABench/RoboMME 上不同 compute 轴的分解实验
- Franka DROID 硬件实验、latency/token/FLOPs 与成功率 Pareto 曲线

### [5]. World Pilot: Steering Vision-Language-Action Models with World-Action Priors [[HTML]](https://arxiv.org/html/2606.12403) [[PDF]](https://arxiv.org/pdf/2606.12403) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.12403`
* **Authors**: Zefu Lin, Rongxu Cui, Junjia Xu, Xiaojuan Jin, Wenling Li, Lue Fan, Zhaoxiang Zhang
* **Author Priority**: Standard
* **一句话结论**: 优先看：World Pilot 是今天最直接连接 VLA 与 World-Action Model 的精选，用 WAM prior 同时 steering 感知层和动作层。
* **关键词**: `World-Action Model` `Latent Steering` `Action Steering` `OOD manipulation` `Video-pretrained priors`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

VLA 的语义 grounding 主要来自静态 image-text 预训练，但机器人操作是连续、接触丰富且强动态的过程。静态图文预训练无法告诉 action generator 场景在动作作用下会怎样变化，因此当视角、几何或接触容差偏离训练分布时，VLA 容易变脆。视频预训练和 World-Action Model 提供了自然补充：它们含有动作条件下的场景演化信息。World Pilot 的动机是把 WAM 的动态先验注入 VLA 决策链，而不是只把世界模型当成可视化未来的模块。它关注的核心问题是：如何让 scene-evolution latent 和 anticipated trajectory 真正影响 perception 与 action generation。

#### ⚙️ 核心方法

World Pilot 在标准 VLA pipeline 上增加一个 video-pretrained WAM branch。标准 VLA 用 VLM 编码图像和语言得到 multimodal hidden states，再由 action generator 输出未来动作 chunk；World Pilot 则让 WAM 从相同输入出发，同时预测 scene-evolution latent 和 coarse action-trajectory hypothesis。两者来自 shared encoder，因此 latent 描述的是某条动作轨迹可能导致的场景变化，trajectory 则是该预测背后的运动假设。方法通过两条路径注入先验：Latent Steering 在 perception side 条件化 VLM/感知层，让策略表示包含场景演化信息；Action Steering 在 action-generator side 提供 anticipated trajectory，作为运动级先验。摘录明确说明其实现构建在 ABot-M0 上，VLM backbone 为 Qwen3-VL，动作头是 DiT-based flow matching，并使用 Cosmos Policy 作为 WAM，评估时 WAM 在线运行，训练时预计算 WAM 输出，同时对 WAM conditions 加 dropout 防止过度依赖。

#### 📊 实验与结果

World Pilot 在两个模拟 benchmark 上评估。LIBERO-Plus 是基于 LIBERO 的 10,030 个 OOD perturbation tasks，覆盖 background、camera、language、light、layout、robot、noise 七类扰动，模型只在 LIBERO 训练并 zero-shot 测试扰动。RoboCasa 强调日常厨房场景中的长时程操作。摘录给出明确数字：World Pilot 在 LIBERO-Plus 上 Total success rate 达到 84.7%，为三随机种子平均，比最强 reported baseline 高 2.6 个百分点，并在 Camera、Light、Background、Noise 上领先。结论还声称在所有真实机器人设置中获得最高成功率，但摘录没有给出真实机器人具体数值、任务和硬件细节，因此需保守看待真实证据强度。

#### ⚠️ 风险 / 保留意见

- World Pilot 继承 WAM 覆盖范围，若测试场景超出 WAM 视频/动作分布，steering 可能误导策略。
- WAM 在线运行会增加推理成本，尤其在真实机器人闭环控制中可能影响频率。
- 对 WAM condition 使用 dropout 说明过度依赖风险真实存在，需要核查消融。

#### 💭 结论与启发

World Pilot 最值得借鉴的是双路径注入：动态先验既可以改 perception hidden state，也可以直接约束 action generator。对后续系统设计来说，WAM 不应只评价视频预测像不像，而应评价它的 latent 和 trajectory 是否能提升 OOD 操作成功率。复现时可以先从预计算 WAM features 开始，验证 Latent Steering 与 Action Steering 各自贡献，再考虑在线 WAM 的时延和稳定性。它也提示 World Model 方向需要与具体 action interface 绑定，否则很容易停留在“看起来合理的未来”。

#### 🔎 读 PDF 先核查

- Latent Steering 具体注入 VLM 哪些层，是否会破坏原有语义 grounding？
- Action Steering 的 coarse trajectory 在训练和推理时如何与 flow-matching action head 融合？
- LIBERO-Plus 七类扰动中，WAM prior 对 language/layout/robot 扰动是否同样有效？

#### 📌 上传 PDF 后优先看

- World Pilot 架构图与 Latent Steering/Action Steering 接口
- LIBERO-Plus 分扰动结果表和 WAM condition dropout 消融
- 真实机器人设置、在线 WAM 推理成本和失败案例

### [6]. OGPO: Sample Efficient Full-Finetuning of Generative Control Policies [[VIP]] [[HTML]](https://arxiv.org/html/2605.03065) [[PDF]](https://arxiv.org/pdf/2605.03065) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.03065`
* **Authors**: Sarvesh Patil, Mitsuhiko Nakamoto, Manan Agarwal, Shashwat Saxena, Jesse Zhang, Giri Anantharaman, Cleah Winston, Chaoyi Pan, Douglas Chen, Nai-Chieh Huang, Zeynep Temel, Oliver Kroemer, Sergey Levine, Abhishek Gupta, Hongkai Dai, Paarth Shah, Max Simchowitz
* **Author Priority**: Core VIP
* **一句话结论**: 优先看：OGPO 是生成式控制策略 RL 微调的重要补位，关注如何用 off-policy critics 高效全量微调 diffusion/flow policy。
* **关键词**: `Generative control policy` `RL finetuning` `Off-policy critic` `Modified PPO` `Diffusion policy`
* **证据来源**: arXiv HTML (Introduction, Method, Conclusion)

#### 📖 背景与动机

扩散和 flow-based generative control policies 已成为机器人模仿学习中的强参数化方式，但 BC 策略在部署时常对任务细节和环境变化很脆。通过 RL 自主微调预训练策略是自然方向，可减少额外人工数据需求；难点是生成式策略的动作由多步 denoising 或 flow 过程产生，如何把价值信号稳定传回完整生成过程并保持多模态行为，并不直接。传统 on-policy RL 样本效率低，纯 off-policy 又可能难以处理复杂生成策略分布。OGPO 的动机是在保留 GCP 多模态表达能力的同时，用更高数据复用率完成全参数 RL fine-tuning。

#### ⚙️ 核心方法

根据摘要和摘录，OGPO 即 Off-policy Generative Policy Optimization，核心是维护 off-policy critic networks 来最大化数据复用，并通过 modified PPO objective 将 policy gradients 传播过完整的 generative process，把 critic 作为 terminal reward 使用。当前 HTML 摘录的方法部分只给出一个关于 trajectory-level multimodality 的 mental model：在存在左右绕障两种模式的任务中，OGPO 倾向于在决策点保留与关键动作方向正交的方差，从而维持左右两种可行轨迹分支；同时在动作分布两端进行“stretching”，使轨迹分布在可行模式周围更锐化。结论还指出，OGPO 结合了 on-policy 与 off-policy 方法的优点。由于摘录缺少完整算法伪代码、损失定义和 critic 更新细节，不能进一步捏造 PPO 修改形式；但可确认其主张是对 diffusion/flow GCP 做 full-finetuning，而非只训练小头或 adapter。

#### 📊 实验与结果

摘要称 OGPO 在多任务、高精度插入和灵巧控制等 manipulation tasks 上达到 state-of-the-art，并强调样本效率。结论进一步说该方法在 numerous tasks 上有高成功率和高样本效率。当前摘录没有给出具体 benchmark 名称、成功率、样本数量、baseline 列表或真实/仿真划分，因此实验细节证据不足，只能把它作为一篇需要重点核查完整表格的 RL fine-tuning 论文。值得注意的是，作者自己在结论中指出 parallel denoising rollouts 用于估计 Q-values 时，对大型 VLA 模型可能非常昂贵，这为实验可扩展性和实际部署成本划出了重要边界。

#### ⚠️ 风险 / 保留意见

- Q-value 估计需要 parallel denoising rollouts，对大模型 VLA/GCP 的推理成本可能过高。
- off-policy critic 的学习质量会直接影响完整生成过程的梯度，存在价值误差放大风险。
- 当前摘录缺少完整实验数字，SOTA 主张需要核查任务设置和 baseline 公平性。

#### 💭 结论与启发

OGPO 对我的启发是，VLA/GCP 的后训练不能只讨论 RL 能否提升成功率，还要讨论生成过程本身如何被优化。若直接在最终动作上做 policy gradient，可能无法保留扩散策略的多模态轨迹结构；OGPO 的价值在于尝试让 critic 信号穿过整个生成链条，同时利用 off-policy 数据提高样本效率。后续阅读应优先判断它是否真的适合大规模 VLA，还是更适合作为中等规模 diffusion/flow policy 的精调算法。

#### 🔎 读 PDF 先核查

- modified PPO objective 如何定义，梯度具体怎样穿过 diffusion/flow 生成步骤？
- off-policy critic 使用哪些数据训练，如何控制分布外动作的 Q 过估计？
- parallel denoising rollouts 的数量与性能/成本之间有什么消融关系？

#### 📌 上传 PDF 后优先看

- 算法章节中的 OGPO 损失、critic 更新和 full-finetuning 流程
- 多任务、高精度插入、灵巧控制实验表和 baseline 设置
- Q-value 估计成本、parallel rollout 消融和大型 VLA 可扩展性讨论

## Watchlist

### [W1]. Making Foresight Actionable: Repurposing Representation Alignment in World Action Models [[HTML]](https://arxiv.org/html/2606.12217) [[PDF]](https://arxiv.org/pdf/2606.12217)
* **Paper ID**: `2606.12217`
* **Authors**: Lu Qiu, Yizhuo Li, Yi Chen, Yuying Ge, Yixiao Ge, Xihui Liu
* **Author Priority**: Standard
* **为什么还值得留意**: AGRA 很贴合 World Action Model 方向：它指出“看起来合理的未来视频”不等于“可用的动作表征”，并用 attention analysis 与 causal intervention 诊断 action decoder 关注无关区域的问题。它进入 watchlist 是因为 WAM interface alignment 很重要，但相比 World Pilot，当前摘录更像针对单个 WAM 表征错配的修正，覆盖面和 VLA 系统整合程度略弱。后续应重点看真实 IRON-R01 humanoid 的 OOD 设置和 DINOv2/SigLIP 对齐消融。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. DAM-VLA: Decoupled Asynchronous Multimodal Vision Language Action model [[HTML]](https://arxiv.org/html/2606.12105) [[PDF]](https://arxiv.org/pdf/2606.12105)
* **Paper ID**: `2606.12105`
* **Authors**: Pankhuri Vanjani, Zhuoyue Li, Jakub Suliga, Moritz Reuss, Gianluca Geraci, Xinkai Jiang, Rudolf Lioutikov
* **Author Priority**: Standard
* **为什么还值得留意**: DAM-VLA 抓住了 VLA 的时间同步假设问题：语言、视觉、本体、力觉并不应共享同一处理频率，异步 latent buffer 对真实控制很有工程意义。它没有进入最终精选，主要是因为今天精选已由 TacCoRL 覆盖触觉/接触闭环，且 DAM-VLA 的方法更偏架构与传感器频率管理。仍建议跟踪其 Franka 七个 contact-rich tasks 和 25Hz RGB、100Hz proprioception/force 的异步设计细节。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. Bridging the Morphology Gap: Adapting VLA Models to Dexterous Manipulation via Intent-Conditioned Fine-Tuning [[HTML]](https://arxiv.org/html/2606.12109) [[PDF]](https://arxiv.org/pdf/2606.12109)
* **Paper ID**: `2606.12109`
* **Authors**: Chuanke Pang, Junyi Huang, Zhijun Zhao, Yaobing Wang, Kun Xu, Xilun Ding
* **Author Priority**: Standard
* **为什么还值得留意**: InDex 关注 VLA 从低 DoF 平行夹爪迁移到高 DoF 灵巧手的 morphology gap，用 virtual grasp intent 和 decoupled fine-tuning 避免 catastrophic forgetting 与 action manifold collapse。它进入 shortlist 是因为 cross-morphology adaptation 很重要，但摘录显示实验主要是 robosuite 仿真与 teleoperation 数据，真实部署证据不足。相比今天精选，它与 VLA 主线相关但对 Sim2Real/RL/world model 的贡献不够中心。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics [[VIP]] [[HTML]](https://arxiv.org/html/2606.12365) [[PDF]](https://arxiv.org/pdf/2606.12365)
* **Paper ID**: `2606.12365`
* **Authors**: Adam Wei, Nicholas Pfaff, Thomas Cohn, Arif Kerem Dayı, Constantinos Daskalakis, Giannis Daras, Russ Tedrake
* **Author Priority**: Extended VIP
* **为什么还值得留意**: Ambient Diffusion Policy 由 Russ Tedrake 参与，问题很实际：如何从失败、噪声、sim-to-real gap 或任务不匹配的 suboptimal data 中只吸收有用部分。它提出 noise-dependent data usage，并在 noisy trajectories、sim-to-real gap、task mismatch 三类分布偏移上评估，理论和方法都值得看。未入最终精选的原因是它更偏 imitation learning/data mixture for diffusion policy，不是今天 VLA/World Model 主线的核心，但对大规模机器人数据清洗和共训练很有参考价值。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
