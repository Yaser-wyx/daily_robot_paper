# RoboPulse | 2026-04-17

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 57 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线很清楚：机器人学习正在从“直接把视觉和语言映射成动作”转向“在推理时补进规划、价值评估、状态抽象与结构化数据生成”，目标是把 VLA 真正推向复杂长时序与部署场景。入选的六篇分别补上了这条链路上的关键缺口：隐式规划、3D 表征稳定训练、抽象 sim2real、动态 affordance 推理、无需微调的测试时 steering，以及移动操作中的低成本示教扩增。它们进入最终精选，不是因为都已经给出决定性结论，而是因为方法切口清晰、问题定义扎实、且都直接回应“如何把泛化能力变成可部署能力”这个核心命题。VIP 作者里今天最值得优先跟踪的是 Donglin Wang，他的 WAV 直接落在 World Model + VLA 的交叉中心；其余核心名单在本批 final picks 中露出较少，后续更值得观察是否会出现 Levine、Finn、Abbeel、Sadigh 等团队的跟进工作。

## 今日信号

- VLA 研究正在从一步式 action decoding 转向带有 world model、value estimation 和 verifier 的 inference-time planning。
- Sim2Real 的问题定义正在上移：研究者不再只处理动力学参数失配，而开始正面处理抽象状态、形态差异与部分可观测性。
- 数据效率路线重新强调结构化先验，包括 3D 表征、TAMP 变换、affordance 约束和模态分工，而不是单纯追加示教数据。

## Editor's Picks

### [1]. World-Value-Action Model: Implicit Planning for Vision-Language-Action Systems [[VIP]] [[HTML]](https://arxiv.org/html/2604.14732) [[PDF]](https://arxiv.org/pdf/2604.14732) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.14732`
* **Authors**: Runze Li, Hongyin Zhang, Junxi Jin, Qixin Zeng, Zifeng Zhuang, Yiqi Tang, Shangke Lyu, Donglin Wang
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，它把 world model 和 value estimation 直接嵌进 VLA 推理链，代表了从“直接出动作”转向“隐式规划”的清晰升级。
* **问题与切口**: 这篇工作直指当前 VLA 的一个核心短板：大多数模型把决策拆成逐步动作预测，缺少对长时序后果的内部评估，因此在复杂操作里容易局部正确、整体失序。WAV 的切口不是外接显式规划器，而是在 VLA 内部学习可供“想一想再做”的未来轨迹潜结构，把世界演化、价值判断和动作生成打通，试图以更低推理代价获得更强的长期一致性与泛化能力。
* **核心方法与证据**: 从摘录可见，WAV 的方法脉络是先学习由视觉观测与语言指令条件化的未来轨迹潜表示，再由 learned world model 预测潜在未来演化，用 value model 评估长期效用，最后由 action model 产出可执行动作。证据主要来自 LIBERO 多套泛化测试、真实世界长时序操作、关于 latent trajectory planning 作用的消融，以及推理效率和内存开销分析；但摘录里没有给出更细的训练目标和定量幅度，因此具体增益仍需保守看待。
* **正文要点**:
  - 核心主张是用结构化潜变量表征未来轨迹，把 world model、value model 与 action model 放进统一 VLA 框架。
  - 实验问题覆盖 LIBERO 多类泛化、真实世界长时序操作、latent planning 贡献，以及推理效率与显存开销。
  - 方法强调 implicit planning 而非显式轨迹优化，试图避免传统规划在 VLA 中的搜索代价。
* **为什么值得跟**:
  - 如果这条路线成立，VLA 可以在不引入重型显式搜索的前提下获得更强的长时序决策能力。
  - 它把世界建模与价值评估重新带回 VLA 主干，代表了 World Action Model 方向的一个自然演化。
  - 这类隐式规划接口更容易与现有生成式动作头兼容，工程上比完全重做规划栈更可落地。
* **风险 / 保留意见**:
  - HTML 摘录没有展开 latent rollout 的训练细节，value 学习是否稳定、是否会误导动作选择仍不清楚。
  - 真实世界验证范围在摘录中描述较粗，复杂长时序能力是否能脱离特定任务设定复现，还需要看完整实验。
* **建议先看**: 先看方法部分里 latent trajectory、world model 与 value coupling 的关系，再看实验是否证明收益确实来自隐式规划，而不只是模型容量或训练配方变化。
* **关键词**: `VLA` `world model` `implicit planning` `value estimation` `robot manipulation`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)
* **读 PDF 先核查**:
  - value model 的监督信号到底来自回报估计、成功标签，还是某种自举式目标？
  - 潜在 world model 只预测未来 latent state，还是同时约束动作与观测重建一致性？
  - 推理时 action model 如何利用 value 信息做选择，是真正的候选排序还是更接近条件化解码？
* **上传 PDF 后优先看**:
  - 潜变量轨迹表示与训练目标章节
  - LIBERO 泛化与 latent planning 消融实验
  - 真实机器人长时序任务与推理效率分析

### [2]. R3D: Revisiting 3D Policy Learning [[HTML]](https://arxiv.org/html/2604.15281) [[PDF]](https://arxiv.org/pdf/2604.15281) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.15281`
* **Authors**: Zhengdong Hong, Shenrui Wu, Haozhe Cui, Boyi Zhao, Ran Ji, Yiyang He, Hangxing Zhang, Zundong Ke, Jun Wang, Guofeng Zhang, Jiayuan Gu
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它不是再堆 3D 模块，而是先定位 3D policy 失败根因，再给出一套更像“工程配方”的稳定扩展路线。
* **问题与切口**: 这篇工作重新审视 3D policy learning 为什么长期“看起来很合理、但总是训不稳也泛化差”。作者的核心判断是，以点云或 3D 场景为中心的策略本来有机会带来更好的视角泛化和跨本体迁移，但过去路线被训练配方拖累，导致强 3D 感知模型难以真正上桌。R3D 的新意在于把问题拆开：先找出失效来源，再给出一个面向规模化的 3D encoder + diffusion decoder 组合，让 3D 策略不再只是概念上优越。
* **核心方法与证据**: 这篇文章的价值首先在于诊断而不是单纯堆新模块。作者明确指出，3D policy 训练不稳和过拟合严重，关键原因在于 3D 数据增强缺位以及 BatchNorm 对这类设置的负面影响；在此基础上，构建了适合规模化的 transformer 3D encoder 与 diffusion decoder。证据来自 RoboTwin 2.0 与 ManiSkill2 两个常用基准，既看较干净环境，也看带强随机化的 Hard 设置，并覆盖不同时间尺度的任务；从摘录看，结论主要落在模拟环境中的稳定性和泛化提升。
* **正文要点**:
  - 论文把 3D policy learning 的主要失败根因归因于缺少 3D 数据增强以及 Batch Normalization 的副作用。
  - 提出的是 transformer-based 3D encoder 加 diffusion decoder 的组合，并明确为大规模稳定训练与预训练迁移设计。
  - 实验覆盖 RoboTwin 2.0 的 Easy/Hard 设置和 ManiSkill2 的短长时序任务，重点看泛化与稳健性。
* **为什么值得跟**:
  - 它把“3D policy 为什么没跑出来”讲得更具体，这对后续 3D-native VLA 很关键。
  - 如果稳定训练问题被解决，3D 表征有机会成为跨视角和跨机器人泛化的更强底座。
  - 这类工作比单次榜单提升更重要，因为它在定义未来 3D 机器人学习的默认训练范式。
* **风险 / 保留意见**:
  - 从摘录能看到的证据主要还是模拟评测，真实机器人上的转移价值目前证据不足。
  - 性能提升可能部分来自训练稳定化配方本身，而不完全来自更强的 3D 语义建模能力。
* **建议先看**: 先读失败诊断部分，确认作者为什么认为过去 3D policy 不稳定；再看新架构与训练配方，最后核对 Hard 设置下的收益是否真正支撑“3D 可规模化”。
* **关键词**: `3D policy learning` `point cloud` `diffusion policy` `transformer` `generalization`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 到底是哪类 3D augmentation 对性能和稳定性贡献最大，是否跨任务一致？
  - BatchNorm 被替换成了什么归一化或训练策略，收益来自哪里最明显？
  - 这些改进是否真的支撑 cross-embodiment transfer，还是主要提升了视角与域随机化泛化？
* **上传 PDF 后优先看**:
  - 失败诊断与训练不稳定分析章节
  - 3D encoder / decoder 设计与归一化策略
  - RoboTwin Hard 与 ManiSkill2 泛化对比实验

### [3]. Abstract Sim2Real through Approximate Information States [[HTML]](https://arxiv.org/html/2604.15289) [[PDF]](https://arxiv.org/pdf/2604.15289) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.15289`
* **Authors**: Yunfu Deng, Yuhao Li, Josiah P. Hanna
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把 sim2real 问题从“参数失配”推进到“抽象状态失配”，概念上更干净，也更贴近真实部署里常见的建模现实。
* **问题与切口**: 这篇工作处理的是一个比传统 sim2real 更棘手、但在工程上很常见的问题：模拟器为了便宜可用，往往采用比真实机器人更抽象的状态表示，于是训练域和部署域根本不共享同一套状态语义。作者据此提出 abstract sim2real，并强调这不再只是动力学参数校准问题，而是一个带部分可观测性的表示落差问题。ASTRA 的新意就在于把“抽象掉的信息如何在部署时补回来”作为核心对象，而不是默认模拟器足够忠实。
* **核心方法与证据**: 从摘录可见，ASTRA 的方法主轴是把抽象模拟器带来的部分可观测性显式化处理：作者提出 history-based grounding，让策略通过历史信息恢复抽象掉的关键因素，并学习一个 correction function，隐式补偿抽象状态到目标域之间的缺口。实验设计也围绕这个定义展开，不仅比较 Direct Transfer、Domain Randomization、COMPASS、RMA 等基线，还考察不同抽象程度下 grounding 与自预测状态表征的作用。结论声称 learned grounding 对形态变化也更稳，但真实机器人范围仍需谨慎解读。
* **正文要点**:
  - 论文把 sim2real 从“同一状态动作空间下的参数失配”推进到“抽象状态表征失配”的更一般问题。
  - ASTRA 的核心是历史依赖策略与 grounding correction，用来补偿抽象化时被丢掉的隐变量影响。
  - 实验横跨真实机器人任务，以及导航与 humanoid locomotion 的不同抽象层级设置。
* **为什么值得跟**:
  - 这条路线让低保真但高可用的抽象模拟器重新变得有价值，降低真实任务前期建模成本。
  - 它把 information state 与 grounding 问题带回 sim2real 讨论，理论上比纯随机化更有解释力。
  - 如果对形态变化也有效，这会比经典参数随机化更接近跨平台迁移的真实需求。
* **风险 / 保留意见**:
  - 摘录没有展开两个真实机器人任务的细节，当前还难判断其部署广度和失败模式。
  - 历史依赖的 grounding 可能对序列长度、传感延迟和未建模因素较敏感，训练与复现门槛不低。
* **建议先看**: 先把 formalization 读透，确认作者定义的 abstract sim2real 与传统 sim2real 差别在哪里；再看 grounding correction 与表征学习设计，最后重点核对抽象层级变化后各方法相对优势是否真的翻转。
* **关键词**: `Sim2Real` `abstract simulator` `information state` `recurrent policy` `grounding correction`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
* **读 PDF 先核查**:
  - approximate information state 是和策略联合学习，还是先独立学好再用于控制？
  - correction function 具体作用在抽象状态、观测历史还是动作输出层面？
  - 当抽象程度继续增大时，domain randomization 还剩多少作用，grounding 从哪里开始成为主导因素？
* **上传 PDF 后优先看**:
  - abstract sim2real 的问题定义与理论动机
  - grounding correction 与自预测状态表征章节
  - 真实机器人转移与抽象层级消融实验

### [4]. ADAPT: Benchmarking Commonsense Planning under Unspecified Affordance Constraints [[HTML]](https://arxiv.org/html/2604.14902) [[PDF]](https://arxiv.org/pdf/2604.14902) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.14902`
* **Authors**: Pei-An Chen, Yong-Ching Liang, Jia-Fong Yeh, Hung-Ting Su, Yi-Ting Chen, Min Sun, Winston Hsu
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把 embodied planning 的难点从“会不会按指令做”改成“先判断现在该不该这么做”，诊断意义很强。
* **问题与切口**: 这篇工作抓住了 embodied agent 一个经常被忽略的现实问题：指令在语言上成立，不代表当前环境里就真的可执行。物体是否可用、是否需要先清洁或加热、是否满足隐含前提，往往决定了后续计划是否合理。作者因此提出 DynAfford 来系统测这类能力，并用 ADAPT 在决策时显式处理“动作能否执行”和“若不能该如何保留任务意图地改做”这两个问题，相比传统失败后重规划，更像是在计划执行接口上补了一层常识判断。
* **核心方法与证据**: 这篇工作的证据主要分成两层。第一层是 DynAfford 这个 benchmark：作者在 AI2-THOR 2.0 中构造了动态家庭环境，让物体可用性随状态变化而变化，且这些前提并不直接写进指令。第二层是 ADAPT 这个 decision-time inference 机制，它把动作执行建模为受潜在前提约束的过程，并在单一决策链路中包含 affordance inference 与 applicability resolution 两个阶段。摘录里没有给出具体胜负数据，但实验目标和数据构成已经足以看出其诊断意图非常明确。
* **正文要点**:
  - DynAfford 被构造成诊断型 benchmark，专门隔离“隐含前提不满足”这一类动态 affordance 失败。
  - ADAPT 在决策时先判断计划动作是否可执行，再在必要时选择保留任务意图的替代动作。
  - 数据侧给出了 2,628 条专家示教、10,106 条语言标注、57 个场景和六类家居任务。
* **为什么值得跟**:
  - 它让 embodied planning 的评估更接近真实家庭任务，而不是只测指令跟随。
  - ADAPT 这类决策时 affordance 检查机制，很适合作为现有 VLA 的外接安全层或恢复层。
  - 如果 benchmark 被广泛采用，领域会更容易区分“会说会做”和“真的理解当前可执行性”的系统。
* **风险 / 保留意见**:
  - 摘录未展示完整结果表，因此不同 agent family 上的泛化强度目前还不能下定论。
  - AI2-THOR 的诊断价值很高，但与真实家居操作中的感知噪声和接触误差仍有距离。
* **建议先看**: 先看 benchmark 设计与任务分布，确认它到底在测什么；再看 ADAPT 如何把可执行性判断和替代动作选择放进同一决策流程，最后核对实验是否真在测 commonsense recovery 而不是语言模板记忆。
* **关键词**: `affordance reasoning` `embodied planning` `commonsense` `benchmark` `AI2-THOR`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 潜在 precondition 在实现中是如何被表征和判定的，是否依赖显式状态标签？
  - 当 ADAPT 替换原计划动作时，怎样保证保留的是任务级意图而不是局部贪心修补？
  - 对更强的 VLM/VLA 代理，ADAPT 的增益是否仍然稳定，还是主要帮助较弱的规划器？
* **上传 PDF 后优先看**:
  - benchmark 构建、任务类型与 violation taxonomy
  - ADAPT 的 affordance inference / applicability resolution 机制
  - 不同 embodied agent 的对比与失败恢复分析

### [5]. Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion [[HTML]](https://arxiv.org/html/2511.14178) [[PDF]](https://arxiv.org/pdf/2511.14178) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2511.14178`
* **Authors**: Zhuo Li, Junjia Liu, Zhipeng Dong, Tao Teng, Quentin Rouxel, Darwin Caldwell, Fei Chen
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它给“无需微调就把预训练 VLA 带上机器人”提供了一条可操作的 inference-time 路线。
* **问题与切口**: 这篇工作切中的是真实部署里一个很实际的问题：预训练 VLA 往往不是“不会”，而是落到具体机器人和具体任务时，采样出来的动作不够可靠，于是大家被迫重新收数据做微调。VLA-Pilot 试图把这一步前移到推理时，通过开放世界验证和搜索式动作细化，在不改动底层权重的前提下提升零样本部署表现。它的创新点不在于再训练一个更大的策略，而在于把 VLA 推理过程重新组织成一个可校验、可筛选、可闭环修正的过程。
* **核心方法与证据**: 从摘录看，VLA-Pilot 的关键思路是把“部署失败”当成推理时决策偏移，而不是立即回到数据收集与微调。具体做法是让 MLLM 充当开放世界 verifier，配合 evolutionary diffusion 在推理时对动作候选进行迭代筛选和优化，并通过闭环机制持续修正。实验覆盖模拟与真实世界，且明确比较了 steering baseline、直接 fine-tuning、cross-embodiment generalization、组件贡献和推理延迟。作者还给出了 GPT-4o、候选规模和搜索步数等实现线索，但更细的成本收益仍需看全文。
* **正文要点**:
  - 方法强调 plug-and-play inference-time steering，不需要额外微调或新示教数据。
  - 核心组件包括 MLLM 驱动的 EPS-CoT、evolutionary diffusion 动作细化，以及闭环在线修正。
  - 实验问题覆盖下游任务提升、与 steering baseline 和 fine-tuning 对比、跨本体泛化、消融和延迟。
* **为什么值得跟**:
  - 它提供了比重新微调更轻量的部署方案，现实吸引力很强。
  - 这类 test-time steering 把生成式策略和规划式搜索重新接上，对未来 VLA 很可能是重要方向。
  - 如果跨本体泛化证据成立，它意味着部署适配可以更多依靠推理而非再训练。
* **风险 / 保留意见**:
  - 对外部 MLLM verifier 的依赖可能带来显著的时延、成本与稳定性问题。
  - 摘录虽声称可逼近一定 fine-tuning 效果，但长期闭环稳定性与失败恢复边界仍缺少细节支撑。
* **建议先看**: 先看作者如何定义预训练 VLA 在部署时的失败来源，再读 verifier + search 的闭环机制，最后重点核对它与直接 fine-tuning 的比较和延迟代价。
* **关键词**: `VLA` `inference-time steering` `evolutionary diffusion` `MLLM verifier` `zero-shot deployment`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
* **读 PDF 先核查**:
  - EPS-CoT 在验证动作时到底读取哪些观测证据，如何避免只靠语言常识打分？
  - 性能对候选数量、搜索步数和 MLLM 温度有多敏感，延迟拐点在哪里？
  - 当 steering 与基础 VLA 分布明显冲突时，系统如何避免长时序中的局部修正反而放大误差？
* **上传 PDF 后优先看**:
  - inference-time steering 算法与 verifier 接口
  - 与基线及 fine-tuning 的对比、cross-embodiment 结果
  - 延迟分析与核心模块消融

### [6]. DockAnywhere: Data-Efficient Visuomotor Policy Learning for Mobile Manipulation via Novel Demonstration Generation [[HTML]](https://arxiv.org/html/2604.15023) [[PDF]](https://arxiv.org/pdf/2604.15023) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.15023`
* **Authors**: Ziyu Shan, Yuheng Zhou, Gaoyuan Wu, Ziheng Ji, Zhenyu Wu, Ziwei Wang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它切中了移动操作里最常见但常被低估的 docking 偏差问题，而且用的是很节省数据的生成式补强思路。
* **问题与切口**: 这篇工作关注移动操作里一个非常具体但普遍存在的问题：导航阶段哪怕只带来小幅 docking 偏差，后续固定基座式 visuomotor policy 看到的画面就可能完全偏掉，导致原本在单一停靠点上学到的技能迅速失效。DockAnywhere 的切口非常务实，它不要求重新大量采集移动操作数据，而是把少量源示教“抬升”为多个可行停靠配置下的新示教，再配套合成新观测，从而用结构化扩增来补足视角泛化缺口。
* **核心方法与证据**: DockAnywhere 的方法核心不是换一个更大的策略，而是用结构化生成扩展训练数据。作者先解析源轨迹，把与底座停靠位置强相关的运动段和较稳定的技能段拆开，再用 TAMP 风格的空间变换把示教迁移到新的 docking 点；随后用 3D 点云级编辑合成对应视觉观测，以形成新的 observation-action 序列。证据来自 ManiSkill 中五个递进式移动操作任务、对静态基线和数据增强基线的比较、组件消融，以及真实世界部署验证；摘录中还给出每个任务只需少量源示教这一关键信号。
* **正文要点**:
  - 方法先把源示教拆成 docking 相关的低精度运动段与相对稳定的技能段，再做空间变换生成新轨迹。
  - 视觉侧通过 3D 点云的 point-level editing 合成新观测，并用第三人称视角减轻 docking 偏差带来的观测错位。
  - 实验在 ManiSkill 中构造多种非理想 docking 场景，随后做消融并验证真实世界泛化。
* **为什么值得跟**:
  - 它直接面向移动操作最常见的部署误差，工程价值很高。
  - 方法把 TAMP 的结构先验和 imitation learning 的数据需求连接起来，思路比单纯图像增强更扎实。
  - 如果低成本示教扩增有效，移动底盘与操控臂之间的系统耦合问题就更容易被数据化解决。
* **风险 / 保留意见**:
  - 如果任务成功高度依赖细粒度接触过程，几何式轨迹迁移和观测合成可能不足以保持可执行性。
  - 当前证据主要围绕 docking 引发的视角变化，其他移动操作误差源是否同样受益还不清楚。
* **建议先看**: 先看示教分解与 TAMP 变换是怎么把单点示教扩展成多 docking 配置的，再看观测合成是否足够物理可信，最后核对真实部署里泛化收益是不是主要来自视角设计还是数据生成本身。
* **关键词**: `mobile manipulation` `data augmentation` `demonstration generation` `docking variability` `TAMP`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 轨迹中的 motion segment 与 skill segment 是如何稳定切分的，遇到噪声示教会不会失效？
  - 第三人称观测相对第一人称的优势有多依赖相机标定和场景可视性？
  - 经过空间变换后的轨迹在接触时序和可执行性上如何验证，没有被“几何上能改、动力学上不能做”拖垮吗？
* **上传 PDF 后优先看**:
  - 示教解析与 TAMP-based trajectory relocation
  - 3D 点云观测合成与第三人称观测设计
  - docking shift 泛化、基线对比与真实部署

## Watchlist

### [W1]. Emergent Neural Automaton Policies: Learning Symbolic Structure from Visuomotor Trajectories [[HTML]](https://arxiv.org/html/2603.25903) [[PDF]](https://arxiv.org/pdf/2603.25903)
* **Paper ID**: `2603.25903`
* **Authors**: Yiyuan Pan, Xusheng Luo, Hanjiang Hu, Peiqi Yu, Changliu Liu
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇进入 shortlist，主要因为它试图从 visuomotor demonstrations 中自动抽取状态机，让长时序控制重新获得可解释的离散结构，这对 long-horizon robotics 很有研究味道。它没有进最终精选，是因为当前主线更偏向 VLA、world model、sim2real 与部署导向的方法，而 ENAP 更像是神经符号层面的结构学习。另一个保守点是，摘录里的核心证据仍以结构提取与控制效果为主，和今天的 VLA/World Action Model 主轴连接还不够直接。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. Flow with the Force Field: Learning 3D Compliant Flow Matching Policies from Force and Demonstration-Guided Simulation Data [[HTML]](https://arxiv.org/html/2510.02738) [[PDF]](https://arxiv.org/pdf/2510.02738)
* **Paper ID**: `2510.02738`
* **Authors**: Tianyu Li, Yihan Li, Zizhe Zhang, Nadia Figueroa
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇值得跟踪，因为它把力觉、顺应性和 3D visuomotor policy 放到同一条 sim2real 管线上，对接触丰富任务非常关键。没进最终精选，主要是题目更聚焦于 compliant manipulation 的专门场景，和今天更核心的 VLA、world/value/action、抽象 sim2real 主线相比略窄。再加上方法较依赖仿真中的特权信息与定制数据生成，当前更像一条强应用路线而非通用范式。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. Multi-Modal Manipulation via Multi-Modal Policy Consensus [[HTML]](https://arxiv.org/html/2509.23468) [[PDF]](https://arxiv.org/pdf/2509.23468)
* **Paper ID**: `2509.23468`
* **Authors**: Haonan Chen, Jiaming Xu, Hongyu Chen, Kaiwen Hong, Binghao Huang, Chaoqi Liu, Jiayuan Mao, Yunzhu Li, Yilun Du, Katherine Driggs-Campbell
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇进入 shortlist，是因为它没有沿用常见的 feature concatenation，而是把多模态操作策略拆成按模态分工的 diffusion experts，再用 router 学习共识权重，设计上很干净。它没有进入最终精选，原因是今天的焦点更偏 VLA、sim2real、world model 和部署规划，而这篇更像“多传感器融合范式升级”。从摘录看，方法潜力不错，但目前与长时序规划或 world-action 建模的耦合还不够强。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. IROSA: Interactive Robot Skill Adaptation using Natural Language [[HTML]](https://arxiv.org/html/2603.03897) [[PDF]](https://arxiv.org/pdf/2603.03897)
* **Paper ID**: `2603.03897`
* **Authors**: Markus Knauer, Samuel Bustamante, Thomas Eiband, Alin Albu-Schäffer, Freek Stulp, João Silvério
* **Author Priority**: Standard
* **为什么还值得留意**: IROSA 值得保留在 watchlist，因为它把自然语言技能调整落到了工业场景里，并通过工具调用和保护性抽象层处理安全与可验证性，这一点很务实。它没有进入最终精选，是因为贡献重心更偏系统集成和技能参数化适配，而不是今天更优先的 VLA 核心建模、sim2real 抽象迁移或 world model 路线。换句话说，这是一篇很好的工业接口论文，但研究前沿性不如 final picks 那么集中。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
