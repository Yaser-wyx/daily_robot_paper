# RoboPulse | 2026-04-28

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 97 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线很清楚：VLA 正从“能做多任务”转向“能被稳定操控、能在低数据下继续适配、能借助 RL 与人类视频继续扩展、也能被更严肃地做 Sim2Real 评测”。最终精选覆盖了这条链条上的六个关键位置：基础模型能力边界、在线 RL 精修、低数据后训练失锁、保留 VLM 泛化性的架构改造、人类意图先验迁移，以及评测层面的 sim-to-real 统计推断。之所以把它们放进最终精选，是因为它们不是单点提效，而是在重新定义下一阶段通用机器人系统该怎么训练、怎么适配、怎么验证。VIP 作者里最值得优先跟踪的是 Sergey Levine、Chelsea Finn、Karol Hausman 所代表的 PI 路线，以及 Jeannette Bohg 对低数据 VLA 后训练失锁问题的系统化刻画。

## 今日信号

- 今天最值得记住的研究信号是：VLA 的下一步不只是更大模型，而是通过上下文条件化、可控接口和结构化先验，把“泛化能力”变成可调度、可转向、可迁移的能力。
- 今天最值得记住的趋势判断是：RL 正在重新进入 VLA 主线，但形态不是从头学控制，而是围绕预训练表征做轻量、样本高效、接触阶段导向的在线精修。
- 今天最值得记住的趋势判断是：Sim2Real 的竞争焦点正在从单纯“怎么迁移”扩展到“怎么可信评测”和“怎么在部署约束下运行”，评测与系统约束开始上升为一等研究对象。

## Editor's Picks

### [1]. $π_{0.7}$: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities [[VIP]] [[HTML]](https://arxiv.org/html/2604.15483) [[PDF]](https://arxiv.org/pdf/2604.15483) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.15483`
* **Authors**: Physical Intelligence, Bo Ai, Ali Amin, Raichelle Aniceto, Ashwin Balakrishna, Greg Balke, Kevin Black, George Bokinsky, Shihao Cao, Thomas Charbonnier, Vedant Choudhary, Foster Collins, Ken Conley, Grace Connors, James Darpinian, Karan Dhabalia, Maitrayee Dhaka, Jared DiCarlo, Danny Driess, Michael Equi, Adnan Esmail, Yunhao Fang, Chelsea Finn, Catherine Glossop, Thomas Godden, Ivan Goryachev, Lachlan Groom, Haroun Habeeb, Hunter Hancock, Karol Hausman, Gashon Hussein, Victor Hwang, Brian Ichter, Connor Jacobsen, Szymon Jakubczak, Rowan Jen, Tim Jones, Gregg Kammerer, Ben Katz, Liyiming Ke, Mairbek Khadikov, Chandra Kuchi, Marinda Lamb, Devin LeBlanc, Brendon LeCount, Sergey Levine, Xinyu Li, Adrian Li-Bell, Vladislav Lialin, Zhonglin Liang, Wallace Lim, Yao Lu, Enyu Luo, Vishnu Mano, Nandan Marwaha, Aikys Mongush, Liam Murphy, Suraj Nair, Tyler Patterson, Karl Pertsch, Allen Z. Ren, Gavin Schelske, Charvi Sharma, Baifeng Shi, Lucy Xiaoyang Shi, Laura Smith, Jost Tobias Springenberg, Kyle Stachowicz, Will Stoeckle, Jiaming Tang, Jimmy Tanner, Shalom Tekeste, Marcel Torne, Kyle Vedder, Quan Vuong, Anna Walling, Haohuan Wang, Jason Wang, XuDong Wang, Chris Whalen, Samuel Whitmore, Blake Williams, Charles Xu, Sukwon Yoo, Lili Yu, Wuming Zhang, Zhuoyang Zhang, Ury Zhilinsky
* **Author Priority**: Core VIP
* **一句话结论**: 今天最该优先看的总纲论文之一；如果只挑一篇看 generalist VLA 的能力边界，就先看它。
* **问题与切口**: 这篇工作直指机器人基础模型最关键的短板：已有 VLA 虽然规模越来越大，但很难像语言模型那样把见过的技能重新组合成未见任务。π0.7 的切口不是继续堆单一机器人数据或做任务专用微调，而是在训练中引入多样上下文条件，让模型学会利用任务、场景与执行线索进行可操控推理，从而把泛化从“同任务更稳”推进到跨任务、跨场景、跨 embodiment 的可转向能力。
* **核心方法与证据**: 从摘录看，论文核心是 diverse context conditioning，也就是在训练时向模型提供额外 episode 信息，并在测试时可选地继续利用这些上下文。实验围绕五类问题展开：高难度灵巧任务的开箱即用表现、灵活指令跟随、跨 embodiment 迁移、未见技能组合，以及任务与上下文多样性扩展实验。证据形态主要是多组行为评测与对比，能确认方法范围很广，但具体收益分解仍需 PDF 细看。
* **正文要点**:
  - 训练核心不是单纯扩数据，而是引入多样上下文条件化与 prompting 策略。
  - 实验被明确拆成五类能力问题：开箱即用表现、指令跟随、跨 embodiment、技能组合、多样性扩展。
  - 摘要与实验摘录都强调其在复杂任务上可与更专用的 RL 微调模型竞争。
* **为什么值得跟**:
  - 它把通用机器人模型的评判标准从“是否覆盖更多任务”提升到“是否能在新情境下重新组合技能”。
  - 它提示未来 scaling 轴不只在数据量，也在上下文多样性与条件化设计。
  - 它直接来自 Chelsea Finn、Sergey Levine、Karol Hausman 所在路线，值得持续跟踪其后续扩展。
* **风险 / 保留意见**:
  - 大规模协作系统通常组件很多，单靠 HTML 摘录还看不清真正驱动增益的是数据、上下文还是模型结构。
  - 训练时和测试时上下文的可用性边界尚不清楚，真实部署是否依赖额外提示需要回 PDF 核查。
* **建议先看**: 先顺着引言里“generalist 不等于 compositional generalization”的论点，看上下文条件化究竟如何定义。再跳到五类实验，判断它提升的是泛化本身，还是更强的任务提示利用能力。
* **关键词**: `VLA` `robot foundation model` `context conditioning` `compositional generalization` `cross-embodiment`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - diverse context conditioning 具体注入了哪些 episode 信息，哪些在测试时是必需的、哪些只是可选增强？
  - 跨 embodiment 泛化体现为真正的动作接口迁移，还是主要来自共享高层表征后的快速适配？
  - 任务与上下文多样性扩展实验里，性能提升是否出现明显边际递减或饱和？
* **上传 PDF 后优先看**:
  - 方法章节里关于 context conditioning 与 prompting 设计的定义和接口。
  - 跨 embodiment 与 compositional generalization 的实验设置和评测口径。
  - 多样性扩展实验、失败案例和限制讨论。

### [2]. RL Token: Bootstrapping Online RL with Vision-Language-Action Models [[VIP]] [[HTML]](https://arxiv.org/html/2604.23073) [[PDF]](https://arxiv.org/pdf/2604.23073) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.23073`
* **Authors**: Charles Xu, Jost Tobias Springenberg, Michael Equi, Ali Amin, Adnan Esmail, Sergey Levine, Liyiming Ke
* **Author Priority**: Core VIP
* **一句话结论**: 如果你关心 VLA 怎么被 RL 真正接管而不是整模重训，这篇值得优先读。
* **问题与切口**: 这篇论文瞄准 VLA 在真实操作中的“最后一毫米”问题：基础模型往往已经会做任务，但在接触、对位、插入、拧紧这类高精度阶段仍然慢且脆弱。作者提出 RL Token，把预训练 VLA 的知识压缩成一个适合在线强化学习读取的接口，再用很小的 actor-critic 头在少量真实交互中做精修，目标不是替换 VLA，而是让 RL 只接管最该改进的那一段控制。
* **核心方法与证据**: 方法上，论文先让 VLA 暴露一个紧凑的 RL token，再围绕它训练轻量 actor 与 critic；实验问题还明确拆解到 chunked action prediction、policy regularization、reference-action pass-through 等组件贡献。评测覆盖四个需要亚毫米精度与接触鲁棒性的真实任务，并对比其他 RL 路线与基座 VLA。摘录中的结论声称只需数小时真实练习即可改善成功率与速度，且最难阶段可出现显著提速。
* **正文要点**:
  - 作者把方法问题明确成四问：是否优于基座 VLA、是否优于替代 RL 路线、各组件有何贡献、是否学到新策略。
  - 实验专门选取需要高精度、接触丰富控制的真实操作任务，而非宽松的离线 benchmark。
  - 组件设计不只是一枚 RL token，还包括动作分块、策略正则和 reference-action pass-through。
* **为什么值得跟**:
  - 它给出了一条现实可行的 VLA+在线 RL 路线，重点是几小时内而不是几周内适配。
  - 它把 RL 的作用限定为在预训练表征之上做轻量精修，降低了全模型在线更新的代价与不稳定性。
  - 它直接回答了“基础模型会做，但不够准不够快”这一真实部署痛点。
* **风险 / 保留意见**:
  - 结论已提示该路线仍需要额外人工介入或监督，自动化程度并非完全闭环。
  - 当前证据集中在少数精密操作任务，是否能扩展到更开放、更长时程的技能仍待验证。
* **建议先看**: 先看 RL token 如何作为 VLA 与 RL 的接口被定义，再看与替代 RL 方法的比较和组件消融。最后重点看策略分析，判断它是真的学到新策略，还是只是在原策略附近局部修补。
* **关键词**: `VLA` `online RL` `RL token` `precision manipulation` `actor-critic`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
* **读 PDF 先核查**:
  - RL token 来自 VLA 的哪一层或哪类表征，在线学习时底座参数是否被冻结？
  - reference-action pass-through 在什么条件下触发，它会不会限制策略探索空间？
  - 性能收益主要来自接触关键阶段的速度提升，还是来自整体成功率与容错性的同步改善？
* **上传 PDF 后优先看**:
  - 方法章节里 RL token 与 actor-critic 接口的具体定义。
  - 与其他 RL 基线、基座 VLA 的对比实验和组件消融。
  - 策略变化分析、行为可视化或阶段性速度改善证据。

### [3]. Breaking Lock-In: Preserving Steerability under Low-Data VLA Post-Training [[VIP]] [[HTML]](https://arxiv.org/html/2604.23121) [[PDF]](https://arxiv.org/pdf/2604.23121) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.23121`
* **Authors**: Suning Huang, Jiaqi Shao, Ke Wang, Qianzhong Chen, Jiankai Sun, Yanjiang Guo, Mac Schwager, Jeannette Bohg
* **Author Priority**: Core VIP
* **一句话结论**: 这是今天最该补的“负面现象论文”；做低数据 VLA 后训练的人基本都该看。
* **问题与切口**: 这篇工作抓住了一个实践里很常见、但此前没有被充分命名的问题：通用 VLA 在少量演示上做 supervised fine-tuning 之后，往往会变得“锁死”，明明学会了技能，却不再响应新的语言重定向。作者把这种失锁拆成 concept lock-in 和 spatial lock-in 两类，核心贡献不是单纯再给一个微调技巧，而是把“低数据后训练会破坏 steerability”明确成一个可测、可分析、可比较的研究问题。
* **核心方法与证据**: 从摘要与正文摘录看，DeLock 的关键思路是把问题从“引入更多额外监督”转成“保住预训练阶段已有的可转向几何”。文中先设计专门的 benchmark 去系统探测 lock-in，而不是只测已训练指令上的成功率；再分析表征与 denoising dynamics 的失锁特征，并引入 visual encoder weight-drift regularization。摘录未完整展开全部损失项，因此具体机制与权重配比需要回 PDF 核查。
* **正文要点**:
  - 论文明确区分 concept lock-in 与 spatial lock-in，并给出“只会抓训练物体/只会去训练位置”这类失锁现象。
  - 实验目标之一是构造专门 probing benchmark，用来测“能否在新指令下重新转向”，而非只测常规成功率。
  - 作者还尝试从表征变化与 denoising dynamics 两条线解释 lock-in 的形成与缓解。
* **为什么值得跟**:
  - 它把很多人已经遇到但难以量化的问题正式化了，这会直接影响今后 VLA 后训练 benchmark 的设计。
  - 它提醒社区：低数据适配的真正目标不是只把目标任务做对，而是适配后仍然保持可重定向性。
  - Jeannette Bohg 路线在机器人泛化与可操控性上的判断，一向值得优先跟踪。
* **风险 / 保留意见**:
  - HTML 摘录没有完整给出 DeLock 的全部机制，复现时可能会卡在具体实现细节上。
  - 当前结论建立在特定预训练 flow-based VLA 与低数据协议上，对其他底座是否同样成立还不能直接外推。
* **建议先看**: 先看问题定义和 benchmark，因为这篇最重要的不只是方法，而是把“后训练后不听话”变成可测对象。再看表征与去噪分析，判断 DeLock 是真的保住了 steerability，还是只是减缓了过拟合。
* **关键词**: `VLA post-training` `lock-in` `low-data SFT` `steerability` `representation drift`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - weight-drift regularization 具体约束了哪些视觉编码器参数，它与行为克隆损失如何平衡？
  - denoising dynamics 的哪些可观测特征最能区分 concept lock-in 与 spatial lock-in？
  - 与“直接增加更多后训练演示”相比，DeLock 的收益主要来自正则本身还是来自 benchmark 设计更敏感地揭示了问题？
* **上传 PDF 后优先看**:
  - 问题定义与 lock-in benchmark 设计部分。
  - 表征分析与 denoising dynamics 分析部分。
  - 与强基线及更大后训练数据集对比的实验和限制讨论。

### [4]. $M^2$-VLA: Boosting Vision-Language Models for Generalizable Manipulation via Layer Mixture and Meta-Skills [[VIP]] [[HTML]](https://arxiv.org/html/2604.24182) [[PDF]](https://arxiv.org/pdf/2604.24182) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.24182`
* **Authors**: Siyao Xiao, Yuhong Zhang, Zhifang Liu, Zihan Gao, Jingye Zhang, Sinwai Choo, Dake Zhong, Mengzhe Wang, Xiao Lin, Xianfeng Zhou, Jia Jia, Haoqian Wang
* **Author Priority**: Core VIP
* **一句话结论**: 想看“少改 VLM、少忘语义、还能做操控”这一路线，这篇值得排前列。
* **问题与切口**: M²-VLA 的核心主张是：一个泛化能力强的通用 VLM，不该在进入机器人领域后就被端到端细调到遗忘原本语义能力。论文试图把 VLM 直接当作更强的 manipulation backbone，用 Mixture of Layers 从不同层提取对控制真正有用的信息，再用 Meta Skill Module 缩小高层语义理解与低层精细动作之间的落差。它代表的是“保留 VLM 天赋，再补控制接口”而不是“把 VLM 完全改造成控制器”。
* **核心方法与证据**: 方法部分围绕两块展开：MoL 负责从 VLM 多层表征中选择并混合任务关键特征，MSM 负责 meta-skill 检索与动作细化，以缓解模型容量受限下的操控表达问题。证据链包含指令跟随与新物体泛化、标准仿真套件、真实世界实验，以及可视化与消融。摘录还给出一个重要工程信号：参数高效设计使得训练成本明显降低，但具体性能代价需要回 PDF 对照。
* **正文要点**:
  - 作者明确批评主流 VLA 的端到端 fine-tuning 会损害 VLM 原有语义理解并带来灾难性遗忘。
  - MoL 的目标是桥接语义表征与细粒度动作控制，MSM 的目标是引入 meta-skill 检索与动作修正。
  - 证据覆盖泛化任务、标准仿真、真实世界和可解释性分析，而不只是一组单 benchmark 结果。
* **为什么值得跟**:
  - 它正面回应了 VLM 语义能力与机器人控制精度之间的结构性张力。
  - 如果这条路线成立，未来很多 VLA 进展可能来自更聪明的接口设计，而不是更重的全量微调。
  - 参数高效训练让这类方法更容易被普通实验室复现和迭代。
* **风险 / 保留意见**:
  - 从摘录看不清收益究竟主要来自 MoL、MSM，还是来自所选 VLM backbone 本身。
  - 真实世界设置、失败模式和与强基线差距的细节在 HTML 摘录中仍然偏少。
* **建议先看**: 先看方法图和 MoL/MSM 的信息流，因为这篇的价值首先在架构主张。再看 instruction following 与 novel object 泛化实验，判断它是否真的比全量细调更保留语义可泛化性。
* **关键词**: `VLA` `VLM backbone` `Mixture of Layers` `Meta Skill Module` `catastrophic forgetting`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - MoL 混合的是哪些层级特征，权重是静态学习到的还是输入相关的动态选择？
  - MSM 中 meta-skill 的构建与检索机制是什么，它依赖显式技能库还是隐式记忆？
  - 泛化收益更多来自保留 VLM 语义能力，还是来自额外的动作表达与轨迹学习容量？
* **上传 PDF 后优先看**:
  - MoL 与 MSM 的方法细节和信息流设计。
  - instruction-following 与 novel-object generalization 的实验。
  - 可视化、消融，以及真实世界鲁棒性分析。

### [5]. Learning Human-Intention Priors from Large-Scale Human Demonstrations for Robotic Manipulation [[HTML]](https://arxiv.org/html/2604.24681) [[PDF]](https://arxiv.org/pdf/2604.24681) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.24681`
* **Authors**: Yifan Xie, YuAn Wang, Guangyu Chen, Jinkun Liu, Yu Sun, Wenbo Ding
* **Author Priority**: Standard
* **一句话结论**: 这是今天最值得关注的人类视频扩展路线；如果你在找 robot-only 数据之外的 scaling path，应优先看。
* **问题与切口**: 这篇论文试图解决一个很大的问题：人类视频里有大量操作先验，但原始视频同时混着场景理解、人体运动和 embodiment 差异，难以直接拿来学机器人控制。作者一方面重建出 HA-2.2M 这样的大规模 action-language 数据，另一方面提出分层 VLA 框架 MoT-HRA，把操作拆成空间 grounding、人类意图/手部运动建模和 embodiment-specific 动作生成三部分，核心新意是让人类视频能监督机器人策略，而不要求每段数据都带机器人动作。
* **核心方法与证据**: 数据侧，HA-2.2M 来自异构人类视频，经由 hand-centric filtering、spatial reconstruction、temporal segmentation 和 language alignment 重建。模型侧，MoT-HRA 由三个耦合专家组成：人类动作意图专家用 MANO 风格目标监督，精细动作专家用机器人动作监督，二者又与视觉语言专家通过 3D 轨迹目标共同训练。实验覆盖手部动作生成、SimplerEnv 与真实操作，并报告了各组件消融。
* **正文要点**:
  - 论文不仅给模型，还给出 HA-2.2M 这一由人类视频重建的大规模 action-language 数据资产。
  - MoT-HRA 把操作拆成视觉语言、意图建模和 embodiment-specific 动作三个耦合专家。
  - 训练时明确区分人类视频与机器人数据的监督角色，并通过共享目标把两者接起来。
* **为什么值得跟**:
  - 它提供了机器人演示之外更可扩展的数据路径，符合 VLA 长期 scaling 需求。
  - 它强调“人类意图先验”而不是生硬模仿人体轨迹，这比直接做人到机映射更有方法论价值。
  - 它把数据引擎和模型分解一起推进，说明扩展路线不只是多收数据那么简单。
* **风险 / 保留意见**:
  - 整条管线高度依赖视频重建、时间分段和语言对齐质量，噪声传播风险很高。
  - 结论里已承认方法仍有限制，但 HTML 摘录没有展开具体失效场景与域差来源。
* **建议先看**: 先看 HA-2.2M 的构建逻辑，确认数据质量控制做到了什么程度。再看三专家如何共享信息与目标，因为这决定了人类视频先验是否真能落到机器人动作层。
* **关键词**: `human demonstrations` `VLA` `hierarchical policy` `intention prior` `cross-embodiment learning`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
* **读 PDF 先核查**:
  - HA-2.2M 的重建噪声和对齐偏差是如何过滤、评估或抑制的？
  - 三个专家在训练和推理时分别交换哪些中间表示，耦合关系有多强？
  - 在人类先验带来的收益里，有多少来自更好的结构归纳，而不是单纯更多的数据量？
* **上传 PDF 后优先看**:
  - 数据集构建、筛选与语言对齐流程。
  - 分层专家架构与多源监督目标的定义。
  - 各组件消融、真实世界鲁棒性和限制讨论。

### [6]. Betting for Sim-to-Real Performance Evaluation [[HTML]](https://arxiv.org/html/2604.24018) [[PDF]](https://arxiv.org/pdf/2604.24018) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.24018`
* **Authors**: Zaid Mahboob, Yujia Chen, Bowen Weng
* **Author Priority**: Standard
* **一句话结论**: 这不是最炫的机器人模型论文，但它可能是今天最容易被低估的 Sim2Real 评测方法论文。
* **问题与切口**: 这篇论文关心的不是如何把策略迁移到真实世界，而是在真实试验极其昂贵、次数受限时，怎样更准确、更高效地估计机器人在现实中的表现。作者把机器人研究者常做的“先看仿真、再决定要不要上真机”的隐性做法正式化为 betting 视角，用序贯下注机制把仿真信息转成对真实表现估计的帮助。它补的是 sim-to-real 评测层，而不是训练层。
* **核心方法与证据**: 方法上，作者给出一个抽象的序贯 betting algorithm：每一轮在看到新真实样本前，先结合已有仿真样本与历史真实样本决定下注比例；若后续真实结果验证了预测，财富增加，反之减少，而下注为零时就退化为普通 Monte Carlo 估计。论文声称在理论上能给出优于 Monte Carlo 的条件，并在实验里比较 ideal Kelly、half Kelly 与多种 simulator 变体；摘录也强调偏差较大的 simulator 会明显失效。
* **正文要点**:
  - 论文的对象是 performance evaluation，在真实试验预算极少时如何做更可信的估计。
  - 核心机制是用仿真辅助信息动态更新对真实结果的下注权重，而不是直接学习控制策略。
  - 实验与结论都把 Monte Carlo 作为基线，并讨论了 Kelly 类策略和 biased simulator 的表现差异。
* **为什么值得跟**:
  - Sim2Real 的瓶颈不只是迁移本身，很多时候更关键的是如何可信地比较、筛选和认证方法。
  - 它给出了一个能把“对仿真有多信”写进统计估计过程里的正式框架。
  - 对基准评测、系统验证和安全相关部署，这类工作可能比单次 SOTA 更有长期影响。
* **风险 / 保留意见**:
  - 当前摘录非常偏理论，真实机器人实验覆盖范围与外部有效性还需要回 PDF 仔细确认。
  - 方法对 simulator mismatch 很敏感，若仿真偏差严重，下注机制未必带来稳定收益。
* **建议先看**: 先看问题定义和算法框架，确认作者解决的是评测推断而不是策略学习。再看理论假设与 biased simulator 实验，判断这套框架在现实中对 mismatch 的容忍度。
* **关键词**: `Sim2Real` `performance evaluation` `sequential betting` `Monte Carlo` `Kelly criterion`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 下注权重具体依赖哪些仿真统计量，它对校准误差或分布偏移有多敏感？
  - 优于 Monte Carlo 的理论条件是否能覆盖真实机器人里常见的非平稳漂移？
  - 当失败事件稀有且代价极高时，这种估计框架能否仍然保持有效与稳健？
* **上传 PDF 后优先看**:
  - 问题定义、估计器和下注算法的形式化部分。
  - 理论假设、定理条件及其与 Monte Carlo 的比较。
  - biased simulator、收敛行为和早期稳定性相关实验。

## Watchlist

### [W1]. Modular Sensory Stream for Integrating Physical Feedback in Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2604.23272) [[PDF]](https://arxiv.org/pdf/2604.23272)
* **Paper ID**: `2604.23272`
* **Authors**: Jimin Lee, Huiwon Jang, Myungkyu Koo, Jungwoo Park, Jinwoo Shin
* **Author Priority**: Standard
* **为什么还值得留意**: MoSS 进入 shortlist 的理由很充分：它抓住了 VLA 在真实接触任务里最缺的一环，即如何把触觉、力矩等异质物理反馈以可扩展方式接进预训练策略。两阶段训练和多模态物理信号融合也很有工程价值。之所以没有进入最终精选，是因为它更像一条重要增强模块路线，问题范围相对聚焦，且从摘录看主要证据集中在接触丰富的特定真实任务，战略外延不如最终入选的几篇广。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. Characterizing Vision-Language-Action Models across XPUs: Constraints and Acceleration for On-Robot Deployment [[HTML]](https://arxiv.org/html/2604.24447) [[PDF]](https://arxiv.org/pdf/2604.24447)
* **Paper ID**: `2604.24447`
* **Authors**: Kaijun Zhou, Qiwei Chen, Da Peng, Zhiyang Li, Xijun Li, Jinyu Gu
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇是很有价值的部署系统论文：它把 VLA 上机部署从“能不能跑”推进到“在不同 XPU 上以什么成本、能耗和时延跑得最合理”，还提出了训练免费的加速思路。进入 watchlist 是因为它对真实机器人落地很关键。没有进最终精选，主要因为今天的主线更偏模型能力、学习机制与 Sim2Real 评测本体，而这篇更偏硬件共表征与部署优化。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. AsyncShield: A Plug-and-Play Edge Adapter for Asynchronous Cloud-based VLA Navigation [[HTML]](https://arxiv.org/html/2604.24086) [[PDF]](https://arxiv.org/pdf/2604.24086)
* **Paper ID**: `2604.24086`
* **Authors**: Kai Yang, Zedong Chu, Yingnan Guo, Zhengbo Wang, Shichao Xie, Yanfen Shen, Xiaolong Wu, Xing Li, Mu Xu
* **Author Priority**: Standard
* **为什么还值得留意**: AsyncShield 值得保留在 watchlist，因为它把云端 VLA 导航中的异步延迟问题拆成了几何映射、约束优化和 RL 适配三部分，问题定义很清楚，也很贴近实际系统。它没有进最终精选，一是更偏导航与云边部署这一子场景，二是摘录里的证据重点仍是仿真稳健性分析，真实部署说服力从现有材料看还不够强。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

### [W4]. Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines [[HTML]](https://arxiv.org/html/2604.23001) [[PDF]](https://arxiv.org/pdf/2604.23001)
* **Paper ID**: `2604.23001`
* **Authors**: Ziyao Wang, Bingying Wang, Hanrong Zhang, Tingting Du, Tianyang Chen, Guoheng Sun, Yexiao He, Zheyu Shen, Wanghao Ye, Ang Li
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇 survey 之所以进 shortlist，是因为它把 VLA 研究重心从模型架构拉回到 datasets、benchmarks 和 data engines，这对理解领域走向很有用。它没有进最终精选，不是质量问题，而是今天更需要能推动研究前沿判断的原始方法论文；这篇更适合作为背景框架和后续检索地图。
* **证据来源**: arXiv HTML (Introduction)
