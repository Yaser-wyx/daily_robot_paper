# RoboPulse | 2026-05-14

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 93 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线非常集中：VLA 正在从“更大模型直接端到端控制”转向可部署系统工程，包括鲁棒 RL 微调、长程任务分解、动作表示、数据筛选、低延迟推理和跨模态触觉控制。最终精选的 6 篇分别覆盖视觉扰动下的策略稳健性、agent-tool 式长程执行、连续旋转 latent action、示教帧冗余压缩、diffusion VLA 实时化，以及触觉-视觉 dexterous manipulation，彼此互补而不是同质重复。VIP 作者中，Pieter Abbeel 参与的 ViTacFormer 值得优先读完整实验；Donglin Wang 参与的 CUBic 虽未进最终精选，但在双臂统一感知控制上应继续跟踪。今天没有 Sergey Levine、Chelsea Finn、Pieter Abbeel 以外更多核心名单密集出现，因此更像是方法方向扩散的一天，而不是单一顶级组强势主导的一天。

## 今日信号

- VLA 的近期突破点不只在 backbone scale，而是在训练目标、执行接口和推理机制上补足部署时的弱环节。
- 长程 embodied agent 越来越倾向于把高层语义规划和低层 VLA 执行解耦，但关键问题变成调用接口是否足够可训练、可验证、可恢复。
- 动作表示和数据表示正在成为 VLA 的新瓶颈：latent action 几何结构、帧选择策略和 tactile forecasting 都在挑战“直接喂全量轨迹”的默认范式。

## Historical Rediscovery

- **Paper**: Retrieve-then-Steer: Online Success Memory for Test-Time Adaptation of Generative VLAs [[HTML]](https://arxiv.org/html/2605.10094) [[PDF]](https://arxiv.org/pdf/2605.10094)
  - **Paper ID**: `2605.10094`
  - **来源日期**: 2026-05-13
  - **当时可能被低估的信号**: 当时为了避免记忆类论文过度集中而被降权，但“persistent deployment + 成功经验检索 + test-time adaptation”其实是很强的真实机器人部署信号。
  - **为什么现在值得再看**: 现在 VLA 的核心问题正在从一次性 benchmark 成功率转向长期复用、场景内自适应和真实部署稳定性；这篇直接连接 VLA、在线适应和部署记忆，值得作为 RL+VLA / test-time adaptation 支线重看。
  - **建议动作**: 加入精读
  - **关键词**: `VLA` `test-time adaptation` `online memory` `persistent deployment` `generative policy`
- **Paper**: Unified Noise Steering for Efficient Human-Guided VLA Adaptation [[HTML]](https://arxiv.org/html/2605.10821) [[PDF]](https://arxiv.org/pdf/2605.10821)
  - **Paper ID**: `2605.10821`
  - **来源日期**: 2026-05-12
  - **当时可能被低估的信号**: 当时因证据集中在四个真实任务和 frozen decoder 设定而没有上提，但 action-to-noise inversion 与人类纠错成本这两个问题本身就是部署期 VLA 调参的关键瓶颈。
  - **为什么现在值得再看**: 如果你今天关注 RL 如何真正接入 VLA，而不是只在仿真里做 policy improvement，这篇提供了一个可核查的在线纠错与噪声空间适配切口。
  - **建议动作**: 加入精读
  - **关键词**: `RL+VLA` `human correction` `online RL` `flow matching` `noise steering`
- **Paper**: NoiseGate: Learning Per-Latent Timestep Schedules as Information Gating in World Action Models [[HTML]](https://arxiv.org/html/2605.07794) [[PDF]](https://arxiv.org/pdf/2605.07794)
  - **Paper ID**: `2605.07794`
  - **来源日期**: 2026-05-11
  - **当时可能被低估的信号**: 当时它被视为特定 WAM/MoT 训练策略，优先级低于动态一致性诊断类论文；但“按 latent timestep 控制信息流”可能是 WAM 训练稳定性和动作可控性的具体抓手。
  - **为什么现在值得再看**: WAM 现在的关键不只是能生成视频，而是生成过程如何被动作、奖励和任务目标稳定约束；这篇与 World Action Model、reward optimization 和细粒度 denoising control 强相关。
  - **建议动作**: 加入精读
  - **关键词**: `World Action Model` `latent schedule` `reward optimization` `video-action denoising` `RoboTwin`
- **Paper**: ELVIS: Ensemble-Calibrated Latent Imagination for Long-Horizon Visual MPC [[HTML]](https://arxiv.org/html/2605.04709) [[PDF]](https://arxiv.org/pdf/2605.04709)
  - **Paper ID**: `2605.04709`
  - **来源日期**: 2026-05-07
  - **当时可能被低估的信号**: 当时因为它偏 model-based RL/control、不是 language-conditioned VLA 而被放低，但“长时程 latent imagination + 不确定性截断 + sim-to-real”正好补上 VLA/WAM 在闭环规划评测里的缺口。
  - **为什么现在值得再看**: World Model 方向不能只看生成质量，还要看能否支撑长时程控制和真实迁移；这篇适合作为 World Model 到闭环控制、Sim2Real 的桥接论文重读。
  - **建议动作**: 快速浏览
  - **关键词**: `World Model` `visual MPC` `long-horizon planning` `Sim2Real` `model-based RL`
- **Paper**: SEVO: Semantic-Enhanced Virtual Observation for Robust VLA Manipulation via Active Illumination and Data-Centric Collection [[HTML]](https://arxiv.org/html/2605.11114) [[PDF]](https://arxiv.org/pdf/2605.11114)
  - **Paper ID**: `2605.11114`
  - **来源日期**: 2026-05-13
  - **当时可能被低估的信号**: 当时被看作数据采集与视觉预处理技巧，但历史记录里的真实机器人、100 trials per condition、ACT/SmolVLA 差异分析，是很具体的鲁棒性与部署评测信号。
  - **为什么现在值得再看**: 如果今天要判断 VLA 在真实场景里的泛化瓶颈，observation-space 语义增强和主动光照可能比复杂架构更快暴露 Sim2Real 问题；它和 VLA 鲁棒部署、低成本真实评测强相关。
  - **建议动作**: 快速浏览
  - **关键词**: `VLA` `Sim2Real` `robust manipulation` `active illumination` `real robot evaluation`

## Editor's Picks

### [1]. What to Ignore, What to React: Visually Robust RL Fine-Tuning of VLA Models [[HTML]](https://arxiv.org/html/2605.13105) [[PDF]](https://arxiv.org/pdf/2605.13105) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.13105`
* **Authors**: Yuanfang Peng, Jingjing Fu, Chuheng Zhang, Li Zhao, Jiang Bian, Mingyu Liu, Ling Zhang, Jun Zhang, Rui Wang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为它把 VLA 的 RL fine-tuning 从单纯追任务成功推进到“知道哪些视觉变化该忽略、哪些该响应”。
* **问题与切口**: PAIR-VLA 面向部署时视觉分布偏移：光照、纹理、干扰物或目标姿态变化可能只改变输入外观，也可能改变应执行动作。论文的切口不是再扩大预训练数据，而是在 PPO 微调中引入成对视觉变体，让策略同时学习 task-irrelevant invariance 和 task-relevant sensitivity。这比标准任务奖励更细，因为任务成功本身很难告诉模型视觉变化的动作语义。
* **核心方法与证据**: 方法在 PPO 上叠加两个辅助目标：一个约束任务无关视觉变体下动作分布更一致，另一个鼓励任务相关变化下保留可响应性。实验基于 ManiSkill3 pick-and-place 设置，覆盖 OpenVLA 和 flow-matching VLA backbone，并比较 OOD 成功率、微调效率、消融贡献和相机姿态等泛化情形。证据主要来自模拟环境，真实机器人迁移仍需 PDF 细读确认。
* **正文要点**:
  - 正文明确把视觉变化区分为应忽略的 nuisance shift 与应响应的 action-dependent shift。
  - 实验问题覆盖 OOD generalization、RL fine-tuning efficiency、目标消融和 viewpoint shift 泛化。
  - 结论声称在未用于构造成对视图的 lighting changes 上也有泛化收益，但这更适合作为趋势信号而非已充分闭环的真实部署证据。
* **为什么值得跟**:
  - 它给 VLA+RL 提供了比任务奖励更结构化的视觉鲁棒性监督。
  - 它直接回应部署场景中的视觉干扰，而不是只在训练分布内提升成功率。
  - 它可作为后续 sim2real robust fine-tuning 的目标函数模板。
* **风险 / 保留意见**:
  - 目前证据以 ManiSkill3 模拟任务为主，真实感知噪声和相机标定误差下的稳定性未知。
  - 成对视觉变体如何构造会强烈影响 invariance/sensitivity 的边界，复现时需要核查数据生成细节。
* **建议先看**: 先看作者如何定义 task-preserving 与 task-relevant visual variants，再看两个辅助目标与 PPO loss 的耦合方式。实验部分优先核查消融是否真的证明两个目标各自必要。
* **关键词**: `VLA` `RL fine-tuning` `visual robustness` `PPO` `OOD generalization`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 成对视觉变体是自动生成、规则构造还是任务特定标注，是否会限制扩展到真实场景？
  - invariance 项如何避免把本应响应的目标姿态或接触相关变化误压平？
  - 相较标准 PPO，收益主要来自更强鲁棒性还是来自额外正则带来的训练稳定性？
* **上传 PDF 后优先看**:
  - 辅助目标定义与 PPO 联合优化章节
  - 视觉变体构造和 benchmark 设置章节
  - OOD、消融、camera-pose/lighting 泛化实验

### [2]. Towards Long-horizon Embodied Agents with Tool-Aligned Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2605.13119) [[PDF]](https://arxiv.org/pdf/2605.13119) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.13119`
* **Authors**: Zixing Lei, Changxing Liu, Yichen Xiong, Minhao Xiong, Yuanzhuo Ding, Zhipeng Zhang, Weixin Li, Siheng Chen
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为它把 VLA 从单一长程控制器改造成可被 VLM agent 调用的工具族，正对长程 embodied task 的系统瓶颈。
* **问题与切口**: VLAs-as-Tools 认为当前 VLA 不适合独自承担长程任务中的全局规划、进度跟踪、失败恢复和具体控制。它让高层 VLM agent 负责场景理解与任务分解，把多个专门 VLA 作为 bounded subtask executor 调用。新意在于不只做 planner-policy 拼接，还提出 Tool-Aligned Post-Training，让 VLA 工具更忠实响应 agent invocation。
* **核心方法与证据**: 实验围绕四个问题：agent-tool 策略是否提升长程表现，tool-aligned post-training 是否增强调用忠实度，各组件贡献如何，以及少样本适应是否更高效。正文提到 OpenVLA-OFT、Physical Intelligence 系列模型等 backbone，在 LIBERO-Long、RoboTwin 和 CALVIN 上评估。证据边界在于工具划分、调用协议和恢复逻辑若高度手工化，真实开放任务泛化要谨慎判断。
* **正文要点**:
  - 框架把 temporal reasoning、global planning、recovery 与局部物理执行显式分工。
  - Tool-Aligned Post-Training 目标是提升 VLA 执行对 agent invocation 的 fidelity。
  - 实验覆盖 LIBERO-Long、RoboTwin 单臂任务和 CALVIN_D，强调长程与 subtask structure。
* **为什么值得跟**:
  - 它提供了一条比端到端长程 VLA 更现实的系统路线。
  - 它把 VLA 的价值重新定位为可组合技能执行器，便于接入已有 agent planning。
  - 它把 instruction alignment 和 downstream few-shot adaptation 放进同一框架评估。
* **风险 / 保留意见**:
  - 若 VLA 工具集合需要大量人工定义，系统可扩展性会受限。
  - 高层 VLM 的错误分解可能被低层工具忠实执行，从而放大计划层错误。
* **建议先看**: 先读 agent-tool 接口和 Tool-Aligned Post-Training 数据构造，再读 LIBERO-Long 上的失败恢复案例。重点判断它是通用架构创新，还是依赖具体 benchmark 的任务拆分。
* **关键词**: `long-horizon VLA` `VLM agent` `tool use` `post-training` `embodied planning`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
* **读 PDF 先核查**:
  - Tool-Aligned Post-Training 的训练样本如何连接自然语言调用、视觉状态和低层动作？
  - VLM agent 如何判断工具执行失败并触发 recovery，是否依赖外部状态标签？
  - 工具族规模扩大后，tool selection 错误和 subtask boundary 错误如何处理？
* **上传 PDF 后优先看**:
  - VLAs-as-Tools 架构与调用接口章节
  - Tool-Aligned Post-Training 数据与目标章节
  - LIBERO-Long、few-shot adaptation 和 ablation 实验

### [3]. RotVLA: Rotational Latent Action for Vision-Language-Action Model [[HTML]](https://arxiv.org/html/2605.13403) [[PDF]](https://arxiv.org/pdf/2605.13403) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.13403`
* **Authors**: Qiwei Li, Xicheng Gong, Xinghang Li, Peiyan Li, Quanyun Zhou, Hangjun Ye, Jiahuan Zhou, Yadong Mu
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为它把 latent action 从离散 token 推向连续旋转流形，直指跨 embodiment VLA 预训练的动作空间问题。
* **问题与切口**: RotVLA 关注 LAM 在异构机器人数据和人类视频预训练中的统一动作表示。作者批评离散量化式 encode-decode LAM 容易退化为目标帧重建，表达容量有限，也缺少物理结构。论文提出连续 rotational latent action，把 latent action 建模为具有连续性、可组合性和几何结构的旋转元素，并用 triplet frame learning 强化时间动态。
* **核心方法与证据**: 正文显示 LAM encoder 使用冻结 DINOv2 提取帧特征，再经时空 transformer；RotVLA 以 InternVL3.5-1B 初始化 VLM backbone，并接 flow-matching action expert。实验细节包含大规模预训练、下游 fine-tuning、absolute EEF pose 与 Rotate6D 表示。证据重点应核查：旋转 latent 是否真学到可转移 motion dynamics，而不只是更强模型和训练预算带来的收益。
* **正文要点**:
  - 论文明确指出离散 LAM 可能出现 trivial target-frame reconstruction。
  - RotVLA 用 continuous rotational latent action 替代离散 latent token。
  - triplet frame learning 被用来约束 temporal compositionality 并缓解 representation collapse。
* **为什么值得跟**:
  - 跨 embodiment VLA 的核心难点之一是动作空间对齐，这篇直接处理表示层。
  - 连续几何 latent 可能比离散 token 更适合接触、旋转和末端执行器轨迹。
  - 它把 latent action、flow matching 和 VLM backbone 结合成较完整的预训练路线。
* **风险 / 保留意见**:
  - HTML 摘录没有充分展示各 benchmark 的定量结果，需谨慎判断实际收益幅度。
  - 旋转 latent 与具体机器人 action space 的匹配可能依赖 abs EEF/Rotate6D 设定。
* **建议先看**: 先看 latent action 的数学定义和 triplet learning 目标，再看它与下游 action head 的接口。实验部分要把 LAM 表示消融和 backbone/training-budget 因素分开读。
* **关键词**: `latent action model` `rotational representation` `flow matching` `cross-embodiment` `VLA pretraining`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - rotational latent action 的群结构如何映射到非旋转主导的平移、夹爪或接触动作？
  - triplet frame learning 如何避免仅编码视觉帧差而不是可执行动作语义？
  - 与离散 LAM 对比时，是否控制了模型规模、预训练数据和下游 fine-tuning 步数？
* **上传 PDF 后优先看**:
  - rotational latent action 表示定义章节
  - triplet frame learning 与 collapse 防护章节
  - LAM 消融、跨 embodiment 和下游 manipulation 实验

### [4]. FrameSkip: Learning from Fewer but More Informative Frames in VLA Training [[HTML]](https://arxiv.org/html/2605.13757) [[PDF]](https://arxiv.org/pdf/2605.13757) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.13757`
* **Authors**: Bin Yu, Shijie Lian, Xiaopeng Lin, Zhaolong Shen, Yuliang Wei, Changti Wu, Hang Yuan, Haishan Liu, Bailing Wang, Cong Huang, Kai Chen
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为它从数据层挑战 VLA 训练默认假设：密集示教轨迹里的每一帧并不等价。
* **问题与切口**: FrameSkip 认为 teleoperation 轨迹中大量低变化片段会主导训练流，而对齐、接触、抓取、释放等关键转折反而稀疏，造成 temporal supervision imbalance。它不是改 VLA 架构或 loss，而是在训练前给帧打重要性分数，在目标 retention ratio 下保留更有信息量的帧。这个切口朴素但重要，尤其适合大规模 VLA 数据清洗和训练成本控制。
* **核心方法与证据**: 方法用 action variation、visual-action coherence、task-progress priors 和 gripper-transition preservation 计算帧级重要性，预缓存不同保留率下的索引，并在训练时重映射 dataset query。实验在 StarVLA 框架中进行，VLM understanding expert 来自 Qwen3-4B-VL-Instruct，action expert 为 DiT 并用 flow-matching 生成连续动作。证据主要说明不改模型即可改变监督分布，但具体阈值和任务依赖要细查。
* **正文要点**:
  - FrameSkip 明确把训练问题表述为 trajectory frame selection，而非模型结构改造。
  - 保留规则同时考虑动作变化、视觉-动作一致性、任务进度先验和夹爪状态转折。
  - 缓存 compressed views 后接入 minibatch training，推理过程保持不变。
* **为什么值得跟**:
  - 它可能降低 VLA 训练成本，同时减少低信息帧带来的监督偏置。
  - 它为 Open X-Embodiment 类大数据集提供了可落地的数据筛选思路。
  - 它提醒后续 VLA scaling 不能只看数据量，还要看时间监督密度。
* **风险 / 保留意见**:
  - 重要性评分包含 task-progress priors，跨任务迁移时可能需要重新校准。
  - 删除帧可能损害需要平滑控制或微小接触调整的任务，不能只看平均成功率。
* **建议先看**: 先读 importance estimator 的各项定义，再看不同 retention ratio 下的性能变化。重点核查它是否在长程、接触密集和低变化但高精度任务上仍然稳定。
* **关键词**: `data pruning` `VLA training` `trajectory redundancy` `frame selection` `flow matching`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - visual-action coherence 的计算是否依赖特定视觉编码器或动作尺度归一化？
  - 低保留率下，模型是否丢失了接触前微调和闭环纠偏所需的连续监督？
  - FrameSkip 在不同 benchmark 上的最优 retention ratio 是否一致，还是高度任务相关？
* **上传 PDF 后优先看**:
  - frame importance estimator 章节
  - retention ratio 与 cached index 训练机制章节
  - 不同任务类型、保留率和 ablation 实验

### [5]. Realtime-VLA FLASH: Speculative Inference Framework for Diffusion-based VLAs [[HTML]](https://arxiv.org/html/2605.13778) [[PDF]](https://arxiv.org/pdf/2605.13778) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.13778`
* **Authors**: Jiahui Niu, Kefan Gu, Yucheng Zhao, Shengwen Liang, Tiancai Wang, Xing Hu, Ying Wang, Huawei Li
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为它把 diffusion-based VLA 的推理延迟问题具体化为可工程实现的 speculative inference 框架。
* **问题与切口**: Realtime-VLA FLASH 针对 dVLA 在真实机器人上全量推理慢、replanning 频率受限的问题。它引入轻量 draft model 生成候选动作，并用主模型 Action Expert 做并行验证；在关键阶段或验证不可靠时，通过 phase-aware fallback 回到 full inference。新意不是单纯压缩模型，而是把高频控制中的多数 replanning 轮次走 flash path，同时保留可靠性后备。
* **核心方法与证据**: HTML 摘录给出较具体的实验设置：在线推理在单张 RTX 4090D 上，模拟评估 LIBERO 四个 suite，真实平台为 UR5 加双 RealSense D435i，在传送带分拣任务上测试。正文声称用 7.8 ms speculative round 替换许多 58.0 ms full inference round，并基本保持任务表现。证据边界在于 fallback 阈值偏启发式，且真实任务种类仍较窄。
* **正文要点**:
  - FLASH 包含 lightweight draft model、parallel verification 和 phase-aware fallback 三个核心环节。
  - 目标是减少 replanning 时 full inference 调用，而不是改变底层 dVLA 训练范式。
  - 实验同时覆盖 LIBERO 模拟和 UR5 conveyor-belt sorting 真实任务。
* **为什么值得跟**:
  - 实时性是 VLA 上机器人部署的硬门槛，这篇直接处理 latency-control mismatch。
  - speculative inference 为 diffusion policy 类模型提供了不同于 action chunking 的加速方向。
  - fallback 机制让低延迟路径可以在可靠性不足时退回高保真推理。
* **风险 / 保留意见**:
  - 阈值和 phase 判断若需人工调参，跨任务泛化和稳定性会受影响。
  - 真实实验只覆盖有限的 reactive manipulation 场景，难以代表复杂长程任务。
* **建议先看**: 先看 flash path 与 full path 的切换条件，再看验证失败和 fine-adjustment phase 的处理。实验部分重点核查速度收益是否伴随隐藏的成功率、平滑性或安全性代价。
* **关键词**: `diffusion VLA` `speculative inference` `real-time control` `latency` `replanning`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - draft model 的训练目标和主模型 Action Expert 验证标准是否会引入分布不匹配？
  - phase-aware fallback 如何识别需要高保真推理的阶段，是否依赖任务特定启发式？
  - 高频 replanning 对动作平滑性、碰撞风险和控制稳定性有什么影响？
* **上传 PDF 后优先看**:
  - FLASH 推理路径与验证机制章节
  - phase-aware fallback 和阈值设计章节
  - LIBERO 延迟-成功率权衡与真实 UR5 实验

### [6]. ViTacFormer: Learning Cross-Modal Representation for Visuo-Tactile Dexterous Manipulation [[VIP]] [[HTML]](https://arxiv.org/html/2506.15953) [[PDF]](https://arxiv.org/pdf/2506.15953) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2506.15953`
* **Authors**: Liang Heng, Haoran Geng, Kaifeng Zhang, Pieter Abbeel, Jitendra Malik
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，尤其因为 Pieter Abbeel 参与且主题从 VLA 扩展到视觉-触觉 dexterous manipulation 的表示学习。
* **问题与切口**: ViTacFormer 关注灵巧操作中视觉不足以覆盖的接触、遮挡和摩擦控制问题。它用 cross-attention encoder 融合高分辨率视觉与触觉信号，并加入 autoregressive tactile-prediction head 预测未来接触，从而让策略不只被动读取当前触觉，而是学习可用于动作生成的跨模态表示。相对普通视觉 imitation learning，它把 tactile forecasting 变成控制表示的一部分。
* **核心方法与证据**: 方法部分包含 cross-attention multimodal integration、autoregressive tactile forecasting、整体网络与学习流程。实验设计回答两类问题：与 imitation learning SOTA 的比较，以及各组件是否有效。任务覆盖 Peg Insertion、Cap Twist、Vase Wipe、Book Flip 和 making hamburgers 等长程/精细操作。论文也在结论中承认依赖人类遥操作数据，且对未见新任务的自主泛化有限。
* **正文要点**:
  - 模型显式用 cross-attention 建模视觉和触觉之间的依赖，而非简单 token 拼接。
  - autoregressive tactile prediction 用于提前建模未来接触信号。
  - 实验任务包含视觉遮挡、旋转控制、摩擦控制和长程组合操作。
* **为什么值得跟**:
  - 触觉是 dexterous manipulation 的关键信号，这篇把它放到表示学习核心位置。
  - 未来 VLA 若要处理高精度接触任务，需要类似的跨模态预测能力。
  - Abbeel/Malik 组合让这篇在机器人学习和视觉表示两端都值得跟踪。
* **风险 / 保留意见**:
  - 方法仍是 imitation learning 范式，泛化到未见任务的能力被作者自己列为限制。
  - 触觉硬件、数据采集和同步质量可能显著影响复现难度。
* **建议先看**: 先看 cross-attention 融合和 tactile forecasting 是否真正影响 action generation，再看长程任务中错误恢复能力。实验部分尤其要关注组件消融和触觉缺失/噪声条件。
* **关键词**: `visuo-tactile learning` `dexterous manipulation` `cross-attention` `tactile forecasting` `imitation learning`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - tactile forecasting head 是作为辅助损失提升表示，还是在推理时直接影响动作选择？
  - 视觉-触觉 cross-attention 在遮挡和接触密集任务上分别贡献多少？
  - making hamburgers 这类长程任务的成功是否来自表示泛化，还是来自任务特定示教覆盖？
* **上传 PDF 后优先看**:
  - cross-attention multimodal integration 章节
  - autoregressive tactile forecasting 章节
  - 任务对比、组件消融和 long-horizon manipulation 实验

## Watchlist

### [W1]. BlockVLA: Accelerating Autoregressive VLA via Block Diffusion Finetuning [[HTML]](https://arxiv.org/html/2605.13382) [[PDF]](https://arxiv.org/pdf/2605.13382)
* **Paper ID**: `2605.13382`
* **Authors**: Ruiheng Wang, Shuanghao Bai, Haoran Zhang, Badong Chen, Xiangyu Xu
* **Author Priority**: Standard
* **为什么还值得留意**: BlockVLA 进入 shortlist 是因为它处理 AR VLA 的推理延迟和长程误差积累，提出 block diffusion finetuning，在动作块之间保持 autoregressive 依赖、块内并行 denoising。它没有进入最终精选，主要因为今天已有 Realtime-VLA FLASH 更直接覆盖部署实时性，而 BlockVLA 的贡献更偏 decoding/architecture 效率，需进一步确认在真实机器人和低 NFE 设置下的收益边界。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. CUBic: Coordinated Unified Bimanual Perception and Control Framework [[VIP]] [[HTML]](https://arxiv.org/html/2605.13452) [[PDF]](https://arxiv.org/pdf/2605.13452)
* **Paper ID**: `2605.13452`
* **Authors**: Xingyu Wang, Pengxiang Ding, Jingkai Xu, Donglin Wang, Zhaoxin Fan
* **Author Priority**: Core VIP
* **为什么还值得留意**: CUBic 值得 watchlist，因为 Donglin Wang 属于核心关注作者，且双臂 manipulation 的独立感知与协同控制是重要问题。它未进最终精选，是因为主题更偏 bimanual visuomotor policy，而不是今天主线里最强的 VLA/RL/world-model 交叉；不过其 shared tokenized representation 和 RoboTwin/real-world 评估值得后续核查。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. Guide, Think, Act: Interactive Embodied Reasoning in Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2605.13632) [[PDF]](https://arxiv.org/pdf/2605.13632)
* **Paper ID**: `2605.13632`
* **Authors**: Yiran Ling, Qing Lian, Jinghang Li, Qing Jiang, Tianming Zhang, Xiaoke Jiang, Chuanxiu Liu, Jie Liu, Lei Zhang
* **Author Priority**: Standard
* **为什么还值得留意**: GTA-VLA 进入 shortlist 是因为它把 human visual guidance、spatial CoT 和 OOD failure recovery 接入 VLA，方向上贴近可纠正 embodied agent。没有进入最终精选，是因为最终集合已包含视觉鲁棒 RL 和长程 agent-tool 两条更核心路线；GTA-VLA 的交互指导机制仍需看 PDF 中是否真正超越 benchmark prompt/interface 设计。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

### [W4]. MindVLA-U1: VLA Beats VA with Unified Streaming Architecture for Autonomous Driving [[HTML]](https://arxiv.org/html/2605.12624) [[PDF]](https://arxiv.org/pdf/2605.12624)
* **Paper ID**: `2605.12624`
* **Authors**: Yuzhou Huang, Benjin Zhu, Hengtong Lu, Victor Shea-Jay Huang, Haiming Zhang, Wei Chen, Jifeng Dai, Yan Xie, Hongsheng Li
* **Author Priority**: Standard
* **为什么还值得留意**: MindVLA-U1 值得 watchlist，因为它把 VLA 放到自动驾驶端到端系统里，提出 unified streaming architecture、shared backbone、streaming memory 和 language-to-action route。它没有进入最终精选，主要是 domain 偏 autonomous driving，和今天机器人 manipulation/VLA 部署主线稍有距离；但如果后续关注 world action model 或 streaming embodied memory，它应被重新拉高优先级。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
