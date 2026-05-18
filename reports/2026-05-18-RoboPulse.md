# RoboPulse | 2026-05-18

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 81 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线不是单纯把 VLA 做大，而是围绕“物理先验、世界模型反馈、动作世界模型、RL 训练效率、灵巧/移动操作基准”重新整理机器人学习的可迁移性问题。最终精选保留了从大规模人类视频获取物理常识、用在线反馈修正 world model、把 aerial VLN 改写为 world-action prediction、降低 VLA RL 梯度开销、建设灵巧手 MuJoCo 基准，以及从 robot-free human demos 学 whole-body mobile manipulation 这六条互补路线。VIP 作者里，He Wang 参与的 DexJoCo 值得优先跟踪，因为它直接补齐灵巧手评测和数据工具链；Jeannette Bohg 与 Shuran Song 参与的 HoMMI 也应优先看，因为它把人类示教、移动操作和跨 embodiment policy 设计连在了一起。Jiangmiao Pang 参与的 STABLE 虽未进精选，但在“任务到仿真场景生成”方向与 Sim2Real 数据闭环强相关，建议放入后续观察。

## 今日信号

- VLA 研究正在从“更多机器人轨迹”转向“先获得物理常识、场景生成能力和跨 embodiment 表征，再适配到动作”。
- World model 的重点开始从离线预测未来，转向测试时闭环校正、短时潜变量预测和可控动作解码。
- VLA+RL 的瓶颈不一定在采样，训练中哪些动作片段真正产生学习信号，正在成为效率优化的核心问题。

## Historical Rediscovery

- **Paper**: WarmPrior: Straightening Flow-Matching Policies with Temporal Priors [[HTML]](https://arxiv.org/html/2605.13959) [[PDF]](https://arxiv.org/pdf/2605.13959)
  - **Paper ID**: `2605.13959`
  - **来源日期**: 2026-05-15
  - **当时可能被低估的信号**: 用近期动作历史构造 source distribution，而不是只改网络结构；同时历史记录明确提到扩展到 prior-space RL，这比普通 policy smoothing 更接近可部署控制问题。
  - **为什么现在值得再看**: 对 VLA、RL+VLA 和真实机器人 action chunk/control 都有直接参考价值，尤其适合重新评估生成式动作头如何利用历史动作降低采样难度。
  - **建议动作**: 加入精读
  - **关键词**: `VLA action head` `flow matching policy` `temporal prior` `RL exploration`
- **Paper**: Slot-MPC: Goal-Conditioned Model Predictive Control with Object-Centric Representations [[HTML]](https://arxiv.org/html/2605.14937) [[PDF]](https://arxiv.org/pdf/2605.14937)
  - **Paper ID**: `2605.14937`
  - **来源日期**: 2026-05-15
  - **当时可能被低估的信号**: 历史记录里同时出现 object-centric slot representation、action-conditioned dynamics 和推理时 MPC，这三个信号组合起来比单纯表征学习更有长期规划价值。
  - **为什么现在值得再看**: 如果今天关注 VLA 外接 world model、规划 wrapper 或长时程 manipulation，这篇可作为非语言侧的 dynamics-planning 参考点。
  - **建议动作**: 加入精读
  - **关键词**: `world model` `object-centric representation` `MPC` `goal-conditioned planning`
- **Paper**: MAPLE: Latent Multi-Agent Play for End-to-End Autonomous Driving [[HTML]](https://arxiv.org/html/2605.14201) [[PDF]](https://arxiv.org/pdf/2605.14201)
  - **Paper ID**: `2605.14201`
  - **来源日期**: 2026-05-15
  - **当时可能被低估的信号**: reactive agents、diversity-aware RL 和 closed-loop rollout 这些信号当时可能被“不是 manipulation”掩盖了。
  - **为什么现在值得再看**: 对真实部署评测、闭环训练和多智能体交互中的 VLA+RL 很有启发，尤其适合借鉴其如何避免只做 open-loop 指标。
  - **建议动作**: 快速浏览
  - **关键词**: `VLA` `closed-loop rollout` `diversity-aware RL` `deployment evaluation`
- **Paper**: EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields [[HTML]](https://arxiv.org/html/2605.06192) [[PDF]](https://arxiv.org/pdf/2605.06192)
  - **Paper ID**: `2605.06192`
  - **来源日期**: 2026-05-08
  - **当时可能被低估的信号**: 历史记录强调它不是泛泛视频生成，而是让动作和运动学状态更精确地指导未来视频合成，这正是 World Action Model 的关键接口。
  - **为什么现在值得再看**: 值得用来比较 VLA/WAM 中 action-conditioned prediction 的设计选择，尤其是空间几何、交互动态和事件感知融合。
  - **建议动作**: 加入精读
  - **关键词**: `world model` `action-conditioned video` `kinematic action field` `World Action Model`
- **Paper**: DOT-Sim: Differentiable Optical Tactile Simulation with Precise Real-to-Sim Physical Calibration [[HTML]](https://arxiv.org/html/2604.27367) [[PDF]](https://arxiv.org/pdf/2604.27367)
  - **Paper ID**: `2604.27367`
  - **来源日期**: 2026-05-01
  - **当时可能被低估的信号**: 精确 real-to-sim physical calibration、可微校准和光学触觉渲染的组合，比普通仿真平台更接近可复现实验闭环。
  - **为什么现在值得再看**: 如果后续研究涉及 contact-rich manipulation、触觉 VLA 或真实部署前的仿真校准，这篇能补齐 Sim2Real 和物理感知侧的关键背景。
  - **建议动作**: 继续跟踪
  - **关键词**: `Sim2Real` `tactile simulation` `real-to-sim calibration` `contact-rich manipulation`

## Editor's Picks

### [1]. PhysBrain 1.0 Technical Report [[HTML]](https://arxiv.org/html/2605.15298) [[PDF]](https://arxiv.org/pdf/2605.15298) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.15298`
* **Authors**: Shijie Lian, Bin Yu, Xiaopeng Lin, Changti Wu, Hang Yuan, Xiaolin Hu, Zhaolong Shen, Yuzhuo Miao, Haishan Liu, Yuxuan Tian, Yukun Shi, Cong Huang, Kai Chen
* **Author Priority**: Standard
* **一句话结论**: 值得优先看：PhysBrain 把人类第一视角视频转成物理常识监督，再迁移到 VLA，是对“机器人轨迹不够覆盖物理世界”这一瓶颈的正面回应。
* **关键词**: `Physical commonsense` `Egocentric video` `VLA adaptation` `Structured QA supervision` `Embodied priors`
* **证据来源**: arXiv HTML (Introduction)

#### 📖 背景与动机

PhysBrain 1.0 的出发点是，当前 VLA 很多进展仍围绕“收集机器人轨迹、拟合动作策略、继续扩数据”展开，但机器人交互数据昂贵、平台相关，并且轨迹模仿本身不保证模型理解视角变化、物体状态、空间关系和任务组合背后的物理规律。论文提出“Understanding first, action next”的原则，把 embodied intelligence 的训练重心从动作模仿推向物理 commonsense acquisition。对机器人/VLA 来说，这条线重要在于它试图利用人类 egocentric video 的规模优势，给机器人策略补充更广泛的物理先验，再在下游 VLA 中适配，而不是把所有能力都压在机器人数据采集上。

#### ⚙️ 核心方法

当前摘录可以确认的核心方法是一个两阶段路线。第一阶段是 data engine：从大规模人类第一视角视频中抽取 scene elements、spatial dynamics、action execution 和 depth-aware relations，并把这些结构化物理信息转成 question-answer supervision，用来训练 PhysBrain VLMs。这里的新意不是简单视频字幕化，而是把人类视频中的对象、空间、动作执行和深度关系组织成可监督的物理常识任务。第二阶段是从 PhysBrain VLM 到 VLA policy 的迁移，摘要明确提到采用 capability-preserving 和 language-sensitive 的 adaptation design，目标是在保留已有视觉语言能力的同时，把物理先验传给动作策略。摘录没有给出完整模块图、损失函数或适配层细节，因此只能保守判断：它更像是“物理理解预训练 + VLA 适配”的系统报告，而非单一控制算法。

#### 📊 实验与结果

摘录只明确说结果覆盖多个场景或指标的开头信息，但没有提供完整 benchmark 名称、具体任务、对比模型和数值。因此这里不能引用未展示的实验数字。可确认的证据边界是：论文声称 PhysBrain VLM 学到的物理 priors 会进一步 transfer 到 VLA policies，并试图证明这些 priors 对 action adaptation 有价值。读原文时应重点核查实验是否真正隔离了“物理常识监督”的贡献，例如与纯视频字幕监督、纯机器人轨迹训练、只加数据不加结构化 QA 的基线相比是否有稳定收益；还要看是否包含真实机器人结果，还是主要停留在视觉语言理解与模拟任务。

#### ⚠️ 风险 / 保留意见

- 摘录没有提供完整实验表和数值，当前只能把有效性视为待核查主张。
- 从人类 egocentric video 到机器人动作策略存在明显 embodiment gap，迁移设计是否足够强需要看消融。
- 结构化 QA 监督的质量高度依赖 data engine，自动抽取错误可能被模型系统性吸收。

#### 💭 结论与启发

这篇的启发在于，VLA 的下一步可能不是单纯追加 action tokens 或更大 robot dataset，而是要把“物理世界如何变化”作为中间学习目标显式建模。后续选题可以沿着三个方向推进：一是建立可审计的物理关系抽取数据管线，二是研究物理 VLM 到 VLA action head 的低破坏适配，三是设计能区分语言理解、视觉识别和真实物理推理的评测。复现时不宜一开始追求全量系统，先验证小规模 egocentric video QA 是否能提升具体 manipulation generalization。

#### 🔎 读 PDF 先核查

- PhysBrain 的 data engine 如何把 scene elements、spatial dynamics、action execution 和 depth-aware relations 变成可验证的 QA 样本？
- capability-preserving 和 language-sensitive adaptation 具体保护了哪些 VLM/VLA 能力，是否有对应消融？
- 下游 VLA 提升来自物理先验本身，还是来自额外视频数据规模和语言监督的混合效应？

#### 📌 上传 PDF 后优先看

- 数据引擎与物理 QA 构造章节
- PhysBrain VLM 到 VLA policy 的适配设计章节
- 下游 VLA 对比实验与消融表

### [2]. Feedback World Model Enables Precise Guidance of Diffusion Policy [[HTML]](https://arxiv.org/html/2605.15705) [[PDF]](https://arxiv.org/pdf/2605.15705) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.15705`
* **Authors**: Tuo An, Jindou Jia, Gen Li, Jingliang Li, Chuhao Zhou, Pengfei Liu, Bofan Lyu, Jiaqi Bai, Xinying Guo, Geng Li, Jianfei Yang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看：它把 world model 从静态开环预测器改成测试时在线校正器，直接服务 diffusion policy 的 OOD 引导。
* **关键词**: `Feedback world model` `Diffusion policy` `Test-time guidance` `OOD robustness` `Latent observer`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

World model 在机器人里常被用来预测动作后果，从而辅助训练、规划或测试时动作选择；但实际部署中，一旦机器人进入训练分布外状态，模型预测会漂移，开环滚动越长越不可信。Feedback World Model 抓住一个很实际的信号：执行动作后，机器人会观察到真实下一状态，这个观测天然暴露了预测与现实的偏差。论文因此把问题从“训练一个更强的世界模型”改成“在推理时用真实观测不断修正世界模型的 latent predictive state”。这对 Sim2Real 和 VLA/RL 都重要，因为真实部署中分布偏移不可避免，在线闭环纠偏可能比继续离线扩数据更可控。

#### ⚙️ 核心方法

方法的核心是 feedback world model。与把 pretrained world model 当成固定 open-loop predictor 不同，它在执行过程中维护一个 lightweight feedback state，并在每次观察真实 next state 后在线更新，用这个状态补偿后续 latent prediction 的误差。摘录明确说该过程不需要额外训练数据，也不更新模型参数，并且可解释为 latent-space observer，论文还声称具有收敛保证。用于控制时，作者把更可靠的 feedback prediction 与 controllability-aware 或 action-aware guidance 结合，去指导 diffusion policy 的动作生成：世界模型不只是预测未来，还根据动作是否能带来可控、任务一致的后果来影响采样方向。这里的新意在于把预测误差校正纳入测试时闭环，而不是只在训练阶段把 world model 当辅助 loss，或在推理时用静态模型评估候选动作。

#### 📊 实验与结果

实验围绕两个问题：在线反馈是否能降低 OOD prediction error，以及结合可控性引导后是否能提升 diffusion policies 的 OOD success rate。模拟部分覆盖 Robomimic 和 LIBERO-Plus 共七个 manipulation tasks；Robomimic 使用 Square、Tool-Hang、Transport，并在 low-data regime 下只用官方 demonstrations 的 20% 训练 diffusion policy；LIBERO-Plus 使用 LIBERO-10 中四个 single-task settings，重点是官方 robot initial-state perturbation 类别。真实实验也包含 manipulation tasks，OOD 由 robot initial-state perturbations 引入。摘录没有给出具体成功率数字，因此只能确认实验设置较完整，不能扩写定量幅度。

#### ⚠️ 风险 / 保留意见

- 反馈修正依赖每步真实观测质量，遮挡、感知延迟或状态估计噪声可能破坏 observer 假设。
- OOD 设置主要来自初始状态扰动，是否覆盖物体属性、动力学、任务组合变化仍需查全文。
- guidance 与 diffusion policy 的计算开销和实时性在真实机器人上需要重点核查。

#### 💭 结论与启发

这篇对系统设计的最大启发是：world model 不必承担一次性准确预测整个未来的压力，可以作为执行时持续校正的 latent observer。后续如果做 VLA 或 diffusion policy 的真实部署，可以考虑把观测反馈写进推理循环，让模型每个 action chunk 后更新对环境的内部预测，再决定下一步动作。复现优先级应放在小型 OOD manipulation benchmark 上，先验证 prediction error 的在线下降是否稳定，再看 policy success 是否跟随改善。

#### 🔎 读 PDF 先核查

- feedback state 的更新规则具体依赖哪些 latent 变量，是否需要访问真实状态还是只用视觉观测？
- action-aware guidance 如何度量 controllability，它与 diffusion sampling 的接口是什么？
- 在线 prediction error 降低是否必然转化为任务成功率提升，在哪些任务上二者可能脱钩？

#### 📌 上传 PDF 后优先看

- feedback world model 与 latent observer 理论章节
- controllability-aware/action-aware guidance 方法章节
- Robomimic、LIBERO-Plus 与真实机器人 OOD 实验表

### [3]. WorldVLN: Autoregressive World Action Model for Aerial Vision-Language Navigation [[HTML]](https://arxiv.org/html/2605.15964) [[PDF]](https://arxiv.org/pdf/2605.15964) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.15964`
* **Authors**: Baining Zhao, Jiacheng Xu, Weicheng Feng, Xin Zhang, Zhaolu Wang, Haoyang Wang, Shilong Ji, Ziyou Wang, Jianjie Fang, Zhiheng Zheng, Weichen Zhang, Yu Shang, Wei Wu, Chen Gao, Xinlei Chen, Yong Li
* **Author Priority**: Standard
* **一句话结论**: 值得优先看：WorldVLN 把 aerial VLN 明确建模为 autoregressive world-action problem，是 world action model 在导航场景的一次系统化落地。
* **关键词**: `World action model` `Aerial VLN` `Autoregressive prediction` `UAV navigation` `Action-aware GRPO`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)

#### 📖 背景与动机

Aerial VLN 要求无人机根据自然语言指令，在 3D 环境中闭环感知并连续行动。传统 VLN/VLA 往往直接从当前观测和语言映射到动作，但导航中的困难在于局部视野、长距离路径、语言目标和未来状态耦合紧密，单步反应式策略容易在未见环境中失效。WorldVLN 的动机是，导航智能不应只回答“现在该做什么”，还要预测“做了这个动作后世界状态会如何变化”。因此它把 aerial VLN 重写为 prediction-driven world-action problem，让 agent 通过短时世界状态转移预测来选择动作。这条路线与 World Model/World Action Model 方向高度一致，也比全序列视频生成更贴近实时控制。

#### ⚙️ 核心方法

WorldVLN 的核心是 autoregressive world action model。摘录说明它不是生成完整未来视频 clip，而是适配 latent autoregressive video backbone，用于预测 short-horizon world-state transitions，并直接解码动作。实验设置中提到它使用 InfinityStar 作为 latent autoregressive backbone，action decoder 初始化来自 Wan VAE 和 TSformer-VO-style priors。可以保守理解为：模型在潜空间里逐步预测局部世界演化，同时把预测结果接到动作解码器上，实现闭环导航决策。论文还提到 Action-aware GRPO，用来把动作层面的强化学习信号引入训练，并在消融中分析 autoregressive architecture 和 Action-aware GRPO 的作用。当前摘录没有展示完整网络结构、token 定义和损失细节，因此不能断言其 WAM 形式与其他 world model 的精确差异，只能确认它强调短视野潜变量预测与动作联合。

#### 📊 实验与结果

实验覆盖 outdoor 和 indoor UAV benchmarks，包括 UAV-Flow 和 IndoorUAV，并与代表性 VLN 与 VLA baselines 按相应 benchmark protocol 比较。摘录明确说作者分析 training curves 来展示 WAM paradigm 的潜力，并对 autoregressive architecture 与 Action-aware GRPO 做消融，最后还部署到真实 UAV 平台以观察 real-world generalization。训练资源方面，摘录给出使用 8 张 NVIDIA A800 80GB GPU，simulator rollouts 在 RTX 4090 workstation 上执行。虽然摘要声称 WorldVLN 在表 1 和表 2 中表现强，但摘录没有给出具体数值，不能引用提升幅度。

#### ⚠️ 风险 / 保留意见

- 无人机导航的安全约束和真实部署细节在摘录中不足，需核查是否只是有限场景演示。
- 模型依赖大型潜变量视频 backbone，训练和部署成本可能较高。
- 短视野 world-state prediction 对长程语义目标的帮助程度需要看失败案例和消融。

#### 💭 结论与启发

这篇给后续 WAM 选题的启发是，把 world model 压缩成短时、潜空间、动作可解码的模块，可能比追求高保真视频生成更适合机器人闭环控制。对 VLA 导航系统而言，可以尝试把“预测未来观测”与“输出下一步动作”合并训练，而不是把规划、视觉语言理解和控制完全分开。阅读全文时应重点判断 Action-aware GRPO 是否真的改变了策略学习，还是主要收益来自更强 backbone 和预训练初始化。

#### 🔎 读 PDF 先核查

- WorldVLN 的 latent world-state transition 是如何表示和监督的，是否需要显式未来观测标签？
- Action-aware GRPO 相比普通 GRPO 或行为克隆具体改进了哪些导航失败模式？
- 真实 UAV 部署与仿真 benchmark 之间的观测、动作和动力学接口是否一致？

#### 📌 上传 PDF 后优先看

- 模型架构与 latent autoregressive backbone 章节
- Action-aware GRPO 训练目标与消融章节
- UAV-Flow、IndoorUAV 和真实 UAV 部署实验章节

### [4]. Learn Where Outcomes Diverge: Efficient VLA RL via Probabilistic Chunk Masking [[HTML]](https://arxiv.org/html/2605.16154) [[PDF]](https://arxiv.org/pdf/2605.16154) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.16154`
* **Authors**: Vaidehi Bagaria, Nikshep Grampurohit, Pulkit Verma
* **Author Priority**: Standard
* **一句话结论**: 值得优先看：它指出 VLA RL 的主要耗时可能是梯度计算而非 rollout，并用 probabilistic chunk masking 把学习集中到结果分歧片段。
* **关键词**: `VLA RL` `GRPO` `Probabilistic chunk masking` `Training efficiency` `LIBERO`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

#### 📖 背景与动机

VLA 后训练越来越依赖 RL，尤其是 GRPO 这类 critic-free 方法，因为它可以直接优化任务成功而不必训练额外 value model。但大家常把效率瓶颈默认放在 rollout collection，于是去做更快模拟器或 world model 加速采样。本文的关键观察是，在作者的运行中 gradient computation 占每步 wall-clock time 的 78%，rollout collection 只占 21%。问题不是没有数据，而是反向传播在每个 action chunk 上都花费算力，包括许多对成败差异贡献很小的阶段。对大 VLA 来说，这个判断很重要：7B 级模型的后训练成本可能主要来自无差别更新，而不是环境交互。

#### ⚙️ 核心方法

论文提出 Probabilistic Chunk Masking，核心思想是只对更可能区分成功和失败 outcome 的 action chunks 计算 actor update，把梯度预算从全轨迹转移到更有学习价值的片段。实验中模型是 OpenVLA-OFT，一个预测 7-DoF action chunks 的 7B VLA。作者先用 deterministic、multi-grasp-aware 的规则给每个 chunk 标注语义阶段：active-grip 表示持续抓取和搬运，pre-grasp 是 sustained closure 前最多三个 chunks，release-ramp 是释放后的最多三个 chunks，approach 覆盖接触前剩余片段，tail 覆盖释放后 open-gripper 片段；重叠窗口用优先级处理。PCM 与 full-trajectory chunk-level GRPO 的差别在于 actor update 是否覆盖全部 chunks，其他 rollout groups、rewards、advantages 和 optimizer settings 保持一致。当前摘录没有展示概率采样公式细节，但可以确认其方法目标是选择性分配梯度，而不是改变环境或奖励。

#### 📊 实验与结果

实验基于 SimpleVLA-RL 和 verl pipeline，使用 GRPO groups of 10 rollouts per prompt，在 LIBERO-Object、LIBERO-Spatial 和 LIBERO-Goal 上评估。摘录中的 RQ1 对比显示，在 LIBERO-Object 上，PCM 与 full-trajectory GRPO 使用同一 SFT 初始化 OpenVLA-OFT、相同 rollout groups、rewards、advantages 与 optimizer settings，并训练固定 200 steps；两者 step-wise learning curves 几乎相同，最终 accuracy 匹配。论文据此主张 PCM 保持每步学习动态，同时提升效率。需要注意的是，摘录没有给出节省的实际 wall-clock 数字或跨全部 benchmark 的完整成功率表。

#### ⚠️ 风险 / 保留意见

- phase labeling 依赖 gripper-close fraction 和手工规则，迁移到非抓取任务或灵巧手动作可能不稳。
- 当前证据主要围绕 LIBERO manipulation，真实机器人 RL 成本和收益仍需核查。
- 跳过部分 chunk 的梯度可能漏掉长程依赖，尤其是导航、观察调整或前置接触策略。

#### 💭 结论与启发

这篇提示后续做 VLA RL 不能只盯 rollout 加速，必须先 profiling 训练时间组成。对于复现或系统优化，可以把 action chunk 按语义阶段、成功失败分歧和 advantage variance 排序，只更新高信息片段，以降低 7B VLA 后训练成本。更长远看，PCM 的思想可扩展成“学习哪些时刻值得学习”的 credit assignment 模块，与 world model 的预测误差、接触事件或视觉变化结合，形成更通用的选择性更新策略。

#### 🔎 读 PDF 先核查

- PCM 的 chunk 采样概率如何从成功/失败 outcome divergence 中计算，是否只依赖 phase 标签？
- 在 LIBERO-Spatial 和 LIBERO-Goal 上，PCM 是否仍能保持最终成功率并减少实际 wall-clock？
- 当任务关键因素发生在 approach 或 active perception 阶段时，PCM 会不会低估早期 chunk 的梯度价值？

#### 📌 上传 PDF 后优先看

- 时间开销 profiling 与 Fig. 1 类型证据
- Probabilistic Chunk Masking 算法与 phase labeling 细节
- LIBERO 三套 benchmark 的效率、成功率和消融表

### [5]. DexJoCo: A Benchmark and Toolkit for Task-Oriented Dexterous Manipulation on MuJoCo [[VIP]] [[HTML]](https://arxiv.org/html/2605.16257) [[PDF]](https://arxiv.org/pdf/2605.16257) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.16257`
* **Authors**: Hanwen Wang, Weizhi Zhao, Xiangyu Wang, Siyuan Huang, He Lin, Boyuan Zheng, Rongtao Xu, Gang Wang, Yao Mu, He Wang, Lue Fan, Hongsheng Li, Zhaoxiang Zhang, Tieniu Tan
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看：DexJoCo 是面向任务型灵巧操作的 MuJoCo benchmark/toolkit，并有 He Wang 参与，适合作为后续 dexterous VLA/RL 评测入口。
* **关键词**: `Dexterous manipulation` `MuJoCo benchmark` `DexJoCo` `Teleoperation` `He Wang`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

现有 VLA 和机器人数据系统大多围绕 manipulator-gripper 平台，虽然能覆盖大量 pick-and-place 和基础操作，但难以评测灵巧手在工具使用、接触丰富操作、双手协作和长程任务中的独特能力。DexJoCo 的动机是建立一个标准化 benchmark，让研究者不只比较“能不能抓起物体”，而是系统评估 dexterous hands 相比平行夹爪更擅长的功能性任务。对 Sim2Real、RL 和 VLA 都很重要，因为没有统一环境、任务、数据和评测管线，就很难判断灵巧操作模型到底在动作空间、触觉/本体感知、接触建模还是视觉策略上失败。He Wang 参与也使其在灵巧操作社区中值得优先跟踪。

#### ⚙️ 核心方法

DexJoCo 包含 benchmark 与 toolkit 两部分。摘要明确说它提供 11 个 functionally grounded tasks，覆盖 tool-use、bimanual coordination、long-horizon execution 和 reasoning，并收集 1.1K trajectories，同时支持 domain randomization 来评估鲁棒性。方法摘录展示了低成本数据采集系统，包含 hand motion retargeting 和 wrist motion tracking。由于人手和机器人手结构不同，作者采用 GeoRT，一种无需 paired human-robot annotations 的 lightweight self-supervised retargeting 方法，把 human fingertip keypoints 映射为 robot joint positions，并通过保持指尖运动方向、扩大工作空间覆盖、维持灵敏度、保持 pinch behaviors 和避免 self-collisions 等目标进行优化。腕部跟踪则记录初始 wrist pose 作为参考，后续动作用 relative pose changes 表示，再由机器人执行 delta actions。

#### 📊 实验与结果

摘录确认 DexJoCo 的实验和工具链围绕 11 个任务、1.1K 条轨迹、domain randomization 与 MuJoCo 环境展开，但没有给出完整 benchmark 表格和模型成功率数字。结论中作者总结了现有方法的几个问题：当前 VLA 多在 gripper-based data 上预训练，action space 与 dexterous hands 不匹配，action heads 难以捕捉高维关节耦合；vision-only policies 在 contact-rich manipulation 中不足，即使加入 proprioception 也可能缺失 contact forces 等关键线索。由此可确认，该论文不只是发布环境，也试图用实验暴露 dexterous manipulation 中模型和传感的系统性短板。

#### ⚠️ 风险 / 保留意见

- 1.1K trajectories 对训练通用 dexterous foundation policy 可能仍偏小，更适合作为基准与初步数据源。
- MuJoCo 中的接触和真实灵巧手硬件差距需要通过 Sim2Real 实验进一步验证。
- 如果任务资产和 teleoperation pipeline 复现门槛较高，社区采用速度可能受影响。

#### 💭 结论与启发

DexJoCo 对后续研究的价值在于，它把灵巧操作从零散 demo 推向可比较 benchmark。做 VLA/RL 选题时，可以用它检测 gripper-centric foundation model 在高维手部 action space 下的失败模式，再研究 embodiment-aware action representation、hand-centric pretraining 和 tactile/proprioceptive fusion。复现上不应只跑一个视觉策略 baseline，而要重点观察不同 action head、retargeting 表征、domain randomization 和接触感知输入对任务成功的影响。

#### 🔎 读 PDF 先核查

- 11 个 functionally grounded tasks 分别如何覆盖 tool-use、bimanual coordination、long-horizon execution 和 reasoning？
- GeoRT retargeting 误差会如何影响下游 policy learning，论文是否区分数据采集误差与策略失败？
- domain randomization 是否真实提升跨资产、跨初始状态或跨硬件的鲁棒性？

#### 📌 上传 PDF 后优先看

- 任务定义、数据规模与 benchmark protocol 章节
- teleoperation、GeoRT retargeting 与 wrist tracking 章节
- VLA/RL baseline、domain randomization 和失败案例分析章节

### [6]. HoMMI: Learning Whole-Body Mobile Manipulation from Human Demonstrations [[VIP]] [[HTML]](https://arxiv.org/html/2603.03243) [[PDF]](https://arxiv.org/pdf/2603.03243) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.03243`
* **Authors**: Xiaomeng Xu, Jisang Park, Han Zhang, Eric Cousineau, Aditya Bhat, Jose Barreiros, Dian Wang, Jeannette Bohg, Shuran Song
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看：HoMMI 有 Jeannette Bohg 和 Shuran Song 参与，解决 robot-free human demos 到 whole-body mobile manipulation 的跨 embodiment 学习问题。
* **关键词**: `Whole-body mobile manipulation` `Robot-free demonstration` `UMI` `Cross-embodiment policy` `Jeannette Bohg`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

#### 📖 背景与动机

移动操作要求机器人同时协调双臂、底盘、躯干、头部和多源视觉输入，这比桌面单臂操作更接近真实家庭或服务场景。传统 teleoperation 对移动操作机器人来说昂贵、慢且不直观，而 UMI 这类手持设备能低成本收集末端执行器轨迹和 wrist camera 观测，但 wrist-centric 数据缺少全局场景信息，不足以支撑长程导航和主动感知。HoMMI 的动机是，在保持 robot-free human demonstration 可扩展性的同时，引入 egocentric sensing 捕获全局上下文，并显式处理由此带来的人到机器人 observation/action embodiment gap。对 VLA 和 imitation learning 来说，这正是从桌面操作走向真实移动操作的关键断点。

#### ⚙️ 核心方法

HoMMI 是一个数据采集与 policy learning 框架。它在 bimanual UMI 基础上加入 egocentric sensing，用头戴或第一视角观测捕获移动操作所需的全局上下文；同时，为避免直接加入 ego RGB 和 head action 造成更大的跨 embodiment gap，作者设计了 cross-embodiment hand-eye policy。摘要和结论明确提到两个核心设计：embodiment-agnostic visual representation，以及 relaxed look-at point head action representation。前者目标是减少人类示教视觉与机器人部署视觉之间的外观和视角差异，后者则把头部动作从直接 6-DoF 预测改成更适合机器人执行的注视点表示。最后，whole-body controller 负责在物理约束下协调机器人 base、torso、head 和 arms，实现末端执行器跟踪与主动感知。摘录没有给出网络结构细节，因此不能扩写具体 loss 或控制器公式。

#### 📊 实验与结果

实验问题很明确：能否从 robot-free human demonstrations 学到 long-horizon bimanual mobile manipulation，并转移到真实 mobile manipulator。评估覆盖四类能力：cross-embodiment transfer、bimanual/whole-body coordination、long-horizon navigation 和 active perception。对比包括 Wrist-Only(UMI)，即只用 wrist RGB 和 gripper trajectories；RGB-Only(UMI+Ego)，即直接加入 head RGB 并预测 gripper 和 6-DoF head actions；以及其他消融。摘录说明实验是 extensive real world experiments，但没有给出任务数量、成功率或具体提升幅度，因此只能确认其真实机器人验证范围较关键，不能引用定量结论。

#### ⚠️ 风险 / 保留意见

- robot-free human demos 到真实移动机器人仍有动作尺度、碰撞约束和动力学差异，控制器承担了较多转移压力。
- relaxed look-at point 表示是否适用于所有主动感知任务，需要看失败案例。
- 摘录未给出定量结果，真实实验规模和统计显著性需全文核查。

#### 💭 结论与启发

HoMMI 对系统设计的启发是，移动操作不能简单把桌面 UMI 扩成双手版本；全局 egocentric context、头部主动感知和 whole-body control 必须一起设计。后续复现可先从一两个长程双手任务做起，比较 wrist-only、naive ego RGB 和 embodiment-agnostic representation 的差异。对于 VLA 研究，这篇提示 action space 设计和控制接口可能比模型大小更关键，尤其是在需要移动底盘与头部协同的任务中。

#### 🔎 读 PDF 先核查

- embodiment-agnostic visual representation 具体如何构建，是否需要人类和机器人配对数据？
- relaxed look-at point head action representation 相比直接 6-DoF head action 解决了哪些失败模式？
- whole-body controller 与 learned policy 的接口如何分工，哪些能力来自学习，哪些来自控制器约束？

#### 📌 上传 PDF 后优先看

- HoMMI 数据采集接口与 egocentric sensing 章节
- cross-embodiment hand-eye policy 设计章节
- 真实移动操作任务、baseline 消融和失败案例章节

## Watchlist

### [W1]. Health-Conditioned Vision-Language-Action Models for Malfunction-Aware Robot Control [[HTML]](https://arxiv.org/html/2605.16056) [[PDF]](https://arxiv.org/pdf/2605.16056)
* **Paper ID**: `2605.16056`
* **Authors**: Hüseyin Arslan, Özgür Erkent
* **Author Priority**: Standard
* **为什么还值得留意**: Health-conditioned VLA 进入 watchlist，因为它把 robot physical degradation 显式输入到 VLA policy，关注真实部署中关节退化、执行器能力下降和弱夹爪等问题。摘录显示它在 VLA-Adapter Pro 上加入 health vector projector，并在 LIBERO Spatial 的单关节退化设置中评估，方向很实用。但它没有进入最终精选，主要因为当前范围限制在单关节退化和单一 LIBERO suite，作者也承认任务覆盖较窄。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. CLARE: Continual Learning for Vision-Language-Action Models via Autonomous Adapter Routing and Expansion [[HTML]](https://arxiv.org/html/2601.09512) [[PDF]](https://arxiv.org/pdf/2601.09512)
* **Paper ID**: `2601.09512`
* **Authors**: Ralf Römer, Yi Zhang, Yuming Li, Angela P. Schoellig
* **Author Priority**: Standard
* **为什么还值得留意**: CLARE 进入 watchlist，因为 continual learning 对长期运行的 VLA 很关键，它用 autonomous adapter routing and expansion 试图避免遗忘、减少旧数据依赖，并支持任务序列扩展。摘录显示它在 LIBERO continual learning 设置和 FR3 真实任务上评估，还分析了哪些层适合扩展。但它没有进入最终精选，是因为今天主线更偏 VLA+world model/RL/Sim2Real 系统信号，而 CLARE 更像持续学习架构专项，需等完整实验细节再决定是否深挖。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

### [W3]. NavRL++: A System-Level Framework for Improving Sim-to-Real Transfer in Reinforcement Learning-Based Robot Navigation [[HTML]](https://arxiv.org/html/2605.15559) [[PDF]](https://arxiv.org/pdf/2605.15559)
* **Paper ID**: `2605.15559`
* **Authors**: Zhefan Xu, Hanyu Jin, Kenji Shimada
* **Author Priority**: Standard
* **为什么还值得留意**: NavRL++ 进入 watchlist，因为它正面研究 RL navigation 的 sim-to-real transfer，并把 sensor noise、perception failures、system latency 和 control response 等部署因素纳入系统分析。摘录显示它包含同模拟器评估、跨模拟器迁移，以及 aerial 和 legged platforms 的真实实验，和今天 Sim2Real 方向高度相关。但它没有进入最终精选，主要因为它不是 VLA/World Action Model 论文，且当前摘录更像系统级导航 RL pipeline，和精选里的 VLA 主线距离稍远。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. STABLE: Simulation-Ready Tabletop Layout Generation via a Semantics-Physics Dual System [[VIP]] [[HTML]](https://arxiv.org/html/2605.16137) [[PDF]](https://arxiv.org/pdf/2605.16137)
* **Paper ID**: `2605.16137`
* **Authors**: Zhen Luo, Yixuan Yang, Xudong Xu, Jinkun Hao, Zhaoyang Lyu, Feng Zheng, Jiangmiao Pang, Yanwei Fu
* **Author Priority**: Core VIP
* **为什么还值得留意**: STABLE 进入 watchlist，因为它由 Jiangmiao Pang 参与，并提出 semantics-physics dual system，把任务指令到 tabletop layout generation 拆成 LLM Semantic Reasoner 与 geometry-aware Physics Corrector。它对 embodied AI 的合成数据和 simulation-ready scene generation 很有价值，尤其适合作为 Sim2Real 数据环境生成模块观察。但它没有进入最终精选，是因为它更偏场景生成与数据基础设施，而非直接 VLA policy、RL 或 world/action model；需要后续看它生成的场景是否真正提升机器人策略训练。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
