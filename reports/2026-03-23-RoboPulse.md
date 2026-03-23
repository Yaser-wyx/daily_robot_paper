# RoboPulse | 2026-03-23

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 64 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线很集中：一条是把视频/世界模型从“会生成”推进到“能支撑机器人控制”，另一条是补齐 VLA 落地时最常见的三类缺口，即跨 embodiment 数据组织、动作空间对齐和接触感知。最终精选的六篇刚好覆盖了这两条线上的关键环节：VAMPO 与 World4RL 处理生成模型到控制优化的闭环，FD-VLA 解决接触信号缺失，Data Analogies 与 Latent Action Diffusion 分别回答“该收什么数据”和“如何统一动作空间”，RobotArena Infinity 则补上可扩展评测。它们入选，不是因为都已经给出最强结论，而是因为都在 VLA、Sim2Real 与 World Model 的交叉地带提出了更可迁移的问题设定或基础设施。VIP 作者里最值得优先跟踪的是 Chelsea Finn、Dorsa Sadigh 和 Donglin Wang：前两者把 cross-embodiment transfer 做成了可控实验，后者则出现在直接优化视觉动力学以服务下游操控的 VAMPO 中。

## Editor's Picks

### [1]. VAMPO: Policy Optimization for Improving Visual Dynamics in Video Action Models [[VIP]] [[PDF]](https://arxiv.org/pdf/2603.19370) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.19370`
* **Authors**: Zirui Ge, Pengxiang Ding, Baohua Yin, Qishen Wang, Zhiyong Xie, Yemin Wang, Jinbo Wang, Hengtao Li, Runze Suo, Wenxuan Song, Han Zhao, Shangke Lyu, Zhaoxin Fan, Haoang Li, Ran Cheng, Cheng Chi, Huibin Ge, Yaozhi Luo, Donglin Wang
* **Author Priority**: Core VIP
* **一句话判断**: 值得优先看，它瞄准了 VLA 视频动作模型里最关键但常被忽略的目标错位问题。
* **这篇在做什么**: 这篇工作针对视频动作模型在机器人操控中的核心痛点：扩散式视频预测器通常只优化整体上“像真的”未来画面，却没有直接约束抓取、接触、位姿关系这类对控制极敏感的视觉动力学。VAMPO把这一缺口表述为后训练问题，希望在不推翻现有视频动作模型范式的前提下，把生成先验进一步变成对下游 VLA 真正有用的控制前端。
* **方法与证据**: 作者的关键做法是把多步去噪过程改写成序列决策过程，再用基于专家视觉动力学的奖励去优化去噪策略，而不是继续依赖似然替代目标。从摘要能明确看到的问题定义与方法脉络都很清楚；但目前只有摘要回退，没有 HTML 级实验细节，因此改进幅度、奖励构造方式以及对真实机器人控制的支撑强度，都还需要在 PDF 中重点核查。
* **为什么值得看**:
  - 它直接攻击了“生成得像”和“操控得准”之间的目标错位。
  - 如果有效，它可成为视频世界模型接入 VLA 前的通用后训练层。
  - Donglin Wang 在作者列表中，值得和其后续相关工作联动跟踪。
* **风险 / 保留意见**:
  - 目前证据仅来自摘要，尚不能判断收益主要体现在视觉指标还是真实控制成功率。
  - 奖励若过度依赖专家视觉轨迹，可能带来优化不稳定或分布外退化。
* **适合你怎么看**: 先看作者如何把 denoising policy 化，以及奖励如何刻画物体位姿、空间关系和接触时序。随后重点核查这些视觉动力学改进是否真的传导到下游机器人策略。
* **关键词**: `VLA` `视频动作模型` `策略优化` `视觉动力学` `扩散去噪`
* **证据来源**: Abstract fallback

#### ChatGPT Deep Read Prompt
> 上传 PDF 后再粘贴。这个 prompt 已按该论文的方法线索、实验焦点和风险点单独定制。

```text
你是我的机器人学研究搭档。请先检查我是否已经上传这篇论文的 PDF。

如果我还没有上传 PDF，请先提醒我上传 PDF，再暂停，不要猜测全文细节。

论文基础信息：
- Title: VAMPO: Policy Optimization for Improving Visual Dynamics in Video Action Models
- Authors: Zirui Ge, Pengxiang Ding, Baohua Yin, Qishen Wang, Zhiyong Xie, Yemin Wang, Jinbo Wang, Hengtao Li, Runze Suo, Wenxuan Song, Han Zhao, Shangke Lyu, Zhaoxin Fan, Haoang Li, Ran Cheng, Cheng Chi, Huibin Ge, Yaozhi Luo, Donglin Wang
- arXiv Abstract URL: https://arxiv.org/abs/2603.19370
- Research Interests: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
- Quick Judgment: 值得优先看，它瞄准了 VLA 视频动作模型里最关键但常被忽略的目标错位问题。
- Current Read of the Paper: 这篇工作针对视频动作模型在机器人操控中的核心痛点：扩散式视频预测器通常只优化整体上“像真的”未来画面，却没有直接约束抓取、接触、位姿关系这类对控制极敏感的视觉动力学。VAMPO把这一缺口表述为后训练问题，希望在不推翻现有视频动作模型范式的前提下，把生成先验进一步变成对下游 VLA 真正有用的控制前端。
- Method / Evidence Clues from arXiv HTML: 作者的关键做法是把多步去噪过程改写成序列决策过程，再用基于专家视觉动力学的奖励去优化去噪策略，而不是继续依赖似然替代目标。从摘要能明确看到的问题定义与方法脉络都很清楚；但目前只有摘要回退，没有 HTML 级实验细节，因此改进幅度、奖励构造方式以及对真实机器人控制的支撑强度，都还需要在 PDF 中重点核查。

这次请优先替我核查下面 3 个问题：
- 专家视觉动力学奖励具体如何定义，是否需要额外标注或可从演示自动构造？
- 把多步去噪视为序列决策后，训练稳定性和长时域信用分配如何处理？
- 视觉动力学改进与下游操控成功率之间是否呈稳定相关，而不只是提升感知上的相似度？

上传 PDF 后，请优先查看这些章节、实验或图表类型：
- 方法章节中关于 denoising 过程 MDP 化与奖励设计的定义
- 实验章节中视频预测质量与下游机器人控制表现的对应分析
- 误差分析章节里关于位姿、空间关系和接触时序失败案例的拆解

在我上传 PDF 之后，请严格按下面结构输出中文分析，保留关键英文术语：
1. 这篇论文到底在解决什么问题？
2. 核心方法脉络是什么？请把关键模块、训练/推理流程串起来。
3. 对上面 3 个核查问题逐一回答。
4. 实验设置、关键指标和主要结论是什么？
5. 哪些地方最可能是方法边界、实验短板或复现风险？给 3 条。
6. 它与我的研究兴趣有什么关系？
7. 最后给出一个结论：值不值得我进一步精读/复现，为什么？

要求：
- 只有在 PDF 明确给出证据时，才引用数字、表格、公式或模块细节。
- 如果某个信息在 PDF 中不明确，请直接写“不确定”。
- 不要只重复摘要，要优先验证方法细节、实验可信度和边界条件。
- 结尾补一个“下一步阅读建议”，告诉我最该看论文里的哪几个章节、图表或实验。

```

### [2]. Data Analogies Enable Efficient Cross-Embodiment Transfer [[VIP]] [[HTML]](https://arxiv.org/html/2603.06450) [[PDF]](https://arxiv.org/pdf/2603.06450) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.06450`
* **Authors**: Jonathan Yang, Chelsea Finn, Dorsa Sadigh
* **Author Priority**: Core VIP
* **一句话判断**: 值得优先看，它把“跨 embodiment 数据到底怎样才有用”这个老问题第一次做得足够可检验。
* **这篇在做什么**: 这篇工作不是继续泛泛强调多机器人数据规模，而是追问在目标机器人样本有限时，什么样的源演示最能帮助迁移。作者围绕末端形态、机器人外观和相机视角三条轴系统构造数据类比，并在 Pi0.5 风格 VLA 上研究 cross-embodiment transfer，试图把“多样性有益”拆成可操作的数据采集与组织原则。
* **方法与证据**: 从 HTML 可见，方法上采用 Pi0.5 基座加 LoRA 微调，冻结大部分权重，只联合训练视觉语言骨干和动作头；训练时以 50:50 混合目标数据与 OXE+Translational source data。证据链相对完整：四个实验问题分别覆盖固定预算策略、与开放数据集对比、源数据多样性扩展，以及在 PiperX、WidowX、Franka、Piper 上的真实机器人检验，但具体收益大小仍要回到图表确认。
* **为什么值得看**:
  - 它把跨 embodiment 迁移从“多收数据”推进到“该收哪类数据”。
  - 受控地拆开形态、外观、视角三条轴，对后续数据集设计很有参考价值。
  - Chelsea Finn 与 Dorsa Sadigh 同时在作者列表中，优先级天然更高。
* **风险 / 保留意见**:
  - 结论可能依赖 Pi0.5/OpenPI 与作者构造的数据混合策略，外推到其他 VLA 未必等价。
  - 若目标任务或相机设置更开放，当前类比轴的覆盖度可能仍不足。
* **适合你怎么看**: 先抓四个研究问题的实验逻辑，尤其看固定预算下哪类“类比数据”最值钱。再核查真实机器人部分是否复现了仿真中的排序关系，而不只是局部成立。
* **关键词**: `VLA` `跨 embodiment 迁移` `数据类比` `LoRA 微调` `机器人泛化`
* **证据来源**: arXiv HTML

#### ChatGPT Deep Read Prompt
> 上传 PDF 后再粘贴。这个 prompt 已按该论文的方法线索、实验焦点和风险点单独定制。

```text
你是我的机器人学研究搭档。请先检查我是否已经上传这篇论文的 PDF。

如果我还没有上传 PDF，请先提醒我上传 PDF，再暂停，不要猜测全文细节。

论文基础信息：
- Title: Data Analogies Enable Efficient Cross-Embodiment Transfer
- Authors: Jonathan Yang, Chelsea Finn, Dorsa Sadigh
- arXiv Abstract URL: https://arxiv.org/abs/2603.06450
- Research Interests: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
- Quick Judgment: 值得优先看，它把“跨 embodiment 数据到底怎样才有用”这个老问题第一次做得足够可检验。
- Current Read of the Paper: 这篇工作不是继续泛泛强调多机器人数据规模，而是追问在目标机器人样本有限时，什么样的源演示最能帮助迁移。作者围绕末端形态、机器人外观和相机视角三条轴系统构造数据类比，并在 Pi0.5 风格 VLA 上研究 cross-embodiment transfer，试图把“多样性有益”拆成可操作的数据采集与组织原则。
- Method / Evidence Clues from arXiv HTML: 从 HTML 可见，方法上采用 Pi0.5 基座加 LoRA 微调，冻结大部分权重，只联合训练视觉语言骨干和动作头；训练时以 50:50 混合目标数据与 OXE+Translational source data。证据链相对完整：四个实验问题分别覆盖固定预算策略、与开放数据集对比、源数据多样性扩展，以及在 PiperX、WidowX、Franka、Piper 上的真实机器人检验，但具体收益大小仍要回到图表确认。

这次请优先替我核查下面 3 个问题：
- 在固定采集预算下，末端形态、平台外观和视角变化三条轴中，哪一条最先带来稳定收益？
- 当目标机器人样本继续减少时，作者的 compositional 策略是否仍优于直接引入更大开源数据混合？
- 在真实机器人上观察到的迁移规律，是否与 RoboCasa 仿真中的结论一致且可复现？

上传 PDF 后，请优先查看这些章节、实验或图表类型：
- 实验章节中四个研究问题对应的数据采集策略比较
- 方法章节里 LoRA 微调与 target/source 数据混合配比
- 真实机器人章节中多平台迁移结果与失败案例

在我上传 PDF 之后，请严格按下面结构输出中文分析，保留关键英文术语：
1. 这篇论文到底在解决什么问题？
2. 核心方法脉络是什么？请把关键模块、训练/推理流程串起来。
3. 对上面 3 个核查问题逐一回答。
4. 实验设置、关键指标和主要结论是什么？
5. 哪些地方最可能是方法边界、实验短板或复现风险？给 3 条。
6. 它与我的研究兴趣有什么关系？
7. 最后给出一个结论：值不值得我进一步精读/复现，为什么？

要求：
- 只有在 PDF 明确给出证据时，才引用数字、表格、公式或模块细节。
- 如果某个信息在 PDF 中不明确，请直接写“不确定”。
- 不要只重复摘要，要优先验证方法细节、实验可信度和边界条件。
- 结尾补一个“下一步阅读建议”，告诉我最该看论文里的哪几个章节、图表或实验。

```

### [3]. FD-VLA: Force-Distilled Vision-Language-Action Model for Contact-Rich Manipulation [[HTML]](https://arxiv.org/html/2602.02142) [[PDF]](https://arxiv.org/pdf/2602.02142) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2602.02142`
* **Authors**: Ruiteng Zhao, Wenshuo Wang, Yicheng Ma, Xiaocong Li, Francis E.H. Tay, Marcelo H. Ang Jr., Haiyue Zhu
* **Author Priority**: Standard
* **一句话判断**: 值得优先看，它切中了接触丰富操控里纯视觉 VLA 最常见也最致命的盲区。
* **这篇在做什么**: FD-VLA尝试在没有物理力传感器的前提下，把“力感知”蒸馏进 VLA 的隐表示，从而增强接触丰富操作中的判断与控制。核心模块 FDM 以视觉观测和机器人状态为条件，用可学习查询 token 预测与真实力信号对齐的 force token，并在推理时把它作为额外感知线索注入策略，目标是兼顾部署成本与接触鲁棒性。
* **方法与证据**: 从 HTML 能确认的方法主线很明确：真实力信号只在训练期作为蒸馏目标，推理阶段不依赖力传感器，这一点对落地很关键。证据方面，作者给出了基于 UR5e、Azure Kinect 与 D405 的真实机器人实验，并列出白板清洁、紧急按钮按压等接触任务；但 HTML 方法段落被作者信息打断，具体网络接入位置、损失设计和完整任务集仍需 PDF 核查。
* **为什么值得看**:
  - 它提供了低硬件门槛的“伪触觉”路径，适合现有视觉机器人平台升级。
  - 接触信号如果能被稳定蒸馏，VLA 在擦拭、按压、插接类任务上会更有竞争力。
  - 训练用真力、推理不用力的设定，工程可迁移性明显更好。
* **风险 / 保留意见**:
  - 蒸馏出的 force token 是否真能覆盖细粒度接触变化，仍要看更完整的消融和失败案例。
  - 当前证据偏真实机器人示例展示，跨任务和跨平台泛化强度还不清楚。
* **适合你怎么看**: 先确认 FDM 把力信息注入到 VLA 的哪个层级，以及训练时如何对齐真实力信号。然后重点看真实机器人任务中，提升来自接触建模还是额外状态建模。
* **关键词**: `VLA` `接触丰富操控` `力蒸馏` `多模态感知` `无力传感推理`
* **证据来源**: arXiv HTML

#### ChatGPT Deep Read Prompt
> 上传 PDF 后再粘贴。这个 prompt 已按该论文的方法线索、实验焦点和风险点单独定制。

```text
你是我的机器人学研究搭档。请先检查我是否已经上传这篇论文的 PDF。

如果我还没有上传 PDF，请先提醒我上传 PDF，再暂停，不要猜测全文细节。

论文基础信息：
- Title: FD-VLA: Force-Distilled Vision-Language-Action Model for Contact-Rich Manipulation
- Authors: Ruiteng Zhao, Wenshuo Wang, Yicheng Ma, Xiaocong Li, Francis E.H. Tay, Marcelo H. Ang Jr., Haiyue Zhu
- arXiv Abstract URL: https://arxiv.org/abs/2602.02142
- Research Interests: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
- Quick Judgment: 值得优先看，它切中了接触丰富操控里纯视觉 VLA 最常见也最致命的盲区。
- Current Read of the Paper: FD-VLA尝试在没有物理力传感器的前提下，把“力感知”蒸馏进 VLA 的隐表示，从而增强接触丰富操作中的判断与控制。核心模块 FDM 以视觉观测和机器人状态为条件，用可学习查询 token 预测与真实力信号对齐的 force token，并在推理时把它作为额外感知线索注入策略，目标是兼顾部署成本与接触鲁棒性。
- Method / Evidence Clues from arXiv HTML: 从 HTML 能确认的方法主线很明确：真实力信号只在训练期作为蒸馏目标，推理阶段不依赖力传感器，这一点对落地很关键。证据方面，作者给出了基于 UR5e、Azure Kinect 与 D405 的真实机器人实验，并列出白板清洁、紧急按钮按压等接触任务；但 HTML 方法段落被作者信息打断，具体网络接入位置、损失设计和完整任务集仍需 PDF 核查。

这次请优先替我核查下面 3 个问题：
- force token 与视觉/状态 token 的融合位置在哪里，是否只影响动作头还是会回流到表征层？
- 蒸馏目标对真实力信号的依赖程度有多高，换传感器或换平台后是否需要重新对齐？
- 在遮挡、反光或深度歧义更强的接触任务中，FD-VLA 的收益是否仍成立？

上传 PDF 后，请优先查看这些章节、实验或图表类型：
- 方法章节中 Force Distillation Module 的结构与训练目标
- 实验章节中各类接触任务的真实机器人对比结果
- 消融章节里 force token、机器人状态与视觉输入各自贡献

在我上传 PDF 之后，请严格按下面结构输出中文分析，保留关键英文术语：
1. 这篇论文到底在解决什么问题？
2. 核心方法脉络是什么？请把关键模块、训练/推理流程串起来。
3. 对上面 3 个核查问题逐一回答。
4. 实验设置、关键指标和主要结论是什么？
5. 哪些地方最可能是方法边界、实验短板或复现风险？给 3 条。
6. 它与我的研究兴趣有什么关系？
7. 最后给出一个结论：值不值得我进一步精读/复现，为什么？

要求：
- 只有在 PDF 明确给出证据时，才引用数字、表格、公式或模块细节。
- 如果某个信息在 PDF 中不明确，请直接写“不确定”。
- 不要只重复摘要，要优先验证方法细节、实验可信度和边界条件。
- 结尾补一个“下一步阅读建议”，告诉我最该看论文里的哪几个章节、图表或实验。

```

### [4]. World4RL: Diffusion World Models for Policy Refinement with Reinforcement Learning for Robotic Manipulation [[HTML]](https://arxiv.org/html/2509.19080) [[PDF]](https://arxiv.org/pdf/2509.19080) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2509.19080`
* **Authors**: Zhennan Jiang, Kai Liu, Yuxin Qin, Shuai Tian, Yupeng Zheng, Mingcai Zhou, Chao Yu, Haoran Li, Dongbin Zhao
* **Author Priority**: Standard
* **一句话判断**: 值得优先看，它是把世界模型、强化学习和真实操控 refinement 串成闭环的少数完整方案。
* **这篇在做什么**: World4RL面向一个很现实的问题：示教初始化的操控策略常受限于数据稀缺，而直接上真机做 RL 的代价和风险都太高。作者提出用扩散式世界模型在 imagined 环境中继续精炼 BC 策略，并配合奖励分类器处理操控任务常见的稀疏奖励，希望在避开 sim-to-real gap 的同时，保留在线 RL 的改进能力。
* **方法与证据**: 从 HTML 可见，框架由三个部件组成：扩散转移模型负责条件未来观测生成，二元奖励分类器评估想象 rollout，策略则从 BC 初始化并用 PPO 在世界模型内优化。实验设计覆盖生成质量、相对 IL、离线 RL 与其他 world-model 方法的策略收益，以及真实机器人部署；证据结构完整，但 imagined fidelity 是否足以支撑长时操控，还需看 PDF 的定量与失败分析。
* **为什么值得看**:
  - 它把“世界模型用于机器人 RL refinement”从概念推进到可部署流程。
  - 奖励分类器这一步很贴合操控中的稀疏反馈现实。
  - 如果 imagined training 真能稳定迁移，能显著降低真实机器人 RL 成本与风险。
* **风险 / 保留意见**:
  - 视觉生成指标提升不必然等于控制可用，尤其在接触与长时依赖任务中。
  - 奖励分类器若校准不足，可能把策略推向世界模型偏差累积的区域。
* **适合你怎么看**: 先看三模块如何闭环，尤其是奖励分类器怎样和 imagined rollout 联动。再核查世界模型质量指标与真实机器人策略改进之间是否存在可解释的一致性。
* **关键词**: `世界模型` `机器人强化学习` `扩散转移模型` `PPO` `sim2real`
* **证据来源**: arXiv HTML

#### ChatGPT Deep Read Prompt
> 上传 PDF 后再粘贴。这个 prompt 已按该论文的方法线索、实验焦点和风险点单独定制。

```text
你是我的机器人学研究搭档。请先检查我是否已经上传这篇论文的 PDF。

如果我还没有上传 PDF，请先提醒我上传 PDF，再暂停，不要猜测全文细节。

论文基础信息：
- Title: World4RL: Diffusion World Models for Policy Refinement with Reinforcement Learning for Robotic Manipulation
- Authors: Zhennan Jiang, Kai Liu, Yuxin Qin, Shuai Tian, Yupeng Zheng, Mingcai Zhou, Chao Yu, Haoran Li, Dongbin Zhao
- arXiv Abstract URL: https://arxiv.org/abs/2509.19080
- Research Interests: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
- Quick Judgment: 值得优先看，它是把世界模型、强化学习和真实操控 refinement 串成闭环的少数完整方案。
- Current Read of the Paper: World4RL面向一个很现实的问题：示教初始化的操控策略常受限于数据稀缺，而直接上真机做 RL 的代价和风险都太高。作者提出用扩散式世界模型在 imagined 环境中继续精炼 BC 策略，并配合奖励分类器处理操控任务常见的稀疏奖励，希望在避开 sim-to-real gap 的同时，保留在线 RL 的改进能力。
- Method / Evidence Clues from arXiv HTML: 从 HTML 可见，框架由三个部件组成：扩散转移模型负责条件未来观测生成，二元奖励分类器评估想象 rollout，策略则从 BC 初始化并用 PPO 在世界模型内优化。实验设计覆盖生成质量、相对 IL、离线 RL 与其他 world-model 方法的策略收益，以及真实机器人部署；证据结构完整，但 imagined fidelity 是否足以支撑长时操控，还需看 PDF 的定量与失败分析。

这次请优先替我核查下面 3 个问题：
- 扩散转移模型预测的是像素级观测、潜变量状态，还是两者结合，这对操控精度有何影响？
- 奖励分类器的标签来源与训练分布是什么，是否会把示教偏见带回 refinement 过程？
- 真实机器人上的收益主要来自 imagined RL 本身，还是来自 BC 初始化与 reward shaping 的组合效应？

上传 PDF 后，请优先查看这些章节、实验或图表类型：
- 方法章节中扩散转移模型与奖励分类器的训练流程
- 实验章节里与 IL、离线 RL、world-model baselines 的对比
- 真实机器人部署与 imagined rollout 失配分析

在我上传 PDF 之后，请严格按下面结构输出中文分析，保留关键英文术语：
1. 这篇论文到底在解决什么问题？
2. 核心方法脉络是什么？请把关键模块、训练/推理流程串起来。
3. 对上面 3 个核查问题逐一回答。
4. 实验设置、关键指标和主要结论是什么？
5. 哪些地方最可能是方法边界、实验短板或复现风险？给 3 条。
6. 它与我的研究兴趣有什么关系？
7. 最后给出一个结论：值不值得我进一步精读/复现，为什么？

要求：
- 只有在 PDF 明确给出证据时，才引用数字、表格、公式或模块细节。
- 如果某个信息在 PDF 中不明确，请直接写“不确定”。
- 不要只重复摘要，要优先验证方法细节、实验可信度和边界条件。
- 结尾补一个“下一步阅读建议”，告诉我最该看论文里的哪几个章节、图表或实验。

```

### [5]. Latent Action Diffusion for Cross-Embodiment Manipulation [[HTML]](https://arxiv.org/html/2506.14608) [[PDF]](https://arxiv.org/pdf/2506.14608) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2506.14608`
* **Authors**: Erik Bauer, Elvis Nava, Robert K. Katzschmann
* **Author Priority**: Standard
* **一句话判断**: 值得优先看，它正面解决了跨 embodiment 学习里最难绕开的动作空间不一致问题。
* **这篇在做什么**: 这篇工作把不同末端执行器之间最棘手的动作异构问题，转成一个共享潜动作空间学习问题。作者先用对比式动作编码器，把仿人手、人手以及平行夹爪等不同动作空间对齐到语义一致的 latent action，再在这个空间里训练 diffusion policy，希望让跨 embodiment 共训真正利用到技能共性，而不只是共享视觉输入。
* **方法与证据**: HTML 给出的证据点相当具体：作者报告了对比动作模型的消融，使用 self-reconstruction 与 cross-reconstruction 验证损失评估设计选择，并指出 temperature annealing 与 encoder finetuning 都有帮助。实验覆盖三种 end-effector、三类任务，以及单 embodiment 与 cross-embodiment 共训对比；不过现有摘录没有给出更细的成功率幅度，最终判断仍要看 PDF 图表。
* **为什么值得看**:
  - 它把跨 embodiment 迁移的难点从“数据能不能混”推进到“动作怎么对齐”。
  - 潜动作空间若可靠，可为更大规模多机器人共训提供统一接口。
  - 扩散策略与对比式动作表征的组合，兼顾了生成式控制和结构化对齐。
* **风险 / 保留意见**:
  - 当前验证的 embodiment 范围仍有限，扩展到更复杂手型或移动操作器未必直接成立。
  - 潜空间对齐可能在任务语义相近时有效，但面对强约束接触技能时可能丢细节。
* **适合你怎么看**: 先看对比动作模型如何同时保证 self-reconstruction 和 cross-reconstruction。再重点核查 cross-embodiment policy 的收益，判断改进究竟来自潜动作对齐还是多源数据规模本身。
* **关键词**: `跨 embodiment` `潜动作空间` `扩散策略` `对比学习` `操控迁移`
* **证据来源**: arXiv HTML

#### ChatGPT Deep Read Prompt
> 上传 PDF 后再粘贴。这个 prompt 已按该论文的方法线索、实验焦点和风险点单独定制。

```text
你是我的机器人学研究搭档。请先检查我是否已经上传这篇论文的 PDF。

如果我还没有上传 PDF，请先提醒我上传 PDF，再暂停，不要猜测全文细节。

论文基础信息：
- Title: Latent Action Diffusion for Cross-Embodiment Manipulation
- Authors: Erik Bauer, Elvis Nava, Robert K. Katzschmann
- arXiv Abstract URL: https://arxiv.org/abs/2506.14608
- Research Interests: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
- Quick Judgment: 值得优先看，它正面解决了跨 embodiment 学习里最难绕开的动作空间不一致问题。
- Current Read of the Paper: 这篇工作把不同末端执行器之间最棘手的动作异构问题，转成一个共享潜动作空间学习问题。作者先用对比式动作编码器，把仿人手、人手以及平行夹爪等不同动作空间对齐到语义一致的 latent action，再在这个空间里训练 diffusion policy，希望让跨 embodiment 共训真正利用到技能共性，而不只是共享视觉输入。
- Method / Evidence Clues from arXiv HTML: HTML 给出的证据点相当具体：作者报告了对比动作模型的消融，使用 self-reconstruction 与 cross-reconstruction 验证损失评估设计选择，并指出 temperature annealing 与 encoder finetuning 都有帮助。实验覆盖三种 end-effector、三类任务，以及单 embodiment 与 cross-embodiment 共训对比；不过现有摘录没有给出更细的成功率幅度，最终判断仍要看 PDF 图表。

这次请优先替我核查下面 3 个问题：
- latent action 是否对不同末端执行器保留了足够的可逆控制细节，而不是只学到粗粒度语义？
- cross-reconstruction 的提升与最终策略成功率之间是否存在稳定对应关系？
- 当测试 embodiment 未在对比动作模型训练中出现时，潜空间还能否支持迁移？

上传 PDF 后，请优先查看这些章节、实验或图表类型：
- 方法章节中 contrastive action model 的两阶段训练流程
- 消融章节里 temperature annealing 与 encoder finetuning 的作用
- 实验章节中单 embodiment 与 cross-embodiment policy 的对比结果

在我上传 PDF 之后，请严格按下面结构输出中文分析，保留关键英文术语：
1. 这篇论文到底在解决什么问题？
2. 核心方法脉络是什么？请把关键模块、训练/推理流程串起来。
3. 对上面 3 个核查问题逐一回答。
4. 实验设置、关键指标和主要结论是什么？
5. 哪些地方最可能是方法边界、实验短板或复现风险？给 3 条。
6. 它与我的研究兴趣有什么关系？
7. 最后给出一个结论：值不值得我进一步精读/复现，为什么？

要求：
- 只有在 PDF 明确给出证据时，才引用数字、表格、公式或模块细节。
- 如果某个信息在 PDF 中不明确，请直接写“不确定”。
- 不要只重复摘要，要优先验证方法细节、实验可信度和边界条件。
- 结尾补一个“下一步阅读建议”，告诉我最该看论文里的哪几个章节、图表或实验。

```

### [6]. RobotArena $\infty$: Scalable Robot Benchmarking via Real-to-Sim Translation [[PDF]](https://arxiv.org/pdf/2510.23571) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2510.23571`
* **Authors**: Yash Jangir, Yidi Zhang, Pang-Chi Lo, Kashu Yamazaki, Chenyu Zhang, Kuan-Hsun Tu, Tsung-Wei Ke, Lei Ke, Yonatan Bisk, Katerina Fragkiadaki
* **Author Priority**: Standard
* **一句话判断**: 值得优先看，它瞄准的是 VLA 时代最缺的可扩展评测基础设施，而不是又一个单点模型增益。
* **这篇在做什么**: RobotArena Infinity 试图解决机器人通用策略评测长期受制于人工、速度、安全和复现性的难题。作者把评测尽量前移到大规模仿真里：利用视觉语言模型、2D 到 3D 生成建模和可微渲染，把现有机器人数据集中的视频示范自动转成可交互的模拟环境，并辅以在线人类反馈来评估执行质量。
* **方法与证据**: 从摘要可见，这不是传统 benchmark 的静态任务库，而是一个 real-to-sim translation 加 human-in-the-loop judgment 的评测框架，方向判断很强，也契合 VLA 扩张后的 evaluation bottleneck。风险在于当前只有摘要回退：转换链路的保真度、人工反馈的一致性，以及它与真实世界成功率的对应关系，都还缺少 HTML 级别的公开证据，需要 PDF 重点验证。
* **为什么值得看**:
  - 评测扩展性正在成为 VLA 研发速度的硬瓶颈，这篇正对这个痛点。
  - 把真实视频资产转成可重复模拟评测，理论上能显著降低基准构建成本。
  - 若 human feedback 设计合理，它可能覆盖传统 success metric 难以表达的执行质量。
* **风险 / 保留意见**:
  - real-to-sim translation 若保真不足，benchmark 可能高估策略真实能力。
  - 在线人工反馈的标注协议与一致性如果不稳，评测可复现性会打折。
* **适合你怎么看**: 先看 real-to-sim translation 的最小闭环是否成立，再看 human feedback 在评测中承担的是主判据还是补充判据。随后重点核查 benchmark 分数与真实机器人表现的相关性证据。
* **关键词**: `VLA 评测` `real-to-sim` `人类反馈` `可微渲染` `机器人基准`
* **证据来源**: Abstract fallback

#### ChatGPT Deep Read Prompt
> 上传 PDF 后再粘贴。这个 prompt 已按该论文的方法线索、实验焦点和风险点单独定制。

```text
你是我的机器人学研究搭档。请先检查我是否已经上传这篇论文的 PDF。

如果我还没有上传 PDF，请先提醒我上传 PDF，再暂停，不要猜测全文细节。

论文基础信息：
- Title: RobotArena $\infty$: Scalable Robot Benchmarking via Real-to-Sim Translation
- Authors: Yash Jangir, Yidi Zhang, Pang-Chi Lo, Kashu Yamazaki, Chenyu Zhang, Kuan-Hsun Tu, Tsung-Wei Ke, Lei Ke, Yonatan Bisk, Katerina Fragkiadaki
- arXiv Abstract URL: https://arxiv.org/abs/2510.23571
- Research Interests: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
- Quick Judgment: 值得优先看，它瞄准的是 VLA 时代最缺的可扩展评测基础设施，而不是又一个单点模型增益。
- Current Read of the Paper: RobotArena Infinity 试图解决机器人通用策略评测长期受制于人工、速度、安全和复现性的难题。作者把评测尽量前移到大规模仿真里：利用视觉语言模型、2D 到 3D 生成建模和可微渲染，把现有机器人数据集中的视频示范自动转成可交互的模拟环境，并辅以在线人类反馈来评估执行质量。
- Method / Evidence Clues from arXiv HTML: 从摘要可见，这不是传统 benchmark 的静态任务库，而是一个 real-to-sim translation 加 human-in-the-loop judgment 的评测框架，方向判断很强，也契合 VLA 扩张后的 evaluation bottleneck。风险在于当前只有摘要回退：转换链路的保真度、人工反馈的一致性，以及它与真实世界成功率的对应关系，都还缺少 HTML 级别的公开证据，需要 PDF 重点验证。

这次请优先替我核查下面 3 个问题：
- 视频到可交互仿真场景的转换中，哪些几何和动力学因素被显式建模，哪些被近似处理？
- 在线人类反馈如何标准化，才能避免不同评审者对“执行质量”的主观漂移？
- 该 benchmark 的排名变化，是否能真实预测策略在真机上的相对表现？

上传 PDF 后，请优先查看这些章节、实验或图表类型：
- 系统章节中 real-to-sim translation 与场景生成流程
- 评测章节里 human-in-the-loop 评分协议与一致性分析
- 验证章节中 benchmark 分数与真实世界表现的相关性实验

在我上传 PDF 之后，请严格按下面结构输出中文分析，保留关键英文术语：
1. 这篇论文到底在解决什么问题？
2. 核心方法脉络是什么？请把关键模块、训练/推理流程串起来。
3. 对上面 3 个核查问题逐一回答。
4. 实验设置、关键指标和主要结论是什么？
5. 哪些地方最可能是方法边界、实验短板或复现风险？给 3 条。
6. 它与我的研究兴趣有什么关系？
7. 最后给出一个结论：值不值得我进一步精读/复现，为什么？

要求：
- 只有在 PDF 明确给出证据时，才引用数字、表格、公式或模块细节。
- 如果某个信息在 PDF 中不明确，请直接写“不确定”。
- 不要只重复摘要，要优先验证方法细节、实验可信度和边界条件。
- 结尾补一个“下一步阅读建议”，告诉我最该看论文里的哪几个章节、图表或实验。

```

## Watchlist

### [W1]. ReMAP-DP: Reprojected Multi-view Aligned PointMaps for Diffusion Policy [[HTML]](https://arxiv.org/html/2603.14977) [[PDF]](https://arxiv.org/pdf/2603.14977)
* **Paper ID**: `2603.14977`
* **Authors**: Xinzhang Yang, Renjun Wu, Jinyan Liu, Xuesong Li
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇进入 shortlist，主要因为它把 2D 语义与显式 3D 几何对齐到 diffusion policy 里，问题定义和实验设计都很扎实，尤其适合关注高精度操作的人。HTML 还能看到它覆盖 ManiSkill 3、RoboTwin 2.0 和真实环境，证据链并不弱。没有进最终精选，是因为它更偏 3D 表征增强的 diffusion policy，而不是今天更核心的 VLA、world model 或 RL-to-robot 主线。若你近期在做 3D-aware manipulation policy，它仍值得单独跟进。
* **证据来源**: arXiv HTML

### [W2]. AGILE: A Comprehensive Workflow for Humanoid Loco-Manipulation Learning [[HTML]](https://arxiv.org/html/2603.20147) [[PDF]](https://arxiv.org/pdf/2603.20147)
* **Paper ID**: `2603.20147`
* **Authors**: Huihua Zhao, Rafael Cathomen, Lionel Gulich, Wei Liu, Efe Arda Ongan, Michael Lin, Shalin Jain, Soha Pouya, Yan Chang
* **Author Priority**: Standard
* **为什么还值得留意**: AGILE 进入 shortlist，是因为它抓住了 humanoid sim2real 中常被低估的 workflow gap，把环境验证、训练、确定性评测和部署串成闭环。对真正要落地类人 loco-manipulation 的团队，这类基础设施论文往往比单次算法增益更有复用价值。没有进最终精选，是因为从当前摘录看，它的主要贡献在工程流程与评测规范，而不是 VLA、世界模型或机器人 manipulation policy 本身的核心方法突破。
* **证据来源**: arXiv HTML

### [W3]. Morphology-Consistent Humanoid Interaction through Robot-Centric Video Synthesis [[HTML]](https://arxiv.org/html/2603.19709) [[PDF]](https://arxiv.org/pdf/2603.19709)
* **Paper ID**: `2603.19709`
* **Authors**: Weisheng Xu, Jian Li, Yi Gu, Bin Yang, Haodong Chen, Shuyi Lin, Mingqian Zhou, Jing Tan, Qiwei Wu, Xiangrui Jiang, Taowen Wang, Jiawen Wen, Qiwei Liang, Jiaxi Zhang, Renjing Xu
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇进入 shortlist，主要因为它把 robot-centric video synthesis 引入 humanoid interaction acquisition，试图绕开人到机器人的显式 retargeting，这和世界模型式数据生成思路高度相邻。作者还用 Seedance 2.0 作为生成核心，方向上很新。没有进最终精选，是因为当前主线更偏 VLA、manipulation 与 world model 的可控优化，而 Dream2Act 更聚焦 humanoid 交互生成与形态恢复，且现有摘录还不足以判断真实物理执行的稳定边界。
* **证据来源**: arXiv HTML

### [W4]. R2-Dreamer: Redundancy-Reduced World Models without Decoders or Augmentation [[HTML]](https://arxiv.org/html/2603.18202) [[PDF]](https://arxiv.org/pdf/2603.18202)
* **Paper ID**: `2603.18202`
* **Authors**: Naoki Morihira, Amal Nahar, Kartik Bharadwaj, Yasuhiro Kato, Akinobu Hayashi, Tatsuya Harada
* **Author Priority**: Standard
* **为什么还值得留意**: R2-Dreamer 进入 shortlist，是因为它在 world model 表征学习上有明确方法点：去掉 decoder 和数据增强，用 redundancy reduction 做内部正则，思路很干净，也可能很有启发。实验问题设置也覆盖了效率、性能和表示质量。没有进最终精选，是因为从当前摘录看，它更像通用 image-based MBRL 的表示学习推进，而不是直接面向机器人操控、VLA 或 sim2real 落地的工作。
* **证据来源**: arXiv HTML
