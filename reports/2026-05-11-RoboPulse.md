# RoboPulse | 2026-05-11

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 81 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线不是单一 VLA 架构扩张，而是围绕“如何让动作模型更可部署、更可验证、更能利用未来想象”展开：视频规划、动作推理、世界动作模型一致性、低数据适配、触觉反馈和潜在推理都在争夺下一代机器人基础模型的位置。最终精选保留了两类强信号：一类是 LVP、MolmoAct2 这种面向通用部署的大模型路线，另一类是 WAM/LaRA/AT-VLA/ACA 这种针对可靠性、实时反馈和适配效率的机制型论文。VIP 作者上，Pieter Abbeel 与 Russ Tedrake 参与的 LVP 最值得优先跟踪，Dieter Fox 参与的 MolmoAct2 也值得关注其开放权重和低成本硬件部署主张。没有进入精选的论文多是方向重要但证据边界、工程成熟度或与今日主线的贴合度略低。

## 今日信号

- VLA 正从“看图给动作”转向“生成或评估未来”：视频规划、WAM 和 latent reasoning 都在尝试把动作放进可预测的时序结构里。
- 真实部署问题正在压过 benchmark 分数本身：低成本硬件、少样本适配、触觉闭环、延迟和开放权重成为今天多篇论文的共同焦点。
- 世界模型路线的关键瓶颈不再只是画面是否逼真，而是动作与状态转移是否动态一致、是否能作为测试时选择或策略学习的可靠信号。

## Editor's Picks

### [1]. Large Video Planner Enables Generalizable Robot Control [[VIP]] [[HTML]](https://arxiv.org/html/2512.15840) [[PDF]](https://arxiv.org/pdf/2512.15840) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2512.15840`
* **Authors**: Boyuan Chen, Tianyuan Zhang, Haoran Geng, Caiyi Zhang, Peihao Li, Kiwhan Song, William T. Freeman, Jitendra Malik, Pieter Abbeel, Russ Tedrake, Vincent Sitzmann, Yilun Du
* **Author Priority**: Core VIP
* **一句话结论**: 优先读：这是今天最强的“视频作为机器人规划主模态”路线，且有 Pieter Abbeel 与 Russ Tedrake 加持。
* **问题与切口**: LVP 试图绕开传统 VLA 直接从图像和语言预测动作的路径，把大规模视频预训练放在机器人基础模型的中心位置。它的核心切口是先生成“人会如何完成任务”的视频运动计划，再把该计划重定向到不同机器人形态上。相对已有 VLA，它强调视频天然包含时空动态与物理过程，因此更适合作为跨任务、跨场景的规划表示。
* **核心方法与证据**: 正文给出的路线是两阶段：14B 参数视频基础模型根据场景帧和文本任务生成视频计划，随后通过开源重建与重定向工具把视觉计划转成机器人动作。数据侧包含作者整理的人类活动与机器人演示视频。实验摘录显示其在第三方任务套件上做零样本泛化评估，并在咖啡豆舀取、撕胶带等更难任务中展示优势，但具体数值仍需 PDF 核查。
* **正文要点**:
  - 方法明确把“规划”放在视频空间，而不是把 MLLM 直接扩展到 action token。
  - 论文强调可把同一视频计划重定向到灵巧五指手或平行夹爪等不同 embodiment。
  - 实验摘录称基线在接近训练分布的 pick-and-place 上较强，但在任务级泛化上更吃力。
* **为什么值得跟**:
  - 如果视频生成计划可靠，机器人 foundation model 可以更充分利用互联网规模人类活动视频。
  - 它把“形态无关的意图/运动计划”和“形态相关的控制执行”拆开，提供了新的系统分解方式。
  - 对 VLA 社区而言，这是从语言-图像预训练迁移到动作之外的另一条基础模型路线。
* **风险 / 保留意见**:
  - 视频计划到真实控制的重定向质量可能成为主要瓶颈，摘要摘录不足以判断失败模式。
  - 实验虽声称强零样本泛化，但具体任务数量、成功率和基线公平性需上传 PDF 后核查。
* **建议先看**: 先看视频规划模型、数据构建和 retargeting 三者如何衔接，再看第三方任务评估是否真的支持“任务级泛化”这一主张。尤其要核查失败案例是否来自生成视频不合理，还是动作提取不稳定。
* **关键词**: `Large Video Planner` `video foundation model` `robot planning` `retargeting` `zero-shot generalization`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 视频生成计划中哪些信息足以被稳定重定向为机器人动作，哪些仍依赖手工或外部工具假设？
  - 人类活动视频与机器人演示视频在训练中如何配比，是否会影响机器人可执行性？
  - 所谓任务级泛化的优势是否主要来自视频先验，还是来自评估任务与互联网视频分布的重合？
* **上传 PDF 后优先看**:
  - 视频基础模型架构与训练数据章节
  - action extraction / retargeting 机制章节
  - 第三方任务套件、零样本实验和失败案例分析

### [2]. MolmoAct2: Action Reasoning Models for Real-world Deployment [[VIP]] [[PDF]](https://arxiv.org/pdf/2605.02881) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.02881`
* **Authors**: Haoquan Fang, Jiafei Duan, Donovan Clay, Sam Wang, Shuo Liu, Weikai Huang, Xiang Fan, Wei-Chuan Tsai, Shirui Chen, Yi Ru Wang, Shanli Xing, Jaemin Cho, Jae Sung Park, Ainaz Eftekhar, Peter Sushko, Karen Farley, Angad Wadhwa, Cole Harrison, Winson Han, Ying-Chun Lee, Eli VanderBilt, Rose Hendrix, Suveen Ellawela, Lucas Ngoo, Joyce Chai, Zhongzheng Ren, Ali Farhadi, Dieter Fox, Ranjay Krishna
* **Author Priority**: Extended VIP
* **一句话结论**: 优先读但要带着证据边界读：MolmoAct2 把开放、低成本、推理增强和真实部署问题放在同一个 VLA 系统里。
* **问题与切口**: MolmoAct2 面向的是当前 VLA 在真实部署中的痛点：闭源 frontier 模型不可控，开放模型常绑定昂贵硬件，推理增强策略又可能带来过高延迟。它提出一个 fully open action reasoning model，并围绕空间/具身推理 backbone、低到中成本平台数据和双臂遥操作数据来补齐部署链条。由于这里只提供摘要回退信息，系统细节和实验强度需要保守看待。
* **核心方法与证据**: 摘要中可确认的模块包括 MolmoER 这一面向空间与具身推理特化的 VLM backbone，训练语料规模为 3.3M sample，并采用 specialize-then-rehearse recipe。论文还释放三类面向低到中成本平台的数据，其中 MolmoAct2-BimanualYAM 包含 720 小时双臂遥操作轨迹。摘要没有提供完整实验设置和成功率细节，因此部署有效性只能先视为作者主张。
* **正文要点**:
  - 论文明确把“真实部署标准”作为评价对象，而不只是追求通用 VLA benchmark 表现。
  - MolmoER 被描述为专门强化空间和具身推理的 VLM backbone。
  - MolmoAct2-BimanualYAM 的 720 小时双臂遥操作数据是摘要中最明确的数据资产信号。
* **为什么值得跟**:
  - 开放权重与低成本平台结合，可能降低 VLA 真实复现实验门槛。
  - 双臂数据若质量足够，会补上开放 VLA 在 bimanual manipulation 上的稀缺资源。
  - Dieter Fox 参与使其在机器人部署和 embodied AI 社区内值得持续跟踪。
* **风险 / 保留意见**:
  - 当前只有摘要回退，缺少正文实验、模型结构和失败模式证据。
  - “action reasoning”若依赖复杂推理链，仍需核查其延迟是否真正满足闭环控制。
* **建议先看**: 上传 PDF 后先确认它的开放内容到底包括权重、数据、代码还是部分组件，再看低成本硬件上的真实任务成功率与延迟。不要只看模型名，要看部署约束是否被严格测量。
* **关键词**: `MolmoAct2` `action reasoning` `open VLA` `bimanual manipulation` `real-world deployment`
* **证据来源**: Abstract fallback
* **读 PDF 先核查**:
  - MolmoER 的 specialize-then-rehearse 具体如何避免空间推理特化后遗忘通用视觉语言能力？
  - 720 小时双臂数据覆盖哪些任务、硬件和传感器配置，是否足以支撑跨平台泛化？
  - 论文如何量化 reasoning 带来的收益与推理延迟之间的取舍？
* **上传 PDF 后优先看**:
  - 模型与 MolmoER 训练配方章节
  - 数据集发布与硬件平台描述章节
  - 真实部署评估、延迟和成功率实验

### [3]. Is the Future Compatible? Diagnosing Dynamic Consistency in World Action Models [[HTML]](https://arxiv.org/html/2605.07514) [[PDF]](https://arxiv.org/pdf/2605.07514) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.07514`
* **Authors**: Bo-Kai Ruan, Teng-Fang Hsiao, Ling Lo, Hong-Han Shuai
* **Author Priority**: Standard
* **一句话结论**: 优先读：它给 WAM 提出一个很关键的可靠性轴线，即未来预测必须和动作导致的状态变化相容。
* **问题与切口**: 这篇论文关注 World Action Model 的核心盲点：生成的未来可能视觉上合理，却未必和它声称执行的动作序列动态一致。作者把 action-state consistency 定义为 WAM 可靠性的缺失维度，并用它区分成功与失败轨迹。相对只看 reward、视觉预测质量或 value 的路线，它提供了一个更贴近“动作是否真的造成该状态转移”的诊断与测试时选择信号。
* **核心方法与证据**: 方法上，WAM 在每个决策步采样多个候选分支，每个分支同时预测动作序列和未来观测。作者提出 Consistency-Exploring，通过环境执行评估分支一致性；以及 Consistency-Consensus，在不执行环境的情况下按预测未来之间的共识打分。实验覆盖 Cosmos-Policy/RoboCasa 与 LingBot-VA/RoboTwin 2.0，摘录中报告 RoboCasa 上有小幅但一致的提升，并指出 background collapse 是重要失败模式。
* **正文要点**:
  - 论文比较了 joint-prediction 与 inverse-dynamics 两类 WAM formulation，而不是只验证单一模型。
  - Consistency-Consensus 的意义在于不依赖真实环境执行，尝试把一致性变成测试时选择信号。
  - 作者明确指出低动态失败轨迹可能因背景坍塌而显得“高一致”。
* **为什么值得跟**:
  - WAM 若要用于规划，必须证明 imagined rollout 和动作因果链条相容。
  - 一致性指标可能成为无 value model 情况下的候选动作筛选工具。
  - 它为评估世界模型提供了比“视频看起来像不像”更机器人化的诊断维度。
* **风险 / 保留意见**:
  - 摘录中可见的提升幅度较 modest，是否具有统计和任务层面的强意义需核查。
  - 一致性可能被低动态或背景不变场景欺骗，作者自己也承认该失败模式。
* **建议先看**: 先看 action-state consistency 的定义和两个测试时策略，再看它在成功/失败轨迹上的分离度。重点判断该指标是在真实物理因果上有效，还是只捕捉了视觉变化幅度。
* **关键词**: `World Action Model` `action-state consistency` `test-time scaling` `imagined rollout` `dynamic compatibility`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - consistency score 是否能区分动作导致的状态变化与环境中无关视觉变化？
  - Consistency-Consensus 在不执行环境时依赖什么共识假设，何时会失效？
  - background collapse 失败模式是否可以通过任务动态性或视觉掩码缓解？
* **上传 PDF 后优先看**:
  - action-state consistency 定义与算法章节
  - RoboCasa 和 RoboTwin 2.0 对比实验
  - 失败模式、background collapse 和测试时开销分析

### [4]. Escaping the Diversity Trap in Robotic Manipulation via Anchor-Centric Adaptation [[HTML]](https://arxiv.org/html/2605.07381) [[PDF]](https://arxiv.org/pdf/2605.07381) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.07381`
* **Authors**: Yanzhe Chen, Kevin Yuchen Ma, Qi Lv, Yiqi Lin, Zechen Bai, Chen Gao, Mike Zheng Shou
* **Author Priority**: Standard
* **一句话结论**: 值得优先看：它把 VLA 适配中的“多样性越多越好”直觉反过来审视，问题意识很强。
* **问题与切口**: 这篇论文处理 VLA 落地到具体硬件时的少样本真实适配问题。作者提出 diversity trap：在有限演示预算下，盲目追求覆盖更多状态和任务，可能因为每个区域样本密度不足而带来不可消失的估计噪声。它的新意是把适配误差拆成 coverage 和 density 两类压力，并提出 Anchor-Centric Adaptation，让数据围绕关键 anchor 做更高密度巩固，而非平均撒到所有变化上。
* **核心方法与证据**: HTML 摘录只给出较少方法细节，但能确认论文形式化了 Coverage-Density Trade-off，并围绕 ACA 框架评估三个问题：是否缓解 diversity trap、是否跨 VLA backbone 泛化，以及 anchor 的数量、空间布局和 consolidation budget 对结果的敏感性。实验摘录还提到 boundary mining 与 residual adaptation 的单独和联合贡献会被评估。具体算法、任务和数值需 PDF 核查。
* **正文要点**:
  - 论文明确指出真实机器人 post-training 常受限于几十到几百条轨迹预算。
  - 核心假设是有限预算下 coverage 与 density 存在冲突，而不是简单最大化多样性。
  - 实验设计关注 anchor properties，包括数量、空间布局和巩固预算。
* **为什么值得跟**:
  - 这直接影响 VLA 真机微调的数据采集策略，具有很强实践价值。
  - 如果成立，少样本适配应从“覆盖尽量广”转向“关键区域采得足够密”。
  - 它为 embodiment gap 下的数据预算分配提供了可分析框架。
* **风险 / 保留意见**:
  - 当前摘录缺少 ACA 的完整算法细节和任务结果，主张强度需进一步验证。
  - anchor 选择若依赖人工经验或特定任务结构，泛化到开放任务可能受限。
* **建议先看**: 先看 Coverage-Density Trade-off 的形式化是否严谨，再看 boundary mining 和 residual adaptation 如何实际选 anchor、用数据。实验部分要重点看不同预算下策略是否稳定优于 diverse sampling。
* **关键词**: `VLA adaptation` `diversity trap` `anchor-centric adaptation` `coverage-density trade-off` `real-robot finetuning`
* **证据来源**: arXiv HTML (Introduction, Experiments)
* **读 PDF 先核查**:
  - anchor 是如何自动发现或选择的，是否需要任务先验或人工标注？
  - coverage 与 density 误差分解是否能预测真实实验中的性能变化？
  - ACA 在不同 VLA backbone 上的收益是否来自方法本身，还是来自特定数据分布？
* **上传 PDF 后优先看**:
  - Coverage-Density Trade-off 理论章节
  - ACA、boundary mining 与 residual adaptation 方法章节
  - 低预算适配实验和 anchor sensitivity ablation

### [5]. AT-VLA: Adaptive Tactile Injection for Enhanced Feedback Reaction in Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2605.07308) [[PDF]](https://arxiv.org/pdf/2605.07308) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.07308`
* **Authors**: Xiaoqi Li, Muhe Cai, Jiadong Xu, Juan Zhu, Hongwei Fan, Yan Shen, Guangrui Ren, Hao Dong
* **Author Priority**: Standard
* **一句话结论**: 优先读：AT-VLA 把触觉以较克制的方式接入 VLA，目标是解决接触丰富任务中的实时反应问题。
* **问题与切口**: AT-VLA 针对 VLA 在拉链、盖子、擦拭、盖章等接触丰富任务中的短板：视觉和语言足以表达目标，却难以及时感知接触状态、阻力和完成条件。论文的新意不是简单在下游微调时塞入触觉模态，而是提出 Adaptive Tactile Injection，在保留预训练视觉语言能力的同时动态融合触觉表示；同时用 Tactile Reaction Dual-Stream 区分慢速语义推理与快速触觉反应。
* **核心方法与证据**: 方法沿用类似 GO-1 的 VLA action modeling，并参考双系统策略：慢系统负责高层视觉语言推理，快系统承担低层触觉反应。实验硬件为 AgiBot Genie1 双 7-DoF 机械臂，配前视和腕部相机，夹爪带 Xense Robotics 触觉传感器。评估包括四个接触丰富任务和两个非接触任务，每个任务收集 30-50 条演示并做 15 次测试；具体成功率需 PDF 核查。
* **正文要点**:
  - 论文关注新模态微调可能破坏预训练 VLA 能力的问题，而不只是触觉是否有用。
  - 任务定义中 Unzip Bag、Stamp、Wipe Vase、Unscrew Lid 都要求根据接触反馈调整动作。
  - 实验设置同时包含非接触任务，用于观察触觉机制是否损害原有能力。
* **为什么值得跟**:
  - 接触丰富操作是视觉主导 VLA 的真实短板，触觉闭环很可能是必要补充。
  - 双流设计直接回应 VLA 推理慢、低层反应不够快的问题。
  - 少量演示下的触觉适配若有效，对工业和家庭细操作都有参考价值。
* **风险 / 保留意见**:
  - 硬件和触觉传感器较具体，迁移到其他夹爪或触觉阵列可能不直接。
  - 每任务 15 次测试规模不大，成功率差异的稳定性需要核查。
* **建议先看**: 先看 Adaptive Tactile Injection 如何避免破坏 VLA backbone，再看 Dual-Stream 的频率、接口和控制闭环。实验上要重点核查接触任务提升是否显著高于非接触任务变化。
* **关键词**: `tactile VLA` `contact-rich manipulation` `dual-stream control` `adaptive injection` `feedback reaction`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - Adaptive Tactile Injection 的门控或融合机制是否能解释何时该信任触觉、何时该保持视觉语言先验？
  - 快触觉流与慢 VLA 推理流之间如何同步，是否存在动作冲突或延迟累积？
  - 非接触任务结果是否证明新增触觉模块没有造成灾难性干扰？
* **上传 PDF 后优先看**:
  - Adaptive Tactile Injection 结构章节
  - Tactile Reaction Dual-Stream 控制接口章节
  - 接触丰富任务实验、非接触任务对照和 ablation

### [6]. Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2602.01166) [[PDF]](https://arxiv.org/pdf/2602.01166) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2602.01166`
* **Authors**: Shuanghao Bai, Jing Lyu, Wanqi Zhou, Zhe Li, Dakai Wang, Lei Xing, Xiaoguang Zhao, Pengwei Wang, Zhongyuan Wang, Cheng Chi, Badong Chen, Shanghang Zhang
* **Author Priority**: Standard
* **一句话结论**: 优先读：LaRA-VLA 是今天最典型的“把 CoT 变成 latent reasoning”VLA 路线，目标明确且贴近效率问题。
* **问题与切口**: LaRA-VLA 试图解决 VLA 中显式 Chain-of-Thought 推理的两个问题：生成长文本推理带来推理开销，离散语言推理也与连续感知和控制存在表示错配。它的核心切口是把多模态 CoT 内化到连续 latent 表示中，在推理时不再显式生成长 CoT，而是用紧凑文本 CoT latent 与视觉 latent 支撑动作预测。相对直接 CoT prompting，它更像训练期蒸馏和控制期压缩。
* **核心方法与证据**: 正文摘录显示其流程包括结构化 CoT 数据构建、LaRA-VLA 架构和 curriculum-based training。数据侧采用 anchor-first, generate-later 自动标注：用 Qwen3-VL 从初始帧和任务指令抽取语义 anchor，并从轨迹中分割 temporal anchor，以补足长程子任务、目标定位和动作级推理监督。实验覆盖 LIBERO、SimplerEnv 和真实长程操作，但具体结果数值需 PDF 核查。
* **正文要点**:
  - 论文把文本 CoT、视觉 grounding 和动作预测统一到 latent 空间，而不是保留显式推理输出。
  - 自动标注管线强调 semantic anchor 与 temporal anchor，减少冗余或不完整监督。
  - 实验问题覆盖仿真 SOTA 对比、真实长程任务和 latent reasoning 组件有效性。
* **为什么值得跟**:
  - 它回应了 reasoning-augmented VLA 的关键工程瓶颈：推理时间与控制频率。
  - latent CoT 若有效，可能在保留推理收益的同时避免显式文本生成成本。
  - 该方向连接 VLA、CoT distillation 和连续控制表示，后续可与 WAM 或视频规划结合。
* **风险 / 保留意见**:
  - latent reasoning 的可解释性弱于显式 CoT，错误诊断可能更困难。
  - 自动生成 CoT 标注依赖 Qwen3-VL 与轨迹分割质量，可能引入系统性偏差。
* **建议先看**: 先看课程训练如何把显式 CoT 迁移到 latent，再看 ablation 是否能分离文本 latent、视觉 latent 和普通 VLA backbone 的贡献。真实长程任务部分要核查效率收益是否与成功率同时成立。
* **关键词**: `Latent Reasoning VLA` `chain-of-thought` `latent representation` `curriculum training` `long-horizon manipulation`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - latent CoT 在训练后是否真正替代显式 CoT，还是只作为额外容量提升？
  - semantic anchor 和 temporal anchor 的自动标注错误会如何影响动作学习？
  - 推理效率提升是否在真实机器人闭环频率上体现，而不只是减少文本 token 输出？
* **上传 PDF 后优先看**:
  - 结构化 CoT 数据构建与 anchor 标注章节
  - latent reasoning 架构和 curriculum training 章节
  - LIBERO/SimplerEnv、真实长程任务和 ablation 实验

## Watchlist

### [W1]. BioProVLA-Agent: An Affordable, Protocol-Driven, Vision-Enhanced VLA-Enabled Embodied Multi-Agent System with Closed-Loop-Capable Reasoning for Biological Laboratory Manipulation [[VIP]] [[HTML]](https://arxiv.org/html/2605.07306) [[PDF]](https://arxiv.org/pdf/2605.07306)
* **Paper ID**: `2605.07306`
* **Authors**: Zhaohui Du, Zhe Wang, Hongmei Fei, Xiwen Cao, Ting Xiao, Qi Wang, Huanbo Jin, Jiaming Gu, Quan Lu, Zhe Liu
* **Author Priority**: Core VIP
* **为什么还值得留意**: BioProVLA-Agent 进入 shortlist 是因为它把实验协议理解、VLM-RAG 状态验证和 VLA 执行放进湿实验室机器人闭环，应用场景很具体。没有进入最终精选，主要是摘录更像系统集成框架，实验段落可见部分偏相关工作叙述，缺少足够清晰的定量证据和与今日 VLA/WAM 主线的直接方法突破。后续若 PDF 显示真实 wet-lab 多步骤成功率、失败恢复和低成本硬件复现细节扎实，可以升级关注。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. NoiseGate: Learning Per-Latent Timestep Schedules as Information Gating in World Action Models [[HTML]](https://arxiv.org/html/2605.07794) [[PDF]](https://arxiv.org/pdf/2605.07794)
* **Paper ID**: `2605.07794`
* **Authors**: Wen Huang, Haoran Sun, Yongjian Guo, Yunxuan Ma, Haoran Li, Jing Long, Zhouying Mo, Zhong Guan, Yucheng Guo, Shuai Di, Junwu Xiong
* **Author Priority**: Standard
* **为什么还值得留意**: NoiseGate 值得放入 watchlist，因为它把 WAM 中每个 latent frame 的 timestep schedule 解释为可学习信息门控，并用任务 reward 优化，切中 joint video-action denoising 的细粒度控制问题。它没有进入最终精选，是因为相较动态一致性诊断论文，它更偏特定 WAM/MoT 训练策略，且证据主要围绕 RoboTwin 与特定 Wan/Action-Expert substrate。上传 PDF 后应重点看 GRPO 优化是否稳定、是否依赖特定 backbone。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. Learning Visual Feature-Based World Models via Residual Latent Action [[HTML]](https://arxiv.org/html/2605.07079) [[PDF]](https://arxiv.org/pdf/2605.07079)
* **Paper ID**: `2605.07079`
* **Authors**: Xinyu Zhang, Zhengtong Xu, Yutian Tao, Yeping Wang, Yu She, Abdeslam Boularias
* **Author Priority**: Standard
* **为什么还值得留意**: RLA-WM 进入 shortlist 是因为 visual feature-based world model 是今天 world model 方向的重要分支，它试图用 DINO feature residual 上的 latent action 避免像素视频生成的高成本与幻觉。没有进入最终精选，是因为其主线更偏 feature dynamics 与离线视觉 RL，和 VLA 部署/动作推理的直接关系略弱。仍应跟踪它能否把 BC 扩展成 WAM，以及在 RLA-WM 内做 visual RL 的可复现性。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts [[HTML]](https://arxiv.org/html/2605.06175) [[PDF]](https://arxiv.org/pdf/2605.06175)
* **Paper ID**: `2605.06175`
* **Authors**: Yuhua Jiang, Junjie Lu, Xinyao Qin, Xiaoyu Chen, Kaixin Wang, Feifei Gao, Li Zhao
* **Author Priority**: Standard
* **为什么还值得留意**: VLA-GSE 值得观察，因为 PEFT 如何适配 VLM 到 VLA 是真实部署中的基础问题，它提出 generalized expert 与 routed specialized experts 的分解，并结合 SVD 初始化和梯度尺度平衡。没有进入最终精选，是因为它更像参数高效微调技术论文，方法新意集中在 adapter/expert 设计，而不是 VLA 行为建模或 world/action reasoning 本身。后续重点看它相对 LoRA、FFT 和 OpenVLA-OFT 式配置的稳定收益。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
