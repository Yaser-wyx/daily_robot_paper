# RoboPulse | 2026-05-28

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 85 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线很清楚：VLA 正在从“模型能力展示”转向部署、闭环评测、视频世界模型接口和动作执行效率这些更硬的问题。最终精选覆盖了工厂真实部署、闭环视频世界模拟器、类人 loco-manipulation 数据生成、VLA 泛化 benchmark、视频模型转策略、World Action Model 推理调度，基本对应了 VLA/Sim2Real/world model 的关键断点。VIP 作者里最值得优先跟踪的是 2605.27724 的 Yuke Zhu，因为这篇直接把 VLA 数据扩展问题推进到类人全身移动操作；其他精选目前未命中核心 VIP 作者，但主题上与 Levine/Finn/Abbeel/Song 等路线高度相关。整体判断是：本轮不只是“更大模型”，而是在追问机器人 foundation policy 如何被评估、如何闭环、如何低成本产生数据、以及如何进入真实生产约束。

## 今日信号

- VLA 的下一轮竞争点正在从单次成功率转向部署闭环中的延迟、失败模式、质量约束和可复现评测。
- 视频世界模型和 World Action Model 正在形成两条互补路线：一条用视频模拟器替代部分真实评测，另一条把中间视频状态变成可调度的动作条件。
- 类人和长程操作暴露出传统遥操作数据采集的瓶颈，自动生成、分解复用和进度/价值结构将成为数据效率核心工具。

## Historical Rediscovery

- **Paper**: FrameSkip: Learning from Fewer but More Informative Frames in VLA Training [[HTML]](https://arxiv.org/html/2605.13757) [[PDF]](https://arxiv.org/pdf/2605.13757)
  - **Paper ID**: `2605.13757`
  - **来源日期**: 2026-05-14
  - **当时可能被低估的信号**: 当时可能低估了 action variation、visual-action coherence、task-progress priors 与 gripper-transition preservation 这些信号的组合价值；这些不是普通抽帧，而是围绕动作变化和任务进展筛选帧。
  - **为什么现在值得再看**: 如果现在关注 VLA 后训练和真实部署，数据效率会直接影响模型迭代速度与跨任务泛化；这篇可作为检查 VLA demonstrations 中哪些帧真正驱动策略学习的切入点。
  - **建议动作**: 加入精读
  - **关键词**: `VLA` `data efficiency` `demonstration pruning` `action representation`
- **Paper**: Latent Bridge: Feature Delta Prediction for Efficient Dual-System Vision-Language-Action Model Inference [[HTML]](https://arxiv.org/html/2605.02739) [[PDF]](https://arxiv.org/pdf/2605.02739)
  - **Paper ID**: `2605.02739`
  - **来源日期**: 2026-05-05
  - **当时可能被低估的信号**: 当时可能低估了“不改预训练模型本体”的工程信号；这种兼容式加速如果稳定，可能比重训策略更容易进入真实机器人系统。
  - **为什么现在值得再看**: VLA 真实部署离不开实时闭环，尤其在长时程操作和高频感知-动作循环里，推理延迟会变成策略质量的一部分；这篇和 real-time VLA inference 直接相关。
  - **建议动作**: 加入精读
  - **关键词**: `VLA` `real-time inference` `dual-system VLA` `deployment`
- **Paper**: Modular Sensory Stream for Integrating Physical Feedback in Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2604.23272) [[PDF]](https://arxiv.org/pdf/2604.23272)
  - **Paper ID**: `2604.23272`
  - **来源日期**: 2026-04-28
  - **当时可能被低估的信号**: 当时可能低估了 modular sensory stream 的长期价值；它不是只加传感器，而是尝试用可扩展方式融合异质物理反馈。
  - **为什么现在值得再看**: 如果研究 World Action Model 或真实 manipulation，物理反馈是视觉预测之外的重要状态信号；这篇值得作为接触任务中 VLA 如何闭环感知物理世界的参考。
  - **建议动作**: 加入精读
  - **关键词**: `VLA` `physical feedback` `tactile` `contact-rich manipulation`
- **Paper**: Refining Compositional Diffusion for Reliable Long-Horizon Planning [[HTML]](https://arxiv.org/html/2605.03075) [[PDF]](https://arxiv.org/pdf/2605.03075)
  - **Paper ID**: `2605.03075`
  - **来源日期**: 2026-05-06
  - **当时可能被低估的信号**: 当时可能低估了 training-free guidance 在长时程规划中的实用性；它瞄准的是 mode-averaging 这种会直接破坏计划可靠性的痛点。
  - **为什么现在值得再看**: 长时程操作和 World Action Model 都需要把局部动作生成与全局目标一致性接起来；即使它不是 VLA 主干论文，也可补充规划层如何稳定支持 action rollout。
  - **建议动作**: 快速浏览
  - **关键词**: `long-horizon planning` `diffusion planning` `manipulation` `world action model`
- **Paper**: Drift-Resistant Navigation World Model with Anchored Epipolar Guidance [[HTML]](https://arxiv.org/html/2605.24761) [[PDF]](https://arxiv.org/pdf/2605.24761)
  - **Paper ID**: `2605.24761`
  - **来源日期**: 2026-05-26
  - **当时可能被低估的信号**: 当时可能低估了 anchor-guided rollout 与 epipolar guidance 对长期预测稳定性的启发；虽然场景偏导航，但 drift 问题是 world model 共性问题。
  - **为什么现在值得再看**: 今天再看 world model 和 WAM 时，长期 rollout 是否漂移是核心瓶颈；这篇可作为几何约束如何提升 action-conditioned prediction 稳定性的参考。
  - **建议动作**: 继续跟踪
  - **关键词**: `world model` `long-horizon rollout` `geometric consistency` `sim2real`

## Editor's Picks

### [1]. A Factory-Floor Deployment Case Study of VLA Pipelines for Industrial Packaging Task: Workflow, Failures, and Lessons [[HTML]](https://arxiv.org/html/2605.27461) [[PDF]](https://arxiv.org/pdf/2605.27461) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.27461`
* **Authors**: Brian Zhu, Philipp Schmitt, Philine Meister, Lukas Gensler, Momen Khalil, Emmanuele Poggi, Johannes Hechtl, Carsten Braunroth, Kai Wurm, Gokul Narayanan, Eugen Solowjow, Georg von Wichert, Andre Scholz, Felix Albrecht, Maxmillian Metzner
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为它不是又一个 VLA demo，而是把 Pi0.5 类策略放进真实工厂包装任务后，系统性记录了哪些工程细节会让策略失效。
* **关键词**: `VLA deployment` `industrial packaging` `Pi0.5 finetuning` `failure taxonomy` `latency`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

#### 📖 背景与动机

这篇关注的是 VLA 从实验室走向工业现场时最容易被论文平均指标掩盖的问题：透明袋、杂乱堆叠、纸箱剩余空间、下游合盖平面约束和吞吐/安全/低延迟要求，会把看似可泛化的 manipulation policy 拉回到非常具体的可靠性挑战。工业包装任务本身不炫技，但它非常适合暴露 VLA 的部署缺口：视觉上有透明反光与遮挡，动作上要完成 pick-place 和整理，结果上还必须满足质量检测式约束。现有 VLA 研究常在受控实验室展示能力，失败成本较低；而工厂部署要求策略不仅能偶尔完成，还要在长时间、重复、扰动场景下稳定工作。因此这篇的价值在于把“如何微调一个预训练 Pi0.5 到单一真实任务”写成部署案例，而不是只报告最终成功率。

#### ⚙️ 核心方法

当前摘录能确认的方法主线是：作者以预训练 Pi0.5 policy 为起点，在 Siemens Factory 的具体包装工作站上做迭代式数据采集和微调。任务接口是视觉观察、语言/任务条件和机器人动作，目标是从一堆随机摆放的透明 accessory bag 中抓取一个袋子，放入纸盒剩余空腔，并确保袋子及内部物品低于 closing plane。方法的新意不在于提出新 backbone，而在于把 VLA pipeline 的生产化适配过程拆成可复盘的工程闭环：真实控制栈响应性、遥操作数据质量、推理延迟、异步 inference loop 或 real-time chunking、失败 episode 标注与错误归因。摘录还显示他们把失败按常见错误类别量化，说明训练不是一次性微调，而是围绕现场失败模式持续调整数据和系统。由于 HTML 摘录没有给出完整模型配置、数据规模、微调轮次和控制频率，不能把它解读为一个可直接复现的算法配方；更稳妥地说，它是一篇 VLA 部署工作流与失败分析论文。

#### 📊 实验与结果

实验是在真实工业包装任务上进行的，最后一轮数据采集和训练后，作者做了更完整评估。评估模拟机器人清空一个包含 30 个随机摆放袋子的 bin，每个 episode 对应一次单袋 pick-and-place，时间限制为 1 分钟；无论成功失败，目标袋都会在 episode 末移除，直到 bin 清空。Trial 1 包含 Settled Parts 约束，Trial 2 和 3 更自由；失败 episode 被人工记录短描述，再归入常见错误类别并在图表中汇总。HTML 明确给出的一个关键数字是：在失败 episode 中，“Bag Contents Remain on Product”占 65%，显示主要瓶颈不是简单抓不到，而是透明袋与附件内容、产品表面和质量约束之间的细粒度关系。结论明确说最终成功率没有达到预期，因此这篇的证据价值主要在失败诊断和部署经验，而不是宣称工业可用。

#### ⚠️ 风险 / 保留意见

- 单一工厂、单一包装任务，结论对其他工业场景的外推需要谨慎。
- 摘录没有提供完整成功率、数据量和微调细节，难以独立判断训练收益来源。
- 真实部署中的 latency/jitter、透明物体感知和质量约束耦合，复现成本可能高于普通 VLA benchmark。

#### 💭 结论与启发

这篇对后续选题的启发是：VLA 工业落地论文不应只问模型是否会执行指令，而要把控制栈、数据采集延迟、失败标注和质量约束纳入主实验。复现时可以把它当成 deployment checklist：先保证遥操作闭环足够顺，再收集覆盖失败模式的数据，最后才比较策略版本。系统设计上，它提醒我们 transparent/deformable/clutter 场景里，“成功放置”需要被拆成动作成功和下游质量成功两个指标，否则模型会在视觉上看似完成但实际不合格。

#### 🔎 读 PDF 先核查

- Pi0.5 微调过程中每一轮新增数据主要覆盖哪些失败模式，是否能看到错误分布随迭代移动？
- 异步推理和 real-time chunking 对动作平滑性、遥操作示教质量和最终策略表现分别有多大影响？
- 失败里 65% 的 bag contents 问题是感知错误、抓取策略错误、放置后整理不足，还是质量判定定义过严？

#### 📌 上传 PDF 后优先看

- 部署工作流与数据采集章节
- 失败模式分类表和最终评估实验
- 控制栈延迟、异步推理和 real-time chunking 相关分析

### [2]. GE-Sim 2.0: A Roadmap Towards Comprehensive Closed-loop Video World Simulators for Robotic Manipulation [[HTML]](https://arxiv.org/html/2605.27491) [[PDF]](https://arxiv.org/pdf/2605.27491) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.27491`
* **Authors**: Boxiang Qiu, Liliang Chen, Yue Liao, Nan Wang, Lintao Wang, Jiayi Luo, Wenzhi Zhao, Shengcong Chen, Di Chen, Ye Li, Chen Gao, Shuicheng Yan, Si Liu, Maoqing Yao, Guanghui Ren
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为 GE-Sim 2.0 把视频世界模型从“生成好看 rollouts”推进到闭环 policy evaluation、reward judging 和数据生成。
* **关键词**: `closed-loop simulator` `video world model` `robot manipulation` `world judge` `policy improvement`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

机器人世界模型的核心瓶颈不是能不能生成视频，而是生成的视频能否被策略当作可信环境来交互。真实机器人评测慢、贵、难复现；传统物理模拟器在接触、可变形物、细粒度视觉外观和机器人执行特性上又经常和真实世界偏离。随着 VLA 和大规模 robot policy 进入长程、双臂、接触丰富任务，评测本身成为扩展瓶颈。GE-Sim 2.0 的动机正是补上这个空缺：如果一个 action-conditioned video model 能在闭环中响应策略动作、预测后续状态，并提供可验证 reward，那么它就不只是 world model，而是可服务于 policy evaluation 和 policy improvement 的视频模拟器。对于 Sim2Real 和 World Model 方向，这篇重要在于它尝试把真实机器人数据、视频生成、状态估计和自动评判连接成完整闭环。

#### ⚙️ 核心方法

当前摘录能确认 GE-Sim 2.0 建立在 Genie Envisioner 的 action-conditioned video generation 框架上，并重新用数千小时真实机器人数据训练，数据覆盖 teleoperation、contact-rich interaction 和 on-robot policy deployment。基础模块 GE-Base 把机器人世界建模为多视角 text-and-image-to-video 生成：输入语言指令和初始多视角观察，模型以自回归 chunk 方式预测未来视频，并通过稀疏 memory 保存之前生成 chunk 的关键帧来延长时域上下文。多视角输入由共享 video encoder 处理，结合 3D rotary positional embedding、view embedding 和 view-specific noise map，让 head/wrist 等相机视角在同一生成过程中协同。GE-Sim 2.0 的关键新增模块包括：从视频 latent 解码 proprioceptive state 的 state expert，用于支持下一段动作/状态闭环；world judge，将 rollout 转成机器可验证成功信号；以及用模拟 rollout 和 reward 过滤出的数据来改进 downstream policy。摘录未给出全部网络尺寸和训练损失细节，因此应保守理解为一套闭环视频模拟器路线图，而非完全透明的复现配方。

#### 📊 实验与结果

实验设计围绕五个问题展开：视觉质量、闭环忠实度、reward 可验证性、是否能改善策略，以及组件贡献。任务侧，摘录明确说评估包含六个长程双臂 manipulation tasks，用来覆盖接触丰富和长程交互。GE-Sim 2.0 不只在 WorldArena 和 replay metric 上看视频质量，还比较 policy 在 GE-Sim 2.0 中运行时的结果是否与真实机器人一致，并检验 world judge 是否能替代人工检查。后续还用 world model 和 reward 生成过滤训练数据，测试是否能提升下游 policy。HTML 摘录没有给出具体成功率、相关系数或提升幅度，因此不能引用数字；但实验结构本身显示作者明确把“video generator”升级成“closed-loop simulator”作为中心主张。

#### ⚠️ 风险 / 保留意见

- 视频模拟器的闭环可信度可能强依赖训练数据覆盖，长尾接触失败未必能被视频 latent 捕捉。
- world judge 如果存在系统性偏差，可能把错误 rollout 过滤成伪成功数据。
- 摘录未提供关键量化结果，当前只能判断实验问题设置完整，不能独立确认提升幅度。

#### 💭 结论与启发

这篇对系统设计的启发是，world model 不应只输出未来帧，还需要提供状态接口、评判接口和数据闭环接口。后续读 PDF 应重点看真实机器人一致性如何定义，以及 world judge 的错误类型，因为这决定它能否用于减少实机评测。复现上可以先缩小目标：不必一开始训练大视频模型，而是用已有视频模型加一个 state decoder 和 reward judge，验证在少数 manipulation task 上是否能排序 policy 或筛选 rollouts。

#### 🔎 读 PDF 先核查

- GE-Sim 2.0 的 closed-loop faithfulness 是按最终成功、轨迹相似度、状态误差还是人类评判来衡量？
- state expert 解码的 proprioceptive state 在下一 chunk 预测中具体如何使用，错误会不会在自回归 rollout 中累积？
- world judge 的训练标签来自人工、规则还是真实执行结果，它在失败边界样本上的 false positive 率如何？

#### 📌 上传 PDF 后优先看

- GE-Base 多视角自回归视频生成方法章节
- closed-loop faithfulness 与真实机器人对齐实验
- world judge、state expert 和 policy improvement 消融实验

### [3]. HumanoidMimicGen: Data Generation for Loco-Manipulation via Whole-Body Planning [[VIP]] [[HTML]](https://arxiv.org/html/2605.27724) [[PDF]](https://arxiv.org/pdf/2605.27724) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.27724`
* **Authors**: Kevin Lin, Ajay Mandlekar, Caelan Reed Garrett, Nikita Chernyadev, Yu Fang, Runyu Ding, Yuqi Xie, Justin Tran, Linxi Fan, Yuke Zhu
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，尤其要跟踪 Yuke Zhu，因为它把 MimicGen 式数据生成推进到类人全身 loco-manipulation，并给出 sim-and-real co-training 证据。
* **关键词**: `humanoid manipulation` `loco-manipulation` `data generation` `whole-body planning` `Yuke Zhu`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

#### 📖 背景与动机

VLA 在固定机械臂操作上已经积累了不少数据和模型，但类人机器人面临完全不同的数据瓶颈：机器人不只是伸手抓取，还要移动 base、协调腿、躯干和手臂，并在环境中保持可达性和稳定性。遥操作类人全身任务成本高、动作空间高维、示教难以覆盖多样初始状态；而已有自动数据生成方法多针对固定机械臂，不能直接处理导航、全身姿态和接触操作的组合。HumanoidMimicGen 的问题意识很清楚：如果未来 VLA 要扩展到 humanoid，不可能只靠人类遥操作堆数据，必须能从少量专家演示中合成更多可训练的全身操作轨迹。这也是它进入精选的主要原因：它不是单纯类人控制论文，而是在为 humanoid VLA 的数据规模化补基础设施。

#### ⚙️ 核心方法

当前摘录能确认 HumanoidMimicGen 使用少量 source demonstrations，通过 whole-body planning 将导航、全身运动和 manipulation 片段组合并适配到新状态。核心想法是把接触丰富的全身技能从原始示教中抽取出来，在新的物体姿态和机器人 root pose 下重新规划，使生成数据覆盖更多初始条件。与传统 MimicGen 针对机械臂末端轨迹重放不同，类人场景必须同时处理 base placement、legged locomotion、torso/arm coordination 和可达性，因此方法需要在片段拼接时保证前后状态兼容，并避免小的 base 误差让后续操作不可达。论文还引入 G1 Loco-Manipulation benchmark，在 robosuite 和 MuJoCo 上构建模拟 G1 humanoid 任务。摘录没有展开具体优化目标、运动规划器形式和失败恢复策略，因此不能细说公式；可以确定的是，它以“少量真实/专家示教到大量模拟轨迹”的数据生成流程为中心，并进一步通过 sim-and-real co-training 验证生成数据能与有限真实演示互补。

#### 📊 实验与结果

实验包含一个基于 robosuite 和 MuJoCo 的 humanoid loco-manipulation simulation benchmark，使用模拟 G1 humanoid，共 9 个任务。任务沿三个维度变化：base motion 需求从小范围重定位到多阶段导航，物体交互从单臂到双臂和全身交互，执行 horizon 也有差异；每个任务使用二值成功条件，并随机采样物体位姿和机器人 root pose。该设计专门考察 locomotion-manipulation interface，因为 base placement 的小误差就可能让后续 manipulation 不可达。结论还指出，作者通过 sim-and-real co-training 验证 HumanoidMimicGen 生成的模拟数据在结合有限真实演示时能改善真实类人表现。HTML 摘录没有给出具体成功率和提升幅度，因此当前只能确认有真实策略性能验证，不能量化效果。

#### ⚠️ 风险 / 保留意见

- 基准仍以模拟 G1 和 MuJoCo/robosuite 为核心，真实类人部署的接触、平衡和硬件限制可能更复杂。
- 片段组合依赖 whole-body planning，若规划器或可达性判定不稳，生成数据可能含隐性偏差。
- 摘录缺少生成数据规模、真实演示数量和成功率提升，复现前需核查实验细节。

#### 💭 结论与启发

这篇最值得借鉴的是把数据生成从“轨迹扰动”升级为“技能片段与全身规划组合”。如果后续做 humanoid VLA 或移动操作，数据 pipeline 应把 navigation、base placement 和 manipulation success 联合建模，而不是把走路和操作拆成两个孤立模块。读 PDF 时应重点确认生成轨迹如何保持动力学合理性，以及 sim 数据在真实 co-training 中到底提升了哪些任务，因为这决定它是通用数据引擎还是只适用于结构化 benchmark。

#### 🔎 读 PDF 先核查

- HumanoidMimicGen 如何在拼接导航、全身运动和 manipulation 片段时保证状态连续性和接触合理性？
- 生成数据对真实策略性能的提升主要来自更多初始状态覆盖，还是来自更好的 base placement 分布？
- G1 Loco-Manipulation 的 9 个任务中，哪些任务最能区分普通 imitation、MimicGen 变体和 HumanoidMimicGen？

#### 📌 上传 PDF 后优先看

- HumanoidMimicGen 数据生成与 whole-body planning 方法章节
- G1 Loco-Manipulation benchmark 任务定义
- sim-and-real co-training 与真实类人验证实验

### [4]. Colosseum V2: Benchmarking Generalization for Vision Language Action Models [[HTML]](https://arxiv.org/html/2605.27759) [[PDF]](https://arxiv.org/pdf/2605.27759) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.27759`
* **Authors**: Jeremy Morgan, Prajwal Vijay, Hyeonho Oh, Jincen Song, Ashvin Arora, Alina Du, Gaurav Sukhatme, Jesse Thomason, Ishika Singh
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为 Colosseum V2 把 VLA 泛化拆成视觉、语言和动作扰动，并尝试证明模拟评测能预测真实相对表现。
* **关键词**: `VLA benchmark` `generalization` `simulation evaluation` `bimanual manipulation` `sim-to-real proxy`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

#### 📖 背景与动机

VLA 的强视觉和语言理解容易造成一种错觉：只要模型能识别新物体、理解新指令，就能在机器人任务里泛化。Colosseum V2 反驳的正是这个简化叙事。机器人策略的泛化还取决于动作空间、初始状态、接触几何、双臂协调和长程执行，而这些部分很难从互联网级视觉语言预训练中直接继承。现有 benchmark 往往任务少、扰动单一或只覆盖某类机械臂，导致我们很难判断模型到底是语言泛化、视觉泛化，还是仅在训练分布附近做动作复现。Colosseum V2 的价值在于提供一个更系统的模拟评测框架，专门观察 VLA 在 visual、language、action 三条轴上的退化方式，并把单臂与双臂 morphology 都纳入测试。

#### ⚙️ 核心方法

当前摘录能确认 Colosseum V2 是一个大规模、GPU-parallelized simulation benchmark，而不是新 VLA 模型。benchmark 包含 28 个 simulation tasks，覆盖两种 Franka Panda 设置：单臂 parallel-jaw gripper 和双臂 shared workspace。单臂任务类别包括 Pick、Pick & Place、Reorientation、Insertion、Tool Use、Articulated Object Interaction 和 Long-Horizon Manipulation；双臂任务采用相近分类，但强调双臂协调和共享物体操作。方法上的关键是把泛化因素标准化：视觉扰动、语言扰动和动作/初始条件扰动被作为不同评估轴，而任务类别从简单 primitive 到复杂长程行为递进。这样的设计使研究者可以区分模型是在语义理解上失败，还是在高维动作空间与初始条件变化下失败。摘录还显示作者关注 sim-to-real proxy：模拟结果不仅用于排名，还用于预测真实世界相对性能变化。具体扰动参数、资产集和 VLA 接口需要 PDF 核查。

#### 📊 实验与结果

实验覆盖 28 个任务和两种 robot morphology。结论指出，一些模型能较稳健地处理语言扰动，某些情况下也能处理视觉扰动，但在初始条件变化下仍敏感，尤其在更高维动作空间中表现更脆弱。这一点对 VLA 评测很关键：模型可能看起来具备强 VLM 能力，却在动作条件稍变时明显退化。论文还声称模拟结果能够可靠预测真实世界中的相对性能变化，从而支持 Colosseum V2 作为真实评测 proxy 的实用性；不过摘录没有给出相关系数、真实任务数量或具体模型排名。因此当前可确认的是它提供了系统扰动评测和 sim-to-real 排序验证，不能引用具体数值结论。

#### ⚠️ 风险 / 保留意见

- 模拟 benchmark 仍可能低估真实接触、传感噪声和硬件执行误差。
- 如果任务资产和扰动分布有限，模型可能对 Colosseum V2 本身过拟合。
- 摘录没有给出真实世界验证规模，sim-to-real proxy 主张需要读完整实验确认。

#### 💭 结论与启发

这篇适合作为后续 VLA paper review 的评测参照：不要只看平均成功率，要问模型在语言、视觉和动作扰动下分别掉在哪里。做系统实验时，可以借鉴其 task taxonomy，把简单 pick-place 与 insertion、tool use、articulated object、long-horizon 和 bimanual coordination 分开报告。更重要的是，如果它的模拟相对排序确实能预测真实变化，那么它可以成为筛选 VLA checkpoint 和数据策略的低成本前置评估。

#### 🔎 读 PDF 先核查

- Colosseum V2 如何精确定义 visual、language 和 action perturbation，三者是否能独立控制？
- 模拟相对性能预测真实世界变化的验证规模有多大，是否覆盖双臂和长程任务？
- 不同 VLA 模型在初始条件扰动下失败，是因为视觉定位、动作解码还是 closed-loop correction 不足？

#### 📌 上传 PDF 后优先看

- benchmark 任务 taxonomy 与扰动定义章节
- VLA 模型泛化结果表
- sim-to-real 相关性或真实机器人验证实验

### [5]. Turning Video Models into Generalist Robot Policies [[HTML]](https://arxiv.org/html/2605.27817) [[PDF]](https://arxiv.org/pdf/2605.27817) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.27817`
* **Authors**: Sizhe Lester Li, Evan Kim, Xingjian Bai, Tong Zhao, Tao Pang, Max Simchowitz, Vincent Sitzmann
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为 VERA 选择不把视频模型重训成 action head，而是用 Jacobian IDM 把视频计划翻译成动作，路线清晰且有跨 embodiment 潜力。
* **关键词**: `video model policy` `inverse dynamics` `Jacobian IDM` `world model` `embodiment generalization`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

机器人 foundation policy 的一个长期矛盾是：视频模型可能从海量视觉数据中学到丰富的空间和动态先验，但机器人动作数据稀缺、embodiment-specific，直接把动作头接到大模型上容易消耗这些泛化能力。现有 VLA 通常希望通过微调把 vision-language backbone 变成 action predictor，但动作与语言/图像的统计结构差异很大，且不同机器人命令空间不同。本文提出的问题是：能否保留视频模型作为 embodiment-agnostic planner，只训练一个特定机器人的 inverse dynamics model，把预测视频转成可执行动作？如果成立，机器人系统就可以更灵活地替换视频 planner，并把少量 action-labeled/self-play 数据集中用于 video-to-action translator。这对 World Model 与 VLA 的交叉非常关键，因为它把“看见未来”与“执行未来”解耦。

#### ⚙️ 核心方法

论文系统被称为 VERA。当前摘录能确认其结构是视频 planner 加 embodiment-specific inverse dynamics model，其中视频模型负责根据观察历史和目标生成未来视觉计划，IDM 负责从相邻或成段视频变化中恢复机器人动作。作者明确把核心技术挑战定义为 video-to-action problem：机器人不能执行像素，只能执行位置、速度或力矩等命令，因此 translator 必须 faithful、data-efficient，并能随 DoF 增长扩展。方法核心是 Jacobian IDM，实验默认使用 Wan-family 预训练视频模型作为 planner，用 VGGT 初始化的 J-IDM 作为 translator。推理时系统闭环运行：视频模型生成未来 chunk，J-IDM 翻译成 action chunk，机器人执行后再根据新观察重新规划。相对端到端 VLA 的新意是 decoupling：视频 planner 保持相对 embodiment-agnostic，不同视频模型可替换，动作学习集中在机器人特定 IDM 上。摘录没有给出 Jacobian IDM 的完整数学形式，因此不能展开具体雅可比估计公式。

#### 📊 实验与结果

实验评估 VERA 的 closed-loop manipulation，并将 Jacobian IDM 与其他 IDM 变体隔离比较，同时对比 VLA 和 world-action baselines。仿真环境包括 PushT、MimicGen Panda 和 Allegro-Sim cube reorientation；硬件包括 Panda-Real，在 DROID 上 post-training，以及 Allegro-Real dexterous reorientation。作者报告 closed-loop success 和 task progress，并在附录放置 setup 与视频模型消融。摘录中的定性结论是 Jacobian IDM 能较忠实地把 world model 预测的视频 chunk 翻译为机器人可执行 action chunk，并在不同环境中保持执行与生成一致。结论也明确 VERA 仍需要 robot-specific video 用于 planner post-training，并依赖 off-the-shelf optical-flow trackers；HTML 未给出具体成功率，因此不能量化优于基线多少。

#### ⚠️ 风险 / 保留意见

- 仍需要机器人特定视频做 planner post-training，完全零样本 embodiment transfer 不能从摘录确认。
- 依赖光流/追踪器，遮挡、反光、手部自遮挡或高速接触可能影响 IDM 忠实度。
- 视频计划若物理上不可靠，IDM 再忠实也可能执行错误目标。

#### 💭 结论与启发

这篇的最大启发是把 world model policy 拆成可替换 planner 和机器人特定 translator。后续做系统时，可以先用强视频模型产生目标视觉轨迹，再用小数据训练 IDM，而不是急着把动作头塞进大模型。评审或复现时要重点看 J-IDM 是否真的比普通 IDM 在高 DoF 上更稳，以及 video planner 的 post-training 数据需求；如果这两点成立，它会是一条比端到端 VLA 更模块化的 generalist robot policy 路线。

#### 🔎 读 PDF 先核查

- Jacobian IDM 相比普通 IDM 的收益是否主要出现在高 DoF 任务，如 Allegro dexterous reorientation？
- 视频 planner 的 robot-specific post-training 需要多少数据，是否会削弱其 embodiment-agnostic 优势？
- 当视频模型生成物理不可执行或接触错误的未来时，VERA 是否有检测或重规划机制？

#### 📌 上传 PDF 后优先看

- Video-to-Action Problem 与 Jacobian IDM 方法章节
- IDM 变体消融实验
- Panda-Real 和 Allegro-Real 硬件结果

### [6]. SANTS: A State-Adaptive Scheduler for World Action Models [[HTML]](https://arxiv.org/html/2605.27947) [[PDF]](https://arxiv.org/pdf/2605.27947) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.27947`
* **Authors**: Yirui Sun, Guangyu Zhuge, Keliang Liu, Jie Gu, Xinyu Bing, Zhongxue Gan, Chunxu Tian
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为 SANTS 抓住了 World Action Model 的一个细节但关键的问题：动作不一定需要最干净的视频条件，而需要状态自适应的 denoising depth。
* **关键词**: `World Action Model` `adaptive denoising` `scheduler` `diffusion policy` `RoboTwin 2.0`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

World Action Model 通过未来视频表示来条件化动作生成，理论上能把视频模型的时空先验传给机器人控制。但 pixel-space WAM 的推理成本高，因为未来视频通常要经过多步 denoising；更重要的是，视觉越清晰不一定越有利于动作。对 fine-grained manipulation 来说，过晚的 denoising 可能生成更好看的画面，却引入与动作无关甚至物理不可靠的细节。SANTS 的动机来自一个很实际的观察：沿视频 noise trajectory 的 action utility 是 state-dependent 的，不同阶段、不同状态需要不同的视频 refinement 程度。因此问题从“如何生成最真实未来视频”变成“动作分支应在什么中间视频状态上读条件”。这对 WAM 部署很重要，因为它同时影响成功率和推理延迟。

#### ⚙️ 核心方法

SANTS 构建在一个预训练 video-to-action diffusion policy 上，不引入新的机器人策略 backbone。摘录显示其接口是冻结的 video-action Transformer：在某个 noise level 下，policy 维护 video latent，每次 video-denoising forward pass 预测更新 latent 的 flow field，同时提取 video tokens 的 pooled hidden representation 作为 scheduler state。SANTS 不更新 Transformer blocks、video head、action head 或 action denoising process，而只学习调度策略：观察中间表示后，决定是否停止在当前 terminal video state，让 action branch 生成 action chunk；如果不停止，则预测沿剩余 noise axis 前进多远。这个设计把 scheduler learning 与 policy learning 解耦，使不同调度策略在相同 policy capacity 下比较，也让 scheduler 可附着到兼容的 video-action diffusion policy。相对固定 terminal denoising depth 的 WAM，SANTS 的新意在于把 denoising 变成 state-adaptive noise-trajectory control，而不是固定步数的视觉质量优化。

#### 📊 实验与结果

实验先做 offline diagnostic，检查 action utility 是否确实随视频 denoising depth 和状态变化。作者在 RoboTwin 2.0 目标域数据上 fine-tune video-action backbone，并让 action branch 在 shifted flow-matching schedule 的中间 video states 上也能观察条件；随后冻结策略参数，在随机采样、人工 phase-annotated 的片段上扫描七个 video denoising depths。phase 标注只用原始示教视频和机器人运动，覆盖 approach、free-space motion、coarse transport 和 fine phases，用来避免按 depth-scan loss 反向解释。后续实验评估 simulation 与真实机器人上的 closed-loop success/latency，并消融 stopping 与 progression 决策。结论提到 RoboTwin 2.0 和七个真实机器人任务，但 HTML 摘录中的具体延迟数字缺失，因此不能引用。

#### ⚠️ 风险 / 保留意见

- 调度器依赖中间 video features 可表征 action utility，不同 WAM backbone 上泛化性需验证。
- 人工 phase annotation 用于诊断，若阶段划分粗糙，可能掩盖更细粒度的接触状态差异。
- 如果基础 video-action policy 本身训练不足，SANTS 只能选择较好中间状态，不能修复错误动态模型。

#### 💭 结论与启发

这篇对 WAM 设计的启发非常直接：不要默认最终 denoised video 是动作最优条件。后续实现 WAM 时，应暴露中间 video latent/features，并把停止时刻作为策略决策的一部分，这可能同时降低推理成本和减少晚期视觉 hallucination 对动作的干扰。读 PDF 时我会重点看 depth scan 曲线是否在不同任务阶段明显不同，以及真实机器人 latency/success trade-off 是否稳定；如果成立，SANTS 可作为很多 video-action diffusion policy 的轻量插件。

#### 🔎 读 PDF 先核查

- 七个 denoising depths 的 action utility 曲线是否在不同任务 phase 上呈现稳定可解释的最优深度？
- SANTS 的 stopping 和 progression 两个决策分别贡献多少成功率和延迟收益？
- 调度器是否能迁移到不同 video-action backbone，还是需要每个 WAM 单独训练？

#### 📌 上传 PDF 后优先看

- offline depth diagnostic 与 phase-annotated 分析
- SANTS scheduler 方法与冻结 policy interface
- 仿真/真实机器人 success-latency trade-off 和消融实验

## Watchlist

### [W1]. Tabero: Learning Gentle Manipulation with Closed-Loop Force Feedback from Vision, Touch, and Language [[HTML]](https://arxiv.org/html/2605.27886) [[PDF]](https://arxiv.org/pdf/2605.27886)
* **Paper ID**: `2605.27886`
* **Authors**: Qiwei Wu, Rui Zhang, Xin Xiang, Tao Li, Weihua Zhang, Junjie Lai, Renjing Xu
* **Author Priority**: Standard
* **为什么还值得留意**: Tabero 进入 watchlist 是因为它补足了 VLA 在 tactile/force-sensitive manipulation 上的短板，并提出从开源 manipulation 数据迁移到 Isaac Lab、增加触觉信息的 pipeline。它没有进入最终精选，主要因为当前摘录更像 benchmark/model suite 与数据平台工作，和今天最核心的 world model、Sim2Real 闭环、工业部署主线相比优先级略低。值得后续看其 tactile gripper 替换导致的成功率下降如何被模型补偿，以及闭环 force feedback 是否真能提升 gentle manipulation。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)

### [W2]. ProgVLA: Progress-Aware Robot Manipulation Skill Learning [[HTML]](https://arxiv.org/html/2605.28231) [[PDF]](https://arxiv.org/pdf/2605.28231)
* **Paper ID**: `2605.28231`
* **Authors**: Seungsu Kim, Jinyoung Choi, Seungmin Baek, Jean-Michel Renders
* **Author Priority**: Standard
* **为什么还值得留意**: ProgVLA 值得放入 watchlist，因为它关注 compact VLA、长序列压缩和 explicit progress representation，并报告 0.1B 参数模型在 LIBERO、Meta-World 和真实机器人设置中与大模型竞争。它没有进入最终精选，是因为当前主线更强调 VLA 部署、评测闭环和世界模型接口；ProgVLA 更偏高效架构与训练策略。后续应重点核查 progress-aware heads 的实际贡献是否显著，以及是否主要收益来自 DUNE/DINOv3 视觉 backbone 和 Perceiver resampling。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

### [W3]. What Frozen VLAs Already Know About Success: A Probing Study of Value-Like Structure in Foundation Robot Policies [[HTML]](https://arxiv.org/html/2605.28527) [[PDF]](https://arxiv.org/pdf/2605.28527)
* **Paper ID**: `2605.28527`
* **Authors**: Jiachen Zhang (1 and 2), Junnan Nie (1), Junyi Lao (1), Wei Cheng (1), Chenghao Liu (1), Jiaxin Jiang (2), Songfang Huang (1) ((1) Peking University, (2) China Agricultural University)
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇很有研究味道：它探测 frozen VLA 表征里是否已经有 value-like success structure，并在 Pi0.5 的候选 action prefix selection 中报告 push-plate 从 26.7% 到 44.3% 的提升。它没有进入最终精选，是因为它更像 probing/control diagnostic，而不是完整 VLA/world model 系统论文。仍然值得跟踪，因为如果线性 probe 能稳定读出 outcome-derived targets，它可能成为 RL+VLA 中低成本 value guidance 的入口。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. PrimitiveVLA: Learning Reusable Motion Primitives for Efficient and Generalizable Robotic Manipulation [[HTML]](https://arxiv.org/html/2605.28634) [[PDF]](https://arxiv.org/pdf/2605.28634)
* **Paper ID**: `2605.28634`
* **Authors**: Yutai Li, Shaohui Peng, Jiaming Guo, Di Huang, Zihao Zhang, Yuxuan Guo, Yunkai Gao, Siming Lan, Ling Li, Xing Hu, Yunji Chen
* **Author Priority**: Standard
* **为什么还值得留意**: PrimitiveVLA 进入 watchlist 是因为它正面挑战 direct instruction-to-control mapping，主张用 primitive-centric disassemble & assemble 和 Multimodal Canonical Representation 提升数据效率与泛化。它没有进入最终精选，主要因为摘录中的方法依赖 VLM-based semantic decomposer 和 primitive 表述，具体可复现性、分解稳定性与真实收益需要更谨慎核查。后续适合重点看 50% training data 的实验、OOD/long-horizon 设置，以及 primitive disassembly 与 MCR 的单独消融。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
