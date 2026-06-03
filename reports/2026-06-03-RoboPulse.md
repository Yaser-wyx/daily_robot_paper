# RoboPulse | 2026-06-03

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 108 papers scanned · 10 shortlisted · 6 editor's picks

今天这组论文的主线很集中：VLA 不再只是把视觉、语言和动作端到端接起来，而是在追问“控制接口”到底应该给策略什么信息，以及哪些信息应该在训练时被压缩、对齐或预测。最终精选覆盖了 demo-conditioned VLA、test-time prompt adaptation、geometry/semantic world action model、state-guided spatial alignment、开源硬件软件栈，以及 embodied CoT 规模化预训练，基本对应了 VLA 泛化的六个关键瓶颈。VIP 作者上，Dieter Fox 参与的 SeeTraceAct 值得优先看其跨 embodiment demo grounding 设定；Cewu Lu 同时出现在 GeoAlign 与 OpenEAI-Platform，是今天最值得跟踪的核心作者信号；Xiaolong Wang 的 ConTrack 虽未进精选，但在人类示范到灵巧手 RL 跟踪上应保留关注。整体趋势是：可执行机器人策略正在从“语义理解增强”转向“空间、几何、轨迹、状态和推理接口的工程化重构”。

## 今日信号

- VLA 泛化的关键变量正在从更大的 backbone 转向更干净的执行接口：latent prompt、trajectory trace、state-guided geometry token 和 embodied CoT 都是在重写策略接收上下文的方式。
- World Action Model 的价值判断正在变得更细：今天的论文更强调预测训练带来的结构化表征，而不是必须在推理时显式 rollout 未来图像。
- Sim2Real 与真实部署证据越来越依赖硬件、数据、控制和模型的闭环复现，OpenEAI-Platform 与 GeoAlign 这类工作说明仅报仿真 benchmark 已不够有说服力。

## Historical Rediscovery

- **Paper**: ImagineUAV: Aerial Vision-Language Navigation via World-Action Modeling and Kinodynamic Planning [[HTML]](https://arxiv.org/html/2606.01205) [[PDF]](https://arxiv.org/pdf/2606.01205)
  - **Paper ID**: `2606.01205`
  - **来源日期**: 2026-06-02
  - **当时可能被低估的信号**: 当时因为摘录较少、且从操作转到 UAV VLN 被降权；但标题和历史备注已经明确给出 world-action modeling、latent video diffusion、action extractor、kinodynamic planning 这几个强信号。
  - **为什么现在值得再看**: 现在值得再看它如何把世界预测和动作生成耦合起来，尤其是几何一致性和动力学约束如何进入 VLA/WAM 式系统。对 World Model、World Action Model、Sim2Real 规划接口都有参考价值。
  - **建议动作**: 加入精读
  - **关键词**: `World Action Model` `latent video diffusion` `kinodynamic planning` `VLN` `future observation`
- **Paper**: PaCo-VLA: Passivity-Shielded Compliance Prior for Contact-Rich Vision-Language-Action Manipulation [[HTML]](https://arxiv.org/html/2606.00515) [[PDF]](https://arxiv.org/pdf/2606.00515)
  - **Paper ID**: `2606.00515`
  - **来源日期**: 2026-06-02
  - **当时可能被低估的信号**: 当时因为主线偏 world model、数据合成和动作解码而没入选；但“passivity-shielded compliance prior”和真实接触任务证据需求，正是 VLA 真实部署中容易被模型论文低估的控制契约问题。
  - **为什么现在值得再看**: VLA 真机部署越来越绕不开 contact-rich manipulation 和 safety layer。它和 VLA、Sim2Real、安全执行、真实接触控制强相关，适合补足纯策略/世界模型路线在物理交互层的短板。
  - **建议动作**: 加入精读
  - **关键词**: `VLA` `contact-rich manipulation` `passivity shield` `compliance control` `real deployment`
- **Paper**: PACE: Phase-Aware Chunk Execution for Robot Policies with Action Chunking [[HTML]](https://arxiv.org/html/2606.00537) [[PDF]](https://arxiv.org/pdf/2606.00537)
  - **Paper ID**: `2606.00537`
  - **来源日期**: 2026-06-02
  - **当时可能被低估的信号**: 当时被视作测试时执行修正，而非新架构；但历史备注已经指出 action chunk policy 的执行 horizon 是很多部署失败的低估因素。
  - **为什么现在值得再看**: 当前 VLA 和 diffusion action head 大量使用 action chunking，长时程操作中的重规划频率、动作复用和阶段切换会直接影响真实表现。它适合作为 RL+VLA 或 VLA 部署评测中的执行层基线。
  - **建议动作**: 快速浏览
  - **关键词**: `action chunking` `VLA deployment` `test-time execution` `long-horizon manipulation` `diffusion policy`
- **Paper**: LEGS: Fine-Tuning Teleop-Free VLAs for Humanoid Loco-manipulation in an Embodied Gaussian Splatting World [[HTML]](https://arxiv.org/html/2606.01458) [[PDF]](https://arxiv.org/pdf/2606.01458)
  - **Paper ID**: `2606.01458`
  - **来源日期**: 2026-06-02
  - **当时可能被低估的信号**: 当时因为偏 humanoid sim2real 数据管线、离 VLA/world model 核心架构稍远而降权；但 teleop-free VLA fine-tuning、3DGS 仿真和 humanoid loco-manipulation 的组合本身是强部署信号。
  - **为什么现在值得再看**: 如果关注 VLA 在真实机器人上的数据获取成本、仿真可迁移性和长时程全身操作，这篇可能比普通模型改进更有工程价值。它和 Sim2Real、VLA fine-tuning、真实部署数据生成直接相关。
  - **建议动作**: 加入精读
  - **关键词**: `Sim2Real` `VLA fine-tuning` `3D Gaussian Splatting` `humanoid` `teleop-free data`
- **Paper**: SafeVLA-Bench: A Benchmark for the Success-Safety Gap in Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2606.00773) [[PDF]](https://arxiv.org/pdf/2606.00773)
  - **Paper ID**: `2606.00773`
  - **来源日期**: 2026-06-02
  - **当时可能被低估的信号**: 当时因为是评测框架而非策略或世界模型方法被排除；但历史备注中的 success-safety gap、STL safety specs、violation severity 是真实部署评测中很容易被低估的信号。
  - **为什么现在值得再看**: 随着 VLA、RL+VLA 和 World Action Model 开始追求真实部署，单看 task success 会遗漏安全失败。它能作为审稿、benchmark 设计和真机评测的补充维度。
  - **建议动作**: 快速浏览
  - **关键词**: `VLA benchmark` `safety evaluation` `STL specs` `real deployment` `success-safety gap`

## Editor's Picks

### [1]. SeeTraceAct: Visibility-Aware Latent Planning from Cross-Embodiment Demonstration Videos [[VIP]] [[HTML]](https://arxiv.org/html/2606.02745) [[PDF]](https://arxiv.org/pdf/2606.02745) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.02745`
* **Authors**: Jaehyeon Son, Junhyun Kim, Kyle Kam, Jeremiah Coholich, Seok Joon Kim, Jinhoo Kim, Chris Dongjoo Kim, Jaemin Cho, Dieter Fox, Zsolt Kira
* **Author Priority**: Extended VIP
* **一句话结论**: 值得优先看：SeeTraceAct 把 one-shot 跨 embodiment 示范视频转成可见性感知的未来末端轨迹 latent plan，直击 demo-conditioned VLA 在小目标精确定位上的短板。
* **关键词**: `demo-conditioned VLA` `cross-embodiment` `visibility-aware trace` `latent planning` `Dieter Fox`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

这篇论文关注的是 VLA 扩展到新任务时最现实的瓶颈：如果每个新任务都要重新收集机器人遥操作数据，通用策略很难规模化。作者把问题设成 one-shot demo-conditioned VLA，即用户只做一次示范，机器人就要在未见任务上执行；示范还可能来自不同 embodiment，例如人手视频或另一种机器人。这个设定对 VLA 很重要，因为它把语言指令、视觉观察和动作生成之外的“示范理解”也纳入策略条件。现有端到端方法容易在需要精确空间 grounding 的任务上失败，特别是目标区域很小、交互点局部且跨 embodiment 外观差异明显时。SeeTraceAct 的动机就是让策略不要只从整段视频中隐式吸收任务意图，而要显式学习未来末端执行器应当经过哪里、哪些轨迹点在当前视角中可见。

#### ⚙️ 核心方法

方法建立在 GR00T N1.5 架构之上，原本包含 VLM 与 flow-matching action expert。SeeTraceAct 在这个基础上加入 demo-conditioned 的 latent planning 结构：训练时每个 seen task 有机器人专家轨迹、任务匹配的示范视频和语言指令；测试时面对 held-out unseen task，只给一段示范视频和指令，策略在每个时刻根据当前观测预测 action chunk。核心新意是用未来 end-effector trace 作为空间 grounding 信号，并且引入 visibility-aware 预测，避免把当前视角不可见的轨迹点当作同等强的监督。HTML 摘录可确认 trace label 是通过把末端执行器位置投影到各个 static camera view 自动生成的，这使得监督不依赖额外人工标注。论文的关键接口因此不是直接从人类动作到机器人动作的映射，而是从跨 embodiment 示范中抽取一个可见性感知的空间计划，再让 action expert 根据当前机器人状态和观测执行。当前摘录没有展开所有 loss 细节或网络头设计，因此对 latent trace 如何编码进 action expert、visibility mask 如何参与训练，需要等 PDF 核查。

#### 📊 实验与结果

实验主要有两个层面。仿真部分提出并使用 RoboCasa-DC，包含 category-balanced split 和 precision-sensitive split；每个 split 都 hold out 五个 unseen evaluation tasks，其余 19 个任务用于训练。precision-sensitive split 特别选择小 target interaction ratio 的任务，例如 TurnOffStove、CoffeePressButton、TurnOffSinkFaucet、PnPCounterToSink 和 PnPStoveToCounter，用来检验精确空间 grounding。真实机器人部分使用 Franka Panda 桌面操作，摘录中明确列出四个 seen tasks：Pick Coke、Stack Blocks、Stack Cups 和 Close Laptop，并提到每个任务收集 150 episode pairs。结论称 SeeTraceAct 在 baseline 中表现最强，尤其在 precision-sensitive tasks 上有较大收益，但摘录未给出具体成功率数字，因此不能引用表格数值。

#### ⚠️ 风险 / 保留意见

- trace label 依赖末端位置投影，遇到遮挡、多接触工具使用或非末端主导任务时监督信号可能不足。
- 当前摘要强调 precision-sensitive gain，但具体 baseline 设置、统计显著性和失败类型需要 PDF 表格核查。
- 跨 embodiment 示范是否能覆盖人手、第三视角、不同相机布局等真实用户场景，摘录证据仍有限。

#### 💭 结论与启发

这篇给后续 VLA 选题的启发是：demo-conditioned policy 不能只把示范视频当作另一个视觉 token 序列，而应当构造一个与控制直接相关的中间计划表示。未来复现时可以先不追求完整跨 embodiment 泛化，而是在已有 VLA backbone 上加入可见轨迹预测或 keypoint trace 辅助头，观察小目标交互任务是否显著改善。它也提示我们评测 VLA 新任务泛化时，要专门设计 precision-sensitive split，否则平均成功率可能掩盖空间定位失败。

#### 🔎 读 PDF 先核查

- visibility-aware trace 在训练中是作为辅助监督、输入条件，还是两者兼有？它与 flow-matching action expert 的连接方式是什么？
- RoboCasa-DC 的 precision-sensitive split 是否真正隔离了小目标定位难度，还是同时引入了任务类别和动作复杂度偏差？
- 真实 Franka 任务中，跨 embodiment 示范来自人类还是同机器人视角？这会直接影响方法的可部署性判断。

#### 📌 上传 PDF 后优先看

- 方法章节中的 visibility-aware trace prediction 和 latent planning 模块。
- RoboCasa-DC benchmark 构造、precision-sensitive split 定义和 target interaction ratio 说明。
- 真实机器人实验的示范来源、相机设置、baseline 对比和失败案例。

### [2]. TTT-VLA: Test-Time Latent Prompt Optimization for Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2606.03127) [[PDF]](https://arxiv.org/pdf/2606.03127) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.03127`
* **Authors**: Wenbo Zhang, Jianxiong Li, Shuai Yang, Sijin Chen, Jiajun Liu, Lingqiao Liu, Xiao Ma
* **Author Priority**: Standard
* **一句话结论**: 值得优先看：TTT-VLA 把部署期适应从昂贵 RL 转成 frozen policy 上的 latent prompt test-time optimization，是 VLA 分布偏移处理的一条轻量路线。
* **关键词**: `test-time training` `latent prompt optimization` `VLA adaptation` `flow matching` `SimplerEnv`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

VLA 在大规模预训练和多机器人数据上进展很快，但部署时仍会遭遇视觉条件、环境布局、物体外观和 embodiment 的分布偏移。传统的部署期改进常诉诸 RL，虽然能从交互中优化策略，但成本高、依赖 reward，并且容易带来安全和样本效率问题。另一方面，近年的 VLA 已经显示 prompt 是一种有效控制接口，但大多依赖外部语言指导或人工设计，不是真正从交互中自适应。TTT-VLA 的问题意识是：如果 prompt 本身可以成为可学习的 latent control variable，那么测试时是否只更新 prompt、冻结大模型主体，就能在不重训策略的情况下改善执行？这对机器人系统很有吸引力，因为它把 online adaptation 的更新对象限制在小规模 latent token 上，理论上更易部署和回滚。

#### ⚙️ 核心方法

论文把 VLA policy 写成由当前观测和统一 conditioning context 共同决定 action chunk 的条件策略，其中 conditioning 既可以包含语言、状态、图像等显式语义，也可以包含可学习 latent prompt。当前实现中，latent prompt 是一段可学习 prompt tokens，维度与 policy backbone hidden dimension 对齐，长度是超参数。基础动作生成沿用 flow-based VLA formulation：给定目标 action chunk、噪声样本和插值时间，策略学习条件 vector field。Latent Prompt Optimization 并不替代原有 action objective，而是在训练阶段学习一个可用于状态 grounding 的 latent prompt interface；部署时冻结 policy，只对 latent prompt 做 test-time training。摘录还显示实验包含三个版本：直接 fine-tune 的 baseline、加入 SG-LP 的 state grounded latent prompt，以及进一步执行 TTT 的完整 TTT-VLA。方法新意在于把 test-time learning 的可更新参数收缩到 prompt 层，让适应行为通过隐式上下文调制动作预测，而不是改动 VLM 或 action head 主体。当前摘录未充分说明 test-time objective 的具体形式、交互反馈来源和 reward/自监督信号，因此这些是阅读 PDF 的重点。

#### 📊 实验与结果

实验使用 SimplerEnv，覆盖 single-embodiment 和 multi-embodiment 两类设置。单 embodiment 包括固定 WidowX 和 Google Robot tasks；多 embodiment 设置则在 OXE-Aug 训练、在 WidowX 评估。摘录列出 WidowX 任务缩写 Spoon、Carrot、Cube 和 Eggplant，对应 Put Spoon on Towel、Put Carrot on Plate、Stack Blocks、Put Eggplant in Basket。对比中既报告 public state-of-the-art，也设置严格控制：无 state expert/latent prompt 的 baseline、+SG-LP，以及 +SG-LP+TTT 的完整方法。结论称在 single-embodiment 和 multi-embodiment 中都有改进，但 HTML 摘录没有提供具体成功率、交互轮数或训练开销数字，因此结果只能保守表述为 SimplerEnv 上的趋势性证据。

#### ⚠️ 风险 / 保留意见

- test-time objective 在摘录中证据不足，若依赖任务 reward 或多次交互，实际部署成本可能高于标题暗示。
- prompt-only 更新虽然参数少，但可能在长时序任务中产生局部适应、跨场景遗忘或不稳定行为。
- SimplerEnv 结果需要核查是否覆盖真实机器人，当前摘录只能确认仿真 benchmark。

#### 💭 结论与启发

TTT-VLA 的启发是把 VLA adaptation 看成接口学习问题，而不是每次都动 policy 主干。对系统设计来说，可以为部署期保留一组可优化 latent variables，用少量交互或自监督信号调节动作分布，同时保持主模型可审计、可缓存。复现时应优先实现最小版本：固定 VLA backbone，加入 state-grounded prompt token，对比训练期 prompt 和测试期 prompt 更新各自贡献。真正有价值的问题不是 prompt 是否能提高 benchmark，而是它在多少交互预算内、用什么反馈信号、以多大风险改变动作。

#### 🔎 读 PDF 先核查

- TTT 阶段优化 latent prompt 的损失到底来自 reward、action consistency、state prediction，还是其他自监督信号？
- SG-LP 相比普通 latent prompt 的 state grounding 机制是什么，是否需要额外 state expert 或特殊标注？
- prompt-only 更新在多任务连续部署时是 per-episode、per-task 还是持续累积？失败时如何重置？

#### 📌 上传 PDF 后优先看

- Latent Prompt Optimization 的 test-time objective 与优化流程。
- SG-LP、baseline、TTT-VLA 三者的消融表。
- SimplerEnv multi-embodiment 设置中的交互预算、训练数据和失败案例。

### [3]. GeoSem-WAM: Geometry- and Semantic-Aware World Action Models [[HTML]](https://arxiv.org/html/2606.03188) [[PDF]](https://arxiv.org/pdf/2606.03188) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.03188`
* **Authors**: Fulong Ma, Daojie Peng, Wenjun Yue, Jiahang Cao, Bintao Wang, Qiang Zhang, Jun Ma
* **Author Priority**: Standard
* **一句话结论**: 值得优先看：GeoSem-WAM 把 WAM 的辅助预测从 RGB 未来图像扩展到几何与语义监督，适合跟踪 world action model 是否正在转向结构化表征学习。
* **关键词**: `World Action Model` `geometry supervision` `semantic supervision` `training-only auxiliary heads` `LIBERO`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

World Action Models 近期被用于 embodied decision-making，但一个关键争议是：它们的收益到底来自推理时显式想象未来，还是来自预测训练带来的鲁棒 latent representation。GeoSem-WAM 明确站在后一个方向上，认为 WAM 的主要价值更可能是通过辅助预测学习对动作有用的未来感知表征。现有 WAM 多以 RGB future prediction 为主，这对复杂操作环境的空间结构、对象关系和任务语义理解可能不够。对于 VLA 和机器人 manipulation 来说，RGB 像素预测能捕获外观变化，却不一定能让策略理解物体边界、布局、可操作区域和语义角色。因此这篇的动机是用几何和语义监督增强 world-action representation，同时保持部署时的动作推理效率。

#### ⚙️ 核心方法

HTML 摘录显示，GeoSem-WAM 是一个 geometry- and semantics-enhanced world-action model，定位为 robot manipulation 的 plug-and-play 模块。它在训练时把 auxiliary DPT-style prediction heads 接到 intermediate video-expert tokens 上，用 dense geometric 与 semantic supervision 塑造表征；部署时保持 action inference pipeline 不变，不额外增加 test-time 计算。方法叙述强调不盲目扩模型或数据规模，而是在 CLIP、EVA-CLIP 等大规模视觉语言预训练基础上，把通用视觉文本对齐迁移到物理交互场景，并通过定制的多模态 world prediction supervision 强化 task-specific structured representation。可以确认的核心思想是：预测任务不只是 RGB reconstruction，而是让中间 token 同时学习视觉动态、空间布局和对象级语义，使 action policy 获得更强的 spatial motion awareness 与 task logical reasoning。当前摘录没有完整列出几何监督来源、语义标签来源、各辅助头 loss 权重和 plug-and-play 接入的具体 backbone，因此这些细节不能推断过度。

#### 📊 实验与结果

实验在两个仿真 benchmark 上进行：LIBERO 与 RoboTwin。LIBERO 包括 Spatial、Object、Goal、Long 四个 suite，每个 suite 提供 500 expert demonstrations、覆盖 10 tasks，用于考察空间配置、物体类别、目标规格和长时序执行。RoboTwin 是 bimanual manipulation 的 real-to-sim benchmark，包含 in-domain easy setting 和带 domain randomization 的更难设置，扰动包括场景杂物、背景纹理、光照和桌面高度。评价指标是 success rate。摘录中明确给出 GeoSem-WAM 在 LIBERO 的 overall average success rate 为 98.5%，但其他表格数值和与各 SOTA 的差距没有完整呈现。结论强调训练时结构化监督有效且推理不增加开销，不过真实机器人证据在摘录中未出现。

#### ⚠️ 风险 / 保留意见

- 几何和语义监督的来源、质量与成本在摘录中不完整，可能影响复现难度。
- 目前可确认实验主要是仿真 LIBERO/RoboTwin，真实部署泛化证据不足。
- 98.5% LIBERO 成绩需要核查任务划分、baseline 是否同 backbone、是否存在 benchmark 饱和。

#### 💭 结论与启发

GeoSem-WAM 对后续选题的价值在于，它把 WAM 从“生成未来画面”重新解释为“训练期结构化表征约束”。如果这个判断成立，很多 VLA 系统可以用更轻的方式受益于 world modeling：只在训练时加入 depth、segmentation、semantics 或 affordance 预测头，部署时丢弃辅助头，仅保留被塑形的 token。复现上应优先验证训练-only auxiliary supervision 是否真比 RGB prediction 更稳，而不是急着做复杂 test-time imagination。

#### 🔎 读 PDF 先核查

- DPT-style 几何与语义 prediction heads 分别预测什么目标，标签来自真实标注、预训练模型还是仿真 oracle？
- GeoSem-WAM 是接在哪个 VLA/action backbone 上，plug-and-play 是否需要改变 action decoder 输入维度？
- LIBERO 98.5% 的提升主要来自 Long、Spatial 还是 Object suite？这些 suite 的消融能否支持结构化监督主张？

#### 📌 上传 PDF 后优先看

- 模型架构中 intermediate video-expert tokens 与 auxiliary heads 的连接方式。
- 几何/语义监督数据来源、loss 设计和训练-only 部署策略。
- LIBERO 与 RoboTwin 的分 suite 对比、消融和 domain randomization 结果。

### [4]. GeoAlign: Beyond Semantics with State-Guided Spatial Alignment in VLA Models [[VIP]] [[HTML]](https://arxiv.org/html/2606.03240) [[PDF]](https://arxiv.org/pdf/2606.03240) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.03240`
* **Authors**: Yizhi Chen, Zhanxiang Cao, Xinyi Peng, Yixiao Zheng, Xiaxi Si, Yiheng Li, Liyun Yan, Keqi Zhu, Xueyun Chen, Shengcheng Fu, Tianyue Zhan, Yufei Jia, Jinming Yao, Yan Xie, Kun Wang, Cewu Lu, Yue Gao
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看：GeoAlign 由 Cewu Lu 参与，直接把 RGB-derived geometry 与机器人 proprioceptive state 对齐，用于解决 VLA 语义强但空间执行弱的问题。
* **关键词**: `state-guided spatial alignment` `RGB-derived geometry` `proprioceptive query` `VLA` `Cewu Lu`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

当前 VLA 往往受益于大规模 VLM 的语义 grounding，但机器人操作成败常取决于更细的几何关系：夹爪相对物体的位置、透明或环形物体的可操作区域、遮挡下的边界，以及不同执行阶段应关注的 affordance。GeoAlign 的出发点是，语义 token 不足以支撑可执行 manipulation，策略需要一种在 RGB 输入下获得几何感知、又不依赖部署时深度传感器的接口。这对 Sim2Real 和真实机器人很重要，因为 RGB-D 数据可以在离线阶段帮助学习几何表示，但实际 rollout 中深度传感器可能不稳定、昂贵或不可用。论文因此提出 state-guided spatial alignment：让机器人自身状态去查询图像空间几何特征，从而获得随操作阶段变化的 compact geometry tokens。

#### ⚙️ 核心方法

GeoAlign 在 language-conditioned VLA policy-learning 设置下工作。每个时间步输入 multi-view RGB images、语言指令和 proprioceptive state，输出 horizon action chunk。方法分成两阶段：第一阶段用 robot-domain RGB-D 数据对 RGB geometry branch 做 offline post-training，摘录明确提到适配 Depth Anything V2-Small，并在之后丢弃 depth head；第二阶段在 policy training 与 rollout 中，只使用 RGB、语言和机器人状态，不输入 measured depth、point clouds 或 depth maps。架构上，GeoAlign 将 decoder context 分解为 RGB-language semantic tokens 和 compact geometry tokens。冻结的 geometry branch 将多视角 RGB 映射为 image-space GEP feature grid；机器人 proprioceptive-state query slots 对这个 feature grid 做 cross-attention，产生与当前执行阶段相关的几何 token，再供 flow-matching action decoder 使用。新意在于几何不是作为全局特征静态拼接，而是由 state 引导选择：同一场景中，接近、抓取、放置阶段需要的空间证据不同，state query 让模型动态读取。

#### 📊 实验与结果

实验围绕三项主张：RGB-derived geometry 是否提升策略表现，收益是否来自 robot-domain geometry post-training 和 proprioceptive state querying，以及方法是否能用于真实 geometry-critical manipulation。评测包括 LIBERO 四个 suite、三个 shared SimplerEnv Google Robot Fractal task families，以及真实 AgileX ALOHA 平台八个桌面任务。摘录明确写到 LIBERO 总计 8,000 rollouts，真实任务覆盖透明容器、环形胶带、遮挡透明胶带和相对盘子的放置等几何关键场景。摘要给出 GeoAlign 在 LIBERO 达到 99.0%，在三个 SimplerEnv 任务族上为 85.3%。受控变体共享 Isaac-GR00T N1.6-3B backbone，比较 RGB-only、无 post-training、无 spatial querying 等消融。具体逐任务表格需 PDF 核查。

#### ⚠️ 风险 / 保留意见

- 离线 RGB-D post-training 需要 robot-domain depth supervision，数据采集和跨平台适配成本需要评估。
- 方法依赖 proprioceptive state query，若状态估计噪声大或 embodiment 差异明显，几何 token 质量可能下降。
- LIBERO/SimplerEnv 数字很强，需要核查是否存在 benchmark 饱和、任务重叠或 backbone 优势。

#### 💭 结论与启发

GeoAlign 是今天最有系统设计价值的 VLA 论文之一，因为它给出了“训练用深度、部署只用 RGB”的清晰路线。后续构建 VLA 时，可以把几何分支作为独立模块离线 post-train，再通过 state query 把几何证据压缩成少量 token，而不是把所有 patch token 塞给 action head。它也提醒我们，空间 alignment 的关键不是单纯加 depth feature，而是让机器人状态决定当前该看哪里、读什么几何关系。

#### 🔎 读 PDF 先核查

- GEP feature grid 是用哪些 robot-domain RGB-D 数据 post-train 的，和 policy demonstration 数据是否重叠？
- state query slots 的数量、初始化和 cross-attention 层数如何影响不同阶段的 affordance selection？
- 真实 ALOHA 八个任务中，GeoAlign 相比 RGB-only 的提升是否集中在透明、遮挡和环形物体场景？

#### 📌 上传 PDF 后优先看

- 两阶段 pipeline：Depth Anything V2-Small post-training、丢弃 depth head、GEP feature 提取。
- state-guided spatial querying 模块和与 flow-matching action decoder 的接口。
- LIBERO/SimplerEnv/真实 ALOHA 的 controlled ablations 与几何关键任务失败案例。

### [5]. OpenEAI-Platform: An Open-source Embodied Artificial Intelligence Hardware-Software Unified Platform [[VIP]] [[HTML]](https://arxiv.org/html/2606.03392) [[PDF]](https://arxiv.org/pdf/2606.03392) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.03392`
* **Authors**: Jinyuan Zhang, Luoyi Fan, Leiyu Wang, Yeqiang Wang, Yicheng Zhu, Cewu Lu, Nanyang Ye
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看：OpenEAI-Platform 不只是又一个 VLA，而是把低成本 6+1 DoF 硬件、控制和 Qwen3-VL-4B+DiT action head 做成可复现开源栈。
* **关键词**: `open-source robotics platform` `Qwen3-VL` `Diffusion Transformer action head` `feature query bottleneck` `Cewu Lu`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

真实 embodied AI 的瓶颈不只是模型能力，也包括硬件可获得性、控制精度、数据采集成本和复现实验环境。许多前沿 VLA 系统依赖专有大规模数据或昂贵商业机械臂，导致研究者难以验证模型、扩展数据或复现实验。OpenEAI-Platform 的意义在于把硬件与软件作为一个统一系统处理：OpenEAI-Arm 提供低成本 6+1 DoF 机械臂设计和控制方法，OpenEAI-VLA 则提供基于开源数据训练的可复现策略。对 VLA 社区来说，这类平台论文值得精选，不是因为单个 benchmark 一定刷新 SOTA，而是因为它可能降低真实机器人数据闭环的门槛，使更多实验从仿真走向可复制的真实部署。Cewu Lu 参与也使其成为核心作者跟踪信号。

#### ⚙️ 核心方法

OpenEAI-VLA 使用 Qwen3-VL-Instruct 4B 作为 backbone VLM，并接入 Diffusion Transformer 风格 action head。一个关键设计是固定长度 learnable feature query：模型不把所有 VLM hidden states 都输入 action head，而是在图像和文本 token 后追加一段固定长度、与 VLM token embedding space 同维的可学习 token 序列。经过 VLM 后，只取这些 query 对应的 final-layer hidden states 作为 compact conditioning embeddings，再送入 action generator。这个接口相当于 VLM 到动作头之间的固定带宽 bottleneck，使 action head 计算基本不随 image patches 或 text tokens 数量增长，同时让 query tokens 学会压缩与任务相关的视觉和指令信息。动作生成端是 18-layer DiT-style action expert，输出连续 action chunks。摘录还表明训练采用两阶段 recipe，并只使用 open-source robot 和 multimodal datasets，但具体数据构成、阶段目标、动作规范和硬件控制细节需要 PDF 核查。

#### 📊 实验与结果

实验评估 OpenEAI-Arm 和 OpenEAI-VLA 在四个真实 manipulation tasks 上的表现，任务从短时 pick-and-place 到长时 dual-arm deformable-object manipulation，包括 Clean Table、Make Tea、Fold Towel 和 Fold T-shirt。评测分两条线：硬件比较中，用同一个 OpenEAI-VLA 分别在 OpenEAI-Arm、ARX R5 和 AgileX Piper 等 6-DoF 机械臂上，在匹配规模的遥操作数据和相同 fine-tuning 设置下比较；模型比较中，以 OpenEAI-Arm 为平台，比较 ACT、Octo、OpenVLA-oft 以及其他系列模型。摘要称 OpenEAI-Arm 优于部分商业臂，OpenEAI-VLA 也优于若干 baselines，但摘录未给出具体成功率或硬件指标数值，因此只能确认其真实任务与统一协议，而不能复述表格细节。

#### ⚠️ 风险 / 保留意见

- 平台论文的价值高度依赖开源完整度，机械设计、BOM、控制固件、数据和训练代码需要逐项核查。
- 低成本硬件的精度、耐久性和安全性可能随装配质量变化，复现实验方差会较大。
- 模型比较若受硬件平台、数据规模或任务设计影响，不能简单外推为通用 VLA 排名。

#### 💭 结论与启发

OpenEAI-Platform 的启发是，VLA 研究如果想真正走向 Sim2Real 和真实数据扩展，需要把硬件接口当成论文贡献的一部分。固定长度 feature query 也很实用：它为 VLM-to-action 提供稳定带宽，适合在不同图像数量和文本长度下控制 action head 成本。后续如果做实验平台建设，应优先关注这类可复制硬件加开源 VLA recipe，而不是只在昂贵商业臂上验证模型。

#### 🔎 读 PDF 先核查

- OpenEAI-Arm 的开源硬件文件、控制系统和标定流程是否足以让外部实验室复现同等精度？
- 两阶段 OpenEAI-VLA 训练分别使用哪些 open-source robot/multimodal datasets，是否包含目标评测任务相近数据？
- 固定长度 learnable feature query 相比读取全部 VLM hidden states 的消融收益来自稳定性、速度还是泛化？

#### 📌 上传 PDF 后优先看

- OpenEAI-Arm 硬件规格、制造成本、控制精度和装配说明。
- OpenEAI-VLA 的 feature query bottleneck、DiT action head 和两阶段训练数据。
- 四个真实任务中的硬件比较、模型比较、统一 evaluation protocol 和失败案例。

### [6]. Revisiting Embodied Chain-of-Thought for Generalizable Robot Manipulation [[HTML]](https://arxiv.org/html/2606.03784) [[PDF]](https://arxiv.org/pdf/2606.03784) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.03784`
* **Authors**: Nan Sun, Yuan Zhang, Yongkun Yang, Wentao Zhao, Peiyan Li, Jun Guo, Wenxuan Song, Pengxiang Ding, Runze Suo, Yifei Su, Xin Xiao, Xinghang Li, Huaping Liu
* **Author Priority**: Standard
* **一句话结论**: 值得优先看：这篇用近百万轨迹规模重新检验 embodied CoT，结论指向“动作级语言指导”比高层推理文字更能帮助 VLA。
* **关键词**: `embodied chain-of-thought` `VLA pretraining` `action guidance` `image-space trajectories` `ERVLA`
* **证据来源**: arXiv HTML (Introduction, Experiments)

#### 📖 背景与动机

Embodied CoT 的直觉是让机器人先推理再行动，把语言推理链作为从 VLM 到动作控制的中间桥梁。但机器人控制和纯语言任务不同，高层语义解释不一定能改善低层动作生成；VLA 在复杂、分布外场景中失败，常常不是“不知道任务含义”，而是不知道下一步末端该如何移动、该看哪里、如何把视觉 grounding 转成连续动作。此前 ECoT 工作显示显式 reasoning traces 可能有帮助，但有效形式和集成方式仍不清楚。本文的价值在于用很大规模的 embodied CoT corpus 系统重做这个问题：什么样的 CoT 对 action policy 真有用，CoT 是否能成为更强 VLM 迁移到 VLA 的接口，以及它能否作为可扩展的 action pre-training signal。

#### ⚙️ 核心方法

摘录可确认，论文构建了目前规模很大的 embodied CoT corpus，包含 978,743 trajectories、226.3M samples 和 2592.5 hours of data。实验围绕三类问题组织：不同 embodied CoT 字段对 action policy learning 的作用，ECoT 是否能把更强 VLM backbone 转成更强 VLA action policy，以及 ECoT 能否作为 scalable pre-training signal。核心结论是，有效 CoT 必须把高层 semantic understanding 落到具体 linguistic action guidance，例如 end-effector movement 和 image-space trajectories；单纯高层 reasoning 只有边际收益。方法上，作者先用统一 backbone 和 autoregressive prediction 做 controlled studies，识别有用 CoT fields、评估预训练价值和 VLM-to-VLA transfer；随后比较 ERVLA 与强 baseline，并消融 reasoning-action integration 与 CoT pre-training scale；最后做真实任务评估。当前摘录没有给出 ERVLA 架构细节、CoT 标注生成方式或训练目标，因此不能具体描述 decoder 结构和 loss。

#### 📊 实验与结果

实验使用三个互补 benchmark。LIBERO 是常用 manipulation benchmark，但摘录也指出其固定设置可能鼓励 benchmark-specific overfitting；LIBERO-Plus 扩展了 camera、state、language、background 和 layout shifts，用于更强泛化评测；第三个 benchmark 名称在摘录处被截断，不能补全。实验分三段：Sec. 3.1 做统一 backbone 下的 controlled studies，分析 CoT 字段、预训练价值和 VLM-to-VLA transfer；Sec. 3.2 比较 ERVLA 与强 baselines，并消融 reasoning-action integration 和 CoT pre-training scale；Sec. 3.3 评估真实机器人任务，覆盖语义理解、鲁棒场景 grounding 和长时序能力。除 corpus 规模外，摘录没有给出成功率或表格数字，因此结果只能表述为论文声称大规模实验证明 action-grounded CoT 更有效。

#### ⚠️ 风险 / 保留意见

- CoT corpus 的生成、质量控制和是否含模型蒸馏偏差在摘录中不清楚，是复现最大风险。
- 大规模数据带来的收益可能与 CoT 形式纠缠，需要仔细看 scale ablation 才能判断因果。
- 如果 CoT 以语言形式介入动作生成，推理延迟、错误解释和长时序累积偏差都需评估。

#### 💭 结论与启发

这篇对阅读策略的启发非常明确：以后看到 embodied CoT 论文，不应只问 reasoning 是否更“像人”，而要问它是否提供了可执行的动作约束。对系统设计来说，最值得尝试的是把 CoT 拆成高层语义、末端运动描述、图像空间轨迹等字段，并通过消融找出真正帮助 action head 的部分。它也提示 VLM-to-VLA transfer 可能需要一个动作语言中间层，而不是直接把更强 VLM 接到动作头。

#### 🔎 读 PDF 先核查

- CoT corpus 中 end-effector movement 和 image-space trajectories 是人工标注、规则生成还是由模型自动生成？
- ERVLA 如何把 reasoning tokens 与 action prediction 集成，是作为输入条件、辅助输出，还是多阶段推理？
- scale ablation 是否证明 CoT 字段本身有效，而不是 978,743 trajectories 的数据规模带来主要提升？

#### 📌 上传 PDF 后优先看

- CoT corpus 构建、字段定义、标注/生成流程和质量控制。
- 不同 CoT fields 的 controlled studies，尤其高层 reasoning vs action guidance。
- ERVLA 与 baselines 的 LIBERO、LIBERO-Plus、真实机器人对比和 scale ablation。

## Watchlist

### [W1]. See Less, Specify More: Visual Evidence Budgets for Generalizable VLAs [[HTML]](https://arxiv.org/html/2606.02735) [[PDF]](https://arxiv.org/pdf/2606.02735)
* **Paper ID**: `2606.02735`
* **Authors**: Yueh-Hua Wu, Tatsuya Matsushima, Kei Ota
* **Author Priority**: Standard
* **为什么还值得留意**: S2 进入 watchlist 是因为它抓住了 VLA 泛化中的接口问题：Specify More 用更细的轨迹/子任务语言减少执行歧义，See Less 用 visual evidence budget 抑制无关视觉干扰。它没有进入最终精选，主要是因为今天已有多篇精选覆盖了更核心的空间 grounding、几何对齐和 test-time adaptation；同时摘录显示其主要实例化在 OpenPI pi05_base/LIBERO 设置上，需要进一步核查真实机器人和跨 backbone 证据。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. ConTrack: Constrained Hand Motion Tracking with Adaptive Trade-off Control [[VIP]] [[HTML]](https://arxiv.org/html/2606.03177) [[PDF]](https://arxiv.org/pdf/2606.03177)
* **Paper ID**: `2606.03177`
* **Authors**: Yutong Liang, Quanquan Peng, Ri-Zhao Qiu, Xiaolong Wang
* **Author Priority**: Core VIP
* **为什么还值得留意**: ConTrack 值得保留关注，因为 Xiaolong Wang 是核心优先作者，且论文处理人类示范到灵巧手 contact-rich tracking 的 RL 难题，包含 constrained task-style allocation、online dual controller、reset library 和 contact priors。它未进最终精选，是因为主题更偏 dexterous motion tracking/RL，而不是今天主线中的 VLA、world model 或 vision-language-action policy；不过如果后续关注人类示范到机器人灵巧操作，这篇应优先补读。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. AirDreamer: Generalist Drone Navigation with World Models [[HTML]](https://arxiv.org/html/2606.03252) [[PDF]](https://arxiv.org/pdf/2606.03252)
* **Paper ID**: `2606.03252`
* **Authors**: Zian Liu, Andong Yang, Chunkai Yang, Ruidong An, Chao Gao, Guyue Zhou
* **Author Priority**: Standard
* **为什么还值得留意**: AirDreamer 进入 watchlist 是因为它把 Dreamer V3 world model 与 RL policy 用于未知杂乱环境无人机导航，并报告仿真和真实 drone transfer，符合 world model + sim2real 的关注方向。它没有进入最终精选，主要因为应用域是 aerial navigation 而非 manipulation/VLA，且方法更接近 RL navigation stack；摘要中 5.3% success rate improvement 值得记住，但需要 PDF 确认 baseline、公平性和真实平台细节。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. Partially Observable Adversarial Patch Attacks on Vision-Language-Action Models in Robotics [[HTML]](https://arxiv.org/html/2606.03556) [[PDF]](https://arxiv.org/pdf/2606.03556)
* **Paper ID**: `2606.03556`
* **Authors**: Xiaofei Wang, Mingliang Han, Tianyu Hao, Yi Yang, Yun-Bo Zhao, Keke Tang
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇 adversarial patch attack 进入 watchlist，是因为 VLA 走向真实部署后，部分可观测攻击模型比 full-rollout attack 更接近现实威胁。它没有进入最终精选，原因是今天重点放在提升 VLA/World Model 能力与可复现系统，而该文偏安全评测；但其“只用短前缀生成固定 patch 并影响后续帧”的设定，对后续 VLA robustness checklist 很有价值。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
