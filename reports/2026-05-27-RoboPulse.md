# RoboPulse | 2026-05-27

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 59 papers scanned · 10 shortlisted · 6 editor's picks

今天主线很清楚：VLA 正在从“会完成任务”转向“可被细粒度指令控制、可持续学习、可调用外部能力、可被长期记忆支撑”。最终精选覆盖了 steerable VLA 数据监督、记忆 benchmark、真实世界 continual learning、VLM-as-reward 的在线 RL、Sim2Real 全流程，以及具身工具协议，基本对应 VLA 落地前最关键的六个系统短板。Sim2Real 与 RL 方向里，HyperSim 和 SOLE-R1 值得优先看，因为它们不是只改策略结构，而是在数据、奖励、训练闭环和部署链路上重构系统。显式作者名单中，Chelsea Finn 出现在 RoboMME，应优先跟踪；FineVLA 和 ETP 在上下文中标为 core tier，但摘录作者名与给定核心作者名单未直接重合，需后续用 PDF/元数据核查。

## 今日信号

- VLA 的下一阶段竞争点正在从通用任务成功率转向过程可控性，包括执行臂、接触区域、方向、历史记忆和工具调用。
- 真实机器人部署问题被重新表述为数据生命周期问题：合成数据、少量真实数据、回放缓存、持续更新和部署反馈都在进入同一训练闭环。
- World model 与 reward model 的边界正在变软，视频语言推理、进度预测、物理先验和动作可控预测都在成为机器人学习的监督来源。

## Historical Rediscovery

- **Paper**: Afford-VLA: Action-Aligned Visual Planning via Internalized Affordance [[HTML]](https://arxiv.org/html/2605.24203) [[PDF]](https://arxiv.org/pdf/2605.24203)
  - **Paper ID**: `2605.24203`
  - **来源日期**: 2026-05-26
  - **当时可能被低估的信号**: 当时被 OASIS 的“中间表示对齐”主题盖过，但候选记录里已经出现了 Qwen3-VL-4B-Instruct、GR00T-style flow-matching action head、双 RealSense 真实机器人设置这些工程落地信号。
  - **为什么现在值得再看**: 现在值得再看，因为 action-aligned affordance 很可能是连接 VLA 高层语义、低层动作策略和 WAM 接口的一条实用路线，尤其适合对照真实部署中的中间表示是否真正可执行。
  - **建议动作**: 加入精读
  - **关键词**: `VLA` `affordance` `action-aligned planning` `real robot` `World Action Model`
- **Paper**: Contrastive Conceptor Activation Steering (COAST): Unlocking Vision-Language-Action Models through Hidden States [[HTML]](https://arxiv.org/html/2605.17144) [[PDF]](https://arxiv.org/pdf/2605.17144)
  - **Paper ID**: `2605.17144`
  - **来源日期**: 2026-05-19
  - **当时可能被低估的信号**: 当时它被归为 inference-time steering / 表示干预方法，优先级低于系统和 benchmark；但“success/failure rollouts + frozen VLA hidden states”本身就是很强的部署适应信号。
  - **为什么现在值得再看**: 现在值得再看，因为如果跨任务 failure geometry 可靠，它可能提供一种不重训或少重训 VLA 的失败恢复机制，适合和 RL fine-tuning、test-time adaptation、真实机器人评测放在一起比较。
  - **建议动作**: 加入精读
  - **关键词**: `VLA` `failure rollouts` `activation steering` `test-time adaptation` `RL+VLA`
- **Paper**: BlockVLA: Accelerating Autoregressive VLA via Block Diffusion Finetuning [[HTML]](https://arxiv.org/html/2605.13382) [[PDF]](https://arxiv.org/pdf/2605.13382)
  - **Paper ID**: `2605.13382`
  - **来源日期**: 2026-05-14
  - **当时可能被低估的信号**: 当时它被认为偏 architecture acceleration，但候选记录中的“长时程误差累积”和“速度-成功率权衡”其实是 VLA 真实落地的核心瓶颈。
  - **为什么现在值得再看**: 现在值得再看，因为实时 VLA、长时程操作和 action chunking / diffusion action head 的取舍正在变得关键；它可以作为评估 VLA 推理结构是否适合部署的参照。
  - **建议动作**: 快速浏览
  - **关键词**: `VLA` `block diffusion` `long-horizon control` `inference latency` `action blocks`
- **Paper**: Robotic Strawberry Harvesting with Robust Vision and Deep Reinforcement Learning based Sim-to-Real Control [[HTML]](https://arxiv.org/html/2605.23863) [[PDF]](https://arxiv.org/pdf/2605.23863)
  - **Paper ID**: `2605.23863`
  - **来源日期**: 2026-05-25
  - **当时可能被低估的信号**: 当时因不属于通用 VLA / world model 主线被降级，但“仿真训练 + PPO + 真实执行”的完整工程闭环是评估 Sim2Real 论文可用性的强信号。
  - **为什么现在值得再看**: 现在值得再看，因为它能补足 VLA/WAM 论文常缺的真实部署视角：失败率、闭环延迟、鲁棒性和仿真到真实控制接口，适合作为 Sim2Real grounding case。
  - **建议动作**: 快速浏览
  - **关键词**: `Sim2Real` `reinforcement learning` `PPO` `real robot` `deployment`
- **Paper**: Learning Action Manifold with Multi-view Latent Priors for Robotic Manipulation [[HTML]](https://arxiv.org/html/2605.11832) [[PDF]](https://arxiv.org/pdf/2605.11832)
  - **Paper ID**: `2605.11832`
  - **来源日期**: 2026-05-13
  - **当时可能被低估的信号**: 当时因模块较多、已有相近空间-动作耦合路线而未精选；但候选记录显示它覆盖 LIBERO、LIBERO-Plus、RoboTwin 2.0 和真实设置，实验面宽度是被低估的信号。
  - **为什么现在值得再看**: 现在值得再看，因为 3D-aware VLA、动作流形和真实操控评测都与你的 VLA/WAM 主线相关，可用来判断空间表征是否真正改善 action policy。
  - **建议动作**: 继续跟踪
  - **关键词**: `VLA` `action manifold` `multi-view perception` `3D manipulation` `real setting`

## Editor's Picks

### [1]. FineVLA: Fine-Grained Instruction Alignment for Steerable Vision-Language-Action Policies [[VIP]] [[HTML]](https://arxiv.org/html/2605.27284) [[PDF]](https://arxiv.org/pdf/2605.27284) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.27284`
* **Authors**: Xintong Hu, Xuhong Huang, Jinyu Zhang, Yutong Yao, Yuchong Sun, Qiuyue Wang, Mingsheng Li, Sicheng Xie, Yitao Liu, Junhao Chen, Yixuan Chen, Yingming Zheng, Shuai Bai, Tao Yu
* **Author Priority**: Core VIP
* **一句话结论**: 优先看：FineVLA 把 VLA 的“听懂目标”推进到“听懂执行方式”，对可控机器人策略和数据标注体系都很关键。
* **关键词**: `VLA` `fine-grained instruction` `steerable policy` `robot data annotation` `RoboFine-VLM`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

这篇论文瞄准 VLA 数据中长期被低估的问题：多数机器人轨迹只配有粗粒度目标语言，比如“把物体放到某处”，却没有说明用哪只手、从哪个方向接近、抓哪里、如何旋转、最终姿态是什么。对真实机器人来说，这些细节常常决定安全性、可复现性和用户可控性。现有 VLA 即使能完成任务，也可能把人类指令中关于执行过程的约束忽略掉，因此很难用于需要精细交互、双臂协调或接触敏感操作的场景。FineVLA 的价值在于把 steerability 明确定义成 action-instruction alignment 问题，而不是只做更大模型或更多任务数据。

#### ⚙️ 核心方法

摘录显示，FineVLA 包含数据构建、过程级标注、benchmark、可扩展标注器和策略训练几部分。FineVLA-Tool 首先把 10 个开源机器人数据集中的 972,247 条轨迹统一到可处理格式，解决异构 action/state 表示、同任务示范冗余和原始语言过粗三个问题；随后通过聚类和人工验证筛出 47,159 条代表性轨迹，并为它们补充细粒度、action-aligned 的过程监督。论文还训练 RoboFine-VLM，使其在同一标注 schema 下为新轨迹生成细粒度描述，并构建 RoboFine-Bench 评估机器人视频理解。最后，FineVLA-Policy 通过控制 FG:Raw instruction mixture，研究细粒度语言与原始任务语言混合时对 VLA 策略可控性的影响。当前摘录只能确认框架级流程和部分结果，具体标注维度定义、策略架构细节和训练损失需要看 PDF。

#### 📊 实验与结果

HTML 明确给出的实验线索包括：FineVLA-Data 来自 10 个开源数据集，起点规模为 972,247 条轨迹，最终形成 47,159 条人工验证、过程级监督轨迹；RoboFine-VLM 在 held-out RoboFine-Bench 上达到 71.0% VQA accuracy 和 83.6% captioning score；FineVLA-Policy 在受控 FG:Raw 指令混合设置下评估，结论指向细粒度指令能提升策略的 steerability。摘录没有完整表格，也没有给出所有任务成功率、baseline 名称和消融曲线，因此不能进一步声称其在所有 VLA benchmark 上全面领先。证据强项在数据规模和标注体系，策略收益仍需核查具体实验。

#### ⚠️ 风险 / 保留意见

- 细粒度标注质量高度依赖人工验证和 schema 设计，跨机器人平台迁移可能出现语义不一致。
- RoboFine-VLM 作为可扩展标注器可能放大训练集偏差，需要看失败案例和人工一致性。
- 策略改进是否来自细粒度语言本身，还是来自更干净的轨迹筛选，需要重点核查消融。

#### 💭 结论与启发

这篇最值得借鉴的是把 VLA 数据从“任务标签”升级为“执行约束标签”。后续如果做可控 VLA 或复现实验，不应只收集更多演示，而要设计能落到 action token、接触点和运动方向的语言 schema。系统设计上，可以把 FineVLA 看作数据层基础设施：先统一轨迹，再压缩冗余，再补过程级语义，最后用 VLM 扩展标注。读 PDF 时重点判断它的标注维度是否足够通用，以及策略实验是否真的证明了 steerability，而不只是提升了视频问答或 caption 指标。

#### 🔎 读 PDF 先核查

- FineVLA 的十个细粒度维度是否覆盖了双臂、接触、路径、旋转和最终状态等真实部署中最常见的可控变量？
- FG:Raw instruction mixture 的最佳比例如何变化，是否存在细粒度语言过多反而损害泛化的情况？
- RoboFine-VLM 自动扩展标注时，错误标注会如何影响 FineVLA-Policy 的执行可控性？

#### 📌 上传 PDF 后优先看

- 数据构建与标注 schema 章节
- FineVLA-Policy 的 FG:Raw 混合实验与消融
- RoboFine-Bench 的视频理解指标、失败案例和人工验证流程

### [2]. RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies [[VIP]] [[HTML]](https://arxiv.org/html/2603.04639) [[PDF]](https://arxiv.org/pdf/2603.04639) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.04639`
* **Authors**: Yinpei Dai, Hongze Fu, Jayjun Lee, Yuejiang Liu, Haoran Zhang, Jianing Yang, Chelsea Finn, Nima Fazeli, Joyce Chai
* **Author Priority**: Core VIP
* **一句话结论**: 优先看：RoboMME 是 VLA 长时程记忆能力的系统 benchmark，且有 Chelsea Finn 参与，适合作为后续 memory-VLA 选题入口。
* **关键词**: `robot memory` `VLA benchmark` `non-Markovian manipulation` `Chelsea Finn` `history-dependent policy`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

机器人长期任务经常不是 Markov 的：当前画面看起来相同，但历史不同，正确动作就不同。例如擦桌子要记住擦了几遍，搬动物体后要记住原位置，被遮挡物体要靠过去观察恢复状态。现有 VLA 逐渐加入记忆机制，但评测往往局限在单一任务或非标准设置，难以判断 symbolic memory、perceptual memory、recurrent state 等路线到底各自适合什么场景。RoboMME 的动机是给 long-horizon、history-dependent manipulation 一个统一评测框架，让记忆不再只是模型内部实现细节，而成为可比较、可诊断的能力维度。

#### ⚙️ 核心方法

论文构建 RoboMME benchmark，并把任务设计锚定到认知记忆分类：temporal、spatial、object、procedural 四类。摘录强调所有任务都被刻意设计成非 Markovian，即相同当前观测可能对应不同历史和不同动作，从而迫使模型利用过去信息。方法部分还给出 MME-VLA 模型族：共享基础 VLA backbone，输入包括语言 token 和当前多视角 RGB image token；架构参考 pi0/pi05 风格的 multi-expert transformer，由 VLM expert 融合语言视觉，由 action expert 在 denoising timestep 条件下预测动作。不同记忆表示和不同 integration mechanism 被放入同一框架对比，包括符号、感知、循环等记忆形态。当前摘录能确认 benchmark 结构、四类记忆维度和模型比较框架，但不能完整确认每种 memory module 的实现细节、训练配方和全部任务列表。

#### 📊 实验与结果

实验目标是评估历史依赖操作中的记忆行为。摘录说明 RoboMME 包含 16 个 manipulation 任务，覆盖四个认知维度，并通过 MME-VLA suite 控制比较不同记忆表示和整合机制。关键结论是没有单一设计在所有场景中稳定占优：symbolic、perceptual、recurrent memory 各有适用边界，这一点对模型选择比单一平均分更重要。HTML 没有提供完整数值表、各模型成功率或每类任务的排名，因此这里不能引用具体提升幅度。证据边界在于：我们目前能相信它提出了系统化 benchmark 和比较框架，但需要 PDF 验证 benchmark 规模、任务难度和统计稳定性。

#### ⚠️ 风险 / 保留意见

- benchmark 是否覆盖真实家务操作中的长时程遮挡、物体状态变化和人机交互仍需核查。
- 共享 backbone 下的对比更公平，但也可能限制某些记忆机制的最佳实现。
- 如果任务过度人工构造，模型在 RoboMME 上的记忆能力可能不等同于真实部署能力。

#### 💭 结论与启发

RoboMME 提醒后续读 VLA 论文时不能只看单步视觉 grounding 或任务成功率，而要问模型是否知道自己刚刚做过什么、看过什么、改变过什么。对系统设计而言，记忆不应只有一种默认实现：计数和步骤历史可能适合 symbolic memory，遮挡和空间恢复可能更需要 perceptual memory，技能阶段切换可能依赖 recurrent state。复现时最有价值的是先跑一个小型非 Markov 任务集，观察错误是否来自遗忘、错误检索还是记忆注入方式不对。

#### 🔎 读 PDF 先核查

- 四类记忆任务中，哪一类最能区分 symbolic、perceptual 和 recurrent memory 的优势？
- MME-VLA 的 memory integration mechanism 是在 VLM expert、action expert，还是跨 block attention 层面注入历史？
- RoboMME 的任务是否存在仅靠短期视觉线索或数据偏置绕过记忆需求的可能？

#### 📌 上传 PDF 后优先看

- RoboMME 任务定义与四类记忆维度
- MME-VLA 架构和不同 memory representation 的实现
- 各记忆机制对比、消融和失败案例分析

### [3]. Can VLA Models Learn from Real-World Data Continually without Forgetting? [[HTML]](https://arxiv.org/html/2605.26820) [[PDF]](https://arxiv.org/pdf/2605.26820) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.26820`
* **Authors**: Jiarun Zhu, Yijun Hong, Xiaoquan Sun, Zetian Xu, Mingqi Yuan, Zhiyong Wang, Wenjun Zeng, Jiayu Chen
* **Author Priority**: Standard
* **一句话结论**: 优先看：这篇把 VLA continual learning 拉到真实机器人数据上，直接回答部署后持续学新技能会不会遗忘。
* **关键词**: `continual learning` `VLA` `catastrophic forgetting` `replay buffer` `real-world robot data`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

#### 📖 背景与动机

VLA 模型如果要进入真实环境，不能只在一次性训练后冻结；机器人会不断遇到新物体、新场景和新任务，需要从新增数据中继续学习。但持续微调很容易造成 catastrophic forgetting：新任务学会了，旧技能被覆盖。以往 continual learning 研究多在模拟或窄任务环境中验证，对真实世界 VLA 部署的约束不足，比如全量重训成本太高、真实数据收集昂贵、回放预算有限、动作分布不同。本文的重要性在于把问题从“VLA 能否泛化”推进到“VLA 能否长期维护技能库”，这对机器人产品化比单次 benchmark 成绩更接近核心瓶颈。

#### ⚙️ 核心方法

摘录显示，论文构建了真实世界 VLA continual learning dataset，并系统研究 replay-based 方法在部署约束下的表现。基本问题设定是顺序接收多个真实机器人任务数据，模型需要学习新任务同时保留旧任务能力；naive sequential fine-tuning 作为直接微调基线，用来暴露遗忘程度。论文重点比较回放预算、回放频率和 action normalization 等低层实现因素，因为这些因素在真实 VLA adaptation 中可能比复杂算法更决定结果。结论指出，在配置得当时，小规模 replay budget 能几乎消除 catastrophic forgetting，并且 well-configured sequential learning pipeline 可超过 joint multi-task training。当前摘录只能确认 replay 是核心手段、动作归一化和频率是关键变量，但不能确认具体模型 backbone、任务数量、回放采样策略和优化超参。

#### 📊 实验与结果

HTML 给出了清晰的遗忘证据：naive Sequential FT 在前三个任务上从 single-task baseline 的 100.0、97.5、100.0 分别跌到 15.0、25.0、13.3；排除最后训练、尚未被遗忘的任务后，平均分降到 17.8，而 single-task baseline 为 99.2。摘录还说明遗忘并不均匀，deformable folding task 遗忘最严重，并且某些视觉共享属性会引发跨任务物体混淆，例如“green”同时出现在按钮和目标碗中。结论部分称 modest replay budget 在正确 replay frequency 和 action normalization 下几乎消除遗忘，但完整数值、任务名和方法表需 PDF 核查。

#### ⚠️ 风险 / 保留意见

- 结果可能对任务顺序、任务相似度和视觉属性冲突高度敏感。
- 回放缓存虽小，但真实机器人长期部署中仍涉及数据选择、隐私和存储策略。
- 如果 backbone 或动作空间换成其他 VLA，action normalization 的最优配置可能不稳定。

#### 💭 结论与启发

这篇的启发是，VLA 部署不是一次训练问题，而是持续维护问题。后续做机器人系统时，应把 replay buffer、任务顺序记录、动作归一化和回归测试集作为基础设施，而不是论文后期补丁。它也提醒我们：catastrophic forgetting 不只是抽象分数下降，还会表现为颜色、物体和任务语义的具体混淆。读 PDF 时应重点找可复现的 replay 配方，因为这类低层细节往往比新算法名更能决定真实机器人是否能稳定更新。

#### 🔎 读 PDF 先核查

- modest replay budget 的具体规模是多少，它如何随任务数增长而变化？
- action normalization 为什么会显著影响 continual VLA，是动作幅值、任务分布还是优化稳定性的原因？
- well-configured sequential learning 超过 joint training 的结论是否在不同任务顺序下仍成立？

#### 📌 上传 PDF 后优先看

- 真实世界 continual learning dataset 和任务顺序设置
- replay frequency、budget、action normalization 消融
- 遗忘机制的定性案例和 joint training 对比

### [4]. SOLE-R1: Video-Language Reasoning as the Sole Reward for On-Robot Reinforcement Learning [[HTML]](https://arxiv.org/html/2603.28730) [[PDF]](https://arxiv.org/pdf/2603.28730) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.28730`
* **Authors**: Philip Schroeder, Thomas Weng, Karl Schmeckpeper, Eric Rosen, Stephen Hart, Ondrej Biza
* **Author Priority**: Standard
* **一句话结论**: 优先看：SOLE-R1 把视频语言推理模型直接用作在线 RL 的唯一 dense reward，是 VLA+RL 方向非常有野心的系统尝试。
* **关键词**: `VLA+RL` `video-language reward` `online reinforcement learning` `progress prediction` `reward hacking`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

用 VLM 或 LLM 给机器人 RL 提供奖励一直很诱人，因为它可能减少人工 reward engineering，让机器人只凭自然语言目标和视觉观察学习新技能。但问题是，通用 VLM 在 partial observability、分布偏移和机器人视角下容易出错，RL 又会主动利用这些错误，形成 reward hacking。论文动机正是解决“foundation model 可以评价任务，但不够可靠到能做唯一奖励”这个矛盾。SOLE-R1 不把 VLM 当离线打分器，而是训练一个面向视频轨迹、逐时刻推理和进度预测的 reward model，用于 on-robot online RL，因而非常贴近 VLA 策略适应新任务的需求。

#### ⚙️ 核心方法

SOLE-R1 输入原始视频观察和自然语言目标，输出 temporally grounded chain-of-thought reasoning，并在 <answer> 中给出 scalar progress value，作为在线 RL 的 dense reward。训练采用两阶段 hybrid recipe：第一阶段 SFT 使用 spatiotemporal reasoning data，让模型学习基于图像/视频、query、rationale、answer 的视频原生推理；第二阶段 RLVR 针对 progress prediction 继续优化，因为 SFT 中最终标量答案只占输出 token 的小部分，监督信号相对弱。摘录还说明训练数据来自 video trajectory and reasoning synthesis pipeline，并包含真实 non-expert trajectories，用来提升模型识别失败、部分完成和中间进度的能力。当前摘录能确认 CoT+progress 的接口和 SFT+RLVR 的训练逻辑，但不能确认 reward 标量范围、RL 算法细节、机器人控制接口和安全约束。

#### 📊 实验与结果

实验假设覆盖面很广：SOLE-R1 要在 zero-shot reward prediction 上超过更大的通用 reasoning model 和专用 reward model，要比 GPT-5、Gemini-3-Pro 更不易 reward hacking，要验证 CoT 和 authentic non-expert trajectories 的贡献，还要展示任务多样性驱动的 scaling law，并能 steer 强预训练 VLA 策略学习新任务。HTML 明确给出训练数据规模为 1.2M spatiotemporal CoT traces，来自 41K videos。摘录没有给出成功率、相关系数或 reward hacking 的具体数值，因此只能保守认为其提供了较完整的实验路线，具体说服力取决于 PDF 中在线机器人实验和对照设置。

#### ⚠️ 风险 / 保留意见

- CoT reward model 可能产生看似合理但视觉 grounding 错误的解释，RL 仍可能利用残余偏差。
- 使用通用模型名称作为对比很强，但需要核查调用设置、提示词和评估公平性。
- 在线 RL 依赖唯一 learned reward，真实机器人安全边界和异常处理必须单独验证。

#### 💭 结论与启发

SOLE-R1 对后续选题的价值在于把 VLM supervision 从“事后评估”推进到“训练中的进度信号”。如果成立，它会让 VLA 策略不只模仿数据，而能在自然语言目标下通过在线交互改善。复现时不应一开始追求完整 on-robot RL，而应先验证 progress prediction 与真实任务阶段的相关性，再测试是否会出现 reward hacking。系统设计上，SOLE-R1 更像一个可插拔的 world/action evaluator：它不直接生成动作，但决定哪些动作序列看起来在接近目标。

#### 🔎 读 PDF 先核查

- SOLE-R1 的 scalar progress value 如何标定，是否跨任务可比，还是只在单任务内部有效？
- RLVR 阶段具体使用哪些 verifiable signals 来训练进度预测，是否依赖合成标签质量？
- 在 steer 预训练 VLA 学新任务时，策略失败是来自 reward 误判、探索不足，还是 VLA action prior 限制？

#### 📌 上传 PDF 后优先看

- SFT+RLVR 训练配方和 progress reward 定义
- reward hacking 对比实验与失败案例
- 在线 RL 机器人任务、VLA steering 实验和安全约束

### [5]. HyperSim: A Holistic Sim-To-Real Framework For Robust Robotic Manipulation [[HTML]](https://arxiv.org/html/2605.26638) [[PDF]](https://arxiv.org/pdf/2605.26638) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.26638`
* **Authors**: Junyi Dong, Haotian Luo, Ziwei Xu, Shengwei Bian, Heng Zhang, Sitong Mao, Jingyi Guo, Yang Xu, Wenhao Chen, Qiuyu Feng, Yao Mu, Ping Luo, Shunbo Zhou, Xiaodong Wu
* **Author Priority**: Standard
* **一句话结论**: 优先看：HyperSim 是 Sim2Real 操作领域的全链路框架，强在把高保真仿真、对抗轨迹和少量真实数据合训练接起来。
* **关键词**: `Sim2Real` `robotic manipulation` `synthetic data` `adversarial trajectory` `co-training`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

机器人 foundation model 越大，对动作-观测序列数据的需求越高，但真实机器人数据昂贵、慢且难覆盖长尾情况。合成数据是自然方案，可 Sim2Real gap 会让仿真训练出的 manipulation policy 到真实世界失效，尤其在视觉外观、状态分布和动态扰动上差异明显。HyperSim 的动机不是单独提升渲染或做 domain randomization，而是提出从 synthetic data generation 到 policy training 再到 real deployment 的整体框架。它关注的是视觉操作里的零样本和少样本部署，这对当前 VLA/机器人策略从数据瓶颈走向可扩展训练很重要。

#### ⚙️ 核心方法

HyperSim 由三个核心支柱组成：high-fidelity environment synthesis、adversarial trajectory generation、sim-and-real co-training。高保真环境用于缓解视觉渲染差异，让合成观察更接近真实机器人相机；对抗轨迹生成通过扰动目标位置、姿态或状态分布扩展训练覆盖，迫使策略在动态扰动和边界情形下更稳健；sim-and-real co-training 则把少量人工真实演示与仿真数据结合，学习更 domain-invariant 的表征。摘录中的方法部分主要重复摘要级框架，实验部分透露了目标 2D 位置和方向会被扰动以生成 adversarial trajectories。当前摘录只能确认三模块设计和总体训练目标，不能确认具体渲染管线、策略网络、损失函数、合训练比例和部署校准细节。

#### 📊 实验与结果

实验在 Galaxea R1 humanoid robot 上进行，视觉输入来自头部和腕部 RGB 相机，频率为 10 Hz。任务是工业分拣式深箱操作：机器人要把目标物体如红色插头从中央深 bin 移到左右相邻 bin；相比平面抓取，深箱会带来更强运动学约束、碰撞风险和贴边 corner case。实验验证三个假设：完整 HyperSim 和消融变体能零样本真实部署，少量真实演示 co-training 能提升性能，对抗轨迹能增强动态扰动鲁棒性。摘要还提到包含 400 次 real-world evaluation。HTML 未给出具体成功率和表格，因此不能判断提升幅度，只能确认其实验强调真实部署和细粒度指标。

#### ⚠️ 风险 / 保留意见

- 当前证据集中在一个深箱分拣类任务，跨物体、跨场景和跨机器人泛化需核查。
- 高保真仿真构建成本可能较高，是否比直接采集真实数据更划算需要看工程细节。
- 对抗轨迹扰动范围若调得不当，可能训练出过保守或偏离真实分布的策略。

#### 💭 结论与启发

HyperSim 的启发是 Sim2Real 不应只靠单一技巧解决。真实部署差距至少有三层：视觉长相不像、训练状态覆盖不够、仿真和真实表征不一致。后续做操作数据扩展时，可以借鉴这种分层思路：先保证场景足够像，再主动生成困难轨迹，最后用少量真实数据把表征拉回真实域。读 PDF 时我会特别关注它的 ablation 是否能证明三根支柱各自必要，以及 400 次真实评估是否覆盖足够多的物体位姿和扰动类型。

#### 🔎 读 PDF 先核查

- 高保真环境 synthesis 具体解决了哪些视觉 gap，是材质、光照、相机位姿，还是几何接触？
- adversarial trajectory generation 的扰动策略是否来自任务失败分布，还是手工随机采样？
- sim-and-real co-training 中少量真实演示的规模和采样方式如何影响零样本与少样本部署表现？

#### 📌 上传 PDF 后优先看

- HyperSim 三模块架构和数据生成流程
- 零样本、少样本真实机器人实验及消融表
- 对抗轨迹扰动设置、动态干扰测试和失败案例

### [6]. Enabling Extensible Embodied Capabilities with Tools [[VIP]] [[HTML]](https://arxiv.org/html/2605.26637) [[PDF]](https://arxiv.org/pdf/2605.26637) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.26637`
* **Authors**: Xueyang Zhou, Zijia Wang, Qianjiang Li, Yibo Hu, Guiyao Tie, Li Wan, Yidan Liu, Pan Zhou, Lichao Sun, Yongchao Chen
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看：ETP 把 embodied capability 从单体 VLA 中外置成工具协议，适合跟踪长时程组合任务的系统化路线。
* **关键词**: `embodied tools` `VLA systems` `tool protocol` `EmbodiedToolBench` `capability externalization`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

很多具身智能方法把感知、推理、规划和控制都压进一个统一参数化策略里，典型代表包括 VLA 和分层视觉语言系统。但这些能力本质上异构：高层规划、几何感知、安全检查、低层控制的目标函数和可靠性要求不同。单体模型在标准 benchmark 上进步明显，却容易在长时程、组合式、安全关键任务上暴露结构性短板。本文的动机是把能力外置为可独立优化、可发现、可调用、可组合的工具，而不是继续要求一个模型内部学会所有东西。对 VLA 来说，这是一条与扩大模型规模互补的系统路线。

#### ⚙️ 核心方法

论文提出 Embodied Tool Protocol，即 ETP，用于 embodied tool 的 registration、discovery、invocation 和 execution，并整理 100+ validated tools，覆盖 perception、cognition、reasoning、execution 等能力。核心思想是 capability externalization：模型在推理时动态调用外部工具，把异构能力拆成独立模块，从而提升覆盖范围、模块复用、鲁棒性和多工具组合能力。论文还提出 EmbodiedToolBench，系统评估 tool-use competence，包括 tool-need recognition、tool selection、tool execution 和 tool-chain composition。摘录显示实验关注三个问题：工具增强是否提升 embodied performance，当前模型是否具备工具使用意识与组合能力，哪些任务更适合 tool offloading。当前摘录只能确认协议和 benchmark 设计方向，不能确认每个工具接口 schema、调度算法、失败恢复机制和安全隔离细节。

#### 📊 实验与结果

实验评估八个代表性开源和闭源模型，场景包括 EmbodiedBench 的 EB-ALFRED、EB-Habitat、EB-Navigation、EB-Manipulation，以及真实机器人平台。摘录称工具增强在 Table 1 中 consistent improves embodied performance，并且附录有部分多轮统计分析；但没有给出具体成功率、置信区间或每个模型的提升数值，因此不能引用定量幅度。实验问题还包括模型在工具需求识别、选择、执行、多工具组合上的熟练程度，以及哪些能力适合外置。结论指出 capability externalization 提升表现，但也揭示当前模型在工具使用上的不足。证据强项是覆盖面，边界是数值和真实机器人细节需 PDF 核查。

#### ⚠️ 风险 / 保留意见

- 工具协议增加系统复杂度，错误可能来自模型、工具、接口或执行环境，诊断链路更长。
- 100+ 工具的验证标准、可复现性和跨平台可用性需要重点审查。
- 工具调用在安全关键机器人任务中需要权限控制、失败回退和实时性保证。

#### 💭 结论与启发

ETP 的关键启发是，未来 VLA 未必靠一个 action head 解决所有问题，而可能变成 tool-using embodied agent：策略负责判断意图、上下文和调用时机，专用工具负责几何、导航、检测、规划或执行。对后续系统设计，这意味着要认真定义工具接口、状态传递、错误码和调用日志。复现时可以先做小型工具集，不追求 100+ 覆盖，而是验证 tool-need recognition 和 tool-chain composition 是否真正改善长时程任务。

#### 🔎 读 PDF 先核查

- ETP 的 tool schema 是否足够表达机器人执行中的输入状态、坐标系、约束和失败返回？
- 工具增强的收益主要来自感知工具、规划工具、控制工具，还是多工具组合？
- 闭源和开源模型在 tool-need recognition 与 tool-chain composition 上的差距是否稳定？

#### 📌 上传 PDF 后优先看

- ETP 协议定义、工具注册和调用接口
- EmbodiedToolBench 四类工具能力评估
- EmbodiedBench 与真实机器人平台上的工具增强消融

## Watchlist

### [W1]. ParkingWorld: End-to-End Autonomous Parking Reinforcement Learning from Corrective Experience in 3DGS Simulation [[HTML]](https://arxiv.org/html/2605.25029) [[PDF]](https://arxiv.org/pdf/2605.25029)
* **Paper ID**: `2605.25029`
* **Authors**: Zhengcheng Yu, Changze Li, Haoran Liu, Tong Qin
* **Author Priority**: Standard
* **为什么还值得留意**: ParkingWorld 进入 watchlist 是因为它把 3D Gaussian Splatting 仿真、纠错经验和端到端 autonomous parking RL 接在一起，属于 Sim2Real 与 corrective experience 的有趣交叉。它没有进入最终精选，主要是场景集中在自动泊车，和今天 VLA/通用操作/具身工具主线的贴合度弱于 HyperSim 与 SOLE-R1。摘录中的实验设置较具体，包括 5 个 3DGS 停车场景、239 个车位和每方法 200 次 trial，后续可作为 3DGS-based RL sim2real 的专项跟踪。
* **证据来源**: arXiv HTML (Introduction, Experiments)

### [W2]. ParkourFormer: Integrating Predictive Supervision and Sequence Modeling into Parkour Locomotion [[HTML]](https://arxiv.org/html/2605.25782) [[PDF]](https://arxiv.org/pdf/2605.25782)
* **Paper ID**: `2605.25782`
* **Authors**: Yanheng Mai, Wenhao Xu, Zirui Huang, Yifei Fu, Shengwei Dong, Xinjue Wang, Kailun Huang, Yanzhe Xie, Renjing Xu
* **Author Priority**: Standard
* **为什么还值得留意**: ParkourFormer 进入 watchlist 是因为它把 humanoid parkour 表述为 future-conditioned sequence modeling，并结合 RGB-D、历史 token、cross-attention、AMP-style motion state 和 PPO，契合 RL + 预测监督趋势。未进最终精选的原因是它更偏腿足运动控制和 humanoid locomotion，VLA/语言动作接口较弱。若后续关注 world action model 或未来状态预测对控制稳定性的作用，这篇值得补读。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. Modernising Reinforcement Learning-Based Navigation for Embodied Semantic Scene Graph Generation [[HTML]](https://arxiv.org/html/2603.25415) [[PDF]](https://arxiv.org/pdf/2603.25415)
* **Paper ID**: `2603.25415`
* **Authors**: Roman Küble, Marco Hüller, Mrunmai Phatak, Rainer Lienhart, Jörg Hähner
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇进入 watchlist 是因为它讨论语义场景图作为 embodied semantic world model，并用 PPO 更新基于 RL 的导航探索，和世界模型构建、主动感知有关。未进入精选是因为它的核心贡献更像 RL navigation/SSG 现代化，而不是 VLA、Sim2Real 或 action-conditioned world model 的主线突破。摘录里的重要信号是 PPO 相比 REINFORCE 带来稳定学习，而 imitation learning 和 depth input 对 REINFORCE 没有解决根本优化问题。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

### [W4]. Physically Native World Models: A Hamiltonian Perspective on Generative World Modeling [[HTML]](https://arxiv.org/html/2605.00412) [[PDF]](https://arxiv.org/pdf/2605.00412)
* **Paper ID**: `2605.00412`
* **Authors**: Sen Cui, Jingheng Ma
* **Author Priority**: Standard
* **为什么还值得留意**: Physically Native World Models 进入 watchlist 是因为它从 Hamiltonian 视角讨论 world model，正好对应今天关注的 World Model 和 physically reliable prediction。未进入最终精选，是因为摘录主要是概念性动机，缺少可确认的机器人实验、benchmark 数字或具体系统接口。它适合作为理论路线跟踪：后续若 PDF 提供 action-controllable、long-horizon stable prediction 的实证框架，再提高优先级。
* **证据来源**: arXiv HTML (Introduction)
