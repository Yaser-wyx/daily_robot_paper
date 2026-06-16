# RoboPulse | 2026-06-16

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 183 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线非常集中：VLA 正在从“看图听指令后直接出动作”转向更闭环、更物理、更可校正的系统，包括触觉反应、可测量仿真、潜空间世界动作模型、几何世界建模、在线 RL 微调和短期记忆。最终精选的 6 篇分别覆盖了 VLA 落地最关键的六个瓶颈：接触反馈、Sim2Real 数据生成、动作条件动态预测、3D 几何推理、稀疏结果奖励下的在线改进，以及长时序部分可观测任务。VIP 作者上，T-Rex 同时出现 Pieter Abbeel、Yuke Zhu、Danfei Xu，PRISM 有 Yuke Zhu，值得优先跟踪；watchlist 里 Cewu Lu 的 PO-PDDL 和 Xiaolong Wang 的 EgoPhys 也分别代表符号 POMDP 与可变形物理数字孪生两条重要支线。整体看，今天不是单点模型刷榜，而是机器人基础模型开始补齐“触觉、物理、几何、记忆、在线反馈”这些部署必需能力。

## 今日信号

- VLA 的下一阶段重点不再只是扩大视觉语言预训练，而是把触觉、几何、潜在动态和历史记忆接入动作生成闭环。
- Sim2Real 与 world model 论文都在减少对真实机器人遥操作数据的依赖，但可信度越来越依赖物理参数、传感器协议和真实机器人验证是否闭合。
- 在线 RL 微调开始从稀疏 episode 成败标签中拆出更细粒度的训练信号，这可能成为 VLA 从演示模仿走向部署自改进的关键接口。

## Historical Rediscovery

- **Paper**: Elastic Queries Reinforcement Learning: Self-Aware Policy Execution for VLA Models [[HTML]](https://arxiv.org/html/2606.14375) [[PDF]](https://arxiv.org/pdf/2606.14375)
  - **Paper ID**: `2606.14375`
  - **来源日期**: 2026-06-15
  - **当时可能被低估的信号**: 当时可能低估了“联合选择 latent input、denoising budget、action chunk length”这个信号；它不是单纯省算力，而是在困难接触阶段和简单阶段之间动态调度执行策略。
  - **为什么现在值得再看**: 现在值得再看，因为 VLA 真实部署越来越受延迟、动作块长度和闭环频率制约；它直接连接 RL 后训练、VLA action head 和长时程操作中的自适应执行。
  - **建议动作**: 加入精读
  - **关键词**: `VLA` `RL+VLA` `adaptive inference` `action chunking` `deployment`
- **Paper**: ContactWorld: What Matters in Vision-Tactile World Models for Contact-Rich Manipulation [[HTML]](https://arxiv.org/html/2606.13877) [[PDF]](https://arxiv.org/pdf/2606.13877)
  - **Paper ID**: `2606.13877`
  - **来源日期**: 2026-06-15
  - **当时可能被低估的信号**: 当时可能低估了它对 spatially structured、temporally continuous representation 的系统比较，以及“联合正则 fused multimodal latents 反而可能损害规划”的经验信号。
  - **为什么现在值得再看**: 现在值得再看，因为 World Model / World Action Model 若要进入真实操作，接触、触觉和长时预测是核心短板；这篇虽偏 benchmark/经验研究，但问题设置和你的 world model 兴趣高度重合。
  - **建议动作**: 加入精读
  - **关键词**: `world model` `vision-tactile` `contact-rich manipulation` `long-horizon planning`
- **Paper**: PhysVLA: Towards Physically-Grounded VLA for Embodied Robotic Manipulation [[HTML]](https://arxiv.org/html/2606.13886) [[PDF]](https://arxiv.org/pdf/2606.13886)
  - **Paper ID**: `2606.13886`
  - **来源日期**: 2026-06-15
  - **当时可能被低估的信号**: 当时可能低估了 plug-and-play、低延迟物理约束这一部署信号；phase-aware finite-state machine 和 selective Lagrangian gate 虽像规则包装器，但正好适合验证 VLA 的物理 grounding 缺口。
  - **为什么现在值得再看**: 现在值得再看，因为 Sim2Real 和真实部署不只需要更大模型，也需要能在不重训主干的情况下约束动作；它与 VLA、physically grounded action generation 和部署期安全性直接相关。
  - **建议动作**: 快速浏览
  - **关键词**: `VLA` `physical grounding` `Sim2Real` `inference-time steering` `deployment`
- **Paper**: ReactVLA: Fast and Lightweight Reactive Robot Manipulation via Improved Mean Flow Action Generation [[HTML]](https://arxiv.org/html/2606.14255) [[PDF]](https://arxiv.org/pdf/2606.14255)
  - **Paper ID**: `2606.14255`
  - **来源日期**: 2026-06-15
  - **当时可能被低估的信号**: 当时可能低估了低延迟本身的研究价值；如果真实 Diana 机器人 20 runs 设置下仍能保持精度，它会比单纯模拟吞吐提升更接近实际 VLA 部署痛点。
  - **为什么现在值得再看**: 现在值得再看，因为 VLA 与 World Action Model 最终都要面对实时闭环控制，采样步数、延迟和精度的折中会决定真实机器人可用性。
  - **建议动作**: 快速浏览
  - **关键词**: `VLA` `low latency` `action generation` `real robot evaluation` `deployment`
- **Paper**: CorridorVLA: Explicit Spatial Constraints for Generative Action Heads via Sparse Anchors [[HTML]](https://arxiv.org/html/2604.21241) [[PDF]](https://arxiv.org/pdf/2604.21241)
  - **Paper ID**: `2604.21241`
  - **来源日期**: 2026-04-24
  - **当时可能被低估的信号**: 当时可能低估了 sparse anchors 的可解释空间约束价值；它不是泛泛加感知特征，而是把动作生成限制在更贴近控制目标的空间 corridor 中。
  - **为什么现在值得再看**: 现在值得再看，因为 World Action Model 和 VLA 部署都需要更可控、可解释的 action head；虽然缺少 real-robot 实验，但它对结构化动作生成仍有参考价值。
  - **建议动作**: 继续跟踪
  - **关键词**: `VLA` `generative action head` `spatial constraints` `World Action Model` `control`

## Editor's Picks

### [1]. T-Rex: Tactile-Reactive Dexterous Manipulation [[VIP]] [[HTML]](https://arxiv.org/html/2606.17055) [[PDF]](https://arxiv.org/pdf/2606.17055) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.17055`
* **Authors**: Dantong Niu, Zhuoyang Liu, Zekai Wang, Boning Shao, Zhao-Heng Yin, Anirudh Pai, Yuvan Sharma, Stefano Saravalle, Ruijie Zheng, Jing Wang, Ryan Punamiya, Mengda Xu, Yuqi Xie, Yunfan Jiang, Letian Fu, Konstantinos Kallidromitis, Matteo Gioia, Junyi Zhang, Jiaxin Ge, Haiwen Feng, Fabio Galasso, Wei Zhan, David M. Chan, Yutong Bai, Roei Herzig, Jiahui Lei, Fei-Fei Li, Ken Goldberg, Jitendra Malik, Pieter Abbeel, Yuke Zhu, Danfei Xu, Jim (Linxi)Fan, Trevor Darrell
* **Author Priority**: Core VIP
* **一句话结论**: 优先看：T-Rex 是今天最贴近真实灵巧操作瓶颈的 VLA 工作，因为它把高频触觉反应正式放进大模型动作生成链路。
* **关键词**: `触觉反应` `灵巧操作` `VLA` `Mixture-of-Transformer-Experts` `双臂灵巧手`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)

#### 📖 背景与动机

当前很多 VLA 在语义理解和视觉条件动作生成上进展很快，但遇到薄卡插槽、钥匙开锁、柔顺接触和微滑移控制时，单靠 RGB 或低频视觉闭环很容易失效。人类灵巧操作依赖触觉中的力变化、局部形变和接触瞬态，而这些信号往往发生在视觉控制回路反应之前。摘录明确指出，现有学习式 VLA 要么忽略触觉，要么只使用偏静态的触觉编码器，原因包括触觉训练数据稀缺、缺少标准评估、架构难以同时处理视觉语言上下文与高频触觉，以及静态 tactile encoder 难以捕捉微观动态。T-Rex 进入精选，是因为它把问题定义为 tactile-reactive dexterous manipulation，而不是简单给 VLA 多拼一个传感器输入；这正好对应灵巧手、双臂和接触丰富操作走向真实部署时最硬的短板。

#### ⚙️ 核心方法

T-Rex 的核心是 Mixture-of-Transformer-Experts backbone 加 spatial-temporal tactile encoder。摘录显示，MoT backbone 包含三个专家：latent expert 处理视觉和语言观测，并预测未来视觉表示，为动作生成提供时间上下文；action expert 从纯噪声开始去噪，生成低频 action plan；tactile expert 复用缓存的视觉语言上下文，在后续去噪阶段接入高频触觉观测，对动作进行细化，输出可执行 action chunk。这个分工的价值在于把“语义与视觉规划”和“接触后的快速修正”拆成连续接口，而不是让同一个网络在同一频率下同时承担所有职责。触觉编码部分也不是单一路径：每个手指的 VQ-VAE 压缩近期 force history 得到时间 token，当前 force vector 直接投影以保留瞬时接触状态，同时还用卷积编码形变图，形成时空触觉表示。当前摘录只能确认这些模块级设计，不能确认完整损失函数、token 维度、去噪步数或训练配比；但从描述看，创新点在于把触觉作为动作去噪后段的高频 refinement 信号，而非静态辅助特征。

#### 📊 实验与结果

实验设置很重：真实机器人为固定基座双臂 Dexmate Vega-1，配两只 22-DoF Sharpa Wave 灵巧手；观测包括 ZED 头部 RGB 相机、两个单目腕部相机、每指触觉力向量和形变图；动作用双臂相对末端 delta 控制与手指绝对关节控制。对比基线有 6 个，包括 ACT 风格的 ViTacFormer、slow-fast 视觉触觉 diffusion policy RDP、Tactile-VLA、预训练 VLA EgoScale 及其 tactile 变体等，并声明使用相同机器人设置、动作空间和评估协议。摘要还提到 100 小时 tactile-rich 数据集。摘录没有给出成功率表格或具体任务成绩，因此不能判断领先幅度；但可以确认它的证据重点是真实双臂灵巧手、触觉丰富任务和同平台多基线比较，而非只在仿真里展示触觉融合。

#### ⚠️ 风险 / 保留意见

- 摘录没有提供具体成功率、任务数量和统计方差，当前只能判断实验设计较完整，不能判断提升幅度是否稳定。
- 系统依赖高质量多指触觉传感和灵巧手平台，迁移到低成本夹爪或不同 tactile hardware 的成本可能很高。
- MoT、VQ-VAE 触觉编码和扩散式动作去噪组合较复杂，复现实验可能受数据采集、同步频率和传感器标定影响很大。

#### 💭 结论与启发

这篇最值得拿来思考“触觉应该接在 VLA 的哪里”。如果把触觉直接拼到早期观察 token，模型可能学到的是慢速相关性；T-Rex 的设计启发是让视觉语言模块先给出低频计划，再让触觉专家在动作去噪后段做接触修正。后续阅读 PDF 时，我会重点检查触觉频率、action chunk 频率、触觉缺失或延迟下的退化，以及 tactile expert 是否真的学到闭环反应，而不是只在训练分布内做条件模仿。

#### 🔎 读 PDF 先核查

- tactile expert 在去噪后段接入触觉，相比早期融合或简单 concat，消融中是否能证明它带来更快的接触修正？
- 100 小时 tactile-rich 数据覆盖了哪些接触模式，是否足以支撑新物体、新材料和新任务泛化？
- 高频触觉输入与低频 action chunk 之间如何同步，延迟或触觉噪声是否会导致策略不稳定？

#### 📌 上传 PDF 后优先看

- 方法章节中的 MoT backbone、触觉专家和动作去噪流程图
- 实验章节中的真实机器人任务定义、成功率表格和各基线公平性说明
- 消融章节中的无触觉、静态触觉、不同 tactile encoder 与频率设置对比

### [2]. SimWeaver: Zero-Shot RGB Sim-to-Real for Deformable Manipulation [[HTML]](https://arxiv.org/html/2606.15338) [[PDF]](https://arxiv.org/pdf/2606.15338) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.15338`
* **Authors**: Wenkang Hu, Haoran Wang, Yitong Li, Liu Liu, Mengao Zhao, Lai Jiang, Xincheng Tang, Junhang Wei, Zhengjie Shu, Zhendong Wang, Zhizhong Su, Huamin Wang, Ruigang Yang
* **Author Priority**: Standard
* **一句话结论**: 优先看：SimWeaver 是今天 Sim2Real 方向最实用的一篇，因为它把可变形物体的 RGB-only 零样本迁移拆成仿真可信度、资产、轨迹生成和成像协议四个可工程化环节。
* **关键词**: `RGB Sim2Real` `可变形操作` `物理参数化资产` `塑料袋操作` `合成演示`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

可变形物体操作一直是 Sim2Real 的难点：衣物、塑料袋、丝绸等对象状态空间巨大、形变非线性强，和夹爪接触后还会出现折叠、滑移、遮挡与自碰撞。真实数据虽然最可靠，但为每个任务采集遥操作演示成本很高，且很难覆盖可变形对象的多样初始状态。过去刚体操作中常用的仿真合成路线，在可变形物体上往往因为物理参数不对应真实材料、深度传感不稳定、渲染与相机 ISP 差距明显而失效。SimWeaver 进入精选，是因为它没有只宣称“更多仿真数据”，而是把 deformable RGB sim-to-real 的失败源逐个工程化：测量支撑的 simulator 和 asset，拓扑感知轨迹合成，以及面向真实 RGB 相机的协议。对于后续做 VLA 数据扩展和低成本真实部署，这类 pipeline 的价值比单一模型结构更大。

#### ⚙️ 核心方法

SimWeaver 由四个互相咬合的组件构成。SimWeaver-Sim 负责可靠的可变形仿真，摘录强调它和常见 PBD 参数不同，尽量使用可测量物理量而非手工调参的抽象参数。SimWeaver-Asset 是可扩展资产框架，包含来自 CLOTH3D 的服装网格以及塑料袋等 prior dataset 中不足的类别，统一为 triangle-mesh 表示，便于在 solver 和 renderer 间复用。关键是 material parameterization：每个资产绑定到 RGBench 的织物测量库条目，使用单位面积质量、弯曲刚度、拉伸、摩擦等现实可测属性，避免把 sim-to-real 成功建立在不可解释调参上。SimWeaver-Syn 是 deterministic topology-aware trajectory synthesizer，用来为每个任务生成演示；摘要明确说每个任务使用 200 条模拟演示训练 RGB VLA policy。SimWeaver-Real 则涉及 sim-to-real protocol 和 ISP-aware 处理，说明作者把真实相机成像链路也视作迁移变量。当前摘录只能确认模块组成和物理参数思路，不能确认具体轨迹合成算法细节或 ISP 配置。

#### 📊 实验与结果

实验使用双臂平台：两台 Piper 6-DOF 机械臂、平行夹爪、一个 overhead 和两个 wrist-mounted RealSense D435i 相机。策略在 SimWeaver-Syn 为每个任务生成的 200 条演示上全量微调，并在 5 个可变形真实任务上评估，其中包括塑料袋操作。摘录提到 DP3 点云基线在同样演示上五个真实任务全部失败，作者将其归因于消费级 RGB-D 在 matte-black grippers、丝绸和袋子表面上的深度采集限制，而不是泛化为点云方法本身无效。仿真可靠性部分还比较了 SimWeaver-Sim、Isaac Sim PhysX particle cloth 和 Newton VBD，并在相同 garment asset、相同双臂抓取抬升动作和相同硬件下统计每步时间。结论摘录明确写到每任务达到 80% 真实成功率，但平均成功率数字在提供文本中缺失，因此不能补写。

#### ⚠️ 风险 / 保留意见

- 零样本结果依赖 simulator、资产物理参数和真实相机协议共同成立，单独替换硬件或材料后可能需要重新验证。
- 摘录没有给出每个任务完整成功率、失败类型和置信区间，80% per task 的稳定性需要看表格。
- DP3 失败被归因于深度采集限制，这对 RGB 路线有利，但也意味着结论受具体传感器和表面材质影响。

#### 💭 结论与启发

SimWeaver 的启发是，Sim2Real for deformable manipulation 不能只问“仿真像不像”，而要问物理参数是否可测、资产是否覆盖真实材料、合成轨迹是否符合拓扑约束、相机成像是否被纳入协议。对于后续复现或选题，最值得借鉴的是用小规模但高质量的每任务 200 条仿真演示，配合可解释物理参数，而不是盲目堆大规模合成数据。若要扩展到 VLA，重点应放在怎样让语言任务、RGB 观测和物理资产元数据形成统一训练接口。

#### 🔎 读 PDF 先核查

- SimWeaver-Syn 的 topology-aware 轨迹合成具体如何避免生成物理可行但任务语义错误的演示？
- 测量支撑的材料参数在不同真实物体之间如何绑定，是否需要人工选择 fabric class？
- ISP-aware sim-to-real protocol 对最终成功率贡献有多大，是否有关闭该模块的消融？

#### 📌 上传 PDF 后优先看

- SimWeaver-Sim 与 SimWeaver-Asset 的物理参数定义和材料绑定方式
- 5 个真实可变形任务的成功率表、失败案例和每任务 200 demos 设置
- 与 Isaac Sim、VBD、DP3 等基线的公平比较和消融实验

### [3]. LaWAM: Latent World Action Models for Efficient Dynamics-Aware Robot Policies [[HTML]](https://arxiv.org/html/2606.15768) [[PDF]](https://arxiv.org/pdf/2606.15768) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.15768`
* **Authors**: Jialei Chen, Kai Wang, Kang Chen, Shuaihang Chen, Feng Gao, Wenhao Tang, Zhiyuan Li, Weilin Liu, Zhuyu Yao, Boxun Li, Yuanbo Xu, Chao Yu
* **Author Priority**: Standard
* **一句话结论**: 优先看：LaWAM 是 world action model 路线中很值得读的一篇，因为它把昂贵的像素级未来视频生成压缩成 latent visual subgoal。
* **关键词**: `World Action Model` `latent visual subgoal` `VLA` `latent dynamics` `LIBERO`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

VLA 的强项是把视觉语言预训练迁移到机器人动作，但很多模型仍然主要根据当前图像和指令直接预测动作，对“执行候选动作后场景会怎样变化”缺乏显式建模。World-Action Model 试图补这个缺口，用预测的未来观测或状态作为策略上下文，让动作生成更 dynamics-aware。但现有 WAM 常走像素级图像或视频生成路线，把大量容量花在视觉重建、纹理和背景细节上，推理也可能因为迭代生成而变慢。对机器人 manipulation 来说，策略往往只需要知道与动作相关的未来变化，比如物体位姿、接触关系或局部空间结构，不一定需要完整视频。LaWAM 入选，是因为它抓住了 WAM 的核心矛盾：未来建模有用，但像素级想象太贵；latent subgoal 可能是更适合动作生成的中间层。

#### ⚙️ 核心方法

LaWAM 保留 future-conditioned policy 的思想，但把未来表示放在冻结视觉编码器的 feature space 中。方法先定义当前观测、语言指令和固定物理 horizon 内的 action chunk；普通 VLA 直接建模当前视觉语言到动作，而常见 WAM 会先生成未来图像或 clip，再用 inverse dynamics model 把期望未来映射到动作。LaWAM 的替代方案是学习 latent-action-conditioned model：用冻结视觉 encoder 得到当前 feature 和 horizon feature，训练 latent action posterior 从观察到的 transition 中推断 latent action，再由 decoder 根据当前 feature 和 latent action 预测 horizon feature。这个 decoder 被保留下来作为 Latent World Model，也就是 LaWM。推理时，policy 不需要生成像素视频，而是预测 latent action，再由 LaWM 展开成 embodiment-grounded latent visual subgoal，供 action-chunk generation 使用。摘录还说明 LaWM 用约 3000 小时机器人视频和 1500 小时 egocentric human videos 预训练，human videos 只通过 dynamics prior 贡献，不直接参与语言机器人轨迹整合。新意在于把 latent action token 扩展为空间结构化 latent visual subgoal，而不是只让 policy 使用压缩动作 token。

#### 📊 实验与结果

实验覆盖五个维度：仿真 benchmark、推理效率、真实世界迁移、latent dynamics 行为和组件贡献。LIBERO 是明确出现的主要 benchmark，摘录称在四个标准 LIBERO suites 上，LaWAM 在 VLA、latent-action 和 WAM baselines 中获得最佳平均成功率；同时指出相比 latent-action baselines 的差距说明，将紧凑 action tokens 展开为空间结构化 latent visual subgoals 更有效。效率方面，摘录明确提到 LaWAM 用 230M LaWM 替代大型视频生成 backbone，避免昂贵的 pixel-space imagination。真实机器人或其他 benchmark 细节在摘录中只被概括为 real-world transfer，没有给出任务、成功率或延迟数字，因此只能保守认为它提供了跨仿真和真实设置的证据线索，具体强度需要查表。

#### ⚠️ 风险 / 保留意见

- 核心收益依赖冻结视觉 feature 是否保留动作相关几何与接触信息，latent subgoal 可能遗漏细粒度物理状态。
- 摘录没有给出具体 LIBERO 成功率、真实机器人任务和推理延迟数字，领先幅度需核查。
- 预训练数据规模包含数千小时视频，复现成本和数据配方敏感性可能较高。

#### 💭 结论与启发

LaWAM 对后续系统设计的启发是：world model 不一定要输出人眼可看的未来视频，机器人策略更需要可被动作头消费的未来表示。若做 VLA+WAM 复现，可以优先实现 latent feature prediction 和 subgoal-conditioned action head，而不是接入完整视频扩散模型。阅读 PDF 时尤其要确认 latent subgoal 是否可视化出稳定的动作相关变化，以及它在长 horizon、多物体遮挡或接触任务中是否比普通 history-conditioned VLA 更可靠。

#### 🔎 读 PDF 先核查

- LaWM 预测的 latent visual subgoal 是否真的编码可控未来变化，而不是学习到数据集里的平均视觉先验？
- latent action posterior 与 policy-predicted latent action 在训练和推理之间是否存在分布偏移？
- 230M LaWM 相比 pixel-space WAM 的效率优势在端到端机器人控制频率上有多大？

#### 📌 上传 PDF 后优先看

- 模型章节中的 latent action posterior、LaWM decoder 和 policy integration
- LIBERO 及真实机器人结果表，特别是 VLA、latent-action、pixel WAM 对比
- latent dynamics 可视化、推理延迟和组件消融章节

### [4]. Geometric Action Model for Robot Policy Learning [[HTML]](https://arxiv.org/html/2606.17046) [[PDF]](https://arxiv.org/pdf/2606.17046) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.17046`
* **Authors**: Jisang Han, Seonghu Jeon, Jaewoo Jung, René Zurbrügg, Honggyu An, Tifanny Portela, Marco Hutter, Marc Pollefeys, Seungryong Kim, Sunghwan Hong
* **Author Priority**: Standard
* **一句话结论**: 优先看：GAM 值得作为 LaWAM 的几何对照阅读，因为它认为 VLA/WAM 的关键缺口不是未来视频，而是 3D 几何底座。
* **关键词**: `几何基础模型` `3D manipulation` `World Action Model` `GFM` `LIBERO`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

通用机器人策略既要听懂语言，又要理解物体、相机和动作在三维世界中的交互。近年的 VLA 借助视觉语言模型获得语义先验，视频 WAM 借助生成模型获得时间先验，但许多方法仍主要运行在 2D 图像帧或 2D 派生 latent space 上。对接触丰富操作而言，这会留下空间歧义：同一张 RGB 图里，深度、可达性、遮挡、物体表面朝向和相机视角变化都可能影响动作选择。GAM 的动机是直接把 pretrained geometric foundation model 当作共享底座，让感知、未来预测和动作解码都在几何表征中完成。它入选不是因为一定比所有 VLA 更大，而是因为今天的 world model 讨论里，LaWAM 代表 latent future，GAM 代表 geometric future，两者共同指向“动作需要显式未来上下文”。

#### ⚙️ 核心方法

GAM 的核心做法是 repurpose pretrained geometric foundation model。摘录显示，它将 GFM 在中间层切开：浅层作为 observation encoder，深层继续作为几何与动作共享的解码 substrate；在切分层插入 causal future predictor，根据语言、proprioception 和历史上下文预测未来 latent tokens。这样，模型不是在外部另接一个视频生成器或几何模块，而是在同一个 GFM 内部把当前观测、未来几何和动作生成串起来。实现上，作者使用 DA3-Giant，并在 Track4World 上 fine-tune 作为 backbone；在 alternating attention 开始的某一层插入 12-layer causal predictor；语言由 frozen T5 encoder 提取 token；策略使用上下文 horizon 进行预训练和后训练，并从 proprioceptive states 预测 end-effector action chunks。训练上，GAM 先在 RoboCasa365、MimicGen 和 OpenX-Embodiment 的 784K 单臂机器人轨迹上预训练，再针对 benchmark post-train；同时冻结部分早期层和 depth head，并用仿真 ground-truth depth 监督深度。当前摘录中的若干符号和具体宽度缺失，因此不能补写层号、horizon 或 action chunk 长度。

#### 📊 实验与结果

实验摘录显示，GAM 在两个仿真 benchmark 上评估泛化，并在 LIBERO 上训练与测试，另有面向 out-of-distribution robustness 的评估设置。实现细节给出了较明确的训练来源：784K 单臂轨迹来自 RoboCasa365、MimicGen 和 OpenX-Embodiment，backbone 为 DA3-Giant fine-tuned on Track4World，语言编码器为 frozen T5。结论称 GAM 在广泛仿真和真实 benchmark 上取得更高准确率、更快推理和更强泛化，但提供摘录没有包含具体成功率、推理时间或真实机器人任务描述。因此实验部分的可信信息主要是评估覆盖方向和训练配置，而非可引用的数值结论。需要特别核查的是，depth supervision 使用 simulator ground truth 是否限制了真实部署，以及几何预测是否在真实 RGB 条件下仍然稳定。

#### ⚠️ 风险 / 保留意见

- 方法依赖大型 GFM、深度头和仿真 depth supervision，真实世界深度/几何误差可能传导到动作。
- 摘录没有给出数值结果，结论中的 superior accuracy 和 faster inference 需要查表验证。
- 预训练轨迹主要描述为单臂数据，迁移到双臂、灵巧手和强接触任务的边界尚不清楚。

#### 💭 结论与启发

GAM 提醒我，机器人 world model 不应只在时间维度上预测“未来会长什么样”，还要在三维几何上回答“哪里可接触、哪里被遮挡、动作会如何改变空间关系”。如果后续设计 VLA 系统，可以把几何 foundation model 看作比普通视觉 encoder 更强的状态表示层，再在中间层插入 causal predictor。和 LaWAM 对读时，重点应比较 latent visual subgoal 与 geometric latent token 哪个更适合作为 action head 的条件。

#### 🔎 读 PDF 先核查

- GFM 中间层切分的位置如何选择，是否有层位置消融证明该接口最适合动作预测？
- 未来几何 token 的监督来自哪里，真实世界没有 simulator depth 时如何保持稳定？
- GAM 的 faster inference 是相对视频 WAM、普通 VLA，还是相对其他几何策略？

#### 📌 上传 PDF 后优先看

- 模型结构图：GFM split、causal predictor、language/proprioception/action 接口
- 训练数据与监督章节，尤其是 depth supervision 和冻结层设置
- 仿真、OOD 与真实 benchmark 的结果表和推理速度对比

### [5]. Hierarchical Advantage Weighting for Online RL Fine-Tuning of VLAs from Sparse Episode Outcomes [[HTML]](https://arxiv.org/html/2606.17043) [[PDF]](https://arxiv.org/pdf/2606.17043) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.17043`
* **Authors**: Tongyan Fang, Siyuan Huang, Naiyu Fang, Ganlong Zhao, Zhongjin Luo, Jianbo Liu, Xiaogang Wang, Ying Dong, Hongsheng Li
* **Author Priority**: Standard
* **一句话结论**: 优先看：HABC 是今天 RL+VLA 最关键的一篇，因为它直面在线微调中“只有 episode 成败，却需要 transition 级训练信号”的核心难题。
* **关键词**: `在线 RL 微调` `VLA` `稀疏奖励` `双头 critic` `人工干预`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

预训练 VLA 通过示范学习可以获得较强泛化，但部署时仍会遇到示范覆盖不足、covariate shift 和错误累积。要让策略从自己的失败中改进，在线 RL fine-tuning 很重要；但真实机器人 rollout 往往只得到一个 episode 级二元结果：成功或失败。直接把这个稀疏标签压成单一 reward 或 advantage，会把两类反馈混在一起：当前状态是否仍有机会成功，即 viability；以及在已经能成功时是否完成得高效，即 efficiency。一旦策略具备基本成功能力，二元成功标签很难再指导它区分慢、绕、依赖干预的轨迹。HABC 入选，是因为它没有把 VLA RL 讲成通用 PPO/SAC 问题，而是针对 VLA action chunk、人工干预数据和稀疏 episode outcome 设计 transition-level behavior-cloning weight。

#### ⚙️ 核心方法

HABC 的基本设置是，机器人每步观察多视角图像、proprioception 和语言任务 prompt，执行固定 horizon 的 action chunk。作者定义 segment 为同一控制器下的最大连续区间，controller 可以是当前策略或人类；window 是从 segment 中抽取的固定长度训练样本；post-intervention policy execution suffix 是最后一次干预后的策略执行段。所有方法共享 flow-matching VLA actor，用带权 flow-matching loss 训练，权重来自 viability value 和 efficiency value。在线 fine-tuning 数据来自三类：离线 demonstrations、自主 rollouts 及其 episode outcome、人类干预数据。核心是 dual-head critic 和 intervention-aware credit assignment：viability head 在成功稀少时提供“这个状态是否还可完成”的信号，efficiency head 在成功可靠后鼓励更短或更有效轨迹；同时限制 outcome labels 只作用于 policy execution segments，以避免把人类干预造成的成功错误归功给策略。摘录说明部署 actor 不变，HABC 主要改变训练权重生成方式，这对接入现有 VLA 很重要。

#### 📊 实验与结果

实验是三项真实双臂任务：Pencil Pouch、Paper Bag、Snack Bag，均涉及多阶段双臂协调和可变形物体，包括插入、拉链、开袋、放瓶、放入多件物品和拉绳等。机器人平台为 ARX X5 双臂，观测包含三路 RGB：顶部 Intel RealSense D455 和两个腕部 Intel RealSense D405。动作空间为末端执行器坐标系，训练 chunk size 为 50，推理为 25；基础 VLA 来自一个预训练离线 checkpoint，并在 8 张 A800 上微调。基线包括 SFT、Imit-DAgger、Imit-Recap 等共五类。结论称 viability head、efficiency head 和防止 credit leakage 都有作用，但摘录没有提供成功率或轨迹长度数字，因此目前只能确认实验是真实机器人在线微调场景，不能量化领先幅度。

#### ⚠️ 风险 / 保留意见

- 方法依赖 critic 将 episode outcome 拆成 transition 权重，若 critic 校准差，可能放大错误信用分配。
- 真实实验任务数量为三项，虽然难度高，但跨平台和跨任务泛化仍需更多证据。
- 在线 RL 微调需要真实 rollout 和人类干预数据，部署成本与安全约束不可忽视。

#### 💭 结论与启发

HABC 对我后续看 VLA-RL 非常有参考价值：真正的问题不是“能不能用 RL”，而是如何把现实中廉价可得的成败标签、干预片段和示范数据转成稳定的 actor 监督。它也提示，在机器人在线学习中，成功本身至少包含 viability 和 efficiency 两层含义，训练目标需要分层。后续复现时，可先在现有 flow-matching VLA 上实现权重生成模块，检查是否无需改部署 actor 就能提升在线改进效率。

#### 🔎 读 PDF 先核查

- viability value 和 efficiency value 的训练标签分别如何从 episode outcome 与干预片段构造？
- 限制 outcome labels 到 policy execution segments 后，是否会丢失人类干预前关键失败状态的学习信号？
- HABC 对不同初始 VLA 能力是否敏感，弱策略和已接近成功的策略各自收益如何？

#### 📌 上传 PDF 后优先看

- 方法章节中的 dual-head critic、transition weight 和 intervention-aware credit assignment
- 三项真实双臂任务的在线学习曲线、成功率和轨迹长度结果
- 消融章节：去掉 viability、去掉 efficiency、去掉干预信用控制的影响

### [6]. Scaling Short-Term Memory of Visuomotor Policies for Long-Horizon Tasks [[VIP]] [[HTML]](https://arxiv.org/html/2606.16178) [[PDF]](https://arxiv.org/pdf/2606.16178) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.16178`
* **Authors**: Rutav Shah, Rajat Kumar Jenamani, Xiaohan Zhang, Lingfeng Sun, Roberto Martín-Martín, Yuke Zhu, Deva Ramanan, Karl Schmeckpeper
* **Author Priority**: Core VIP
* **一句话结论**: 优先看：PRISM 值得进入精选，因为它把 VLA/visuomotor policy 中常被忽略的短期记忆问题放到长时序任务核心位置。
* **关键词**: `短期记忆` `visuomotor policy` `部分可观测` `gated attention` `长时序任务`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

许多机器人任务不是当前图像就能决定动作：物体可能已经离开视野，步骤计数需要历史，等待一段时间后再关设备也需要记忆。人类认知中短期记忆覆盖从数秒到数分钟的经验，对日常动作非常重要；但很多 imitation-learned visuomotor policies 仍偏 myopic，只根据当前感知输入行动。对于长时序和部分可观测任务，这会导致策略无法记住先前拿过什么、放在哪里、已经完成了几步，进而在后续动作中出现重复、遗漏或语义错乱。PRISM 入选，是因为它关注的是通用机器人策略规模化后一定会遇到的 POMDP 问题：不是再加大当前帧 encoder，而是让策略有效利用最近交互历史，同时抑制历史中的伪相关。

#### ⚙️ 核心方法

PRISM 是 transformer-based visuomotor policy，目标是在固定 memory budget 内使用短期历史。摘录显示，在每个时间步，策略处理截断历史和任务描述；每个 observation 包含图像和 proprioceptive state，过去动作也作为 token 输入。图像由 image encoder 编码成 visual tokens，proprioception 和 past actions 分别经各自 encoder 变成 token，指令由 pretrained text encoder 得到 language tokens。所有 token 按时间顺序打包，并使用 causal mask；位置编码同时保留时间结构和图像空间结构。Transformer 的 context window 就是短期记忆，最后一个 observation token 的隐藏状态进入 action head，输出动作分布参数。摘要还提到两个关键组件：gated attention 用于选择性过滤检索到的信息、压制无关历史细节；另一个组件在提供摘录中没有完整展开，但主题是 scaling short-term memory。当前摘录只能确认 token 化历史、causal transformer、gated attention 的总体思路，不能确认具体门控公式、训练损失或 benchmark 全貌。

#### 📊 实验与结果

实验摘录较少，只能确认推理时策略以语言 token 作为静态 prefix，观察和动作 token 随时间累积；达到 horizon budget 后，只保留最近若干步历史。评估关注对新物体位置的泛化，以及长时序任务中的历史利用能力。结论提到 ReMemBench 上绝对成功率处在一个区间内，但具体数值在用户提供摘录中缺失，因此不能引用。作者将低绝对成功率解释为长时序任务本身困难，而不是记忆机制无效，并认为未来需要同时改进感知、控制和记忆。由于摘录没有列出 baseline、任务数和消融结果，当前只能把它视作“短期记忆 benchmark 与架构方向”的强信号，具体性能主张需要 PDF 表格核查。

#### ⚠️ 风险 / 保留意见

- 摘录缺少完整实验数字和基线细节，当前难以判断 gated attention 的实际收益幅度。
- 短期 memory window 只保留最近步骤，面对跨天或长期任务仍需持久记忆机制。
- 历史 token 增长会带来计算和注意力干扰，门控是否足以抑制伪相关需要消融验证。

#### 💭 结论与启发

PRISM 的价值在于提醒 VLA 读者，很多失败不是语义理解失败，而是部分可观测条件下缺少可用历史。后续做长时序 manipulation 时，可以把短期交互历史当作一等输入，包括过去图像、proprioception 和动作，而不是只在高层 planner 里维护状态。上传 PDF 后，我会重点查 gated attention 的设计与消融，因为“更多历史”不一定更好，关键是模型能否过滤无关记忆并在动作头处使用真正相关的过去事件。

#### 🔎 读 PDF 先核查

- gated attention 如何判断哪些历史 token 应被保留，它是否有显式监督或完全端到端学习？
- memory budget 增大时，性能是持续提升、饱和，还是因为伪相关而下降？
- ReMemBench 的任务是否真正需要记忆，还是可以被当前视觉线索或数据偏置部分解决？

#### 📌 上传 PDF 后优先看

- PRISM 架构章节：历史 token、causal mask、gated attention 和 action head
- ReMemBench 任务定义、baseline 设置和成功率表
- memory length、无 gated attention、仅当前帧策略等消融实验

## Watchlist

### [W1]. Retrieve, Don't Retrain: Extending Vision Language Action Models to New Tasks at Test Time [[HTML]](https://arxiv.org/html/2606.15631) [[PDF]](https://arxiv.org/pdf/2606.15631)
* **Paper ID**: `2606.15631`
* **Authors**: Jeongeun Park, Juhan Park, Taekyung Kim, Sungjoon Choi, Dongyoon Han, Sangdoo Yun
* **Author Priority**: Standard
* **为什么还值得留意**: ReCAP 进入 watchlist，因为它提出“retrieve, don't retrain”的 VLA 新任务适配范式：冻结策略，通过追加 human-hand 或便宜 embodiment 的 pool-side demonstrations，在测试时检索任务进展来扩展能力。它没有进最终精选，主要是因为今天的最终 6 篇已经覆盖了更基础的触觉、Sim2Real、world model、RL 和记忆主线；ReCAP 更像是 retrieval-augmented adaptation 的重要旁支，需要进一步核查 cross-embodiment 检索是否在真实机器人上足够稳。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)

### [W2]. PO-PDDL: Learning Symbolic POMDPs from Visual Demonstrations for Robot Planning Under Uncertainty [[VIP]] [[HTML]](https://arxiv.org/html/2606.15654) [[PDF]](https://arxiv.org/pdf/2606.15654)
* **Paper ID**: `2606.15654`
* **Authors**: Wenjing Tang, Xuanjin Jin, Yuan Liu, Renming Huang, Cewu Lu, Panpan Cai
* **Author Priority**: Core VIP
* **为什么还值得留意**: PO-PDDL 值得 watchlist，尤其因为作者中有 Cewu Lu，且它把 VLA 低层技能、VLM 感知和符号 POMDP planning 连接起来，面向部分可观测与随机执行的真实任务规划。没有进入最终精选，是因为它更偏规划表示和模型学习，而不是今天主线里的 VLA 动作生成、Sim2Real 或 world/action model；但若后续关注 VLA+planner，它应优先补读。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. EgoPhys: Learning Generalizable Physics Models of Deformable Objects from Egocentric Video [[VIP]] [[HTML]](https://arxiv.org/html/2606.16202) [[PDF]](https://arxiv.org/pdf/2606.16202)
* **Paper ID**: `2606.16202`
* **Authors**: Hyunjin Kim, Ri-Zhao Qiu, Guangqi Jiang, Xiaolong Wang
* **Author Priority**: Core VIP
* **为什么还值得留意**: EgoPhys 进入 watchlist，因为 Xiaolong Wang 参与，且它从 egocentric RGB-only video 学可变形物体物理数字孪生，和 SimWeaver 的可变形 Sim2Real 形成互补。它未进最终精选，是因为当前摘录更强调物理重建、数字孪生和规划转移，而不是直接 VLA policy 训练；但对可变形操作的 world model 和仿真评估非常值得跟踪。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. ATHENA: Accelerated Multi-Task Heterogeneous Influence Functions for Robot Data Curation [[HTML]](https://arxiv.org/html/2606.16208) [[PDF]](https://arxiv.org/pdf/2606.16208)
* **Paper ID**: `2606.16208`
* **Authors**: Tao Xu, Jiaxin Wang, Runhao Zhang, Jiayi Guan, Xianchao Zeng, Weixi Song, Xinyu Zhou, Zhetao Chen, Guang Chen, Yong-Lu Li
* **Author Priority**: Standard
* **为什么还值得留意**: ATHENA 进入 watchlist，因为它处理 VLA 数据质量和 demonstration curation，且给出了面向 billion-parameter multitask VLA 的 influence-function 加速思路，摘录中还明确出现 313.4 倍 influence computation speedup。它没有进入最终精选，是因为它更偏数据筛选基础设施，不直接解决动作闭环、物理建模或在线 RL；不过若后续要做大规模 VLA fine-tuning 数据治理，它可能非常实用。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
