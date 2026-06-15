# RoboPulse | 2026-06-15

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 79 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线非常清晰：VLA 正在从“更大的端到端策略”转向“可被引导、可被后训练、可建模未来、可闭环纠偏”的系统化机器人学习栈。最终精选保留了三类互补路线：FRS/OGPO/HyVLA 代表如何在已有 generative/VLA policy 上做 test-time steering、RL fine-tuning 与完整部署栈；μ0/WAM4D/FAWAM 则代表 world model / world action model 正在从像素预测转向 3D、4D、力觉与接触动力学接口。VIP 作者上，Sergey Levine 与 Chelsea Finn 共同出现在 FRS，Sergey Levine 也参与 OGPO，这两篇应优先跟踪，因为它们都直指“如何低成本改进已有机器人通用策略”。整体看，今天最值得注意的不是单点 benchmark，而是机器人基础模型正在补齐推理时控制、RL 后训练、几何预测和真实硬件闭环执行之间的接口。

## 今日信号

- VLA 的下一步竞争点正在从单次指令跟随，转向如何把冻结或半冻结的 generative policy 当作可搜索、可引导、可强化优化的行为先验。
- World model / world action model 正在明显远离纯 2D 视频生成，转向 3D traces、4D geometric tokens、force/tactile 等更贴近控制约束的中间表示。
- 真实机器人部署论文开始强调完整 stack：数据采集、表示、SFT、RL post-training、异步执行和反馈纠偏必须一起设计，而不是只报告一个更大的 VLA backbone。

## Historical Rediscovery

- **Paper**: NavWAM: A Navigation World Action Model for Goal-Conditioned Visual Navigation [[HTML]](https://arxiv.org/html/2606.13494) [[PDF]](https://arxiv.org/pdf/2606.13494)
  - **Paper ID**: `2606.13494`
  - **来源日期**: 2026-06-12
  - **当时可能被低估的信号**: 当时可能低估了它把 WAM 从 manipulation 扩展到 goal-conditioned visual navigation 的信号，尤其是同时比较 NWM、Cosmos Predict2、OmniVLA，并包含 simulation pretraining 加 real-robot adaptation。
  - **为什么现在值得再看**: 今天再看有价值，因为它直接对应 World Action Model、action chunk、视觉目标条件控制和 Sim2Real adaptation；即使任务域是导航，也可能给 VLA/WAM 的统一 latent-action 表示提供参考。
  - **建议动作**: 加入精读
  - **关键词**: `World Action Model` `goal-conditioned navigation` `action chunk` `Sim2Real` `visual navigation`
- **Paper**: EA-WM: Event-Aware World Models with Task-Specification Grounding for Long-Horizon Manipulation [[HTML]](https://arxiv.org/html/2606.13053) [[PDF]](https://arxiv.org/pdf/2606.13053)
  - **Paper ID**: `2606.13053`
  - **来源日期**: 2026-06-12
  - **当时可能被低估的信号**: 当时可能低估了 event prediction 作为长时程操作中间表示的价值；候选信息里已有 PointMaze、Deformable、Wall-Single、LIBERO-goal 等多 benchmark 线索，说明它不是纯概念提案。
  - **为什么现在值得再看**: 现在值得再看，因为 VLA 和 world model 的关键瓶颈之一是长时程任务中的事件级进展判断、失败验证和规划闭环；EA-WM 正好落在 World Model + 长时程操作的交叉点。
  - **建议动作**: 加入精读
  - **关键词**: `World Model` `event prediction` `long-horizon manipulation` `verifier-guided planning` `LIBERO`
- **Paper**: Demystifying Action Space Design for Robotic Manipulation Policies [[HTML]](https://arxiv.org/html/2602.23408) [[PDF]](https://arxiv.org/pdf/2602.23408)
  - **Paper ID**: `2602.23408`
  - **来源日期**: 2026-04-24
  - **当时可能被低估的信号**: 当时可能低估了 action space 作为 VLA/WAM 公共接口的基础性；候选 note 明确提到它覆盖多种硬件平台、真实机器人与仿真，并比较不同生成式策略范式。
  - **为什么现在值得再看**: 今天再看很重要，因为 VLA、RL+VLA 和 World Action Model 最终都要落到动作表示；如果 action space 设计不稳，world/action modeling 的收益很可能无法转化为真实机器人表现。
  - **建议动作**: 加入精读
  - **关键词**: `action space` `robot manipulation` `VLA deployment` `Sim2Real` `policy design`
- **Paper**: Learning to Assist: Collaborative VLAs for Implicit Human-Robot Collaboration [[HTML]](https://arxiv.org/html/2606.12475) [[PDF]](https://arxiv.org/pdf/2606.12475)
  - **Paper ID**: `2606.12475`
  - **来源日期**: 2026-06-12
  - **当时可能被低估的信号**: 当时可能低估了 demonstration action leakage 和 premature assistance 这类部署期问题的研究价值；候选信息还显示它包含 16 人用户研究和 NASA TLX、SUS、Human-Robot Fluency 等指标。
  - **为什么现在值得再看**: 现在值得再看，因为 VLA 走向真实部署后，inference-time mitigation、人机协作失败模式和 action chunk 的副作用会变得更关键；它能补足模型能力论文之外的部署评测视角。
  - **建议动作**: 快速浏览
  - **关键词**: `VLA` `human-robot collaboration` `action chunking` `deployment evaluation` `inference-time mitigation`
- **Paper**: FTP-1: A Generalist Foundation Tactile Policy Across Tactile Sensors for Contact-Rich Manipulation [[HTML]](https://arxiv.org/html/2606.13102) [[PDF]](https://arxiv.org/pdf/2606.13102)
  - **Paper ID**: `2606.13102`
  - **来源日期**: 2026-06-12
  - **当时可能被低估的信号**: 当时可能低估了跨 26 个来源、21 种传感器，以及 3 个独立机构在不同 embodiment 和任务套件上评估的信号；这些历史信息说明它的价值不只是单一触觉模型。
  - **为什么现在值得再看**: 今天再看有意义，因为真实部署中的 VLA 和 world/action model 很难只靠视觉处理接触丰富任务；触觉基础策略可能成为 Sim2Real 和精细 manipulation 的关键支撑模块。
  - **建议动作**: 继续跟踪
  - **关键词**: `tactile policy` `contact-rich manipulation` `VLA limitation` `real-robot evaluation` `Sim2Real`

## Editor's Picks

### [1]. Improving Robotic Generalist Policies via Flow Reversal Steering [[VIP]] [[HTML]](https://arxiv.org/html/2606.13675) [[PDF]](https://arxiv.org/pdf/2606.13675) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.13675`
* **Authors**: Andy Tang, William Chen, Andrew Wagenmaker, Chelsea Finn, Sergey Levine
* **Author Priority**: Core VIP
* **一句话结论**: 优先看：FRS 给出了一个很有价值的方向，即不重新训练大 VLA，也能通过反向 flow 把粗粒度语义指导转成更合适的动作模式。
* **关键词**: `Flow Reversal Steering` `VLA steering` `flow matching policy` `DSBC` `robot RL bootstrap`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

#### 📖 背景与动机

这篇论文切中 generalist robot policy 的核心矛盾：大规模多任务数据训练出的 VLA/flow policy 已经包含很多“合理行为”先验，但面对训练分布外的新任务、长时程任务或需要试错适应的场景时，直接用语言命令调用这些先验往往不够稳定。传统做法是补 demonstration、重新训练或 fine-tune，但这在真实机器人上成本很高，也没有充分利用模型内部已经学到的多模态行为分布。FRS 的动机是把 flow matching generalist 看成一个可反向查询的行为空间：如果人或 VLM 能给出一个“差但合理”的动作提示，系统能否把它映射到 generalist policy 附近更可执行、更像训练分布的动作模式？这对 VLA、Sim2Real 和机器人 RL 都重要，因为它把 test-time semantic guidance、policy prior 和后续自改进连接起来。

#### ⚙️ 核心方法

FRS 的关键机制是“flow reversal steering”。论文关注 flow matching generalist policies：正常推理时，policy 从 latent/noise 经 flow 生成动作；FRS 则把一个 suboptimal but reasonable action 反向通过 flow policy，找到对应的 latent noise，再把这个 latent 映射到附近的 generalist action modes。这样，外部 reasoner 不需要输出精确控制，只需要提供语义上合理的方向，FRS 再借助已有 policy 的行为先验生成更像机器人可执行分布的动作。摘录还显示作者把 FRS 用在两类学习流程中：一是零训练条件下由 VLM 或人类指导 generalist，二是用 FRS 改善后的轨迹快速学习新任务，即 Diffusion Steering via Behavior Cloning（DSBC）；此外还用于 bootstrapping DSRL，使 RL 能从更好的经验起点出发。当前摘录只能确认其高层流程与实验问题，不能确认具体 flow 反演算法细节、latent 邻域搜索形式、VLM 打分接口或 DSBC 损失函数，因此这些需要后续读 PDF 核查。

#### 📊 实验与结果

实验覆盖模拟和真实操控。模拟部分使用 LIBERO，包含 Spatial、Object、Goal splits，以及 LIBERO-90 中 base policy 达到 40% success 的 62 个任务；随后在一个 15-task subset 上用 FRS 成功轨迹训练 DSBC，并在该子集及一个 base policy 几乎失败的 10-task subset 上运行 DSRL + FRS。作者强调使用没有在相应 LIBERO splits 上训练过的 base VLA，以保留改进空间。真实机器人部分摘录只说明存在多种 real-world manipulation settings，未给出具体成功率。结论称 FRS 能让 humans/VLMs 引导 state-of-the-art VLAs，并支持 DSBC 和 DSRL bootstrap，但摘录没有给出核心表格数值，因此只能保守认为证据覆盖面较广，定量强度需看正文表格。

#### ⚠️ 风险 / 保留意见

- FRS 依赖外部“合理但不精确”的动作或语义指导，若 guidance 本身偏离任务关键接触阶段，反演可能仍会落入无效模式。
- 当前摘录没有展示反向 flow 的数值稳定性、latent 搜索成本和失败案例，复现风险集中在实现细节。
- 真实机器人结果只在摘录中被概括，部署泛化和长期试错安全性仍需看完整实验。

#### 💭 结论与启发

这篇最值得借鉴的是把 VLA policy 从“黑盒动作生成器”改造成“可被反向查询的行为库”。后续选题可以沿着两条线推进：一是研究如何让 VLM、人类偏好或 affordance detector 提供更可靠的 steering signal；二是把 FRS 类方法作为 RL 前置数据放大器，先用 policy prior 生成可接受轨迹，再用少量真实交互做精修。阅读 PDF 时应重点确认它是否真的减少了重新收集 demonstration 的需求，以及在 base policy 完全不具备某技能时是否仍有效。

#### 🔎 读 PDF 先核查

- FRS 反向通过 flow policy 时，如何定义“nearby generalist action modes”，是 latent perturbation、优化搜索还是采样重排？
- VLM 指导在实验中具体输出什么信号，是否需要任务特定 prompt 或人工筛选？
- DSBC 与 DSRL + FRS 的收益分别来自更好的初始轨迹、更高数据多样性，还是来自过滤掉明显坏动作？

#### 📌 上传 PDF 后优先看

- 方法章节中的 flow reversal 与 latent steering 细节
- LIBERO 零训练、DSBC、DSRL 三组实验表格与消融
- 真实机器人任务设置、失败案例和外部 guidance 接口

### [2]. OGPO: Sample Efficient Full-Finetuning of Generative Control Policies [[VIP]] [[HTML]](https://arxiv.org/html/2605.03065) [[PDF]](https://arxiv.org/pdf/2605.03065) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.03065`
* **Authors**: Sarvesh Patil, Mitsuhiko Nakamoto, Manan Agarwal, Shashwat Saxena, Jesse Zhang, Giri Anantharaman, Cleah Winston, Chaoyi Pan, Douglas Chen, Nai-Chieh Huang, Zeynep Temel, Oliver Kroemer, Sergey Levine, Abhishek Gupta, Hongkai Dai, Paarth Shah, Max Simchowitz
* **Author Priority**: Core VIP
* **一句话结论**: 优先看：OGPO 是今天最直接面向“generative control policy 如何用 RL 高效全量微调”的论文，且有 Sergey Levine 参与。
* **关键词**: `OGPO` `generative control policy` `off-policy RL` `PPO fine-tuning` `multimodal trajectories`
* **证据来源**: arXiv HTML (Introduction, Method, Conclusion)

#### 📖 背景与动机

Generative control policies，包括 diffusion 和 flow action policies，已经成为机器人模仿学习里的强参数化方式，能表达多峰动作分布，也适合从 demonstration 学复杂操作。但 BC policy 在部署时通常对细微环境变化很脆弱，零样本成功率难以稳定覆盖真实场景。用 RL fine-tune 是自然选择，可是 generative policy 的采样链长、动作分布复杂，常规 on-policy 方法样本效率低，off-policy critic 又很难稳定地给整个生成过程传梯度。OGPO 试图解决这个矛盾：既保留 off-policy 数据复用和 critic 价值传播，又能针对 diffusion/flow 类 GCP 做 full-finetuning，而不是只调小模块或额外 residual。对 VLA+RL 来说，它提供了一个重要范式：把大生成式控制头作为 RL 可优化对象，而不是只把它当 frozen prior。

#### ⚙️ 核心方法

OGPO 的核心是 Off-policy Generative Policy Optimization。根据摘录，它维护 off-policy critic networks 以最大化数据复用，并通过 modified PPO objective 将 policy gradient 传播过完整的 generative process，同时把 critic 作为 terminal reward 使用。论文给出的直觉是 OGPO 会对 trajectory-level multimodality 做选择性“stretching”：在类似绕障左/右两种模式的任务中，它不是简单压缩分布到单一平均动作，而是在决策点附近保留与关键方向正交的方差，使左右两条可行模式仍被保留；在动作极端区域则 sharpen 分布，让轨迹更集中于高价值模式。这个解释对 generative policy 很关键，因为 RL fine-tuning 常见风险是 mode collapse 或把多峰 demonstration 学成单峰。当前摘录只能确认 OGPO 使用 critic、modified PPO、full generative process gradient 与多峰保持直觉，不能确认重要实现细节，例如 critic 输入是完整 denoising trajectory 还是 action chunk、parallel denoising rollouts 如何估计 Q、以及 PPO ratio 如何定义在生成链上。

#### 📊 实验与结果

摘录称 OGPO 在多任务操作、高精度插入和 dexterous control 上达到 state-of-the-art performance，并强调 sample efficiency，但没有给出具体 benchmark 名称、成功率、样本步数或对比数值。结论中唯一明确的实验相关边界是：为了估计 Q-values，OGPO 需要 parallel denoising rollouts，这对大型 VLA 可能因推理成本过高而变得昂贵。方法摘录还用双模式绕障的 mental model 解释其保持 trajectory-level multimodality 的机制，但这属于概念说明，不等同于定量结果。因此，这篇的证据强度必须等读者上传 PDF 后核查主表、样本效率曲线和消融，尤其要确认“full-finetuning”相对 LoRA、residual policy 或 actor-only fine-tuning 的真实优势。

#### ⚠️ 风险 / 保留意见

- parallel denoising rollouts 对大 VLA 推理成本可能过高，真实机器人在线 RL 部署会受限。
- 摘录没有给出具体任务数值，state-of-the-art 主张需要完整表格验证。
- full-finetuning generative policy 可能带来灾难性遗忘或安全探索风险，需要看是否有保守更新约束。

#### 💭 结论与启发

OGPO 值得作为 VLA 后训练路线的基准阅读。它提醒我，机器人 generative policy 的 RL fine-tuning 不能只追求 reward 上升，还必须保护轨迹分布的多模态结构，否则高精度任务可能变成“平均动作失败”。后续复现时应先在小型 diffusion/flow policy 上验证 modified PPO 和 critic 估计，再考虑迁移到更大 VLA；系统设计上则要提前估算 denoising rollout 数量、critic 训练稳定性和真实机器人采样预算。

#### 🔎 读 PDF 先核查

- OGPO 的 modified PPO objective 如何在 diffusion/flow 生成链上计算概率比或等价更新量？
- off-policy critic 的 terminal reward 设计是否会牺牲中间接触阶段的 credit assignment？
- 论文如何证明 OGPO 保留 trajectory-level multimodality，而不是仅在概念图中解释？

#### 📌 上传 PDF 后优先看

- 算法章节中的 modified PPO objective 和 critic 学习细节
- 多任务、高精度插入、dexterous control 的主结果与样本效率曲线
- parallel denoising rollouts、Q-value 估计数量和计算成本消融

### [3]. $μ_0$: A Scalable 3D Interaction-Trace World Model [[HTML]](https://arxiv.org/html/2606.13769) [[PDF]](https://arxiv.org/pdf/2606.13769) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.13769`
* **Authors**: Seungjae Lee, Yoonkyo Jung, Jusuk Lee, Jonghun Shin, Amir Hossein Shahidzadeh, Yao-Chih Lee, H. Jin Kim, Jia-Bin Huang, Furong Huang
* **Author Priority**: Standard
* **一句话结论**: 优先看：μ0 把 world model 的预测目标从像素视频改成 3D interaction traces，是非常值得跟踪的可扩展机器人世界模型接口。
* **关键词**: `3D interaction traces` `world model` `TraceExtract` `cross-embodiment` `video pretraining`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

机器人 world model 面临一个数据悖论：互联网和人类视频很丰富，但带机器人 action label 的数据昂贵、硬件绑定且跨 embodiment 不兼容。纯像素视频模型虽然可扩展，却把大量容量花在外观、背景和纹理重建上，不一定学到操控真正需要的度量几何、接触结构和遮挡关系；直接 action model 又需要特定机器人动作标签，难以从异构视频中学习。μ0 的动机是寻找一种中间表示：既比像素更贴近物理交互，又不绑定具体机器人控制接口。它选择预测 salient interaction points 的平滑 3D trajectories，包括物体、工具、手和接触区域等关键点。这个方向对 VLA 与 Sim2Real 很重要，因为它可能把大规模视频预训练转化为跨 embodiment 可用的“未来交互几何先验”。

#### ⚙️ 核心方法

μ0 是一个 query-conditioned 3D trace-space world model。它不预测 dense pixels，也不直接预测机器人动作，而是根据查询条件预测语义关键交互点的未来 3D motion traces。为了解决训练监督来源问题，作者提出 TraceExtract：自动从多源视频中选择 semantic keypoints，构建 globally aligned traces，并把 motion segments 与 hierarchical language captions 关联起来，从而形成 event-captioned 3D trace tuples。模型训练上，摘录显示它结合 pretrained vision-language backbone，并利用 TraceExtract 产生的视频监督进行预训练。这个设计的新意在于把“语言描述的事件”和“3D interaction trajectory”对齐，使 world model 的输出既可被语言条件化，又保留可用于下游控制或规划的几何结构。当前摘录只能确认 TraceExtract 的高层组成和 3D trace 预测目标，不能确认关键点选择算法、3D 对齐如何处理相机运动与遮挡、caption 层级如何构造，以及下游 grounding 到机器人 action 的具体接口。

#### 📊 实验与结果

实验首先评估 trace prediction quality，并同时比较 2D 和 3D baselines。指标包括 moving points 上的 ADE、FDE，以及用于衡量轨迹形状且对时间错位更鲁棒的 DTW。摘录称 μ0 在 2D 上取得 best Top-5 ADE、FDE、DTW，在 3D 上所有报告的 ADE、FDE、DTW 指标和预测 horizon 都最好；同时预测延迟为 0.29s，比摘录中下一个最快的 2D baseline Track2Act 的 0.85s 快 2.9 倍。定性例子据称进一步支持结果。需要注意的是，摘录没有给出完整任务、数据集规模和下游机器人控制成功率，因此目前能确认的是 trace 预测质量和效率优势，而不是闭环操控性能已经充分验证。

#### ⚠️ 风险 / 保留意见

- 3D trace 质量高度依赖 TraceExtract，若关键点选择或全局对齐失败，模型监督会系统性偏差。
- 预测 interaction traces 并不等于可执行 robot actions，下游 grounding 接口仍是风险点。
- 摘录重点是预测指标，闭环规划或真实机器人部署证据不足。

#### 💭 结论与启发

μ0 对后续选题的启发是，world model 不一定要在像素空间里证明自己。对机器人而言，预测少量语义关键点的 3D 运动可能比生成逼真视频更可用，也更容易跨机器人形态迁移。复现时可以先不追求完整视频数据管线，而是从已有 RGB-D 或多视角数据中抽 interaction points，验证 trace prediction 是否能提升 affordance 估计、subgoal 生成或 inverse dynamics。阅读全文时最重要的是确认这些 traces 如何被控制器消费。

#### 🔎 读 PDF 先核查

- TraceExtract 如何在异构视频中稳定选择 contact regions、hands、tools 和 objects 的关键点？
- μ0 的 query conditioning 具体包含语言、视觉历史还是目标点提示，输出 trace 如何与任务目标绑定？
- 论文是否展示 trace 预测能实际提升机器人规划或 policy learning，而不只是预测误差更低？

#### 📌 上传 PDF 后优先看

- TraceExtract 数据生成流程和 3D 对齐细节
- 2D/3D trace prediction 主表、Top-5 采样设置与 latency 对比
- 下游 grounding、planning 或 robot learning 章节

### [4]. WAM4D: Fast 4D World Action Model via Spatial Register Tokens [[HTML]](https://arxiv.org/html/2606.14048) [[PDF]](https://arxiv.org/pdf/2606.14048) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.14048`
* **Authors**: Ying Li, Xiaobao Wei, Jiajun Cao, Hao Wang, Xiaowei Chi, Chengyu Bai, Qianpu Sun, Jiajun Li, Xiaojie Zhang, Jian Tang, Sirui Han, Shanghang Zhang
* **Author Priority**: Standard
* **一句话结论**: 优先看：WAM4D 代表 world action model 的几何化路线，用训练期 4D 几何监督换取推理期更轻量的动作生成。
* **关键词**: `WAM4D` `world action model` `spatial register tokens` `4D geometry` `causal video-action transformer`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

World action models 试图同时建模未来观察和可执行动作，比单纯 VLA 更强调“预测未来如何变化”与“生成机器人如何做”之间的耦合。但已有 WAM 多在 2D video 或 latent space 中工作，容易生成视觉合理但几何不一致的 rollout，特别是对精密操作中的 3D 空间约束、遮挡接触和物体相对位姿不够敏感。另一方面，直接让模型预测 dense 4D representation 会引入昂贵的几何解码，拖慢因果动作生成。WAM4D 的问题设定正是这个 trade-off：如何把几何 foundation model 的 3D/4D 先验蒸馏进 video-action transformer，同时避免部署时承担完整 dense geometry 预测成本。这对真实机器人很重要，因为部署需要低延迟，但训练又必须让模型知道空间和接触。

#### ⚙️ 核心方法

WAM4D 的核心是 spatial register tokens。根据摘录，它在训练期把这些轻量 register tokens 作为 future-depth readouts，用来把 pretrained geometric priors 转移到 causal video-action transformer 中；推理时则移除 register branch，使 action inference 保持轻量。模型骨架是 Mixture-of-Transformers WAM，并设计 causal mixture attention，为不同模态定义可见性约束，以避免非因果 shortcut。直观理解，WAM4D 并不要求模型部署时生成完整 4D 场景，而是在训练过程中通过 depth/geometry supervision 迫使内部表示吸收空间一致性，然后把这个表示用于动作生成。实验设置还提到用 Depth Anything 3 生成真实演示的离线 pseudo-depth，这表明方法不完全依赖昂贵真实深度标注。当前摘录只能确认 register distillation、causal mixture attention、训练期几何监督和推理期轻量化这些主张，不能确认 token 结构、loss 权重、MoT 路由细节或移除 register branch 后的表示保持机制。

#### 📊 实验与结果

实验覆盖模拟控制、视频和几何质量、真实操控。模拟使用 RoboTwin 2.0 完整任务套件，clean setting 相对简单，randomized setting 包含 clutter、illumination、background、tabletop height、object placement 和语言变化；几何监督使用重新收集的 RoboTwin demonstrations，每个任务包含 50 条 clean trajectories 和 500 条 randomized trajectories。真实机器人在 AstriBot S1 上评估四个任务：plate lifting、bottle placement、pen cap removal、LEGO sorting；每个任务 100 条 demonstration，共 400 条，并且每个方法每任务 10 次物理 rollout。结论称 WAM4D 改善 spatial consistency 和 action prediction，但也承认当前 WAM 仍慢于 VLA。摘录没有给出成功率或表格数值，因此定量优势需看全文。

#### ⚠️ 风险 / 保留意见

- 依赖 pseudo-depth 和几何 foundation prior，深度估计误差可能在接触/遮挡区域放大。
- 作者承认 WAM 当前仍慢于 VLA，实时部署收益需要结合任务频率判断。
- 每个真实任务 10 次 rollout 的设置较小，真实硬件统计置信度需谨慎。

#### 💭 结论与启发

WAM4D 的系统启发在于：几何监督可以作为训练期正则和表示蒸馏，而不必成为推理期负担。后续做 VLA 或 WAM 系统时，可以考虑把 depth、point tracking、scene flow 等几何目标作为 auxiliary branch，在部署时裁掉，只保留动作头。真正需要核查的是这种蒸馏是否在随机化、遮挡和长时程任务上稳定提升，而不是只改善视频/深度质量指标。若效果成立，它会是 Sim2Real 中一个实用的表示学习模板。

#### 🔎 读 PDF 先核查

- spatial register tokens 在训练期读取 future depth 的方式是什么，是否需要未来帧监督导致训练/推理分布差异？
- causal mixture attention 如何防止 video、geometry、action 模态之间的信息泄漏？
- WAM4D 的动作提升是否主要来自几何监督，还是来自 MoT backbone 和数据规模？

#### 📌 上传 PDF 后优先看

- spatial register distillation 与 register branch 移除机制
- RoboTwin clean/randomized 主结果、geometry quality 指标和消融
- AstriBot S1 四个真实任务的 rollout 统计、失败案例和速度对比

### [5]. FAWAM: Force-Aware World Action Models for Closed-Loop Contact-Rich Manipulation [[HTML]](https://arxiv.org/html/2606.08555) [[PDF]](https://arxiv.org/pdf/2606.08555) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.08555`
* **Authors**: Haotian He, Zeyu Yan, Qipeng Liu, Ning Guo, Wenzhao Lian
* **Author Priority**: Standard
* **一句话结论**: 优先看：FAWAM 把 force 从输入模态提升为预测与闭环纠偏信号，是 contact-rich manipulation 里很实际的 world action model 方向。
* **关键词**: `force-aware WAM` `contact-rich manipulation` `wrench prediction` `residual correction` `closed-loop control`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

接触丰富任务，如擦拭、削皮、推动和旋转，需要机器人持续调节与环境的物理交互。仅靠视觉很难判断弱接触、过大压力、卡滞或摩擦变化，这些状态往往在图像里不可见或滞后。已有 force/tactile VLA 或 visuomotor 方法通常把力觉当作额外 observation，让 policy 多一个输入，但没有充分利用 force 对未来接触演化的预测价值，也没有把预测力轨迹用于执行时闭环修正。FAWAM 的动机是把 force 放到三个层次：perception、prediction 和 closed-loop execution。对真实机器人来说，这比只做视觉语言动作映射更接近可部署系统，因为接触阶段的失败往往发生在动作 chunk 内部，必须比高层 VLA 更快地纠偏。

#### ⚙️ 核心方法

FAWAM 包含两个主要模块。第一是 Force-Envisioned Action Model，运行在 1 Hz，编码最近的 6-axis force/torque 历史为 compact contact features，并通过 AdaLN-Zero-style modulation 注入动作生成；它还联合预测未来 action trajectories 和 end-effector wrench trajectories，以显式学习机器人运动与接触后果之间的耦合。第二是 Force-Guided Residual Corrector，运行在 10 Hz，在执行过程中用模型预测的 force trajectory 作为参考，与实时 force feedback 比较，并输出 residual corrections，应对 action chunk 内出现的意外接触变化。这个结构的关键新意是把 force 既作为历史感知信号，也作为未来世界模型目标，还作为在线控制误差参考。当前摘录只能确认模块频率、输入输出和高层机制，不能确认 residual corrector 的控制形式、稳定性约束、force loss 权重或与原动作 chunk 的叠加边界。

#### 📊 实验与结果

真实硬件实验使用 Franka Research 3 机械臂，腕部安装 ATI Axia80-M8 6 轴力/力矩传感器，视觉来自三台 Intel RealSense D435i，包括一个腕部相机和两个第三人称视角。数据采集使用带力反馈的 leader-follower teleoperation system，基于 FACTR，让操作者能感知 follower 端接触力。任务包括 Erase Whiteboard、Peel Cucumber、Pivot Box 和 Wipe Vase，都要求持续接触和对力敏感的执行；数据多样性通过改变白板/花瓶倾角、桌高等条件引入。结论中明确给出 FAWAM achieves an 85.0% success，但摘录没有列出 baseline 数值、每任务成功率或统计方差，因此只能确认其真实机器人验证方向扎实，完整优势需看实验表。

#### ⚠️ 风险 / 保留意见

- 需要腕部 6 轴力/力矩传感器和力反馈遥操作数据，硬件与采集门槛较高。
- 1 Hz 高层 action model 加 10 Hz residual corrector 的稳定性和延迟边界需要仔细验证。
- 摘录只给出总体 85.0% success，缺少 baseline 和任务拆分，难以判断提升来源。

#### 💭 结论与启发

FAWAM 对系统设计的启发很直接：contact-rich manipulation 不应只把 force 当作 observation token，而应预测未来力并用它做在线误差参考。后续如果复现实验，可以从单任务擦拭或插入开始，先验证 predicted wrench trajectory 是否能提前反映接触失稳，再加 residual corrector。论文也提示 VLA 的 action chunk 执行需要低层反馈回路，否则高层模型即使语义正确，也可能在接触细节上失败。

#### 🔎 读 PDF 先核查

- Force-Guided Residual Corrector 如何把 predicted wrench 与实时 wrench 的误差映射成动作 residual？
- 联合预测 action 和 force 是否显著优于只把 force history 作为输入，消融结果如何？
- 85.0% success 的任务分布、baseline 差距和失败模式分别是什么？

#### 📌 上传 PDF 后优先看

- Force-Envisioned Action Model 与 AdaLN-Zero force modulation 细节
- Force-Guided Residual Corrector 的控制频率、稳定性和残差约束
- 四个真实接触任务的成功率表、消融和失败案例

### [6]. Hy-Embodied-0.5-VLA: From Vision-Language-Action Models to a Real-World Robot Learning Stack [[HTML]](https://arxiv.org/html/2606.14409) [[PDF]](https://arxiv.org/pdf/2606.14409) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.14409`
* **Authors**: He Zhang, Lingzhu Xiang, Haitao Lin, Zeyu Huang, Minghui Wang, Dingyan Zhong, Yubo Dong, Yihao Wu, Yongming Rao, Dongsheng Zhang, Wanjia He, Ling Chen, Kai Huang, Jiahao Chen, Sichang Su, Xumin Yu, Ziyi Wang, Chengwei Zhu, Xiao Teng, Yuchun Guo, Yufeng Zhang, Yuandong Liu, Rui Wang, Zisheng Lu, Han Hu, Zhengyou Zhang
* **Author Priority**: Standard
* **一句话结论**: 优先看：HyVLA-0.5 不是单一模型技巧，而是把 VLA、数据、SFT、RL post-training 和真实部署打通的系统报告。
* **关键词**: `HyVLA-0.5` `VLA stack` `conditional flow matching` `FlowPRO` `cross-embodiment deployment`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

这篇的价值在于它不把 VLA 当成孤立 policy，而是讨论如何把 VLA 变成真实机器人学习栈。当前 VLA 架构已经能把视觉、语言和连续控制连接起来，但部署 generalist robot 需要更多组件：数据采集要有高保真动作标签和触觉/操作细节，训练要兼顾预训练、SFT 和后训练，动作表示要能跨平台，执行层还要处理真实硬件约束。论文指出传统 master-slave teleoperation 会让操作者适应机器人工作空间，缺少直接 haptic feedback；人类数据或 UMI 能缓解数据稀缺，但原始 human demonstrations 动作标签过粗，手持框架也有局限。HyVLA-0.5 的目标是把这些问题放在同一个 pipeline 中解决，因此比单点 benchmark 更接近产业化 VLA stack。

#### ⚙️ 核心方法

HyVLA-0.5 遵循 VLA 范式：预训练 VLM 负责广义语义感知，专门 action module 把多模态上下文转为低层控制。系统包含三部分。第一，backbone 是 embodied VLM Hy-Embodied-0.5，采用 Mixture-of-Transformers 架构，支持 modality-adaptive computation 和 native-resolution image encoding。第二，action expert 通过 conditional flow matching 生成连续 action chunks，并把机器人特有的 state/action streams 与 VLM 分离，再通过 shared attention 耦合。第三，image encoder 扩展为 compact memory encoder，通过 interleaved temporal-spatial attention 聚合多帧观察历史。结论还提到 rel-EE/delta-chunk representation 用于保持动作接口相对独立于平台运动学，FlowPRO 将真实失败案例转化为紧凑 offline refinement，异步执行用于部署。当前摘录能确认完整组件，但不能确认 FlowPRO 的 RL/post-training 目标、数据筛选方式、memory 长度和 action chunk 参数。

#### 📊 实验与结果

实验回答两个问题：SFT 后在模拟和真实硬件上表现如何，以及 FlowPRO post-training 能把已部署 policy 提升多少。真实硬件 SFT 分为两条 track：Track A 在同一 tele-operated robot platform 上 fine-tune 和评估；Track B 只用 UMI demonstrations fine-tune，并部署到形态不同的机器人上，不使用目标机器人 teleoperation。摘录称 Track A 有四个任务，Track B 有两个任务。模拟评估使用 RoboTwin 2.0，在 Clean 和 Randomized 设置下报告任务成功率，并与八个 contemporary VLA systems 比较；完整 per-task breakdown 放在 Appendix。摘录未给出主表数值，因此目前只能确认评估范围和系统设计，不应引用具体提升幅度。

#### ⚠️ 风险 / 保留意见

- 系统组件很多，收益可能来自数据、表示、backbone、FlowPRO 或执行层组合，归因难度高。
- 摘录没有给出关键结果数值，必须查看主表和消融后才能判断是否超越现有 VLA。
- 完整栈可能对数据采集平台、UMI 流程和部署工程要求高，复现成本较大。

#### 💭 结论与启发

HyVLA-0.5 最值得学习的是系统分层：VLM backbone、flow action expert、memory encoder、跨 embodiment action representation、FlowPRO 后训练和异步执行各自承担不同职责。对后续选题而言，它提醒我不要只优化 policy loss，而要把数据接口和部署接口一起设计。读全文时要重点分离哪些组件带来主要收益，尤其是 compact memory、rel-EE/delta-chunk 和 FlowPRO；如果消融清楚，这篇可以作为搭建真实 VLA pipeline 的路线图。

#### 🔎 读 PDF 先核查

- FlowPRO 如何把真实失败案例转化为 offline refinement，是否属于 RL post-training、偏好优化还是过滤式再训练？
- rel-EE/delta-chunk representation 在跨机器人部署中如何处理不同末端、尺度和动力学约束？
- compact memory encoder 的多帧历史对长时程任务提升有多大，是否有单独消融？

#### 📌 上传 PDF 后优先看

- 模型章节中的 MoT backbone、action expert 和 compact memory encoder
- RoboTwin Clean/Randomized 主表、八个 VLA baseline 和组件消融
- Track A/Track B 真实部署、FlowPRO post-training 和异步执行细节

## Watchlist

### [W1]. Elastic Queries Reinforcement Learning: Self-Aware Policy Execution for VLA Models [[HTML]](https://arxiv.org/html/2606.14375) [[PDF]](https://arxiv.org/pdf/2606.14375)
* **Paper ID**: `2606.14375`
* **Authors**: Ge Wang, Xinyu Tan, Xiang Li, Man Luo, Chengsi Yao, Shenhao Yan, Jiahao Yang, Fan Feng, Honghao Cai, Xiangyuan Wang, Zhixin Mai, Yiming Zhao, Yatong Han, Zhen Li
* **Author Priority**: Standard
* **为什么还值得留意**: EQRL 很值得进 shortlist，因为它把 VLA 执行看成 state-dependent resource allocation：每次 query 可联合选择 latent input、denoising budget 和 action chunk length。它没有进入最终精选，主要是因为今天已有 FRS/OGPO 覆盖了更核心的 VLA steering 与 RL fine-tuning，而 EQRL 摘录中的定量证据还需要完整表格验证。后续应关注它是否真的能在困难接触阶段用更多计算、在简单阶段节省推理，而不是只做动态预算调参。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. PhysVLA: Towards Physically-Grounded VLA for Embodied Robotic Manipulation [[HTML]](https://arxiv.org/html/2606.13886) [[PDF]](https://arxiv.org/pdf/2606.13886)
* **Paper ID**: `2606.13886`
* **Authors**: Namai Chandra, Shriram Damodaran, Lin Wang
* **Author Priority**: Standard
* **为什么还值得留意**: PhysVLA 进入 watchlist 是因为它提出 plug-and-play inference-time physics wrapper，用 phase-aware finite-state machine 和 selective Lagrangian gate 给冻结 VLA 加物理约束，方向很实用。没有进最终精选，是因为摘录显示它更像推理时规则/约束包装器，相比 FRS、OGPO、WAM4D、FAWAM 的模型与训练贡献略窄。它声称增加低于 1 ms latency，并在 LIBERO-Spatial 上最高带来 17 pp success increase，这两个数字值得后续核查。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. ReactVLA: Fast and Lightweight Reactive Robot Manipulation via Improved Mean Flow Action Generation [[HTML]](https://arxiv.org/html/2606.14255) [[PDF]](https://arxiv.org/pdf/2606.14255)
* **Paper ID**: `2606.14255`
* **Authors**: Yanzhao Guo, Wenkai Chen, Jianwei Zhang
* **Author Priority**: Standard
* **为什么还值得留意**: ReactVLA 值得跟踪，因为低延迟是 diffusion/VLA 部署的硬瓶颈，它用 improved Mean Flow action generator 把多步采样压到 one-to-few-step，并配合 Attention Residual Transformer。没有进入最终精选，是因为其主线偏工程加速，和今天更优先的 world/action model、force closed-loop、RL post-training 相比，研究问题覆盖面稍窄。后续要看低延迟是否在真实 Diana 机器人 20 runs 设置下保持精度，而不是只在模拟中提升吞吐。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. ContactWorld: What Matters in Vision-Tactile World Models for Contact-Rich Manipulation [[HTML]](https://arxiv.org/html/2606.13877) [[PDF]](https://arxiv.org/pdf/2606.13877)
* **Paper ID**: `2606.13877`
* **Authors**: Zhiyuan Zhang, Pokuang Zhou, Kaidi Zhang, Adeesh Desai, Temitope Amosa, Davood Soleymanzadeh, Jiuzhou Lei, Minghui Zheng, Yu She
* **Author Priority**: Standard
* **为什么还值得留意**: ContactWorld 进入 watchlist 是因为它系统研究 vision-tactile world models，覆盖 12 个 contact-rich manipulation tasks，并强调 spatially structured 与 temporally continuous representations 对长时程规划重要。没有进入最终精选，是因为它更像 benchmark 和经验研究，而 FAWAM 已经提供了更直接的 force-aware closed-loop action model。后续值得阅读其 JEPA-style latent world model 设计，尤其是为何对 fused multimodal latents 做联合正则会损害规划表现。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
