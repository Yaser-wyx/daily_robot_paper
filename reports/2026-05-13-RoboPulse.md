# RoboPulse | 2026-05-13

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 89 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线很清楚：VLA 正在从“直接看图出动作”转向更强的中间结构，包括世界/未来预测、潜在动作、空间姿态、记忆检索、动态校正与关键阶段避险。最终精选保留了六个互补切口：WAM 概念框架、视频想象到动作的接口、动作-位姿双向耦合、测试时 dreaming、安全/动态 wrapper，以及层级经验记忆。VIP 作者中，Cewu Lu 出现在 X-Imitator，值得优先跟踪其在空间感知与模仿学习耦合方向的后续工作；其余核心/扩展 VIP 在本组精选摘录中未出现。整体看，今天最值得关注的是“训练后/测试时增强”与“世界模型式动作生成”正在成为 VLA 落地可靠性的主要增量来源。

## 今日信号

- VLA 的下一步不只是扩大模型，而是在动作生成前后加入可解释的结构化中介，如未来状态、潜在动作、位姿、记忆和任务相关注意力。
- 测试时机制正在变成机器人论文的高频抓手：不改主干参数，通过检索、校正、dreaming 或观测重写来提升部署鲁棒性。
- 长时程与真实部署问题被重新定义为动态、记忆和局部环境适应问题，而不是单次零样本 benchmark 上的平均成功率问题。

## Editor's Picks

### [1]. World Action Models: The Next Frontier in Embodied AI [[PDF]](https://arxiv.org/pdf/2605.12090) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.12090`
* **Authors**: Siyin Wang, Junhao Shi, Zhaoyang Fu, Xinzhe He, Feihong Liu, Chenchen Yang, Yikang Zhou, Zhaoye Fei, Jingjing Gong, Jinlan Fu, Mike Zheng Shou, Xuanjing Huang, Xipeng Qiu, Yu-Gang Jiang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，尤其适合作为今天 World Action Model 方向的概念总纲。
* **问题与切口**: 这篇把分散在 VLA、world model、video prediction 与 action generation 中的路线统一到 World Action Models 概念下。它的核心判断是：传统 VLA 多是反应式 observation-to-action 映射，缺少对“动作介入后世界如何演化”的显式建模；WAM 则应同时建模未来状态与动作，把策略学习从只预测动作推进到联合预测 future states and actions。
* **核心方法与证据**: 当前只有摘要回退信息，因此不能判断其正文是否包含系统性 taxonomy、实验或详尽对比。摘要显示论文主要做三件事：形式化定义 WAM，澄清它与相关概念的边界，并追溯早期发展脉络。证据形态更像综述/立场框架，而非提出单一算法；应重点核查它是否给出可操作的架构分类、训练目标分类和应用场景边界。
* **正文要点**:
  - 摘要明确把 WAM 定义为统一 predictive state modeling 与 action generation 的 embodied foundation model。
  - 论文关注的分布目标不是 actions alone，而是 future states 与 actions 的联合分布。
  - 该文声称现有文献在架构、学习目标和应用场景上较碎片化，需要统一概念框架。
* **为什么值得跟**:
  - 它给 VLA 与 world model 的交叉研究提供了一个可引用的命名和边界。
  - 如果 taxonomy 扎实，可帮助区分 video imagination、inverse dynamics、policy learning 与 model-based control 的关系。
  - 对选题判断有用：后续可以把新论文放进 WAM 框架里比较，而不是只按 benchmark 成绩排序。
* **风险 / 保留意见**:
  - 目前只有摘要，无法确认正文是否有足够技术深度或只是概念重命名。
  - 若缺少实验或标准化评估协议，它对方法选择的直接指导价值会有限。
* **建议先看**: 先读定义与 disambiguation 部分，确认 WAM 与 VLA、world model、world action model 的边界。随后看它如何组织早期工作，判断这个框架是否能服务你的论文筛选体系。
* **关键词**: `World Action Model` `VLA` `world model` `predictive state modeling` `embodied AI`
* **证据来源**: Abstract fallback
* **读 PDF 先核查**:
  - 它是否给出 WAM 的必要条件，还是把所有带预测模块的 VLA 都纳入同一类？
  - 它如何区分“预测未来视频再控机器人”和“联合建模未来状态-动作”的方法差异？
  - 它是否提出评估 WAM 的核心任务维度，如长时程、动态干预、闭环稳定性或 sim2real？
* **上传 PDF 后优先看**:
  - WAM formal definition 与概念边界章节
  - architecture / objective taxonomy 类型章节
  - 应用场景、开放问题或 benchmark 建议章节

### [2]. From Imagined Futures to Executable Actions: Mixture of Latent Actions for Robot Manipulation [[HTML]](https://arxiv.org/html/2605.12167) [[PDF]](https://arxiv.org/pdf/2605.12167) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.12167`
* **Authors**: Yajie Li, Bozhou Zhang, Chun Gu, Zipei Ma, Jiahui Zhang, Jiankang Deng, Xiatian Zhu, Li Zhang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，是今天“imagined future 如何变成可执行动作”问题上最直接的一篇。
* **问题与切口**: MoLA 处理的是视频生成模型在机器人控制中的关键断点：未来画面可能视觉上合理，却未必包含对控制最有用的因果动作信息。它不直接把生成帧喂给策略，也不简单从视频回归动作，而是引入 mixture of latent actions，把 imagined visual trajectories 转成结构化、可执行的动作表征，再由 diffusion action head 输出控制命令。
* **核心方法与证据**: 方法链条较完整：先用视频生成模型合成未来视觉 rollout，随后用多个 modality-aware inverse dynamics models 从视觉转移中推断互补 latent actions，最后用动作头解码成机器人动作。实验摘录覆盖仿真与真实场景，并列出 CALVIN、LIBERO、LIBERO-Plus；其中 CALVIN 使用 ABC-D split，LIBERO-Plus 用于受控扰动鲁棒性。具体数值需等 PDF 核查。
* **正文要点**:
  - MoLA 的核心接口是 MoIDM，用来把预测未来视觉轨迹转换为 latent-action representation。
  - 论文明确批评现有路线存在 visual realism 与 control relevance 的错配。
  - 实验设计覆盖 CALVIN、LIBERO、LIBERO-Plus，并声称包含仿真和真实机器人设置。
* **为什么值得跟**:
  - 它把 world-model/video-generation 路线和可执行控制之间的接口问题具体化。
  - 如果 latent actions 足够稳健，可成为 WAM 类方法中比 raw future frames 更合适的中间层。
  - 对长时程 manipulation 很关键，因为未来预测只有能转译成动作才有部署价值。
* **风险 / 保留意见**:
  - 视频生成模型的未来 rollout 若偏离真实动力学，latent action 也可能继承错误因果线索。
  - 摘录未给出延迟、采样成本和真实机器人规模，部署成本需要重点核查。
* **建议先看**: 先抓住 MoIDM 如何从视觉转移中抽取 latent actions，再看 action head 是否真正减少了 imagined future 到控制的错配。实验部分优先比较 ablation，而不是只看最终成功率。
* **关键词**: `MoLA` `latent action` `inverse dynamics` `video generation` `diffusion policy`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - MoIDM 的不同 modality-aware 分支分别捕捉什么动作因素，混合机制是否可解释？
  - 生成未来视频的质量下降时，latent action 解码是否仍比直接 policy conditioning 稳定？
  - 在 CALVIN ABC-D 与 LIBERO-Plus 扰动设置中，收益主要来自 imagination、inverse dynamics，还是 diffusion action head？
* **上传 PDF 后优先看**:
  - MoIDM / mixture of inverse dynamics models 方法章节
  - simulation benchmark 对比与 ablation 表
  - real-world experiment 与 latency / failure case 分析

### [3]. X-Imitator: Spatial-Aware Imitation Learning via Bidirectional Action-Pose Interaction [[VIP]] [[HTML]](https://arxiv.org/html/2605.12162) [[PDF]](https://arxiv.org/pdf/2605.12162) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.12162`
* **Authors**: Kai Xiong, Hongjie Fang, Lixin Yang, Cewu Lu
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，且有 Cewu Lu 参与，是空间感知和动作生成双向耦合路线的重点卡位。
* **问题与切口**: X-Imitator 针对视觉模仿学习中空间感知与动作执行被割裂的问题。它不把 pose 当作一次性辅助监督，也不让 action 单向依赖视觉特征，而是建立 action branch 与 pose branch 的双路径结构：当前位姿预测受过去动作条件影响，动作预测也受位姿轨迹约束，从而让机器人在操作过程中持续更新“物体在哪里、我该如何动”的闭环关系。
* **核心方法与证据**: 摘录显示框架共享视觉编码器，同时预测未来动作轨迹和目标物体 pose trajectory；pose 以 3D translation 与 6D rotation 组成的 9D 表示建模。实验覆盖 24 个仿真任务、四类 benchmark，包括 Adroit、DexArt、MetaWorld 与 RoboTwin 2.0，并设置 RQ 检验双向交互、替代交互机制和条件轨迹长度。限制也写得明确：依赖刚体 SE(3) pose 与外部 pose label。
* **正文要点**:
  - 框架由 action branch 和 pose branch 两条并行路径组成，并共享视觉编码器。
  - 方法同时预测未来 action trajectory 与 object pose trajectory，而不是只做动作回归。
  - 作者在限制中承认当前假设目标可用刚体 SE(3) pose 表示，难直接处理绳、布等形变物体。
* **为什么值得跟**:
  - 它把空间感知从后处理模块提升为动作生成中的持续交互变量。
  - 对双臂、灵巧手和接触敏感任务有启发，因为这些任务的相对位姿变化决定执行成败。
  - VIP 核心作者 Cewu Lu 参与，使其值得纳入空间机器人学习方向的持续跟踪。
* **风险 / 保留意见**:
  - 训练 pose label 依赖外部估计器，遮挡、运动模糊或光照差会影响可复现性。
  - 如果任务无法稳定定义目标刚体 pose，方法优势可能明显下降。
* **建议先看**: 优先看 bidirectional action-pose interaction 的具体条件方式和 ablation。然后核查 pose label 来源、噪声敏感性，以及不同 benchmark 上是否是同一机制稳定增益。
* **关键词**: `imitation learning` `spatial perception` `pose trajectory` `bidirectional interaction` `Cewu Lu`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 动作分支如何利用过去或预测的 pose trajectory，是否只是特征拼接还是有显式交互算子？
  - 双向 action-pose interaction 相比单向 pose-conditioned policy 的收益在哪些任务最明显？
  - 外部 pose estimator 出错时，X-Imitator 是否有鲁棒性评估或退化分析？
* **上传 PDF 后优先看**:
  - architecture design 中 action branch / pose branch 交互机制
  - ablation：双向交互 vs 单向/无交互替代方案
  - limitations 与 pose label / rigid SE(3) 假设相关章节

### [4]. DreamAvoid: Critical-Phase Test-Time Dreaming to Avoid Failures in VLA Policies [[HTML]](https://arxiv.org/html/2605.11750) [[PDF]](https://arxiv.org/pdf/2605.11750) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.11750`
* **Authors**: Xianzhe Fan, Yuxiang Lu, Shenyuan Gao, Xiaoyang Wu, Ruihua Han, Manling Li, Hengshuang Zhao
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把 VLA 失败规避具体落到测试时关键阶段的 world-model 式预演。
* **问题与切口**: DreamAvoid 关注 fine-grained manipulation 中“短暂关键阶段导致不可逆失败”的问题。它的切口不是全程重规划，而是在测试时识别低容错阶段，再对候选动作进行未来视频/结果预演和失败规避。核心新意在于把 consequence-awareness 限制在 sparse critical phases，让 VLA 保持常规执行效率，同时在插入、对齐、接触建立等高风险片段启动更慢但更审慎的 dreaming 机制。
* **核心方法与证据**: 方法包含 Dream Trigger 与测试时 dreaming。摘录给出 Trigger 细节：冻结 DINOv2-ViT-B/14 编码多相机历史与当前帧，和 proprioception 拼接后经三层 MLP 判断阶段；真实部署中异步 1 Hz 轮询，单次约 50 ms，约占控制周期 3%。实验在 AgileX PiperX，含前视与腕部相机，任务包括 Cup Sleeving、Charger Plugging、Cap Opening、Screw Insertion，并对比 Base VLA 与 GPC-RANK。
* **正文要点**:
  - Dream Trigger 用冻结 DINOv2-ViT-B/14 与三层 MLP 做关键阶段识别。
  - 系统把高计算量 dreaming 限制在 sparse critical phases，而非全程运行。
  - 真实实验任务集中在对齐、接触和细微动作误差敏感的操作。
* **为什么值得跟**:
  - 它把 world model / video generation 的成本问题转化为“何时值得想象”的调度问题。
  - 对真实机器人很实用，因为很多失败不是全局规划错，而是关键接触阶段动作误差放大。
  - 可作为 VLA safety layer 思路，未来可能迁移到 WAM 或传统控制策略上。
* **风险 / 保留意见**:
  - 未来视频生成与多候选评分会引入延迟，作者自己也把加速列为未来方向。
  - 关键阶段识别若漏检或误检，可能导致该想象时不想象，或在不必要阶段拖慢控制。
* **建议先看**: 先看 Dream Trigger 如何定义和学习 critical phase，再看 dreaming/scoring 如何介入动作选择。实验部分重点读 failure case，而不是只看平均提升。
* **关键词**: `DreamAvoid` `test-time dreaming` `critical phase` `failure avoidance` `video generation`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - critical phase 的标签或边界如何获得，autonomous boundary learning 具体减少了多少人工依赖？
  - DreamAvoid 在候选动作评分时使用的未来视频信号是否真正预测失败原因，还是只做视觉相似度排序？
  - 异步 1 Hz trigger 在更快接触任务中是否足够，控制周期变化时机制如何调参？
* **上传 PDF 后优先看**:
  - Dream Trigger 与 autonomous boundary learning 方法章节
  - candidate action dreaming / scoring 流程
  - 真实机器人任务、延迟与失败案例分析

### [5]. Overcoming Dynamics-Blindness: Training-Free Pace-and-Path Correction for VLA Models [[HTML]](https://arxiv.org/html/2605.11459) [[PDF]](https://arxiv.org/pdf/2605.11459) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.11459`
* **Authors**: Yanyan Zhang, Chaoda Song, Vikash Singh, Xinpeng Li, Kai Ye, Zhe Hu, Zhongzhu Pu, Yu Yin, Vipin Chaudhary
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它是今天动态环境 VLA 的最清晰 training-free wrapper。
* **问题与切口**: PPC 针对 chunked-action VLA 的 dynamics-blindness：模型从单帧生成未来动作块，然后开环执行，面对传送带、加速目标或突发扰动时容易错过时机。它不要求重训，也不改主干，而是在推理时用闭式算子修正动作块的 pace 与 path，使执行速度和轨迹形状对环境运动作出补偿。这个问题设定非常贴近真实部署。
* **核心方法与证据**: 摘录显示 PPC 将每个 action chunk 的修正目标分解为正交的 pace 和 path 两个通道，无可学习参数，backbone-agnostic。作者还构建 MoveBench，在 ManiSkill/SAPIEN 中固定任务、机械臂和场景，只改变目标运动 regime，包括匀速、加速、不规则运动和静态对照；数据规模为 10 个环境、每个 1000 demonstrations，总计 10K trajectories 与 460K frames。
* **正文要点**:
  - PPC 是 closed-form、training-free、inference-time wrapper，不需要重新训练 VLA。
  - MoveBench 通过固定任务、机械臂和场景，把 motion regime 作为主要评估轴隔离出来。
  - 运动设置包括 uniform、accelerated、irregular 三类动态，以及 static control。
* **为什么值得跟**:
  - 它正面处理 action chunking 的开环代价，这是很多 VLA 部署中的结构性问题。
  - training-free 设计让它更容易叠加到已发布 VLA 上做快速验证。
  - MoveBench 若设计扎实，可成为评估动态场景鲁棒性的有用基准。
* **风险 / 保留意见**:
  - 闭式修正依赖对运动状态的估计，真实视觉噪声下是否稳定需要核查。
  - 方法可能更适合目标运动可被短时估计的任务，对复杂接触动力学未必足够。
* **建议先看**: 先读 pace/path 分解的数学直觉和适用假设，再看 MoveBench 是否真正只隔离 motion 变量。实验中重点比较不同 motion regime 下的失败模式。
* **关键词**: `PPC` `dynamics-blindness` `action chunking` `MoveBench` `training-free`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
* **读 PDF 先核查**:
  - pace 与 path 两个通道的正交假设在非线性接触任务中是否仍成立？
  - PPC 如何获得或估计目标运动，感知误差会如何传导到动作修正？
  - MoveBench 的动态增益是否来自对 motion regime 的通用适应，还是对 pick task 的特定补偿？
* **上传 PDF 后优先看**:
  - PPC closed-form operator 与 pace/path decomposition
  - MoveBench 任务构造和运动 regime 定义
  - 按动态类型划分的实验结果与 ablation

### [6]. ECHO: Continuous Hierarchical Memory for Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2605.10993) [[PDF]](https://arxiv.org/pdf/2605.10993) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.10993`
* **Authors**: Yanbin Hu, Jin Cui, Jiayi Lu, Ruixuan Yang, Jun Ye, Boran Zhao, Xingyu Chen, Xuguang Lan, Pengju Ren
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把 VLA 长时程泛化问题推向层级记忆与经验检索。
* **问题与切口**: ECHO 处理 long-horizon manipulation 中记忆容量和经验复用的问题。它认为已有 memory-augmented VLA 多采用线性或扁平存储，缺少按任务类别、子目标和动作模式组织经验的结构先验，因此难以泛化到未见过的长任务组合。ECHO 将成功经验放入 continuous hierarchical space，以 hyperbolic memory 和 entailment-aware retrieval 支持从相似类别迁移可复用先验。
* **核心方法与证据**: 方法上，ECHO 使用双层思路：把长期成功经验组织在双曲层级空间中，通过 entailment-cone/tree search 检索，并用 residual injection 注入基础策略以保持稳定。实验摘录显示评估覆盖 LIBERO 四个标准 suites、LIBERO-Long、LIBERO-Plus、cross-suite generalization、ablation、retrieval latency 和 memory injection strength；还在 Franka Emika Panda 上做真实平台验证。具体提升幅度需看 PDF。
* **正文要点**:
  - ECHO 明确针对 flat memory retrieval 缺少 manipulation category 层级组织的问题。
  - 实验问题包括 unseen long-horizon task compositions，且强调无 target-suite demonstrations 的 source-suite memory reuse。
  - 结论称通过 residual injection 在引入长期记忆先验时保留 base policy 稳定性。
* **为什么值得跟**:
  - 长时程 VLA 很难只靠当前视觉和指令完成，结构化经验记忆是自然补强方向。
  - 双曲/层级空间为“相似子任务迁移”提供了比扁平最近邻更强的归纳偏置。
  - 如果延迟可控，它可作为部署中持续积累经验的基础模块。
* **风险 / 保留意见**:
  - 记忆质量和验证机制会决定上限，错误成功经验可能被反复检索放大。
  - 层级结构是否能扩展到更开放的真实任务，需要比 LIBERO 更长期的验证。
* **建议先看**: 先看 hyperbolic memory 与 entailment-aware retrieval 如何定义经验相似性。随后核查 residual injection 的稳定性 ablation，以及 memory size 增大时的延迟曲线。
* **关键词**: `ECHO` `hierarchical memory` `hyperbolic space` `long-horizon manipulation` `experience retrieval`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
* **读 PDF 先核查**:
  - continuous hierarchical space 中的节点或记忆单元如何由轨迹构建，是否需要人工类别标签？
  - entailment-cone retrieval 相比 flat memory 的增益主要来自层级结构还是检索度量？
  - residual injection strength 如何影响 policy stability，是否存在任务相关调参敏感性？
* **上传 PDF 后优先看**:
  - memory construction 与 hyperbolic / entailment retrieval 方法章节
  - cross-suite generalization 与 unseen task composition 实验
  - ablation：short-term memory、flat retrieval、injection strength、latency

## Watchlist

### [W1]. SEVO: Semantic-Enhanced Virtual Observation for Robust VLA Manipulation via Active Illumination and Data-Centric Collection [[HTML]](https://arxiv.org/html/2605.11114) [[PDF]](https://arxiv.org/pdf/2605.11114)
* **Paper ID**: `2605.11114`
* **Authors**: Tianchonghui Fang, Yuan Zhuang, Fei Miao
* **Author Priority**: Standard
* **为什么还值得留意**: SEVO 进入 shortlist 是因为它直击低成本机器人和 LeRobot 社区最常见的 sim2real/跨环境失败：背景、光照和视角变化导致策略崩溃。它的 observation-space 语义高亮很实用，且摘录中有真实机器人、100 trials per condition、ACT/SmolVLA 差异分析。但它更像数据采集与视觉预处理技巧，方法通用性和目标类别扩展性需继续观察，因此未进最终精选。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. Learning Action Manifold with Multi-view Latent Priors for Robotic Manipulation [[HTML]](https://arxiv.org/html/2605.11832) [[PDF]](https://arxiv.org/pdf/2605.11832)
* **Paper ID**: `2605.11832`
* **Authors**: Junjin Xiao, Dongyang Li, Yandan Yang, Shuang Zeng, Tong Lin, Xinyuan Chang, Feng Xiong, Mu Xu, Xing Wei, Zhiheng Ma, Qing Zhang, Wei-Shi Zheng
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇关注 multi-view latent priors、geometry-guided gated transformer 和 action manifold learning，切中了 VLA 的 3D 空间理解与动作优化瓶颈。它覆盖 LIBERO、LIBERO-Plus、RoboTwin 2.0 和真实设置，实验面看起来较宽。未进最终精选主要因为今天已有 X-Imitator 代表空间-动作耦合路线，而这篇从摘录看模块较多，需先核查各模块贡献是否清晰可分。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. GuidedVLA: Specifying Task-Relevant Factors via Plug-and-Play Action Attention Specialization [[HTML]](https://arxiv.org/html/2605.12369) [[PDF]](https://arxiv.org/pdf/2605.12369)
* **Paper ID**: `2605.12369`
* **Authors**: Xiaosong Jia, Bowen Yang, Zuhao Ge, Xian Nie, Yuchen Zhou, Cunxin Fan, Yufeng Li, Yilin Chai, Chao Jing, Zijian Liang, Qingwen Bu, Haidong Cao, Chao Wu, Qifeng Li, Zhenjie Yang, Chenhe Zhang, Hongyang Li, Zuxuan Wu, Junchi Yan, Yu-Gang Jiang
* **Author Priority**: Standard
* **为什么还值得留意**: GuidedVLA 值得 watch，因为它把 action decoder 的注意力显式拆到 object grounding、skill recognition 和 geometry perception，回应了 VLA shortcut learning 与 causal confusion。它还覆盖 LIBERO-Plus、RoboTwin 2.0 和双臂真实平台，有很强的鲁棒性评估取向。未进最终精选是因为其核心更偏 attention specialization 与引导机制，和今天主线中的 WAM、test-time adaptation、memory、dynamics wrapper 相比优先级略低。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. Retrieve-then-Steer: Online Success Memory for Test-Time Adaptation of Generative VLAs [[HTML]](https://arxiv.org/html/2605.10094) [[PDF]](https://arxiv.org/pdf/2605.10094)
* **Paper ID**: `2605.10094`
* **Authors**: Jianchao Zhao, Huoren Yang, Yusong Hu, Yuyang Gao, Qiguan Ou, Cong Wan, SongLin Dong, Zhiheng Ma, Yihong Gong
* **Author Priority**: Standard
* **为什么还值得留意**: Retrieve-then-Steer 很接近最终精选：它研究 persistent deployment，把成功测试经验存进 online success memory，再检索为 generative VLA 的采样先验。这个设定与 ECHO 的记忆路线互补，也贴近真实机器人反复执行同类任务的场景。未进最终精选主要是为了避免记忆类论文过度集中；相较 ECHO，它更偏局部部署适应，理论结构和长期泛化边界还需 PDF 核查。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
