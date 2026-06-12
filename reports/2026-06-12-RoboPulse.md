# RoboPulse | 2026-06-12

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 88 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线很清楚：VLA 正在从“直接从当前观测预测动作”转向更强的测试时引导、显式记忆、世界模型预测和可执行动作联合建模。最终精选覆盖了三条互补路径：用 Flow Reversal Steering 从通用策略的行为先验里挖出可用动作，用 Mana/EgoEngine 扩展高质量灵巧操作数据与 sim-to-real 管线，用 WEAVER/MaskWAM/μVLA 分别补上世界模型、目标 grounding 和部分可观测记忆。核心 VIP 里 Chelsea Finn、Sergey Levine、Pieter Abbeel 的两篇最值得优先跟踪，分别代表通用机器人策略的测试时改进和灵巧工具操作的 sim-to-real；扩展 VIP 里 Danfei Xu 参与的 EgoEngine 也值得关注，因为它直接瞄准人类视频到机器人示范的规模化瓶颈。整体看，今天不是单点 benchmark 刷分，而是在回答一个系统问题：如何让大模型机器人策略在新任务、长时序、接触丰富和观测不完整条件下仍然可改进、可落地。

## 今日信号

- VLA 的下一阶段重点不只是扩大数据和模型，而是把测试时 steering、记忆状态和世界模型预测变成可操作的策略改进接口。
- World Action Model 正在从纯 RGB 未来预测走向对象 mask、事件谓词、goal-progress value 与 action chunk 的联合表示，以减少预测和控制之间的断层。
- Sim2Real 与数据生成的重心正在向高保真灵巧操作、人类视频转换和触觉/接触模态扩展，说明通用策略的短板越来越集中在物理交互细节。

## Historical Rediscovery

- **Paper**: Making Foresight Actionable: Repurposing Representation Alignment in World Action Models [[HTML]](https://arxiv.org/html/2606.12217) [[PDF]](https://arxiv.org/pdf/2606.12217)
  - **Paper ID**: `2606.12217`
  - **来源日期**: 2026-06-11
  - **当时可能被低估的信号**: 当时被压低排序的信号是：它已经用 attention analysis 和 causal intervention 指向 action decoder 关注无关区域的问题，而不只是提出一个更好看的预测模型。
  - **为什么现在值得再看**: 现在值得再看，因为你的兴趣明确包括 World Action Model；AGRA 对 WAM 表征对齐、OOD humanoid 设置和 DINOv2/SigLIP 对齐消融都可能提供可借鉴的诊断框架。
  - **建议动作**: 加入精读
  - **关键词**: `World Action Model` `representation alignment` `action decoder` `OOD humanoid` `VLA interface`
- **Paper**: DAM-VLA: Decoupled Asynchronous Multimodal Vision Language Action model [[HTML]](https://arxiv.org/html/2606.12105) [[PDF]](https://arxiv.org/pdf/2606.12105)
  - **Paper ID**: `2606.12105`
  - **来源日期**: 2026-06-11
  - **当时可能被低估的信号**: 当时可能被低估的是异步 latent buffer 的系统价值：25Hz RGB 与 100Hz proprioception/force 不强行同步，直接回应真实接触任务中的频率错配。
  - **为什么现在值得再看**: 现在值得再看，因为 RL+VLA 和真实部署评测都需要处理视觉、语言、本体、力觉的不同时间尺度；Franka contact-rich tasks 能帮助判断异步 VLA 是否比同步 token 化更稳。
  - **建议动作**: 加入精读
  - **关键词**: `VLA` `asynchronous multimodal` `force feedback` `contact-rich manipulation` `real robot control`
- **Paper**: Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics [[HTML]](https://arxiv.org/html/2606.12365) [[PDF]](https://arxiv.org/pdf/2606.12365)
  - **Paper ID**: `2606.12365`
  - **来源日期**: 2026-06-11
  - **当时可能被低估的信号**: 当时被低估的信号是 noise-dependent data usage 同时覆盖 noisy trajectories、sim-to-real gap、task mismatch 三类分布偏移，而不是只做常规 diffusion policy 改进。
  - **为什么现在值得再看**: 现在值得再看，因为 VLA/RL+VLA 共训练会越来越依赖混杂、失败和跨域数据；这篇可能为数据清洗、负样本利用和 Sim2Real 数据混合提供方法参考。
  - **建议动作**: 加入精读
  - **关键词**: `imitation learning` `diffusion policy` `suboptimal data` `Sim2Real` `data mixture`
- **Paper**: From Noise to Intent: Anchoring Generative VLA Policies with Residual Bridges [[HTML]](https://arxiv.org/html/2604.21391) [[PDF]](https://arxiv.org/pdf/2604.21391)
  - **Paper ID**: `2604.21391`
  - **来源日期**: 2026-04-24
  - **当时可能被低估的信号**: 当时暂留 watchlist 的信号是它声称同时覆盖鲁棒性、效率、跨 embodiment 与真实机器人，但需要 PDF 实证细节确认；这个野心本身值得回看。
  - **为什么现在值得再看**: 现在值得再看，因为你的兴趣覆盖 VLA、World Action Model 和长时程操作；语义意图与局部执行分离，可能是连接高层语言目标和低层动作稳定生成的一条路线。
  - **建议动作**: 快速浏览
  - **关键词**: `VLA` `generative policy` `residual bridge` `intent conditioning` `cross-embodiment`
- **Paper**: QuadVerse: An Integrated Framework Aligning Visual-Physical Reality for Quadruped Simulation [[HTML]](https://arxiv.org/html/2606.07118) [[PDF]](https://arxiv.org/pdf/2606.07118)
  - **Paper ID**: `2606.07118`
  - **来源日期**: 2026-06-08
  - **当时可能被低估的信号**: 当时被低估的是它把 3DGS 视觉重建、semantic mesh contact calibration 和 residual actuator compensation 放在同一个 real-to-sim-to-real 框架里，而不是只优化单个仿真组件。
  - **为什么现在值得再看**: 现在值得再看，因为你的兴趣包含 Sim2Real 和 World Model；QuadVerse 可作为研究视觉真实感、接触校准和执行器残差如何共同影响真实部署的系统参照。
  - **建议动作**: 继续跟踪
  - **关键词**: `Sim2Real` `real-to-sim-to-real` `visual-physical alignment` `contact calibration` `robot deployment`

## Editor's Picks

### [1]. Improving Robotic Generalist Policies via Flow Reversal Steering [[VIP]] [[HTML]](https://arxiv.org/html/2606.13675) [[PDF]](https://arxiv.org/pdf/2606.13675) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.13675`
* **Authors**: Andy Tang, William Chen, Andrew Wagenmaker, Chelsea Finn, Sergey Levine
* **Author Priority**: Core VIP
* **一句话结论**: 优先看；这篇把 flow-based VLA 的反向过程变成测试时动作 steering 接口，是今天最贴近“通用策略如何在新任务上快速变强”的论文。
* **关键词**: `Flow Reversal Steering` `VLA` `test-time steering` `DSBC` `DSRL`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

#### 📖 背景与动机

通用机器人策略已经能从大规模多任务数据里学到丰富行为先验，但在新任务、长时序任务或指令偏离训练分布时，直接下命令常常不够。传统补救是补采示范、重训模型，成本高且迭代慢；而作者的出发点是，模型内部并不只是会复现训练指令，它还包含大量“合理行为模式”。如果能在不重训或少量试错的条件下调用这些模式，VLA 就能从静态大模型变成可被人类、VLM 或 RL 过程持续引导的策略。这个问题对 VLA 和 RL+VLA 都很关键，因为现实部署里失败往往不是完全不会动，而是需要把已有技能组合到未见任务上。

#### ⚙️ 核心方法

FRS 的核心思想是利用 flow matching generalist 的可逆结构：先接受一个次优但语义上合理的动作建议，再把这个动作通过 flow policy 反向映射到 latent noise，随后在 latent 空间中寻找附近更符合 generalist 行为模式的动作。这样，粗粒度的语义指导可以被转换成底层可执行动作，而不要求指导者直接给出精确控制。摘录明确提到，FRS 可以由人类或 VLM 这样的 reasoner 引导，把策略推向“reasonable behaviors”。论文还提出用 FRS 产生的改进轨迹做快速学习，包括 Diffusion Steering via Behavior Cloning，即 DSBC，以及用 FRS bootstrap DSRL。相对普通 VLA 直接执行语言指令，FRS 的新意在于把通用策略本身作为动作流形和行为先验，而不是把外部建议当作最终动作；相对常规 RL，它把探索空间约束在策略已知的合理动作模式附近。当前摘录不能确认具体反向积分细节、latent neighborhood 的搜索策略或 VLM 评分接口，需要上传 PDF 后核查。

#### 📊 实验与结果

实验围绕三个问题展开：FRS 是否能零训练地让 VLM 指导 generalist 产生更合理行为，FRS 改进轨迹是否能快速训练新任务策略，以及 FRS 是否能帮助 generalist 更高效地从经验中改进。仿真部分使用 LIBERO，包括 Spatial、Object、Goal splits，以及 LIBERO-90 中一组任务；作者还说明基础 VLA 没有在对应测试 split 上训练，以保留改进空间。后续实验使用 15-task 子集训练 DSBC，并在该子集及更困难的 10-task 子集上运行 DSRL+FRS。摘录还声称覆盖多种仿真和真实世界 manipulation 设置，但没有提供完整成功率表格，因此只能判断实验面较广，具体提升幅度和真实机器人强度需看正文表格。

#### ⚠️ 风险 / 保留意见

- FRS 依赖基础 flow generalist 已经包含足够接近目标任务的行为模式，完全陌生技能可能无法被 steering 出来。
- VLM 或人类语义指导如何稳定转化为动作候选，可能成为部署时的主要不确定性。
- 摘录未给出完整定量结果，真实机器人提升、失败案例和计算开销需要 PDF 进一步核查。

#### 💭 结论与启发

这篇给后续选题的启发是：通用 VLA 的改进接口可以不局限于继续预训练或监督微调，而是直接利用生成式策略的反向过程做测试时动作修正。复现时应优先从已有 flow/diffusion action policy 入手，做小规模 LIBERO steering 实验，验证“次优动作反推 noise 再重采样”是否比直接执行 VLM 建议更稳。系统设计上，FRS 很适合作为 planner/reasoner 与 low-level generalist 之间的 adapter。

#### 🔎 读 PDF 先核查

- FRS 中“suboptimal but reasonable actions”具体由 VLM、人类还是采样策略产生，评分与筛选接口如何定义？
- 反向 flow 得到 latent noise 后，论文怎样定义 nearby generalist action modes，是否需要多次采样或额外优化？
- DSBC 和 DSRL+FRS 的改进主要来自更好初始轨迹、更多成功数据，还是来自约束探索分布？

#### 📌 上传 PDF 后优先看

- 方法章节中 flow reversal、latent steering 和动作重构流程的算法描述
- LIBERO 各 split、15-task 子集和 hard 10-task 子集的定量表格与消融
- 真实机器人实验设置、VLM/human guidance 接口和失败案例分析

### [2]. Mana: Dexterous Manipulation of Articulated Tools [[VIP]] [[HTML]](https://arxiv.org/html/2606.13677) [[PDF]](https://arxiv.org/pdf/2606.13677) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.13677`
* **Authors**: Zhao-Heng Yin, Guanya Shi, Pieter Abbeel, C. Karen Liu
* **Author Priority**: Core VIP
* **一句话结论**: 优先看；Mana 把铰接工具灵巧操作重写成 animation-to-policy 的 sim-to-real 管线，瞄准的是现有 VLA/灵巧手系统很少真正解决的接触与内部自由度耦合问题。
* **关键词**: `dexterous manipulation` `articulated tools` `sim-to-real` `Allegro hand` `animation pipeline`
* **证据来源**: arXiv HTML (Introduction, Experiments)

#### 📖 背景与动机

很多真实工具不是刚体，而是带内部关节和细薄把手的铰接机构，例如 tongs、pliers、clothespins 和 syringes。机器人不仅要抓住工具，还要在保持稳定接触的同时驱动内部自由度，这比普通抓取或刚体重排更难。摘录强调，已有灵巧操作进展主要集中在刚体对象，而铰接工具需要同时满足稳定支撑和功能性施力，两者可能要求复杂甚至冲突的力配置。这个方向对 sim-to-real 很重要，因为工具使用是机器人走向实际环境的关键能力，但真实数据采集昂贵、接触动力学难建模、手指尺度和物体细节误差都会放大失败。Mana 的价值在于，它试图用程序化 keyframe、动画式轨迹生成和点云策略训练，把复杂工具操作拆成可迁移的训练流程。

#### ⚙️ 核心方法

Mana，即 Manipulation Animator，把 dexterous manipulation 解释为一个 animation problem。根据摘要，系统采用 coarse-to-fine pipeline，将程序生成的 grasp keyframes 转换为 manipulation trajectories，再用于训练可执行策略。摘录能确认它围绕铰接物体的几何、URDF 和点云输入构建训练流程：实验中作者用相机扫描生成 meshes 和 URDF models，并输入 Mana pipeline 训练 point-cloud-based policies。方法上的关键不是简单模仿人类遥操作，而是先生成满足功能目标的粗略抓取和操作关键帧，再逐步细化成能驱动多指手完成工具内部自由度动作的轨迹。相对 open-loop trajectory，最终策略需要从观测中闭环适应物体姿态；相对 teleoperation baseline，Mana 追求减少人工控制负担并提高跨对象实例泛化。当前摘录没有给出完整优化目标、动画轨迹如何转成控制命令、接触约束如何处理等细节，因此这些只能作为方法方向判断，不能替代正文算法阅读。

#### 📊 实验与结果

实验覆盖四类铰接对象：tongs、pliers、clothespins 和 syringes，每类两个实例，包含不同尺寸、形状和关节类型。摘录给出物体厚度约 0.8–1.5cm，相对 Allegro hand 较小，且驱动需要 3–7N，这说明任务确实处在接触丰富且手指尺度不友好的区间。比较基线包括 open-loop Mana policy 和 teleoperation；teleoperation 中人类操作者使用 GeoRT 系统，并有 1 小时练习时间。论文还分阶段评估操作流程，确保每个 phase 从特定状态开始。摘录没有给出最终成功率，因此不能判断 Mana 对遥操作或开环轨迹的量化优势，只能确认 benchmark 设计比较贴近真实灵巧工具使用。

#### ⚠️ 风险 / 保留意见

- 方法可能高度依赖高质量扫描、URDF 建模和程序化 keyframe 设计，新增工具类别的工程成本需要核查。
- 铰接接触对摩擦、柔顺性和手指尺度误差敏感，sim-to-real 成功是否稳定仍需看失败案例。
- 摘录未提供跨类别泛化或完全新工具测试细节，泛化边界不明确。

#### 💭 结论与启发

Mana 对系统设计的启发在于，灵巧操作不一定要从端到端 VLA 直接学起，可以先用动画/关键帧语言构造“可行行为骨架”，再训练感知闭环策略补偿现实偏差。后续如果做工具使用，优先考虑这种 coarse-to-fine 结构：几何建模负责功能约束，策略学习负责执行鲁棒性。阅读 PDF 时应重点判断它是否真正减少人工示范需求，以及 keyframe 生成是否足够自动化。

#### 🔎 读 PDF 先核查

- Mana 的 procedurally-generated grasp keyframes 是如何生成和筛选的，是否需要为每类工具手写规则？
- 从 animation trajectory 到闭环 point-cloud policy 的训练监督是什么，是否包含接触力或仅使用状态/动作轨迹？
- 真实机器人中失败主要来自抓取初始化、工具内部关节驱动，还是 sim-to-real 动力学偏差？

#### 📌 上传 PDF 后优先看

- coarse-to-fine Mana pipeline 和 keyframe/trajectory 生成方法章节
- 四类工具、两实例设置下的分阶段成功率与 baseline 对比表
- 真实机器人部署细节，包括扫描建模、URDF、控制频率和失败案例

### [3]. EgoEngine: From Egocentric Human Videos to High-Fidelity Dexterous Robot Demonstrations [[VIP]] [[PDF]](https://arxiv.org/pdf/2606.12604) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.12604`
* **Authors**: Yangcen Liu, Shuo Cheng, Xinchen Yin, Woo Chul Shin, Alfred Cueva, Yiran Yang, Zhenyang Chen, Chuye Zhang, Danfei Xu
* **Author Priority**: Extended VIP
* **一句话结论**: 优先看但需谨慎；EgoEngine 只给了摘要回退信息，不过它正中“把海量第一人称人类视频变成机器人示范”的数据瓶颈。
* **关键词**: `egocentric video` `robot demonstration generation` `dexterous manipulation` `sim-to-real` `retargeting`
* **证据来源**: Abstract fallback

#### 📖 背景与动机

灵巧操作策略受限于大规模机器人示范采集成本，而 egocentric human videos 提供了更便宜、更丰富、更多样的 manipulation 行为来源。问题在于，人类视频不能直接用于机器人学习：一方面存在 visual gap，人手、视角和机器人本体不同；另一方面存在 action gap，人类手部运动不等于机器人可执行动作，尤其在灵巧手或复杂夹持下更明显。EgoEngine 的动机就是同时填补这两个 gap，把人类第一人称视频转换成既能用于视觉训练、又能用于动作监督的机器人数据。对 VLA 和 sim-to-real 来说，这类方法重要，因为它试图把互联网式或可穿戴采集的人类经验转成机器人可用的高保真 demonstration，从而扩大策略训练数据的来源。

#### ⚙️ 核心方法

当前只有摘要可用，因此只能确认 EgoEngine 是一个从 egocentric RGB video 到 robot data 的 scalable framework。给定第一人称 RGB 视频，它输出两类结果：第一是 high-fidelity robot observation video，也就是在保留场景上下文和时间对齐的同时，用机器人替换人类；第二是 task-aligned、executable robot action trajectory，并且动作需要满足 feasibility constraints。可以合理推断，系统至少包含视觉重渲染/替换、时序对齐、人体到机器人动作映射和可行性约束检查几个模块，但摘要没有说明具体使用扩散生成、3D 重建、运动 retargeting、优化还是仿真验证，因此不能写成确定事实。相对只做视频预测或只做人手轨迹 retargeting 的路线，EgoEngine 的主张更系统：同时生成机器人视角观测和机器人可执行动作，让转换数据能直接服务 robot learning。

#### 📊 实验与结果

摘要称实验在 simulation 和 real robots 上展示 EgoEngine 能够规模化转换人类视频为机器人数据，并支持后续机器人学习，但没有给出任务列表、数据规模、模型架构、成功率或对比基线。因此目前只能确认它声称覆盖仿真和真实机器人两类验证，不能引用任何具体性能提升。证据边界也很明显：摘要没有说明转换后的视频是否用于 VLA 预训练、行为克隆还是策略微调，也没有说明 action trajectory 的可执行性如何评估。上传 PDF 后需要重点核查真实机器人任务数量、是否存在未见场景泛化，以及与直接遥操作/人手 retargeting/合成数据方法的对比。

#### ⚠️ 风险 / 保留意见

- 目前只有摘要，方法细节和实验强度都无法验证，所有系统模块只能保守推断。
- 人类到机器人动作转换可能受 embodiment 差异、遮挡和接触状态不可观测限制。
- 高保真 robot observation video 若依赖生成模型，可能引入物理不一致或与动作轨迹不匹配的问题。

#### 💭 结论与启发

EgoEngine 值得纳入精选，是因为它代表了 VLA 数据扩展的一条关键路线：不是继续昂贵采集机器人示范，而是把人类 egocentric 行为转换成机器人可训练数据。后续复现不应一开始追求全系统，而可以拆成两个验证：视频中人手到机器人外观替换是否保持任务语义，动作 retargeting 是否能在仿真中闭环执行。若 PDF 证据扎实，它可能成为构建低成本灵巧操作数据引擎的重要参考。

#### 🔎 读 PDF 先核查

- EgoEngine 如何保证生成的 robot observation video 与输出 action trajectory 在时间和物理接触上保持一致？
- human-to-robot action trajectory 的 feasibility constraints 具体包括哪些约束，是否通过仿真或真实机器人验证？
- 转换数据最终用于哪类策略训练，和真实机器人示范相比性能差距如何？

#### 📌 上传 PDF 后优先看

- 系统架构章节，尤其是视觉替换、时序对齐和动作生成模块
- simulation 与 real robot 实验任务、数据规模和对比基线
- 可执行性验证、失败案例和 embodiment gap 分析

### [4]. $\texttt{WEAVER}$, Better, Faster, Longer: An Effective World Model for Robotic Manipulation [[HTML]](https://arxiv.org/html/2606.13672) [[PDF]](https://arxiv.org/pdf/2606.13672) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.13672`
* **Authors**: Arnav Kumar Jain, Yilin Wu, Jesse Farebrother, Gokul Swamy, Andrea Bajcsy
* **Author Priority**: Standard
* **一句话结论**: 优先看；WEAVER 把机器人 world model 的评价标准明确压到 fidelity、consistency、efficiency 三者同时成立，并连接到策略评估、改进和规划。
* **关键词**: `world model` `multi-view latent dynamics` `policy improvement` `planning` `advantage filtering`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)

#### 📖 背景与动机

机器人 world model 的长期承诺是用 learned simulator 降低真实交互成本，支持 policy evaluation、policy improvement 和 test-time planning。但在机器人 manipulation 中，单纯能预测短期图像并不够：用于评估策略时需要预测结果与真实执行相关，用于改进策略时需要长时序 rollout 不崩，用于规划时还必须足够快。很多模型可能只满足其中一项，例如图像逼真但慢，或 latent rollout 快但与真实奖励相关性弱。WEAVER 的动机是把这三个 desiderata 同时作为架构目标，而不是把世界模型当成一个孤立的视频预测模块。对于今天的 World Model/World Action Model 主题，这篇提供了比较清晰的系统化评价框架。

#### ⚙️ 核心方法

WEAVER 全称 World Estimation Across Views for Embodied Reasoning，是一个 multi-view world model，训练目标包括预测 future latents 和 reward values。摘录表明，它不是只生成未来 RGB，而是在 latent dynamics 中支持长时序模拟，并能沿着 recorded action trajectories 或 sampled action chunks 输出 reward 估计。用于 policy evaluation 时，作者把真实 rollout 中记录的 action trajectory open-loop 放进 WEAVER，记录预测 reward；用于 policy improvement 时，从当前策略采样若干 step action chunk，在 world model 内 forward simulate 多次，形成一批 imagined rollouts，再计算 Monte-Carlo n-step advantage。如果最高分 rollout 的 advantage 超过一个小的正阈值，就把它 distill 回 base policy；这个 filtering 机制用于避免模型想象质量不足时盲目更新策略。方法新意在于把多视角 latent prediction、reward prediction 和优势筛选策略改进串成闭环。摘录中的公式和具体超参缺失，因此不能确认 rollout 次数、horizon 或阈值。

#### 📊 实验与结果

实验明确围绕三种下游能力展开：policy evaluation、policy improvement 和 planning。摘录说明 policy evaluation 使用真实 rollout 的 recorded actions，在 WEAVER 中 open-loop 执行，并关注需要 40+ 次 latent dynamics 迭代的长时序任务，这直接考验 temporal consistency 和效率。policy improvement 则基于 action chunk sampling、world-model rollout、advantage 估计和过滤后蒸馏。虽然摘要称 WEAVER 在 robotic manipulation tasks 上达到 state-of-the-art，但摘录没有给出具体 benchmark 名称、成功率、相关性数值或速度指标。因此当前能确认的是实验设计和下游用途，而不是具体 SOTA 幅度。

#### ⚠️ 风险 / 保留意见

- world model 的 reward prediction 若与真实奖励偏离，policy improvement 可能把模型偏差蒸馏进策略。
- open-loop replay recorded actions 能评估模型相关性，但不能完全代表闭环部署鲁棒性。
- 摘录未给出多视角传感要求和计算开销，真实系统集成成本需核查。

#### 💭 结论与启发

WEAVER 的价值在于把 world model 从“预测未来好不好看”拉回机器人控制问题：预测是否能评价策略、改进策略、支持规划。后续阅读和复现时，应优先看它如何定义 fidelity，以及 predicted reward 与真实成功之间的相关性。系统设计上，这篇提示我们在 VLA 外挂 world model 时，最好使用 advantage filtering 这类保守更新机制，避免把不可靠想象直接转成训练标签。

#### 🔎 读 PDF 先核查

- WEAVER 的 multi-view latent 表示如何融合视角，是否需要固定相机布局才能工作？
- predicted reward values 的监督信号来自哪里，和真实任务成功率的相关性如何报告？
- advantage-based filtering 的阈值和 rollout horizon 对 policy improvement 稳定性有多敏感？

#### 📌 上传 PDF 后优先看

- WEAVER 架构与 multi-view latent/reward prediction 训练目标
- policy evaluation 中预测 reward 与真实结果相关性的实验表格
- policy improvement 和 planning 的 rollout 设置、消融与失败案例

### [5]. MaskWAM: Unifying Mask Prompting and Prediction for World-Action Models [[HTML]](https://arxiv.org/html/2606.13515) [[PDF]](https://arxiv.org/pdf/2606.13515) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.13515`
* **Authors**: Hanyang Yu, Haitao Lin, Jingbo Zhang, Wenyao Zhang, Chenghao Gu, Heng Li, Ping Tan
* **Author Priority**: Standard
* **一句话结论**: 优先看；MaskWAM 把 mask 同时作为 prompt 和预测目标，给 WAM/VLA 的空间 grounding 问题提供了一个直接且可验证的设计。
* **关键词**: `World Action Model` `mask prompting` `future mask prediction` `object-centric grounding` `LIBERO`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

World Action Models 通过未来视频预测来学习动作，理论上比直接 observation-to-action 更能利用物理动态和时序结构。但现实操作中，纯文本指令容易在杂乱场景里产生指代歧义，纯 RGB 预测又可能被背景和任务无关区域牵引，导致模型看起来会预测视频，却没有真正 grounding 到目标物体。MaskWAM 的问题设定非常具体：WAM 要想服务机器人控制，必须知道“哪个区域重要”，并在预测未来时保持对象中心语义。这个方向与 VLA 的痛点一致，因为很多失败不是语言理解错，而是空间定位、目标 disambiguation 和视觉注意力漂移。Mask supervision 在这里不是附加可视化，而是把任务相关区域变成模型训练和推理接口的一部分。

#### ⚙️ 核心方法

MaskWAM 输入当前 RGB observation、proprioceptive state、language instruction，以及可选 first-frame target mask；输出 action chunk、future RGB frames 和 future masks。模型建立在 Wan 2.2 之上，把传统 WAM 的 RGB future prediction 扩展为 RGB+mask 的联合预测。关键设计是 unified Mixture of Transformers：action expert 与 video/action tokens 通过 joint attention 交互，使动作生成和未来视觉预测处在同一个 token 序列中。为了复用预训练视频 backbone 的视觉先验，mask 没有使用独立专用 encoder，而是被渲染成 RGB-compatible 三通道图像，背景使用单独颜色，时间 horizon 和空间分辨率与 RGB 预测对齐。这样 mask 既可以作为显式输入 prompt 消除目标歧义，也可以作为 future prediction target 迫使模型关注任务相关区域。相对 RGB-only WAM，它的新意是把对象中心空间监督嵌入世界-动作联合建模，而不是只在后处理阶段做分割。

#### 📊 实验与结果

MaskWAM 在 LIBERO 上与 WorldVLA、GR00T-N1、Motus、FastWAM 等基线比较，并在 RoboTwin 2.0 上测试多任务泛化。摘录明确给出 LIBERO 平均成功率 98.4%，并称达到新 SOTA；与 RGB-only variant 相比，辅助 mask prediction 将性能从 97.3% 提升到 98.4%，说明即使部署时没有视觉 prompt，mask 监督也能改善 base policy learning。摘录还提到 attention maps 显示 RGB-only 模型容易关注背景，而 mask supervision 让模型更聚焦任务相关区域。RoboTwin 2.0 部分声称在随机指令、环境和物体位置下评估，但具体数值被截断，需看 PDF。

#### ⚠️ 风险 / 保留意见

- mask 标注或生成质量可能成为训练瓶颈，真实部署中 first-frame mask prompt 的获得方式也需明确。
- LIBERO 已接近高成功率区间，98.4% 与 97.3% 的差异需要结合统计方差和任务拆分判断。
- 把 mask 渲染成 RGB-compatible 图像复用 backbone 很实用，但可能限制细粒度实例区分或多对象关系表达。

#### 💭 结论与启发

MaskWAM 给后续系统设计的启发很直接：如果 WAM/VLA 在 clutter 或多目标场景中不稳，不一定先换更大模型，可以先把对象级空间监督纳入预测目标。复现上可以从 RGB-only WAM 加一个 future mask auxiliary head 或 RGB-rendered mask target 开始，验证注意力和成功率是否同步改善。选题上，它也提示 World Action Model 的竞争点会从“能否预测未来”转向“预测的未来是否绑定到任务相关实体”。

#### 🔎 读 PDF 先核查

- MaskWAM 的 first-frame target mask 在训练和测试中分别如何获得，是否需要人工标注或额外分割模型？
- MoT action expert 与 video tokens 的 joint attention 是否是性能提升关键，还是主要来自 mask auxiliary loss？
- 在 RoboTwin 2.0 的随机环境和物体位置下，mask prompt 与无 prompt 两种模式差异有多大？

#### 📌 上传 PDF 后优先看

- MaskWAM 架构、mask RGB-compatible encoding 和 MoT action expert 细节
- LIBERO 表格中各任务拆分、RGB-only 消融和统计方差
- RoboTwin 2.0 泛化实验、attention 可视化和失败案例

### [6]. $μ$VLA: On Recurrent Memory for Partially Observable Manipulation in VLA Models [[HTML]](https://arxiv.org/html/2606.12497) [[PDF]](https://arxiv.org/pdf/2606.12497) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.12497`
* **Authors**: Egor Cherepanov, Nikita Kachaev, Daniil Zelezetsky, Aydar Bulatov, Artem Pshenitsyn, Yuri Kuratov, Alexey Skrynnik, Aleksandr I. Panov, Alexey K. Kovalev
* **Author Priority**: Standard
* **一句话结论**: 优先看；μVLA 是一篇难得的 controlled isolation study，专门回答 VLA 在部分可观测 manipulation 中“只加 recurrence 到底有没有用”。
* **关键词**: `recurrent memory` `partial observability` `VLA` `OpenVLA-OFT` `TBPTT`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

主流 VLA 通常从当前观测预测未来 action chunk，这在可观测任务中有效，但在部分可观测场景里会失效：目标线索可能只在开头出现，物体身份可能被遮挡或洗牌，当前画面不再包含决策所需信息。已有 memory-augmented VLA 往往同时加入历史窗口、KV-cache、外部检索、压缩模块、辅助损失或层级记忆，导致很难判断真正起作用的是 recurrence 本身，还是周边工程。μVLA 的动机是把 recurrence 当作受控变量放进强预训练 VLA backbone 中，隔离研究 recurrent memory tokens 的作用。这对 VLA 很重要，因为如果简单 recurrence 就能显著改善部分可观测任务，它会成为比复杂检索记忆更容易复现和部署的 baseline。

#### ⚙️ 核心方法

μVLA 在 transformer 中加入一小组 learnable memory tokens，并通过 fine-tuning 让这些 token 在 episode step 之间传递信息。摘录的技术细节主要来自附录：memory tokens 放在 multimodal prefix 末尾，即 vision patches 和 proprioception token 之后、language instruction 之前。作者指出 OpenVLA-OFT input context 在 context block 内使用 bidirectional self-attention，因此 memory token 在 context 内的相对位置不改变可读写关系。方法还包含完整 attention mask、context-to-action zero 的信息论论证、episodic dataloader、fine-tuning protocol，以及带 reset operator 的 TBPTT loop。关键接口是跨时间步保留 recurrent state，同时在 episode 边界重置，并通过 truncated backpropagation through time 训练跨步 credit assignment。相对外部 memory/retrieval 方法，μVLA 的新意是最小化额外机制，尽量只测 recurrence、memory bandwidth、episodic dataloader 和 TBPTT 长度的影响。

#### 📊 实验与结果

主要实验使用 MIKASA-Robo，一个为部分可观测 tabletop manipulation 设计的 benchmark。任务覆盖 cue-recall、occlusion、sequential/predictive memory 三类，例如 RememberColor、ShellGame、TakeItBack 和 Intercept。摘录说明该 benchmark 的 latent dependency structure 在任务层面有文档，并允许对 recurrent channel 做 causal interventions，因此适合隔离 memory dependence。结论摘要显示，recurrence 可以在 fine-tuning 阶段加入 memoryless OpenVLA-OFT checkpoint，收益集中在 cue-recall；episodic dataloader、memory bandwidth 和 TBPTT length 都被分析，其中 TBPTT length 对 cue-recall 是重要杠杆。但具体数值在摘录中缺失或损坏，不能引用。

#### ⚠️ 风险 / 保留意见

- MIKASA-Robo 专为记忆依赖设计，结果迁移到开放真实机器人任务仍需验证。
- recurrence 解决的是历史信息保留，不一定处理长时序规划、探索或复杂物理建模。
- TBPTT、episode dataloader 和 reset 细节会显著影响结果，复现时容易因训练协议不同而偏离。

#### 💭 结论与启发

μVLA 的启发是，面对部分可观测失败，先做一个干净的 recurrent token baseline，可能比直接引入复杂检索或长上下文更有诊断价值。复现时应优先选择 cue-recall 和 occlusion 任务，做 memory ablation、reset intervention 和 TBPTT sweep，确认模型是否真的使用跨步状态。系统设计上，μVLA 适合成为 OpenVLA 类模型的轻量记忆插件，但真实机器人部署还要评估 state reset、episode segmentation 和延迟问题。

#### 🔎 读 PDF 先核查

- memory tokens 在每个时间步如何更新和传递，是否只依赖 transformer hidden state 还是有显式 recurrent operator？
- context-to-action zero 的 attention mask 设计具体防止了哪些信息泄漏，如何证明 memory channel 被真实使用？
- TBPTT length 的最优区间为什么呈现摘录所说的 U-shape，和 action chunk 长度是否耦合？

#### 📌 上传 PDF 后优先看

- memory token placement、attention mask 和 reset operator 的方法/附录细节
- MIKASA-Robo 三类部分可观测任务的分组结果与 causal intervention
- episodic dataloader、memory bandwidth、TBPTT length 的消融表格

## Watchlist

### [W1]. EA-WM: Event-Aware World Models with Task-Specification Grounding for Long-Horizon Manipulation [[HTML]](https://arxiv.org/html/2606.13053) [[PDF]](https://arxiv.org/pdf/2606.13053)
* **Paper ID**: `2606.13053`
* **Authors**: Kailin Wang, Haoxiang Jie, Yaoyuan Yan, Jiacheng Zhou, Zhiyou Heng
* **Author Priority**: Standard
* **为什么还值得留意**: EA-WM 进入 shortlist 是因为它把 world model 的输出从视觉/latent prediction 扩展到 task-specification-grounded event prediction 和 verifier-guided planning，很贴近长时序 manipulation 的真实需求。摘录中已有 PointMaze、Deformable、Wall-Single 和 LIBERO-goal 等多 benchmark 线索，并给出部分成功率改善，例如 PointMaze 从 0.90 到 0.94、Deformable 94%、Wall-Single 95%。没有进入最终精选的原因是主题与 WEAVER/MaskWAM 重叠，而当前摘录的方法段更像相关工作与框架描述，核心模型细节不如精选论文清晰。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. Learning to Assist: Collaborative VLAs for Implicit Human-Robot Collaboration [[HTML]](https://arxiv.org/html/2606.12475) [[PDF]](https://arxiv.org/pdf/2606.12475)
* **Paper ID**: `2606.12475`
* **Authors**: Leo Xu, Letian Li, Alex Cuellar, Michael Hagenow
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇值得 watchlist，因为它把 VLA 放进 implicit human-robot collaboration，并指出 action-chunking policies 的 demonstration action leakage 会导致 premature assistance，这是很有价值的真实交互失败模式。实验还包含 16 人用户研究、NASA TLX、SUS 和 Human-Robot Fluency 等主观指标，比纯离线 benchmark 更接近部署。没有进最终精选，是因为它更偏 HRC 应用诊断与 inference-time mitigation，和今天主线中的 world model、VLA 可扩展训练、sim-to-real 灵巧操作相比方法外延略窄。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. NavWAM: A Navigation World Action Model for Goal-Conditioned Visual Navigation [[HTML]](https://arxiv.org/html/2606.13494) [[PDF]](https://arxiv.org/pdf/2606.13494)
* **Paper ID**: `2606.13494`
* **Authors**: Daichi Azuma, Taiki Miyanishi, Koya Sakamoto, Shuhei Kurita, Yaonan Zhu, Petr Khrapchenkov, Motoaki Kawanabe, Yusuke Iwasawa, Yutaka Matsuo
* **Author Priority**: Standard
* **为什么还值得留意**: NavWAM 进入 watchlist 是因为它把 navigation world-model prediction、goal-progress value 和 executable action chunk 放入共享 latent sequence，代表 WAM 从 manipulation 延伸到 goal-conditioned visual navigation。摘录显示它比较 NWM、Cosmos Predict2 和 OmniVLA，并采用 simulation pretraining 加 real-robot adaptation，方向很完整。没有进入最终精选，主要是今天关注重点更偏 manipulation/VLA/Sim2Real，导航场景虽相关但优先级低于 WEAVER 和 MaskWAM。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. FTP-1: A Generalist Foundation Tactile Policy Across Tactile Sensors for Contact-Rich Manipulation [[VIP]] [[HTML]](https://arxiv.org/html/2606.13102) [[PDF]](https://arxiv.org/pdf/2606.13102)
* **Paper ID**: `2606.13102`
* **Authors**: Chengbo Yuan, Zicheng Zhang, Mingjie Zhou, Wendi Chen, Yi Wang, Zhuoyang Liu, Dantong Niu, Shuo Wang, Hui Zhang, Wenkang Zhang, Yingdong Hu, Yuanqing Gong, Wanli Xing, Chuan Wen, Cewu Lu, Kaifeng Zhang, Yang Gao
* **Author Priority**: Core VIP
* **为什么还值得留意**: FTP-1 有核心 VIP Cewu Lu，且提出跨 26 个来源、21 种传感器的 generalist foundation tactile policy，针对 contact-rich manipulation 中视觉 VLA 的短板。它还由 3 个独立机构在不同 embodiment 和任务套件上评估，包含 simulation 和 real-robot 设置，每个仿真任务 100 rollouts、真实任务 20 rollouts。没有进入最终精选，是因为它更偏 tactile foundation policy，不是今天标题方向中最中心的 VLA/WAM/world model，但后续做接触丰富操作时应重点补读。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
