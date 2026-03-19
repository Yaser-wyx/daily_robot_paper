今天这批里，真正贴近你主线的高价值工作主要集中在三条线上：VLA 的动作语义细化、world model 向可执行闭环推进，以及围绕泛化/持续学习的基础问题重估。直接打中 Sim2Real 的顶级候选不多，因此本期筛选更偏向 VLA 与 world model 交叉，而不是传统导航、SLAM 或纯控制。优先作者名单里，Cewu Lu 和 Dorsa Sadigh 各有一篇值得跟进，但更偏“问题定义与泛化诊断”，适合用来校准研究判断。

### [1]. World-Env: Leveraging World Model as a Virtual Environment for VLA Post-Training（ID: 2509.24948）
* **Title**: World-Env: Leveraging World Model as a Virtual Environment for VLA Post-Training
* **摘要介绍**: 这篇工作直指 VLA 在示范稀缺场景下的瓶颈：模仿学习高度依赖大规模演示，而真实机器人环境又往往不可随意重置，导致基于 RL 的后训练难以真正落地。摘要显示，作者尝试把 world model 直接作为 VLA 的虚拟交互环境，用于承载策略后训练与能力补偿，把高风险、低重复性的真实试错转移到可控生成环境中。其核心吸引力不在于再加数据，而在于给 VLA 提供一个可反复试验的闭环优化载体。
* **为什么值得看**:
  - 直接把 `VLA`、`RL` 和 `world model` 接成了一个后训练闭环。
  - 抓住了“真实环境不可重置”这一机器人后训练痛点。
  - 对高风险场景中的安全试错流程有现实意义。
* **潜在风险/局限**:
  - 效果会高度依赖 world model 对任务相关动力学的保真度。
  - 摘要没有说明生成环境与真实机器人之间的偏差如何被校正。
* **关键词**: `VLA` `World Model` `RL Post-Training`

### [2]. EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards（ID: 2603.17808）
* **Title**: EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards
* **摘要介绍**: 这篇论文关注“视频世界模型能看不能用”的核心痛点：生成的未来帧即便视觉连贯，也可能不满足机器人刚体与运动学约束，最终无法转成可执行动作。摘要显示，作者引入逆动力学模型奖励，对齐视频 world model 与真实动作可执行性，把视觉预测质量和控制有效性绑定起来。这比单纯追求画面逼真更贴近机器人闭环控制需求，也让世界模型从“会想象”更进一步走向“能落地执行”。
* **为什么值得看**:
  - 直击视频 world model 与可执行动作脱节的问题。
  - 用 IDM reward 连接生成质量与控制有效性，思路很硬。
  - 对 planning-as-generation 或 model-based control 都有启发。
* **潜在风险/局限**:
  - 若逆动力学模型不准，奖励信号本身可能带偏对齐方向。
  - 提升可执行性可能会牺牲长时视觉一致性或生成多样性。
* **关键词**: `Video World Model` `Inverse Dynamics` `Executable Actions`

### [3]. KineVLA: Towards Kinematics-Aware Vision-Language-Action Models with Bi-Level Action Decomposition（ID: 2603.17524）
* **Title**: KineVLA: Towards Kinematics-Aware Vision-Language-Action Models with Bi-Level Action Decomposition
* **摘要介绍**: 该工作把现有 VLA 常见的“粗粒度指令”问题进一步扒开：很多操控任务目标相同，但执行过程在方向、轨迹、姿态和相对位移上存在细粒度差异，现有语言动作接口往往表达不够。摘要显示，作者提出一个更强调运动学属性的 VLA 任务设定，并设计双层动作分解来承载“目标不变、执行多样”的控制需求。尤其对于个性化操控、精细轨迹约束和人机可控性研究，这是一条很值得跟进的路线。
* **为什么值得看**:
  - 它把 VLA 从任务级指令推进到细粒度运动学语言。
  - 双层动作分解很适合处理同目标、多执行风格的场景。
  - 对精细操控和可控执行风格都有直接价值。
* **潜在风险/局限**:
  - 更丰富的运动学指令和标注可能显著抬高数据成本。
  - 跨任务、跨本体泛化能力在摘要里还看不清楚。
* **关键词**: `VLA` `Kinematics` `Action Decomposition`

### [4]. Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning（ID: 2603.03818）
* **Title**: Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning
* **摘要介绍**: 这篇论文讨论一个非常关键但常被忽略的问题：大规模预训练 VLA 在持续学习新技能时，是否会像传统行为克隆策略那样严重遗忘旧能力。摘要给出的核心结论相当直接：预训练 VLA 对灾难性遗忘的抵抗力可能比预想更强，这意味着“先大规模预训练、再逐步增量扩展技能库”也许比从头做 continual robot learning 更可行。这对长期技能库维护和低成本增量训练都有现实意义。
* **为什么值得看**:
  - 如果结论成立，会改写大家对 robot continual learning 的预期。
  - 直接比较预训练 VLA 与传统 BC 的遗忘行为，很有信息量。
  - 对构建长期扩展的机器人技能库非常关键。
* **潜在风险/局限**:
  - 摘要没给出适用范围，可能依赖特定任务与预训练规模。
  - 抗遗忘不等于前向迁移强，也不等于新增技能学习高效。
* **关键词**: `Continual Learning` `VLA` `Catastrophic Forgetting`

### [5]. Mimic Intent, Not Just Trajectories（ID: 2602.08602）
* **Title**: Mimic Intent, Not Just Trajectories
* **摘要介绍**: 这篇来自 Cewu Lu 团队的工作对当前端到端模仿学习提出了一个有分量的质疑：不少方法，包括 VLA 在内，之所以难以适应环境变化和技能迁移，可能是因为它们只在模仿轨迹表面，而没有显式抓住行为意图。摘要显示，作者尝试在端到端 IL 中把“意图”与“执行细节”解耦，让策略学到更稳定的任务本质。它本质上在问：模型学到的是动作表面，还是任务背后的因果与目的。
* **为什么值得看**:
  - 对“模仿轨迹就能泛化”这一默认假设提出了正面挑战。
  - 意图/执行解耦很契合 skill transfer 与 robust manipulation。
  - 来自优先作者名单，且问题定义本身值得持续跟踪。
* **潜在风险/局限**:
  - “意图”如何表征与监督，落地上可能并不简单。
  - 若任务本身含糊，解耦效果可能受数据偏置影响很大。
* **关键词**: `Imitation Learning` `Intent Modeling` `Skill Transfer`

### [6]. Grounding Robot Generalization in Training Data via Retrieval-Augmented VLMs（ID: 2603.11426）
* **Title**: Grounding Robot Generalization in Training Data via Retrieval-Augmented VLMs
* **摘要介绍**: 这篇由 Dorsa Sadigh 等人提出的工作不直接追求再做一个更强策略，而是追问一个更基础的问题：机器人所谓“泛化”到底是在泛化什么。摘要显示，作者提出 RADAR 框架，用 retrieval-augmented VLM 直接把测试任务与训练数据做对应比较，以判断评测究竟要求插值、组合泛化还是更远分布外能力。对当前很多只看平均成功率的操控论文，这种先量化“泛化距离”再讨论性能的视角很有价值。
* **为什么值得看**:
  - 不再只报成功率，而是试图量化泛化到底离训练分布多远。
  - retrieval-augmented VLM 为评测解释性提供了可操作工具。
  - 对设计 benchmark 和读懂泛化结果都很有帮助。
* **潜在风险/局限**:
  - 它更像分析框架，而不是直接提升控制性能的方法。
  - 判断质量可能强烈依赖检索库覆盖度和表示能力。
* **关键词**: `Robot Generalization` `Retrieval-Augmented VLM` `Evaluation`

# 🧭 ChatGPT Follow-up Pack

### 💡 World-Env: Leveraging World Model as a Virtual Environment for VLA Post-Training [[PDF]](https://arxiv.org/pdf/2509.24948) [[ChatGPT]](https://chatgpt.com/)
> **适合何时点开**: 如果你需要确认方法细节、实验数字、公式推导或复现难度，打开 ChatGPT 后上传 PDF，再粘贴下面的 prompt。

* **Authors**: Junjin Xiao, Yandan Yang, Xinyuan Chang, Ronghan Chen, Feng Xiong, Mu Xu, Wei-Shi Zheng, Qing Zhang
* **Abstract Link**: https://arxiv.org/abs/2509.24948

```text
你是我的机器人学研究搭档。请先检查我是否已经上传这篇论文的 PDF。

如果我还没有上传 PDF，请先提醒我上传 PDF，再暂停，不要猜测全文细节。

论文基础信息：
- Title: World-Env: Leveraging World Model as a Virtual Environment for VLA Post-Training
- Authors: Junjin Xiao, Yandan Yang, Xinyuan Chang, Ronghan Chen, Feng Xiong, Mu Xu, Wei-Shi Zheng, Qing Zhang
- arXiv Abstract URL: https://arxiv.org/abs/2509.24948
- Research Interests: VLA (Vision-Language-Action), Sim2Real, RL+VLA, World Model
- Abstract: Vision-Language-Action (VLA) models trained via imitation learning suffer from significant performance degradation in data-scarce scenarios due to their reliance on large-scale demonstration datasets. Although reinforcement learning (RL)-based post-training has proven effective in addressing data scarcity, its application to VLA models is hindered by the non-resettable nature of real-world environments. This limitation is particularly critical in high-risk domains such as industrial automation, where interactions often induce state changes that are costly or infeasible to revert. Furthermore, existing VLA approaches lack a reliable mechanism for detecting task completion, leading to redundant actions that reduce overall task success rates. To address these challenges, we propose RehearseVLA:, an RL-based post-training framework that replaces physical interaction with a low-cost world model-based virtual simulator. RehearseVLA: consists of two key components: (1) a physically-consistent world simulator that generates temporally consistent future visual observations, and (2) a vision-language model (VLM)-guided instant reflector that provides continuous reward signals and predicts action termination. This simulated environment enables VLA models to safely explore and generalize beyond their initial imitation learning distribution. Our method achieves notable performance gains with as few as five expert demonstrations per task. Experiments on complex robotic manipulation tasks demonstrate that RehearseVLA: effectively overcomes the data inefficiency, safety constraints, and inefficient execution of conventional VLA models that rely on real-world interaction, offering a practical and scalable solution for post-training in resource-constrained settings. Our code is available at this https URL.

在我上传 PDF 之后，请严格按下面结构输出中文分析，保留关键英文术语：
1. 这篇论文到底在解决什么问题？
2. 核心方法脉络是什么？
3. 真正的新意有哪些？给 3 条。
4. 实验设置、关键指标和主要结论是什么？
5. 哪些地方最可能是方法边界、实验短板或复现风险？给 3 条。
6. 它与我的研究兴趣有什么关系？
7. 最后给出一个结论：值不值得我进一步精读/复现，为什么？

要求：
- 只有在 PDF 明确给出证据时，才引用数字、表格、公式或模块细节。
- 如果某个信息在 PDF 中不明确，请直接写“不确定”。
- 结尾补一个“下一步阅读建议”，告诉我最该看论文里的哪几个章节、图表或实验。

```

---


### 💡 EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards [[PDF]](https://arxiv.org/pdf/2603.17808) [[ChatGPT]](https://chatgpt.com/)
> **适合何时点开**: 如果你需要确认方法细节、实验数字、公式推导或复现难度，打开 ChatGPT 后上传 PDF，再粘贴下面的 prompt。

* **Authors**: Ruixiang Wang, Qingming Liu, Yueci Deng, Guiliang Liu, Zhen Liu, Kui Jia
* **Abstract Link**: https://arxiv.org/abs/2603.17808

```text
你是我的机器人学研究搭档。请先检查我是否已经上传这篇论文的 PDF。

如果我还没有上传 PDF，请先提醒我上传 PDF，再暂停，不要猜测全文细节。

论文基础信息：
- Title: EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards
- Authors: Ruixiang Wang, Qingming Liu, Yueci Deng, Guiliang Liu, Zhen Liu, Kui Jia
- arXiv Abstract URL: https://arxiv.org/abs/2603.17808
- Research Interests: VLA (Vision-Language-Action), Sim2Real, RL+VLA, World Model
- Abstract: Video generative models are increasingly used as world models for robotics, where a model generates a future visual rollout conditioned on the current observation and task instruction, and an inverse dynamics model (IDM) converts the generated frames into executable robot actions. However, current video world models lack explicit executability constraints. As a result, visually coherent rollouts may still violate rigid-body and kinematic consistency, producing unstable or infeasible control commands when decoded by an IDM. We refer to this mismatch between visual generation and physically executable control as the executability gap. While this gap can be mitigated at inference time using techniques such as rejection sampling, such approaches are inefficient due to the high cost of video generation. In this paper, we leverage the executability gap as a training signal and introduce Executable Video Alignment (EVA), a reinforcement-learning post-training framework for aligning video world models. EVA trains an inverse dynamics model on real robot trajectories and repurposes it as a reward model that evaluates generated videos through the action sequences they induce, encouraging smooth motions measured by velocity, acceleration, and jerk while penalizing actions that violate embodiment constraints. Importantly, the reward remains informative even when generated videos contain severe visual artifacts, since such artifacts typically translate into unstable or out-of-bound actions. Experiments on the RoboTwin benchmark and a real bimanual robot show that EVA reduces embodiment-specific artifacts in generated rollouts and improves downstream task execution success.

在我上传 PDF 之后，请严格按下面结构输出中文分析，保留关键英文术语：
1. 这篇论文到底在解决什么问题？
2. 核心方法脉络是什么？
3. 真正的新意有哪些？给 3 条。
4. 实验设置、关键指标和主要结论是什么？
5. 哪些地方最可能是方法边界、实验短板或复现风险？给 3 条。
6. 它与我的研究兴趣有什么关系？
7. 最后给出一个结论：值不值得我进一步精读/复现，为什么？

要求：
- 只有在 PDF 明确给出证据时，才引用数字、表格、公式或模块细节。
- 如果某个信息在 PDF 中不明确，请直接写“不确定”。
- 结尾补一个“下一步阅读建议”，告诉我最该看论文里的哪几个章节、图表或实验。

```

---


### 💡 KineVLA: Towards Kinematics-Aware Vision-Language-Action Models with Bi-Level Action Decomposition [[PDF]](https://arxiv.org/pdf/2603.17524) [[ChatGPT]](https://chatgpt.com/)
> **适合何时点开**: 如果你需要确认方法细节、实验数字、公式推导或复现难度，打开 ChatGPT 后上传 PDF，再粘贴下面的 prompt。

* **Authors**: Gaoge Han, Zhengqing Gao, Ziwen Li, Jiaxin Huang, Shaoli Huang, Fakhri Karray, Mingming Gong, Tongliang Liu
* **Abstract Link**: https://arxiv.org/abs/2603.17524

```text
你是我的机器人学研究搭档。请先检查我是否已经上传这篇论文的 PDF。

如果我还没有上传 PDF，请先提醒我上传 PDF，再暂停，不要猜测全文细节。

论文基础信息：
- Title: KineVLA: Towards Kinematics-Aware Vision-Language-Action Models with Bi-Level Action Decomposition
- Authors: Gaoge Han, Zhengqing Gao, Ziwen Li, Jiaxin Huang, Shaoli Huang, Fakhri Karray, Mingming Gong, Tongliang Liu
- arXiv Abstract URL: https://arxiv.org/abs/2603.17524
- Research Interests: VLA (Vision-Language-Action), Sim2Real, RL+VLA, World Model
- Abstract: In this paper, we introduce a novel kinematics-rich vision-language-action (VLA) task, in which language commands densely encode diverse kinematic attributes (such as direction, trajectory, orientation, and relative displacement) from initiation through completion, at key moments, unlike existing action instructions that capture kinematics only coarsely or partially, thereby supporting fine-grained and personalized manipulation. In this setting, where task goals remain invariant while execution trajectories must adapt to instruction-level kinematic specifications. To address this challenge, we propose KineVLA, a vision-language-action framework that explicitly decouples goal-level invariance from kinematics-level variability through a bi-level action representation and bi-level reasoning tokens to serve as explicit, supervised intermediate variables that align language and action. To support this task, we construct the kinematics-aware VLA datasets spanning both simulation and real-world robotic platforms, featuring instruction-level kinematic variations and bi-level annotations. Extensive experiments on LIBERO and a Realman-75 robot demonstrate that KineVLA consistently outperforms strong VLA baselines on kinematics-sensitive benchmarks, achieving more precise, controllable, and generalizable manipulation behaviors.

在我上传 PDF 之后，请严格按下面结构输出中文分析，保留关键英文术语：
1. 这篇论文到底在解决什么问题？
2. 核心方法脉络是什么？
3. 真正的新意有哪些？给 3 条。
4. 实验设置、关键指标和主要结论是什么？
5. 哪些地方最可能是方法边界、实验短板或复现风险？给 3 条。
6. 它与我的研究兴趣有什么关系？
7. 最后给出一个结论：值不值得我进一步精读/复现，为什么？

要求：
- 只有在 PDF 明确给出证据时，才引用数字、表格、公式或模块细节。
- 如果某个信息在 PDF 中不明确，请直接写“不确定”。
- 结尾补一个“下一步阅读建议”，告诉我最该看论文里的哪几个章节、图表或实验。

```

---


### 💡 Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning [[PDF]](https://arxiv.org/pdf/2603.03818) [[ChatGPT]](https://chatgpt.com/)
> **适合何时点开**: 如果你需要确认方法细节、实验数字、公式推导或复现难度，打开 ChatGPT 后上传 PDF，再粘贴下面的 prompt。

* **Authors**: Huihan Liu, Changyeon Kim, Bo Liu, Minghuan Liu, Yuke Zhu
* **Abstract Link**: https://arxiv.org/abs/2603.03818

```text
你是我的机器人学研究搭档。请先检查我是否已经上传这篇论文的 PDF。

如果我还没有上传 PDF，请先提醒我上传 PDF，再暂停，不要猜测全文细节。

论文基础信息：
- Title: Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning
- Authors: Huihan Liu, Changyeon Kim, Bo Liu, Minghuan Liu, Yuke Zhu
- arXiv Abstract URL: https://arxiv.org/abs/2603.03818
- Research Interests: VLA (Vision-Language-Action), Sim2Real, RL+VLA, World Model
- Abstract: Continual learning is a long-standing challenge in robot policy learning, where a policy must acquire new skills over time without catastrophically forgetting previously learned ones. While prior work has extensively studied continual learning in relatively small behavior cloning (BC) policy models trained from scratch, its behavior in modern large-scale pretrained Vision-Language-Action (VLA) models remains underexplored. In this work, we found that pretrained VLAs are remarkably resistant to forgetting compared with smaller policy models trained from scratch. Simple Experience Replay (ER) works surprisingly well on VLAs, sometimes achieving zero forgetting even with a small replay data size. Our analysis reveals that pretraining plays a critical role in downstream continual learning performance: large pretrained models mitigate forgetting with a small replay buffer size while maintaining strong forward learning capabilities. Furthermore, we found that VLAs can retain relevant knowledge from prior tasks despite performance degradation during learning new tasks. This knowledge retention enables rapid recovery of seemingly forgotten skills through finetuning. Together, these insights imply that large-scale pretraining fundamentally changes the dynamics of continual learning, enabling models to continually acquire new skills over time with simple replay. Code and more information can be found at this https URL

在我上传 PDF 之后，请严格按下面结构输出中文分析，保留关键英文术语：
1. 这篇论文到底在解决什么问题？
2. 核心方法脉络是什么？
3. 真正的新意有哪些？给 3 条。
4. 实验设置、关键指标和主要结论是什么？
5. 哪些地方最可能是方法边界、实验短板或复现风险？给 3 条。
6. 它与我的研究兴趣有什么关系？
7. 最后给出一个结论：值不值得我进一步精读/复现，为什么？

要求：
- 只有在 PDF 明确给出证据时，才引用数字、表格、公式或模块细节。
- 如果某个信息在 PDF 中不明确，请直接写“不确定”。
- 结尾补一个“下一步阅读建议”，告诉我最该看论文里的哪几个章节、图表或实验。

```

---


### 💡 Mimic Intent, Not Just Trajectories [[PDF]](https://arxiv.org/pdf/2602.08602) [[ChatGPT]](https://chatgpt.com/)
> **适合何时点开**: 如果你需要确认方法细节、实验数字、公式推导或复现难度，打开 ChatGPT 后上传 PDF，再粘贴下面的 prompt。

* **Authors**: Renming Huang, Chendong Zeng, Wenjing Tang, Jintian Cai, Cewu Lu, Panpan Cai
* **Abstract Link**: https://arxiv.org/abs/2602.08602

```text
你是我的机器人学研究搭档。请先检查我是否已经上传这篇论文的 PDF。

如果我还没有上传 PDF，请先提醒我上传 PDF，再暂停，不要猜测全文细节。

论文基础信息：
- Title: Mimic Intent, Not Just Trajectories
- Authors: Renming Huang, Chendong Zeng, Wenjing Tang, Jintian Cai, Cewu Lu, Panpan Cai
- arXiv Abstract URL: https://arxiv.org/abs/2602.08602
- Research Interests: VLA (Vision-Language-Action), Sim2Real, RL+VLA, World Model
- Abstract: While imitation learning (IL) has achieved impressive success in dexterous manipulation through generative modeling and pretraining, state-of-the-art approaches like Vision-Language-Action (VLA) models still struggle with adaptation to environmental changes and skill transfer. We argue this stems from mimicking raw trajectories without understanding the underlying intent. To address this, we propose explicitly disentangling behavior intent from execution details in end-2-end IL: Mimic Intent, Not just Trajectories(MINT). We achieve this via multi-scale frequency-space tokenization, which enforces a spectral decomposition of action chunk representation. We learn action tokens with a multi-scale coarse-to-fine structure, and force the coarsest token to capture low-frequency global structure and finer tokens to encode high-frequency details. This yields an abstract Intent token that facilitates planning and transfer, and multi-scale Execution tokens that enable precise adaptation to environmental dynamics. Building on this hierarchy, our policy generates trajectories through next-scale autoregression, performing progressive intent-to-execution reasoning, thus boosting learning efficiency and generalization. Crucially, this disentanglement enables one-shot transfer of skills, by simply injecting the Intent token from a demonstration into the autoregressive generation process. Experiments on several manipulation benchmarks and on a real robot demonstrate state-of-the-art success rates, superior inference efficiency, robust generalization against disturbances, and effective one-shot transfer.

在我上传 PDF 之后，请严格按下面结构输出中文分析，保留关键英文术语：
1. 这篇论文到底在解决什么问题？
2. 核心方法脉络是什么？
3. 真正的新意有哪些？给 3 条。
4. 实验设置、关键指标和主要结论是什么？
5. 哪些地方最可能是方法边界、实验短板或复现风险？给 3 条。
6. 它与我的研究兴趣有什么关系？
7. 最后给出一个结论：值不值得我进一步精读/复现，为什么？

要求：
- 只有在 PDF 明确给出证据时，才引用数字、表格、公式或模块细节。
- 如果某个信息在 PDF 中不明确，请直接写“不确定”。
- 结尾补一个“下一步阅读建议”，告诉我最该看论文里的哪几个章节、图表或实验。

```

---


### 💡 Grounding Robot Generalization in Training Data via Retrieval-Augmented VLMs [[PDF]](https://arxiv.org/pdf/2603.11426) [[ChatGPT]](https://chatgpt.com/)
> **适合何时点开**: 如果你需要确认方法细节、实验数字、公式推导或复现难度，打开 ChatGPT 后上传 PDF，再粘贴下面的 prompt。

* **Authors**: Jensen Gao, Dorsa Sadigh, Sandy Huang, Dhruv Shah
* **Abstract Link**: https://arxiv.org/abs/2603.11426

```text
你是我的机器人学研究搭档。请先检查我是否已经上传这篇论文的 PDF。

如果我还没有上传 PDF，请先提醒我上传 PDF，再暂停，不要猜测全文细节。

论文基础信息：
- Title: Grounding Robot Generalization in Training Data via Retrieval-Augmented VLMs
- Authors: Jensen Gao, Dorsa Sadigh, Sandy Huang, Dhruv Shah
- arXiv Abstract URL: https://arxiv.org/abs/2603.11426
- Research Interests: VLA (Vision-Language-Action), Sim2Real, RL+VLA, World Model
- Abstract: Recent work on robot manipulation has advanced policy generalization to novel scenarios. However, it is often difficult to characterize how different evaluation settings actually represent generalization from the training distribution of a given policy. To work towards more precise evaluation of generalization in robotics, we propose RADAR, a scalable framework for directly comparing test-time evaluation tasks to policy training data, to determine what form of policy generalization is required. RADAR consists of a two-stage pipeline: first, retrieval using generalist policy embeddings identifies which training examples are relevant for a given evaluation task. Next, vision-language models (VLMs) analyze the evaluation task against the retrieved data, outputting interpretable analysis on how they compare along a variety of axes, and an overall classification of what type of policy generalization is required. Through controlled experiments, we demonstrate that VLMs are effective at analyzing data for generalization, and that our retrieval step effectively identifies examples needed to make accurate classifications with respect to the training data. Furthermore, we scale RADAR to large-scale datasets, where we observe agreement with human-defined benchmark conditions from prior work. We provide demonstrations at this http URL.

在我上传 PDF 之后，请严格按下面结构输出中文分析，保留关键英文术语：
1. 这篇论文到底在解决什么问题？
2. 核心方法脉络是什么？
3. 真正的新意有哪些？给 3 条。
4. 实验设置、关键指标和主要结论是什么？
5. 哪些地方最可能是方法边界、实验短板或复现风险？给 3 条。
6. 它与我的研究兴趣有什么关系？
7. 最后给出一个结论：值不值得我进一步精读/复现，为什么？

要求：
- 只有在 PDF 明确给出证据时，才引用数字、表格、公式或模块细节。
- 如果某个信息在 PDF 中不明确，请直接写“不确定”。
- 结尾补一个“下一步阅读建议”，告诉我最该看论文里的哪几个章节、图表或实验。

```

---
