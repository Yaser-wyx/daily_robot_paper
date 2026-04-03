# RoboPulse | 2026-04-03

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 68 papers scanned · 10 shortlisted · 6 editor's picks

今天这组最终精选的主线非常清晰：VLA 正在从“直接出动作”转向“把可验证的世界建模、几何先验和闭环评测一起做扎实”，而 RL 侧则在补上长时程、多模态与 sim2real 的数据生成能力。入选论文里，最强的一条线是把 world model / world-action model 做成可用于规划、验证或自我改进的中枢，而不是只做辅助生成；另一条线则是围绕 VLA 微调与评测，把动作分布的物理容忍度和闭环鲁棒性真正纳入训练与基准。VIP 作者里今天最值得优先跟踪的是 Chelsea Finn 参与的 2604.01985，它直接切中 world model 可靠性这个核心瓶颈；扩展名单中 Abhishek Gupta 的 2603.15789 也值得高优先级跟进，因为它代表了大规模 RL 数据生成走向更通用操控的一条强信号。整体看，今天的 shortlist 不只是“模型更大”，而是明显在追求可验证、可闭环、可迁移的 embodied intelligence 训练范式。

## 今日信号

- 今天最值得记住的研究信号是：world model 的下一阶段竞争点不是生成得像不像，而是能否在弱标注和分布外动作下自检、自证并服务下游策略学习。
- 今天最值得记住的研究信号是：驾驶 VLA/WAM 正在快速转向显式几何、专家解耦和闭环评测，说明“语言推理强”本身已经不足以支撑安全关键决策。
- 今天最值得记住的研究信号是：机器人 VLA 与生成式策略优化都在重新拥抱动作空间结构，无论是 feasible action neighborhood 还是 chunk-level posterior，本质上都在减少把物理控制硬离散成单一正确答案的误配。

## Editor's Picks

### [1]. World Action Verifier: Self-Improving World Models via Forward-Inverse Asymmetry [[VIP]] [[HTML]](https://arxiv.org/html/2604.01985) [[PDF]](https://arxiv.org/pdf/2604.01985) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.01985`
* **Authors**: Yuejiang Liu, Fan Feng, Lingjing Kong, Weifeng Lu, Jinzhou Tang, Kun Zhang, Kevin Murphy, Chelsea Finn, Yilun Du
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看；这篇不是单纯再做一个更大的 world model，而是直指“世界模型为什么在差动作和分布外情形下不可靠”这个根因。
* **问题与切口**: 这篇工作试图解决通用 world model 在真实机器人数据稀缺时最棘手的问题：模型往往只在少量已见动作附近可靠，但评估、规划和策略优化需要它对大量次优乃至错误动作也有稳定判断。作者提出 World Action Verifier，把动作条件预测拆成“状态是否可信”和“什么动作能导致该转移”两个更容易学的部分，再据此发现自身预测错误并主动挑选更有信息量的交互数据。相对已有只靠更多动作标注或更大视频预训练的路线，它的创新点在于把 forward-inverse asymmetry 变成可操作的自我改进机制。
* **核心方法与证据**: 从 HTML 可见，方法核心是一个半监督验证框架：在少量动作标注交互数据与大量无动作视频共存的设定下，先把验证问题形式化，再分解为子目标生成、稀疏逆动力学验证和前向世界模型学习，最后耦合成 self-improvement cycle。实验围绕四个问题展开：前向预测与逆动力学谁更容易泛化、稀疏 IDM 是否更抗分布移位、这种 forward-inverse asymmetry 是否真能带来自我提升、以及收益能否转移到下游策略学习。证据边界上，摘录明确覆盖 MiniGrid 与机器人场景，但未给出更细的量化细节，因此强结论应落在机制有效而非具体幅度。
* **正文要点**:
  - 作者明确把问题放在“小规模动作标注数据 + 大规模无动作视频”的半监督 world model 学习设定下。
  - 方法依赖一个循环一致性结构，把多样子目标生成器、稀疏逆动力学模型和前向模型耦合起来筛选更有价值的交互。
  - 实验问题设置强调对未见物体和新交互形式的分布外泛化，而不是只看同分布一步预测。
* **为什么值得跟**:
  - 它把 world model 可靠性问题从“再扩数据”改写成“先验证再扩数据”，更接近可持续自举。
  - 如果逆动力学验证确实比前向预测稳健，这会改变很多 VLA/world model 系统的数据采集优先级。
  - 论文同时检查下游 policy learning，说明它瞄准的是可用性闭环而非单独的生成指标。
* **风险 / 保留意见**:
  - 当前摘录无法判断自我改进循环对复杂高维视觉机器人任务的真实成本与稳定性。
  - 方法高度依赖逆动力学稀疏表示是否真的保留关键因果信息，跨平台泛化仍需谨慎。
* **建议先看**: 先抓住作者的中心论点：为什么 inverse verification 比 forward prediction 更容易、更稳健。然后顺着四个 RQ 看证据链，重点确认这种不对称性是否真的转化成更好的数据选择与下游策略提升。
* **关键词**: `world model` `inverse dynamics` `self-improvement` `semi-supervised verification` `policy learning`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 稀疏逆动力学表示究竟保留了哪些足以支撑验证、但又不必重建完整未来状态的关键信息？
  - self-improvement cycle 中由谁决定“最有信息量的交互”，其选择是否会引入新的采样偏置？
  - 当动作本身高度多模态时，状态可信但动作解释不唯一的情形会如何影响 verifier 的可靠性？
* **上传 PDF 后优先看**:
  - 方法章节中关于 semi-supervised verification 问题定义与分解假设的部分
  - 实验章节里比较 forward prediction 与 sparse/vanilla inverse dynamics 泛化差异的部分
  - 下游策略学习结果与误差案例分析类图表或可视化部分

### [2]. DriveDreamer-Policy: A Geometry-Grounded World-Action Model for Unified Generation and Planning [[HTML]](https://arxiv.org/html/2604.01765) [[PDF]](https://arxiv.org/pdf/2604.01765) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.01765`
* **Authors**: Yang Zhou, Xiaofeng Wang, Hao Shao, Letian Wang, Guosheng Zhao, Jiangnan Shao, Jiagang Zhu, Tingdong Yu, Zheng Zhu, Guan Huang, Steven L. Waslander
* **Author Priority**: Standard
* **一句话结论**: 值得优先看；它把驾驶 WAM 从“会生成未来画面”推进到“用几何支撑统一生成与规划”的更实用形态。
* **问题与切口**: 这篇工作的切口很明确：现有 world-action model 虽然试图连接 VLA 与 world model，但大多停留在 2D 外观或潜变量层面，几何 grounding 不够强，因而难以支撑物理世界中的安全规划。DriveDreamer-Policy 试图把语言理解、深度生成、未来视频生成和动作规划放进一个统一框架里，并让深度成为显式几何脚手架。它的新意不只是多任务共训，而是用几何感知的世界表示同时服务“看见未来”和“决定怎么开”，把世界生成能力从展示型能力拉回规划主链。
* **核心方法与证据**: 从摘录看，模型结构是“大语言模型 + 三个轻量生成专家”的模块化设计：LLM 处理语言指令、多视角图像与动作，再通过紧凑 query interface 驱动深度、未来视频和动作三个生成头。作者强调 depth 作为显式几何支撑，并用解耦的信息流组织方式连接规划与生成。实验在 Navsim 基准上做闭环规划评测，同时单独评估 video/depth 生成质量；闭环指标使用 PDMS 与 EPDMS，说明作者至少试图同时证明规划效果与世界生成质量。证据边界在于摘录没有展开消融与失败模式，所以当前更适合把它判断为结构方向很强、具体收益幅度待查。
* **正文要点**:
  - 论文把 depth generation、future video generation 与 motion planning 放进单一 modular architecture。
  - 作者强调 large language model 只做统一条件建模，具体世界生成与规划由三个 lightweight generators 完成。
  - 实验同时覆盖 Navsim 闭环规划指标与世界生成指标，试图证明几何表示对两端都有价值。
* **为什么值得跟**:
  - 它代表驾驶领域 WAM 的一个清晰方向：世界建模不再是 planner 外挂，而是与动作生成共结构。
  - 把深度作为显式中间几何层，有助于缓解纯 2D VLM/VLA 在遮挡、距离和可通行性上的弱点。
  - 模块化设计比端到端黑盒更利于切换运行模式，也更接近工业系统需要的可解释接口。
* **风险 / 保留意见**:
  - 统一框架可能在任务间产生优化竞争，HTML 摘录不足以判断三头之间是否真正互利而非互相牵制。
  - 驾驶闭环得分提升是否主要来自更强 planner 而非更好的 world generation，目前证据还不够分离。
* **建议先看**: 先看作者如何定义 geometry-grounded world-action model，以及 depth 在信息流中的角色。随后重点核查闭环规划与生成评测是否形成同一条因果链，而不是两个并列任务。
* **关键词**: `world-action model` `autonomous driving` `geometry grounding` `depth generation` `planning`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 深度作为显式几何 scaffold 时，究竟是给 planner 提供约束，还是主要提升视频未来预测的一致性？
  - 三个生成专家共享哪些表示、又在哪些接口被刻意隔离，以避免统一模型退化成任务拼接？
  - 在罕见或安全关键场景里，世界生成质量提升是否真的对应更稳健的动作选择？
* **上传 PDF 后优先看**:
  - 方法章节里 query interface 与 geometry-aware representation 的设计部分
  - 实验章节中闭环 planning 指标与 world generation 指标的对应分析
  - 消融或案例分析中关于 depth scaffold、模块拆分和运行模式切换的部分

### [3]. UniDriveVLA: Unifying Understanding, Perception, and Action Planning for Autonomous Driving [[HTML]](https://arxiv.org/html/2604.02190) [[PDF]](https://arxiv.org/pdf/2604.02190) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.02190`
* **Authors**: Yongkang Li, Lijun Zhou, Sixu Yan, Bencheng Liao, Tianyi Yan, Kaixin Xiong, Long Chen, Hongwei Xie, Bing Wang, Guang Chen, Hangjun Ye, Wenyu Liu, Haiyang Sun, Xinggang Wang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看；它不是继续堆 3D token，而是正面处理驾驶 VLA 里“空间感知和语义推理互相打架”的结构性问题。
* **问题与切口**: UniDriveVLA 针对当前驾驶 VLA 的核心矛盾给出了一种很有代表性的回答：若直接沿用 2D VLM，空间感知不够；若强行塞入 3D 表征，又容易损伤原生推理能力。作者认为问题根源在于共享参数上同时优化 perception 与 reasoning 会产生表征干扰，因此提出把 understanding、perception、action planning 分成不同专家，再控制它们之间的交互。它的价值在于把“统一模型”从单体大模型，改写成可分工但仍端到端协同的 Mixture-of-Transformers 架构。
* **核心方法与证据**: HTML 摘录显示，框架建立在 Qwen3-VL 之上，并采用多阶段训练：先做驾驶预训练，再联合训练整体系统，最后冻结 vision-language 模块去微调感知与动作专家。核心方法包括专门的 Understanding、Perception、Action experts，以及 sparse perception 机制，用较稀疏的空间先验来减轻与语义推理的冲突。证据层面，作者给出了相对完整的训练设置和优化策略，说明这不是概念性工作；但摘录未展开关键消融，因此目前最可信的判断是“架构假设明确且工程路径清楚”，而非已完全证明最优。
* **正文要点**:
  - 论文明确提出 perception-reasoning conflict，认为单体参数共享会导致空间表征与语义推理相互干扰。
  - 架构上采用 Understanding、Perception、Action 三个 expert，并通过受控的 cross-expert interaction 协作。
  - 训练流程分阶段进行，最后冻结 vision-language backbone 再微调感知与动作分支。
* **为什么值得跟**:
  - 它给驾驶 VLA 提供了一条比“单体端到端更大”更可控的扩展路线。
  - 如果稀疏空间先验能减少干扰，类似设计也可能迁移到机器人操控 VLA。
  - 论文把感知、理解、规划统一到同一框架里，但保留了模块职责，便于后续诊断和替换。
* **风险 / 保留意见**:
  - 专家解耦是否真的降低冲突，还是只是增加参数与训练复杂度，仍需看严格消融。
  - 基于特定底座 VLM 的收益可能与 Qwen3-VL 强绑定，跨底座可迁移性暂不明确。
* **建议先看**: 先看作者如何论证 perception-reasoning conflict 成立，再看 expert 之间的信息交换设计是否足够克制。阅读时要重点区分：性能提升来自专家分工，还是来自更重训练配方与数据混合。
* **关键词**: `VLA` `autonomous driving` `Mixture-of-Transformers` `sparse perception` `planning`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
* **读 PDF 先核查**:
  - Understanding、Perception、Action 三个 expert 的边界是语义上的，还是由训练信号与接口硬约束出来的？
  - sparse perception 机制抽取了哪些空间先验，它为什么不会再次侵蚀 VLM 的语义推理能力？
  - 多阶段训练里冻结与解冻的时机是否决定了最终冲突缓解效果？
* **上传 PDF 后优先看**:
  - 方法章节中 Mixture-of-Transformers 与 cross-expert interaction 的设计部分
  - 训练设置与阶段化优化策略的章节
  - 消融实验里关于 expert 拆分、sparse perception 和 backbone 冻结策略的部分

### [4]. Bench2Drive-VL: Benchmarks for Closed-Loop Autonomous Driving with Vision-Language Models [[PDF]](https://arxiv.org/pdf/2604.01259) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.01259`
* **Authors**: Xiaosong Jia, Yuqian Shao, Zhenjie Yang, Qifeng Li, Zhiyuan Zhang, Junchi Yan
* **Author Priority**: Standard
* **一句话结论**: 值得看，但更像“评测基础设施论文”；它的重要性在于把 VLM4AD 从静态问答拉回闭环驾驶，而不是提出新的主模型。
* **问题与切口**: 从仅有的摘要信息看，Bench2Drive-VL 的目标非常直接：现有 VLM4AD 基准大多还是静态问答式 open-loop 评测，难以暴露累计误差和分布外状态下的真实驾驶问题，因此作者把闭环评测正式引入 VLM 驾驶。它作为 Bench2Drive 的扩展，核心价值不在于单一算法提升，而在于重构“什么算可靠的 VLM 驾驶评估”。如果这个基准设计得当，它会对后续 VLA/VLM 驾驶工作形成更高门槛，因为很多靠文本理解刷分的方法在闭环里未必站得住。
* **核心方法与证据**: 证据严格受限于摘要。可以确认的是，论文至少提出了一个名为 DriveCommenter 的闭环生成器，用于自动生成更具分歧性或更贴近驾驶过程的评测内容，并将闭环机制接入 Bench2Drive。摘要明确指出其动机是覆盖人类采集数据中较少出现的分布外状态，这与闭环评价的核心痛点一致。但由于缺少 HTML 正文，我们无法判断任务构成、场景覆盖、指标设计、自动生成文本的质量控制与 benchmark 统计规模，因此对其结论应保持保守，只能判断其问题定义非常重要。
* **正文要点**:
  - 摘要明确批评现有 VLM4AD benchmark 主要停留在 static QA 的 open-loop 评测。
  - 论文把 closed-loop evaluation 引入 Bench2Drive，目标是暴露累计误差与分布外输入下的性能。
  - 已知组件里包括一个名为 DriveCommenter 的闭环生成器，但具体机制在现有材料中证据不足。
* **为什么值得跟**:
  - 没有可靠闭环基准，驾驶 VLA/VLM 的方法比较很容易被开放环节中的代理指标误导。
  - 它抓住了驾驶系统真正难点：模型一旦偏离演示分布，后续状态会越来越不像训练集。
  - 如果 benchmark 设计足够强，它会直接改变后续论文呈现结果的方式与说服标准。
* **风险 / 保留意见**:
  - 目前只有摘要回退信息，无法判断 benchmark 是否真的覆盖了关键长尾场景与安全失效模式。
  - 自动化生成评测内容若控制不严，可能带来文本偏差或评价目标错位。
* **建议先看**: 上传 PDF 后先不要急着看排行榜，优先核查 benchmark 构造原则、闭环协议和自动生成文本的质量控制。当前材料不足以支持对其结论强背书，更适合把它当作高潜力评测基础设施。
* **关键词**: `closed-loop benchmark` `VLM4AD` `autonomous driving` `evaluation` `distribution shift`
* **证据来源**: Abstract fallback
* **读 PDF 先核查**:
  - DriveCommenter 具体生成什么类型的闭环文本或场景干预，它如何避免把 benchmark 变成 prompt engineering 测试？
  - 闭环协议如何定义成功、失败与安全事件，是否能与已有 Bench2Drive 结果可比？
  - 基准是否区分模型的场景理解缺陷与控制执行缺陷，避免把所有问题混为单一分数？
* **上传 PDF 后优先看**:
  - benchmark 构建与 closed-loop evaluation protocol 章节
  - 自动生成器 DriveCommenter 的设计与质量控制章节
  - 指标定义、场景分布和基线结果汇总类章节或表格

### [5]. Boosting Vision-Language-Action Finetuning with Feasible Action Neighborhood Prior [[HTML]](https://arxiv.org/html/2604.01570) [[PDF]](https://arxiv.org/pdf/2604.01570) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.01570`
* **Authors**: Haochen Niu, Kanyu Zhang, Shuyu Yin, Qinghai Guo, Peilin Liu, Fei Wen
* **Author Priority**: Standard
* **一句话结论**: 值得优先看；它抓住了 VLA 微调里一个长期被忽略但极实际的问题：物理动作通常不是“唯一正确答案”。
* **问题与切口**: 这篇论文关注 VLA 微调阶段的一个根本失配：很多现有做法沿用语言模型式目标，把每个状态映射到单一正确动作 token，但真实操控里往往存在一片近似等价、都能推动任务进展的 feasible action neighborhood。作者提出 FAN-guided regularizer，希望把策略输出分布塑造成更符合该邻域几何的形态，而不是学成尖锐、脆弱的单峰分布。相对常规 SFT 或 RFT，这项工作的真正新意在于把“动作容忍度”显式变成正则化对象，直接服务样本效率与 OOD 泛化。
* **核心方法与证据**: 摘录显示，方法核心是给动作分布引入一个高斯型先验，使模型在训练时朝着更平滑、更符合 FAN 几何的分布靠拢，并且该正则既能接到 supervised finetuning，也能接到 reinforcement finetuning。实验覆盖 OpenVLA 与 OpenVLA-OFT 两类代表性 VLA，分别对应单动作与 action chunk 输出；任务上覆盖 ManiSkill 与 LIBERO，并明确评估绝对性能、OOD 泛化、样本效率和收敛速度。作者还强调标准方法会产生 spiky policy distribution，这为方法动机提供了较强证据链。
* **正文要点**:
  - 论文把状态对应一组近似等价可行动作的性质定义为 feasible action neighborhood，并将其视为 VLA 微调应显式利用的结构。
  - 所提正则同时适用于 SFT 与 RFT，而不是只服务某一种后训练范式。
  - 实验不仅看平均成功率，还专门看扰动下鲁棒性、样本效率和收敛速度。
* **为什么值得跟**:
  - 它提醒我们不要把语言离散监督目标原封不动移植到连续物理控制。
  - 如果动作邻域先验有效，很多 VLA 微调的泛化问题可能来自目标函数而非模型容量不足。
  - 该思路对 action chunk 模型尤其相关，因为时序动作本来就存在更强的等价路径空间。
* **风险 / 保留意见**:
  - 用高斯先验逼近 FAN 可能过于简化，真实可行动作集合未必局部各向同性。
  - 当前证据主要来自特定 benchmark 与两类 VLA，跨机器人本体和复杂接触任务的普适性待验证。
* **建议先看**: 先看作者如何实证证明标准 VLA 微调会学出 spiky distribution，这是整篇论文是否站得住的关键。随后重点核查 FAN 正则在 SFT 与 RFT 下是否真的共享同一机制，而不是两个经验技巧。
* **关键词**: `VLA finetuning` `feasible action neighborhood` `regularization` `OOD generalization` `robot manipulation`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
* **读 PDF 先核查**:
  - FAN 在实验中是被显式估计、局部近似，还是仅通过目标分布形状间接编码？
  - 高斯先验对多模态或非凸动作可行域是否会带来错误平滑，进而压制关键策略分支？
  - 在 OpenVLA-OFT 这类 chunk policy 中，FAN 是对单步动作还是对整段动作联合建模的？
* **上传 PDF 后优先看**:
  - 方法章节中 FAN 定义、目标分布构造与正则项推导的部分
  - 实验章节里 spiky policy distribution 的诊断与可视化部分
  - SFT/RFT、单步动作与 action chunk 两类设定的对比消融部分

### [6]. Emergent Dexterity via Diverse Resets and Large-Scale Reinforcement Learning [[HTML]](https://arxiv.org/html/2603.15789) [[PDF]](https://arxiv.org/pdf/2603.15789) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.15789`
* **Authors**: Patrick Yin, Tyler Westenbroek, Zhengyu Zhang, Joshua Tran, Ignacio Dagnino, Eeshani Shilamkar, Numfor Mbiziwo-Tiapo, Simran Bagaria, Xinlei Liu, Galen Mullins, Andrey Kolobov, Abhishek Gupta
* **Author Priority**: Standard
* **一句话结论**: 值得高优先级看；它代表了一条很强的 RL for sim2real 方向：先把 reset 分布做对，再让大规模 on-policy RL 真正吃到更广状态空间。
* **问题与切口**: OmniReset 试图解决当前大规模模拟 RL 在操控任务上经常遇到的两个老问题：一是高度依赖任务特定奖励、课程和演示工程，二是即便算力加大，训练也容易反复访问狭窄状态区域而很快饱和。作者提出的核心思路并不花哨，而是用多样但最小结构化的 reset states 配合大批量 on-policy RL，让策略持续接触更丰富的接触态与中间态，从而在长时程、接触密集操控中涌现更复杂的灵巧行为。它的重要性在于把“数据生成机制”而不是“更复杂算法”推到主位。
* **核心方法与证据**: 从摘录可见，实验问题围绕三个层面：是否优于基线、关键设计选择是否重要、以及学到的 RL policy 能否进一步生成适合 sim2real 的多样数据。任务覆盖拧桌腿、抽屉插入、peg insertion、cube stacking、wall slide、cupcake placement 等多类操控，明显强调长时程与接触复杂性。结论部分进一步表明作者不仅关注 simulation asymptotic performance，也关注 learned policies 能否直接迁移到现实世界。证据边界在于目前 HTML 摘录没有展示 reset 生成机制的细粒度算法与真实部署细节，因此最稳妥的判断是“范式很强、实现细节待查”。
* **正文要点**:
  - 论文的核心主张是：多样 reset 状态与大批量 on-policy RL 的结合，能显著扩展训练访问到的状态空间。
  - 实验任务覆盖多种接触密集、长时程操控，而不局限于单一装配或抓取模板。
  - 作者明确把 learned RL policies 视为 sim-to-real 数据生成器，而不只是单任务终端策略。
* **为什么值得跟**:
  - 它为 sim2real 提供了一条更接近可扩展数据引擎的路线，而不是每个任务都重新做奖励与课程设计。
  - 如果 reset 分布设计真是瓶颈，那么很多 RL 操控方法的计算饱和问题有了更直接的解释。
  - 这条线与 VLA 并不冲突，反而可能成为未来大规模机器人后训练或数据合成的重要来源。
* **风险 / 保留意见**:
  - reset 分布虽被称为 minimally structured，但真实落地时可能仍包含相当多任务先验。
  - 从仿真到现实的成功是否依赖特定物体、控制器和观测设置，目前摘录不足以判断。
* **建议先看**: 先看 Section 3.3 一类位置里作者对 reset 设计原则的界定，因为那决定了方法到底有多“通用”。然后重点核查仿真表现提升与真实迁移成功之间是否存在清晰的中间证据链。
* **关键词**: `reinforcement learning` `sim2real` `data generation` `reset distribution` `dexterous manipulation`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
* **读 PDF 先核查**:
  - OmniReset 中“diverse resets”是如何生成和筛选的，它们到底包含多少任务特定结构？
  - 性能提升主要来自更广状态覆盖，还是来自更容易的 credit assignment 与探索起点？
  - 用于 sim2real transfer 的数据生成策略是否真的比直接行为克隆或专家示范更具多样性和鲁棒性？
* **上传 PDF 后优先看**:
  - 方法章节中 reset state 设计原则与数据生成流程的部分
  - 实验章节里关键设计决策消融和样本复杂度对比部分
  - 真实机器人迁移设置、成功案例与失败分析类章节或图表

## Watchlist

### [W1]. AnchorVLA: Anchored Diffusion for Efficient End-to-End Mobile Manipulation [[HTML]](https://arxiv.org/html/2604.01567) [[PDF]](https://arxiv.org/pdf/2604.01567)
* **Paper ID**: `2604.01567`
* **Authors**: Jia Syuen Lim, Zhizhen Zhang, Peter Bohm, Brendan Tidd, Zi Huang, Yadan Luo
* **Author Priority**: Standard
* **为什么还值得留意**: AnchorVLA 进入 shortlist 的原因很充分：它把移动操作里“多峰动作分布”和“控制时延”这对经典矛盾处理得很具体，用 anchor-guided diffusion、截断去噪和残差修正去平衡多样性与实时性，而且还给了真实四足移动操作部署信号。之所以没进最终精选，是因为它更像高质量系统工程整合，研究外延主要集中在推理效率与执行稳健性折中；相较今天入选的 world model / WAM / RL 主线，它的范式推进力度稍弱一些。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. Causal Scene Narration with Runtime Safety Supervision for Vision-Language-Action Driving [[HTML]](https://arxiv.org/html/2604.01723) [[PDF]](https://arxiv.org/pdf/2604.01723)
* **Paper ID**: `2604.01723`
* **Authors**: Yun Li, Yidu Zhang, Simon Thompson, Ehsan Javanmardi, Manabu Tsukada
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇值得关注，因为它提示了一个常被低估的事实：VLA 驾驶中的文本组织形式本身就是控制性能变量，因果化叙述和运行时安全监督可能比单纯追加更多文本更有效。它没有进最终精选，主要是因为当前贡献更偏输入重构与安全包络层，而不是对世界建模、动作建模或统一架构的根本推进；另外其效果有多大程度依赖具体 LMDrive 设定，仍需要更强外部验证。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

### [W3]. UAV-Track VLA: Embodied Aerial Tracking via Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2604.02241) [[PDF]](https://arxiv.org/pdf/2604.02241)
* **Paper ID**: `2604.02241`
* **Authors**: Qiyao Zhang, Shuhua Zheng, Jianli Sun, Chengxiang Li, Xianke Wu, Zihan Song, Zhiyong Cui, Yisheng Lv, Yonglin Tian
* **Author Priority**: Standard
* **为什么还值得留意**: UAV-Track VLA 有两个亮点：一是把 embodied aerial tracking 明确做成 VLA 问题，二是同时带来了大规模数据集/基准和双分支解码架构，方向上很新。没有进入最终精选，主要因为它的主战场是无人机跟踪这一更垂直的子领域，和今天围绕通用 VLA、world model、sim2real 操控的主线相比外延稍窄；现有摘录也不足以判断其方法贡献与 benchmark 贡献各自占比。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

### [W4]. Posterior Optimization with Clipped Objective for Bridging Efficiency and Stability in Generative Policy Learning [[HTML]](https://arxiv.org/html/2604.01860) [[PDF]](https://arxiv.org/pdf/2604.01860)
* **Paper ID**: `2604.01860`
* **Authors**: Yuhui Chen, Haoran Li, Zhennan Jiang, Yuxing Qin, Yuxuan Wan, Weiheng Liu, Dongbin Zhao
* **Author Priority**: Standard
* **为什么还值得留意**: POCO 值得留在 watchlist，因为它正面解决生成式策略在 temporal action chunk 场景下做 RL 微调时的稳定性与效率矛盾，posterior inference 视角也和今天的 VLA/RL 融合主题高度相关。它没进最终精选，是因为从当前摘录看，方法更偏 generative policy learning 的优化框架，而非直接推动 VLA/world model 主线；另外真实收益有多大程度来自 clipped objective、chunk critic 或 offline-to-online 配方，还需要读完整正文拆开验证。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
