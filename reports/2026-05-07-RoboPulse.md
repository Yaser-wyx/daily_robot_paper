# RoboPulse | 2026-05-07

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 65 papers scanned · 10 shortlisted · 5 editor's picks

今天主线很清楚：VLA 正在从“直接从图像到动作”转向更可编辑、更可 rollout、更能被 RL 后训练校准的策略体系。最终精选覆盖了长时程层级规划、离散扩散驾驶自修正、驾驶员中心世界模型、latent action 监督综述式实验，以及 latent reasoning + RL 后训练，基本对应 VLA/World Model/World Action Model 的关键交叉点。VIP 作者上，He Wang 的 HDFlow、Yue Wang 的 ReflectDrive-2、Hao Su 的 Driver-WM 最值得优先跟踪，分别代表 manipulation planning、driving VLA、human-in-the-loop world model 三条线。未入选但仍进 watchlist 的论文多半是方向强、系统感强，但从摘录看证据边界、工程依赖或与今日主线的贴合度略弱。

## 今日信号

- VLA 研究正在把“动作预测”拆成可编辑 token、latent reasoning、goal posterior、world rollout 等中间层，以便提高可控性和后训练空间。
- World model 不再只预测外部场景，正在扩展到驾驶员状态、触觉未来、长时程 latent MPC 等更贴近真实闭环部署的动态对象。
- RL/RFT 的角色正在从单纯提高分数转向修正 imitation learning 的分布偏移，并与离散扩散、latent reasoning、counterfactual feedback 结合。

## Editor's Picks

### [1]. HDFlow: Hierarchical Diffusion-Flow Planning for Long-horizon Tasks [[VIP]] [[HTML]](https://arxiv.org/html/2605.04525) [[PDF]](https://arxiv.org/pdf/2605.04525) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.04525`
* **Authors**: Nandiraju Gireesh, Yuanliang Ju, Chaoyi Xu, Weiheng Liu, Yuxuan Wan, He Wang
* **Author Priority**: Core VIP
* **一句话结论**: 优先看，尤其适合跟踪长时程 manipulation 中“世界模型 latent space + 生成式层级规划”的下一步形态。
* **问题与切口**: HDFlow 面向长时程、稀疏奖励、接触丰富的机器人任务，切口不是再训练一个单一扩散规划器，而是把高层子目标生成与低层快速轨迹执行分离。它用扩散模型承担战略性 subgoal sequence，用 rectified flow 负责更快的低层执行，试图同时解决长时程任务的组合复杂度和扩散迭代推理慢的问题。相对已有生成式 planner，新意在于把层级分解、world model latent space 和两类生成模型的优势明确组合起来。
* **核心方法与证据**: 正文摘录显示方法分两阶段：先训练带 contrastive objective 的 RSSM 世界模型，借助 DINOv2 encoder 学出带任务进度语义的 latent space；再冻结 latent 表示，在其上训练层级 planner。高层部分是带 EBM 引导、manifold-aware 的 diffusion subgoal planner，低层是 rectified flow planner，用于提升实时执行效率。实验围绕 FurnitureBench 的 one_leg、lamp、round_table、cabinet 等任务，比较 SOTA、非混合层级 planner、单 planner、核心组件消融与推理效率；但具体数值需等 PDF 核查。
* **正文要点**:
  - 将长时程 manipulation 分解为高层 latent subgoal 规划和低层动作/轨迹生成，而不是单一端到端生成。
  - 世界模型采用 RSSM，并通过 contrastive objective 强化 latent space 中的语义结构和进度信息。
  - 实验设计明确覆盖 FurnitureBench 的多任务、多初始化难度、组件消融和推理效率，适合检查方法是否真的兼顾性能与实时性。
* **为什么值得跟**:
  - 如果成立，它为长时程 VLA/世界模型控制提供了一个可复用的层级生成式规划范式。
  - 高层 diffusion 与低层 rectified flow 的分工，回应了扩散规划器在实时机器人控制中的推理成本问题。
  - He Wang 在 manipulation/world model 方向值得跟踪，这篇与今日 Sim2Real、World Action Model 主题高度相关。
* **风险 / 保留意见**:
  - 摘录没有给出成功率、推理延迟或真实机器人结果，性能优势需要 PDF 表格和设置细节验证。
  - 方法依赖预训练视觉 encoder、RSSM latent 质量和层级训练稳定性，复现成本可能不低。
* **建议先看**: 先看 world model latent space 如何被定义为“有进度语义”的空间，再看 high-level diffusion 与 low-level rectified flow 的接口。实验部分优先核查 ablation 是否能证明混合架构优于单一范式。
* **关键词**: `Hierarchical Planning` `Diffusion Planning` `Rectified Flow` `World Model` `FurnitureBench`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - contrastive world model 的正负样本或进度信号如何构造，是否真正对应可执行子目标？
  - EBM-guided 高层 diffusion 在 manifold 上如何约束 subgoal，是否会引入额外采样成本？
  - 低层 rectified flow 的速度优势是否在同等成功率下成立，还是用性能换取实时性？
* **上传 PDF 后优先看**:
  - 方法章节中的 world model learning 与 contrastive objective 设计
  - 层级 planner 架构、EBM guidance、diffusion-flow 接口说明
  - FurnitureBench 主结果、组件消融、推理效率实验

### [2]. ReflectDrive-2: Reinforcement-Learning-Aligned Self-Editing for Discrete Diffusion Driving [[VIP]] [[HTML]](https://arxiv.org/html/2605.04647) [[PDF]](https://arxiv.org/pdf/2605.04647) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.04647`
* **Authors**: Huimin Wang, Yue Wang, Bihao Cui, Pengxiang Li, Ben Lu, Mingqian Wang, Tong Wang, Chuan Tang, Teng Zhang, Kun Zhan
* **Author Priority**: Core VIP
* **一句话结论**: 优先看，它把 driving VLA 的离散 token 规划、扩散生成和 RL 对齐自修正放在同一个闭环问题里。
* **问题与切口**: ReflectDrive-2 针对自动驾驶 imitation policy 常见的纵向速度误判和横向航向漂移，提出一种可原地编辑的离散扩散规划器。核心不是生成一次轨迹后交给外部 refine 网络，而是把轨迹表示为离散 BEV coordinate tokens，用 masked diffusion 并行生成，再用同一个条件 token 模型 AutoEdit 重写部分 token。它的新意在于把 goal hypothesis、trajectory drafting、token-space correction 和 RL reward 对齐放进统一动作 token 空间。
* **核心方法与证据**: 方法流程包括 goal-point posterior、goal-conditioned masked diffusion 和 AutoEdit 三个耦合组件。训练上先构造沿纵向进度和横向 heading 的结构化扰动，让模型恢复专家轨迹；随后用 PDMS 作为 reward 做 reinforcement fine-tuning。实验摘录显示在 NAVSIM/nuPlan 闭环规划基准上评估 4 秒、2Hz ego trajectory，指标包含碰撞、可行驶区域、TTC、舒适性和进度。模型使用相机时序帧、导航指令、ego-state token，并与端到端 planner 和 VLA planner 比较；具体排名和收益需核查 PDF。
* **正文要点**:
  - 把驾驶轨迹离散化为 token，使同一模型既能生成轨迹，也能对局部错误 token 做原地修正。
  - AutoEdit 针对纵向进度和横向航向两类常见规划错误，避免额外引入独立 refinement network。
  - 实验使用 NAVSIM 闭环基准与 PDMS 相关指标，训练包含 SFT 与基于规划得分的 reinforcement fine-tuning。
* **为什么值得跟**:
  - 离散 token action space 让 driving VLA 更接近语言模型式编辑和 RL 对齐流程。
  - 并行 masked decoding 可能比自回归轨迹生成更适合实时驾驶规划。
  - Yue Wang 在核心作者名单中，这篇是今日 RL + VLA driving 方向最直接的精选。
* **风险 / 保留意见**:
  - 摘录提到 proprietary pretrained weights，复现与公平比较需要特别关注。
  - 自修正是否真的来自 AutoEdit 机制，而非模型规模、预训练或 reward fine-tuning，需要看消融。
* **建议先看**: 先追踪离散轨迹 token 的定义和 AutoEdit 的 mask/重写策略，再看 RL fine-tuning 如何把 PDMS reward 传回 token policy。实验中重点看相对 DiffusionDrive、GoalFlow、DriveVLA 类方法的公平性。
* **关键词**: `Discrete Diffusion` `Driving VLA` `AutoEdit` `Reinforcement Fine-Tuning` `NAVSIM`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - goal-point posterior 生成的行为假设如何与后续 masked diffusion 解码绑定？
  - AutoEdit 选择哪些 token 重写，选择机制是否依赖显式错误检测或 reward signal？
  - PDMS reward fine-tuning 是否会牺牲舒适性、进度或安全指标中的某一项？
* **上传 PDF 后优先看**:
  - 离散轨迹 tokenization 与 masked diffusion decoder 设计
  - AutoEdit 训练扰动、编辑策略和 RL fine-tuning 目标
  - NAVSIM 主结果、消融、与 VLA/扩散驾驶 baselines 的比较

### [3]. Driver-WM: A Driver-Centric Traffic-Conditioned Latent World Model for In-Cabin Dynamics Rollout [[VIP]] [[HTML]](https://arxiv.org/html/2605.05092) [[PDF]](https://arxiv.org/pdf/2605.05092) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.05092`
* **Authors**: Haozhuang Chi, Daosheng Qiu, Hao Su, Haochen Liu, Zirui Li, Haoruo Zhang, Chen Lv
* **Author Priority**: Core VIP
* **一句话结论**: 优先看，因为它把 world model 的对象从车外场景扩展到驾驶员状态，是 L2/L3 human-in-the-loop 安全的重要支线。
* **问题与切口**: Driver-WM 关注的是自动驾驶共享控制中的驾驶员反应预测，而不是常见的外部交通世界模型。它提出 driver-centric latent world model，在车外交通上下文条件下 rollout 车内驾驶员动态，同时兼顾骨架几何预测和行为、情绪、交通、车辆状态等语义识别。新意在于把 in-cabin intelligence 从静态识别推进到多步 latent rollout，并用因果 gated coupling 控制外部环境对内部驾驶员状态的影响。
* **核心方法与证据**: 方法采用双流架构，分别编码 out-cabin traffic 与 in-cabin driver state，再通过 gated causal injection 把外部上下文以时间因果方式注入内部 latent rollout。摘录显示特征来自冻结的视觉语言模型，实验在 AIDE assistive driving benchmark 上进行，视频切成 3 秒片段、10 帧采样；给定观测步后在 latent space 预测未来步，并解码为 HALPE-136 2D skeleton。四个辅助分类头用于语义正则，但标签不作为 transition 或 gating 输入，这是证据边界中比较重要的设计。
* **正文要点**:
  - 研究对象从道路场景预测转向驾驶员动态预测，契合 L2/L3 接管 readiness 问题。
  - 双流 latent world model 用 gated causal injection 连接车外交通与车内驾驶员状态。
  - 实验同时评估未来 skeleton rollout 与辅助语义识别，并明确排除语义标签作为时序条件输入。
* **为什么值得跟**:
  - 它提醒 world model 不只是预测环境，还可以预测人机共驾系统中的人类反应。
  - 对 takeover、shared control、驾驶员监控系统来说，多步 rollout 比单帧识别更接近决策需求。
  - Hao Su 是核心优先作者，这篇可作为 robotics/AD human-centered world model 的跟踪入口。
* **风险 / 保留意见**:
  - 摘录没有给出与现有 in-cabin recognition 或 trajectory forecasting 方法的具体性能差距。
  - AIDE benchmark 到真实 L2/L3 部署的外推仍需谨慎，尤其是安全关键异常场景覆盖。
* **建议先看**: 先看 gated causal injection 是否真正强制时间因果，再看辅助语义 head 是提升 rollout 还是只提升识别指标。PDF 中应重点确认 long-horizon 误差随时间增长的曲线或等价分析。
* **关键词**: `Driver-Centric World Model` `In-Cabin Dynamics` `Causal Gating` `Shared Control` `AIDE`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 外部交通上下文通过 gate 注入内部 latent 时，是否有机制防止未来信息泄漏？
  - 辅助语义分类 head 对 skeleton rollout 的贡献有多大，是否做了去除 head 的消融？
  - 所谓 critical inertia effect 在实验中如何定义和验证，是否只是观察性结论？
* **上传 PDF 后优先看**:
  - 双流架构与 gated causal injection 的方法细节
  - AIDE 数据协议、观测/预测窗口和标签使用约束
  - long-horizon skeleton rollout、语义辅助任务、消融实验

### [4]. From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2605.04678) [[PDF]](https://arxiv.org/pdf/2605.04678) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.04678`
* **Authors**: Yihan Lin, Haoyang Li, Yang Li, Haitao Shen, Yihan Zhao, Chao Shao, Jing Zhang
* **Author Priority**: Standard
* **一句话结论**: 优先看，它像一篇 VLA latent action 监督的路线图，适合用来校准后续论文的技术取舍。
* **问题与切口**: 这篇系统研究 latent action supervision 在 VLA 中的作用，问题切口很实用：异构机器人数据和人类视频的 action space 不一致，直接统一训练会有动作语义错配。作者把 latent action 分成两类视角：image-based latent action 用视觉转移正则化轨迹，action-based latent action 用动作抽象统一 target space；并在统一 VLA baseline 下比较四种集成策略。它的价值不在单一模型炫技，而在给出 formulation-task correspondence 的经验判断。
* **核心方法与证据**: 摘录显示 image-based latent action 采用 UniVLA 式两阶段 latent action model，使用冻结 DINOv2 visual encoder 和 Transformer VQ-VAE 建模观测转移，并区分 controllable/uncontrollable latent；同时加入轻量 action-supervised regularization。实验围绕三个问题：image-based 还是 action-based、更优集成架构、离散 token 还是连续表示。评估覆盖 LIBERO-Long、RoboTwin 2.0 子集和真实 JAKA 机械臂；结论称 image-based 更利于长时程推理与场景泛化，action-based 更支持复杂任务，直接预测离散 latent action 效果最好。
* **正文要点**:
  - 把 latent action supervision 拆成 image-based trajectory regularization 与 action-based target unification 两条路线。
  - 在统一 VLA baseline 下比较多种集成策略，避免只在不同模型间做不可控横向比较。
  - 实验覆盖长时程 LIBERO、复杂 RoboTwin 任务和真实 JAKA 设置，适合作为经验性设计指南。
* **为什么值得跟**:
  - VLA 数据异构是规模化训练的核心瓶颈，latent action 是当前最有希望的中间表示之一。
  - 这篇能帮助判断何时该用视觉转移 latent，何时该用动作空间 latent。
  - 它补足今日精选中偏方法论的一环，为看 LaST-R1、HDFlow 等 latent 设计提供参照。
* **风险 / 保留意见**:
  - 系统比较的结论可能依赖所选统一 baseline、latent model 预训练方式和任务集合。
  - 摘录只给出方向性结论，缺少具体显著性、失败案例和跨 embodiment 分析。
* **建议先看**: 先看四种 latent action integration strategy 的定义，再对照不同 benchmark 的任务属性。阅读时不要只看平均表现，应关注哪些任务支持 image-based 与 action-based 的分工判断。
* **关键词**: `Latent Action` `VLA Supervision` `Discrete Tokens` `LIBERO` `RoboTwin`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 四种集成策略分别改变了 VLA 的输入、目标还是中间监督，是否可公平比较？
  - image-based latent action 的 controllable/uncontrollable 分解是否在机器人任务中可解释？
  - 离散 latent token 优于连续表示的结论是否在真实 JAKA 实验中同样成立？
* **上传 PDF 后优先看**:
  - latent action taxonomy 与四种 integration strategy
  - UniVLA/VQ-VAE latent action model 的训练与冻结设置
  - LIBERO、RoboTwin、JAKA 分任务结果和离散/连续消融

### [5]. LaST-R1: Reinforcing Robotic Manipulation via Adaptive Physical Latent Reasoning [[HTML]](https://arxiv.org/html/2604.28192) [[PDF]](https://arxiv.org/pdf/2604.28192) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.28192`
* **Authors**: Hao Chen, Jiaming Liu, Zhonghao Yan, Nuowei Han, Renrui Zhang, Chenyang Gu, Jialin Gao, Ziyu Guo, Siyuan Qian, Yinxi Wang, Peng Jia, Shanghang Zhang, Pheng-Ann Heng
* **Author Priority**: Standard
* **一句话结论**: 优先看，它是今日最贴近“VLA latent reasoning + 在线 RL 后训练”的 manipulation 论文。
* **问题与切口**: LaST-R1 针对 latent-reasoning VLA 多停留在静态 imitation learning 的问题，提出用 RL post-training 释放“reasoning-before-acting”策略的适应性。它不显式生成语言 CoT 或未来图像，而是在统一 VLA 中先生成 latent reasoning embeddings，再预测动作，从而希望保留物理动态建模能力，同时降低显式中间输出的延迟和离散化瓶颈。核心新意是 LAPO，即围绕 latent-to-action 的策略优化，把 latent reasoning 与 action generation 联合纳入 RL 更新。
* **核心方法与证据**: 方法基于 Qwen3-VL-4B 架构，结合 SigLIP2-Large 视觉编码器和 LLM backbone；图像嵌入与语言嵌入进入 LLM 后，模型先 autoregressively 生成 latent reasoning embeddings，再通过扩展 action token vocabulary 预测离散化动作。训练流程包括大规模自定义数据预训练、SFT warm-up，以及在模拟器中在线 RL 收集 rollout 并更新 policy。实验覆盖 LIBERO-Spatial/Object/Goal/Long、消融、真实机器人部署和泛化能力；摘录没有具体分数，但问题设置与今日 RL + VLA 主题高度一致。
* **正文要点**:
  - 提出 latent Chain-of-Thought 式 reasoning-before-acting，但避免显式语言或未来状态生成。
  - LAPO 将 latent reasoning 与动作预测绑定到 RL post-training，而不是只做静态 imitation learning。
  - 实验覆盖 LIBERO 四套任务、真实机器人部署和泛化分析，设计上瞄准适应性与长时程能力。
* **为什么值得跟**:
  - RL 后训练正在成为 VLA 从离线模仿走向可适应策略的关键路径。
  - latent reasoning 提供了比语言 CoT 更低延迟、比直接动作更结构化的中间层。
  - 这篇与 Karamcheti/OpenVLA 系列背景高度相关，适合跟踪下一代 robotic foundation model 训练范式。
* **风险 / 保留意见**:
  - 自定义大规模数据和在线 RL 细节可能显著影响结果，复现门槛较高。
  - latent reasoning 的可解释性有限，需要确认它是否真的编码物理动态，而非只是额外隐层容量。
* **建议先看**: 先抓住 latent reasoning embeddings 如何构造、何时生成、如何接到 action tokens。随后重点看 LAPO 的 objective 与消融，确认 RL 增益来自 latent-to-action 优化而非训练预算。
* **关键词**: `Latent Reasoning` `VLA` `RL Post-Training` `LAPO` `LIBERO`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - latent reasoning embeddings 是否有专门监督信号，还是完全由动作/RL 目标间接塑形？
  - LAPO 与常规 policy optimization 的差异具体体现在哪里，优势是否由消融支持？
  - 在线 RL rollout 的采样效率、失败恢复和 simulator-to-real 泛化如何处理？
* **上传 PDF 后优先看**:
  - LaST-R1 统一模型结构与 latent reasoning 生成机制
  - LAPO 目标、RL post-training 流程和 SFT warm-up 设置
  - LIBERO 主结果、真实机器人部署、核心消融与泛化实验

## Watchlist

### [W1]. CRAFT: Counterfactual-to-Interactive Reinforcement Fine-Tuning for Driving Policies [[VIP]] [[HTML]](https://arxiv.org/html/2605.04470) [[PDF]](https://arxiv.org/pdf/2605.04470)
* **Paper ID**: `2605.04470`
* **Authors**: Keyu Chen, Nanfei Ye, Yida Wang, Wenchao Sun, Danqi Zhao, Hao Cheng, Sifa Zheng
* **Author Priority**: Core VIP
* **为什么还值得留意**: CRAFT 进入 shortlist 是因为它直接处理 open-loop imitation driving policy 到 closed-loop deployment 的分布偏移，并把 counterfactual fine-tuning 与 interactive RL feedback 结合。它还显式覆盖 VLA 与 world action model 语境下的驾驶策略后训练，方向非常相关。没有进入最终精选，主要是因为今日已选择 ReflectDrive-2 作为 driving RL/VLA 代表；CRAFT 从摘录看更偏 post-training 框架，具体收益和协议调整需要 PDF 进一步核查。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)

### [W2]. ConsisVLA-4D: Advancing Spatiotemporal Consistency in Efficient 3D-Perception and 4D-Reasoning for Robotic Manipulation [[HTML]](https://arxiv.org/html/2605.05126) [[PDF]](https://arxiv.org/pdf/2605.05126)
* **Paper ID**: `2605.05126`
* **Authors**: Wei Li, Jizhihui Liu, Li Yixing, Junwen Tong, Rui Shao, Liqiang Nie
* **Author Priority**: Standard
* **为什么还值得留意**: ConsisVLA-4D 关注 3D perception 与 4D reasoning 的时空一致性，切中了当前 2D VLA 在复杂空间操控中的弱点。它适合继续观察，因为它试图把 instruction-grounded scene alignment、3D spatial understanding 和 future reasoning 放到统一框架。未进最终精选，是因为提供的 method 摘录更多在定位相关工作，核心模块与实验细节证据不足。
* **证据来源**: arXiv HTML (Introduction, Method)

### [W3]. RLDX-1 Technical Report [[HTML]](https://arxiv.org/html/2605.03269) [[PDF]](https://arxiv.org/pdf/2605.03269)
* **Paper ID**: `2605.03269`
* **Authors**: Dongyoung Kim, Huiwon Jang, Myungkyu Koo, Suhyeok Jang, Taeyoung Kim, Beomjun Kim, Byungjun Yoon, Changsung Jang, Daewon Choi, Dongsu Han, Donguk Lee, Heeseung Kwon, Hojin Jeon, Jaehyun Kang, Jaekyoung Bae, Jihyuk Lee, Jimin Lee, John Won, Joonwoo Ahn, Junhyeong Park, Junyoung Sung, Kyungmin Lee, Minseong Han, Minsung Yoon, Sejune Joo, Seonil Son, Seungcheol Park, Seunggeun Cho, Seungjun Moon, Seungku Kim, Yonghoon Dong, Yongjin Cho, Youngchan Kim, Chang Hwan Kim, Dohyeon Kim, Heecheol Kim, Heewon Lee, Hensen Ahn, Hyungkyu Ryu, Hyunsoo Choi, Hyunsoo Shin, Jaeheon Jung, Jaewoo Kim, Jinwook Kim, Joochul Chang, Joonsoo Kim, Junghun Park, Jungwoo Park, Junho Cho, Junhyeok Park, Junwon Lee, Kangwook Lee, Kwanghoon Kim, Kyoungwhan Choe, Manoj Bhadu, Nayoung Oh, Sangjun Kim, Sangwoo Kim, Seunghoon Shim, Seunghyun Kim, Seungjun Lee, Seungyup Ka, Sungryol Yang, Wook Jung, Yashu Shukla, Yeonjae Lee, Yeonwoo Bae, Jinwoo Shin
* **Author Priority**: Standard
* **为什么还值得留意**: RLDX-1 是大系统型 VLA 技术报告，涵盖 dexterous manipulation、multi-stream action transformer、motion awareness、long-term memory 和 physical sensing，工程野心很强。它进入 watchlist 是因为真实世界 humanoid/single-arm 操作和多 benchmark 覆盖度值得跟踪。未进最终精选，是因为论文更像系统报告，作者不在优先名单中，且摘录里的模型规模、数据构成和真实评估细节需要更多核查后才适合深推。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. Learning to Feel the Future: DreamTacVLA for Contact-Rich Manipulation [[HTML]](https://arxiv.org/html/2512.23864) [[PDF]](https://arxiv.org/pdf/2512.23864)
* **Paper ID**: `2512.23864`
* **Authors**: Guo Ye, Zexi Zhang, Xu Zhao, Shang Wu, Haoran Lu, Shihan Lu, Han Liu
* **Author Priority**: Standard
* **为什么还值得留意**: DreamTacVLA 很有意思，因为它把 VLA 的 contact-blindness 具体落到高分辨率触觉、Hierarchical Spatial Alignment 和 tactile world model 预测未来触觉图像。它与 World Model 和 contact-rich manipulation 主题贴合，尤其适合作为触觉 VLA 支线跟踪。未进最终精选，是因为今日主线更偏视觉-语言-动作、RL 后训练和驾驶/长时程规划；触觉传感器、数据和部署条件也可能让可复现性更受限。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W5]. ELVIS: Ensemble-Calibrated Latent Imagination for Long-Horizon Visual MPC [[HTML]](https://arxiv.org/html/2605.04709) [[PDF]](https://arxiv.org/pdf/2605.04709)
* **Paper ID**: `2605.04709`
* **Authors**: Yurui Du, Pinhao Song, Yutong Hu, Renaud Detry
* **Author Priority**: Standard
* **为什么还值得留意**: ELVIS 进入 watchlist 是因为它处理 visual MPC 中长时程 latent imagination 的不确定性和多模态未来，用 GMM-MPPI 与 ensemble-UCB-gated return truncation 改进 Dreamer-style RSSM planning。它还明确提到 zero-shot sim-to-real 的真实沙喷任务，和今日 Sim2Real/World Model 方向相关。未进最终精选，是因为它更偏 model-based RL/control，而非 VLA 或 language-conditioned action；与今日核心 VLA 线相比优先级略低。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
