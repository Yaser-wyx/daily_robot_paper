# RoboPulse | 2026-06-23

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 256 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线很集中：VLA 正在从“看图出动作”的监督策略，转向带世界模型、动作预测、主动感知和 RL 后训练的闭环系统。最终精选保留了三类关键方向：SafeDojo 与 dVLA-RL 代表安全/RL 后训练，Vesta 与 WAM Survey 帮助建立 embodied reasoning 与 world action model 的系统框架，FlowDPG 与 See2Act 则把 diffusion/flow policy 推向真实长程操作和主动视角选择。VIP 作者里，Yuke Zhu 参与的 Vesta 值得优先跟踪，因为它试图把定位、空间推理、导航和长程规划压进单一 embodied generalist；Deepak Pathak 参与的 FlowDPG 直接切中真实机器人 RL；Danfei Xu 参与的 See2Act 则把主动感知作为 imitation policy 内生能力处理。整体看，今天更像是 VLA 后训练与 world/action model 概念收敛的一天，而不是单点 benchmark 刷榜。

## 今日信号

- VLA 的下一步不只是扩大模型或数据，而是把可预测未来、可优化动作和可验证安全性放进同一个闭环。
- World Action Model 正在从松散概念变成一个可比较的技术族谱，核心分歧在 future 表示、action coupling、backbone 和部署方式。
- 真实机器人后训练正在绕开昂贵或脆弱的端到端梯度路径，转向 critic 梯度蒸馏、denoising trajectory RL 和主动感知式推理。

## Historical Rediscovery

- **Paper**: UniT: Toward a Unified Physical Language for Human-to-Humanoid Policy Learning and World Modeling [[HTML]](https://arxiv.org/html/2604.19734) [[PDF]](https://arxiv.org/pdf/2604.19734)
  - **Paper ID**: `2604.19734`
  - **来源日期**: 2026-04-22
  - **当时可能被低估的信号**: 视觉锚定的 latent action tokenizer、human+robot 混合预训练、真实 humanoid 任务和 OOD 设定同时出现，说明它不只是动作迁移工程，而可能是在探索跨具身 action/world 表征。
  - **为什么现在值得再看**: 今天关注 VLA、World Model 和 World Action Model 时，跨 embodiment 的动作 token 与物理语言可能直接影响 VLA 如何吸收人类数据、机器人数据和长时程控制经验。
  - **建议动作**: 加入精读
  - **关键词**: `world model` `latent action tokenizer` `cross-embodiment` `humanoid policy learning` `VLA`
- **Paper**: Co-VLA: Coordination-Aware Structured Action Modeling for Dual-Arm Vision-Language-Action Systems [[HTML]](https://arxiv.org/html/2606.20285) [[PDF]](https://arxiv.org/pdf/2606.20285)
  - **Paper ID**: `2606.20285`
  - **来源日期**: 2026-06-19
  - **当时可能被低估的信号**: Structured Action Expert、Latent-Aware Controller 和 Co-Motion 数据范式同时指向“动作结构本身”而不是单纯扩大模型或数据，这一点当时可能被 world model 主线盖过。
  - **为什么现在值得再看**: 对长时程操作和真实部署来说，双臂协调是 VLA 能否从单臂 demo 扩展到复杂任务的关键瓶颈；这篇可作为 World Action Model 中 action factorization 与 coordination prior 的参考。
  - **建议动作**: 加入精读
  - **关键词**: `VLA` `dual-arm manipulation` `structured action modeling` `coordination` `long-horizon operation`
- **Paper**: Tri-Info: Generalizable, Interpretable Failure Prediction for VLA Models via Information Theory [[HTML]](https://arxiv.org/html/2606.19998) [[PDF]](https://arxiv.org/pdf/2606.19998)
  - **Paper ID**: `2606.19998`
  - **来源日期**: 2026-06-19
  - **当时可能被低估的信号**: 覆盖六个 VLA、三个 benchmark，并包含真实 ALOHA 轨迹；这些信号说明它不是只在单一模型上做离线诊断，而是在接近 deployment safety 的评测设置中验证预警能力。
  - **为什么现在值得再看**: VLA 走向真实部署后，失败预测、接管触发和安全监测会成为策略能力之外的核心问题；它与 VLA deployment、真实评测和安全闭环强相关。
  - **建议动作**: 加入精读
  - **关键词**: `VLA safety` `failure prediction` `real ALOHA` `deployment` `interpretability`
- **Paper**: ThinkingVLA: Interleaved Vision and Language Reasoning for Robotic Manipulation [[PDF]](https://arxiv.org/pdf/2606.17937)
  - **Paper ID**: `2606.17937`
  - **来源日期**: 2026-06-17
  - **当时可能被低估的信号**: next visual state prediction 加 inverse dynamics 的分解，比普通 reasoning VLA 更接近“先想象状态变化，再反推动作”的 action-conditioned world modeling；当时因只有摘要回退而被压低优先级。
  - **为什么现在值得再看**: 如果后续 PDF 能支撑架构和实验细节，这篇可能对 VLA 长时程推理、视觉状态预测和动作反演提供直接参考。当前适合补读确认其真实贡献强度。
  - **建议动作**: 快速浏览
  - **关键词**: `reasoning VLA` `visual state prediction` `inverse dynamics` `world action model` `manipulation planning`
- **Paper**: Bridging the Embodiment Gap: Disentangled Cross-Embodiment Video Editing [[HTML]](https://arxiv.org/html/2605.03637) [[PDF]](https://arxiv.org/pdf/2605.03637)
  - **Paper ID**: `2605.03637`
  - **来源日期**: 2026-05-06
  - **当时可能被低估的信号**: 显式解耦任务语义与 embodiment 表征这一点，比一般视频数据增强更接近机器人预训练数据可迁移性的根问题。
  - **为什么现在值得再看**: VLA 和 WAM 若要利用互联网视频或人类示范，需要解决语义保持、具身转换和物理一致性之间的张力；这篇可作为 cross-embodiment data engine 的线索继续看。
  - **建议动作**: 继续跟踪
  - **关键词**: `Sim2Real` `embodiment gap` `human video` `VLA data` `cross-embodiment`

## Editor's Picks

### [1]. SafeDojo: Safe Reinforcement Learning for VLA via Interactive World Model [[HTML]](https://arxiv.org/html/2606.20698) [[PDF]](https://arxiv.org/pdf/2606.20698) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.20698`
* **Authors**: Kai Tang, Peidong Jia, Zhong Chu, Jixian Wu, Rui Ma, Jiajun Cao, Fangyuan Zhao, Sixiang Chen, Yichen Guo, Xiaowei Chi, Chun-Kai Fan, Kevin Zhang, Jinchang Xu, Fubing Yang, Weishi Mi, Xiaozhu Ju, Jian Tang, Shanghang Zhang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看：SafeDojo 把 world model-based imagination 用于 VLA 安全 RL，是今天最直接连接 VLA、safe RL 与 Sim2Real 部署风险的一篇。
* **关键词**: `Safe RL` `VLA` `World Model` `SafeLIBERO` `Imagined Trajectories`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

SafeDojo 关注的是 VLA 部署中很现实的安全问题：在障碍物丰富、接触密集的操作场景里，策略不仅要完成任务，还要避免碰撞。传统 safe RL 往往需要真实环境探索，或者依赖人工设计的 safety function，这两点都不适合开放环境中的高维视觉输入和不可逆物理失败。对 VLA 来说，安全边界不是低维状态里的简单约束，而是隐藏在图像、物体布局和语言目标共同决定的动作可行性中。因此，这篇的动机不是单纯提高成功率，而是让 VLA 在不依赖真实危险探索的前提下学习“哪些动作会出事”。

#### ⚙️ 核心方法

论文提出 SafeDojo，定位为面向 VLA 的 model-based safe RL 框架。根据摘录，核心是利用 interactive video world model 生成 imagined trajectories，并在这些想象轨迹上学习任务进展信号与安全信号，从而减少真实探索和人工安全函数需求。它建立在 OpenVLA-OFT 这类离散 action-token VLA backbone 上，先用 SafeLIBERO demonstration 得到共享 SFT checkpoint，再在此基础上做在线 RL 与安全优化。方法的新意在于把安全学习从真实机器人试错迁移到 world model imagination：VLA 不只是预测下一步动作，也借由可交互视频模型观察潜在动作后果。当前摘录能确认其目标包括 collision-free safe VLA policies、world model imagined trajectories、task progress 与 safety signal 学习；但具体 reward 形式、世界模型交互接口、RL objective 和安全信号标注机制仍需看 PDF 方法章节核查。

#### 📊 实验与结果

实验主要在 SafeLIBERO 上进行，环境基于 LIBERO 和 Robosuite，使用单臂 Franka Emika Panda 7-DoF 机械臂。SafeLIBERO 包含 Spatial、Goal、Object、Long 四个 suite，每个 suite 有四个任务和两种 obstacle-interference level；训练只在 Level I，评估覆盖 Level I 和 Level II，以测试泛化。论文还报告了 5 个真实 Franka 任务验证。对比包括 OpenVLA-OFT、AEGIS、PPO、SafeVLA 以及 model-based RL baselines，且都基于同一 OpenVLA-OFT backbone 和共享 SFT checkpoint。结论摘录称 SafeDojo 在 SafeLIBERO 两个 level 的 aggregate TSR、SSR、ETS 上最好，并在真实部署上也有最佳平均表现，但除这些指标名外，摘录没有给出完整数字，不能进一步展开具体幅度。

#### ⚠️ 风险 / 保留意见

- 安全能力高度依赖 interactive world model 的预测可信度，尤其是接触、碰撞和遮挡状态是否被准确建模。
- 摘录没有说明 imagined safety signal 与真实碰撞风险之间的校准方式，部署时可能存在仿真安全与真实安全错配。
- 真实机器人验证只有 5 个 Franka 任务的信息，任务多样性和长期运行稳定性还需要 PDF 进一步确认。

#### 💭 结论与启发

这篇对后续选题的启发在于：VLA 安全不一定要从外部 CBF 或规则过滤器开始，也可以把安全看成可通过 world model 反事实想象学习的策略属性。若要复现，优先应复刻 SafeLIBERO 的 Level I 到 Level II 泛化设置，并检查世界模型错误如何影响安全指标。系统设计上，可以把 SafeDojo 当作“VLA 后训练层”：底层仍保留通用 VLA，外层通过想象轨迹把任务进展和安全约束合并优化。

#### 🔎 读 PDF 先核查

- interactive video world model 如何接收候选动作并生成可用于安全学习的 imagined trajectory？
- task progress signal 与 safety signal 是由模型预测、规则生成，还是从 demonstration/benchmark 标注中学习得到？
- SafeDojo 在 Level II OOD 障碍布局上的提升来自 world model 泛化，还是来自 RL 对 SafeLIBERO 分布的适配？

#### 📌 上传 PDF 后优先看

- 方法章节中的 world model 交互接口与 RL objective
- SafeLIBERO Level I/Level II 泛化实验和 TSR/SSR/ETS 表格
- 真实 Franka 任务设置、失败案例和 safety violation 定义

### [2]. World Action Models: A Survey [[HTML]](https://arxiv.org/html/2606.20781) [[PDF]](https://arxiv.org/pdf/2606.20781) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.20781`
* **Authors**: Qiuhong Shen, Shihua Zhang, Yue Liao, Qi Li, Zhenxiong Tan, Shizun Wang, Shuicheng Yan, Xinchao Wang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看：这篇 survey 的价值不在新算法，而在给 World Action Model 划边界、建分类法，适合作为后续 WAM/VLA/world model 阅读地图。
* **关键词**: `World Action Model` `Survey` `VLA` `Action Coupling` `Embodied Prediction`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

过去两年 embodied AI 从 VLA 走向能预测未来的策略模型，但“world model”“video generation model”“action-conditioned video model”“VLA”“World Action Model”之间边界开始混乱。标准 VLA 可以把观察和指令映射到动作，却不显式建模自己的动作如何改变环境，因此对物理、接触、视角变化和长程后果的表达有限。与此同时，很多工作借用视频生成模型、语言模型或视觉语言 backbone 做 action-grounded prediction，但命名和评估标准并不统一。这篇 survey 的动机是为 WAM 建立共同语言：哪些模型只是生成视频，哪些模型真正把可行动未来与控制决策耦合起来。

#### ⚙️ 核心方法

论文把 WAM 抽象成一个共同数学对象：关于未来预测和未来动作的条件联合分布。基于这个视角，它用四个维度组织已有工作：predictive substrate，即模型预测什么形式的未来；action coupling，即动作与未来预测如何绑定；architectural backbone，即使用视频生成、语言、视觉语言或其他模型族；deployment regime，即模型在控制环中如何被调用。这个框架比按论文枚举更有价值，因为同名 WAM 可能实现细节完全不同，而异名工作可能共享同一技术结构。摘录还显示，论文把数据与评估作为单独问题处理：训练数据决定未来变量、动作标签质量和 embodiment transfer；评估协议则决定模型是否真的能服务闭环控制，而不仅是生成看起来合理的视频。

#### 📊 实验与结果

作为 survey，它没有提出单一实验结果，而是系统整理数据来源和评估维度。摘录中明确提到 WAM 训练数据被分成五类，其中 robot teleoperation 被认为能提供最干净的 action-conditioned trajectory，因为人类操作者驱动 embodiment 并同步记录命令流和视觉观察；Open X-Embodiment 被描述为跨实验室、跨平台的典型资源。评估方面，论文强调视觉保真度、闭环成功率、物理合理性和评估成本之间存在 trade-off。这里的重要证据不是数值，而是它把“看起来像未来”的视频生成与“能改善控制”的 action-grounded evaluation 区分开。

#### ⚠️ 风险 / 保留意见

- survey 的判断依赖作者分类框架，具体论文归类可能随新工作快速变化。
- 摘录没有展示完整 taxonomy 表和覆盖论文清单，需要核查是否遗漏关键 VLA/RL/world model 工作。
- 概念边界有助于理解，但不能替代对各 WAM 在真实机器人闭环中的实证比较。

#### 💭 结论与启发

这篇适合作为之后建立 paper reading database 的骨架。读 WAM 类论文时，可以强制记录四个字段：预测什么未来、动作如何进入模型、backbone 是什么、推理时如何闭环调用。对系统设计也有帮助：如果目标是机器人控制，而不是视频预测，就必须把 evaluation 指向闭环任务成功、物理一致性和动作可执行性。后续读 SafeDojo、MV-WAM、UniviewVLA、See2Act 时，都可以用这篇 survey 的四维框架做横向比较。

#### 🔎 读 PDF 先核查

- 论文如何精确定义 WAM 与普通 world model、video generation model、VLA 的边界？
- 四维 taxonomy 是否能覆盖 SafeDojo、MV-WAM、UniviewVLA、See2Act 这类近期工作？
- 作者认为 WAM 最可靠的评估协议是闭环机器人任务、离线规划，还是 action-conditioned prediction 指标？

#### 📌 上传 PDF 后优先看

- WAM 定义与边界澄清章节
- 四维 taxonomy：predictive substrate、action coupling、backbone、deployment regime
- 数据来源与评估协议章节，尤其是 closed-loop control 相关讨论

### [3]. Vesta: A Generalist Embodied Reasoning Model [[VIP]] [[HTML]](https://arxiv.org/html/2606.20905) [[PDF]](https://arxiv.org/pdf/2606.20905) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.20905`
* **Authors**: Johan Bjorck, Zhiqi Li, Yunze Man, Jing Wang, An-Chieh Cheng, Sifei Liu, Shihao Wang, Zhiding Yu, Abhishek Badki, Stan Birchfield, Valts Blukis, Yevgen Chebotar, Siyi Chen, Sicong Leng, Yu-Cheng Chou, Tianli Ding, Boyi Li, Zhengyi Luo, Hang Su, Jonathan Tremblay, Tingwu Wang, Bowen Wen, Jimmy Wu, Xianghui Xie, Hanrong Ye, Hongxu Yin, K.R. Zentner, Liangyan Gui, Yu-Xiong Wang, Yuke Zhu, Linxi "Jim" Fan, Jan Kautz
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看：Vesta 是今天最重要的 embodied generalist 论文，且有 Yuke Zhu 参与，适合重点跟踪其空间推理、记忆和规划统一建模路线。
* **关键词**: `Embodied Generalist` `Spatial Reasoning` `Memory` `Action Planning` `Yuke Zhu`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

Vesta 解决的是 embodied robot stack 过度碎片化的问题。真实机器人需要同时做定位、空间推理、导航、长期记忆和高层规划，而现有系统常把这些能力拆成多个 specialist，再由 planner VLM 和 action VLA 形成层级堆栈。这种方式计算成本高，也容易出现级联错误：一个模块的定位或记忆失败会污染后续规划，最终影响动作执行。Vesta 的动机是训练一个统一 embodied foundation model，让同一个模型在多个能力轴上都达到或超过 specialist，从而减少系统拼接带来的复杂性。对 VLA 方向而言，它更像是 action policy 上游的 generalist planner，但会直接影响未来 VLA 如何接入记忆、导航和空间 grounding。

#### ⚙️ 核心方法

根据摘录，Vesta 的方法由两部分支撑：一是大规模、多样化、经过 curated 的 embodied corpus，用于诱导 spatial grounding；二是一个简单的 multimodal memory harness，让模型能在长时间跨度上推理。论文把能力范围覆盖到 localization、spatial reasoning、navigation、long-horizon planning 等，目标是用单一 foundation model 替代多个 per-task specialist。实验中还引入 offline action planning benchmark，把真实机器人规划评估转成 MCQ：每个决策点给出当前观察、语义目标和历史，让 planner 选择下一步子目标或动作。当前摘录只能确认它是 embodied planner/generalist，并非底层连续控制 VLA；它与 action model 的关系更像“高层决策器 + 下游 actor”。具体模型架构、训练语料规模、memory harness 的输入输出格式、以及如何与真实 manipulation actor 连接，需要 PDF 进一步核查。

#### 📊 实验与结果

论文在 embodied reasoning 和 action planning 上报告了多类 benchmark。摘录称 Vesta 在 cognition 和 localization benchmark 中平均分最高，在多数 cognition 与 localization benchmark 上领先，其余保持接近。对于真实机器人，结论明确给出一个数字：在 memory-heavy manipulation tasks 上，相比 actor-only baseline，成功率提高 38.3%。论文还设计 offline action planning benchmark，以 MCQ 形式降低真实机器人评估成本，并报告 Vesta 显著优于其他模型。需要注意的是，摘录中关于“平均超过 strongest individual baseline”和“超过 ensemble baseline”的具体点数缺失，因此不能引用具体幅度。

#### ⚠️ 风险 / 保留意见

- Vesta 更偏高层 embodied reasoning/planning，不能直接等同于端到端低层 VLA 控制策略。
- offline MCQ planning benchmark 能降低成本，但可能无法完全反映闭环执行中的误差累积。
- 摘录没有给出训练语料细节和模型尺寸，复现难度与数据依赖需要重点核查。

#### 💭 结论与启发

Vesta 的启发在于，VLA 系统可能不应只追求更强 actor，而应把 planner 的空间记忆和长期推理能力系统化。对后续阅读来说，应关注它如何构造 embodied corpus，以及 memory harness 是否足够简单到可以被其他 VLA pipeline 复用。如果复现资源有限，可以先复刻 offline planning MCQ 评估，用它测试不同 VLM/VLA planner 在历史信息和空间 grounding 下的决策质量，再决定是否接真实机器人。

#### 🔎 读 PDF 先核查

- Vesta 的 multimodal memory harness 如何表示历史观察、语言目标和空间状态？
- offline MCQ planning benchmark 的候选动作如何生成，是否会把规划问题简化为检索问题？
- 真实机器人 memory-heavy tasks 中 38.3% 提升来自 planner 记忆能力，还是来自更好的任务分解与 actor 调用接口？

#### 📌 上传 PDF 后优先看

- 数据构建与 embodied corpus 章节
- multimodal memory harness 和模型架构章节
- offline action planning benchmark 与 real-world manipulation 实验

### [4]. FlowDPG: Deterministic Policy Gradient on Flow Matching Policies for Real-World Manipulation [[VIP]] [[HTML]](https://arxiv.org/html/2606.22303) [[PDF]](https://arxiv.org/pdf/2606.22303) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.22303`
* **Authors**: Kexin Shi, Junyao Shi, Poorvi Hebbar, Zhuolun Zhao, Tarun Amarnath, Yifan Su, Shikhar Bahl, Deepak Pathak
* **Author Priority**: Extended VIP
* **一句话结论**: 值得优先看：FlowDPG 是真实机器人 RL 后训练的强信号论文，针对 flow matching policy 避免 BPTT，并在双臂 AirPods 装配上给出 92% 端到端成功率。
* **关键词**: `Flow Matching` `DDPG` `Real-World RL` `Diffusion Transformer` `Deepak Pathak`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

FlowDPG 面向 imitation learning 在长程、接触密集任务中的短板：监督策略会继承 demonstration distribution，一旦部署环境偏离数据覆盖，错误会沿多个阶段累积。真实机器人 RL 是自然补充，但对 flow matching policy 来说，标准 policy gradient 需要沿多步 ODE 从噪声到动作反传，计算昂贵且数值脆弱。扩散/flow 类策略在机器人中很强，但如果 RL 后训练路径过重，就很难用于真实硬件迭代。FlowDPG 的核心动机是保留 flow policy 的表达能力，同时让 critic gradient 能以更稳定、更便宜的方式进入 velocity field。Deepak Pathak 参与也让这篇值得作为真实机器人 RL 路线重点跟踪。

#### ⚙️ 核心方法

方法是一个为 flow matching policies 定制的 DDPG-style RL。摘录显示，视觉部分用 DINOv2 encoder 融合多视角 RGB 和 proprioceptive state，得到共享 state embedding；flow matching velocity predictor 是 Diffusion Transformer，一次前向生成 n-step action chunk。价值部分在共享 embedding 上接三个容量匹配的 MLP，包括 value head 和两个接收 flatten action chunk 的 Q-networks，并配套 EMA target 用于 value loss。关键思想是把 critic gradient 蒸馏进训练时的 velocity field，通过 single-step projection 和 L2 regression 避免沿 denoising ODE 做 BPTT。直觉上，它把 demonstration-driven vector 与 critic-improvement vector 结合：一个保持行为分布和可执行性，另一个推动策略向高价值动作移动。结论还提到该更新在三个明确近似下可恢复 vanilla DPG，这说明作者试图给方法一个理论连接，而不只是工程 trick。

#### 📊 实验与结果

实验任务是长程双臂 AirPods assembly，包含 8 个顺序子阶段，case 和 pod pose 随机，硬件为两台 Franka，示范通过 GELLO teleoperation 采集。每个 policy 在 25 个 cases 上评估，共 50 次 pod manipulation；阶段内失败不会终止 episode，允许 retry。指标包括 per-stage success rate、阶段平均 Avg，以及要求所有 pods 正确插入的 end-to-end Overall。对比覆盖 value-conditioning 方法、冻结 base policy 加 adapter 的 auxiliary-module 方法，以及 critic-gradient 类方法。结论明确给出 FlowDPG 在该任务上达到 92% end-to-end success，并称机制级消融支持各设计选择。摘录没有给出各 baseline 数值，因此不应夸大相对幅度。

#### ⚠️ 风险 / 保留意见

- 奖励依赖 stage-level annotations，可能限制在更开放任务中的适用性。
- 一致性正则只最小化平均 projection error，少数 critic gradient 不可靠状态可能未被识别。
- AirPods assembly 证据很强但任务类型集中，需要验证是否泛化到更多物体、工具和接触模式。

#### 💭 结论与启发

FlowDPG 对系统设计的启发很直接：如果已有 diffusion/flow imitation policy，不一定要推倒重来做 RL policy，可以把 critic 的改进方向压进生成过程的 velocity field。复现时应优先实现最小闭环：固定 flow policy backbone、训练 Q/value heads、验证 single-step projection 是否稳定，再上真实机器人。论文也提醒我们，机器人 RL 后训练的关键不只是 reward 设计，而是让梯度路径与生成式策略的采样机制相容。

#### 🔎 读 PDF 先核查

- critic gradient 到 velocity field 的 single-step projection 具体如何定义，在哪些近似下等价于 DPG？
- demonstration-driven vector 与 critic-improvement vector 的权重或调度如何影响稳定性？
- stage-level reward annotation 的成本是多少，是否能替换成自动进度估计或视觉奖励模型？

#### 📌 上传 PDF 后优先看

- FlowDPG objective、projection 和 L2 regression 推导
- 双臂 AirPods assembly 任务协议与 baseline 表格
- 机制级消融：BPTT 替代、critic gradient、consistency regularizer

### [5]. dVLA-RL: Reinforcement Learning over Denoising Trajectories for Discrete Diffusion Vision-Language-Action Models [[PDF]](https://arxiv.org/pdf/2606.23623) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.23623`
* **Authors**: Yuhao Wu, Yitian Liu, Weijie Shen, Mishuo Han, Wenjie Xu, Haotian Liang, Zhongshan Liu, Yinan Mao, Lei Xu, Xinping Guan, Ru Ying, Ran Zheng, Wei Sui, Xiaokang Yang, Wenbo Ding, Yao Mu
* **Author Priority**: Standard
* **一句话结论**: 值得优先看但需保守阅读：dVLA-RL 只提供摘要回退信息，仍然重要，因为它把 RL 明确引入 discrete diffusion VLA 的 denoising trajectory。
* **关键词**: `Discrete Diffusion VLA` `RL` `Denoising Trajectory` `Masked Generative Modeling` `Policy Refinement`
* **证据来源**: Abstract fallback

#### 📖 背景与动机

dVLA-RL 关注的是 Discrete Diffusion VLA 的后训练空白。现有 VLA action 表达大致包括连续 diffusion/flow、离散 autoregressive、并行解码，以及近期的离散扩散式 masked generative modeling。dVLA 的吸引力在于把视觉、语言和动作统一到离散 token 空间，并通过迭代 refinement 生成动作；但摘要明确指出，它此前主要停留在 SFT 训练，RL 进一步优化策略的潜力尚未充分探索。问题在于 dVLA 最终动作的边缘概率难以处理，常规 RL objective 很难直接套用。这对 VLA 很关键，因为如果离散扩散动作模型不能做 RL 后训练，就会在真实长程任务和偏离示范分布时受限。

#### ⚙️ 核心方法

当前只有摘要回退，能确认的信息有限：论文提出 dVLA-RL，目标是在 discrete diffusion VLA 上做 reinforcement learning，并且标题说明优化对象是 denoising trajectories，而不是只看最终动作。合理推断是，作者试图绕开最终动作 marginal probability intractable 的困难，把 RL 信号分配或建模在离散扩散的逐步去噪过程中，使策略 refinement 过程本身可优化。摘要还说明 dVLA 通过 masked generative modeling 统一 vision、language、action token，这意味着 RL 设计需要处理离散 token、迭代生成和动作可执行性三者的耦合。由于没有 HTML 方法摘录，不能确认它使用 PPO、policy gradient、trajectory likelihood surrogate、reward shaping 还是 critic-based 方案；也不能确认模型 backbone、任务环境或训练细节。

#### 📊 实验与结果

由于该条只有 abstract fallback，实验信息不足。可以确认的只有研究对象和挑战：dVLAs 已经作为 VLA 架构替代出现，但 RL refinement 尚未被充分探索；核心困难是最终动作 marginal probability 难以求解。摘要没有提供 benchmark、机器人平台、任务类型、baseline、成功率或消融结果，因此不能判断其真实机器人证据强弱。它入选最终精选的原因不是已有证据最完整，而是题目方向精准命中“RL + VLA + diffusion action model”交叉点，且可能补上 dVLA 从 SFT 到 RL 后训练的关键缺口。

#### ⚠️ 风险 / 保留意见

- 只有摘要回退，方法细节和实验支撑都无法核查，当前判断应视为方向性优先。
- dVLA 的离散去噪轨迹 RL 可能引入较高方差或 credit assignment 难题，需要看具体 objective。
- 如果实验只在仿真或离线 benchmark 上验证，真实机器人部署价值仍需谨慎评估。

#### 💭 结论与启发

这篇最值得带着问题读，而不是直接相信主张。后续如果要做 dVLA 或 token-based VLA，RL 后训练会不可避免地遇到最终动作概率不可 tractable 的问题，因此 denoising trajectory 可能是一个自然优化对象。复现上应先抽象出 dVLA 的逐步 mask/refine 状态，把每一步看作可加 reward 或 advantage 的中间决策，再判断作者方案是否比直接对最终动作做黑盒 RL 更稳定。

#### 🔎 读 PDF 先核查

- dVLA-RL 如何定义 denoising trajectory 上的 policy probability 或 surrogate objective？
- RL 信号是作用在每个离散去噪步骤、最终动作，还是两者联合？
- 方法是否需要额外 critic/reward model，还是只依赖环境回报和生成轨迹 likelihood 近似？

#### 📌 上传 PDF 后优先看

- 方法章节中对 final action marginal probability intractability 的处理
- denoising trajectory RL objective 与训练流程
- 实验 benchmark、baseline 和是否包含真实机器人验证

### [6]. Learning to See While Learning to Act: Diffusion Models for Active Perception in Robot Imitation [[VIP]] [[HTML]](https://arxiv.org/html/2606.23625) [[PDF]](https://arxiv.org/pdf/2606.23625) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.23625`
* **Authors**: Kuancheng Wang, Vaibhav Saxena, Shuo Cheng, Yotto Koga, Danfei Xu
* **Author Priority**: Extended VIP
* **一句话结论**: 值得优先看：See2Act 把主动感知并入 diffusion imitation policy，让机器人在学动作的同时学会去哪里看，是 occlusion manipulation 的强相关方向。
* **关键词**: `Active Perception` `Diffusion Policy` `Imitation Learning` `Occlusion` `Danfei Xu`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

See2Act 解决的是 imitation learning 默认 full observability 的问题。许多桌面操作方法假设固定相机能看到关键物体和接触区域，但真实任务里目标常被遮挡，机器人必须先搜索、换视角，再执行操作。直接增加更多视角会让数据需求快速膨胀，也未必告诉策略哪些视角真正有用；把 viewpoint planner 单独拿出来又会增加系统复杂度和误差耦合。See2Act 的动机是把“在哪里看”和“如何动作”放进同一个 diffusion policy 过程中，让视角选择成为动作去噪的一部分。Danfei Xu 参与使这篇在主动感知和机器人学习交叉方向上值得重点跟踪。

#### ⚙️ 核心方法

核心思想是：diffusion trajectory 同时也是 viewpoint trajectory。训练时，每个 noisy action 会配对一个 camera pose 和 observation，并锚定到同一个 target keyframe；早期 diffusion step 对应更宽的上下文视角，后期 step 对应更接近目标的视角。推理时，动作 denoising 会同步更新相机位姿，因此策略在预测动作的过程中主动获取越来越有信息量的观察。论文还把 action 表示在 camera frame 而不是固定 world frame 中，使 camera pose 成为动作坐标系的一部分，从而把移动相机和动作去噪耦合起来。这个设计避免了单独 viewpoint planner 或 reward 的需求，属于把 active perception 内生进 imitation policy 的路线。当前摘录能确认其使用 diffusion-based visuomotor IL、6-DoF camera trajectory refinement 和 keyframe-anchored training；具体网络结构、相机运动约束和 keyframe 提取规则需看正文。

#### 📊 实验与结果

实验覆盖模拟和真实机器人，核心问题是主动 viewpoint refinement 是否能解决 fixed-view、multi-view、passive-view selection 和 zoom-only baseline 处理不了的 partial observability。模拟部分使用 Ravens 作为遮挡和搜索诊断 benchmark，包含 4 个任务；其中 place-red-in-green 包含红块、绿碗和干扰物，并设计了 3 个 front-view occlusion 难度变体。论文还评估了与 strong multi-view 和 3D manipulation policies 的竞争性、学习到的 viewpoint policy 是否产生系统搜索行为、对初始相机位姿的敏感性，以及 digital-twin 到真实机器人的 zero-shot transfer。结论明确给出：使用 depth observations，真实机器人 zero-shot sim-to-real 达到 95% success，且只用 50 demonstrations。

#### ⚠️ 风险 / 保留意见

- 方法依赖可控相机或可移动视角，固定外参生产线场景未必直接适用。
- camera-frame action 表示会把感知误差和控制误差耦合，标定与深度质量可能影响部署。
- 50 demonstrations 和 95% success 很有吸引力，但需要核查任务数量、试验次数和失败模式。

#### 💭 结论与启发

See2Act 的启发是把主动感知从模块级规划问题变成生成策略内部的逐步 refinement 问题。对后续系统设计，可以考虑让 diffusion policy 不只输出末端动作，也输出下一步传感器位姿、crop、viewpoint 或注意区域。复现时最值得先做 occlusion diagnostic：在 Ravens 或类似任务中比较 fixed-view、passive multi-view selection 和 denoising-coupled viewpoint update，确认收益来自主动搜索而非额外视角信息本身。

#### 🔎 读 PDF 先核查

- keyframe-anchored camera poses 是如何从 demonstration 中提取并分配到 diffusion steps 的？
- 推理时相机位姿更新是否受物理可达性、速度或碰撞约束限制？
- 95% real-robot success 的任务范围、rollout 数量和 baseline 差距分别是多少？

#### 📌 上传 PDF 后优先看

- 训练流程：keyframe action、camera pose noising 与 denoising coupling
- Ravens occlusion tasks、multi-view/passive/zoom baseline 对比
- 真实机器人 zero-shot sim-to-real 实验和失败案例

## Watchlist

### [W1]. MV-WAM: Manifold-Aware World Action Model with Value Augmentation [[HTML]](https://arxiv.org/html/2606.21088) [[PDF]](https://arxiv.org/pdf/2606.21088)
* **Paper ID**: `2606.21088`
* **Authors**: Jintao Chen, Peidong Jia, Qingpo Wuwu, Jiaming Liu, Mengfei Du, Chun-Kai Fan, Xiaowei Chi, Hao Chen, Chengyu Bai, Zezhong Qian, Hao Wang, Jiajun Cao, Weishi Mi, Xiaozhu Ju, Jian Tang, Shanghang Zhang
* **Author Priority**: Standard
* **为什么还值得留意**: MV-WAM 进入 watchlist 是因为它直接讨论 WAM 在 OOD 场景下的鲁棒性，并提出 manifold-aware objectives、cross-modality causal masking，以及把 visual prediction、action generation、value estimation 放在同一 MoTs-based diffusion backbone 中。摘录还给出 1.9B 参数、Video Expert 预训练和 RoboTwin 2.0/真实机器人验证线索，方向很强。没有进入最终精选主要是因为今天已有 SafeDojo 与 WAM Survey 覆盖 world model/WAM 主线，而 MV-WAM 的关键收益需要依赖完整实验表格判断。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. UniviewVLA: A Unified Multiview Vision-Language-Action Model with World Modeling [[HTML]](https://arxiv.org/html/2606.21501) [[PDF]](https://arxiv.org/pdf/2606.21501)
* **Paper ID**: `2606.21501`
* **Authors**: Tao Xu, Runhao Zhang, Zhijian Huang, Jiayi Guan, Jiaxin Wang, Yifan Ding, Yong-Lu Li, Long Chen, Guang Chen, Jinghui Lu
* **Author Priority**: Standard
* **为什么还值得留意**: UniviewVLA 值得跟踪，因为它针对遮挡任务，从标准 agent-view 和 wrist-view 生成辅助多视角未来视图，并将每个生成视图从 625 token 压缩到 16 token，以降低闭环推理成本。它与 See2Act 同属“遮挡下如何看”的问题，但更偏生成辅助视角和 multiview world modeling。没有进入最终精选，是因为 See2Act 在主动感知与真实 zero-shot sim-to-real 上的信息更集中，而 UniviewVLA 的数字和任务效果在摘录中缺失较多。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. OpenHLM: An Empirical Recipe for Whole-Body Humanoid Loco-Manipulation [[HTML]](https://arxiv.org/html/2606.22174) [[PDF]](https://arxiv.org/pdf/2606.22174)
* **Paper ID**: `2606.22174`
* **Authors**: Yingdong Hu, Haodong Zhu, Boyuan Zheng, Yihang Hu, Tong Zhang, Zunhao Chen, Junming Zhao, Ruiqian Nai, Yang Gao
* **Author Priority**: Standard
* **为什么还值得留意**: OpenHLM 进入 watchlist 是因为它把 VLA 推向 humanoid whole-body loco-manipulation，而不是把腿当移动底座、手当独立操作器，问题非常前沿。摘录显示它有 HLM-12 benchmark、真实世界每个 policy-task 五次 rollout、以及围绕 teleoperation、VLA 设计和 cheap data 的 one-variable-at-a-time roadmap。没有进入最终精选，是因为今天主题更偏 VLA/WAM/RL/world model，而 OpenHLM 更像 humanoid 系统 recipe，需在 humanoid 专题中重点读。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

### [W4]. Cloak: Zero-Shot Cross-Embodiment Manipulation by Masking the End-Effector from the VLA [[HTML]](https://arxiv.org/html/2606.22836) [[PDF]](https://arxiv.org/pdf/2606.22836)
* **Paper ID**: `2606.22836`
* **Authors**: Michael Piseno, Guy Tevet, C. Karen Liu
* **Author Priority**: Standard
* **为什么还值得留意**: Cloak 值得 watchlist，因为它提出一个很朴素但可能有效的 zero-shot cross-embodiment recipe：从腕部视角中 mask 掉 end-effector，让 VLA 学到更 embodiment-agnostic 的视觉推理，再用 FK/IK 做 tip-pose retargeting。它不需要目标 embodiment 数据、重训练或提前知道目标硬件，这对复用 gripper-centric 数据很有价值。没有进入最终精选，是因为它更偏 cross-embodiment 视觉/运动接口技巧，和今天最终精选中的 RL、world model、active perception 主线相比优先级略低。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)
