# RoboPulse | 2026-06-26

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 84 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线很清晰：VLA 正在从“直接给动作”转向“带有系统辨识、未来预测、价值估计与数据覆盖意识的闭环控制接口”。最终精选覆盖了 in-context world modeling、灵巧手 RL 预训练、触觉 WAM、竞赛级 VLA+RL 工程、world model 幻觉诊断，以及开放行为克隆栈，基本对应 VLA 落地时最关键的泛化、接触、持续优化和数据基础设施问题。VIP 作者中，Jeannette Bohg 的 Play2Perfect、Xiaolong Wang 的 world model 幻觉分析、Pieter Abbeel 参与的 ABC 都值得优先跟踪；watchlist 里 Jiajun Wu 参与的 CoStream 也显示出组合式操作技能的长期价值。整体看，今天不是单点模型架构更新，而是“如何让 VLA/WAM 在真实机器人上可诊断、可微调、可复现、可扩展”的系统化推进。

## 今日信号

- VLA/WAM 的下一阶段竞争点正在从语言理解和动作生成，转向对执行上下文、接触状态、未来轨迹和失败风险的显式建模。
- Sim2Real 论文越来越强调可复用工程闭环：仿真采样、RL/DAgger、人类修正、在线失败检测和真实机器人验证被组织成一个持续优化系统。
- 开放数据与诊断 benchmark 的价值上升，因为没有覆盖度、安全性、幻觉和真实任务成功率的共同度量，单个 VLA 模型的能力声明很难比较。

## Historical Rediscovery

- **Paper**: ROAD-VLA: Robust Online Adaptation via Self-Distillation for Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2606.25800) [[PDF]](https://arxiv.org/pdf/2606.25800)
  - **Paper ID**: `2606.25800`
  - **来源日期**: 2026-06-25
  - **当时可能被低估的信号**: scalar advantage 转成 action-token 级 dense supervision，以及明确指出 text-based privileged teacher 和低层动作之间的 modality gap，这两个信号比普通 VLA 微调更接近动作学习机制问题。
  - **为什么现在值得再看**: 今天如果关注 VLA 如何在部署期自适应、如何把奖励或优势信号落到动作 token，ROAD-VLA 值得重新看；尤其适合作为 RL+VLA 后训练和 online adaptation 的补充线索。
  - **建议动作**: 加入精读
  - **关键词**: `VLA` `online adaptation` `self-distillation` `RL+VLA` `action-token supervision`
- **Paper**: Action ControlNet: A Lightweight Delay-Aware Adapter for Smooth Asynchronous Control in Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2606.25985) [[PDF]](https://arxiv.org/pdf/2606.25985)
  - **Paper ID**: `2606.25985`
  - **来源日期**: 2026-06-25
  - **当时可能被低估的信号**: 异步执行延迟、chunk handoff discontinuity、控制平滑性，以及 Kinetix、Meta-World MT50、真实 SO-ARM101 的线索，说明它不是纯模型结构小改，而是在处理闭环部署可靠性。
  - **为什么现在值得再看**: 对 VLA、Sim2Real 和真实机器人评测都很相关；如果今天要判断 VLA 是否能稳定落地，延迟感知控制和动作块交接问题比离线 benchmark 更值得复盘。
  - **建议动作**: 加入精读
  - **关键词**: `VLA` `real deployment` `asynchronous control` `Sim2Real` `control smoothness`
- **Paper**: GRAFT: Graph-Based Affordance Transfer via Part Correspondence [[HTML]](https://arxiv.org/html/2606.25241) [[PDF]](https://arxiv.org/pdf/2606.25241)
  - **Paper ID**: `2606.25241`
  - **来源日期**: 2026-06-25
  - **当时可能被低估的信号**: part graph、UFGW graph matching、contact-level correspondence 和 zero-shot affordance transfer 同时出现，说明它可能提供了比语言标签更细的可迁移操作先验。
  - **为什么现在值得再看**: 与 Sim2Real、VLA 数据生成、未见物体操作强相关；如果要构建 world/action model 的可操作物体先验，GRAFT 值得作为几何泛化模块重看。
  - **建议动作**: 快速浏览
  - **关键词**: `Sim2Real` `affordance transfer` `unseen objects` `contact correspondence` `data generation`
- **Paper**: KinDER: A Physical Reasoning Benchmark for Robot Learning and Planning [[HTML]](https://arxiv.org/html/2604.25788) [[PDF]](https://arxiv.org/pdf/2604.25788)
  - **Paper ID**: `2604.25788`
  - **来源日期**: 2026-04-29
  - **当时可能被低估的信号**: 25 个程序生成环境、13 个 baseline、统一物理推理评测框架，以及 Danfei Xu 和 Tom Silver 的作者组合，显示它可能成为后续机器人推理论文的常用压力测试。
  - **为什么现在值得再看**: 对 World Model、World Action Model 和长时程机器人规划评测有直接价值；适合用来判断模型是否真的学到物理因果与可执行计划，而不是只在语言或视觉问答上表现好。
  - **建议动作**: 加入精读
  - **关键词**: `physical reasoning` `benchmark` `robot learning` `planning` `world model`
- **Paper**: EvolvingAgent: Curriculum Self-evolving Agent with Continual World Model for Long-Horizon Tasks [[HTML]](https://arxiv.org/html/2502.05907) [[PDF]](https://arxiv.org/pdf/2502.05907)
  - **Paper ID**: `2502.05907`
  - **来源日期**: 2026-04-30
  - **当时可能被低估的信号**: continual world model 与 curriculum self-evolving agent 放在同一框架中，说明它可能包含关于长时程探索和世界模型持续更新的可迁移思想。
  - **为什么现在值得再看**: 虽然离机器人 VLA 操作还有转译距离，但对 RL+VLA、长时程任务和 World Action Model 的训练机制有启发，适合快速判断是否有可借鉴的 curriculum 或记忆更新设计。
  - **建议动作**: 快速浏览
  - **关键词**: `continual world model` `long-horizon tasks` `RL` `curriculum` `embodied agent`

## Editor's Picks

### [1]. In-Context World Modeling for Robotic Control [[PDF]](https://arxiv.org/pdf/2606.26025) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.26025`
* **Authors**: Siyin Wang, Junhao Shi, Senyu Fei, Zhaoyang Fu, Li Ji, Jingjing Gong, Xipeng Qiu
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为它把 VLA 泛化失败重新表述为“缺少系统辨识上下文”的问题，而不是单纯扩大数据或微调模型。
* **关键词**: `VLA` `in-context adaptation` `world modeling` `system identification` `Sim2Real`
* **证据来源**: Abstract fallback

#### 📖 背景与动机

这篇关注 VLA 在新相机视角、新机器人形态或新执行环境下的泛化问题。常见 VLA 只根据当前视觉观测和语言指令输出动作，默认训练时见过的执行上下文仍然成立；一旦相机、动力学、机构或环境配置变化，模型缺少判断“自己处在什么系统里”的变量，只能依赖额外数据微调。对机器人控制来说，这正是 Sim2Real 和跨平台部署的痛点：任务语义可能没变，但执行映射、观测几何和动作后果变了。论文的价值在于把适应问题从“给新任务示范”转为“让策略从短历史交互中识别系统”。

#### ⚙️ 核心方法

当前摘录只能确认其核心框架名为 In-Context World Modeling, ICWM，并且将 system identification 作为 in-context adaptation 来处理。它不是用上下文窗口告诉模型要做什么任务，而是让机器人先进行一小段自生成、任务无关的交互，从这些历史观测和动作后果中推断关键系统变量，再据此调整后续控制。这个设定与传统 in-context learning 的差异很重要：示范上下文通常编码任务意图或动作范例，ICWM 的上下文则编码“这个系统如何响应动作”。从 VLA 角度看，它相当于给策略加入一个隐式世界模型或执行上下文估计器，使当前观测和语言不再是唯一条件。由于只有摘要回退，摘录未说明具体网络结构、上下文长度、系统变量是否显式监督、动作空间如何接入，也不能确认它与现有 world model/VLA backbone 的训练细节。

#### 📊 实验与结果

摘要明确指出目标场景包括 altered camera viewpoints 与 robot morphologies，并强调 ICWM 可减少新环境下数据密集微调的需求。但当前没有 HTML 实验段落，不能引用任何 benchmark 名称、成功率、对比模型、消融结果或真实机器人数字。可保守判断，实验应围绕跨视角、跨形态或跨环境配置泛化展开，重点验证短历史交互是否能帮助策略识别系统差异。对读者来说，上传 PDF 后最需要核查的是它是否只在受控变量变化中有效，还是能覆盖真实部署中常见的复合 shift。

#### ⚠️ 风险 / 保留意见

- 只有摘要回退，方法结构和实验强度目前证据不足。
- 短历史自交互可能引入安全成本，真实机器人上探索动作如何约束需要核查。
- 如果系统变化超出训练分布，in-context 推断可能只是拟合表面相关性。

#### 💭 结论与启发

这篇给后续 VLA 系统设计的启发是：不要只把上下文窗口当成任务提示或示范缓存，还可以把它当成在线系统辨识接口。对于多机器人、多相机、多环境部署，策略需要先知道“动作在当前系统里会产生什么效果”，再执行语言任务。复现时应优先做最小验证：固定任务语义，只改变相机外参、末端执行器或动力学参数，比较无上下文、任务示范上下文和 ICWM 式交互上下文的差异。

#### 🔎 读 PDF 先核查

- ICWM 的短历史交互是随机探索、学习到的 probing policy，还是由主策略自然产生？
- 系统变量是显式建模还是完全隐式编码，训练时有没有 ground-truth system parameter 监督？
- 在相机视角和机器人形态同时变化时，性能是否仍然来自上下文推断而非训练分布覆盖？

#### 📌 上传 PDF 后优先看

- 方法章节中的上下文构造、系统辨识目标和策略接口。
- 跨视角、跨形态、跨环境配置的泛化实验。
- 与普通 VLA 微调、示范式 in-context learning、无上下文策略的消融对比。

### [2]. Play2Perfect: What Matters in Dexterous Play Pretraining for Precise Assembly? [[VIP]] [[HTML]](https://arxiv.org/html/2606.26428) [[PDF]](https://arxiv.org/pdf/2606.26428) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.26428`
* **Authors**: Tyler Ga Wei Lum, Kushal Kedia, C. Karen Liu, Jeannette Bohg
* **Author Priority**: Core VIP
* **一句话结论**: 非常值得优先看，因为 Jeannette Bohg 团队把灵巧手精密装配拆成“先通过 play 学接触先验，再用 RL 精修”的可验证路线。
* **关键词**: `dexterous manipulation` `play pretraining` `reinforcement learning` `precise assembly` `Sim2Real`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

多指灵巧手理论上比平行夹爪更接近人手能力，但精密装配长期困难：接触多、自由度高、遮挡严重，模仿学习很难收集高质量示范；同时任务奖励稀疏，直接 RL 探索插入、拧紧、对齐等行为又效率很低。过去不少工作通过定制夹具、工具附件或环境约束降低难度，但这会牺牲通用性。Play2Perfect 的问题意识是，机器人在追求精密装配前，应先获得一个能处理多物体、多接触、多姿态变化的 dexterous play prior，再把这个先验精修到具体装配目标上。

#### ⚙️ 核心方法

论文使用 Split and Aggregate Policy Gradients, SAPG 训练 play policy，这是 PPO 的 population-based 变体，适合大规模并行环境中的探索。actor 采用 LSTM 聚合交互历史，用于推断未观测的物体属性，再通过 MLP 输出机械臂和手部动作。训练采用 asymmetric actor-critic：actor 只接收部署时可用观测，critic 额外接收无噪声、无延迟观测，手掌和物体速度，奖励信号，以及最小目标距离、物体是否被抬起等进度特征；这些 privileged information 只在训练阶段使用。摘录还明确说预训练和 finetuning 使用同一套 RL 算法和超参数。新意不只是“play pretraining”，而是系统研究 play 的对象多样性、目标、轨迹多样性和目标精度等因素如何影响下游精密装配。

#### 📊 实验与结果

实验围绕四个问题：密集任务奖励能否替代 play pretraining，哪些 play 设计选择最重要，精密接触装配是否仍需 RL finetuning，以及策略能否从仿真迁移到真实装配。硬件是 22-DoF Sharpa 五指手加 7-DoF KUKA iiwa 14；任务包括 Tight-Insertion、Assemble-Beam 和 Screw-Leg。论文使用 success rate 等指标，并声明 ablation 显示对象多样性、目标、轨迹多样性和目标精度都会影响下游表现，最后称策略可 zero-shot transfer 到真实世界灵巧装配。摘录没有给出具体成功率，因此不能判断提升幅度。

#### ⚠️ 风险 / 保留意见

- 系统学习的是短程装配技能，不是完整自主装配流水线。
- 任务 sequencing、active-part selection 和 goal poses 仍由外部指定。
- 真实迁移虽被声明为 zero-shot，但具体场景数量、失败模式和鲁棒性需要看 PDF。

#### 💭 结论与启发

这篇适合作为“灵巧操作预训练该怎么设计”的重点读物。它提醒我们，精密装配不是靠更复杂的末端奖励就能解决，先验的覆盖范围、交互历史建模和目标精度会直接影响 RL 精修效率。后续复现可以先不追求完整硬件，而是在仿真中比较无 play、单物体 play、多物体 play、不同 goal precision 的 finetuning 曲线，再看这些因素是否稳定影响插入和拧紧任务。

#### 🔎 读 PDF 先核查

- play 预训练的目标设计中，哪些因素对下游装配提升最大，是否存在任务依赖性？
- LSTM 历史聚合主要帮助识别物体属性、接触状态，还是补偿观测噪声和延迟？
- zero-shot sim-to-real 的成功是否依赖特定 3D 打印部件、视觉追踪设置或外部 goal pose？

#### 📌 上传 PDF 后优先看

- play pretraining 任务设计与奖励/目标定义章节。
- 对象多样性、轨迹多样性、目标精度相关 ablation。
- 真实机器人 zero-shot transfer 设置、成功标准和失败案例。

### [3]. Tactile-WAM: Touch-Aware World Action Model with Tactile Asymmetric Attention [[HTML]](https://arxiv.org/html/2606.26663) [[PDF]](https://arxiv.org/pdf/2606.26663) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.26663`
* **Authors**: Siyu Wu, Linjing You, Junjie Zhu, Yaozu Liu, Changhao Zhang, Jian Liu, Weiqiang Wang, Qi Li, Jituo Li, Hengshuang Zhao
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为它把 WAM 的未来预测从 RGB 扩展到触觉，同时明确指出触觉 token 可能污染视觉动力学建模。
* **关键词**: `World Action Model` `tactile sensing` `contact-rich manipulation` `asymmetric attention` `future prediction`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

World Action Model 的吸引力在于同时生成动作和未来状态，使策略不只输出动作，还能预测动作会把世界带到哪里。但在接触丰富的 manipulation 中，视觉上合理的未来并不等于物理上正确：插入、装配、搜索和重定向常常取决于滑移、卡滞、接触法向、小角度误差等弱可见甚至不可见信息。直接加入触觉预测看似自然，却可能破坏已有视觉动态先验，因为触觉信号通常稀疏、局部、事件驱动，与视频 token 的统计结构不同。论文提出的核心问题就是：如何让 WAM 用触觉指导动作，而不让触觉污染视觉未来生成。

#### ⚙️ 核心方法

Tactile-WAM 的核心机制是 Tactile Asymmetric Attention Mechanism, TAAM。摘录明确说明 TAAM 包含 VideoClean mask 和 touch-aware bias：VideoClean 阻止 video query 访问 tactile key/value token，从而保护视频预测分支不被稀疏触觉信号干扰；同时保留 action query 对触觉 token 的访问，让动作生成仍能利用未来接触变化。touch-aware bias 则进一步强化动作注意力对触觉变化的利用。这个设计的关键是非对称信息流：视觉预测保持相对“干净”，动作去噪或动作生成可以读取触觉。这比简单多模态拼接更有针对性，因为它承认不同模态对不同输出头的价值不同。当前摘录没有完整展示 loss、触觉表示格式、预测 horizon 和具体 backbone 细节，只能确认其目标是同时预测未来触觉接触状态并生成动作。

#### 📊 实验与结果

实验在 ManiFeel simulation benchmark 和匹配的 contact-rich real-robot tasks 上进行，对比对象包括基于通用 action-policy 的 baseline 以及 DreamZero-based RGB-only WAM baseline。摘录明确说 Tactile-WAM 在 ManiFeel 上整体成功率超过 RGB-only DreamZero 和 action-policy baseline，且提升在装配和插入任务上更明显；但 HTML 摘录中的具体 trial 数和成功率数字缺失，因此不能引用数值。论文还指出 object search 和 peg 相关任务仍然困难，说明触觉未来对局部接触纠错有帮助，但不能自动解决视觉搜索和长程恢复。

#### ⚠️ 风险 / 保留意见

- 触觉硬件、校准和数据采集成本可能限制复现。
- VideoClean 假设视觉预测应避免触觉 token，但某些场景中视觉和触觉可能需要更紧耦合。
- 长程搜索、恢复和规划仍是失败点，WAM 本身不等于完整任务策略。

#### 💭 结论与启发

这篇对 WAM 系统设计的启发是，多模态不是简单把 token 拼起来，而是要控制信息路由。触觉对动作很关键，但它未必应该同等影响视频生成；把不同 query 的访问权限分开，是一个可迁移到力觉、深度、proprioception 的设计思想。后续阅读应重点判断 TAAM 的收益是否来自触觉预测本身、attention mask，还是额外模型容量，并关注真实机器人任务是否能证明触觉在视觉不可见接触中的必要性。

#### 🔎 读 PDF 先核查

- TAAM 的 VideoClean mask 与 touch-aware bias 分别贡献多少，是否有清晰消融？
- 未来触觉状态的表示是接触二值、触觉图像、力/位移特征，还是 learned token？
- 真实机器人提升主要集中在哪类接触失败，例如滑移、卡滞、插入偏差还是搜索误判？

#### 📌 上传 PDF 后优先看

- TAAM 架构、attention mask 和 tactile routing 细节。
- ManiFeel 各任务类别的 per-task 结果与消融。
- 真实机器人接触任务设置、触觉传感器配置和失败案例。

### [4]. Learning to Fold: prizewinning solution at LeHome Challenge 2026 (1st place online, 2nd offline) [[HTML]](https://arxiv.org/html/2606.27163) [[PDF]](https://arxiv.org/pdf/2606.27163) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.27163`
* **Authors**: Ilia Larchenko
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为它是竞赛级 VLA+RL+Sim2Real 工程报告，给出了真实 leaderboard 约束下什么方法真正有效。
* **关键词**: `VLA` `reinforcement learning` `deformable manipulation` `DAgger` `Sim2Real`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

LeHome Challenge 2026 的任务是双臂衣物折叠，属于典型 deformable-object manipulation：视觉状态高维、物体形变复杂、动作需要双臂协调，且仿真到真实的差异明显。相比刚体抓取，衣物折叠很难用固定关键点或解析控制完全解决；相比纯 BC，复杂失败模式又需要持续采样和修正。作者的系统在 online simulation round 62 支队伍中第 1，real-world final 第 2，这使它特别有参考价值：它不是提出单一漂亮概念，而是在竞赛压力下把 VLA、RL、DAgger、失败检测和工程优化组合成可运行闭环。

#### ⚙️ 核心方法

系统核心是让 policy 同时承担 action predictor 和 value estimator：同一个网络预测动作，也预测 success、progress 以及少量任务相关未来量，这些预测用于 advantage estimation、在线失败检测和 candidate selection。训练是异步 flywheel：training worker、多个 rollout worker 和 manual DAgger station 之间主要通过 HuggingFace Hub 交换模型和数据。advantage 以两种方式影响策略：一是 AWR 式 sampler 重加权，高 advantage frame 被更频繁加载；二是 RECAP-style advantage conditioning，把 advantage 作为输入，从而在推理时支持 classifier-free guidance。作者认为这种 conditioning/reweighting family 比 PPO-style 方法更适合 flow-matching VLA。架构从团队此前 BEHAVIOR-1K 方案发展而来，摘录只透露包含 frozen SigLIP 等组件，完整细节需看 PDF。

#### 📊 实验与结果

online round 在 Isaac Sim 中评估四类衣物，每类 20 件，共 80 件，其中包括 seen 和 unseen garments；每个 garment 评估 10 次，按四类平均成功率排名。最终策略在 62 支队伍中第 1，总成功率 79.63%，领先第二名 6.1 个百分点；per-type 分数为 74.5% / 70.0% / 80.5% / 93.5%。摘要还说明真实世界决赛第 2。作者在结论中坦率指出系统是大量实践选择的组合，多数没有严格 ablation，这降低了因果解释强度，但提高了工程经验价值。

#### ⚠️ 风险 / 保留意见

- 许多贡献是工程组合，缺少完整 ablation，难以确认单个组件贡献。
- 竞赛环境和 SO-ARM101 设置可能限制外推到其他双臂平台。
- 依赖仿真 rollouts、手动 DAgger 和大量系统调参，复现成本较高。

#### 💭 结论与启发

这篇最适合当作 VLA+RL 落地手册阅读，而不是只当算法论文。它强调 value head、advantage-conditioned policy、异步 rollout、hard-mining、环境增强和人工 DAgger 的组合效应。对后续系统设计来说，一个重要启发是：当 VLA 是 flow-matching 或生成式动作模型时，不一定要强行套 PPO；用 advantage 做数据采样和条件输入，可能是更稳定的 RL 接口。复现时应优先抽取“policy as value function”和“advantage-conditioned inference”两个最小模块验证。

#### 🔎 读 PDF 先核查

- policy 自身的 success/progress/future heads 是否经过独立校准，在线失败检测的误报和漏报如何处理？
- advantage conditioning 在推理时的 classifier-free guidance 具体如何影响动作分布和安全性？
- 真实世界第 2 的失败主要来自 sim-to-real gap、视觉误差、衣物物理差异还是执行器限制？

#### 📌 上传 PDF 后优先看

- RL flywheel、AWR sampling 和 advantage conditioning 章节。
- policy architecture 与 success/progress/future prediction heads。
- leaderboard 结果、真实决赛设置和 qualitative failure analysis。

### [5]. Hallucination in World Models is Predictable and Preventable [[VIP]] [[HTML]](https://arxiv.org/html/2606.27326) [[PDF]](https://arxiv.org/pdf/2606.27326) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.27326`
* **Authors**: Nicklas Hansen, Xiaolong Wang
* **Author Priority**: Core VIP
* **一句话结论**: 必须优先看，因为 Xiaolong Wang 参与的这篇把 world model 幻觉从现象描述推进到可预测、可缓解的数据覆盖问题。
* **关键词**: `world model` `hallucination` `coverage` `MMBench2` `targeted data collection`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

生成式 world model 已能渲染看似真实、可由动作控制的未来，但 rollout 可能视觉流畅却偏离真实动力学。对机器人和 RL 来说，这比普通视频生成错误更危险，因为下游 planner 或 policy 会直接使用这些未来轨迹决策。论文的核心假设是 hallucination 集中在 state-action coverage 较低的区域，因此轻量的数据中心信号既能预测幻觉风险，也能指导缓解。这个问题与 VLA/WAM 高度相关：如果模型能生成未来但不知道何时不可信，未来预测反而会放大错误控制。

#### ⚙️ 核心方法

作者引入 MMBench2，一个包含 427 小时、210 个任务的数据集，带 ground-truth actions、rewards 和 live simulators，并训练一个 350M 参数视觉 world model。模型大体遵循 Dreamer 4 的架构和训练 recipe：先通过 masked auto-encoding 训练 video tokenizer，再冻结 tokenizer，用 block-causal Transformer dynamics model 在空间 latent token 上做 flow matching，并接入 action token 条件。随后通过一系列 targeted finetuning 实验分析 hallucination。论文识别三类幻觉模式：perceptual、action-marginal 和摘录中未完整展开的后续类型。方法重点不是提出一个全新大模型，而是把 hallucination 与覆盖度、采样重加权、奖励标签和 targeted data collection 联系起来。

#### 📊 实验与结果

实验训练 350M action-conditioned world model，训练数据约 20M frames，覆盖 200 个连续控制任务，并保留剩余数据测试；论文明确只使用 RGB observations，尽管低维状态可用。评估分四个阶段：无 reward label 的 action-conditioned pretraining，加入 coverage-aware reweighted sampling 的 mid-training，带 reward label 的 world modeling，以及 seen/unseen task 上通过 targeted data collection finetuning。指标包括 tokenizer 重建 PSNR、相对 last-frame baseline 的 rollout PSNR gain 等。结论称 targeted data collection 能在很大程度上缓解 hallucination，但不同数据源信息量差异很大。

#### ⚠️ 风险 / 保留意见

- PSNR 类指标可能无法完全反映规划安全性和任务成功率。
- 数据集和 simulator 覆盖虽大，但真实机器人动力学差异仍未从摘录中确认。
- targeted data collection 有效，但需要知道在哪里采数据，实际系统中可能形成闭环成本。

#### 💭 结论与启发

这篇对 world model 研究的价值在于给出一个可操作诊断框架：先定位低覆盖 state-action 区域，再判断幻觉类型，再用目标采样修复。对于 VLA/WAM 系统，未来预测模块必须配套 uncertainty 或 coverage 信号，否则 rollout 视觉质量会掩盖动力学错误。后续阅读应重点核查覆盖度信号如何计算、是否能在线使用、是否能预测下游 planner failure，以及 targeted data collection 比随机、专家或 closed-loop 数据到底强在哪里。

#### 🔎 读 PDF 先核查

- 论文使用哪些轻量 data-centric signals 预测低覆盖区域，它们是否需要 simulator 或 ground-truth state？
- 三类 hallucination 的判定标准是什么，是否能映射到机器人控制失败类型？
- coverage-aware mid-training 和 targeted data collection 哪个贡献更大，二者是否互补？

#### 📌 上传 PDF 后优先看

- MMBench2 数据集构成、任务覆盖和 train/test 划分。
- hallucination 类型定义、检测指标和可视化案例。
- coverage-aware reweighting 与 targeted data collection 的消融实验。

### [6]. Scalable Behavior Cloning with Open Data, Training, and Evaluation [[VIP]] [[PDF]](https://arxiv.org/pdf/2606.27375) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.27375`
* **Authors**: Arthur Allshire, Himanshu Gaurav Singh, Ritvik Singh, Adam Rashid, Hongsuk Choi, David McAllister, Justin Yu, Yiyuan Chen, Huang Huang, Pieter Abbeel, Xi Chen, Rocky Duan, Phillip Isola, Jitendra Malik, Fred Shentu, Guanya Shi, Philipp Wu, Angjoo Kanazawa
* **Author Priority**: Core VIP
* **一句话结论**: 必须优先看，因为 Pieter Abbeel 参与的 ABC 把开放数据、硬件、训练和评测打包成行为克隆基础设施，而不只是又一个策略模型。
* **关键词**: `behavior cloning` `open dataset` `VLA` `Diffusion Transformer` `robot manipulation`
* **证据来源**: Abstract fallback

#### 📖 背景与动机

机器人行为克隆长期受限于数据规模、硬件可得性、训练代码不透明和真实评测昂贵。VLA/DiT 模型看似强大，但没有足够开放的 teleoperation 数据和可重复评测，很难判断架构改动是否真的提升真实操作。ABC 的重要性在于把 manipulation BC 的基础设施整体开放：数据、硬件、训练、仿真和评估都作为系统的一部分。对 VLA 社区来说，这类工作可能比单个模型技巧更有长期影响，因为它提供了比较 Diffusion Transformer、VLA 和训练 recipe 的共同地基。

#### ⚙️ 核心方法

当前只有摘要回退，能确认 ABC 是 fully open-source stack for manipulation with behavior cloning。核心数据集 ABC-130K 包含 3500 小时 teleoperation 数据，超过 130K episodes，覆盖 195 个任务；同时开放 accessible hardware setup、training infrastructure 和 simulation pipeline。论文还释放 400 小时 sim-teleop 数据，并给出 co-training recipe，使仿真与真实评估结果相关，从而在昂贵真实实验前用仿真作为 model-design 和 training decision 的可靠 proxy。方法上它比较 Diffusion Transformers 和 VLA 模型的常见架构选择，并以真实世界评估支撑结论。摘要未给出具体模型结构、任务拆分、数据采集协议或评测数字，因此这些不能展开。

#### 📊 实验与结果

摘要明确说明结果基于真实世界评估，并声称最终策略能完成 box folding 等 dexterous tasks 以及后文被截断的更多任务。已知规模包括 3500 小时真实 teleoperation、130K+ episodes、195 tasks，以及 400 小时 sim-teleop 数据。论文的实验重点应是不同训练 recipe、DiT/VLA 架构选择、sim-real correlated evaluation 和真实 manipulation 成功情况。由于缺少 HTML 正文，不能引用具体成功率、benchmark 表格或哪种架构胜出。它入选的原因主要是基础设施和开放数据价值，而不是摘要中某个具体指标。

#### ⚠️ 风险 / 保留意见

- 只有摘要回退，无法确认数据许可、硬件成本和完整复现门槛。
- 大规模 BC 仍可能受 teleop 分布限制，对长程纠错和主动探索支持不足。
- 仿真与真实评估“相关”需要看统计证据，不能仅凭摘要判断可靠程度。

#### 💭 结论与启发

这篇应该作为后续所有 VLA/BC 复现实验的资源候选。它提供的不只是数据量，而是开放硬件、训练基础设施、仿真管线和真实评测之间的闭环。如果 co-training recipe 的 sim-real 相关性站得住，它能显著降低做架构消融的成本。阅读 PDF 时应把重点放在数据覆盖、评测协议和训练 recipe，而不是只看最终 policy demo；真正有用的是哪些设计决策能稳定迁移到真实机器人。

#### 🔎 读 PDF 先核查

- ABC-130K 的 195 个任务如何分布，是否覆盖长程、接触丰富和双手操作任务？
- sim-teleop co-training 如何建立与真实评估的相关性，相关性在哪些任务上失效？
- DiT 和 VLA 架构比较控制了哪些变量，例如数据量、backbone、action representation 和训练步数？

#### 📌 上传 PDF 后优先看

- 数据集采集协议、任务 taxonomy 和硬件设置。
- co-training recipe 与 sim-real correlation 证据。
- DiT/VLA 架构选择、训练 recipe 消融和真实机器人评测。

## Watchlist

### [W1]. CoStream: Composing Simple Behaviors for Generalizable Complex Manipulation [[VIP]] [[PDF]](https://arxiv.org/pdf/2606.26423)
* **Paper ID**: `2606.26423`
* **Authors**: Haonan Chen, Yuxiang Ma, Stephen Tian, Xiaoshen Han, Wenlong Huang, Feiyang Wu, Yunzhu Li, Jiajun Wu, Edward H. Adelson, Yilun Du
* **Author Priority**: Extended VIP
* **为什么还值得留意**: CoStream 进入 shortlist 是因为它面向长程、接触丰富、高精度 manipulation，且 Jiajun Wu 属于扩展关注作者。它提出由简单独立行为组合出复杂操作能力，对 GPU 插 PCIe 这类高精度任务很有吸引力。没有进入最终精选，主要是当前只有摘要回退，方法细节、实验规模和真实机器人证据不足，暂时难以判断它相对 VLA/WAM/RL 主线的确定性贡献。
* **证据来源**: Abstract fallback

### [W2]. Improving Vision-Language-Action Model Fine-Tuning with Structured Stage and Keyframe Supervision [[HTML]](https://arxiv.org/html/2606.26801) [[PDF]](https://arxiv.org/pdf/2606.26801)
* **Paper ID**: `2606.26801`
* **Authors**: Yuan Xu, Yixiang Chen, Kai Wang, Jiabing Yang, Peiyan Li, Qisen Ma, Yan Huang, Liang Wang
* **Author Priority**: Standard
* **为什么还值得留意**: StaKe 值得跟踪，因为它针对 VLA fine-tuning 中常见的 gripper-event transition 失败，提出从 demonstration gripper states 自动生成 stage classifier 和 keyframe predictor 监督，不需要人工标注且不改变 inference loop。它覆盖 RoboTwin 2.0 bimanual simulation 和 real-robot tasks，方向实用。未进最终精选，是因为它更像 VLA 微调辅助监督的局部改进，战略宽度低于 ICWM、Tactile-WAM、world model 幻觉和 ABC 这几篇。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. ForesightSafety-VLA: A Unified Diagnostic Safety Benchmark for Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2606.27079) [[PDF]](https://arxiv.org/pdf/2606.27079)
* **Paper ID**: `2606.27079`
* **Authors**: Mingyang Lyu, Yinqian Sun, Yiyang Jia, Sicheng Shen, Moquan Sha, Huangrui Li, Feifei Zhao, Yi Zeng
* **Author Priority**: Standard
* **为什么还值得留意**: ForesightSafety-VLA 进入 watchlist 是因为 VLA 安全评测正在变成部署前的必需环节，论文提供 13 类安全 taxonomy，并从 Safe-Core、Safe-Lang、Safe-Vis 以及场景结构、语言、视觉变化等维度诊断模型。它没有进入最终精选，不是因为不重要，而是因为今天主线更偏控制、world model、RL 和数据基础设施；这篇更适合作为安全评测专题单独深读。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

### [W4]. World Action Models Enable Continual Imitation Learning with Recurrent Generative Replays [[HTML]](https://arxiv.org/html/2606.27374) [[PDF]](https://arxiv.org/pdf/2606.27374)
* **Paper ID**: `2606.27374`
* **Authors**: Manish Kumar Govind, Dominick Reilly, Smit Patel, Hieu Le, Srijan Das
* **Author Priority**: Standard
* **为什么还值得留意**: ReGen 值得跟踪，因为它把 WAM 的生成未来能力用于 continual imitation learning，用 pseudo-replay trajectories 代替存储旧任务原始示范，直接切中 catastrophic forgetting。它使用 Cosmos-Policy/Cosmos-Predict2-2B，并在仿真和真实 manipulation 中评估。未进最终精选，是因为当前摘录中的关键数字、任务细节和 pseudo-trajectory 质量边界不完整；相比 Tactile-WAM 和 world model 幻觉论文，它的证据链还需要 PDF 核查。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)
