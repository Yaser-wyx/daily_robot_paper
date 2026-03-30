# RoboPulse | 2026-03-26

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 72 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线很清楚：VLA 正在从“会看会说会动”转向“在遮挡、干扰、长时程和跨域部署下仍然可靠”，入选论文大多围绕外部记忆、3D/触觉等状态补全，以及更可控的推理与迁移接口展开。最终精选之所以成立，不是因为单点精度宣称，而是因为它们都给出了较明确的方法切口：冻结策略上的在线适配、插件式几何融合、接触感知多模态路由、长时程 episodic memory、点云表征驱动的 sim2real，以及由事件触发的主动协作。对作者追踪上，今天最值得优先看的 VIP 线索是 Hao Su 的主动协作操作框架，以及 Lerrel Pinto、Dieter Fox 参与的 Point Bridge，它们分别对应人机协作决策与跨域表示学习两条高价值方向。若从研究组合看，今天的 shortlist 也提示了一个重要信号：VLA、world model 与 sim2real 正在通过“中间表征和外部结构”而不是仅靠更大模型参数发生耦合。

## 今日信号

- 今天最值得记住的研究信号是，VLA 的下一阶段增益越来越依赖外部结构化补丁，例如记忆、事件机、几何 token 和触觉门控，而不是单纯继续放大主干模型。
- 今天最值得记住的研究信号是，3D/触觉/点云等中间表征正在成为连接 VLA、sim2real 与长时程操作的共同语言，因为它们直接服务于可执行的状态消歧。
- 今天最值得记住的研究信号是，world model 相关工作更像在向‘可压缩、可规划、可约束的潜在世界状态’收敛，但真正进入精选仍需要与机器人操作闭环结合得更紧。

## Editor's Picks

### [1]. SOMA: Strategic Orchestration and Memory-Augmented System for Vision-Language-Action Model Robustness via In-Context Adaptation [[HTML]](https://arxiv.org/html/2603.24060) [[PDF]](https://arxiv.org/pdf/2603.24060) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.24060`
* **Authors**: Zhuoran Li, Zhiyang Li, Kaijun Zhou, Jinyu Gu
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它代表了一条不改 VLA 参数、靠外部记忆与编排系统提升部署鲁棒性的现实路线。
* **问题与切口**: 这篇工作针对 VLA 在开放环境中最现实的短板：一旦出现视觉噪声、语言歧义或环境变化，单体策略缺少长期记忆、缺少对失败原因的判断，也缺少动态补救手段。SOMA 的新意不是继续微调策略，而是在冻结 backbone 外侧搭建一套可在线工作的记忆与编排层，让模型在执行时检索既往经验、识别失败成因，并调用外部干预接口完成上下文适配，因此更像是把 VLA 从静态策略升级为带执行中介的系统。
* **核心方法与证据**: 方法上，SOMA把冻结 VLA 外接成一条在线闭环：先用对比式双记忆检索找相似经验，再由带归因能力的 LLM orchestrator 判断失败来源，并通过 MCP 接口触发干预；离线阶段再把执行轨迹做记忆巩固，沉淀成后续可复用先验。证据主要来自跨三种 backbone、LIBERO-PRO 与 LIBERO-SOMA 的评测，以及围绕 Dual-Stage Memory Consolidation 的消融。就当前摘录看，作者强调的是跨场景一致增益与适配能力，而不是依赖一次性微调。
* **正文要点**:
  - SOMA 不改动冻结 VLA 参数，而是通过在线 orchestration、双记忆检索与可扩展干预来做上下文适配。
  - 实验覆盖多个 backbone、25 个任务，并同时使用 LIBERO-PRO 与作者构建的 LIBERO-SOMA 来刻画 OOD 干扰。
  - 作者专门做了记忆巩固相关消融，说明其重点不是单次检索，而是把执行轨迹沉淀成更可靠的先验。
* **为什么值得跟**:
  - 它给出了一条比重新训练更接近部署现实的 VLA 增强路径。
  - 它把“失败归因”显式纳入机器人控制闭环，而不只做被动检索增强。
  - 如果这种外接式架构成立，未来不同 VLA backbone 可能共享同一套记忆与干预基础设施。
* **风险 / 保留意见**:
  - 当前证据更偏高保真仿真环境，真实机器人上的可靠性与时延代价仍需谨慎判断。
  - 系统包含检索、编排、干预多个部件，整体增益可能依赖精心设计的接口与失败类型定义，复现门槛不低。
* **建议先看**: 先抓住“失败归因驱动的在线干预”这条主线，再看双记忆检索与离线记忆巩固如何配合，判断它究竟是在补 VLA 的记忆缺口，还是在外接一个任务执行器。若你关心部署价值，优先看 benchmark 设计是否真的覆盖 recurring failure mode。
* **关键词**: `VLA鲁棒性` `外部记忆` `RAG` `在线适配` `OOD操作`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)
* **读 PDF 先核查**:
  - 双记忆检索中，哪些记忆项真正决定了后续干预效果，是否会因错误检索放大失败归因偏差？
  - LLM orchestrator 的归因判断是否稳定，还是只在作者定义的 recurring failure mode 上有效？
  - 离线记忆巩固带来的提升，究竟来自信息压缩本身，还是来自对干预策略分布的再平衡？
* **上传 PDF 后优先看**:
  - 方法章节里关于 Dual-Memory Retrieval 与 Attribution-Driven Orchestrator 的模块定义
  - 实验章节中 LIBERO-SOMA 五类 OOD 挑战维度与任务构造方式
  - 消融章节中 Memory Consolidation 与干预模块分别贡献多少

### [2]. 3D-Mix for VLA: A Plug-and-Play Module for Integrating VGGT-based 3D Information into Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2603.24393) [[PDF]](https://arxiv.org/pdf/2603.24393) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.24393`
* **Authors**: Bin Yu, Shijie Lian, Xiaopeng Lin, Zhaolong Shen, Yuliang Wei, Haishan Liu, Changti Wu, Hang Yuan, Bailing Wang, Cong Huang, Kai Chen
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把“如何把 3D 真正接进 VLA”这个分散问题做成了有比较基线的系统结论。
* **问题与切口**: 这篇工作直指一个越来越重要的问题：现有 VLA 大多借助 2D 预训练视觉语言模型起家，语义理解强，但空间智能与深度几何感知不足，导致精细操作中的定位、姿态和关系判断常常不够可靠。作者没有简单再堆一个 3D 模块，而是把“3D 信息该怎样并入 VLA”本身作为研究对象，系统比较多种 VGGT 融合路径，最后提出可插拔的 3D-Mix，核心贡献在于证明有效的 3D 增强更依赖合理的信息融合机制，而非笨重地重写整套 VLA 架构。
* **核心方法与证据**: 方法核心是把冻结的 VGGT-1B 作为几何 token 提供器，再用统一训练协议比较九类 3D 融合方式，最后抽出最有效的语义条件化门控设计，形成可插拔的 3D-Mix 模块。实验上，作者固定 Qwen3-VL-4B 和 VGGT 的训练设置，在 BridgeV2 训练，并在 SIMPLER 与 LIBERO 等互补场景验证跨域与域内表现；结论并不声称需要大规模改 backbone，而是强调轻量、兼容与跨六个 MLLM 系列的一致增益。
* **正文要点**:
  - 作者先做了九种 VGGT 融合方案的标准化 pilot study，再据此提出 3D-Mix，而不是直接给单一设计。
  - VGGT 作为冻结 3D 特征提取器输入多视角 RGB，重点比较的是融合策略，而非 3D 编码器本身。
  - 结论强调“语义条件化的自适应门控”优于更重的结构改造，且可直接插入多种 MLLM 系列与 GR00T-style VLA。
* **为什么值得跟**:
  - 它把 3D 融合从经验工程变成了可以复用的设计结论。
  - 插件式模块更容易落到现有 VLA 栈上，工程迁移成本相对低。
  - 如果空间智能瓶颈确实主要卡在融合层，这会直接影响下一代 VLA 的架构优先级。
* **风险 / 保留意见**:
  - 当前结论建立在特定 3D encoder 与标准化协议之上，换用其他几何模型后排序可能变化。
  - 多视角 RGB 和额外 3D 模块会带来部署成本，真实机器人上的时延与标定鲁棒性仍需核实。
* **建议先看**: 先看九种融合方案的比较逻辑，确认作者到底控制了哪些变量；再看 GatedFusion 为什么在跨 benchmark、跨 backbone 下更稳。读这篇的关键不是 3D encoder 本身，而是 2D 语义与 3D 几何之间的信息路由设计。
* **关键词**: `VLA` `3D融合` `VGGT` `空间推理` `插件模块`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 九种融合方案的差异主要来自信息注入位置、token 组织方式，还是训练稳定性与优化难度？
  - GatedFusion 的收益在需要精细几何操作的任务上是否显著高于普通抓取或导航式任务？
  - 冻结 VGGT 的前提下，几何 token 是否已经足够，还是未来还需要与动作头做更深层联合训练？
* **上传 PDF 后优先看**:
  - 九种 VGGT 融合方案的系统比较与设计变量控制
  - GatedFusion/3D-Mix 的具体结构与插入位置说明
  - 跨不同 MLLM 系列和 benchmark 的泛化结果与失败案例

### [3]. TacVLA: Contact-Aware Tactile Fusion for Robust Vision-Language-Action Manipulation [[HTML]](https://arxiv.org/html/2603.12665) [[PDF]](https://arxiv.org/pdf/2603.12665) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.12665`
* **Authors**: Kaidi Zhang, Heng Zhang, Zhengtong Xu, Zhiyuan Zhang, Md Rakibul Islam Prince, Xiang Li, Xiaojing Han, Yuhao Zhou, Arash Ajoudani, Yu She
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它提供了一个很实际的判断：VLA 不是永远缺更多模态，而是缺按状态激活正确模态。
* **问题与切口**: TacVLA 解决的是纯视觉语言 VLA 在接触密集操作中的典型失灵：一旦被遮挡、需要细致插拔或依赖接触反馈，视觉信息往往既不完整也不够敏感。它的切口不是把触觉粗暴并联进模型，而是提出 contact-aware 的状态依赖融合，让触觉只在真正发生物理接触时参与决策，从而兼顾信息增益与噪声控制。相较于“多加一个模态就会更强”的直觉，这篇的价值在于强调何时引入触觉，和如何把触觉变成动作决策真正需要的条件信号。
* **核心方法与证据**: 方法上，TacVLA将触觉模态接入 transformer policy，但不是始终拼接，而是用接触感知门控在检测到物理接触时才打开触觉 token，以实现状态依赖的多模态融合。证据来自一套真实机器人平台上的拆解与箱内抓取任务，对比基线后又加入遮挡和人类干扰等鲁棒性评测。结合结论段可见，作者并未把方案包装成通用感知升级，而是把贡献边界限定在 contact-rich、短时程、需要细微调整的 manipulation 场景。
* **正文要点**:
  - TacVLA 通过接触感知门控，只在检测到接触时激活触觉 token，避免无效多模态噪声。
  - 实验聚焦约束锁定拆解与箱内抓取，并专门测试遮挡和人为扰动下的鲁棒性。
  - 作者明确承认当前门控依赖二值阈值、触觉分辨率有限，且评测主要覆盖短时程接触任务。
* **为什么值得跟**:
  - 它把多模态融合从静态拼接推进到状态驱动的模态路由。
  - 对装配、拆解、箱中抓取这类视觉天然吃亏的任务，触觉是更现实的能力补丁。
  - 作者主动公开限制，使这项工作更像可扩展起点，而不是被过度包装的全能方案。
* **风险 / 保留意见**:
  - 方案对触觉硬件布置和传感器质量有依赖，跨平台迁移未必直接成立。
  - 当前实验任务集中于短时程接触操作，对通用长时程 VLA 的外推仍需谨慎。
* **建议先看**: 先看 contact-aware gating 的触发逻辑，再看它在遮挡与扰动场景下是否真正补上了视觉盲区。若你关心后续可扩展性，重点审视作者自己列出的限制是否会在长时程任务里放大。
* **关键词**: `触觉融合` `VLA` `接触感知` `多模态路由` `精细操作`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 二值接触阈值对不同材质、不同抓取力和不同传感器噪声是否敏感？
  - 触觉 token 只在接触后激活，会不会错过接触前的接近阶段信息，从而限制预触碰策略优化？
  - 在更长时程任务中，接触状态切换频繁时，门控机制是否会造成多模态表示不稳定？
* **上传 PDF 后优先看**:
  - 方法章节中 contact-aware gating 的输入、触发与融合细节
  - 真实机器人任务定义与遮挡/人为扰动鲁棒性设置
  - 限制与讨论章节里关于二值阈值和传感器分辨率的自我评估

### [4]. Chameleon: Episodic Memory for Long-Horizon Robotic Manipulation [[HTML]](https://arxiv.org/html/2603.24576) [[PDF]](https://arxiv.org/pdf/2603.24576) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.24576`
* **Authors**: Xinying Guo, Chenxi Jiang, Hyun Bin Kim, Ying Sun, Yang Xiao, Yuhang Han, Jianfei Yang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把机器人长时程记忆从‘检索文本摘要’推进到‘保留可决策感知细节的 episodic memory’。
* **问题与切口**: 这篇工作面向长时程 manipulation 中一个很核心但常被低估的问题：到了关键决策时刻，当前观测往往已经不足以区分真实状态，因为重要线索可能被遮挡、被覆盖，或者只存在于先前交互历史里。作者认为，现有 embodied memory 常把经验压缩成偏语义的摘要，再做相似检索，这对需要感知级消歧的操作并不够。Chameleon 因此转向更接近 episodic memory 的路线，把带几何依据的多模态细节写入记忆，并在需要时按目标导向召回，从而服务长时程、非马尔可夫式决策。
* **核心方法与证据**: 方法上，Chameleon用可微分架构实现三件事：在交互过程中把带几何约束的多模态 token 写入记忆，以保留消歧所需细节；在决策时按目标导向召回相关经历；再把召回结果汇总成单一 decision state 供策略生成未来末端执行器轨迹。实验在作者构建的 Camo-Dataset 上进行，并直接部署到同一台 UR5e 真实机器人，比较对象含 Diffusion Policy、Flow Matching 与 ACT，同时配有五个变体消融和表征分析。作者还额外提出 DSR/MSR，说明他们意识到“记忆对了但动作没做好”和“记忆就错了”必须分开看。
* **正文要点**:
  - Chameleon 将几何落地的多模态 token 写入记忆，而不是先做强语义压缩，再做相似性检索。
  - 结构灵感来自 EC–HC–PFC 的功能分工，但实现上是 fully differentiable，并把单一 decision state 输入策略。
  - 实验不仅报告真实机器人表现，还引入 DSR 与 MSR 区分“记忆检索正确”与“后续操作执行正确”。
* **为什么值得跟**:
  - 它切中了长时程机器人操作真正缺的不是更大策略，而是可用于消歧的记忆表示。
  - 真实机器人评测让这项工作不止停留在记忆架构概念验证。
  - 把记忆正确性与操作正确性拆开评估，对后续研究定位瓶颈很有价值。
* **风险 / 保留意见**:
  - 数据集与真实部署来自同一任务设定，跨场景、跨机器人、跨传感器的记忆泛化仍需进一步验证。
  - 受生物启发的模块划分很吸引人，但真正起作用的可能是具体表示与检索设计，而不一定是整体认知比喻。
* **建议先看**: 先看作者如何定义 perceptual aliasing，以及为什么语言式压缩记忆会丢失决策所需细节；再看 DSR/MSR 这组指标，判断改进主要来自记忆命中，还是来自控制策略本身。若你做长时程 manipulation，这篇应优先读方法总览与指标设计。
* **关键词**: `episodic memory` `长时程操作` `perceptual aliasing` `几何记忆` `真实机器人`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 记忆写入时保留多少几何细节才足以消歧，是否存在容量与检索效率之间的拐点？
  - goal-directed recall 在存在多个相似历史片段时如何避免召回决策无关但外观相似的 episode？
  - DSR 与 MSR 的分离分析是否显示瓶颈已从记忆转移到低层控制，还是两者都在受益？
* **上传 PDF 后优先看**:
  - 问题设定与总体架构中关于 perceptual aliasing 和 decision state 的定义
  - 实验章节中 Camo-Dataset、真实机器人部署与 DSR/MSR 指标说明
  - 消融与表征分析章节，核查几何写入和目标导向召回各自贡献

### [5]. Point Bridge: 3D Representations for Cross Domain Policy Learning [[VIP]] [[HTML]](https://arxiv.org/html/2601.16212) [[PDF]](https://arxiv.org/pdf/2601.16212) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2601.16212`
* **Authors**: Siddhant Haldar, Lars Johannsmeier, Lerrel Pinto, Abhishek Gupta, Dieter Fox, Yashraj Narang, Ajay Mandlekar
* **Author Priority**: Extended VIP
* **一句话结论**: 值得优先看，这是今天 shortlist 里 sim2real 含金量最高的一篇，且有 Lerrel Pinto、Dieter Fox 这条作者线索。
* **问题与切口**: Point Bridge 针对的是机器人基础模型当前最硬的瓶颈之一：真实操作数据太贵，仿真与合成数据虽然便宜，却常因为视觉域差无法直接转化为真实世界收益。它的思路不是继续做像素级对齐，也不是依赖明确对象标注，而是用更统一、域无关的点式 3D 表征，把仿真和现实都映射到相对稳定的几何接口上，再在这个接口上学习策略。新意在于把 sim2real 的核心矛盾从“图片长得不像”转向“决策所需的几何结构能否对齐”。
* **核心方法与证据**: 从摘录看，Point Bridge 通过自动化的点式表示与统一策略学习流程，把模拟数据和真实观测映射到相对一致的 3D 表征空间，从而减少视觉外观差异对策略学习的污染。实验使用 Franka Research 3、RGB-D 与双目相机，在对象类型和摆放变化较大的操作任务上评估 zero-shot sim-to-real，同时分析少量真实数据加入后的进一步收益，并系统拆解组件贡献。证据重点不是大规模 benchmark 横扫，而是证明在较弱显式对齐条件下，3D 表征能成为跨域政策学习的桥。
* **正文要点**:
  - Point Bridge 的核心不是显式视觉对齐或对象级对齐，而是用统一的点式表示跨越仿真与现实域差。
  - 作者在最小视觉和对象对齐条件下做 zero-shot sim-to-real，并进一步测试少量真实数据协同训练。
  - 文中明确指出其依赖 VLM 与相机位姿对齐，这说明它并非完全摆脱感知先验与采集约束。
* **为什么值得跟**:
  - 它直接回应了机器人数据规模化最现实的问题：如何让合成数据真正可用。
  - 3D 表征作为跨域接口，比纯视觉外观对齐更接近操作决策本质。
  - 这条路线若成立，会显著提升 foundation policy 与模拟数据管线的耦合效率。
* **风险 / 保留意见**:
  - 对相机位姿对齐的依赖意味着部署时环境变化可能迅速引入新的分布偏移。
  - 如果上游深度或 VLM 失败，点式表示未必仍然保持域无关，系统鲁棒性会受牵连。
* **建议先看**: 先看点式表征如何在仿真和现实之间建立 domain-agnostic 接口，再看 zero-shot transfer 与少量 real co-training 的关系。若你更关心实用落地，优先核查相机位姿对齐与深度估计模块是否构成隐含前提。
* **关键词**: `Sim2Real` `点云表示` `跨域策略学习` `零样本迁移` `Foundation Model`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 统一点式表示真正消除了哪些域差，哪些误差仍被留给 VLM、深度估计或控制器承担？
  - zero-shot transfer 的成败更依赖表征本身，还是依赖相机位姿与观测几何的一致性假设？
  - 少量真实数据带来的提升，是在校正表示偏差，还是主要在补足动作分布与接触动力学差异？
* **上传 PDF 后优先看**:
  - 方法章节中 point-based representation 的构造与训练接口
  - 实验章节里 zero-shot sim-to-real 设置与少量真实数据协同训练比较
  - 局限性讨论，特别是相机位姿对齐和上游视觉模型依赖

### [6]. Event-Driven Proactive Assistive Manipulation with Grounded Vision-Language Planning [[VIP]] [[HTML]](https://arxiv.org/html/2603.23950) [[PDF]](https://arxiv.org/pdf/2603.23950) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.23950`
* **Authors**: Fengkai Liu, Hao Su, Haozhuang Chi, Rui Geng, Congzhi Ren, Xuqing Liu, Yucheng Xu, Yuichi Ohsita, Liyun Zhang
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，它把 VLM 在机器人里的角色从“听命执行”推进到了“基于事件证据主动协作”。
* **问题与切口**: 这篇工作的切口与常见 VLA 操作不同，它不再把机器人当成等待指令的执行端，而是试图让机器人像协作伙伴一样，从人类动作导致的环境变化中推断下一步可提供的帮助。作者因此提出事件驱动的主动辅助框架：当工作空间出现由人和物体交互引发的状态转移时，系统先用事件监测器锁定关键前后状态，再交给 grounded vision-language planning 进行目标推断与动作生成。新意在于把“什么时候该帮忙”与“帮什么”一并转化为基于事件证据的 embodied 推理问题。
* **核心方法与证据**: 方法上，这篇工作把“人发指令后机器人响应”改成“人造成环境状态变化后机器人主动推断并行动”。具体做法是用事件监测与状态机抽取稳定的交互前后快照，再在事件触发的决策点调用 grounded VLM 进行目标推断与辅助动作生成。证据主要来自真实桌面 number-block 协作任务，作者专门设计了可解和不可解两类场景，考察系统能否在没有用户请求的情况下决定是否介入，以及介入动作是否符合任务规则。结论强调显式 pre/post 证据优于若干基线。
* **正文要点**:
  - 框架以事件监测器捕捉人类交互引起的工作空间状态变化，并在事件触发点调用 grounded VLM 推理。
  - 任务不是传统 request-driven instruction following，而是根据前后状态快照主动判断何时介入、该提供什么帮助。
  - 实验聚焦真实桌面数字块协作，区分可解与不可解场景，检验系统是否能在无额外请求下给出符合规则的辅助动作。
* **为什么值得跟**:
  - 它把机器人协作的触发机制从显式请求推进到基于环境事件的主动介入。
  - Hao Su 这条作者线值得持续跟踪，因为它连接了 VLM 推理与协作操作决策。
  - 若事件驱动范式成立，未来 assistive manipulation 可减少人为指令负担并提升协作流畅度。
* **风险 / 保留意见**:
  - 当前验证任务规则较清晰、对象语义较简单，向开放式协作扩展时意图推断难度会显著上升。
  - 系统表现可能强依赖事件切分质量；若感知噪声导致快照不稳定，主动辅助可能反而打断人类流程。
* **建议先看**: 先看 event state machine 如何定义稳定的 pre/post snapshots，因为这是整套主动协作是否成立的关键。随后再看 VLM 推理究竟承担的是目标推断、动作合成，还是两者都做，以及错误主要出在哪一层。
* **关键词**: `主动协作` `VLM规划` `事件驱动` `辅助操作` `人机协同`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 事件状态机对“稳定前后快照”的判定若出错，后续 VLM 推理会不会系统性偏航？
  - 在不可解场景中，模型如何区分‘应该等待’与‘应该主动纠错’，其失败模式是什么？
  - 当前由事件触发的短视决策，能否自然扩展到更长时程、更弱结构化的人机协作任务？
* **上传 PDF 后优先看**:
  - 方法章节中 event monitor、state machine 与 pre/post snapshot 的定义
  - 实验章节里 solvable/unsolvable 场景划分与评价标准
  - 基线比较部分，核查显式 pre/post 证据到底带来了哪些可归因增益

## Watchlist

### [W1]. TAG: Target-Agnostic Guidance for Stable Object-Centric Inference in Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2603.24584) [[PDF]](https://arxiv.org/pdf/2603.24584)
* **Paper ID**: `2603.24584`
* **Authors**: Jiaying Zhou, Zhihao Zhan, Ruifeng Zhai, Qinhan Lyu, Hao Liu, Keze Wang, Liang Lin, Guangrun Wang
* **Author Priority**: Standard
* **为什么还值得留意**: TAG 抓住了 VLA 在杂乱场景中常见的 instance-level grounding 失误，并且采用 inference-time guidance 这一工程上很轻的切口，进入 shortlist 很合理。它没有进入最终精选，主要因为从摘录看其贡献更像对推理阶段偏差的定向修补，而非对状态表示、记忆或跨域能力的更深层推进；如果后续 PDF 显示其跨任务收益和代价控制都很强，优先级可能上升。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. Red-Teaming Vision-Language-Action Models via Quality Diversity Prompt Generation for Robust Robot Policies [[HTML]](https://arxiv.org/html/2603.12510) [[PDF]](https://arxiv.org/pdf/2603.12510)
* **Paper ID**: `2603.12510`
* **Authors**: Siddharth Srikanth, Freddie Liang, Ya-Chuan Hsu, Varun Bhatt, Shihan Zhao, Henry Chen, Bryon Tjanaka, Minjune Hwang, Akanksha Saran, Daniel Seita, Aaquib Tabrez, Stefanos Nikolaidis
* **Author Priority**: Standard
* **为什么还值得留意**: Q-DIG 的价值在于把 VLA 的语言脆弱性系统化成 red-teaming 与数据增强问题，这对部署安全和鲁棒性很重要。之所以留在 watchlist，是因为它更偏评测与数据生成框架，和今天主线里的操作状态建模、记忆、sim2real 或 world-action 建模相比，离“直接提升机器人执行闭环能力”还隔了一层。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. ManiDreams: An Open-Source Library for Robust Object Manipulation via Uncertainty-aware Task-specific Intuitive Physics [[HTML]](https://arxiv.org/html/2603.18336) [[PDF]](https://arxiv.org/pdf/2603.18336)
* **Paper ID**: `2603.18336`
* **Authors**: Gaotian Wang, Kejia Ren, Andrew S. Morgan, Kaiyu Hang
* **Author Priority**: Standard
* **为什么还值得留意**: ManiDreams 符合 today 关注的 world model / intuitive physics 方向，而且把不确定性表示、传播与约束统一进规划回路，这一点很有研究味道。未进最终精选的原因在于它从摘录看更像开放库与框架平台，核心贡献强调模块化和可组合性，而不是在 VLA 或通用机器人基础模型闭环上给出更强的一线突破。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. Latent-WAM: Latent World Action Modeling for End-to-End Autonomous Driving [[HTML]](https://arxiv.org/html/2603.24581) [[PDF]](https://arxiv.org/pdf/2603.24581)
* **Paper ID**: `2603.24581`
* **Authors**: Linbo Wang, Yupeng Zheng, Qiang Chen, Shiwei Li, Yichen Zhang, Zebin Xing, Qichao Zhang, Xiang Li, Deheng Qian, Pengxuan Yang, Yihang Dong, Ce Hao, Xiaoqing Ye, Junyu han, Yifeng Pan, Dongbin Zhao
* **Author Priority**: Standard
* **为什么还值得留意**: Latent-WAM 在 world action model 方向上很契合今日主题，尤其是把空间压缩表示与动态潜变量建模耦合起来做端到端规划，思路清晰。它没有进入最终精选，主要因为场景是自动驾驶而非操作机器人，虽然研究信号值得跟踪，但与今天以 VLA manipulation、sim2real 和 embodied assistance 为主线的最终组合相比，相关性稍弱。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
