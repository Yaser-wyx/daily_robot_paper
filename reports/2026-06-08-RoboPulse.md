# RoboPulse | 2026-06-08

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 71 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线非常集中：VLA 不再只是在更大 backbone 上做动作回归，而是在动作表示、潜在动作、规划 token、权重空间适配和 WAM 推理模式上重新设计“从视觉语言到控制”的中间层。最终精选的 6 篇都围绕一个共同问题：如何让机器人在数据稀缺、长时序、跨域或真实部署条件下获得更稳的动作生成，而不是单纯依赖端到端单点预测。Sim2Real 方向今天没有只选视觉逼真或动力学校准，而是优先保留了能直接影响 VLA/RL 后训练与真实机器人迁移的论文。VIP 作者上，最终精选中最值得优先跟踪的是 Pulkit Agrawal 参与的 2606.06627；watchlist 中 Danfei Xu 参与的 2606.07464 也值得持续观察，因为它把长上下文压缩与规划目标绑定到自动驾驶 VA/VLA。核心优先作者名单在这组最终精选摘录里没有直接强命中，因此今天更像是“扩展 VIP + 新动作表示路线”的信号日。

## 今日信号

- VLA 的性能瓶颈正在从“模型够不够大”转向“动作空间是否被结构化、可规划、可对齐地表示”。
- 人类视频、潜在动作和权重空间生成都在尝试绕开真实机器人动作标注稀缺，但它们共同的风险是对齐信号是否足够接近真实控制。
- World Action Model 和 action-token planning 同时指向一个趋势：长时序机器人策略需要在执行前或执行中显式管理未来，而不是只对当前观测反应。

## Historical Rediscovery

- **Paper**: Discrete-WAM: Unified Discrete Vision-Action Token Editing for World-Policy Learning [[HTML]](https://arxiv.org/html/2606.05645) [[PDF]](https://arxiv.org/pdf/2606.05645)
  - **Paper ID**: `2606.05645`
  - **来源日期**: 2026-06-05
  - **当时可能被低估的信号**: 当时可能低估了“未来视觉状态 + ego action 统一离散 token 化”的接口价值，尤其是 counterfactual future 与 action token editing 可能迁移为机器人 WAM 的设计参照。
  - **为什么现在值得再看**: 今天关注 VLA/WAM、world model 与 action-conditioned prediction，这篇提供了一个把视觉未来和动作放进同一离散编辑框架的候选范式，适合横向借鉴到 manipulation policy/world-policy learning。
  - **建议动作**: 加入精读
  - **关键词**: `World Action Model` `discrete action tokens` `counterfactual future` `world-policy learning`
- **Paper**: AffordanceVLA: A Vision-Language-Action Model Empowering Action Generation through Affordance-Aware Understanding [[HTML]](https://arxiv.org/html/2606.06155) [[PDF]](https://arxiv.org/pdf/2606.06155)
  - **Paper ID**: `2606.06155`
  - **来源日期**: 2026-06-05
  - **当时可能被低估的信号**: 当时可能低估了 Which2Act、Where2Act、How2Act 这种结构化 affordance forecasting 作为中间表征的工程价值，尤其是在 VLA action generation 前显式约束可操作区域与动作形式。
  - **为什么现在值得再看**: 如果继续推进 VLA 在真实操作中的可靠动作生成，affordance-aware understanding 仍是很实际的补强路线；它和 VLA、长时程操作中的局部可执行性判断高度相关。
  - **建议动作**: 加入精读
  - **关键词**: `VLA` `affordance forecasting` `3D action space` `robot manipulation`
- **Paper**: TAM: Torque Adaptation Module for Robust Motion Transfer in Manipulation [[HTML]](https://arxiv.org/html/2606.06218) [[PDF]](https://arxiv.org/pdf/2606.06218)
  - **Paper ID**: `2606.06218`
  - **来源日期**: 2026-06-05
  - **当时可能被低估的信号**: 当时可能低估了“冻结高层策略，只适配底层 torque response”的部署信号；这类模块可能比重新训练 VLA 更适合快速弥合真实硬件差异。
  - **为什么现在值得再看**: 今天若关心 VLA 到真实机器人部署，底层 torque adaptation 可以作为 policy 外围的 Sim2Real 稳健化层，尤其对 contact-rich manipulation 和跨机器人 motion transfer 有参考价值。
  - **建议动作**: 快速浏览
  - **关键词**: `Sim2Real` `torque adaptation` `motion transfer` `real deployment`
- **Paper**: LadderMan: Learning Humanoid Perceptive Ladder Climbing [[HTML]](https://arxiv.org/html/2606.05873) [[PDF]](https://arxiv.org/pdf/2606.05873)
  - **Paper ID**: `2606.05873`
  - **来源日期**: 2026-06-05
  - **当时可能被低估的信号**: 当时可能低估了“感知基础模型 + RL/模仿学习 + 真实全身接触任务”的组合信号；高难度梯子攀爬比普通 locomotion 更接近长期、接触密集的 embodied control。
  - **为什么现在值得再看**: 对 RL+VLA、Sim2Real 和真实部署评测来说，它可作为非 manipulation 但高压力闭环系统案例，帮助判断视觉感知如何进入真实机器人长时程控制。
  - **建议动作**: 快速浏览
  - **关键词**: `Sim2Real` `RL` `vision foundation model` `real humanoid deployment`
- **Paper**: Partially Observable Adversarial Patch Attacks on Vision-Language-Action Models in Robotics [[HTML]](https://arxiv.org/html/2606.03556) [[PDF]](https://arxiv.org/pdf/2606.03556)
  - **Paper ID**: `2606.03556`
  - **来源日期**: 2026-06-03
  - **当时可能被低估的信号**: 当时可能低估了“部分可观测攻击”比 full-rollout attack 更贴近真实威胁；短前缀生成固定 patch 并影响后续帧的设定，对部署评测很具体。
  - **为什么现在值得再看**: 你的兴趣包含真实部署评测，这篇可补进 VLA robustness checklist，尤其用于思考 closed-loop VLA 在有限观测、连续帧和真实干扰下的脆弱性。
  - **建议动作**: 继续跟踪
  - **关键词**: `VLA robustness` `adversarial patch` `real deployment evaluation` `closed-loop safety`

## Editor's Picks

### [1]. What Matters When Cotraining Robot Manipulation Policies on Everyday Human Videos? [[VIP]] [[HTML]](https://arxiv.org/html/2606.06627) [[PDF]](https://arxiv.org/pdf/2606.06627) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.06627`
* **Authors**: Richard Li, Aditya Prakash, Andrew Wen, Saurabh Gupta, Yilun Du, Pulkit Agrawal
* **Author Priority**: Extended VIP
* **一句话结论**: 值得优先看，因为它直接回答了 everyday human videos 能否真正帮助机器人操控 cotraining，以及哪些数据因素会造成正迁移或负迁移。
* **关键词**: `human video cotraining` `robot manipulation` `hand pose transfer` `data scarcity` `Sim2Real`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

这篇论文切中 VLA 和机器人基础模型最现实的数据瓶颈：遥操作示范贵、强化学习难扩展，而互联网上的人类日常视频海量存在。问题在于，以往能做 human-to-robot transfer 的 end-to-end cotraining 往往依赖“对齐过”的人类数据，例如动作被刻意编排得像机器人、相机视角一致，甚至用专门硬件捕捉 3D hand pose。真正的 everyday human video 则更自然、更杂乱，也更接近可规模化来源，但人与机器人之间存在视角、运动模式、执行器和动作空间差异。论文的价值在于不只是提出一个数据集，而是系统追问：手部标注质量、场景多样性、自然运动 gap 和网络结构分工，究竟哪些因素会决定这种视频能否转化为机器人策略收益。

#### ⚙️ 核心方法

方法核心是一个人类视频与机器人轨迹共同训练的框架，目标是在 observation/action 对齐和 embodiment specialization 之间取得平衡。摘录能确认，人类数据来自 egocentric moving head-camera，机器人数据使用相近位置的 egocentric camera，但两者传感器尺寸和焦距差异明显，因此视觉对齐本身就是难点。人类动作来自 triangulated hand labels 或 monocular hand pose estimation，再被转换到机器人动作空间；机器人平台是 6-DOF AgileX Piper arm，动作空间包含 TCP pose 和离散抓取命令。框架显然不只是把人手轨迹当作伪机器人动作，而是通过坐标变换、动作空间映射和网络结构设计，让共享表示能吸收可迁移的视觉-运动规律，同时允许不同 embodiment 保留专门参数，避免过度 representation alignment。当前摘录还能确认作者强调 Sec. 4.2、4.3 用于 observation/action alignment，Sec. 4.4、4.5 用于防止 harmful alignment；但具体 loss、网络分支和参数共享细节需要 PDF 中方法章节核查。

#### 📊 实验与结果

实验围绕 robot-only training 与 human cotraining 的差异展开，重点看低机器人数据条件下的零样本泛化。HTML 摘录明确写到，新数据集包含 532 条人类视频和 28 小时高质量 triangulated hand labels；实验显示 human cotraining 在所有 robot data regimes 下都有一致收益，低数据场景增益最大，Pull task 尤其受益。作者还比较 TriHands 与 EgoDex，结论是 TriHands 尽管小时数更少，却在所有任务上优于 EgoDex，因而场景多样性可能比单纯数据规模更关键。证据边界也很清楚：简单任务上可以看到 motion transfer，但最复杂任务的 motion transfer 仍不确定；随着机器人同分布数据增加，human cotraining 的优势会缩小。摘录没有给出完整成功率数字，因此不能展开具体表格对比。

#### ⚠️ 风险 / 保留意见

- 复杂任务上的 motion transfer 证据仍不充分，不能直接推断 everyday videos 已能稳定解决长时序操控。
- 方法依赖高质量手部轨迹和坐标/动作映射，换相机、换手部估计器或换机器人后复现风险较高。
- 人类自然动作与机器人可执行动作之间仍有 inherent motion gap，过度共享表示可能带来负迁移。

#### 💭 结论与启发

这篇对后续选题的启发是：human video for robotics 不应只问“数据够不够多”，而要拆成手部几何质量、场景多样性、相机分布、动作可执行性和网络共享策略几个变量。若要复现或扩展，可以先把它作为 VLA/RL post-training 的低数据增强模块，而不是期待直接替代机器人示范。尤其值得沿着“scene diversity beats scale”的线索做更细的 ablation。

#### 🔎 读 PDF 先核查

- TriHands 相比 EgoDex 的优势到底来自 hand label quality、scene diversity，还是相机/任务分布更接近机器人评测？
- 网络中哪些层或模块允许 embodiment specialization，哪些层共享，是否有明确证据证明这样能减少 harmful alignment？
- 复杂任务 motion transfer 不确定时，失败主要来自视觉识别、手到 TCP 映射、gripper timing，还是长时序误差累积？

#### 📌 上传 PDF 后优先看

- 方法章节中的 observation/action alignment 与 embodiment specialization 设计
- TriHands、EgoDex、robot-only 与 human cotraining 的任务级消融表
- 真实机器人 rollout 失败案例和复杂任务 motion transfer 分析

### [2]. ActionMap: Robot Policy Learning via Voxel Action Heatmap [[HTML]](https://arxiv.org/html/2606.06904) [[PDF]](https://arxiv.org/pdf/2606.06904) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.06904`
* **Authors**: Pei Yang, Hai Ci, Yanzhe Chen, Qi Lv, Han Cai, Mike Zheng Shou
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为它把 VLA 动作头从单点回归改成 voxel action heatmap，直接挑战当前 VLA decoder 的默认设计。
* **关键词**: `VLA action decoder` `voxel heatmap` `OpenVLA-OFT` `LIBERO` `data efficiency`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

#### 📖 背景与动机

这篇论文的问题意识很明确：VLA backbone、训练 recipe 和数据规模进展很快，但动作 decoder 长期停留在单点预测。无论是 autoregressive token bins、L1 regression，还是 flow-matching denoising，本质上都把动作空间当作缺少几何结构的输出变量。对于机器人末端执行器控制，这会浪费动作之间的空间邻近关系，也难以表达多峰示范或软监督。尤其在数据效率和末端精度敏感的 manipulation 场景里，仅靠扩大 backbone 未必能解决动作 head 的结构缺陷。ActionMap 因此把研究焦点从“VLA 看懂什么”转向“VLA 如何表示和选择动作”，这对所有基于连续控制的 VLA 系统都有直接参考价值。

#### ⚙️ 核心方法

ActionMap 的核心是一个可插入现有 VLA 的 voxel heatmap action head。它用体素化动作空间替代单个连续动作点，并用 Gaussian-blob target 加 cross-entropy 训练，使网络不仅学习目标动作本身，也学习邻近动作的软概率结构。摘录显示，该 head 可以替换 OpenVLA-OFT 的 parallel-decoding L1 regression head，也可以接入带 flow-matching action expert 的 VLM/VLA 系统；这说明作者试图把 ActionMap 设计成 action representation 层面的模块，而不是依赖某个特定 backbone。相对已有单点 decoder，它的新意在于显式保留动作空间的几何邻近性，让训练信号从“对/错一个点”变成“在局部空间内形成概率热图”。这也可能天然支持 multimodal demonstrations：如果多个相近或可行动作都能完成任务，heatmap 比 L1 平均值更不容易坍缩到不可执行中间点。当前摘录不能确认体素维度如何覆盖姿态、gripper 和时间序列，也不能确认 inference 时如何从 heatmap 解码连续动作，需要上传 PDF 后核查。

#### 📊 实验与结果

实验以两个 backbone VLA 为基线：OpenVLA-OFT 和一个 flow-matching action expert 模型。主要模拟评测在 LIBERO 四个 suites：Spatial、Object、Goal、Long；每个 success rate 来自 50 trials、10 tasks、共 500 episodes，并使用 LIBERO seed 7。数据效率实验在 LIBERO-Spatial 的 10%、25%、50% 分层子集上 finetune。摘录还说明 OpenVLA-OFT 相关实验使用 LoRA finetuning，rank 32，训练 10000 optimizer steps，有效 batch size 64。结论层面，作者声称 ActionMap 在 LIBERO 和真实 Franka manipulation 中带来 success rate、training convergence 和 data efficiency 提升，但摘录没有给出具体数值，因此只能保守表述为方向性收益，不能复述表格数字。

#### ⚠️ 风险 / 保留意见

- voxel grid 随每轴分辨率呈多项式增长，动作粒度、显存和参数规模之间存在硬约束。
- 如果姿态、夹爪和多步动作都体素化，输出空间设计可能变复杂，部署延迟也需核查。
- 真实 Franka 证据在摘录中较笼统，需要确认任务数量、随机化程度和失败案例。

#### 💭 结论与启发

ActionMap 的启发是，VLA 的动作输出层值得被当成一等研究对象。后续做系统设计时，可以把 backbone scaling 与 action head structure 分开评估：同一 VLA backbone 下比较 L1、flow、token bin、heatmap 或混合表示，可能比单纯换大模型更有信息量。复现时应优先从 LIBERO-Spatial 低数据子集入手，因为那里最能看出 soft spatial supervision 是否改善收敛和样本效率。

#### 🔎 读 PDF 先核查

- ActionMap 的 voxel 表示覆盖哪些动作维度，是否同时处理位置、旋转、夹爪和动作 horizon？
- Gaussian-blob target 的尺度如何设定，不同任务或机器人上的尺度敏感性是否做了消融？
- 真实 Franka 实验中的提升是否来自更精确末端定位，还是来自训练稳定性和低数据正则化？

#### 📌 上传 PDF 后优先看

- ActionMap head 的体素化动作定义和 heatmap 解码流程
- LIBERO 四个 suite 与低数据子集上的对比/消融表
- 真实 Franka manipulation 设置、任务列表和失败案例分析

### [3]. Dreaming when Necessary: Advancing World Action Models with Adaptive Multi-Modal Reasoning [[HTML]](https://arxiv.org/html/2606.07089) [[PDF]](https://arxiv.org/pdf/2606.07089) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.07089`
* **Authors**: Yinzhou Tang, Jingbo Xu, Yu Shang, Zihao Song, Chen Gao, Wei Wu, Yong Li
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为 AdaWAM 把 World Action Model 的视频预测和动作生成改成按执行上下文自适应切换的多模态推理。
* **关键词**: `World Action Model` `adaptive reasoning` `video-action prediction` `long-horizon manipulation` `dynamic router`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

World Action Model 的吸引力在于它不只是从当前图像反应式地产生动作，而是显式建模未来观测与机器人动作之间的耦合。对接触丰富、物理动态复杂或长时序 manipulation 来说，这比普通 VLA 更接近“先想象后行动”。但现有 WAM 也有明显瓶颈：依赖 video prediction 作为 action prior 会带来计算延迟，长任务中每一步都做高成本视觉 rollout 并不总是必要；同时，纯视觉预测未必能处理子任务切换和高层语义决策。AdaWAM 的核心动机是把执行过程拆成不同 reasoning modes：任务转换时需要文本/语义推理来决定下一阶段，精细操作时需要视觉推理来辅助控制。

#### ⚙️ 核心方法

AdaWAM 的方法由多模态推理数据标注、动态路由和不同预测模式组成。摘录能确认，作者首先构建 trajectory-guided subtask annotation pipeline：从机器人状态轨迹中解析 end-effector motion、gripper transitions 和任务相关 motion patterns，生成每个预定义子任务的候选时间窗口；随后使用 Qwen3-VL 8B 作为 semantic verifier，在视觉观测、子任务描述、完成标准和上下文条件下识别子任务最早稳定完成的帧，并通过时序单调性和 segment validity 约束融合边界。另一个关键数据环节是 motion-based fine manipulation labeling，用于标注 LIBERO、RoboTwin 和真实实验中的关键操作区间。推理上，AdaWAM 使用轻量 dynamic router，根据执行上下文在文本推理、视觉推理、video-action joint prediction 和 action-only prediction 等模式间切换。相对固定 video-action joint prediction，它的创新点是“dreaming when necessary”：在需要物理 foresight 时才引入视觉未来推理，在任务切换或高层决策时转向文本条件，从而兼顾长时序性能和计算开销。具体 router 输入、训练 loss 和切换阈值在摘录中不足，需要 PDF 进一步确认。

#### 📊 实验与结果

评测覆盖三个层面：LIBERO、RoboTwin 2.0，以及真实机器人平台，包括 AgileX Split-Type ALOHA 和 PiPER 6-DoF arms。真实任务摘录中明确提到 Clean Table 和 Wipe Table，并且作者区分 trivial tasks 与 hard tasks，后者强调 long-horizon operation 和 fine-grained manipulation。为了验证 adaptive reasoning module，实验包含两个变体：去掉 textual reasoning 的 AdaWAM w/o T.R.，以及去掉 visual reasoning 的 AdaWAM w/o V.R.。摘录中的结论称 AdaWAM 在模拟和真实平台上优于 state-of-the-art embodied policies，并减少不必要 reasoning，但没有给出具体成功率、延迟或计算量数字。因此目前只能确认其评测设计覆盖了性能与模块消融，不能引用精确幅度。

#### ⚠️ 风险 / 保留意见

- 多模态标注 pipeline 依赖预定义子任务、轨迹启发和 Qwen3-VL 验证，标注误差可能影响 router 学习。
- dynamic router 若切换错误，可能在需要物理 foresight 时过早 action-only，或在简单步骤引入额外延迟。
- 真实机器人任务数量从摘录看有限，需要确认是否足以支撑泛化主张。

#### 💭 结论与启发

AdaWAM 对后续 WAM/VLA 选题的启发是：未来建模不必是全程昂贵 video rollout，而可以变成一个上下文触发的工具。系统设计上，可以把高层子任务边界、细粒度接触阶段和动作预测模式显式绑定，形成“语义转场 + 视觉精操”的混合策略。复现时不应只看最终成功率，还要重点评估 router 的选择是否与任务阶段一致，以及节省的推理成本是否真实可部署。

#### 🔎 读 PDF 先核查

- dynamic router 依据哪些观测或隐藏状态决定文本推理、视觉推理和 action-only 模式？
- Qwen3-VL 8B 标注出的子任务边界是否有人类审核或误差评估，边界噪声对性能影响多大？
- AdaWAM 的性能提升和计算节省是否同时成立，还是在不同任务难度下存在 trade-off？

#### 📌 上传 PDF 后优先看

- multimodal reasoning data annotation pipeline 与子任务边界构造
- dynamic router 的结构、训练目标和推理流程
- LIBERO、RoboTwin 2.0 与真实 Clean/Wipe Table 的消融和延迟/成本评估

### [4]. LARA: Latent Action Representation Alignment for Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2606.07100) [[PDF]](https://arxiv.org/pdf/2606.07100) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.07100`
* **Authors**: Mengya Liu, Baoxiong Jia, Jiangyong Huang, Jingze Zhang, Siyuan Huang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为 LARA 把 LAM 的潜在动作和 VLA 内部表示共同对齐，试图让无标签人类/机器人视频真正服务于动作学习。
* **关键词**: `latent action model` `VLA alignment` `VQ-VAE` `Open-X-Embodiment` `unlabeled video`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

VLA 的核心瓶颈之一是真实机器人 action-labeled data 稀缺，而互联网上和机器人日志中的无标签交互视频远多于带动作标注的数据。Latent Action Model 因此成为一个重要路线：从视觉状态转移中学习离散 latent actions，再把它们作为 VLA 的额外监督或先验。但已有 LAM-based VLA 往往采用两阶段训练：先独立预训练 LAM，再冻结或间接使用其表示训练 VLA。这样会产生两个问题：LAM 的 latent action 未必被真实机器人动作 grounding，VLA 也被一个冻结的、可能不适配策略内部表示的 latent space 限制。LARA 的重要性在于把 latent action representation alignment 作为主问题处理，而不是把 LAM 当成外部特征提取器。

#### ⚙️ 核心方法

摘录显示，LARA 建立在典型 LAM 组件之上：Inverse Dynamic Model 根据当前和未来视觉观测预测连续 latent action；Vector Quantizer 将 latent 离散化为 codebook token，遵循 VQ-VAE 思路；Forward Dynamic Model 在当前观测和量化 latent action 条件下重建未来观测。不同于传统两阶段方案，LARA 的目标是把 latent action space 与 VLA policy internal representations 共同对齐，形成互惠关系：LAM 通过真实 action trajectories 获得 grounding，VLA 通过 LAM 的 forward dynamics priors 获得正则化。也就是说，latent action 不再只是从视频动态中无监督学到的离散 token，而要与策略真正要输出的机器人动作和内部控制表征发生联系。当前摘录只能确认它面向 post-training refinement、latent action refiner 和多范式 VLA 适配；具体 alignment loss 如何连接 codebook、policy hidden states 与真实动作轨迹，是否端到端更新 LAM/VLA，以及训练稳定性设计，都需要 PDF 的方法章节核查。

#### 📊 实验与结果

实验问题设计较完整：一是 LARA 相比现有 VLA 在多样机器人 benchmark 上表现如何；二是它作为 VLA post-training refinement module 和 LAM latent action refiner 的作用有多大；三是对新任务和新机器人 embodiment 的泛化能力，以及哪些训练因素关键。摘录明确区分两个设置：OXE-Constrained Comparison 要求所有模型只使用 Open-X-Embodiment 范围内数据，可更干净地比较模型设计；Unconstrained Comparison 则不限制模型设计和预训练数据，用来观察性能上限。结论称 LARA 可跨多种范式展示 versatility，但摘录没有给出具体 benchmark 名称、成功率或消融数字。因此目前证据足以判断其问题设置重要，具体领先幅度必须等待 PDF 表格核查。

#### ⚠️ 风险 / 保留意见

- alignment 目标若设计不当，可能把 LAM 的视频动态偏差强行注入 VLA，而不是提升控制。
- 需要确认 LARA 是否增加训练复杂度、显存成本和对无标签视频质量的敏感性。
- 跨 embodiment 泛化主张在摘录中缺少具体平台和任务细节，需谨慎看待。

#### 💭 结论与启发

LARA 给出的启发是，latent action 不能只追求视觉未来可重建，还必须被机器人可执行动作 grounding。后续如果做 human video 或 unlabeled robot video 预训练，可以把“LAM 表示是否贴近 policy hidden/action manifold”作为核心评估，而不是只看 reconstruction loss。系统上，它适合与 VLA post-training 结合：先用无标签视频提供动态先验，再用少量真实动作轨迹校准 latent-action-to-control 的关系。

#### 🔎 读 PDF 先核查

- LARA 的 alignment loss 具体作用在哪些表示之间：LAM codebook、VLA hidden state、动作 token 还是连续 action？
- LAM 在 VLA 训练期间是冻结、联合更新，还是通过 refiner 部分更新？
- OXE-constrained 与 unconstrained 设置下，LARA 的收益是否来自方法本身，而不是额外数据或 backbone 差异？

#### 📌 上传 PDF 后优先看

- LARA alignment objective 和 LAM/VLA 联合训练流程
- OXE-Constrained Comparison 的模型、数据和公平性设置
- latent action refiner、post-training refinement 与跨 embodiment 泛化消融

### [5]. Coarse-to-Control: Action-Token Planning for Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2606.07107) [[PDF]](https://arxiv.org/pdf/2606.07107) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.07107`
* **Authors**: Jinhao Wu, Shiduo Zhang, Yicheng Liu, Xiaopeng Yu, Sixian Li, Siyin Wang, Hang Zhao, Jing Huo, Yang Gao, Jingjing Gong, Xipeng Qiu, Yu-Gang Jiang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为它把 VLA 的链式推理从文本或图像中间结果移到 action-token space，更贴近真实控制轨迹。
* **关键词**: `action-token planning` `VLA` `Coarse-to-Control` `LIBERO` `long-horizon manipulation`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

许多 VLA 直接把观测和语言映射到动作，这在短任务中可以工作，但长时序任务会出现早期错误累积。根本张力在于，语言指令描述的是目标，而不是运动细节；策略必须在一次前向传播中同时解决 approach direction、wrist orientation、grasp pose 和 waypoint sequence。文本 CoT 可能能解释任务，但未必贴近控制流形；视觉 subgoal 又可能增加生成负担或与低层动作脱节。Coarse-to-Control 的动机是建立一个介于高层语义和可执行动作之间的中间层，但这个中间层不是自然语言，也不是未来图像，而是 coarse action tokens。这样规划信号与执行信号共享离散动作词表，理论上更容易约束在机器人可执行轨迹附近。

#### ⚙️ 核心方法

Coarse-to-Control 是一个 plan-execute VLA。策略先预测一段 compact coarse action tokens，用来概括未来轨迹意图；随后再在该 plan 条件下生成 executable action tokens。关键是 joint plan-execute tokenizer：长时序规划 token 和短时序可执行 token 位于共享离散 action vocabulary 中，因此规划不是外部文本 rationale，而是控制空间内的粗粒度轨迹表达。摘录中还说明，所有本地训练 policy variants 使用同一个 PaliGemma-based action-token VLA backbone，并从 FAST checkpoints 初始化；模型包含独立的 VLM、proprioception 和 action streams。摘录给出 evaluated configuration：VLM stream hidden size 2048，proprioception 和 action streams hidden size 1024，18 hidden layers，8 attention heads，1 key-value head，head dimension 256，maximum position length 8192，且这些评测中 LoRA disabled，加载 EMA weights 做 evaluation。方法上的新意是把 planning 内化到 action-token manifold，而不是依赖文本 CoT 或视觉 CoT；但 tokenizer 如何从连续轨迹抽取 coarse tokens、plan 长度如何设定、训练时是否有 teacher forcing，摘录不足，需要核查原文。

#### 📊 实验与结果

实验覆盖 simulation benchmarks 和 real-world robot manipulation。模拟部分使用 LIBERO 和 SimplerEnv-WidowX：LIBERO 包含 Spatial、Object、Goal、Long 四个 suite，按每任务 50 rollouts 汇报 per-suite 和 average success；SimplerEnv-WidowX 评估 real-to-sim generalization，覆盖四个 WidowX manipulation tasks，每任务 24 rollouts。对比 baseline 横跨 No-CoT、textual CoT、visual CoT 和 Action CoT 四类 reasoning styles。结论称 action-token reasoning 在 LIBERO、SimplerEnv-WidowX 和真实机器人任务上提升 benchmark performance，并显示设计选择的重要性。但摘录没有提供具体成功率、真实任务数量或消融数值，因此只能确认评测范围和主张方向。

#### ⚠️ 风险 / 保留意见

- coarse action token 的可解释性和覆盖度需要验证，若 tokenizer 设计偏差，规划 token 可能压缩掉关键控制细节。
- 共享离散动作词表可能贴近控制流形，但也可能限制连续精细控制精度。
- 真实机器人结果在摘录中缺少任务细节和失败分析，泛化强度需进一步核查。

#### 💭 结论与启发

这篇的关键启发是：长时序 VLA 的中间规划层最好与动作空间同构或至少强相关。相比让模型输出文字解释，action-token planning 更适合直接服务控制，也更容易做 ablation：去掉 plan、改变 coarse token 粒度、比较文本/视觉/action CoT。后续复现可以优先在 LIBERO-Long 和 SimplerEnv-WidowX 上检查早期错误是否减少，因为这类任务最能体现 plan-execute 分解的价值。

#### 🔎 读 PDF 先核查

- joint plan-execute tokenizer 如何构造 coarse action tokens，它们与 executable action tokens 的时间尺度关系是什么？
- action-token planning 相比 textual CoT 和 visual CoT 的提升是否主要出现在 LIBERO-Long 等长时序任务？
- 预测的 coarse plan 在推理时是否可被检查或纠错，错误 plan 会如何影响后续 executable actions？

#### 📌 上传 PDF 后优先看

- joint plan-execute tokenizer 与 coarse/action token 定义
- No-CoT、textual CoT、visual CoT、Action CoT 的公平对比设置
- LIBERO-Long、SimplerEnv-WidowX 和真实机器人长时序任务的消融结果

### [6]. Robotic Policy Adaptation via Weight-Space Meta-Learning [[HTML]](https://arxiv.org/html/2606.07217) [[PDF]](https://arxiv.org/pdf/2606.07217) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.07217`
* **Authors**: Christian Bianchi, Siamak Yousefi, Alessio Sampieri, Andrea Roberti, Luca Rigazio, Fabio Galasso, Luca Franco
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为 WIZARD 把 VLA 适配从任务级微调变成根据语言和短视频生成 LoRA 权重，直接瞄准部署成本。
* **关键词**: `weight-space meta-learning` `LoRA generation` `VLA adaptation` `LIBERO` `zero-shot policy adaptation`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

大型 VLA 虽然具备通用操控潜力，但遇到新任务或分布变化时通常仍需要 task-specific demonstrations、action annotations 和额外 fine-tuning。LoRA 等轻量 adapter 能降低微调成本，却没有消除“每个任务都要收集动作标注并训练一个专家”的流程负担。WIZARD 的动机是把适配问题转成 weight-space meta-learning：给定语言指令和一段短 demonstration video，直接生成 frozen VLA policy 的任务特定 LoRA 参数，而不是在测试时做梯度优化。这对真实部署很重要，因为用户更容易提供一段演示视频和任务描述，而不是提供完整动作标签数据集。论文还特别强调预训练 state-of-the-art 在 unseen dataset suite 上可能出现 0% success，这说明适配不是锦上添花，而是 VLA 落地的必要环节。

#### ⚙️ 核心方法

WIZARD 将 robotic test-time adaptation 形式化为权重生成问题。给定 frozen backbone 的 pretrained VLA，目标是在测试时不做 gradient-based optimization，而由 meta-network 根据 task evidence 生成 task-specific parameter updates。meta-training 数据由多个 manipulation tasks 构成，每个任务包含语言 prompt、视觉观测、proprioceptive state 和 action sequence；对每个任务，作者先获得 expert policy 或对应 LoRA 权重，再训练 meta-network 学习从任务证据到权重空间的映射。摘录中明确提到三个稳定训练原则：multimodal weight structuring、scale-aware parameter generation 和 alignment-oriented supervision in weight-space。直观上，语言负责给出目标语义，短视频提供任务动态和空间布局，而 meta-network 输出 LoRA 参数，使同一个 frozen VLA 在不同任务上获得不同适配。相对 retrieval-based adaptation 或 supervised fine-tuning，WIZARD 的新意在于直接遍历一个 learnable weight manifold。当前摘录不能确认 meta-network 架构、LoRA 注入层、视频编码方式和权重监督损失，需要重点核查。

#### 📊 实验与结果

实验重点是 strict held-out distribution shift 下的 weight-space inference，对比 supervised fine-tuning、retrieval-based adaptation 和 task-specific expert policies。LIBERO 是主 benchmark，包含 Spatial、Object、Goal 和 LIBERO-10；这些数据集环境相近但任务分布不同，适合测试 held-out generalization。摘录还提到真实世界结果、数据效率和 warm-start adaptation。一个明确数字来自结论摘录：在 LIBERO-Spatial Task 1 上，WIZARD 不做 task-specific gradient updates 达到 90% success，而 MT-VLA 从 22% 开始，需要约 25 个 demonstrations 才能追平。这个结果如果在正文中设置公平，说明权重生成可以显著降低标注与微调需求；但其他任务的完整数值仍需 PDF 表格验证。

#### ⚠️ 风险 / 保留意见

- WIZARD 依赖 meta-training 任务形成可学习的 weight manifold，超出训练任务族的泛化可能有限。
- 生成 LoRA 权重的稳定性和安全性需要验证，错误权重可能导致策略整体行为漂移。
- 短 demonstration video 若缺少动作标签，能否充分表达接触、力度和隐藏状态仍是部署风险。

#### 💭 结论与启发

WIZARD 对后续系统设计的启发是：VLA 适配可以不只在数据空间或 prompt 空间做，也可以在权重空间做。它适合作为“少示范、无动作标注、快速部署”的候选路线，尤其可与已有 frozen VLA 和 LoRA 基础设施结合。复现时应优先检查 held-out split 是否严格、expert LoRA 是否泄漏任务信息，以及生成 adapter 与少量真实微调结合时是否能作为 warm start。

#### 🔎 读 PDF 先核查

- meta-network 输入的短 demonstration video 是否只含视觉，还是也使用 proprioception 或其他状态信息？
- 生成 LoRA 的监督来自 task-specific expert policy 权重，还是还包含行为克隆/动作预测损失？
- WIZARD 在 LIBERO-10 长时序任务和真实世界任务上的表现是否同样接近 expert，而不只是单个 Spatial task 强？

#### 📌 上传 PDF 后优先看

- meta-network 架构、LoRA 注入位置和 weight-space supervision
- held-out distribution shift 的任务划分与 baselines 公平性
- 数据效率、warm-start adaptation 和真实世界实验结果

## Watchlist

### [W1]. STRIPS-WM: Learning Grounded Propositional STRIPS-style World Models from Images [[HTML]](https://arxiv.org/html/2606.06832) [[PDF]](https://arxiv.org/pdf/2606.06832)
* **Paper ID**: `2606.06832`
* **Authors**: Abhiroop Ajith, Constantinos Chamzas
* **Author Priority**: Standard
* **为什么还值得留意**: STRIPS-WM 进入 watchlist，因为它从图像转移到 grounded propositional STRIPS-style world model，正好对应视觉长时序规划中“哪些事实可行动、动作会改变什么”的核心问题。它没有进入最终精选，主要因为当前方向更偏 VLA/WAM/动作表示，而该文更偏符号任务规划；同时摘录中的实验集中在 BlocksWorld、DinnerTable 和 DinnerTable Real，机器人闭环部署证据相对有限。仍值得后续关注其 lexicographic objective、transition/applicability slack 和 sparse effects 是否能稳定从真实图像中学出可规划模型。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)

### [W2]. QuadVerse: An Integrated Framework Aligning Visual-Physical Reality for Quadruped Simulation [[HTML]](https://arxiv.org/html/2606.07118) [[PDF]](https://arxiv.org/pdf/2606.07118)
* **Paper ID**: `2606.07118`
* **Authors**: Yuxiang Chen, Yuanhao Wang, Ziheng Zhang, Meng Zhang, Yu Liu, Yufei Jia, Tiancai Wang, Erjin Zhou, Jin Xie
* **Author Priority**: Standard
* **为什么还值得留意**: QuadVerse 进入 watchlist，因为它把 3DGS 视觉重建、semantic mesh contact calibration 和 residual actuator compensation 放在同一个 quadruped real-to-sim-to-real 框架里，是 Sim2Real 方向很完整的一篇。没有进最终精选，是因为它主要服务四足 locomotion 和视觉导航，不是今天 VLA manipulation/WAM 的核心主线。摘录中的 Unitree Go2、RealSense D435i、Livox Mid-360、Isaac Gym、1024 parallel environments 和 2000 FPS rendering throughput 都说明工程系统含量很高，适合后续按 Sim2Real 专题单独深读。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. CAPE: Contrastive Action-conditioned Parallel Encoding for Embodied Planning [[HTML]](https://arxiv.org/html/2606.07304) [[PDF]](https://arxiv.org/pdf/2606.07304)
* **Paper ID**: `2606.07304`
* **Authors**: Cong Chen, Haowen Wang, Zhixiang Zhang, Pei Ren, Zhengping Che
* **Author Priority**: Standard
* **为什么还值得留意**: CAPE 进入 watchlist，因为它用 action-conditioned contrastive objective 学习未来状态表示，避免视觉 dynamics model 把容量浪费在规划无关的像素重建上，和 world model for planning 很相关。没有进最终精选，是因为摘录显示它更偏 representation/dynamics evaluation，包括 DROID 的 future-state retrieval、offline action matching 和 RoboCasa zero-shot evaluation，而不是完整 VLA/WAM 策略系统。后续应重点看 InfoNCE、parallel action-query decoder 和闭环规划效果之间是否有直接因果证据。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. Planning-aligned Token Compression for Long-Context Autonomous Driving [[VIP]] [[HTML]](https://arxiv.org/html/2606.07464) [[PDF]](https://arxiv.org/pdf/2606.07464)
* **Paper ID**: `2606.07464`
* **Authors**: Zhixuan Liang, Yuxiao Chen, Yurong You, Peter Karkus, Wenhao Ding, Boyi Li, Alexander Popov, Yan Wang, Maximilian Igl, Yiming Li, Danfei Xu, Nikolai Smolyanskiy, Boris Ivanovic, Ping Luo, Marco Pavone
* **Author Priority**: Extended VIP
* **为什么还值得留意**: COMPACT-VA 进入 watchlist，主要因为 Danfei Xu 在作者列表中，而且它把 long-context autonomous driving 的 token compression 与 trajectory planning 对齐，属于 VA/VLA 在自动驾驶中的重要变体。没有进最终精选，是因为任务域是 autonomous driving，不是本轮机器人操控/VLA/WAM 主线。它仍值得跟踪，尤其是 conditional VQ-VAE 工作记忆是否真的优于 temporal decay 等规则压缩，并能保留 stop-controlled intersections、yield 和 unprotected turns 中的决策关键历史。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
