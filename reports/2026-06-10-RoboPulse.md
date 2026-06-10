# RoboPulse | 2026-06-10

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 95 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线很集中：VLA 正在从“端到端模仿策略”走向更可控的数据、奖励、层级编排、仿真评测和世界动作模型。最终精选覆盖了六个互补入口：CAST 解决语言指令细粒度接地，SARM2 把 dense reward 接入自改进 RL，Hi-VLA 系统性拆解层级代理设计，sim-real correlation 论文回应 VLA 评测可信度，Efficient-WAM 关注世界动作模型部署成本，AllDayNav 则把长期导航、记忆和真实世界 RL 串起来。VIP 作者中，Sergey Levine/Dhruv Shah 的 CAST、Pieter Abbeel 的 SARM2、Dhruv Shah/Mohit Shridhar 的 Hi-VLA，以及 He Wang 的 AllDayNav 最值得优先跟踪。整体看，今天不是单点模型能力提升，而是围绕“让 VLA 可训练、可评测、可部署、可持续改进”的系统化推进。

## 今日信号

- VLA 的瓶颈正在从模型架构本身转向数据语义多样性、奖励密度和测试时决策校验这些系统接口。
- Sim2Real 评测开始从“仿真是否逼真”转向“仿真是否保留真实世界中的策略排序、失败模式和模型选择结论”。
- World Action Model 的核心竞争点不再只是未来视频是否清晰，而是未来表征是否足够动作相关、低延迟、可闭环部署。

## Historical Rediscovery

- **Paper**: Video2Sim2Real: Full-Stack Autonomous Dexterous Skill Acquisition from a Single Human Video [[HTML]](https://arxiv.org/html/2606.08828) [[PDF]](https://arxiv.org/pdf/2606.08828)
  - **Paper ID**: `2606.08828`
  - **来源日期**: 2026-06-09
  - **当时可能被低估的信号**: 当时可能被低估的是“从单个视频到真实灵巧操作”的端到端链路，而不只是某个模块；Kinova Gen + Leap Hand、IsaacGym 和多类日常操作任务也说明它有真实系统野心。
  - **为什么现在值得再看**: 与你的 Sim2Real、World Action Model 和真实部署评测兴趣高度贴近，尤其适合观察视频示范如何转成可执行动作先验与真实策略。
  - **建议动作**: 加入精读
  - **关键词**: `Sim2Real` `dexterous manipulation` `human video` `digital twin` `real deployment`
- **Paper**: Two Bridges, One Pathway: From VLMs to Generalizable VLAs with Embodied Trajectory-Coupled Data [[HTML]](https://arxiv.org/html/2606.08520) [[PDF]](https://arxiv.org/pdf/2606.08520)
  - **Paper ID**: `2606.08520`
  - **来源日期**: 2026-06-09
  - **当时可能被低估的信号**: 当时可能被低估的是 Embodied Trajectory-Coupled data 作为渐进桥接数据配方的价值；它不是单纯扩数据，而是在对齐视觉语言表征与动作目标。
  - **为什么现在值得再看**: 现在值得再看，因为 VLA 的核心瓶颈仍是从互联网/VLM 能力迁移到可泛化动作策略；LIBERO、SimplerEnv、VLABench 和 WidowX 真实任务覆盖也贴近部署评测。
  - **建议动作**: 加入精读
  - **关键词**: `VLA` `VLM-to-VLA` `trajectory-coupled data` `generalization` `real robot`
- **Paper**: GEAR-VLA: Learning Geometry-Aware Action Representations for Generalizable Robotic Manipulation [[HTML]](https://arxiv.org/html/2606.08530) [[PDF]](https://arxiv.org/pdf/2606.08530)
  - **Paper ID**: `2606.08530`
  - **来源日期**: 2026-06-09
  - **当时可能被低估的信号**: 当时可能被低估的是它同时覆盖 unseen objects、background shifts 和 embodiment differences，这些比单一 benchmark 提升更接近真实 VLA 部署问题。
  - **为什么现在值得再看**: 与你关心的 VLA、Sim2Real 和跨 embodiment 泛化强相关；虽然方法栈很重，但正适合作为判断“几何与动作表征是否能提升 VLA 真实泛化”的重点样本。
  - **建议动作**: 加入精读
  - **关键词**: `VLA` `geometry-aware action` `embodiment canonicalization` `3D representation` `deployment`
- **Paper**: MotionVLA: Injecting Geometric Motion into Vision-Language-Action Model [[HTML]](https://arxiv.org/html/2606.08288) [[PDF]](https://arxiv.org/pdf/2606.08288)
  - **Paper ID**: `2606.08288`
  - **来源日期**: 2026-06-09
  - **当时可能被低估的信号**: 当时可能被低估的是 motion memory 对长程 VLA 稳定性的意义；RoboTwin2.0、LIBERO 和 Agilex Piper 初步结果提示它可能改善 motion consistency 与 path efficiency。
  - **为什么现在值得再看**: 如果今天要看长时程操作、World Action Model 或动作连续性，这篇值得补上，因为它提供了一个轻量但针对性强的 VLA 表征增强切口。
  - **建议动作**: 快速浏览
  - **关键词**: `VLA` `geometric motion` `long-horizon manipulation` `temporal stability` `motion consistency`
- **Paper**: World Model for Robot Learning: A Comprehensive Survey [[HTML]](https://arxiv.org/html/2605.00080) [[PDF]](https://arxiv.org/pdf/2605.00080)
  - **Paper ID**: `2605.00080`
  - **来源日期**: 2026-05-04
  - **当时可能被低估的信号**: 当时可能被低估的是它对多条路线的结构化价值：不是提供单点实验，而是帮助判断哪些 world/action model 工作真正服务机器人学习闭环。
  - **为什么现在值得再看**: 与你的 World Model、World Action Model、RL+VLA 兴趣直接相关；今天再看可以用它校准其他候选论文在规划、仿真、评估和数据生成中的位置。
  - **建议动作**: 快速浏览
  - **关键词**: `world model` `robot learning` `planning` `simulation` `evaluation`

## Editor's Picks

### [1]. CAST: Counterfactual Labels Improve Instruction Following in Vision-Language-Action Models [[VIP]] [[HTML]](https://arxiv.org/html/2508.13446) [[PDF]](https://arxiv.org/pdf/2508.13446) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2508.13446`
* **Authors**: Catherine Glossop, William Chen, Arjun Bhorkar, Dhruv Shah, Sergey Levine
* **Author Priority**: Core VIP
* **一句话结论**: 优先看：CAST 用反事实语言-动作标签直接补 VLA 指令跟随短板，是今天最贴近通用机器人数据瓶颈的一篇。
* **关键词**: `VLA` `counterfactual labels` `instruction grounding` `PaliGemma` `real-world evaluation`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

这篇论文针对 VLA 一个很现实的问题：模型虽然能把开放词汇指令映射到动作，但在相似视觉观测下区分细粒度命令的能力不足。机器人数据集通常只有单一、粗粒度或语义不够丰富的语言标注，导致模型容易学习“看见什么就做什么”的视觉先验，而不是认真利用语言。对通用机器人而言，这会限制可控性：同一个场景里，用户可能要求靠近不同目标、避开干扰物、执行相似但动作结果不同的任务。人工重新采集和标注细粒度指令数据成本高，CAST 的动机就是在不增加人类示范的前提下，用 VLM 生成反事实标签，让同一观测对应多个不同语言-动作关系，从而迫使 VLA 学会语言与动作之间更细的绑定。

#### ⚙️ 核心方法

CAST 的核心思想是把已有机器人数据从“单观测、单语言、单动作”扩展成包含反事实指令与动作标签的训练集。根据摘录，作者使用 VLM 生成多样的 counterfactual labels，并为同一观测分配多个 language-action pairs，使策略不能只依赖场景中最显眼的视觉线索，而需要根据指令选择对应行为。模型侧，HTML 摘录明确提到 CounterfactualVLA 使用 PaliGemma 作为基础 VLM 架构，是一个 3B 参数模型，由 2B Gemma 语言模型和 400M SigLIP 视觉语言模型组成。训练后的 checkpoint 也被提到可用。当前摘录只能确认其总体流程是“VLM 辅助生成反事实标注，再用增强数据训练 VLA”，但没有足够信息还原反事实动作如何被精确生成、过滤、对齐到控制空间，以及不同任务中标签质量控制的细节。相对常规 VLA 训练，它的新意不在更大模型，而在改变监督信号结构：让相近视觉状态下存在多个可区分的语言条件，从数据层面强化 instruction grounding。

#### 📊 实验与结果

实验覆盖真实世界导航和操作两类任务。摘录明确给出作者进行了 645 次真实世界导航试验和 120 次真实世界操作试验，并额外报告了无干扰物操作任务的 120 次试验，用来观察 CAST 在杂乱环境中的增益。结论部分称，相比没有反事实标签的等价标准 VLA，CAST 在导航和操作上大约将成功率翻倍。需要注意的是，当前摘录没有提供 Fig. 4、Table II、Table III 的具体数值，因此不能进一步比较各 baseline 的绝对成功率。摘录还提到 CoNVOI 有 6 个任务因基础设施问题缺失评估，这会影响横向对比的完整性。整体证据强点是真机 trial 数量较多，边界是具体任务分布、失败类型和统计显著性仍需看 PDF 表格。

#### ⚠️ 风险 / 保留意见

- 反事实标注依赖 VLM 的物理接地能力，标签错误可能被放大为策略偏差。
- 摘录未展示反事实动作生成和过滤细节，复现时最难确认的是数据增强 pipeline。
- 部分 baseline 评估任务缺失，横向比较需要核查是否仍公平。

#### 💭 结论与启发

这篇对后续 VLA 选题的启发是：提升指令跟随不一定先从更大模型或更多示范开始，也可以从“同一状态下构造互斥语言目标”入手。复现时我会优先把 CAST 当作数据增强模块，而不是完整替换策略架构：先在已有行为克隆数据上生成 hard negative 或 counterfactual instruction，再观察语言敏感性是否提升。系统设计上，它提示我们应显式评测“相似观察、不同指令”的分辨能力，这比单纯平均成功率更能暴露 VLA 是否真的听懂命令。

#### 🔎 读 PDF 先核查

- CAST 如何从 VLM 输出中生成可执行的反事实动作标签，而不只是生成不同语言描述？
- 训练时多个 language-action pairs 如何组织采样，是否会引入互相冲突的监督信号？
- 成功率提升主要来自杂乱场景中的目标消歧，还是来自更一般的行为多样性增强？

#### 📌 上传 PDF 后优先看

- 反事实标签生成与过滤流程章节
- 真实世界导航和操作结果表格
- 无干扰物与有干扰物操作任务的对比实验

### [2]. SARM2: Multi-Task Stage Aware Reward Modeling for Self Improving Robotic Manipulation [[VIP]] [[HTML]](https://arxiv.org/html/2606.10305) [[PDF]](https://arxiv.org/pdf/2606.10305) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.10305`
* **Authors**: Qianzhong Chen, Hau Zheng, Justin Yu, Suning Huang, Jiankai Sun, Ken Goldberg, Chuan Wen, Pieter Abbeel, Yide Shentu, Philipp Wu, Mac Schwager
* **Author Priority**: Core VIP
* **一句话结论**: 优先看：SARM2 把长程操作的阶段感知奖励模型做成多任务版本，并接入自改进 RL，是 VLA+RL 方向的关键样本。
* **关键词**: `VLA fine-tuning` `reward model` `reinforcement learning` `stage-aware reward` `self-improvement`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

长程机器人操作很难只靠行为克隆扩展，因为高质量示范昂贵，且策略容易停留在示范分布附近。VLA 在短程任务上已经成为主流端到端范式，但面对多阶段、组合式、工具使用类任务时，单纯 SFT 往往既缺 dense feedback，也缺主动纠错能力。奖励模型可以缓解这个问题：离线时用于重加权和筛选数据，在线时可为机器人 rollout 提供强化学习信号。但摘录指出已有路线有两类缺口：任务特定 stage-aware reward 精准但需要每个任务标注；通用 VLM reward 适用面广但对长程细粒度进展判断太粗。SARM2 的目标就是在多任务场景里给出可泛化、密集、阶段感知的奖励，并让策略通过自主 rollout 形成数据飞轮。

#### ⚙️ 核心方法

方法分成 SARM2 和 SPIRAL 两部分。SARM2 是多任务 stage-aware reward model，用任务无关的 action primitive 作为中间表示，替代原 SARM 中依赖任务特定标注的 stage estimator。摘录给出的动机是，许多 manipulation demonstration 都能分解成跨任务复用的动作原语序列，而且原语词表较小，部分原语语义相近或互为对偶，因此可以压缩成更通用的阶段表示。随后，SARM2 结合 multi-gate MoE value decoder，为不同任务或阶段生成更准确的 dense progress estimate。SPIRAL 则把 SARM2 的 dense rewards 用到 autonomous on-policy self-improvement 中，让策略从便宜的自主 rollout 中持续改进，而不是只依赖离线示范或人工 DAgger。当前摘录能确认 action-primitive stage estimator、MMoE value decoder 和 CQL/在线改进式 reward-aligned loop 的总体关系，但具体 reward target、MoE gate 输入、rollout 采样和策略更新公式需要 PDF 进一步核查。新意在于把“阶段感知”从单任务工程标注转成可跨任务复用的原语层接口。

#### 📊 实验与结果

实验围绕三个问题：SARM2 的原语阶段估计器和 MMoE 是否提升长程与组合任务 value modeling；SPIRAL 是否能通过 rollout 超过 BC 和 offline RL baseline；奖励模型质量为何对数据飞轮关键。摘录明确说明 reward model evaluation 使用 10 个 manipulation tasks，分为 5 个 classic tasks 和 5 个 unconventional tasks，后者包含工具使用或多阶段组合执行。对比包括 ReWiND、TOPReward 和 Robometer，并提到 TOPReward 使用 Qwen3-VL-8B-Instruct，Robometer 还测试了 LoRA fine-tuned variant。结论称 SARM2 在 10-task benchmark 上表现优于若干基线，SPIRAL 支持 continual policy refinement。由于摘录未给出具体数值，不能判断增益幅度和各任务方差，需后续核查表格。

#### ⚠️ 风险 / 保留意见

- action primitive 词表是否足够覆盖开放长程任务，是跨域泛化的核心风险。
- 奖励模型错误会直接驱动 on-policy self-improvement，可能造成 reward hacking 或错误数据飞轮。
- 摘录未给出真实机器人证据细节，部署可信度需要看实验章节。

#### 💭 结论与启发

这篇值得作为“VLA 后训练/RL 化”的主线论文读。它提示我们，直接让 VLM 判断任务成功可能太粗，而把操作拆成可复用 action primitives，能提供更稳定的中间监督。后续如果做长程 manipulation，我会优先评估能否从现有示范中自动抽取阶段或原语，再训练 dense reward，而不是直接上稀疏成功奖励。系统上，SARM2+SPIRAL 的组合也提醒我们，奖励模型本身必须被当成一等公民评测，否则在线自改进只是把偏差迭代放大。

#### 🔎 读 PDF 先核查

- action-primitive stage estimator 的原语集合如何定义、压缩和标注，是否依赖内部数据？
- MMoE value decoder 相比单头 value model 的收益主要来自任务分化还是阶段分化？
- SPIRAL 中策略更新如何避免被不准确 dense reward 牵引到错误行为？

#### 📌 上传 PDF 后优先看

- SARM2 action primitive stage estimator 设计章节
- 10-task reward model 对比与消融表格
- SPIRAL on-policy rollout 与 BC/offline RL 对比实验

### [3]. What Matters in Orchestrating Robot Policies: A Systematic Study of Hierarchical VLA Agents [[VIP]] [[HTML]](https://arxiv.org/html/2606.10267) [[PDF]](https://arxiv.org/pdf/2606.10267) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.10267`
* **Authors**: Jiaheng Hu, Mohit Shridhar, Caden Lu, Dhruv Shah, Hao-Tien Lewis Chiang, Jie Tan, Annie Xie
* **Author Priority**: Extended VIP
* **一句话结论**: 优先看：这篇不是提出单一 Hi-VLA，而是系统回答层级 VLA 里 planner、controller、终止、观察和记忆到底哪些设计更重要。
* **关键词**: `hierarchical VLA` `VLM planner` `VLA controller` `memory` `ALOHA`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

#### 📖 背景与动机

层级 VLA 已经成为长程操作的一条自然路线：高层 VLM 负责把复杂任务分解成语言子目标，低层 VLA 负责执行每个子目标。但现有系统往往各做各的，planner、controller、切换条件、观察表示和记忆机制都不同，很难判断性能来自哪一个组件。论文动机很清楚：单体 VLA 在短程指令上可控，但长程、组合、抽象推理任务受限，一方面训练数据多是短轨迹片段，另一方面对 VLM 进行动作微调可能损害原有推理能力。层级化可以保留 VLM 的规划能力，同时让 VLA 专注执行，但如果没有统一研究框架，社区很容易被个别系统结果误导。本文价值在于做 controlled study，提炼 Hi-VLA 的设计原则。

#### ⚙️ 核心方法

论文构建了一个灵活的 Hi-VLA 统一框架，把代表性层级代理归入同一组件化接口：高层 VLM policy 生成或更新子目标，低层 VLA policy 执行动作，termination condition 决定何时从执行切回规划，observation representation 向 planner 提供环境状态，memory system 维护跨阶段上下文。摘录没有给出算法细节全文，但实验部分明确表示作者分别评估高层 VLM、低层 VLA、终止条件、观察模态和记忆机制，并在最后聚合每个组件的最佳设计，与 flat VLA 和 naive hierarchical VLA 比较。这种方法的新意不在于发明一个复杂模块，而在于把 Hi-VLA 从经验堆叠变成可消融的系统工程问题。当前摘录只能确认研究对象和组件维度，不能确认具体使用了哪些 VLM/VLA 模型、各观察编码形式、记忆写入策略和终止判别器实现。对读者来说，关键是把它当作“层级 VLA 设计空间地图”来读，而非只看最终成功率。

#### 📊 实验与结果

主实验在 MuJoCo ALOHA suite 中进行，摘录称该模拟桌面操作 benchmark 已展示 real-to-sim transferability；此外作者还在真实 ALOHA 机器人上做实验。任务被分为 short-horizon、long-horizon 和 reasoning 三类，以覆盖普通执行、长程组合和需要推理的场景。实验依次分析高层 VLM、低层 VLA、termination、observation representation、memory system 的影响，并把每个组件的最佳选择聚合后，与 flat VLA 和 naive hierarchical VLA 比较。当前摘录没有提供任何具体成功率或模型名称，因此结果只能保守表述为“系统性评估并给出设计指导”。证据边界在于，需要 PDF 中的 Sec. 4.2-4.7 确认每个组件结论是否稳定、是否只在 ALOHA 类任务成立。

#### ⚠️ 风险 / 保留意见

- 设计原则可能强依赖 MuJoCo ALOHA 和 ALOHA 机器人任务形态。
- 若高层 VLM 或低层 VLA 选择有限，结论可能不能外推到最新通用策略。
- 摘录缺少具体数值，当前只能确认研究框架，不能确认哪项设计最关键。

#### 💭 结论与启发

这篇适合当作搭建 Hi-VLA 系统前的检查清单。它提醒我不要只问“用哪个 planner”，还要同时设计何时重规划、planner 看什么、历史如何保留，以及低层控制器能否稳定执行语言子目标。后续复现时，可以不完整复刻所有组合，而是优先复现框架中的组件消融：flat vs naive hierarchy vs best aggregated hierarchy。论文阅读重点应放在负结果和组件敏感性上，因为这些比最终最优配置更能指导真实系统设计。

#### 🔎 读 PDF 先核查

- termination condition 是规则、模型判别还是由 planner 自我判断，哪种对长程任务最稳？
- planner 的 observation representation 中，图像、语言摘要和历史记忆各自贡献多大？
- 聚合最佳组件后的 Hi-VLA 是否存在组件交互效应，还是各项改进可以近似独立叠加？

#### 📌 上传 PDF 后优先看

- 高层 VLM 与低层 VLA 组件消融章节
- termination、observation、memory 三组设计实验
- flat VLA、naive Hi-VLA 与 best aggregated Hi-VLA 总对比

### [4]. A Practical Recipe Towards Improving Sim-and-Real Correlation for VLA Evaluation [[HTML]](https://arxiv.org/html/2606.10366) [[PDF]](https://arxiv.org/pdf/2606.10366) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.10366`
* **Authors**: Shuo Wang, Hanyuan Xu, Yingdong Hu, Fanqi Lin, Yang Gao
* **Author Priority**: Standard
* **一句话结论**: 优先看：这篇把 VLA 仿真评测从“看起来逼真”拉回到“能否保留真实模型排序”，对 Sim2Real benchmark 选择很有用。
* **关键词**: `Sim2Real` `VLA evaluation` `rank correlation` `benchmark` `perturbation`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

VLA 模型越来越多，真实机器人评测却昂贵、慢且难以规模化，因此仿真 benchmark 成为模型选择和失败分析的重要工具。但仿真是否能替代真实评测，不能只看视觉/物理是否更逼真，而要看它是否保留真实世界中的结论：哪个策略更强、哪些扰动会失败、性能变化是否与真实一致。论文的动机正是 sim-and-real correlation。近年的 VLA-Arena、SIMPLER、REALM 等平台提升了任务多样性、视觉真实感和 perturbation 结构，但仍未被广泛当作可靠真实代理。本文将问题转成测量问题：评估仿真是否能在策略排序、一致性相关和扰动失败模式上预测真实世界表现。

#### ⚙️ 核心方法

方法核心是统一比较多个模拟 VLA benchmark、多个近期 VLA policies、任务和扰动因素，并用排名一致性与相关性指标衡量 sim-real 对齐。摘录明确提到作者比较 VLA-Arena、SIMPLER、REALM 三个代表性模拟 benchmark，覆盖五个近期 VLA policy，其中包括 GR00T N1.6 和 GR00T N1.7，其他模型名在摘录中因格式缺失不能可靠还原。作者认为，一个 faithful simulator 应该保留真实世界中的 policy ranking，因为模型选择本质上是相对决策：如果真实世界中 A 优于 B，仿真最好也给出相同排序。指标包括 Spearman rank correlation、Pearson correlation 和 Mean Maximum Rank Violation。Spearman 衡量相对排序，Pearson 衡量分数线性跟踪，MMRV 衡量高 margin 排名错误的严重程度。相对常见 benchmark 论文，这篇的新意是把“仿真可用性”定义为决策一致性，而不只是任务覆盖或渲染质量。当前摘录没有给出 practical recipe 的完整建议，需要看正文确认哪些模拟信号更可靠。

#### 📊 实验与结果

实验设计覆盖多平台、多策略、多任务和 perturbation factors，目标是判断模拟评测是否保留真实世界结论。摘录称研究会测量 policy ranking consistency、performance correlation 和 perturbation-wise failure patterns，并据此刻画现有 simulator 的局限。Method 摘录提到 Table 1 展示各 benchmark 和扰动维度下的策略排名，Table 2 报告 Spearman、Pearson 和 MMRV。由于当前没有具体表格数值，不能说哪一个平台总体最好，也不能引用具体相关系数。结论保守表达为：提升 sim-real correlation 既需要可靠 simulator design，也需要 appropriate simulator use；模拟器应优先保留真实策略排序，尤其避免严重误导模型选择的排名错误。

#### ⚠️ 风险 / 保留意见

- 结论可能随被评估的五个 VLA policy 集合变化，不能自动外推到所有新模型。
- 若真实世界评测本身 trial 数不足或任务偏窄，相关性指标会受噪声影响。
- 摘录缺少具体平台排名和 recipe 细节，暂不能给出明确 benchmark 选择建议。

#### 💭 结论与启发

这篇对日常论文筛选和复现实验很实用：以后看 VLA 仿真结果时，不能只问 benchmark 是否真实，而要问它是否能预测真实模型排序。系统设计上，如果资源有限，可以把仿真用于筛掉明显差的模型、定位扰动失败模式，但最终模型选择仍要用少量真实评测校准。复现时我会优先实现 Spearman、Pearson、MMRV 三类指标，把自己的 sim benchmark 与小规模真实 rollout 做闭环验证。

#### 🔎 读 PDF 先核查

- 三种模拟平台在不同 perturbation 维度上的相关性是否一致，还是只在特定扰动下有效？
- MMRV 揭示的高 margin 排名错误主要来自视觉差距、物理差距还是任务协议差距？
- 论文提出的 practical recipe 是否能转化为具体 benchmark 使用流程，而不只是评估后分析？

#### 📌 上传 PDF 后优先看

- Table 1 的各平台策略排名结果
- Table 2 的 Spearman、Pearson、MMRV 指标
- perturbation-wise failure pattern 与 practical recipe 章节

### [5]. Efficient-WAM: A 1B-Parameter World-Action Model with Low-Cost Future Imagination [[HTML]](https://arxiv.org/html/2606.10040) [[PDF]](https://arxiv.org/pdf/2606.10040) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.10040`
* **Authors**: Jiajun Li, Tiecheng Guo, Yifan Ye, Rongyu Zhang, Xiaowei Chi, Qianpu Sun, Ying Li, Yunfan Lou, Yan Huang, Zhihe Lu, Meng Guo, Shanghang Zhang
* **Author Priority**: Standard
* **一句话结论**: 优先看：Efficient-WAM 把世界动作模型的重点从高清未来视频转向动作相关低成本想象，是 WAM 部署方向的重要信号。
* **关键词**: `World Action Model` `future imagination` `low latency` `action-centric representation` `video-action denoising`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

World-Action Models 通过把未来视觉预测和动作生成耦合起来，为机器人控制提供物理动态和世界先验。但现有强 WAM 往往依赖很大的视频生成器，默认更清晰、更真实的未来视频会带来更好的动作。这在部署上代价很高：推理延迟大、硬件要求高，难以满足实时闭环控制。论文提出一个更实用的判断：控制需要的不是照片级未来，而是保留任务相关几何、运动趋势和接触线索的未来表征。对 VLA/WAM 领域而言，这个转向很关键，因为它把模型能力指标从“生成质量”重新绑定到“动作质量”和“延迟预算”。Efficient-WAM 试图在保持未来想象控制收益的同时，大幅降低推理成本。

#### ⚙️ 核心方法

Efficient-WAM 是一个 1B 参数 World-Action Model，核心是 action-centric future imagination。根据摘录，它通过从 WAN-2.2-5B 转移得到 compact video expert，压缩视频分支；再引入 low-resolution future latents 和 asymmetric video-action denoising，减少未来想象的计算量，同时保留动作生成所需的物理先验。实验设置中作者区分两个版本：Efficient-WAM 作为结构基线，保留高分辨率未来预测和对称 denoising，用来隔离 1B compact video expert 的贡献；Efficient-WAM-RT 则是面向实时物理部署的优化版本，集成低分辨率未来 latent 与非对称视频-动作 denoising，以少量精度交换低延迟。摘录还提到遵循 action-chunking policies 进行闭环动作预测。当前摘录只能确认这些模块和设计原则，不能还原 MoT 模型内部结构、token 设计、denoising schedule 或动作头训练损失。相对已有 WAM，它的新意是承认视觉未来可以降保真，只要动作相关信息不丢。

#### 📊 实验与结果

实验部分围绕模型配置展开：Efficient-WAM 用来验证轻量化 1B 架构是否仍能保持控制先验，Efficient-WAM-RT 用来验证面向实时部署的低延迟 pipeline。摘录称高分辨率未来预测和对称 denoising 可作为 distilled 1B 架构能力上界，而低分辨率 future latents 与 asymmetric denoising 会有意降低视觉保真，以换取速度。结论称该框架实现了大幅 inference latency reduction，同时保持控制收益。由于摘录没有给出具体 benchmark、任务成功率、延迟数值或真实机器人 trial，不能引用“多少倍加速”或“多少成功率”。现阶段可确认的证据是论文系统性比较结构基线和实时优化版本，但具体性能边界需要看实验表格。

#### ⚠️ 风险 / 保留意见

- 低分辨率未来 latent 可能在精细接触、透明物体或小目标任务中丢失关键线索。
- 摘录未给出具体延迟和成功率数值，部署收益需要核查表格。
- 从 WAN-2.2-5B 转移的 compact expert 可能带来训练资源和数据依赖风险。

#### 💭 结论与启发

这篇对 WAM 方向的最大启发是：未来预测应服务控制，而不是服务视觉保真。后续做世界模型或 action model 时，可以把未来表示设计成任务相关 bottleneck，优先评测动作成功率、闭环延迟和失败类型，而不是只看视频质量。复现上，我会优先关注 Efficient-WAM-RT 的三个接口：低分辨率 future latent、视频/动作非对称 denoising、action chunk 输出。如果这些模块能独立插入已有策略，就可能成为实用的部署优化组件。

#### 🔎 读 PDF 先核查

- compact video expert 从 WAN-2.2-5B 转移时保留了哪些能力，哪些能力被有意舍弃？
- low-resolution future latents 在哪些任务上不影响控制，在哪些任务上会明显伤害精细操作？
- asymmetric video-action denoising 如何分配视频与动作计算预算，是否会改变闭环稳定性？

#### 📌 上传 PDF 后优先看

- compact video expert 与 world-knowledge transfer 章节
- Efficient-WAM vs Efficient-WAM-RT 消融实验
- 延迟、成功率和真实部署结果表格

### [6]. AllDayNav: Lifelong Navigation via Real-World Reinforcement Learning [[VIP]] [[HTML]](https://arxiv.org/html/2606.10927) [[PDF]](https://arxiv.org/pdf/2606.10927) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.10927`
* **Authors**: Hang Yin, Yinan Liang, Jiazhao Zhang, Jiahang Liu, Minghan Li, Zhizheng Zhang, He Wang
* **Author Priority**: Core VIP
* **一句话结论**: 优先看：AllDayNav 把真实世界长期导航、开放词汇指令、记忆更新和 RL 自学习合成闭环，是今天最系统的 embodied navigation 论文。
* **关键词**: `lifelong navigation` `real-world RL` `multimodal memory` `VLA` `CQL`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

长期导航要求机器人在动态环境中持续记住并更新场景理解，而不是每次都从零开始。传统显式地图或 scene graph 在结构化环境中有效，但面对长时间运行、局部视野、物体位置变化和开放词汇用户目标时，维护成本和泛化能力都会受限。VLA foundation models 提供了视觉语义理解和指令到动作的基础能力，但摘录指出它们仍缺少 persistent multimodal memory，也难以通过持续交互自我适应。AllDayNav 的动机就是把环境动态隐式写入大模型参数，并配合自演化多模态记忆，让机器人在未知动态环境中自主探索、生成开放词汇指令、检索目标并通过强化学习持续改进。

#### ⚙️ 核心方法

AllDayNav 是一个闭环 lifelong self-learning navigation framework，由四个模块组成。第一是 self-evolving multimodal memory database，维护并更新视觉 keyframes、语义描述和时间上下文，用来承载长期场景经验。第二是 self-instruction generation 与 hybrid goal retrieval 机制，让系统能从记忆中生成或检索开放词汇导航目标。第三是 pretrained VLA navigation backbone，将观察和目标图像映射到导航动作；该模型通过大规模 image-goal navigation 数据预训练，获得基础 visuomotor 和空间能力。第四是 conservative Q-learning-based policy optimization，用自主交互产生的数据做策略优化。摘录还说系统实现 memory-policy co-evolution，并包含 sim-to-real transfer 和 online learning 的实现细节。当前摘录只能确认 CQL 风格优化和记忆-策略闭环，不能确认 reward 定义、memory 写入/遗忘规则、goal retrieval 打分和在线更新频率。相比单纯地图式导航或零样本 VLA，它的新意在于把长期记忆数据库、开放词汇自指令和真实世界 RL 改进联成一个可持续运行系统。

#### 📊 实验与结果

实验使用 Habitat simulator 作为主要仿真平台，预训练数据来自 HM3D 和 MP3D 的训练划分。主评估选取五个未见室内场景，以测试不同布局和空间配置下的泛化能力。真实机器人部分部署在 Unitree Go2 四足机器人上，覆盖三个真实环境：实验室、客厅和家庭。摘录称系统能够从初始化、自主探索到响应用户指令完整运行，并强调无监督、无人工干预的持续自我改进。当前没有具体成功率、路径效率、探索时长或 RL 收敛曲线，因此不能量化相对提升。证据强点是真实平台和多环境部署；边界是需要核查用户指令集合、环境动态变化程度和 online learning 是否在真实机器人上充分闭环。

#### ⚠️ 风险 / 保留意见

- 长期记忆库可能累积过期或错误语义描述，影响开放词汇目标检索。
- CQL 式在线改进若奖励或目标生成有偏，可能把导航策略推向局部行为模式。
- 摘录缺少定量结果，真实部署的稳定性和学习效率仍需核查。

#### 💭 结论与启发

AllDayNav 对我后续看导航类 VLA 的启发是，长期能力不只是更大的 backbone，而是记忆、目标生成、检索和策略更新的闭环设计。复现时可以先拆成两个可验证子系统：多模态 memory 是否能稳定支持开放词汇 goal retrieval，RL 更新是否真的改善未见环境导航。系统设计上，它也提醒我们不要把地图和记忆对立起来；即使不显式构建 scene graph，也需要可查询、可更新、带时间上下文的外部记忆来支撑长时运行。

#### 🔎 读 PDF 先核查

- self-evolving memory 如何决定写入、更新和遗忘，是否能处理物体位置变化？
- self-instruction generation 产生的目标如何避免偏离真实用户需求或环境可达性？
- CQL-based policy optimization 在真实 Unitree Go2 部署中是否在线执行，还是主要在仿真中验证？

#### 📌 上传 PDF 后优先看

- multimodal memory database 与 hybrid goal retrieval 章节
- CQL policy optimization 和在线学习实现细节
- Habitat 五场景与 Unitree Go2 三真实环境评估结果

## Watchlist

### [W1]. HiMem-WAM: Hierarchical Memory-Gated World Action Models for Robotic Manipulation [[HTML]](https://arxiv.org/html/2606.10363) [[PDF]](https://arxiv.org/pdf/2606.10363)
* **Paper ID**: `2606.10363`
* **Authors**: Xiaoquan Sun, Ruijian Zhang, Chen Cao, Yihan Sun, Jiahui Chen, Zetian Xu, Bo Chen, Haijier Chen, Zhen Yang, Jiarun Zhu, Yijun Hong, JingZhe Xu, Jingrui Pang, Mingqi Yuan, Jiayu Chen
* **Author Priority**: Standard
* **为什么还值得留意**: HiMem-WAM 进入 watchlist 是因为它和 Efficient-WAM 同属 WAM 主线，但更强调长程 manipulation 的记忆门控、skill latent 和 latent action。摘录显示它评估 LIBERO、LIBERO-PLUS、RMBench，并包含真实机器人部署，方向很相关。不过最终没有进入精选，是因为今天已选择 Efficient-WAM 代表 WAM 部署效率主线，而 HiMem-WAM 的具体增益和记忆机制细节仍需 PDF 数值支撑。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. VeriSpace: Spatially Grounded Action Verification for Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2606.10568) [[PDF]](https://arxiv.org/pdf/2606.10568)
* **Paper ID**: `2606.10568`
* **Authors**: Guiyu Zhao, Longteng Guo, Junyou Zhu, Jun Fu, Yanghong Mei, Bin Cao, Jie Jiang, Xingjian He, Jing Liu
* **Author Priority**: Standard
* **为什么还值得留意**: VeriSpace 值得跟踪，因为它把 VLA 测试时动作选择从 one-shot prediction 改成 sample-and-verify，并引入 RGB-D/3D-aware spatial grounding 来评估候选 7D 操作动作。它对真实部署可靠性很有意义，且摘录显示包含 SimplerEnv-WidowX、LIBERO 和真实机器人实验。未进最终精选的原因是今天主线更偏训练、评测和 WAM/RL 系统，VeriSpace 更像测试时校验模块，优先级略低。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. GHOST: Hierarchical Sub-Goal Policies for Generalizing Robot Manipulation [[HTML]](https://arxiv.org/html/2606.10025) [[PDF]](https://arxiv.org/pdf/2606.10025)
* **Paper ID**: `2606.10025`
* **Authors**: Sriram Krishna, Ben Eisner, Haotian Zhan, Ying Yuan, Haoyu Zhen, Chuang Gan, Shubham Tulsiani, David Held
* **Author Priority**: Standard
* **为什么还值得留意**: GHOST 进入 watchlist 是因为它用 3D end-effector sub-goal 和低层 goal-conditioned controller 做层级 manipulation，和 Hi-VLA 的层级设计问题形成呼应。它还通过把 3D goal 投影成图像平面 end-effector heatmaps，提供了连接人类示范和机器人策略的实用接口。未进精选主要因为最终已选 2606.10267 作为更系统的层级 VLA 设计研究，而 GHOST 更偏具体 imitation learning 架构。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

### [W4]. MIND-V: Hierarchical World Model for Long-Horizon Robotic Manipulation with RL-based Physical Alignment [[HTML]](https://arxiv.org/html/2512.06628) [[PDF]](https://arxiv.org/pdf/2512.06628)
* **Paper ID**: `2512.06628`
* **Authors**: Ruicheng Zhang, Mingyang Zhang, Jun Zhou, Xiaofan Liu, Zunnan Xu, Zhizhou Zhong, Puxin Yan, Haocheng Luo, Xiu Li
* **Author Priority**: Standard
* **为什么还值得留意**: MIND-V 值得列入 watchlist，因为它提出层级视频 world model，用 Semantic Reasoning Hub、Behavioral Semantic Bridge 和 Motor Video Generator 合成长程操作视频，并用 GRPO 与 Physical Foresight Coherence reward 做物理对齐。摘录中有较具体的训练和推理成本信息，例如 CogVideoX-5B 初始化、Bridge V2、111-frame 三子任务视频约 50GB VRAM。没有进入最终精选，是因为它更偏数据合成/视频世界模型，离 VLA 控制闭环和真实机器人执行证据还有一层距离。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
