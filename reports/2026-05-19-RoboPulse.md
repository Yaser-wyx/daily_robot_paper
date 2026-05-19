# RoboPulse | 2026-05-19

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 161 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线集中在三件事：高自由度 VLA 是否能真正进入复杂双臂双手操作，世界模型是否从视觉预测走向可交互评测，以及 RL/后训练如何避免把通用 VLA 压回单任务策略。最终精选保留了系统、基准、表征、RL 优化和实时规划接口这几类互补论文，原因是它们分别对应数据采集、记忆评测、跨具身动作表征、world model benchmark、跨任务 RL 和 4D flow planning 的关键短板。VIP 作者里最值得优先跟踪的是 Huazhe Xu 参与的 Dexora、Chelsea Finn 参与的 RoboMME，以及 Dhruv Shah 参与的 WorldArena 2.0；三篇分别代表高 DoF VLA、记忆型通用策略评测和世界模型平台化评测。整体趋势是 VLA 正从“会跟语言做动作”转向“能记忆、能规划、能跨具身、能在真实平台闭环验证”。

## 今日信号

- VLA 的竞争焦点正在从单臂夹爪任务转向更高自由度、更长时序、更强历史依赖的 embodied control。
- 世界模型论文开始把视觉质量之外的触觉、RL 交互、真实机器人平台纳入评测，说明“好看的视频预测”已不足以证明机器人价值。
- RL 后训练和 latent action/flow planning 都在试图解决同一个问题：如何给 VLA 一个更稳定、可迁移、可闭环优化的行动接口。

## Historical Rediscovery

- **Paper**: Health-Conditioned Vision-Language-Action Models for Malfunction-Aware Robot Control [[HTML]](https://arxiv.org/html/2605.16056) [[PDF]](https://arxiv.org/pdf/2605.16056)
  - **Paper ID**: `2605.16056`
  - **来源日期**: 2026-05-18
  - **当时可能被低估的信号**: 当时可能被低估的信号是：它关注关节退化、执行器能力下降和弱夹爪这类真实部署变量，而不是只在视觉或语言扰动上做鲁棒性。
  - **为什么现在值得再看**: 如果今天重新看 VLA 的真实部署评测，这篇能作为 malfunction-aware VLA 的切入点；它和 VLA、Sim2Real 后的真实硬件偏移、部署期鲁棒控制强相关。
  - **建议动作**: 加入精读
  - **关键词**: `VLA` `real deployment` `malfunction-aware control` `robustness`
- **Paper**: CLARE: Continual Learning for Vision-Language-Action Models via Autonomous Adapter Routing and Expansion [[HTML]](https://arxiv.org/html/2601.09512) [[PDF]](https://arxiv.org/pdf/2601.09512)
  - **Paper ID**: `2601.09512`
  - **来源日期**: 2026-05-18
  - **当时可能被低估的信号**: 当时可能被低估的信号是：它不仅在 LIBERO continual learning 设置中评估，还提到 FR3 真实任务，说明目标不是纯离线架构实验。
  - **为什么现在值得再看**: 现在值得再看，因为 VLA 从单任务策略走向持续部署时，遗忘、任务序列扩展和模块化适配会变成关键瓶颈；它与长时程 VLA、真实部署更新和 post-training 路线相关。
  - **建议动作**: 加入精读
  - **关键词**: `VLA` `continual learning` `adapter routing` `real robot`
- **Paper**: Reinforcement Learning with Action Chunking [[HTML]](https://arxiv.org/html/2507.07969) [[PDF]](https://arxiv.org/pdf/2507.07969)
  - **Paper ID**: `2507.07969`
  - **来源日期**: 2026-05-12
  - **当时可能被低估的信号**: 当时可能被低估的信号是：Sergey Levine 参与，且论文把 action chunking 放进 offline-to-online RL 和长时稀疏奖励语境，而不是只当作推理加速技巧。
  - **为什么现在值得再看**: 今天如果关注 RL+VLA 或 World Action Model，chunked control 如何在线改进、如何处理长时奖励，是很核心的问题；这篇适合作为 VLA 后训练和 chunked action RL 的方法底座。
  - **建议动作**: 加入精读
  - **关键词**: `RL` `action chunking` `VLA adaptation` `long-horizon control`
- **Paper**: Learning to Feel the Future: DreamTacVLA for Contact-Rich Manipulation [[HTML]](https://arxiv.org/html/2512.23864) [[PDF]](https://arxiv.org/pdf/2512.23864)
  - **Paper ID**: `2512.23864`
  - **来源日期**: 2026-05-07
  - **当时可能被低估的信号**: 当时可能被低估的信号是：它不是简单加入触觉输入，而是预测未来触觉图像，把 contact-rich manipulation 明确建成 world model 问题。
  - **为什么现在值得再看**: 如果今天关心 World Model 或 World Action Model 在真实操作中的作用，接触丰富任务是视觉模型最容易失效的场景；这篇和 tactile VLA、未来状态预测、接触操控强相关。
  - **建议动作**: 快速浏览
  - **关键词**: `tactile VLA` `world model` `contact-rich manipulation` `future prediction`
- **Paper**: NavRL++: A System-Level Framework for Improving Sim-to-Real Transfer in Reinforcement Learning-Based Robot Navigation [[HTML]](https://arxiv.org/html/2605.15559) [[PDF]](https://arxiv.org/pdf/2605.15559)
  - **Paper ID**: `2605.15559`
  - **来源日期**: 2026-05-18
  - **当时可能被低估的信号**: 当时可能被低估的信号是：它有跨模拟器迁移、同模拟器评估，以及 aerial 和 legged platforms 的真实实验线索，部署因素覆盖比普通 Sim2Real 论文更完整。
  - **为什么现在值得再看**: 虽然不是 VLA 主线，但它对 Sim2Real 和 RL 真实部署的变量建模很有参考价值；这些系统因素同样会影响 VLA/WAM 落地时的闭环控制可靠性。
  - **建议动作**: 快速浏览
  - **关键词**: `Sim2Real` `RL` `real deployment` `system latency`

## Editor's Picks

### [1]. Dexora: Open-source VLA for High-DoF Bimanual Dexterity [[VIP]] [[HTML]](https://arxiv.org/html/2605.18722) [[PDF]](https://arxiv.org/pdf/2605.18722) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.18722`
* **Authors**: Zongzheng Zhang, Jingrui Pang, Zhuo Yang, Kun Li, Minwen Liao, Saining Zhang, Guoxuan Chi, Jinbang Guo, Huan-ang Gao, Modi Shi, Dongyun Ge, Yao Mu, Jiayuan Gu, Rui Chen, Hao Dong, Huazhe Xu, Li Yi, Yixin Zhu, Hang Zhao, Pengwei Wang, Shanghang Zhang, Guocai Yao, Jianyu Chen, Hongyang Li, Hao Zhao
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，因为 Dexora 直接瞄准开源 VLA 里最缺的双臂双手 36-DoF 灵巧操作，并给出采集、训练、判别器和跨具身转移的完整系统线索。
* **关键词**: `VLA` `bimanual dexterity` `high-DoF control` `teleoperation` `cross-embodiment`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

现有 VLA 大多停留在单臂夹爪、双臂低自由度夹爪，或单臂灵巧手这几类设定，真正需要双臂协同和手指细操作的任务仍然缺少统一开源系统。Dexora 的动机很明确：瓶盖、书本、插装等任务并不是简单把两个夹爪策略拼起来就能解决，手臂轨迹、手指接触和语言目标需要被端到端地联合建模。对于 VLA 和 Sim2Real 来说，高 DoF 不是炫技，而是逼迫模型学习动作空间结构、接触时序和跨具身降维的试金石。

#### ⚙️ 核心方法

Dexora 的核心是把数据、硬件和策略接口一起设计，而不是只提出一个网络。摘录显示，它用混合遥操作管线解耦粗粒度手臂运动和细粒度手指关节：手臂运动来自轻量外骨骼背包，手指由 Apple Vision Pro 的 markerless hand tracking 驱动；同时驱动真实硬件和 MuJoCo twin，以构建和目标具身匹配的数据语料。策略端被描述为能够输出同步 arm-hand 轨迹的 VLA，并且动作空间覆盖双臂双手 36-DoF。训练中还引入数据质量判别器，用于 post-training 阶段引导模型更多利用高质量示范。实验设置里明确给出 policy 是 28 层、hidden size 1024、16 heads；判别器较小，为 12 层、hidden size 512、8 heads、30M 参数。相对已有 OpenVLA、RT-2、GR00T、RDT 等路线，新意不只在模型，而在把高 DoF 具身、示范采集、仿真孪生、数据筛选和低 DoF downshifting 放进同一系统。

#### 📊 实验与结果

实验从三个轴验证：基础与灵巧任务性能、OOD 鲁棒性与跨具身转移、以及训练数据组成和数据质量判别器消融。摘录明确写到基线包括 Diffusion Policy、一个 flow-matching action generator VLA，以及 GR00T N1；DP 直接在连续动作上训练，其他 VLA 需要做 action-space adaptation。训练资源和流程也较清楚：policy 预训练 100K gradient steps，判别器训练 10K steps，8×NVIDIA A100、总 batch size 64、AdamW。结论声称 Dexora 在基础和灵巧任务上优于强基线，对 OOD shifts 鲁棒，并可通过轻量 action projectors 跨具身转移；但摘录没有给出具体成功率表格，因此只能把“更高成功率”视为论文主张，需等 PDF 核查数值。

#### ⚠️ 风险 / 保留意见

- 高 DoF 系统强依赖专用遥操作硬件和校准流程，复现实验门槛可能高于普通 VLA。
- 摘要和 HTML 摘录未给出具体成功率与统计方差，真实性能差距需要核查表格和失败案例。
- 跨具身下放到低 DoF 的 action projector 是否泛化到未见机器人，目前只能据结论保守判断。

#### 💭 结论与启发

这篇的启发在于，高自由度 VLA 不能只靠扩大模型或数据量，还需要重新设计数据采集接口和动作空间。后续如果做复现，优先不是完整复刻外骨骼，而是抽象出“粗手臂控制 + 细手指控制 + 数据质量筛选”的 pipeline，看它是否能迁移到已有双臂平台。系统设计上，Dexora 提醒我把高 DoF 当作统一上游，再通过投影适配低 DoF，而不是从夹爪策略往上硬扩展。

#### 🔎 读 PDF 先核查

- 数据质量判别器具体以什么正负样本或质量标签训练，是否会偏向特定操作者风格？
- 36-DoF 动作表示如何同步手臂与手指时序，action-space adaptation 对各基线是否公平？
- 从高 DoF 到低 DoF 的 lightweight action projector 是否只在相近具身有效，还是能跨较大 morphology gap？

#### 📌 上传 PDF 后优先看

- 系统与遥操作数据采集章节，特别是外骨骼、Vision Pro hand tracking 和 MuJoCo twin 的同步方式
- 实验主表与 OOD/cross-embodiment 结果表，核查成功率、方差和任务定义
- 数据质量判别器与训练数据组成消融，确认性能增益来自数据筛选还是模型容量

### [2]. RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies [[VIP]] [[HTML]](https://arxiv.org/html/2603.04639) [[PDF]](https://arxiv.org/pdf/2603.04639) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.04639`
* **Authors**: Yinpei Dai, Hongze Fu, Jayjun Lee, Yuejiang Liu, Haoran Zhang, Jianing Yang, Chelsea Finn, Nima Fazeli, Joyce Chai
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，因为 RoboMME 把 VLA 的“记忆能力”从零散案例变成标准化 benchmark，并且有 Chelsea Finn 参与，适合作为长时程 VLA 评测基准跟踪。
* **关键词**: `robot memory` `VLA benchmark` `non-Markovian manipulation` `multi-expert transformer` `long-horizon control`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

长时程机器人任务经常不是当前图像能完全决定下一步动作：机器人可能需要记住擦了几遍桌子、某个物体被遮挡前的位置、书本原来在哪一格，或人类示范中的事件顺序。现有 VLA 虽然开始加入记忆模块，但评测往往局限在自定义任务和不可比设置，导致我们很难判断一种 memory design 到底提升了哪类历史依赖行为。RoboMME 的价值在于把 memory 明确拆成 cognitive dimensions，并把非马尔可夫任务系统化，这对通用策略和 VLA 长时程评测非常关键。

#### ⚙️ 核心方法

RoboMME 包含两层贡献：一是 benchmark，二是用于受控比较的 MME-VLA 模型族。摘录显示，任务被有意构造成非马尔可夫：相同当前观测可能来自不同历史，却要求不同动作，因此模型必须利用过去信息。任务设计参考人类记忆理论，将评测落到 temporal、spatial、object、procedural 四类记忆。模型侧基于共享 VLA backbone，输入语言 token 和当前多视角 RGB image tokens；架构采用类似 pi0/pi05 的 multi-expert transformer，包括融合语言视觉的 VLM expert，以及结合 VLM features 和 denoise timestep 预测动作的 action expert。文中比较 symbolic memory、perceptual memory、recurrent memory 等表示，并研究不同 integration mechanism 如何把 memory 注入策略。当前摘录能确认其使用 blockwise causal attention：block 内双向，block 间因果；但各 memory variant 的具体实现细节、token 长度和训练配方仍需 PDF 核查。

#### 📊 实验与结果

实验目标不是单纯刷成功率，而是严谨评估 history-dependent behavior。摘要称 RoboMME 是 large-scale standardized benchmark，并包含 16 个 manipulation 任务；正文摘录说明所有任务都要求模型利用当前不可见的历史信息。实验还开发了一组 VLA 模型，对 symbolic、perceptual、recurrent memory 以及多种 integration 方式做 controlled comparison。结论给出的关键信息是：没有单一 memory design 在所有设定中稳定占优，symbolic、perceptual 和 recurrent 表示可能各有适用区间。摘录没有提供具体成功率、任务分布或显著性结果，因此目前最稳妥的判断是它提供了评测框架和设计结论，而非某个模型的绝对 SOTA 证明。

#### ⚠️ 风险 / 保留意见

- benchmark 是否覆盖真实长时程机器人中的噪声、恢复与重新规划，还需看任务细节。
- 不同 memory integration 的算力、上下文长度和训练数据量是否公平，摘录证据不足。
- 如果任务是人为构造的非马尔可夫案例，可能高估显式记忆模块相对普通闭环策略的必要性。

#### 💭 结论与启发

这篇适合后续作为 VLA memory 论文的评测锚点。它提醒我不要只问模型有没有历史窗口，而要问它记住的是事件顺序、空间状态、物体身份还是程序化技能。系统复现上，可先抽取四类 memory task taxonomy，用于检查已有策略在遮挡、计数、位置恢复和重复操作中的 failure mode；阅读上应重点看各 memory 表示的归纳偏置，而不是只看总平均分。

#### 🔎 读 PDF 先核查

- RoboMME 的 16 个任务如何分布到 temporal、spatial、object、procedural 四类记忆，每类是否难度均衡？
- symbolic、perceptual、recurrent memory 在哪些任务类型上互有优势，是否能解释为可操作的设计规则？
- blockwise causal attention 和 memory integration 的上下文成本如何随时长扩展，是否适合真实机器人在线部署？

#### 📌 上传 PDF 后优先看

- benchmark/task design 章节，核查四类记忆任务的定义、例子和非马尔可夫构造
- MME-VLA architecture 与 memory variants 章节，重点看表示和注入接口
- 实验结果和消融章节，核查各 memory design 在不同任务类型上的分项表现

### [3]. SCAR: Self-Supervised Continuous Action Representation Learning [[VIP]] [[HTML]](https://arxiv.org/html/2605.16412) [[PDF]](https://arxiv.org/pdf/2605.16412) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.16412`
* **Authors**: Hongjia Liu, Fan Feng, Minghao Fu, Xinyue Wang, Haofei Lu, Biwei Huang
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，因为 SCAR 把动作从原始控制命令提升为跨具身 latent factor，是 world model 和 VLA 跨 embodiment 泛化里很有潜力的接口论文。
* **关键词**: `latent action` `world model` `cross-embodiment` `inverse dynamics` `self-supervised learning`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

世界模型通常把 action 当作环境转移的条件输入，但机器人里的原始命令并不等于真实物理干预：不同 morphology、控制器、延迟、接触状态会让同一 command 产生不同效果，而不同 command 也可能导致相似视觉变化。SCAR 的出发点是，action 应该是解释可控变化的独立表征因子，而不只是某个机器人 API 的低维控制量。对于 Sim2Real、跨具身 VLA 和世界模型训练，这个问题非常核心：如果 action interface 被某个 embodiment 绑定，模型就很难利用其他机器人或虚拟 agent 的数据。

#### ⚙️ 核心方法

SCAR 提出的是 self-supervised continuous action representation learning，核心是 joint inverse-forward dynamics。问题设定中，数据来自多个具身，每条轨迹包含视频序列、具身特定 command sequence 和 embodiment identity。模型假设存在一个未观测的统一 latent action，表示跨具身共享的 controllable factor；原始 command 只是这个 latent action 在某个具身和控制接口下的具体实现。SCAR 从视觉转移中推断 latent action，再用它条件化 world model，目标是让模型学习“导致世界怎么变”的动作，而不是“某台机器人收到了什么命令”。摘要还说明它建立在 pretrained generative backbone 上，并通过 inverse dynamics 从 visual transitions 估计动作表征，通过 forward dynamics 约束该表征能预测后续变化。结论强调该表征应 compact、less embodiment-dependent。当前摘录只能确认总体框架和建模目标，关于具体损失、latent 维度、冻结/微调策略和生成 backbone 类型，需要上传 PDF 后核查。

#### 📊 实验与结果

SCAR 在两个 embodied world-modeling benchmark 上评估：Robotwin 和 Procgen。Robotwin 用于机器人跨具身操作，主任务为 place_a2b_left，设置四种 embodiment；Franka 是低数据 target embodiment，其余三个 embodiment 各提供 300 个 source episodes。评估包含 held-out place_a2b_left 的 target-task prediction，以及 place_a2b_right 的 zero-shot transfer-task prediction。Procgen 用于虚拟具身迁移，虽然动作接口是共享离散动作，但 agent 外观、动力学、交互规则、布局和任务结构不同，因此可检验 latent-action 思路是否超出机器人连续控制。摘录没有给出具体指标数值，因此只能确认实验覆盖低数据 target、source transfer 和 zero-shot task transfer，不能断言提升幅度。

#### ⚠️ 风险 / 保留意见

- latent action 是否真的 embodiment-invariant，可能依赖视觉中可观察到的接触和运动是否充分。
- 只从视觉转移学习动作表征，遇到遮挡、微小力控或不可见接触时可能信息不足。
- 摘录未给出具体损失和结果数值，复现难点集中在 backbone、latent bottleneck 和训练稳定性。

#### 💭 结论与启发

SCAR 对后续选题的启发是，跨具身泛化不一定从统一机器人 URDF 或统一 action tokenizer 开始，也可以从视觉效果反推共享动作语义。做 world model 时，我会优先考虑把 raw action 和 inferred effect action 分开：前者服务控制执行，后者服务预测和迁移。复现可从 Robotwin 小规模做起，比较 raw command conditioning、embodiment-conditioned action 和 SCAR-style latent action 在低数据 target 上的预测误差与迁移表现。

#### 🔎 读 PDF 先核查

- SCAR 如何防止 latent action 编码静态 embodiment identity，而不是只编码可控变化？
- inverse-forward dynamics 中 forward 预测目标是像素、latent feature 还是生成模型内部状态？
- 在 Robotwin 的低数据 Franka 设定中，target episodes 数量是多少，SCAR 对少样本 target 的敏感性如何？

#### 📌 上传 PDF 后优先看

- problem formulation 与 latent action 定义章节，核查变量、假设和 identifiability 讨论
- model/loss 章节，重点看 inverse-forward dynamics、bottleneck 和 generative backbone 连接方式
- Robotwin 与 Procgen 结果表，核查 target prediction、zero-shot transfer 和 ablation

### [4]. WorldArena 2.0: Extending Embodied World Model Benchmarking on Modality, Functionality and Platform [[VIP]] [[HTML]](https://arxiv.org/html/2605.17912) [[PDF]](https://arxiv.org/pdf/2605.17912) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.17912`
* **Authors**: Yu Shang, Yinzhou Tang, Yiding Ma, Zhuohang Li, Lei Jin, Weikang Su, Xin Jin, Zhaolu Wang, Ziyou Wang, Xin Zhang, Haisheng Su, Weizhen He, Wei Wu, Haoyi Duan, Gordon Wetzstein, Xihui Liu, Dhruv Shah, Zhaoxiang Zhang, Zhibo Chen, Jun Zhu, Yonghong Tian, Tat-Seng Chua, Wenwu Zhu, Chen Gao, Yong Li
* **Author Priority**: Extended VIP
* **一句话结论**: 值得优先看，因为 WorldArena 2.0 把 embodied world model 评测从视觉预测扩展到触觉、RL 功能和真实机器人平台，是世界模型方向的基准型论文。
* **关键词**: `world model benchmark` `visuotactile` `reinforcement learning` `sim-to-real` `real robot evaluation`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

世界模型在具身智能里越来越重要，但如果评测只看生成画面是否逼真，就无法判断模型是否能支持规划、策略学习和真实机器人决策。已有 benchmark 多偏 vision-only prediction、offline application 或 simulator evaluation，这会漏掉接触、交互反馈、Sim2Real gap 和闭环控制中的关键问题。WorldArena 2.0 的动机是把 world model 从“预测视频的模块”重新评估为“可服务具身任务的环境模型”，因此关注 modality、functionality 和 platform 三个维度。

#### ⚙️ 核心方法

WorldArena 2.0 是在 WorldArena 基础上的扩展 benchmark。原 WorldArena 已经联合评估 perceptual quality 和 functional utility：开放环视觉预测覆盖视觉质量、运动质量、内容一致性、物理遵循、3D accuracy、controllability 等维度，并把 world model 用作 synthetic data engine、policy evaluator 和 action planner。2.0 的新意是沿三条轴扩展。第一，modality 从 vision-only 推进到 visuotactile，使评测能触及 contact-aware physical interaction。第二，functionality 从离线用途扩展到 interactive reinforcement learning tasks，用于检查世界模型是否能支撑策略学习而非仅做回放预测。第三，platform 从 simulator-based evaluation 扩展到 real-world robotic testbeds，用于暴露 sim-to-real gap。当前摘录中的 method 部分主要重复摘要，未展开具体任务、指标和平台接口，因此只能确认 benchmark 的设计框架和扩展方向。

#### 📊 实验与结果

实验摘录从 WorldArena 到 WorldArena 2.0 的演进讲起，说明旧版已包含 open-loop visual prediction 的多维指标和三类 embodied roles。新版则加入 visuotactile sensory inputs、interactive RL tasks 和 real-world robotic testbeds。结论明确写到，实验覆盖 12 个 state-of-the-art models，并揭示 substantial sim-to-real gaps，同时指出 embodied world model design 的关键改进方向。由于摘录没有列出 12 个模型名称、具体任务、指标数值或真实机器人平台配置，目前只能把这篇作为 benchmark scope 和趋势判断的强信号，不能引用具体排名或性能差距。

#### ⚠️ 风险 / 保留意见

- benchmark 范围很大，若任务和指标设计不够统一，可能难以形成清晰模型排序。
- 真实机器人 testbed 的硬件、控制栈和失败恢复会影响可复现性。
- 摘录未给出模型列表和量化结果，当前只能判断框架价值，不能判断评测结论强度。

#### 💭 结论与启发

这篇最重要的提醒是，world model 论文以后要同时回答三个问题：能预测吗、能帮策略学习吗、能上真实平台吗。后续阅读和选题中，我会把 world model benchmark 分成视觉、接触、规划、RL 和 real-robot 五类证据，不再只接受视频指标。若要做系统设计，可借鉴其三轴评测，把自己的模型先定位为 data engine、policy evaluator、planner 或 RL environment，再选择对应实验。

#### 🔎 读 PDF 先核查

- WorldArena 2.0 的 visuotactile 输入如何采集和表示，触觉指标是预测质量还是下游任务表现？
- interactive RL tasks 中 world model 扮演环境、奖励代理还是策略训练辅助器？
- 12 个 SOTA 模型的失败模式是否集中在 sim-to-real、contact dynamics 还是 long-horizon planning？

#### 📌 上传 PDF 后优先看

- benchmark design 章节，核查 modality、functionality、platform 三轴的具体任务和指标
- model evaluation 结果表，确认 12 个模型、排名方式和分项指标
- real-world robotic testbed 章节，重点看硬件设置、Sim2Real gap 分析和失败案例

### [5]. DyGRO-VLA: Cross-Task Scaling of Vision-Language-Action Models via Dynamic Grouped Residual Optimization [[HTML]](https://arxiv.org/html/2605.17486) [[PDF]](https://arxiv.org/pdf/2605.17486) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.17486`
* **Authors**: Sixu Lin, Yunpeng Qing, Litao Liu, Ming Zhou, Ruixing Jin, Xiaoyi Fan, Guiliang Liu
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，但要带着审稿眼光看，因为 DyGRO-VLA 直指 RL 优化 VLA 的跨任务退化问题，方向重要而方法细节在摘录中仍不充分。
* **关键词**: `RL post-training` `VLA` `cross-task generalization` `residual optimization` `Sim2Real`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

#### 📖 背景与动机

RL 给 VLA 后训练提供了从离线模仿走向环境主动优化的路径，但常见问题是越优化越像单任务专家，损失了 VLA 作为 generalist controller 的多任务迁移能力。DyGRO-VLA 的动机正是这个矛盾：RL 能提升控制精度，却可能让大模型过拟合到窄任务分布。对于机器人 VLA，这不是小问题，因为真实部署往往要求同一策略处理空间变化、物体变化、目标变化和长时程组合任务。论文强调 cross-task feature representations，是想保留共享结构，再在任务差异上做更细粒度优化。

#### ⚙️ 核心方法

当前摘录能确认 DyGRO-VLA 是面向 VLA 的 RL 优化方法，关注 cross-task scaling，并提出 Dynamic Grouped Residual Optimization。摘要称它是一个 two-stage 方法，但后续 HTML 摘录没有展开完整 method，因此不能捏造具体公式或模块细节。可保守理解的是，作者先分析 RL optimizer 让 VLA 任务特化的现象，再通过跨任务特征表示来提升泛化；从题名和限制部分看，方法包含动态分组、残差优化和 routing 机制，routing 依赖已知 task identity 训练出的 task embeddings。限制还说明 online stage 需要 environment interaction，对 reward sparsity 和 hyperparameter tuning 敏感。因此，DyGRO-VLA 更像是在通用 VLA 主干上进行结构化 RL 后训练：通过某种分组残差路径隔离任务特定更新，同时尽量保护跨任务共享特征。具体 grouped residual 的参数位置、动态路由规则、两阶段训练顺序和 reward 设计都必须等 PDF 核查。

#### 📊 实验与结果

实验覆盖 LIBERO 和 RoboTwin2.0。LIBERO 是 lifelong learning benchmark，五个 suites 共 130 tasks；摘录列出 Spatial、Object、Goal、Long 等套件，用于评估空间、物体、目标和长时程能力。RoboTwin2.0 是双臂操作 benchmark，作者选择四个代表任务评估 real-world transfer performance 和 practical deployability。基线包括 Octo、OpenVLA、SpatialVLA、π-FAST* 等大 VLA，也包括 lightweight multi-task policies；所有 baseline 在混合的统一训练集上训练，以评估多任务能力。结论直接列出三点局限：在线训练敏感、routing 依赖任务边界、真实世界评估有限。摘录未给出主结果数值，因此不能确认提升幅度，只能确认实验设计面向跨任务和 Sim2Real。

#### ⚠️ 风险 / 保留意见

- online RL 阶段对稀疏奖励和超参数敏感，机器人交互成本和训练稳定性是主要风险。
- routing 依赖已知任务身份和 task embeddings，开放世界中任务边界模糊时可能退化。
- 真实评估只覆盖少数任务和特定 Sim2Real 设置，泛化结论需要更宽平台验证。

#### 💭 结论与启发

DyGRO-VLA 的价值在于提出一个非常实际的问题：VLA 后训练不能只看单任务成功率，也要防止通用表示被 RL 洗掉。后续做 RL+VLA 时，我会把 cross-task retention 作为核心指标，至少同时报告 seen-task improvement 和 held-out/generalist degradation。复现上应先在 LIBERO 多套件混合训练中验证 grouped residual 是否真的比全量 RL fine-tuning 更稳，再考虑真实双臂迁移。

#### 🔎 读 PDF 先核查

- Dynamic grouped residual optimization 的分组依据是任务、特征子空间还是梯度统计？
- two-stage 训练中哪一阶段负责保护通用表示，哪一阶段负责在线性能提升？
- routing 需要 task identity 时，面对自然语言新任务或组合任务如何选择 residual group？

#### 📌 上传 PDF 后优先看

- method 章节，核查 DyGRO 的两阶段流程、grouping 和 routing 细节
- LIBERO 多任务主结果与消融，重点看跨任务平均分和灾难性退化
- RoboTwin2.0/real-world transfer 章节，核查四个任务、真实平台和 Sim2Real 设置

### [6]. RoboFlow4D: A Lightweight Flow World Model Toward Real-Time Flow-Guided Robotic Manipulation [[HTML]](https://arxiv.org/html/2605.17522) [[PDF]](https://arxiv.org/pdf/2605.17522) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.17522`
* **Authors**: Sixu Lin, Junliang Chen, Huaiyuan Xu, Zhuohao Li, Guangming Wang, Yixiong Jing, Sheng Xu, Runyi Zhao, Brian Sheil, Lap-Pui Chau, Guiliang Liu
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为 RoboFlow4D 把 3D flow world model 做成轻量实时规划接口，直接连接 observation-planning-execution 闭环。
* **关键词**: `4D flow` `world model` `robotic manipulation` `real-time planning` `VLA`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

机器人在 3D 环境中操作时，仅从观察直接输出动作经常会遇到不可解释失败；显式的 pre-execution planning 可以给策略一个中间目标和物理运动约束。已有 predictive flow planner 往往堆叠多个模块，计算开销高，难以实时部署。RoboFlow4D 的目标是把 4D flow 预测变成轻量 world model：从视觉观察和语言指令直接预测未来多帧 3D flows，再用这个显式规划信号指导动作生成。对 VLA 来说，这提供了介于纯端到端动作和重型世界模拟器之间的实用接口。

#### ⚙️ 核心方法

RoboFlow4D 的核心是 end-to-end 4D flow world model。摘录显示，它直接从 2D visual observations 和 textual instructions 预测 goal-oriented multi-frame 3D flows，在物理 3D 空间估计时序运动，从而统一 perception 和 planning。该 flow 输出不是最终动作，而是显式的 3D planning interface，可与 general action policies 集成，形成 observation-planning-execution closed loop。论文强调 slow-fast collaboration：flow prediction 作为较慢的规划模块，action control 作为较快的执行模块，从而兼顾实时性和资源效率。相对模块化 pipeline，它避免先重建、再预测、再规划、再控制的多模型堆叠。当前摘录只能确认总体架构、输入输出和闭环范式；具体 3D flow 表示、从 2D 到 3D 的几何假设、policy conditioning 方式、slow-fast 频率设置和损失函数仍需 PDF 核查。

#### 📊 实验与结果

实验在仿真和真实设置中进行。仿真 benchmark 包括 LIBERO 和 ManiSkill3：LIBERO 有 5 个 suites、130 tasks，摘录列出 Spatial、Object、Goal；ManiSkill3 选取 PushCube、PickCube、StackCube 三个任务。LIBERO 上对比 Octo、CogACT、OpenVLA、TraceVLA、SpatialVLA、4D-VLA 等近期 VLA；ManiSkill3 上对比 BC、ACT、OpenVLA 等 imitation 与 VLA baseline。结论称 RoboFlow4D 作为轻量 end-to-end 4D world model，可用低成本 3D flow-conditioned policy learning 支持实时闭环操作。摘录未给出速度、成功率或真实机器人任务数值，因此实时性和性能优势需要看主表、延迟表和真实任务视频/日志。

#### ⚠️ 风险 / 保留意见

- 从 2D 观察预测 3D flow 可能依赖深度估计或几何先验，遮挡和透明物体会放大误差。
- flow-guided policy 的收益可能与基础 action policy 强弱高度耦合。
- 摘录未提供 latency、资源占用和真实机器人成功率，实时部署主张需要重点核查。

#### 💭 结论与启发

这篇适合启发轻量 world model 的系统设计：不必每次都生成完整未来视频或可微仿真，只要预测对控制有用的 3D motion field。后续如果做 VLA 规划接口，我会比较三种中间表示：language subgoal、future image latent 和 3D flow；RoboFlow4D 提供了一个更接近控制几何的选择。复现优先看 ManiSkill3 三任务，因为任务清晰、可快速验证 flow 是否真的改善动作闭环。

#### 🔎 读 PDF 先核查

- RoboFlow4D 的 multi-frame 3D flow 是在点云、体素、隐式场还是相机空间中表示？
- slow-fast collaboration 的规划频率和控制频率如何设置，延迟是否随任务复杂度增长？
- flow prediction 错误如何影响 action policy，是否有失败检测或 replanning 机制？

#### 📌 上传 PDF 后优先看

- model architecture 章节，核查 2D observation 到 3D flow 的表示和网络接口
- LIBERO/ManiSkill3 主结果与消融，确认 flow guidance 相对直接动作策略的贡献
- real-world 与 efficiency 章节，重点看 latency、算力、闭环频率和真实任务成功率

## Watchlist

### [W1]. OrbiSim: World Models as Differentiable Physics Engines for Embodied Intelligence [[HTML]](https://arxiv.org/html/2605.16395) [[PDF]](https://arxiv.org/pdf/2605.16395)
* **Paper ID**: `2605.16395`
* **Authors**: Jiajian Li, Jingyuan Huang, Junru Gong, Qi Wang, Xiaokang Yang, Yunbo Wang
* **Author Priority**: Standard
* **为什么还值得留意**: OrbiSim 进入 watchlist 是因为它把 world model 明确定位为 fully differentiable physics engine，并尝试把结构化场景资产、神经动力学、视觉生成和 downstream RL 放到同一可微仿真回路中。它没有进入最终精选，主要是因为今天的 VLA/Sim2Real 主线里它更偏世界模型和可微仿真范式，且摘录没有提供足够量化结果来判断相对经典模拟器和已有 world model 的优势强度。后续值得核查它在 Robosuite Push、Isaac Lab Stack、AdaManip Articulated、Physion Drape 上的物理一致性和 RL 梯度收益。
* **证据来源**: arXiv HTML (Introduction, Experiments)

### [W2]. Contrastive Conceptor Activation Steering (COAST): Unlocking Vision-Language-Action Models through Hidden States [[HTML]](https://arxiv.org/html/2605.17144) [[PDF]](https://arxiv.org/pdf/2605.17144)
* **Paper ID**: `2605.17144`
* **Authors**: Miranda Muqing Miao, Subin Kim, Brandon Yang, Lyle Ungar
* **Author Priority**: Standard
* **为什么还值得留意**: COAST 进入 watchlist 是因为它提出用 success/failure rollouts 拟合 conceptor，在 frozen VLA hidden states 上做 activation steering，属于低成本适配 VLA 的有趣路线。没有进最终精选，是因为它更像 inference-time steering/表示干预方法，而不是今天主线中更基础的系统、benchmark 或 world/action model 接口。值得继续看它在 MetaWorld ML45、LIBERO-10 和真实任务上的增益是否稳定，以及跨任务共享 failure geometry 是否可靠。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

### [W3]. StableVLA: Towards Robust Vision-Language-Action Models without Extra Data [[HTML]](https://arxiv.org/html/2605.18287) [[PDF]](https://arxiv.org/pdf/2605.18287)
* **Paper ID**: `2605.18287`
* **Authors**: Yiyang Fu, Chubin Zhang, Shukai Gong, Yufan Deng, Kaiwei Sun, Qiyang Min, Qibin Hou, Yansong Tang, Jianan Wang, Daquan Zhou
* **Author Priority**: Standard
* **为什么还值得留意**: StableVLA 进入 watchlist 是因为它系统讨论视觉扰动下 VLA 鲁棒性，并用 Information Bottleneck Adapter/Fused IB-Adapter 在不加额外数据的情况下抑制视觉 nuisance。没有进最终精选，是因为其贡献更偏 adapter robustness，和今天更优先的高 DoF VLA、记忆基准、latent action、world model 平台化相比，主题覆盖面稍窄。后续应核查 ImageNet-C 式 corruption protocol 是否真实反映机器人视觉退化，以及 LIBERO、CALVIN 上的无扰动性能是否受损。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)

### [W4]. Key-Gram: Extensible World Knowledge for Embodied Manipulation [[HTML]](https://arxiv.org/html/2605.18556) [[PDF]](https://arxiv.org/pdf/2605.18556)
* **Paper ID**: `2605.18556`
* **Authors**: Jingjing Fan, Siyuan Li, Botao Ren, Zhidong Deng
* **Author Priority**: Standard
* **为什么还值得留意**: Key-Gram 进入 watchlist 是因为它尝试把 instruction-side world knowledge 从视觉推理主干中分离出来，用 task-specific key-grams 和外部条件记忆缓解语言视觉竞争，这与 World Action Model 和 VLA 可扩展知识接口有关。没有进入最终精选，是因为方法依赖 deterministic hashed lookup、key-gram 分解和层内调制，摘录尚不足以判断其知识扩展是否真的优于更简单的 prompt/memory adapter。后续重点看 RoboTwin2.0、LIBERO、LIBERO-Plus 和 Piper 双臂真实实验中的泛化与消融。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
