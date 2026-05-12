# RoboPulse | 2026-05-12

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 174 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线很集中：VLA 研究正在从“更大的端到端策略”转向恢复能力、结构化中间变量、记忆、世界模型和可迁移适配机制。最终精选覆盖了失败轨迹再利用、action-free video 预训练、参数空间能力迁移、长时记忆基准、World Action Model 范式融合，以及层级视觉 grounding 六条互补路线。它们入选不是因为单点指标，而是因为都在回答 VLA 部署里的关键瓶颈：偏移后如何恢复、少标注数据如何用、长任务如何保持状态、世界模型如何真正落到动作。VIP 作者里，Donglin Wang 连续出现在 CapVector 与 RoboMemArena，值得跟踪其团队在 VLA 适配与基准化上的系统布局；Jiangmiao Pang 参与的 HiVLA 代表层级 VLA 路线；Sergey Levine 的 Q-chunking 虽列入 watchlist，也应作为 RL+action chunking 的重要背景阅读。

## 今日信号

- VLA 的核心竞争点正在从静态 imitation success 转向对失败、延迟、分布偏移和长期记忆的可恢复控制。
- World model 与 latent action 不再只是视频预测辅助模块，而被重新包装为动作生成、迁移和策略结构化的中间接口。
- 参数空间迁移、noise-space adaptation、action chunking 等方法显示：VLA 适配正在寻找比全量微调更便宜、更可复用的学习通道。

## Editor's Picks

### [1]. RePO-VLA: Recovery-Driven Policy Optimization for Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2605.09410) [[PDF]](https://arxiv.org/pdf/2605.09410) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.09410`
* **Authors**: Weijia Liufu, Xiaoyu Guo, Ruiyi Chen, Jingzhi Liu, Kaidong Zhang, Xiwen Liang, Jianqi Lin, Dawei Sun, Yuze Wang, Rongtao Xu, Bingqian Lin, Bowen Yang, Tongtong Cao, Bowen Peng, Dongyu Zhang, Guangrun Wang, Min Wang, Liang Lin, Xiaodan Liang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为它把失败轨迹从“丢弃样本”改造成 VLA 长时操作恢复能力的训练资源。
* **问题与切口**: RePO-VLA 针对长时、接触丰富、尤其是双臂操作里的执行漂移问题：成功示范只告诉模型如何顺利完成任务，却很少教模型在抓取滑移、接触异常或节奏错位后如何回到可成功状态。论文的核心切口是把轨迹分成 success、recovery 和 failure 三类角色，而不是把失败 rollout 视为噪声。新意在于它强调“恢复段”的独立监督价值，并试图让 VLA 从不完美交互数据中学会自主纠错。
* **核心方法与证据**: 方法包含 Recovery-Aware Initialization 和 Progress-Aware Semantic Value Function。RAI 会切出恢复片段并重置历史，使纠正动作依赖当前 adverse state，而不是被前序失败上下文污染；PAS-VF 则用进度感知的语义价值信号对齐时空轨迹。实验摘录显示其在 FRBench-Sim 的 Dynamic Grasp Failure 上进行扰动恢复评估，协议包括 RoboTwin Clean/Random、每任务 50 次 rollout，以及在抓取起始阶段强制打开夹爪 30 帧来制造失败。证据边界主要来自摘要和 HTML 中的仿真与恢复扰动描述，真实泛化细节需等 PDF 核查。
* **正文要点**:
  - 论文明确把成功、恢复、失败轨迹分配给不同训练角色，强调失败终端区域也能提供恢复价值信号。
  - Dynamic Grasp Failure 扰动不改变语言任务，而是破坏物体控制，测试策略能否重新建立有效抓取。
  - 摘录中给出的 Phase I 与 full RePO-VLA 对比显示，恢复训练被设计为不牺牲基础任务能力，同时改善注入失败后的恢复表现。
* **为什么值得跟**:
  - 它把 VLA 的评价重心从 nominal success 推向执行中断后的闭环韧性。
  - 它为人类纠错、失败数据回收和在线恢复训练提供了清晰的问题分解。
  - 接触丰富双臂任务是 VLA 落地的高风险区，该论文正面处理了这类场景。
* **风险 / 保留意见**:
  - 恢复片段切分和历史重置的标注或规则依赖程度需要核查，否则复现成本可能偏高。
  - HTML 摘录主要展示特定扰动协议，尚不足以判断其对多样真实失败模式的覆盖。
* **建议先看**: 先读轨迹角色定义和 RAI/PAS-VF 的训练流程，再看 Dynamic Grasp Failure 的扰动设置是否足以代表真实接触失败。重点判断它是在学通用恢复，还是主要适配了人为注入的失败模式。
* **关键词**: `VLA recovery` `failure trajectory` `contact-rich manipulation` `semantic value function` `bimanual manipulation`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - RAI 的恢复片段边界如何确定，是否需要人工标注或任务特定启发式？
  - PAS-VF 的进度语义信号如何与动作监督耦合，是否会在失败后误判任务阶段？
  - full RePO-VLA 相比只做恢复初始化的增益，主要来自价值条件化还是数据重加权？
* **上传 PDF 后优先看**:
  - 方法章节中的 success/recovery/failure 轨迹定义与切片规则
  - FRBench-Sim Dynamic Grasp Failure 的扰动协议和 baseline 设置
  - 恢复数据可视化、消融实验和真实机器人评估章节

### [2]. ALAM: Algebraically Consistent Latent Transitions for Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2605.10819) [[PDF]](https://arxiv.org/pdf/2605.10819) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.10819`
* **Authors**: Zuojin Tang, Haoyun Liu, Xinyuan Chang, Changjie Wu, Dongjie Huo, Yandan Yang, Bin Liu, Zhejia Cai, Feng Xiong, Mu Xu, jiachen Luo, De Ma, Zhiheng Ma, Gang Pan
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为它把 action-free video 里的变化关系约束成可生成、可组合的 VLA latent action。
* **问题与切口**: ALAM 面向 VLA 数据稀缺问题：有动作标签的机器人数据贵，但无动作视频大量存在。传统 latent action model 可以从视频重建中学到变化表征，却未必适合被策略生成或与机器人动作复用。ALAM 的关键新意是把场景转移表示成近似“差分”：连续变化应可组合，时间反转应改变符号。这样 action-free video 不只是提供未来帧预测信号，而是提供带代数结构的 latent transition prior，服务下游 VLA policy learning。
* **核心方法与证据**: 框架分两阶段：预训练时，relational encoder 接收两个观察端点，在未来帧重建之外加入 composition consistency 与 reversal consistency，使 latent transition 近似可加、可反向；迁移时冻结 encoder，并在现成 VLA backbone 上用 shared flow-matching objective 联合建模 latent transition 与真实机器人动作。实验覆盖 MetaWorld MT50、LIBERO 四个 suite，以及 Piper 6-DoF 真实任务。HTML 摘录给出任务集合、30k 训练步等设置，但部分成功率细节和误差降幅在摘录中缺失或格式不完整，应保守看待。
* **正文要点**:
  - 论文把转移表征定义为两个观察之间的 relational latent，而不是单帧状态编码。
  - composition consistency 要求相邻两段变化合成后接近跨越更长时间的变化。
  - transfer 阶段强调 latent 与 robot action 共同生成，比单独解码 latent 更贴近 VLA action head。
* **为什么值得跟**:
  - 它提供了一条把公开视频或 action-free robot video 接入 VLA 训练的结构化路线。
  - 代数约束让 latent action 更可能被策略复用，而不只是服务像素重建。
  - 它连接了 world model、latent action 和 flow-matching VLA，是今天 World Action Model 方向的重要补充。
* **风险 / 保留意见**:
  - 代数一致性是否在复杂接触、遮挡和非刚体变化中仍成立，需要看更细实验。
  - HTML 摘录没有完整呈现关键定量表，实际增益大小和统计稳定性需核查 PDF。
* **建议先看**: 先看 structured latent transitions 的定义和两个正则项，再追 transfer 阶段如何把 latent transition 与真实动作放进同一个 flow-matching 目标。读实验时重点比较“重建好”与“策略可用”是否被清楚区分。
* **关键词**: `latent action model` `action-free video` `algebraic consistency` `flow matching` `world model`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - composition 与 reversal 两个约束的权重如何设定，对下游策略性能是否敏感？
  - 冻结 relational encoder 后，latent transition 与机器人动作之间的对应关系如何避免 embodiment mismatch？
  - 在 LIBERO Long 或真实任务中，ALAM 的收益是否主要来自长时结构，还是来自额外视频预训练数据？
* **上传 PDF 后优先看**:
  - Structured Latent Transitions 和代数正则定义章节
  - transfer 到 VLA backbone 的 shared flow-matching 训练设计
  - MetaWorld、LIBERO Long 与真实 Piper 任务的消融和失败案例

### [3]. CapVector: Learning Transferable Capability Vectors in Parametric Space for Vision-Language-Action Models [[VIP]] [[HTML]](https://arxiv.org/html/2605.10903) [[PDF]](https://arxiv.org/pdf/2605.10903) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.10903`
* **Authors**: Wenxuan Song, Han Zhao, Fuhao Li, Ziyang Zhou, Xi Wang, Jing Lyu, Pengxiang Ding, Yan Wang, Donglin Wang, Haoang Li
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，尤其要跟踪 Donglin Wang 团队如何把辅助目标微调的收益压缩成可迁移参数向量。
* **问题与切口**: CapVector 处理的是 VLA 下游适配的效率问题：标准 SFT 简单但常常不能充分释放预训练 VLA 的能力，带辅助目标的微调可能更强却引入额外计算负担。论文提出把辅助-objective SFT 带来的能力增益从具体任务中解耦出来，在参数空间中提取 capability vector，再与预训练模型合并形成 capability-enhanced meta model。它的切口不是再设计一个动作头，而是把“空间感知、多模态推理等能力提升”视为可迁移的参数方向。
* **核心方法与证据**: 方法脉络借鉴 model merging、低秩更新和 VLA checkpoint 插值相关工作，但强调通过参数算术抽取能力向量，而非简单 ensemble。实验问题设计较完整：包括域内能力迁移、任务无关性与域外迁移、多 VLA 架构适用性、能力向量质量机制，以及 sim-to-real、跨机器人 embodiment 和真实场景可用性。HTML 摘录没有给出完整数值结果，但研究问题覆盖了有效性、效率、机制和现实部署，说明论文正文应有较系统的消融与跨设置验证。
* **正文要点**:
  - CapVector 试图保留辅助目标 SFT 的性能收益，同时维持标准 SFT 的简单和计算效率。
  - 论文把 capability vector 定义在参数空间，通过模型合并向 pretrained VLA 注入能力。
  - 实验 RQ 明确包括 sim-to-real 和跨 embodiment，这使其不只是离线 checkpoint 合并技巧。
* **为什么值得跟**:
  - 如果成立，它能显著降低 VLA 在新任务上反复设计辅助损失的成本。
  - 参数空间能力迁移为多技能、多机器人 VLA 维护提供了可组合思路。
  - Donglin Wang 出现在作者列表中，这条线值得作为核心作者网络里的持续跟踪对象。
* **风险 / 保留意见**:
  - HTML 摘录缺少关键定量表，当前只能确认实验设计，不能确认增益规模。
  - 能力向量是否真“任务无关”，可能高度依赖源任务、目标任务和基础模型相似度。
* **建议先看**: 先读 capability vector 的构造公式和合并流程，再看 RQ2/RQ5 是否真正证明跨任务、跨域、跨 embodiment。不要只看平均成功率，要检查负迁移和失败任务。
* **关键词**: `capability vector` `model merging` `VLA finetuning` `sim-to-real` `parameter space transfer`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 能力向量从辅助-objective SFT 中如何分离，是否需要成对 checkpoint 或特定训练路径？
  - 不同 VLA 架构之间的 vector transfer 是同构参数合并，还是需要映射机制？
  - sim-to-real 实验中，向量来自仿真后直接合并到真实策略的条件和限制是什么？
* **上传 PDF 后优先看**:
  - capability vector 定义、参数算术和模型合并算法
  - RQ2 域外迁移与任务无关性实验
  - RQ5 sim-to-real、跨 embodiment 和真实场景评估

### [4]. RoboMemArena: A Comprehensive and Challenging Robotic Memory Benchmark [[VIP]] [[HTML]](https://arxiv.org/html/2605.10921) [[PDF]](https://arxiv.org/pdf/2605.10921) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.10921`
* **Authors**: Huashuo Lei, Wenxuan Song, Huarui Zhang, Jieyuan Pei, Jiayi Chen, Haodong Yan, Han Zhao, Pengxiang Ding, Zhipeng Zhang, Lida Huang, Donglin Wang, Yan Wang, Haoang Li
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，因为 RoboMemArena 把 VLA 长时记忆从附加功能提升成可系统评估的核心能力。
* **问题与切口**: RoboMemArena 针对机器人记忆 benchmark 的缺口：现有评测往往任务覆盖有限、结构不够复杂、缺少形成记忆所需的多模态标注，并且多停留在仿真。该工作构建了 26 个任务，平均轨迹长度超过 1,000 步，且 68.9% 子任务依赖记忆，使“过去观察和动作”成为完成任务的必要条件。它还提供 keyframe-centered multimodal supervision 与 paired real-world memory tasks，把基准从普通长时任务推进到部分可观测条件下的记忆能力评估。
* **核心方法与证据**: 生成管线利用 VLM 设计和组合子任务，再通过 atomic functions 生成完整轨迹，并提供 subtask instructions 与 native keyframe annotations 等记忆相关标注。论文还提出 PrediMem，一个 dual-system VLA，其中高层 VLM planner 管理 memory bank，低层策略通过 predictive coding objective 让隐状态对物理状态转移更敏感，且据摘要称不增加推理时成本。HTML 摘录主要给出 benchmark 构成、标注类型和 PrediMem 总体结构，具体任务分布、真实评测协议和 baseline 表现需后续核查。
* **正文要点**:
  - RoboMemArena 明确报告 26 个任务、平均轨迹超过 1,000 步，并标注 68.9% 子任务为 memory-dependent。
  - benchmark 不是只给轨迹，还包含 subtask instruction 与 native keyframe annotation。
  - PrediMem 采用高层 VLM planner 管理 memory bank，并用预测编码目标强化物理状态转移敏感性。
* **为什么值得跟**:
  - 长时 VLA 的瓶颈常常不是单步动作，而是记住先前观察、对象位置和任务进度。
  - 该 benchmark 可用于区分真正记忆机制与仅靠当前帧反应的策略。
  - Donglin Wang 团队同时出现在 CapVector 与 RoboMemArena，显示其关注 VLA 适配与评测基础设施。
* **风险 / 保留意见**:
  - VLM 自动生成子任务可能引入模板偏差，任务多样性需要看正文验证。
  - 真实世界 paired memory tasks 的规模和代表性在摘录中不足，不能过度推断。
* **建议先看**: 先看任务生成管线和 memory-dependent 子任务判定标准，再看 PrediMem 是否只是 benchmark 附带 baseline，还是能代表一条强方法路线。评估时尤其要关注部分可观测性是否真实存在。
* **关键词**: `robotic memory` `long-horizon manipulation` `benchmark` `VLA planner` `predictive coding`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
* **读 PDF 先核查**:
  - memory-dependent 子任务的判定依据是什么，是否由规则、VLM 或人工审核给出？
  - native keyframe annotation 如何用于训练和评测，是否会泄漏任务进度信息？
  - PrediMem 的 memory bank 更新、检索和遗忘机制如何设计，推理成本为何不增加？
* **上传 PDF 后优先看**:
  - benchmark 任务生成与 memory-dependence 标注规则
  - keyframe-centered multimodal supervision 的数据格式和使用方式
  - PrediMem 架构、baseline 对比和真实世界 paired tasks

### [5]. HarmoWAM: Harmonizing Generalizable and Precise Manipulation via Adaptive World Action Models [[HTML]](https://arxiv.org/html/2605.10942) [[PDF]](https://arxiv.org/pdf/2605.10942) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.10942`
* **Authors**: Qiuxuan Feng, Jiale Yu, Jiaming Liu, Yueru Jia, Zhuangzhe Wu, Hao Chen, Zezhong Qian, Shuo Gu, Peng Jia, Siwei Ma, Shanghang Zhang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为 HarmoWAM 正面处理 World Action Model 中泛化 transit 与精细操作之间的范式冲突。
* **问题与切口**: HarmoWAM 关注 World Action Model 的核心矛盾：Imagine-then-Execute 借助视频预测和逆动力学，可能更擅长可泛化的运动 transit，但互动精度不足；Joint Modeling 直接建模动作与视频表示，动作更细致连贯，却可能受限于表征泛化。论文先把这种 trade-off 作为系统实验观察，再提出 adaptive WAM，用共享世界模型连接时空推理和动作生成，并通过两个互补 action experts 与过程自适应 gating 来协调预测式和反应式控制。
* **核心方法与证据**: 整体架构以 Wan2.2-TI2V-5B 为世界模型实例，并在大规模机器人数据上继续预训练以获得物理建模与泛化能力；摘录称其预测 13 帧未来视频。动作侧设计两个 Transformer-based experts，一个偏向借助未来视觉先验进行 transit，另一个偏向精细、时序一致的操作控制，再由 Process-Adaptive Gating Mechanism 动态融合。实验为真实双臂 Franka Research 3，三路 RealSense 视角，含四个单臂与两个双臂任务，每任务 100 条 SpaceMouse 示范，并比较 SOTA VLA、Imagine-then-Execute 和 Joint Modeling 类 baseline。
* **正文要点**:
  - 论文把 WAM 分成 Imagine-then-Execute 与 Joint Modeling 两类，并明确提出二者在泛化和精度上存在 trade-off。
  - HarmoWAM 使用共享 world model 加两个互补 action experts，而不是只选择一种 WAM 范式。
  - 实验覆盖真实双臂 Franka 设置，任务包括单臂操作和双臂协作操作。
* **为什么值得跟**:
  - 它直接对应今天关注的 World Action Model 方向，并把范式比较转化为架构设计。
  - 如果 gating 能稳定工作，WAM 可能同时获得长程时空先验和接触级动作精度。
  - 真实双臂平台和 OOD 场景评估使其比纯仿真 WAM 更接近部署问题。
* **风险 / 保留意见**:
  - 世界模型规模和预训练数据量较大，复现门槛可能明显高于普通 VLA 方法。
  - adaptive gating 的可解释性与失败模式需要重点核查，否则可能只是经验性融合。
* **建议先看**: 先读论文如何定义并实验证明两类 WAM 的 trade-off，再看 HarmoWAM 的 gating 是否真的按任务阶段切换专家。实验部分优先查 ID/OOD 分别对应哪些失败和成功案例。
* **关键词**: `World Action Model` `future video prediction` `adaptive gating` `dual-arm manipulation` `world model`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - Process-Adaptive Gating Mechanism 的输入信号是什么，是否显式识别任务阶段或接触状态？
  - 两个 action experts 的训练目标是否不同，还是只靠结构差异形成互补？
  - OOD 评估中，HarmoWAM 的优势来自世界模型泛化、专家融合，还是机器人数据预训练规模？
* **上传 PDF 后优先看**:
  - WAM 两类范式 trade-off 的系统实验与分析章节
  - HarmoWAM 架构、两个 action experts 和 gating 机制
  - 真实 Franka ID/OOD 任务、消融实验和失败案例

### [6]. HiVLA: A Visual-Grounded-Centric Hierarchical Embodied Manipulation System [[VIP]] [[HTML]](https://arxiv.org/html/2604.14125) [[PDF]](https://arxiv.org/pdf/2604.14125) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.14125`
* **Authors**: Tianshuo Yang, Guanyu Chen, Yutian Chen, Zhixuan Liang, Yitian Liu, Zanxin Chen, Chunpu Xu, Haotian Liang, Jiangmiao Pang, Yao Mu, Ping Luo
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，因为 HiVLA 代表 Jiangmiao Pang 参与的层级 VLA 路线，试图保留 VLM 推理而把控制交给专门 action expert。
* **问题与切口**: HiVLA 针对端到端 VLA 的一个常见副作用：在窄控制数据上微调时，模型可能损伤基础 VLM 的语义推理与视觉理解能力。它提出 visual-grounded-centric hierarchical framework，把高层语义规划与低层运动控制显式解耦。高层 VLM planner 负责任务分解和视觉 grounding，输出 subtask instruction 与目标 bounding box；低层 DiT-based Action Expert 接收这些结构化计划并执行控制。新意在于把 grounding 作为高低层之间的中心接口，而不是让动作头直接吸收所有语义推理压力。
* **核心方法与证据**: 方法分为 High-Level VLM Planner Agent 和 DiT-based Action Expert。planner 在每个决策步接收总目标、夹爪状态、前一子任务以及动作前后的视觉历史，决定下一步做什么和在哪里做；action expert 则重点研究如何有效条件化高层计划。实验在 RoboTwin2.0 仿真和真实机器人操作中验证，并显式提出三个问题：是否优于耦合式 SOTA VLA、控制策略对高层 reasoning error 是否鲁棒、不同视觉表示和 guidance injection 如何影响性能。摘录给出 domain randomization 设置，但完整指标和真实平台细节需查 PDF。
* **正文要点**:
  - HiVLA 显式解耦 VLM semantic planning 和 low-level motor control，以避免窄控制微调侵蚀 VLM 推理。
  - 高层输出不仅是子任务语言，还包括 precise target bounding box，形成视觉 grounding 中间接口。
  - 实验问题包含 planner 错误鲁棒性，说明作者意识到层级系统的误差传播风险。
* **为什么值得跟**:
  - 层级 VLA 是端到端路线的重要替代方案，尤其适合长时、组合式和多目标操作。
  - 视觉 grounding 接口让研究者能更清楚地区分感知失败、规划失败和控制失败。
  - Jiangmiao Pang 在核心作者名单中，该论文值得纳入 VIP 跟踪链路。
* **风险 / 保留意见**:
  - 层级系统依赖 planner 输出质量，bounding box 错误可能直接影响低层动作。
  - HTML 摘录不足以判断真实机器人任务规模和相对 SOTA 的实际优势。
* **建议先看**: 先看高层 planner 的输入输出 schema，再看低层 DiT action expert 如何注入 bounding box 与 subtask instruction。读实验时优先关注 planner error 鲁棒性，而不是只看总成功率。
* **关键词**: `hierarchical VLA` `visual grounding` `VLM planner` `DiT action expert` `RoboTwin2.0`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)
* **读 PDF 先核查**:
  - planner 生成的 bounding box 是零样本 VLM 输出、微调 grounding 模块，还是结合规则后处理？
  - Action Expert 如何利用 subtask instruction 与目标框，注入方式对性能差异有多大？
  - 当高层 planner 给出错误子任务或错误目标框时，低层策略是否有纠错能力？
* **上传 PDF 后优先看**:
  - High-Level VLM Planner Agent 的 structured inference 流程
  - DiT-based Action Expert 的条件化和 guidance injection 设计
  - RoboTwin2.0 domain randomization、planner error 鲁棒性和真实机器人实验

## Watchlist

### [W1]. Understanding Asynchronous Inference Methods for Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2605.08168) [[PDF]](https://arxiv.org/pdf/2605.08168)
* **Paper ID**: `2605.08168`
* **Authors**: Ayoub Agouzoul
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇进入 watchlist 是因为它系统比较 VLA 异步推理中的 IT-RTC、TT-RTC、VLASH 和 A2C2，直接触及 action chunking 与推理延迟导致 observation staleness 的部署问题。它没有进入最终精选，主要因为更像方法横评与工程诊断，原创核心机制相对不如 RePO-VLA、ALAM 或 HarmoWAM 鲜明。仍建议在阅读异步 VLA 和 real-time control 时优先扫实验结论，尤其是不同 delay 下方法排名会跨 benchmark 改变这一点。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. VEGA: Visual Encoder Grounding Alignment for Spatially-Aware Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2605.10485) [[PDF]](https://arxiv.org/pdf/2605.10485)
* **Paper ID**: `2605.10485`
* **Authors**: Hao Wang, Xiaobao Wei, Jingyang He, Chengyu Bai, Chun-Kai Fan, Jiajun Cao, Jintao Chen, Ying Li, Shanyu Rong, Ming Lu, Xiaozhu Ju, Jian Tang, Shanghang Zhang
* **Author Priority**: Standard
* **为什么还值得留意**: VEGA 值得列入 watchlist，因为它把 VLA 空间推理瓶颈定位到 visual encoder 层，并提出直接对齐 DINOv2-FiT3D 特征，避免在 LLM-level visual tokens 上做经验层搜索。它没有进入最终精选，是因为主题更偏视觉 backbone grounding，对今天的 recovery、world/action model、RL adaptation 主线支撑略弱。若后续关注 RoboTwin 2.0、ALOHA 或 3D-aware VLA 表征，它应作为重要补充。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. Unified Noise Steering for Efficient Human-Guided VLA Adaptation [[HTML]](https://arxiv.org/html/2605.10821) [[PDF]](https://arxiv.org/pdf/2605.10821)
* **Paper ID**: `2605.10821`
* **Authors**: Junjie Lu, Xinyao Qin, Yuhua Jiang, Kaixin Wang, Chuheng Zhang, Bin Liang, Jun Yang, Min Xu, Li Zhao
* **Author Priority**: Standard
* **为什么还值得留意**: UniSteer 进入 watchlist 是因为它把 human corrective intervention、online RL 和 flow-matching VLA 的 noise-space finetuning 接到同一个接口里，和 RL+VLA 方向高度相关。它没进入最终精选，主要是摘要与摘录显示方法很有价值，但证据范围集中在四个真实任务和特定 frozen decoder 设定，当前不如 RePO-VLA 或 ALAM 对主线的结构性贡献更强。建议后续重点核查 action-to-noise inversion 的稳定性和人类纠错成本。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. Reinforcement Learning with Action Chunking [[VIP]] [[HTML]](https://arxiv.org/html/2507.07969) [[PDF]](https://arxiv.org/pdf/2507.07969)
* **Paper ID**: `2507.07969`
* **Authors**: Qiyang Li, Zhiyuan Zhou, Sergey Levine
* **Author Priority**: Core VIP
* **为什么还值得留意**: Q-chunking 因 Sergey Levine 参与且直接讨论 RL with action chunking，必须保留在 watchlist；它为 VLA 中常见的 chunked action policy 提供了 offline-to-online RL 背景。它没有进入最终精选，是因为论文核心不是 VLA 本身，而是面向长时稀疏奖励 RL 的通用 action chunking recipe。对于今天主题，它最适合作为 RL adaptation 与 chunked control 的方法背景，而非 VLA/World Model 主论文。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)
