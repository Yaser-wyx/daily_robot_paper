# RoboPulse | 2026-05-29

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 76 papers scanned · 10 shortlisted · 5 editor's picks

今天的主线很清晰：VLA 论文正在从“更大的通用策略”转向“可部署系统”的关键缺口，包括置信度、真实机器人评测、离线到在线 RL、自监督 3D/动态表征，以及从人类视频扩展机器人数据。最终精选保留了五条互补路线：VLAConf 解决部署时是否可信，PhAIL 解决真实机器人上如何可靠比较，BORA 处理高维灵巧手的 RL 适配，Qwen-VLA 代表统一 embodied foundation model 的规模化方向，Phantom 则给出不用机器人数据训练策略的强信号。VIP 作者里优先跟踪 Yue Wang 相关的 VLA 可靠性线索，以及 Jeannette Bohg 在人类视频到机器人学习上的持续推进；Qwen-VLA 虽只有摘要回退，但按 shortlist 标注也值得后续核查其核心作者与技术报告细节。整体看，今天不是单点能力刷新，而是围绕 VLA 的评估、适配、数据和部署闭环在同步补齐。

## 今日信号

- VLA 的下一阶段竞争点正在从离线 benchmark success rate 转向真实机器人部署中的置信度、延迟、统计显著性和风险控制。
- 3D、动态、时间到成功分布、人类视频编辑等方法都在把“动作相关信息”前移到表征或评测层，而不是只让下游 policy 自己吸收。
- RL+VLA 正在走向更保守的残差式在线适配：先用离线数据稳住语义与动作意图，再用受限的人类介入在线修正真实物理误差。

## Historical Rediscovery

- **Paper**: What Frozen VLAs Already Know About Success: A Probing Study of Value-Like Structure in Foundation Robot Policies [[HTML]](https://arxiv.org/html/2605.28527) [[PDF]](https://arxiv.org/pdf/2605.28527)
  - **Paper ID**: `2605.28527`
  - **来源日期**: 2026-05-28
  - **当时可能被低估的信号**: 当时可能低估了 Pi0.5 候选 action prefix selection 中 push-plate 成功率从 26.7% 到 44.3% 的信号；这说明 probing 不只是解释工具，可能已经能影响动作选择。
  - **为什么现在值得再看**: 现在如果要做 VLA 后训练、test-time reranking 或 World Action Model 风格的动作评估，这篇提供了一个从 frozen policy 中读出 success structure 的切入点，和 RL+VLA、value guidance、真实部署前的低成本策略筛选强相关。
  - **建议动作**: 加入精读
  - **关键词**: `VLA` `RL+VLA` `value guidance` `action prefix selection` `probing`
- **Paper**: PrimitiveVLA: Learning Reusable Motion Primitives for Efficient and Generalizable Robotic Manipulation [[HTML]](https://arxiv.org/html/2605.28634) [[PDF]](https://arxiv.org/pdf/2605.28634)
  - **Paper ID**: `2605.28634`
  - **来源日期**: 2026-05-28
  - **当时可能被低估的信号**: 当时可能低估了 primitive-centric disassemble & assemble 以及 Multimodal Canonical Representation 对数据效率、OOD 和 long-horizon 设置的潜在意义。
  - **为什么现在值得再看**: 如果当前关注 World Action Model 或长时程 VLA，primitive 表示可以作为动作空间压缩和可组合规划的中间层；尤其值得核查 50% training data、OOD/long-horizon 实验和 primitive/MCR 消融。
  - **建议动作**: 加入精读
  - **关键词**: `VLA` `motion primitives` `long-horizon manipulation` `OOD generalization` `action abstraction`
- **Paper**: ProgVLA: Progress-Aware Robot Manipulation Skill Learning [[HTML]](https://arxiv.org/html/2605.28231) [[PDF]](https://arxiv.org/pdf/2605.28231)
  - **Paper ID**: `2605.28231`
  - **来源日期**: 2026-05-28
  - **当时可能被低估的信号**: 当时可能低估了 0.1B 参数模型在 LIBERO、Meta-World 和真实机器人设置中与大模型竞争这一信号，尤其是 progress-aware heads 可能带来的效率收益。
  - **为什么现在值得再看**: 现在 VLA 研究不只需要更大模型，也需要可部署、可监控、能处理长序列的策略结构；progress representation 与 VLA、真实机器人评测和长时程操作高度相关。
  - **建议动作**: 加入精读
  - **关键词**: `VLA` `progress representation` `compact model` `long sequence` `real robot`
- **Paper**: Learning from Trials and Errors: Reflective Test-Time Planning for Embodied LLMs [[HTML]](https://arxiv.org/html/2602.21198) [[PDF]](https://arxiv.org/pdf/2602.21198)
  - **Paper ID**: `2602.21198`
  - **来源日期**: 2026-05-26
  - **当时可能被低估的信号**: 当时可能低估了 reflection-in-action、reflection-on-action、BEHAVIOR-1K 长程任务、人类评价和 oracle reflection 对照这些部署评测信号。
  - **为什么现在值得再看**: 对 VLA/RL 系统来说，真实部署中的失败恢复和测试时调整会越来越关键；这篇虽不直接做低层 VLA policy，但与长时程操作、失败反思、World Model/World Action Model 的高层闭环接口相关。
  - **建议动作**: 快速浏览
  - **关键词**: `long-horizon tasks` `test-time planning` `failure recovery` `embodied LLM` `deployment adaptation`
- **Paper**: Characterizing Vision-Language-Action Models across XPUs: Constraints and Acceleration for On-Robot Deployment [[HTML]](https://arxiv.org/html/2604.24447) [[PDF]](https://arxiv.org/pdf/2604.24447)
  - **Paper ID**: `2604.24447`
  - **来源日期**: 2026-04-28
  - **当时可能被低估的信号**: 当时可能低估了 on-robot deployment 约束本身的研究价值；这些硬件与延迟瓶颈会直接决定 VLA、World Model 或动作模型能否闭环运行。
  - **为什么现在值得再看**: 当前 VLA 和 World Action Model 越来越依赖实时推理、动作重排和多模态编码，部署侧的 XPU profiling 与加速策略会影响模型设计和真实评测可行性。
  - **建议动作**: 快速浏览
  - **关键词**: `VLA` `on-robot deployment` `XPU` `latency` `acceleration`

## Editor's Picks

### [1]. VLAConf: Calibrated Task-Success Confidence for Vision-Language-Action Models [[VIP]] [[HTML]](https://arxiv.org/html/2605.29605) [[PDF]](https://arxiv.org/pdf/2605.29605) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.29605`
* **Authors**: Dehao Huang, Aoxiang Gu, Chengjie Zhang, Bolin Zou, Wenlong Dong, Zilang Cen, Yue Wang, Hong Zhang
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，因为 VLAConf 把 VLA 的“能不能做成”显式转成可校准的任务成功置信度，并且面向离散与连续动作头都可用。
* **关键词**: `VLA confidence` `calibration` `frozen representations` `LIBERO shift` `risk-sensitive robotics`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

#### 📖 背景与动机

VLA 在开放世界 manipulation 中最大的问题之一不是完全不会做，而是系统不知道自己什么时候可能失败。真实部署会遇到分布偏移、长尾物体、遮挡、执行误差和人机协作约束，单纯输出动作无法支持回滚、请求接管或风险敏感决策。已有置信度方法常依赖 ensemble 或动作 token 概率：前者推理代价高，后者更适合离散动作模型，对连续动作或 flow-matching action head 的 VLA 不自然。VLAConf 的动机在于从冻结 VLA 内部表征中抽取与任务成功相关的信号，再把它校准为任务成功概率。这使它更像部署监控层，而不是重新训练一个 policy。由于作者列表包含核心关注作者 Yue Wang，这条线也值得作为 VLA 可靠性方向重点跟踪。

#### ⚙️ 核心方法

当前 HTML 摘录能确认 VLAConf 是一个 representation-level confidence framework：它不从重复采样的分歧或 action-token likelihood 估计信心，而是利用冻结 VLA backbone 的内部特征学习一个成功相关的置信度信号。实验设置里明确使用两个异构 VLA：OpenVLA-OFT 代表离散自回归动作输出，另一个 state-of-the-art generalist VLA 通过 flow matching 输出连续动作；两者在置信度学习时保持冻结。方法的新意在于把“任务是否会成功”作为独立于动作参数化的预测对象，从而跨离散与连续 action head 复用。摘录还提到 online evidence 能在执行过程中进一步改善置信度质量，合理推断其推理流程不是只在初始观测上打分，而是可以随 rollout 追加观测证据更新信心。不过当前摘录没有给出具体校准损失、特征层选择、temperature 或后处理公式，因此这些细节需要上传 PDF 后核查，不能把它描述成某种已知 calibration trick。

#### 📊 实验与结果

实验覆盖两个层面：一是 LIBERO-Goal、LIBERO-Spatial、LIBERO-Object 作为 in-distribution evaluation；二是 LIBERO-Pro 和 LIBERO-Plus 用于 shifted conditions，考察扰动和未见任务下置信度是否仍有信息量。对比项包括 PCA-kmeans 这类 post-hoc OOD baseline，以及其他摘录未完整展开的置信度参考方法；关键设定是 backbones 冻结，避免把提升混同为 policy 再训练效果。HTML 摘录没有给出具体 AUROC、ECE 或成功率数字，因此这里只能保守说：作者声称 VLAConf 在标准 LIBERO 与 shifted benchmarks 上给出更有信息量的任务成功概率，并保持单次前向推理效率。摘录还提到真实机器人实验，但没有足够细节说明任务数量、机器人平台或显著性。

#### ⚠️ 风险 / 保留意见

- 置信度学习依赖冻结表征中已经含有成功相关信息；如果 backbone 对失败模式本身不可分，后验校准可能无能为力。
- HTML 摘录未提供校准指标、置信区间或真实机器人任务细节，部署可信度需要看完整实验表。
- online evidence 的更新方式可能引入延迟或状态依赖，实际安全接管阈值需要单独验证。

#### 💭 结论与启发

这篇对后续系统设计的启发是：VLA 部署不应只做 action generation，还需要一个与 policy 解耦的 success monitor。尤其在连续动作 VLA 和 diffusion/flow action head 逐渐增多后，基于 token probability 的 confidence 会越来越窄。复现时我会优先把它当作 frozen-policy diagnostic module，而不是新 policy；先在 LIBERO shift split 上验证 calibration，再看是否能驱动 early abort、human takeover 或 retry policy。若方法确实单次前向可用，它可以成为 VLA benchmark 的标准附加输出。

#### 🔎 读 PDF 先核查

- VLAConf 具体抽取哪一层或哪几类内部特征来预测任务成功，是否对 OpenVLA-OFT 与连续动作 VLA 使用同一接口？
- 校准目标是 episode-level success、step-level success probability，还是执行过程中累积更新的 success estimate？
- online evidence 如何融合到置信度中，它是在每步重估、滑动窗口聚合，还是显式建模历史状态？

#### 📌 上传 PDF 后优先看

- 方法章节中的 representation-level confidence head、特征选择与校准损失。
- LIBERO-Pro/LIBERO-Plus shifted evaluation 的置信度指标、可靠性图和 ablation。
- 真实机器人实验中的失败预警、阈值选择、延迟与单次前向成本。

### [2]. PhAIL: A Real-Robot VLA Benchmark and Distributional Methodology [[HTML]](https://arxiv.org/html/2605.29710) [[PDF]](https://arxiv.org/pdf/2605.29710) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.29710`
* **Authors**: Sergey Arkhangelskiy
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为 PhAIL 不是又报一个 VLA 成功率，而是直接挑战真实机器人评测的统计方法。
* **关键词**: `real-robot benchmark` `time-to-success CDF` `VLA evaluation` `statistical testing` `human-relative throughput`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

#### 📖 背景与动机

真实机器人 VLA 评测长期依赖固定超时下的二元成功率，通常每个条件 rollout 数有限，也很少给出置信区间或 paired statistical comparison。这个做法在模型差距很大时还能粗略排序，但在 SOTA 间差距接近时，采样噪声足以掩盖真实差异。更麻烦的是，吞吐量、cycle time、completion fraction 与 binary success 经常给出不同排名，而论文通常不会明确说明选择哪个指标更符合任务目标。PhAIL 的价值在于把评测对象从单个 scalar 改成 time-to-success CDF，并把评分与显著性检验拆开：一个用于排名，一个用于判断是否真的可区分。这对 VLA 社区很重要，因为如果评测本身不稳，后续关于 architecture、data 或 RL fine-tuning 的结论都会被噪声污染。

#### ⚙️ 核心方法

PhAIL 提出 Physical AI Leaderboard，是一个基于 Franka FR3 的开放真实机器人 benchmark，并配套 dataset、per-rollout artifacts 和端到端 reference implementation。方法核心是把 time-to-success cumulative distribution function 作为 evaluation primitive：每次 rollout 不只记录是否在固定超时前成功，而是记录完成时间分布。评分端使用 Human-Relative Throughput，即相对于同一 fixture 下人类遥操作参考的无量纲标量，并通过 bootstrap confidence intervals 表达不确定性。显著性端使用 Kolmogorov-Smirnov test，按对象分别计算并 macro-average，从而判断两个 policy 的完成时间分布是否可区分。这个拆分很关键：ranking metric 可以服务 leaderboard，而 statistical test 防止把噪声差异误读成模型优势。HTML 摘录还强调不同 CDF 聚合规则可能给出相反 top-1 排名，说明作者不是只在换指标，而是在暴露真实机器人评测目标本身的多义性。

#### 📊 实验与结果

摘录显示 PhAIL 在四个公开可用 VLA 上、四个对象上进行真实机器人评测。作者报告 macro-averaged KS test 能在二元阈值指标无法可靠区分的 rollout budget 下，解析两个接近比较：GR00T vs. ACT，以及 OpenPI vs. ACT；而最接近的一对 OpenPI vs. GR00T 仍未解析。这个结论比单纯给出谁第一更重要，因为它说明有些模型差异在现有样本量下不该被强行排序。结论部分还指出，同一个 CDF 上的不同 principled aggregation rule 可能产生相反 top-1 排名，进一步证明评测指标选择会影响论文叙事。HTML 摘录没有完整给出每格 rollout 数、四个对象名称或具体 HRT 数字，因此不能扩展成更细的排名表。

#### ⚠️ 风险 / 保留意见

- 平台是 Franka FR3 和特定 fixture，评测方法通用性强，但 leaderboard 结论不应直接外推到所有机器人形态。
- KS test 与 HRT 的任务解释需要社区共识，否则不同聚合规则仍可能服务不同叙事。
- 摘录未完整提供 rollout budget、对象类别和失败处理细节，统计功效需要读完整实现。

#### 💭 结论与启发

这篇最值得借鉴的是评测哲学：真实机器人 VLA 不应该只问“是否成功”，还要问“多快成功、分布如何、差异是否显著”。后续读 VLA 论文时，我会把固定超时成功率视为低维摘要，而不是最终证据。若要搭建内部 benchmark，可以直接参考 PhAIL 的 scoring/test 分离：排行榜指标用于沟通，paired 或 distributional test 用于决策。它也提醒我们，接近模型之间没有显著差异时，诚实报告 unresolved comparison 比强行声称 SOTA 更有价值。

#### 🔎 读 PDF 先核查

- PhAIL 的 HRT 具体如何从 time-to-success CDF 聚合，超时失败在分布中如何处理？
- macro-averaged KS test 在 per-object 层面的样本量、paired/session 控制和多重比较问题如何处理？
- 四个公开 VLA 的执行接口是否统一，低层控制、相机、prompt 和 reset 流程是否会影响公平性？

#### 📌 上传 PDF 后优先看

- 评测方法章节中的 time-to-success CDF、HRT 定义和 bootstrap 置信区间。
- 统计检验章节中的 KS test、per-object macro averaging 与样本量设定。
- 真实机器人 benchmark 描述、per-rollout artifacts 和四个 VLA 的接口适配细节。

### [3]. BORA: Bridging Offline Reinforcement Learning and Online Residual Adaptation for Real-World Dexterous VLA Models [[HTML]](https://arxiv.org/html/2605.30226) [[PDF]](https://arxiv.org/pdf/2605.30226) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.30226`
* **Authors**: Zhongxi Chen, Yifan Han, Yanming Shao, Huanming Liu, Congsheng Xu, Xiaoyu Chen, Yao Mu, Wenzhao Lian
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为 BORA 把 VLA、offline RL 和真实机器人在线残差适配串成了面向灵巧手的完整 post-training pipeline。
* **关键词**: `offline-to-online RL` `dexterous manipulation` `VLA post-training` `residual adaptation` `human-in-the-loop`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

灵巧操作是 VLA 部署中最难的分支之一：高自由度手部控制会放大动作噪声，遮挡和接触使视觉反馈不稳定，而同一个任务又可能有多种可行手姿，导致 imitation learning 很难从演示中抽取唯一且泛化的物理交互意图。VLA 虽能提供语义 grounding，但在真实 dexterous execution 中容易出现 compounding errors，单靠离线模仿很难覆盖硬件误差和接触细节。直接在线 RL 又有样本效率、硬件安全和 temporal inconsistency 风险。BORA 的动机是用 offline RL 先从数据中学习更稳定的 manipulation skill，再通过 Human-in-the-Loop online residual RL 在真实机器人上小幅修正执行误差，避免让高维探索直接冲击硬件。

#### ⚙️ 核心方法

BORA 是一个 two-stage adaptation pipeline。第一阶段是 offline RL post-training，摘录明确提到 action-conditioned critic 和 consistency policy，目标是在高维、多模态连续动作空间中提供更有效的 value guidance。作者批评 generative action architecture 的迭代 denoising 会加剧 credit assignment failure：RL 信号需要穿过很多时序 denoising step，容易在冗余微动作和噪声 action manifold 中累积失真，进而破坏高层 VLM 表征与动作意图的对齐。BORA 因此通过 action-conditioned value guidance 来缓解高维动作生成和视觉遮挡下的价值估计问题。第二阶段是真实机器人上的 HiL online residual RL adaptation：不是重写基础 VLA，而是在部署时学习 residual compensation，用于修正 real-world execution discrepancy。摘录还说 inherited action-conditioned critic 支持 residual policy learning，说明离线 critic 不只是训练后丢弃，而会参与在线 fine-tuning。当前 HTML 摘录未给出具体 RL 算法、critic loss、residual action 参数化或 HiL 触发规则，因此这些需要后续核查。

#### 📊 实验与结果

实验平台为 Franka arm 加 12-DoF dexterous hand，任务包括 Pick the plush toy、Pick and Place、Open the box、Pull the tissue、Press the button。每个任务在标准配置下做 20 trials，并在 novel unseen objects 上再做 20 trials，以考察泛化。作者围绕三个问题组织实验：BORA 是否改善 offline RL post-training，online adaptation 是否样本高效地弥合真实部署差距，以及 action-conditioned critic 是否支持 residual learning。基线建立在预训练 VITRA VLM 上，均采用 VLA 架构，但摘录未完整列出所有 baseline 名称和数值结果。结论声称 extensive evaluations across five complex real-world dexterous tasks demonstrate 有效性，但当前摘录不足以引用具体成功率或提升幅度。

#### ⚠️ 风险 / 保留意见

- 真实机器人在线 residual RL 依然涉及硬件风险，HiL 规则和安全边界若不清晰会影响可复现性。
- 方法绑定 12-DoF dexterous hand 场景，向更高自由度手或不同末端执行器迁移仍需验证。
- 摘录没有完整数值、算法细节和 baseline 表，offline RL 与 online residual 各自贡献需要看消融。

#### 💭 结论与启发

BORA 的启发在于把 VLA fine-tuning 看成“语义策略稳定性”和“物理执行可靠性”的分层问题。对灵巧手而言，完全端到端在线 RL 过于激进，而只做 imitation 又不够贴近接触物理；离线 critic 加在线 residual 是更现实的折中。后续如果复现，我会先关注 action-conditioned critic 是否真的能改善高维动作 credit assignment，再评估 residual policy 是否只在小范围补偿中工作。它也适合和 VLAConf 结合：置信度低或接触异常时触发 residual adaptation 或人类介入。

#### 🔎 读 PDF 先核查

- BORA 的 action-conditioned critic 如何处理 VLA 生成的 action chunk，critic 输入是完整轨迹、当前动作还是 denoising 中间量？
- consistency policy 具体约束什么一致性，是时间一致性、动作分布一致性，还是视觉表征不漂移？
- HiL online residual RL 的人类介入信号是什么，如何限制探索幅度以保护真实硬件？

#### 📌 上传 PDF 后优先看

- offline RL 方法章节中的 action-conditioned critic、consistency policy 和 loss 设计。
- online residual adaptation 章节中的 HiL 机制、residual action 参数化和安全约束。
- 五个真实灵巧任务的主结果、novel object 泛化和逐模块消融。

### [4]. Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments [[VIP]] [[PDF]](https://arxiv.org/pdf/2605.30280) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.30280`
* **Authors**: Qiuyue Wang, Mingsheng Li, Jian Guan, Jinhui Ye, Sicheng Xie, Yitao Liu, Junhao Chen, Zhixuan Liang, Jie Zhang, Xintong Hu, Xuhong Huang, Pei Lin, Junyang Lin, Dayiheng Liu, Shuai Bai, Jingren Zhou, Jiazhao Zhang, Haoqi Yuan, Gengze Zhou, Hang Yin, Ye Wang, Yiyang Huang, Zixing Lei, Wujian Peng, Delin Chen, Yingming Zheng, Jingyang Fan, Xianwei Zhuang, Xin Zhou, Haoyang Li, Anzhe Chen, Tong Zhang, Xuejing Liu, Yuchong Sun, Ruizhe Chen, Zhaohai Li, Chenxu Lü, Zhibo Yang, Tao Yu, Xionghui Chen
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，但需要等完整 HTML/PDF；Qwen-VLA 代表大模型栈试图统一 manipulation、navigation 与多 embodiment action generation 的方向。
* **关键词**: `unified VLA` `Qwen` `DiT action decoder` `joint pretraining` `multi-embodiment`
* **证据来源**: Abstract fallback

#### 📖 背景与动机

具身智能长期被拆成多个专用系统：manipulation 有自己的机器人轨迹数据和 action head，navigation 有 VLN 和路径规划数据，人类 egocentric video 又常被用于观察或表征学习。这种碎片化让模型难以跨任务、跨环境、跨机器人形态泛化，也让 VLA 很难继承通用 VLM 的规模化收益。Qwen-VLA 的问题意识是：能否把这些异质 embodied decision-making problems 放进一个统一 vision-language-action model 中，让同一基础模型既理解视觉语言，又输出连续动作或轨迹。由于当前只有摘要回退，它更像一条 foundation model 方向的重要信号，而不是可完全评估的方法论文。按 shortlist 标注其 VIP tier 为 core，应在 PDF 到位后优先核查作者、数据配方和真实机器人证据。

#### ⚙️ 核心方法

当前摘录只能确认 Qwen-VLA 建立在 Qwen 的 vision-language modeling stack 之上，把原本偏 perception、understanding、reasoning 的能力扩展到 continuous action and trajectory generation。动作侧使用 DiT-based action decoder，这表明它不是简单把动作离散成语言 token，而是用 diffusion-transformer 风格模块生成连续动作或轨迹。训练策略是 large-scale joint pretraining，数据来源包括 robotics manipulation trajectories、human egocentric demonstrations、synthetic simulation data、vision-and-language navigation data、trajectory-centric supervision，以及 auxiliary vision-language 数据。这个设计的新意在于把 VLA 的数据谱系扩展到机器人、人体、仿真、导航和视觉语言辅助任务，而不是只围绕单一机械臂 manipulation。由于摘要没有给出模型尺寸、token/action 表示、DiT 解码步数、embodiment conditioning、坐标系归一化或训练阶段划分，所有关于具体架构接口的判断都必须保守。

#### 📊 实验与结果

摘要声称 Qwen-VLA 研究 across tasks, environments, and robot embodiments 的统一建模，但当前摘录没有给出具体 benchmark、任务数量、机器人平台、成功率或对比结果。因此实验部分只能确认其目标覆盖 heterogeneous embodied decision-making，而不能声称已经在某个具体 benchmark 上达到 SOTA。后续需要重点核查它是否同时报告 manipulation、navigation、human-video transfer 和 simulation-to-real 的结果，以及这些结果是否由同一个 checkpoint 完成。也要看它是否对比专用模型、开源 VLA 和不同数据混合策略，并是否包含真实机器人部署而非只在离线或仿真上验证。

#### ⚠️ 风险 / 保留意见

- 当前只有摘要回退，缺少架构、数据规模、训练算力、评测协议和数值证据。
- 统一模型可能掩盖不同 embodiment 的动作空间差异，接口设计若不透明会难以复现。
- 大规模 joint pretraining 的提升可能来自数据规模而非模型统一性，需要严格消融。

#### 💭 结论与启发

Qwen-VLA 对选题的意义在于提示 VLA foundation model 正在进入“多任务、多数据源、多具身形态统一预训练”阶段。对后续阅读，我不会只看最终平均分，而会重点看 action decoder 如何兼容不同动作空间，以及数据混合是否真的带来跨域迁移。若它能证明同一模型在 manipulation 和 navigation 上都有稳定收益，那么小规模实验室可以考虑复现其数据配方的简化版；若证据不足，则更适合作为趋势观察，而不是短期复现对象。

#### 🔎 读 PDF 先核查

- Qwen-VLA 如何表示不同 robot embodiment 的动作空间，是否有统一 action token、连续轨迹坐标或 embodiment-specific adapter？
- DiT-based action decoder 与 Qwen VLM backbone 的接口是什么，是 cross-attention、latent conditioning 还是端到端联合训练？
- large-scale joint pretraining 中各类数据的混合比例和消融结果是否支持“统一建模”而不只是数据量扩大？

#### 📌 上传 PDF 后优先看

- 模型架构章节中的 Qwen VLM stack、DiT action decoder 和 action/trajectory 表示。
- 数据与训练配方章节中的 robotics、人类视频、仿真、VLN 和辅助 V-L 数据混合。
- 跨任务、跨环境、跨 embodiment 的主结果、消融和真实机器人部署证据。

### [5]. Phantom: Training Robots Without Robots Using Only Human Videos [[VIP]] [[HTML]](https://arxiv.org/html/2503.00779) [[PDF]](https://arxiv.org/pdf/2503.00779) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2503.00779`
* **Authors**: Marion Lepert, Jiaying Fang, Jeannette Bohg
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，因为 Phantom 给出只用人类视频训练闭环机器人策略并零样本上真机的清晰方案，且有 Jeannette Bohg 参与。
* **关键词**: `human videos` `robot-free training` `data editing` `Diffusion Policy` `zero-shot deployment`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

机器人学习的数据瓶颈仍然很硬：teleoperated demonstrations 慢、贵、设备绑定强，规模和多样性都远小于视觉语言模型使用的数据。人类视频天然丰富，包含大量任务意图、物体交互和场景变化，但不能直接当机器人数据用，因为它缺少机器人动作标签，而且人手/手臂外观与机器人末端执行器差异很大。Phantom 的目标是绕过机器人数据采集，把人类第三视角 RGBD 演示转成机器人可用的 observation-action pairs，再训练 closed-loop imitation policy。它重要的地方不是“用视频预训练表征”，而是更进一步尝试从人类视频直接构造机器人训练集，并在没有目标机器人数据的情况下 zero-shot 部署。核心作者 Jeannette Bohg 也使这条 human video for robotics 路线值得持续跟踪。

#### ⚙️ 核心方法

Phantom 假设输入是一组人类 manipulation 视频演示，每帧来自第三视角 RGBD，相应演示使用拇指和食指的 pinch grasp。方法要把每个 human frame 转换为 robot-compatible observation-action pair。动作侧通过 hand pose estimation 推断机器人末端执行器的目标，包括位置、姿态和夹爪开口宽度；摘录明确说姿态使用 6D continuous rotation representation。视觉侧采用 data editing：分割并 inpaint 人类手臂，再 overlay 一个渲染的目标机器人，使训练图像分布尽量接近测试时机器人观测。机器人渲染由 MuJoCo 生成，策略训练使用 Diffusion Policy；Franka 使用 OSC，Kinova 使用 IK 作为低层控制。方法的新意在于把 human-to-robot transfer 具体化为“动作标签生成 + 视觉域编辑”的监督数据构造问题，而不是依赖共采集、人工标注或目标机器人 fine-tuning。当前摘录没有完整说明 hand pose 估计误差处理、相机标定流程和 inpainting 模型细节，需要 PDF 核查。

#### 📊 实验与结果

Phantom 在 Franka 和 Kinova 两种机器人上验证，以展示跨机器人可用性。任务覆盖刚体、可变形物体和多物体 manipulation；作者还强调 zero-shot deployment in novel scenes，即人类视频演示和机器人 rollout 不需要发生在同一环境。实验重点比较不同 data-editing strategy，其中 Hand Inpaint 是 Phantom 的主要方案：训练时分割人类手臂、补全背景，并叠加虚拟机器人。摘录声称展示 strong success rates，但只给出文字没有具体数字，因此不能引用成功率。相对 prior work 的边界也写得较谨慎：作者称据其分析，非 concurrent 已发表工作中没有在无人工标注、只用人类视频的情况下训练可处理刚体、可变形物体和多物体的闭环 imitation policy。

#### ⚠️ 风险 / 保留意见

- 方法假设人类演示为 pinch grasp 且有 RGBD 第三视角，任务形态与夹爪机器人匹配度会限制适用范围。
- hand pose estimation、分割、inpainting 和机器人 overlay 的误差会累积到动作标签与视觉分布中。
- 摘录没有给出具体成功率和失败案例，zero-shot 部署的稳定性需要看完整实验。

#### 💭 结论与启发

Phantom 对数据路线的启发很直接：与其等待更大规模机器人 teleop 数据，不如把丰富的人类视频通过几何和视觉编辑转成可训练的机器人数据。它也提醒我们，human video transfer 的关键不只是表征学习，而是让训练观测看起来像测试机器人观测，同时生成足够可执行的动作标签。复现时我会优先选择夹爪、pinch-like、第三视角 RGBD 容易采集的任务，先验证 hand inpaint + robot overlay 是否比原始人手视频更稳定，再逐步扩展到不同机器人和场景。

#### 🔎 读 PDF 先核查

- Phantom 如何从人手 pose 映射到机器人末端位姿和夹爪宽度，是否需要任务或机器人特定的几何假设？
- Hand Inpaint 与其他 data editing baseline 的差异主要来自去除人手外观，还是来自叠加机器人带来的 test-time visual alignment？
- novel scenes zero-shot 部署中，相机位姿、深度质量和物体类别变化对成功率的影响如何分解？

#### 📌 上传 PDF 后优先看

- 方法章节中的 hand pose estimation、动作标签生成和 6D rotation/action 表示。
- data editing 实验中的 Hand Inpaint、robot overlay、inpainting baseline 对比。
- Franka/Kinova 真实机器人任务结果、novel scene 泛化和失败案例分析。

## Watchlist

### [W1]. 3DVLA: Enhancing Vision-Language-Action Models via 3D Spatial and Instance Understanding [[HTML]](https://arxiv.org/html/2605.29416) [[PDF]](https://arxiv.org/pdf/2605.29416)
* **Paper ID**: `2605.29416`
* **Authors**: Zhongyu Xia, Yousen Tang, Bingqing Wei, Yongtao Wang
* **Author Priority**: Standard
* **为什么还值得留意**: 3DVLA 进入 watchlist，因为它正中 VLA 缺 3D scene understanding 的痛点：multi-view spatial fusion、3D instance module、occlusion geometry prediction 都很贴近真实 manipulation。它没有进最终精选，主要是因为今天精选更需要覆盖置信度、评测、RL 适配、统一模型和人类视频数据这几条系统性主线。后续值得核查其 86.0% LIBERO-Plus zero-shot average success 的评测细节、baseline 公平性和是否真能 plug-and-play 到不同 VLA。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. ElegantVLA: Learning When to Think for Efficient Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2605.29438) [[PDF]](https://arxiv.org/pdf/2605.29438)
* **Paper ID**: `2605.29438`
* **Authors**: Ye Li, Huanan Liu, Kangye Ji, Yuan Meng, Jiajun Fan, Yuansong Wang, Shiyu Qin, Chenglei Wu, Shu-Tao Xia, Zhi Wang
* **Author Priority**: Standard
* **为什么还值得留意**: ElegantVLA 进入 watchlist，因为 VLA 推理延迟和控制频率是部署硬问题，而 phase-adaptive scheduling 用冻结 VLA 学习何时重算、何时复用，很有工程价值。它没有进最终精选，是因为其核心贡献更偏 inference efficiency wrapper，不如 VLAConf/PhAIL/BORA 直接影响可靠性评估和真实适配范式。HTML 已给出 CogACT、GR00T 和 real-world speedup 信号，后续可重点看 scheduler 的训练代价与稳定性。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. VLA-Pro: Cross-Task Procedural Memory Transfer for Vision-Language-Action Models [[PDF]](https://arxiv.org/pdf/2605.29562)
* **Paper ID**: `2605.29562`
* **Authors**: Shengyu Si, Yuanzhuo Lu, Ruimeng Yang, Ziyi Ye, Zuxuan Wu, Yu-Gang Jiang
* **Author Priority**: Standard
* **为什么还值得留意**: VLA-Pro 进入 watchlist，因为把 task-specific LoRA adapters 当作 procedural memories，并在推理时检索融合，是 cross-task generalization 的有趣方向。它没有进最终精选，主要因为当前只有摘要回退，缺少方法和实验细节，无法判断 memory retrieval、dynamic fusion 与 baseline 的真实差异。若 PDF 证明 RoboTwin、RLBench 和 real-world manipulation 上的泛化提升扎实，它可能升级为下一轮重点。
* **证据来源**: Abstract fallback

### [W4]. Gaze2Act: Gaze-Conditioned Vision-Language-Action Policies for Interactive Robot Manipulation [[HTML]](https://arxiv.org/html/2605.30282) [[PDF]](https://arxiv.org/pdf/2605.30282)
* **Paper ID**: `2605.30282`
* **Authors**: Kuangji Zuo, Gen Li, Bofan Lyu, Yanshuo Lu, Boyu Ma, Shijia Han, Xinyu Zhou, Xichen Yuan, Chuhao Zhou, Jiaqi Bai, Geng Li, Jianfei Yang
* **Author Priority**: Standard
* **为什么还值得留意**: Gaze2Act 进入 watchlist，因为 gaze 是语言之外很自然的动态意图通道，尤其适合相似物体选择、局部交互点指定和执行中目标更新。它没有进最终精选，是因为它更像 VLA 人机交互接口创新，而今天最终精选优先保留了更基础的评估、置信度、RL 和数据路线。后续值得看 ego-exo gaze grounding 的鲁棒性，以及 Meta Aria 眼动误差在真实 Unitree G1 任务中的影响。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W5]. DynaFLIP: Rethinking Robotics Perception via Tri-Modal-Dynamics Guided Representation [[HTML]](https://arxiv.org/html/2605.30350) [[PDF]](https://arxiv.org/pdf/2605.30350)
* **Paper ID**: `2605.30350`
* **Authors**: Jusuk Lee, Seungjae Lee, Jonghun Shin, Hoseong Jung, Sungha Kim, Daesol Cho, H. Jin Kim, Jia-Bin Huang, Furong Huang
* **Author Priority**: Standard
* **为什么还值得留意**: DynaFLIP 进入 watchlist，因为它把 image-language-3D flow triplets 用于 dynamics-aware visual pretraining，直接挑战机器人系统过度依赖静态视觉 encoder 的习惯。它没有进最终精选，是因为它更偏 upstream perception representation，而非完整 VLA/action-policy 训练或部署闭环。后续应重点看 simplex-guided multimodal alignment、3D flow 构造质量，以及在 MetaWorld、RLBench、LIBERO 和真实任务上的消融是否支撑“动态表征”这一主张。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
