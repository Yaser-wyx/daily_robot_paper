# RoboPulse | 2026-04-14

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 127 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线很清楚：VLA 正在从“端到端黑盒控制”转向“带显式中间表征的可验证决策”，最终精选里的 GWM、AIM、VP-VLA、ProGAL-VLA 分别把语言对齐潜空间、空间 value map、视觉提示和验证式目标嵌入推到前台。StarVLA-α 入选，是因为它反过来证明很多系统复杂度未必必要，干净的数据管线与强 backbone 可能已经解释了大量增益。RoboLab 则补上 Sim2Real 侧最缺的一环：不是再报一个容易饱和的分数，而是试图在高保真仿真中系统分析真实策略行为。今天最终精选里没有核心 VIP 作者领衔；如果按作者优先级继续跟踪，watchlist 中 Huazhe Xu 的 AffordGen 仍是最值得追加阅读的外延信号。

## 今日信号

- VLA 的下一阶段重点不是把模型做得更黑盒，而是把“目标、意图、空间锚点、验证信号”显式地塞回控制链路。
- world model 的角色正在从被动预测器升级为决策接口，关键不只是生成未来画面，而是让未来表征能直接承载语义、价值或恢复信息。
- benchmark 正重新成为一等研究对象：一类工作在拆解语义泛化失效，另一类工作在重建 simulation 与真实部署之间可诊断的对应关系。

## Editor's Picks

### [1]. Grounded World Model for Semantically Generalizable Planning [[HTML]](https://arxiv.org/html/2604.11751) [[PDF]](https://arxiv.org/pdf/2604.11751) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.11751`
* **Authors**: Quanyi Li, Lan Feng, Haonan Zhang, Wuyang Li, Letian Wang, Alexandre Alahi, Harold Soh
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把 world model 从“看图找目标”推进到“按语言做 MPC 规划”，而且用受控 benchmark 正面检验语义泛化。
* **问题与切口**: 这篇工作瞄准 world model 规划里一个很实际却常被绕开的痛点：测试时往往拿不到目标图像，而只靠图像目标也很难支持自然语言交互。作者把世界模型训练到视觉-语言对齐潜空间里，让 MPC 不再比较“预测未来像不像目标图”，而是比较“预测未来是否更贴近指令语义”。它的新意不是再做一个更大的 VLM policy，而是把语义泛化直接放进规划代价函数。
* **核心方法与证据**: 方法主线是先学习一个落在视觉-语言对齐空间中的 Grounded World Model，再用它对候选动作序列的未来结果打分，评分依据是未来表征与语言指令嵌入的相似度。证据上，作者专门构建了 WISER benchmark：任务都是简单刚性的 pick-and-place，目的是把测试失败尽量归因到语义泛化而非复杂运动控制；训练/测试跨 24 个类别，测试还改变了颜色与指代表达，因此这篇更像是在做“语义规划能力”的定点诊断。
* **正文要点**:
  - 把 action proposal 的评分从“预测图像到目标图像的距离”改成“预测未来到语言指令的相似度”。
  - WISER 故意采用简单且刚性的操作轨迹，用来隔离语义泛化失败而非运动学习失败。
  - 训练与测试跨 24 个类别，测试场景同时变化立方体颜色和指代表达方式。
* **为什么值得跟**:
  - 它提供了一条不依赖目标图像的语言条件规划路线，更接近真实部署时的任务交互方式。
  - 它把 world model 与 VLA 的结合点放在规划代价而非动作头上，研究上更容易分析语义是否真的进入决策。
  - WISER 这类受控 benchmark 对识别“模型会动但不懂指令”的问题很有价值。
* **风险 / 保留意见**:
  - 现有证据集中在简单 pick-and-place 设定，能否外推到长时程或高接触任务仍不清楚。
  - HTML 摘录不足以判断潜空间对齐细节与真实机器人验证强度，复现时需要重点核查训练设计。
* **建议先看**: 先看问题设定与 WISER benchmark，因为这篇最强的地方是把“语义泛化”定义成可检验的规划问题。随后再看方法章节里语言相似度如何进入 MPC 代价。
* **关键词**: `world model` `MPC` `vision-language alignment` `semantic generalization` `benchmark`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 语言对齐潜空间是与 world model 联合训练得到的，还是主要依赖冻结好的视觉/语言编码器？
  - 在 WISER 上的提升主要来自语义评分函数，还是来自 world model 本身的预测质量变化？
  - 当指令包含多步约束、关系约束或非指称性目标时，这种语言相似度代价还能否稳定工作？
* **上传 PDF 后优先看**:
  - 方法章节中的潜空间对齐方式与 MPC 代价定义
  - WISER 的数据划分、测试变化因素与任务构造逻辑
  - 与 VLM-based VLA 及 goal-image world model 的对比实验

### [2]. AIM: Intent-Aware Unified world action Modeling with Spatial Value Maps [[HTML]](https://arxiv.org/html/2604.11135) [[PDF]](https://arxiv.org/pdf/2604.11135) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.11135`
* **Authors**: Liaoyuan Fan, Zetian Xu, Chen Cao, Wenyao Zhang, Mingqi Yuan, Jiayu Chen
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把 unified world action model 的瓶颈讲清楚了，并用显式空间 value map 把“会看未来”转成“会下手”。
* **问题与切口**: AIM 的核心判断很直接：预训练视频生成模型擅长建模场景如何变化，但机器人动作解码还需要明确知道“该和哪里交互、交互意图是什么”。因此它不再要求动作头直接从未来视觉表征里倒推出逆动力学线索，而是先预测一个与意图对齐的空间 value map，作为视频分支和动作分支之间的显式接口。这个切口切中了当下 unified WAM 经常需要大量机器人域微调的结构性原因。
* **核心方法与证据**: 从摘录看，AIM 以 Wan2.2-TI2V-5B 为视频先验，沿用多视角打包策略把头部和双腕相机拼成统一画布，再结合结构化 action tokenization 做联合建模。关键不是单纯三头预测，而是让 future video、future value map 和 future action 共存，并通过 intent-causal attention 限制动作头获取未来信息的路径。实验在 50 个 RoboTwin 仿真任务、统一 30K 数据集上进行；Stage1 与 RL post-training 的对比也说明，大部分收益已来自架构本身。
* **正文要点**:
  - 在视频分支旁增加显式 value-map 预测路径，而不是只从 RGB future 直接解码动作。
  - 采用三视角 T-pose 画布输入，尽量复用预训练视频模型的视觉接口。
  - Stage1 与 RL post-training 分开汇报，用来隔离结构设计与后续自蒸馏式优化的贡献。
* **为什么值得跟**:
  - 它把视频先验与机器人控制之间的结构错位说得更具体，便于后续方法对症下药。
  - 空间 value map 让 world action model 更接近“先找交互位点，再出动作”的机器人常识。
  - 如果这个接口设计成立，后续很多视频基模型都可能被更低成本地转成可控的机器人模型。
* **风险 / 保留意见**:
  - 现有证据主要来自 RoboTwin 仿真，真实机器人迁移和跨 embodiment 稳定性仍待核查。
  - value map 的监督来源、分辨率与噪声鲁棒性在摘录里不够清楚，复现门槛可能不低。
* **建议先看**: 先看架构图和 intent-causal attention 的信息流约束，再看 Stage1 与 RL post-training 的拆分实验。若这两处站得住，AIM 的主张就基本成立。
* **关键词**: `world action model` `spatial value map` `video prior` `intent-aware control` `RoboTwin`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - value map 的训练信号来自显式标注、未来状态投影，还是模型内部自监督构造？
  - intent-causal attention 具体如何阻断 future RGB 对动作头的直接泄漏，相关消融是否充分？
  - 当交互区域分布很散或任务需要高接触双臂协调时，单一空间 value map 还够不够表达意图？
* **上传 PDF 后优先看**:
  - value-map 分支与 intent-causal attention 的方法章节
  - Stage1、RL post-training 与冻结策略的消融实验
  - Hard 设定下的失败案例与跨任务分析

### [3]. VP-VLA: Visual Prompting as an Interface for Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2603.22003) [[PDF]](https://arxiv.org/pdf/2603.22003) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.22003`
* **Authors**: Zixuan Wang, Yuxin Chen, Yuqi Liu, Jinhui Ye, Pengguang Chen, Changsheng Lu, Shu Liu, Jiaya Jia
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它给 VLA 提供了一个可解释的视觉接口，比单次前向把语言、空间和控制全塞进黑盒更有研究价值。
* **问题与切口**: VP-VLA 直指当下 VLA 的单体瓶颈：一个前向过程要同时负责指令理解、空间 grounding 和低层控制，既容易牺牲空间精度，也容易在分布外场景中失稳。作者把系统拆成两个速度和职责不同的子系统：System 2 Planner 负责把复杂指令分解成子任务并生成视觉接口图像，System 1 Controller 则把这些显式视觉提示转成高频控制。新意在于把 visual prompting 从人机交互工具改造成机器人控制接口。
* **核心方法与证据**: 从正文摘录看，Planner 使用 Qwen3-VL-4B-Instruct，视觉提示生成依赖 SAM3，并只保留目标物体与目标位置得分最高的提示结果；控制器则基于 starVLA 框架上的 QwenOFT 变体。作者还加入辅助视觉 grounding 目标，让控制器在训练中更依赖这些空间锚点。证据上，这篇覆盖了仿真 benchmark 与真实机器人两部分，且明确把 cluttered、under-specified instruction 和 OOD generalization 作为重点场景，但摘录没有给出足够细的量化边界。
* **正文要点**:
  - System 2 以事件驱动方式分解任务并生成视觉接口图像，而不是直接输出连续动作。
  - System 1 在 cross-hairs、bounding boxes 等显式视觉提示条件下执行高频追踪控制。
  - 实验同时覆盖仿真与真实机器人，重点考察杂乱场景、欠指定指令和分布外泛化。
* **为什么值得跟**:
  - 显式视觉接口让推理与执行的责任边界更清楚，也更容易做调试与人工干预。
  - 这条路线可能比纯文本子任务分解更贴近机器人真正需要的空间约束。
  - 如果视觉提示足够稳健，后续可以独立升级 planner 而不必同步重训整个控制器。
* **风险 / 保留意见**:
  - 系统性能会明显受制于 planner 与分割/提示生成模块的误差传播。
  - 两阶段设计的时延、重规划频率和异常恢复机制在摘录中信息不足。
* **建议先看**: 先看 Planner 到 Controller 的视觉接口定义，再看真实机器人部分如何验证它在欠指定和 OOD 场景中的价值。若接口是静态而非可更新的，这会直接影响你对方法上限的判断。
* **关键词**: `VLA` `visual prompting` `dual-system` `grounding` `OOD generalization`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - Planner 在执行过程中会不会重调用，视觉提示是一次性生成还是闭环更新？
  - 辅助视觉 grounding 损失对最终控制性能的贡献有多大，是否只是稳定训练而非真正提升泛化？
  - 当 SAM3 或目标定位给出错误高分提示时，控制器是否有自我纠错或拒绝执行能力？
* **上传 PDF 后优先看**:
  - Planner-Controller 接口与视觉提示生成流程
  - 真实机器人上的 cluttered/under-specified/OOD 实验
  - 提示类型与辅助 grounding 目标的消融分析

### [4]. ProGAL-VLA: Grounded Alignment through Prospective Reasoning in Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2604.09824) [[PDF]](https://arxiv.org/pdf/2604.09824) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.09824`
* **Authors**: Nastaran Darabi, Amit Ranjan Trivedi
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把“语言忽视”问题拆成可验证的目标绑定流程，而不是继续靠更大的黑盒 backbone 硬顶。
* **问题与切口**: ProGAL-VLA 针对的是 VLA 里最难受但也最常见的失效模式：模型表面上接收了语言，实际决策却更多依赖视觉捷径；一旦语义推理真的介入，控制又容易不稳。它的解法不是简单加更多 cross-attention，而是显式构建 3D entity-centric graph，把慢速符号规划产生的子目标与可感知实体对齐，再通过验证后的目标嵌入驱动动作。这相当于在“想做什么”和“手该怎么动”之间插入一个可检查的绑定层。
* **核心方法与证据**: 证据链的设计很讲究隔离变量：快速控制策略仍然是 OpenVLA-7B，与基线共享逐步控制容量；慢速 planner 用 Qwen-2.5-VL-Instruct-7B，但每个 episode 只调用一次，用来生成符号化子目标模板。感知侧用 YOLO-World 做开放词汇检测，再把实例提升到 GSM 图中，并通过 GAC 损失做符号-实体对齐。实验明确围绕三件事展开：缓解 language ignorance、提升长时程操作、以及让 verified goal attention entropy 成为歧义信号。
* **正文要点**:
  - 所有动作都只通过 verified goal embedding 条件化，形成显式 verification bottleneck。
  - 系统把开放词汇检测结果提升为 3D entity-centric graph，再做符号子目标对齐。
  - 实验假设被明确写成三条：语言忽视、长时程操控和歧义/不确定性检测。
* **为什么值得跟**:
  - 它把“语言是否真的进入控制”从不可见的内部激活问题，改造成可验证的目标绑定问题。
  - verified goal 这一设计有机会成为以后 VLA 安全执行、拒绝执行或请求澄清的接口。
  - 在不增加逐步控制模型规模的前提下引入慢速规划，更符合机器人系统分层设计的现实。
* **风险 / 保留意见**:
  - 检测器、3D 图构建和慢速规划共同组成较长链路，任何一环错配都可能导致脆弱性放大。
  - 摘要里提到的鲁棒性提升数字在摘录中被截断，很多关键强结论仍需以 PDF 中完整实验为准。
* **建议先看**: 先盯住 GSM、GAC 和 verification bottleneck 三件事，因为这篇真正的贡献不在 backbone，而在强制语言目标落地的机制设计。然后再看 ambiguity benchmark 是否真能说明熵信号可校准。
* **关键词**: `VLA` `language grounding` `entity graph` `verification bottleneck` `ambiguity detection`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - GAC 损失如何构造正负样本，它是迫使语言起作用，还是只是额外增加了监督强度？
  - 如果 YOLO-World 漏检或误检关键实体，verified goal 机制是否存在回退或恢复路径？
  - attention entropy 与真实执行失败、场景歧义或人类判断之间的相关性是否稳定且可校准？
* **上传 PDF 后优先看**:
  - GSM、GAC 与 verification bottleneck 的方法章节
  - LIBERO-Plus 上针对 language ignorance 与 robustness 的对比实验
  - Custom Ambiguity Benchmark 与不确定性分析章节

### [5]. StarVLA-$α$: Reducing Complexity in Vision-Language-Action Systems [[HTML]](https://arxiv.org/html/2604.11757) [[PDF]](https://arxiv.org/pdf/2604.11757) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.11757`
* **Authors**: Jinhui Ye, Ning Gao, Senqiao Yang, Jinliang Zheng, Zixuan Wang, Yuxin Chen, Pengguang Chen, Yilun Chen, Shu Liu, Jiaya Jia
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它不是再堆模块，而是用受控实验说明很多 VLA 复杂度可能并非必要。
* **问题与切口**: StarVLA-α 的价值不在于再发明一个花哨系统，而在于把当前 VLA 研究里最混乱的部分拆开重做：不同论文混用了不同 backbone、动作表示、数据预处理、embodiment 适配和 benchmark trick，导致很难知道真正有效的因素是什么。作者提出一个极简但强的统一基线，核心假设是“强 VLM 加轻量动作头”已经覆盖了大部分增益，剩下很多复杂度可能只是实验混杂项。
* **核心方法与证据**: 方法上几乎是刻意克制的：统一使用原始 RGB 与原始语言输入，不做 benchmark-specific formatting；动作只用训练集统计做标准化，并直接 pad 到统一维度；主干选 Qwen3-VL，后面接轻量连续动作头。证据上，摘录给出多 benchmark 的强结果，包括 LIBERO 平均 98.8%、SimplerEnv 相对最佳方法再提升，以及双臂/类人场景也能达到可观成功率。结论部分还说明作者进一步分析了动作处理、模型规模、初始化与 batch size 等关键设计项。
* **正文要点**:
  - 全环境共享一条最小化数据管线，不做针对 benchmark 的特殊工程处理。
  - 不同 embodiment 的动作被直接 pad 到统一维度，而不是手工定制复杂动作接口。
  - 论文把自己定位成受控设计研究基线，而不是某个 benchmark 上的专用最优系统。
* **为什么值得跟**:
  - 它为 VLA 社区提供了更干净的比较基线，能减少“工程技巧伪装成方法进步”的风险。
  - 如果极简范式已经很强，很多后续工作就该把精力转向真正缺失的结构能力而非继续堆系统复杂度。
  - 统一管线对跨 embodiment 和 generalist training 的研究尤其重要，因为它降低了实验门槛。
* **风险 / 保留意见**:
  - 强结果可能高度依赖所选 backbone 和训练数据混合，未必意味着所有复杂设计都无价值。
  - 对需要显式记忆、状态估计或规划的任务，这种极简范式的失效边界在摘录里尚未展开。
* **建议先看**: 先看统一预处理和动作表示，再看那些围绕模型规模、初始化和 batch size 的消融。若这些分析做得扎实，这篇会是后续很多 VLA 论文的参照物。
* **关键词**: `VLA baseline` `Qwen3-VL` `generalist training` `action representation` `benchmark control`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 哪些消融真正支持“轻量 action head 已足够”，而不是 backbone 单独决定了大部分性能？
  - 统一 action padding 在多 embodiment 设置下是否引入容量浪费或隐性偏置？
  - 当任务需要长期规划、外部记忆或多阶段纠错时，这个最简系统会先在哪类 benchmark 上失效？
* **上传 PDF 后优先看**:
  - 统一数据管线与动作表示的实现细节
  - 模型规模、初始化、batch size 等设计选择的消融章节
  - generalist training 与单 benchmark 训练的比较结果

### [6]. RoboLab: A High-Fidelity Simulation Benchmark for Analysis of Task Generalist Policies [[PDF]](https://arxiv.org/pdf/2604.09860) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.09860`
* **Authors**: Xuning Yang, Rishit Dagli, Alex Zook, Hugo Hadfield, Ankit Goyal, Stan Birchfield, Fabio Ramos, Jonathan Tremblay
* **Author Priority**: Standard
* **一句话结论**: 值得先放进阅读队列，因为它直指当前通用策略评测的短板；但在没看到 PDF 前，我会把它当作潜力很高的 benchmark 提案而非已被充分验证的标准。
* **问题与切口**: 这篇工作的核心不是提出新的 VLA 或 world model，而是重新定义“怎样评测通用机器人策略才算有信息量”。摘要指出，现有 simulation benchmark 很快就会性能饱和，而且训练与评测之间存在明显域重叠，导致分数好看却难以解释泛化与鲁棒性。RoboLab 想回答两个更关键的问题：仿真中观测到的行为到底能多大程度解释真实策略表现，以及哪些外部因素最强地影响这种表现。
* **核心方法与证据**: 从目前可用信息看，RoboLab 允许人工编写和 LLM 辅助生成场景与任务，并强调 robot-agnostic、policy-agnostic 以及受控扰动分析，这使它更像“分析平台”而不只是排行榜。由于 HTML 不可用、只有摘要回退，我们只能确认其目标定位和大致构成，尚无法判断任务生成机制、扰动分类、真实策略对照协议、以及 sim-real 相关性是否被充分量化。因此这篇入选更多基于方向价值，而非当前证据已经非常完整。
* **正文要点**:
  - 摘要明确把研究问题聚焦为两件事：仿真能否解释真实策略表现，以及哪些外部因素最影响行为。
  - 框架支持人工编写和 LLM 辅助生成场景与任务，强调与具体机器人和策略解耦。
  - 工作试图解决的是 benchmark 饱和和训练/评测域重叠，而不是单纯再增加更多任务数量。
* **为什么值得跟**:
  - Sim2Real 研究真正缺的往往不是更多模型，而是能解释失败来源的高质量分析型 benchmark。
  - 如果它真能建立仿真行为与真实策略表现的对应关系，会直接提高很多 policy 研究的评测效率。
  - robot-agnostic、policy-agnostic 的设计目标，决定了它可能成为多条技术路线共享的测试基座。
* **风险 / 保留意见**:
  - 目前只有摘要证据，很多关键结论仍停留在研究设想层面。
  - benchmark 的价值高度依赖模拟保真度、扰动设计质量和避免数据泄漏的具体实现，这些细节尚未看到。
* **建议先看**: 上传 PDF 后，优先核查 benchmark 构造、扰动体系和 sim-real 对照实验三块。对这篇来说，方法细节和验证协议比总体愿景更重要。
* **关键词**: `simulation benchmark` `task generalist policy` `sim2real analysis` `controlled perturbation` `generalization`
* **证据来源**: Abstract fallback
* **读 PDF 先核查**:
  - RoboLab 用什么协议衡量仿真分析与真实策略表现之间的一致性或可预测性？
  - 它如何具体避免训练与评测之间的域重叠，防止再次出现 benchmark 饱和？
  - 所谓 robot-agnostic 和 policy-agnostic 在任务接口、观测空间和评测指标上是怎样落地的？
* **上传 PDF 后优先看**:
  - benchmark 生成与场景/任务构造章节
  - 扰动分类、外部因素分析与控制变量设计
  - 仿真行为与真实策略表现的对应验证实验

## Watchlist

### [W1]. Vision-Language-Action Model, Robustness, Multi-modal Learning, Robot Manipulation [[HTML]](https://arxiv.org/html/2604.10055) [[PDF]](https://arxiv.org/pdf/2604.10055)
* **Paper ID**: `2604.10055`
* **Authors**: Yuhan Xie, Yuping Yan, Yunqi Zhao, Handing Wang, Yaochu Jin
* **Author Priority**: Standard
* **为什么还值得留意**: STRONG-VLA 进入 shortlist，是因为它抓住了 VLA 落地里很现实的一点：多模态扰动下的鲁棒性训练不能简单当成一个静态联合目标来做，分阶段优化的视角有方法论价值。没有进入最终精选，主要因为从摘录看它更像一套稳健 fine-tuning recipe，而不是对 VLA/world model 结构本身的重新定义；另外正文摘录里部分 backbone 名称缺失，当前证据密度也不够高。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. AnySlot: Goal-Conditioned Vision-Language-Action Policies for Zero-Shot Slot-Level Placement [[HTML]](https://arxiv.org/html/2604.10432) [[PDF]](https://arxiv.org/pdf/2604.10432)
* **Paper ID**: `2604.10432`
* **Authors**: Zhaofeng Hu, Sifan Zhou, Qinbo Zhang, Rongtao Xu, Qi Su, Ci-Jyun Liang
* **Author Priority**: Standard
* **为什么还值得留意**: AnySlot 值得保留关注，因为它和 VP-VLA 一样都在用显式视觉中间目标来拆解语言 grounding 与执行控制，而且 slot-level placement 这个问题本身非常硬。没有进入最终精选，是因为它的任务边界相对更窄、更偏精细放置专用路线，离今天的主线“通用 VLA/world model 结构变化”稍远一步。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. AffordGen: Generating Diverse Demonstrations for Generalizable Object Manipulation with Afford Correspondence [[VIP]] [[HTML]](https://arxiv.org/html/2604.10579) [[PDF]](https://arxiv.org/pdf/2604.10579)
* **Paper ID**: `2604.10579`
* **Authors**: Jiawei Zhang, Kaizhe Hu, Yingqian Huang, Yuanchen Ju, Zhengrong Xue, Huazhe Xu
* **Author Priority**: Core VIP
* **为什么还值得留意**: AffordGen 之所以必须进 watchlist，一方面是它确实在处理泛化与数据稀缺，另一方面它来自核心 VIP 作者 Huazhe Xu，值得额外跟踪。没有进最终精选，是因为它更偏 affordance-aware 数据生成与 imitation learning 扩增，而不是今天最核心的 VLA/world model 决策接口改造；但如果后续你要补 Sim2Real 数据侧文章，它会是优先级很高的一篇。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

### [W4]. WM-DAgger: Enabling Efficient Data Aggregation for Imitation Learning with World Models [[HTML]](https://arxiv.org/html/2604.11351) [[PDF]](https://arxiv.org/pdf/2604.11351)
* **Paper ID**: `2604.11351`
* **Authors**: Anlan Yu, Zaishu Chen, Peili Song, Zhiqing Hong, Haotian Wang, Desheng Zhang, Tian He, Yi Ding, Daqing Zhang
* **Author Priority**: Standard
* **为什么还值得留意**: WM-DAgger 进入 shortlist 的原因很明确：它把 world model 用在 OOD 恢复数据合成和 imitation learning 的 data aggregation 上，这条线对机器人鲁棒性很重要。没有进入最终精选，是因为它更偏 IL 恢复与数据闭环，而非今天主线里的 VLA、语义规划或 world action modeling；同时摘录虽然提到真实世界验证，但方法与实验的关键边界还需要 PDF 进一步确认。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
