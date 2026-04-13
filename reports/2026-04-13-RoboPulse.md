# RoboPulse | 2026-04-13

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 59 papers scanned · 10 shortlisted · 5 editor's picks

今天这组 shortlist 的主线很清晰：一边是在为 VLA 和机器人基础模型补数据，另一边是在把 world model 从“会生成/会拟合”推向“可迁移、可用于控制、可用于经验重用”。最终精选的五篇分别覆盖了可形变体 sim2real 数据引擎、视频-动作联合生成、闭环 agentic 数据合成、形态条件化 world model，以及基于 world model 的经验迁移 RL，代表了当前从“数据规模”转向“数据有效性与可执行性”的关键分叉。它们入选，不只是因为方向热门，更因为正文摘录里都明确给出了方法闭环、实验问题设置和相对现有路线的针对性修补。作者跟踪上，今天最值得优先盯住的是核心名单中的 Jiangmiao Pang；同时 WOMBET 文中引用链条与 Levine/Abbeel 系 RL 脉络高度相关，后续若有同系延展也值得继续追。

## 今日信号

- 今天最值得记住的研究信号是：机器人数据生成正在从“只生成视觉内容”转向“同时保证动作对齐、物理可行和任务闭环验证”的全链路合成。
- 今天最值得记住的研究信号是：world model 的研究重点正在从单一机体或单任务拟合，转向通过形态条件、显式结构信息或不确定性约束来提升跨硬件与跨任务可迁移性。
- 今天最值得记住的研究信号是：VLA 训练瓶颈不再只是数据量不足，而是如何把模拟器、生成模型与后验筛选机制组合成更可靠的“高价值数据放大器”。

## Editor's Picks

### [1]. SIM1: Physics-Aligned Simulator as Zero-Shot Data Scaler in Deformable Worlds [[VIP]] [[HTML]](https://arxiv.org/html/2604.08544) [[PDF]](https://arxiv.org/pdf/2604.08544) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.08544`
* **Authors**: Yunsong Zhou, Hangxu Liu, Xuekun Jiang, Xing Shen, Yuanzhen Zhou, Hui Wang, Baole Fang, Yang Tian, Mulin Yu, Qiaojun Yu, Li Ma, Hengjie Li, Hanqing Wang, Jia Zeng, Jiangmiao Pang
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，它把“可形变体仿真不可信”这个老问题，改写成了一个几何、动力学、动作三者同时对齐的数据引擎问题。
* **问题与切口**: 这篇工作面向服装等可形变物体操作中最现实的痛点：真实数据极贵，而传统 sim2real 又常被刚体假设、软体动力学失真和不合适的运动原语拖垮。SIM1 的核心切口不是单做更强的策略，而是提出一个 physics-aligned 的 real-to-sim-to-real 数据引擎，把有限真实示教转成可扩展的“近真实等价”合成训练基底。相对已有单向仿真或重建路线，它强调场景几何、软体动力学与动作生成三环联动，目标是让纯仿真训练也能支撑服装折叠这类零样本 real deployment。
* **核心方法与证据**: 从摘录看，方法主干分三段。第一段是 SIM1-Scene，把高精度扫描得到的服装网格、URDF 与环境资产变成 metric-accurate 数字场景，先压缩几何偏差。第二段是在对齐后的模拟器里，用 deformation-stabilized solver 和参数校准基础设施复现更稳定的软体交互动力学。第三段再把遥操作示教分解成运动片段，用 diffusion 做动作合成，并叠加视觉随机化扩增训练集。实验围绕三个问题展开：纯仿真训练能否逼近真实数据训练、仿真多样性是否提升跨域鲁棒性、以及合成数据扩展是否比真实采集更高效；但摘录未给出完整数值，所以对幅度判断应保守。
* **正文要点**:
  - 方法明确采用 R2S2R 范式，而不是单向 sim-to-real，作者把它定义为同时桥接几何、动力学与动作的非对称闭环。
  - 实验协议给出真实与仿真两套采集链路：真实端使用双臂平台与 kinesthetic teaching，并记录了 1,000 条真实轨迹。
  - 结论主张纯合成数据训练的策略可实现服装折叠 zero-shot sim-to-real，且与真实数据基线相当；这一点目前只能按作者摘要级证据保守接受。
* **为什么值得跟**:
  - 如果结论成立，它说明可形变体操作的数据扩展不必再完全依赖昂贵真人示教。
  - 它把 sim2real 失败原因从“仿真天然不行”改写为“仿真没有被真实世界充分校准”。
  - 对 VLA 或更大规模机器人策略而言，这类引擎可能成为服装、布料等长尾场景的数据前端。
* **风险 / 保留意见**:
  - 摘录强调对齐成功，但没有展开校准成本、扫描门槛和场景迁移代价，工程复用性仍需核查。
  - 当前亮点集中在 garment folding，是否能外推到拓扑变化更剧烈的可形变任务，正文证据还不够。
* **建议先看**: 先抓住作者如何把“几何对齐、动力学校准、动作扩增”串成一个数据引擎，再看实验三问是否真的支撑“纯仿真≈真实训练”这一定性结论。上传 PDF 后优先检查场景构建与 solver 校准部分，以及 scaling 实验的增益曲线。
* **关键词**: `Sim2Real` `deformable manipulation` `synthetic data scaling` `physics-aligned simulation` `garment folding`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - SIM1 的参数校准具体依赖哪些真实观测信号，才能让软体动力学不只是视觉上相似？
  - 运动片段分解与 diffusion 合成是否会破坏长时序接触一致性，尤其在折叠中间态？
  - 所谓 synthetic scaling 更高效，是否建立在固定真实种子数据量下，还是也隐含了更高的前期建模成本？
* **上传 PDF 后优先看**:
  - 方法章节中关于场景数字化与 metric alignment 的部分
  - 方法/实验章节中关于软体求解器与物理参数校准的消融或对照实验
  - 实验章节中比较纯仿真训练、真实训练与跨域泛化的数据规模曲线

### [2]. VAG: Dual-Stream Video-Action Generation for Embodied Data Synthesis [[HTML]](https://arxiv.org/html/2604.09330) [[PDF]](https://arxiv.org/pdf/2604.09330) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.09330`
* **Authors**: Xiaolei Lang, Yang Wang, Yukun Zhou, Chaojun Ni, Kerui Li, Jiagang Zhu, Tianze Liu, Jiajun Lv, Xingxing Zuo, Yun Ye, Guan Huang, Xiaofeng Wang, Zheng Zhu
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它抓住了 embodied 生成里最关键但最常被回避的问题：只有视频没有动作，根本不够训练策略。
* **问题与切口**: VAG 试图解决一个近来很尖锐的缺口：world model 很会生成视频，但难直接服务 policy learning，因为缺少与视频严格配对的动作轨迹；而已有 world-action 路线又常在视频与动作对齐上不够强，两阶段方案还会叠加误差。该文提出 dual-stream video-action generation，把视频流和动作流放进统一生成框架里同步建模。新意不只是“联合输出两种模态”，而是把对齐本身当作生成机制的一部分处理，希望直接产出能被策略学习消费的数据对。
* **核心方法与证据**: 摘录显示方法建立在 flow matching 上，并在此基础上提出 unified dual-stream 结构。作者强调 synchronized denoising，即视频与动作在同一生成过程中同步去噪，而不是先出视频再补动作。训练数据是 embodied video-action pairs，实验覆盖 AgiBot、LIBERO 和自采数据，说明它既在大规模真实操作数据上评估，也在标准基准上做验证。实现层面，文中给出了视频模型来自 Cosmos-Predict2 的后训练设置，以及生成时长、分辨率和推理步数等细节，这至少说明系统不是纯概念验证。但从现有摘录无法确认其相较两阶段方法的具体增益大小与失败模式。
* **正文要点**:
  - 作者将现有方法分成只生成视频的 WM、带动作但对齐不足的 WA，以及会引入累积误差的两阶段方案，并将 VAG 定位为对三者缺陷的统一回应。
  - 方法核心是基于 flow matching 的双流统一生成，并强调视频流与动作流在去噪过程中的同步性。
  - 实验覆盖一个百万轨迹级真实机器人数据集、LIBERO 与自采数据，说明其证据意图同时指向规模性与可迁移性。
* **为什么值得跟**:
  - 如果视频和动作能稳定共生成，合成数据对 VLA 或策略模型的价值会明显高于纯视频扩增。
  - 它为 World Model 与 World Action Model 之间的接口问题提供了更直接的技术答案。
  - 在大规模机器人数据昂贵的前提下，这类模型可能成为新任务冷启动的重要数据来源。
* **风险 / 保留意见**:
  - 当前摘录没有展开视频真实性与动作可执行性之间的冲突如何被量化，联合生成未必天然保证可控制性。
  - 模型依赖强生成骨干后训练，训练成本与数据质量门槛可能较高，落地复制难度不低。
* **建议先看**: 先看作者怎样形式化 video-action 对齐，以及 synchronized denoising 究竟是结构耦合还是训练约束；再看实验里是否真正证明联合生成优于视频先行或两阶段路线。上传 PDF 后重点核查对齐质量评估与下游 policy learning 受益证据。
* **关键词**: `video-action generation` `World Action Model` `flow matching` `synthetic data` `embodied learning`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 双流同步去噪中，动作流对视频流是对称耦合还是更多扮演条件分支角色？
  - VAG 生成的数据是直接用于行为克隆/策略训练，还是还需要额外过滤与重标注？
  - 在长时序生成中，视频逼真度提升是否会牺牲动作轨迹的稳定性或可执行性？
* **上传 PDF 后优先看**:
  - 方法章节中 dual-stream 结构与 synchronized denoising 的定义
  - 实验章节中与 WM、WA 或两阶段基线的对比设置
  - 实验章节中使用生成数据训练策略的有效性分析

### [3]. Toward Hardware-Agnostic Quadrupedal World Models via Morphology Conditioning [[HTML]](https://arxiv.org/html/2604.08780) [[PDF]](https://arxiv.org/pdf/2604.08780) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.08780`
* **Authors**: Mohamad H. Danesh, Chenhao Li, Amin Abyaneh, Anas Houssaini, Kirsty Ellis, Glen Berseth, Marco Hutter, Hsiu-Chin Lin
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把 world model 从“绑死某一台四足”推进到“显式读懂机体形态后跨硬件工作”的更一般设定。
* **问题与切口**: 这篇论文瞄准 world model 在机器人里一个长期但常被低估的局限：模型往往只对训练时那一台机器人有效，换电机、换腿长、换整机尺寸就要重训。作者提出 QWM，希望让四足 world model 从 hardware-locked specialist 变成 morphology-conditioned generalist。核心切口是把机器人静态物理结构显式输入模型，而不是让模型从交互历史里隐式猜。相较常见只在状态空间里做泛化的路线，它更强调“机体结构是应被建模的一等输入”，这对异构机器人群体尤其关键。
* **核心方法与证据**: 方法上，QWM 基于 DreamerV3 改造了编码器和转移动力学，并额外引入三个部件：从 USD 文件抽取尺度归一化结构特征的 Physical Morphology Encoder、把静态结构与动态本体感觉融合的 morphology-conditioned WM，以及用于跨硬件稳定学习的 Adaptive Reward Normalization。实验设计围绕三问：单一权重能否在异构四足群体上统一学成、能否对未见机器人实现零样本泛化、能否转到真实硬件。作者明确宣称对 Unitree Go1 和 ANYmal-D 做了 real-world zero-shot transfer，但摘录未提供任务难度与量化成功幅度，因此对泛化强度的判断应保持谨慎。
* **正文要点**:
  - 作者把 morphology 视为可从 USD 确定性提取的显式物理描述，而不是需要从历史交互中隐式恢复的潜变量。
  - QWM 的增量设计集中在 PME、形态条件化世界模型和 ARN 三个模块，并附带相关消融。
  - 实验问题设置直接覆盖统一训练、未见机体零样本泛化与真实机器人迁移，目标非常明确。
* **为什么值得跟**:
  - 这类方法若有效，可显著降低多机型机器人重复训练 world model 的成本。
  - 它为“同一控制智能服务异构硬件群”提供了比单纯 domain randomization 更结构化的路径。
  - 对具身基础模型而言，显式形态条件可能是跨 embodiment 泛化的重要接口。
* **风险 / 保留意见**:
  - 当前范围聚焦四足 locomotion，结论未必直接外推到操作机器人或接触更复杂的任务。
  - 依赖 USD 中可解析的结构信息，意味着真实系统建模质量会直接影响 world model 泛化表现。
* **建议先看**: 先读清楚 PME 提取了哪些尺度无关物理特征，以及这些特征如何进入 latent dynamics；再看零样本未见机体与真实转移实验，判断它到底学到的是共性动力学还是更强的结构先验。
* **关键词**: `world model` `morphology conditioning` `quadruped locomotion` `DreamerV3` `zero-shot transfer`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - PME 抽取的结构特征中，哪些对跨机体泛化最关键，哪些只是辅助归一化？
  - ARN 解决的是回报尺度差异还是更深层的优化不稳定问题，它与 morphology conditioning 是否强耦合？
  - 在未见机器人上成功，是因为形态插值有效，还是模型也能承受明显的形态外推？
* **上传 PDF 后优先看**:
  - 方法章节中 USD 到 morphology feature 的构造细节
  - 实验章节中异构机器人统一训练与未见机体零样本结果
  - 附录或消融章节中 PME、ARN 与显式条件注入的贡献分析

### [4]. WOMBET: World Model-based Experience Transfer for Robust and Sample-efficient Reinforcement Learning [[HTML]](https://arxiv.org/html/2604.08958) [[PDF]](https://arxiv.org/pdf/2604.08958) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.08958`
* **Authors**: Mintae Kim, Koushil Sreenath
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它不是把离线数据当既定资源，而是直接问：能否先用 world model 生成更可靠的可迁移经验，再做 offline-to-online RL。
* **问题与切口**: WOMBET 处理的是机器人 RL 里一个很实际的问题：目标任务在线交互太贵、太危险，大家希望从源任务转移经验，但现有 offline-to-online RL 往往默认离线数据集已经给定，很少讨论这些“可迁移经验”本身如何构造。作者提出 World Model-based Experience Transfer，把世界模型学在源任务上，再通过带不确定性惩罚的规划生成候选轨迹，并筛出高回报、低认知不确定性的经验，用于目标任务的在线微调。它的新意在于把“经验生成”和“经验利用”合成一个框架，而不是把数据质量问题留在系统外部。
* **核心方法与证据**: 从摘录可见，方法链条较完整：先在源任务学 world model，再用 uncertainty-penalized MPC 做保守数据生成，然后基于回报和 epistemic uncertainty 双标准过滤轨迹，最后在目标任务中用 offline 与 online 数据的 adaptive sampling 进行微调。理论上，作者声称不确定性惩罚目标给出真实回报下界，并推导了包含分布失配与近似误差的有限样本误差分解。实验在多个 MuJoCo 连续控制基准上考察样本效率、是否需要 fine-tuning、相对 offline-to-online 基线的优势，以及过滤与自适应采样的组件贡献。由于摘录没有给出具体任务迁移跨度与数值幅度，当前更适合把它看成方法论上很扎实的一篇。
* **正文要点**:
  - WOMBET 的关键区别在于不假设固定离线数据集，而是用 source-task world model 主动构造 transferable experience。
  - 作者使用高回报与低 epistemic uncertainty 的双重过滤，而不是只靠模型预测回报挑轨迹。
  - 在线阶段采用 offline/online 自适应采样，强调从先验驱动初始化平稳过渡到目标任务适应。
* **为什么值得跟**:
  - 它把经验迁移问题从“拿到什么数据就用什么”提升为“如何生成更可靠的迁移数据”。
  - 对高成本机器人 RL 来说，这类保守的数据合成逻辑比纯在线探索更接近实际部署需求。
  - world model 在这里不只是做 imagined rollouts，而是直接决定离线经验库的质量上界。
* **风险 / 保留意见**:
  - 证据来自 MuJoCo 连续控制，离真实机器人接触、感知噪声和安全约束仍有距离。
  - 理论保证依赖不确定性估计质量，若 epistemic uncertainty 校准不足，生成经验可能仍带偏差。
* **建议先看**: 先沿着“源任务 world model 生成经验 -> 双标准过滤 -> 目标任务自适应微调”这条主线读，判断每一步是否真的减少了错误经验传递。随后再看理论部分，确认下界和误差分解是否与算法设计紧密对应。
* **关键词**: `offline-to-online RL` `world model` `experience transfer` `uncertainty-aware planning` `sample efficiency`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 双标准过滤中，高回报与低不确定性的权衡是固定阈值还是随任务自适应？
  - source-target 分布差异较大时，world model 生成的经验是否会系统性偏向源任务动力学？
  - adaptive sampling 在训练后期如何避免过度依赖低质量离线数据或过早丢弃有用先验？
* **上传 PDF 后优先看**:
  - 方法章节中 uncertainty-penalized planning 与 trajectory filtering 的定义
  - 理论章节中 lower bound 与 finite-sample error decomposition
  - 实验章节中 component ablation 与 source-to-target transfer 设置

### [5]. V-CAGE: Vision-Closed-Loop Agentic Generation Engine for Robotic Manipulation [[HTML]](https://arxiv.org/html/2604.09036) [[PDF]](https://arxiv.org/pdf/2604.09036) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.09036`
* **Authors**: Yaru Liu, Ao-bo Wang, Nanyang Ye
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把自动化数据合成从脚本流水线推进到带视觉验收的 agentic 闭环，更贴近长时程操作数据真正需要的“可执行性筛选”。
* **问题与切口**: V-CAGE 关注的是 VLA 扩展中一个经常被低估的现实约束：你不只是需要很多合成场景，而是需要语义上连贯、物理上可达、长时程里不早早崩掉的数据。作者提出一个 vision-closed-loop agentic generation engine，不再依赖传统 scripted pipeline，而是让 foundation models 参与任务场景配置、执行与验收。相对已有场景生成方法，它的关键新意在于把 VLM 从“在线规划器”改造成“数据生成环中的自动验证器”，并通过闭环拒绝采样切断错误轨迹继续污染数据集。
* **核心方法与证据**: 方法摘录里最核心的两点是 IGSC 与 VLM-based closed-loop verification。IGSC 用于构建更物理可行的复杂场景，目标是减少几何冲突与不可达目标；随后 OpenClaw agent 执行高层语义计划，VLM 依据视觉成功标准对轨迹做自动验收，把数据验证变成 VLM 引导的 rejection sampling。实验分三部分：一是合成数据训练 VLA 做长时程复杂任务，二是视频压缩策略是否保留关键视觉语义，三是 IGSC 与闭环验证对数据纯度和物理可行性的贡献。文中给出四个长时程任务、每任务 100 条专家轨迹，但当前摘录不足以判断其对现有自动数据管线的绝对领先幅度。
* **正文要点**:
  - 作者明确把 VLM 从推理期 planner/controller 角色转为数据生成期 verifier，用于轨迹拒绝采样。
  - 实验任务聚焦多步长时程操作而非简单抓取，说明该框架重点解决的是复杂链式失败传播。
  - 每个任务生成 100 条带纹理和光照随机化的专家轨迹，显示其目标是合成可训练的 VLA 数据集而非单次成功案例。
* **为什么值得跟**:
  - 对长时程操作来说，数据质量往往比数据量更关键，闭环验证正好击中这一点。
  - 它代表了一种更 agentic 的数据工厂思路：模型不仅生成数据，还参与环境搭建与质量审查。
  - 如果验证器足够可靠，这类框架能减少长链任务中错误示教被大规模放大的风险。
* **风险 / 保留意见**:
  - VLM 充当验证器的可靠性本身需要证据，若视觉判定与真实任务成功不一致，可能引入系统性筛选偏差。
  - 当前任务数和每任务轨迹规模看起来仍偏有限，是否足以支撑大规模 VLA 扩展还需进一步核查。
* **建议先看**: 先看 IGSC 如何定义并消除几何/可达性冲突，再看 VLM rejection sampling 如何决定轨迹去留；最后对照长时程任务实验，判断闭环筛选是否真带来更干净的数据分布。
* **关键词**: `VLA` `agentic data synthesis` `closed-loop verification` `long-horizon manipulation` `scene generation`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - VLM 验证标准如何避免只看最终画面正确，却忽略中间步骤中的非法交互或潜在碰撞？
  - IGSC 生成的场景可行性是通过解析约束保证，还是主要依赖后验筛查？
  - 视频压缩策略若丢失细粒度状态信息，是否会削弱下游 VLA 对关键操作时刻的判断？
* **上传 PDF 后优先看**:
  - 方法章节中 IGSC 场景构建机制
  - 方法/实验章节中 VLM 闭环验证与 rejection sampling 流程
  - 实验章节中长时程任务 VLA 训练结果与组件消融

## Watchlist

### [W1]. AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention [[HTML]](https://arxiv.org/html/2511.18960) [[PDF]](https://arxiv.org/pdf/2511.18960)
* **Paper ID**: `2511.18960`
* **Authors**: Lei Xiao, Jifeng Li, Juntao Gao, Feiyang Ye, Yan Jin, Jingjing Qian, Jing Zhang, Yong Wu, Xiaoyuan Yu
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇进入 shortlist，主要因为它把 VLA 明确从 MDP 重写为 POMDP，并用 recurrent belief-state 近似与 Active Visual Attention 去补历史依赖，这对当前大量 history-agnostic VLA 是一个很直接的结构性修正。它也覆盖了 LIBERO、CALVIN 和真实 Mobile ALOHA，题目与方向都很贴主线。没有进最终精选，是因为从现有摘录看，它更像是在既有 OpenVLA 框架上的时序建模增强，而不是今天最突出的数据生成、world model 或 sim2real 主线突破。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. Adaptive Action Chunking at Inference-time for Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2604.04161) [[PDF]](https://arxiv.org/pdf/2604.04161)
* **Paper ID**: `2604.04161`
* **Authors**: Yuanchang Liang, Xiaobo Wang, Kai Wang, Shuo Wang, Xiaojiang Peng, Haoyu Chen, David Kim Huat Chua, Prahlad Vadakkepat
* **Author Priority**: Standard
* **为什么还值得留意**: AAC 值得跟踪，因为它抓住了 VLA 推理阶段一个真实而常见的工程矛盾：chunk 太大不灵敏，太小又会 mode-jumping，并提出基于动作熵的 inference-time 自适应策略。它跨 RoboCasa、LIBERO 与真实应用做了验证，实用价值不低。之所以留在 watchlist，是因为它更偏推理时策略修补与部署优化，研究冲击力弱于今天最终精选里那些改变数据或 world model 生成范式的工作。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

### [W3]. 2D or 3D: Who Governs Salience in VLA Models? -- Tri-Stage Token Pruning Framework with Modality Salience Awareness [[HTML]](https://arxiv.org/html/2604.09244) [[PDF]](https://arxiv.org/pdf/2604.09244)
* **Paper ID**: `2604.09244`
* **Authors**: Zihao Zheng, Sicheng Tian, Zhihao Mao, Lingyue Zhang, Chenyue Li, Ziyun Zhang, Hong Gao, Yuchen Huang, Yutong Xu, Guojie Luo, Xiang Chen
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇值得保留观察，因为多视觉模态 VLA 的加速问题会越来越重要，而它把 2D/3D token salience 不同这件事单独拎出来，提出 tri-stage pruning 框架，问题定义是对的。实验也给出 RLBench 上的成功率与速度权衡，说明不是空泛提速。没有进入最终精选，主要是因为它的贡献更偏系统优化与加速，对 VLA/world model 主线的范式推进感相对有限。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. Dejavu: Towards Experience Feedback Learning for Embodied Intelligence [[HTML]](https://arxiv.org/html/2510.10181) [[PDF]](https://arxiv.org/pdf/2510.10181)
* **Paper ID**: `2510.10181`
* **Authors**: Shaokai Wu, Yanbiao Ji, Qiuchang Li, Zhiyi Zhang, Qichen He, Wenyuan Xie, Guodong Zhang, Bayram Bayramli, Yue Ding, Hongtao Lu
* **Author Priority**: Standard
* **为什么还值得留意**: Dejavu 进入 shortlist，是因为它提出一种很有前景的后部署学习思路：冻结 VLA 主干，只靠经验库检索与残差控制器进行 memory-based adaptation，这与 embodied agent 的持续学习诉求高度相关。它还用 RL 和语义相似奖励训练 EFN，并在 LIBERO 上接 OpenVLA、UniVLA、GO-1 三个骨干。未进最终精选，是因为当前摘录显示其核心更偏部署后记忆增强，而不是今天重点关注的 world model、world action model 或 sim2real 数据放大主线。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W5]. Generative Simulation for Policy Learning in Physical Human-Robot Interaction [[HTML]](https://arxiv.org/html/2604.08664) [[PDF]](https://arxiv.org/pdf/2604.08664)
* **Paper ID**: `2604.08664`
* **Authors**: Junxiang Wang, Xinwen Xu, Tiancheng Wu, Julian Millan, Nir Pechuk, Zackory Erickson
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇保留在 watchlist 很合理，因为它把“text2sim2real”扩展到 pHRI，自动生成软体人体、场景布局和机器人轨迹，再用于 scratching 和 bathing 的零样本 sim2real，题材稀缺且应用导向明确。它也体现了 LLM/VLM 驱动生成式仿真的一个新落点。之所以没有进入最终精选，是因为当前证据仍集中在两个 assistive 任务，且更偏特定 pHRI 场景，通用性和方法外延性暂时不如最终入选的几篇。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
