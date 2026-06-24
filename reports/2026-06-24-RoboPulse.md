# RoboPulse | 2026-06-24

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 70 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线非常清晰：VLA 不再只是在更大数据上做 imitation，而是在评估、技能自举、几何监督、3D world model 和 action/world-action 统一建模之间形成闭环。最终精选保留了两类论文：一类直接服务机器人策略落地与评估，如 SC3-Eval、InSight、GRA；另一类代表 world model/action model 的底座升级，如 GAM、PAIWorld、Cosmos 3。最值得优先跟踪的 VIP 作者是 Sergey Levine 参与的 SC3-Eval，它把视频世界模型推向可扩展 policy evaluator；扩展名单里的 Jiajun Wu 出现在 InSight，方向是 VLA 自主技能 acquisition，也很贴近后续 RL+VLA 研究。整体看，今天的关键趋势是：几何一致性、动作条件生成、以及从生成模型中提取可监督信号，正在成为机器人 foundation model 能否进入真实系统的分水岭。

## 今日信号

- VLA 研究正在从“扩大行为克隆数据”转向“利用 world/action model 评估、生成、修复和扩展策略能力”的系统级闭环。
- 几何归纳偏置重新变得核心：无论是 2D waypoint、3D-consistent multi-view generation，还是 geometric foundation model，都在回应纯图像 token 对机器人空间控制不够稳定的问题。
- 生成式数据的价值正在被重新界定：高层几何、场景/embodiment 对齐和时间预测更可信，低层控制标签则需要更谨慎地从真实数据或结构化模型中获得。

## Historical Rediscovery

- **Paper**: MV-WAM: Manifold-Aware World Action Model with Value Augmentation [[HTML]](https://arxiv.org/html/2606.21088) [[PDF]](https://arxiv.org/pdf/2606.21088)
  - **Paper ID**: `2606.21088`
  - **来源日期**: 2026-06-23
  - **当时可能被低估的信号**: 当时可能低估了它把 manifold-aware objectives、cross-modality causal masking，以及 visual prediction、action generation、value estimation 放进同一 MoTs-based diffusion backbone 的组合信号；这不是单点模块改进，而是尝试统一预测、动作和值估计。
  - **为什么现在值得再看**: 现在值得再看，因为你的兴趣明确包含 World Action Model、World Model 和 RL+VLA。它还带有 Video Expert 预训练、RoboTwin 2.0 与真实机器人验证线索，适合判断 WAM 是否正在从概念走向可部署闭环策略。
  - **建议动作**: 加入精读
  - **关键词**: `World Action Model` `OOD robustness` `value augmentation` `diffusion backbone` `real robot validation`
- **Paper**: UniviewVLA: A Unified Multiview Vision-Language-Action Model with World Modeling [[HTML]](https://arxiv.org/html/2606.21501) [[PDF]](https://arxiv.org/pdf/2606.21501)
  - **Paper ID**: `2606.21501`
  - **来源日期**: 2026-06-23
  - **当时可能被低估的信号**: 当时可能低估了从 agent-view 和 wrist-view 生成辅助多视角未来视图、并把每个生成视图从 625 token 压缩到 16 token 的系统价值；这同时触及感知补全、未来预测和闭环推理成本。
  - **为什么现在值得再看**: 现在值得再看，因为多视角 world modeling 可能是 VLA 在遮挡、长时程操作和真实部署中提升鲁棒性的核心机制之一。它和你的 VLA、World Model、Sim2Real 兴趣高度重合。
  - **建议动作**: 加入精读
  - **关键词**: `VLA` `multiview` `world modeling` `occlusion` `token compression`
- **Paper**: OpenHLM: An Empirical Recipe for Whole-Body Humanoid Loco-Manipulation [[HTML]](https://arxiv.org/html/2606.22174) [[PDF]](https://arxiv.org/pdf/2606.22174)
  - **Paper ID**: `2606.22174`
  - **来源日期**: 2026-06-23
  - **当时可能被低估的信号**: 当时可能低估了 HLM-12 benchmark、真实世界每个 policy-task 五次 rollout，以及围绕 teleoperation、VLA 设计和 cheap data 的 one-variable-at-a-time roadmap 这些评测与工程路线信号。
  - **为什么现在值得再看**: 现在值得再看，因为真实部署评测和 humanoid 长时程操作正在成为 VLA 能力边界的重要检验场。它虽然偏系统 recipe，但对 Sim2Real、真实 rollout 和 whole-body VLA 数据路线有直接参考价值。
  - **建议动作**: 快速浏览
  - **关键词**: `VLA` `humanoid` `loco-manipulation` `real-world rollout` `benchmark`
- **Paper**: Cloak: Zero-Shot Cross-Embodiment Manipulation by Masking the End-Effector from the VLA [[HTML]](https://arxiv.org/html/2606.22836) [[PDF]](https://arxiv.org/pdf/2606.22836)
  - **Paper ID**: `2606.22836`
  - **来源日期**: 2026-06-23
  - **当时可能被低估的信号**: 当时可能低估了“不需要目标 embodiment 数据、重训练或提前知道目标硬件”这一点；通过 mask end-effector 让腕部视角更 embodiment-agnostic，再用 FK/IK 做 tip-pose retargeting，是很轻量的跨形态迁移信号。
  - **为什么现在值得再看**: 现在值得再看，因为 VLA 真实部署绕不开 cross-embodiment 和 Sim2Real 数据复用。它不直接是 world model 论文，但对把已有 VLA 策略迁移到新硬件很有现实价值。
  - **建议动作**: 继续跟踪
  - **关键词**: `VLA` `cross-embodiment` `zero-shot transfer` `retargeting` `Sim2Real`

## Editor's Picks

### [1]. SC3-Eval: Evaluating Robot Foundation Models via Self-Consistent Video Generation [[VIP]] [[HTML]](https://arxiv.org/html/2606.18610) [[PDF]](https://arxiv.org/pdf/2606.18610) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.18610`
* **Authors**: Wei-Cheng Tseng, Gashon Hussein, Yuzhu Dong, Allen Z. Ren, Lucy X. Shi, XuDong Wang, Sergey Levine, Zhaoshuo Li, Jinwei Gu, Florian Shkurti, Ming-Yu Liu, Quan Vuong
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看：SC3-Eval 把动作条件视频世界模型从“好看的视频生成”推向“可扩展机器人策略评估”，且有 Sergey Levine 参与，和今天的 VLA/world model 主线高度吻合。
* **关键词**: `VLA evaluation` `action-conditioned video world model` `self-consistency` `uncertainty early termination` `Sergey Levine`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

真实机器人上评估 generalist manipulation policy 成本很高：每次 rollout 都需要机器人时间、环境复位和人工监督，跨任务、跨环境比较多个 VLA policy 时尤其难扩展。动作条件视频 world model 看起来是自然替代方案：给定初始多视角观测和动作序列，生成未来帧，再据此给策略打分。但摘录指出这条路线有三个核心难点：自回归生成会累积 drift，多摄像头视角之间必须互相一致，评估器还要能处理被测 policy 产生的训练分布外行为。SC3-Eval 的动机不是训练一个更强控制器，而是构建能预测真实策略表现的 evaluator，这对 VLA 迭代非常关键：如果评估本身可扩展，模型选择、数据筛选、policy debugging 和 sim2real 前的风险控制都会更快。

#### ⚙️ 核心方法

SC3-Eval 的核心是把一个预训练 unified dynamics model 改造成 policy evaluator，并用三类 self-consistency 约束增强生成 rollout 的可信度。当前摘录能确认的机制包括：模型具备联合 forward 与 inverse dynamics；inverse dynamics objective 被用来把生成 rollout 锚定在物理上合理的 action manifold 上，从而缓解自回归漂移；同一个 forward-inverse consistency 信号还能作为 per-chunk uncertainty，用于 early termination。方法和传统 model-based RL 里的 ensemble disagreement、MOReL、MOPO 有相似动机，都是识别 off-manifold rollout，但 SC3-Eval 不依赖额外 ensemble，而是在单一统一世界模型内部提取不确定性，并且用于 policy evaluation 阶段：一旦 rollout 变得不可靠，就提前终止，避免后续漂移继续污染分数。摘录还强调多视角观测的一致性，这说明它不是单帧或单视角视频打分器，而是面向真实机器人多相机评估场景设计。具体三种 self-consistency 的完整定义、训练损失权重和 rollout scoring 细节需要等 PDF 核查。

#### 📊 实验与结果

实验部分将 real-world rollout 定义为 gold standard，并把可扩展替代方案分成 physics simulator、real-to-sim 和 video-model evaluator 三类。SC3-Eval 属于第三类，目标是避免手工资产、动力学调参和逐场景重建。摘录明确说它在七个真实世界 VLA policies 上评估，并与三个强视频模型评估 baseline 比较；结论称它在 closed-loop Pearson correlation 和 MMRV 上优于这些 baseline，并能泛化到 held-out task semantic 场景，但 HTML 摘录中的具体数值缺失，因此不能引用数字。证据边界也很清楚：目前只能确认评估对象是真实 VLA policies、比较对象是 video-model-based baselines、指标包含相关性和排序/方差类指标；真实机器人任务构成、每个 policy 的名称、失败案例和统计显著性需要原文实验表格进一步核查。

#### ⚠️ 风险 / 保留意见

- 评估器本身仍依赖视频 world model 的分布覆盖，遇到罕见接触、遮挡或策略异常行为时，early termination 可能只是在保守拒判。
- HTML 摘录缺失关键数值，当前只能确认优于 baseline 的方向性结论，不能判断提升幅度是否足以替代真实 rollout。
- 如果 scoring 依赖生成帧质量，可能把视觉一致性误当成任务成功，尤其是需要力控或隐藏状态判断的操作任务。

#### 💭 结论与启发

这篇最值得借鉴的是“world model 作为 evaluator”而不是“world model 作为 simulator”的定位变化。后续做 VLA 系统时，可以把 SC3-Eval 类方法放在 policy selection、offline regression test 和 risky rollout filtering 环节，而不是直接替代真实验证。复现时应重点拆解 forward-inverse consistency 如何转成 uncertainty，以及 early termination 后如何计算最终 policy score；如果这个机制稳健，它会成为真实机器人迭代中的高杠杆工具。

#### 🔎 读 PDF 先核查

- forward-inverse consistency 的 uncertainty 是如何按 chunk 计算的，阈值是否需要针对任务或策略重新校准？
- SC3-Eval 的评分如何处理提前终止的 rollout，是悲观记分、截断估计，还是另有归一化机制？
- 七个真实 VLA policies 中是否包含明显 OOD 或失败型策略，相关性提升是否主要来自这些困难样本？

#### 📌 上传 PDF 后优先看

- 方法章节中三类 self-consistency 约束的定义、损失和推理接口
- policy evaluation 实验表格：七个真实 VLA policies、三个 baseline、Pearson/MMRV 等指标
- held-out task、early termination ablation 和 failure cases 章节

### [2]. InSight: Self-Guided Skill Acquisition via Steerable VLAs [[VIP]] [[HTML]](https://arxiv.org/html/2606.24884) [[PDF]](https://arxiv.org/pdf/2606.24884) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.24884`
* **Authors**: Maggie Wang, Lars Osterberg, Stephen Tian, Ola Shorinwa, Jiajun Wu, Mac Schwager
* **Author Priority**: Extended VIP
* **一句话结论**: 值得优先看：InSight 把 VLA 的 primitive-level steerability 和自主数据飞轮结合起来，是“VLA 如何自己补技能”的代表性工作。
* **关键词**: `self-guided skill acquisition` `primitive steerability` `VLA` `VLM-guided data flywheel` `Jiajun Wu`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

#### 📖 背景与动机

VLA 能从 demonstration 中学会操作，但能力边界通常被训练数据锁住：训练集没有 sweeping、twisting 或 pouring，模型就很难在新任务中凭空获得这些 primitive。传统解决方案要么继续采人类演示，要么用仿真或真实 RL 交互学习；前者贵，后者样本复杂度和安全成本高。InSight 的问题设定更贴近长期机器人部署：当机器人遇到一个训练集中没有的动作原语时，能否先识别缺失 primitive，再低成本生成可训练数据，并把新技能纳入统一 VLA，而不破坏原有技能。这个方向对 VLA+RL 很重要，因为它试图把 skill acquisition 从人工数据收集转为 VLM-guided self-improvement，虽然当前摘录显示其执行空间仍比较受限。

#### ⚙️ 核心方法

InSight 有两个主要阶段。第一阶段是自动 demonstration segmentation：系统用 VLM 对任务计划进行分解，并结合 end-effector poses，把已有 demonstration 切成带标签的 primitive，例如“move gripper to the bowl”“lift upward”“pour the bottle”。这样训练出的 VLA 不只是响应完整任务指令，而是能在 primitive-action level 被 steer，也就是可以被显式要求执行某个子动作。第二阶段是 VLM-guided data flywheel：系统让 VLM 识别当前任务需要但训练集中缺失的 primitive，再通过 VLM-guided low-level control 生成训练数据，过滤成功样本后加入训练，扩展 VLA 的技能集合。摘录中的 conclusion 明确指出 skill gap execution 当前限制在 single-axis motions，因此它不是任意复杂轨迹的自动发明器，更像是把 VLM 的任务理解、几何启发式控制和 VLA fine-tuning 串成闭环。相对常规 imitation learning，新意在于 primitive steerability 使“发现缺口”和“补数据”有了明确接口；相对 Code-as-Policies 风格 zero-shot 控制，它把成功执行沉淀为 policy 能复用的训练数据。

#### 📊 实验与结果

实验覆盖仿真和真实硬件。仿真中使用 7DoF Franka Panda 和 LIBERO，研究从 pick-and-place demonstration 中学习 block flipping，通过加入自主获取的 rotate-block primitives 观察性能提升；还用 drawer opening demonstrations 去测试 drawer closing，强调从 OOD initial state 获取缺失 primitive。真实机器人部分使用 6DoF UFactory xArm，评估 bottle twisting、pouring，并与 Code-as-Policies-style zero-shot baseline 比较；随后把 twist、pour 和基础 pick-and-place 组合成长程 twist-then-pour 任务。摘录还说明会检查统一 policy 在加入新 primitives 后是否保留原始 pick-and-place 能力，并扩展到 contact-rich non-prehensile sweeping。当前没有给出成功率数字，因此只能确认实验设计覆盖了 OOD、组合泛化、技能保持和真实硬件，而不能判断各模块提升幅度。

#### ⚠️ 风险 / 保留意见

- 当前摘录明确说缺失技能执行限制在 single-axis motions，复杂接触、多阶段轨迹或高自由度 manipulation 可能超出能力范围。
- 数据飞轮依赖 VLM 判断 primitive gap 和成功过滤，错误标注或错误成功判定可能被放大进训练集。
- 加入新 primitive 后的遗忘风险需要仔细看实验，尤其是原有 pick-and-place 能力是否在更大技能库下稳定。

#### 💭 结论与启发

InSight 对后续选题的启发在于：不要只问 VLA 能否 zero-shot 完成新任务，而要问它能否把一次失败转化成可复用 primitive。系统设计上，可以把 primitive segmentation、VLM gap detection、低层控制器和 VLA post-training 看成一个持续学习 loop。复现时不必一开始追求开放世界技能获取，先在少数可参数化 primitive 上验证 steerability 和技能保持，再扩展到更复杂 waypoint 或 RL fine-tuning，会更现实。

#### 🔎 读 PDF 先核查

- primitive 标签由 VLM plan decomposition 和 end-effector poses 共同产生时，如何处理分段边界不准或 primitive 名称歧义？
- VLM-guided low-level control 生成的新数据和真实 demonstration 在训练中如何混合，是否有质量权重或 curriculum？
- 加入 twist、pour、sweep 等新 primitive 后，原有 pick-and-place 技能保持的证据是否来自同任务重测还是更广泛分布？

#### 📌 上传 PDF 后优先看

- 自动 primitive segmentation pipeline 的细节、prompt 和 pose-based boundary 规则
- VLM-guided data flywheel：gap discovery、低层控制、成功过滤和再训练流程
- 仿真/真实硬件的 ablation：无 steerability、无 VLM gap discovery、无新增数据的对照

### [3]. Supervise What Survives: Geometry-Guided VLA Adaptation from Synthetic Robot Videos [[HTML]](https://arxiv.org/html/2606.24448) [[PDF]](https://arxiv.org/pdf/2606.24448) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.24448`
* **Authors**: Danze Chen, Yanzhe Chen, Qiming Huang, Zhijun Cao, Chen Gao, Mike Zheng Shou
* **Author Priority**: Standard
* **一句话结论**: 值得优先看：GRA 对 synthetic robot video 的监督边界判断很清醒，主张“保留几何、不要伪造低层控制”，对 VLA 数据扩展很有方法论价值。
* **关键词**: `synthetic robot video` `geometry-guided adaptation` `2D waypoint supervision` `OpenVLA-OFT` `sim2real data`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)

#### 📖 背景与动机

VLA 的瓶颈之一是 paired video-action data 稀缺，而真实 teleoperation 需要硬件、操作者和时间。人类操作视频很丰富，human-to-robot video generation 也让合成机器人执行视频变得可扩展，但生成视频缺少真实 action labels。已有路线常把生成视频当作缺 action 的 demonstration，再用 inverse dynamics 或其他方式恢复 pseudo-actions。GRA 质疑这个抽象：视频可靠保存的是“where”，也就是可见的空间轨迹和任务几何；真实 demonstration 才包含“how”，也就是实际电机控制、接触细节和末端执行器命令。如果从生成像素中硬恢复低层动作，可能把生成模型的视觉伪影转成错误控制监督。因此论文要解决的问题是：合成视频到底应该监督 VLA 的哪一部分，怎样利用其几何价值而不污染 action head。

#### ⚙️ 核心方法

GRA 提出 Asymmetric Preservation Principle，并用两阶段协议实现。第一阶段，用生成帧训练 vision backbone，但监督目标不是 pseudo-action，而是 2D waypoint：从 source human video 派生未来若干步的 2D end-effector trajectory，并且与生成像素解耦。也就是说，synthetic robot video 被当成视觉外观和几何布局的数据源，帮助视觉编码器学习任务中的空间结构。第二阶段，在真实 demonstration 上 fine-tune action head，同时保留 persistent waypoint loss，让第一阶段学到的空间结构不会在动作学习时丢失。摘录显示它基于 OpenVLA-OFT，后者在 OpenVLA 上加入 continuous-action regression head；视觉 backbone 输出 tokens，经 Llama-2 7B language model 和 action head 输出 delta-action chunks，包括相对末端平移、roll-pitch-yaw 旋转与 gripper command。GRA 的新意不在于发明新 VLA 架构，而在于重新安放 synthetic video supervision：把它放到视觉几何层，而非低层控制层。当前摘录能确认 waypoint 是归一化图像坐标下的未来 2D end-effector trajectory，具体 horizon 符号和损失权重在 HTML 中缺失。

#### 📊 实验与结果

实验关注三个问题：在相同真实数据预算下是否优于 pseudo-action baseline，收益机制是什么，以及各组件贡献。硬件是 7-DoF Franka Research 3，固定第三人称 RealSense D435，相机视角下评估三个 tabletop pick-and-place 任务：cube pad、cup coaster、mango plate，每个任务 30 trials，并报告单任务成功率和三任务平均。生成视频由 Wan 2.2 基于第三人称人类视频生成，分辨率 480x640，81 frames。所有 baseline 使用 OpenVLA-OFT 架构与相同超参数设定，摘录明确提到 Real-only、Real-only full、DreamGen-style pseudo delta-actions、MimicDreamer-style 等对照，并提到 LoRA rank 32、batch size 16。当前摘录没有给出成功率数字，因此只能判断实验设计较强，不能引用性能提升幅度。

#### ⚠️ 风险 / 保留意见

- 2D waypoint 只能表达图像平面几何，深度、接触力和遮挡后的状态仍可能需要真实动作数据补足。
- 实验任务集中在 tabletop pick-and-place，是否能扩展到 deformable、tool use 或强接触任务仍需验证。
- 生成视频质量和 human-to-robot 对齐程度会影响 waypoint 监督价值，差质量视频可能造成视觉 backbone 偏移。

#### 💭 结论与启发

GRA 的最大启发是给 synthetic data 定义“可信监督边界”。后续如果使用生成视频扩 VLA 数据，不应默认恢复 action，而应区分哪些信息在生成过程中稳定保留：轨迹、目标位置、相对空间关系可能可用，低层控制和接触过程则应由真实数据或物理模型承担。系统设计上可以采用类似双阶段策略：先让视觉层吸收可见几何，再用少量真实 demonstration 训练 action head，同时用几何辅助 loss 防止遗忘。

#### 🔎 读 PDF 先核查

- 从 source human video 派生 2D end-effector waypoints 的具体方法是什么，是否需要手部/末端跟踪器或人工标注？
- persistent waypoint loss 在真实 demonstration fine-tuning 阶段的权重如何设定，过强时是否会限制 action head 学真实控制？
- DreamGen-style 和 MimicDreamer-style pseudo-action baseline 的动作恢复方式是否足够强，失败是否来自伪标签质量还是训练配方？

#### 📌 上传 PDF 后优先看

- Asymmetric Preservation Principle 的论证和两阶段训练流程图
- 三任务真实机器人结果表：Real-only、Real-only full、pseudo-action baselines、GRA 对比
- 组件消融：无 waypoint、无 persistent loss、不同 synthetic video 来源或规模

### [4]. Geometric Action Model for Robot Policy Learning [[HTML]](https://arxiv.org/html/2606.17046) [[PDF]](https://arxiv.org/pdf/2606.17046) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.17046`
* **Authors**: Jisang Han, Seonghu Jeon, Jaewoo Jung, René Zurbrügg, Honggyu An, Tifanny Portela, Marco Hutter, Marc Pollefeys, Seungryong Kim, Sunghwan Hong
* **Author Priority**: Standard
* **一句话结论**: 值得优先看：GAM 试图把 geometric foundation model 变成 perception、future prediction 和 action decoding 的共享底座，是 world-action model 与 3D 几何结合的强信号。
* **关键词**: `Geometric Action Model` `geometric foundation model` `world-action model` `future geometry prediction` `VLA`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

通用机器人策略需要同时理解语言、物体、相机、机器人状态和动作对 3D 世界的影响。现有 VLA 依赖 VLM 的语义先验，WAM 依赖视频生成模型的时间先验，但两者往往仍在 2D image frame 或 2D-derived latent space 中工作，3D 几何关系需要从 action supervision 中隐式学出。这对接触丰富的 manipulation 不够理想，因为控制失败常来自深度、遮挡、相机视角和末端执行器相对位姿的误判。GAM 的动机是直接复用 pretrained geometric foundation model，让几何不仅是输入预处理或辅助头，而是整个策略学习的共享表征基底。它回应的是今天多篇论文共同的问题：VLA 底座如果缺少显式几何结构，就很难稳定进入真实机器人控制。

#### ⚙️ 核心方法

GAM 的关键设计是把 pretrained geometric foundation model 在中间层切开：浅层作为 observation encoder，深层继续承载几何表征能力，中间插入一个 causal future predictor。这个 predictor 在语言、proprioception 和历史视觉上下文条件下预测未来 latent tokens，并在同一 shared substrate 上支持 action decoding 和 future geometry prediction。摘录显示其语言指令使用 frozen T5 encoder 提取 tokens，policy 根据 proprioceptive states 输出 end-effector action chunks。实现上使用 DA3-Giant，并在某个 alternating attention 开始的层插入 12-layer causal predictor；训练时冻结前面部分层和 depth head，并用 simulator ground truth 监督 depth。预训练数据包括来自 RoboCasa365、MimicGen 和 OpenX-Embodiment 的 784K single-arm robot trajectories，之后再在各 benchmark 上 post-train。相对 VLA，它强调几何底座；相对视频 WAM，它不是只生成未来视频，而是把未来几何预测和动作解码放进同一模型路径。HTML 中部分符号和超参数缺失，因此具体层号、horizon、action chunk 长度等需要 PDF 核查。

#### 📊 实验与结果

摘录中的实验包括实现细节和 simulation benchmarks。GAM 在 LIBERO 上训练和评估，该 benchmark 覆盖空间布局、物体身份和任务目标等不同泛化轴；同时还提到用于更严格 OOD robustness 的评估，但 HTML 摘录在该句后截断。结论声称 GAM 在 extensive simulation and real-world benchmarks 上取得更高 accuracy、更快 inference 和更强泛化，但摘录没有给出具体 benchmark 列表、真实机器人任务、成功率或延迟数值，因此这些只能作为作者结论的方向性陈述。可以明确引用的是：使用 DA3-Giant fine-tuned on Track4World，插入 12-layer causal predictor，预训练 784K 单臂机器人轨迹，并用 simulator ground-truth depth 做监督。证据边界在于，当前无法判断性能提升来自 GFM 本身、depth supervision、预训练数据规模，还是 causal predictor 架构。

#### ⚠️ 风险 / 保留意见

- 方法依赖大型 geometric foundation model 和大量轨迹预训练，复现成本可能明显高于普通 VLA fine-tuning。
- 使用 simulator ground-truth depth 监督可能带来仿真依赖，真实场景中的深度噪声和相机标定误差需要单独评估。
- 当前摘录缺少具体结果数值，无法判断“更快 inference”和“真实机器人优势”的实际幅度。

#### 💭 结论与启发

GAM 对后续研究的启发是：world-action model 不一定要从视频生成模型出发，也可以从几何 foundation model 出发，把未来预测和动作解码统一在 3D-aware latent 中。对系统设计而言，这提示我们在选择 VLA backbone 时不应只看语义和语言对齐，还要看其是否天然表达深度、视角和物体几何。复现时应先做简化版：固定 GFM，插入小型 causal predictor，比较 action-only、geometry-only 和 joint prediction，确认共享几何未来预测是否真正提升控制。

#### 🔎 读 PDF 先核查

- GFM 中间层切分位置如何选择，性能是否对 split layer 非常敏感？
- future latent prediction 和 action decoding 的损失如何平衡，是否存在预测几何好但控制不好的情况？
- 真实机器人 benchmark 中的优势主要来自 3D 几何、预训练数据规模，还是 depth supervision？

#### 📌 上传 PDF 后优先看

- 模型架构章节：GFM split、12-layer causal predictor、action decoder 和 depth head 的连接方式
- 预训练与 post-training 配方：784K trajectories 来源、冻结策略、depth supervision
- LIBERO/OOD/真实机器人结果与 ablation：无 causal predictor、无 depth、不同 backbone 对比

### [5]. PAIWorld: A 3D-Consistent World Foundation Model for Robotic Manipulation [[HTML]](https://arxiv.org/html/2606.18375) [[PDF]](https://arxiv.org/pdf/2606.18375) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.18375`
* **Authors**: Yuhang Huang, Xuan Lv, Junyan Xu, Zhiyuan Yu, Jiazhao Zhang, Ruizhen Hu, Wancheng Feng, Shilong Zou, Hewen Xiao, Ziqiao Zhou, Kaiyun Huang, Zhiyu Peng, Juzhan Xu, Hang Zhao, Chenyang Zhu, Renjiao Yi, Yifei Huang, Douhui Wu, Yan Zhang, Kexu Cheng, Chunhe Song, Yunzhi Xue, Xiuhong Zhang, Leitao Guo, Yunji Chen, Bin Wu, Haibin Yu, Kai Xu
* **Author Priority**: Standard
* **一句话结论**: 值得优先看：PAIWorld 直接瞄准多视角 3D-consistent world foundation model，是机器人 world model 从单视角视频生成走向多相机控制环境的重要样本。
* **关键词**: `3D-consistent world model` `multi-view generation` `Geometry-Aware Cross-View Attention` `Geo-RoPE` `Cosmos`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

现有 world foundation models 已能生成较长、较合理的视频 rollout，但多数仍以单视角为主；机器人 manipulation 却天然依赖多摄像头，包括 egocentric、eye-to-hand 和 wrist-mounted views。简单把多视角 token 拼接起来并不能保证跨视角一致，容易出现 object drift、depth inconsistency 和 texture misalignment，这些错误会继续传递到 planning、policy learning 或 synthetic data generation。PAIWorld 的问题设定正是机器人 world model 的关键痛点：如果世界模型不能保持多视角 3D 一致，它生成的视频即使单视角逼真，也可能对控制毫无帮助甚至有害。论文认为需要两个条件同时存在：视角之间的信息通路，以及能约束该通路的 3D 几何信号。

#### ⚙️ 核心方法

PAIWorld 建在 Cosmos-Predict2.5 之上，这是一个在视频 VAE latent space 中工作的 flow-matching diffusion transformer world foundation model；完整模型约 14B 参数，并使用 Cosmos-Reason1 作为 text embedder 来提供 physical-grounded conditioning。方法层面，摘录能确认的模块包括 Geometry-Aware Cross-View Attention、Geometric Rotary Position Embedding，以及 REPA projection heads。其核心思想是：不要让每个视角各自生成再靠数据隐式对齐，而是在 pretrained backbone 中插入跨视角通信模块，并用几何位置编码塑造注意力，使不同 camera views 可以交换与相机几何一致的上下文；同时用训练目标层面的几何信号来强化 3D-consistent content。它处理两类生成范式：action-conditioned video generation 和 text-conditioned multi-view generation。相对普通 multi-view world model，PAIWorld 的新意在于把“跨视角通信”和“几何先验”作为互补必要条件，而不仅是扩大训练数据或拼接视角 token。具体 Geo-RoPE 数学形式、REPA 监督来源和相机标定输入格式需要 PDF 核查。

#### 📊 实验与结果

实验评估 action-conditioned video generation 和 text-conditioned multi-view generation，并在三个 benchmark 上与 state-of-the-art baselines 比较。摘录明确给出实现和数据规模：模型基于 Cosmos-Predict2.5，约 14B 参数；数据集约 2.5M multi-view robotic manipulation video clips，来自 AgiBot-World 35%、RoboMIND 20%、Galaxea 15%、RoboTwin 15%、RoboCOIN 15%。这些数据提供多相机机器人操作视频，并伴随文本描述或相关条件信息。结论称 PAIWorld 通过 Geometry-Aware Cross-View Attention 和 Geo-RoPE 改善 3D-consistent multi-view generation，但当前摘录没有具体指标和数值，不能引用提升幅度。实验可信度的关键在于：是否有专门衡量 cross-view object drift、depth consistency、texture alignment 的指标，以及这些指标是否能预测 downstream planning/control 收益。

#### ⚠️ 风险 / 保留意见

- 14B 级模型和 2.5M 多视角视频数据带来很高训练与复现门槛，普通实验室难以完整复刻。
- 生成一致性不等于控制有效性，如果实验主要是视频指标，下游 policy/planning 收益还需单独验证。
- 跨数据源相机配置、视角数量和标定质量可能差异很大，模型是否依赖高质量 calibration 需要核查。

#### 💭 结论与启发

PAIWorld 的启发是，多视角机器人 world model 不能只追求单视角视频质量，而要把 camera geometry 作为模型结构的一部分。后续如果要做 VLA 数据合成或 model-based planning，应该优先关心跨视角一致性指标，因为这些错误会直接影响位姿估计和动作选择。系统上可以借鉴其双层设计：架构层提供 inter-view communication，目标层提供几何约束；即使不复现 14B 模型，也可以在较小 DiT 或 video transformer 中验证同样原则。

#### 🔎 读 PDF 先核查

- Geometry-Aware Cross-View Attention 如何利用相机内外参，是否需要所有训练数据都有准确 calibration？
- REPA projection heads 提供的几何监督具体来自哪里，和 cross-view attention 的贡献如何区分？
- action-conditioned generation 的评估是否和真实机器人控制或 policy rollout 成功率相关，还是主要停留在视频一致性指标？

#### 📌 上传 PDF 后优先看

- 模型章节：Geometry-Aware Cross-View Attention、Geo-RoPE、REPA heads 的接口和损失
- 数据集与训练章节：2.5M clips 的视角配置、标定质量、action/text 条件形式
- 实验章节：多视角一致性指标、action-conditioned rollout、下游 robotic manipulation 证据

### [6]. Cosmos 3: Omnimodal World Models for Physical AI [[PDF]](https://arxiv.org/pdf/2606.02800) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.02800`
* **Authors**: NVIDIA: Aditi, Niket Agarwal, Arslan Ali, Jon Allen, Martin Antolini, Adeline Aubame, Alisson Azzolini, Junjie Bai, Maciej Bala, Yogesh Balaji, Josh Bapst, Aarti Basant, Mukesh Beladiya, Mohammad Qazim Bhat, Zaid Pervaiz Bhat, Dan Blick, Vanni Brighella, Han Cai, Tiffany Cai, Eric Cameracci, Jiaxin Cao, Yulong Cao, Mark Carlson, Carlos Casanova, Ting-Yun Chang, Yan Chang, Yu-Wei Chao, Prithvijit Chattopadhyay, Roshan Chaudhari, Chieh-Yun Chen, Junyu Chen, Ke Chen, Qizhi Chen, Wenkai Chen, Xiaotong Chen, Yu Chen, An-Chieh Cheng, Click Cheng, Xiu Chia, Jeana Choi, Chaeyeon Chung, Wenyan Cong, Yin Cui, Magdalena Dadela, Nalin Dadhich, Wenliang Dai, Joyjit Daw, Alperen Degirmenci, Rodrigo Vieira Del Monte, Robert Denomme, Sameer Dharur, Marco Di Lucca, Ke Ding, Wenhao Ding, Yifan Ding, Yuzhu Dong, Nicole Drumheller, Yilun Du, Aigul Dzhumamuratova, Aleksandr Efitorov, Hamid Eghbalzadeh, Naomi Eigbe, Imad El Hanafi, Hassan Eslami, Benedikt Falk, Jiaojiao Fan, Jim Fan, Amol Fasale, Sergiy Fefilatyev, Liang Feng, Francesco Ferroni, Sanja Fidler, Xiao Fu, Vikram Fugro, Prashant Gaikwad, TJ Galda, Katelyn Gao, Yihuai Gao, Wenhang Ge, Sreyan Ghosh, Arushi Goel, Vivek Goel, Akash Gokul, Rama Govindaraju, Jinwei Gu, Miguel Guerrero, Elfie Guo, Aryaman Gupta, Siddharth Gururani, Hugo Hadfield, Song Han, Ankur Handa, Zekun Hao, Mohammad Harrim, Ali Hassani, Nathan Hayes-Roth, Yufan He, Chris Helvig, Cyrus Hogg
* **Author Priority**: Standard
* **一句话结论**: 值得优先看但要保守读：Cosmos 3 是 omnimodal world model 底座级论文，摘要信息已足够说明其战略重要性，但缺少 HTML 细节时不能展开具体架构和实验数字。
* **关键词**: `omnimodal world model` `Physical AI` `world-action model` `mixture-of-transformers` `Cosmos 3`
* **证据来源**: Abstract fallback

#### 📖 背景与动机

Physical AI 需要模型同时处理语言、图像、视频、音频和动作序列，而传统 VLM、视频生成器、world simulator、world-action model 往往分散建模。对机器人来说，这种割裂会导致系统工程复杂：理解任务、预测未来、生成视觉数据、输出动作可能分别依赖不同模型，接口之间的信息损失和对齐成本很高。Cosmos 3 的动机是把这些能力放进一个 omnimodal world model 家族中，用统一架构支持灵活输入输出组合，从而成为 embodied agents 的通用底座。它进入精选的原因不是某个单点机器人 benchmark，而是它代表了工业级 foundation model 正在把 action sequence 纳入世界模型的统一模态空间，这对 VLA、WAM 和机器人数据生成路线都有方向性影响。

#### ⚙️ 核心方法

当前只有摘要回退信息，因此只能确认 Cosmos 3 是一族 omnimodal world models，目标是在 unified mixture-of-transformers architecture 中联合处理并生成 language、image、video、audio 和 action sequences。摘要称它支持高度灵活的 input-output configurations，并试图把 vision-language model、video generator、world simulator 和 world-action model 统一到同一框架下。这里最值得关注的是 action 被明确列为一等模态：这意味着模型不只是生成视频或理解图像，而可能在同一表示空间里连接感知、物理预测和动作条件/动作输出。由于没有 HTML 方法摘录，不能推断 mixture-of-transformers 的具体路由机制、tokenization 方案、action 表示、训练数据构成或 post-training 流程。合理的趋势判断是：Cosmos 3 更像底座平台论文，其贡献可能体现在模型族、训练配方和跨任务评估，而不是单一机器人算法。上传 PDF 后需要重点核查机器人 policy model 与 world-action capability 的具体接口。

#### 📊 实验与结果

摘要声称 Cosmos 3 在 diverse understanding and generation tasks 上建立新的 state-of-the-art，并且 post-trained 模型在技术报告发布时被 Artificial Analysis 评为最佳 open-source Text-to-Image 和 Image-to-Video 模型，被 RoboArena 评为最佳 policy model。由于当前只有摘要，不能引用具体 benchmark 名称、分数、模型大小、训练数据规模或机器人任务成功率。对今天主题最相关的证据是：它明确覆盖 action sequences，并把 policy model 排名作为外部评价信号之一。但证据边界同样明显：T2I/I2V 排名不能直接证明机器人控制能力，RoboArena 排名也需要看任务分布、评测协议、是否真实机器人、是否闭源对比和统计稳定性。

#### ⚠️ 风险 / 保留意见

- 当前只有摘要回退，方法和实验细节不足，任何关于模型规模、路由、action token 或机器人指标的说法都必须等 PDF 确认。
- omnimodal 统一架构可能带来很强平台价值，但机器人部署仍取决于 action representation、低延迟推理和真实闭环评估。
- 外部排行榜信号有参考价值，但不能替代任务级 ablation 和真实机器人成功率分析。

#### 💭 结论与启发

Cosmos 3 应作为后续 world model/VLA 底座路线的重点跟踪对象，而不是立刻按普通算法论文复现。阅读时要把问题聚焦在三个方面：action 如何被 token 化并与视频/语言共同训练；world simulator 能否支持闭环 policy rollout；policy model 的评测是否能说明真实控制泛化。若其接口开放，后续可考虑把它作为视频生成、策略评估或 action-conditioned data synthesis 的底座，与 SC3-Eval、PAIWorld 这类更具体机器人方法对接。

#### 🔎 读 PDF 先核查

- Cosmos 3 中 action sequences 的表示和训练目标是什么，能否直接服务机器人 action chunk prediction？
- mixture-of-transformers 架构如何在 language、image、video、audio、action 之间路由信息，是否存在专门的物理或动作专家？
- RoboArena policy model 排名对应哪些任务和评测协议，是否包含真实机器人闭环控制？

#### 📌 上传 PDF 后优先看

- 模型架构章节：mixture-of-transformers、模态 tokenization、action sequence 接口
- post-training 和评测章节：policy model、world simulator、video generation 的训练/评估分支
- 机器人相关实验：RoboArena、world-action tasks、闭环控制或动作条件生成证据

## Watchlist

### [W1]. G$^3$VLA: Geometric inductive bias for Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2606.24472) [[PDF]](https://arxiv.org/pdf/2606.24472)
* **Paper ID**: `2606.24472`
* **Authors**: Yue Peng, Yongzhe Zhao, Artur Habuda, Khuyen Pham, Yanheng Zhu, Tran Nguyen Le, Fares Abu-Dakka, Li Guo
* **Author Priority**: Standard
* **为什么还值得留意**: G3VLA 进入 watchlist 是因为它和今天的几何主线高度相关：通过 intrinsic-conditioned ray embeddings、PRoPE、cross-view fusion 和 point-map distillation，把 calibrated camera geometry 注入 VLA visual tokens。它没有进入最终精选，主要是因为与 GRA、GAM、PAIWorld 相比，摘录呈现的系统新意更偏模块增强，且当前最终精选已经覆盖了合成监督、几何 action model 和多视角 world model 三个更互补方向。PDF 上传后仍值得核查 LIBERO、RoboCasa24、RoboTwin2.0 和真实机器人结果，尤其是多相机几何模块是否稳定提升空间/物体敏感任务。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. Wh0: Generative World Models as Scalable Sources of Egocentric Human Hand Manipulation Data [[HTML]](https://arxiv.org/html/2606.22136) [[PDF]](https://arxiv.org/pdf/2606.22136)
* **Paper ID**: `2606.22136`
* **Authors**: Yangtao Chen, Zixuan Chen, Peiyang Wang, Yong-Lu Li, Jing Huo, Jieqi Shi, Yang Gao
* **Author Priority**: Standard
* **为什么还值得留意**: Wh0 进入 watchlist 是因为它把 generative world models 用作 egocentric human-hand manipulation data source，并明确讨论 scene gap 与 embodiment gap，对 dexterous VLA 很有价值。它没有进入最终精选，是因为今天精选更优先机器人 VLA 评估、技能自举和几何/world-model 底座；Wh0 更像数据生成与 post-training 案例。摘录中 50k WM-H、Unitree G1、Inspire dexterous hands、18 tasks、每任务 20 trials，以及 VITRA 从 8.3% 到 38.9% 的提升非常值得后续细读。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

### [W3]. SkyJEPA: Learning Long-Horizon World Models for Zero-Shot Sim-to-Real Control of Quadrotors [[HTML]](https://arxiv.org/html/2606.23444) [[PDF]](https://arxiv.org/pdf/2606.23444)
* **Paper ID**: `2606.23444`
* **Authors**: Pratyaksh Rao, Wancong Zhang, Randall Balestriero, Yann LeCun, Giuseppe Loianno
* **Author Priority**: Standard
* **为什么还值得留意**: SkyJEPA 进入 watchlist 是因为它把 JEPA-style latent world model 用于 quadrotor long-horizon prediction 和 zero-shot sim-to-real control，覆盖了 RL/world model 与真实部署的另一条分支。它没有进入最终精选，是因为今天关注更偏 manipulation/VLA/world-action model，而该文主体是 aerial robotics dynamics/control。仍建议后续跟踪其 latent dynamics、physics-inspired prober、onboard closed-loop control 和 robustness 实验，因为这些设计可能迁移到移动操作或视触觉世界模型。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. World Value Models for Robotic Manipulation [[PDF]](https://arxiv.org/pdf/2606.24742)
* **Paper ID**: `2606.24742`
* **Authors**: Zhihao Wang, Jianxiong Li, Yu Cui, Yuan Gao, Xianyuan Zhan, Junzhi Yu, Xiao Ma
* **Author Priority**: Standard
* **为什么还值得留意**: World Value Models 进入 watchlist 是因为它提出用 world model 做 generalist robotic value estimation，正好连接 RL、temporal understanding 和未来规划。没有进入最终精选的原因是当前只有摘要回退，缺少 HTML 方法与实验细节，无法判断 WVM 的架构、训练信号和 benchmark 可信度。上传 PDF 后应优先核查它如何把历史 belief grounding 与 future outcome planning 转成 value prediction，以及是否真的优于基于静态 VLM backbone 的 value model。
* **证据来源**: Abstract fallback
