# RoboPulse | 2026-04-07

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 98 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线很清楚：VLA 正在从“能跟随指令”转向“能被精细操控、能跨阶段推理、能接上世界模型与真实部署”的系统化升级。最终精选的 6 篇刚好覆盖三个最关键断点：高层 VLM 到低层动作接口的重构、视频/世界模型对动作与交互的吸收、以及 sim2real 与推理时控制策略的工程闭环。2602.13193、2601.07060 和 2603.09030 入选，是因为它们分别抓住了 steerability、long-horizon progress 和 world-model data paradigm 这三个当前最容易卡住泛化上限的瓶颈。VIP 作者里今天最值得优先跟踪的是 Sergey Levine；此外，虽只进 watchlist 的 Xiaolong Wang 也值得持续关注，因为其 human-in-the-loop 数据效率路线与实机闭环高度相关。

## 今日信号

- VLA 的下一步不是单纯继续堆数据，而是把高层推理如何真正“施加到”低层动作接口上做细，这一点从 steerable commands、progress cues 和 adaptive chunking 三条线同时出现可以看得很清楚。
- 世界模型方向的竞争焦点正从 backbone 之争转向数据范式与动作可控性之争，autonomous play 和 frontier video model + IDM 都在试图把“可想象未来”变成可执行控制。
- Sim2Real 不再只靠单点 domain gap 技巧，模块化 observation/action bridge 与 inference-time control heuristics 正成为更现实、更可部署的路线。

## Editor's Picks

### [1]. Steerable Vision-Language-Action Policies for Embodied Reasoning and Hierarchical Control [[VIP]] [[HTML]](https://arxiv.org/html/2602.13193) [[PDF]](https://arxiv.org/pdf/2602.13193) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2602.13193`
* **Authors**: William Chen, Jagdeep Singh Bhatia, Catherine Glossop, Nikhil Mathihalli, Ria Doshi, Andy Tang, Danny Driess, Karl Pertsch, Sergey Levine
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，它直接改造了 VLM 到 VLA 的接口层，而这正是层级机器人系统最容易卡住泛化的地方。
* **问题与切口**: 这篇工作直指当前层级式机器人系统里最卡脖子的接口问题：高层 VLM 虽能推理，但通常只能用自然语言去驱动低层 VLA，导致推理难以细粒度影响执行。作者提出 Steerable Policies，把低层策略改造成可接受子任务、运动描述、像素级指向等多种命令抽象的 VLA，使高层模型不再只会“下达任务”，而能更具体地塑形动作过程。这比传统语言接口更像把 VLM 的语义能力压进控制通道。
* **核心方法与证据**: 从 HTML 可见，作者给高层 VLM 提供任务说明、各类 steering command 风格示例、历史观测与历史命令，并鼓励其显式推理后再输出 steerable command；部分 grounded command 还会通过额外 Gemini 调用转成坐标。实验在 Bridge WidowX 上沿用 generalist policy 评测协议，并基于 OpenVLA/Prismatic 7B 改造低层策略，同时还验证该接口可迁移到另一类 VLA。当前摘录能支持方法合理性，但具体增益幅度仍需看 PDF。
* **正文要点**:
  - 低层策略支持多种命令抽象，而不再只接收单句自然语言任务描述。
  - 高层 VLM 采用 in-context 提示、显式推理与历史命令/观测回看来生成 steering command。
  - 作者最终保留 pointing command，但放弃 grounded gripper trace，说明不同 steering 形式的可用性并不均衡。
* **为什么值得跟**:
  - 它把 VLM 与 VLA 之间最薄弱的接口层单独做成研究对象，这对后续层级机器人系统很关键。
  - 如果 steerability 真的足够强，高层模型的场景理解与 in-context learning 才有机会稳定落到低层控制。
  - Sergey Levine 这条线值得优先跟踪，因为它明显在重新定义 VLA 的控制接口，而不是只做数据或尺度扩张。
* **风险 / 保留意见**:
  - 方法依赖外部 VLM 提示工程与额外坐标解析调用，真实部署时的时延、成本与稳定性需要核查。
  - HTML 摘录没有给出不同 steering 类型各自的失败模式分布，接口通用性可能强于稳定性。
* **建议先看**: 先看作者如何定义并组织 steering command 空间，再看两类层级控制实验是否真正证明 richer interface 比自然语言接口更能传递推理能力。
* **关键词**: `VLA` `hierarchical control` `steerability` `embodied reasoning` `Sergey Levine`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 不同 steering abstraction 在哪些任务阶段最有效，作者是否给出了分类型 ablation？
  - 高层 VLM 的显式推理究竟提升了任务规划，还是主要帮助了场景指向与对象消歧？
  - 额外的坐标解析调用是否成为系统瓶颈，错误解析会怎样传导到低层动作？
* **上传 PDF 后优先看**:
  - 方法部分：steering command 设计与提示模板
  - 实验部分：层级控制对比与 generalization tasks
  - 误差分析部分：不同 grounded command 的成功率与失败模式

### [2]. PlayWorld: Learning Robot World Models from Autonomous Play [[HTML]](https://arxiv.org/html/2603.09030) [[PDF]](https://arxiv.org/pdf/2603.09030) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.09030`
* **Authors**: Tenny Yin, Zhiting Mei, Zhonghe Zheng, Miyu Yamane, David Wang, Jade Sceats, Samuel M. Bateman, Lihan Zha, Apurva Badithela, Ola Shorinwa, Anirudha Majumdar
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它抓住了机器人世界模型里最被低估的变量：不是再换一个 backbone，而是先换训练数据范式。
* **问题与切口**: 这篇工作的关键判断是，机器人视频世界模型的失真不一定先来自模型容量，而可能先来自训练数据的成功偏置与交互覆盖不足。作者据此提出 PlayWorld，用 autonomous play 而不是人工示范或任务策略 rollout 去训练动作条件世界模型，并把可过夜、无监督地扩大交互分布当成核心贡献。相对现有“示范+微调”的路线，它更像是在重写 world model 的数据来源假设。
* **核心方法与证据**: 方法上，论文采用预训练 Stable Video Diffusion 骨干，使用时空分解注意力并注入逐帧动作条件，以强化动作可控性；同时联合预测三个相机视角，降低部分可观测性影响，并以 DROID 权重初始化，再在 play 数据上微调。HTML 还提到配套 curriculum learning 以消化未筛选交互数据，并给出仿真与下游评估动机；但当前摘录未展开全部指标，因此对“动力学保真度”的强弱仍应保守看待。
* **正文要点**:
  - 核心主张是以自主 play 数据替代成功示范偏置更强的训练来源。
  - 世界模型基于预训练 Stable Video Diffusion，并注入逐帧动作条件以增强可控性。
  - 模型联合预测三个相机视角，并配合 curriculum learning 处理未筛选交互数据。
* **为什么值得跟**:
  - 它把世界模型研究从结构比较拉回到“什么数据最适合学动力学”这个更根本的问题。
  - 如果 autonomous play 能稳定降低 hallucination，世界模型用于策略评估与数据合成的可信度会一起上升。
  - 这条路线天然对可扩展实机采集友好，尤其适合长期、低人工值守的数据工厂。
* **风险 / 保留意见**:
  - play 数据覆盖广但可能稀释任务相关信号，模型是否学到有用交互而非大量无效运动需要核查。
  - HTML 摘录未完整展示与示范数据、任务 rollout 数据的等预算对比，证据强度仍要看全文实验。
* **建议先看**: 先验证作者关于“示范偏置导致世界模型 hallucination”的论证，再看三视角预测和 curriculum 是否真是 autonomous play 成功所必需的关键件。
* **关键词**: `world model` `autonomous play` `video diffusion` `robot data` `simulator`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 在相同数据量、相同算力下，autonomous play 相对示范数据的优势是否仍然成立？
  - 三视角联合预测提升的主要是遮挡鲁棒性，还是对接触动力学的真实建模？
  - curriculum 如何排序未筛选 play 数据，是否会牺牲对稀有但关键交互事件的学习？
* **上传 PDF 后优先看**:
  - 引言部分：数据偏置与 hallucination 假设
  - 方法部分：动作条件视频扩散与多视角建模
  - 实验部分：不同数据来源的世界模型对比与下游用途

### [3]. Veo-Act: How Far Can Frontier Video Models Advance Generalizable Robot Manipulation? [[HTML]](https://arxiv.org/html/2604.04502) [[PDF]](https://arxiv.org/pdf/2604.04502) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.04502`
* **Authors**: Zhongru Zhang, Chenghan Yang, Qingzhou Lu, Yanjiang Guo, Jianke Zhang, Yucheng Hu, Jianyu Chen
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把 frontier video model 从“看起来懂物理”往“能给机器人产出高层动作意图”推进了一步。
* **问题与切口**: 这篇工作试图回答一个很直接但很难的问题：像 Veo-3 这样的前沿视频模型，离可泛化机器人操控到底还有多远。作者提出 Veo-Act，让视频模型先从当前观测生成未来图像序列，再由只用 random-play 数据训练的逆动力学模型恢复动作，并与低层 VLA 组成层级系统。新意不在于再训练一个更大的机器人模型，而在于把通用视频先验转成可执行操控意图。
* **核心方法与证据**: 从摘录看，实验同时覆盖仿真与真实机器人，并专门构造会暴露 VLA instruction-following 失败的混淆设置。系统使用全局相机做视频生成与 IDM 预测，保留腕部相机给低层执行阶段；为支撑大规模训练，作者还搭建了与实机镜像的 IsaacLab 环境，并收集 300k frame-pair 的随机抓取/释放数据训练 multi-head IDM。证据说明方法链条完整，但 HTML 尚不足以判断高层视频规划与低层切换策略各自贡献。
* **正文要点**:
  - 零样本主线是“视频预测未来，再由 IDM 反推出动作”，且 IDM 只用 random-play 数据训练。
  - 系统采用分层结构：高层视频/IDM 提供运动意图，低层 VLA 负责稳健接触执行。
  - 作者同时构建了与实机对应的 IsaacLab 仿真环境，以支撑大规模数据收集与对齐评测。
* **为什么值得跟**:
  - 它是把 foundation video model 真正压到机器人控制链里的代表性尝试，而不是只把视频生成当可视化工具。
  - random-play 训练 IDM 的设定降低了对专家演示的依赖，符合可扩展数据获取的趋势。
  - 如果这条路线成立，未来 world model、video planner 与 VLA executor 的分层组合会更有操作性。
* **风险 / 保留意见**:
  - 高层视频预测是否真的学到任务相关因果，而不是只生成外观合理的未来，需要更细的失败分析。
  - HTML 摘录没有完整展开切换机制与误差累积控制，系统稳定性仍有不确定性。
* **建议先看**: 先把 Veo-3 生成未来、IDM 反推动作、低层 VLA 接管执行这三段链路分开看，再核查作者是否证明了每一段都在贡献泛化而不是互相补漏洞。
* **关键词**: `video model` `inverse dynamics` `hierarchical manipulation` `random play` `VLA`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - IDM 只看全局相机时，如何处理细粒度接触与手部姿态信息的缺失？
  - 从视频规划切到低层 VLA 的时机由什么信号决定，是否存在任务依赖的人工规则？
  - 相比直接用 VLA 或 world model planning，Veo-Act 的优势主要来自视频先验还是层级分工？
* **上传 PDF 后优先看**:
  - 方法部分：Veo-3 到 IDM 的接口设计
  - 实验部分：仿真/实机混淆设置与基线对比
  - 消融或分析部分：random-play IDM、相机配置与切换策略

### [4]. Sim2Real-AD: A Modular Sim-to-Real Framework for Deploying VLM-Guided Reinforcement Learning in Real-World Autonomous Driving [[VIP]] [[HTML]](https://arxiv.org/html/2604.03497) [[PDF]](https://arxiv.org/pdf/2604.03497) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.03497`
* **Authors**: Zilin Huang, Zhengyang Wan, Zihao Sheng, Boyue Wang, Junwei You, Yue Leng, Sikai Chen
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，它不是泛泛谈 sim2real，而是把 VLM-guided RL 上车所缺的 observation/action bridge 拆成了可检验的模块。
* **问题与切口**: 这篇工作聚焦一个部署痛点：仿真里训练出的 VLM-guided RL 驾驶策略，往往依赖仿真原生观测与动作语义，现实车辆根本拿不到同款输入输出。Sim2Real-AD 的贡献，是把这个断点拆成几块明确接口：用 GOB 把单目图像转成仿真兼容 BEV，用 PAM 把策略输出映射到平台无关的物理命令，再用渐进式训练和实时部署链路把它们接起来。它更像一套可落地迁移架构，而不是单一技巧。
* **核心方法与证据**: HTML 摘录给出的证据相对完整：作者围绕五个研究问题组织实验，分别检查算法排序是否保真、GOB/PAM/TPT 的单独贡献、GOB 对 BEV 观测保真度、未见地图泛化，以及能否零样本上真实车辆。仿真实验在 CARLA 0.9.13 上只用 Town 2 训练，并在 Towns 1/3/4/5 测试分布外泛化；结论还声称该框架已接到全尺寸 Ford E-Transit。现有证据足以支撑“工程闭环完整”，但真实道路安全边界仍需谨慎读全文。
* **正文要点**:
  - 框架显式分解为 GOB、PAM、TPT 与实时部署流水线四个模块。
  - 实验设计不只看最终性能，还单独追问观测桥与动作桥各自的贡献。
  - 作者把零样本真实车辆部署写成核心研究问题，而非只停留在仿真泛化。
* **为什么值得跟**:
  - 这篇工作把 VLM-guided RL 从论文里的闭环仿真系统，往真实车辆可部署系统推进了一大步。
  - 模块化拆解让 sim2real 失败不再是黑箱，有助于后续社区做替换、诊断和标准化评测。
  - 它也提醒我们，驾驶中的 world model/VLA 叙事若没有 observation 和 action semantics 对齐，部署就很难成立。
* **风险 / 保留意见**:
  - 真实车实验的场景覆盖、干预机制和安全冗余在摘录里没有展开，不能过度外推到开放道路。
  - GOB 把单目图像转换为 BEV 的误差可能在长尾场景里被 RL 策略放大，这需要细看 failure cases。
* **建议先看**: 先按模块读，不要一上来只看总成绩；优先确认 GOB 和 PAM 是否真的让“仿真策略语义”对接到了真实车辆，而不是被额外工程规则兜住。
* **关键词**: `sim2real` `VLM-guided RL` `autonomous driving` `BEV bridge` `action mapping`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - GOB 在视觉遮挡、车道线缺失或极端光照下的 BEV 误差会怎样影响策略稳定性？
  - PAM 将策略输出映射为物理命令时，是否对不同车辆平台还需要重新标定？
  - TPT 的两阶段切分具体冻结/放开什么模块，为什么比端到端适配更稳定？
* **上传 PDF 后优先看**:
  - 方法部分：GOB、PAM、TPT 的接口定义
  - 实验部分：模块消融与跨 Town 泛化
  - 真实部署部分：车辆平台、实时性与安全干预设置

### [5]. PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation [[HTML]](https://arxiv.org/html/2601.07060) [[PDF]](https://arxiv.org/pdf/2601.07060) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2601.07060`
* **Authors**: Yuanzhe Liu, Jingyuan Zhu, Yuchen Mo, Gen Li, Xu Cao, Jin Jin, Yifan Shen, Zhengyuan Li, Tianjiao Yu, Wenzhen Yuan, Fangqiang Ding, Ismini Lourentzou
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它正面处理了 long-horizon VLA 最常见却最少被建模的错误：重复、漏步和过早结束。
* **问题与切口**: PALM 针对长时程操控里“看得懂局部、但走不完整条任务链”的 VLA 症结，提出把 affordance reasoning 与 subtask progress 建模直接嵌进策略学习。核心切口不是再加一个高层 planner，而是让策略在执行时持续感知当前子任务相关的交互线索，并判断自己已经推进到哪一阶段，从而减少重复动作、跳步和提前收尾。相对传统混合示范行为克隆，这是一种更结构化的闭环时间建模。
* **核心方法与证据**: 从正文摘录可见，PALM 由两个紧耦合模块组成：一是预测未来偏移处 affordance-centric latent 的细粒度 affordance 预测模块，用作稳定感知的中间表征；二是连续 progress estimation，用来描述子任务内部的相位推进。训练上先在 DROID、BridgeData V2、EPIC-KITCHENS、RoboCerebra 上预训练，再用 942 条带 affordance 与连续进度标签的机器人轨迹微调。实验覆盖 LIBERO 与 CALVIN，结论给出了 CALVIN ABCD 提升 12.5% 和 LIBERO-LONG 91.8% 成功率。
* **正文要点**:
  - 作者明确把长时程失败归因于缺少 interaction cue 与 subtask progress 的内部建模。
  - 方法同时学习未来 affordance latent 与连续 progress，而不是只做一步动作预测。
  - 训练数据跨机器人示范与人类第一视角视频，并使用半自动流程补 affordance/进度标签。
* **为什么值得跟**:
  - 这篇工作把 long-horizon VLA 的核心问题从“规划不够强”细化成“阶段感知缺失”，问题定义很有价值。
  - affordance 与 progress 作为中间变量，提供了比纯动作监督更可解释的训练信号。
  - 如果结果在实机上站得住，这会成为长任务 VLA 设计里很自然的结构先验。
* **风险 / 保留意见**:
  - 方法依赖额外的 affordance 和连续进度标签，数据标注成本与跨任务迁移性需要仔细评估。
  - 当前成功很可能部分受益于特定 benchmark 的阶段结构，开放任务上的泛化边界还不清楚。
* **建议先看**: 先看作者如何把 affordance latent 与 progress loop 绑定到闭环控制，再看标签来源与 ablation，判断性能提升到底来自结构设计还是额外监督。
* **关键词**: `long-horizon VLA` `affordance reasoning` `progress estimation` `LIBERO` `CALVIN`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - continuous progress 的监督粒度如何定义，不同任务之间是否共享同一标度？
  - future affordance latent 预测失败时，progress 模块会不会反而放大错误累积？
  - 若去掉 EPIC-KITCHENS/RoboCerebra 这类带时间语义的数据，PALM 还剩多少优势？
* **上传 PDF 后优先看**:
  - 方法部分：affordance latent 与 progress loop 的耦合方式
  - 数据部分：半自动 affordance/进度标注流程
  - 实验部分：CALVIN、LIBERO-LONG 与长时程错误类型分析

### [6]. Adaptive Action Chunking at Inference-time for Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2604.04161) [[PDF]](https://arxiv.org/pdf/2604.04161) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.04161`
* **Authors**: Yuanchang Liang, Xiaobo Wang, Kai Wang, Shuo Wang, Xiaojiang Peng, Haoyu Chen, David Kim Huat Chua, Prahlad Vadakkepat
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它用很轻的 inference-time 改动，直接碰到了 VLA 执行里最现实的稳定性与响应性权衡。
* **问题与切口**: 这篇工作关注一个常被经验设定掩盖的问题：VLA 的 action chunk 长度并非越大越稳、越小越灵，而是在响应新信息与跨 chunk 连续性之间存在明显张力。AAC 的新意是把 chunk size 从固定超参数改成推理时自适应决策，依据动作熵在运输段使用更大 chunk，在关键操作段缩小 chunk，试图同时减少 mode-jumping 和反应迟钝。这是典型的小改动、但可能高杠杆的系统层创新。
* **核心方法与证据**: 从 HTML 可见，AAC 是纯 inference-time 策略，核心信号是 action entropy，而不是重新设计 VLA 主干。实验覆盖 RoboCasa 24 个厨房任务与 LIBERO 四个 suite，并且还包含真实世界应用，目标是证明它能在不同 manipulation stage 间自动切换 chunk 长度。摘要与结论都强调其优于固定 chunk 与若干替代方案；但当前摘录未展开 entropy 计算、阈值机制和真实机细节，因此具体稳定性来源仍要看全文。
* **正文要点**:
  - 论文把固定 chunk length 视为当前 VLA 推理阶段的关键瓶颈之一。
  - AAC 以 action entropy 作为自适应选择 chunk size 的线索。
  - 作者明确区分运输阶段与关键操作阶段，认为两者需要不同 temporal granularity。
* **为什么值得跟**:
  - 它说明 VLA 性能不只受模型规模和数据影响，推理调度本身也是高价值优化点。
  - 如果 AAC 通用，很多现有 action-chunking 模型都可能不改训练就获益。
  - 这类方法对实机很有吸引力，因为工程代价小、可直接叠加到已有系统上。
* **风险 / 保留意见**:
  - action entropy 是否稳定对应“该不该重规划”需要跨模型、跨任务验证。
  - 若自适应机制过于敏感，可能在边界阶段频繁切换 chunk，反而带来新的抖动。
* **建议先看**: 先盯住 entropy 与 chunk size 的映射规则，再看作者是否用分阶段分析证明收益确实来自关键时刻的重规划，而不是整体更保守。
* **关键词**: `VLA` `action chunking` `inference-time control` `entropy` `robot manipulation`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
* **读 PDF 先核查**:
  - action entropy 是按 token、动作维度还是 chunk 分布统计，哪种定义最有效？
  - AAC 的阈值或调度规则是否需要对不同任务重新调参？
  - 在真实机器人上，AAC 的收益主要体现为更高成功率，还是更平滑、更可恢复的执行过程？
* **上传 PDF 后优先看**:
  - 方法部分：entropy 估计与 chunk 调度规则
  - 实验部分：RoboCasa/LIBERO 分任务表现
  - 分析部分：不同 manipulation stage 的 chunk 分布与失败案例

## Watchlist

### [W1]. Human-Robot Copilot for Data-Efficient Imitation Learning [[VIP]] [[HTML]](https://arxiv.org/html/2604.03613) [[PDF]](https://arxiv.org/pdf/2604.03613)
* **Paper ID**: `2604.03613`
* **Authors**: Rui Yan, Zaitian Gongye, Lars Paulsen, Xuxin Cheng, Xiaolong Wang
* **Author Priority**: Core VIP
* **为什么还值得留意**: 它进入 shortlist，主要因为问题切得很准：在少量示范下，策略真正难的是部署时掉进 OOD 状态后谁来高效纠偏。论文把异构 embodiment teleoperation、可调 scaling factor 和 human-in-the-loop 数据增广连成一条实机闭环，且有 Xiaolong Wang 这条值得跟踪的作者线。之所以没进最终精选，是因为它更偏 imitation learning 的数据采集与纠错接口，而不是今天主线中的 VLA/world model/Sim2Real 方法前沿；从当前摘录看，方法通用性强，但对通用机器人智能能力的外溢价值还弱于最终入选几篇。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. E-VLA: Event-Augmented Vision-Language-Action Model for Dark and Blurred Scenes [[HTML]](https://arxiv.org/html/2604.04834) [[PDF]](https://arxiv.org/pdf/2604.04834)
* **Paper ID**: `2604.04834`
* **Authors**: Jiajun Zhai, Hao Shi, Shangwei Guo, Kailun Yang, Kaiwei Wang
* **Author Priority**: Standard
* **为什么还值得留意**: 它进入 shortlist，是因为 E-VLA 把事件相机直接接到 VLA 感知链上，正面处理低照、模糊和 black clipping 这类实际部署里很致命的感知退化。论文还有自建 RGB-event-action 数据与冻结 backbone 下的融合设计，说明作者在追求预训练兼容性。没进最终精选的原因是研究焦点更偏特定传感器增强与恶劣视觉条件鲁棒性，主线深度不如今天入选的 steerability、world model 和 sim2real 断点；此外当前证据更多说明“能补 perception”，对更广泛 VLA reasoning/control 的外推还需保守。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)

### [W3]. Red-Teaming Vision-Language-Action Models via Quality Diversity Prompt Generation for Robust Robot Policies [[HTML]](https://arxiv.org/html/2603.12510) [[PDF]](https://arxiv.org/pdf/2603.12510)
* **Paper ID**: `2603.12510`
* **Authors**: Siddharth Srikanth, Freddie Liang, Ya-Chuan Hsu, Varun Bhatt, Shihan Zhao, Henry Chen, Bryon Tjanaka, Minjune Hwang, Akanksha Saran, Daniel Seita, Aaquib Tabrez, Stefanos Nikolaidis
* **Author Priority**: Standard
* **为什么还值得留意**: 它进入 shortlist，因为这篇 paper 抓住了一个经常被忽略的部署风险：VLA 对语言措辞极其敏感，而我们通常并不知道它会被什么样的自然指令击穿。Q-DIG 用 quality diversity 生成多样、仍与任务相关的对抗式指令，再把这些数据回灌微调，这对稳健性评测和 red-teaming 很有价值。没进最终精选，是因为它更像安全评估与数据增广工具链，而不是今天优先关注的 VLA 控制接口、世界模型或 sim2real 主方法创新。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. DriveVA: Video Action Models are Zero-Shot Drivers [[HTML]](https://arxiv.org/html/2604.04198) [[PDF]](https://arxiv.org/pdf/2604.04198)
* **Paper ID**: `2604.04198`
* **Authors**: Mengmeng Liu, Diankun Zhang, Jiuming Liu, Jianfeng Cui, Hongwei Xie, Guang Chen, Hangjun Ye, Michael Ying Yang, Francesco Nex, Hao Cheng
* **Author Priority**: Standard
* **为什么还值得留意**: 它进入 shortlist，是因为 DriveVA 明确踩在今天关注的 world model / world action model 交叉点上：联合解码未来视频与动作，并强调跨数据集、跨传感器配置的 zero-shot generalization。NAVSIM、nuScenes 和 Bench2Drive 的设置也说明作者在认真碰闭环评测与跨域迁移。没有进入最终精选，主要是当前 HTML 摘录对核心架构与关键证据的展开还不如 Sim2Real-AD 充分，而且驾驶场景下的 world-model 叙事与今天更偏操控的主线相比稍微次一优先级。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)
