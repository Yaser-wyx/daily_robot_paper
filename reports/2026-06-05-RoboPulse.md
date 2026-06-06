# RoboPulse | 2026-06-05

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 82 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线很清晰：VLA 后训练、闭环评估、可扩展推理和 World/World-Action Model 正在从“能跑 benchmark”转向“能解释、能提速、能进入真实控制回路”。最终精选保留了六篇互补论文：FlowPRO 代表无奖励偏好优化，PiL-World 代表 policy-in-the-loop 世界模型评估，WLA/MPCoT/TempoVLA 分别切入统一世界-语言-动作建模、测试时 latent reasoning、速度可控执行，Flash-WAM 则解决 WAM 实时化瓶颈。今天最终精选里没有核心 VIP 作者，但 watchlist 中 LadderMan 同时出现 Pieter Abbeel 与 Yue Wang，TAM 出现 Dieter Fox，值得作为 Sim2Real 与全身控制方向的优先跟踪对象。整体看，VLA 的竞争焦点正在从单步动作预测转向后训练数据构造、闭环想象 rollout、动作条件世界建模和部署时可控性。

## 今日信号

- VLA 后训练正在绕开奖励函数与 critic，转向偏好对、失败干预和 proximal 约束这类更贴近真实机器人采集成本的信号。
- World Model/WAM 的价值不再只是生成未来图像，而是被重新包装成闭环评估、动作推理、测试时扩展和实时控制接口。
- 速度、延迟和行动节奏开始成为 VLA 论文的一等问题，说明部署可控性正在进入模型结构与训练目标本身。

## Historical Rediscovery

- **Paper**: CLAW: Learning Continuous Latent Action World Models via Adversarial Latent Regularization [[HTML]](https://arxiv.org/html/2606.04130) [[PDF]](https://arxiv.org/pdf/2606.04130)
  - **Paper ID**: `2606.04130`
  - **来源日期**: 2026-06-04
  - **当时可能被低估的信号**: 当时可能低估了“adversarial latent regularization + action-free video + controllability benchmark”这个组合，因为它不是大规模真实机器人/VLA 部署论文，但它针对的是 WAM 能否从视频中学出可控动作变量的核心瓶颈。
  - **为什么现在值得再看**: 如果现在关注 RL+VLA、world-action reasoning 或用互联网/机器人视频做可规划表征，这篇比普通视觉表示学习更值得重看；重点应判断 latent action 是否能成为后续机器人控制或 VLA 后训练的中间接口。
  - **建议动作**: 加入精读
  - **关键词**: `World Model` `World Action Model` `latent action` `action-free video` `controllability`
- **Paper**: WAM-Nav: Asymmetric Latent World-Action Modeling for Unified Visual Navigation [[HTML]](https://arxiv.org/html/2606.04907) [[PDF]](https://arxiv.org/pdf/2606.04907)
  - **Paper ID**: `2606.04907`
  - **来源日期**: 2026-06-04
  - **当时可能被低估的信号**: 当时因为任务域偏 navigation、训练依赖仿真导航数据而降级，但“asymmetric action-foresight design”和 zero-shot real-world navigation 的线索可能对移动操作和 embodied policy 有迁移价值。
  - **为什么现在值得再看**: World Action Model 不一定只从 manipulation 起步；导航中的 action-conditional foresight、实时性和真实部署评测，可能给长时程 VLA/移动操作提供可借鉴的架构信号。
  - **建议动作**: 快速浏览
  - **关键词**: `World Action Model` `visual navigation` `latent foresight` `real-world navigation` `long-horizon`
- **Paper**: 3DThinkVLA: Endowing Vision-Language-Action Models with Latent 3D Priors via 3D-Thinking-Guided Co-training [[HTML]](https://arxiv.org/html/2606.04436) [[PDF]](https://arxiv.org/pdf/2606.04436)
  - **Paper ID**: `2606.04436`
  - **来源日期**: 2026-06-04
  - **当时可能被低估的信号**: 当时主要被 LIBERO、SimplerEnv 等模拟 benchmark 证据拖低优先级，但“3D foundation model 蒸馏、reasoning anchor token、zero-shot transfer”这些设计正好对应 VLA 空间泛化短板。
  - **为什么现在值得再看**: 当前 VLA 的瓶颈之一仍是空间理解和跨场景泛化；这篇值得用 benchmark audit 的视角重看，判断其 3D prior 是否只是 benchmark 增益，还是能成为 Sim2Real VLA 表征模块。
  - **建议动作**: 加入精读
  - **关键词**: `VLA` `3D priors` `spatial reasoning` `Sim2Real` `zero-shot transfer`
- **Paper**: What Are We Actually Benchmarking in Robot Manipulation? [[HTML]](https://arxiv.org/html/2606.04233) [[PDF]](https://arxiv.org/pdf/2606.04233)
  - **Paper ID**: `2606.04233`
  - **来源日期**: 2026-06-04
  - **当时可能被低估的信号**: 当时可能因“不提出新 VLA/WAM 系统”而低估，但它提供的是评估可信度过滤器，尤其能约束对高分 VLA、3D-VLA、Sim2Real 结果的解读。
  - **为什么现在值得再看**: 今天再看任何依赖仿真 benchmark 的 VLA、RL+VLA 或 world model 论文，都需要先知道哪些分数可能不代表真实部署能力；它和真实部署评测强相关。
  - **建议动作**: 加入精读
  - **关键词**: `benchmark audit` `VLA evaluation` `Sim2Real` `real deployment` `manipulation benchmarks`
- **Paper**: Wiggle and Go! System Identification for Zero-Shot Dynamic Rope Manipulation [[HTML]](https://arxiv.org/html/2604.22102) [[PDF]](https://arxiv.org/pdf/2604.22102)
  - **Paper ID**: `2604.22102`
  - **来源日期**: 2026-04-27
  - **当时可能被低估的信号**: 当时因为任务域偏动态绳索而被视为支线，但“高风险操作前主动辨识环境/物体动力学”的思想，比单任务技巧更接近可部署机器人策略需要的闭环世界建模。
  - **为什么现在值得再看**: 对 Sim2Real、World Model 和长时程真实操作来说，关键不只是离线学模型，而是部署时如何用少量交互更新可控动力学假设；这篇可作为 WAM/VLA 真实闭环前的实用参照。
  - **建议动作**: 继续跟踪
  - **关键词**: `Sim2Real` `system identification` `world-aware control` `deformable manipulation` `closed-loop probing`

## Editor's Picks

### [1]. FlowPRO: Reward-Free Reinforced Fine-Tuning of Flow-Matching VLAs via Proximalized Preference Optimization [[HTML]](https://arxiv.org/html/2606.05468) [[PDF]](https://arxiv.org/pdf/2606.05468) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.05468`
* **Authors**: Yihao Wu, He Zhang, Junbo Tan, Xueqian Wang, Zhengyou Zhang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为 FlowPRO 直接瞄准真实机器人 VLA 后训练的核心痛点：不用显式奖励和 critic，也能利用失败偏好改进 flow-matching action head。
* **关键词**: `VLA 后训练` `flow matching` `preference optimization` `reward-free RL` `real-robot bimanual`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

VLA 已经成为通用机器人策略的重要范式，但从可演示到可部署之间仍有明显鸿沟。SFT 和 DAgger 能扩展到真实硬件，却往往只间接利用失败信息；基于奖励的 RL 又受限于真实任务奖励设计和 critic 可靠性。FlowPRO 的重要性在于它把问题落到 flow-matching VLA 的后训练：如何在不写奖励、不训练显式价值模型的情况下，把 teleoperation 中的成功、失败、回滚和偏好信号变成稳定的策略改进。对长时程双臂任务来说，这比单纯扩大演示数据更贴近部署瓶颈。

#### ⚙️ 核心方法

FlowPRO 的核心是 RPRO，即面向 flow-matching action head 的 Robotic Flow-matching Proximalized Preference Optimization。摘录显示，作者从 RLHF、DPO、PRO 的理论出发，指出普通 DPO 只约束 preferred 与 dispreferred action 的相对似然，可能出现两者似然一起下降的 underdetermination，从而形成无显式奖励下的 reward-hacking 类失败。RPRO 将 preference objective 拆成 contrastive optimizer 与显式 proximal regularizer，使策略既能拉开偏好动作对，又避免偏离参考策略过远。数据侧，FlowPRO 结合 teleoperated intervention-and-rollback paradigm，并提出 state-wise Smooth Interpolation 来构造偏好数据，而不是只做 trajectory-wise preference contrast。整体流程是先训练 base SFT policy 作为 frozen reference，再用干预/回滚数据离线 fine-tune。当前摘录能确认这些模块与目标，但具体 RPRO 公式细节、插值实现和 Algorithm 2 的逐步伪代码需要 PDF 核查。

#### 📊 实验与结果

实验覆盖四个长时程双臂真实机器人任务：Pack、Cap、USB、Case，平台是 Dobot XTrainer bimanual。作者按四个问题评估：总体性能是否优于 positive-only 与 positive-and-negative baseline，state-wise Smooth Interpolation 是否优于 trajectory-wise contrast，proximal regularizer 是否缓解 plain Flow-DPO 的 reward-hacking，以及 SFT term/proximal regularizer 的单独贡献。摘录明确说每个 Table 1 entry 来自 3 个独立训练 seed，并报告跨 seed mean/std；结论称 FlowPRO 在四个任务和两个 base policy family 上获得最高成功率和最短完成时间。但具体成功率、完成时间和 baseline 名称在摘录中不完整，不能引用。

#### ⚠️ 风险 / 保留意见

- 真实机器人任务虽强相关，但平台集中在 Dobot XTrainer 双臂，跨 embodiment 泛化仍需验证。
- 偏好数据依赖 teleoperated intervention-and-rollback，采集流程可能比摘要表述更复杂。
- 关键优势依赖 RPRO loss 与数据构造共同作用，复现时需要确认插值、负样本和 reference policy 细节。

#### 💭 结论与启发

这篇最值得借鉴的是“把失败信号变成可优化偏好对”的系统化设计。对后续选题来说，FlowPRO 提示 VLA 后训练不一定要走昂贵 reward model 或在线 RL，尤其在 flow-matching action head 下，proximal 约束可能是稳定性的关键。复现时应优先复核数据构造和 loss ablation，而不是只看最终成功率；系统设计上可把 intervention、rollback、preference labeling 做成长期数据闭环。

#### 🔎 读 PDF 先核查

- RPRO 的 proximal regularizer 如何具体作用到 flow-matching action distribution，而不是普通 log-prob policy？
- state-wise Smooth Interpolation 构造的 preferred/dispreferred 对是否会引入人为轨迹平滑偏差？
- FlowPRO 的提升主要来自负样本偏好信号，还是来自 SFT term 与 proximal reference 的稳定化？

#### 📌 上传 PDF 后优先看

- RPRO objective 与 Flow-DPO/PRO 的公式推导章节
- teleoperated intervention-and-rollback 数据采集与 Smooth Interpolation 章节
- 四个真实双臂任务的 baseline、ablation 和 seed 方差表

### [2]. PiL-World: A Chunk-Wise World Model for VLA Policy-in-the-Loop Evaluation [[HTML]](https://arxiv.org/html/2606.05773) [[PDF]](https://arxiv.org/pdf/2606.05773) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.05773`
* **Authors**: Chong Ma, Taiyi Su, Jian Zhu, Jianjun Zhang, Zitai Huang, Yi Xu, Hanli Wang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为 PiL-World 把世界模型从 open-loop 预测推进到 VLA policy-in-the-loop 闭环评估，这是低成本筛选机器人策略的关键接口。
* **关键词**: `policy-in-the-loop` `world model` `VLA evaluation` `closed-loop rollout` `multi-view prediction`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

真实 VLA 部署不是一次性预测完整动作序列，而是观察、执行 action chunk、再观察、再决策的闭环过程。许多机器人 world model 只沿着预采集轨迹做 open-loop future prediction，无法模拟策略自己导致的状态分布漂移。PiL-World 的问题意识很重要：如果世界模型不能把 VLA 上一步执行后的生成观测再喂回策略，它就很难用于可靠评估。对真实机器人来说，硬件安全、场景复位和实验吞吐都限制评测规模，因此一个 chunk-wise、multi-view、policy-in-the-loop 的 imagined rollout 环境有实际价值。

#### ⚙️ 核心方法

当前摘录只能确认 PiL-World 的高层机制：给定当前 observation 和 VLA policy 生成的 action chunk，PiL-World 生成与该 chunk 一致的多视角未来观测，并且这些未来观测匹配 VLA 下一次 inference 所需的图像输入。系统通过交替执行 VLA inference 与 world-model prediction，把多个 action chunk 串成闭环 imagined rollout。与 open-loop world model 的区别在于，下一步 action 不再来自离线轨迹，而来自被评估的 VLA 策略；下一步 observation 也不是真实环境或数据集帧，而是由 PiL-World 根据前一 chunk 预测得到。这个接口使世界模型成为策略评估器，而不只是视频预测器。摘录没有提供网络结构、训练损失、action chunk 表示、多视角相机建模或误差累积控制细节，因此这些部分只能视为合理推断，需要 PDF 进一步确认。

#### 📊 实验与结果

摘录中的 Experiments 部分基本回退为摘要内容，缺少完整实验设置和指标细节。可以确认的是，论文声称在三个真实 dual-arm manipulation tasks 上评估 PiL-World，并在结论中表示其用于 policy-in-the-loop VLA evaluation 时带来改进。能明确的证据边界是：它关注闭环 imagined rollout，而非单帧预测；它生成 multi-view future observations；它将最终生成观测作为下一次策略 query 的输入。具体任务名称、VLA baseline、评估指标、与真实执行结果的相关性、是否可替代真实机器人测试，目前摘录不足以判断。

#### ⚠️ 风险 / 保留意见

- 实验细节在摘录中严重不足，难以判断闭环评估与真实成功率的相关性。
- 世界模型误差会在多 chunk rollout 中累积，可能高估或低估策略表现。
- 如果生成观测分布与真实相机输入有偏差，VLA 下一步 action 可能被评估器伪影误导。

#### 💭 结论与启发

PiL-World 的启发在于把 world model 设计成“策略评测基础设施”。后续阅读应重点检查它是否真的能预测策略排名，而不只是生成合理视频。对于自己的系统设计，可以把这种接口用于离线筛选 checkpoint、比较 action chunk 策略、提前发现闭环失败模式；但部署前仍应保留真实机器人验证，因为 imagined rollout 的误差闭环风险很高。

#### 🔎 读 PDF 先核查

- PiL-World 生成的多视角未来观测与真实 rollout 在策略排名上相关性有多强？
- 闭环 imagined rollout 多个 chunk 后如何控制视觉误差累积和状态漂移？
- 被评估 VLA 是否会利用或放大 PiL-World 的生成伪影，导致评估偏乐观？

#### 📌 上传 PDF 后优先看

- world model 输入输出接口与 chunk-wise rollout 流程章节
- 真实 dual-arm manipulation task 设置与 VLA baseline 章节
- imagined evaluation 与真实机器人评估相关性的实验或表格

### [3]. World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis [[HTML]](https://arxiv.org/html/2606.05979) [[PDF]](https://arxiv.org/pdf/2606.05979) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.05979`
* **Authors**: Yi Yang, Zhihong Liu, Siqi Kou, Yiyang Chen, Yanzhe Hu, Jianbo Zhou, Boyuan Zhao, Zhijie Wei, Xiao Xia, Xueqi Li, Pengfei Liu, Zhijie Deng
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为 WLA 把 world modeling、language reasoning 和 action synthesis 放进同一个自回归框架，是今天最接近“新一代 embodied foundation model”叙事的论文。
* **关键词**: `World-Language-Action` `WAM` `VLA` `autoregressive Transformer` `test-time scaling`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

现有 WAM 借助世界建模接口从 egocentric video 中学习物理动态，但很多方法主要预测下一视觉状态，容易被低层视觉细节牵制；VLA 具备语言推理和指令跟随能力，却未必显式建模未来状态。WLA 的动机是把二者合并：下一状态不只包含图像或 latent physical dynamics，也包含高层 textual intention。这个问题对长时程机器人任务尤其关键，因为策略既要理解子任务语义，又要预测动作对世界的影响。WLA 因此不是单纯加一个视频预测头，而是试图把语义计划、subgoal image 和 low-level action 统一到 embodied foundation model 内。

#### ⚙️ 核心方法

WLA 采用 autoregressive Transformer backbone，而不是 WAM 中常见的 bidirectional diffusion Transformer，输入文本指令、图像和机器人状态，联合预测 textual subtasks、subgoal images 与 robot actions。摘录明确给出 WLA-0 的组成：RynnBrain-2B 作为 2.1B backbone，SANA-600M 作为 World Expert，flow-matching head 作为 390M Action Expert，总参数约 3.4B；每个 expert 有 28 层。World Expert 通过 world modeling objective 监督 fine-grained physical dynamics，Action Expert 负责动作生成。关键新意是 meta-queries：它们让 world prediction 隐式影响 action generation，因此推理时可以关闭显式 world prediction 以保持实时控制，也可以开启 world prediction 做 test-time scaling。也就是说，WLA 不把世界建模只当辅助可视化，而是把它变成动作头的条件化机制。当前摘录能确认模块角色，但具体 token 格式、loss Eq. 3.5 和 meta-query 交互方式仍需核查。

#### 📊 实验与结果

摘录提供了较多实现和 benchmark 线索。WLA-0 在 RoboTwin 2.0 上评估，该 benchmark 包含 50 个需要双臂协调的任务；作者按既有 multi-task protocol，用 2,500 条 clean-scene trajectories 和 25,000 条 strongly randomized trajectories 训练 100k steps。LIBERO 上 action chunk size 为 8，其他设置为 32；训练使用 DeepSpeed 和 AdamW。结论声称 WLA-0 在 memory 相关任务和多任务性能上达到强结果，并支持 long-horizon reasoning 与 real-time robot control。但摘录没有完整列出成功率、SOTA 对比数值和真实机器人设置，因此不能判断领先幅度。

#### ⚠️ 风险 / 保留意见

- 模型规模和专家模块复杂，复现成本明显高于轻量 VLA fine-tuning。
- World Expert 对 action 的真实贡献依赖 meta-query ablation，摘录中尚无完整证据。
- 自回归统一建模可能在实时控制中受延迟和长序列建模成本限制。

#### 💭 结论与启发

WLA 最重要的启发是：world model 可以从“预测未来图像”升级为“为动作生成提供可开关的语义与物理状态先验”。后续如果做系统设计，可以考虑把 subtask text、subgoal image、action chunk 作为统一训练目标，而不是只做 action supervision。阅读时应警惕大模型组合带来的 attribution 问题，优先看 meta-query、World Expert 和 Action Expert 的消融是否足以支撑统一框架主张。

#### 🔎 读 PDF 先核查

- meta-queries 如何把 World Expert 的预测信息传递给 Action Expert，是否有可解释的中间表示？
- 关闭 world prediction 推理时，动作性能与开启 test-time scaling 时的差距有多大？
- WLA 的提升来自 world modeling objective，还是主要来自更大的 backbone 和专家容量？

#### 📌 上传 PDF 后优先看

- WLA architecture、World Expert、Action Expert 与 meta-query 章节
- RoboTwin 2.0、LIBERO 和 memory task 的主结果表
- 关闭/开启 world prediction 与 expert ablation 的实验章节

### [4]. MPCoT: Reward-Guided Multi-Path Latent Reasoning for Test-Time Scalable Vision-Language-Action [[HTML]](https://arxiv.org/html/2606.06245) [[PDF]](https://arxiv.org/pdf/2606.06245) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.06245`
* **Authors**: Boyang Zhang, Lianlei Shan
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为 MPCoT 给 VLA 引入零显式 token 的测试时 latent reasoning，直接回应长时程控制中 one-pass decoder 的脆弱性。
* **关键词**: `latent reasoning` `test-time scaling` `VLA` `OpenVLA-OFT` `path preference`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

长时程 VLA 控制的难点在于早期小错误会沿 action chunk 累积，而标准 one-pass action decoder 几乎没有推理时修正空间。显式 chain-of-thought 可以增加推理深度，但文本或视觉 rationale 会带来延迟、显存开销，并且到连续动作之间仍隔着间接接口。MPCoT 的价值在于把“多路径思考”搬到连续 latent space：不生成 reasoning token，而是在动作解码前生成、细化、选择多个 latent hypothesis。它关注的是 inference-time compute 如何真正帮助 VLA 控制，而不是只在语言层面增加解释。

#### ⚙️ 核心方法

MPCoT 插入 OpenVLA-OFT，在不改变原 8-step action interface 的前提下，于 policy decoder 之前加入 latent reasoning module。每个 control step 中，模型先初始化多个 latent hypotheses，再用权重共享的 refinement steps 迭代细化，最后通过 confidence-aware soft weights 聚合 refined branches，再交给同一个 action head 解码。作者强调它不是多策略 ensemble，也不是 inference-time search，而是单一 policy head 上的轻量 latent refinement。训练阶段有 path-preference objective，对候选 action branch 用 expert-action consistency、world-model/VLM-based progress 和 success feedback 等信号进行评价，从而监督 scorer；推理阶段则不需要 reward feedback。摘录还说明 depth/width ablation 改变 latent steps 和 hypotheses，而不改变 backbone、decoder、action horizon、splits 或 observations。核心新意是把测试时扩展从显式 CoT 转化为可控的 latent depth/width。

#### 📊 实验与结果

实验使用 OpenVLA-OFT 官方 evaluation code 和 splits。LIBERO 被定位为 near-ceiling compatibility benchmark，CALVIN ABC D 与机制消融则作为 sequential robustness、depth/width scaling 和 reward-guided path supervision 的主要证据。LIBERO 报告 suite-level 与 average success rate；CALVIN 报告 1-5 step success rate 和 average successful sequence length，以反映长指令链中的误差累积。摘录说明主结果固定 inference 设置，其他 depth/width 进入消融；结论声称在 LIBERO 和 CALVIN 上相对强 baseline 改善长时程表现。但具体 SR 数值、延迟数值和 baseline 列表未完整给出，需保守看待。

#### ⚠️ 风险 / 保留意见

- 训练时 path preference 依赖 world-model/VLM progress 和 success feedback，信号质量会影响 scorer。
- latent 多路径推理增加推理延迟，实际机器人频率需要核查完整 latency 表。
- 如果 benchmark 接近 ceiling，LIBERO 提升可能不足以证明复杂长时程泛化。

#### 💭 结论与启发

MPCoT 对后续工作最大的启发是：测试时计算可以不通过语言 token，而直接作用在动作前的 latent hypothesis 上。做 VLA 系统时，这类模块适合作为可插拔的风险控制层，用于高不确定状态或长时程子任务；但它是否值得部署，取决于 CALVIN 长链收益与延迟开销的平衡。阅读 PDF 时应重点看 path scorer 的监督质量和 depth/width scaling 是否稳定。

#### 🔎 读 PDF 先核查

- path scorer 在推理时没有 reward feedback，如何避免训练阶段偏好信号与测试状态分布错配？
- latent depth 和 hypothesis width 的收益是否单调，还是很快达到延迟/性能拐点？
- MPCoT 的 soft aggregation 是否会平均掉互斥动作分支，导致接触任务中动作不锐利？

#### 📌 上传 PDF 后优先看

- MPCoT latent hypothesis 初始化、refinement 与 aggregation 章节
- path-preference objective 和 reward/progress 信号定义章节
- CALVIN 长链、depth/width scaling 与 latency ablation 表

### [5]. TempoVLA: Learning Speed-Controllable Vision-Language-Action Policies [[HTML]](https://arxiv.org/html/2606.06491) [[PDF]](https://arxiv.org/pdf/2606.06491) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.06491`
* **Authors**: Dong Jing, Jingchen Nie, Tianqi Zhang, Jiaqi Liu, Huaxiu Yao, Zhiwu Lu, Mingyu Ding
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为 TempoVLA 把执行速度从训练数据的隐含属性变成可控条件，是 VLA 部署中少见但很实用的问题。
* **关键词**: `speed-controllable VLA` `trajectory augmentation` `LIBERO` `flow matching` `dynamic speed control`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

#### 📖 背景与动机

机器人操作并不应该以单一速度运行：空中移动和低风险 transit 可以快，接触、插入、按压等阶段则需要慢和稳。现有 VLA 通常继承 demonstrations 的固定速度，模型压缩、KV-cache 或 RL 加速也多是把策略从一个固定速度推到另一个固定速度，很少支持同一策略内的双向速度控制。TempoVLA 的动机很直接：预测动作的幅值本身决定机器人运动快慢，因此可以通过数据和条件机制让模型学习目标速度。对真实部署来说，这比单纯提升推理 FPS 更接近安全、效率和精度之间的动态权衡。

#### ⚙️ 核心方法

摘录能确认 TempoVLA 由数据侧 Variable-Speed Trajectory Augmentation 与轻量模型侧 conditioning 组成。VSTA 的关键思路是利用动作在平移和旋转增量空间中的线性可组合性，对轨迹做 accumulate-then-split，从而生成不同目标速度下仍可执行的 demonstrations；gripper 信号则离散处理。模型侧将 target speed 作为条件输入，默认用 textual prefix 注入，让单个 VLA 在推理时根据指定速度输出对应幅值的 action。实验基于一个 flow-matching VLA，该模型建立在 PaliGemma 之上并预训练于大规模 embodied datasets。摘录还提到可通过外部 VLM 实现 dynamic speed control，即根据场景阶段选择速度。当前摘录不足以确认完整速度档位、VSTA 数学定义和速度条件是否也可用非文本 token 表示，这些需要 PDF 复核。

#### 📊 实验与结果

仿真实验使用 LIBERO 四个 manipulation suites：Spatial、Object、Goal、Long；每个 suite 含 10 个任务和 500 条人类遥操作 demonstrations。作者指出 LIBERO demonstrations 平滑且没有剧烈速度变化，因此适合作为速度控制测试床。动作是 end-effector command，包含 translation、axis-angle rotation increment 和 gripper signal。训练设置包括 30k iterations、batch size 512、32 张 NVIDIA H20 GPU、固定随机种子。结论称 TempoVLA 支持双向速度控制、提升默认性能，并在真实世界实验中展示动态速度控制；但摘录没有给出具体成功率、速度误差或真实任务数量，不能展开数值比较。

#### ⚠️ 风险 / 保留意见

- 高速端会出现速度提升饱和，摘录暗示 per-step target 超过固定限制后效果受限。
- 速度控制依赖动作幅值可组合假设，接触密集或非线性动力学阶段可能不完全成立。
- 动态速度若由外部 VLM 决策，错误阶段判断可能带来安全风险。

#### 💭 结论与启发

TempoVLA 提醒我们，VLA 部署指标不应只看成功率，还要看速度、接触阶段节奏和用户可控性。复现时可以从数据增强入手，不必先改大模型结构；系统设计上，可以把速度作为 instruction 之外的独立控制旋钮，用于任务阶段调度。后续阅读重点应放在 VSTA 生成轨迹是否真的保持可执行，以及速度控制是否牺牲精度和稳定性。

#### 🔎 读 PDF 先核查

- VSTA 在高风险接触阶段是否会破坏原 demonstration 的时序和接触稳定性？
- target speed textual prefix 是否足够稳定，还是需要显式数值 token 或 controller-side constraint？
- 默认性能提升来自速度增强带来的数据正则化，还是来自推理时速度选择本身？

#### 📌 上传 PDF 后优先看

- Variable-Speed Trajectory Augmentation 的算法与可执行性验证章节
- LIBERO 四套任务上的速度档位、成功率和速度误差表
- 真实世界动态速度控制与外部 VLM 阶段判断实验

### [6]. Flash-WAM: Modality-Aware Distillation for World Action Models [[HTML]](https://arxiv.org/html/2606.05254) [[PDF]](https://arxiv.org/pdf/2606.05254) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.05254`
* **Authors**: Arman Akbari, Ci Zhang, Arash Akbari, Lin Zhao, Yixiao Chen, Weiwei Chen, Xuan Zhang, Geng Yuan, Yanzhi Wang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为 Flash-WAM 直击 WAM 的实时控制瓶颈，并指出 joint video-action diffusion 不能直接套用单模态 step distillation。
* **关键词**: `World Action Model` `step distillation` `modality-aware diffusion` `real-time control` `LingBot-VA`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

#### 📖 背景与动机

WAM 通过联合生成未来视频和机器人动作来建模物理动态，理论上比直接 VLA 更具未来状态先验，但 iterative diffusion 往往需要多步 denoising，难以满足实时控制。Step distillation 是自然方向，可是在 joint video-action setting 中，视频流和动作流的噪声调度、SNR shift 和边缘噪声分布并不一致。Flash-WAM 的重要性在于它没有把 WAM 加速看成普通 diffusion 压缩问题，而是识别出多模态蒸馏的结构性失败模式。对部署来说，能否把 WAM 压到实时 chunk-level latency，决定它是否能从评估/生成工具进入控制回路。

#### ⚙️ 核心方法

Flash-WAM 是 modality-aware step-distillation framework，服务对象是联合 video-action diffusion WAM。摘录指出 off-the-shelf consistency distillation 在这里会失败，因为 video 和 action stream 使用不同 SNR-shifted noise schedules，并在 distillation loss 处处于不同噪声 regime；一个单一 consistency function 很难同时适配两种模态。Flash-WAM 的解决方案是为不同模态选择 consistency-function family 中不同成员，使其匹配各自噪声 regime。实验实例化在 released LingBot-VA shared-backbone model 上，作者选择它是因为开源、WAM 性能强，且参数规模适合 commodity edge deployment。当前摘录没有给出完整蒸馏损失、teacher-student schedule、每模态函数族具体形式或 action/video 权重设置，因此只能确认“模态感知一致性蒸馏”这一主线。

#### 📊 实验与结果

实验设置覆盖两个仿真 benchmark 和一个真实机器人 setup。RoboTwin 2.0 是双臂操作 benchmark，包含 Clean split 和 Randomized split；LIBERO 也用于评估。延迟在单张 NVIDIA L40S GPU 上测量，作者采用一个 chunk-level 实时预算作为参考，但摘录中的具体毫秒数被截断，不能引用。结论声称 Flash-WAM 在 LingBot-VA 上接近恢复原模型任务成功率，并在更少 denoising step 下达到实时 per-chunk latency；同时提到 RoboTwin 2.0、LIBERO 和真实世界结果。由于摘录里的成功率和 speedup 数值缺失，不能判断压缩幅度与性能损失的具体权衡。

#### ⚠️ 风险 / 保留意见

- 方法依赖 video/action 噪声调度差异诊断，换到其他 WAM 架构需重新验证。
- 摘录未给出完整数值，实时性和成功率损失需要 PDF 表格确认。
- 只在 LingBot-VA 上实例化，Motus、DreamZero 等不同架构是否适用仍是开放问题。

#### 💭 结论与启发

Flash-WAM 对我最大的启发是：WAM 实时化不能只照搬图像 diffusion 的蒸馏经验，动作流的噪声性质和控制误差会改变压缩策略。后续如果要做 WAM 部署，应把 video quality、action success 和 latency 分开评估，并检查每个模态的蒸馏目标。它也适合作为读 WAM 论文时的工程标尺：强 world-action model 如果不能低延迟运行，实际控制价值会大打折扣。

#### 🔎 读 PDF 先核查

- Flash-WAM 为 video/action 选择不同 consistency function 的准则是否可迁移到其他 WAM？
- 蒸馏后 action success 的下降与 video prediction quality 的下降是否同步，还是存在模态不一致？
- 单步或少步 denoising 达到实时后，在真实机器人闭环中是否会积累控制误差？

#### 📌 上传 PDF 后优先看

- modality-aware consistency distillation 的失效分析和公式章节
- RoboTwin 2.0、LIBERO 上成功率与 denoising step/latency 权衡表
- 真实机器人 setup 与蒸馏后闭环控制稳定性实验

## Watchlist

### [W1]. Discrete-WAM: Unified Discrete Vision-Action Token Editing for World-Policy Learning [[HTML]](https://arxiv.org/html/2606.05645) [[PDF]](https://arxiv.org/pdf/2606.05645)
* **Paper ID**: `2606.05645`
* **Authors**: Ziyang Yao, Haochen Liu, Yuncheng Jiang, Zeyu Zhu, Zibin Guo, Jingru Wang, Tianle Liu, Jianwei Cui, Kuiyuan Yang, Hongwei Xie, Jingwei Zhao, Guang Chen, Hangjun Ye
* **Author Priority**: Standard
* **为什么还值得留意**: Discrete-WAM 进入 shortlist 是因为它把未来视觉状态和 ego action 都离散 token 化，用统一 token-editing 范式处理 driving world-policy learning，和今天的 WAM/World Action Model 主线高度相关。它没有进入最终精选，主要因为场景是 autonomous driving 而非机器人操作，且方法重心偏离 VLA manipulation；但其 counterfactual future 与离散视觉-动作 token 接口值得后续横向参考。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. LadderMan: Learning Humanoid Perceptive Ladder Climbing [[VIP]] [[HTML]](https://arxiv.org/html/2606.05873) [[PDF]](https://arxiv.org/pdf/2606.05873)
* **Paper ID**: `2606.05873`
* **Authors**: Siheng Zhao, Yuanhang Zhang, Ziqi Lu, Pieter Abbeel, Rocky Duan, Koushil Sreenath, Yue Wang, C. Karen Liu, Guanya Shi
* **Author Priority**: Core VIP
* **为什么还值得留意**: LadderMan 值得跟踪，因为它有 Pieter Abbeel 与 Yue Wang，且问题是高难度 humanoid perceptive ladder climbing，包含 hybrid imitation/RL、vision foundation model bridging sim-to-real、真实 Unitree G1 部署等强机器人信号。没有进入最终精选，是因为它更偏 humanoid locomotion/whole-body manipulation 系统论文，而非今天 VLA/WAM 主线；但 Sim2Real 和全身接触控制价值很高。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. AffordanceVLA: A Vision-Language-Action Model Empowering Action Generation through Affordance-Aware Understanding [[HTML]](https://arxiv.org/html/2606.06155) [[PDF]](https://arxiv.org/pdf/2606.06155)
* **Paper ID**: `2606.06155`
* **Authors**: Qize Yu, Jiadi You, Yuran Wang, Jiaqi Liang, Bowen Ping, Yang Tian, Yue Chen, Minghong Cai, Zeying Gong, Ruihai Wu, Yinchuan Li, Junwei Liang, Yingcong Chen
* **Author Priority**: Standard
* **为什么还值得留意**: AffordanceVLA 进入 shortlist 是因为它试图用 Which2Act、Where2Act、How2Act 这类结构化 affordance forecasting 弥合 VLM 语义空间与机器人 3D 动作空间的错位。未进最终精选，是因为摘录显示方法和实验较像 VLA 中间表征增强，和今天更优先的后训练、闭环 world model、测试时扩展相比新范式冲击略弱；但 LIBERO/CALVIN 与真实任务结果仍值得上传 PDF 后检查。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. TAM: Torque Adaptation Module for Robust Motion Transfer in Manipulation [[VIP]] [[HTML]](https://arxiv.org/html/2606.06218) [[PDF]](https://arxiv.org/pdf/2606.06218)
* **Paper ID**: `2606.06218`
* **Authors**: Dongwon Son, Florian Shkurti, Jason Lee, Naman Shah, Beomjoon Kim, Dieter Fox
* **Author Priority**: Extended VIP
* **为什么还值得留意**: TAM 值得进入 watchlist，因为 Dieter Fox 在作者中，且 torque-interface adaptation 直接面对 sim-to-real、payload 和机器人实例差异，对 contact-rich manipulation 很实用。它没有进入最终精选，是因为它主要是 torque adaptation/motion transfer 模块，并非 VLA 或 World Action Model 本体；但其“冻结策略、只适配底层 torque response”的思路可为 VLA 部署补强。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
