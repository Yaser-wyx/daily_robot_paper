# RoboPulse | 2026-06-17

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 80 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线很清楚：VLA 正在从“更大模型+更多机器人轨迹”转向“从人类视频、传感器、世界模型反馈和评测诊断中提取可行动监督”。最终精选覆盖了六个互补切口：动作中心视觉预训练、World-Action 的在线 RL、自称面向规模化对齐的通用 Manipulation VLA、诊断型 benchmark、推理时视觉验证自改进，以及按需多模态感知。VIP 作者里，Yuke Zhu、Danfei Xu 参与的 CAIP 最值得优先看，因为它直接回答机器人视觉表征如何从人类视频获得动作偏置；Jiangmiao Pang 参与的 EBench 值得跟踪其 leaderboard 和任务 taxonomy；Dhruv Shah 的 VERITAS 虽只有摘要回退，但“visual verifier + inference-time steering”与具身策略自改进方向高度相关。整体看，今天的论文不是单点刷分，而是在补 VLA 部署链条里的几个缺口：数据、表征、反馈、诊断和安全置信度。

## 今日信号

- 人类第一视角视频正在从“辅助语义预训练”升级为“可抽取动作、手-物状态和交互结构的机器人监督来源”。
- World Model / World-Action Model 的重点开始从离线模仿转向在线交互、重建奖励、视频 SFT 与策略共同演化。
- VLA 评测与部署正在补上成功率之外的诊断、验证、传感器选择和不确定性机制，说明社区开始正视真实环境可靠性问题。

## Historical Rediscovery

- **Paper**: Retrieve, Don't Retrain: Extending Vision Language Action Models to New Tasks at Test Time [[HTML]](https://arxiv.org/html/2606.15631) [[PDF]](https://arxiv.org/pdf/2606.15631)
  - **Paper ID**: `2606.15631`
  - **来源日期**: 2026-06-16
  - **当时可能被低估的信号**: “retrieve, don't retrain”把新任务扩展从训练期改到测试期，并且历史备注中特别指出了 human-hand 与低成本 embodiment demonstration pool，这对现实部署的数据追加方式是具体信号。
  - **为什么现在值得再看**: 今天再看 VLA 时，部署期适配比单纯离线微调更关键；它和 VLA、cross-embodiment adaptation、真实机器人稳健性验证直接相关，尤其值得核查检索式任务进展估计是否能成为 World Action Model 的轻量外部记忆。
  - **建议动作**: 加入精读
  - **关键词**: `VLA` `test-time adaptation` `retrieval` `cross-embodiment` `deployment`
- **Paper**: PO-PDDL: Learning Symbolic POMDPs from Visual Demonstrations for Robot Planning Under Uncertainty [[HTML]](https://arxiv.org/html/2606.15654) [[PDF]](https://arxiv.org/pdf/2606.15654)
  - **Paper ID**: `2606.15654`
  - **来源日期**: 2026-06-16
  - **当时可能被低估的信号**: 备注里明确提到 partial observability、stochastic execution 和真实任务规划，这些比普通 LLM planner 更接近机器人闭环失败恢复问题。
  - **为什么现在值得再看**: 如果 VLA 要走向长时程操作，仅靠端到端动作生成很难处理不确定状态；这篇适合作为 VLA+planner、World Model 状态抽象、长期任务执行监控的连接点重新评估。
  - **建议动作**: 加入精读
  - **关键词**: `VLA` `POMDP` `planning under uncertainty` `long-horizon` `VLM`
- **Paper**: EgoPhys: Learning Generalizable Physics Models of Deformable Objects from Egocentric Video [[HTML]](https://arxiv.org/html/2606.16202) [[PDF]](https://arxiv.org/pdf/2606.16202)
  - **Paper ID**: `2606.16202`
  - **来源日期**: 2026-06-16
  - **当时可能被低估的信号**: 当时容易低估的是“egocentric video 到 deformable physics model”这个数据入口：它暗示可从非机器人或弱机器人视角构建可规划的物理模型。
  - **为什么现在值得再看**: World Model 和 Sim2Real 现在都需要更可靠的物理预测，尤其是绳、布、软物体等可变形任务；这篇可作为 VLA 外部物理模拟器或 action-conditioned planning substrate 的候选路线。
  - **建议动作**: 加入精读
  - **关键词**: `World Model` `Sim2Real` `deformable object` `egocentric video` `digital twin`
- **Paper**: GHOST: Hierarchical Sub-Goal Policies for Generalizing Robot Manipulation [[HTML]](https://arxiv.org/html/2606.10025) [[PDF]](https://arxiv.org/pdf/2606.10025)
  - **Paper ID**: `2606.10025`
  - **来源日期**: 2026-06-10
  - **当时可能被低估的信号**: 被低估的信号是 3D sub-goal 到 image-plane heatmap 的接口，它可能比纯语言或纯轨迹监督更适合把示范、视觉目标和控制器对齐。
  - **为什么现在值得再看**: 长时程操作和 World Action Model 都需要可复用的中间动作表征；GHOST 的层级子目标设计可为 VLA 的高层计划、低层控制解耦提供可操作参考。
  - **建议动作**: 快速浏览
  - **关键词**: `hierarchical manipulation` `VLA` `sub-goal policy` `imitation learning` `long-horizon`
- **Paper**: LeHome: A Simulation Environment for Deformable Object Manipulation in Household Scenarios [[HTML]](https://arxiv.org/html/2604.22363) [[PDF]](https://arxiv.org/pdf/2604.22363)
  - **Paper ID**: `2604.22363`
  - **来源日期**: 2026-04-27
  - **当时可能被低估的信号**: 当时可能被低估的是 household deformable tasks 这一场景缺口：可变形家居操作比常规刚体桌面任务更接近真实部署难点。
  - **为什么现在值得再看**: 你的兴趣里 Sim2Real、World Model 和真实部署评测都需要更难、更物理真实的环境；LeHome 可作为检验 VLA/WAM 是否真正理解可变形物理和长时程家居操作的候选 benchmark。
  - **建议动作**: 继续跟踪
  - **关键词**: `Sim2Real` `deformable manipulation` `household robotics` `benchmark` `World Model`

## Editor's Picks

### [1]. Contrastive Action-Image Pre-training for Visuomotor Control [[VIP]] [[HTML]](https://arxiv.org/html/2606.17256) [[PDF]](https://arxiv.org/pdf/2606.17256) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.17256`
* **Authors**: Yuvan Sharma, Dantong Niu, Anirudh Pai, Zekai Wang, Zhuoyang Liu, Baifeng Shi, Stefano Saravalle, Boning Shao, Ruijie Zheng, Jing Wang, Konstantinos Kallidromitis, Yusuke Kato, Fabio Galasso, Yuke Zhu, Danfei Xu, Linxi "Jim" Fan, Jitendra Malik, Trevor Darrell, Roei Herzig
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看：CAIP 直接把第一视角人类视频中的手部动作代理信号用于视觉编码器预训练，切中 VLA/visuomotor control 里“语义强但动作弱”的表征瓶颈。
* **关键词**: `action-centric representation` `egocentric video` `contrastive pretraining` `dexterous manipulation` `VLA encoder`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

#### 📖 背景与动机

机器人操控策略高度依赖视觉特征，但常用视觉 backbone 的预训练目标并不是为物理交互设计的。CLIP/SigLIP 一类模型擅长语义对齐，DINO 一类模型擅长几何和局部结构，但它们通常没有见过操控环境，也没有接受过动作监督；直接拿来做低层控制时，表征可能知道“这是什么”，却不一定知道“该如何推动、抓取或倾倒”。机器人轨迹最适合提供视觉-动作配对，但规模远小于互联网图文或视频数据。CAIP 的核心动机就是在不依赖海量机器人轨迹的前提下，从大规模 egocentric human video 中提取近似动作信号，把视觉表征往可控、可交互的方向推。它进入精选，是因为作者阵容包含 Yuke Zhu、Danfei Xu 等重点关注对象，且问题设定非常贴近 VLA 预训练的下一步：不是只学语义，而是学对动作有用的视觉表征。

#### ⚙️ 核心方法

CAIP 的方法可以理解为“动作-图像对比预训练”。当前 HTML 摘录明确给出的设计是：模型由 ViT 图像编码器、action transformer 和 attention pooling 组成，用人类第一视角视频中的手部姿态作为末端执行器动作的代理信号，将视觉观测与动作 chunk 通过 contrastive objective 对齐。这个设计的关键不在于把人手动作直接当机器人动作执行，而是在预训练阶段让视觉 encoder 对未来交互相关的手部运动、接触前状态和操作对象更敏感。相较于图文对比学习，它引入了物理行动维度；相较于纯机器人数据预训练，它利用了更大规模的人类视频；相较于只做视频自监督，它显式把视觉 embedding 与动作片段绑定。摘录还显示作者在下游只用较少任务演示从头训练策略，并把 CAIP encoder 与多类视觉预训练 baseline 比较。需要保守的是，HTML 摘录没有展开完整损失公式、负样本构造、动作 chunk 的具体时间窗口和手姿态抽取误差处理，因此这些细节应在 PDF 中优先核查。

#### 📊 实验与结果

实验分两块：下游真实机器人策略性能和 action retrieval 表征质量。真实平台是 Dexmate Vega 双臂操作器，配两只 22-DoF Sharpa Wave 灵巧手；视觉来自头部 ZED X Mini 双目相机和两台腕部 ZED X One S-Wide 单目相机。动作控制上，手臂使用末端 delta control，手指使用绝对关节控制。任务设置强调小数据和灵巧操作：每个任务仅 200 条示范，pour 任务为 150 条示范；共六个操控任务，每个任务 12 次评估。对比包括 R3M、MVP、DINOv2、SigLIP、SigLIP 2 等自监督、语言监督、视频和机器人预训练表征。结论摘录明确称模型在下游灵巧操作任务平均成功率达到 76%，优于标准语义或自监督预训练；但逐任务结果、方差、失败模式和统计显著性需要看正文表格与附录。

#### ⚠️ 风险 / 保留意见

- 手部姿态只是机器人末端动作的代理，跨手型、跨物体接触和力控信息可能存在系统偏差。
- 真实机器人评估任务数和 trial 数有限，76% 平均成功率需要结合逐任务难度、方差和 baseline 调参公平性判断。
- 预训练依赖大规模 egocentric video 与手姿态估计质量，复现成本和数据清洗细节可能是主要门槛。

#### 💭 结论与启发

CAIP 对后续选题的启发是：VLA 预训练未必只能扩大机器人轨迹，关键是找到能和机器人控制接口对齐的“动作代理信号”。如果我要复现或借鉴，优先不是复刻完整大规模训练，而是验证一个小规模版本：同一策略架构下，比较语义 encoder、自监督 encoder 和动作对齐 encoder 在接触敏感任务上的差异。系统设计上，它也提示视觉 backbone 不能只用分类或文本检索指标筛选，应该加入 action retrieval、接触前状态判别和低层控制成功率作为表征验收标准。

#### 🔎 读 PDF 先核查

- 手部姿态被转成 action chunk 的具体定义是什么，是否包含速度、相对位移或仅姿态序列？
- contrastive objective 的正负样本构造如何避免同一场景语义相似但动作不同的混淆？
- CAIP 的收益主要来自动作监督、第一视角操控域数据，还是更大的视频数据规模？

#### 📌 上传 PDF 后优先看

- 方法章节中的 action proxy 构造、action transformer 和 attention pooling 细节
- 真实机器人六个任务的逐任务成功率、失败案例和评估协议
- action retrieval 实验、消融实验和与 SigLIP/DINOv2/R3M 等 encoder 的公平对比

### [2]. WAM-RL: World-Action Model Reinforcement Learning with Reconstruction Rewards and Online Video SFT [[HTML]](https://arxiv.org/html/2606.17906) [[PDF]](https://arxiv.org/pdf/2606.17906) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.17906`
* **Authors**: Zezhong Qian, Xiaowei Chi, Yu Qi, Haozhan Li, Zhi Yang Chen, Shanghang Zhang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看：WAM-RL 把 World-Action Model 从纯专家轨迹监督推进到在线 RL 与视频 SFT 联合优化，是今天最贴近 World Model + RL + VLA 交叉点的论文。
* **关键词**: `World-Action Model` `reinforcement learning` `online video SFT` `reconstruction reward` `LIBERO`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

World-Action Model 的吸引力在于，它不只是从图像直接回归动作，而是同时建模未来视觉动态和动作，从而给长时程决策提供更强的预测结构。已有 WA 模型在泛化和数据效率上有潜力，但多数仍依赖专家轨迹监督训练，这会带来两个问题：第一，策略被限制在示范分布内，遇到细粒度控制或需要探索的操作时难以超越老师；第二，模型部署后不能从自己的交互经验中持续改进。对机器人来说，这个限制很关键，因为真实任务中的摩擦、遮挡、接触误差和长时程累积偏差经常不在示范覆盖范围内。WAM-RL 的动机就是把 WA 的世界模型和动作模型放进在线交互闭环里，让视觉预测与动作选择共同演化，而不是把世界模型当固定特征或固定视频生成器。

#### ⚙️ 核心方法

根据 HTML 摘录，WAM-RL 基于 Genie Envisioner-ACT 架构实现：world model 是 DiT-based video generator，actor 消费其中间 latent features 并输出动作。训练框架包含两条耦合更新路径：actor 通过 reinforcement learning 优化，奖励来自 reconstruction-based rewards；world model 则用在线交互中成功轨迹进行 video SFT。作者还加入 KL regularization 来稳定 world model 的 latent space。这个设计的新意在于它没有只做 actor-only RL，也没有只把世界模型离线微调，而是让“预测未来视觉”与“选择动作”通过在线数据互相校正：成功轨迹提高视频模型对当前策略分布的建模能力，更新后的 latent 又反过来为 actor 提供更贴近实际交互的状态表示。当前摘录只能确认这些模块级设计，不能确认重建奖励的精确定义、成功轨迹筛选标准、RL 算法类型、KL 项形式或在线采样预算；这些都需要 PDF 正文核查。

#### 📊 实验与结果

实验在 LIBERO 和 RLBench 上进行，摘录明确提到 LIBERO-Object 以及 RLBench 的 Water Plants 任务。训练实现使用 8 张 NVIDIA A800 GPU，在混合在线 RL 和视频 fine-tuning 设置下训练 8 小时。对比基线包括未加 RL 的 pretrained WA model，即 Base，以及 actor-only reinforcement learning 等方案。评价意图是验证联合优化是否改善细粒度控制和长时程表现，并分析 world model 与 actor 是否需要共同更新。结论声称重建奖励和在线 video SFT 使两个组件共同演化，提升 fine-grained control 与 long-horizon performance；但摘录没有给出具体成功率、提升百分比或误差条，因此不能写成定量胜出，只能表述为作者报告了相对改进趋势。

#### ⚠️ 风险 / 保留意见

- 当前证据主要来自模拟 benchmark，真实机器人交互中的在线 RL 成本、安全约束和失败恢复没有在摘录中得到确认。
- reconstruction reward 可能鼓励视觉可重建性而非任务完成，奖励与真实控制目标的一致性需要仔细检查。
- world model 在线 SFT 只使用成功轨迹可能带来选择偏差，失败经验如何利用仍不清楚。

#### 💭 结论与启发

这篇最值得带着“RL 如何接入 VLA/WA”去读。它提示一个系统设计方向：不要把 world model 只当 planning 前端，也不要把 RL 只接在动作头上，而是让预测模型持续适应策略访问到的新状态分布。复现时我会先做小规模 ablation：固定 world model、只训 actor、只做 video SFT、联合训练四种设置，观察长时程任务中的误差累积。若重建奖励确实有效，它可能成为缺少稠密任务奖励时训练 WA/VLA 的实用桥梁，但必须核查奖励是否真的和成功率相关。

#### 🔎 读 PDF 先核查

- reconstruction-based reward 是基于未来帧重建误差、latent consistency，还是与目标状态相关的视觉指标？
- online video SFT 只采用成功轨迹时，失败轨迹是否完全丢弃，是否影响探索效率？
- 联合更新 world model 和 actor 的稳定性如何，KL regularization 的权重和作用是否有消融支持？

#### 📌 上传 PDF 后优先看

- 方法章节中 reconstruction reward、online video SFT 和 KL regularization 的精确定义
- LIBERO-Object 与 RLBench Water Plants 的对比表、训练曲线和 ablation
- 失败案例分析，尤其是 actor-only RL 与 joint WAM-RL 的差异

### [3]. Qwen-RobotManip Technical Report: Alignment Unlocks Scale for Robotic Manipulation Foundation Models [[PDF]](https://arxiv.org/pdf/2606.17846) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.17846`
* **Authors**: Haoqi Yuan, Zhixuan Liang, Anzhe Chen, Ye Wang, Haoyang Li, Pei Lin, Yiyang Huang, Zixing Lei, Tong Zhang, Jiazhao Zhang, Jie Zhang, Jingyang Fan, Gengze Zhou, Qihang Peng, Chenxu Lv, Xiaoyue Chen, An Yang, Fei Huang, Junyang Lin, Dayiheng Liu, Jingren Zhou, Chenfei Wu, Xiong-Hui Chen
* **Author Priority**: Standard
* **一句话结论**: 值得优先看但要保守：Qwen-RobotManip 声称用 representation、motion、behavior 三层 alignment 解锁机器人操控规模化训练，主题重要，但当前只有摘要回退信息。
* **关键词**: `Qwen-VL` `robot manipulation foundation model` `data alignment` `multi-source training` `VLA scaling`
* **证据来源**: Abstract fallback

#### 📖 背景与动机

这篇的出发点是把语言和多模态 foundation model 的 scaling recipe 迁移到机器人操控：在文本领域，统一表示和大规模异构数据训练已经反复证明有效；但机器人数据天然更碎片化，体现在 embodiment、动作空间、任务语义、采集质量和行为分布都不一致。直接把多源数据混在一起，可能不是规模化，而是相互冲突。VLA 领域现在的核心难题之一，就是如何让来自不同机器人、不同控制频率、不同任务脚本和不同语言标注的数据进入同一个训练目标。Qwen-RobotManip 的摘要称其基于 Qwen-VL，提出跨 representation、motion 和 behavioral dimensions 的 unified alignment framework，使多源训练从冲突变得 coherent。它进入精选，是因为它代表大模型团队推进机器人 foundation model 的方向，虽然目前证据只来自摘要，必须避免过度解读。

#### ⚙️ 核心方法

当前摘录只能确认 Qwen-RobotManip 是一个建立在 Qwen-VL 之上的 generalizable Vision-Language-Action foundation model，并且核心方法被概括为三类 alignment：representation alignment、motion alignment 和 behavioral alignment。合理推断上，representation alignment 可能处理视觉、语言和机器人状态/动作 token 的统一接口；motion alignment 可能处理不同机器人控制空间、轨迹粒度或动作参数化的差异；behavioral alignment 可能处理不同数据源任务意图、示范质量和策略行为分布的兼容。但这些只是基于摘要措辞的趋势判断，不能当作论文已确认细节。摘要还强调 alignment 让模型能吸收此前难以规模化整合的 manipulation data，但没有给出架构图、训练目标、数据混合策略、动作 token 化方式或推理流程。读 PDF 时应重点验证它是否提出了可复用的技术接口，还是更多是一份大规模系统报告。

#### 📊 实验与结果

由于 HTML 不可用，当前只能依据摘要回退信息。摘要称论文研究 scaling recipe 是否能用于 robotic manipulation，并声称 Qwen-RobotManip 通过统一 alignment framework 实现更强泛化，但没有提供可引用的 benchmark 名称、任务数量、成功率、真实机器人设置、对比模型或消融数字。因此这里不能写具体实验结果。能确认的是，作者把实验目标定位为验证“alignment unlocks scale”，即多源操控数据在统一 formulation 下是否能带来真正 generalization。需要在 PDF 中核查：它是否覆盖模拟与真实机器人、是否有跨 embodiment 或跨任务泛化评估、是否有 alignment 组件消融，以及是否和 OpenVLA、RT-X、π0/π0.5 或同类 VLA 做公平对比。

#### ⚠️ 风险 / 保留意见

- 当前只有摘要回退，所有架构、数据和实验细节都需要 PDF 验证，不能提前采信技术主张。
- 大规模系统报告容易把收益混合在模型规模、数据规模、数据清洗和 alignment 设计中，归因风险较高。
- 如果未公开数据、训练细节或评估协议，复现和横向比较会比较困难。

#### 💭 结论与启发

这篇的阅读价值在于判断“大模型式 alignment”是否正在成为机器人操控 foundation model 的主叙事。如果方法细节扎实，它可能提供一套处理异构机器人数据的工程范式：先统一表征，再统一运动接口，最后校准行为分布。对后续选题来说，我会把它作为与 ACE-Ego-0、CAIP 对照的一类路线：前者偏多源机器人/操控 alignment，后两者偏从人类视频抽取可用监督。真正值得复现的不是完整 Qwen 规模，而是其中能否拆出小模型也有效的 alignment module。

#### 🔎 读 PDF 先核查

- representation、motion、behavior 三类 alignment 分别对应哪些具体模块、损失或数据处理流程？
- 性能提升能否通过 alignment 消融证明，而不是仅由模型规模或数据规模解释？
- 评估是否包含跨 embodiment、跨场景和真实机器人泛化，还是主要在已有数据分布内验证？

#### 📌 上传 PDF 后优先看

- 技术报告中的 alignment framework 总览和动作表示章节
- 数据来源、数据清洗、混合比例和训练 recipe
- benchmark 对比、跨域泛化实验和 alignment ablation

### [4]. EBench: Elemental Diagnosis of Generalist Mobile Manipulation Policies [[VIP]] [[HTML]](https://arxiv.org/html/2606.18239) [[PDF]](https://arxiv.org/pdf/2606.18239) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.18239`
* **Authors**: Ning Gao, Jinliang Zheng, Xing Gao, Haoxiang Ma, Hanqing Wang, Yukai Wang, Jiantong Chen, Zanxin Chen, Shujie Zhang, Mingda Jia, Xuekun Jiang, Zihou Zhu, Xinyu Li, Shuai Wang, Hao Li, Wenzhe Cai, Yuqiang Yang, Xudong Xu, Zhaoyang Lyu, Yao Mu, Tai Wang, Jiangmiao Pang, Jia Zeng, Weinan Zhang, Chunhua Shen
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看：EBench 不是又一个单纯刷成功率的 benchmark，而是用能力维度和泛化维度诊断 generalist mobile manipulation policy 的强弱结构。
* **关键词**: `benchmark` `mobile manipulation` `capability diagnosis` `generalization` `VLA evaluation`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

#### 📖 背景与动机

当前通用操控策略越来越常用一个总体 success rate 来宣称进步，但这个数字经常掩盖模型真实能力画像：一个模型可能擅长移动抓取，却在高精度插入上失败；另一个模型可能 tabletop 表现好，但移动长时程任务崩溃。已有 RLBench、CALVIN、LIBERO 等更偏固定场景或特定任务族，RoboCasa、RoboTwin、GenManip 扩大了任务和 embodiment 覆盖，但仍可能各自集中在单一 regime。EBench 的动机是把 mobile manipulation、long-horizon、dexterous-and-precise 放在同一协议下，并用 capability tags 和 generalization dimensions 拆开看。它进入精选，一方面因为 Jiangmiao Pang 在核心优先作者名单中，另一方面因为 VLA 研究已经需要更细的诊断工具来解释“为什么某个 generalist policy 看起来强但部署不稳”。

#### ⚙️ 核心方法

EBench 的方法贡献主要是 benchmark 设计和诊断协议。HTML 摘录明确说明它包含 26 个 manipulation tasks，并标注 5 个 capability dimensions 与 4 个 generalization dimensions。任务被组织为三类：Mobile Pick-and-Place 共 10 个移动任务，Mobile Long-Horizon 共 9 个多阶段移动序列，Table-Top Dexterous-and-Precise 共 7 个固定基座任务，覆盖亚厘米级插入、对齐和双手协调等精细能力。所有任务共享一个双臂移动底盘机器人的统一动作空间：每只手臂可以用 6-DoF joint position 或 6-DoF end-effector pose 控制，并配每臂 gripper width，底盘则接受平面速度和 yaw rate。更重要的是，它不是只报告总分，而是通过 scene、atomic skill、temporal horizon、precision、operating mode 等标签支持能力切片查询，避免容易任务的多数类表现掩盖弱项。摘录还提到测试资产池与训练池 disjoint，强调泛化评估。

#### 📊 实验与结果

实验评估了若干 state-of-the-art generalist manipulation models，摘录中明确出现 XVLA 和 InternVLA-A1，另有部分模型名在 HTML 抽取中缺失。作者报告的关键现象是：总成功率接近的模型可能呈现完全不同的能力 profile；某模型获得最高 test success rate 和最好 train-test retention，而 InternVLA-A1 在 mobile manipulation 上占优，但在 dexterous 相关能力上出现明显退化。EBench 还配套由两条路线合成的数据：精细桌面任务使用 teleoperation，移动和长时程任务使用 key-frame poses 与 cuRobo。由于摘录中若干成功率、步数和具体模型名缺失，不能引用更细数字；但可以确认其证据重心是用分维度诊断揭示总体 success rate 看不到的能力差异。

#### ⚠️ 风险 / 保留意见

- 作为 simulation benchmark，能否预测真实移动双臂平台部署表现还需要真实机器人验证。
- 任务 taxonomy 很有价值，但标签设计可能影响诊断结论，需要检查标注一致性和任务难度均衡。
- 如果 leaderboard 模型训练数据与测试任务存在间接重叠，泛化结论需要额外审慎。

#### 💭 结论与启发

EBench 的价值不是告诉我哪个 VLA 最强，而是提供一种读 VLA 结果的方式：把总成功率拆成任务族、精度、时长、移动性和技能原子。后续做系统评估时，可以借鉴这种 capability-profile 报告，把模型缺陷定位到“移动底盘控制”“双臂协调”“长时程恢复”或“高精度对齐”上。对论文阅读也有帮助：当某篇 VLA 声称 generalist manipulation 时，我会反问它是否跨越了 EBench 这类维度，而不是只在 tabletop pick-place 上泛化。

#### 🔎 读 PDF 先核查

- 5 个 capability dimensions 和 4 个 generalization dimensions 的具体定义是否足够互斥且可复用？
- 训练资产池与测试资产池 disjoint 的构造方式能否真正避免视觉和任务语义泄漏？
- 模型能力差异是否来自策略本身，还是与动作接口、控制频率和任务族数据量相关？

#### 📌 上传 PDF 后优先看

- 任务设计与 taxonomy 章节，尤其是 26 个任务和标签定义
- 模型对比的分维度结果表、train-test retention 和 capability profile 可视化
- 数据生成流程、cuRobo/key-frame/teleoperation 设置与泛化划分

### [5]. Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement [[VIP]] [[PDF]](https://arxiv.org/pdf/2606.18247) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.18247`
* **Authors**: Mingtong Zhang, Dhruv Shah
* **Author Priority**: Extended VIP
* **一句话结论**: 值得优先看但需等 PDF 验证：VERITAS 用 visual verifier 做推理时 steering 和自生成轨迹改进，抓住了 generalist policy 部署后自我提升的问题。
* **关键词**: `visual verifier` `inference-time steering` `self-improvement` `generalist policy` `offline fine-tuning`
* **证据来源**: Abstract fallback

#### 📖 背景与动机

通用机器人策略在真实世界里不应该是一次训练后静态部署，因为环境、物体、视角和执行误差都会持续变化。要让机器人越用越好，需要两个机制：一是在执行时判断候选动作是否可靠，二是把自己的成功经验变成后续训练数据。很多 VLA/generalist policy 直接从观测生成动作，缺少显式反馈环；而在线收集人工示范又昂贵。VERITAS 的摘要提出 generator-verifier 框架：用预训练 generalist robot policy 作为 generator，再配一个 gradient-free visual verifier 在推理时评估动作。它进入精选，是因为 Dhruv Shah 属于扩展关注作者，且该思路与 inference-time compute、policy steering、self-improvement 三条趋势相交。当前只有摘要回退，因此必须把它视作高潜力方向，而非已充分验证的系统。

#### ⚙️ 核心方法

当前摘录只能确认 VERITAS 是一个 generator-verifier framework。generator 是预训练 generalist robot policy，负责产生候选动作或 rollout；visual verifier 是 gradient-free 的，在 inference time 对动作进行评估，从而实现不额外训练的 policy steering。摘要还说明，经过 verifier 筛选或引导的 rollout 可以作为 supervision，用于 offline policy improvement；也就是说，它不仅在推理时改善当次执行，还把 verified self-generated trajectories 回流给策略微调。这里的关键概念是把“视觉验证”变成可插拔反馈模块：不一定改动原始策略参数，也不一定需要人工标签，就能在候选行为之间做选择。需要保守的是，摘要没有说明 verifier 的输入是预测图像、执行后图像、目标图像还是视频片段；也没有说明候选动作如何采样、验证分数如何定义、是否需要语言目标，以及 offline improvement 的训练数据过滤准则。

#### 📊 实验与结果

摘要声称 inference-time verification consistently outperforms vanilla generalists without training on additional demonstration data，并且 verified rollouts 能为 offline policy improvement 提供有效监督，使微调后的策略受益于 self-generated trajectories。除此之外，当前没有 HTML，无法确认 benchmark、机器人平台、任务数量、baseline 名称、提升幅度、trial 数或失败类型。实验解读必须因此保守：可以说作者报告了推理时 steering 与离线自改进两类收益，但不能写具体数字或断言跨真实机器人充分成立。上传 PDF 后，应重点检查它是否在真实机器人、模拟环境或两者中验证；是否只改善短时选择，还是能处理长时程连锁错误；以及 verifier 本身是否引入额外标注、训练或目标图像需求。

#### ⚠️ 风险 / 保留意见

- 只有摘要回退，verifier 的形式、输入、计算成本和适用任务范围都不明确。
- 推理时生成多个候选再验证可能增加延迟，真实机器人闭环控制中是否可用需要确认。
- self-generated trajectories 可能放大 verifier 偏差，若验证标准不稳，离线微调会积累错误监督。

#### 💭 结论与启发

VERITAS 的启发是，VLA 改进不一定只发生在训练前或训练中，也可以发生在 inference time。对系统设计来说，一个外置 verifier 可以成为连接部署、数据筛选和策略微调的中间层：先在执行时减少明显坏动作，再把高置信成功轨迹写回 replay buffer。后续如果我要做相关复现，会先从低成本任务做候选动作重排序，验证视觉分数是否真的和成功率相关，再考虑离线自训练。它也提醒我关注 verifier 的偏差控制，否则自改进会变成自我确认。

#### 🔎 读 PDF 先核查

- visual verifier 具体验证什么信号，是目标达成、轨迹可行性、视觉预测一致性，还是动作后状态评分？
- generator 产生多少候选动作或 rollout，推理时 steering 的计算成本是否适合真实机器人闭环？
- verified self-generated trajectories 用于离线微调时，如何避免 verifier 偏差和分布坍缩？

#### 📌 上传 PDF 后优先看

- VERITAS 框架图和 visual verifier 定义章节
- inference-time steering 的候选生成、评分和选择流程
- offline policy improvement 实验、数据过滤规则和失败案例

### [6]. MuseVLA: An Adaptive Multimodal Sensing Vision-Language-Action Model for Robotic Manipulation [[HTML]](https://arxiv.org/html/2606.17598) [[PDF]](https://arxiv.org/pdf/2606.17598) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.17598`
* **Authors**: Xingyuming Liu, Ruichun Ma, Heyu Guo, Qixiu Li, Qingwen Yang, Lin Luo, Shiqi Jiang, Chenren Xu, Jiaolong Yang, Baining Guo
* **Author Priority**: Standard
* **一句话结论**: 值得优先看：MuseVLA 把传感器当作按需调用的工具，而不是把所有模态无脑融合，适合关注真实操控中 RGB 不足的问题。
* **关键词**: `multimodal sensing` `sensor tool use` `grounded sensor image` `dexterous manipulation` `adaptive VLA`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

大多数 VLA 以 RGB 或 RGB-D 为主要输入，但真实操控里很多关键信息并不稳定地出现在可见光图像中，例如温度、声音、雷达反射或材料属性。人类并不会时时刻刻融合所有感官，而是根据任务选择需要的感知工具：找热物体时看温度，定位声源时听声音，判断遮挡或反射时可能需要其他传感器。机器人如果只依赖 RGB，就容易在“看起来相似但物理属性不同”的任务上失败。MuseVLA 的动机是把多模态传感器集成进 VLA，但采用 on-demand tool use 的方式：先判断该调用哪个传感器、关注什么目标，再把异构测量转成统一中间表示供动作生成。它进入精选，是因为它扩展了 VLA 的感知边界，直接面向真实部署中 RGB 不可观测属性的问题。

#### ⚙️ 核心方法

MuseVLA 的核心流程在摘录中相对清楚：给定任务指令和视觉上下文，模型先生成 sensor token 和 target description，用来选择要调用的传感器模态以及应该关注的目标；随后把所选传感器的测量转换为 grounded sensor image，作为统一的中间表示进行多模态融合和动作生成。这个设计把传感器接入拆成两个层次：决策层负责“何时用什么传感器、看哪里”，表示层负责“把热成像、毫米波雷达、声音强度等异构读数变成模型能处理的图像式表示”。相较于简单 early fusion，它减少了无关模态常驻输入带来的开销；相较于为每个传感器定制动作模型，它用 grounded sensor image 做统一接口。摘录还提到有数据合成 pipeline，可用 grounded sensor images 增强已有 RGB videos，降低大规模多传感器机器人数据采集需求。需要核查的是 sensor token 的训练标签来源、target description 如何 grounding、合成 sensor image 的物理真实性以及动作模型和基础 VLA 的结合方式。

#### 📊 实验与结果

实验覆盖三类问题：需要多模态输入的操控任务成功率、adaptive sensor selection 的性能与效率、以及合成数据预训练对 unseen tasks 的泛化收益。真实平台是桌面机器人，配 12-DoF Robotera XHand 灵巧手和传感器套件，包括 Intel RealSense RGB-D 相机、两台 infiRay T2S 热成像相机、Calterah 4T4R 60GHz 毫米波雷达和 Sipeed 6+1Mic 麦克风阵列。每个传感器都提供与 RGB 视场对齐的 2D heatmap，例如温度热图、反射强度热图和声音强度热图。示范数据通过 MANUS5 手套遥操作采集，并记录动作序列与所有传感器测量。摘录未给出具体成功率数字、任务完整列表或 baseline 结果，因此只能确认评估维度和平台，而不能引用定量提升。

#### ⚠️ 风险 / 保留意见

- grounded sensor image 把异构传感器图像化，可能丢失时序、频谱或三维结构等原始信息。
- 多传感器标定、视场对齐和噪声建模会强烈影响效果，真实部署复现难度较高。
- 合成 sensor data 的泛化能力需要谨慎验证，尤其是温度、声音和雷达读数是否物理可信。

#### 💭 结论与启发

MuseVLA 的最大启发是把传感器选择建模成 tool call，而不是把多模态融合当固定输入拼接。对机器人系统设计来说，这很实用：传感器可以按任务付费调用，模型也能输出目标描述帮助定位采样区域。后续我会重点看它是否真的学会了“何时不用传感器”，因为效率和鲁棒性同样重要。若方法成立，可以推广到触觉、力矩、气味或专业检测仪器，让 VLA 从视觉语言动作模型变成可扩展的感知-动作平台。

#### 🔎 读 PDF 先核查

- sensor token 和 target description 的监督信号如何构造，是否需要人工标注传感器选择？
- grounded sensor image 是否只是 aligned heatmap，还是包含目标区域、语义 mask 或传感器置信度？
- 合成数据预训练对 unseen tasks 的收益是否来自传感器推理能力，还是来自额外数据量？

#### 📌 上传 PDF 后优先看

- 方法章节中的 sensor token、target description 和 grounded sensor image 定义
- 多传感器平台、标定方式和数据采集流程
- adaptive sensor selection、效率消融和 unseen task 泛化实验

## Watchlist

### [W1]. ACE-Ego-0: Unifying Egocentric Human and Robotic Data for VLA Pretraining [[HTML]](https://arxiv.org/html/2606.17200) [[PDF]](https://arxiv.org/pdf/2606.17200)
* **Paper ID**: `2606.17200`
* **Authors**: Hao Li, Ganlong Zhao, Yufei Liu, Haotian Hou, Guoquan Ye, Tongyan Fang, Chunxiao Liu, Siyuan Huang, Jianbo Liu, Xiaogang Wang, Hongsheng Li
* **Author Priority**: Standard
* **为什么还值得留意**: ACE-Ego-0 进入 watchlist 是因为它和今天的人类 egocentric video + robot data 统一预训练主线高度相关，且提出 camera-space actions、cross-embodiment morphology tokens、time-aligned action chunking 等用于处理异构数据的接口。它没有进入最终精选，主要是因为今天同类方向里 CAIP 的动作中心视觉预训练更聚焦，且有核心 VIP 作者；ACE-Ego-0 更像大系统型 VLA pretraining，需要等 PDF 核查统一动作表示和真实机器人六任务结果的细节。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. EgoInfinity: A Web-Scale 4D Hand-Object Interaction Data Engine for Any-View Robot Retargeting and Video-to-Action Robot Learning [[HTML]](https://arxiv.org/html/2606.17385) [[PDF]](https://arxiv.org/pdf/2606.17385)
* **Paper ID**: `2606.17385`
* **Authors**: Gaotian Wang, Kejia Ren, Andrew Morgan, Yiting Chen, Howard H. Qian, Podshara Chanrungmaneekul, Kaiyu Hang
* **Author Priority**: Standard
* **为什么还值得留意**: EgoInfinity 值得放入 watchlist，因为它尝试把纯 RGB 互联网视频转换成 4D 手-物交互、6-DoF 物体状态和可 retarget 的机器人数据，正好补 VLA 数据规模瓶颈。它未进最终精选，是因为当前摘录显示更多是数据引擎和 retargeting pipeline，机器人学习闭环证据还需要看 106 个处理视频、真实执行和学习实验的具体质量。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. ThinkingVLA: Interleaved Vision and Language Reasoning for Robotic Manipulation [[PDF]](https://arxiv.org/pdf/2606.17937)
* **Paper ID**: `2606.17937`
* **Authors**: Tianyi Lu, Hui Zhang, Zijie Diao, Junke Wang, Shengqi Xu, Xingyao Lin, Guojin Zhong, Ziyi Ye, Peng Wang, Zuxuan Wu, Yu-Gang Jiang
* **Author Priority**: Standard
* **为什么还值得留意**: ThinkingVLA 进入 watchlist 是因为它把 manipulation planning 拆成 next visual state prediction 和 inverse dynamics，并尝试用交错视觉-语言生成做显式推理，方向上贴近 reasoning VLA。它没有进入最终精选，主要因为只有摘要回退，Mixture-of-Experts 架构、训练目标、视觉 token 生成和实验结果都无法从当前摘录确认。
* **证据来源**: Abstract fallback

### [W4]. Uncertainty Quantification for Flow-Based Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2606.18043) [[PDF]](https://arxiv.org/pdf/2606.18043)
* **Paper ID**: `2606.18043`
* **Authors**: Ralf Römer, Maximilian Seeliger, Saida Liu, Ben Sturgis, Marco Bagatella, Daniel Marta, Andreas Krause, Angela P. Schoellig
* **Author Priority**: Standard
* **为什么还值得留意**: Uncertainty Quantification for Flow-Based VLA Models 很值得跟踪，因为它面向部署可靠性，提出 VFD 估计 epistemic uncertainty，并用 SAVE 做主动微调；摘录还明确声称相比不确定性 baseline 至少减少 22 的数据收集量。它未进最终精选，是因为今天最终主线更偏 VLA/WA 模型能力构建，而这篇更偏可靠性与主动学习工具；不过在真实部署和安全筛选方向应优先补读。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
