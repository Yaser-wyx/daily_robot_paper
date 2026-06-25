# RoboPulse | 2026-06-25

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 92 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线非常清晰：机器人 VLA 正在从“单步语义到动作映射”转向带记忆、带系统识别、带动作先验和可在线强化的长期控制系统。最终精选覆盖了三条关键路径：长时记忆检索与导航记忆、LLM/scene graph 分层规划、以及 VLA 后训练中的 RL、world model 与 cross-embodiment action prior。VIP 作者上，Yuke Zhu 参与的 HALO、Hao Su 参与的 SAGE-Nav，以及扩展名单里的 Dhruv Shah 参与的 RAVEN 最值得优先跟踪；Danfei Xu 的 GRAFT 虽在 watchlist，但对几何 affordance transfer 也值得后续补读。整体判断是：今天不是单一大模型 scaling 的日子，而是“如何把基础模型变成可部署机器人系统”的方法密集出现。

## 今日信号

- VLA 的瓶颈正在从语义理解转向长期状态、执行延迟、动作分布和环境配置这些更贴近机器人闭环部署的问题。
- 记忆系统出现两条互补路线：HALO 把检索监督蒸馏进低层 visuomotor policy，RAVEN 则把视觉 embedding、位姿和时间外置成可查询的长期导航记忆。
- RL/VLA 后训练开始强调稳定过渡和稠密监督，FORCE 与 ROAD-VLA 都在处理 sparse reward 对高维 action policy 不够用的问题，但最终精选更偏向有完整三阶段框架和真实机器人验证线索的 FORCE。

## Historical Rediscovery

- **Paper**: World Value Models for Robotic Manipulation [[PDF]](https://arxiv.org/pdf/2606.24742)
  - **Paper ID**: `2606.24742`
  - **来源日期**: 2026-06-24
  - **当时可能被低估的信号**: 当时因为只有摘要回退而降权，但 watchlist note 已经指出其核心信号是 generalist robotic value estimation，以及把 historical belief grounding 和 future outcome planning 转成 value prediction。
  - **为什么现在值得再看**: 如果你现在关注 World Action Model 或 RL+VLA，这篇可能提供一个把视觉语言状态、未来结果和价值函数连接起来的切口，值得优先核查其训练信号、benchmark 和相对静态 VLM value model 的增益。
  - **建议动作**: 加入精读
  - **关键词**: `World Model` `Value Model` `Robotic Manipulation` `RL` `Planning`
- **Paper**: Wh0: Generative World Models as Scalable Sources of Egocentric Human Hand Manipulation Data [[HTML]](https://arxiv.org/html/2606.22136) [[PDF]](https://arxiv.org/pdf/2606.22136)
  - **Paper ID**: `2606.22136`
  - **来源日期**: 2026-06-24
  - **当时可能被低估的信号**: 当时被视为数据生成与 post-training 案例而未精选，但候选信息里已有 50k WM-H、Unitree G1、Inspire dexterous hands、18 tasks、每任务 20 trials，以及 VITRA 从 8.3% 到 38.9% 的提升信号。
  - **为什么现在值得再看**: VLA 和 World Model 的交叉正在从“模型能否预测”转向“能否生成可训练、可迁移的交互数据”；这篇正好值得作为 sim-to-real 数据桥和 dexterous policy post-training 案例重看。
  - **建议动作**: 加入精读
  - **关键词**: `Generative World Model` `Dexterous Manipulation` `VLA Data` `Sim2Real` `Egocentric Data`
- **Paper**: G$^3$VLA: Geometric inductive bias for Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2606.24472) [[PDF]](https://arxiv.org/pdf/2606.24472)
  - **Paper ID**: `2606.24472`
  - **来源日期**: 2026-06-24
  - **当时可能被低估的信号**: 当时因为看起来更像模块增强而被压低排序，但候选记录里的 intrinsic-conditioned ray embeddings、PRoPE、cross-view fusion 和 point-map distillation 是很具体的几何归纳偏置信号。
  - **为什么现在值得再看**: 如果你关注真实部署评测和 VLA 的空间泛化，这篇值得重看 LIBERO、RoboCasa24、RoboTwin2.0 与真实机器人结果，判断几何注入是否能成为 VLA/WAM 的稳定底层模块。
  - **建议动作**: 加入精读
  - **关键词**: `VLA` `Geometry` `Multi-view` `Robot Manipulation` `Real Robot`
- **Paper**: SkyJEPA: Learning Long-Horizon World Models for Zero-Shot Sim-to-Real Control of Quadrotors [[HTML]](https://arxiv.org/html/2606.23444) [[PDF]](https://arxiv.org/pdf/2606.23444)
  - **Paper ID**: `2606.23444`
  - **来源日期**: 2026-06-24
  - **当时可能被低估的信号**: 当时因 aerial robotics 与 manipulation/VLA 主线不完全一致而未精选，但 latent dynamics、physics-inspired prober、onboard closed-loop control 和 robustness 实验都被记录为后续值得核查的具体信号。
  - **为什么现在值得再看**: 对 World Model 和真实闭环部署来说，跨域的 long-horizon latent prediction 与 zero-shot sim-to-real 控制经验可能可迁移到移动操作、视触觉世界模型或更强的 action-conditioned prediction。
  - **建议动作**: 快速浏览
  - **关键词**: `Long-horizon World Model` `JEPA` `Zero-shot Sim2Real` `Closed-loop Control` `Robustness`
- **Paper**: PokeVLA: Empowering Pocket-Sized Vision-Language-Action Model with Comprehensive World Knowledge Guidance [[HTML]](https://arxiv.org/html/2604.20834) [[PDF]](https://arxiv.org/pdf/2604.20834)
  - **Paper ID**: `2604.20834`
  - **来源日期**: 2026-04-27
  - **当时可能被低估的信号**: 当时被归类为工程型强作而非最强研究信号，但候选记录中已有两阶段训练范式、世界知识/空间感知注入、LIBERO/LIBERO-Plus 评测等可复查线索。
  - **为什么现在值得再看**: 如果今天要评估 VLA 从大模型原型走向可部署策略，这篇可能比纯扩模路线更有参考价值，也能补充 World Knowledge 与 action policy 结合的轻量路线。
  - **建议动作**: 继续跟踪
  - **关键词**: `VLA` `Efficient Deployment` `World Knowledge` `Spatial Perception` `LIBERO`

## Editor's Picks

### [1]. Memory Retrieval in Visuomotor Policies for Long-Horizon Robot Control [[VIP]] [[HTML]](https://arxiv.org/html/2606.25136) [[PDF]](https://arxiv.org/pdf/2606.25136) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.25136`
* **Authors**: Rutav Shah, Yisu Li, Femi Bello, Yuke Zhu, Roberto Martín-Martín
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看：HALO 直接瞄准长时部分可观测操作中的“该从过去取什么信息”问题，并把 VLM 生成的 VQA 监督接入 visuomotor imitation learning。
* **关键词**: `visuomotor memory` `VQA supervision` `long-horizon manipulation` `imitation learning` `partial observability`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

家庭机器人做长时任务时，当前图像往往不包含完成动作所需的信息：物体先前放在哪、某个容器原本对应哪个盘子、已放入多少物品、某个电器何时开启等。纯反应式策略在这类部分可观测任务上天然不足，而手写记忆或启发式检索又依赖任务假设，难以覆盖空间、关系、数量、事件时间和协作状态等多种记忆类型。Transformer 长上下文注意力看似能解决，但在 imitation learning 中仅靠动作损失学习检索，容易抓住训练集里的伪相关。HALO 的价值在于把“记忆检索”作为 policy 内部能力单独塑形，而不是只把历史帧堆进模型。

#### ⚙️ 核心方法

HALO 的核心是给 visuomotor policy 加入可学习的历史检索机制，并用 VLM 生成的视频问答信号去监督这个检索过程。摘录中可以确认，方法将历史轨迹编码、当前观测 embedding 和问题文本一起输入 policy backbone，通过 VQA head 预测答案；这些问题覆盖物体位置、物体关系、事件顺序、子目标进度等任务相关信息。训练时并不是只做 VQA，而是把 VQA 监督与动作预测共同训练：VLM 的语义先验用于提示“过去哪些信息可能重要”，imitation learning 的动作目标则把这些先验重新落到低层控制所需的状态上。相对普通端到端 IL，HALO 的新意在于检索目标不再完全由最终 action loss 间接反传决定，而有一条显式、可解释的中间监督；相对纯 VLM 记忆，它又没有停留在问答层，而是把检索偏置蒸馏到可执行的 visuomotor policy 中。

#### 📊 实验与结果

实验围绕长时操作中的多类型记忆需求设计。HTML 摘录明确列出五类场景：Retrieve Object 测空间位置记忆，Return to Same Container 测对象关系，Store Objects 测数量累计，另有事件时间和人机协作相关任务。任务都强调当前观测不再包含关键信息，policy 必须从历史交互中取回。论文结论称 HALO 通过 VLM 生成的 VQA 监督缓解了训练中的伪相关，并提升长时 imitation learning 的记忆检索能力。当前摘录没有给出具体成功率、对比表数字或消融幅度，因此只能确认其评估覆盖了空间、关系、数量、事件时间等维度，不能据此判断提升幅度是否在所有任务上稳定。

#### ⚠️ 风险 / 保留意见

- VQA 对生成质量敏感，问题是否真正覆盖控制所需因果信息会直接影响检索学习。
- 如果历史很长或场景变化频繁，检索模块的计算与记忆容量边界需要核查。
- 摘录未提供具体数值，真实机器人泛化强度和消融可靠性需要看完整实验。

#### 💭 结论与启发

这篇最值得借鉴的是把 VLM 从“直接输出动作”退回到“为策略提供检索监督”的位置。对后续系统设计而言，可以把长时机器人任务拆成三层：历史存储、任务相关检索、动作闭环执行；其中检索层需要独立训练信号，否则容易被 action loss 带偏。复现时我会优先做小规模多类型记忆 benchmark，验证 VQA 监督是否真的提升了检索正确性，而不仅是最终成功率。

#### 🔎 读 PDF 先核查

- VQA pairs 是如何生成和筛选的，是否有机制避免 VLM 提供与动作无关或错误的问题答案？
- 检索模块在动作预测时具体返回哪些历史 token 或 embedding，是否能被可视化验证其关注了正确时间段？
- HALO 相比只加长上下文 Transformer 的收益，主要来自 VQA 监督、架构设计，还是训练数据覆盖差异？

#### 📌 上传 PDF 后优先看

- VQA 监督数据生成与训练目标章节
- 长时记忆任务定义和评估协议章节
- 检索消融、错误案例与真实机器人结果章节

### [2]. RAVEN: Long-Horizon Reasoning & Navigation with a Visuo-Spatio-Temporal Memory [[VIP]] [[HTML]](https://arxiv.org/html/2606.25206) [[PDF]](https://arxiv.org/pdf/2606.25206) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.25206`
* **Authors**: Yixun Hu, Zhicheng Zheng, Lihan Zha, Chunwei Xing, Rajdeep Singh, Omar Hossain, Antonio Loquercio, Dhruv Shah
* **Author Priority**: Extended VIP
* **一句话结论**: 值得优先看：RAVEN 把长期机器人记忆做成视觉 embedding、空间位姿和时间索引的系统，比 caption memory 更适合开放词汇导航问答。
* **关键词**: `robotic memory` `visual embeddings` `spatio-temporal retrieval` `navigation QA` `vector database`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

长期部署机器人需要记住过去看过什么、在哪里看到、什么时候看到，并能根据自然语言查询导航回去。传统语义地图依赖封闭类别，难以回答“蓝色帽子上有粉色蝴蝶结”这类细粒度视觉描述；原始视频虽然信息完整，但存储和检索成本过高；把图像先 caption 成文本又会丢掉二级物体、颜色、局部属性等细节。RAVEN 的问题意识很系统：机器人长期记忆不能只存标签，也不能只存视频，而要同时保留视觉语义、空间 grounding 和时间线索。它进入精选是因为这条路线直接连接 VLA/agentic memory 与实际导航部署。

#### ⚙️ 核心方法

RAVEN 构建的是外置的 visuo-spatio-temporal memory。摘录可以确认，它把视觉 embedding 与机器人 pose、时间一起写入 vector database，并把检索结果 grounding 到空间地图中，用于回答问题或导航到目标位置。方法强调直接在视觉 embedding 上检索，而不是先 caption 再检索，从而减少图像到文本压缩带来的细节损失。论文还系统比较了不同 embedding 训练范式，包括 contrastive 模型、autoregressive 多模态模型、自蒸馏视觉模型、闭源 embedding 模型，以及 random retriever baseline。这说明 RAVEN 不是只提出一个 memory wrapper，而是在研究“什么视觉表征适合机器人长期记忆”。推理时，用户查询会在 embedding bank 中找相关历史观测，再结合空间地图确定位置或生成导航目标。相对 caption-based memory，它的新意在于把开放词汇语义保留在高维视觉表征里，并用位姿和时间把它变成可行动的机器人记忆。

#### 📊 实验与结果

实验围绕三件事展开：视觉 embedding 是否比 caption 保留更多细节，记忆长度扩展到数千帧时检索是否仍可靠，以及系统是否能迁移到物理机器人。摘录明确提到评估基准包括 NaVQA、FindingDory 和自建的 RAVEN-QA。NaVQA 基于真实城市机器人导航数据，覆盖描述、空间和时间查询；FindingDory 是 Habitat 中基于记忆的单目标或多目标导航 benchmark；RAVEN-QA 被描述为更具挑战性的导航问答集合。结论称 RAVEN 持续优于 caption-based baselines 和 VLM-only approaches，尤其在二级物体和细微视觉特征回忆上更强。当前摘录没有具体指标数值，因此应把该结论视为方向性证据，需在 PDF 中核对各基准的提升幅度。

#### ⚠️ 风险 / 保留意见

- 外置 vector memory 的性能依赖 embedding 模型，换场景或换相机后可能需要重新评估。
- 长期部署中的地图漂移、重复场景和动态物体会影响 pose-time grounding。
- 结论声称优于 caption/VLM-only，但摘录未给出统计显著性或失败模式。

#### 💭 结论与启发

RAVEN 对我的启发是：机器人记忆不一定要压进 policy 参数，也可以作为可增长、可检索、可空间化的系统组件存在。对于导航和移动操作，embedding memory 加 spatial map 可能比端到端长上下文更可维护，也更容易调试。后续阅读应重点关注它如何处理检索到导航目标的接口，因为这决定了它能否从 QA 系统变成真正的行动系统。

#### 🔎 读 PDF 先核查

- RAVEN 如何把自然语言查询映射到视觉 embedding 检索空间，是否需要额外 query encoder 或 prompt engineering？
- 当检索结果包含多个相似地点时，系统如何利用时间和空间地图消歧并选择导航目标？
- 不同 embedder 的比较是否控制了存储规模、检索延迟和输入分辨率等系统变量？

#### 📌 上传 PDF 后优先看

- memory representation 与 vector database 设计章节
- NaVQA、FindingDory、RAVEN-QA 对比实验章节
- 真实机器人部署、检索失败案例和延迟/规模分析章节

### [3]. SAGE-Nav: Leveraging LLM Planning and Alignment Fusion for Hierarchical Scene Graph-Guided Navigation [[VIP]] [[PDF]](https://arxiv.org/pdf/2606.25497) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.25497`
* **Authors**: Hao Su, Yuehao Huang, Yukai Ma, Yong Liu, Jiajun Lv
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看但要保守：SAGE-Nav 只有摘要回退信息，不过它把 LLM 分层规划、动态 scene graph 和高频控制解耦，正中长时 ObjNav 关键痛点。
* **关键词**: `Object-Goal Navigation` `LLM planning` `scene graph` `hierarchical control` `semantic waypoints`
* **证据来源**: Abstract fallback

#### 📖 背景与动机

Object-Goal Navigation 要求智能体只靠第一视角视觉在未知或新环境中找到目标。单体式策略通常把感知、语义推理、路径选择和低层控制压在一个网络里，面对长时搜索、房间级语义关系和环境泛化时容易失效。摘要指出现有 monolithic methods 在 long-horizon reasoning 上困难，且对新环境泛化不佳。SAGE-Nav 的动机是把“慢速语义规划”和“快速反应控制”分开：LLM 负责抽象推理和 waypoint 分解，scene graph 负责动态环境结构表示，控制环则保持高频执行。这与今天多篇论文的系统化趋势一致。

#### ⚙️ 核心方法

当前摘录只能确认 SAGE-Nav 是一个 hierarchical framework，将 LLM reasoning 与 dynamic scene graphs 结合，用于 ObjNav。LLM 被设定为 global planner，把抽象目标分解为一系列 semantically grounded waypoints；这一路径规划是异步的，不与高频 reactive control loop 强绑定。为把离散规划变成可用的稠密指导，论文设计了 Hierarchical Scene Graph Encoder，使用 relational graph convolutions 生成结构感知 embedding，并保留 semantic 与 spatial topology。合理推断是，系统会在环境探索过程中维护或更新 scene graph，再由 HSGE 把节点、关系、空间布局编码给导航策略。它的新意不在于单独使用 LLM 或 scene graph，而在于把 LLM 的低频全局规划和图结构的空间语义 grounding 接到可实时执行的控制接口上。由于没有 HTML 正文，具体训练目标、waypoint 表达、图更新频率和控制器形式都不能展开断言。

#### 📊 实验与结果

由于该条只有 abstract fallback，当前只能确认任务域是 Object-Goal Navigation，输入为 egocentric visual observations，目标是提升长时推理与新环境泛化。摘要没有给出 benchmark 名称、环境数量、成功率、SPL 或其他导航指标，也没有说明是否有真实机器人实验。因此实验部分应重点保持保守：它进入精选是因为方法组合与今天关注方向高度相关，且有 Hao Su 这个核心关注作者；但目前不能判断其相对基线的实际优势。上传 PDF 后需要重点核查评估是否覆盖未见环境、长路径目标、语义混淆目标，以及 LLM planner 的调用成本和失败模式。

#### ⚠️ 风险 / 保留意见

- 只有摘要证据，具体算法实现、训练方式和实验强度都无法确认。
- LLM 异步规划可能受 hallucination、延迟和环境图不完整影响。
- scene graph 构建质量会成为系统上限，尤其在遮挡和动态环境中。

#### 💭 结论与启发

SAGE-Nav 值得作为“分层 embodied planning 系统”的候选模板来读。若它的 HSGE 真能把语义图和空间拓扑稳定地转成控制指导，那么它对 VLA 系统也有启发：不要让大模型直接高频控制，而是让它产生低频、可校正的结构化目标。后续我会把它与 RAVEN 对照阅读：一个偏记忆检索，一个偏规划图编码，二者可能能组合成长期导航 agent。

#### 🔎 读 PDF 先核查

- LLM 生成的 semantically grounded waypoints 具体是什么格式，如何映射到可导航空间？
- Hierarchical Scene Graph Encoder 的图节点、边和空间属性如何构造，是否在线更新？
- 异步 global planning 与高频 reactive control 出现冲突时，系统如何仲裁或重规划？

#### 📌 上传 PDF 后优先看

- 系统架构与 planner-controller 解耦章节
- scene graph 构建和 HSGE 编码章节
- ObjNav benchmark、泛化评估和 LLM 调用消融章节

### [4]. FORCE: Efficient VLA Reinforcement Fine-Tuning via Value-Calibrated Warm-up and Self-Distillation [[HTML]](https://arxiv.org/html/2606.26006) [[PDF]](https://arxiv.org/pdf/2606.26006) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.26006`
* **Authors**: Shuyi Zhang, Yunfan Lou, Hongyang Cheng, Yichen Guo, Chuyao Fu, Yaoxu Lyu, Xiaojie Zhang, Haoran Li, Pengwei Wang, Zhongyuan Wang, Shanghang Zhang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看：FORCE 把 VLA RL fine-tuning 的冷启动崩塌和低效探索拆成三阶段解决，是今天 RL+VLA 线最完整的一篇。
* **关键词**: `VLA fine-tuning` `reinforcement learning` `offline-to-online RL` `value calibration` `self-distillation`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

VLA 通常先靠 imitation learning 学会从视觉和语言到动作，但 imitation ceiling 会把策略限制在示范数据质量之内，且长时任务中误差会逐步累积。RL fine-tuning 理论上能突破这个上限，却在机器人上很难：初始 Q-function 不稳定会导致 offline-to-online 转换时 catastrophic unlearning，低质量探索数据又让策略更新效率很低，甚至依赖昂贵的人类干预。FORCE 的重要性在于它不是简单把 PPO 或离线 RL 套到 VLA 上，而是正面处理 VLA 后训练中特有的分布支持不匹配、稀疏反馈和策略更新稳定性问题。

#### ⚙️ 核心方法

FORCE 是三阶段框架，覆盖 offline reinforcement learning、offline-to-online bridge，以及 online fine-tuning。摘录明确指出它先用 Value-Calibrated Warm-Up 或 Distributional Warm-up 扩展 Q-function 在当前策略访问分布上的支持，缓解初始 online rollouts 与离线数据之间的 support mismatch。随后在交互环境中继续强化 fine-tuning，并引入 Value-Guided Policy Distillation 以提升样本效率和稳定性。VGPD 的核心思想是用 value 信号指导策略自蒸馏，把高方差的 RL 更新转成更规则化的 policy improvement 过程，从而避免直接梯度更新带来的不稳定。相对普通 SFT，它尝试突破示范上限；相对直接在线 RL，它在进入在线阶段前校准 value 支持；相对依赖人工 intervention 的方法，它强调 intervention-free convergence。当前摘录没有完整公式细节，因此不能展开具体 Bellman 目标或 distillation loss，只能确认其训练流程和问题分解。

#### 📊 实验与结果

实验设计围绕三项主张：Distributional Warm-up 是否缓解 offline-to-online cold-start collapse，VGPD 是否比标准梯度式 RL 更新更稳定和样本高效，以及 FORCE 是否能在物理环境中无实时人类纠正地适应接触丰富任务。摘录明确使用 ManiSkill 做大规模定量 benchmark，并使用 Franka Emika Panda 做真实机器人验证。论文称在仿真实验中 FORCE 达到 SOTA，并通过扩展 policy support 拉开与 prior baselines 的差距；但摘录没有提供具体表格数值、任务列表或成功率。因此目前可以认可其实验覆盖 simulation + real robot 两级证据，但不能引用提升百分比或判断每类任务是否均匀受益。

#### ⚠️ 风险 / 保留意见

- 三阶段训练流程可能复现成本高，对 reward、Q-function 和 rollout 质量都敏感。
- 真实机器人验证范围在摘录中不明确，不能直接外推到多平台或开放环境。
- VGPD 的稳定性依赖 value calibration，若 value 误差系统性偏置，可能强化错误动作。

#### 💭 结论与启发

FORCE 提供了一个很实用的 VLA 后训练蓝图：先别急着在线 RL，先处理 value 支持和分布桥接，再用蒸馏式更新稳定策略。对复现而言，我会优先验证 warm-up 是否真的减少初期性能塌陷，因为这是机器人在线训练最危险的阶段。对选题而言，它提示 RL+VLA 的论文不应只追求最终成功率，更应报告冷启动曲线、干预需求和每次环境交互的收益。

#### 🔎 读 PDF 先核查

- Value-Calibrated Warm-Up 具体如何利用 on-policy rollouts 校准 Q-function，是否需要真实环境交互？
- VGPD 中 teacher 或 distillation target 如何由 value 信号构造，和标准 policy gradient 的差别有多大？
- FORCE 的样本效率提升是否主要来自 warm-up、VGPD，还是来自三阶段训练预算更多？

#### 📌 上传 PDF 后优先看

- 三阶段训练流程和 value warm-up 目标章节
- VGPD 自蒸馏机制与理论说明章节
- ManiSkill、Franka 实验曲线、消融和无干预设置章节

### [5]. In-Context World Modeling for Robotic Control [[PDF]](https://arxiv.org/pdf/2606.26025) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.26025`
* **Authors**: Siyin Wang, Junhao Shi, Senyu Fei, Zhaoyang Fu, Li Ji, Jingjing Gong, Xipeng Qiu
* **Author Priority**: Standard
* **一句话结论**: 值得优先看但需等 PDF：ICWM 把系统识别放进 VLA context window，用 task-agnostic 自交互推断相机、形态等执行上下文，是 world model 方向的关键信号。
* **关键词**: `in-context world modeling` `system identification` `VLA generalization` `cross-setup adaptation` `world model`
* **证据来源**: Abstract fallback

#### 📖 背景与动机

现代 VLA 常假设训练和部署处在相同系统配置中：相机视角、机器人形态、动作空间和动力学都相对固定。一旦相机移动、机械臂不同或环境设置改变，策略只看当前观测和语言指令，很难知道“自己现在处在什么执行系统里”，因此需要大量 fine-tuning。ICWM 的动机是把系统配置显式视为可推断变量，而不是隐藏在训练分布中。它与传统 in-context learning 的差别也很重要：上下文不是用来告诉模型要做什么任务，而是让模型理解这个系统如何响应动作。

#### ⚙️ 核心方法

当前摘录只能确认 ICWM 即 In-Context World Modeling，将 system identification 表述为 in-context adaptation 问题。它让机器人先进行一小段 self-generated、task-agnostic interactions，并把这段历史作为 context，让 policy 自主推断关键系统变量，再执行目标任务。摘要明确说它不同于用 demonstrations 指定任务的传统 ICL：ICWM 使用 context window 理解“系统如何表现”，例如相机视角、机器人 morphology 或其他执行配置。合理推断是，该框架需要某种世界模型或条件策略，从历史观测-动作-结果中估计隐含系统状态，再把这一估计用于后续控制。但因为没有 HTML 正文，不能断言其模型结构、训练数据、损失函数、是否显式预测未来观测，或是否只在 latent 中建模。它的新意在于把 VLA 泛化失败归因于缺少 system variable conditioning，并把短时主动交互作为在线识别接口。

#### 📊 实验与结果

该论文只有摘要回退信息。当前能确认的实验目标应是验证 VLA 在新相机视角、机器人形态或新 setup 下的泛化能力，以及 ICWM 是否能减少针对每个新环境的数据密集 fine-tuning。摘要没有给出 benchmark、任务数量、机器人平台、成功率或对比方法细节。因此它进入精选主要因为 world model / World Action Model 方向契合度高：它把机器人控制中的上下文建模从“任务 demonstration”推进到“系统识别”。但实验证据强度必须等 PDF 核查，尤其要看短历史交互是否 task-agnostic、是否真正跨 embodiment，以及识别动作是否安全可执行。

#### ⚠️ 风险 / 保留意见

- 只有摘要证据，不能确认具体世界模型形式和实验规模。
- 主动自交互可能在真实机器人上带来安全和时间成本。
- 若系统变化超出训练覆盖，in-context 推断可能给出过度自信的错误适配。

#### 💭 结论与启发

ICWM 是今天最像“world action model”苗头的一篇：它把动作后的系统响应作为上下文，让 VLA 先理解执行介质再做任务。对后续选题，我会关注能否把这种 task-agnostic probing 设计成标准化 preamble，让同一策略在不同相机和机器人上快速校准。复现时最关键不是大模型规模，而是构造可控的系统变量变化，并评估 context 长度、probe 动作和泛化范围三者的关系。

#### 🔎 读 PDF 先核查

- ICWM 的 context 中包含哪些自交互信号：动作、图像、状态、奖励还是未来观测预测？
- task-agnostic probing 动作如何生成，是否有安全约束或覆盖性目标？
- 方法是否显式建模系统变量，还是只通过 Transformer context 隐式适配？

#### 📌 上传 PDF 后优先看

- 问题定义与 system variable 建模章节
- self-generated task-agnostic interaction 设计章节
- 跨相机、跨形态或跨环境泛化实验章节

### [6]. Learning Action Priors for Cross-embodiment Robot Manipulation [[HTML]](https://arxiv.org/html/2606.26095) [[PDF]](https://arxiv.org/pdf/2606.26095) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2606.26095`
* **Authors**: Dong Jing, Tianqi Zhang, Jiaqi Liu, Jinman Zhao, Zelong Sun, Li Erran Li, Zhiwu Lu, Mingyu Ding
* **Author Priority**: Standard
* **一句话结论**: 值得优先看：它把 VLA 中常被忽略的 action module 单独预训练成运动先验，直接回应 cross-embodiment 动作分布不一致问题。
* **关键词**: `action prior` `cross-embodiment` `flow matching` `VLA training` `motion latent`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

#### 📖 背景与动机

大多数 VLA 借用 VLM backbone 获得强视觉和语言先验，再接一个 action head 做动作生成。这样语义侧一开始很强，但动作侧往往近似从零学习，早期训练必须同时解决时间动作动力学、跨模态对齐和不同 embodiment 的动作分布差异。跨机器人、跨仿真与真实平台混合训练时，这个问题会进一步放大：相同语言任务可能对应不同状态表示、动作尺度和轨迹节奏。该论文的核心动机是给 action module 也提供类似“预训练先验”，让它先理解运动轨迹分布，再接入视觉语言条件。

#### ⚙️ 核心方法

论文提出两阶段训练。第一阶段在不使用视觉和语言条件的情况下，仅用 action trajectories 训练一个 flow-matching-based encoder-decoder action module，使 action head 先学习结构化动作分布和时间动态。第二阶段再进行 VLA 训练，把已经具有 motion prior 的 action module 与 VLM backbone 对齐。摘录还明确提到 early-stage latent alignment distillation：在训练早期用蒸馏方式把 VLM anchored 到已学到的 action embedding space，从而加速 cross-modal convergence。这个设计的关键接口是 action latent：它既承载无条件运动先验，也成为视觉语言特征进入动作生成的对齐目标。相对常规联合优化，它把“学会怎么动”和“根据图像语言决定怎么动”拆开；相对只做数据混合的 cross-embodiment VLA，它显式处理不同平台动作分布的历史压缩和动态先验问题。

#### 📊 实验与结果

实验覆盖 13 个任务，来自两个模拟 benchmark LIBERO、RoboCasa，以及真实 Franka 平台。摘录说明三类环境在 embodiment、动作和状态表示、场景组成、任务分布上差异较大，所有模型在完整 cross-embodiment mixture 上训练，并在各 benchmark 上不做环境特定 fine-tuning 评估。LIBERO 部分覆盖 Spatial、Object、Goal、Long 四个 task suites，每个 suite 有 10 个任务和 500 条训练示范；评估时每任务 50 个 episode。推理时模型预测 action chunk，默认执行前 5 个动作再重新预测。结论称该方法带来更快收敛、更高成功率和有效历史压缩，但摘录没有给具体提升数字，需要 PDF 核查。

#### ⚠️ 风险 / 保留意见

- action prior 可能学习到数据集中主导 embodiment 的偏置，对少数平台未必公平。
- 无条件动作预训练是否能覆盖视觉接触约束，需要看接触任务失败案例。
- 跨 embodiment action representation 如何统一，是复现的主要工程风险。

#### 💭 结论与启发

这篇对 VLA 系统设计的启发很直接：不要只预训练视觉语言 backbone，也要预训练动作生成器。尤其在多机器人数据混合时，action head 不是薄层解码器，而是需要承担时间压缩、动作平滑和 embodiment 差异吸收的核心模块。后续我会重点关注它的 action latent 是否可迁移到不同 VLM，若可以，它可能成为类似 tokenizer 一样的可复用机器人动作组件。

#### 🔎 读 PDF 先核查

- 无条件 action trajectory 预训练如何处理不同机器人动作维度、尺度和控制频率？
- early-stage latent alignment distillation 的 teacher signal 来自哪里，是否会限制 VLM 表征自由度？
- action prior 对 Long-horizon tasks 的收益是否大于短任务，是否主要来自历史压缩？

#### 📌 上传 PDF 后优先看

- action module 预训练与 flow matching 目标章节
- latent alignment distillation 机制章节
- LIBERO、RoboCasa、Franka 跨 embodiment 对比和消融章节

## Watchlist

### [W1]. GRAFT: Graph-Based Affordance Transfer via Part Correspondence [[VIP]] [[HTML]](https://arxiv.org/html/2606.25241) [[PDF]](https://arxiv.org/pdf/2606.25241)
* **Paper ID**: `2606.25241`
* **Authors**: Mengying Lin, Utkarsh Mishra, Ajay Mandlekar, Danfei Xu
* **Author Priority**: Extended VIP
* **为什么还值得留意**: GRAFT 进入 shortlist 是因为它用 part graph、UFGW graph matching 和 contact-level correspondence 做 zero-shot affordance transfer，对 sim data generation 与 unseen object manipulation 很有价值。它没有进最终精选，主要因为今天主线更偏 VLA 记忆、后训练和 world/action model；GRAFT 更像几何 affordance transfer 专题。Danfei Xu 在扩展关注名单中，建议后续按“几何泛化/数据生成”专题补读。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. Decoupling Semantics and Geometric Grounding: Spatial Visual Prompts for Language-Conditioned Imitation Learning [[HTML]](https://arxiv.org/html/2606.25360) [[PDF]](https://arxiv.org/pdf/2606.25360)
* **Paper ID**: `2606.25360`
* **Authors**: Yanzhe Tang, Xinyu Shao, Yuxuan Hu, Siyu Chen, Bowen Yang, Yajun Gao, Tongtong Cao, Xiu Li, Long Zeng
* **Author Priority**: Standard
* **为什么还值得留意**: SVP-IL 很贴近 VLA 的语义-空间解耦问题：用 foundation model 生成 zero-shot geometric masks，再以 Spatial Visual Prompts 注入 visuomotor policy，适合低数据语言条件操作。没有进最终精选，是因为作者不在关注名单，且方法更偏 perception-control prompt engineering；相比 HALO、FORCE、ICWM，它对今天的长期记忆、RL 后训练和 world model 主线贡献稍弱。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

### [W3]. Action ControlNet: A Lightweight Delay-Aware Adapter for Smooth Asynchronous Control in Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2606.25985) [[PDF]](https://arxiv.org/pdf/2606.25985)
* **Paper ID**: `2606.25985`
* **Authors**: Tiecheng Guo, Meng Guo
* **Author Priority**: Standard
* **为什么还值得留意**: Action ControlNet 关注 VLA 异步执行延迟、chunk handoff discontinuity 和控制平滑性，是非常实用的部署问题；Kinetix、Meta-World MT50 和真实 SO-ARM101 线索也值得看。没有进最终精选，是因为它更像 delay-aware adapter 与 runtime control 稳定化专题，和今天优先的长期记忆、RL fine-tuning、world modeling 相比系统层新意略窄。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

### [W4]. ROAD-VLA: Robust Online Adaptation via Self-Distillation for Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2606.25800) [[PDF]](https://arxiv.org/pdf/2606.25800)
* **Paper ID**: `2606.25800`
* **Authors**: Kejing Wang, Toan Nguyen, Minh Hoang Nguyen, Simon Khan, Flora D. Salim
* **Author Priority**: Standard
* **为什么还值得留意**: ROAD-VLA 进入 watchlist 是因为它同样处理 VLA online adaptation，把 scalar advantage 转成 action-token 级 dense supervision，并指出 text-based privileged teachers 与低层动作之间存在 modality gap。没有进最终精选，主要因为 FORCE 已覆盖 RL+VLA 后训练主线且摘录中实验结构更清楚；ROAD-VLA 的实验摘录部分混入 theorem 内容，当前证据不足以判断 benchmark 强度和真实机器人可靠性。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
