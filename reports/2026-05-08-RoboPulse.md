# RoboPulse | 2026-05-08

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 68 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线很集中：VLA 正在从“直接视觉到动作”转向更结构化的适应、推理与世界建模，Sim2Real、动作分块、对象可寻址表示和未来-现实校验都在争夺控制闭环里的关键位置。最终精选保留了六篇互补论文：一篇偏真实部署的灵巧手 Sim2Real，一篇偏 RL 控制时间尺度，一篇偏 VLA 关系结构，两篇偏 WAM 执行/对象建模，一篇偏参数高效 VLA 适配。VIP 作者里今天最值得优先跟踪的是 He Wang 参与的 2605.05544，因为它直接切入 offline-to-online RL 中动作 chunking 的状态自适应问题。其他核心名单作者未出现在最终精选作者中，因此这里不额外放大作者信号。

## 今日信号

- VLA/WAM 的一个明显趋势是把动作生成从全局隐表示中解耦出来，转向对象、关系、未来轨迹或可信度校验等可诊断中间结构。
- Sim2Real 方向正在把 foundation model 从语言规划器推进到视觉真实度批评器、随机化调参器和多模态策略训练辅助器。
- RL 与 VLA 的结合正在关注“什么时候执行多步、什么时候重规划”这类时间尺度问题，而不只是继续扩大模型或数据。

## Editor's Picks

### [1]. DexSim2Real: Foundation Model-Guided Sim-to-Real Transfer for Generalizable Dexterous Manipulation [[HTML]](https://arxiv.org/html/2605.05241) [[PDF]](https://arxiv.org/pdf/2605.05241) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.05241`
* **Authors**: Zijian Zeng, Fei Ding, Huiming Yang, Xianwei Li, Yuhao Liao
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，尤其适合跟踪 foundation model 如何实际介入灵巧手 Sim2Real 的随机化、感知融合和课程设计。
* **问题与切口**: DexSim2Real 试图解决灵巧操作策略从仿真迁移到真实机器人时对人工 domain randomization 和任务特定调参的依赖。它的核心切口不是单纯扩大随机化范围，而是让视觉语言模型充当视觉真实度批评器，用闭环方式优化仿真参数，并结合触觉-视觉策略与渐进课程，面向接触丰富、精细控制的多指操作。相对传统 DR/ADR，它的新意在于把 foundation model 放进 Sim2Real 调参回路，而不是只用于任务描述或高层规划。
* **核心方法与证据**: HTML 摘录显示系统由 FM-DR、TVCAP 和 PSC 三块组成：FM-DR 使用 VLM 对仿真视觉真实度进行反馈，并通过 CMA-ES 优化随机化参数；TVCAP 用跨注意力融合视觉与触觉，用于零样本 sim-to-real RL；PSC 则借鉴 LLM 任务分解并加入适合接触任务的难度调度。实验覆盖 Isaac Sim、Franka Panda + Allegro Hand、XELA 触觉、双 RealSense 视角，以及六类任务和真实试验；但摘录没有给出完整成功率表，因此结果强度需等 PDF 核查。
* **正文要点**:
  - 提出 FM-DR，用 VLM 作为视觉真实度 critic，对仿真参数做闭环优化，而不是完全依赖人工随机化范围。
  - 实验任务包含 pick-place、stacking、peg insertion、in-hand rotation、tool use 和 pouring，覆盖从抓取到接触丰富操作的梯度。
  - 硬件设置包括 Allegro Hand、XELA 指尖触觉和前视/腕部 RGB 相机，正文证据显示它关注真实多模态闭环而非纯仿真演示。
* **为什么值得跟**:
  - 它把 VLM 的作用推进到 Sim2Real 的参数搜索环节，可能改变灵巧操作里 DR 的人工工程成本。
  - 灵巧手、多触觉、多任务组合让它比常规夹爪 benchmark 更接近高难真实部署问题。
  - 如果 FM-DR 的效果成立，它能为后续自动化仿真校准和跨任务迁移提供可复用范式。
* **风险 / 保留意见**:
  - 摘要和 HTML 摘录强调框架整合，但完整数值、消融幅度和失败案例需要 PDF 验证。
  - VLM 视觉真实性评分是否稳定、是否依赖相机/材质分布，摘录证据不足。
* **建议先看**: 先沿着 FM-DR 的闭环优化主线读，确认 VLM critic 到 CMA-ES 参数更新的接口。随后核查 TVCAP 和 PSC 的消融，判断收益来自 foundation model 还是多组件叠加。
* **关键词**: `Sim2Real` `Dexterous Manipulation` `VLM-guided Domain Randomization` `Visuo-tactile Policy` `Curriculum RL`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - FM-DR 的 VLM 真实性反馈具体比较哪些视觉属性，是否会误把任务无关纹理优化成高分？
  - TVCAP 在无触觉或单视角条件下是否仍有稳定收益，还是主要依赖完整硬件配置？
  - PSC 的难度调度是否可跨六个任务共享，还是每个任务仍需要人工设定关键阶段？
* **上传 PDF 后优先看**:
  - FM-DR 参数优化与 VLM critic 设计章节
  - 六个真实任务的主结果、消融和失败案例
  - 触觉-视觉融合与课程学习的独立贡献实验

### [2]. Adaptive Q-Chunking for Offline-to-Online Reinforcement Learning [[VIP]] [[HTML]](https://arxiv.org/html/2605.05544) [[PDF]](https://arxiv.org/pdf/2605.05544) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.05544`
* **Authors**: Nandiraju Gireesh, Yuanliang Ju, He Wang
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，这是今天唯一有核心 VIP 作者 He Wang 的精选，并且问题切中 offline-to-online RL 的动作时间尺度瓶颈。
* **问题与切口**: Adaptive Q-Chunking 关注 offline-to-online RL 中 action chunking 的固定长度问题。已有 chunking 能减少多步 off-policy bias，并让探索更连贯，但固定 chunk 对所有状态一视同仁：自由空间运动适合长 chunk，接触或临界状态更需要短 chunk 的反应性。论文的核心新意是把 chunk size 做成状态自适应选择，同时指出直接比较不同 chunk critic 会因为折扣尺度不匹配而偏向短 chunk，并在低价值状态退化为噪声。
* **核心方法与证据**: 摘录证据主要来自摘要和引言：论文提出为多个 chunk size 训练 critic，并解决朴素价值比较导致的系统性崩塌问题。它把长时程稀疏奖励、离线示范预训练和在线继续改进放在同一框架下讨论，目标是在不同控制阶段动态选择动作块长度。HTML 没有提供完整方法细节、算法伪代码或实验表，因此目前只能确认问题定义和关键失败模式，不能替代 PDF 中对校准、选择准则和 benchmark 的核查。
* **正文要点**:
  - 论文明确指出固定 chunk size 不适合同时覆盖自由空间长程运动和接触附近的反应控制。
  - 核心技术障碍是不同 chunk critic 的折扣尺度不一致，直接比较会系统性偏向最短 chunk。
  - 研究场景是 offline-to-online RL，强调先从固定数据学习，再通过在线交互继续提升长时程任务表现。
* **为什么值得跟**:
  - 动作分块是 VLA/WAM 和 RL 控制之间的重要接口，这篇把时间尺度选择变成可学习问题。
  - 它可能改善长时程稀疏奖励任务中的探索一致性和信用分配。
  - He Wang 参与使其值得纳入优先跟踪，尤其对机器人操作 RL 方向有作者信号。
* **风险 / 保留意见**:
  - HTML 摘录缺少实验设置和完整算法细节，当前无法判断提升是否跨任务稳健。
  - 多 critic 训练和在线选择可能引入额外估计误差，尤其在低价值或分布外状态。
* **建议先看**: 先看论文如何校准不同 chunk size 的 Q 值，再看它在接触密集与自由空间阶段的选择行为是否符合直觉。实验部分要重点判断收益是否来自自适应 chunk，而不是额外 critic 容量。
* **关键词**: `Offline-to-online RL` `Action Chunking` `Adaptive Control Horizon` `Q-learning` `He Wang`
* **证据来源**: arXiv HTML (Introduction)
* **读 PDF 先核查**:
  - 论文用什么机制消除不同 chunk critic 之间的 discount-scale mismatch？
  - 状态自适应 chunk 选择在接触事件附近是否真的更偏短 chunk，并有可视化或统计支持吗？
  - 在线阶段的样本效率提升是否来自更好探索，还是来自离线初始化质量差异？
* **上传 PDF 后优先看**:
  - 算法章节中的 Q 值校准和 chunk 选择规则
  - 长时程稀疏奖励 benchmark 的主结果
  - 不同 chunk size、固定 chunk 和自适应 chunk 的消融实验

### [3]. TriRelVLA: Triadic Relational Structure for Generalizable Embodied Manipulation [[HTML]](https://arxiv.org/html/2605.05714) [[PDF]](https://arxiv.org/pdf/2605.05714) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.05714`
* **Authors**: Hanyu Zhou, Chuanhao Ma, Gim Hee Lee
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它代表 VLA 泛化路线从隐式视觉特征转向“手-物体-任务”关系结构。
* **问题与切口**: TriRelVLA 针对 VLA 在未见场景和未见物体上泛化不稳的问题，认为根因之一是隐式视觉表示把物体外观、背景纹理和布局纠缠在一起。它提出 triadic relational structure，把操作动作依赖的对象、机器人手和任务关系显式建模，区别于只做语义对象化的中间表示。其价值在于把动作预测从 appearance statistics 中拉出来，转向 action-relevant relations，对开放场景操作泛化更有针对性。
* **核心方法与证据**: 摘录显示 TriRelVLA 使用 Qwen3-4B 作为 LLM backbone，SigLIP 做语义编码，VGGT 中的 DINOv2 做几何编码，并与关系图结构结合。实验比较 OpenVLA、Octo、CogACT、DiffusionPolicy、SpatialVLA、CoA-VLA、CogVLA、SemanticVLA 等方法，在 LIBERO 和 CSOT-Bench 上评估全任务微调与跨场景、物体、任务的 zero-shot 泛化。正文结论摘录强调 triadic representation 与 relational graph 的逐步加入能改善泛化，但具体数值需核查。
* **正文要点**:
  - 论文把 VLA 泛化失败归因于隐式视觉表示对外观、背景和布局的纠缠。
  - 方法显式建模 object-hand-task 三元关系，并通过 relational graph 进一步推动关系驱动动作生成。
  - 评估覆盖 LIBERO 和 CSOT-Bench，并区分全子任务微调与 zero-shot 泛化设置。
* **为什么值得跟**:
  - 它提供了一个比纯语义中间表示更贴近操作动作因果结构的 VLA 设计方向。
  - 如果关系图消融成立，可为后续 VLA 结构化表示提供可复用模块。
  - 跨场景、物体、任务泛化正是当前 VLA 从 benchmark 走向真实部署的核心短板。
* **风险 / 保留意见**:
  - 关系表示的构建是否依赖高质量语义/几何编码器，摘录未充分说明失败模式。
  - CSOT-Bench 的任务覆盖和真实机器人外推能力需要 PDF 进一步确认。
* **建议先看**: 优先看 triadic representation 是如何生成并接入 LLM/action head 的。随后看关系图消融是否在 zero-shot 条件下有一致收益，而不是只提升训练分布表现。
* **关键词**: `VLA` `Triadic Relation` `Embodied Manipulation` `Generalization` `Relational Graph`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
* **读 PDF 先核查**:
  - object-hand-task 三元关系是显式监督、自动构建，还是由模型内部表示自组织得到？
  - 关系图在动作预测中影响哪些 token 或模块，是否会增加推理延迟？
  - 在 unseen object 与 unseen scene 两种设置下，性能增益是否来自同一种关系建模能力？
* **上传 PDF 后优先看**:
  - Triadic representation 和 relational graph 方法章节
  - LIBERO 与 CSOT-Bench 的 zero-shot 泛化结果
  - 三元表示组件和关系图的消融实验

### [4]. VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts [[HTML]](https://arxiv.org/html/2605.06175) [[PDF]](https://arxiv.org/pdf/2605.06175) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.06175`
* **Authors**: Yuhua Jiang, Junjie Lu, Xinyao Qin, Xiaoyu Chen, Kaixin Wang, Feifei Gao, Li Zhao
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它抓住 VLA 适配中全量微调易遗忘、普通 PEFT 又不够会控制的矛盾。
* **问题与切口**: VLA-GSE 研究如何把预训练 VLM 高效适配为 VLA 控制策略，同时保留视觉语言知识。论文认为 full fine-tuning 容易在下游机器人数据上过拟合并造成灾难性遗忘，而普通 PEFT 虽能保护预训练能力，却可能不足以学习精细控制。它提出 generalized and specialized experts：一个常开的通用专家维持基础表示，多路专门专家通过路由提供任务适配容量，目标是在知识保持和控制适应之间取得更好平衡。
* **核心方法与证据**: 方法沿用标准 VLM-to-VLA pipeline：预训练 VLM 编码图像和语言，OpenVLA-OFT 风格 action head 生成动作；action head 全量训练，PEFT 仅作用于 VLM backbone。GSE 通过 SVD 初始化，把权重谱分解中的领先成分分配给 generalized expert，并配合 specialized experts、专家梯度尺度平衡和 backbone weight adjustment。实验采用 Qwen3-VL-4B-Instruct，摘录给出专家配置、训练步数和多 GPU 设置，但主结果数值在摘录中不完整，需要 PDF 核查。
* **正文要点**:
  - 框架将 backbone 适配拆成 always-on generalized expert 与 routed specialized experts。
  - SVD 初始化用于从冻结预训练权重中分配通用与专门低秩成分。
  - 实验采用 OpenVLA-OFT 风格 action head，并把 PEFT 限定在 VLM backbone 上。
* **为什么值得跟**:
  - VLA 数据通常比 VLM 预训练数据小得多，参数高效适配是现实训练成本和泛化之间的关键路径。
  - 通用/专门专家分解可能比单一 LoRA 更适合多任务机器人控制。
  - 它与今日多篇 WAM/VLA 论文形成互补：不是改世界表示，而是改适配机制。
* **风险 / 保留意见**:
  - 专家数量、路由策略和 SVD 初始化可能带来工程复杂度，复现成本不低。
  - 摘录缺少完整对比表，无法判断相对 LoRA、FFT、OpenVLA-OFT 的真实收益幅度。
* **建议先看**: 先看 GSE 如何从 SVD 初始化到路由专家，再看它是否真的缓解遗忘而非只提升控制 benchmark。重点核查 PEFT 参数量、训练成本和性能之间的关系。
* **关键词**: `VLA Fine-tuning` `PEFT` `Mixture of Experts` `SVD Initialization` `OpenVLA-OFT`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - generalized expert 与 specialized experts 的谱成分划分是否有理论或经验依据？
  - 路由专家是否按任务、视觉场景或动作模式分化，论文有没有可解释分析？
  - 知识保持如何被衡量，是否只看控制成功率而忽略原 VLM 能力？
* **上传 PDF 后优先看**:
  - GSE 初始化、路由和梯度平衡方法章节
  - 与 FFT、LoRA、普通 PEFT 的对比实验
  - 遗忘评估、参数量和训练成本分析

### [5]. When to Trust Imagination: Adaptive Action Execution for World Action Models [[HTML]](https://arxiv.org/html/2605.06222) [[PDF]](https://arxiv.org/pdf/2605.06222) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.06222`
* **Authors**: Rui Wang, Yue Zhang, Jiehong Lin, Kuncheng Luo, Jianan Wang, Zhongrui Wang, Xiaojuan Qi
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把 WAM 的核心问题从“能想象未来”推进到“何时信任想象并继续执行”。
* **问题与切口**: 这篇提出的 FFDC-WAM 针对 World Action Model 推理时固定执行动作块的问题。现有 WAM 会联合预测未来视觉和动作，但通常每次推理后执行固定数量动作，无法判断真实物理展开是否仍符合模型想象。论文把 adaptive WAM execution 重新表述为 future-reality verification：当预测未来与观察一致时执行更长，当偏离出现时提前重规划。这是 WAM 走向闭环控制的关键切口。
* **核心方法与证据**: 方法基于 Motus WAM backbone，结合低频宏观规划和高频轻量校验器。FFDC verifier 使用跨视觉与动作模态的 causal attention，对 WAM 预测的未来视觉 token、动作 chunk 与实际观测进行持续验证。训练上包含长时程 WAM 与 verifier 模块；实验在 RoboTwin 50 个操作任务的 clean/random 设置和真实 Astribot S1 两个 pick-and-place 任务上评估。摘录提供了评估协议，但完整成功率和时间结果需查 PDF。
* **正文要点**:
  - 论文将固定动作执行长度替换为基于未来-现实一致性的自适应执行。
  - FFDC verifier 是高频轻量模块，服务于低频 WAM 宏观规划之后的执行监控。
  - 评估包含 RoboTwin 的 clean/random 设置，random 设置引入背景、杂物、高度和光照变化。
* **为什么值得跟**:
  - WAM 若要进入真实机器人闭环，必须处理模型想象与物理现实偏离的问题。
  - 自适应执行可能同时提升效率和安全性，避免每一步都重规划或盲目执行长计划。
  - 它为 action chunking、world model 和在线控制之间建立了清晰接口。
* **风险 / 保留意见**:
  - 真实机器人评估只在摘录中显示两个 pick-and-place 任务，真实覆盖面可能有限。
  - verifier 的误报/漏报代价很高，摘录未充分说明阈值选择和失效恢复策略。
* **建议先看**: 先看 future-reality verification 的判定信号，而不是只看 WAM backbone。随后核查 hard tasks、random setting 和真实机器人结果，判断自适应执行是否真的优于固定 horizon。
* **关键词**: `World Action Model` `Adaptive Execution` `Future-Reality Verification` `Action Chunking` `Causal Attention`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - FFDC verifier 比较的是像素、latent token、动作一致性，还是多模态联合距离？
  - 提前重规划的触发阈值如何设定，是否跨任务共享？
  - 在 hard tasks 中，成功率提升与完成时间变化是否存在明显 trade-off？
* **上传 PDF 后优先看**:
  - FFDC verifier 架构与训练目标章节
  - RoboTwin clean/random 主结果和 hard-task 分析
  - 真实 Astribot S1 部署与固定执行长度对比

### [6]. OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation [[HTML]](https://arxiv.org/html/2605.06481) [[PDF]](https://arxiv.org/pdf/2605.06481) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.06481`
* **Authors**: Yushan Liu, Peibo Sun, Shoujie Li, Yifan Xie, Lingfeng Zhang, Xintao Chao, Shiyuan Dong, Fang Chen, Xiao-Ping Zhang, Wenbo Ding
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把 WAM 的世界表示从整体视频/latent 改成对象可寻址 slot，问题定义很准。
* **问题与切口**: OA-WAM 认为现有 WAM 虽能联合预测场景演化和动作，但常把未来世界表示为整体图像、视频 token 或全局 latent，导致指令引用特定物体时，动作解码器难以稳定定位目标。论文把这个问题定义为 object addressability 缺失，并提出把每帧拆成 robot slot 与 object slots，每个 slot 包含冻结身份向量和动态内容向量。这样目标物体在新布局、相机或背景变化中仍可被语言和动作模块寻址。
* **核心方法与证据**: 方法将 per-slot state tokens 与文本、图像、本体感知和历史动作 token 融合进 block-causal sequence，world head 预测下一帧 slot state，并与动作生成联动。实验覆盖 LIBERO、SimplerEnv 和 LIBERO-Plus：前两者关注标准成功率与 sim-to-real visual matching，LIBERO-Plus 覆盖相机、机器人初始位姿、布局、光照、背景、语言和传感噪声等扰动轴。摘录声称在标准和几何鲁棒轴上领先，但具体百分比有截断，需 PDF 验证。
* **正文要点**:
  - 论文明确提出 WAM 的 object addressability 问题，认为 holistic token 会纠缠目标身份和上下文。
  - 每帧分解为 robot slot 与 object slots，并用冻结 identity address 维持对象可寻址性。
  - 实验设计包含 LIBERO-Plus 的七类受控扰动，尤其强调几何扰动轴与方法假设的对应关系。
* **为什么值得跟**:
  - 对象可寻址表示更符合操作指令的语义结构，如目标物体、容器和干扰物之间的关系。
  - 它为 WAM 鲁棒性提供了可诊断机制，而不只是报告整体成功率。
  - 若 slot 绑定实验成立，可推动 WAM 从全局生成模型转向对象级控制模型。
* **风险 / 保留意见**:
  - slot 分解质量和身份绑定稳定性可能成为瓶颈，摘录未充分说明复杂遮挡或新物体失败情况。
  - 论文主张的 SOTA 数值在摘录中不完整，必须核查表格来源和置信区间。
* **建议先看**: 先读 object slot、identity address 和 block-causal trunk 的连接方式。然后重点看 LIBERO-Plus 的几何扰动、slot swap 或 binding 消融，判断对象可寻址是否是主要收益来源。
* **关键词**: `Object-addressable WAM` `Slot Representation` `Robust Manipulation` `LIBERO-Plus` `World Action Model`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - object slots 是如何检测、初始化和保持跨时间一致的？
  - 冻结 identity address 在新对象、新纹理或遮挡场景中是否仍可靠？
  - OA-WAM 在非几何扰动轴上是否同样有效，还是主要提升相机/布局/机器人初始位姿？
* **上传 PDF 后优先看**:
  - 对象 slot 表示与 identity binding 方法章节
  - LIBERO-Plus 七类扰动结果，特别是几何轴
  - slot swap、OA isolation 和 holistic baseline 对照实验

## Watchlist

### [W1]. EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields [[HTML]](https://arxiv.org/html/2605.06192) [[PDF]](https://arxiv.org/pdf/2605.06192)
* **Paper ID**: `2605.06192`
* **Authors**: Zhaoyang Yang, Yurun Jin, Lizhe Qi, Cong Huang, Kai Chen
* **Author Priority**: Standard
* **为什么还值得留意**: EA-WM 进入 watchlist 是因为它切中 action-conditioned video world model 的另一侧：不是用视频生成辅助策略，而是让动作和运动学状态更精确地指导未来视频合成。Structured Kinematic-to-Visual Action Fields 和事件感知融合对机器人空间几何、交互动态很有价值。但它更偏生成式世界模型质量评估，和今天最终精选中闭环执行、对象寻址、VLA 适配的优先级相比稍靠后。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models [[HTML]](https://arxiv.org/html/2605.06247) [[PDF]](https://arxiv.org/pdf/2605.06247)
* **Paper ID**: `2605.06247`
* **Authors**: Yuhua Jiang, Yijun Guo, Hongbing Yang, Guojun Lei, Nuo Chen, Yinuo Zhang, Shaoqiang Yan, Bo Lin, Feifei Gao, Biqing Qi
* **Author Priority**: Standard
* **为什么还值得留意**: CKT-WAM 值得跟踪，因为它处理异构 WAM 之间的参数高效知识迁移，使用文本 embedding 空间中的 compact context，而不是密集 hidden-state imitation。它与 VLA-GSE 同属高效适配/迁移方向，但当前摘录显示重点在 teacher-student 迁移工程，机器人控制机制本身的新问题定义弱于最终精选。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. Reconstruction or Semantics? What Makes a Latent Space Useful for Robotic World Models [[HTML]](https://arxiv.org/html/2605.06388) [[PDF]](https://arxiv.org/pdf/2605.06388)
* **Paper ID**: `2605.06388`
* **Authors**: Nilaksh, Saurav Jha, Artem Zholus, Sarath Chandar
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇系统比较重建型 latent 与语义型 latent 对 robotic world model 的影响，问题非常基础，尤其适合后续做 world model 选型参考。它没有进入最终精选，主要因为更像表示空间评测研究，而不是直接提出新的 VLA/WAM 控制闭环方法。不过其结论趋势很重要：世界模型不能只按视觉重建质量选择 latent。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. LaST-R1: Reinforcing Robotic Manipulation via Adaptive Physical Latent Reasoning [[HTML]](https://arxiv.org/html/2604.28192) [[PDF]](https://arxiv.org/pdf/2604.28192)
* **Paper ID**: `2604.28192`
* **Authors**: Hao Chen, Jiaming Liu, Zhonghao Yan, Nuowei Han, Renrui Zhang, Chenyang Gu, Jialin Gao, Ziyu Guo, Siyuan Qian, Yinxi Wang, Peng Jia, Shanghang Zhang, Pheng-Ann Heng
* **Author Priority**: Standard
* **为什么还值得留意**: LaST-R1 进入 watchlist 是因为它把 latent reasoning-before-acting 与 RL post-training 结合，和今天的 RL+VLA 方向高度相关。LAPO 这类从 latent reasoning 到 action 的优化路线值得继续追。但它不是今日 arXiv ID 段的新论文，且摘录中涉及自定义大规模数据和真实部署细节需要更多核查，所以保留在观察名单。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
