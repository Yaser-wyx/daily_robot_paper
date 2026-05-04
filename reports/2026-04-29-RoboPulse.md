# RoboPulse | 2026-04-29

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 52 papers scanned · 10 shortlisted · 6 editor's picks

今天的最终精选主线非常集中：VLA 不再被当成“视觉语言直接吐动作”的平面映射器，而是被重新组织成可想象、可分层、可纠错、可异步执行的闭环系统。RISE、DIAL、Libra-VLA 分别代表了想象式策略改进、意图与动作解耦、以及粗到细混合动作空间这三条最活跃的结构路线；PFD 和 DiscreteRTC 则把讨论推进到机制层，追问未来分支到底提供了什么，以及动态任务为何必须边想边做。GS-Playground 入选，是因为高吞吐、照片级视觉和接触稳定性的模拟基础设施，已经开始直接决定 VLA/RL 的上限。VIP 作者在最终精选里并不集中出现，但 shortlist 中 Jiangmiao Pang 的 InternScenes 与 Danfei Xu 参与的 KinDER 仍值得优先跟踪，因为它们分别卡在场景供给和物理推理评测这两个中长期基础设施节点。

## 今日信号

- 今天最值得记住的研究信号是：VLA 正在从“直接生成低层动作”转向“先形成意图、未来或层级结构，再落到控制”的结构化生成范式。
- 今天最值得记住的研究信号是：世界模型的价值不再只看测试时是否显式生成未来，而更看训练期能否提供可蒸馏、可压缩、可用于策略改进的纠错信号。
- 今天最值得记住的研究信号是：Sim2Real 的关键瓶颈正在从单一算法优劣，转向执行机制与数据基础设施，包括异步控制、照片级模拟器和可仿真场景资产供给。

## Editor's Picks

### [1]. RISE: Self-Improving Robot Policy with Compositional World Model [[HTML]](https://arxiv.org/html/2602.11075) [[PDF]](https://arxiv.org/pdf/2602.11075) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2602.11075`
* **Authors**: Jiazhi Yang, Kunyang Lin, Jinwei Li, Wencong Zhang, Tianwei Lin, Longyan Wu, Zhizhong Su, Hao Zhao, Ya-Qin Zhang, Li Chen, Ping Luo, Xiangyu Yue, Hongyang Li
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把“VLA 如何安全地做在线强化学习”具体化成一条可扩展的想象式自我改进路线。
* **问题与切口**: 这篇工作的切口很准：它不直接在真实机器人上做高风险、难复位的 on-policy RL，而是把策略改进搬到“想象环境”里完成。核心新意在于提出一个组合式世界模型，把多视角未来预测和任务进度价值评估分开建模，再把两者接入闭环自我提升流程。相对只靠模仿学习补数据覆盖，或直接用 PPO 一类方法硬做在线微调，这条路线更像是在给 VLA 补一个可恢复、可试错的内部训练场。
* **核心方法与证据**: 方法上，RISE 用 controllable dynamics model 预测多视角未来，再用 progress value model 对想象结果打分，生成可用于策略提升的 advantage 信号；作者强调这种组合式设计允许状态建模与价值建模分别采用更合适的架构和目标。证据层面，HTML 摘录显示其与 VLA 基线、DAgger、PPO、DSRL、RECAP 在接近算力预算下对比，并报告在线适配型方法存在明显不稳定，而 RISE 在成功率和阶段性评分上更稳，但详细增益边界仍需 PDF 核查。
* **正文要点**:
  - 组合式世界模型将未来预测与进度价值评估拆开，而不是用单一模型同时承担两类职责。
  - 训练闭环以 imagined rollouts 替代真实物理环境中的高成本探索，目标是实现持续自我改进。
  - 实验对比覆盖模仿学习、交互纠偏、在线 RL 与离线 RL 路线，但 HTML 摘录未展开完整任务拆解与误差来源。
* **为什么值得跟**:
  - 它直指 VLA 在动态、接触密集操作中最核心的鲁棒性缺口。
  - 它把世界模型从“辅助表征器”推进成“策略提升器”，这对 RL+VLA 很关键。
  - 如果这条路线成立，真实机器人上的试错成本可以被显著转移到想象训练中。
* **风险 / 保留意见**:
  - 想象轨迹与真实执行之间的模型偏差如何累积，HTML 摘录给出的证据还不够充分。
  - 真实收益可能高度依赖 progress value 的质量与多视角预测的稳定性，复现门槛不低。
* **建议先看**: 先看组合式世界模型如何定义未来预测与进度价值的接口，再看它怎样把 imagined outcomes 变成 advantage。随后重点核查与 PPO、DSRL、DAgger 的对比，判断“稳定性提升”是否来自世界模型本身而非训练技巧。
* **关键词**: `VLA` `World Model` `Imagination RL` `Manipulation Robustness` `Policy Improvement`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - progress value model 的监督信号与归一化方式是什么，是否会把阶段定义的人为偏置带进策略学习？
  - 在持续自我改进过程中，作者如何抑制 imagined rollout 的分布漂移与优势估计失真？
  - 最终收益主要来自多视角未来预测、价值分解，还是闭环数据刷新机制本身？
* **上传 PDF 后优先看**:
  - 方法章节中关于组合式世界模型与 advantage 构造的定义
  - 实验章节里与 PPO、DSRL、DAgger、RECAP 的主对比与稳定性描述
  - 消融或限制性分析中关于 imagination horizon、模型偏差与真实迁移的讨论

### [2]. DIAL: Decoupling Intent and Action via Latent World Modeling for End-to-End VLA [[HTML]](https://arxiv.org/html/2603.29844) [[PDF]](https://arxiv.org/pdf/2603.29844) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.29844`
* **Authors**: Yi Chen, Yuying Ge, Hui Zhou, Mingyu Ding, Yixiao Ge, Xihui Liu
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它给端到端 VLA 提出了一种比“VLM 编码后直接出动作”更有结构感的解法。
* **问题与切口**: DIAL 的核心判断是，现有端到端 VLA 过度把预训练 VLM 当成多模态编码器使用，既浪费了高层决策能力，也容易在动作训练中破坏语义表征。它因此把问题拆成“意图形成”和“动作执行”两段：前者由 VLM 通过潜在世界建模生成未来子目标式的 latent intent，后者再把这个意图落到高频控制。相对传统层级规划器，它试图保留端到端可微；相对平面式 action head，它强调语义与执行的角色分工。
* **核心方法与证据**: 方法上，DIAL 采用双系统结构：System-2 负责处理语言、视觉与本体状态，并通过 latent world modeling 生成预测性视觉意图；System-1 则作为基于 flow matching 的反应式策略，对比当前观测与该意图，输出 action chunk。证据层面，HTML 摘录显示其在 RoboCasa GR1 Tabletop 和 IRON-R01-1.11 humanoid 上评估，真实任务覆盖跨形态学习与多阶段协调两类场景，包括 pick-place、pouring、handover、trash collection，但具体提升幅度仍需 PDF 核查。
* **正文要点**:
  - 模型以可微的 latent intent bottleneck 显式分隔高层认知与低层执行。
  - System-2 不直接产出离散计划文本，而是产出带未来指向性的潜在视觉意图。
  - 真实机器人实验同时覆盖来自 EgoDex 的跨形态模仿数据和机器人原生多阶段序列。
* **为什么值得跟**:
  - 它为“VLM 在机器人里到底该做推理还是做编码”提供了更清晰的结构答案。
  - 这类意图-动作解耦设计更适合高维、全身、长时程控制任务。
  - 如果 latent intent 学得稳定，端到端 VLA 有机会兼顾语义泛化和执行精度。
* **风险 / 保留意见**:
  - HTML 摘录没有充分展开 latent intent 的可解释性与错误传播模式。
  - 真实验证集中在单一平台和有限任务集合上，跨平台泛化仍需谨慎判断。
* **建议先看**: 先看 System-2 到 System-1 的接口设计，尤其 latent visual foresight 到 action chunk 的落地方式。再检查真实任务中哪些场景真正需要高层意图约束，避免把纯数据规模效应误读成结构优势。
* **关键词**: `VLA` `Latent World Model` `Intent-Action Decoupling` `Humanoid Manipulation` `Flow Matching`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - latent visual foresight 的表示形式与训练目标是什么，它如何避免退化成普通特征瓶颈？
  - 当高层意图判断失误时，System-1 是否具有局部纠偏能力，还是只能忠实执行？
  - 跨形态 EgoDex 数据与机器人原生多阶段数据各自贡献了多少性能提升？
* **上传 PDF 后优先看**:
  - 方法章节里 dual-system 架构与 latent intent bottleneck 的定义
  - 真实机器人实验章节中四类任务与数据来源的拆分比较
  - 消融章节中与直接动作生成或非可微层级方案的对比

### [3]. Libra-VLA: Achieving Learning Equilibrium via Asynchronous Coarse-to-Fine Dual-System [[HTML]](https://arxiv.org/html/2604.24921) [[PDF]](https://arxiv.org/pdf/2604.24921) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.24921`
* **Authors**: Yifei Wei, Linqing Zhong, Yi Liu, Yuxiang Lu, Xindong He, Maoqing Yao, Guanghui Ren
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把 VLA 的动作生成问题重新表述成一个粗到细、离散加连续的学习平衡问题。
* **问题与切口**: Libra-VLA 反对当前 VLA 常见的单体式动作生成范式，认为复杂操作天然存在层级结构，不该把宏观到达方向和微观姿态对齐混在同一个高频动作流里学。它提出基于 Hybrid Action Space 的 coarse-to-fine 双系统，把离散宏观意图与连续微调残差分开处理，并进一步提出“Libra Point”这一学习均衡概念，试图找到粗细两阶段难度最平衡的粒度。对 VLA 来说，这是一种兼顾可学性、精度与实时性的结构重写。
* **核心方法与证据**: 从 HTML 摘录看，Libra-VLA 以 InternVL2.5-2B 为 VLM 骨干，设置 Parallel Coarse-Action Head 与 Fine-Action Head，并在 Action Refiner 中使用 SigLIP 视觉编码器；作者强调仿真与真实实验均未使用大规模机器人数据预训练。证据上，论文在 LIBERO、LIBERO-Plus 与真实世界任务上评估精度与鲁棒性，并在结论中声称取得领先成功率和更低推理延迟，但“Libra Point”如何被选定、是否跨任务稳定，仍需正文细查。
* **正文要点**:
  - 动作空间被拆成离散的 macro-intent 与连续的 micro-residual，而非平面式统一回归。
  - 论文明确把“粒度平衡”当作核心问题，并以 Libra Point 命名这一均衡点。
  - 作者强调结果是在没有大规模机器人数据预训练的条件下获得的。
* **为什么值得跟**:
  - 它把 VLA 的语义-执行鸿沟具体落到动作空间设计与学习难度分配上。
  - 如果粗细分层成立，VLA 在精细操作和实时控制之间的权衡会更可控。
  - 不依赖大规模机器人预训练而取得强结果，这一点对资源受限团队尤其重要。
* **风险 / 保留意见**:
  - Libra Point 可能依赖任务分布与机器人形态，未必是可迁移的统一规律。
  - 真实实验细节在摘录中较少，实时性与鲁棒性结论仍需更完整证据支撑。
* **建议先看**: 先沿着 Hybrid Action Space 和 Libra Point 这条主线读，判断作者到底是在做结构创新还是在做粒度调参。随后再核查延迟、鲁棒性与无大规模预训练三者之间是否存在隐含取舍。
* **关键词**: `VLA` `Hybrid Action Space` `Coarse-to-Fine` `Dual-System` `Real-Time Control`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
* **读 PDF 先核查**:
  - Libra Point 是通过理论分析、经验扫描还是自动搜索得到的，跨任务是否稳定？
  - 粗到细分解在遇到突发接触或执行偏差时，是否会削弱在线恢复能力？
  - 延迟下降主要来自动作分层设计，还是来自模型规模与头部结构的变化？
* **上传 PDF 后优先看**:
  - 方法章节中 Hybrid Action Space 与 Libra Point 的定义和选择依据
  - 实验章节里 LIBERO 与 LIBERO-Plus 的鲁棒性比较
  - 真实世界与延迟分析章节中的实时控制证据

### [4]. Privileged Foresight Distillation: Zero-Cost Future Correction for World Action Models [[HTML]](https://arxiv.org/html/2604.25859) [[PDF]](https://arxiv.org/pdf/2604.25859) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.25859`
* **Authors**: Pengcheng Fang, Hongli Chen, Xiaohao Cai
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它正面回答了一个关键争议：世界动作模型里的未来分支，到底只是正则化，还是在教动作纠错。
* **问题与切口**: 这篇论文的价值不只在于提出一个技巧，而在于它试图重新解释 world action model 中“联合预测未来视频与动作”这件事的作用机制。作者不同意“未来分支只是训练期正则器”的读法，转而提出 future-as-correction 视角：未来观测为动作去噪提供了可压缩的、动作条件化的修正信息。基于此，PFD 在训练时保留一个能看见未来的 privileged path，把这部分纠错残差蒸馏给 current-only 路径的小型适配器，推理时不再需要未来分支。
* **核心方法与证据**: 方法上，PFD 使用同骨干 teacher-student 结构：Mixture-of-Transformers 同时包含视频 expert 与动作 expert，通过不同 joint attention mask 区分 privileged 与 student 路径；两条流都采用 flow matching，而 current-only 路径额外接一个输出侧 adapter 去吸收 foresight residual。证据方面，HTML 摘录显示评测覆盖 LIBERO 与 RoboTwin 2.0，并与 released/reproduced Fast-WAM 及多种已发布方法比较；结论还提到三类 epistemic probes，但具体 probe 结果需要 PDF 才能完整判断。
* **正文要点**:
  - 论文把争议焦点从“未来是否需要在测试时显式生成”转向“未来在训练期是否提供动作特异的纠错”。
  - 训练时存在可见未来的 privileged path，但推理时仅保留 current-only path 与小型 adapter。
  - 作者使用 matched-capacity、reproduced baseline 与 probes 的框架来支持机制性主张。
* **为什么值得跟**:
  - 它为世界动作模型中未来分支的存在价值提供了更细的机制解释。
  - 如果蒸馏式纠错成立，就能在不增加推理成本的前提下保留训练期未来信息的好处。
  - 这类分析会影响后续 WAM/VLA 架构到底该删未来分支、保未来分支，还是蒸馏未来分支。
* **风险 / 保留意见**:
  - 核心结论对 teacher-student 掩码设计与复现实验设置可能较敏感。
  - HTML 摘录没有给出全部 probe 细节，因此“因果解释已被充分验证”这一点仍需保守看待。
* **建议先看**: 先抓住作者的概念转向：future-as-regularizer 与 future-as-correction 的区别是什么。然后再去看 teacher-student mask、adapter 容量和 probe 设计，判断这是不是一个真正的机制发现，而不只是训练技巧包装。
* **关键词**: `World Action Model` `Privileged Distillation` `Future Correction` `Flow Matching` `LIBERO`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - foresight residual 在实现上如何定义，才能与普通表征正则化清晰区分？
  - adapter 的容量上限在哪里，超过什么规模后“零成本未来纠错”就不再成立？
  - 未来纠错收益主要集中在哪类任务：长时程、多臂协同，还是随机化场景？
* **上传 PDF 后优先看**:
  - 方法章节里 teacher-student 掩码、残差定义与 adapter 设计
  - 与 Fast-WAM 的主对比及 reproduced baseline 的设定
  - probe 或消融章节中对 future-as-regularizer 与 future-as-correction 的区分证据

### [5]. DiscreteRTC: Discrete Diffusion Policies are Natural Asynchronous Executors [[HTML]](https://arxiv.org/html/2604.25050) [[PDF]](https://arxiv.org/pdf/2604.25050) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.25050`
* **Authors**: Pengcheng Wang, Kaiwen Hong, Chensheng Peng, Katherine Driggs-Campbell, Masayoshi Tomizuka, Chenfeng Xu, Chen Tang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把“机器人为什么不能像聊天模型那样一段段想完再动”讲成了一个很清楚的执行机制问题。
* **问题与切口**: DiscreteRTC 的核心观点很强：对物理智能来说，同步式 action chunk 执行的致命问题不是推理慢，而是每次 chunk 切换都要求机器人停下来等新动作，这在动态任务中会直接造成失败。作者因此把异步执行视为结构需求，而不是工程优化；进一步指出，RTC 虽能把切换重写成 inpainting，但基于 flow matching 的实现并不天然适配。离散扩散策略因为原生具备 inpainting 特性，更适合在“边执行边生成”的设定下稳定续写动作。
* **核心方法与证据**: 证据上，作者在 RTC 官方代码与数据集上实现离散扩散版本，并保持优化器、学习率、训练轮数和主体网络规模一致，只把输出头改为 logits，配合简单的动作量化。实验首先在 Kinetix 动态仿真基准上进行，并通过向动作注入高斯噪声强化闭环修正需求；比较对象覆盖 Naive Async、BID、RTC 以及连续/离散两类动作头。结论段进一步声称真实场景也有收益，且可与 VLASH 叠加，但具体增益拆解仍需 PDF。
* **正文要点**:
  - 论文把异步执行定义为动态任务中的结构必要条件，而不是纯粹的低延迟技巧。
  - 作者认为 flow-matching RTC 的 inpainting 主要来自推理时修补，因此难以从预训练中天然获益。
  - 实现上尽量控制变量，只在动作头与离散化建模方式上做关键替换。
* **为什么值得跟**:
  - 它把社区关注点从“多快出下一段动作”转向“切换时动作是否连续且有效”。
  - 离散扩散若真能天然支持 chunk inpainting，会影响后续动作生成范式选择。
  - 该思路与现有方法可组合，具备较强工程落地潜力。
* **风险 / 保留意见**:
  - 当前实现使用较朴素的量化方案，作者自己也承认这会形成性能上限。
  - 结论能否推广到更高维、更接触密集的操作任务，还需要更广泛验证。
* **建议先看**: 先读清楚作者对同步执行、Naive Async 与 RTC 的结构性批判，再看为什么离散扩散的 native inpainting 能替代额外修补机制。随后重点核查量化粒度、推理成本和真实任务连续性之间的关系。
* **关键词**: `Asynchronous Execution` `Discrete Diffusion Policy` `RTC` `Chunk Inpainting` `Dynamic Tasks`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 性能对动作量化粒度有多敏感，简单分桶是否会在精细控制上迅速失效？
  - 离散扩散的原生 inpainting 优势在高自由度、接触密集任务中是否仍然成立？
  - 最终收益有多少来自异步执行机制本身，而不是离散动作头替换后的建模偏好？
* **上传 PDF 后优先看**:
  - 方法章节中对 RTC 与连续 flow-matching 结构失配的论证
  - Kinetix 基准与异步基线设置，尤其是动作噪声注入协议
  - 量化、推理成本与真实世界 chunk 连续性的消融分析

### [6]. GS-Playground: A High-Throughput Photorealistic Simulator for Vision-Informed Robot Learning [[HTML]](https://arxiv.org/html/2604.25459) [[PDF]](https://arxiv.org/pdf/2604.25459) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.25459`
* **Authors**: Yufei Jia, Heng Zhang, Ziheng Zhang, Junzhe Wu, Mingrui Yu, Zifan Wang, Dixuan Jiang, Zheng Li, Chenyu Cao, Zhuoyuan Yu, Xun Yang, Haizhou Ge, Yuchi Zhang, Jiayuan Zhang, Zhenbiao Huang, Tianle Liu, Shenyu Chen, Jiacheng Wang, Bin Xie, Xuran Yao, Xiwa Deng, Guangyu Wang, Jinzhi Zhang, Lei Hao, Zhixing Chen, Yuxiang Chen, Anqi Wang, Hongyun Tian, Yiyi Yan, Zhanxiang Cao, Yizhou Jiang, Hanyang Shao, Yue Li, Lu Shi, Bokui Chen, Wei Sui, Hanqing Cui, Yusen Qin, Ruqi Huang, Lei Han, Tiancai Wang, Guyue Zhou
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它不是单点算法，而是在尝试重做视觉驱动机器人学习所需的模拟基础设施底座。
* **问题与切口**: GS-Playground 解决的是一个越来越硬的基础问题：视觉驱动的机器人学习需要大规模并行模拟，但高保真渲染、仿真资产制作和接触物理稳定性三者往往彼此掣肘。论文试图把这三件事重新捆在一起，构建一个兼顾照片级视觉、并行物理与 real-to-sim 工作流的多模态模拟平台。相对传统大规模模拟器偏重本体感觉和低成本渲染，这项工作更像是为 vision-informed RL、VLA 乃至 VLN 搭数据引擎，而不是只提供一个更好看的环境。
* **核心方法与证据**: 从摘录可见，作者以一套覆盖视觉与几何保真、物理稳定性、操作能力和运动能力的综合基准评估系统。实验中特别给出两类物理稳定性压力测试：一是用 Newton’s Cradle 比较硬接触下的动量传递与能量耗散，二是在 10ms 步长下测试 Spot 模型无控制输入时的基座稳定性；结论段还声称其在照片级渲染、并行 physics stepping 和 Sim2Real transfer 上表现突出。与此同时，作者明确承认 3D Gaussian Splatting 在随机光照和阴影处理上仍有限制。
* **正文要点**:
  - 平台评估不只看渲染效果，还系统覆盖接触稳定性、操作与运动任务。
  - 硬接触与大步长稳定性测试说明作者把物理求解器鲁棒性当成核心卖点。
  - 限制性讨论明确指出 Gaussian Splatting 对随机光照与阴影建模仍然薄弱。
* **为什么值得跟**:
  - 视觉型 RL 和 Sim2Real 的上限，越来越受制于模拟器是否能同时提供逼真视觉与稳定接触。
  - 如果平台真能兼顾高吞吐与照片级效果，它会直接影响 VLA 数据生成和评测方式。
  - 它把“模拟器论文”从环境工具推向了训练范式的一部分。
* **风险 / 保留意见**:
  - 光照与阴影随机化能力受限，可能削弱其作为鲁棒性训练平台的泛化价值。
  - 平台级结果未必能直接转化成跨任务、跨算法的稳定收益，仍需更多下游验证。
* **建议先看**: 先抓平台最硬的两条主线：渲染吞吐与接触稳定性是否真的被同时兼顾。接着再看 real-to-sim 与下游策略实验，判断这是不是一个能真正喂养 VLA/RL 的数据基础设施，而不只是展示性平台。
* **关键词**: `Sim2Real` `Photorealistic Simulation` `3D Gaussian Splatting` `Robot Learning Infrastructure` `Physics Stability`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
* **读 PDF 先核查**:
  - real-to-sim 流程如何与物理参数校准衔接，避免只在视觉上逼真而在接触上失真？
  - 当分辨率、环境数量和物理复杂度同时上升时，吞吐与保真之间的拐点在哪里？
  - 平台带来的 Sim2Real 收益是否能稳定迁移到不同操作与运动任务，而不只限于展示案例？
* **上传 PDF 后优先看**:
  - 系统设计章节中关于渲染、物理与资产管线的整体架构
  - 物理稳定性与求解器鲁棒性实验，尤其是硬接触与大步长测试
  - Sim2Real 转移与限制性讨论，特别是光照和阴影问题

## Watchlist

### [W1]. Genie Sim 3.0 : A High-Fidelity Comprehensive Simulation Platform for Humanoid Robot [[HTML]](https://arxiv.org/html/2601.02078) [[PDF]](https://arxiv.org/pdf/2601.02078)
* **Paper ID**: `2601.02078`
* **Authors**: Chenghao Yin, Da Huang, Di Yang, Jichao Wang, Nanshu Zhao, Chen Xu, Wenjun Sun, Linjie Hou, Zhijun Li, Junhui Wu, Zhaobo Liu, Zhen Xiao, Sheng Zhang, Lei Bao, Rui Feng, Zhenquan Pang, Jiayu Li, Qian Wang, Maoqing Yao
* **Author Priority**: Standard
* **为什么还值得留意**: Genie Sim 3.0 进入 shortlist，主要因为它把高保真仿真平台、LLM 驱动场景生成和统一 benchmark 组合到了一起，方向上与 VLA 数据供给和 Sim2Real 基础设施高度相关。它没有进入最终精选，是因为当前摘录更像平台与工具链宣言，直接面向 VLA/世界模型方法论的研究张力略弱；同时 HTML 中大量引用占位符和实验细节缺口，也让证据强度不如今天入选的几篇。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)

### [W2]. InternScenes: A Large-scale Simulatable Indoor Scene Dataset with Realistic Layouts [[VIP]] [[HTML]](https://arxiv.org/html/2509.10813) [[PDF]](https://arxiv.org/pdf/2509.10813)
* **Paper ID**: `2509.10813`
* **Authors**: Weipeng Zhong, Peizhou Cao, Yichen Jin, Li Luo, Wenzhe Cai, Jingli Lin, Hanqing Wang, Zhaoyang Lyu, Tai Wang, Bo Dai, Xudong Xu, Jiangmiao Pang
* **Author Priority**: Core VIP
* **为什么还值得留意**: InternScenes 值得持续盯，因为它补的是 embodied AI 最稀缺的“可仿真、真实且杂乱”的大规模室内场景供给，而且有核心作者 Jiangmiao Pang 加持。之所以只放 watchlist，是因为它更偏数据集与 benchmark 基座，当前实验重心在场景生成和导航挑战展示，对 VLA、世界模型或策略学习本体的直接推进还不够强。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

### [W3]. KinDER: A Physical Reasoning Benchmark for Robot Learning and Planning [[VIP]] [[HTML]](https://arxiv.org/html/2604.25788) [[PDF]](https://arxiv.org/pdf/2604.25788)
* **Paper ID**: `2604.25788`
* **Authors**: Yixuan Huang, Bowen Li, Vaibhav Saxena, Yichao Liang, Utkarsh Aashu Mishra, Liang Ji, Lihan Zha, Jimmy Wu, Nishanth Kumar, Sebastian Scherer, Danfei Xu, Tom Silver
* **Author Priority**: Extended VIP
* **为什么还值得留意**: KinDER 是一篇很像“未来会被频繁引用”的 benchmark 论文：25 个程序生成环境、13 个 baseline、面向物理推理的统一评测框架，而且有 Danfei Xu 参与，学术关注度不低。它没进最终精选，不是因为不重要，而是因为今天的主线更偏 VLA 结构、世界模型机制和 Sim2Real 执行闭环；KinDER 更偏评测基础设施，和主线的直接方法贡献稍弱。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

### [W4]. ANCHOR: A Physically Grounded Closed-Loop Framework for Robust Home-Service Mobile Manipulation [[HTML]](https://arxiv.org/html/2604.25323) [[PDF]](https://arxiv.org/pdf/2604.25323)
* **Paper ID**: `2604.25323`
* **Authors**: Jinhao Jiang, Shengyu Fang, Sibo Zuo, Yujie Tang, Yirui Li
* **Author Priority**: Standard
* **为什么还值得留意**: ANCHOR 进入 shortlist，是因为它抓住了真实家居 OVMM 中最常见也最致命的问题：符号计划与持续变化的物理世界不一致，并提出了 operability-aware base alignment 与局部异常处理的闭环框架。它没有进入最终精选，主要因为这更像一个面向开放词汇移动操作的模块化系统整合方案，而不是今天更优先的 VLA/世界模型/异步执行方法突破；实验也集中在少数真实环境与任务层级，外推空间仍待观察。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)
