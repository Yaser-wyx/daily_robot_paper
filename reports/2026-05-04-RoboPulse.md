# RoboPulse | 2026-05-04

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 39 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线很清楚：VLA 正在从“离线模仿得像”转向“部署后持续变强”，一条线是用在线 RL 和 fleet-scale 反馈把预训练策略推到真实执行精度，另一条线是把 world model/world action model 真正插进动作生成而非停留在外围预测。最终精选之所以成立，是因为这 6 篇几乎覆盖了当前机器人落地最关键的三块：部署期学习、未来建模、以及 Sim2Real 数据引擎。VIP 作者里，Sergey Levine 的 RL Token 和 Xiaolong Wang 参与的 Lucid-XR 最值得优先跟踪，前者代表 VLA 在线后训练的现实路径，后者代表 XR 原生数据生产与跨 embodiment 迁移。Pieter Abbeel 与 Jiajun Wu 联名的综述虽然未进最终精选，但对后续判断 world model 路线分化仍然很有参考价值。

## 今日信号

- 今天最值得记住的研究信号是：VLA 的竞争点正在从离线预训练规模转向“部署中能否持续学习”，在线 RL 与 fleet data loop 已经开始成为一等公民。
- 今天最值得记住的研究信号是：world model 正从像素级未来生成转向潜变量、动作中心或统一扩散接口，目标不是单纯“看见未来”，而是更直接地改善控制。
- 今天最值得记住的研究信号是：Sim2Real 的瓶颈正被前移到数据生产层，XR 交互、物理引导生成和跨 embodiment 采集正在变成基础设施问题。

## Editor's Picks

### [1]. RL Token: Bootstrapping Online RL with Vision-Language-Action Models [[VIP]] [[HTML]](https://arxiv.org/html/2604.23073) [[PDF]](https://arxiv.org/pdf/2604.23073) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.23073`
* **Authors**: Charles Xu, Jost Tobias Springenberg, Michael Equi, Ali Amin, Adnan Esmail, Sergey Levine, Liyiming Ke
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，它把“如何在几小时真实机器人交互内把 VLA 调到能用”这个落地问题回答得很直接。
* **问题与切口**: 这篇工作的切口非常务实：预训练 VLA 往往已经会做任务，但在真实操作里常败在最后一毫米的精度、速度和接触处理上。作者没有走重训整模的重路线，而是让 VLA 暴露一个紧凑的 RL token，作为保留预训练知识又便于在线强化学习读写的接口，再用小型 actor-critic 只针对关键执行阶段做后训练。相对已有“整模 RL 微调”思路，它更像是在大模型外侧接一个低成本、可快速迭代的精修层。
* **核心方法与证据**: 方法上，论文把预训练 VLA 改造成可输出 RL token 的骨干，再在其上训练轻量 actor 与 critic，而不是直接让 RL 改写整套大模型。HTML 正文明确给出四个关键组件：RL token、分块动作预测、策略正则化、参考动作直通，并围绕四个需要亚毫米级精度的真实机器人任务展开比较与消融，重点考察成功率、执行速度、组件贡献以及策略是否偏离原始示教。作者报告该方法能显著提速，最难阶段可达数倍加速。
* **正文要点**:
  - 实验问题设置很明确，分别检查整体收益、相对替代 RL 方法的表现、组件消融，以及是否学出不同于示教的数据驱动策略。
  - 任务选择集中在接触密集且精度敏感的真实操作场景，说明作者把目标限定在 VLA 最常见的落地短板上。
  - 正文与结论都强调这是“几小时真实练习”的轻量在线学习方案，但也承认仍需要额外人工干预。
* **为什么值得跟**:
  - 它给 VLA 后训练提供了一个现实可执行的接口设计，而不是停留在“可以用 RL”这一层。
  - 它把强化学习的收益聚焦到最关键的接触阶段，符合真实机器人最稀缺的试错预算分配。
  - 它说明在线 RL 不只是补成功率，也可能改变执行策略和速度上限。
* **风险 / 保留意见**:
  - 证据主要来自四个高精度任务，方法是否能外推到更长时程或更开放任务还需要谨慎看待。
  - 方案依赖人工干预与参考动作设计，复现时的人机流程成本可能不低。
* **建议先看**: 先看 RL token 这个接口为什么比直接整模 RL 更合理，再看组件消融与策略变化分析；这篇的价值不只在结果，更在它提出了一条可操作的 VLA 在线后训练路径。
* **关键词**: `VLA` `在线强化学习` `RL token` `真实机器人后训练` `精细操作`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
* **读 PDF 先核查**:
  - RL token 相比其他压缩表征或中间层读出，究竟保留了哪些对在线 RL 最关键的预训练先验？
  - 分块动作预测、策略正则化和参考动作直通三者里，哪个在稳定训练与提升速度上最不可替代？
  - 人工干预具体介入训练流程的哪个环节，这会不会成为大规模部署时的主要瓶颈？
* **上传 PDF 后优先看**:
  - 方法部分里 RL token 与 actor-critic 接口的定义与训练方式
  - 真实机器人主实验中与替代 RL 路线的对比结果
  - 组件消融与策略行为分析这类章节或图表

### [2]. Lucid-XR: An Extended-Reality Data Engine for Robotic Manipulation [[VIP]] [[HTML]](https://arxiv.org/html/2605.00244) [[PDF]](https://arxiv.org/pdf/2605.00244) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.00244`
* **Authors**: Yajvan Ravan, Adam Rashid, Alan Yu, Kai McClennen, Gio Huh, Kevin Yang, Zhutian Yang, Qinxi Yu, Xiaolong Wang, Phillip Isola, Ge Yang
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，它不是再做一个策略，而是在重做机器人训练数据的生产线。
* **问题与切口**: Lucid-XR 的核心不是单点模型创新，而是把“高质量操作数据从哪里来”系统化：作者提出一个面向机器人操作的 XR 数据引擎，把头显上的网页物理仿真、人到机器人的姿态重定向，以及可由自然语言操控的物理引导视频生成串成一条完整管线。相对传统遥操作或封闭式仿真平台，它想解决的是采集门槛高、场景覆盖窄、稀有但关键事件难补足的问题，因此更像是 Sim2Real 时代的数据基础设施。
* **核心方法与证据**: 证据主要围绕系统能力展开。HTML 正文列出多类接触密集环境来测试头显端物理仿真，包括刚体堆叠、液体/粒子倾倒、混合刚体与粒子碰撞、绳结、长时程厨房场景以及带凹形几何的 mug tree，覆盖了不同物理难点。系统还包含人机交互设计、姿态重定向与后续数据放大模块，结论部分进一步声称虚拟示教可支持真实机器人策略的零样本迁移与跨对象、外观、光照泛化，但量化边界仍需结合全文细看。
* **正文要点**:
  - vuer 被设计为直接运行在 XR 头显上的网页物理环境，强调低延迟、可联网扩展和无需专用硬件。
  - 数据不是停留在采集端，作者额外加入了可由自然语言控制的物理引导视频生成，用来继续放大多模态训练样本。
  - 实验场景覆盖刚体、粒子、可变形体、大场景和复杂几何，说明其目标是验证数据引擎的物理适用面而不只是单任务成功率。
* **为什么值得跟**:
  - 它把 Sim2Real 问题前移到数据制造与放大层，这对通用操作模型比单次算法提升更基础。
  - XR 原生交互如果成立，意味着机器人示教数据有机会从实验室流程变成互联网规模流程。
  - 跨 embodiment 的重定向主张，直接对应未来通用机器人数据复用的关键难题。
* **风险 / 保留意见**:
  - HTML 摘录更强调整体系统愿景与场景覆盖，真实转移收益的量化幅度在现有证据里还不够完整。
  - 生成式数据放大是否真正保留动作可执行性，取决于视频生成与物理约束对齐程度，复现门槛可能较高。
* **建议先看**: 先沿着“XR 采集 -> 姿态重定向 -> 物理引导生成 -> 真实部署”这条链读，判断它到底是在做演示工具、仿真平台，还是新的数据引擎。随后重点看跨 embodiment 与零样本迁移证据是否扎实。
* **关键词**: `Sim2Real` `XR 数据引擎` `虚拟示教` `物理引导生成` `跨 embodiment`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 头显端物理仿真在延迟、稳定性和物理保真之间做了什么取舍，哪些任务最受限？
  - 生成的视频数据如何与动作或控制信号保持一致，是否只是视觉扩增还是会反向影响策略监督？
  - 人到机器人的姿态重定向在不同机械手或不同自由度系统之间的适配成本有多高？
* **上传 PDF 后优先看**:
  - 系统总览与数据流设计的章节
  - 各类物理场景与 on-device 仿真验证结果
  - Sim2Real 与跨 embodiment 部署相关的实验或案例分析

### [3]. Learning while Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies [[HTML]](https://arxiv.org/html/2605.00416) [[PDF]](https://arxiv.org/pdf/2605.00416) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.00416`
* **Authors**: Yi Wang, Xinchen Li, Pengwei Xie, Pu Yang, Buqing Nie, Yunuo Cai, Qinglin Zhang, Chendi Qu, Jeffrey Wu, Jianheng Song, Xinlin Ren, Jingshun Huang, Mingjie Pan, Siyuan Feng, Zhi Chen, Jianlan Luo
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把“机器人部署”重新定义成持续学习过程，而不是一次性测试。
* **问题与切口**: 这篇工作的重要性在于视角转换：作者把通用 VLA 的真实部署看成一个持续闭环，而非训练完成后的静态验收。LWD 从预训练 VLA 出发，把部署中的分布偏移、长尾失败、任务变化和人工纠正机会都纳入后训练流程，让多台机器人共享物理经验并迭代更新策略。相对常见的离线模仿或单机微调路线，它更强调 fleet-scale 的经验汇聚与“边部署边学习”的组织方式，这对真正走向商用场景很关键。
* **核心方法与证据**: 从可见正文看，LWD 的技术主轴是用 DIVL 做价值学习、再用 QAM 做策略提取，其中附录式方法段详细给出分布式价值模型的离散支撑、基于 C51 投影的训练方式、分位数提取以及与非对称价值估计之间的理论联系。实验覆盖八个真实机器人任务，既包括超市补货类语义操作，也包括功夫茶、果汁、鸡尾酒、鞋盒打包等 3 到 5 分钟的长时程任务，并显式考察多子任务依赖、语言指令变化、布局变化和恢复能力。HTML 证据足以说明其任务设计很强，但具体收益幅度仍应保守解读。
* **正文要点**:
  - 框架目标不是单任务调优，而是把部署、共享经验、策略更新与再部署闭成一个持续循环。
  - 方法部分明确采用分布式价值建模，并讨论了与非对称价值估计之间的理论对应关系。
  - 真实机评测同时覆盖商超补货与长时程复合操作，任务时长与子任务数量都明显高于常见短程台面操作。
* **为什么值得跟**:
  - 它把通用机器人最现实的问题点出来了：离线预训练强，不代表一上线就能稳。
  - 它强调多机器人共享在线经验，这比单机 RL 更接近真实部署体系的扩展逻辑。
  - 它把长时程、多阶段恢复与语义泛化放进同一框架里，代表更接近产品级评测标准。
* **风险 / 保留意见**:
  - HTML 摘录没有完整展开主实验的量化结果与消融深度，因此收益强度需要等全文核查。
  - fleet-scale 方案往往依赖数据管线、奖励设计和回放配比，系统工程成本可能远高于算法表面复杂度。
* **建议先看**: 先看引言中的部署闭环定义，再读 DIVL/QAM 这条方法主线，最后对照八个真实任务判断它到底是在解决价值学习问题，还是在解决部署系统问题；我倾向于后者更关键。
* **关键词**: `VLA 后训练` `fleet-scale RL` `持续部署学习` `分布式价值学习` `长时程操作`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 部署期的奖励、人工纠正和失败恢复信号是如何被统一进同一个在线学习回路里的？
  - DIVL 与 QAM 分别解决了什么稳定性问题，为什么比直接对预训练策略做 RL 更合适？
  - 离线数据与部署新数据在回放和更新中如何配比，才能避免遗忘原有通用能力？
* **上传 PDF 后优先看**:
  - 框架总览与 deployment loop 的章节
  - DIVL/QAM 及其理论说明部分
  - 八个真实机器人任务的主结果与持续学习分析

### [4]. Being-H0.7: A Latent World-Action Model from Egocentric Videos [[HTML]](https://arxiv.org/html/2605.00078) [[PDF]](https://arxiv.org/pdf/2605.00078) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.00078`
* **Authors**: Hao Luo, Wanpeng Zhang, Yicheng Feng, Sipeng Zheng, Haiweng Xu, Chaoyi Xu, Ziheng Xi, Yuhui Fu, Zongqing Lu
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它代表 world model 与 VLA 结合的一条更轻、更像产品化的潜变量路线。
* **问题与切口**: Being-H0.7 试图解决一个越来越清晰的问题：VLA 直接从观察到动作，容易学到捷径映射，却未必真正编码了接触、动态和任务进展；但如果改走像素级未来视频预测，又会带来过重的训练与推理负担。它的解法是在感知与动作之间插入一组可学习的潜变量查询，让这些查询承担“未来感知的推理接口”，再通过训练期的未来分支把未来相关信息压进潜空间。相较视频 rollout 路线，这更强调用紧凑表示而非显式画面来承载未来信息。
* **核心方法与证据**: 模型采用双分支设计：可部署的 prior 分支只看当前上下文来推断潜变量状态，而仅在训练时使用的 posterior 分支会把未来观察编码进来，并在潜变量空间与 prior 对齐。HTML 摘录还给出若干训练构件，包括基于 V-JEPA2.1 的视觉编码、InternVL3.5 与 Qwen3 的专家组合、flow-matching 动作目标、prior-posterior 对齐损失以及防塌缩正则，并说明预训练混合了人类与机器人操作轨迹。现有证据足以支持“潜空间未来对齐”这一主张，但具体领先幅度需要谨慎等待全文表格。
* **正文要点**:
  - 未来信息只通过训练期 posterior 分支进入模型，部署时不需要显式生成未来帧。
  - 核心创新是把 prior 与 posterior 的对齐放在潜变量推理空间，而不是像素空间。
  - 作者明确强调大规模人类视频预训练与统一序列格式对模型可扩展性的重要作用。
* **为什么值得跟**:
  - 它给 world-action model 提供了一条比视频生成更轻的实现路径，更贴近控制推理需求。
  - 如果潜变量对齐有效，VLA 未来信息注入就不必依赖昂贵 rollout，这对推理时延很重要。
  - 把人类视频与机器人轨迹并入同一训练框架，符合通用机器人扩大数据规模的方向。
* **风险 / 保留意见**:
  - HTML 摘录没有完整暴露主实验增益、失败案例与消融细节，因此当前更适合作为方法趋势判断。
  - 潜空间对齐质量高度依赖编码器与训练目标，复现时可能对实现细节较敏感。
* **建议先看**: 先抓住 prior/posterior 双分支与潜变量对齐这条主线，再看作者为何认为它能替代像素级未来 rollout。随后重点核查人类视频预训练到底贡献了多大比例的效果。
* **关键词**: `latent world-action model` `VLA` `future-aware reasoning` `egocentric video` `潜变量对齐`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 这些 latent queries 具体承载的是任务进展、接触状态，还是更抽象的动作先验？
  - 性能提升里有多少来自潜变量对齐本身，又有多少来自额外的人类视频预训练规模？
  - 在需要显式几何预测的任务上，不做像素级 rollout 是否会留下可见短板？
* **上传 PDF 后优先看**:
  - 双分支架构与潜变量对齐目标的章节
  - 预训练数据与多专家组件的实现说明
  - 与视频 rollout 或无未来建模基线的消融和对比结果

### [5]. STARRY: Spatial-Temporal Action-Centric World Modeling for Robotic Manipulation [[HTML]](https://arxiv.org/html/2604.26848) [[PDF]](https://arxiv.org/pdf/2604.26848) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.26848`
* **Authors**: Yuxuan Tian, Yurun Jin, Bin Yu, Yukun Shi, Hao Wu, Chi Harold Liu, Kai Chen, Cong Huang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把 world model 的未来预测真正压进动作生成回路，而且强调几何与时序一起对控制负责。
* **问题与切口**: STARRY 针对的是 VLA 在空间几何和时间协调上常见的断裂：模型能理解语义，但未来交互状态与动作生成之间耦合太弱，导致挂杯、递交、放置这类需要预判局部关系的任务容易失败。作者提出一个 world-model-enhanced action policy，通过统一扩散过程同时去噪未来时空潜变量与动作序列，再用 GASAM 把预测到的几何信息注入动作注意力分支。相对只做未来表征或只做动作扩散的路线，它更强调“预测与执行共模”。
* **核心方法与证据**: 正文给出的证据相对完整：仿真上在 RoboTwin 2.0 的 Clean 与 Randomized 两个设置评测，50 个双臂任务统一多任务训练，且明确给出示教规模、训练步数与比较基线范围；现实世界里还做了物理执行验证，并通过消融分析时空预测模块与 GASAM 的作用。HTML 摘录中的结论提供了关键结果边界：仿真平均成功率在两种设置下都达到九成以上，真实机平均成功率也有明显提升，说明收益不只停留在模拟器。
* **正文要点**:
  - STARRY 的核心是联合去噪未来时空潜变量与动作序列，而不是把两者分开训练后再弱耦合拼接。
  - GASAM 的设计目标是把 2D 视觉 token 中的预测几何，转成更适合 3D 度量控制使用的选择性调制信息。
  - RoboTwin 2.0 采用 50 个任务的统一多任务训练协议，说明作者希望证明的是通用操作而非单任务特化。
* **为什么值得跟**:
  - 它把 world model 从“辅助理解未来”推进到“直接决定动作生成方式”，方向上很对。
  - 几何感知和时序预测一起进入控制回路，比只做语义增强更贴近真实操作失败机理。
  - 同时有仿真与真实机证据，使其不只是基准分数论文，而更像可迁移的方法路线。
* **风险 / 保留意见**:
  - 当前强证据主要来自 RoboTwin 2.0 协议，跨平台和开放环境鲁棒性仍需更多外部验证。
  - 统一扩散与几何调制听起来有效，但推理开销和工程复杂度在摘录里没有充分展开。
* **建议先看**: 先看联合扩散与 GASAM 这两个部件如何分工，再看它在 Clean/Randomized 与真实机之间是否保持同方向收益；这篇最值得追的是“预测和执行是否真正被绑在一起”。
* **关键词**: `world-model-enhanced policy` `统一扩散` `几何感知注意力` `RoboTwin 2.0` `机器人操作`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 性能收益主要来自时空未来建模，还是来自 GASAM 对几何区域的选择性强调？
  - 在强随机化设置下，预测到的几何信息是否比纯视觉语义更稳定地支持控制？
  - 统一去噪未来潜变量与动作序列会带来多大的推理时延，是否影响闭环控制频率？
* **上传 PDF 后优先看**:
  - 方法部分中联合扩散与 GASAM 的设计说明
  - RoboTwin 2.0 主结果与按任务拆解的章节
  - 真实机器人执行与模块消融分析

### [6]. MotuBrain: An Advanced World Action Model for Robot Control [[HTML]](https://arxiv.org/html/2604.27792) [[PDF]](https://arxiv.org/pdf/2604.27792) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.27792`
* **Authors**: MotuBrain Team, Chendong Xiang, Fan Bao, Haitian Liu, Hengkai Tan, Hongzhe Bi, James Li, Jiabao Liu, Jingrui Pang, Kiro Jing, Louis Liu, Mengchen Cai, Rongxu Cui, Ruowen Zhao, Runqing Wang, Shuhe Huang, Yao Feng, Yinze Rong, Zeyuan Wang, Jun Zhu
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它是当前 shortlist 里最强势的统一 world action model 之一，且结果表达很有压迫感。
* **问题与切口**: MotuBrain 的野心比一般 VLA 增强版更大：它不是只给策略加一个未来模块，而是用 UniDiffuser 形式把视频与动作统一建模，再通过三流 Mixture-of-Transformers 支持策略学习、世界建模、视频生成、逆动力学和联合视频-动作预测等多种能力。相较偏单一控制目标的路线，它试图把“理解世界如何演化”和“根据世界生成动作”放进同一个训练与推理框架里，同时吸收 video-only、task-agnostic 与 cross-embodiment 机器人数据。
* **核心方法与证据**: 从 HTML 摘录可读到的证据有两层。方法上，它在 Motus 基础上继续加入统一多视角建模、独立文本流以及面向 heterogeneous multimodal data 的扩展设计，目标是让单模型覆盖更多数据来源与推理模式。实验上，作者沿用 RoboTwin 2.0 多任务协议，用 clean 与 heavily randomized 两类演示联合训练，并明确给出视频与动作的时间下采样设置；正文还直接报告其在两种设置下都排名第一，且随机化评测平均分超过 95%。这使它在 benchmark 层面非常有竞争力。
* **正文要点**:
  - 单模型同时支持 policy learning、world modeling、video generation、inverse dynamics 与 joint video-action prediction，是其最醒目的统一性主张。
  - 方法新增点不只是一体化训练，还包括 unified multiview modeling 与独立文本流，说明作者在补多模态耦合的结构短板。
  - 实验强调 heterogeneous 数据吸收能力，覆盖 video-only、task-agnostic 与 cross-embodiment 机器人数据。
* **为什么值得跟**:
  - 如果统一模型真的稳定成立，机器人控制、预测与数据利用之间的边界会被明显压缩。
  - 它在标准多任务基准上的结果很强，说明统一 world action model 不一定以性能妥协为代价。
  - 异构数据兼容性对下一阶段机器人基础模型尤其关键，因为高价值数据天然来源不统一。
* **风险 / 保留意见**:
  - 体系庞大且模块多，训练资源、数据清洗与工程实现要求都可能很高，复现门槛不低。
  - 当前强证据集中在 RoboTwin 协议，开放环境与长尾真实任务上的失效模式还需要更多信息。
* **建议先看**: 先看它如何定义“统一”而不是简单堆功能，再重点看多视角、文本流和异构数据这三处是否真的带来可解释的增益。随后再判断 benchmark 高分是数据规模优势，还是架构本身确有贡献。
* **关键词**: `world action model` `UniDiffuser` `Mixture-of-Transformers` `异构多模态数据` `RoboTwin 2.0`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 多视角建模、独立文本流和异构数据扩展三者中，哪一个对最终性能与泛化最关键？
  - 统一训练时如何避免 video-only 数据与 action-conditioned 数据在目标上互相牵制？
  - 它在开放式真实机任务中的优势，是否和在 RoboTwin 基准中的高分来自同一机制？
* **上传 PDF 后优先看**:
  - 统一架构与训练目标的章节
  - 不同架构选择的消融实验
  - RoboTwin 主结果与真实机/开放场景验证部分

## Watchlist

### [W1]. Embodied Interpretability: Linking Causal Understanding to Generalization in Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2605.00321) [[PDF]](https://arxiv.org/pdf/2605.00321)
* **Paper ID**: `2605.00321`
* **Authors**: Hanxin Zhang, Mingshuo Xu, Abdulqader Dhafer, Shigang Yue, Hongbiao Dong, Zhou Daniel Hao
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇进入 shortlist 的原因很充分：它没有继续卷更大的 VLA，而是追问 VLA 为什么在分布偏移下会失败，并用 ISS 与 NMR 把“是否依赖伪相关区域”做成了可干预、可量化的分析框架。它也提供了一个值得记住的判断：可解释性指标可能直接预测泛化能力。没有进最终精选，主要因为它更偏诊断与评估工具，而不是今天主线里最核心的部署学习或 world-action 建模推进；另外现有证据主要绑定在特定 benchmark 与单一策略分析上。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. Thinking in Text and Images: Interleaved Vision--Language Reasoning Traces for Long-Horizon Robot Manipulation [[HTML]](https://arxiv.org/html/2605.00438) [[PDF]](https://arxiv.org/pdf/2605.00438)
* **Paper ID**: `2605.00438`
* **Authors**: Jinkun Liu, Haohan Chi, Lingfeng Zhang, Yifan Xie, YuAn Wang, Long Chen, Hangjun Ye, Xiaoshuai Hao, Wenbo Ding
* **Author Priority**: Standard
* **为什么还值得留意**: IVLR 很有想法：把文本子目标与视觉关键帧交错成显式中间轨迹，试图同时保住因果顺序和几何落点，这对长时程操作很有吸引力。它进入 shortlist，是因为“显式 reasoning trace 作为 VLA 接口”确实是值得跟踪的支线。没有进最终精选，是因为当前摘录中的证据仍以 LIBERO 与 SimplerEnv 为主，真实机器人与更强部署场景支撑不足，而且相较今天主线，它更像结构化规划接口而非更底层的世界建模或在线学习突破。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. VLAs are Confined yet Capable of Generalizing to Novel Instructions [[HTML]](https://arxiv.org/html/2505.03500) [[PDF]](https://arxiv.org/pdf/2505.03500)
* **Paper ID**: `2505.03500`
* **Authors**: Quanyi Li
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇值得保留在 watchlist，因为它抓住了一个很重要但常被模糊处理的问题：VLA 到底是在泛化，还是只是在重放示教覆盖过的组合。作者通过 text latent 和新构造的 libero-ood 去测试“技能重组”能力，这对评估 VLA 真实上限很有价值。之所以没进最终精选，是因为它更偏分析与行为操控研究，方法增量相对集中在诊断框架上，对今天关注的 world model、Sim2Real 和部署期学习主线支撑较弱。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. World Model for Robot Learning: A Comprehensive Survey [[VIP]] [[HTML]](https://arxiv.org/html/2605.00080) [[PDF]](https://arxiv.org/pdf/2605.00080)
* **Paper ID**: `2605.00080`
* **Authors**: Bohan Hou, Gen Li, Jindou Jia, Tuo An, Xinying Guo, Sicong Leng, Haoran Geng, Yanjie Ze, Tatsuya Harada, Philip Torr, Oier Mees, Marc Pollefeys, Zhuang Liu, Jiajun Wu, Pieter Abbeel, Jitendra Malik, Yilun Du, Jianfei Yang
* **Author Priority**: Core VIP
* **为什么还值得留意**: 这篇综述本身很强，尤其作者阵容里有 Pieter Abbeel 与 Jiajun Wu，且它把 world model 在策略学习、规划、仿真、评估与数据生成中的角色系统梳理了一遍。它进入 shortlist，主要因为它能帮我们快速建立今天多篇 world-action 论文之间的坐标系。没有进最终精选，只是因为它是综述而非一手方法论文；更适合作为后续深读与路线判断的背景文献，而不是今天的主攻对象。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)
