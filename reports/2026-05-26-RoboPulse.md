# RoboPulse | 2026-05-26

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 129 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线很集中：VLA 正在从“预训练后直接评测”转向更可靠的闭环适配，包括真实机器人 RL 微调、世界模型内滚动、动作空间几何对齐、跨具身动作头，以及更严格的泛化评测。最终精选保留了方法、训练闭环、评测协议和几何注入四条互补路线，能覆盖 VLA 走向部署前最关键的可靠性瓶颈。VIP 作者上，Dorsa Sadigh 与 Chelsea Finn 参与的 EXPO-FT 最值得优先跟踪，因为它直接把 RL fine-tuning 拉回真实机器人样本效率问题；watchlist 中 Jiajun Wu 相关的 embodied spatial intelligence 与 reflective planning 也值得持续观察。整体判断是：下一阶段 VLA 论文的说服力会越来越依赖真实交互证据、OOD 扰动评测，以及中间表示是否真的贴近可执行动作。

## 今日信号

- VLA 后训练正在从离线 imitation/benchmark 分数，转向少量真实机器人交互下的稳定 RL 微调与可靠成功率提升。
- world model 与 world action model 的关键竞争点不再只是生成清晰视频，而是能否提供可用于策略更新的动作一致性、奖励信号和长期几何稳定性。
- LIBERO-PRO 一类评测暴露出标准 VLA benchmark 的记忆化风险，后续读论文需要优先检查扰动维度、训练测试重合度和真实泛化证据。

## Historical Rediscovery

- **Paper**: GAF: Gaussian Action Field as a 4D Representation for Dynamic World Modeling in Robotic Manipulation [[HTML]](https://arxiv.org/html/2506.14135) [[PDF]](https://arxiv.org/pdf/2506.14135)
  - **Paper ID**: `2506.14135`
  - **来源日期**: 2026-05-25
  - **当时可能被低估的信号**: 当时可能低估了“从未来几何中直接推断动作”这个信号；它不是单纯 3D 表示改进，而是在尝试把 motion-aware 4D world representation 变成操控动作接口。
  - **为什么现在值得再看**: 现在 VLA/WAM 讨论越来越关注可预测未来状态、可执行动作和 4D 场景一致性，这篇正好连接 dynamic world modeling 与 robotic manipulation。即使 VLA/RL 闭环证据较弱，也值得作为 4D world-action 表示路线补看。
  - **建议动作**: 加入精读
  - **关键词**: `World Action Model` `4D representation` `dynamic world modeling` `robotic manipulation` `future geometry`
- **Paper**: LACY: A Vision-Language Model-based Language-Action Cycle for Self-Improving Robotic Manipulation [[HTML]](https://arxiv.org/html/2511.02239) [[PDF]](https://arxiv.org/pdf/2511.02239)
  - **Paper ID**: `2511.02239`
  - **来源日期**: 2026-05-25
  - **当时可能被低估的信号**: 当时可能低估了 bidirectional grounding 和 self-generated training data 的组合信号；虽然任务规模偏 tabletop，但 L2A/A2L/L2C 循环本身对 RL+VLA 后训练和数据扩展很有启发。
  - **为什么现在值得再看**: 当前 VLA 的瓶颈不只是模型结构，还包括如何从执行轨迹中生成可验证的新训练信号。它和自改进 VLA、长时程操作中的语义检查、失败后再标注都有关系。
  - **建议动作**: 加入精读
  - **关键词**: `VLA` `self-improvement` `language-action cycle` `semantic verification` `robotic manipulation`
- **Paper**: StableVLA: Towards Robust Vision-Language-Action Models without Extra Data [[HTML]](https://arxiv.org/html/2605.18287) [[PDF]](https://arxiv.org/pdf/2605.18287)
  - **Paper ID**: `2605.18287`
  - **来源日期**: 2026-05-19
  - **当时可能被低估的信号**: 当时可能低估了“无额外数据提升视觉退化鲁棒性”的部署信号；如果 corruption protocol 与机器人真实视觉退化接近，它可能是低成本提升现有 VLA 稳定性的实用路线。
  - **为什么现在值得再看**: VLA 进入真实机器人后，光照、遮挡、传感器噪声和背景变化会直接影响动作质量。它与真实部署评测、Sim2Real 视觉域偏移、稳健 VLA 后训练强相关。
  - **建议动作**: 快速浏览
  - **关键词**: `VLA robustness` `visual perturbation` `Sim2Real` `adapter` `deployment`
- **Paper**: Realtime-VLA FLASH: Speculative Inference Framework for Diffusion-based VLAs [[HTML]](https://arxiv.org/html/2605.13778) [[PDF]](https://arxiv.org/pdf/2605.13778)
  - **Paper ID**: `2605.13778`
  - **来源日期**: 2026-05-14
  - **当时可能被低估的信号**: 当时可能低估了延迟指标本身的重要性；58.0 ms full inference 与最快 7.8 ms speculative round 的对比说明它面对的是实时闭环控制里的硬约束，而不只是推理加速小优化。
  - **为什么现在值得再看**: 真实机器人 VLA 是否可用，很大程度取决于闭环重规划频率、失败回退和延迟稳定性。它和真实部署、长时程执行、diffusion VLA 工程化直接相关。
  - **建议动作**: 加入精读
  - **关键词**: `Realtime VLA` `diffusion policy` `speculative inference` `latency` `closed-loop control`
- **Paper**: ANCHOR: A Physically Grounded Closed-Loop Framework for Robust Home-Service Mobile Manipulation [[HTML]](https://arxiv.org/html/2604.25323) [[PDF]](https://arxiv.org/pdf/2604.25323)
  - **Paper ID**: `2604.25323`
  - **来源日期**: 2026-04-29
  - **当时可能被低估的信号**: 当时可能低估了 operability-aware base alignment 和局部异常处理作为真实部署信号的价值；它关注的是开放环境里持续变化的物理约束，而不是离线 benchmark 上的单步成功率。
  - **为什么现在值得再看**: World Model / World Action Model 最终要服务于真实世界闭环执行，ANCHOR 可作为对照：没有大模型范式突破时，系统如何处理物理可操作性、异常恢复和家居 OVMM 执行。
  - **建议动作**: 快速浏览
  - **关键词**: `closed-loop manipulation` `real deployment` `OVMM` `physical grounding` `failure recovery`

## Editor's Picks

### [1]. EXPO-FT: Sample-Efficient Reinforcement Learning Finetuning for Vision-Language-Action Models [[VIP]] [[HTML]](https://arxiv.org/html/2605.25477) [[PDF]](https://arxiv.org/pdf/2605.25477) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.25477`
* **Authors**: Perry Dong, Kuo-Han Hung, Tian Gao, Dorsa Sadigh, Chelsea Finn
* **Author Priority**: Core VIP
* **一句话结论**: 优先看：EXPO-FT 是今天最贴近真实部署的 VLA+RL 工作，因为它把预训练 VLA、critic 选择和在线机器人样本效率放在同一个系统里验证。
* **关键词**: `VLA fine-tuning` `real-world RL` `RedQ critic` `action chunk selection` `sample efficiency`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

VLA 预训练策略已经能覆盖多样操作任务，但部署时的核心问题不是“会不会做”，而是能否稳定做到足够高成功率。单纯行为克隆依赖数据分布，遇到高精度、动态或初始状态变化时容易失效；从零开始 RL 又往往交互成本高、探索不稳，不能充分利用 VLA 先验。EXPO-FT 关注的是一个非常实际的缺口：如何在不放弃 pretrained policy 的语义与动作先验的前提下，用少量真实机器人交互把任务成功率推到可部署水平。这也正好切中 VLA 走向 Sim2Real/Real2Real 后训练的关键问题。

#### ⚙️ 核心方法

EXPO-FT 以 pi0.5 这类 VLA 作为基础策略，并从任务特定 LoRA 监督微调 checkpoint 及匹配的机器人归一化统计初始化。摘录明确显示，图像输入被调整为 224x224，critic 使用 RedQ 风格的 10 个 Q 网络 ensemble，并在目标值计算时随机抽取 2 个网络取最小值，以缓解 Q 过估计。策略侧不是直接让 VLA 输出单一路径，而是把 base model 的短视野 action chunk 与一个小的 edit corrector 组合：每次决策采样 8 个 base chunk，再生成 8 个 edit 候选，edit 按 0.05、0.1 或 0.2 缩放后加到 base 上，最后在 16 个候选里用 critic 做 deterministic top-Q 选择。这个设计的新意在于 RL 没有完全重写 VLA，而是把更新压力集中到“候选修正+价值选择”接口上，使预训练先验、在线探索和稳定 critic 能协同工作。当前摘录只能确认这些核心模块，不能进一步断言完整 loss、优化超参或所有消融细节。

#### 📊 实验与结果

实验覆盖 8 个真实机器人操作任务，任务强调动态动作、高精度和多样初始状态。控制空间是末端执行器 Cartesian velocity 与 gripper velocity，运行频率 10 Hz；观测包含 side view 和 wrist view 两路 RGB 图像、以及末端位姿等 proprioception。奖励是二值稀疏完成信号，规则成功检测器据称有超过 95% 的成功识别准确率，最终评估由人观察任务是否成功。结论摘录给出关键结果：EXPO-FT 平均只需 19.1 分钟在线机器人交互，就能显著改善 pretrained VLA baseline 并达到高可靠表现。证据边界是：摘录没有提供每个任务的完整成功率表、方差、失败类型分解和对比方法逐项数字。

#### ⚠️ 风险 / 保留意见

- 真实机器人任务虽有 8 个，但摘录不足以判断任务多样性是否覆盖长程、多物体和强遮挡场景。
- critic top-Q 选择依赖 Q 估计质量，若 reward detector 或分布外状态导致价值偏差，可能选择看似高值但不安全的动作。
- 方法建立在已有任务特定 LoRA checkpoint 上，复现时需要确认 SFT 数据、归一化统计和机器人平台是否可获得。

#### 💭 结论与启发

这篇对后续选题的启发是：VLA 的 RL fine-tuning 不一定要把大模型整体端到端重训，工程上更可行的方式是保留 base policy 的多模态先验，用轻量 edit 和 ensemble critic 做局部搜索与选择。复现时应优先关注候选动作生成、Q ensemble 稳定性、reward detector 可靠性和真实交互时间统计。若要扩展到新平台，可以把它当作“VLA 后处理控制器+在线价值校正”的系统模板，而不是单纯算法模块。

#### 🔎 读 PDF 先核查

- EXPO-FT 的 edit corrector 在不同任务中到底学到的是微小姿态修正、时序节奏调整，还是对 base VLA 的系统性偏差补偿？
- deterministic top-Q 从 16 个候选中选动作时，是否会放大 critic 误差，论文是否给出 ensemble 大小或候选数的消融？
- 平均 19.1 分钟在线交互背后，各任务是否存在明显长尾，失败任务是否需要更多人工 reset 或 reward detector 调试？

#### 📌 上传 PDF 后优先看

- 方法章节中的 critic ensemble、edit corrector 和 action candidate selection 细节。
- 真实机器人 8 个任务的逐任务结果、对比方法、消融实验和交互时间统计。
- reward detector、人工评估协议、reset 方式与失败案例分析。

### [2]. World-VLA-Loop: Closed-Loop Learning of Video World Model and VLA Policy [[HTML]](https://arxiv.org/html/2602.06508) [[PDF]](https://arxiv.org/pdf/2602.06508) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2602.06508`
* **Authors**: Xiaokang Liu, Zechen Bai, Hai Ci, Kevin Yuchen Ma, Mike Zheng Shou
* **Author Priority**: Standard
* **一句话结论**: 优先看：World-VLA-Loop 把 world model 从“视频预测器”推进到“可训练 VLA 的虚拟交互环境”，是今天 world model + VLA 闭环路线的代表。
* **关键词**: `world model` `VLA reinforcement learning` `reward prediction` `near-success trajectories` `co-evolution`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

VLA 用 RL 后训练可以突破行为克隆，但真实机器人 RL 成本高，涉及大量 rollout、reset、监督和安全风险。动作条件视频 world model 看起来能提供虚拟环境，但它们常有两个问题：动作跟随不精确，尤其难区分接近成功但实际失败的轨迹；同时缺少原生 reward，若再用不准确的视觉预测去算 reward，会把误差传给 RL。World-VLA-Loop 的动机是把 world model 做成 VLA 后训练的闭环基础设施：不仅预测未来，还要对动作结果和奖励足够对齐，并能随着策略分布变化持续更新。

#### ⚙️ 核心方法

该工作有两个基础设计和一个高层 co-evolving 范式。第一，作者构造 SANS 数据，专门混合成功与 near-success 轨迹，用来提升 action-outcome alignment；这很关键，因为普通成功数据无法充分教会模型区分“差一点成功”和“已经成功”。第二，训练 state-aware video world model，从 diffusion latents 联合预测未来帧和二值 reward，把 reward estimation 耦合到生成器内部，而不是外接一个独立奖励模块。这样做的主张是：视觉预测和奖励判断共享状态与动作条件，能互相强化。第三，由于 VLA 在 RL 过程中会改变行为分布，框架使用真实 rollout 增广训练数据，再继续更新 world model 和 VLA policy，形成策略与模型共同演进的循环。当前摘录只能确认总体流程和模块关系，不能确认完整扩散架构、RL 算法细节和 SANS 数据规模。

#### 📊 实验与结果

实验覆盖 LIBERO 模拟 benchmark 与自建真实实验室设置，真实系统使用 Franka 机械臂和固定第三人称 RealSense D435 相机。摘录报告 world model 平均 visual alignment 为 88.5%，reward alignment 为 87.25%，说明作者把视觉和奖励一致性都作为核心指标。策略层面，OpenVLA-OFT 在 LIBERO 上平均成功率提升 12.7%，真实场景中分别有 23.4% 和 13.3% 的提升；迭代 refinement 又相对第一个 RL checkpoint 带来平均 13.3% 的真实任务准确率提升。证据边界在于：摘录没有给出任务清单、样本量、统计显著性、失败案例和与真实 RL 成本的直接对照。

#### ⚠️ 风险 / 保留意见

- world model 的 reward 与视觉预测耦合可能共同偏移，若模型生成看似合理但物理错误的未来，RL 会被系统性误导。
- 真实场景使用固定第三人称相机，泛化到多视角、手眼相机或遮挡更强的操作环境仍需验证。
- SANS 依赖 near-success 轨迹设计，数据采集和标注策略可能成为复现门槛。

#### 💭 结论与启发

这篇最值得借鉴的是“世界模型必须为策略优化服务”的评估口径。对于 VLA 后训练，视频是否漂亮不够，关键是动作条件下的 near-success 判别、reward alignment 和分布迭代更新。后续做 world action model 或 virtual rollout 时，可以把 SANS 式成功/近成功混合数据作为重点设计，并把真实 rollout 作为周期性校准信号，而不是一次性训练完 world model 后固定不变。

#### 🔎 读 PDF 先核查

- SANS 中 near-success 轨迹如何定义和采样，是否覆盖了真实机器人最常见的失败模式？
- 联合预测帧和二值 reward 相比独立 reward model 的收益来自共享 latent，还是来自额外监督正则化？
- co-evolving 循环中真实 rollout 的频率、数量和选择策略如何影响最终真实任务提升？

#### 📌 上传 PDF 后优先看

- SANS 数据构造、成功/near-success 轨迹比例与标注规则。
- world model 的动作条件、diffusion latent、reward head 与训练目标细节。
- LIBERO 与真实场景的任务表、迭代训练曲线、失败案例和成本对比。

### [3]. OASIS: Observation-Action Space Alignment via SE(3) Trajectory Prediction for Robotic Manipulation [[HTML]](https://arxiv.org/html/2605.25829) [[PDF]](https://arxiv.org/pdf/2605.25829) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.25829`
* **Authors**: Xinzhe Chen, Sihua Ren, Liqi Huang, Haowen Sun, Mingyang Li, Xingyu Chen, Zeyang Liu, Xuguang Lan
* **Author Priority**: Standard
* **一句话结论**: 优先看：OASIS 把 VLA/WAM 的中间表示显式对齐到 SE(3) 末端轨迹，是解决动作几何缺失问题的一条清晰路线。
* **关键词**: `SE(3) trajectory` `action-space alignment` `metric depth` `VLA` `world action model`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

许多 VLA 依靠 VLM 特征直接解码动作，增强版方法会加入深度、ROI 或 2D 轨迹，WAM 则预测未来图像或 latent。但这些中间表示大多仍停留在 observation space，并不天然符合 6-DoF 末端动作的刚体几何结构，导致 action decoder 必须隐式恢复 SE(3) 关系。OASIS 的问题意识很直接：如果机器人最终要输出的是末端位姿轨迹和 gripper 命令，中间层是否应该被监督成更接近 action space 的几何对象？这对高精度操作、跨视角泛化和真实机器人部署都重要。

#### ⚙️ 核心方法

OASIS 使用源自 Prismatic VLM 的架构，以 Qwen2.5-0.5B 为语言/多模态 backbone，并整合 DINOv2 与 SigLIP 两个视觉编码器；VLM 在 LLaVA-1.5-Instruct 上预训练，用于抽取视觉语义信息。方法核心是 3D-aware feature encoder 与 SE(3) trajectory predictor：前者融合视觉语言与 metric-depth features，后者预测 camera frame 下的八步末端轨迹。随后 action decoder 不是只看普通 VLM token，而是 cross-attend 到 predictor 的 pose-supervised hidden states，生成对应 action chunk。摘录给出实现：trajectory predictor 和 action decoder 都是 transformer，分别有 4 个和 2 个 blocks；模型总参数 1.73B，其中 0.18B 可训练；Qwen2.5-0.5B 通过 LoRA 调整，predictor、decoder 和 projection layers 从零训练，并冻结 DA3METRIC-LARGE。新意在于把“未来/空间辅助信号”从观测预测转成相机坐标系下的可执行末端轨迹。

#### 📊 实验与结果

实验同时覆盖模拟和真实机器人，作者提出四个问题：是否超过 VLA/WAM baseline，metric-depth feature 是否必要，predictor hidden state 的监督目标与参考坐标系如何影响成功率，以及真实机器人多任务和 OOD 扰动下是否保持优势。实现使用 4 张 NVIDIA A800，batch size 64。摘录声称 OASIS 在 simulation benchmarks 和 real-world platforms 上取得更好的操作精度与泛化，但没有给出主表逐项数字。可确认的证据是评测设计包含标准操作 suite、深度消融、隐藏状态监督/参考系消融、真实机器人与 OOD 扰动；不可确认的是具体胜幅、统计波动和失败场景。

#### ⚠️ 风险 / 保留意见

- 当前方法聚焦 tabletop manipulation，复杂移动操作、双臂或接触丰富任务的适用性仍不明确。
- 依赖 metric-depth/GFM 组件，深度估计错误可能直接污染 SE(3) 轨迹监督和 action decoding。
- 摘录没有完整结果表，需核查是否所有提升都来自轨迹对齐，而非更大模型、额外深度特征或训练设置差异。

#### 💭 结论与启发

OASIS 对系统设计的启发是：VLA 的中间接口可以更“机器人化”。与其让 action head 从抽象视觉语义 token 里猜 6-DoF 控制，不如显式预测末端轨迹，把 pose-supervised hidden states 作为动作解码条件。后续阅读应重点比较它与 2D trajectory、future image、latent WAM 的差异，尤其是 camera frame 轨迹监督是否在真实机器人 OOD 扰动下提供了稳定增益。

#### 🔎 读 PDF 先核查

- camera-frame 八步末端轨迹相比 robot/base frame 监督，优势是否来自更稳定的视觉对齐还是更容易训练？
- action decoder cross-attend 到 pose-supervised hidden states 时，轨迹预测误差会如何传播到最终 action chunk？
- OASIS 的收益在高精度接触任务、遮挡任务和普通 pick-place 任务之间是否一致？

#### 📌 上传 PDF 后优先看

- 3D-aware encoder、metric-depth feature 和 SE(3) trajectory predictor 的架构细节。
- hidden-state 监督目标、参考坐标系和深度输入的消融实验。
- 真实机器人多任务、OOD perturbation、失败案例与 baseline 公平性设置。

### [4]. X-DiffVLA: X-Embodied Diffusion Action Heads for Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2605.25044) [[PDF]](https://arxiv.org/pdf/2605.25044) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.25044`
* **Authors**: Boyu Li, Chaoyi Xu, Haoqi Yuan, Xinrun Xu, Börje F. Karlsson, Dongbin Zhao, Haoran Li, Zongqing Lu
* **Author Priority**: Standard
* **一句话结论**: 优先看：X-DiffVLA 面向跨具身 VLA 的动作头瓶颈，用统一动作空间和 diffusion head 处理不同末端执行器，是多机器人迁移方向的关键候选。
* **关键词**: `cross-embodiment` `diffusion action head` `unified action space` `Embodied Forcing` `Morphological Tree Diffusion`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

跨具身数据学习是通用机器人策略的核心难题。大型 VLA 预训练能提供视觉理解和长程规划能力，但下游往往仍要为不同机器人形态微调 embodiment-specific action head。只要末端执行器或自由度变化，就需要新的动作头，这会降低训练效率，也阻碍相似任务间的数据共享。X-DiffVLA 把问题限定在共享机器人 base、异构 end-effector 的场景，目标是让同一套动作头能在 parallel gripper、dexterous hand 等不同形态之间转移，并用扩散模型表达多峰动作分布。

#### ⚙️ 核心方法

X-DiffVLA 的核心是 unified cross-embodied action space 与 diffusion-based action head。它先定义一个标准化动作表示，覆盖机器人 base、gripper 和 dexterous hand 的最大维度；低自由度机器人通过 trailing dimensions zero-padding 对齐到统一向量。为了避免统一空间掩盖形态差异，作者提出 Embodied Forcing，把具体 morphology 信息注入 denoising 过程，引导动作 token 生成，使模型区分不同机器人和功能段。另一个模块是 Morphological Tree Diffusion，用树状形态关系刻画不同末端执行器间的行为相关性，目标是在相似任务中促进跨具身知识迁移。整体思路不是为每个机器人单独训练 action head，而是让 diffusion head 在共享动作空间中进行条件生成。当前摘录只能确认这些设计方向与接口，不能确认 morphological tree 的具体构建规则、loss 形式和采样算法。

#### 📊 实验与结果

评测覆盖 RoboCasa、Isaac Gym 和真实环境。RoboCasa 提供高保真任务与物体渲染，但原生具身支持有限；作者因此引入 Isaac Gym，扩展到更广泛的 embodiment，包括一个 gripper 和两类 dexterous hands，并覆盖十个不同物体。真实部署同时包含 parallel-gripper 和 dexterous-hand robots，用于验证从模拟到物理硬件的迁移。摘录说明使用 Being-H0 2B 作为 backbone 来验证 action head，但没有提供完整成功率数字、逐平台对比或消融结果。因此可以保守判断：实验覆盖面与问题设置有价值，但具体优势强度需要打开 PDF 核查。

#### ⚠️ 风险 / 保留意见

- 统一动作空间的 zero-padding 简洁但可能引入无效维度，复杂 morphology 下可能造成学习负担。
- 当前设定强调共享 robotic base 和异构 end-effector，不能直接等同于任意跨机器人迁移。
- 真实部署证据在摘录中缺少逐任务数字，需要核查是否存在模拟强、真实弱的落差。

#### 💭 结论与启发

这篇值得关注的原因不是它一定已经解决跨具身，而是它把 action head 作为 VLA 泛化瓶颈单独抽出来处理。对于多机器人系统，统一动作空间、形态条件 denoising 和 morphology-aware transfer 是可以复用的设计语言。后续若做跨夹爪/灵巧手任务，应重点比较 X-DiffVLA 与“共享 backbone + 多 action heads”的成本、数据效率和负迁移风险。

#### 🔎 读 PDF 先核查

- Morphological Tree Diffusion 的树结构是人工定义、由机器人形态参数生成，还是从数据中学习？
- 统一动作空间中的 zero-padding 维度在 denoising 和 loss 计算时是否被 mask，如何避免无效维度干扰？
- 真实 parallel-gripper 与 dexterous-hand 部署中，跨具身共享是否真的优于单具身专用 action head？

#### 📌 上传 PDF 后优先看

- unified action space 的维度定义、mask/zero-padding 处理和 embodiment token 设计。
- Embodied Forcing 与 Morphological Tree Diffusion 的训练目标、采样流程和消融。
- RoboCasa、Isaac Gym、真实机器人三类实验的逐平台结果和跨具身泛化设置。

### [5]. Understanding the Impact of Geometric Foundation Models on Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2605.24642) [[PDF]](https://arxiv.org/pdf/2605.24642) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.24642`
* **Authors**: Yurou Yang, Muyuan Lin, Roberto Martin-Martin, Martin Labrie, Shreekant Gayaka, Cheng-Hao Kuo, Luca Carlone
* **Author Priority**: Standard
* **一句话结论**: 优先看：这篇不是提出单一炫技模型，而是系统追问 GFM 到底如何影响 VLA，是判断几何注入路线是否可靠的重要实验论文。
* **关键词**: `geometric foundation model` `VGGT` `GR00T-N1.5` `early fusion` `spatial forcing`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)

#### 📖 背景与动机

VLA 与 geometric foundation model 的结合正在升温，VGGT 等 3D reconstruction/GFM 能给机器人带来更强几何表征，看似自然会提升操作。但关键问题仍不清楚：现代 VLA 本身是否已经具备足够几何理解？几何信息应该早期融合、晚期融合，还是通过 spatial forcing 影响动作专家？其他训练和架构选择会不会比 GFM 本身更重要？这篇以 GR00T-N1.5 和 VGGT 为具体对象，试图用实验分析回答这些问题，对读者判断“加 3D 模块是否真有用”很有价值。

#### ⚙️ 核心方法

作者围绕特定 VLA GR00T-N1.5 和 GFM VGGT 搭建几何 VLA 对比。摘录明确说，在写作时 Early Fusion 与 Late Fusion 路线没有可用开源代码，因此作者基于 GR00T-N1.5 自行实现原型；同时也把 Spatial Forcing 从原本基于 OpenVLA/pi0 的实现适配到 GR00T，以保证比较更公平。方法重点不是一个新模块，而是控制变量式比较不同几何注入位置：Early Fusion 倾向于在较早视觉/多模态阶段注入几何，Late Fusion 则在后续决策阶段结合，Spatial Forcing 用空间约束方式影响策略表示。HTML 摘录中还出现 Early Fusion 训练动态分析，显示不同任务收敛速度不同，并提示多任务干扰和 cabinet 操作瓶颈。当前摘录只能确认实验框架、模型选择和部分训练动态观察，不能断言最终全局结论的完整强弱排序。

#### 📊 实验与结果

实验围绕 GR00T-N1.5、VGGT、Early Fusion、Late Fusion 与 Spatial Forcing 适配展开。摘录中的训练动态给出若干具体观察：PnPCounterToSink 在 epoch 5 达到 92% 成功率，PnPCounterToCab 到 epoch 50 达到 65.3% 峰值，PnPCounterToMicrowave 在 epoch 35 达到 76% 后到 epoch 50 降至 40%，作者据此认为存在多任务干扰或灾难性遗忘迹象；cabinet 相关任务表现较低，约 52-65.3%，被识别为瓶颈。证据边界是这些数字来自摘录中的局部分析，不足以替代完整主表；需要核查 benchmark、训练轮次、公平性和最终平均结果。

#### ⚠️ 风险 / 保留意见

- 结论绑定 GR00T-N1.5 与 VGGT，未必能直接推广到其他 VLA/GFM 组合。
- Early/Late Fusion 为作者原型实现，结果可能受工程细节和调参程度影响。
- 摘录展示了部分训练动态，但缺少完整主实验数字，需谨慎引用总体结论。

#### 💭 结论与启发

这篇对阅读策略的价值很高：几何 foundation model 不是即插即用的性能保证，注入位置、动作专家接口、任务类型和训练动态都可能决定成败。后续做 VLA+3D 时，应把 baseline 公平适配、任务级收敛曲线、多任务干扰和失败类别作为必查项。它也提醒我们，几何增强论文若只报平均分，可能掩盖不同任务上的正负迁移。

#### 🔎 读 PDF 先核查

- GR00T-N1.5 原始 VLA 在没有 VGGT 时的几何理解到底弱在哪里，论文是否给出诊断实验？
- Early Fusion、Late Fusion 和 Spatial Forcing 的比较是否控制了参数量、训练步数和输入信息量？
- 多任务干扰是否由几何特征注入导致，还是 GR00T action expert 本身在异质任务上已有遗忘问题？

#### 📌 上传 PDF 后优先看

- 实验设计中 GR00T-N1.5、VGGT 与各 fusion baseline 的实现公平性。
- 任务级训练曲线、峰值与最终性能差异，尤其是 cabinet/microwave 等瓶颈任务。
- 关于 VLA 是否已有几何能力、最佳注入架构和设计选择影响的结论章节。

### [6]. LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization [[VIP]] [[HTML]](https://arxiv.org/html/2510.03827) [[PDF]](https://arxiv.org/pdf/2510.03827) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2510.03827`
* **Authors**: Xueyang Zhou, Yangming Xu, Guiyao Tie, Yongchao Chen, Guowen Zhang, Duanfeng Chu, Pan Zhou, Lichao Sun
* **Author Priority**: Core VIP
* **一句话结论**: 优先看：LIBERO-PRO 是今天最重要的评测警报，指出标准 LIBERO 高分可能严重混入记忆化而非真实 VLA 泛化。
* **关键词**: `VLA benchmark` `LIBERO-PRO` `memorization` `OOD perturbation` `robust evaluation`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

LIBERO 已成为 VLA 领域常用评测套件，许多大规模预训练模型和任务特定系统都用它报告结果，因此它实际上影响了社区对方法优劣的判断。如果训练和评测配置复用高度相似的任务、布局或动作序列，模型可能通过记忆固定映射拿到高分，却没有真正理解指令、场景变化或可迁移动作策略。LIBERO-PRO 的动机是修正这个评价缺口：通过合理扰动对象、初始状态、指令和环境，测试 VLA 是否能在保持任务语义可行的情况下泛化，而不是只复现训练集布局。

#### ⚙️ 核心方法

LIBERO-PRO 设计了 perturbation-based evaluation framework，在四个正交维度生成受控变体。对象属性扰动改变非本质视觉属性，如颜色、纹理或尺寸，同时保持语义等价；初始配置扰动改变物体绝对和相对位置，并保持物理合理性；指令扰动包含语义级复述和任务级变化，前者保持意图，后者在训练分布内改变目标对象或动作；环境扰动改变背景、光照或纹理等视觉上下文，不改变任务可行性。这个框架的关键新意不是提出更难任务，而是把“合理变化下是否仍会做”作为 VLA 评测的基本要求，并把对象、布局、语言和环境四类记忆化来源拆开。当前摘录没有提供完整数据生成算法和每个扰动强度细节，因此对 benchmark 构造细节应保守表达。

#### 📊 实验与结果

摘录给出最强烈的实验结论：现有模型在标准 LIBERO evaluation 下可达到超过 90% accuracy，但在 LIBERO-PRO 的 generalized setting 下 performance collapses to 0.0%。作者将这一差距解释为模型依赖训练集中动作序列和环境布局的 rote memorization，而非真正指令理解或鲁棒动作策略。由于摘录没有列出所有模型、训练数据、评测 split 和逐扰动维度结果，我们不能进一步判断崩塌是否对所有模型同等成立，也不能推断具体哪类扰动最致命。即便如此，该结果足以作为 VLA benchmark 使用中的高优先级风险信号。

#### ⚠️ 风险 / 保留意见

- 0.0% 崩塌结论需要核查具体模型列表、训练协议和 generalized setting 是否保持任务可行且公平。
- 扰动若过强或改变隐含任务约束，可能把鲁棒性评测变成分布外压力测试，需要看作者如何界定 reasonable perturbations。
- 作为 benchmark 论文，它揭示问题强于解决问题，不能直接提供提升 VLA 鲁棒性的训练方法。

#### 💭 结论与启发

LIBERO-PRO 对后续读论文的影响很直接：凡是只报告标准 LIBERO 高分的 VLA 方法，都需要额外核查训练测试重合、初始状态扰动、语言复述和环境变化。它也适合作为内部复现基准，用来区分“动作序列记忆”和“任务策略泛化”。如果要设计新方法，最好从一开始就把 LIBERO-PRO 式扰动纳入 validation，而不是等主结果完成后再做附录鲁棒性测试。

#### 🔎 读 PDF 先核查

- generalized setting 中四类扰动的具体强度如何定义，是否每个扰动都保持原任务可解？
- 标准 LIBERO 超过 90% 到 LIBERO-PRO 0.0% 的崩塌，在不同模型和不同扰动维度上是否一致？
- 任务级指令扰动仍在训练分布内的证据是什么，是否可能引入了未见组合导致额外难度？

#### 📌 上传 PDF 后优先看

- benchmark 构造章节中四类 perturbation 的生成规则、可行性检查和 split 设计。
- 实验主表中模型列表、标准 LIBERO 与 LIBERO-PRO 的逐模型对比。
- 按对象、初始状态、指令、环境维度拆分的失败分析与示例。

## Watchlist

### [W1]. Afford-VLA: Action-Aligned Visual Planning via Internalized Affordance [[HTML]](https://arxiv.org/html/2605.24203) [[PDF]](https://arxiv.org/pdf/2605.24203)
* **Paper ID**: `2605.24203`
* **Authors**: Runze Wang, Yuqian Fu, Yu Li, Tao Lin, Tianwen Qian, Mohamed Elhoseiny, Bo Zhao, Yanwei Fu, Yu-Gang Jiang, Xiangyang Xue
* **Author Priority**: Standard
* **为什么还值得留意**: Afford-VLA 进入 watchlist，因为它把 VLA 的视觉规划重新定义为局部、视觉 grounded、内部生成且 action-aligned 的 affordance 接口，和 OASIS 的动作空间对齐主题互补。摘录显示其实现使用 Qwen3-VL-4B-Instruct、GR00T-style flow-matching action head、双 RealSense 真实机器人设置，工程信息较丰富。没有进入最终精选主要是因为今日主线中已有 OASIS 覆盖“中间表示对齐”，而 Afford-VLA 的完整结果数字和相对优势在摘录中证据不足。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

### [W2]. ESI-Bench: Towards Embodied Spatial Intelligence that Closes the Perception-Action Loop [[VIP]] [[HTML]](https://arxiv.org/html/2605.18746) [[PDF]](https://arxiv.org/pdf/2605.18746)
* **Paper ID**: `2605.18746`
* **Authors**: Yining Hong, Jiageng Liu, Han Yin, Manling Li, Leonidas Guibas, Li Fei-Fei, Jiajun Wu, Yejin Choi
* **Author Priority**: Extended VIP
* **为什么还值得留意**: ESI-Bench 值得跟踪，因为它把 spatial intelligence 从被动观察改成 perception-action loop，覆盖 10 类任务和 29 个子类，且作者中有 Li Fei-Fei、Jiajun Wu、Yejin Choi 等扩展关注对象。它对 embodied reasoning 和主动感知评测很重要，但与今天 VLA/RL/world model 操作策略主线略有距离。没有进入最终精选，是因为它更偏 benchmark 与 embodied spatial QA，而非直接的 VLA 后训练或动作模型方法。
* **证据来源**: arXiv HTML (Introduction, Experiments)

### [W3]. Learning from Trials and Errors: Reflective Test-Time Planning for Embodied LLMs [[VIP]] [[HTML]](https://arxiv.org/html/2602.21198) [[PDF]](https://arxiv.org/pdf/2602.21198)
* **Paper ID**: `2602.21198`
* **Authors**: Yining Hong, Huang Huang, Manling Li, Li Fei-Fei, Leonidas Guibas, Jiajun Wu, Yejin Choi
* **Author Priority**: Extended VIP
* **为什么还值得留意**: Reflective Test-Time Planning 进入 watchlist，因为它讨论 embodied LLM 如何在测试时通过 reflection-in-action 和 reflection-on-action 从失败中学习，和 RL/VLA 的部署适应问题相关。摘录显示任务基于 BEHAVIOR-1K 长程家庭任务，并包含人类评价和 oracle reflection 对照，方向很有潜力。未进最终精选的原因是它更偏高层 embodied LLM planning，当前摘录与低层 VLA action policy、Sim2Real 或 world action model 的直接连接较弱。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. Drift-Resistant Navigation World Model with Anchored Epipolar Guidance [[HTML]](https://arxiv.org/html/2605.24761) [[PDF]](https://arxiv.org/pdf/2605.24761)
* **Paper ID**: `2605.24761`
* **Authors**: Po-Chien Luan, Zimin Xia, Wuyang Li, Yang Gao, Alexandre Alahi
* **Author Priority**: Standard
* **为什么还值得留意**: DR-NWM 值得留在 watchlist，因为它针对导航 world model 的 perceptual drift 与 geometric drift，提出 anchor-guided rollout、bidirectional epipolar guidance 和 AC-DiT，并在 RECON、HuRoN、SCAND、TartanDrive 上评估。它对长期 rollout 世界模型很有启发，尤其是把几何一致性指标纳入生成质量评估。没有进入最终精选，主要是因为应用场景偏导航而非操作型 VLA/WAM，和今日机器人 manipulation/VLA 后训练主线的贴合度略低。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
