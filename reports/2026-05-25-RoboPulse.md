# RoboPulse | 2026-05-25

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 54 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线很清楚：VLA 正在从“直接模仿动作”转向“用世界模型、几何轨迹、价值函数或在线反馈修正动作生成”。最终精选覆盖了三条互补路线：视频生成先验到真实 humanoid HOI、几何一致的视频世界模型、以及面向 VLA 控制的 RL/规划/迭代解码改造。它们入选不是因为单点指标，而是因为都在回答同一个关键问题：如何让视觉-语言条件下的动作不只看起来合理，还能被闭环执行。VIP 作者里最值得优先跟踪的是 2605.22272 的 Jiangmiao Pang；扩展名单虽未直接主导精选，但 Yilun Du 出现在 GEM-4D 作者中，值得继续观察其视频世界模型与机器人规划交叉方向。

## 今日信号

- 视频世界模型的评价重心正在从 photorealism 转向 correspondence、point tracking、depth 和可执行动作抽取。
- VLA 的下一步瓶颈不只是更大数据，而是闭环推理时如何引入价值、奖励、迭代停止和跨周期复用。
- Sim2Real 方向正在形成两类强信号：一类借生成视频/4D 表示绕开真实数据稀缺，另一类在专用场景中用仿真 RL 加强部署闭环。

## Historical Rediscovery

- **Paper**: Lost in Fog: Sensor Perturbations Expose Reasoning Fragility in Driving VLAs [[HTML]](https://arxiv.org/html/2605.21446) [[PDF]](https://arxiv.org/pdf/2605.21446)
  - **Paper ID**: `2605.21446`
  - **来源日期**: 2026-05-21
  - **当时可能被低估的信号**: 当时可能低估了它把 sensor perturbation、explanation consistency 与 trajectory reliability 放在同一诊断里的价值；1,996 个场景、8 类扰动和尾部 L2 deviation 风险信号比一般鲁棒性小实验更具体。
  - **为什么现在值得再看**: 如果今天关注 VLA 的真实部署评测与 Sim2Real 失配，这篇可作为评估协议和 failure taxonomy 的参考，尤其适合对照 World Action Model 或驾驶 VLA 是否真的更稳。
  - **建议动作**: 加入精读
  - **关键词**: `Driving VLA` `robustness` `sensor perturbation` `deployment evaluation` `Sim2Real`
- **Paper**: Hand-in-the-Loop: Improving VLA Policies for Dexterous Manipulation via Seamless Hand-Arm Intervention [[HTML]](https://arxiv.org/html/2605.15157) [[PDF]](https://arxiv.org/pdf/2605.15157)
  - **Paper ID**: `2605.15157`
  - **来源日期**: 2026-05-21
  - **当时可能被低估的信号**: 当时可能低估了 hand-arm intervention 中 teleoperation command 与策略状态不匹配这个工程瓶颈；gesture jumps 和 command discontinuity 是真实系统很容易暴露但论文常回避的问题。
  - **为什么现在值得再看**: 对长时程操作和真实部署而言，VLA 失败后的无缝人类介入、恢复和继续执行会越来越关键；它和 RL+VLA 后训练、interactive imitation、real-robot data collection 都有直接连接。
  - **建议动作**: 加入精读
  - **关键词**: `VLA` `dexterous manipulation` `human intervention` `real robot` `long-horizon manipulation`
- **Paper**: DISC: Decoupling Instruction from State-Conditioned Control via Policy Generation [[HTML]](https://arxiv.org/html/2605.20856) [[PDF]](https://arxiv.org/pdf/2605.20856)
  - **Paper ID**: `2605.20856`
  - **来源日期**: 2026-05-21
  - **当时可能被低估的信号**: 当时可能低估了 hypernetwork 由指令生成任务特定 visuomotor policy 参数这个结构信号；它提供了检查模型是否真正使用语言、而非依赖场景捷径的清晰切口。
  - **为什么现在值得再看**: 今天再看 VLA 与 World Action Model 时，语言、状态和动作策略的解耦是关键问题；这篇可帮助判断模型的 instruction grounding 是否足够干净。
  - **建议动作**: 快速浏览
  - **关键词**: `VLA grounding` `policy generation` `instruction conditioning` `observation leakage` `visuomotor control`
- **Paper**: Key-Gram: Extensible World Knowledge for Embodied Manipulation [[HTML]](https://arxiv.org/html/2605.18556) [[PDF]](https://arxiv.org/pdf/2605.18556)
  - **Paper ID**: `2605.18556`
  - **来源日期**: 2026-05-19
  - **当时可能被低估的信号**: 当时可能低估了 task-specific key-grams 与外部条件记忆的接口意义；即使 hashed lookup 和层内调制需要验证，这种模块化知识注入路线本身值得比较。
  - **为什么现在值得再看**: 如果要研究 VLA 如何扩展到更复杂任务和长时程操作，外部世界知识、任务记忆和动作生成之间的接口会变得重要；它也提供了可与 prompt、memory adapter、WAM 类方法对照的样本。
  - **建议动作**: 继续跟踪
  - **关键词**: `VLA` `world knowledge` `memory` `World Action Model` `embodied manipulation`
- **Paper**: Understanding Asynchronous Inference Methods for Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2605.08168) [[PDF]](https://arxiv.org/pdf/2605.08168)
  - **Paper ID**: `2605.08168`
  - **来源日期**: 2026-05-12
  - **当时可能被低估的信号**: 当时可能低估了不同 delay 下方法排名会跨 benchmark 改变这一诊断信号；这说明实时 VLA 的优劣不能只看静态成功率或单一延迟设置。
  - **为什么现在值得再看**: 对真实机器人、长时程控制和 diffusion/autoregressive VLA 都有现实意义；今天研究 World Action Model 或实时闭环 VLA 时，需要把推理时序和控制闭环一起纳入评估。
  - **建议动作**: 快速浏览
  - **关键词**: `real-time VLA` `asynchronous inference` `action chunking` `latency` `deployment evaluation`

## Editor's Picks

### [1]. Imagine2Real: Towards Zero-shot Humanoid-Object Interaction via Video Generative Priors [[VIP]] [[HTML]](https://arxiv.org/html/2605.22272) [[PDF]](https://arxiv.org/pdf/2605.22272) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.22272`
* **Authors**: Jiahe Chen, ZiRui Wang, Feiyu Jia, Xiao Chen, Xiaojie Niu, Weishuai Zeng, Tianfan Xue, Xiaowei Zhou, Jiangmiao Pang, Jingbo Wang
* **Author Priority**: Core VIP
* **一句话结论**: 优先看：它把视频生成先验、4D 点轨迹和 humanoid 全身交互连到真实执行，是今天最贴近 Sim2Real+HOI 的一篇。
* **关键词**: `Humanoid HOI` `video generative prior` `4D point trajectory` `zero-shot sim2real` `Behavior Foundation Model`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

#### 📖 背景与动机

Humanoid-object interaction 的核心难点不是单纯走路或抓取，而是全身运动、物体运动和接触过程必须一致。HTML 摘录指出，现有 HOI 受限于高质量 3D 交互数据稀缺，VLA 扩展又缺少大规模 humanoid-specific 数据；而基于 AMP 的专用行为虽可用少量高质量数据训练，但任务覆盖面受样本限制。视频生成模型提供了新的数据先验，但若依赖 CAD、显式几何或复杂 morphology retargeting，就会出现 representation misalignment 和 retargeting complexity。Imagine2Real 的动机正是把“看视频学交互”转成更轻的机器人可执行接口。

#### ⚙️ 核心方法

方法主线是用统一 4D point trajectories 表示机器人和物体运动，避免从视频生成结果直接对齐到完整关节、网格或 CAD 几何。摘录明确提到 Keypoints Tracker 只跟踪稀疏 critical points，因此它不是试图还原完整人体动作，而是抽取对交互最关键的轨迹信号。随后系统在 Behavior Foundation Model 的 latent space 中搜索，使跟踪目标落到 humanoid 可自然执行的行为流形上，而不是直接在 joint space 硬追踪。训练上，BFM backbone 使用 AMASS、LAFAN1、100STYLE 等超过 10,000 clips、约 68.5 小时人体动作，并通过 pink IK retarget 到机器人；Keypoints Tracker 使用 LAFAN1、OMOMO 和部分 AMASS loco-manipulation，过滤掉难以由三个关键点表达的动作后得到超过 4,000 clips、约 8.86 小时。当前摘录只能确认这些级联模块和数据来源，不能确认具体网络结构、损失细节或控制器参数。

#### 📊 实验与结果

实验围绕三个问题设计：latent search 是否比直接 joint-space tracking 带来更自然步态和平滑动作；稀疏关键点是否足以完成全身 HOI；以及能否从视频生成一路走到真实 humanoid 物理执行。摘录提到代表性任务包括 carrying 和 pushing objects，并声称展示了高成功率、鲁棒 motion tracking 和 zero-shot physical deployment。可引用的明确数字主要来自训练数据规模，而不是最终成功率表格；因此对结果应保守理解为：HTML 摘录支持其进行了仿真到真实的端到端验证，但不足以核查每个任务的具体成功率、失败模式和统计显著性。

#### ⚠️ 风险 / 保留意见

- 稀疏 critical points 可能不足以表达复杂接触、双手细操作或需要精确姿态约束的 HOI。
- BFM latent search 的效果依赖预训练动作流形，超出人体动作分布或机器人能力边界时可能失败。
- HTML 摘录未给出完整真实机器人实验数字，部署稳健性仍需核查 PDF 细节。

#### 💭 结论与启发

这篇的启发在于，它没有把视频生成模型当作直接控制器，而是把生成先验压缩成机器人可跟踪的 4D 轨迹接口，再用行为模型 latent space 保证动作自然性。后续选题可以沿着“生成视频到稀疏物理约束到闭环控制”的链路展开，尤其适合 humanoid 或移动操作这种完整 3D 标注稀缺的场景。复现时应优先验证关键点选择、latent search 代价函数和真实控制器接口，而不是只复现视频生成。

#### 🔎 读 PDF 先核查

- 三个 critical points 分别如何定义，是否对不同物体和交互类型自适应？
- BFM latent-space tracking 相比 joint-space tracking 的收益来自自然性、稳定性还是接触成功率？
- zero-shot 真实部署中视频生成误差如何被控制器吸收，失败时主要卡在感知、轨迹还是接触？

#### 📌 上传 PDF 后优先看

- 方法章节中的 4D point trajectory 表示与 Keypoints Tracker 细节
- BFM latent search、tracking objective 和控制接口
- 真实 humanoid 部署实验、失败案例和任务成功率表格

### [2]. GEM-4D: Geometry-Enhanced Video World Models for Robot Manipulation [[HTML]](https://arxiv.org/html/2605.22882) [[PDF]](https://arxiv.org/pdf/2605.22882) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.22882`
* **Authors**: Kaichen Zhou, Yuzhen Chen, Fangneng Zhan, Hang Hua, Grace Chen, Xinhai Chang, Ao Qu, Yilun Du, Zhuang Liu, Paul Pu Liang, Mengyu Wang
* **Author Priority**: Standard
* **一句话结论**: 优先看：GEM-4D 把视频世界模型的核心指标从画面真实推进到 4D correspondence consistency，直接服务机器人 action extraction。
* **关键词**: `video world model` `4D correspondence` `geometry distillation` `robot manipulation` `inverse dynamics`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

#### 📖 背景与动机

视频世界模型在机器人里很有吸引力，因为它可以从单帧观察和语言指令预测未来，从而作为规划器或动作提取器。但摘录强调，生成视频“看起来合理”并不等于能用于控制；同一 3D 表面点在时间上的对应关系如果漂移，机器人从未来视频中提取轨迹时就会得到错误动作。传统通用视频生成模型缺少 embodiment-aware dynamics，VLA 又通常需要大规模 embodiment-specific training。GEM-4D 针对的是两者之间的空档：保留视频生成的泛化能力，同时给未来帧加入几何一致性，使生成结果能被机器人操作模块消费。

#### ⚙️ 核心方法

GEM-4D 的核心是把 pretrained geometry foundation model 蒸馏出的 dense 4D correspondence supervision 注入视频生成 backbone 训练中。它并不是在推理时外挂一个昂贵几何模块，而是在训练阶段让模型同时学习 appearance 和 geometric structure；结论摘录还强调其保持 single-stream architecture，推理时没有额外成本。下游闭环部分引入 adaptive inverse dynamics system，把生成视频转换成可执行机器人动作。可以确认的方法接口包括：输入为观察与语言指令，输出为未来 rollout；训练监督覆盖外观、深度和 correspondence consistency；动作执行依赖从生成 rollout 中抽取动作。当前摘录只能确认几何蒸馏和 inverse dynamics 的总体设计，不能确认具体 backbone、蒸馏损失权重、点对应采样策略或 inverse dynamics 的完整算法细节。

#### 📊 实验与结果

实验分两部分：4D scene reconstruction quality，以及生成 rollout 是否提升下游 manipulation action planning/execution。训练数据覆盖 ManiSkill3、RLBench、Bridge 和 RT-1；真实域评估使用 Droid 的 400 个 unseen samples，其中 depth 来自 Depth Anything V3，point tracking 来自 CoTracker3；合成域评估包含 780 个 unseen samples。摘录没有给出具体指标数值，但说明评价维度包括 appearance、depth、correspondence consistency 和机器人建模能力。证据边界是：HTML 足以说明实验覆盖真实与合成数据、并关注几何一致性到动作执行的链路，但不能支持引用具体提升幅度。

#### ⚠️ 风险 / 保留意见

- 几何监督来自预训练 geometry foundation model，蒸馏误差可能被世界模型继承。
- 真实域 depth 和 tracking 由外部模型估计，评估标签本身可能含噪。
- 能否迁移到强接触、透明物体或大遮挡场景，需要看 PDF 的失败案例。

#### 💭 结论与启发

GEM-4D 对后续系统设计的价值在于提醒我们：机器人视频世界模型不能只优化 FVD 或视觉质量，必须显式约束可操作的几何连续性。它和 JOPAT 都把 point/correspondence 当成 action interface 的一部分，但 GEM-4D 更偏生成式未来预测和 rollout-to-action。读 PDF 时应重点判断 dense 4D supervision 是否真能改善控制，而不是只改善几何评估指标。

#### 🔎 读 PDF 先核查

- dense 4D correspondence supervision 是在哪些层或输出上注入，是否影响视频生成多样性？
- adaptive inverse dynamics 如何从 rollout 中处理多解动作和接触不确定性？
- Droid 真实评估中 depth/track 伪标签误差是否会掩盖或放大模型优势？

#### 📌 上传 PDF 后优先看

- geometry foundation model 蒸馏目标和训练损失
- 4D scene reconstruction 的 appearance/depth/correspondence 指标
- rollout-to-action 的 inverse dynamics 与机器人执行实验

### [3]. Agentic-VLA: Efficient Online Adaptation for Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2605.22896) [[PDF]](https://arxiv.org/pdf/2605.22896) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.22896`
* **Authors**: Ruofan Jin, Zaixi Zhang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看但要审慎：Agentic-VLA 把在线适应、自动奖励和语言探索整合进 VLA，主张很重要，证据需重点核查。
* **关键词**: `online adaptation` `VLA` `adaptive reward synthesis` `language-guided exploration` `LIBERO`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

VLA 的强项是把视觉、语言和动作放进统一策略，但静态 imitation learning 容易在新环境中脆弱：一旦状态偏离训练分布，模型可能重复记忆轨迹而非理解任务语义。机器人部署时又常常没有 oracle reward，传统 RL 难以直接使用。Agentic-VLA 关注的是 VLA 从离线示教走向在线自适应的关键问题：能否在没有人工重新标注大量示教的情况下，利用模型自身反馈、语言指导和经验记忆提升新任务表现。这对 Reinforcement Learning + VLA 特别重要，因为它试图把 VLA 的语义先验和 RL 的试错改进连接起来。

#### ⚙️ 核心方法

方法把 manipulation 建模为 MDP，状态包含视觉观察、proprioceptive state 和任务指令，VLA policy 以 action tokenization 方式自回归生成离散动作 token 序列。框架包含三部分：Adaptive Reward Synthesis 根据当前 VLA 能力和任务复杂度动态生成与调整 reward，并将复杂任务分解为更可学习的信号；Language-Guided Exploration 用自然语言建议约束探索，使在线尝试不是纯随机扰动；Experience Memory 则用于跨任务复用经验。实验中基础模型是 OpenVLA-OFT，使用 action chunking 和 parallel decoding；ARS 的 progress estimation 使用 VLAC foundation critic。当前摘录只能确认组件名称、问题设定和部分依赖模型，不能确认 reward synthesis 的具体 prompt、更新频率、RL objective 或 memory retrieval 机制。

#### 📊 实验与结果

主要 benchmark 是 LIBERO，包括 Spatial、Object、Goal、Long 四个 task suites，每个任务 50 expert demonstrations；额外在 dual-arm RoboTwin 2.0 上评估泛化。指标包括 Success Rate，以及由 VLAC critic 估计的 normalized Progress，范围从 0 到 1；LIBERO 默认以 5 个 independent seeds 的均值和标准差报告，每个任务 50 trials。摘录显示它以 OpenVLA-OFT 为 base model，并与在线适应相关组件结合。由于未提供具体成功率提升数字，当前只能判断实验设计覆盖了标准单臂 benchmark 和双臂补充验证，不能断言各组件贡献大小。

#### ⚠️ 风险 / 保留意见

- 自动 reward 依赖 VLAC 等 critic，若 critic 对 OOD 状态误判，在线适应可能朝错误方向优化。
- 语言引导探索的效果可能与提示模板和任务语义清晰度强相关。
- HTML 摘录缺少具体结果表，需警惕 agentic 框架复杂但真实收益有限。

#### 💭 结论与启发

这篇适合用来思考 VLA 在线学习的系统架构，而不是只看作一个 benchmark 刷分方法。它把 reward generation、curriculum、language exploration 和 memory 都放到 VLA 外环，说明未来 VLA 部署可能更像“策略+自监督评估器+任务级探索器”的组合。复现上应先做最小化版本：固定 OpenVLA-OFT 和 VLAC，只验证 ARS 或 LGE 单组件是否真的改善 LIBERO 长任务。

#### 🔎 读 PDF 先核查

- ARS 生成的 reward 是基于语言规则、critic score 还是二者组合，如何防止 reward hacking？
- Experience Memory 的检索粒度是 task、state-action trajectory 还是语言子目标？
- 在线适应需要多少环境交互，和重新收集 demonstrations 相比是否真正高效？

#### 📌 上传 PDF 后优先看

- Adaptive Reward Synthesis 的算法细节与 reward 示例
- LIBERO 四套任务的主结果和组件消融
- RoboTwin 2.0 双臂泛化实验与交互预算

### [4]. $π_0$-EqM: Equilibrium Matching for Closed-Loop Vision-Language-Action Control [[HTML]](https://arxiv.org/html/2605.23128) [[PDF]](https://arxiv.org/pdf/2605.23128) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.23128`
* **Authors**: Huanming Liu, Congsheng Xu, Jianmin Ji, Yao Mu
* **Author Priority**: Standard
* **一句话结论**: 优先看：π0-EqM 把 VLA action decoder 从固定步数 flow matching 改成可停止、可 warm-start 的 equilibrium solving，问题切得很准。
* **关键词**: `Equilibrium Matching` `VLA action decoder` `closed-loop control` `RoboTwin` `iterative inference`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

许多 VLA 系统把 action decoder 当作固定成本黑箱：每个控制周期都用固定采样或积分步数生成 action chunk，然后只执行短 horizon 的第一步。这在闭环控制中并不理想，因为不同状态需要的推理深度不同，相邻控制周期又高度相关，理论上应复用上一周期的迭代信息。扩散或 flow decoder 的中间状态通常绑定时间或噪声语义，早停和跨周期 warm start 都不自然。π0-EqM 的动机是把 inference depth 变成 deployed policy 的一部分，用 equilibrium matching 为 VLA 控制提供更灵活的迭代动作生成机制。

#### ⚙️ 核心方法

论文在不改变上游 VLA stack 的情况下，将 π0 中的 flow-matching expert 替换为 Equilibrium Matching decoder。EqM 学习的是 time-invariant conditional vector field，其根对应目标 equilibrium action chunks；训练时从 demonstration chunk、structural noise 和 interpolation factor 构造 interpolant，并让向量场匹配目标方向，同时调度标量在接近数据流形时衰减到零，使数据 manifold 成为稳定 equilibrium。推理时不再按固定时间语义采样，而是求解根，摘录提到使用 Nesterov-accelerated solver。由于 receding-horizon setup 只执行 immediate action，系统可以把解码视为每个控制步中的 iterative inference，并进一步讨论 residual thresholding、早停和 warm start。当前摘录能确认数学框架和部署意图，但公式细节在摘录中不完整。

#### 📊 实验与结果

RoboTwin 上的结果是最明确的：在 matched 300-step budget 下，π0-EqM 在 19 个任务中提升 12 个、下降 5 个、持平 2 个，平均成功率从 40.4% 提到 50.2%；较大收益出现在 pick_dual_bottles、place_cans_plasticbox 和 put_bottles_dustbin。LIBERO 上，Spatial 从 96.8% 到 97.2%，LIBERO-10 从 85.2% 到 87.0%，四套平均从 94.15% 到 94.35%，Object 和 Goal 接近 baseline。阈值扫描显示不同任务偏好的 residual threshold 不同，作者也承认只覆盖了两个 RoboTwin 任务，因此非单调现象仍是示例性证据。

#### ⚠️ 风险 / 保留意见

- RoboTwin 有明显提升，但 LIBERO 平均提升很小，收益可能依赖任务难度和剩余 headroom。
- threshold scans 只覆盖少量任务，自动选择停止阈值仍未充分解决。
- 替换 decoder 是否保持大规模 VLA 预训练兼容性，需要看实现和训练成本。

#### 💭 结论与启发

这篇的价值在于把 VLA 控制的推理过程本身作为研究对象，而不只是扩大模型或数据。对系统设计来说，固定采样步数可能是浪费，也可能在复杂状态下不够；EqM 提供了以 residual 作为计算分配信号的思路。后续复现可以先在现有 flow action decoder 上实现可比的 early stopping 和 warm start baseline，再判断 EqM 的收益究竟来自 equilibrium formulation 还是更好的计算调度。

#### 🔎 读 PDF 先核查

- EqM decoder 与原 flow-matching expert 的训练数据、参数量和优化预算是否完全可比？
- residual threshold 如何在部署时自动设定，是否可由任务状态或不确定性预测？
- 跨控制周期 warm start 在实验中贡献多大，是否单独消融？

#### 📌 上传 PDF 后优先看

- EqM training objective 与 inference solver 细节
- RoboTwin 19-task 表格和失败任务分析
- threshold scan、early stopping、warm-start 相关消融

### [5]. Point Tracking Improves World Action Models [[HTML]](https://arxiv.org/html/2605.23856) [[PDF]](https://arxiv.org/pdf/2605.23856) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.23856`
* **Authors**: Jiarui Guan, Wenshuai Zhao, Yue Pei, Ziliang Chen, Arno Solin, Juho Kannala
* **Author Priority**: Standard
* **一句话结论**: 优先看：JOPAT 明确提出 point tracking 是 world-action model 的状态接口，和今天的几何世界模型趋势高度一致。
* **关键词**: `World Action Model` `point tracking` `visibility modeling` `diffusion transformer` `action-free video pretraining`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

#### 📖 背景与动机

机器人策略学习需要理解环境动态，但只预测像素会把真正的物体运动和光照、纹理等干扰因素混在一起。VLA 有语义优势，却常缺少 dynamics understanding；World Action Models 尝试把视频先验转成控制能力，但如果未来状态仍主要以像素表示，长时程遮挡、局部出画和可控对应关系都难以处理。JOPAT 的背景判断是：motion correspondence 应该显式进入世界-动作模型，而不是隐含在视觉 latent 里。这对于部分可观测、遮挡和长 horizon manipulation 很关键，因为机器人需要知道“哪个点移动到哪里”，而不只是未来图像长什么样。

#### ⚙️ 核心方法

JOPAT 是 JOint Pixel-And-Track World-Action Model，在单个 denoising diffusion transformer 中联合预测 latent visual observations、2D point tracks with visibility 和 actions。它的关键接口是 pixel-track future state：视觉 latent 提供语义和外观信息，point tracks 提供运动对应，visibility 则编码缺失证据、遮挡或出画状态。实验设计中作者称其为 state-interface hypothesis，即 track-augmented future state 应比 pixel-centric world-action modeling 更适合 manipulation policy learning。另一个重要点是 action-free video pretraining：如果预训练监督的也是后续动作生成要使用的 pixel-track future state，那么无动作视频可以转移 motion priors。当前摘录能确认统一扩散 transformer、三种预测模态和预训练思路，但不能确认轨迹点采样密度、网络 tokenization 和训练损失细节。

#### 📊 实验与结果

实验围绕四个问题：主性能是否优于 prior policy-learning 和 world-action baselines；visual latents、point tracks、visibility 是否都必要；在长 horizon distribution shift、occlusion、distractors 下是否鲁棒；action-free video pretraining 是否帮助有限 demonstrations 下的控制。结论摘录称在 LIBERO 和 real-world LeRobot tasks 上超过 pixel-based baselines，并提高数据效率、能从 action-free video 转移动作先验。但 HTML 摘录未给出具体成功率和提升幅度，因此可确认的是评估范围和主张，不能引用数值或断言某个 benchmark 上的排名。

#### ⚠️ 风险 / 保留意见

- grid-based sparse point tracks 可能漏掉精细形变、接触边界或小物体关键运动。
- point tracking 质量会影响 action model，上游 tracker 在遮挡和反光物体上的误差可能传导到控制。
- 真实 LeRobot 任务细节和数据规模需核查，否则难判断部署外推能力。

#### 💭 结论与启发

JOPAT 和 GEM-4D 共同说明，世界模型用于机器人时需要一个比像素更行动友好的状态表示。JOPAT 的启发尤其适合做复现：可以从现有 diffusion policy 或 WAM 中加入 point tracks/visibility 辅助头，测试是否提升遮挡与分布转移鲁棒性。后续选题可聚焦“轨迹表示的粒度”：稀疏点、dense correspondence、3D Gaussian 或 4D point trajectory 哪一种最适合作为 action interface。

#### 🔎 读 PDF 先核查

- point tracks 是由外部 tracker 生成监督，还是模型端到端学习并在控制时自预测？
- visibility head 在遮挡场景中如何参与动作生成，是条件输入还是联合去噪目标？
- action-free video pretraining 的收益在低示教数量下是否显著大于常规视频 latent pretraining？

#### 📌 上传 PDF 后优先看

- JOPAT 架构中的 pixel-track-action token 设计
- LIBERO 与 LeRobot 主结果、数据效率曲线
- tracks、visibility、visual latent 和 action-free pretraining 消融

### [6]. V-VLAPS: Value-Guided Planning for Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2601.00969) [[PDF]](https://arxiv.org/pdf/2601.00969) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2601.00969`
* **Authors**: Ke Ren, Ali Salamatian, Kieran Pattison, Cyrus Neary
* **Author Priority**: Standard
* **一句话结论**: 优先看：V-VLAPS 用 learned value 修正 VLA-guided MCTS 的 policy bias，是 VLA+planning 路线中很实用的一步。
* **关键词**: `VLA planning` `MCTS` `value head` `Octo` `LIBERO`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

VLA 作为行为克隆策略可以提供强 action prior，但在 OOD 状态和长 horizon 任务中容易出错。VLA-guided planning 用 MCTS 在模拟 rollout 中探索可能结果，能缓解纯反应式策略的问题；但如果节点选择仍主要依赖 policy prior 和 visit-count exploration，当预训练策略偏向错误动作时，搜索也会被带偏。V-VLAPS 的动机是利用 VLA representation 中潜在的成功/失败信息，训练一个 value signal 来指导 tree search。它关注的是部署可靠性问题：不更新大模型参数，只在规划阶段用价值估计纠正短视或错误的动作偏好。

#### ⚙️ 核心方法

论文扩展 VLAPS：先用固定预训练 Octo VLA policy 在 LIBERO 任务上无规划 rollout，收集状态并计算 Monte Carlo value targets；再用 Octo last-layer representation/readout 训练一个三层 MLP value head；最后把 learned value 集成进 VLAPS 的 MCTS node selection score，使搜索更偏向高价值分支。数据收集上，每个 suite 的 value-head training rollouts 覆盖所有任务，但每个任务只使用 10 个初始状态中的 4 个，具体为 indices 0、3、6、9；评估使用全部 10 个初始状态，因此包含部分 initial-state generalization。测试时 value head 冻结，所有适应来自 MCTS planning 而非参数更新。当前摘录能确认 value head、训练数据构造和搜索集成思路，但 scoring rule 公式在摘录中不完整。

#### 📊 实验与结果

实验比较三种条件：plain Octo VLA、无 learned value 的 VLAPS，以及加入 value head 的 V-VLAPS。评估覆盖五个 LIBERO suites：object、spatial、goal、libero_10 和 libero_90，分别测试物体识别、空间关系、目标状态、长 horizon 和更大多样性任务。value head 每个 suite 离线训练一次，评估阶段冻结；四个 10-task suites 使用任务和初始状态完整网格，libero_90 则采样任务并使用对应初始状态。结论摘录给出重要边界：V-VLAPS 的收益出现在 MCTS 有时间离开 near-root states、且任务仍有 value ranking headroom 的 regime；在 root-level timeout 的困难任务中价值项分离度有限。

#### ⚠️ 风险 / 保留意见

- value head 来自 Octo rollout，若 rollout 覆盖不到关键失败模式，MCTS guidance 会受限。
- 收益依赖搜索预算；低预算或 near-root timeout 场景下价值项可能几乎不起作用。
- 只在 LIBERO 摘录范围内确认，真实机器人或更复杂仿真中的价值泛化未知。

#### 💭 结论与启发

V-VLAPS 给出的启发很直接：VLA 不一定要在线微调才可变强，利用其 latent representation 训练轻量 value head，再接入规划器，可能是更可控的可靠性增强路径。对复现来说，它比完整 RL-VLA 更容易落地，因为参数更新集中在三层 MLP，部署时只改 MCTS scoring。后续可重点比较 value-guided search、critic-guided retry 和 model-predictive rollout 三类外环控制方式。

#### 🔎 读 PDF 先核查

- value target 的 Monte Carlo 计算如何定义成功、部分成功和失败回报？
- learned value 在 MCTS scoring 中与 policy prior、visit count 的权重如何调节？
- 在 libero_90 的任务采样下，value head 是否真正跨任务泛化，还是 suite-specific memorization？

#### 📌 上传 PDF 后优先看

- value-head 数据收集和 Monte Carlo target 定义
- MCTS node selection scoring rule
- 不同搜索预算、LIBERO suite 和 root-timeout 失败分析

## Watchlist

### [W1]. GAF: Gaussian Action Field as a 4D Representation for Dynamic World Modeling in Robotic Manipulation [[HTML]](https://arxiv.org/html/2506.14135) [[PDF]](https://arxiv.org/pdf/2506.14135)
* **Paper ID**: `2506.14135`
* **Authors**: Ying Chai, Litao Deng, Ruizhi Shao, Jiajun Zhang, Kangchen Lv, Liangjun Xing, Xiang Li, Hongwen Zhang, Yebin Liu
* **Author Priority**: Standard
* **为什么还值得留意**: GAF 进入 watchlist 是因为它提出 V-4D-A，把 3D Gaussian Splatting 扩展为 motion-aware 4D 表示，并从未来几何中直接推断动作，和今天的 4D/world-action model 主线相符。它没有进入最终精选，主要因为与 GEM-4D、JOPAT、Imagine2Real 相比，摘录呈现的创新更偏具体表示和系统实现，和 VLA/RL 闭环结合较弱。仍值得后续核查 RLBench 9 任务、20 demonstrations、100 unseen poses 以及真实部署细节。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. Robotic Strawberry Harvesting with Robust Vision and Deep Reinforcement Learning based Sim-to-Real Control [[HTML]](https://arxiv.org/html/2605.23863) [[PDF]](https://arxiv.org/pdf/2605.23863)
* **Paper ID**: `2605.23863`
* **Authors**: Al Bashir, Shao-Yang Chang, Partho Ghose, Prem Raj, Chen-Kang Huang, Azlan Zahid
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇适合 watchlist，因为它是明确的 sim-to-real agricultural robotics 系统：草莓实例分割、Isaac Lab 中 PPO reaching、ROS 到 UR10e 真实执行，工程闭环完整。未进最终精选的原因是方法重心更偏专用感知和 DRL 控制系统，不属于通用 VLA/world model 主线。后续若关注农业机器人部署，可重点看 HRAttnEdge-YOLO26-seg 和 PPO sim2real 的失败率、闭环延迟与鲁棒性。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. USIM and U0: A Vision-Language-Action Dataset and Model for General Underwater Robots [[HTML]](https://arxiv.org/html/2510.07869) [[PDF]](https://arxiv.org/pdf/2510.07869)
* **Paper ID**: `2510.07869`
* **Authors**: Junwen Gu, Zhiheng Wu, Pengxuan Si, Shuang Qiu, Zhentao Zhang, Yukai Feng, Luoyang Sun, Laien Luo, Lianyi Yu, Jian Wang, Zhengxing Wu
* **Author Priority**: Standard
* **为什么还值得留意**: USIM/U0 入 watchlist 是因为它把 VLA 推向 underwater robots，并给出 905K frames、2275 trajectories、约 25 小时 BlueROV2 interaction 的仿真数据规模。未进最终精选，是因为当前摘录中 method 部分信息重复摘要，核心模型结构和动作接口证据不足，且评估主要仍需 PDF 表格支撑。它适合作为 embodiment-specific VLA dataset 的后续跟踪对象。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)

### [W4]. LACY: A Vision-Language Model-based Language-Action Cycle for Self-Improving Robotic Manipulation [[HTML]](https://arxiv.org/html/2511.02239) [[PDF]](https://arxiv.org/pdf/2511.02239)
* **Paper ID**: `2511.02239`
* **Authors**: Youngjin Hong, Houjian Yu, Mingen Li, Changhyun Choi
* **Author Priority**: Standard
* **为什么还值得留意**: LACY 值得 watchlist，因为它提出 L2A、A2L、L2C 的 language-action cycle，用行动解释和语义验证支持自生成训练数据，方向上贴近自改进 VLA。未进最终精选，是因为摘录显示任务集中在 tabletop pick-and-place，规模为仿真最多 4,000 demos、真实 212 demos/50 unseen scenarios，通用机器人控制和世界模型联系相对弱。后续可关注 bidirectional grounding 是否真的提升 OOD 泛化，而不只是增强可解释性。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
