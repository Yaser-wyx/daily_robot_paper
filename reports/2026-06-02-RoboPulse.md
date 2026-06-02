# RoboPulse | 2026-06-02

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 197 papers scanned · 10 shortlisted · 5 editor's picks

今天的主线很清楚：VLA 正在从“直接把视觉语言映射成动作”转向带预测、生成、筛选和安全接口的行动系统。最终精选覆盖了五条互补路线：统一视频-动作世界模型、可组合数据合成、跨任务跨具身 VLA 基座、离散扩散动作解码，以及面向动态物体的 latent-space 预测包装器。它们入选不是因为都给出了完整闭环答案，而是因为分别击中了机器人学习当前最硬的瓶颈：数据规模、时延、动作接口、测试时推理和 sim2real 迁移。VIP 作者里，Jianlan Luo 的 τ0-WM、Yue Wang 的 RoboDream、Jiangmiao Pang 参与的 Discrete Diffusion VLA 值得优先跟踪；它们分别代表了世界模型、生成式数据引擎和统一动作解码架构的关键方向。

## 今日信号

- VLA 的竞争焦点正在从单步策略精度转向“预测未来再行动”的系统能力，世界模型开始成为动作生成、动作评估和部署时重规划的共同接口。
- Sim2Real 数据路线出现明显分化：一类用真实机器人和异构视频预训练扩大覆盖面，另一类用可控生成模型或 3DGS 混合仿真合成可训练演示。
- 动作解码不再只是工程头部选择，离散扩散、action chunk 执行策略、passivity shield 和 latent 预测都在重写 VLA 到控制器之间的契约。

## Historical Rediscovery

- **Paper**: VLA-Pro: Cross-Task Procedural Memory Transfer for Vision-Language-Action Models [[PDF]](https://arxiv.org/pdf/2605.29562)
  - **Paper ID**: `2605.29562`
  - **来源日期**: 2026-05-29
  - **当时可能被低估的信号**: 当时因只有摘要回退而降级，但 watchlist note 已经点出 RoboTwin、RLBench 和 real-world manipulation 泛化如果扎实，就可能升级为重点；这个“推理时检索融合 procedural memory”的信号容易被低估。
  - **为什么现在值得再看**: 对 VLA、RL+VLA 和长时程任务很相关：如果不同任务经验能以 adapter memory 形式组合，它可能提供比单一端到端策略更可维护的扩展路线。
  - **建议动作**: 加入精读
  - **关键词**: `VLA` `procedural memory` `cross-task generalization` `LoRA adapters` `real-world manipulation`
- **Paper**: 3DVLA: Enhancing Vision-Language-Action Models via 3D Spatial and Instance Understanding [[HTML]](https://arxiv.org/html/2605.29416) [[PDF]](https://arxiv.org/pdf/2605.29416)
  - **Paper ID**: `2605.29416`
  - **来源日期**: 2026-05-29
  - **当时可能被低估的信号**: 当时被系统性主线挤出精选，但 note 中提到的 multi-view spatial fusion、3D instance module、occlusion geometry prediction，以及 LIBERO-Plus zero-shot success 信号，都比普通 3D 感知补丁更贴近 VLA 部署瓶颈。
  - **为什么现在值得再看**: 对 VLA 和 Sim2Real 都值得再看：真实机器人失败常来自空间、遮挡和实例级误识别，3D-aware VLA 表征可能是 world/action model 接入真实场景前的关键前置模块。
  - **建议动作**: 加入精读
  - **关键词**: `VLA` `3D spatial understanding` `instance grounding` `occlusion` `Sim2Real`
- **Paper**: ConsisVLA-4D: Advancing Spatiotemporal Consistency in Efficient 3D-Perception and 4D-Reasoning for Robotic Manipulation [[HTML]](https://arxiv.org/html/2605.05126) [[PDF]](https://arxiv.org/pdf/2605.05126)
  - **Paper ID**: `2605.05126`
  - **来源日期**: 2026-05-07
  - **当时可能被低估的信号**: 当时因为核心模块和实验细节证据不足而未入选，但“spatiotemporal consistency”和“future reasoning for robotic manipulation”本身是 VLA 从静态视觉条件反射走向预测式动作建模的关键信号。
  - **为什么现在值得再看**: 现在值得从 WAM 角度重读：如果它真的把未来状态推理接到操作策略中，就比普通 3D VLA 更接近 action-conditioned world modeling。
  - **建议动作**: 快速浏览
  - **关键词**: `VLA` `4D reasoning` `future reasoning` `spatiotemporal consistency` `World Action Model`
- **Paper**: ExoActor: Exocentric Video Generation as Generalizable Interactive Humanoid Control [[HTML]](https://arxiv.org/html/2604.27711) [[PDF]](https://arxiv.org/pdf/2604.27711)
  - **Paper ID**: `2604.27711`
  - **来源日期**: 2026-05-01
  - **当时可能被低估的信号**: 当时因多环节限制和系统可行性展示属性而降级，但“exocentric video generation as interactive humanoid control”这个中间表示信号与 WAM/VLA robustness 讨论高度同频。
  - **为什么现在值得再看**: 对 World Model、World Action Model 和 humanoid long-horizon control 值得再看：视频生成如果能承载未来交互状态，可能成为语言目标与低层动作之间的可视化预测层。
  - **建议动作**: 继续跟踪
  - **关键词**: `World Model` `World Action Model` `humanoid control` `video generation` `long-horizon control`
- **Paper**: ParkingWorld: End-to-End Autonomous Parking Reinforcement Learning from Corrective Experience in 3DGS Simulation [[HTML]](https://arxiv.org/html/2605.25029) [[PDF]](https://arxiv.org/pdf/2605.25029)
  - **Paper ID**: `2605.25029`
  - **来源日期**: 2026-05-27
  - **当时可能被低估的信号**: 当时因自动泊车场景与通用操作主线距离较远而被压低，但 note 中已有 5 个 3DGS 停车场景、239 个车位、每方法 200 次 trial 这类相对具体的实验设置信号。
  - **为什么现在值得再看**: 虽然不是 VLA 操作论文，但对 Sim2Real 与 RL+视觉策略很有参考价值：3DGS 场景重建加 corrective experience 的路线，可能迁移到机器人操作的仿真数据生成与闭环修正。
  - **建议动作**: 快速浏览
  - **关键词**: `Sim2Real` `reinforcement learning` `3D Gaussian Splatting` `corrective experience` `closed-loop evaluation`

## Editor's Picks

### [1]. $τ_0$-WM: A Unified Video-Action World Model for Robotic Manipulation [[VIP]] [[HTML]](https://arxiv.org/html/2606.01027) [[PDF]](https://arxiv.org/pdf/2606.01027) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.01027`
* **Authors**: Pengfei Zhou, Shengcong Chen, Di Chen, Jiaxu Wang, Rongjun Jin, Bingwen Zhu, Yike Pan, Songen Gu, Kuanning Wang, Shufeng Nan, Xingyu Qiu, Chenhao Qiu, Pu Yang, Yunuo Cai, Jianxiong Gao, Yifan Li, Yanwei Fu, Xiangyu Yue, Zhi Chen, Jianlan Luo
* **Author Priority**: Core VIP
* **一句话结论**: 优先看；τ0-WM 把动作生成、未来视频预测和动作评估放进同一个视频扩散世界模型，是今天最接近“VLA + world model + test-time reasoning”完整范式的一篇。
* **关键词**: `video-action world model` `VLA` `test-time computation` `multi-view manipulation` `heterogeneous pretraining`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

机器人操作的核心难点不只是根据图像和语言选一个动作，而是要在真实执行前判断这个动作会把场景推向哪里。传统 VLA 或模仿学习策略通常把未来压缩进动作输出本身，缺少显式的后果预测；视频模型能预测视觉变化，但未必能输出某个具体机器人可执行的连续动作。τ0-WM 试图把这两边合起来：既学习多视角、语言条件下的动作块，又能用动作条件视频模拟器 rollout 候选动作的未来结果。这对长时程、接触密集、多阶段任务尤其重要，因为失败往往来自中间状态偏差，而不是初始语义理解错误。论文还强调异构数据来源，包括真实机器人遥操作、UMI-style、人类 egocentric 交互视频和面向仿真的 rollout 轨迹，动机是让模型同时吸收可执行动作和更宽的物理变化先验。

#### ⚙️ 核心方法

当前摘录可以确认，τ0-WM 建在共享的视频扩散 backbone 上，并提供两个互补接口。第一是 video action model：输入多视角观测、语言指令和机器人状态，联合预测未来视觉 latent 与连续 action chunks，因此动作不是孤立 token，而是和预测到的未来视觉演化绑定。第二是 action-conditioned video simulator：给定候选 action chunks，roll out 多视角未来，并预测 dense task-progress scores，用于评估或修正动作。这个设计的关键新意在于，它没有把 policy、video prediction、action scoring 做成三个松散模块，而是用同一未来预测框架共享表征。训练侧则利用异构交互数据，使模型既能从机器人轨迹学到 embodiment-specific 可执行动作，也能从 UMI-style 和 egocentric 视频中获得更广的接触与物体运动经验。部署侧摘录提到 test-time computation，会把候选动作选择和 rectification 纳入闭环执行；但具体采样数、评分损失、扩散调度和动作修正细节需要看 PDF 才能确认。

#### 📊 实验与结果

实验聚焦 long-horizon、fine-grained 的真实机器人操作任务，目标问题包括 VAM policy 性能、异构预训练数据是否提升下游表现，以及部署时计算是否进一步改善闭环执行。摘录明确提到三类机器人 embodiment：AGIBOT-G01、ARX manipulators 和双臂 Franka 系统；任务包括语言条件、多视角的 packing 与 assembly。主要指标是 task success rate，对比对象包括代表性 policy 和 video-action baseline，其中点名了 Fast-WAM；test-time reasoning 还对比 standard execution、classifier-free guidance 和 Action Coherence Guidance。摘录没有给出具体成功率数字，因此只能判断其证据形态是多机器人、多任务、真实机器人部署加数据组成与测试时计算消融，不能复述未给出的表格结论。

#### ⚠️ 风险 / 保留意见

- 视频扩散世界模型的推理成本可能较高，部署时 action selection/rectification 的实时性需要重点核查。
- 异构数据带来的收益需要区分来自机器人动作数据、egocentric 视频先验还是任务分布扩大，摘录不足以判断因果贡献。
- dense task-progress score 是否能可靠对应真实任务成功，尤其在长时程接触任务中可能存在奖励代理偏差。

#### 💭 结论与启发

这篇最值得作为后续系统设计参考：VLA 不一定要在一次前向里直接承诺动作，而可以把动作作为可被想象、评分和修正的候选。复现时我会先缩小到单机器人多视角任务，验证“联合预测视觉 latent + action chunk”是否真的优于只加视频预测辅助损失。选题上，它提示一个很有价值的问题：世界模型在机器人里不只是生成视频，而是要提供与控制接口兼容的未来证据。

#### 🔎 读 PDF 先核查

- action-conditioned video simulator 的 dense task-progress score 是如何标注或学习的，是否依赖任务特定监督？
- VAM 联合预测未来视觉 latent 和连续 action chunks 时，两个目标之间是否存在训练冲突，论文如何平衡？
- 部署时 rectification 到底修改动作块的哪一部分，是否能在真实机器人控制频率下稳定运行？

#### 📌 上传 PDF 后优先看

- 模型架构与共享视频扩散 backbone 章节
- 异构数据组成、预训练配方与 ablation 实验
- 真实机器人部署时 action selection/rectification 的实验设置和失败案例

### [2]. RoboDream: Compositional World Models for Scalable Robot Data Synthesis [[VIP]] [[HTML]](https://arxiv.org/html/2606.02577) [[PDF]](https://arxiv.org/pdf/2606.02577) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.02577`
* **Authors**: Junjie Ye, Rong Xue, Basile Van Hoorick, Runhao Li, Harshitha Rajaprakash, Pavel Tokmakov, Muhammad Zubair Irshad, Vitor Guizilini, Yue Wang
* **Author Priority**: Core VIP
* **一句话结论**: 优先看；RoboDream 把生成式世界模型做成 embodiment-centric 数据引擎，直接回应机器人数据稀缺和 sim2real 可用性问题。
* **关键词**: `robot data synthesis` `video diffusion` `embodiment-centric world model` `DROID` `sim2real`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

机器人学习长期受限于高质量交互数据，而遥操作收集既贵又慢，还难以覆盖新物体、新场景和新视角。单纯用视频扩散做视觉增强通常只能改变表面外观，不能保证机器人本体运动合理；如果生成过程中出现 embodiment hallucination，合成演示反而会教坏策略。RoboDream 的动机是把世界模型从“好看的视频生成器”推进到“可训练机器人策略的数据合成器”：生成必须锚定机器人运动、场景先验和物体布局，才能在视觉真实的同时保持动作物理可行。它入选的原因在于问题非常关键：如果有限真实数据能通过可控世界模型扩展为可用演示，VLA 和 imitation learning 的 scaling bottleneck 会被实质性缓解。

#### ⚙️ 核心方法

摘录显示 RoboDream 的核心是面向具身合成的 multi-modal video diffusion transformer，并从 Cosmos-Predict2 2B foundation model fine-tune。方法把 noisy video latent、VAE 编码的 rendered robot motion video，以及编码后的 scene prior 拼接成多模态输入；由于背景大多静态，scene prior image 会沿时间维展开成静态视频，为每个时间步提供像素对齐的环境参考。为支持多视角生成，论文采用 multi-view tokenization，而不是简单空间拼接不同相机画面，以降低多相机之间的空间歧义。它还强调生成可以覆盖 novel objects、novel scenes 和 novel viewpoints，并提出 retrieval and rebirth 与 prop-free teleoperation 两种部署模式。当前摘录只能确认这些模块和训练设置的大框架，具体如何从生成视频转成 policy training episode、如何约束动作一致性、如何处理物体交互失败，需要 PDF 中方法细节核查。

#### 📊 实验与结果

实验在真实世界四个日常操作任务上评估：Put Marker into Bowl、Remove Marker from Bowl、Put Cube into Cup、Wipe Table with Towel。平台是与 DROID 设置一致的 Franka Panda，所有真实评估每个 policy 做 20 次 rollout；pick-and-place 任务允许 partial success，例如抓取成功但放置失败计半分。训练侧，RoboDream 从 Cosmos-Predict2 2B fine-tune，并使用约 40k 条带相机标定的 DROID episode，在 2 个节点、每个 8 张 NVIDIA A100 上训练一周。摘录说明实验关注生成数据是否提升策略、prop-free teleoperation 的效率、数据引擎 scaling 和 zero-shot 泛化，但未给出最终成功率表，因此这里只能确认实验覆盖面和评估协议，不能夸大结果幅度。

#### ⚠️ 风险 / 保留意见

- 生成视频的物理可执行性仍需通过动作、接触和轨迹一致性验证，不能只看 photorealism。
- 训练成本较高，2 节点 8 A100 一周的设置会影响复现门槛。
- 真实评估任务数量有限，四个 everyday manipulation 任务是否代表更复杂长时程技能仍需谨慎。

#### 💭 结论与启发

RoboDream 对我的最大启发是：机器人数据合成的关键不是“换背景”或“扩图像”，而是把本体运动作为生成锚点，让视觉、场景和动作共同成立。系统设计上，它适合和 VLA fine-tuning pipeline 结合，先把少量真实遥操作转成可重生、可换物体和视角的数据池。复现时不必一开始追求完整多视角 photorealistic 生成，可以先验证 rendered robot motion video + scene prior 是否比普通视频增强更能提升 policy。

#### 🔎 读 PDF 先核查

- rendered robot motion video 在生成中提供的是完整动作轨迹、关键帧还是低层姿态序列？
- RoboDream 生成的数据进入 policy 训练时，动作标签如何与生成画面严格对齐？
- prop-free teleoperation 相比传统遥操作节省的数据成本，是通过更少实物道具、更少人工时间，还是更高数据复用率实现的？

#### 📌 上传 PDF 后优先看

- multi-modal video diffusion transformer 与 multi-view tokenization 章节
- 生成数据到 policy fine-tuning 的数据接口和质量过滤流程
- 四个真实任务的 scaling、zero-shot 与 ablation 表格

### [3]. Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments [[VIP]] [[PDF]](https://arxiv.org/pdf/2605.30280) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.30280`
* **Authors**: Qiuyue Wang, Mingsheng Li, Jian Guan, Jinhui Ye, Sicheng Xie, Yitao Liu, Junhao Chen, Zhixuan Liang, Jie Zhang, Xintong Hu, Xuhong Huang, Pei Lin, Junyang Lin, Dayiheng Liu, Shuai Bai, Jingren Zhou, Jiazhao Zhang, Haoqi Yuan, Gengze Zhou, Hang Yin, Ye Wang, Yiyang Huang, Zixing Lei, Wujian Peng, Delin Chen, Yingming Zheng, Jingyang Fan, Xianwei Zhuang, Xin Zhou, Haoyang Li, Anzhe Chen, Tong Zhang, Xuejing Liu, Yuchong Sun, Ruizhe Chen, Zhaohai Li, Chenxu Lü, Zhibo Yang, Tao Yu, Xionghui Chen
* **Author Priority**: Core VIP
* **一句话结论**: 优先看但要保守读；Qwen-VLA 的价值在于尝试把操作、导航、轨迹生成等异构具身决策统一到一个 Qwen 系 VLA 基座，但当前只有摘要回退信息。
* **关键词**: `unified VLA` `Qwen` `DiT action decoder` `heterogeneous pretraining` `embodied foundation model`
* **证据来源**: Abstract fallback

#### 📖 背景与动机

具身智能研究常被任务边界切碎：操作模型、导航模型、仿真策略和轨迹预测模型各自训练，导致能力难以迁移到新任务、新环境和新机器人。Qwen-VLA 的问题意识是，能否像视觉语言模型统一感知、理解和推理一样，把不同 embodied decision-making 问题也统一到一个 vision-language-action model 中。这对 VLA 方向非常重要，因为机器人 foundation model 的关键不只是单任务成功率，而是跨数据源、跨任务语义和跨 embodiment 的表示共享。摘要提到它扩展 Qwen 的视觉语言建模栈，从 perception、understanding、reasoning 走向 continuous action 与 trajectory generation，这说明论文更偏基座模型路线，而不是单个操作技巧或单一 benchmark 优化。

#### ⚙️ 核心方法

当前摘录只能确认 Qwen-VLA 的方法轮廓：它以 Qwen 的 vision-language modeling stack 为基础，并通过 DiT-based action decoder 扩展到连续动作和轨迹生成。训练上使用 large-scale joint pretraining recipe，数据源包括机器人操作轨迹、人类 egocentric demonstrations、合成仿真数据、vision-and-language navigation data、trajectory-centric supervision 和辅助视觉语言任务。这个配方的潜在新意在于把多种具身监督统一成一个模型训练问题，让视觉语言推理 token 与动作/轨迹输出之间共享语义基础。由于没有 HTML 方法段，无法确认动作表示是 chunk、waypoint、continuous control 还是多头输出，也无法确认 DiT decoder 如何接入 Qwen backbone、是否冻结部分参数、如何平衡 navigation 与 manipulation 数据。对这篇需要特别避免过度解读：摘要足以说明方向和架构意图，不足以判断实现细节优劣。

#### 📊 实验与结果

摘要回退信息没有给出具体实验设置、benchmark 名称、机器人平台、对比方法或量化结果。因此目前只能推断论文会围绕跨任务、跨环境、跨 embodiment 的统一建模进行评估，但不能声称其在某个 benchmark 上超过特定 baseline。它之所以进入最终精选，是因为统一 VLA 基座模型本身对今天主题有战略价值：如果一个模型能同时处理 manipulation trajectories、egocentric demonstrations、synthetic simulation、VLN 和 trajectory-centric supervision，那么它可能成为后续动作解码、world model wrapper 或 sim2real 数据引擎的底座。上传 PDF 后必须优先核查实验覆盖是否真的支撑“unifying”这一主张。

#### ⚠️ 风险 / 保留意见

- 当前只有摘要，缺少方法和实验细节，所有关于实现效果的判断都应降级为待验证假设。
- 异构联合预训练容易出现数据源不平衡，模型可能在主流数据域表现强但跨 embodiment 泛化有限。
- 统一模型若缺少清晰动作接口，可能很难被直接部署到真实机器人闭环控制。

#### 💭 结论与启发

这篇适合作为“VLA 基座模型路线”的参照，而不是马上作为可复现系统。后续阅读重点不是看它是否在单个任务刷榜，而是看它如何定义统一动作空间、如何把导航和操作监督放进同一训练目标，以及 DiT action decoder 是否真正解决连续控制问题。对选题而言，它提示可以把世界模型和动作解码研究建立在更通用的 VLM/VLA backbone 上，而不是每个任务重新训练策略。

#### 🔎 读 PDF 先核查

- DiT-based action decoder 输出的动作或轨迹格式是什么，能否覆盖不同机器人 embodiment？
- joint pretraining 中 manipulation、navigation、egocentric 和 synthetic 数据如何采样与加权？
- 模型是否展示了跨任务或跨机器人零样本/少样本迁移，而不只是多数据集联合训练？

#### 📌 上传 PDF 后优先看

- 模型架构中 Qwen backbone 与 DiT action decoder 的连接方式
- 联合预训练数据配方、任务格式统一和损失设计
- 跨任务、跨环境、跨 embodiment 泛化实验与消融

### [4]. Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies [[VIP]] [[HTML]](https://arxiv.org/html/2508.20072) [[PDF]](https://arxiv.org/pdf/2508.20072) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2508.20072`
* **Authors**: Zhixuan Liang, Yizhuo Li, Tianshuo Yang, Chengyue Wu, Sitong Mao, Liuao Pei, Tian Nian, Shunbo Zhou, Xiaokang Yang, Jiangmiao Pang, Yao Mu, Ping Luo
* **Author Priority**: Core VIP
* **一句话结论**: 优先看；Discrete Diffusion VLA 把扩散式动作生成收回统一 transformer 内部，是动作解码架构上很值得跟踪的一篇。
* **关键词**: `discrete diffusion` `action decoding` `VLA transformer` `action chunk` `adaptive demasking`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

现有 VLA 动作解码大致有两条路线：一种像语言模型一样自回归地产生离散动作 token，结构统一但动作质量和顺序依赖可能受限；另一种在 VLM backbone 外接 MLP、连续扩散或 flow-matching action head，动作建模更强，但会把感知、语言和动作生成的信息通路切开。Discrete Diffusion VLA 针对的正是这个矛盾：机器人动作需要并行、多维、可逐步修正的生成机制，但 VLA 又需要保持统一 backbone 和视觉语言预训练先验。离散扩散提供了折中方案：动作被离散化为 token chunk，通过 mask/demask 的方式逐步细化，既避免固定左到右顺序，又保留 transformer 内部的联合注意力。

#### ⚙️ 核心方法

方法输入图像观测和语言指令，支持单视角或多视角，并扩展 VLM backbone 生成动作。每个 action chunk 被表示为长度为 L 的离散 action token 序列，每个 token 来自离散 bin vocabulary，并额外加入 [MASK] token。训练时通过离散扩散前向过程随机 mask 动作 token，统一 transformer 同时 attend visual features、language embeddings 和部分未 mask 的 action tokens，学习逐步恢复被 mask 的动作。推理时模型根据 denoising schedule 逐步 demask，形成 adaptive decoding order：高置信动作 token 可以先确定，低置信部分继续 refine。摘录还提到 secondary re-masking，意味着模型可能会重新遮蔽不可靠 token 以修正动作。相对外接连续扩散头，这里的新意是动作扩散仍在统一 transformer backbone 内完成，并共享 cross-entropy objective 和 token vocabulary，从而试图保护预训练 VLM priors。

#### 📊 实验与结果

实验覆盖三个机器人设置：Franka Panda 上的 LIBERO，包含 Spatial、Object、Goal、Long 四个 suite，每个 suite 10 个任务、500 个 demo；Google Robot 上的 SimplerEnv-Fractal，报告 Visual Matching 和 Variant Aggregation；WidowX Robot 上的 SimplerEnv-Bridge，用于和 BridgeData-V2 对齐的 real-to-sim 评估。输入包括 RGB、语言和可选末端位姿 proprioception，不使用 depth、affordance 或其他辅助输入。对比覆盖 AR token decoders、separate MLP action decoders、continuous diffusion/flow-matching heads，以及 OpenVLA、Octo、HPT、TraceVLA、SpatialVLA 等相关方法。摘录没有给出具体得分，因此只能确认它的实验设计覆盖了动作解码范式比较和多平台 benchmark，不能引用胜幅。

#### ⚠️ 风险 / 保留意见

- 动作离散化的 bin 设计会影响精度，尤其对高频、接触敏感或连续力控任务可能有限制。
- 统一 cross-entropy 目标是否足以学习复杂连续控制，需要看真实机器人或 long-horizon 失败案例。
- adaptive decoding 与 secondary re-masking 的推理开销和稳定性需要核查。

#### 💭 结论与启发

这篇对后续 VLA 架构选择很有用：动作头不一定要在 backbone 外部做连续扩散，离散扩散可能提供更统一、更可扩展的动作生成接口。复现上，可以先在 LIBERO 或 SimplerEnv 做小规模对照，把 AR、外接 diffusion head 和 backbone 内 discrete diffusion 放在同一 VLM 上比较。系统设计上，它提醒我关注“动作生成顺序”本身，高置信维度先定、低置信维度后 refine，可能比固定 token 顺序更适合多自由度机器人。

#### 🔎 读 PDF 先核查

- 动作 token 的离散 bin 如何定义，是否按维度独立量化，是否会损失精细控制能力？
- secondary re-masking 的触发条件是什么，能否显著减少错误动作 token 传播？
- 与连续 diffusion head 相比，统一 backbone 内训练是否真的改善 OOD robustness，消融如何证明？

#### 📌 上传 PDF 后优先看

- 离散动作扩散公式、mask/demask schedule 与 secondary re-masking 推理流程
- LIBERO、SimplerEnv-Fractal、SimplerEnv-Bridge 的对比表和消融
- 动作离散化粒度、token vocabulary 与控制频率设置

### [5]. Intercepting the Future: Latent-Space Predictive World Model for Dynamic VLA Manipulation [[HTML]](https://arxiv.org/html/2606.02486) [[PDF]](https://arxiv.org/pdf/2606.02486) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.02486`
* **Authors**: Shahram Najam Syed, Arthur Jakobsson, Haoran Hao, Jeffrey Ichnowski
* **Author Priority**: Standard
* **一句话结论**: 优先看；AHEAD 用小型 latent world model 包装冻结 VLA，专门补动态物体场景中的感知-行动时延，是很实用的 world-action 接口思路。
* **关键词**: `latent world model` `dynamic manipulation` `frozen VLA` `optical flow` `adaptive horizon`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

多数 VLA 在静态操作上泛化不错，但默认世界在观察和执行之间基本不变；一旦物体在传送带、抛接、滚动或碰撞后继续运动，当前观测很快过期，机器人执行的动作就落在错误位置。AHEAD 的动机非常直接：不要要求重训整个 VLA，而是在冻结的 VLA 前面加一个 motion-aware latent world model，让动作解码器看到预测后的未来状态。这个问题对真实部署很重要，因为很多家庭、工厂和人机交互场景都不是静止桌面操作，缩短控制环路也无法完全消除延迟。论文把人类式的 anticipatory internal model 转成工程接口：预测未来视觉 token，再让原 VLA 按未来而不是过时观察行动。

#### ⚙️ 核心方法

AHEAD 是一个 predict-then-act wrapper，核心是训练一个小型世界模型，在 VLA 的 feature space 中预测未来 patch tokens，而不是在像素空间生成完整视频。它使用 optical flow 得到每个 token 的速度和加速度条件，使预测显式感知运动趋势；同时引入 language-and-motion saliency mask，把预测容量集中在任务相关、运动相关 patch 上，避免浪费在背景或无关区域。模型会向前 rollout 一个 adaptive horizon，并在预测不确定性超过阈值时停止，随后把预测后的 latent observation 输入冻结的 action decoder。摘录明确强调 backbone 是未修改的 OpenVLA，说明方法目标是低侵入地增强已有 VLA，而不是重新训练端到端动态策略。需要注意的是，具体 wrapper 参数量、OpenVLA 尺寸和百分比结果在摘录中被截断，不能引用；但方法接口已经足够清楚：latent future prediction + saliency + uncertainty-gated horizon + frozen VLA action decoding。

#### 📊 实验与结果

实验包括仿真和真实机器人。仿真使用自定义 MuJoCo 环境与 Franka Emika Panda，覆盖四类动态：恒速运输，如 conveyor、beam、pole push with red cup；重力驱动，如 rolling ball；反应式接触，如 air hockey、ballistic catching；以及碰撞后的混沌动态，如 multi-deflection pinball、occlusion deflection、plinko drop。真实平台是 UFactory xArm 7，配固定第三方 RGB 相机和平行夹爪，评估五个动态任务：静态物体放到移动传送带箱、静态箱接收移动物体、乒乓球拍拦截、停止滚动球、机械发射器抛射物抓取。摘录还提到 speed-sensitivity sweep 和组件消融，但具体成功率数字被截断，因此只能确认任务覆盖和动态类型，不能复述百分比结论。

#### ⚠️ 风险 / 保留意见

- latent patch token 预测依赖 optical flow，遮挡、反光或快速碰撞可能导致速度/加速度估计不稳。
- 冻结 VLA 的 action decoder 可能仍不具备动态拦截所需的控制技能，预测未来状态只能部分弥补。
- adaptive horizon 的不确定性阈值若校准不当，可能过早停止预测或在高不确定未来上行动。

#### 💭 结论与启发

AHEAD 的启发在于，world model 可以作为已有 VLA 的轻量前置模块，而不必总是重训一个庞大的 video-action foundation model。对复现和产品化都很有吸引力：如果已有 OpenVLA 类策略可用，可以先在 latent space 预测未来观测，测试动态物体场景是否改善。选题上，它把“世界模型”落在一个具体痛点上，即处理控制时延和动态目标，而不是泛泛追求视频预测质量。

#### 🔎 读 PDF 先核查

- world model 预测的是哪一层 VLA patch tokens，预测误差如何影响最终 action decoder？
- language-and-motion saliency mask 如何构造，是否需要额外监督或只依赖语言与 optical flow？
- adaptive horizon 的不确定性阈值如何设定，是否能跨任务和速度范围泛化？

#### 📌 上传 PDF 后优先看

- latent-space predictor、velocity/acceleration conditioning 与 saliency mask 章节
- 动态仿真任务、真实 xArm 7 任务和 speed-sensitivity sweep
- 组件消融：无 saliency、固定 horizon、像素预测或无 world model 对比

## Watchlist

### [W1]. PaCo-VLA: Passivity-Shielded Compliance Prior for Contact-Rich Vision-Language-Action Manipulation [[HTML]](https://arxiv.org/html/2606.00515) [[PDF]](https://arxiv.org/pdf/2606.00515)
* **Paper ID**: `2606.00515`
* **Authors**: Haofan Cao, Zhaoyang Li, Zhichao You, Liang Guo, Tianrui Li
* **Author Priority**: Standard
* **为什么还值得留意**: PaCo-VLA 进入 watchlist 是因为它抓住了 VLA 到真实接触控制之间的安全接口问题：低频 VLA 不直接给电机命令，而是输出语义绑定、任务阶段和 admittance schedule，再由 passivity shield 执行。它没有进入最终精选，主要是因为今天主线更偏 world model、数据合成和动作解码；PaCo-VLA 更像控制契约与安全层论文，需要等 PDF 进一步核查真实 connector 和 EV charging-gun 证据强度。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. PACE: Phase-Aware Chunk Execution for Robot Policies with Action Chunking [[HTML]](https://arxiv.org/html/2606.00537) [[PDF]](https://arxiv.org/pdf/2606.00537)
* **Paper ID**: `2606.00537`
* **Authors**: Junnan Nie (1), Jiayi Li (2), Jiachen Zhang (1), Junyi Lao (1), Chenghao Liu (1), Tianle Zhang (2), Songfang Huang (1) ((1) Peking University, (2) JD Explore Academy)
* **Author Priority**: Standard
* **为什么还值得留意**: PACE 值得关注，因为 action chunking 的执行 horizon 是很多 VLA/diffusion policy 部署时被低估的关键变量，而它提出 training-free、phase-aware 的在线选择规则。没有进最终精选，是因为它更像测试时执行策略修正，不直接提出新的 VLA/world model 架构；但对复现任何 action chunk policy 都很实用。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. SafeVLA-Bench: A Benchmark for the Success-Safety Gap in Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2606.00773) [[PDF]](https://arxiv.org/pdf/2606.00773)
* **Paper ID**: `2606.00773`
* **Authors**: Jialiang Fan, Weizhe Xu, Oleg Sokolsky, Insup Lee, Fanxin Kong
* **Author Priority**: Standard
* **为什么还值得留意**: SafeVLA-Bench 进入 watchlist 是因为它把 VLA leaderboards 的成功率盲区形式化为 STL safety specs，并报告 Succ-But-Unsafe 与 Violation Severity Index。未进最终精选，是因为它是评测框架而非策略或世界模型方法；不过它对后续审稿和系统评估很重要，尤其适合补充“成功但不安全”的证据维度。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. ImagineUAV: Aerial Vision-Language Navigation via World-Action Modeling and Kinodynamic Planning [[HTML]](https://arxiv.org/html/2606.01205) [[PDF]](https://arxiv.org/pdf/2606.01205)
* **Paper ID**: `2606.01205`
* **Authors**: Xuchen Liu, Jiawei Huang, Shihao Xia, Bingxi Liu, Jinqiang Cui, Jiankun Yang
* **Author Priority**: Standard
* **为什么还值得留意**: ImagineUAV 和今天的 world-action modeling 主题高度相关：它用 latent video diffusion 先想象 instruction-conditioned future observations，再通过 action extractor 和 kinodynamic planning 得到 6-DoF UAV motion。没有进入最终精选，是因为提供摘录较少，且应用域从机械臂操作转到 UAV VLN；仍值得后续看它如何处理几何一致性和动力学约束。
* **证据来源**: arXiv HTML (Introduction)

### [W5]. LEGS: Fine-Tuning Teleop-Free VLAs for Humanoid Loco-manipulation in an Embodied Gaussian Splatting World [[HTML]](https://arxiv.org/html/2606.01458) [[PDF]](https://arxiv.org/pdf/2606.01458)
* **Paper ID**: `2606.01458`
* **Authors**: Hojune Kim, Timothy Chen, Jiankai Sun, Lars W. Osterberg, Qianzhong Chen, Ke Wang, Mac Schwager
* **Author Priority**: Standard
* **为什么还值得留意**: LEGS 值得放入 watchlist，因为它把 3D Gaussian Splatting 背景、MuJoCo 前景物理和程序化 motion primitives 组合成 teleop-free humanoid loco-manipulation 数据生成系统。未进最终精选，是因为它更偏 humanoid sim2real 数据管线，和 VLA/world model 核心架构线稍远；但若关注 3DGS 仿真和无遥操作微调，它可能非常有参考价值。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
