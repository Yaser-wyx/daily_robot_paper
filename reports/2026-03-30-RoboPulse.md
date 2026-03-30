# RoboPulse | 2026-03-30

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 51 papers scanned · 10 shortlisted · 6 editor's picks

今天这组最终精选的主线很清楚：一条是离散 token VLA 正从“能生成动作”转向“能迭代修正、还能联动未来观测”的更强生成范式，另一条是后训练与部署鲁棒性开始从单纯参数更新转向教师蒸馏、记忆系统和外部编排。入选论文之所以成立，是因为它们都对应真实落地瓶颈：长时误差累积、在线分布偏移、OOD 失效、以及 world model 的可控性与物理一致性。相较之下，纯加速、纯评测或偏感知侧 Sim2Real 的工作仍重要，但对今天这条“VLA 到可部署机器人系统”的主线推动略弱一档。VIP 作者里今天最值得优先跟踪的是 Donglin Wang，他同时出现在 MMaDA-VLA 与 Fast-dVLA 上，基本串起了统一离散扩散 VLA 的能力设计与推理工程两条线。

## 今日信号

- 今天最值得记住的研究信号是：VLA 后训练正在从“离线 SFT 或在线 RL 二选一”转向教师引导的 on-policy 蒸馏，把真实偏轨状态上的密集监督当成核心资源。
- 今天最值得记住的研究信号是：离散 token VLA 的竞争焦点已不只是生成得快，而是能否在整段动作上反复修正早期错误，从而真正改善长时一致性。
- 今天最值得记住的研究信号是：world model 只有在和策略先验、物理对齐或外部适应系统深度耦合时才更有机会进入机器人主栈，而不是作为孤立的视频生成器存在。

## Editor's Picks

### [1]. MMaDA-VLA: Large Diffusion Vision-Language-Action Model with Unified Multi-Modal Instruction and Generation [[VIP]] [[PDF]](https://arxiv.org/pdf/2603.25406) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.25406`
* **Authors**: Yang Liu, Pengxiang Ding, Tengyue Jiang, Xudong Wang, Wenxuan Song, Minghui Lin, Han Zhao, Hongyin Zhang, Zifeng Zhuang, Wei Zhao, Siteng Huang, Jinkui Shi, Donglin Wang
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，它把离散扩散 VLA 从“只生成动作”推进到“同时生成未来观测与动作”的统一建模。
* **问题与切口**: 这篇工作瞄准现有 VLA 在长时操作里的几个结构性短板：层级架构额外复杂，自回归解码容易累积早期错误，环境动态往往还要靠外挂模块补。MMaDA-VLA 的切口是把语言、图像和连续控制统一映射到同一离散 token 空间，用单一扩散骨干同时做多模态理解与生成，并并行输出未来目标观测和动作块，试图把“感知-目标想象-执行”收进一个原生框架里。
* **核心方法与证据**: 目前可确认的信息主要来自摘要回退：作者采用原生离散扩散 formulation，以 masked token denoising 训练单一 backbone，并通过迭代去噪对整段输出做无序、全局式修正，而不是按固定顺序逐 token 锁死结果。摘要把主要证据指向三点：缓解时间不一致、降低长时误差累积、无需额外 dynamics 模块即可显式预测未来观测；但具体数据集、对比对象和增益幅度仍需 PDF 核查。
* **正文要点**:
  - 把语言、图像与连续机器人控制共同嵌入一个统一的离散 token 空间。
  - 单一 backbone 通过 masked token denoising 并行生成未来目标观测与动作 chunk。
  - 当前公开证据仅到摘要层，真实增益主要来自方法主张，实验边界还未在 HTML 中展开。
* **为什么值得跟**:
  - 它把 VLA 与 world-model 式未来观测预测直接耦合，方向上比“只预测动作”的策略更完整。
  - 无序迭代修正比自回归一次性提交更适合处理长时操作中的前错后传问题。
  - 如果验证成立，这类统一 token 空间会降低多模块拼接带来的训练和部署复杂度。
* **风险 / 保留意见**:
  - 缺少 HTML 正文，当前还无法判断未来观测分支究竟提供了多强的动态建模能力。
  - 连续控制离散化后再做扩散生成，可能带来精度损失、词表设计敏感性和推理时延问题。
* **建议先看**: 上传 PDF 后，先看未来目标观测分支是否真的承担了环境动态建模，再看它与动作 chunk 联合去噪的训练目标如何设计。随后核查性能收益到底来自统一建模本身，还是主要来自模型规模与预训练。
* **关键词**: `离散扩散 VLA` `统一 token 空间` `未来观测生成` `动作 chunk` `World Action`
* **证据来源**: Abstract fallback
* **读 PDF 先核查**:
  - 连续控制被如何离散化，并与图像、语言 token 在同一去噪过程中协同更新？
  - 未来目标观测的监督来自哪一时刻或哪一类 horizon，是否影响模型的规划语义？
  - 联合生成未来观测后，闭环执行的提升究竟来自更好的动作修正，还是来自隐式目标约束？
* **上传 PDF 后优先看**:
  - 方法总览与 unified discrete diffusion formulation
  - 训练目标与迭代去噪流程
  - 基准实验和未来观测分支消融

### [2]. VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation [[HTML]](https://arxiv.org/html/2603.26666) [[PDF]](https://arxiv.org/pdf/2603.26666) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.26666`
* **Authors**: Zhide Zhong, Haodong Yan, Junfeng Li, Junjie He, Tianran Zhang, Haoang Li
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它给出了 VLA 后训练里少见的“在线但不靠稀疏奖励硬搜”的中间路线。
* **问题与切口**: 这篇文章针对 VLA 落地时最现实的后训练矛盾：离线 SFT 高效但容易被分布偏移击穿，还可能遗忘预训练泛化；在线 RL 更鲁棒，却常被稀疏奖励和低样本效率拖住。VLA-OPD 的核心切口是让学生策略按自身当前能力 on-policy 地探索环境，再用冻结教师对这些真实遇到的偏轨状态给出密集 token 级指导，把“在错态上学会恢复”变成后训练主线。
* **核心方法与证据**: 从 HTML 可见，算法是一个闭环迭代过程：学生策略与环境交互收集轨迹，教师策略作为冻结专家在学生真正到达的状态上提供参考分布，学生再据此持续对齐更新。实验设计明确围绕四个问题展开：相对稀疏奖励在线 RL 的收敛效率、从极低数据 SFT 或双臂复杂初始策略中恢复性能、是否减轻 catastrophic forgetting，以及不同对齐目标的稳定性差异；结论里作者特别强调 Reverse-KL 是关键设计。
* **正文要点**:
  - 教师策略冻结为稳健专家，学生策略则按自身分布 on-policy 地持续采样与更新。
  - 核心监督不是环境稀疏奖励，而是教师在学生偏轨状态上提供的密集 token 级指导。
  - 实验问题设置明确覆盖效率、性能恢复、遗忘控制和对齐目标消融，Reverse-KL 被作者突出为最优选择。
* **为什么值得跟**:
  - 它给 VLA 后训练提供了比纯离线 SFT 更抗分布偏移、比纯在线 RL 更省样本的一条实用途径。
  - 在学生自己犯错后再学习恢复行为，比只在专家轨迹上模仿更接近真实部署。
  - 如果 forgetting 控制成立，这类方法有机会把通用基础能力和任务定制能力真正接到一起。
* **风险 / 保留意见**:
  - 方法上高度依赖一个足够强且可查询的教师策略，适用前提并不低。
  - 虽然避开了稀疏奖励探索，但仍需要在线交互，真实机器人上的成本与安全性要单独评估。
* **建议先看**: 先看教师信号的形式和 Reverse-KL 对齐目标的定义，再看极低数据初始化与 forgetting 实验；这能直接判断它到底是“更稳的蒸馏”，还是确实解决了在线适应问题。
* **关键词**: `VLA 后训练` `On-policy distillation` `Reverse-KL` `在线适应` `Catastrophic forgetting`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 教师对学生轨迹给出的 token 级监督具体是什么形式，如何避免只做静态重标注？
  - 为什么 Reverse-KL 在这里比其他对齐目标更稳定，它到底改变了哪些失败模式？
  - 性能提升中，on-policy 状态分布覆盖和教师密集监督各自贡献有多大？
* **上传 PDF 后优先看**:
  - 算法流程与对齐目标定义
  - 低数据初始化和复杂协调任务实验
  - 遗忘评测与目标函数消融

### [3]. DFM-VLA: Iterative Action Refinement for Robot Manipulation via Discrete Flow Matching [[HTML]](https://arxiv.org/html/2603.26320) [[PDF]](https://arxiv.org/pdf/2603.26320) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.26320`
* **Authors**: Jiayi Chen, Wenxuan Song, Shuai Chen, Jingbo Wang, Zhijun Li, Haoang Li
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它直击离散 token VLA 最核心的解码缺陷：前面生成错了，后面能不能改。
* **问题与切口**: 现有离散动作 VLA 不管是自回归还是离散扩散，通常一旦生成出 token 就难在后续真正翻案，导致早期局部错误会一路传到整段动作。DFM-VLA 的新意是把动作解码写成 token 级概率 velocity field 的演化过程，让整段动作序列在推理中被反复整体修正，而不是一次性定稿。它试图把“可回看、可纠错”的序列 refinement 做成离散 VLA 的默认能力。
* **核心方法与证据**: HTML 正文给出了相当完整的实现脉络：模型沿用统一离散 token 架构，文本用 Emu3 tokenizer，视觉用 VQ tokenizer，动作先经 FAST 离散化再做 BPE 压缩到 1024 词表，并比较辅助 velocity head 与 embedding-guided 两种 velocity-field 构造。推理端再叠加 two-stage decoding。实验覆盖 CALVIN、LIBERO、真实操作，并专门分析调度超参、解码行为、执行质量与效率权衡。
* **正文要点**:
  - 动作编码不是直接回归，而是 FAST 离散化后再做 BPE 压缩，并与语言、视觉 token 统一建模。
  - 方法层面同时给出 auxiliary velocity head 和 embedding-guided 两种 velocity-field 构造。
  - 实验不仅比 CALVIN、LIBERO 和真实任务结果，也专门分析解码行为、调度超参和效率折中。
* **为什么值得跟**:
  - 它把 VLA 解码从一次性输出改成可修正过程，对长时操作一致性是更本质的改动。
  - 方法保留了统一离散 token 路线，与现有离散 VLA 主干兼容性较强。
  - 正文里专门研究解码行为与效率，有助于把“为什么有效”说清，而不只给终点分数。
* **风险 / 保留意见**:
  - 迭代 refinement 与两阶段解码意味着推理成本仍可能偏高，真实闭环频率要看具体部署。
  - tokenization、调度超参和 velocity-field 设计看起来都很关键，跨平台鲁棒性仍需观察。
* **建议先看**: 先看 velocity-field 的两种构造和 two-stage decoding 如何分工，再读超参与行为分析部分；这篇的价值很大程度上在于它解释了离散 VLA 为什么需要“可回改”的解码机制。
* **关键词**: `Discrete flow matching` `动作迭代修正` `离散 token VLA` `Two-stage decoding` `Robot manipulation`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 两种 velocity-field 构造各自依赖什么监督信号，差异到底落在表达能力还是训练稳定性上？
  - two-stage decoding 的预算如何分配，什么情况下粗阶段与精修阶段会互相拖累？
  - 相对于自回归和离散扩散基线，真正带来提升的是“可回改”本身，还是新的 tokenization 与调度设置？
* **上传 PDF 后优先看**:
  - 架构与 tokenization 设计
  - velocity-field 与解码调度消融
  - 真实任务与效率行为分析

### [4]. SOMA: Strategic Orchestration and Memory-Augmented System for Vision-Language-Action Model Robustness via In-Context Adaptation [[HTML]](https://arxiv.org/html/2603.24060) [[PDF]](https://arxiv.org/pdf/2603.24060) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.24060`
* **Authors**: Zhuoran Li, Zhiyang Li, Kaijun Zhou, Jinyu Gu
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为它不是再训一个更大的 VLA，而是把鲁棒性改造成围绕冻结策略的在线系统能力。
* **问题与切口**: SOMA 关注的是部署期 OOD 干扰下 VLA 为什么会脆：它缺少长期记忆，失败后也说不清是感知、指令理解还是策略执行出了问题，更谈不上及时介入。作者的切口不是微调 backbone，而是在冻结 VLA 外围搭起一个 in-context adaptation 系统：双记忆 RAG 检索历史经验，LLM orchestrator 做归因与策略编排，MCP 负责触发可扩展干预，离线再把执行轨迹沉淀成更可靠的先验。
* **核心方法与证据**: 从 HTML 可读到的证据重点在系统闭环与评测设计。在线部分由 contrastive Dual-Memory RAG、Attribution-Driven LLM Orchestrator 和 MCP interventions 组成，离线部分是 Memory Consolidation 持续蒸馏执行 traces。实验跨三个 backbone、25 个任务，在 LIBERO-PRO 和作者新建的 LIBERO-SOMA 上测试多类 OOD 变化，并用消融检查双阶段记忆巩固的作用；但部分具体增益数值在摘录中缺失，只宜做方向性判断。
* **正文要点**:
  - 核心思路是给冻结 VLA 外挂一套在线适应系统，而不是对策略参数本身做微调。
  - 系统由双记忆检索、LLM 归因编排、MCP 干预与离线记忆巩固四部分组成。
  - 评测覆盖 LIBERO-PRO 与新建 LIBERO-SOMA，共 25 个任务，并显式面向 OOD 变化设计。
* **为什么值得跟**:
  - 它提供了一条可 retrofit 到现有 VLA 上的鲁棒性路线，工程现实感很强。
  - 把失败归因和干预触发显式化，明显更接近真实机器人运维而非静态 benchmark。
  - 如果记忆巩固机制有效，这类系统可能成为通用 VLA 部署栈的长期组成部分。
* **风险 / 保留意见**:
  - 性能提升可能部分依赖检索质量、工具干预和编排策略，而不是底层策略真的更强。
  - RAG 与 LLM orchestration 会引入额外时延和错误传播链，真实系统稳定性仍需核查。
* **建议先看**: 先顺着在线闭环看检索、归因、干预三者如何衔接，再看 LIBERO-SOMA 的任务构造；这能帮助判断它是在做真实鲁棒性，还是在做 benchmark 特定的外部补丁。
* **关键词**: `Memory-augmented VLA` `In-context adaptation` `RAG` `LLM orchestrator` `OOD robustness`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)
* **读 PDF 先核查**:
  - 双记忆里到底存了什么类型的经验，检索粒度与更新频率如何影响干预质量？
  - 失败归因是如何生成并验证的，怎样避免 LLM 归因看起来合理但方向错误？
  - 跨不同 backbone 的收益中，哪些来自通用系统设计，哪些依赖特定 MCP 工具链？
* **上传 PDF 后优先看**:
  - 在线系统流水线与记忆模块
  - LIBERO-SOMA 基准设计与 OOD 维度
  - 记忆巩固和干预组件消融

### [5]. Policy-Guided World Model Planning for Language-Conditioned Visual Navigation [[HTML]](https://arxiv.org/html/2603.25981) [[PDF]](https://arxiv.org/pdf/2603.25981) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.25981`
* **Authors**: Amirhosein Chahe, Lifeng Zhou
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把 world model planning 从“单独做得更好”改成“由策略先给出可行起点再规划”。
* **问题与切口**: 语言条件视觉导航里，反应式策略通常能做局部控制，却缺少长时规划；纯 world model 规划又容易在高维动作空间里从一个糟糕初始分布开始采样。PiJEPA 的核心想法是让两者分工：先微调一个 Octo 系策略，在当前观测和语言条件下给出信息充分的动作分布；再在同一冻结视觉编码器的潜空间里，用 JEPA world model 预测未来状态，并用这个策略先验去 warm-start MPPI 规划。
* **核心方法与证据**: HTML 提供了较清晰的实验与实现细节。数据使用 CAST，且其 counterfactual instruction-action augmentation 被用来缓解策略忽视语言的 posterior collapse；动作被表示成 4 维位移与航向变化。作者比较 DINOv2 与 V-JEPA-2 两类冻结编码器，并让 policy 与 JEPA 共用表示空间。结论层面的主要证据是：该方法在两类编码器上都拿到更好的位置精度，同时呈现出“策略负责局部控制，规划补足长程定位”的分工。
* **正文要点**:
  - 两阶段框架中，策略先给出动作分布，再用该分布 warm-start MPPI 对 JEPA world model 做规划。
  - policy 与 world model 共用同一冻结视觉表征空间，并比较了 DINOv2 与 V-JEPA-2 两类编码器。
  - CAST 的 counterfactual 指令-动作增强被明确用于缓解语言被忽视的问题。
* **为什么值得跟**:
  - 它给出了策略与 world model 的清晰接口，而不是让两者互相替代。
  - 共享潜空间让模块化升级更可行，也更利于诊断到底是表征、策略还是规划出了问题。
  - 论文结论里的“策略管局部、规划管长程”是很有价值的系统分工判断。
* **风险 / 保留意见**:
  - 当前证据集中在导航，接触丰富的操作任务能否复用这套混合范式仍不明确。
  - MPPI 规划效果可能高度依赖采样分布、代价函数和潜空间预测质量，调参成本不低。
* **建议先看**: 先看策略先验如何进入 MPPI 采样与更新，再看 DINOv2 与 V-JEPA-2 的对比结果；这篇最值得抓住的是它如何把 policy prior 变成可用的 planning initializer。
* **关键词**: `World model planning` `JEPA` `MPPI` `Language-conditioned navigation` `Policy prior`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 策略先验具体如何参数化 MPPI 的采样分布与更新过程？
  - JEPA world model 是否显式接收语言条件，还是语言只通过策略先验进入规划？
  - 失败案例里主要瓶颈是潜空间动态预测、目标代价设计，还是策略初始化本身？
* **上传 PDF 后优先看**:
  - 两阶段方法与 MPPI 初始化机制
  - CAST 数据构造与动作/编码器表示
  - 基线比较与策略-规划分工分析

### [6]. ABot-PhysWorld: Interactive World Foundation Model for Robotic Manipulation with Physics Alignment [[PDF]](https://arxiv.org/pdf/2603.23376) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.23376`
* **Authors**: Yuzhi Chen, Ronghan Chen, Dongjie Huo, Yandan Yang, Dekang Qi, Haoyun Liu, Tong Lin, Shuang Zeng, Junjin Xiao, Xinyuan Chang, Feng Xiong, Xing Wei, Zhiheng Ma, Mu Xu
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把机器人 world model 的关键问题从“像不像”提升到“是否守物理、是否可控”。
* **问题与切口**: 很多视频 world model 在机器人操作里看起来像，但一遇到接触与受力就会出现穿模、反重力这类物理违规行为，根源在于训练数据偏通用视觉、目标函数偏似然拟合。ABot-PhysWorld 的切口很明确：做一个面向操作的交互式 world foundation model，在大规模操作视频上引入 physics-aware 标注，并把物理一致性作为后训练对齐目标，而不是只追求更真实的像素生成。
* **核心方法与证据**: 目前能确认的证据来自摘要回退。作者报告了一个 14B Diffusion Transformer，训练数据是三百万段带 physics-aware annotation 的操作视频；后训练采用基于 DPO 的框架，并用 decoupled discriminators 压制不符合物理的生成同时尽量保留视觉质量。另一个关键组件是 parallel context block，用于精确注入空间动作条件并支持 cross-embodiment control；同时提出训练独立的 EZSbench 评测泛化。具体实验协议和拆解仍需 PDF 核验。
* **正文要点**:
  - 摘要明确给出 14B 模型规模和三百万段带物理标注的操作视频数据。
  - DPO 式后训练配合 decoupled discriminators，目标是同时抑制物理违规行为并保留视觉质量。
  - parallel context block 与 EZSbench 说明作者同时关注动作可控性和训练独立的泛化评估。
* **为什么值得跟**:
  - 物理一致性是 world model 真正能服务规划、模拟和数据生成的前提，不是可有可无的加分项。
  - 把动作可控视频生成和 cross-embodiment control 放进同一框架，有机会连接 world model 与机器人控制。
  - 训练独立的评测基准如果设计扎实，会比只看自家训练分布内结果更有说服力。
* **风险 / 保留意见**:
  - 当前只有摘要证据，尚无法判断物理对齐是否真的改善了交互预测而不只是压掉明显伪影。
  - 模型规模、数据筛选和偏好对齐流程都很重，复现门槛和组件归因难度可能较高。
* **建议先看**: 上传 PDF 后，先核查 physics alignment 的偏好构造与 decoupled discriminators 的职责分工，再看 EZSbench 如何定义并测量物理泛化。若这两处站得住，这篇就不只是大模型叙事。
* **关键词**: `World foundation model` `Physics alignment` `Diffusion Transformer` `Action-controllable video` `DPO`
* **证据来源**: Abstract fallback
* **读 PDF 先核查**:
  - 物理违规样本如何定义、标注并进入 DPO 偏好学习？
  - parallel context block 在什么空间和粒度上注入动作条件？
  - EZSbench 如何把物理合理性、控制可用性与纯视觉逼真度区分开？
* **上传 PDF 后优先看**:
  - 数据与 physics-aware 对齐目标
  - 动作条件注入与 cross-embodiment 控制
  - EZSbench 评测协议与泛化分析

## Watchlist

### [W1]. Fast-dVLA: Accelerating Discrete Diffusion VLA to Real-Time Performance [[VIP]] [[HTML]](https://arxiv.org/html/2603.25661) [[PDF]](https://arxiv.org/pdf/2603.25661)
* **Paper ID**: `2603.25661`
* **Authors**: Wenxuan Song, Jiayi Chen, Shuai Chen, Jingbo Wang, Pengxiang Ding, Han Zhao, Yikai Qin, Xinhu Zheng, Donglin Wang, Yan Wang, Haoang Li
* **Author Priority**: Core VIP
* **为什么还值得留意**: 它进入 shortlist 的理由很充分：一方面由 Donglin Wang 这条核心作者线牵引，另一方面它直接处理离散扩散 VLA 最现实的部署瓶颈，即推理速度。HTML 里能看到作者不仅揭示了 bidirectional dVLA 隐含的 block-wise 自回归倾向，还给出 KV cache 复用、diffusion forcing、异步蒸馏和并行调度的一整套工程化方案。没有进最终精选，主要因为它更像一篇很强的系统加速论文，战略价值偏“让已有范式更可用”，而不是像 MMaDA-VLA、DFM-VLA 那样直接改写能力边界。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models [[VIP]] [[HTML]](https://arxiv.org/html/2603.25766) [[PDF]](https://arxiv.org/pdf/2603.25766)
* **Paper ID**: `2603.25766`
* **Authors**: Yiru Wang, Anqing Jiang, Shuo Wang, Yuwen Heng, Zichong Gu, Hao Sun
* **Author Priority**: Core VIP
* **为什么还值得留意**: 它进入 shortlist，是因为多帧多视角自动驾驶 VLA 的算力压力是真问题，而 ETA-VLA 用 Temporal Fusion Module 和 Intra-LLM Sparse Aggregator 给出了一条比较完整的 token 压缩路径。论文还在 NAVSIM v2 上报告了精度与 FLOPs 的同时收益，说明它不是只省算不保性能。之所以没进最终精选，是因为它更偏驾驶场景内的效率工程，和今天以机器人操作、鲁棒适应、world model 为主线的筛选标准相比，外延稍窄。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

### [W3]. Can Vision Foundation Models Navigate? Zero-Shot Real-World Evaluation and Lessons Learned [[HTML]](https://arxiv.org/html/2603.25937) [[PDF]](https://arxiv.org/pdf/2603.25937)
* **Paper ID**: `2603.25937`
* **Authors**: Maeva Guerrier, Karthik Soma, Jana Pavlasek, Giovanni Beltrame
* **Author Priority**: Standard
* **为什么还值得留意**: 它进入 shortlist，不是因为提出了新模型，而是因为真实世界双平台、五环境、五类 VNM 的系统性评测非常稀缺，而且论文明确指出碰撞、重复场景误判和图像扰动脆弱性这三类失效模式。没有进最终精选，主要因为今天更优先方法论文而不是评测论文；但对任何做导航 VLA 或 world model 的人来说，这篇都应当被当作部署约束来读，而不是可有可无的背景材料。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

### [W4]. DRUM: Diffusion-based Raydrop-aware Unpaired Mapping for Sim2Real LiDAR Segmentation [[HTML]](https://arxiv.org/html/2603.26263) [[PDF]](https://arxiv.org/pdf/2603.26263)
* **Paper ID**: `2603.26263`
* **Authors**: Tomoya Miyawaki, Kazuto Nakashima, Yumi Iwashita, Ryo Kurazume
* **Author Priority**: Standard
* **为什么还值得留意**: 它进入 shortlist，主要靠 Sim2Real 路线的清晰度：用在真实数据上预训练的 diffusion prior，把合成 LiDAR 翻译成更接近真实测量的范围图、反射强度和 raydrop 噪声，再服务下游语义分割。没有进最终精选，是因为它更偏感知域迁移和分割，而不是今天核心要盯的 VLA、world action 或操作型 world model。尽管如此，它仍然是把 diffusion 用到机器人 Sim2Real 感知侧的一个扎实样本。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)
