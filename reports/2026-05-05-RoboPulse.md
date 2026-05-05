# RoboPulse | 2026-05-05

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 132 papers scanned · 10 shortlisted · 6 editor's picks

今天这组最终精选高度集中在一个主线：把 VLA 从“会做任务”推进到“能在真实部署里稳定做对任务”，核心抓手分别是自适应推理、长程分解、世界模型训练机制重解释，以及高精度 sim2real 落地。入选论文共同特点不是单纯再提成功率，而是直接处理真实机器人最痛的几类瓶颈：推理时延、复合任务误差累积、未来预测分支到底有没有用，以及毫米级控制下的迁移失真。作者跟踪上，优先看 Dorsa Sadigh 的 HandelBot，它代表高精度灵巧操作的现实落地；扩展名单里 Dieter Fox 参与的 MolmoAct2 也应持续跟踪，因为它明显瞄准开源可部署 VLA 的平台位。若看后续趋势，Jiangmiao Pang 的 Robo3R 虽未入终选，但在“几何感知先行”这条支线仍值得持续观察。

## 今日信号

- 今天最值得记住的研究信号是：VLA 正从统一大模型叙事转向“按需思考”的系统设计，是否在合适时刻触发更深推理，正在成为部署成败的关键变量。
- 今天最值得记住的研究信号是：长程操作的突破点不再只是更大预训练，而是把子目标生成、执行监测和误差纠偏显式做成闭环。
- 今天最值得记住的研究信号是：world model 与 sim2real 两条线正在靠拢，前者开始追问训练中未来信息真正贡献了什么，后者则更强调如何把这些表征变成低成本、可迁移、可校正的真实控制能力。

## Editor's Picks

### [1]. MolmoAct2: Action Reasoning Models for Real-world Deployment [[VIP]] [[HTML]](https://arxiv.org/html/2605.02881) [[PDF]](https://arxiv.org/pdf/2605.02881) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.02881`
* **Authors**: Haoquan Fang, Jiafei Duan, Donovan Clay, Sam Wang, Shuo Liu, Weikai Huang, Xiang Fan, Wei-Chuan Tsai, Shirui Chen, Yi Ru Wang, Shanli Xing, Jaemin Cho, Jae Sung Park, Ainaz Eftekhar, Peter Sushko, Karen Farley, Angad Wadhwa, Cole Harrison, Winson Han, Ying-Chun Lee, Eli VanderBilt, Rose Hendrix, Suveen Ellawela, Lucas Ngoo, Joyce Chai, Zhongzheng Ren, Ali Farhadi, Dieter Fox, Ranjay Krishna
* **Author Priority**: Extended VIP
* **一句话结论**: 值得优先看，它不是再堆一个 VLA，而是把“开放、可部署、可推理、可迁移”几件现实约束放到同一系统里统一解决。
* **问题与切口**: 这篇工作瞄准当下 VLA 最现实的落差：闭源前沿模型难复现，开源替代常依赖昂贵硬件，加入推理后又容易把延迟拉到不可用。MolmoAct2 的切口很明确，不把“会思考”当成附加展示，而是围绕真实部署重做动作推理模型栈，包括更偏空间/具身理解的骨干、可解释但高效的 thinking 变体，以及跨异构平台的迁移能力。相对已有路线，它强调的是开源与工程可用性的同时成立。
* **核心方法与证据**: 从 HTML 摘录看，方法上它以 Molmo2-ER 为初始化骨干，保留 Molmo2 的视觉语言架构，用 SigLIP2 ViT 编码视觉输入，再通过连接器把图像或视频特征压到语言模型 token 空间，并与指令及机器人文本元数据交织输入。正文可见作者同时区分普通模型与 MolmoAct2-Think，后者主打自适应深度推理。证据边界上，摘录明确提到其在仿真与真实环境评测、少量示范微调和跨平台迁移上都优于强基线，但这里没有展开完整数表，因此更稳妥的判断是：论文已展示较强部署导向证据，具体幅度需看 PDF。
* **正文要点**:
  - 模型核心建立在面向空间与具身推理专门化的 Molmo2-ER 骨干之上，而不是直接套用通用 VLM。
  - 视觉连接器显式利用不同 ViT 层特征，并对图像与视频采用不同的池化压缩策略，说明作者在控制时延与信息保真之间做了工程权衡。
  - 真实世界微调设置、固定相机顺序、机器人专属数据与 50K 更新等细节在 HTML 中可见，说明部署实验不是只停留在概念验证。
* **为什么值得跟**:
  - 它代表开源 VLA 里少见的“从训练到部署全链路”叙事，而不只是离线 benchmark 取胜。
  - 如果 MolmoAct2-Think 的按需推理确实兼顾解释性与延迟，它会直接影响后续 VLA 的系统设计范式。
  - Dieter Fox 参与使其更值得跟踪，因为这条线天然连接具身感知、操作与真实机器人评测。
* **风险 / 保留意见**:
  - HTML 摘录没有给出关键性能表和失败分布，当前对其领先幅度的判断仍需保守。
  - 方法栈较复杂，跨平台迁移到底来自骨干能力、数据配方还是推理机制，单靠摘录还无法拆清。
* **建议先看**: 先抓“为何要做 fully open action reasoning model for deployment”这条主线，再读 Molmo2-ER 与 MolmoAct2-Think 如何在时延、空间推理和迁移之间做取舍。上传 PDF 后，优先确认真实机器人实验与 few-shot 微调是否真正支撑其部署主张。
* **关键词**: `VLA` `动作推理` `开放权重` `真实部署` `跨平台迁移`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - Molmo2-ER 相比原始 Molmo2，究竟在哪些空间或具身推理能力上带来最直接的控制收益？
  - MolmoAct2-Think 的自适应深度推理是如何被触发和截断的，延迟收益与性能收益如何平衡？
  - 跨异构机器人平台的迁移能力，主要来自统一表征设计，还是来自机器人文本元数据与微调配方？
* **上传 PDF 后优先看**:
  - 方法章节里关于视觉连接器、token 压缩与机器人元数据注入的设计说明
  - 真实机器人实验章节，尤其是部署设置、任务类型与失败案例分析
  - few-shot 微调与跨平台迁移实验的对比表或消融部分

### [2]. VLA-ATTC: Adaptive Test-Time Compute for VLA Models with Relative Action Critic Model [[HTML]](https://arxiv.org/html/2605.01194) [[PDF]](https://arxiv.org/pdf/2605.01194) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.01194`
* **Authors**: Wenhao Li, Xiu Su, Dan Niu, Yichao Cao, Hongyan Xu, Zhe Qu, Lei Fan, Shan You, Chang Xu
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把 test-time compute 明确引入 VLA，并用相对式动作 critic 避开了绝对价值评估常见的不稳定问题。
* **问题与切口**: 这篇论文解决的是 VLA 在复杂场景里“反应快但想得不够”的结构性问题。作者没有把深思考做成全程常开，而是提出自适应 TTC 机制：简单状态走 reflexive execution，只有在不确定时才进入 deliberation phase。新意在于它不直接做传统价值估计，而是用 Relative Action Critic 在候选动作之间做成对比较，把“选更好的动作”变成更容易学的排序问题。这个切口很贴近真实控制，因为它同时考虑鲁棒性与控制频率。
* **核心方法与证据**: HTML 摘录显示，VLA-ATTC 包含两个关键组件：基于不确定性的 cognitive clutch 负责决定何时从快速执行切换到测试时深思考；进入 TTC 阶段后，RAC 对生成的动作候选做两两比较以选优，而非回归绝对分值。作者还加入高效采样策略与自动化偏好对构建流程，减少算力和人工标注负担。实验覆盖 LIBERO-LONG 和 Agilex Piper 真实机器人，基座选用 PI0 与 PI0.5，并围绕有效性、消融、机制合理性和效率提出四个研究问题，证据结构是完整的，但具体收益幅度仍需回看 PDF。
* **正文要点**:
  - 不确定性触发的 cognitive clutch 是系统入口，核心不是一直多算，而是在必要时多算。
  - RAC 用相对比较替代绝对动作价值估计，作者明确把这视为更稳定、更易学习的目标。
  - 实验设计同时检查效果、机制、阈值与候选规模影响，以及控制频率是否还能满足实践要求。
* **为什么值得跟**:
  - 它把 LLM 侧已经成熟的 test-time compute 思路真正落到了 VLA 控制链路上。
  - 相对式 critic 若成立，可能成为今后动作候选重排的一类通用轻量模块。
  - 它关注真实机器人上的控制频率问题，因此比只在离线仿真中加推理更有部署价值。
* **风险 / 保留意见**:
  - HTML 摘录未展示 TTC 触发频率与最坏时延分布，实际部署成本可能依任务而波动很大。
  - RAC 成效可能依赖候选动作质量；若基座生成本身较弱，相对排序未必能补回根本缺陷。
* **建议先看**: 先看作者如何定义并估计不确定性，因为那决定了 TTC 什么时候介入。再看 RAC 的训练数据构造与候选动作来源，这两处最能判断方法是否能稳定复用到别的 VLA 基座。
* **关键词**: `VLA` `test-time compute` `Relative Action Critic` `不确定性触发` `动作候选选择`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 不确定性度量具体依赖哪些信号，它在不同任务和不同基座模型上是否需要重新校准？
  - RAC 的成对比较标签由自动化流程生成后，是否会把基座偏差直接固化进 critic？
  - 候选动作数量、可学习 query 数量与控制时延之间的拐点在哪里？
* **上传 PDF 后优先看**:
  - 方法章节中 cognitive clutch 与不确定性度量的正式定义
  - RAC 训练与自动化偏好对构建流程的实验或消融部分
  - 效率评测章节，尤其是控制频率、时延开销与不同候选规模对比

### [3]. Anticipation-VLA: Solving Long-Horizon Embodied Tasks via Anticipation-based Subgoal Generation [[HTML]](https://arxiv.org/html/2605.01772) [[PDF]](https://arxiv.org/pdf/2605.01772) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.01772`
* **Authors**: Zhilong Zhang, Wenyu Luo, Haonan Wang, Yifei Sheng, Yidi Wang, Hanyuan Guo, Haoxiang Ren, Xinghao Du, Yuhan Che, Tongtong Cao, Lei Yuan, Yang Yu
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它抓住了长程 VLA 的核心病灶不是单步控制，而是固定粒度分解带来的误差累积。
* **问题与切口**: Anticipation-VLA 针对长时程任务中最常见的失败模式提出了更细的解决思路：不是预先把任务切成固定子任务，而是根据执行状态递归地产生未来子目标，让分解粒度随情境变化。它要解决的是已有长程方法在复杂阶段切得太粗、在简单阶段切得太细的问题。相对传统 skill retrieval 或静态 VLM planning，这篇工作的创新在于把 anticipation model 变成持续在线的层级机制，并同时生成多模态子目标。
* **核心方法与证据**: 从摘录可见，作者先把问题放进 GMDP 形式化里，再把 anticipation model 定义为从当前状态与活跃目标映射到更近一步子目标的函数；这个输出还可递归回灌为新的活跃目标，因此能多层分解直到得到可执行目标。作者强调其最优性与最短路径奖励结构有关，并围绕模拟、真实环境、超参数敏感性、未见任务泛化以及子目标文本和图像质量提出五个问题。实验覆盖 LIBERO 四套件与 VLABench 中极难的 Hammer Nail & Hang Picture 任务，说明它的证据重点就是长程鲁棒性。
* **正文要点**:
  - 方法核心不是一次性规划，而是随着执行推进反复细化子目标，直接对冲 compounding error。
  - 理论叙事里引入了全局最优性与 shortest-path reward 结构，说明作者试图给层级分解一个强化学习视角的正当性。
  - 实验中特别强调几乎所有模型都会失败的长程任务，表明论文主攻的是困难区间而非平均任务。
* **为什么值得跟**:
  - 它为长时程 VLA 提供了比固定层级分解更灵活的在线规划接口。
  - 若多模态子目标生成确实稳定，后续 VLA 可能更容易把语言、图像与动作计划统一到一个执行闭环里。
  - 这条路线与世界模型、层级 RL 都有接口，后续扩展空间很大。
* **风险 / 保留意见**:
  - HTML 摘录没有充分展开 anticipation model 的训练细节，递归分解是否稳定可能是复现难点。
  - 理论最优性依赖特定奖励结构，真实机器人任务是否严格满足这一前提仍需谨慎看待。
* **建议先看**: 先看形式化定义与递归子目标生成逻辑，判断它究竟是规划模块还是可学习的层级控制接口。然后重点读长程 benchmark 和未见任务泛化，因为那是这篇工作的真正价值所在。
* **关键词**: `长程任务` `层级规划` `子目标生成` `VLA` `误差累积`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 递归子目标生成在什么条件下停止，停止准则是否会对成功率和时延造成明显影响？
  - 多模态子目标中的文本与图像各自承担什么功能，是否存在一方主导另一方冗余的情况？
  - 理论上的 shortest-path optimality 在真实机器人任务里是如何近似落实到训练目标中的？
* **上传 PDF 后优先看**:
  - 问题形式化与 anticipation model 定义所在的方法章节
  - 长程任务实验章节，尤其是 LIBERO-Long 与 VLABench 困难任务结果
  - 关于子目标文本/图像质量评估与超参数敏感性的分析部分

### [4]. Privileged Foresight Distillation: Zero-Cost Future Correction for World Action Models [[HTML]](https://arxiv.org/html/2604.25859) [[PDF]](https://arxiv.org/pdf/2604.25859) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.25859`
* **Authors**: Pengcheng Fang, Hongli Chen, Xiaohao Cai
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它不只是在 world action model 上加一个技巧，而是在追问“未来预测分支到底贡献了什么”这个更根本的问题。
* **问题与切口**: 这篇工作切入点很强：既然已有结果表明 world action model 的未来视频分支在推理时可以去掉且几乎不掉性能，那么训练时的未来预测到底在起什么作用？作者反对“它只是共享骨干正则化”的简单解释，转而提出 future-as-correction 观点，即未来观测在训练中给动作去噪提供了可压缩的修正信号。PFD 的目标不是保留测试时想象，而是把这种特权前视纠偏蒸馏到仅看当前观测的路径里。
* **核心方法与证据**: 从 HTML 可见，PFD 采用同一骨干上的 teacher-student 构造：有未来访问权限的 privileged path 产生动作侧 correction signal，而 current-only path 通过一个小型输出适配器吸收这部分 residual，推理时只保留 current-only path 与适配器。作者沿用 Mixture-of-Transformers 骨干、视频专家与动作专家，并以不同 joint attention mask 区分 teacher 与 student 视野。证据上，除常规 benchmark 外，论文还特别设计 matched-capacity、shuffled-future 与 budget 等 epistemic probes，说明它不仅追求结果提升，也在验证解释是否成立。
* **正文要点**:
  - 论文真正的贡献是把未来分支的作用从“正则化”重解释为“动作纠偏信号”。
  - PFD 只在训练期引入特权路径，推理时不实例化未来分支，目标是零额外测试成本。
  - 作者设置了专门的 epistemic probes，而不只做基准对比，说明其研究重点包含机制辨析。
* **为什么值得跟**:
  - 它为 world action model 研究提供了更可检验的机制假说，而不只是经验上有用。
  - 如果纠偏蒸馏成立，未来信息就可以从高成本预测任务转化为更轻量的训练监督。
  - 这类解释框架有机会影响后续世界模型是否需要显式生成未来的设计选择。
* **风险 / 保留意见**:
  - HTML 摘录没有展开 probe 的具体结果，当前仍不能断言 future-as-correction 已被充分证成。
  - 方法依赖 same-backbone teacher-student 设定，其结论是否跨架构普适还需要进一步核查。
* **建议先看**: 先读引言与方法，看作者如何拆解“regularizer reading”与“future-as-correction reading”的分歧。再重点看那些 epistemic probes，因为真正决定这篇论文价值的不是增益本身，而是解释能否站住。
* **关键词**: `World Action Model` `蒸馏` `未来纠偏` `训练机制` `零测试成本`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - shuffled-future 等 probe 到底在多大程度上排除了“只是更强正则化”的解释？
  - 小型输出适配器吸收的 residual 更像动作偏置修正，还是更深层的状态表征补偿？
  - 这种 privileged foresight distillation 对不同 attention mask 或不同 world model 骨干是否同样有效？
* **上传 PDF 后优先看**:
  - 引言与问题设定部分对 future branch 作用的两种解释
  - 方法章节中 privileged path、student path 与 adapter 的构造说明
  - 实验章节里的 epistemic probes 与跨 benchmark 对比结果

### [5]. HandelBot: Real-World Piano Playing via Fast Adaptation of Dexterous Robot Policies [[VIP]] [[HTML]](https://arxiv.org/html/2603.12243) [[PDF]](https://arxiv.org/pdf/2603.12243) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.12243`
* **Authors**: Amber Xie, Haozhi Qi, Dorsa Sadigh
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，它把 sim2real 放到极端高精度灵巧操作里检验，而且出自 Dorsa Sadigh 这条线，研究含金量和跟踪价值都很高。
* **问题与切口**: HandelBot 处理的是一个比常见抓取或装配更苛刻的任务设定：双手机器人弹钢琴，要求毫米级精度、快速独立指法和长时序协调。论文的核心问题不是“能否在仿真学会”，而是“仿真学到的高自由度策略如何快速适应到真实世界”。作者提出两阶段流程：先拿到仿真中表现最好的策略与轨迹，再通过快速适配把它修正为真实可执行方案。这使它成为高精度 sim2real 的强案例，而不是普通 dexterous RL 的又一次验证。
* **核心方法与证据**: 从摘录看，系统由两只 Tesollo DG-5F 机械手分别挂载在 Franka Panda 与 FR3 机械臂上，作者还设计了 3D 打印支架来匹配人类弹琴姿态。仿真环境采用 ManiSkill，训练后不是直接部署整套闭环策略，而是先选择验证 F1 最优轨迹作为名义 open-loop 方案，再在真实世界加一层安全与可行性修正：通过 PyRoki 求解受约束逆运动学，惩罚自碰撞与接触不稳定。这些细节说明论文把“快速适配”具体落实到轨迹选择与安全修正，而不仅是泛泛说 domain adaptation。
* **正文要点**:
  - 论文把难点明确放在高自由度、毫米级精度、双手协同的真实钢琴演奏，而不是标准灵巧操作 benchmark。
  - sim2real 起点不是任意仿真策略，而是先按验证 F1 选择最强仿真轨迹作为名义解。
  - 真实部署前加入受约束 IK 与安全层，说明作者承认并正面处理直接迁移的硬件风险。
* **为什么值得跟**:
  - 它给出了一个比常见 manipulation task 更严苛的 sim2real 测试台，能逼出迁移方法真正的边界。
  - 对于高精度灵巧控制，论文强调快速适配而非海量真人示教，方向上非常实际。
  - Dorsa Sadigh 的参与使其更值得长期跟踪，因为这类系统工作往往会外溢到更广义的 dexterous adaptation 问题。
* **风险 / 保留意见**:
  - HTML 摘录未展开两阶段适配的完整学习目标与误差来源，当前仍难判断泛化是否超出钢琴这一强结构化任务。
  - 真实控制依赖脚本化臂部位姿轨迹与安全层，最终能力边界可能更多体现为“在受约束设定下稳定执行”。
* **建议先看**: 先看系统设定与两阶段流程，判断作者把哪些难点交给仿真策略、哪些留给现实适配。随后重点读真实机器人实验与失败案例，因为这篇论文最重要的价值就在那些迁移细节里。
* **关键词**: `Sim2Real` `灵巧操作` `钢琴演奏` `快速适配` `强化学习`
* **证据来源**: arXiv HTML (Introduction, Experiments)
* **读 PDF 先核查**:
  - 两阶段流程中，真实世界适配究竟校正了哪些误差，是动力学、接触时序，还是机械安装偏差？
  - 验证 F1 最优轨迹作为名义 open-loop 解这一选择，是否会牺牲对实时扰动的响应能力？
  - 受约束 IK 安全层在多大程度上只是保护硬件，还是已经实质参与了任务成功？
* **上传 PDF 后优先看**:
  - 系统与硬件章节，尤其是双手平台和安装姿态设计
  - 方法章节里仿真策略到真实适配的两阶段定义
  - 真实机器人实验与失败分析部分，尤其是安全层和 IK 修正的作用

### [6]. Sentinel-VLA: A Metacognitive VLA Model with Active Status Monitoring for Dynamic Reasoning and Error Recovery [[HTML]](https://arxiv.org/html/2605.01191) [[PDF]](https://arxiv.org/pdf/2605.01191) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.01191`
* **Authors**: Wenhao Li, Xiu Su, Yichao Cao, Hongyan Xu, Xiaobo Xia, Shan You, Yi Chen, Chang Xu
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把 VLA 的“会推理”推进成“会监测、会纠错、会扩展自身边界”的更完整认知闭环。
* **问题与切口**: Sentinel-VLA 解决的是当前 VLA 在长程执行里最典型的三连问题：推理能力不足、过程状态不可见、出错后缺乏自纠。它的创新不在于简单加一个思维链，而是引入主动状态监测的 sentinel 模块，让模型只在初始规划或检测到错误时触发动态推理与恢复方案，从而把深思考变成按需调用的资源。相较普通 reasoning-augmented VLA，它更像一套元认知控制框架，关注的是执行中的自监控。
* **核心方法与证据**: 根据 HTML 摘录，Sentinel-VLA 建立在公开的 PI0 上，继承其 VLM expert 与 action expert，并新增一个与 action expert 架构一致的 status monitor expert。训练数据不是人工逐条标注，而是通过 EC-Gen 自动生成与注释，覆盖 44 个 RLBench 任务、约 11000 条轨迹和 260 万以上 transitions。作者还提出 Self-Evolving Continual Learning，让系统识别自身能力边界并自动采集扩展数据，再配合 OC-Adapter 做持续学习。证据上，这篇工作的方法链很完整，但摘要级信息多于正文细节，因此对具体恢复机制仍应保守表述。
* **正文要点**:
  - 状态监测模块是新增核心，它让模型在执行过程中显式判断是否需要触发更深推理或错误恢复。
  - 训练数据通过自动化 EC-Gen 管线构建，规模覆盖 44 个任务和约 260 万 transitions。
  - 作者不只做单次训练，还提出 SECL 与 OC-Adapter，试图把能力边界识别和持续扩展纳入统一框架。
* **为什么值得跟**:
  - 它把 VLA 从一次性决策器推进为带执行监护能力的系统，更贴近真实机器人需求。
  - 按需触发推理的设计，与部署中的延迟和算力约束天然兼容。
  - 如果 SECL 机制有效，VLA 后续可能更像持续演化系统，而不是一次训完的静态策略。
* **风险 / 保留意见**:
  - HTML 方法摘录混入摘要文本，细粒度实现与损失设计信息不足，需要 PDF 才能确认关键机制。
  - 自动生成数据与自扩展流程可能引入偏差累积，能力边界识别是否可靠仍是主要风险点。
* **建议先看**: 先看 sentinel 模块到底监测什么、如何触发推理与恢复，再看 SECL 如何定义“能力边界”。如果这两点成立，这篇论文的价值会超过单纯又一个更强基准模型。
* **关键词**: `VLA` `元认知` `状态监测` `错误恢复` `持续学习`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - status monitor expert 的监督信号来自哪里，它如何区分普通偏差与需要恢复的真正错误状态？
  - 动态推理与恢复是在动作层重规划、在语言层重解释，还是两者同时发生？
  - SECL 所识别的能力边界是否可量化、可迁移，还是高度依赖 RLBench 数据生成分布？
* **上传 PDF 后优先看**:
  - 方法章节中 sentinel/status monitor 的输入输出与触发逻辑
  - EC-Gen、SECL 与 OC-Adapter 的训练流程说明
  - 实验章节里关于错误恢复、持续学习与任务扩展的结果分析

## Watchlist

### [W1]. Latent Bridge: Feature Delta Prediction for Efficient Dual-System Vision-Language-Action Model Inference [[HTML]](https://arxiv.org/html/2605.02739) [[PDF]](https://arxiv.org/pdf/2605.02739)
* **Paper ID**: `2605.02739`
* **Authors**: Yudong Liu, Yuan Li, Zijia Tang, Yuxi Zheng, Yueqian Lin, Qinsi Wang, Yi Li, Shuangjun Liu, Shuai Zhang, Taotao Jing, Dashan Gao, Ning Bi, Jingwei Sun, Yiran Chen, Hai Li
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇进入 shortlist 的原因很明确：它切中了双系统 VLA 的实际瓶颈，不改预训练模型本体，而是通过预测相邻时刻的 VLM 特征增量来省推理成本，部署意义很强。之所以没有进最终精选，是因为它更像高质量系统加速方案，研究野心主要在效率保真与架构兼容性，而不是对 VLA 能力边界提出新的认知框架。若后续你更关心 real-time VLA inference，这篇仍值得补看。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. Seeing Realism from Simulation: Efficient Video Transfer for Vision-Language-Action Data Augmentation [[HTML]](https://arxiv.org/html/2605.02757) [[PDF]](https://arxiv.org/pdf/2605.02757)
* **Paper ID**: `2605.02757`
* **Authors**: Chenyu Hui, Xiaodi Huang, Siyu Xu, Yunke Wang, Shan You, Fei Wang, Tao Huang, Chang Xu
* **Author Priority**: Standard
* **为什么还值得留意**: 它进入 shortlist，是因为 sim2real 数据增强这条线很实用：把模拟视频转成更真实训练视频，并显式追求语义、动作轨迹与环境多样性的保留。没有进最终精选，主要因为从摘录看，它更偏训练数据工程与生成式增强管线，方法价值成立，但对今天主线中的 VLA 推理机制、world model 解释或长程决策创新贡献相对次一级。若你在做低成本真实泛化，这篇仍有参考价值。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. TouchGuide: Inference-Time Steering of Visuomotor Policies via Touch Guidance [[VIP]] [[HTML]](https://arxiv.org/html/2601.20239) [[PDF]](https://arxiv.org/pdf/2601.20239)
* **Paper ID**: `2601.20239`
* **Authors**: Zhemeng Zhang, Jiahua Ma, Xincheng Yang, Xin Wen, Yuzhi Zhang, Boyan Li, Yiran Qin, Jin Liu, Can Zhao, Li Kang, Haoqin Hong, Zhenfei Yin, Philip Torr, Hao Su, Ruimao Zhang, Daolin Ma
* **Author Priority**: Core VIP
* **为什么还值得留意**: 这篇值得关注，一是有 Hao Su 参与，二是它把触觉指导做成 inference-time steering，而不是要求从头重训整个 visuo-tactile policy，这个切口很聪明。未入最终精选的原因是它更偏细粒度接触操控与多模态融合，和今天主线里的 VLA、world action model、长程推理闭环相比稍微偏支线；另外摘录显示其主要价值在特定接触任务的精修能力，而非更普适的通用部署框架。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. Robo3R: Enhancing Robotic Manipulation with Accurate Feed-Forward 3D Reconstruction [[VIP]] [[HTML]](https://arxiv.org/html/2602.10101) [[PDF]](https://arxiv.org/pdf/2602.10101)
* **Paper ID**: `2602.10101`
* **Authors**: Sizhe Yang, Linning Xu, Hao Li, Juncheng Mu, Jia Zeng, Dahua Lin, Jiangmiao Pang
* **Author Priority**: Core VIP
* **为什么还值得留意**: Robo3R 进入 shortlist，主要因为它代表了很值得跟踪的一条基础支线：先把可操作的 3D 几何重建做准，再去支撑 manipulation。Jiangmiao Pang 在作者列表中也提高了跟踪优先级。之所以没进最终精选，是因为它当前更像 manipulation-ready 3D perception 基座，而非直接推动 VLA 或 world action model 范式转向；但如果你后续关心几何感知如何反哺操作，这篇很可能是后续关键拼图。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
