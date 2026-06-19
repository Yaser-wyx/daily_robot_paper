# RoboPulse | 2026-06-19

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 113 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线非常集中：VLA 正在从“当前图像到动作”的反应式策略，转向带记忆、可想象未来、可压缩、可几何泛化、可用少量真实数据修复的系统化机器人基础模型。最终精选保留了三类最值得追踪的方向：World Action Model 的记忆与中间表征，RL/模仿策略的数据效率，以及 VLA 在旋转、视角、物体 OOD 上的泛化机制。VIP 作者里最值得优先跟踪的是 Jiangmiao Pang 与 Huazhe Xu 的 MemoryWAM，以及 Shuran Song 连续两篇围绕在线探索和 action-view augmentation 的工作，它们分别切中长程记忆、RL finetuning、真实数据扩增三条关键线。整体判断是：今天不是单点模型刷榜，而是在补 VLA 走向真实部署前缺失的“长期上下文、有效探索、物理一致数据和几何归纳偏置”。

## 今日信号

- World Action Model 的竞争焦点正在从“能不能生成未来视频”转向“什么样的历史记忆和未来中间表征最够用、最高效”。
- VLA/RL 的样本效率路线开始更重视复用已有生成策略的多模态候选，而不是单纯增加在线 rollouts 或扩大模型。
- Sim2Real 与部署泛化的短板越来越明确地落在物理一致的数据增强、旋转等变换结构、以及失败前检测这些系统接口上。

## Historical Rediscovery

- **Paper**: WEAVER, Better, Faster, Longer: An Effective World Model for Robotic Manipulation [[HTML]](https://arxiv.org/html/2606.13672) [[PDF]](https://arxiv.org/pdf/2606.13672)
  - **Paper ID**: `2606.13672`
  - **来源日期**: 2026-06-18
  - **当时可能被低估的信号**: 当时被 SC3-Eval、DREAM-Chunk、PAIWorld、Cosmos 3 分别占据主线位置挤出，但它同时覆盖 fidelity、consistency、efficiency，并连接 policy evaluation、policy improvement 和 planning，这个组合信号不只是泛泛 world model。
  - **为什么现在值得再看**: 今天再看很合适，因为你的兴趣包含 World Model、World Action Model 和真实机器人操作规划；WEAVER 可能提供一条把机器人世界模型从预测模型推进到策略评估与规划工具的线索。
  - **建议动作**: 加入精读
  - **关键词**: `World Model` `robotic manipulation` `planning` `policy evaluation` `policy improvement`
- **Paper**: Mem-World: Memory-Augmented Action-Conditioned World Models for Persistent Robot Manipulation [[HTML]](https://arxiv.org/html/2606.18960) [[PDF]](https://arxiv.org/pdf/2606.18960)
  - **Paper ID**: `2606.18960`
  - **来源日期**: 2026-06-18
  - **当时可能被低估的信号**: 历史备注里最关键但可能被低估的是 wrist camera 快速运动、末端遮挡导致 world model 遗忘或幻觉的问题；这比一般 rollout 质量更贴近真实机器人部署中的长期闭环失效。
  - **为什么现在值得再看**: 你的方向明确包含 World Model、World Action Model 和长时程操作；Mem-World 值得和 WEAVER、PAIWorld 类工作放在一起看，判断记忆检索和 persistent rollout 是否能补上长任务中的状态连续性。
  - **建议动作**: 加入精读
  - **关键词**: `action-conditioned world model` `long-horizon manipulation` `memory` `persistent rollout` `real deployment`
- **Paper**: Qwen-RobotManip Technical Report: Alignment Unlocks Scale for Robotic Manipulation Foundation Models [[PDF]](https://arxiv.org/pdf/2606.17846)
  - **Paper ID**: `2606.17846`
  - **来源日期**: 2026-06-18
  - **当时可能被低估的信号**: 当时因为只有摘要回退，模型接口、数据规模、对齐损失和真实机器人评估证据无法核查，所以被降级；但 representation、motion、behavior 三维统一 alignment 本身是很强的 VLA scale-up 信号。
  - **为什么现在值得再看**: 如果今天要判断 VLA 是否进入大模型规模化与后训练阶段，这篇应重新看 PDF；它和 VLA、真实机器人操控、数据对齐以及行为层 alignment 都直接相关。
  - **建议动作**: 快速浏览
  - **关键词**: `VLA` `foundation model` `alignment` `robotic manipulation` `scale-up`
- **Paper**: Motion-Focused Latent Action Enables Cross-Embodiment VLA Training from Human EgoVideos [[HTML]](https://arxiv.org/html/2606.18955) [[PDF]](https://arxiv.org/pdf/2606.18955)
  - **Paper ID**: `2606.18955`
  - **来源日期**: 2026-06-18
  - **当时可能被低估的信号**: 历史备注中被低估的信号是 motion-focused latent action 和 motion/background 解耦；虽然当时真实可执行轨迹证据不如更直接的方法，但它可能降低人类视频转机器人训练数据的瓶颈。
  - **为什么现在值得再看**: 你的兴趣包含 VLA 和 World Action Model；如果跨具身 latent action 能从人类视频中形成可迁移动作先验，它会影响 VLA 预训练、动作表示和 sim-to-real 数据闭环。
  - **建议动作**: 继续跟踪
  - **关键词**: `VLA` `latent action` `cross-embodiment` `human ego videos` `pretraining`
- **Paper**: BioProVLA-Agent: An Affordable, Protocol-Driven, Vision-Enhanced VLA-Enabled Embodied Multi-Agent System with Closed-Loop-Capable Reasoning for Biological Laboratory Manipulation [[HTML]](https://arxiv.org/html/2605.07306) [[PDF]](https://arxiv.org/pdf/2605.07306)
  - **Paper ID**: `2605.07306`
  - **来源日期**: 2026-05-11
  - **当时可能被低估的信号**: 当时被认为更像系统集成，定量证据和方法突破不够清晰；但 closed-loop-capable reasoning、状态验证和 VLA 执行同时出现，是真实多步骤机器人部署里值得保留的信号。
  - **为什么现在值得再看**: 你的兴趣包含 VLA、长时程操作和真实部署评测；这篇可作为检查 VLA 系统在具体高约束场景中如何做闭环验证、失败恢复和协议驱动执行的案例。
  - **建议动作**: 快速浏览
  - **关键词**: `VLA` `closed-loop reasoning` `real deployment` `long-horizon manipulation` `laboratory robotics`

## Editor's Picks

### [1]. MemoryWAM: Efficient World Action Modeling with Persistent Memory [[VIP]] [[HTML]](https://arxiv.org/html/2606.20562) [[PDF]](https://arxiv.org/pdf/2606.20562) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.20562`
* **Authors**: Sizhe Yang, Juncheng Mu, Tianming Wei, Chenhao Lu, Xiaofan Li, Linning Xu, Zhengrong Xue, Zhecheng Yuan, Dahua Lin, Jiangmiao Pang, Huazhe Xu
* **Author Priority**: Core VIP
* **一句话结论**: 优先看：MemoryWAM 直接针对长程 manipulation 中 WAM 的记忆-效率矛盾，且有 Jiangmiao Pang、Huazhe Xu 参与，和今天 VLA/world model 主线高度重合。
* **关键词**: `World Action Model` `persistent memory` `long-horizon manipulation` `VLA` `Huazhe Xu`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

这篇的核心问题是：机器人在开放场景中不能只根据当前观测行动，因为关键线索可能早已出现、被遮挡，或需要延迟后才影响决策。现有 VLA 多数把当前图像和语言直接映射到动作，适合短程语义技能，但缺少对历史和环境演化的显式建模。WAM 通过同时建模视觉预测和动作，为“先理解世界如何变化，再控制机器人”提供了更强范式；瓶颈在于，短窗口推理省显存和延迟，却容易丢失非马尔可夫信息，完整 KV 历史又会让长任务成本快速增长。MemoryWAM 因此切中一个很现实的部署矛盾：真实长程任务需要记忆，但机器人控制又不能承受无限增长的推理负担。

#### ⚙️ 核心方法

MemoryWAM 的方法可以理解为给 WAM 加一个混合持久记忆系统，而不是简单扩大上下文窗口。摘录明确说明，它同时保留高保真的短期上下文、任务起点或事件边界附近的 anchor frames，以及压缩后的 gist tokens，用来在长程任务中保存“足够有用”的历史信息。模型基于 pretrained Wan2.2-TI2V-5B，沿用其 video DiT、T5 文本编码器和 3D causal video VAE；这说明它不是从零训练机器人模型，而是在强视频生成骨干上接入动作和记忆机制。推理时，短窗口负责当前局部规划，anchor frames 提供早期状态约束，gist tokens 承担长期历史的抽象压缩。相对已有 WAM，新意不在“把所有历史都塞进 Transformer”，而是在历史信息保真度和计算成本之间做结构化分层。当前摘录只能确认这些模块级设计，不能确认每个 token 的具体构造细节、损失函数形式或完整维度配置。

#### 📊 实验与结果

实验部分围绕效率、策略表现和设计有效性展开。摘录显示作者先描述模型架构、训练设置和推理协议，再系统比较不同记忆机制在推理延迟、GPU memory overhead 和任务表现上的差异；随后在 memory-dependent manipulation simulation 和 real-world tasks 上评估，并做 hybrid memory 各组件消融。结论称 MemoryWAM 在仿真和真实记忆依赖任务中优于竞争 VLA 与 WAM baseline，同时达到 practical inference efficiency。需要注意的是，摘录没有给出具体成功率、延迟或显存数字，因此只能把结果解读为作者主张的综合优势，上传 PDF 后应优先核查量化幅度和任务难度。

#### ⚠️ 风险 / 保留意见

- 长程记忆是否真正来自 gist/anchor 机制，而不是视频骨干或数据分布优势，需要看消融是否足够强。
- 真实机器人任务如果数量少或脚本化程度高，可能高估了 persistent memory 对开放部署的收益。
- 基于大型视频 DiT 的系统即使优化记忆，仍可能有训练和部署资源门槛。

#### 💭 结论与启发

这篇给后续系统设计的启发是：长程机器人策略不一定要在单一上下文表示里二选一，而可以把历史拆成近期细节、关键起点和压缩语义三层。对于复现，最值得先做的是把同一 WAM backbone 接入不同记忆策略，单独测 latency、memory 和任务成功率的 trade-off。对选题而言，MemoryWAM 把 WAM 从“未来视频生成”推进到“可部署的历史管理”，这可能成为长任务 VLA 的基础接口。

#### 🔎 读 PDF 先核查

- gist tokens 是如何从历史观测中形成和更新的，是否会在关键细节被压缩掉时导致错误动作？
- anchor frames 具体选择任务起点、事件边界还是固定位置，对不同长程任务是否稳定有效？
- MemoryWAM 的推理成本相对完整 KV cache 和短窗口 WAM 的真实下降幅度是多少？

#### 📌 上传 PDF 后优先看

- 方法章节中的 hybrid memory 结构与推理流程
- 效率实验：latency、GPU memory overhead 与窗口长度关系
- 真实机器人与 memory-dependent simulation 的任务定义、baseline 和消融

### [2]. DF-ExpEnse: Diffusion Filtered Exploration for Sample Efficient Finetuning [[VIP]] [[HTML]](https://arxiv.org/html/2606.19656) [[PDF]](https://arxiv.org/pdf/2606.19656) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.19656`
* **Authors**: Calvin Luo, Chen Sun, Shuran Song
* **Author Priority**: Core VIP
* **一句话结论**: 优先看：DF-ExpEnse 把 diffusion policy 的多模态候选和 critic ensemble 的不确定性结合起来，是 RL finetuning VLA/生成控制策略时很实用的探索模块。
* **关键词**: `diffusion policy` `reinforcement learning finetuning` `exploration` `critic ensemble` `Shuran Song`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

机器人策略如果只靠离线 imitation learning，往往继承示范数据的覆盖范围；一旦进入新状态，策略可能没有足够经验修正。自然路线是用 pretrained generative control policy 初始化，再通过在线 RL finetuning 适配自采经验，但在线机器人数据昂贵，探索质量直接决定样本效率。扩散策略等生成控制模型已经能表达多模态动作分布，意味着它们不只是行为克隆器，也能产生多种可执行候选用于探索。传统 RL 探索如果直接在连续动作空间加噪，容易产生低质量动作；DF-ExpEnse 的动机是用生成策略先过滤出“像动作”的候选，再用 critic ensemble 选择既有价值又有探索兴趣的动作。

#### ⚙️ 核心方法

DF-ExpEnse 是一个在线经验采集阶段的探索策略，可叠加在多种对 pretrained diffusion policy 做 RL finetuning 的算法上。每个时间步，它先从扩散策略中独立采样一组候选动作，这利用了生成控制策略的多模态建模能力，使候选集落在离线行为先验附近。然后它复用 RL 训练中已有的 Q-value function ensemble，对每个候选动作评估两个因素：价值估计和 critic disagreement。前者防止探索偏离可完成任务的区域，后者提供不确定性或探索兴趣。最终动作来自二者线性组合下的候选选择。摘录还说明该方法可扩展到 fleet setting，让多个 agent 之间通信探索信息，形成集体探索。重要的是，DF-ExpEnse 只在在线经验收集时使用；评估 finetuned policy 时关闭该模块，因此不会给测试时增加额外计算。当前摘录不能确认完整目标函数、ensemble size 或候选数的具体设置。

#### 📊 实验与结果

实验目标是验证 DF-ExpEnse 是否提升 pretrained diffusion policy 经 RL finetuning 后的样本效率。摘录明确说明它可与不同底层 RL finetuning 技术结合，并以 DSRL (Noise Aliasing) 作为主要算法之一。作者强调评估 rollout 时不启用 DF-ExpEnse，以保证和其他 baseline 的测试时计算公平。实验部分会描述 RL 算法、任务环境、模型组件和标准超参数，但摘录没有提供具体 benchmark 名称、成功率曲线或样本效率倍数。因此目前只能确认它的实验设计关注在线采样质量，而不能引用具体性能提升幅度。

#### ⚠️ 风险 / 保留意见

- 方法依赖 critic ensemble 的不确定性质量；早期 critic 未训练好时可能误导探索。
- 候选动作来自 diffusion policy，若离线先验缺失关键行为模式，探索仍可能受限。
- fleet extension 很有吸引力，但摘录不足以判断通信成本和多机器人真实可行性。

#### 💭 结论与启发

这篇对 RL+VLA 的启发是：探索不一定要在原始连续动作空间盲目扰动，可以先由生成策略给出行为先验内的候选，再用价值和不确定性做选择。后续复现可以先把它实现成 diffusion policy rollout wrapper，而不是改动整个训练框架。系统设计上，DF-ExpEnse 提供了一个干净接口：训练时改善数据采集，测试时不改变策略结构，这对真实机器人部署尤其有吸引力。

#### 🔎 读 PDF 先核查

- 价值估计和 critic disagreement 的线性组合权重如何设定，是否对任务和训练阶段敏感？
- 候选动作数量增加带来的在线控制延迟是否会影响真实机器人 rollouts？
- DF-ExpEnse 相比简单 entropy/noise exploration 的收益主要来自 diffusion 候选质量还是 ensemble uncertainty？

#### 📌 上传 PDF 后优先看

- 方法章节中 candidate sampling 与 exploration interest 计算
- RL finetuning 实验的学习曲线和样本效率对比
- fleet setting 扩展及其是否有独立实验支持

### [3]. One Demo is Worth a Thousand Trajectories: Action-View Augmentation for Visuomotor Policies [[VIP]] [[HTML]](https://arxiv.org/html/2606.19586) [[PDF]](https://arxiv.org/pdf/2606.19586) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.19586`
* **Authors**: Chuer Pan, Litian Liang, Dominik Bauer, Eric Cousineau, Benjamin Burchfiel, Siyuan Feng, Shuran Song
* **Author Priority**: Core VIP
* **一句话结论**: 优先看：1001 Demos 用真实 eye-in-hand demonstration 生成物理可行动作和视角序列，是 Sim2Real 数据增强里非常具体、可复现价值高的一篇。
* **关键词**: `action-view augmentation` `Sim2Real` `fisheye camera` `3D Gaussians` `Shuran Song`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

这篇解决的是 visuomotor policy 的空间鲁棒性问题：同一个技能在训练时看起来稳定，但机器人初始位姿稍变、场景里多出障碍物，观测就会 OOD，随后状态分布偏移并积累成执行失败。常规做法是让人类在不同空间配置下反复采集同一技能，这虽然有效，却昂贵且难规模化。论文提出从单条或少量真实 eye-in-hand demonstration 中自动扩增轨迹级数据，让策略见到更多初始相机位姿和带障碍情形。它的重要性在于，Sim2Real 里很多增强只改图像不改动作，或只改动作不保证视觉一致；1001 Demos 试图同时生成真实感 fisheye observation 和物理可行 action trajectory。

#### ⚙️ 核心方法

1001 Demos 是离线数据增强框架，输入来自带单个 fisheye camera 的便携式 parallel gripper，包含 scene scanning 和 task demonstration 的 fisheye video pair。第一步，它用 fisheye image sequences 重建场景点云用于 motion planning，同时构建 fisheye 3D Gaussians 表示用于 novel view rendering。第二步，给定场景点云和原始示范轨迹，它在同一场景中规划从不同初始 camera poses 出发的平滑、collision-free 轨迹，并渲染这些轨迹对应的新视角观测。第三步，它还可通过 scene editing 加入障碍物，生成 obstacle-avoiding demonstrations。方法的新意在于把动作增强和视角增强绑定起来：不是只做图像风格扰动，而是生成轨迹级、eye-in-hand、fisheye、物理可行的 action-view paired demonstrations。当前摘录能确认三模块流程，但不能确认轨迹优化目标、碰撞检测细节或 3D Gaussian 训练参数。

#### 📊 实验与结果

实验覆盖真实和仿真环境，关注三个问题：action-view augmentation 是否提升对未见初始配置和障碍的鲁棒性、怎样做增强、以及增强多少最有利。仿真中使用 RoboMimic 的 square peg-in-hole 任务，以 200 条专家 demonstrations 为基础数据；作者把 wrist pinhole observation 转成 GoPro fisheye lens 参数下的 fisheye image，FoV 为 155 度，并对比无增强、ground-truth novel-view rendering、Aug Action Only 和 SPARTN 等基线。结论称该框架能赋予策略原始 demo 中没有展示的 obstacle avoidance 和 novel initial configuration robustness。摘录没有给出具体成功率，因此应保守看作强主张，需核查完整表格。

#### ⚠️ 风险 / 保留意见

- 依赖场景重建和 novel view rendering 质量，反光、透明物体或动态场景可能削弱增强可信度。
- 从原始轨迹生成新轨迹时，任务语义是否始终保持不变需要逐任务验证。
- 仿真 fisheye 转换与真实 fisheye 采集之间仍可能存在感知分布差异。

#### 💭 结论与启发

这篇最有价值的启发是把数据增强从“像素层”提升到“动作-视角-几何一致”的轨迹层。复现时可以先从单任务入手，验证不同初始位姿下的规划轨迹和渲染观测是否足以训练 diffusion policy 或 ACT 类策略。选题上，它补齐了 VLA/visuomotor policy 面对 OOD 初始状态时的数据短板，也提示后续可把 3D reconstruction、motion planning 和 policy learning 更紧地结合起来。

#### 🔎 读 PDF 先核查

- 从单条 demonstration 生成的替代轨迹是否保持同一任务的接触时序和操作语义？
- obstacle-avoiding demos 中的障碍是如何编辑进场景并影响 motion planning 的？
- 增强数量增加时性能何时饱和，是否会因渲染伪影或轨迹偏差带来负迁移？

#### 📌 上传 PDF 后优先看

- 3D scene reconstruction、fisheye 3D Gaussians 与 novel view rendering 流程
- RoboMimic square 的增强策略对比和数量消融
- 真实机器人任务中 novel initial configuration 与 obstacle robustness 的评估设置

### [4]. EquiVLA: A General Framework for Rotationally Equivariant Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2606.19784) [[PDF]](https://arxiv.org/pdf/2606.19784) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.19784`
* **Authors**: Thien-Loc Ha, Quang-Tan Nguyen, Trong-Bao Ho, Long Dinh, Minh Duc Nguyen, Gia-Binh Nguyen, Pham Tri Quang, Minh N. Vu, Duy M. H. Nguyen, An Thai Le, Ngo Anh Vien
* **Author Priority**: Standard
* **一句话结论**: 优先看：EquiVLA 把旋转等变性系统接入 frozen VLM + flow-matching action head，是提升 VLA 几何泛化的清晰框架。
* **关键词**: `equivariance` `VLA` `SO(2)` `flow matching` `GR00T N1.5`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

VLA 依靠大规模视觉语言预训练获得语义泛化，但在机器人操作中，几何泛化同样关键。很多任务在物体旋转、夹爪朝向和空间布局变化下本质相同，普通 VLA 却需要更多数据覆盖这些朝向变化。问题根源是模型没有利用 manipulation 中天然存在的旋转对称性，只把不同朝向当作不同视觉模式学习。EquiVLA 的重要性在于，它没有要求重训大型 VLM，而是在 frozen vision-language backbone 和 flow-matching Diffusion Transformer action head 的接口处注入 equivariance。对真实机器人而言，这种归纳偏置可能比单纯扩数据更可控，也更适合低数据 finetuning。

#### ⚙️ 核心方法

EquiVLA 由两个关键模块构成。EquiPerceptor 从 frozen ViT features 中产生近似 SO(2)-equivariant 的视觉表示，目标是在不改动大规模 VLM 主体的情况下，让视觉侧对图像平面旋转具有结构化响应。EquiActor 是一个精确 SO(2)-equivariant 的 flow-matching Diffusion Transformer action head，用于把等变视觉条件映射到等变动作序列。两者合在一起，形成从 camera observation 到 predicted action sequence 的近似 equivariance chain。摘录说明框架适用于任何“frozen vision-language backbone + flow-matching DiT action head”的架构，并在 GR00T N1.5 上实例化。相对已有方法，它不是把数据旋转增强当作外部技巧，而是把旋转结构写进视觉适配器和动作头。当前摘录不能确认 EquiPerceptor 的具体群卷积或 symmetrization 实现细节，但能确认它的设计目标和系统位置。

#### 📊 实验与结果

实验使用 LIBERO、CALVIN 仿真 benchmark，以及 Mobile ALOHA 真实机器人任务。主要对比三种模型：GR00T N1.5 非等变 baseline，仅替换 action head 的 GR00T N1.5 + EquiActor，以及同时加入 EquiPerceptor 的 EquiVLA。LIBERO 设置包括 LIBERO-10、Goal、Object、Spatial 四个 suite，每个 suite 10 个任务、每任务约 40 条 demonstration；在 relative 和 absolute end-effector control 下评估，每个任务 50 次 rollout，每个 suite 500 次，并跨两个 seeds 报告成功率。作者还引用 OpenVLA、SmolVLA 等 published results 作参考，但提示设置不同。摘录结论称 EquiVLA 优于非等变 baseline，且收益随数据规模变化。具体数值需查 PDF。

#### ⚠️ 风险 / 保留意见

- SO(2) 旋转等变更适合平面旋转，对复杂 3D 姿态变化的覆盖可能有限。
- EquiPerceptor 只是近似等变，视觉 backbone 冻结后是否存在不可控破坏需要实证。
- 引用其他 VLA published results 时设置不同，不能作为严格 apples-to-apples 比较。

#### 💭 结论与启发

EquiVLA 的启发是：VLA 泛化不一定只靠更大模型或更多数据，机器人任务中的几何结构可以作为模型接口级约束。复现时最值得做的是先只替换 action head，测 EquiActor 单独收益，再加入 visual adapter 看端到端链条是否真的提升旋转泛化。对系统设计而言，它提供了一个低侵入方案：保留 frozen VLM 语义能力，同时在动作生成侧加入几何归纳偏置。

#### 🔎 读 PDF 先核查

- EquiPerceptor 如何从 frozen ViT features 构造近似 SO(2)-equivariant 表示，误差如何度量？
- EquiActor 的精确等变性在连续动作 chunk 和不同控制模式下如何保持？
- 在 Mobile ALOHA 真实任务中，性能提升是否主要来自旋转泛化而非其他训练差异？

#### 📌 上传 PDF 后优先看

- EquiPerceptor 与 EquiActor 的数学定义和架构接口
- LIBERO relative/absolute control 下的严格 baseline 对比
- CALVIN 与 Mobile ALOHA 中针对旋转变化的任务设计和消融

### [5]. ImageWAM: Do World Action Models Really Need Video Generation, or Just Image Editing? [[HTML]](https://arxiv.org/html/2606.19531) [[PDF]](https://arxiv.org/pdf/2606.19531) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.19531`
* **Authors**: Yuyang Zhang, Wenyao Zhang, Zekun Qi, He Zhang, Haitao Lin, Jingbo Zhang, Yao Mu, Xiaokang Yang, Wenjun Zeng, Xin Jin
* **Author Priority**: Standard
* **一句话结论**: 优先看：ImageWAM 挑战“WAM 必须生成视频”的默认设定，用单帧 image editing 作为世界-动作中间表征，方向非常值得跟进。
* **关键词**: `ImageWAM` `image editing` `World Action Model` `endpoint frame` `RoboTwin`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

近期 WAM 常把视频生成当作视觉世界建模和机器人控制之间的桥梁：先想象未来视频，再用未来指导动作。这很直观，因为视频预训练能学到运动、交互和场景演化。但完整视频预测对机器人控制未必最优：多帧 future tokens 让推理变贵，模型容量被背景、外观细节和时间平滑占用，长程想象还可能积累错误并误导动作。ImageWAM 的问题意识非常尖锐：机器人策略到底需要完整未来视频，还是只需要一个足以表达任务结果的视觉中间状态？这对 WAM 的效率和表征设计都有直接影响。

#### ⚙️ 核心方法

ImageWAM 把 WAM 的中间视觉推理从“生成未来轨迹视频”改成“编辑当前图像得到 endpoint frame”。形式上，在每个时间步，机器人接收当前 image observation 和 task instruction，预测一个 action chunk。传统 video WAM 会预测多帧 future visual trajectory；ImageWAM 只预测一个 source-conditioned endpoint frame，用它概括任务指定的视觉变换，再供 action expert 预测动作。架构上，它基于 image editing backbone，如 OmniGen2、Ovis-U1、Flux2 这类变体模型，并在 image editing branch 上接入 action expert。这个设计的关键假设是：图像编辑任务天然要求视觉理解和生成，单帧目标状态已经包含足够动作相关信息，而无需建模完整中间过程。相对视频 WAM，新意在于压缩中间表征并减少对 action-irrelevant temporal detail 的建模。当前摘录不能确认 action expert 的完整结构和训练损失细节。

#### 📊 实验与结果

实验覆盖 LIBERO、LIBERO-Plus、RoboTwin 2.0 以及若干真实 manipulation tasks。摘录强调 ImageWAM 不使用额外 embodied policy pretraining，只在 downstream benchmark demonstrations 上训练。LIBERO 按 Spatial、Object、Goal、LIBERO-Long 四个标准 suite 训练，每个 suite 包含 500 条 expert demonstrations、10 个任务；LIBERO-Plus 使用原始 LIBERO 训练 demonstrations，不加入 augmented LIBERO-Plus training data，并按 LIBERO-Plus protocol 评估。RoboTwin 2.0 用于大规模双臂仿真评估。结论明确给出 ImageWAM 在 RoboTwin (Random) 上达到 93.56% success rate。其他具体对比幅度需查全文。

#### ⚠️ 风险 / 保留意见

- 单帧 endpoint 可能不足以表达需要中间接触过程、避障或时序约束的任务。
- image editing backbone 的预训练分布与机器人 wrist/external views 是否匹配仍需验证。
- 高成功率若主要来自仿真 benchmark，真实机器人泛化边界还需看任务细节。

#### 💭 结论与启发

ImageWAM 给 WAM 研究一个重要反向问题：世界模型不必默认越完整越好，动作预测可能只需要紧凑、任务相关的未来状态。对复现而言，可以把视频生成 WAM 和 endpoint image WAM 放在同一 action head 下对比 latency、成功率和失败模式。对选题而言，这篇可能推动 WAM 从“生成质量竞赛”转向“控制有用性竞赛”，尤其适合资源受限的实时机器人系统。

#### 🔎 读 PDF 先核查

- endpoint frame 是作为显式生成图像输入 action expert，还是以隐状态形式参与动作预测？
- 在长程或接触密集任务中，单帧未来是否会丢失关键时序信息？
- ImageWAM 相比视频 WAM 的推理成本下降是否与成功率提升同时成立？

#### 📌 上传 PDF 后优先看

- ImageWAM 架构中 image editing branch 与 action expert 的连接方式
- LIBERO/LIBERO-Plus 与 RoboTwin 的 baseline 表格和消融
- 真实机器人任务中 endpoint prediction 失败案例与视频 WAM 对比

### [6]. Pose6DAug: Physically Plausible Multi-view Object Swapping for Robot Data Augmentation [[PDF]](https://arxiv.org/pdf/2606.20118) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.20118`
* **Authors**: Jonghoon Lee, Seong Hyeon Park, Byungwoo Jeon, Minha Lee, Jinwoo Shin
* **Author Priority**: Standard
* **一句话结论**: 值得进精选但需保守阅读：Pose6DAug 只有摘要回退信息，不过它针对 VLA 物体 OOD 的 failure-driven 多视角物理一致增强，和 Sim2Real 痛点高度相关。
* **关键词**: `Pose6DAug` `Sim2Real` `object swapping` `multi-view consistency` `OOD objects`
* **证据来源**: Abstract fallback

#### 📖 背景与动机

VLA policies 在通用 manipulation 上很有潜力，但遇到训练分布外的新物体时仍容易失败，尤其当外观或几何和训练对象差异明显。传统补救方式是针对每个 failure case 再采集多视角 teleoperation demonstrations，但这会把部署成本推高到难以持续。Pose6DAug 的动机是把失败修复变成数据重用问题：既然成功 episode 已经包含物理有效的 action trajectory 和 calibrated multi-view observations，那么能否在不重新采集数据的情况下，把被操作物体替换成 failure object，得到新的、有物理依据的示范？它重要在于直面 VLA 的 OOD object generalization，并试图避免纯 2D 编辑破坏多视角一致性。

#### ⚙️ 核心方法

当前摘录只能确认 Pose6DAug 是一个 failure-driven data augmentation framework，用 policy 自己的 successful episodes 来生成针对 failure modes 的 demonstrations，而不需要额外数据采集。它的关键操作是保留原成功 episode 中的 action trajectory 和 calibrated multi-view observation structure，只替换 manipulated object，从而得到新的物理 grounded demonstrations。摘要还明确指出，naive 2D video editing 会破坏 multi-view consistency，因此 Pose6DAug 应该包含某种 6D pose 或多视角约束下的 object swapping 机制，以保证新对象在不同相机视角中几何一致。由于没有 HTML 方法摘录，不能具体断言它如何估计姿态、如何渲染遮挡、如何处理接触几何或如何筛选物理合理轨迹。保守理解是：它把成功轨迹作为动作骨架，把失败物体作为替换目标，在多视角标定约束下生成 VLA finetuning 数据。

#### 📊 实验与结果

目前只有摘要回退，因此实验细节证据不足。可以确认的是，论文目标是让 VLA policies 在 novel、out-of-distribution objects 上更稳，并将方法定位为无需新数据采集的 failure-driven augmentation。摘要没有提供 benchmark 名称、机器人平台、任务数量、成功率或对比基线，因此不能引用任何具体实验结论。它进入精选的原因不是已有摘录显示了强量化结果，而是问题设置与今天 Sim2Real/VLA 数据效率主线高度契合，并且“successful episode to failure-mode demo”的机制有较强系统价值。上传 PDF 后必须优先核查实验证据是否支撑这一主张。

#### ⚠️ 风险 / 保留意见

- 只有摘要信息，方法细节和实验可信度目前无法充分判断。
- 保留原轨迹替换新物体时，若新物体几何、质量或可抓取区域差异大，物理可行性可能不成立。
- 多视角一致编辑仍可能在遮挡、接触和光照处产生伪影，影响 VLA 学习。

#### 💭 结论与启发

Pose6DAug 的启发在于把部署失败转化为有针对性的数据增强，而不是把每个失败都交给人工重新 teleoperate。后续如果做 VLA OOD object repair，可以优先考虑记录成功轨迹、相机标定和对象 6D pose，让数据闭环具备可编辑性。它也提醒我们，VLA 数据增强不能只看单视角图像真实感，多视角一致性和动作轨迹物理合理性才是能否迁移到真实机器人上的关键。

#### 🔎 读 PDF 先核查

- 对象替换如何保证 6D pose、多视角遮挡和接触关系的一致性？
- 当 failure object 的几何尺寸明显不同于 successful episode 中的对象时，原 action trajectory 如何仍然物理可行？
- 增强数据是用于 finetuning VLA、重训练策略，还是作为失败恢复数据闭环的一部分？

#### 📌 上传 PDF 后优先看

- 方法章节中的 6D pose object swapping 与 multi-view rendering/consistency 机制
- failure-driven 数据选择流程和无需新采集的具体假设
- novel OOD object 实验设置、真实机器人结果和失败案例

## Watchlist

### [W1]. Mem-World: Memory-Augmented Action-Conditioned World Models for Persistent Robot Manipulation [[HTML]](https://arxiv.org/html/2606.18960) [[PDF]](https://arxiv.org/pdf/2606.18960)
* **Paper ID**: `2606.18960`
* **Authors**: Zirui Zheng, Jiaqian Yu, Xiongfeng Peng, jun shi, Mingyi Li, Chao Zhang, Weiming Li, Dong Wang, Huchuan Lu, Xu Jia
* **Author Priority**: Standard
* **为什么还值得留意**: Mem-World 和 MemoryWAM 同样关注 persistent world modeling，但更偏多视角 action-conditioned video rollout，尤其针对 wrist camera motion 和 end-effector occlusion。它进入 watchlist 是因为 W-VMem 的 surfel-indexed 记忆与几何检索很值得看，但今天最终精选中 MemoryWAM 更直接覆盖 WAM 记忆-效率-策略执行闭环，且有核心 VIP 作者。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. Finetuning Vision-Language-Action Models Requires Fewer Layers Than You Think [[HTML]](https://arxiv.org/html/2606.20246) [[PDF]](https://arxiv.org/pdf/2606.20246)
* **Paper ID**: `2606.20246`
* **Authors**: Gia-Binh Nguyen, Trong-Bao Ho, Thien-Loc Ha, Khoa Vo, Philip Lund Møller, Quang T. Nguyen, Long Dinh, Tuan Dam, Vu Duong, Tung M. Luu, Trung Le, Tran Nguyen Le, Minh Vu, An Thai Le, Ngan Le, Daniel Sonntag, James Zou, Jan Peters, Duy M. H. Nguyen, Ngo Anh Vien
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇关于 CKA-guided layer pruning 的 VLA 压缩非常实用，结论声称 30-50% transformer layers 可移除且保持竞争性能，适合后续做部署效率专题。它没有进最终精选，是因为今天主线更偏 world/action modeling、RL exploration 和 Sim2Real 数据机制；压缩虽重要，但与 VLA 行为能力机制的关系稍间接。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

### [W3]. Co-VLA: Coordination-Aware Structured Action Modeling for Dual-Arm Vision-Language-Action Systems [[HTML]](https://arxiv.org/html/2606.20285) [[PDF]](https://arxiv.org/pdf/2606.20285)
* **Paper ID**: `2606.20285`
* **Authors**: Yandong Wang, Jiaqian Yu, Xiongfeng Peng, Lu Xu, Yamin Mao, Weiming Li, Jaewook Yoo, Dongwook Lee, Daehyun Ji, Mingbo Zhao, Chao Zhang
* **Author Priority**: Standard
* **为什么还值得留意**: Co-VLA 针对双臂 VLA 的显式协调建模，提出 Structured Action Expert、Latent-Aware Controller 和 Co-Motion 数据范式，适合关注 bimanual deployment 的读者。它留在 watchlist，是因为摘要和摘录显示方法工程性强，但相比 EquiVLA、ImageWAM、MemoryWAM，它对今天核心的 world model/RL/Sim2Real 主线贡献略窄。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. Tri-Info: Generalizable, Interpretable Failure Prediction for VLA Models via Information Theory [[HTML]](https://arxiv.org/html/2606.19998) [[PDF]](https://arxiv.org/pdf/2606.19998)
* **Paper ID**: `2606.19998`
* **Authors**: Jinghan Yang, Yunchao Zhang, Wang Yuan, Haolun Wan, Jiaming Zhang, Zhengyang Hu, Yanchao Yang
* **Author Priority**: Standard
* **为什么还值得留意**: Tri-Info 用信息论信号做 VLA failure prediction，覆盖六个 VLA、三个 benchmark，并包含真实 ALOHA 轨迹，是安全部署方向的重要候选。它没有进入最终精选，主要因为它是监测与预警模块，不是策略学习、WAM 或数据增强本体；但若后续做 VLA deployment safety，应优先补读。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
