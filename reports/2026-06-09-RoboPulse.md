# RoboPulse | 2026-06-09

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 159 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线很清晰：VLA 正在从单步策略走向“可被调度、可被强化学习微调、可跨 embodiment 吸收人类数据”的系统化机器人栈，同时 humanoid loco-manipulation 把评测、世界模型和实时控制推到前台。最终精选覆盖了六个互补切面：VoLo 做物理世界里的闭环编排，Q-VGM 做 flow-matching VLA 的离线 RL 微调，Ego-Pi 验证 egocentric 人类数据能教机器人新语义，SIMPLE 补 humanoid 仿真评测缺口，MotionWAM 把 WAM 推向实时 humanoid，Cosmos 3 则代表通用 omnimodal world model 的大模型路线。VIP 作者里最值得优先跟踪的是 Chelsea Finn 参与的 Ego-Pi 和 Yue Wang 参与的 SIMPLE：前者关系到人类数据到机器人策略的可扩展训练，后者关系到 humanoid foundation model 的可复现实验基准。其余精选虽然没有命中 VIP 名单，但分别卡在 VLA/WAM 系统落地的关键瓶颈上，因此比单纯提高 benchmark 分数的工作更值得今天优先阅读。

## 今日信号

- VLA 的竞争焦点正在从“端到端动作预测”转向“高层推理、低层技能、监控恢复和物理时序约束如何闭环协同”。
- flow-matching VLA、human egocentric data 和 world-action model 都在试图解决同一个问题：如何在不重新采集海量机器人数据的情况下，让已有 foundation policy 获得任务回报、语义迁移或长时序控制能力。
- humanoid loco-manipulation 正在形成独立赛道，评测基准、统一 whole-body action space 和实时世界模型推理会成为接下来判断方法可信度的核心指标。

## Historical Rediscovery

- **Paper**: CAPE: Contrastive Action-conditioned Parallel Encoding for Embodied Planning [[HTML]](https://arxiv.org/html/2606.07304) [[PDF]](https://arxiv.org/pdf/2606.07304)
  - **Paper ID**: `2606.07304`
  - **来源日期**: 2026-06-08
  - **当时可能被低估的信号**: action-conditioned contrastive objective、future-state representation、parallel action-query decoder 这些信号说明它可能在绕开像素重建式 dynamics model 的容量浪费。
  - **为什么现在值得再看**: 今天关注 World Model / World Action Model 时，最关键的问题之一是模型是否学到对动作选择有用的未来状态表征，而不是只会预测视觉外观；CAPE 正好值得重新核查其闭环规划证据。
  - **建议动作**: 加入精读
  - **关键词**: `World Model` `action-conditioned representation` `embodied planning` `future-state prediction`
- **Paper**: STRIPS-WM: Learning Grounded Propositional STRIPS-style World Models from Images [[HTML]](https://arxiv.org/html/2606.06832) [[PDF]](https://arxiv.org/pdf/2606.06832)
  - **Paper ID**: `2606.06832`
  - **来源日期**: 2026-06-08
  - **当时可能被低估的信号**: lexicographic objective、transition/applicability slack、sparse effects 这些机制可能是从真实图像中抽取可规划因果结构的关键线索。
  - **为什么现在值得再看**: VLA/WAM 若要走向长时程操作，需要知道哪些事实可行动、动作会改变什么；这篇虽然不是端到端 VLA，但可能补上 action/world abstraction 层。
  - **建议动作**: 加入精读
  - **关键词**: `World Model` `STRIPS` `long-horizon planning` `grounded visual abstraction`
- **Paper**: Tabero: Learning Gentle Manipulation with Closed-Loop Force Feedback from Vision, Touch, and Language [[HTML]](https://arxiv.org/html/2605.27886) [[PDF]](https://arxiv.org/pdf/2605.27886)
  - **Paper ID**: `2605.27886`
  - **来源日期**: 2026-05-28
  - **当时可能被低估的信号**: 从开源 manipulation 数据迁移到 Isaac Lab、引入触觉信息、关注 tactile gripper 替换后的性能补偿，这些都指向 VLA 真实部署中的接触鲁棒性问题。
  - **为什么现在值得再看**: 当前 VLA 很容易在 force-sensitive/contact-rich manipulation 上失效；如果闭环 force feedback 能稳定提升 gentle manipulation，它会成为 VLA 到真实操作的重要补丁。
  - **建议动作**: 快速浏览
  - **关键词**: `VLA` `tactile feedback` `force control` `closed-loop manipulation`
- **Paper**: Gaze2Act: Gaze-Conditioned Vision-Language-Action Policies for Interactive Robot Manipulation [[HTML]](https://arxiv.org/html/2605.30282) [[PDF]](https://arxiv.org/pdf/2605.30282)
  - **Paper ID**: `2605.30282`
  - **来源日期**: 2026-05-29
  - **当时可能被低估的信号**: 相似物体选择、局部交互点指定、执行中目标更新，以及 Meta Aria 到 Unitree G1 的真实任务线索，说明它不只是接口包装。
  - **为什么现在值得再看**: VLA 部署需要处理用户意图变化和局部目标歧义；gaze-conditioned VLA 正好连接语言之外的实时 grounding 与 action selection。
  - **建议动作**: 快速浏览
  - **关键词**: `VLA` `gaze conditioning` `interactive manipulation` `real robot`
- **Paper**: Learning-augmented robotic automation for real-world manufacturing [[HTML]](https://arxiv.org/html/2604.22235) [[PDF]](https://arxiv.org/pdf/2604.22235)
  - **Paper ID**: `2604.22235`
  - **来源日期**: 2026-04-27
  - **当时可能被低估的信号**: FSM、预教动作段、可插拔 learned primitive、神经 3D 安全监控和安全回退这些信号，说明它提供了少见的真实产线部署约束。
  - **为什么现在值得再看**: 如果今天评估 VLA、World Action Model 或 RL 策略的真实可部署性，这篇能作为工程边界条件参考：学习模块如何嵌入可靠自动化流程。
  - **建议动作**: 继续跟踪
  - **关键词**: `real-world deployment` `manufacturing robotics` `learned primitives` `safety fallback`

## Editor's Picks

### [1]. VoLo: A Physical Orchestrator for Open-Vocabulary Long-Horizon Manipulation [[HTML]](https://arxiv.org/html/2606.07723) [[PDF]](https://arxiv.org/pdf/2606.07723) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.07723`
* **Authors**: Siyi Chen, Hugo Hadfield, Alex Zook, Mikaela Angelina Uy, Chan Hee Song, Erwin Coumans, Xuning Yang, Faisal Ladhak, Qing Qu, Stan Birchfield, Jonathan Tremblay, Valts Blukis
* **Author Priority**: Standard
* **一句话结论**: 值得优先看：VoLo 把 VLA/WAM、感知模型和传统 grasp/place primitive 放进一个 VLM 管理的物理闭环，切中了开放词汇长程操作里“会规划但不会稳健执行”的系统瓶颈。
* **关键词**: `Physical Orchestration` `Open-vocabulary manipulation` `VLA/WAM tools` `Failure recovery` `RoboVoLo`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

开放词汇长程操作不是把若干 pick-and-place 串起来那么简单。机器人需要理解否定条件、复杂指代、物体功能、场景记忆和执行中的失败恢复；同时真实物理世界不会因为模型推理而暂停，动作、观察和工具调用的时序会直接影响结果。现有端到端 VLA/WAM 能生成动作或 rollout，但在多物体、多阶段任务里，单一策略很难同时承担高层推理、状态跟踪、错误检测和低层稳定控制。VoLo 的动机是把这些能力拆成可中断工具，并让 VLM 作为 physical orchestrator 管理“何时调用、何时监控、何时打断、何时恢复”。这使它更像一个真实机器人系统论文，而不是单纯策略网络论文。

#### ⚙️ 核心方法

VoLoAgent 的核心是闭环编排：VLM 不直接承担所有连续控制，而是把 VLA/WAM rollout、感知模型以及 grasp/place primitive 当作可中断工具来调用。摘录明确提到，系统关注物理世界中决策、动作和工具调用的 timing，并把 VLA/WAM 作为 interruptible tool 纳入计划、监控和恢复流程。低层方面，HTML 摘录给出了抓取/放置 primitive 使用同一套 Cartesian-to-joint solver：阻尼最小二乘 IK、null-space joint centering、多起点 ladder、关节限位投影、FK 复核旋转误差以及避免跳到不连续 IK 分支的约束。这说明论文并不只依赖大模型输出，而是把传统运动学鲁棒性作为系统底座。方法新意主要在“orchestration”而非单个模块：VLM 负责把语言目标、场景状态、工具执行反馈和恢复动作组织成一个可持续运行的物理闭环。当前摘录不能确认 VLA/WAM 的具体架构细节、prompt 结构或所有工具 API，因此这些部分需要上传 PDF 后核查。

#### 📊 实验与结果

实验部分给出了 RoboVoLo benchmark：126 个开放词汇长程 manipulation 任务，覆盖四类推理需求，包括 commonsense grounding、memory、complex references 等。任务设计强调不能靠 instruction-independent 的固定行为解决，目标是隔离长程推理与执行耦合能力。结论称 VoLoAgent 优于已有 baselines，消融显示 orchestration 是主要增益来源；但摘录没有保留具体成功率、各 baseline 名称和消融表数字，所以这里只能把它作为方向性证据，而不能引用定量幅度。比较有价值的是 failure analysis 指向 completion monitoring accuracy，说明作者并未把失败简单归因于低层控制，而是把完成状态判断作为后续系统瓶颈。

#### ⚠️ 风险 / 保留意见

- 摘录未给出完整定量表，VoLo 相对 baseline 的优势幅度和统计稳定性需要核查原文。
- 系统依赖 VLM 编排、感知模型、VLA/WAM 和手工 primitive，复现风险来自模块接口和工程细节。
- completion monitoring 被作者点为关键失败来源，长程任务中错误状态一旦被误判，后续恢复可能持续偏离目标。

#### 💭 结论与启发

这篇对后续选题的启发是：长程 VLA 不一定要押注单一端到端策略，物理编排可能是更务实的系统路线。尤其在真实机器人里，可中断、可监控、可恢复比单次动作生成质量更重要。复现时应优先搭一个小规模 orchestrator，把 VLM 规划、状态检测、低层 primitive 和失败恢复接口固定下来，再替换不同 VLA/WAM backbone。读论文时重点看它如何定义工具边界、如何判断子任务完成、以及 orchestration 消融是否真正排除了更强低层 primitive 的影响。

#### 🔎 读 PDF 先核查

- VoLoAgent 如何决定何时打断 VLA/WAM rollout，打断依据来自视觉状态、语言计划还是工具返回信号？
- completion monitoring 的错误类型主要是误报成功、漏检失败，还是复杂指代下的目标混淆？
- RoboVoLo 的 126 个任务是否能区分高层推理增益和低层 grasp/place primitive 鲁棒性增益？

#### 📌 上传 PDF 后优先看

- 系统架构与 tool API 定义章节
- RoboVoLo benchmark 任务构成与 baseline 设置
- orchestration 消融和 failure analysis 章节

### [2]. Q-VGM: Q-Guided Value-Gradient Matching for Flow-Matching VLA Policies [[HTML]](https://arxiv.org/html/2606.08015) [[PDF]](https://arxiv.org/pdf/2606.08015) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.08015`
* **Authors**: Ziqian Wang, Jiayu Sun, Xingjian Mao, Minqian Wang, Yao Mu
* **Author Priority**: Standard
* **一句话结论**: 值得优先看：Q-VGM 直接处理 flow-matching VLA 难以用 RL 稳定微调的问题，用 critic 的 value-gradient 改进速度场，是 VLA 后训练路线里很关键的一步。
* **关键词**: `Flow-matching VLA` `Offline RL` `Value-gradient matching` `Chunk critic` `Policy fine-tuning`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

flow-matching VLA 适合连续控制，因为它通过迭代去噪或速度场把噪声映射到动作 chunk，能表达多模态动作分布。但这类策略给 RL 微调带来两类麻烦：一方面，直接把 value 反传过多步 denoising 在 VLA 尺度上数值不稳定；另一方面，很多 policy-gradient 方法需要可 tractable 的 action likelihood，而 flow policy 往往不方便提供。机器人领域又迫切需要从 imitation/SFT 走向 task-aware post-training，因为少量示范很难覆盖真实任务奖励和失败模式。Q-VGM 的重要性在于它不试图把 flow policy 硬改成传统 stochastic policy，而是用 Q 函数的一阶信息去指导 velocity correction，让 RL 信号进入 flow-matching policy 的原生训练接口。

#### ⚙️ 核心方法

方法流程分两步。第一步训练 action-sensitive chunk critic：critic 条件化在与 VLA 相同的视觉-语言上下文上，但不直接吃所有 prefix token，而是参考 RL Token 设计，把 VLA prefix 压缩成 readout vector，再与 proprioception 投影拼接成 critic state；critic 在 temporally extended action chunk 上学习 value。摘录说明 VLA backbone 和 RLT encoder 在 critic training 与 policy fine-tuning 中冻结，这降低了离线 RL 破坏 pretrained 表征的风险。第二步是 Q-guided value-gradient matching：根据 critic 在 clean action chunk 上的 action-space gradient，对 clean-action estimate 做迭代 Q-gradient ascent，并用 adaptive keep-best selection 保留更优动作；然后把这种动作改进转成 residual velocity correction，让 flow action expert 学会匹配。关键新意是把 critic 的一阶改进信号投影回 velocity-field parameterization，而不是在测试时重排样本或直接对 denoising 链反传。当前摘录不能确认所有损失项形式和稳定化超参，需看 PDF 方法公式。

#### 📊 实验与结果

实验覆盖 simulation 和真实机器人：LIBERO 的 40 个 tabletop tasks、RoboTwin 2.0 的 dual-arm 14-DoF qpos action space，以及两个 7-DoF 真实机械臂桌面任务。设置上，作者从 few-shot SFT 初始化，用 SFT policy 收集固定 rollout buffer，训练 Cal-QL critic，然后在完全离线条件下微调策略，不再与环境交互。对比包括 test-time Q selection、test-time Q guidance、Q-guided action distillation 等共享同一 SFT checkpoint、rollout data、RLT features 和 Cal-QL critic 的 baseline，因此比较焦点比较集中：差异主要是 critic 如何作用于策略。摘录没有给出成功率或提升数值，所以只能确认实验设计覆盖了离线、仿真和少量 real-robot 证据，不能判断提升幅度。

#### ⚠️ 风险 / 保留意见

- 方法依赖 critic 的 action-gradient 质量，离线 buffer 覆盖不足时可能把策略推向 Q 过估计区域。
- VLA backbone 冻结提高稳定性，但也可能限制对新视觉域或新语言语义的适应。
- 摘录未提供具体定量结果，真实机器人任务数量也较少，部署泛化还需要谨慎判断。

#### 💭 结论与启发

这篇最值得借鉴的是“把 RL 信号适配到生成式 action expert 的自然参数化里”。如果后续要做 VLA 后训练，不必只在测试时做 Q rerank，也不必强行套 PPO/SAC；可以考虑让 critic 先产生局部动作改进，再蒸馏为 policy 的内部速度场或残差。复现上应从 LIBERO 小任务开始，先验证 critic gradient 是否真的改善 action chunk，再比较 test-time guidance 与 policy fine-tuning 的差别。读原文时尤其要核查 Cal-QL critic 的训练稳定性、keep-best 选择规则和 residual velocity matching 是否会牺牲原始 flow policy 的多模态性。

#### 🔎 读 PDF 先核查

- Q-VGM 的 iterative Q-gradient ascent 如何避免离线 critic 过估计导致的动作漂移？
- residual velocity matching 会不会压缩 flow policy 原本的多模态动作分布？
- 与 test-time Q guidance 相比，Q-VGM 的优势主要来自训练后推理更快，还是来自策略分布本身被改善？

#### 📌 上传 PDF 后优先看

- critic state/RL Token 设计与 chunk-level value learning
- value-gradient 到 velocity correction 的推导与损失
- LIBERO、RoboTwin 2.0 和真实机器人对比表及消融

### [3]. Ego-Pi: VLA Fine-Tuning for Ego-Centric Human and Robot Data [[VIP]] [[HTML]](https://arxiv.org/html/2606.08107) [[PDF]](https://arxiv.org/pdf/2606.08107) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.08107`
* **Authors**: Ji Woong Kim, Ke Wang, Zipeng Fu, Sirui Chen, Cong Zhao, Jeff Lai, Chelsea Finn
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看：Ego-Pi 有 Chelsea Finn 参与，重点不是又做一个 VLA，而是验证 egocentric 人类数据能否把机器人数据中没有的高层任务语义迁移到 humanoid/dexterous robot。
* **关键词**: `Egocentric human data` `VLA fine-tuning` `Cross-embodiment transfer` `Task semantics` `Chelsea Finn`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

机器人学习长期受限于交互数据稀缺，而人类第一视角视频和示范更容易规模化采集。随着 Apple Vision Pro、Meta Ray-Ban 这类 egocentric 设备普及，以及 humanoid/dexterous hand 与人手形态更接近，用人类数据补足机器人数据语义覆盖变得更现实。Ego-Pi 关注的不是低层轨迹模仿，而是更高层的 task semantics：例如机器人数据只包含把番茄放进一个碗，人类数据展示按颜色分类，模型能否学会“分类规则”并组合已有机器人技能。这个问题对 VLA 很关键，因为真正可扩展的机器人策略不可能为每个新规则、新组合、新排序逻辑都采集机器人示范。

#### ⚙️ 核心方法

当前 HTML 方法摘录很短，只能确认论文围绕 pretrained VLA foundation model 做 human-robot co-training，并在结论中明确提出 practical recipe：action interleaving、human 与 robot hand 的 action alignment、以及 subtask prediction。结合实验描述，可以保守理解为：机器人数据提供可执行的低层技能和 embodiment-specific action grounding，人类 egocentric 数据提供机器人数据缺失的高层语义、规则和组合行为；训练时需要避免人类数据破坏预训练机器人动作能力，因此通过 action interleaving 保留已有权重或行为分布，通过 action alignment 缓解人手和机器人手之间的 embodiment gap，通过 subtask prediction 帮助模型把长任务拆成更易迁移的语义阶段。论文还研究 wrist camera 的作用和 robot hand 选择的影响，说明它把跨 embodiment 迁移视作系统设计问题，而非单纯数据混合问题。由于方法摘录只显示“hyperparameters in Table 2”，具体网络结构、loss、action representation 和 interleaving 细节必须等 PDF 核查。

#### 📊 实验与结果

实验围绕四个问题展开：简单 co-training 是否能教高层语义，subtask generation 和视觉增强是否有帮助，机器人手选择是否影响语义迁移，以及 wrist camera 是否关键。任务包括 tomato sorting by color、boxing、packaging。番茄任务中，机器人数据教基本放置技能，人类示范提供按颜色分到两个碗的规则，用来测试模型能否把新语义绑定到已有机器人技能。结论声称该 recipe 能让 humanoid robot 学到只存在于人类数据中的 novel sorting logic、skill composition 和 rule-based ordering，并达到 90% or higher success rate。需要注意，摘录也承认任务相对短程、偏简单 pick-and-place，并处于固定相机场景，因此这个结果更像人类数据语义迁移的强信号，而不是通用长程 dexterous manipulation 的最终证明。

#### ⚠️ 风险 / 保留意见

- 任务相对短程且偏 pick-and-place，不能直接外推到复杂接触、工具使用或开放场景。
- 固定相机设置降低了视觉泛化难度，egocentric 人类数据到机器人视角的迁移仍需更强证据。
- 方法细节在摘录中不足，action interleaving 和 action alignment 的具体实现会显著影响复现。

#### 💭 结论与启发

Ego-Pi 给后续选题的启发是：人类数据的价值可以先定位在“教语义和组合规则”，而不是直接替代机器人动作数据。一个可复现方向是选择机器人已会的低层技能，再用少量 egocentric 人类数据引入新的分类、排序或条件执行规则，观察模型能否把语义映射到已有技能库。阅读原文时，我会重点核查 action alignment 是否真的解决了手形差异，subtask prediction 是否只是辅助监督，还是推理时也参与控制。作为 Chelsea Finn 参与的工作，它值得纳入长期跟踪，尤其与后续 human data scaling 论文对照。

#### 🔎 读 PDF 先核查

- action interleaving 具体如何保护 pretrained robot policy，不让人类数据破坏低层动作能力？
- human hand 与 robot hand 的 action alignment 是几何映射、token 对齐，还是通过额外监督学习得到？
- 90% 以上成功率主要来自 subtask prediction、视觉增强、手型选择，还是数据本身的语义覆盖？

#### 📌 上传 PDF 后优先看

- human-robot co-training recipe 与 action representation 章节
- 三类任务的数据构成、训练协议和成功率表
- wrist camera、robot hand choice、subtask prediction 的消融

### [4]. SIMPLE: Simulation-Based Policy Learning and Evaluation for Humanoid Loco-manipulation [[VIP]] [[HTML]](https://arxiv.org/html/2606.08278) [[PDF]](https://arxiv.org/pdf/2606.08278) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.08278`
* **Authors**: Songlin Wei, Zhenhao Ni, Jie Liu, Zhenyu Zhao, Junjie Ye, Hongyi Jing, Junkai Xia, Xiawei Liu, Michael Leong, Liang Heng, Di Huang, Yue Wang
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看：SIMPLE 有 Yue Wang 参与，核心价值是为 humanoid loco-manipulation 提供可复现的大规模仿真学习与评测栈，而不是单个策略技巧。
* **关键词**: `Humanoid benchmark` `Loco-manipulation` `MuJoCo + Isaac Sim` `VR teleoperation` `Yue Wang`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

humanoid foundation model 发展很快，但评测明显滞后。真实机器人测试昂贵、慢、难复现，也很难公平 side-by-side 比较不同策略；现有仿真 benchmark 又多集中在桌面机械臂或轮式机器人，无法覆盖 humanoid 需要的动态行走、全身平衡、上肢操作和接触丰富任务。SIMPLE 的动机是补上“可规模化、可复现、面向 whole-body loco-manipulation”的评测基础设施。对 VLA/Physical AI 研究来说，这类基准很重要：如果没有稳定评测环境，humanoid VLA、WAM 或 policy learning 的进展就容易停留在精选 demo，而难以判断泛化、失败模式和训练数据效率。

#### ⚙️ 核心方法

SIMPLE 是一个 full-stack simulation infrastructure。方法核心是 dual-simulator architecture：MuJoCo 负责刚体动力学、接触求解和机器人控制；Isaac Sim 负责 photorealistic ray-traced rendering；每个 simulation step 将物理状态同步到渲染端。这个解耦设计试图同时利用 MuJoCo 的接触稳定性和 Isaac Sim 的视觉多样性。为了支持 generalist foundation models，SIMPLE 还采用 decoupled whole-body control scheme：高层策略，例如 VLA，预测上肢 kinematic trajectories 和 base navigation commands，再交给 lower-body controller 执行。框架还包含大规模 asset curation、数据采集 pipeline 和标准化 evaluation protocol。摘要明确给出规模：60 个 whole-body tasks、50 个 indoor scenes、超过 1,000 个 object assets，并支持 motion planning 自动轨迹生成和低延迟 VR teleoperation。当前摘录不能确认每类任务的完整定义、控制频率、sim-to-real 校准或评价指标细节，需要 PDF 进一步核查。

#### 📊 实验与结果

摘录显示 SIMPLE 集成并大规模 benchmark mainstream humanoid policies，但实验段落在 HTML 中基本回退到摘要，未保留具体策略列表、成功率、排名或消融数字。可以确认的证据是 benchmark 范围和系统能力：60 个任务、50 个室内场景、超过 1,000 个物体，并提供自动轨迹生成与 VR 遥操作两类数据采集方式。作为评测论文，它的实验价值主要不在某个模型刷新指标，而在是否能稳定复现 humanoid loco-manipulation 的多样任务、是否能让不同策略在同一 physics/rendering/control pipeline 下比较。由于摘录缺少定量细节，必须保守表达为“提供评测基础设施和初步基准”，不能声称某类策略显著胜出。

#### ⚠️ 风险 / 保留意见

- dual-simulator 同步会引入工程复杂度，物理状态与渲染状态一致性需要仔细验证。
- 高层 VLA 与 lower-body controller 解耦虽然实用，但可能限制真正统一 whole-body action learning 的评估。
- 摘录缺少 benchmark 结果表，暂时无法判断任务难度分布和 baseline 区分度。

#### 💭 结论与启发

SIMPLE 对后续工作的价值在于提供 humanoid 研究的“评测底座”。如果我要做 humanoid VLA 或 WAM，不能只依赖真实机器人 demo，而应先用类似 SIMPLE 的多任务、多场景环境筛掉不稳定策略。复现和阅读重点应放在任务 taxonomy、控制接口和 evaluation protocol：一个 benchmark 是否有用，取决于它是否能暴露策略在导航、平衡、接触、抓取和视觉泛化上的不同失败模式。作为 Yue Wang 参与的工作，它也值得和后续 PSI Lab 的 humanoid policy 论文一起追踪。

#### 🔎 读 PDF 先核查

- SIMPLE 的 decoupled whole-body control 是否会让 benchmark 更偏向评估上肢 VLA，而低估腿部任务驱动交互？
- 60 个任务如何覆盖导航、平衡、接触、手部操作和长程目标组合，难度是否分层？
- MuJoCo 物理与 Isaac Sim 渲染同步在高速接触或遮挡场景下是否会产生可观测偏差？

#### 📌 上传 PDF 后优先看

- task taxonomy、scene/asset 构成与评价指标章节
- dual-simulator 同步和 whole-body control 接口
- mainstream humanoid policy benchmark 表与失败案例

### [5]. MotionWAM: Towards Foundation World Action Models for Real-Time Humanoid Loco-Manipulation [[HTML]](https://arxiv.org/html/2606.09215) [[PDF]](https://arxiv.org/pdf/2606.09215) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.09215`
* **Authors**: Jia Zheng, Teli Ma, Yudong Fan, Zifan Wang, Shuo Yang, Junwei Liang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看：MotionWAM 把 WAM 从桌面操作推进到实时 humanoid loco-manipulation，并用统一 whole-body motion latent 挑战上肢策略加下肢控制器的常见层级范式。
* **关键词**: `World Action Model` `Humanoid loco-manipulation` `Dual-DiT` `Whole-body motion latent` `Real-time control`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

WAM 的吸引力在于把视频动力学先验接到策略上，让机器人不只是从当前图像直接输出动作，而能借助未来视觉状态或世界动态进行行动推断。但传统 WAM 常受限于高维 video-action latent 的迭代 denoising，推理太慢，不适合 humanoid 闭环控制。humanoid loco-manipulation 还存在另一个结构性问题：多数系统让高层 manipulation policy 控上半身，低层 locomotion controller 只跟踪 base velocity、torso height 或 orientation，导致上下身 action space 不一致，腿部被降级成保持平衡的工具，难以完成踩踏、踢动、脚部辅助接触等任务驱动动作。MotionWAM 的重要性在于同时瞄准“实时 WAM”和“统一全身动作空间”。

#### ⚙️ 核心方法

MotionWAM 被描述为 dual-DiT WAM：一个 Video DiT 建模 egocentric video dynamics，一个 Motion DiT 将视频生成过程中的中间 denoising features 反演为 whole-body humanoid action。它采用 predict-video-dynamics-then-invert 范式，不是直接学习 VLA 式 observation-to-action mapping，而是预测统一 whole-body motion latent。该 latent 覆盖 locomotion、torso motion、height regulation、foot interaction 和 hand manipulation，再由 low-level controller 转换为关节命令。训练采用三阶段 recipe：先做 egocentric video pretraining，再做 cross-embodiment action post-training，最后在 Unitree G1 上用 whole-body teleoperation fine-tuning 专门化。这个设计的新意在于把世界模型的未来视觉隐状态与动作生成耦合，同时把上肢、下肢、躯干和脚部交互放在同一动作表示内。摘录未给出 tokenization 细节、DiT 规模和 latency 数值，需要原文核查。

#### 📊 实验与结果

真实机器人实验围绕三问：视频世界模型是否优于强 VLA baseline，三阶段训练各自贡献什么，以及 WAM 是否足够快用于闭环 humanoid 控制。硬件是 Unitree G1 humanoid，双 ALOHA2 grippers，头戴 Intel RealSense D435i RGB camera；teleoperation 数据由 PICO VR 三点追踪经 SMPL retarget 到机器人；部署时策略输出由 SONIC whole-body controller 跟踪。所有 baselines 和 MotionWAM 作为 WebSocket policy server 在单张 NVIDIA RTX 4090 workstation 上闭环查询。任务是九个真实 whole-body loco-manipulation 任务。结论声称 MotionWAM 超过最强 VLA baseline，但摘录中“by over”后的具体数值缺失，因此不能引用提升幅度，只能确认作者主张有 real-robot 对比和训练阶段消融。

#### ⚠️ 风险 / 保留意见

- 结论中的优势幅度在摘录里缺失，必须核查原文定量表和统计方差。
- 系统依赖 Unitree G1、ALOHA2 grippers、SONIC controller 和 VR teleoperation pipeline，跨平台复现门槛高。
- predict-video-dynamics-then-invert 的中间特征是否真正提升因果控制，而非只是更强预训练表征，需要看消融。

#### 💭 结论与启发

MotionWAM 最有启发的一点是把 WAM 的动作接口从局部末端控制升级到统一 whole-body latent。对于 humanoid 系统设计，这可能比单纯换更大的 VLA backbone 更关键，因为许多任务失败来自 action space 结构不对，而不是语言理解不够。后续阅读应重点核查三阶段训练各自带来的增益、实时推理延迟以及脚部交互任务的具体表现。复现时不必一开始做完整 humanoid，可先在仿真中比较 hierarchical upper-body policy 与 unified whole-body latent 在需要腿部参与任务上的差异。

#### 🔎 读 PDF 先核查

- Video DiT 的中间 denoising features 如何与 Motion DiT 耦合，是 cross-attention、feature conditioning 还是 latent sharing？
- 统一 whole-body motion latent 在脚部交互任务上是否显著优于上肢策略加 base command 的层级 baseline？
- 三阶段训练中 egocentric video pretraining、cross-embodiment post-training 和 G1 teleop fine-tuning 各自贡献多大？

#### 📌 上传 PDF 后优先看

- dual-DiT 架构和 motion latent 表示章节
- 九个真实机器人任务、baseline 设置和实时延迟结果
- 三阶段训练消融与脚部/全身交互失败案例

### [6]. Cosmos 3: Omnimodal World Models for Physical AI [[PDF]](https://arxiv.org/pdf/2606.02800) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.02800`
* **Authors**: NVIDIA: Aditi, Niket Agarwal, Arslan Ali, Jon Allen, Martin Antolini, Adeline Aubame, Alisson Azzolini, Junjie Bai, Maciej Bala, Yogesh Balaji, Josh Bapst, Aarti Basant, Mukesh Beladiya, Mohammad Qazim Bhat, Zaid Pervaiz Bhat, Dan Blick, Vanni Brighella, Han Cai, Tiffany Cai, Eric Cameracci, Jiaxin Cao, Yulong Cao, Mark Carlson, Carlos Casanova, Ting-Yun Chang, Yan Chang, Yu-Wei Chao, Prithvijit Chattopadhyay, Roshan Chaudhari, Chieh-Yun Chen, Junyu Chen, Ke Chen, Qizhi Chen, Wenkai Chen, Xiaotong Chen, Yu Chen, An-Chieh Cheng, Click Cheng, Xiu Chia, Jeana Choi, Chaeyeon Chung, Wenyan Cong, Yin Cui, Magdalena Dadela, Nalin Dadhich, Wenliang Dai, Joyjit Daw, Alperen Degirmenci, Rodrigo Vieira Del Monte, Robert Denomme, Sameer Dharur, Marco Di Lucca, Ke Ding, Wenhao Ding, Yifan Ding, Yuzhu Dong, Nicole Drumheller, Yilun Du, Aigul Dzhumamuratova, Aleksandr Efitorov, Hamid Eghbalzadeh, Naomi Eigbe, Imad El Hanafi, Hassan Eslami, Benedikt Falk, Jiaojiao Fan, Jim Fan, Amol Fasale, Sergiy Fefilatyev, Liang Feng, Francesco Ferroni, Sanja Fidler, Xiao Fu, Vikram Fugro, Prashant Gaikwad, TJ Galda, Katelyn Gao, Yihuai Gao, Wenhang Ge, Sreyan Ghosh, Arushi Goel, Vivek Goel, Akash Gokul, Rama Govindaraju, Jinwei Gu, Miguel Guerrero, Elfie Guo, Aryaman Gupta, Siddharth Gururani, Hugo Hadfield, Song Han, Ankur Handa, Zekun Hao, Mohammad Harrim, Ali Hassani, Nathan Hayes-Roth, Yufan He, Chris Helvig, Cyrus Hogg
* **Author Priority**: Standard
* **一句话结论**: 值得优先看但需谨慎：Cosmos 3 只有摘要回退信息，作为 NVIDIA 的 omnimodal world model 大路线信号很重要，但具体机器人证据必须等完整论文核查。
* **关键词**: `Omnimodal world model` `Physical AI` `Mixture-of-transformers` `World-action model` `NVIDIA Cosmos`
* **证据来源**: Abstract fallback

#### 📖 背景与动机

Physical AI 需要的 foundation model 不只理解图像和语言，还要能处理视频动态、声音、动作序列和未来状态生成。传统 VLM、video generator、world simulator、world-action model 往往分开训练和使用，导致 embodied agent 系统里存在多模型拼接、模态接口不统一和训练目标不一致的问题。Cosmos 3 的动机是用统一的 omnimodal world model 同时处理和生成 language、image、video、audio、action sequences，从而把理解、生成、仿真和策略建模合成一个可扩展 backbone。对今天的 VLA/WAM 主题来说，它代表更上游的大模型路线：如果模型本身能统一世界动态与动作序列，机器人策略可能不再需要在 VLM、video model、action head 之间做大量手工桥接。

#### ⚙️ 核心方法

当前只有 abstract fallback，能确认的信息有限：Cosmos 3 是一组 omnimodal world models，采用 unified mixture-of-transformers architecture，支持高度灵活的 input-output configurations，并声称可统一 vision-language models、video generators、world simulators 和 world-action models。这里不能补充具体网络层数、tokenizer、训练数据规模、损失函数或 action representation，因为摘录没有提供。可以保守推断，它的关键方法主张是把不同模态作为同一 transformer 混合架构中的可组合输入输出，而不是为每种任务单独训练模型；这会让 embodied agent 在同一 backbone 中完成感知理解、未来视频生成、世界状态模拟和动作序列建模。真正需要核查的是 action sequence 在架构中是否与图像/视频/语言对等建模，还是作为特定 post-training head；以及 mixture-of-transformers 是用于模态专家、任务专家还是规模扩展。

#### 📊 实验与结果

摘要声称 Cosmos 3 在多样 understanding 和 generation tasks 上达到新的 state-of-the-art，并称 post-trained Cosmos 3 models 在技术报告发布时被 Artificial Analysis 评为最佳 open-source Text-to-Image 和 Image-to-Video models，被 RoboArena 评为最佳 policy model。由于只有摘要回退，不能引用任何具体 benchmark 名称、分数、排名日期之外的细节或机器人任务设置。对机器人读者而言，目前可确认的证据边界是：它不仅报告视觉生成能力，也把 policy model 纳入评估叙事；但是否有真实机器人闭环控制、sim2real、long-horizon manipulation 或 WAM-style planning 的强证据，必须等待 HTML/PDF 正文核查。

#### ⚠️ 风险 / 保留意见

- 只有摘要信息，所有架构、数据、实验细节都不能展开，当前只能作为趋势信号处理。
- 大规模 omnimodal 模型的 policy 能力可能依赖 post-training 和评测平台，未必直接转化为可复现机器人部署。
- “统一所有模态”的系统复杂度很高，action 接口、实时性和安全约束可能成为落地瓶颈。

#### 💭 结论与启发

Cosmos 3 的阅读价值在于判断 world model 是否正在从机器人小模型走向通用 omnimodal backbone。对后续选题，它提示两个方向：一是把 WAM/VLA 看成更大 omnimodal 模型的 action-conditioned 子能力，二是关注 action sequence 与 video dynamics 是否能在同一模型内互相强化。但在只有摘要时，不应把它当作已验证的机器人方法。上传 PDF 后应优先确认 policy evaluation 的任务定义、action 表示和模型实时性，再决定它是可复现技术路线，还是主要代表大厂 scaling signal。

#### 🔎 读 PDF 先核查

- Cosmos 3 中 action sequences 是原生模态 token，还是通过 post-training policy head 接入？
- RoboArena 的 policy model 评估具体包含哪些机器人任务、输入输出接口和对比模型？
- mixture-of-transformers 架构如何在 language、image、video、audio、action 之间共享或隔离能力？

#### 📌 上传 PDF 后优先看

- 模型架构与模态 tokenization 章节
- policy model/RoboArena 评估设置与结果
- 训练数据、post-training recipe 和实时推理约束

## Watchlist

### [W1]. MotionVLA: Injecting Geometric Motion into Vision-Language-Action Model [[HTML]](https://arxiv.org/html/2606.08288) [[PDF]](https://arxiv.org/pdf/2606.08288)
* **Paper ID**: `2606.08288`
* **Authors**: Shanglin Yuan, Weiheng Zhao, Xianda Guo, Wei Sui, Li Yu, Wenyu Liu, Xinggang Wang
* **Author Priority**: Standard
* **为什么还值得留意**: MotionVLA 进入 shortlist 是因为它提出“记住连接过去帧的 motion，而不是简单记住历史帧”的接口，对长程 VLA 的时序稳定性很有价值。它在 RoboTwin2.0、LIBERO 和初步 Agilex Piper 结果上主张提升 motion consistency 与 path efficiency。但今天没有进最终精选，主要是因为它更像 VLA 表征增强模块，系统层面的闭环、RL 后训练或 humanoid/world-model 影响面弱于六篇精选。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. Two Bridges, One Pathway: From VLMs to Generalizable VLAs with Embodied Trajectory-Coupled Data [[HTML]](https://arxiv.org/html/2606.08520) [[PDF]](https://arxiv.org/pdf/2606.08520)
* **Paper ID**: `2606.08520`
* **Authors**: Linqi Yin, Shiduo Zhang, Shenling Qiu, Chenxin Li, Zhaoyang Fu, Lei Xiao, Xiang Wang, Chenchen Yang, Zhe Xu, Pengfang Qian, Jingjing Gong, Xipeng Qiu, Xuanjing Huang, Yu-Gang Jiang
* **Author Priority**: Standard
* **为什么还值得留意**: Two Bridges, One Pathway 值得跟踪，因为它把 VLM 到 VLA 的 gap 拆成 embodied distribution gap 和 action objective gap，并用 Embodied Trajectory-Coupled data 做渐进桥接。它覆盖 LIBERO、SimplerEnv、VLABench 和 WidowX 真实任务，问题设定很正。但与 Ego-Pi 相比，它的摘录更偏中间数据配方，今天最终精选更优先保留了 human egocentric data 到机器人语义迁移这条更直接的机器人数据扩展信号。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)

### [W3]. GEAR-VLA: Learning Geometry-Aware Action Representations for Generalizable Robotic Manipulation [[HTML]](https://arxiv.org/html/2606.08530) [[PDF]](https://arxiv.org/pdf/2606.08530)
* **Paper ID**: `2606.08530`
* **Authors**: Yuan Zhang, Shiqi Zhang, Yedong Shen, Shuai Dong, Jiajun Deng, Xin Zhang, Yuxuan Gao, Jiajia Wu, Xin Nie, Zhiyuan Cheng, Jianmin Ji, Yanyong Zhang, Xingyi Zhang, Jia Pan
* **Author Priority**: Standard
* **为什么还值得留意**: GEAR-VLA 进入 watchlist 是因为它同时处理 coarse-to-fine action learning、semantic-aligned 3D integration 和 embodiment canonicalization，目标直指 VLA 真实部署中的 unseen objects、background shifts 和 embodiment differences。摘录中训练规模很大，包括 240 H200、Qwen2.5-VL、VGGT、FAST tokenizer 和 causal VQ-VAE，工程投入值得关注。没有进最终精选的原因是方法栈很重，摘录虽信息丰富但需要更多定量证据来判断各模块是否必要。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. Video2Sim2Real: Full-Stack Autonomous Dexterous Skill Acquisition from a Single Human Video [[HTML]](https://arxiv.org/html/2606.08828) [[PDF]](https://arxiv.org/pdf/2606.08828)
* **Paper ID**: `2606.08828`
* **Authors**: Yunhai Han, Jianuo Qiu, Linhao Bai, Ziyu Xiao, Zihang Zeng, Yangcen Liu, Zhaodong Yang, Shalin Jain, Wenrui Ma, Jiaqi Fu, Yuqian Zheng, Manisha Natarajan, Muhammad Zubair Irshad, Kenneth Shaw, Matthew Gombolay, Zsolt Kira, Harish Ravichandar
* **Author Priority**: Standard
* **为什么还值得留意**: Video2Sim2Real 很贴近 Sim2Real 主题：从单个人类视频重建 digital twin，提取运动先验，再通过 trajectory refinement 和 decoupled sim-to-real policy 获得 dexterous skills。它覆盖 Kinova Gen + Leap Hand、IsaacGym 和多类日常操作任务，完整栈很吸引人。没有进最终精选，是因为今天主线更偏 VLA/WAM 与 humanoid foundation policy；这篇更像独立 dexterous skill acquisition 系统，适合后续 Sim2Real 专题深读。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
