# RoboPulse | 2026-03-27

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 69 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线很清楚：VLA 正在从“看图到动作”的平面映射，转向更统一的生成式建模、更显式的几何/动力学中间层，以及更面向闭环部署的世界模型训练。最终精选的 6 篇论文，分别覆盖统一离散扩散 VLA、3D 运动先验、RL 稳定化 world model、可形变物体合成数据、零样本 sim2real 和空中操控迁移，基本串起了从模型、数据到新 embodiment 的完整链条。它们入选的共同原因，不只是 headline 新，而是都在回答“如何让机器人模型跨时域、跨平台、跨分布真正工作”这个更硬的问题。VIP 作者里，今天建议优先跟踪 Donglin Wang、Cewu Lu、Yuke Zhu、Dieter Fox 和 Dhruv Shah 这几条线，因为他们分别押中了扩散式 VLA、几何先验、可扩展数据生成与激进 sim2real 的关键方向。

## 今日信号

- 今天最值得记住的研究信号是：VLA 正在从纯动作回归或自回归生成，转向统一生成式框架以及显式几何/动力学中间层。
- 今天最值得记住的研究信号是：sim2real 的重心正从“再采更多真实数据”转向“能否用更强的合成数据引擎和训练配方直接替代真实采集”。
- 今天最值得记住的研究信号是：world model 和跨 embodiment VLA 的评估标准正在从单步质量转向闭环稳定性、物理一致性与真实部署可用性。

## Editor's Picks

### [1]. MMaDA-VLA: Large Diffusion Vision-Language-Action Model with Unified Multi-Modal Instruction and Generation [[VIP]] [[HTML]](https://arxiv.org/html/2603.25406) [[PDF]](https://arxiv.org/pdf/2603.25406) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.25406`
* **Authors**: Yang Liu, Pengxiang Ding, Tengyue Jiang, Xudong Wang, Wenxuan Song, Minghui Lin, Han Zhao, Hongyin Zhang, Zifeng Zhuang, Wei Zhao, Siteng Huang, Jinkui Shi, Donglin Wang
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，它代表了扩散式 VLA 从“动作头替代品”走向“统一多模态机器人生成模型”的一次正面冲击。
* **问题与切口**: 这篇工作试图把 VLA 从“VLM 加策略头”或“离散动作自回归”两条主流路线，推进到单一扩散生成框架里。作者把语言、图像与连续控制统一离散化到同一 token 空间，通过原生离散扩散同时完成多模态理解、目标观测生成与动作生成，主打减少层级拼接的结构负担，并缓解长时程执行中的时间不一致与误差累积。相对已有路线，它的野心不是单点提速，而是把感知、语言与动作放进同一训练目标与推理范式中。
* **核心方法与证据**: 方法上，MMaDA-VLA 采用原生离散扩散 formulation，把多模态输入映射到统一离散空间，并用单一去噪 Transformer 学习联合分布。推理时它不是单向生成动作，而是迭代式地同步细化目标观测与动作 token；从摘要与 HTML 摘录看，作者还强调了大规模 cross-embodiment 预训练，并在 LIBERO、CALVIN 和真实场景中检验多任务、泛化与长时程能力，但具体增益幅度仍需看 PDF 正文核查。
* **正文要点**:
  - 把语言、图像与连续控制统一到同一离散 token 空间里，用单一扩散目标训练。
  - 推理时同步细化目标观测与动作 token，而不是只自回归生成动作序列。
  - 实验覆盖 LIBERO、CALVIN 与真实场景，重点考察多任务泛化和长时程操控。
* **为什么值得跟**:
  - 如果这条路线成立，VLA 的系统设计可以从“基础模型加外接模块”转向更统一的生成范式。
  - 同步生成目标观测与动作，意味着模型可能在内部显式或隐式承担了一部分环境动态建模功能。
  - Donglin Wang 这条线值得继续跟，因为它正在把扩散式建模从图像生成真正推向机器人控制主体。
* **风险 / 保留意见**:
  - HTML 摘录没有展开关键 ablation，暂时无法确认统一扩散范式是否以更高算力成本换来收益。
  - 连续控制离散化后在真实机器人上的精细动作和实时性边界仍不清楚。
* **建议先看**: 先看它如何定义统一离散空间与同步去噪，再看长时程任务里这种统一生成范式是否真的比层级式或自回归式更稳。若 PDF 里有 ablation，优先核对长期一致性和真实部署收益是否来自架构本身。
* **关键词**: `离散扩散 VLA` `多模态统一建模` `长时程操控` `cross-embodiment 预训练`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 连续动作被离散化后，控制精度和动作延迟是如何受影响的？
  - 同步去噪目标观测与动作 token，究竟在哪类长时程失败模式上优于纯动作生成？
  - cross-embodiment 预训练带来的收益里，架构因素和数据规模因素各占多大比例？
* **上传 PDF 后优先看**:
  - 方法部分：统一离散 token space 与单一去噪 Transformer 的定义
  - 实验部分：LIBERO Long、CALVIN 长时程设定与泛化评测
  - 分析部分：真实机器人结果与时间一致性相关 ablation

### [2]. LaMP: Learning Vision-Language-Action Policies with 3D Scene Flow as Latent Motion Prior [[VIP]] [[HTML]](https://arxiv.org/html/2603.25399) [[PDF]](https://arxiv.org/pdf/2603.25399) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.25399`
* **Authors**: Xinkai Wang, Chenyi Wang, Yifu Xu, Mingzhe Ye, Fu-Cheng Zhang, Jialin Tian, Xinyu Zhan, Lifeng Zhu, Cewu Lu, Lixin Yang
* **Author Priority**: Core VIP
* **一句话结论**: 非常值得优先看，它给 VLA 补上了一个更接近物理交互本质的 3D 运动中间层。
* **问题与切口**: LaMP 的切口很明确：当前很多 VLA 直接从 2D 语义特征回归动作，等于把 3D 接触关系、物体运动和交互几何都隐式塞进策略网络里学，导致陌生空间动态下容易失真。作者因此把 dense 3D scene flow 做成潜在运动先验，嵌入预训练 VLA 内部，试图在语言语义和低层控制之间插入一个更物理、更几何化的中间层。与单独训练世界模型不同，它强调把运动预测变成策略内部的共享表征，而不是外接模块。
* **核心方法与证据**: 架构上它是双专家设计：Motion Expert 用 flow matching 生成一步部分去噪的 3D scene flow，Action Expert 则在 gated cross-attention 条件下利用该隐状态输出动作。实验设计围绕四个问题展开，分别检查几何 foresight、3D 相比 2D optical flow 的价值、OOD 鲁棒性，以及不同融合策略的差异；评测覆盖 LIBERO、LIBERO-Plus 和 SimplerEnv-WidowX 这类更接近真实视觉失配的环境，但摘录没有给出完整数值边界。
* **正文要点**:
  - 采用双专家结构，Motion Expert 先生成 3D scene flow 运动先验。
  - Action Expert 通过 gated cross-attention 接收运动隐状态，而非简单拼接特征。
  - 实验显式比较 3D scene flow 与 2D optical flow，并检查 OOD 鲁棒性与融合策略。
* **为什么值得跟**:
  - 它把 VLA 的“语义强、物理弱”问题，转化成一个更可检验的几何建模问题。
  - 它不是另起一套 task-specific world model，而是尝试把运动先验真正并入预训练 VLA 框架。
  - Cewu Lu 这条线值得持续跟踪，因为它正把 3D 几何表征更直接地压进机器人策略。
* **风险 / 保留意见**:
  - 3D scene flow 的质量高度依赖几何估计，深度噪声和遮挡下的稳定性仍需核查。
  - HTML 摘录没有展示训练和推理代价，实际部署时的实时性边界暂不明确。
* **建议先看**: 先抓住它为什么坚持把 3D scene flow 作为潜在中间层，而不是直接做像素到动作映射。随后重点看 3D 对 2D、gated cross-attention 对简单融合的对比证据是否足够扎实。
* **关键词**: `3D scene flow` `latent motion prior` `双专家 VLA` `gated cross-attention` `OOD 泛化`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)
* **读 PDF 先核查**:
  - 一步部分去噪的 3D scene flow 为什么足以作为有效运动先验，而不需要更长预测窗口？
  - 性能提升主要来自 3D 几何先验本身，还是来自双专家带来的额外模型容量？
  - 在视觉扰动和跨域转移下，Motion Expert 的误差会如何向 Action Expert 传递？
* **上传 PDF 后优先看**:
  - 方法部分：Motion Expert、Action Expert 与 gated cross-attention 的接口
  - 实验部分：3D scene flow 对 2D optical flow 的直接比较
  - 鲁棒性部分：OOD、视觉扰动与跨域迁移评测

### [3]. Persistent Robot World Models: Stabilizing Multi-Step Rollouts via Reinforcement Learning [[HTML]](https://arxiv.org/html/2603.25685) [[PDF]](https://arxiv.org/pdf/2603.25685) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.25685`
* **Authors**: Jai Bardhan, Patrik Drozdik, Josef Sivic, Vladimir Petrik
* **Author Priority**: Standard
* **一句话结论**: 如果你在跟 world model 作为机器人模拟器的路线，这篇应该优先读，它正面处理了多步 rollout 崩溃这个真瓶颈。
* **问题与切口**: 这篇论文不再把机器人 world model 只当作“短视频预测器”，而是直指它在 autoregressive 部署时会因 exposure bias 快速崩溃的核心瓶颈。作者要解决的是多步 rollout 的持续性问题：让 action-conditioned video diffusion 模型在反复把自己生成的片段喂回去时，仍能维持时序一致和场景可用性，从而更接近可用于策略评估或训练的模拟器。这比单步重建更贴近真实部署语境。
* **核心方法与证据**: 方法上，作者从预训练 Ctrl-World 出发，对 UNet 以 LoRA 方式做轻量后训练，并额外微调 action encoder，其余模块保持冻结。核心不是继续 teacher-forcing，而是用模型自己的 autoregressive rollouts 做 RL post-training，并用与图像质量和一致性相关的 reward 加权更新；HTML 还给出一段理论推导，说明最优方向会向高奖励样本偏移。证据主要来自 DROID 验证划分上的长时程 rollout 评测，是否能转化为下游策略收益仍待正文细看。
* **正文要点**:
  - 核心问题是 autoregressive rollout 下的 exposure bias，而不是单步视频质量。
  - 后训练直接使用模型自己的生成 rollout，弥补 teacher-forcing 与闭环部署的落差。
  - 实现上以 Ctrl-World 为底座，只对 UNet 做 LoRA 并微调 action encoder。
* **为什么值得跟**:
  - 世界模型能否成为机器人学习中的实用模拟器，关键不在首帧质量，而在闭环 rollout 能撑多久。
  - 它把 RL 后训练引入生成式 world model，提供了一条从离线拟合走向部署对齐的路径。
  - 如果这类方法稳住了长时程视频仿真，VLA 的数据扩展与评测方式都可能被改写。
* **风险 / 保留意见**:
  - 如果奖励主要偏向图像相似性，模型可能只是学会维持观感，而不是保持可控物理过程。
  - 当前证据集中在 DROID 验证划分，跨平台和跨任务外推能力还没有从摘录中看到。
* **建议先看**: 先读它如何把“多步稳定性”正式写成后训练目标，再看 rollout 评测是否真的覆盖了世界模型最常见的崩溃模式。若正文有失败案例，优先看模型是在外观、时序还是动作条件一致性上先失真。
* **关键词**: `robot world model` `video diffusion` `RL 后训练` `exposure bias` `autoregressive rollout`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 奖励函数里的图像指标与任务相关物理一致性之间，相关性到底有多强？
  - 多步 rollout 的稳定性提升能否转化为更好的策略训练或评测，而不只是更好看的视频？
  - LoRA 式轻量后训练在更复杂场景和更长 horizon 上是否仍然有效？
* **上传 PDF 后优先看**:
  - 目标函数与理论部分：reward-weighted 后训练为何对 rollout 稳定有用
  - 实现部分：LoRA、action encoder 微调与奖励设计
  - 实验部分：长时程 rollout 稳定性评测与失败案例

### [4]. SoftMimicGen: A Data Generation System for Scalable Robot Learning in Deformable Object Manipulation [[VIP]] [[HTML]](https://arxiv.org/html/2603.25725) [[PDF]](https://arxiv.org/pdf/2603.25725) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.25725`
* **Authors**: Masoud Moghani, Mahdi Azizian, Animesh Garg, Yuke Zhu, Sean Huver, Ajay Mandlekar
* **Author Priority**: Core VIP
* **一句话结论**: 如果你关心可扩展机器人数据而不只看模型，这篇值得高优先级阅读，它把可形变物体数据生成系统化了。
* **问题与切口**: SoftMimicGen 聚焦一个被低估但越来越关键的问题：可形变物体操作的数据几乎无法像刚体任务那样靠大规模人工采集持续扩张。作者提出的是一套从少量人类示范自动合成大规模数据的系统，而不是单个任务技巧，目标是把 cloth、soft object 等高成本场景也纳入可扩展的机器人数据生产线，并覆盖多种机器人 embodiment。它更像是在搭建 deformable manipulation 时代的数据基础设施。
* **核心方法与证据**: 从摘录看，作者用 Apple Vision Pro 采集源示范，并将人手动作重定向到平行夹爪、灵巧手、人形与双臂平台等不同 embodiment。每个任务只需 1 到 3 条源示范，SoftMimicGen 就生成 1,000 条更广初始状态分布下的演示，再用这些数据训练策略并在需要精细和动态操作的 deformable task suite 上验证。作者也在结论里明确限制：当前方法假设固定的 object-centric subtask sequence。
* **正文要点**:
  - 每个任务只需 1 到 3 条源示范，就生成 1,000 条更广初始状态分布下的演示。
  - 覆盖四类 embodiment，且动作表示会随平台控制接口变化而调整。
  - 作者明确承认当前系统假设固定的 object-centric subtask sequence。
* **为什么值得跟**:
  - 可形变物体一直是大模型机器人数据扩张中的短板，这篇正面补这个缺口。
  - 它把“少量高质量人类示范”转成“可大规模生产的训练数据”，对真实采集成本有直接价值。
  - Yuke Zhu 和 Ajay Mandlekar 这条数据生成路线，和未来机器人基础模型的数据供给关系很近。
* **风险 / 保留意见**:
  - 固定 object-centric subtask sequence 的假设，可能限制开放式可形变操作与恢复行为。
  - HTML 摘录没有展开仿真逼真度与 sim2real 误差来源，真实外推边界还不够清楚。
* **建议先看**: 先把它当成数据基础设施论文来读，而不是单一任务算法。优先看生成管线如何处理 deformable task 的状态变化，再看哪些任务确实从合成数据里获益、哪些仍暴露固定子任务序列的限制。
* **关键词**: `deformable manipulation` `合成数据生成` `cross-embodiment` `仿真管线` `远程操作`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 系统如何表示和约束 deformable object 的状态，才能让少量示范安全扩增成大规模数据？
  - 哪些生成步骤是自动完成的，哪些仍依赖人工设定的 task structure 或 subtask 顺序？
  - 当任务需要失败恢复或非固定顺序操作时，这套管线会在哪里先失效？
* **上传 PDF 后优先看**:
  - 系统部分：示范采集、动作重定向与数据生成流程
  - 任务部分：deformable task suite 与多 embodiment 设定
  - 分析部分：固定子任务假设带来的限制与失败模式

### [5]. MolmoB0T: Large-Scale Simulation Enables Zero-Shot Manipulation [[VIP]] [[HTML]](https://arxiv.org/html/2603.16861) [[PDF]](https://arxiv.org/pdf/2603.16861) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.16861`
* **Authors**: Abhay Deshpande, Maya Guru, Rose Hendrix, Snehal Jauhri, Ainaz Eftekhar, Rohun Tripathi, Max Argus, Jordi Salvador, Haoquan Fang, Matthew Wallingford, Wilbert Pumacay, Yejin Kim, Quinn Pfeifer, Ying-Chun Lee, Piper Wolters, Omar Rayyan, Mingtong Zhang, Jiafei Duan, Karen Farley, Winson Han, Eli Vanderbilt, Dieter Fox, Ali Farhadi, Georgia Chalvatzaki, Dhruv Shah, Ranjay Krishna
* **Author Priority**: Extended VIP
* **一句话结论**: 这是今天 sim2real 方向最该优先看的论文之一，即便你不完全接受 headline，也必须看它把争论推到了什么程度。
* **问题与切口**: MolmoB0T 的中心命题很激进：只靠足够大规模、足够多样的模拟合成数据，也能把操作策略零样本迁移到真实世界，而不必再默认需要真实数据或任务级微调。它不是只展示一个模型结果，而是把 procedural data generation、数据混合和多类策略训练串成一套开放 recipe，直接回应“开源社区能否自己造出 foundation-style robot policy”这一问题。
* **核心方法与证据**: 证据链由真实与仿真两端组成：作者在 Franka FR3 的 tabletop 操作和 RB-Y1 的 mobile manipulation 上做 zero-shot real-world evaluation，并强调所有 MolmoBot policy 从未见过 real-robot data，也没有真实后训练。HTML 摘录还透露他们专门分析了并行去噪时间步采样、absolute vs. delta action representation 等 recipe 选择，说明论文关注点不只是规模口号，也在拆解哪些训练设计真正影响 sim2real。
* **正文要点**:
  - 所有 MolmoBot policy 都只在模拟数据上训练，没有真实机器人后训练或微调。
  - 评测不只做 tabletop manipulation，也覆盖 mobile manipulation。
  - 作者专门分析训练 recipe，如并行去噪时间步采样与 absolute/delta action representation。
* **为什么值得跟**:
  - 如果这条路线可复现，机器人基础模型研究对重资产真实采集的依赖会被明显削弱。
  - 它把 sim2real 的讨论从“是否需要真实数据”推进到“什么规模和配方的模拟数据才够”。
  - Dieter Fox 和 Dhruv Shah 共同出现，使这条纯模拟扩展路线非常值得继续追踪。
* **风险 / 保留意见**:
  - 论文主张很强，但摘录没有给出完整的任务覆盖面与真实失败案例分解。
  - 零样本迁移成功可能高度依赖其数据引擎与配方细节，外部团队复现门槛未必低。
* **建议先看**: 先读真实世界 zero-shot 结果，再回头读 recipe ablation。真正值得关心的不是 headline 本身，而是哪几个数据和训练设计让 sim2real 从口号变成了可复现配方。
* **关键词**: `zero-shot sim2real` `合成机器人数据` `程序化生成` `移动操作` `开放配方`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - MolmoBot-Engine 里究竟哪些分布因素最关键，真正支撑了零样本真实迁移？
  - 收益主要来自模拟数据规模与多样性，还是来自策略类与动作表示的具体选择？
  - 最先暴露失败的环节是感知分布偏移、接触动力学，还是长时程任务组合？
* **上传 PDF 后优先看**:
  - 真实评测部分：Franka FR3 与 RB-Y1 的 zero-shot 结果
  - 数据部分：MolmoBot-Engine 与数据混合配方
  - ablation 部分：动作表示与去噪时间步采样选择

### [6]. $π$, But Make It Fly: Physics-Guided Transfer of VLA Models to Aerial Manipulation [[HTML]](https://arxiv.org/html/2603.25038) [[PDF]](https://arxiv.org/pdf/2603.25038) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.25038`
* **Authors**: Johnathan Tucker, Denis Liu, Aiden Swann, Allen Ren, Javier Yu, Jiankai Sun, Brandon Kim, Lachlain McGranahan, Quan Vuong, Mac Schwager
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为它把 VLA 的跨 embodiment 叙事推到了一个更苛刻也更真实的测试场景。
* **问题与切口**: AirVLA 关注的不是常规机械臂泛化，而是一个更极端的 embodiment transfer 问题：操控预训练的 VLA 能否迁移到欠驱动、强耦合的空中操作平台。作者的判断很务实，从摘录看他们认为视觉语义表征可以迁移，但飞行所需的动力学控制不能直接照搬，因此提出用物理引导去补齐 VLA 与 aerial manipulation 之间的“动态差距”。这比从零训练空中策略更现实。
* **核心方法与证据**: 系统以多视角 RGB 和语言指令为输入，输出相对末端位姿命令，再交给低层飞控执行。方法上有两根主线：一是在推理时加入 payload-aware 的垂向补偿，处理抓取后有效质量突变带来的下沉；二是用 Gaussian-splatting 管线从少量种子轨迹合成更多训练数据。实验则显式拆分迁移能力、实时 chunking 与物理补偿、数据增强，以及 navigate-then-grasp 这类组合任务，但摘录尚不足以判断其跨任务普适性。
* **正文要点**:
  - 作者明确区分“视觉表征可迁移”和“飞行动力学不可直接迁移”这两件事。
  - 推理时加入 payload-aware 垂向补偿，专门处理抓取后质量突变带来的下沉。
  - Gaussian-splatting 数据管线用于从少量轨迹高效合成更多训练数据。
* **为什么值得跟**:
  - VLA 真正的跨 embodiment 能力，只有在空中操作这类极端动力学场景下才算经得起检验。
  - 它展示了一条更务实的迁移路径：保留预训练语义能力，用物理补偿弥补新平台动态差异。
  - 这篇论文把基础模型操作与空中机器人两个相对分离的研究圈层连接了起来。
* **风险 / 保留意见**:
  - 任务设置看起来仍较专用化，是否能外推到更广泛的空中交互任务还不清楚。
  - 低层飞控与高层 VLA 的边界较强，最终收益可能部分依赖控制器工程质量而非模型本身。
* **建议先看**: 先把它当成一篇“迁移边界诊断”论文来读，而不只是一个 aerial VLA 系统。重点核查物理补偿和数据增强各自带来多少贡献，以及它们是否真的让预训练 VLA 学到的语义操作能力保留下来。
* **关键词**: `aerial manipulation` `cross-embodiment transfer` `physics-guided control` `Gaussian splatting` `VLA`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)
* **读 PDF 先核查**:
  - payload-aware compensation 的计算方式是什么，它对载荷估计误差有多敏感？
  - 预训练 VLA 究竟迁移了操作语义，还是主要迁移了可用视觉表征？
  - 在组合任务里，主导失败的是导航、悬停稳定性，还是接触执行阶段？
* **上传 PDF 后优先看**:
  - 系统部分：高层动作接口与低层飞控的责任边界
  - 实验部分：RTC、payload-aware guidance 与迁移效果拆分
  - 数据部分：Gaussian-splatting 合成数据对导航与组合任务的作用

## Watchlist

### [W1]. Fast-dVLA: Accelerating Discrete Diffusion VLA to Real-Time Performance [[VIP]] [[HTML]](https://arxiv.org/html/2603.25661) [[PDF]](https://arxiv.org/pdf/2603.25661)
* **Paper ID**: `2603.25661`
* **Authors**: Wenxuan Song, Jiayi Chen, Shuai Chen, Jingbo Wang, Pengxiang Ding, Han Zhao, Yikai Qin, Xinhu Zheng, Donglin Wang, Yan Wang, Haoang Li
* **Author Priority**: Core VIP
* **为什么还值得留意**: 它进 shortlist，因为离散扩散 VLA 真正落地迟早要过“实时推理”这道关，而 Fast-dVLA 抓住了 bidirectional dVLA 隐含的 block-wise 自回归模式，提出 KV cache 复用、diffusion forcing 和蒸馏式训练，工程价值很高。没有进最终精选，主要是因为它更像推理系统优化而非能力边界推进；从摘录看，结论高度依赖速度与性能的权衡，科学新意弱于今天入选的统一建模、几何先验和 sim2real 主线。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. LILAC: Language-Conditioned Object-Centric Optical Flow for Open-Loop Trajectory Generation [[HTML]](https://arxiv.org/html/2603.25481) [[PDF]](https://arxiv.org/pdf/2603.25481)
* **Paper ID**: `2603.25481`
* **Authors**: Motonari Kambara, Koki Seno, Tomoya Kaichi, Yanan Wang, Komei Sugiura
* **Author Priority**: Standard
* **为什么还值得留意**: 它进 shortlist，因为它把语言条件下的 manipulation planning 改写成 object-centric 2D optical flow 预测，并尝试借人类与网页视频降低 embodiment-specific 数据需求，这条路线对低成本数据扩展很有吸引力。没有进最终精选，是因为它目前仍是 open-loop、2D flow 到轨迹的链条，相比 LaMP 的 3D latent motion prior，物理接触建模和闭环控制说服力稍弱；此外，摘录里更多证据集中在 benchmark 构建与模块设计，真实泛化边界还不够清楚。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. Towards Generalizable Robotic Data Flywheel: High-Dimensional Factorization and Composition [[HTML]](https://arxiv.org/html/2603.25583) [[PDF]](https://arxiv.org/pdf/2603.25583)
* **Paper ID**: `2603.25583`
* **Authors**: Yuyang Xiao, Yifei Zhou, Haoran Wang, Wenxuan Ou, Yuxiao Liu
* **Author Priority**: Standard
* **为什么还值得留意**: 它进 shortlist，因为它正面处理“数据飞轮怎么组织”这个常被忽视的问题，用 object、action、environment 因子的分解与组合去驱动真实机器人迭代采集和训练。没有进最终精选，是因为从摘录看 F-ACIL 更像启发式数据策展框架，方法贡献与证据边界都偏场景依赖；相比今天入选论文，它对 VLA、world model 或 sim2real 主线的直接推动稍弱。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)

### [W4]. Diagnose, Correct, and Learn from Manipulation Failures via Visual Symbols [[HTML]](https://arxiv.org/html/2512.02787) [[PDF]](https://arxiv.org/pdf/2512.02787)
* **Paper ID**: `2512.02787`
* **Authors**: Xianchao Zeng, Xinyu Zhou, Youcheng Li, Jiayou Shi, Tianle Li, Liangming Chen, Lei Ren, Yong-Lu Li
* **Author Priority**: Standard
* **为什么还值得留意**: 它进 shortlist，因为失败诊断、纠错和从失败中学习本来就是 VLA 走向开放世界部署必须补上的一环，而 ViFailback 还提供了真实世界失败数据、VQA 对和基准，这在当前文献里并不多见。没有进最终精选，是因为它更偏失败分析与监督信号设计，而不是今天的核心主线之一；就摘录证据看，它对策略能力本身的提升机制仍需要结合完整正文再判断。
* **证据来源**: arXiv HTML (Introduction, Experiments)
