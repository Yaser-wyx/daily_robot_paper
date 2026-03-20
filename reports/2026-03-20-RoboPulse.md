# RoboPulse | 2026-03-20

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 93 papers scanned · 10 shortlisted · 6 editor's picks

今天主线集中在两条：一条是用生成式 3D 世界、数字孪生和自动化仿真，把 VLA 的强化学习与数据扩展重新搬回可扩展的模拟侧；另一条是把世界建模与动作验证前移到接触和推理环节，提高 OOD 与接触密集场景下的可靠性。最终精选的六篇刚好覆盖 sim-to-real RL 扩展、数字孪生在线强化学习、视触觉 world model、自动化仿真数据引擎、跨形态轨迹迁移和推理期自验证，主线完整且互补。VIP 作者里最值得优先跟踪的是 TrajBooster，对应核心名单中的 Cewu Lu 和 Donglin Wang，而且它直接切中 humanoid VLA 的跨形态适配难题。其余入选虽无核心 VIP 作者加持，但在 RL+VLA、world model 与 sim-to-real 方法趋势上都很强，适合作为本期主读。

## Editor's Picks

### [1]. Scaling Sim-to-Real Reinforcement Learning for Robot VLAs with Generative 3D Worlds [[PDF]](https://arxiv.org/pdf/2603.18532) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.18532`
* **Authors**: Andrew Choi, Xinjie Wang, Zhizhong Su, Wei Xu
* **Author Priority**: Standard
* **一句话判断**: 如果你关心 RL 微调会不会把通用 VLA 训成场景专用策略，这篇值得优先看，但当前证据仅到摘要层。
* **这篇在做什么**: 这篇工作抓住了一个很实际的矛盾：真实世界 RL 虽然绕开 sim-to-real，却可能把原本广泛预训练的 VLA 压成少数场景里的过拟合策略。作者主张把 RL 微调重新放回仿真侧，并用生成式 3D 世界自动提供更丰富的场景与物体多样性，以更低人工成本维持泛化能力与可迁移性。
* **方法与证据**: 从摘要能确认的方法主线，是以 3D world generative models 生成训练环境，再对机器人 VLA 做 RL fine-tuning，试图同时缓解手工搭场景和真实交互采样的双重瓶颈。证据层面目前只有摘要，没有 HTML 方法细节，也看不到奖励设计、生成世界约束和真实机器人评估设置，因此对效果强度只能作正向但保守的趋势判断。
* **为什么值得看**:
  - 把 VLA 的 RL 扩展问题重新转成可扩展的环境与数据生成问题。
  - 直接回应真实世界 RL 易过拟合、仿真搭建又昂贵的两难。
  - 生成式 3D 世界与机器人后训练结合，方向上很契合基础模型时代。
* **风险 / 保留意见**:
  - 只有摘要回退，关键实现如 world generation 约束和 sim-to-real 协议都还不透明。
  - 若生成场景的物理真实性不足，可能只扩大表面多样性，未必带来真实泛化。
* **适合你怎么看**: 先看作者如何定义保持 VLA 通用性这个目标，再核查生成式 3D 世界是否真的进入 RL 闭环而不只是做离线数据扩增。随后重点看真实部署部分是否证明了多样性增益而非单场景调参。
* **关键词**: `VLA` `Sim2Real` `强化学习后训练` `生成式3D世界` `泛化`
* **证据来源**: Abstract fallback

#### ChatGPT Deep Read Prompt
> 上传 PDF 后再粘贴。这个 prompt 已按该论文的方法线索、实验焦点和风险点单独定制。

```text
你是我的机器人学研究搭档。请先检查我是否已经上传这篇论文的 PDF。

如果我还没有上传 PDF，请先提醒我上传 PDF，再暂停，不要猜测全文细节。

论文基础信息：
- Title: Scaling Sim-to-Real Reinforcement Learning for Robot VLAs with Generative 3D Worlds
- Authors: Andrew Choi, Xinjie Wang, Zhizhong Su, Wei Xu
- arXiv Abstract URL: https://arxiv.org/abs/2603.18532
- Research Interests: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
- Quick Judgment: 如果你关心 RL 微调会不会把通用 VLA 训成场景专用策略，这篇值得优先看，但当前证据仅到摘要层。
- Current Read of the Paper: 这篇工作抓住了一个很实际的矛盾：真实世界 RL 虽然绕开 sim-to-real，却可能把原本广泛预训练的 VLA 压成少数场景里的过拟合策略。作者主张把 RL 微调重新放回仿真侧，并用生成式 3D 世界自动提供更丰富的场景与物体多样性，以更低人工成本维持泛化能力与可迁移性。
- Method / Evidence Clues from arXiv HTML: 从摘要能确认的方法主线，是以 3D world generative models 生成训练环境，再对机器人 VLA 做 RL fine-tuning，试图同时缓解手工搭场景和真实交互采样的双重瓶颈。证据层面目前只有摘要，没有 HTML 方法细节，也看不到奖励设计、生成世界约束和真实机器人评估设置，因此对效果强度只能作正向但保守的趋势判断。

这次请优先替我核查下面 3 个问题：
- 生成式 3D 世界是按任务语言、物体类别还是场景布局来条件化生成的？
- RL 微调阶段如何约束预训练 VLA 不退化成场景特化策略？
- 真实机器人评估究竟验证了哪些跨场景或跨物体迁移，而不只是仿真内收益？

上传 PDF 后，请优先查看这些章节、实验或图表类型：
- 生成式 3D 世界构建与物理约束章节
- VLA 的 RL fine-tuning 目标与训练流程章节
- sim-to-real 泛化实验与真实机器人评测章节

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

### [2]. TwinRL-VLA: Digital Twin-Driven Reinforcement Learning for Real-World Robotic Manipulation [[HTML]](https://arxiv.org/html/2602.09023) [[PDF]](https://arxiv.org/pdf/2602.09023) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2602.09023`
* **Authors**: Qinwen Xu, Jiaming Liu, Rui Zhou, Shaojun Shi, Nuowei Han, Zhuoyang Liu, Chenyang Gu, Shuo Gu, Yang Yue, Gao Huang, Wenzhao Zheng, Sirui Han, Peng Jia, Shanghang Zhang
* **Author Priority**: Standard
* **一句话判断**: 如果今天只看一篇 RL+VLA 的落地论文，TwinRL-VLA 应该排在前列。
* **这篇在做什么**: 论文瞄准真实机器人上做在线 RL 的核心瓶颈：探索效率低，而且可探索空间被监督微调数据分布强烈束缚。作者据此提出 TwinRL，用数字孪生去扩大并重塑 VLA 的有效探索空间，让模型在真实操作里不只依赖少量演示，而能借助仿真侧持续获得更有价值的交互。
* **方法与证据**: 从 HTML 可见，作者先通过系统性真实实验提出关键观察：在线 RL 的有效探索范围与 SFT 数据分布紧密相关。实验部分给了较扎实的证据框架，包括 FR3 双相机平台、真实世界基线对比、组件消融，以及在不同背景和光照下的鲁棒性评估；同时还用网格化 workspace 区分 ID 与 OOD 区域，说明其关注的不只是平均成功率。
* **为什么值得看**:
  - 把数字孪生从离线验证工具推进成在线 RL 的探索放大器。
  - 它直接解释了为何真实世界 RL 常常受困于演示分布边界。
  - ID 与 OOD 的网格化协议，有助于把探索范围和泛化收益分开讨论。
* **风险 / 保留意见**:
  - 数字孪生与真实环境的一致性成本可能不低，迁移收益依赖建模质量。
  - 当前摘录主要展示单一硬件与任务设定，跨平台通用性仍待 PDF 细查。
* **适合你怎么看**: 先看作者提出的核心经验结论，即探索空间如何被 SFT 分布锁定；再顺着 TwinRL 的数字孪生介入点去看，它究竟是在做数据扩增、探索引导，还是直接参与策略更新。
* **关键词**: `VLA` `数字孪生` `在线强化学习` `真实机器人操作` `OOD泛化`
* **证据来源**: arXiv HTML

#### ChatGPT Deep Read Prompt
> 上传 PDF 后再粘贴。这个 prompt 已按该论文的方法线索、实验焦点和风险点单独定制。

```text
你是我的机器人学研究搭档。请先检查我是否已经上传这篇论文的 PDF。

如果我还没有上传 PDF，请先提醒我上传 PDF，再暂停，不要猜测全文细节。

论文基础信息：
- Title: TwinRL-VLA: Digital Twin-Driven Reinforcement Learning for Real-World Robotic Manipulation
- Authors: Qinwen Xu, Jiaming Liu, Rui Zhou, Shaojun Shi, Nuowei Han, Zhuoyang Liu, Chenyang Gu, Shuo Gu, Yang Yue, Gao Huang, Wenzhao Zheng, Sirui Han, Peng Jia, Shanghang Zhang
- arXiv Abstract URL: https://arxiv.org/abs/2602.09023
- Research Interests: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
- Quick Judgment: 如果今天只看一篇 RL+VLA 的落地论文，TwinRL-VLA 应该排在前列。
- Current Read of the Paper: 论文瞄准真实机器人上做在线 RL 的核心瓶颈：探索效率低，而且可探索空间被监督微调数据分布强烈束缚。作者据此提出 TwinRL，用数字孪生去扩大并重塑 VLA 的有效探索空间，让模型在真实操作里不只依赖少量演示，而能借助仿真侧持续获得更有价值的交互。
- Method / Evidence Clues from arXiv HTML: 从 HTML 可见，作者先通过系统性真实实验提出关键观察：在线 RL 的有效探索范围与 SFT 数据分布紧密相关。实验部分给了较扎实的证据框架，包括 FR3 双相机平台、真实世界基线对比、组件消融，以及在不同背景和光照下的鲁棒性评估；同时还用网格化 workspace 区分 ID 与 OOD 区域，说明其关注的不只是平均成功率。

这次请优先替我核查下面 3 个问题：
- TwinRL 具体在哪个环节利用数字孪生，是初始化缓冲区、在线筛选探索目标，还是直接参与策略优化？
- 实验里 ID 与 OOD 区域的划分规则，会不会放大某类方法对空间覆盖的优势？
- 当 SFT 数据本身偏窄时，TwinRL 能否稳定跳出原分布，而不是只在边界附近微扩展？

上传 PDF 后，请优先查看这些章节、实验或图表类型：
- TwinRL 框架与数字孪生交互流程章节
- 真实世界实验设置与 workspace 网格化评测章节
- 组件消融与背景光照鲁棒性实验章节

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

### [3]. OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation [[HTML]](https://arxiv.org/html/2603.19201) [[PDF]](https://arxiv.org/pdf/2603.19201) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.19201`
* **Authors**: Yuhang Zheng, Songen Gu, Weize Li, Yupeng Zheng, Yujie Zang, Shuai Tian, Xiang Li, Ruihai Wu, Ce Hao, Chen Gao, Si Liu, Haoran Li, Yilun Chen, Shuicheng Yan, Wenchao Ding
* **Author Priority**: Standard
* **一句话判断**: 做接触密集操作或多模态 world model 的研究者，这篇值得高优先级精读。
* **这篇在做什么**: 这篇工作把问题直接落在视觉单模态不够的接触密集操作上。作者不仅提出大规模 visuo-tactile-action 数据集 OmniViTac，还构建 OmniVTA，把未来触觉信号和视觉演化一起建模，用于擦拭、装配这类依赖接触力、摩擦变化和状态切换的闭环操作，目标是让触觉不再只是被动观测。
* **方法与证据**: 方法主线很清楚：用双流条件生成 world model 分别建模视觉与触觉时序，再用联合 conditioner 融合 vision、tactile 和 action，并以 dynamic-aware loss 强调高频触觉变化。实验也围绕四个关键问题展开：触觉编码是否有效、未来触觉预测是否更准、预测触觉能否提升策略，以及控制器是否能生成合理动作。
* **为什么值得看**:
  - 它把触觉从辅助输入升级成可预测、可控制的世界状态变量。
  - 对 contact-rich manipulation 来说，world model 比纯 imitation policy 更有解释力。
  - 数据集与方法同时推进，比只做模型或只做 benchmark 更可能带动后续跟进。
* **风险 / 保留意见**:
  - 多传感器系统的硬件门槛较高，复现成本可能明显高于纯视觉 VLA。
  - 当前摘录未给出数据规模、跨任务跨度和真实部署范围，泛化强度仍需谨慎判断。
* **适合你怎么看**: 先读 world model 结构，而不是先看 policy 头，因为这篇真正的创新点在未来视觉-触觉联合建模。随后重点核查预测到的触觉信息是如何进入控制闭环的。
* **关键词**: `Visuo-Tactile` `World Model` `接触密集操作` `扩散Transformer` `触觉预测`
* **证据来源**: arXiv HTML

#### ChatGPT Deep Read Prompt
> 上传 PDF 后再粘贴。这个 prompt 已按该论文的方法线索、实验焦点和风险点单独定制。

```text
你是我的机器人学研究搭档。请先检查我是否已经上传这篇论文的 PDF。

如果我还没有上传 PDF，请先提醒我上传 PDF，再暂停，不要猜测全文细节。

论文基础信息：
- Title: OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation
- Authors: Yuhang Zheng, Songen Gu, Weize Li, Yupeng Zheng, Yujie Zang, Shuai Tian, Xiang Li, Ruihai Wu, Ce Hao, Chen Gao, Si Liu, Haoran Li, Yilun Chen, Shuicheng Yan, Wenchao Ding
- arXiv Abstract URL: https://arxiv.org/abs/2603.19201
- Research Interests: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
- Quick Judgment: 做接触密集操作或多模态 world model 的研究者，这篇值得高优先级精读。
- Current Read of the Paper: 这篇工作把问题直接落在视觉单模态不够的接触密集操作上。作者不仅提出大规模 visuo-tactile-action 数据集 OmniViTac，还构建 OmniVTA，把未来触觉信号和视觉演化一起建模，用于擦拭、装配这类依赖接触力、摩擦变化和状态切换的闭环操作，目标是让触觉不再只是被动观测。
- Method / Evidence Clues from arXiv HTML: 方法主线很清楚：用双流条件生成 world model 分别建模视觉与触觉时序，再用联合 conditioner 融合 vision、tactile 和 action，并以 dynamic-aware loss 强调高频触觉变化。实验也围绕四个关键问题展开：触觉编码是否有效、未来触觉预测是否更准、预测触觉能否提升策略，以及控制器是否能生成合理动作。

这次请优先替我核查下面 3 个问题：
- 双流 world model 相比单流联合建模，究竟在哪类接触状态转移上体现优势？
- 预测未来触觉信号是直接作为控制条件，还是只通过潜变量间接影响策略？
- dynamic-aware weighted loss 是否真正提升了关键接触瞬间的建模，而不是只改善局部重建？

上传 PDF 后，请优先查看这些章节、实验或图表类型：
- 数据集构建与视觉触觉时间对齐章节
- 双流 world model 与损失设计章节
- TactileVAE、触觉预测和控制器消融实验章节

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

### [4]. V-Dreamer: Automating Robotic Simulation and Trajectory Synthesis via Video Generation Priors [[HTML]](https://arxiv.org/html/2603.18811) [[PDF]](https://arxiv.org/pdf/2603.18811) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.18811`
* **Authors**: Songjia He, Zixuan Chen, Hongyu Ding, Dian Shao, Jieqi Shi, Chenxu Li, Jing Huo, Yang Gao
* **Author Priority**: Standard
* **一句话判断**: 如果你关心自动造数据能否真正支撑机器人学习，这篇是今天最值得看的系统型论文之一。
* **这篇在做什么**: V-Dreamer 想把通用机器人最稀缺的两样东西一起自动化：可执行的仿真环境和高质量示教轨迹。它从自然语言指令出发，结合 LLM、3D 生成模型和视频生成先验，自动产出 open-vocabulary 的 3D 操作场景与专家轨迹，并把这些结果直接送入下游模仿学习与真实部署验证。
* **方法与证据**: 从 HTML 可以确认，这不是单一模块创新，而是贯通场景生成、几何校验、轨迹合成到真实机器人执行的完整 pipeline。作者特意选用不含探索的 ACT 作为下游策略，以尽量把性能变化归因到合成数据本身；实验则围绕数据规模与质量、语义和几何多样性、物理可执行性以及 zero-shot real transfer 四条主线展开。
* **为什么值得看**:
  - 它把数据扩展从补充采集，推进到自动生成可训练任务分布。
  - 用 ACT 做下游评估，思路上更容易隔离数据质量而不是算法差异。
  - 对 sim-to-real 社区很有价值，因为它同时要求语义多样性和物理可执行性。
* **风险 / 保留意见**:
  - 缺少直接可比的端到端 baseline，系统整体收益可能难拆解到各子模块。
  - 若任务主要集中在桌面操作，开放词汇场景的外延能力可能仍被任务模板限制。
* **适合你怎么看**: 先看场景与轨迹是如何自动生成并被物理约束筛掉的，再看 ACT 实验，因为这能决定论文是在做视觉花活还是在做真正可用的数据基础设施。
* **关键词**: `仿真数据生成` `视频生成先验` `Sim2Real` `模仿学习` `场景合成`
* **证据来源**: arXiv HTML

#### ChatGPT Deep Read Prompt
> 上传 PDF 后再粘贴。这个 prompt 已按该论文的方法线索、实验焦点和风险点单独定制。

```text
你是我的机器人学研究搭档。请先检查我是否已经上传这篇论文的 PDF。

如果我还没有上传 PDF，请先提醒我上传 PDF，再暂停，不要猜测全文细节。

论文基础信息：
- Title: V-Dreamer: Automating Robotic Simulation and Trajectory Synthesis via Video Generation Priors
- Authors: Songjia He, Zixuan Chen, Hongyu Ding, Dian Shao, Jieqi Shi, Chenxu Li, Jing Huo, Yang Gao
- arXiv Abstract URL: https://arxiv.org/abs/2603.18811
- Research Interests: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
- Quick Judgment: 如果你关心自动造数据能否真正支撑机器人学习，这篇是今天最值得看的系统型论文之一。
- Current Read of the Paper: V-Dreamer 想把通用机器人最稀缺的两样东西一起自动化：可执行的仿真环境和高质量示教轨迹。它从自然语言指令出发，结合 LLM、3D 生成模型和视频生成先验，自动产出 open-vocabulary 的 3D 操作场景与专家轨迹，并把这些结果直接送入下游模仿学习与真实部署验证。
- Method / Evidence Clues from arXiv HTML: 从 HTML 可以确认，这不是单一模块创新，而是贯通场景生成、几何校验、轨迹合成到真实机器人执行的完整 pipeline。作者特意选用不含探索的 ACT 作为下游策略，以尽量把性能变化归因到合成数据本身；实验则围绕数据规模与质量、语义和几何多样性、物理可执行性以及 zero-shot real transfer 四条主线展开。

这次请优先替我核查下面 3 个问题：
- 视频生成先验产出的轨迹是如何转成机器人可执行动作序列的？
- 几何约束与物理校验具体过滤掉了哪些不稳定场景或不可执行轨迹？
- 下游收益究竟来自更大数据量，还是来自开放词汇场景带来的分布扩展？

上传 PDF 后，请优先查看这些章节、实验或图表类型：
- 自然语言到 3D 场景生成与校验章节
- 轨迹合成、可执行性约束与机器人接口章节
- ACT 下游学习与 zero-shot sim-to-real 实验章节

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

### [5]. TrajBooster: Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning [[VIP]] [[HTML]](https://arxiv.org/html/2509.11839) [[PDF]](https://arxiv.org/pdf/2509.11839) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2509.11839`
* **Authors**: Jiacheng Liu, Pengxiang Ding, Qihang Zhou, Yuxuan Wu, Da Huang, Zimian Peng, Wei Xiao, Weinan Zhang, Lixin Yang, Cewu Lu, Donglin Wang
* **Author Priority**: Core VIP
* **一句话判断**: 这是今天最该优先追的 VIP 论文之一，跨形态 humanoid VLA 适配问题打得很准。
* **这篇在做什么**: TrajBooster 关注一个现实难题：预训练 VLA 面对新机器人时，动作空间对不齐，双足 humanoid 又受全身协同与动态平衡约束，更难快速适配。作者以末端执行器轨迹作为 morphology-agnostic 接口，把轮式 humanoid 的真实操作数据抽成 6D 双臂轨迹，在仿真里重定向到 Unitree G1，再用于双足 VLA 后训练。
* **方法与证据**: 方法是 real-to-sim-to-real：先提取 Agibot-World beta 轨迹，再训练分层 retargeting 模型和 whole-body controller，之后让 VLA 先吃仿真重定向数据，再用少量真实遥操作数据适配。实验覆盖 retargeting、适配速度、OOD 位置泛化和零样本技能。
* **为什么值得看**:
  - 它把跨 embodiment 迁移的接口从原始动作改成轨迹，思路更稳健也更可扩展。
  - 对 humanoid VLA 来说，这比单纯换 action head 更接近真实部署痛点。
  - Cewu Lu 和 Donglin Wang 都在核心 VIP 名单里，值得优先跟进。
* **风险 / 保留意见**:
  - 效果可能高度依赖源机器人数据质量，以及轨迹重定向时的控制器稳定性。
  - 从轮式 humanoid 到双足 humanoid 的成功经验，不一定直接外推到更异构的 embodiment。
* **适合你怎么看**: 先看轨迹接口如何处理 Agibot 与 G1 的工作空间差异，这是整篇是否成立的根。然后重点查两步后训练是否真的减少了真实遥操作需求，而不是只增加了一个昂贵的仿真中间层。
* **关键词**: `Humanoid VLA` `跨形态迁移` `轨迹重定向` `Sim2Real` `whole-body manipulation`
* **证据来源**: arXiv HTML

#### ChatGPT Deep Read Prompt
> 上传 PDF 后再粘贴。这个 prompt 已按该论文的方法线索、实验焦点和风险点单独定制。

```text
你是我的机器人学研究搭档。请先检查我是否已经上传这篇论文的 PDF。

如果我还没有上传 PDF，请先提醒我上传 PDF，再暂停，不要猜测全文细节。

论文基础信息：
- Title: TrajBooster: Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning
- Authors: Jiacheng Liu, Pengxiang Ding, Qihang Zhou, Yuxuan Wu, Da Huang, Zimian Peng, Wei Xiao, Weinan Zhang, Lixin Yang, Cewu Lu, Donglin Wang
- arXiv Abstract URL: https://arxiv.org/abs/2509.11839
- Research Interests: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
- Quick Judgment: 这是今天最该优先追的 VIP 论文之一，跨形态 humanoid VLA 适配问题打得很准。
- Current Read of the Paper: TrajBooster 关注一个现实难题：预训练 VLA 面对新机器人时，动作空间对不齐，双足 humanoid 又受全身协同与动态平衡约束，更难快速适配。作者以末端执行器轨迹作为 morphology-agnostic 接口，把轮式 humanoid 的真实操作数据抽成 6D 双臂轨迹，在仿真里重定向到 Unitree G1，再用于双足 VLA 后训练。
- Method / Evidence Clues from arXiv HTML: 方法是 real-to-sim-to-real：先提取 Agibot-World beta 轨迹，再训练分层 retargeting 模型和 whole-body controller，之后让 VLA 先吃仿真重定向数据，再用少量真实遥操作数据适配。实验覆盖 retargeting、适配速度、OOD 位置泛化和零样本技能。

这次请优先替我核查下面 3 个问题：
- 末端轨迹在重定向前做了哪些归一化或约束，才能跨越 Agibot 与 G1 的臂展差异？
- 为什么用仿真重定向动作替换原始动作标签，会比直接微调更利于新 embodiment 适配？
- 后训练带来的收益主要体现在 OOD 位置泛化，还是体现在全新技能的零样本迁移？

上传 PDF 后，请优先查看这些章节、实验或图表类型：
- 真实轨迹提取与跨 embodiment 重定向章节
- 分层 retargeting 模型与 DAgger 训练章节
- 真实世界适配、OOD 泛化和零样本技能实验章节

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

### [6]. Action Draft and Verify: A Self-Verifying Framework for Vision-Language-Action Model [[HTML]](https://arxiv.org/html/2603.18091) [[PDF]](https://arxiv.org/pdf/2603.18091) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.18091`
* **Authors**: Chen Zhao, Zhuoran Wang, Haoyang Li, Shifeng Bao, Guanlin Li, Youhe Feng, Yang Li, Jie Tang, Jing Zhang
* **Author Priority**: Standard
* **一句话判断**: 这是今天最值得快速跟进的推理期 VLA 方法，思路简单且从摘录看真实收益明确。
* **这篇在做什么**: ADV 要解决的是 diffusion VLA 在 OOD 环境里常见的一个弱点：动作精度高，但对异常状态的恢复和结构化泛化不够稳定。作者把 diffusion expert 和 auto-regressive VLM 的长处拆开再组合，让前者一次起草多个连续动作候选，再由后者用单次前向打分选出更可信的 action chunk。
* **方法与证据**: 证据相对直接。方法上，VLM 用类似 perplexity 的分数对多个 candidate chunks 做 reranking，额外代价只是一遍验证前向。实验覆盖基线比较、机制分析、打分可靠性和 tokenization 影响；摘录也表明，在 matched 设置下 ADV 相比 diffusion baseline 在仿真和真实世界均有提升。
* **为什么值得看**:
  - 它不是重训一个全新 VLA，而是在推理期重新分配生成和验证职责。
  - 把 auto-regressive 先验用作 verifier，而不是直接做低层控制，思路很实用。
  - 在 OOD 场景下强调 recovery 与稳健性，契合真实部署最常见的失败模式。
* **风险 / 保留意见**:
  - 候选动作数量和 reranking 代价若设置不当，实时性可能受到影响。
  - 当前证据虽有真实世界收益，但跨 backbone 和任务族的普适性还要继续核查。
* **适合你怎么看**: 先看 verifier 的打分定义是否真的对应动作可执行性，而不是只偏好语言上更顺的序列。随后再看 OOD 实验，因为这决定 ADV 是普适稳健化方法，还是只在特定分布偏移下有效。
* **关键词**: `VLA` `Diffusion Policy` `Action Verification` `OOD鲁棒性` `推理期重排`
* **证据来源**: arXiv HTML

#### ChatGPT Deep Read Prompt
> 上传 PDF 后再粘贴。这个 prompt 已按该论文的方法线索、实验焦点和风险点单独定制。

```text
你是我的机器人学研究搭档。请先检查我是否已经上传这篇论文的 PDF。

如果我还没有上传 PDF，请先提醒我上传 PDF，再暂停，不要猜测全文细节。

论文基础信息：
- Title: Action Draft and Verify: A Self-Verifying Framework for Vision-Language-Action Model
- Authors: Chen Zhao, Zhuoran Wang, Haoyang Li, Shifeng Bao, Guanlin Li, Youhe Feng, Yang Li, Jie Tang, Jing Zhang
- arXiv Abstract URL: https://arxiv.org/abs/2603.18091
- Research Interests: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
- Quick Judgment: 这是今天最值得快速跟进的推理期 VLA 方法，思路简单且从摘录看真实收益明确。
- Current Read of the Paper: ADV 要解决的是 diffusion VLA 在 OOD 环境里常见的一个弱点：动作精度高，但对异常状态的恢复和结构化泛化不够稳定。作者把 diffusion expert 和 auto-regressive VLM 的长处拆开再组合，让前者一次起草多个连续动作候选，再由后者用单次前向打分选出更可信的 action chunk。
- Method / Evidence Clues from arXiv HTML: 证据相对直接。方法上，VLM 用类似 perplexity 的分数对多个 candidate chunks 做 reranking，额外代价只是一遍验证前向。实验覆盖基线比较、机制分析、打分可靠性和 tokenization 影响；摘录也表明，在 matched 设置下 ADV 相比 diffusion baseline 在仿真和真实世界均有提升。

这次请优先替我核查下面 3 个问题：
- ADV 需要起草多少个 candidate chunks 才能稳定带来收益，计算成本如何随之变化？
- perplexity-style 分数与长期任务成功率的相关性，是否强于与短期动作平滑性的相关性？
- Textual FAST 这类离散化方案为何更适合 verification，而不是直接改善 action generation？

上传 PDF 后，请优先查看这些章节、实验或图表类型：
- ADV 框架与 verifier 打分定义章节
- matched-setting 下的主结果与 OOD 对比实验章节
- scoring reliability 与 tokenization 消融章节

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

### [W1]. MLA: A Multisensory Language-Action Model for Multimodal Understanding and Forecasting in Robotic Manipulation [[HTML]](https://arxiv.org/html/2509.26642) [[PDF]](https://arxiv.org/pdf/2509.26642)
* **Paper ID**: `2509.26642`
* **Authors**: Zhuoyang Liu, Jiaming Liu, Jiadong Xu, Nuowei Han, Chenyang Gu, Hao Chen, Kaichen Zhou, Renrui Zhang, Kai Chin Hsieh, Kun Wu, Zhengping Che, Jian Tang, Shanghang Zhang
* **Author Priority**: Standard
* **为什么还值得留意**: MLA 进入 shortlist，主要因为它把 VLA 从视觉语言动作扩到点云、触觉等多传感器理解与未来 multisensory objective 预测，且有单臂、双臂真实机器人和 RLBench 三层评测。它与今天主线中的 contact-rich control 和 world-modeling 方向高度相关。没有进最终精选，是因为当前摘录对核心建模细节展开不够，方法辨识度和证据强度都略弱于同样做视触觉闭环、但结构更清晰的 OmniVTA。
* **证据来源**: arXiv HTML

### [W2]. ManiDreams: An Open-Source Library for Robust Object Manipulation via Uncertainty-aware Task-specific Intuitive Physics [[HTML]](https://arxiv.org/html/2603.18336) [[PDF]](https://arxiv.org/pdf/2603.18336)
* **Paper ID**: `2603.18336`
* **Authors**: Gaotian Wang, Kejia Ren, Andrew S. Morgan, Kaiyu Hang
* **Author Priority**: Standard
* **为什么还值得留意**: ManiDreams 值得放入 watchlist，因为它把不确定性显式放进 intuitive physics 模型和规划闭环，而不是只在训练时做域随机化，这对真实操作鲁棒性很重要。开源库定位、模块化 runtime pipeline、真实机器人与扰动基准也都有实际价值。没有进最终精选，是因为它更偏 uncertainty-aware planning framework，而不是今天更优先的 VLA、RL+VLA 或 world-action model 主线。
* **证据来源**: arXiv HTML

### [W3]. FASTER: Rethinking Real-Time Flow VLAs [[HTML]](https://arxiv.org/html/2603.19199) [[PDF]](https://arxiv.org/pdf/2603.19199)
* **Paper ID**: `2603.19199`
* **Authors**: Yuxiang Lu, Zhe Liu, Xianzhe Fan, Zhenya Yang, Jinghua Hou, Junyi Li, Kaixin Ding, Hengshuang Zhao
* **Author Priority**: Standard
* **为什么还值得留意**: FASTER 进入 shortlist，主要靠两点：一是它把 real-time VLA 的反应速度问题拆成 TTFA 与 execution horizon 的系统分析，二是给 flow-based VLA 提出 horizon-aware schedule 和 early stopping 的工程化改进。对真实部署尤其边缘设备很实用。没有进最终精选，是因为这篇更像推理系统与时延优化论文，和今天优先看的表示学习、world model、sim-to-real 训练范式相比，研究重心稍偏基础设施。
* **证据来源**: arXiv HTML

### [W4]. Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model [[HTML]](https://arxiv.org/html/2603.18342) [[PDF]](https://arxiv.org/pdf/2603.18342)
* **Paper ID**: `2603.18342`
* **Authors**: Yanchuan Tang, Taowen Wang, Yuefei Chen, Boxuan Zhang, Qiang Guan, Ruixiang Tang
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇进入 shortlist，是因为它抓住了 VLA 安全落地里常被忽略的一点：平均不确定性会稀释短暂但关键的失败前兆，因此改用 max-based sliding window pooling 去保留风险尖峰。它也给 OpenVLA 在多个 LIBERO 套件上的 rollout-level failure prediction 提供了一个清晰评测框架。没有进最终精选，是因为当前证据主要集中在仿真与黑盒后验分析，距离直接提升控制、数据或 world model 能力还有一步。
* **证据来源**: arXiv HTML
