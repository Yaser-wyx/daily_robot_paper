# RoboPulse | 2026-06-04

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 73 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线很清楚：VLA 不再只是在更大离线数据上做行为克隆，而是在尝试把“部署经验、物理可执行性、潜在动作、视频/世界模型、数字生成数据”接进同一个训练闭环。最终精选的 6 篇分别覆盖了大规模 latent dynamics、fleet-scale 在线强化学习、跨 embodiment world action model、UMI 数据适配、带 success potential 的 flow policy，以及 humanoid loco-manipulation 的数字生成管线，基本对应 VLA 训练栈的关键短板。VIP 作者里，He Wang 参与的 LDA-1B、Jianlan Luo 参与的 LWD、Yuke Zhu 参与的 GRAIL 都值得优先跟踪，因为它们分别押注 foundation-scale 动力学学习、真实部署中的持续 RL、以及人形机器人数据生成。整体看，今天更像是“如何让 VLA 从可模仿走向可部署”的一组论文，而不是单点 benchmark 刷分。

## 今日信号

- VLA 后训练正在从纯行为克隆转向混合质量经验利用：在线 RL、success-potential、physical validation 都在解决失败轨迹如何不被浪费的问题。
- World model / world action model 的重点正在从“能生成未来视频”转向“能按动作精确生成、能跨 embodiment 条件化、能服务 policy evaluation”。
- 机器人数据扩展不再只靠真实遥操作，UMI 适配、视频先验、3D asset 合成和异构数据 ingestion 正在形成新的数据工程竞争线。

## Historical Rediscovery

- **Paper**: See Less, Specify More: Visual Evidence Budgets for Generalizable VLAs [[HTML]](https://arxiv.org/html/2606.02735) [[PDF]](https://arxiv.org/pdf/2606.02735)
  - **Paper ID**: `2606.02735`
  - **来源日期**: 2026-06-03
  - **当时可能被低估的信号**: 当时被低估的信号是：Specify More 用更细的轨迹/子任务语言减少执行歧义，See Less 用 visual evidence budget 主动压制无关视觉干扰，这正好对应 VLA 在真实场景中被背景和模糊指令拖垮的问题。
  - **为什么现在值得再看**: 现在值得再看，因为它和 VLA 泛化、空间 grounding、长时程任务分解都有直接关系；即使真实机器人和跨 backbone 证据仍需核查，这个“少看但说清楚”的接口设计可能对 World Action Model 的任务条件化也有启发。
  - **建议动作**: 加入精读
  - **关键词**: `VLA` `generalization` `visual evidence budget` `task specification` `instruction grounding`
- **Paper**: AirDreamer: Generalist Drone Navigation with World Models [[HTML]](https://arxiv.org/html/2606.03252) [[PDF]](https://arxiv.org/pdf/2606.03252)
  - **Paper ID**: `2606.03252`
  - **来源日期**: 2026-06-03
  - **当时可能被低估的信号**: 当时被低估的信号是：Dreamer V3 world model 用于未知杂乱环境无人机导航，并报告了仿真到真实 drone transfer；虽然不是 manipulation，但 world model + RL + real transfer 的组合非常贴近当前研究兴趣。
  - **为什么现在值得再看**: 现在值得再看，因为它可以作为 World Model 在真实机器人闭环中的案例参考，尤其适合比较 action-conditioned prediction、policy learning 和 sim2real 评测链路。应用域是 aerial navigation，但方法问题和 VLA/World Action Model 的部署评估高度相通。
  - **建议动作**: 加入精读
  - **关键词**: `world model` `Dreamer V3` `RL` `Sim2Real` `real robot transfer`
- **Paper**: ElegantVLA: Learning When to Think for Efficient Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2605.29438) [[PDF]](https://arxiv.org/pdf/2605.29438)
  - **Paper ID**: `2605.29438`
  - **来源日期**: 2026-05-29
  - **当时可能被低估的信号**: 当时被低估的信号是：phase-adaptive scheduling 在冻结 VLA 上学习何时重算、何时复用，并已有 CogACT、GR00T 和 real-world speedup 信号；这不是简单加速，而是影响闭环控制稳定性的部署机制。
  - **为什么现在值得再看**: 现在值得再看，因为真实 VLA 或 World Action Model 系统不仅要会推理，还要在控制频率下可靠运行。它和真实部署评测、长时程操作中的计算预算分配、在线策略执行效率直接相关。
  - **建议动作**: 快速浏览
  - **关键词**: `VLA` `inference efficiency` `control frequency` `real-world speedup` `deployment`
- **Paper**: DynaFLIP: Rethinking Robotics Perception via Tri-Modal-Dynamics Guided Representation [[HTML]](https://arxiv.org/html/2605.30350) [[PDF]](https://arxiv.org/pdf/2605.30350)
  - **Paper ID**: `2605.30350`
  - **来源日期**: 2026-05-29
  - **当时可能被低估的信号**: 当时被低估的信号是：image-language-3D flow triplets 和 simplex-guided multimodal alignment 试图把动态信息注入视觉预训练，而不是只依赖静态 image-language encoder。
  - **为什么现在值得再看**: 现在值得再看，因为 World Action Model 需要能表达动作后果和状态变化的表征；它虽然不是完整 policy 论文，但在 MetaWorld、RLBench、LIBERO 和真实任务上的验证线索，可能对 VLA perception backbone 和 dynamics grounding 有参考价值。
  - **建议动作**: 加入精读
  - **关键词**: `dynamics-aware representation` `VLA perception` `3D flow` `robot pretraining` `world action model`
- **Paper**: AsyncShield: A Plug-and-Play Edge Adapter for Asynchronous Cloud-based VLA Navigation [[HTML]](https://arxiv.org/html/2604.24086) [[PDF]](https://arxiv.org/pdf/2604.24086)
  - **Paper ID**: `2604.24086`
  - **来源日期**: 2026-04-28
  - **当时可能被低估的信号**: 当时被低估的信号是：它把 asynchronous cloud-based VLA 的延迟问题拆成几何映射、约束优化和 RL 适配，问题定义比单纯报告导航成功率更接近真实系统瓶颈。
  - **为什么现在值得再看**: 现在值得再看，因为真实部署评测不能只看离线策略能力，还要看云边延迟、动作滞后和安全约束。它与 VLA real deployment、RL adaptation、Sim2Real 系统鲁棒性直接相关，虽然应用场景偏导航。
  - **建议动作**: 继续跟踪
  - **关键词**: `VLA deployment` `cloud robotics` `asynchronous control` `RL adaptation` `robust navigation`

## Editor's Picks

### [1]. LDA-1B: Scaling Latent Dynamics Action Model via Universal Embodied Data Ingestion [[VIP]] [[HTML]](https://arxiv.org/html/2602.12215) [[PDF]](https://arxiv.org/pdf/2602.12215) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2602.12215`
* **Authors**: Jiangran Lyu, Kai Liu, Xuheng Zhang, Haoran Liao, Yusen Feng, Wenxuan Zhu, Tingrui Shen, Jiayi Chen, Jiazhao Zhang, Yifei Dong, Wenbo Cui, Senmao Qi, Shuo Wang, Yixin Zheng, Mi Yan, Xuesong Shi, Haoran Li, Dongbin Zhao, Ming-Yu Liu, Zhizheng Zhang, Li Yi, Yizhou Wang, He Wang
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看：LDA-1B 把 UWM 从概念推进到 1B 参数和 30k 小时级异构具身数据 ingestion，是今天最接近 robot foundation model 数据范式重写的一篇。
* **关键词**: `latent dynamics` `Unified World Model` `heterogeneous embodied data` `robot foundation model` `He Wang`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

这篇论文瞄准的是当前大规模机器人模型的核心矛盾：行为克隆可以稳定扩展，但它强依赖高质量 expert action，许多低质量、非专家、甚至只有交互动态价值的数据会被丢弃或弱利用。对于 VLA 和 Sim2Real 来说，这很关键，因为真实机器人系统最终需要的不只是“模仿正确动作”，还需要理解动作如何改变场景、哪些视觉变化可预测、哪些物理规律可迁移。作者将 Unified World Model 作为替代路线，认为同时学习 dynamics、policy 和 visual forecasting 可以让不同质量数据承担不同角色。不过，摘录也指出已有 UWM 实例离 foundation-level 还远，原因包括数据使用粗糙、数据集碎片化、难以稳定扩大模型规模。LDA-1B 的动机就是把异构 embodied data 组织成可扩展训练资产，而不是只筛出可行为克隆的部分。

#### ⚙️ 核心方法

LDA-1B 的核心是“universal embodied data ingestion”：不同质量、不同来源的 embodied 数据不再被当成同质 demonstration，而是被分配给 dynamics、policy、visual forecasting 等不同学习目标。根据摘录，模型在结构化 DINO latent space 中学习 dynamics，并使用 mixed-frequency multimodal diffusion transformer，使得训练可以扩展到 1B 参数级别。这里的新意不只是模型大，而是把 UWM 的多任务学习和数据分层结合起来：高质量 robot trajectories 可以服务 action/policy 学习，异构的人类或机器人轨迹可以更多提供物理交互和视觉预测信号，从而缓解纯 BC 对 expert data 的依赖。当前摘录只能确认它联合学习 dynamics、policy 和 visual forecasting，以及 EI-30k 数据集包含超过 30k 小时的人类和机器人轨迹；关于 latent dynamics 的具体状态变量、loss 权重、diffusion transformer 的层级设计、不同数据质量如何自动或人工分配，还需要上传 PDF 后核查。方法定位上，它更像是把机器人 foundation model 的训练目标从“动作监督”扩展到“动作-视觉-动态联合建模”。

#### 📊 实验与结果

摘录明确给出了 RoboCasa-GR1 simulation 实验：这是包含 24 个 tabletop rearrangement 和 articulated-object manipulation 任务的模拟厨房 benchmark，使用 GR-1 humanoid robot 和 Fourier dexterous hands，并从头戴相机的 egocentric RGB 观察中完成高自由度灵巧操作。作者按 GR00T 协议，每个任务用 1,000 条轨迹 finetune，每个任务 51 次 trial，报告平均成功率。对比包括 GR00T、其强变体以及 UWM，并复现了一个 1B 参数 GR00T-EI10k 基线，使用 EI-30k 高质量子集和 Qwen3-VL encoder。摘录中唯一完整可引用的数值是原始 GR00T-N1.6 为 3B 参数、成功率 47.6%；LDA 的完整表格结果在摘录中被截断，因此不能捏造最终提升幅度。结论只可保守写为：作者声称跨实验表现强，但具体优势、消融贡献和真实机器人证据需要核查全文。

#### ⚠️ 风险 / 保留意见

- 当前摘录未完整展示 LDA 相对 GR00T-EI10k、UWM 的最终成功率，不能仅凭结论判断提升幅度。
- EI-30k 的数据清洗、质量分层和数据来源分布会强烈影响可复现性，需要确认是否公开到足够细。
- UWM 联合目标可能带来训练复杂度和目标冲突，尤其是 dynamics、policy、forecasting 在不同质量数据上的权重选择。

#### 💭 结论与启发

这篇对后续选题的启发是：机器人 foundation model 的关键不一定只是收集更多 expert demos，而是把“不可直接模仿但包含动态信息”的数据转化为训练信号。复现上可以先不追 1B 参数，而是验证一个小规模 data-role assignment：同一批异构数据中，哪些用于视觉预测，哪些用于 inverse/action 学习，哪些只用于 dynamics latent consistency。系统设计上，LDA-1B 值得作为 VLA 数据管线的参考，把数据 ingestion、质量标注、训练目标分配作为一等公民。

#### 🔎 读 PDF 先核查

- EI-30k 中不同质量数据是如何被定义、筛选和分配到 dynamics、policy、visual forecasting 目标的？
- structured DINO latent space 在动作预测和视觉预测之间承担什么接口角色，是否比像素空间或 VAE latent 更稳定？
- LDA 的性能提升主要来自数据规模、数据分层、多目标 UWM，还是 1B 参数模型容量？

#### 📌 上传 PDF 后优先看

- 数据构建与 universal embodied data ingestion 章节
- 模型架构与 mixed-frequency multimodal diffusion transformer 章节
- RoboCasa-GR1 对比表、消融实验和任何真实机器人部署实验

### [2]. Learning While Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies [[VIP]] [[HTML]](https://arxiv.org/html/2605.00416) [[PDF]](https://arxiv.org/pdf/2605.00416) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.00416`
* **Authors**: Yi Wang, Xinchen Li, Pengwei Xie, Pu Yang, Buqing Nie, Yunuo Cai, Qinglin Zhang, Chendi Qu, Jeffrey Wu, Jianheng Song, Xinlin Ren, Jingshun Huang, Mingjie Pan, Siyuan Feng, Zhi Chen, Jianlan Luo
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看：LWD 把 VLA 后训练放到 fleet-scale 部署闭环里，用真实机器人在线 RL 处理长尾失败，是今天最贴近落地部署的一篇。
* **关键词**: `fleet-scale RL` `online post-training` `VLA deployment` `distributional value learning` `Jianlan Luo`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

大规模 VLA 预训练给了机器人广泛的初始能力，但离真实部署仍有距离。原因在于真实世界不是固定 test distribution：机器人进入商店、家庭或工作空间后，会遇到新物体、新布局、新语言指令、用户偏好和长尾失败。离线数据再大，也很难覆盖部署时出现的局部变化和人类纠正机会。LWD 的出发点是把 deployment 从一次性验收改成持续学习过程：机器人执行任务、收集共享物理经验、改进策略、再部署，形成 fleet-scale offline-to-online RL 闭环。这对 VLA 尤其重要，因为 generalist policy 如果只靠静态 demonstration，很容易在长任务和低频失败上停滞；而在线 RL 若设计不当，又会带来安全、成本、价值估计不稳和策略退化问题。因此论文的价值在于尝试把 RL 的持续改进能力和 VLA 的泛化初始策略结合起来。

#### ⚙️ 核心方法

LWD 从 pretrained VLA policy 出发，在部署期间持续收集真实机器人经验，并通过离线到在线的 RL 框架进行 post-training。摘录显示其关键组件包括 DIVL value learning 和 QAM policy extraction；附录片段还提到 distributional value model 使用固定 categorical support，并采用类似 C51 的 projection，把 scalar target 投影到相邻 atoms 后用 cross entropy 训练。方法上，DIVL 似乎服务于分布式/非对称价值估计：不是只学一个均值 value，而是从数据集 action-values 的分布中提取特定分位或非对称统计，以便更稳健地处理混合质量部署数据。QAM 则被描述为用于 policy extraction 的模块，当前摘录无法确认其完整公式和采样策略。整体流程可以理解为：初始化 VLA，fleet 部署并回收数据，用 distributional value 评估动作或状态的改进潜力，再用特定 extraction/selection 机制更新可部署策略。当前摘录只能确认其 online RL、DIVL、QAM 和 distributional value 细节片段，不能进一步捏造 replay buffer 规模、更新频率或安全约束。

#### 📊 实验与结果

实验完全落在真实任务上，这是它进入精选的主要原因。摘录列出 8 个 real-world tasks：4 个 grocery restocking 任务，包括 flat-shelf restocking、misplaced-item correction、freezer restocking with door operation、open-cooler restocking with carton handling；另有 4 个 long-horizon tasks，包括 brewing Gongfu Tea、making Fruit Juice、making Cocktail、packing shoes into a Shoebox。长任务通常持续 3-5 分钟，包含 5-8 个 annotated subtasks，涉及抓取调整、容器处理、倒取、工具使用和最终放置等接触丰富技能。评估变化包括物体实例、杂乱程度、货架和容器布局、语言指令和商店配置。摘录没有给出最终成功率数字或统计显著性，因此只能说作者声称 LWD 在这些任务上带来提升；具体 baselines、改进幅度、失败模式和 fleet 规模需要核查全文。

#### ⚠️ 风险 / 保留意见

- 真实部署在线 RL 的安全策略、人工干预成本和失败恢复机制在摘录中不充分。
- 没有摘录到完整数值结果，难以判断 LWD 相比 filtered BC、offline RL 或继续 imitation 的实际收益。
- fleet-scale 结论依赖机器人数量、任务流量和数据共享机制，复现门槛可能很高。

#### 💭 结论与启发

LWD 的启发在于把 VLA 评估从“离线 benchmark 成功率”推到“部署后能否继续变好”。后续如果做系统设计，应把日志、失败分类、人类纠正、value learning 和安全回滚一起纳入策略生命周期，而不是把 RL 当成训练后单独加的算法模块。选题上，这篇很适合追踪 generalist VLA post-training：如何从 mixed deployment experience 中稳定学习，可能比再堆静态数据更接近商业机器人长期能力增长。

#### 🔎 读 PDF 先核查

- DIVL 的非对称价值估计具体如何避免高估失败轨迹或低估可恢复轨迹？
- QAM policy extraction 是直接更新 VLA action head，还是通过候选动作筛选/加权方式改进策略？
- 8 个真实任务中的提升是否来自在线 RL 本身，还是来自更多人工纠正和部署数据覆盖？

#### 📌 上传 PDF 后优先看

- DIVL 和 QAM 方法章节
- 真实机器人任务设置、数据收集闭环与安全机制章节
- 8 个任务的主结果表、消融实验和失败案例分析

### [3]. OSCAR: Omni-Embodiment Skeleton-Conditioned World Action Model for Robotics [[HTML]](https://arxiv.org/html/2606.04463) [[PDF]](https://arxiv.org/pdf/2606.04463) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.04463`
* **Authors**: Zhuoyuan Wu, Jun Gao
* **Author Priority**: Standard
* **一句话结论**: 值得优先看：OSCAR 用 2D skeleton 作为跨机器人和人手的统一动作条件，是 world action model 服务 policy evaluation 的清晰尝试。
* **关键词**: `World Action Model` `skeleton conditioning` `policy evaluation` `cross-embodiment` `video world model`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

视频 world model 已经成为机器人策略评估、想象训练和 action planning 的关键候选模块，但机器人场景下的问题比通用视频生成更苛刻：模型不仅要生成看起来合理的未来，还要精确跟随动作，知道动作何时发生、在哪里发生，并且能跨不同机器人 embodiment 泛化。现有 robot video datasets 场景多样性有限，action-conditioned video model 又容易把动作条件学成弱提示，导致生成视频不能可靠反映 policy 的真实后果。OSCAR 的动机正是补上这个缺口：构建一个 action-conditioned video world model，既能利用机器人和 egocentric human 数据扩展场景，又能用统一的动作表示跨机械臂和人手。对于 World Action Model 方向，这篇的价值不在于单纯生成质量，而在于把生成模型定位为 policy evaluation 工具。

#### ⚙️ 核心方法

OSCAR 的方法有两个核心设计。第一是大规模标准化数据管线：对广泛的机器人和 egocentric human datasets 进行整理、过滤和去重，形成干净的 joint-training dataset，覆盖多样任务、场景、动作和 robot embodiments。第二是用 2D kinematic skeleton rendering 作为统一条件表示。相比直接用关节命令、末端位姿或带纹理机器人渲染，2D skeleton 更接近 embodiment-agnostic 接口：更换机器人时主要更新 kinematic specification，而 texture-free render 降低模型把外观纹理绑定到特定机器人本体的风险。摘录显示作者在 Cosmos-Predict2.5-2B 上 finetune，并且使用单个 GH200 GPU。方法上，这相当于把 robot arms 和 human hands 都映射到一种可视化运动骨架，再让视频 diffusion model 学习从当前图像和 skeleton 条件到未来视频的动作后果预测。当前摘录只能确认其 skeleton conditioning、数据管线、Cosmos-Predict2.5-2B finetune 和跨四种机器人 embodiment 加人手的主张；具体 skeleton 定义、动作序列编码、训练 loss 和 rollout 长度需要核查 PDF。

#### 📊 实验与结果

摘录显示 OSCAR 的评估重点是 policy evaluation，而不是只看视频质量。论文沿用了 SIMPLER、IRASim、WorldEval、EnerVerse-AC、WorldGym 等相关工作语境，并在 public RoboArena leaderboard 上评估：使用 WorldGym 中的 off-the-shelf generalist DROID policies，报告 OSCAR rollouts 与官方 BT/Elo ranking 之间的 Pearson correlation 和 MMRV。作者还声称模型在 action following、appearance quality 和 motion consistency 上优于既有 baselines，但摘录未给出具体数值，因此不能引用提升幅度。结论中明确提到训练数据覆盖四种 robot embodiments 加 human hand，这支持其 cross-embodiment 叙事。证据边界在于：我们还需要看到视频生成指标、人工评价协议、RoboArena 相关性的具体数值，以及 closed-loop policy evaluation 是否真的能替代真实执行。

#### ⚠️ 风险 / 保留意见

- 2D skeleton 可能丢失力、接触、夹爪状态和深度约束，生成结果未必能完整反映执行可行性。
- policy evaluation 依赖 VLM 或人类判断时，评价噪声和偏差可能被误认为 world model 能力。
- 跨 embodiment 泛化主张需要看具体机器人差异，四种机器人加人手仍可能不足以覆盖真实硬件空间。

#### 💭 结论与启发

OSCAR 对系统设计的启发是：world action model 的接口设计可能比模型 backbone 更重要。一个统一、低纹理、几何化的动作条件可以让视频模型避开 embodiment 外观绑定，为多机器人 policy evaluation 提供共同语言。后续复现可以从小规模 skeleton-conditioned video prediction 做起，重点不必先追大模型，而是评估动作条件是否真的在像素位置和时间上被遵守。选题上，这篇适合和 Sim2Real policy evaluation、VLM-as-judge、closed-loop imagination 结合阅读。

#### 🔎 读 PDF 先核查

- 2D kinematic skeleton 如何编码夹爪开合、接触意图和末端执行器差异？
- OSCAR 与 RoboArena BT/Elo ranking 的相关性是否在不同任务类别和不同 policy family 上都稳定？
- 模型生成错误会如何影响 downstream policy selection，是否存在偏好某类外观合理但物理错误轨迹的风险？

#### 📌 上传 PDF 后优先看

- 数据标准化、过滤和去重管线章节
- 2D skeleton rendering 条件表示与模型训练章节
- RoboArena policy evaluation、Pearson/MMRV 结果和人工/VLM 评价协议

### [4]. VISTA: Vision-Grounded and Physics-Validated Adaptation of UMI data for VLA Training [[HTML]](https://arxiv.org/html/2606.04708) [[PDF]](https://arxiv.org/pdf/2606.04708) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.04708`
* **Authors**: Siyuan Yang, Linzheng Guo, Ouyang Lu, Zhaxizhuoma, Daoran Zhang, Xinmiao Wang, Ting Xiao, Fangzheng Yan, Zhijun Chen, Yan Ding, Chao Yu, Chenjia Bai, Xuelong Li
* **Author Priority**: Standard
* **一句话结论**: 值得优先看：VISTA 把 UMI 数据进入 VLA 训练前的视觉域偏移和物理可执行性问题拆开处理，是非常实用的数据适配论文。
* **关键词**: `UMI data` `VLA training` `fisheye vision` `physical validation` `Sim2Real`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

UMI 和 FastUMI 让人类用手持 gripper 大规模采集真实操作数据成为可能，但这些数据直接喂给大规模 VLA 会遇到两个强 mismatch。第一是视觉 mismatch：wrist-mounted fisheye camera 带来严重径向畸变、非均匀空间分辨率和局部 gripper-centric 视角，而许多 VLM/VLA backbone 预训练在标准视角图像上。第二是物理 mismatch：人类采集的末端轨迹不一定满足目标机器人的运动学限制、碰撞约束或控制器带宽，直接模仿可能教会策略不可执行动作。这个问题对 Sim2Real 和 VLA 扩展都很重要，因为 UMI 数据规模化的吸引力正来自低成本采集；如果数据不能被 VLA 稳定消化，规模优势会被 domain gap 和物理不可行性抵消。VISTA 的动机就是在数据进入 VLA 训练前，先做 vision-grounded 和 physics-validated adaptation。

#### ⚙️ 核心方法

VISTA 研究 language-conditioned manipulation policies from UMI-style demonstrations。每个时间步，策略接收自然语言指令、左右 wrist-mounted fisheye camera 视图，以及 proprioceptive robot state，输出一个未来 action chunk。论文把原始 UMI 数据的问题建模为两类不满足标准 VLA 预训练假设：视觉观察不在 VLM 预训练域内，动作标签不一定是目标机器人可执行动作。对应地，VISTA 引入 UMI-VQA 来做 fisheye-aligned visual grounding，使模型在训练中学习 wrist fisheye 视角下的物体、空间和任务相关视觉理解；同时引入 trajectory physical validation，对轨迹的运动学可行性、碰撞风险和 replay fidelity 进行评分或筛选，从而避免把不可执行动作当成监督信号。摘录还提到有 model-level architecture components，但未完整展开，因此只能确认其包含数据级视觉监督、物理验证分数，以及完整 VISTA 系统对 VLA baseline 的评估。新意在于它不把 UMI 当成普通 demo dataset，而是把视觉域适配和机器人可执行性验证作为 VLA 数据工程的必要阶段。

#### 📊 实验与结果

实验按三层组织，逻辑较清楚。第一层是 diagnostic validation：验证两个核心挑战是否真实存在，即 state-of-the-art VLM/VLA 在 wrist-mounted fisheye observations 下显著退化，以及大量 raw UMI trajectories 因运动学不可行、碰撞风险或 replay fidelity 差而无法在目标 embodiment 上忠实 replay。第二层是 data-level validation：验证 UMI-VQA 与 action data co-training 比 generic VQA supervision 更有利于 downstream policy，同时 physical-validation scores 与真实部署成功有强预测关系。第三层是 model-level validation：在 UMI-style simulation benchmarks 和 20 个多样真实操作任务上，将完整 VISTA 与强 VLA baselines 对比，并做关键组件消融。摘录没有具体成功率或相关系数，因此只能引用任务数量和实验层级，不能写具体提升幅度。

#### ⚠️ 风险 / 保留意见

- physical validation score 是否能跨机器人、任务和控制器稳定预测真实成功，还需要看具体定义和相关性数值。
- UMI-VQA 的标注或生成方式会影响视觉 grounding 质量，可能引入语言偏差。
- 如果过滤过强，可能丢掉困难但有价值的恢复轨迹；如果过滤过弱，又会保留不可执行动作。

#### 💭 结论与启发

VISTA 的启发非常直接：VLA 数据扩展不能只讨论采集规模，还要讨论“数据是否适合被某个机器人执行”。后续做 UMI 或人类示教数据时，应把相机模型、视角畸变、动作 replay、碰撞检查和控制带宽放到训练前验证流程中。复现上可以先构建一个小型 physical validation pipeline，把轨迹按可执行性分层，再比较 full BC、filtered BC 和加权训练。它也提醒我们，很多 VLA 失败不是模型架构问题，而是数据接口与目标 embodiment 没有对齐。

#### 🔎 读 PDF 先核查

- UMI-VQA 的问题答案来自人工标注、自动生成还是 VLM 伪标注，如何避免把错误视觉理解注入 VLA？
- trajectory physical-validation score 具体由哪些运动学、碰撞和 replay fidelity 指标组成？
- 20 个真实任务中，VISTA 的收益主要来自视觉 grounding、轨迹过滤/加权，还是模型结构组件？

#### 📌 上传 PDF 后优先看

- UMI-VQA 构建与 fisheye visual grounding 章节
- trajectory physical validation 指标、阈值和 replay 设置章节
- 20 个真实任务主结果、数据级消融和模型级消融

### [5]. Potential-Guided Flow Matching for Vision-Language-Action Policy Improvement [[HTML]](https://arxiv.org/html/2606.04968) [[PDF]](https://arxiv.org/pdf/2606.04968) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.04968`
* **Authors**: Yunpeng Mei, Jiakai He, Hongjie Cao, Chenyu Wang, Xiaowen Zhu, Yihan Zhou, Jiamin Wang, Chenbo Xin, Peng Cheng, Yuxuan Yang, Yijie Wang, Xinhu Zheng, Gao Huang, Jie Chen, Gang Wang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看：ForesightFlow 用同一个 flow policy 生成动作和 success potential，给混合质量 VLA 经验利用提供了比完整 critic 更轻的路线。
* **关键词**: `flow matching` `VLA policy improvement` `success potential` `mixed-quality experience` `offline RL`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

许多 VLA policy 已经被建模为对 action chunks 的条件生成模型，flow matching 因训练稳定、能表达连续动作分布而受到关注。但机器人部署后得到的数据往往质量混杂：成功示范、部分完成、可恢复错误和彻底失败混在一起。全量 BC 会模仿失败，filtered BC 会丢掉失败前的有用片段和恢复信息，offline RL 虽能利用奖励结构，却通常需要额外大 critic，训练和调参成本高。ForesightFlow 问的问题很具体：生成式 VLA policy 自己能否提供类似 critic 的 foresight？如果每个生成的 action chunk 同时带有一个 success-potential 轨迹，那么模型就能在不引入独立价值网络的情况下，对候选动作进行自评分和改进。这对 RL + VLA 很重要，因为它把价值判断嵌入 action generation 本身，可能更适合大模型 action head 的后训练。

#### ⚙️ 核心方法

ForesightFlow 在混合质量数据上 fine-tune VLA flow policy，包含四个成分：augmented action-potential endpoint、stage-level success-potential targets、decoupled advantage-weighted flow matching，以及 self-guided best-of-N inference。标准 flow VLA 学的是给定上下文下 action chunk 的条件分布；ForesightFlow 把 endpoint 扩展为动作加 success-potential vector，且 potential 与动作 horizon 对齐。这个 potential 不是独立 critic network，而是同一个 flow endpoint 的额外生成坐标，可理解为每个局部片段位于成功任务轨迹上的条件可能性。训练时，stage-level targets 提供潜在成功监督；decoupled advantage-weighted flow matching 用 advantage 权重选择性强化更好动作，同时避免把 value hallucination 直接耦合进动作监督。推理时，策略可以生成多个候选 action chunks，并用自身生成的 potential 平均分数做 best-of-N 选择。摘录还提到 one-step CFM boundary estimator 用于保持 advantage 计算成本接近 supervised flow matching；具体公式、NFE 设置和权重细节需核查全文。

#### 📊 实验与结果

实验围绕四个问题展开：是否优于 full BC、filtered BC 和 flow/offline-RL baselines；decoupled weighting 是否防止 value hallucination；one-step foresight 是否保留高 NFE integration 的排序信息；self-guided best-of-N inference 是否提升长程执行。模拟实验使用 OmniGibson 中 BEHAVIOR-1K 的 5 个任务，Galaxea R1 Pro humanoid embodiment，任务包括 Turning on radio、Picking up trash、Spraying fruit trees、Cook hot dogs、Wash a baseball cap，覆盖双臂协调、articulated-object interaction、mobile manipulation 和长程序列。指标包括 success rate 和 normalized Q-Score，后者捕捉 stage-wise progress。摘录还提到真实机器人在 DexTeleop TeleAvatar Lite 双臂平台上评估，但具体任务和数值被截断，因此只能确认存在 real-world evaluation，不能写性能幅度。

#### ⚠️ 风险 / 保留意见

- success potential 由数据分布学习，若混合数据标签或阶段边界不可靠，模型自评分可能偏置。
- best-of-N 推理会增加采样成本，长程任务中候选动作评分错误可能累积。
- 没有完整摘录到真实机器人任务和数值，难以判断 sim 到 real 的稳健性。

#### 💭 结论与启发

这篇适合用于思考 VLA 后训练的轻量替代 critic 方案。它的关键价值在于把“动作生成”和“动作好坏估计”放进同一个 flow endpoint，使混合质量经验不必在 full BC 和 hard filtering 之间二选一。复现上，可以先在已有 diffusion/flow action policy 中增加一个 horizon-aligned scalar head，比较 full BC、filtered BC、advantage-weighted 和 best-of-N 的差异。系统上，它也提示部署日志应包含 stage progress 或 success boundary，否则 potential target 很难可靠构造。

#### 🔎 读 PDF 先核查

- stage-level success-potential targets 是如何从 mixed-quality trajectories 中构造的，是否需要人工阶段标注？
- decoupled advantage-weighted flow matching 如何具体阻止 potential hallucination 影响动作学习？
- self-guided best-of-N 的收益是否随 N 增长稳定，还是主要来自额外采样预算？

#### 📌 上传 PDF 后优先看

- Action-Potential Flow State 与 potential target 构造章节
- decoupled advantage-weighted flow matching 和 boundary estimator 章节
- BEHAVIOR-1K、真实双臂平台结果与 best-of-N 消融

### [6]. GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors [[VIP]] [[HTML]](https://arxiv.org/html/2606.05160) [[PDF]](https://arxiv.org/pdf/2606.05160) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.05160`
* **Authors**: Tianyi Xie, Haotian Zhang, Jinhyung Park, Zi Wang, Bowen Wen, Jiefeng Li, Xueting Li, Qingwei Ben, Haoyang Weng, Yufei Ye, David Minor, Tingwu Wang, Chenfanfu Jiang, Sanja Fidler, Jan Kautz, Linxi Fan, Yuke Zhu, Zhengyi Luo, Umar Iqbal, Ye Yuan
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看：GRAIL 用 3D assets 和 video foundation model priors 生成 humanoid loco-manipulation 数据，是人形机器人 Sim2Real 数据扩展的高价值路线。
* **关键词**: `humanoid loco-manipulation` `3D assets` `video priors` `Sim2Real` `Yuke Zhu`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

人形机器人 loco-manipulation 的难点在于数据必须同时满足全身平衡、物体接触、场景几何和目标机器人可执行性。遥操作和动捕能提供高质量 demonstrations，但每换一个物体或地形都可能需要真实环境重搭、演员或机器人采集，难以规模化。直接从野外视频重建 robot-ready 4D trajectories 虽然视觉覆盖广，但会遭遇尺度、相机、遮挡、物体几何和机器人形态不匹配等问题。GRAIL 的动机是反过来做：不从无约束视频恢复世界，而是从已知 3D assets 和 simulator-ready scene 出发，再利用 video foundation models 的人类交互先验合成参考视频。这样，物体几何、纹理、相机参数、metric scale、环境深度和 robot-proportioned morphology 都可控，为后续重建和 retarget 提供 privileged setup。这对 Sim2Real 很重要，因为它把数据生成的大部分不确定性留在虚拟环境内，只在部署时接触真实机器人。

#### ⚙️ 核心方法

GRAIL 输入一个 3D object asset，输出 humanoid loco-manipulation demonstrations，包括 humanoid kinematic motion、object kinematic motion 和 robot actions。管线分三步。第一步，组装完整 3D configuration：角色预先适配目标机器人，场景和物体已知，渲染初始帧后交给 VFM 合成 reference human-object interaction video。作者选择先生成人类视频而不是机器人视频，因为当前 VFM 对人类操作有更强先验，人手和人体重建工具也更成熟。第二步，利用已知 3D configuration 进行 4D HOI trajectory reconstruction，包括 human pose estimation、object tracking 和 joint optimization，以得到更连贯的交互轨迹。第三步，把重建运动 retarget 到目标 humanoid，并在每个 task family 上训练 task-general tracking policies。最后，作者还用生成数据训练 egocentric visual policies，经 sim-to-real pipeline 部署到真实 Unitree G1 上做 pick-up 和 stair-climbing。当前摘录能确认这些阶段和接口，但不能确认 VFM 名称、优化目标公式、tracking policy 架构或 sim-to-real 随机化细节。

#### 📊 实验与结果

实验覆盖 GRAIL 管线三阶段。首先评估生成的 4D HOI sequences 是否比既有 generation baselines 更物理可执行；对比包括 training-based 的 CHOIS、HOIDiff，以及 training-free 的 DAViD，在来自 ComAsset 的 20 个 everyday objects 共享评估集上进行。指标分为几何质量、物理/可执行性等轴线，摘录中明确提到 contact distance 和 penetration ratio，但具体公式细节和结果数值不完整，因此不能写具体排名或提升。其次，论文评估这些 4D HOI sequences 能否规模化转成 task-general loco-manipulation policies，而不只是逐条轨迹 replay。最后，作者展示生成数据的实际价值：训练 egocentric visual policies，并在真实 Unitree G1 上进行 autonomous loco-manipulation，包括 pick-up 和 stair-climbing。真实部署存在但摘录未给成功率。

#### ⚠️ 风险 / 保留意见

- VFM 对人类交互的先验可能生成视觉合理但物理或接触细节不可靠的视频，需要看优化和过滤如何处理。
- 从人类 HOI 到 humanoid robot 的 retarget 可能在手部、关节限制、足底接触和动态平衡上产生误差。
- 真实 Unitree G1 任务覆盖 pick-up 和 stair-climbing，仍需确认是否能扩展到更复杂多物体长程任务。

#### 💭 结论与启发

GRAIL 的最大启发是把“视频先验”放在可控 3D 场景中使用，而不是盲目相信野外视频重建。对于人形机器人，数据生成应尽量让几何、尺度和目标 morphology 从一开始就已知，再借助 VFM 补足动作多样性和交互先验。后续复现可以从单物体 pickup 的 asset-to-video-to-retarget 小闭环开始，重点验证生成 HOI 的接触质量和 retarget 后的动态可执行性。选题上，它把 world model、数字孪生、Sim2Real 和 humanoid VLA 数据生成连接得很紧。

#### 🔎 读 PDF 先核查

- VFM 生成的 reference HOI video 如何被约束在已知 3D scene 内，避免与物体几何和尺度冲突？
- joint optimization 在 human pose、object tracking 和接触一致性之间如何权衡？
- Unitree G1 真实部署中，视觉策略对未见物体、地形和接触失败的鲁棒性如何？

#### 📌 上传 PDF 后优先看

- robot-centric human video generation 与 3D scene setup 章节
- 4D HOI reconstruction、joint optimization 和 retargeting 章节
- ComAsset 对比、task-general tracking policy 结果和 Unitree G1 Sim2Real 部署实验

## Watchlist

### [W1]. CLAW: Learning Continuous Latent Action World Models via Adversarial Latent Regularization [[HTML]](https://arxiv.org/html/2606.04130) [[PDF]](https://arxiv.org/pdf/2606.04130)
* **Paper ID**: `2606.04130`
* **Authors**: Tewodros Ayalew, Matthew Jeung, Samuel Wheeler, Xiao Zhang, Andre de la Cruz Arce, Kaylene Stocking, Michael Maire, Matthew R. Walter
* **Author Priority**: Standard
* **为什么还值得留意**: CLAW 进入 watchlist 是因为它直接对准 action-free video 中的 continuous latent action world model，并用 adversarial latent regularization 处理信息泄漏问题，和 World Model / World Action Model 主线高度相关。它没有进入最终精选，主要因为当前摘录显示其重点偏自监督表示、视觉规划和 controllability benchmark，缺少 VIP 作者和大规模真实机器人/VLA 部署证据。后续值得核查其 14 个任务上的 planning 结果、与 AdaWorld/LAPO 的差异，以及 latent action 是否真的可迁移到机器人控制。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. What Are We Actually Benchmarking in Robot Manipulation? [[HTML]](https://arxiv.org/html/2606.04233) [[PDF]](https://arxiv.org/pdf/2606.04233)
* **Paper ID**: `2606.04233`
* **Authors**: Tianchong Jiang, Xiangshan Tan, Samuel Wheeler, Luzhe Sun, Tewodros W. Ayalew, Matthew Walter
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇 benchmark audit 很值得保留，因为它提醒 LIBERO、CALVIN、SimplerEnv、RoboCasa、RoboTwin 2.0 等 manipulation benchmark 的分数可能受到 shortcut、统计显著性、过拟合和数据源依赖影响。没有进入最终精选，是因为它不是 VLA/World Model 方法论文，也不直接提出新训练系统。它对阅读今天其他论文很重要：凡是依赖 LIBERO 或 RoboCasa 的结果，都应回头用这篇的诊断框架审视。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

### [W3]. 3DThinkVLA: Endowing Vision-Language-Action Models with Latent 3D Priors via 3D-Thinking-Guided Co-training [[HTML]](https://arxiv.org/html/2606.04436) [[PDF]](https://arxiv.org/pdf/2606.04436)
* **Paper ID**: `2606.04436`
* **Authors**: Jiaxin Shi, Xidong Zhang, Fucai Zhu, Zhe Li, Siyu Zhu, Weihao Yuan
* **Author Priority**: Standard
* **为什么还值得留意**: 3DThinkVLA 进入 watchlist 是因为它试图把 3D geometry perception 和 high-level spatial reasoning 分层注入 VLA，并且部署时不需要额外 3D sensor 或辅助模型。没有进入最终精选，主要因为它依赖 LIBERO、LIBERO-PLUS、SimplerEnv 等模拟 benchmark，且当前摘录中缺少真实机器人证据；考虑到 benchmark audit 的警示，需要谨慎看待 100% suite success 这类结果。后续应重点核查 3D foundation model 蒸馏、reasoning anchor token 和 zero-shot transfer 的消融。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. WAM-Nav: Asymmetric Latent World-Action Modeling for Unified Visual Navigation [[HTML]](https://arxiv.org/html/2606.04907) [[PDF]](https://arxiv.org/pdf/2606.04907)
* **Paper ID**: `2606.04907`
* **Authors**: Ning Yang, Yan Huang, Kaiwen Peng, Ziheng He, Kai Wang, Cui Miao, Kailin Lyu, Guo Li, Xiaofeng Wang, Zheng Zhu, Jing Liu, Nianfeng Liu
* **Author Priority**: Standard
* **为什么还值得留意**: WAM-Nav 进入 watchlist 是因为它把 latent world-action modeling 用到统一视觉导航，强调 action generation 与 latent visual foresight 的共享生成框架，和 World Action Model 主题相邻。它没有进入最终精选，是因为任务域主要是 navigation 而不是 manipulation/VLA policy improvement，且摘录显示训练依赖 VLN-N1 的仿真导航数据。后续可关注它的 zero-shot real-world navigation、实时性和 asymmetric action-foresight 设计是否能迁移到移动操作。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
