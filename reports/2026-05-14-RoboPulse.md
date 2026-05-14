# RoboPulse | 2026-05-14

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 93 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线非常集中：VLA 不再只是把视觉、语言和动作端到端接起来，而是在鲁棒性、长时程分解、动作表征、可纠错交互、跨 embodiment 标定和结构化 world model 上补齐部署短板。最终精选的 6 篇覆盖了从 RL fine-tuning、agent-tool 架构、latent action、interactive CoT、camera-frame action 到混合动力学 world model 的关键路径，基本对应“能不能稳、能不能长、能不能统一、能不能规划”。VIP 作者上，2511.17001 被标为 core tier，值得优先核查其跨机器人动作统一是否真的能支撑大规模预训练；watchlist 中 2605.13452 含 Donglin Wang，也应继续跟踪其双臂统一感知控制路线。整体看，今天更像是 VLA 系统工程化的一天：论文都在处理模型进入真实机器人前必须面对的接口、时延、数据和分布偏移问题。

## 今日信号

- VLA 的鲁棒性研究正在从“多做数据增强”转向显式区分哪些视觉变化应忽略、哪些变化必须改变动作。
- 长时程机器人任务的主流解法正在从单一端到端策略转向 VLM 负责规划与恢复、VLA 负责局部可调用技能的分层组合。
- 动作空间与动力学模型正在被重新结构化：camera-frame action、rotational latent action、MoE world model 都指向更物理一致的中间表示。

## Historical Rediscovery

- **Paper**: Retrieve-then-Steer: Online Success Memory for Test-Time Adaptation of Generative VLAs [[HTML]](https://arxiv.org/html/2605.10094) [[PDF]](https://arxiv.org/pdf/2605.10094)
  - **Paper ID**: `2605.10094`
  - **来源日期**: 2026-05-13
  - **当时可能被低估的信号**: online success memory 把测试期成功经验直接转成 generative VLA 的采样先验，这不是普通检索增强，而是部署期策略自适应信号。
  - **为什么现在值得再看**: 对 VLA 真实机器人反复执行同类任务、test-time adaptation、长期记忆与失败恢复都很关键，也可和 World Action Model 的部署期修正机制对照阅读。
  - **建议动作**: 加入精读
  - **关键词**: `VLA` `test-time adaptation` `success memory` `persistent deployment` `generative policy`
- **Paper**: Unified Noise Steering for Efficient Human-Guided VLA Adaptation [[HTML]](https://arxiv.org/html/2605.10821) [[PDF]](https://arxiv.org/pdf/2605.10821)
  - **Paper ID**: `2605.10821`
  - **来源日期**: 2026-05-12
  - **当时可能被低估的信号**: human corrective intervention、online RL 和 flow-matching VLA 的 noise-space finetuning 被统一到同一适配接口，说明它可能不是单点技巧，而是部署期纠错闭环。
  - **为什么现在值得再看**: 和你的 RL+VLA 兴趣高度重合，尤其适合检查 action-to-noise inversion、人类纠错成本、在线微调稳定性这些真实部署瓶颈。
  - **建议动作**: 加入精读
  - **关键词**: `RL+VLA` `human correction` `online RL` `flow matching` `noise steering`
- **Paper**: NoiseGate: Learning Per-Latent Timestep Schedules as Information Gating in World Action Models [[HTML]](https://arxiv.org/html/2605.07794) [[PDF]](https://arxiv.org/pdf/2605.07794)
  - **Paper ID**: `2605.07794`
  - **来源日期**: 2026-05-11
  - **当时可能被低估的信号**: 把每个 latent frame 的 timestep schedule 解释为可学习信息门控，并用任务 reward 优化，这暗示 WAM 的生成过程本身可以被任务目标重塑。
  - **为什么现在值得再看**: 如果今天关注 World Action Model 如何从视频-动作联合生成走向可控策略学习，这篇值得再看；重点应核查 GRPO 优化稳定性和对特定 backbone 的依赖。
  - **建议动作**: 加入精读
  - **关键词**: `World Action Model` `joint video-action denoising` `reward optimization` `latent schedule` `RoboTwin`
- **Paper**: SEVO: Semantic-Enhanced Virtual Observation for Robust VLA Manipulation via Active Illumination and Data-Centric Collection [[HTML]](https://arxiv.org/html/2605.11114) [[PDF]](https://arxiv.org/pdf/2605.11114)
  - **Paper ID**: `2605.11114`
  - **来源日期**: 2026-05-13
  - **当时可能被低估的信号**: observation-space 语义高亮直接针对背景、光照、视角变化导致的策略崩溃，并且历史记录提到真实机器人、100 trials per condition、ACT/SmolVLA 差异分析。
  - **为什么现在值得再看**: 对 Sim2Real 和低成本 VLA 部署很实用，尤其适合作为评估鲁棒视觉输入、主动照明和数据中心采集策略的案例。
  - **建议动作**: 快速浏览
  - **关键词**: `Sim2Real` `robust VLA` `active illumination` `semantic observation` `real robot evaluation`
- **Paper**: ELVIS: Ensemble-Calibrated Latent Imagination for Long-Horizon Visual MPC [[HTML]](https://arxiv.org/html/2605.04709) [[PDF]](https://arxiv.org/pdf/2605.04709)
  - **Paper ID**: `2605.04709`
  - **来源日期**: 2026-05-07
  - **当时可能被低估的信号**: 针对 long-horizon latent imagination 的不确定性和多模态未来建模，并明确出现 zero-shot sim-to-real 的真实任务线索。
  - **为什么现在值得再看**: 对 World Model、长时程操作和 Sim2Real 都有直接参考价值，可作为 VLA/WAM 之外的 model-based control 对照，帮助判断 latent imagination 何时能支撑真实闭环控制。
  - **建议动作**: 继续跟踪
  - **关键词**: `World Model` `visual MPC` `long-horizon planning` `Sim2Real` `model-based RL`

## Editor's Picks

### [1]. What to Ignore, What to React: Visually Robust RL Fine-Tuning of VLA Models [[HTML]](https://arxiv.org/html/2605.13105) [[PDF]](https://arxiv.org/pdf/2605.13105) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.13105`
* **Authors**: Yuanfang Peng, Jingjing Fu, Chuheng Zhang, Li Zhao, Jiang Bian, Mingyu Liu, Ling Zhang, Jun Zhang, Rui Wang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为它把 VLA 的 RL fine-tuning 从只追任务成功率推进到显式学习“该忽略什么视觉扰动、该响应什么视觉变化”。
* **关键词**: `VLA` `RL fine-tuning` `visual robustness` `PPO` `OOD generalization`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

#### 📖 背景与动机

这篇关注 VLA 部署时最常见也最棘手的问题：预训练和监督微调后的策略在仿真或训练集内能完成任务，但遇到灯光、桌面纹理、干扰物、相机位姿等视觉变化时会出现不稳定。普通 PPO 只用任务奖励优化成功与否，无法告诉模型某个视觉变化是无关噪声，还是目标状态改变后必须调整动作的关键信号。对机器人来说，这一区分非常重要：忽略目标无关纹理是鲁棒性，忽略目标位姿变化则是灾难。PAIR-VLA 的动机正是把这种 action-dependent visual shift 写进 RL fine-tuning 目标中，使 VLA 不只是“看得更多”，而是学会对视觉变化做行为层面的选择性响应。

#### ⚙️ 核心方法

PAIR-VLA 在 PPO 优化中加入两类基于成对视觉变体的辅助目标。第一类是不变性项，用来压低模型对任务无关视觉变化的动作差异，使同一任务在不同纹理、光照或干扰外观下保持相近行为。第二类是敏感性项，用来鼓励模型在任务相关变化出现时改变动作，例如目标位置或需要操作的对象状态发生变化。当前摘录只能确认它是在 PPO fine-tuning 阶段叠加这些辅助目标，并同时适配 autoregressive VLA 与 flow-matching VLA；更细的损失形式、配对样本构造细节和权重设置需要读 PDF 附录核查。方法上的新意在于，它没有把所有增强都视为 invariant augmentation，而是把视觉变化按动作后果分成“应该保持策略一致”和“应该改变策略输出”两类，这比单纯 reward learning 或 domain randomization 更贴近机器人控制问题。

#### 📊 实验与结果

实验在 ManiSkill3 中进行，重点是带视觉干扰的 pick-and-place 任务，问题设置包括 OOD 泛化、RL fine-tuning 效率、两个辅助目标的贡献，以及是否能推广到未用于构造配对视图的变化。摘录明确提到使用 OpenVLA 作为 autoregressive VLA，并使用一个 flow-matching VLA 作为另一类 backbone；两者都先得到 SFT checkpoint，再在相同 PPO 设置下比较标准 PPO 与 PAIR-VLA。结果表述为在 unseen table textures、target-pose shifts、increasing visual clutter、unseen lighting conditions 和 camera-pose experiment 上均有提升，但摘录没有给出具体成功率数字，因此只能保守认为其证据支持“多类视觉 shift 下优于 PPO”，不能引用幅度。

#### ⚠️ 风险 / 保留意见

- 配对视觉变体如何生成会强烈影响训练信号，若配对规则偏窄，真实部署中的扰动类型可能覆盖不足。
- 实验主要来自 ManiSkill3，真实机器人证据在摘录中不足，sim-to-real 可信度需要进一步核查。
- 辅助目标与 PPO reward 的权重可能敏感，复现时需要关注超参数和稳定性。

#### 💭 结论与启发

这篇对后续 VLA 研究的启发是：鲁棒性不应只看输入分布偏移，而要看偏移是否改变最优动作。做复现时，可以先把 paired visual variants 做成独立数据层，再把 invariance/sensitivity loss 插进现有 PPO 或 offline RL 流程。选题上，它适合延伸到真实相机外参变化、遮挡、动态 distractor，以及语言目标歧义场景，重点验证模型到底学会了动作条件不变性，还是只对特定增强过拟合。

#### 🔎 读 PDF 先核查

- PAIR-VLA 如何定义 task-irrelevant 与 task-relevant visual variants，配对构造是否需要人工标签或任务先验？
- 不变性项和敏感性项分别作用在动作 token、action distribution 还是隐藏表示上，对 PPO 稳定性有什么影响？
- 未见光照和相机位姿上的提升是否来自真正的策略鲁棒性，还是来自与训练扰动共享的低层视觉统计？

#### 📌 上传 PDF 后优先看

- 辅助目标定义与配对样本构造章节
- PPO 训练细节、loss 权重和超参数附录
- OOD 视觉扰动、消融实验与 camera-pose/generalization 结果表

### [2]. Towards Long-horizon Embodied Agents with Tool-Aligned Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2605.13119) [[PDF]](https://arxiv.org/pdf/2605.13119) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.13119`
* **Authors**: Zixing Lei, Changxing Liu, Yichen Xiong, Minhao Xiong, Yuanzhuo Ding, Zhipeng Zhang, Weixin Li, Siheng Chen
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为它把长时程 embodied VLA 从单模型闭环控制改成 VLM agent 调度多个 VLA 工具的系统架构。
* **关键词**: `VLA-as-tools` `long-horizon manipulation` `VLM agent` `tool alignment` `few-shot adaptation`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

#### 📖 背景与动机

当前 VLA 在局部操作上进步很快，但长时程任务同时要求场景理解、任务分解、进度追踪、失败恢复和多技能组合。让单个 VLA 端到端承担所有职责，会遇到两个压力：一是长闭环规划对模型推理和状态记忆要求高，二是不同物理操作的数据需求差异大，有限 embodied 数据难以覆盖。VLAs-as-Tools 的核心判断是，VLA 更适合作为可调用的局部动作执行器，而不是单独承担整个 agent。高层 VLM 负责全局时序推理和恢复，底层 VLA 工具负责 bounded subtask，这一划分更接近机器人系统的模块化实践，也更适合长任务中反复检查、重试和切换技能。

#### ⚙️ 核心方法

框架由一个高层 VLM agent 和一组 specialized VLA tools 组成。VLM agent 做 scene analysis、global planning、progress monitoring 和 recovery，并通过工具调用方式触发某个 VLA 执行局部子任务。论文进一步提出 Tool-Aligned Post-Training，用来让 VLA 工具更忠实地响应 agent invocation，即工具不只是会执行语言条件动作，还要和上层规划接口对齐。当前摘录只能确认该 post-training 目标是提高 invocation fidelity、specialize VLA tools，同时尽量不丢失 pretrained semantic capabilities；具体数据格式、调用模板、负例或 alignment loss 需要读正文。相比把 planning 全塞进 VLA，本文的新意是把 VLA 的能力边界显式系统化：VLM 处理长时程结构，VLA 处理短时程物理闭环，从而降低单模型必须同时学会规划、控制和恢复的难度。

#### 📊 实验与结果

实验围绕四个问题：VLAs-as-tools 是否提升长时程 embodied performance，Tool-Aligned Post-Training 是否提高执行对调用的忠实度，各组件贡献，以及 few-shot adaptation 的数据效率。摘录列出的 benchmark 包括 LIBERO-Long、RoboTwin 和 CALVIN，其中 RoboTwin 使用 Franka 单臂可执行的 8 个任务，CALVIN 使用 CALVIN_D 的 80%/20% train-test episode split。使用的 VLA backbone 包括 OpenVLA-OFT 和另一个摘录未完整显示的模型，并在需要时加入 OpenVLA 监督适配基线。结论称在 LIBERO-Long 上对任务成功、instruction alignment、few-shot adaptation 和 robustness 有显著改善，但没有提供具体数值，需避免夸大幅度。

#### ⚠️ 风险 / 保留意见

- 系统效果依赖高层 VLM 的规划可靠性，错误分解可能让底层 VLA 工具执行得越忠实越偏离目标。
- 工具边界和 invocation schema 若需要人工设计，扩展到开放任务时维护成本可能较高。
- 摘录中缺少真实机器人实验细节，长时程仿真结果到真实部署仍需验证。

#### 💭 结论与启发

这篇适合作为“VLA agent 化”的系统设计参考。后续读论文应重点看工具调用接口是否足够通用，以及 Tool-Aligned Post-Training 是否能作为一种标准 post-training recipe 复用到不同 VLA。复现上，可以先在 LIBERO-Long 这类有子任务结构的 benchmark 上实现高层 planner + VLA executor，再逐步加入失败检测和 recovery。研究延伸可关注自动发现工具边界、从 demonstrations 中学习 invocation，以及把工具执行置信度反馈给 VLM planner。

#### 🔎 读 PDF 先核查

- Tool-Aligned Post-Training 的训练样本如何构造，是否需要把长任务自动切成可调用子任务？
- 高层 VLM 如何判断 VLA tool 执行成功、失败或需要 recovery，是否依赖环境状态标签？
- 工具专门化会不会降低单个 VLA 的泛化能力，论文是否有跨任务或跨 benchmark 的负迁移分析？

#### 📌 上传 PDF 后优先看

- VLAs-as-Tools 系统架构与工具调用接口章节
- Tool-Aligned Post-Training 数据构造和目标函数章节
- LIBERO-Long、RoboTwin、CALVIN 的消融和 few-shot adaptation 表

### [3]. RotVLA: Rotational Latent Action for Vision-Language-Action Model [[HTML]](https://arxiv.org/html/2605.13403) [[PDF]](https://arxiv.org/pdf/2605.13403) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.13403`
* **Authors**: Qiwei Li, Xicheng Gong, Xinghang Li, Peiyan Li, Quanyun Zhou, Hangjun Ye, Jiahuan Zhou, Yadong Mu
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为它试图用连续 rotational latent action 取代离散量化 LAM，为跨 embodiment VLA 预训练提供更有物理结构的动作中间空间。
* **关键词**: `latent action model` `rotational representation` `flow matching` `cross-embodiment` `VLA pretraining`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

Latent Action Model 是处理异构机器人数据和人类视频的重要方向，因为不同平台的关节、末端执行器和动作标注往往不兼容，需要一个统一的 latent action space 来做 VLA 预训练。现有 LAM 常用 encode-decode 加 VQ-VAE 式离散量化，把动作变成适合 next-token prediction 的离散 token，但这带来三个隐患：latent 容量被量化限制，表示可能退化成重构目标帧的捷径，而且缺少与真实运动几何对应的结构。RotVLA 的核心动机是把 latent action 建成连续旋转结构，使其具备连续性、可组合性和物理意义，从而更适合表达真实动作动态。

#### ⚙️ 核心方法

RotVLA 分成 LAM 与 VLA 两层。LAM 端使用冻结 DINOv2 提取帧级视觉特征，再经时空 transformer 编码，并用 transformer decoder 支撑 latent action 学习；摘录明确给出 latent action dimension 为 16。其关键变化是把 latent action 建模为连续 rotational representation，而不是离散 token，并引入 triplet frame learning 来约束时间动态、避免表示坍缩。VLA 端以 InternVL3.5-1B 初始化 backbone，接一个 24-layer Diffusion Transformer action expert，用 flow-matching 方式生成动作。微调时机器人动作使用 absolute end-effector pose，包括 xyz position 和 Rotate6D orientation，这与 rotational latent action 的设计相匹配。当前摘录只能确认这些模块和训练轮廓，无法确认 rotation group 的精确定义、triplet loss 公式和人类视频对齐细节。

#### 📊 实验与结果

摘录提供了较具体的实现信息：LAM 和 RotVLA 都预训练 200k steps，batch size 为 256；下游 finetuning batch size 为 128；完整模型约 1.7B 参数，其中 vision encoder 304M、language model 752M、action head 305M、latent action model 290M。实验声称使用大规模跨 embodiment 机器人数据和人类视频预训练，并通过下游机器人任务验证可迁移运动动态。结论强调 RotVLA 能缓解 representation collapse、学习 meaningful and transferable motion dynamics，但摘录没有给出 benchmark 名称、成功率或对比数字，因此目前只能把它视作动作表示路线的强候选，不能判断其相对 UniVLA 或离散 LAM 的实际收益幅度。

#### ⚠️ 风险 / 保留意见

- 连续 rotational latent action 的优化可能比离散 token 更难，训练稳定性和超参数敏感性需要核查。
- 摘录缺少 benchmark 和定量结果，当前无法确认收益是否来自表示本身还是更大的模型/数据。
- 将人类视频动作映射到机器人可执行动作时，latent 的物理可解释性可能仍存在语义落差。

#### 💭 结论与启发

这篇的价值在于提醒我们：VLA 的动作空间不一定必须迎合语言模型的离散 token 范式，物理结构可能比 token 兼容性更重要。后续如果做跨 embodiment 预训练，可以把 RotVLA 与 camera-frame action、TCP pose、Rotate6D 等几何规范结合起来看。复现时不宜一开始追完整 1.7B 系统，可先验证 triplet frame LAM 是否真的比 VQ latent 更少坍缩，并测试 latent composition 是否对应可解释的运动组合。

#### 🔎 读 PDF 先核查

- Rotational latent action 的数学空间和维度 16 如何对应，是否能直接组合或插值出稳定运动？
- Triplet frame learning 如何避免 LAM 只编码目标帧外观，论文是否有 collapse 诊断或 latent 可视化？
- RotVLA 的收益在控制模型、预训练数据和动作表示之间如何拆分，是否有公平消融？

#### 📌 上传 PDF 后优先看

- rotational latent action 定义和 triplet frame learning 章节
- LAM 与 VLA action expert 的训练流程和数据混合细节
- 下游任务对比、latent 可视化和表示坍缩消融

### [4]. Guide, Think, Act: Interactive Embodied Reasoning in Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2605.13632) [[PDF]](https://arxiv.org/pdf/2605.13632) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.13632`
* **Authors**: Yiran Ling, Qing Lian, Jinghang Li, Qing Jiang, Tianming Zhang, Xiaoke Jiang, Chuanxiu Liu, Jie Liu, Lei Zhang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为它把 VLA 从被动 sense-to-act 策略推进到可由人类视觉提示纠偏的 interactive embodied reasoning。
* **关键词**: `interactive VLA` `visual guidance` `embodied CoT` `OOD robustness` `failure recovery`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

#### 📖 背景与动机

多数 VLA 把图像、语言和动作紧耦合为直接 Sense-to-Act 映射，在训练分布内表现可以很强，但一旦遇到杂乱、光照变化、未见物体或语言指令歧义，就缺少透明的中间接口。即使 embodied CoT 能显示一些推理过程，也未必能让用户直接重新 grounding 机器人注意力或提供空间纠正。GTA-VLA 的动机是把人类视觉提示引入 VLA 推理链路，让用户用 affordance point、box、trace 等稀疏空间先验纠正策略。这对真实机器人很关键，因为部署时完全自治往往不现实，一个自然、低成本的视觉指导接口能显著提高失败恢复和空间歧义处理能力。

#### ⚙️ 核心方法

GTA-VLA 的框架名为 Guide, Think, Act，核心是 spatially steerable embodied reasoning。它允许用户提供显式视觉 cues，将这些稀疏空间 priors 直接条件化到统一的 spatial-visual Chain-of-Thought 中，再由模型产生动作。与普通 VLA 相比，它不是从观测和语言直接到动作，而是在“Guide”阶段引入人类或外部空间提示，在“Think”阶段形成可受提示影响的空间视觉推理，再在“Act”阶段执行。当前摘录只能确认支持的提示形式包括 affordance points、boxes 和 traces，并声称其能用于 failure recovery 与 spatial ambiguity；具体 prompt 表示、视觉 cue 编码、CoT supervision 来源以及动作头结构需要读正文。方法新意主要在于把可纠错性做成 VLA 的一等接口，而不是事后通过重新描述语言指令或重启任务来修正。

#### 📊 实验与结果

实验从三个轴评估：标准 benchmark 表现、OOD robustness，以及显式视觉指导在空间歧义下的效果。标准 benchmark 包括 LIBERO 和 SimplerEnv；OOD 泛化使用作者提出的 SimplerEnv-Plus，扰动覆盖 visual、robot、language 和 object-centric factors；此外还研究 sparse visual guidance 是否能在语言不足时解决歧义。结论称该方法在仿真和真实世界中都表现出强 autonomous performance，并在 OOD shift 和 spatial ambiguity 下改善 failure recovery。但摘录没有给出真实机器人任务、次数和成功率细节，也没有具体 benchmark 数字，因此应把实验解读为“覆盖面较广的证据框架”，定量可信度需查表确认。

#### ⚠️ 风险 / 保留意见

- 依赖用户或外部模块提供高质量视觉 cue，真实使用中提示错误可能误导策略。
- 视觉 CoT 的可解释性不等于因果可靠性，需要确认中间推理是否真正影响动作。
- SimperEnv-Plus 是作者自建 OOD benchmark，扰动设计是否公平需要核查。

#### 💭 结论与启发

这篇适合启发“人机协同 VLA”方向：与其追求完全自动的黑箱泛化，不如给系统一个低带宽但高语义密度的纠错通道。后续系统设计可以把视觉提示来源扩展为人类点击、检测器输出、语言解析出的区域，或失败后自动生成的 affordance proposal。读 PDF 时应重点看视觉 cue 如何进入模型，以及在没有 cue、有错误 cue、cue 稀疏时性能如何变化，这决定它是实用交互接口还是仅在精心设置下有效。

#### 🔎 读 PDF 先核查

- GTA-VLA 如何编码 point、box、trace 等视觉 cue，它们是在图像 token、prompt token 还是动作条件中融合？
- spatial-visual CoT 的监督来自人工标注、自动生成还是模型自蒸馏，是否会引入推理幻觉？
- 在错误或偏移的人类 guidance 下，模型是否有拒绝、降权或恢复机制？

#### 📌 上传 PDF 后优先看

- Guide-Think-Act 架构和视觉 cue 编码章节
- SimplerEnv-Plus 扰动定义与 OOD 评估协议
- 视觉指导消融、错误提示鲁棒性和真实机器人实验

### [5]. Unify Robot Actions in Camera Frame [[VIP]] [[HTML]](https://arxiv.org/html/2511.17001) [[PDF]](https://arxiv.org/pdf/2511.17001) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2511.17001`
* **Authors**: Sicheng Xie, Lingchen Meng, Zijie Diao, Haidong Cao, Zhiying Du, Shuyuan Tu, Jiaqi Leng, Qiuyue Wang, Mingsheng Li, Shuai Bai, Zuxuan Wu, Yu-Gang Jiang
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，因为它把跨 embodiment 动作统一落到 camera-frame TCP action 和可规模化外参估计上，是 VLA 数据工程的底层问题。
* **关键词**: `camera-frame action` `cross-embodiment` `camera calibration` `TCP action` `VLA data`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

跨机器人学习的关键瓶颈之一是动作语义不统一。关节角在不同机器人间维度和含义不一致，末端位姿依赖 robot base frame 且常记录 flange 而非更贴近抓取的 TCP，delta action 又受局部坐标约定影响。很多现有方法绕开问题：要么给不同 embodiment 设专用 action head，要么学习 latent action space，但并没有从几何层面解决动作含义错位。本文提出把动作统一到 camera frame，利用相机外参把不同平台的 TCP action 转成具有一致几何语义的表示。这对 VLA 和 Sim2Real 都很重要，因为视觉输入通常以相机为中心，若动作也在相机系中表达，跨数据集预训练和视觉-动作对齐会更自然。

#### ⚙️ 核心方法

论文提出 CalibAll，用于从离线机器人数据集中估计 camera extrinsics，并将异构动作转换为 camera-frame TCP actions。流程包含 preprocessing、camera extrinsic estimation 和 postprocessing 三阶段，目标是获得 robot base frame 到 camera frame 的刚体变换。它强调只需要现有数据集中常见的两类信息：RGB video sequences 和 joint angles at each timestamp，因此适合补标那些原本缺少外参注释的大规模离线数据。完成标定后，作者构建 Camera-Frame Action Dataset，将不同机器人平台的动作语义标准化。方法上的关键点是把“统一动作空间”从模型内部 latent 表示转成显式几何标定问题，且声称 training-free、robot-independent。当前摘录能确认总体管线和输入输出，但具体外参优化、TCP 恢复、异常处理和多相机场景细节需要继续核查。

#### 📊 实验与结果

标定实验在 DREAM 数据集上评估，该数据集包含约 57K 张 Franka Panda 真实图像。对比方法包括 DREAM 变体、RoboPose、CtRNet 和 CtRNet-X，指标为 ADD 和 AUC。摘录给出明确数字：CalibAll 达到 AUC 97.642、ADD 0.008 m；最佳先前方法 CtRNet-X 为 AUC 86.231、ADD 0.014 m，CalibAll 的 AUC 提升超过 11 点。结论还称其应用到 16 个数据集、4 个机器人平台，并显示 camera-frame action pretraining 改善下游表现。这里标定证据较强，但下游 VLA 预训练的具体任务、收益幅度和对照设置在摘录中不足，需要看完整实验表。

#### ⚠️ 风险 / 保留意见

- 方法依赖 RGB 视频和关节角质量，遮挡严重、同步不准或关节标定误差会影响外参估计。
- camera-frame action 对固定相机设置友好，但多相机、移动相机或眼在手相机下的统一策略需核查。
- 下游提升可能同时来自数据清洗和动作规范化，需看消融确认 camera frame 本身贡献。

#### 💭 结论与启发

这篇应作为跨 embodiment VLA 数据管线的重点阅读。相比直接设计更复杂的 action head，先把历史数据的坐标语义对齐可能是更高杠杆的工作。对后续系统设计的启发是：数据集发布时应把 camera extrinsics、TCP 定义、base frame、action convention 作为一等元数据；若要复用 Open X-Embodiment 类数据，也应先评估动作坐标的一致性。复现优先从 CalibAll 标定质量开始，再验证 camera-frame action 是否提升不同机器人混合训练。

#### 🔎 读 PDF 先核查

- CalibAll 的外参估计如何仅依赖 RGB 和 joint angles，是否需要已知机器人 CAD、kinematic chain 或分割先验？
- camera-frame TCP action 在单臂和双臂机器人中如何定义左右臂语义，是否存在动作冲突或尺度差异？
- 下游 pretraining 改善是否在相同数据量、相同模型和相同训练步数下与 base-frame action 公平比较？

#### 📌 上传 PDF 后优先看

- CalibAll 外参估计核心算法和输入假设章节
- Camera-Frame Action Dataset 构建、平台覆盖和后处理细节
- DREAM 标定表、下游预训练消融和跨 embodiment transfer 实验

### [6]. Prismatic World Model: Learning Compositional Dynamics for Planning in Hybrid Systems [[HTML]](https://arxiv.org/html/2512.08411) [[PDF]](https://arxiv.org/pdf/2512.08411) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2512.08411`
* **Authors**: Mingwei Li, Xiaoyuan Zhang, Chengwei Yang, Zilong Zheng, Yaodong Yang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为它把 world model 的失败点明确指向混合接触动力学过平滑，并用结构化 MoE 建模物理模式切换。
* **关键词**: `world model` `model-based RL` `hybrid dynamics` `Mixture-of-Experts` `planning`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

机器人中的 model-based RL 和 planning 很依赖 world model 的长时程预测质量，但真实物理常是 hybrid system：连续运动会被接触、碰撞、滑动、粘滞、腾空和支撑等离散事件打断。单一 monolithic latent dynamics model 往往倾向学习全局连续的平均动力学，在模式边界处把不连续变化过平滑。对 planner 来说，这种平滑会在 lookahead 中积累误差，尤其在接触丰富的操作和腿式运动中让搜索结果失真。PRISM-WM 的动机是把 world model 结构化为可组合动态 primitive，使模型显式或隐式地区分物理模式，而不是用一个网络硬拟合所有状态转移。

#### ⚙️ 核心方法

PRISM-WM 使用 context-aware Mixture-of-Experts 架构：gating mechanism 根据当前上下文隐式识别物理模式，不同 expert 负责专门的动力学区域。摘录还说明它通过 latent orthogonalization 迫使专家学习互斥的 dynamics，从而避免普通 MoE 中多个 expert 学到相似平均解。模型可替换现有 target paradigm 中的 monolithic dynamics 和 reward models，作者在保持 TD-MPC2 和 PWM 超参数一致的前提下，仅替换为 MoE-based architecture。方法的核心新意不只是加 MoE，而是把专家分化与混合动力学的 contact mode 对齐，希望 gating 能呈现可解释的 mode-switching。当前摘录中专家数量处显示缺失，公式和正交化具体实现也未给出，因此只能确认结构思想，不能补充细节。

#### 📊 实验与结果

实验覆盖 model-based planning、direct policy learning 和 zero-shot sim-to-sim transfer，环境来自多个 simulator：DMControl 的标准 locomotion、Humanoid-Bench 的 whole-body control，以及 DiffRL 的高维 contact-rich 任务。作者称为保持一致，保留 TD-MPC2 和 PWM 的超参数，只替换 dynamics/reward model 结构，并进行 planning horizon、expert cardinality、inference efficiency 等消融，同时用可视化解释 gating 的模式切换行为。结论称 PRISM-WM 优于 vanilla MoE baselines，并通过 latent orthogonalization 获得更清晰的专家专门化。但摘录未提供任何具体分数、任务列表或成功率，因此目前应关注方法假设和实验覆盖，而非定量强弱。

#### ⚠️ 风险 / 保留意见

- MoE gating 的物理模式解释可能是事后相关，不一定严格对应真实接触状态。
- 专家数量、正交化强度和 planner horizon 可能高度耦合，迁移到新任务需要调参。
- 摘录缺少真实机器人或视觉输入证据，目前更偏连续控制和仿真 world model。

#### 💭 结论与启发

这篇对 world model 方向的启发是：机器人动力学建模不能只追求更大 latent model，还要匹配物理系统的分段和模式切换结构。若后续做 VLA + world model，可以考虑让高层语言/视觉状态预测与低层 contact-mode dynamics 分开建模。复现时应先在接触边界清晰的低维环境验证 MoE 专家是否真的专门化，再看长 horizon planning 是否减少 compounding error。对论文阅读来说，最关键是区分 PRISM-WM 相对普通 MoE 的收益到底来自正交化、gating 设计，还是更多参数。

#### 🔎 读 PDF 先核查

- latent orthogonalization 如何定义，是否直接作用于 expert hidden states、latent transitions 还是预测残差？
- gating mechanism 的模式切换是否与真实接触事件对齐，论文是否有定量或可视化证据？
- 在保持 TD-MPC2/PWM 超参数不变时，PRISM-WM 的计算开销和 inference efficiency 是否适合在线 planning？

#### 📌 上传 PDF 后优先看

- PRISM-WM MoE 架构、gating 和 latent orthogonalization 章节
- DMControl、Humanoid-Bench、DiffRL 的主结果和 planning horizon 消融
- expert cardinality、inference efficiency 与 mode-switching 可视化

## Watchlist

### [W1]. BlockVLA: Accelerating Autoregressive VLA via Block Diffusion Finetuning [[HTML]](https://arxiv.org/html/2605.13382) [[PDF]](https://arxiv.org/pdf/2605.13382)
* **Paper ID**: `2605.13382`
* **Authors**: Ruiheng Wang, Shuanghao Bai, Haoran Zhang, Badong Chen, Xiangyu Xu
* **Author Priority**: Standard
* **为什么还值得留意**: BlockVLA 进入 shortlist 是因为它瞄准 autoregressive VLA 的推理时延和长时程误差累积，用 block diffusion 在 action block 内并行去噪、block 间保留自回归依赖。它没有进入最终精选，主要因为今天已有多篇更直接处理鲁棒性、长时程系统和动作统一的论文；同时该文更偏 inference/training architecture acceleration，需要等 PDF 核查 LIBERO 与 SimplerEnv 上的速度-成功率权衡。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. FrameSkip: Learning from Fewer but More Informative Frames in VLA Training [[HTML]](https://arxiv.org/html/2605.13757) [[PDF]](https://arxiv.org/pdf/2605.13757)
* **Paper ID**: `2605.13757`
* **Authors**: Bin Yu, Shijie Lian, Xiaopeng Lin, Zhaolong Shen, Yuliang Wei, Changti Wu, Hang Yuan, Haishan Liu, Bailing Wang, Cong Huang, Kai Chen
* **Author Priority**: Standard
* **为什么还值得留意**: FrameSkip 的价值在于从数据层挑战“每帧 demonstration 都同等有用”的默认假设，通过 action variation、visual-action coherence、task-progress priors 和 gripper-transition preservation 选择更有信息的帧。它暂列 watchlist 而非精选，是因为摘录中的方法较像训练数据 pruning recipe，重要但突破性取决于不同 benchmark、retention ratio 和模型规模下是否稳定成立。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. Realtime-VLA FLASH: Speculative Inference Framework for Diffusion-based VLAs [[HTML]](https://arxiv.org/html/2605.13778) [[PDF]](https://arxiv.org/pdf/2605.13778)
* **Paper ID**: `2605.13778`
* **Authors**: Jiahui Niu, Kefan Gu, Yucheng Zhao, Shengwen Liang, Tiancai Wang, Xing Hu, Ying Wang, Huawei Li
* **Author Priority**: Standard
* **为什么还值得留意**: Realtime-VLA FLASH 值得跟踪，因为它把 diffusion-based VLA 的部署瓶颈具体落到 replanning latency，并用 draft model、parallel verification 和 phase-aware fallback 减少 full inference。摘录给出 58.0 ms full inference 与最快 7.8 ms speculative round 的对比，工程信号很强；未进精选是因为它更偏实时推理加速框架，且仍依赖 heuristic thresholds，需进一步看失败模式和真实任务可靠性。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. CUBic: Coordinated Unified Bimanual Perception and Control Framework [[VIP]] [[HTML]](https://arxiv.org/html/2605.13452) [[PDF]](https://arxiv.org/pdf/2605.13452)
* **Paper ID**: `2605.13452`
* **Authors**: Xingyu Wang, Pengxiang Ding, Jingkai Xu, Donglin Wang, Zhaoxin Fan
* **Author Priority**: Core VIP
* **为什么还值得留意**: CUBic 因为含 core 关注作者 Donglin Wang 且处理双臂 coordinated perception/control，必须进入 watchlist。它没有进入最终精选，是因为今天 VLA 主线更偏通用模型、动作统一和 world model，而 CUBic 更专注 bimanual visuomotor policy；后续应重点核查其 shared tokenized representation 是否真的统一了独立感知与跨臂协调，而不是 benchmark 特化。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
