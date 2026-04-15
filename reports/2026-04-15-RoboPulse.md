# RoboPulse | 2026-04-15

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 77 papers scanned · 10 shortlisted · 6 editor's picks

今天这组最终精选的主线非常清晰：VLA 正从“会做任务”转向“在风险、扰动、精细空间约束和跨形态条件下也能可靠工作”，同时 world model / latent reasoning 开始真正进入动作决策内环。入选论文里，既有对 VLA 语义安全与鲁棒性的直接拷问，也有用显式中间目标、动作流形、潜在 CoT 和跨本体控制去重写策略结构的尝试，因此比单纯刷成功率更值得优先看。作者层面，今天最该优先跟踪的 VIP 命中是 Jiangmiao Pang 参与的 2602.05791，它代表了跨 humanoid 通用控制这条高价值主线；其余最终精选虽未明显命中核心名单，但在评测范式、策略分解和 world modeling 上都有较强方法信号。整体上，这批论文说明：未来一阶段的竞争点，不只是更大的 VLA，而是谁能把安全、稳健性、几何精度与可迁移控制真正耦合进统一系统。

## 今日信号

- 今天最值得记住的研究信号是：VLA 评测正在从任务成功率转向“语义安全 + 近风险行为 + 扰动稳健性”的联合刻画，单一 SR 指标已经明显不够。
- 今天最值得记住的研究信号是：显式中间表示重新回到舞台中央，不论是视觉目标、潜在世界状态还是动作流形，本质上都在降低端到端策略的耦合难度。
- 今天最值得记住的研究信号是：通用机器人策略的扩展路径正在分叉，一支押注更强的 VLA/world model，另一支则强调几何、形态一致性和可部署控制结构。

## Editor's Picks

### [1]. HazardArena: Evaluating Semantic Safety in Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2604.12447) [[PDF]](https://arxiv.org/pdf/2604.12447) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.12447`
* **Authors**: Zixing Chen, Yifeng Gao, Li Wang, Yunhan Zhao, Yi Liu, Jiayu Li, Xiang Zheng, Zuxuan Wu, Cong Wang, Xingjun Ma, Yu-Gang Jiang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把 VLA 的“会做”与“做得安全吗”强行拆开，直接指出当前成功率导向评测的盲区。
* **问题与切口**: 这篇工作聚焦一个很关键但常被忽略的问题：VLA 可能在动作执行层面看似正确，却在视觉-语言语义层面触发危险后果。作者提出 HazardArena，用成对的 safe/unsafe twin scenarios 去控制变量，专门测模型是否真正理解情境风险，而不是只会把任务做完。相对已有安全评测主要标注禁行动作或只看终点成功，这篇的新意在于把“语义风险”变成可系统评估的对象，并把安全性从任务完成度里剥离出来。
* **核心方法与证据**: 从 HTML 摘录可确认，HazardArena 通过四阶段流程构建：先抽取安全类别，再做类别绑定资产、生成风险场景，最后形成安全/危险双胞胎场景。安全类别来自 ISO 13482:2014 与 DeepMind AutoRT 报告的综合，覆盖食品、财产、化学、隐私、火灾、人身和电气等七类。作者的核心证据不是只看 unsafe 场景终点 SR，而是引入 commit 一类近风险进展信号，并报告一个无需训练的 Safety Option Layer 能压低危险执行，同时尽量保住安全任务表现；但从摘录里仍看不到更细的统计幅度与分布细节。
* **正文要点**:
  - 基准以 safe/unsafe twin scenario 控制非安全因素，强调语义条件改变而非动作模板改变。
  - 作者明确指出 unsafe twin 上的 endpoint SR 会低估真实风险，需用更细的 near-hazard 指标补充。
  - 七类风险源自标准与安全报告综合，而不是随意罗列危险案例。
* **为什么值得跟**:
  - 它补上了 VLA 评测里最危险的一块空白：任务完成不等于行为安全。
  - 如果这一评测范式被接受，后续 VLA 训练目标和部署验收标准都可能被重写。
  - 训练外的轻量安全层如果稳定有效，会比重新训练整套策略更有部署吸引力。
* **风险 / 保留意见**:
  - 基准仍是受控构造场景，能否覆盖开放家庭环境中的复合长时风险还需谨慎判断。
  - Safety Option Layer 的收益边界目前只能保守理解为趋势性结果，HTML 摘录不足以支撑更细强度判断。
* **建议先看**: 先看基准构建逻辑和 twin scenario 设计，因为这决定了它是不是在测“语义安全”而不是普通鲁棒性。其次重点看 unsafe twin 指标设计与 SOL 的证据边界，判断它对现有 VLA 评测体系的冲击是否成立。
* **关键词**: `VLA 安全评测` `语义安全` `benchmark` `safe-unsafe twins` `Safety Option Layer`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
* **读 PDF 先核查**:
  - unsafe twin 中的风险是否会被场景资产或视觉提示强度泄漏，导致模型靠表面线索而非真实语义判断？
  - commit 类指标具体如何界定近风险推进，它与最终危险完成之间的相关性是否稳定？
  - SOL 作为训练外模块在不同 VLA policy 上的保性能能力是否一致，还是只对部分策略有效？
* **上传 PDF 后优先看**:
  - 基准构建章节：重点核查 twin scenario 的变量控制与七类风险定义。
  - 实验章节：优先看 unsafe twin 指标、safe/unsafe 对照结果与跨策略比较。
  - 消融或附录章节：核查 SOL 的插入方式、失败案例与误拒绝安全任务的分析。

### [2]. STRONG-VLA: Decoupled Robustness Learning for Vision-Language-Action Models under Multimodal Perturbations [[HTML]](https://arxiv.org/html/2604.10055) [[PDF]](https://arxiv.org/pdf/2604.10055) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.10055`
* **Authors**: Yuhan Xie, Yuping Yan, Yunqi Zhao, Handing Wang, Yaochu Jin
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把 VLA 鲁棒性从“多加扰动一起训”改写成两阶段解耦优化，问题定义比结果本身更重要。
* **问题与切口**: STRONG-VLA 解决的是多模态扰动下 VLA 极易脆弱的问题，尤其当视觉污染和语言噪声同时出现时，传统把鲁棒性当作单一联合目标的训练方式容易与任务保真度冲突。作者提出一个解耦式微调框架：先让模型在逐步扩大的扰动分布中获取鲁棒性，再用干净数据把策略重新拉回名义任务分布。相对常见的 joint robustness training，这篇的核心新意在于把鲁棒性视为分布依赖问题，而不是一个可以和原任务目标简单并列优化的静态属性。
* **核心方法与证据**: 从摘录看，方法有两个阶段：Stage I 做 robustness acquisition，通过逐步扩张的扰动分布暴露模型；Stage II 用 clean data 做 task-aligned refinement。实验覆盖多个 VLA backbone，明确包括 OpenVLA-7B 与 OpenVLA-OFT，另外还有一类 HTML 中名称未完整显示的骨干；OpenVLA 系列用 LoRA 做参数高效微调，另一骨干用直接策略微调。评测在 LIBERO 四个 task suites 上进行，结论强调跨骨干的稳定提升，但作者也坦承对未见视觉扰动的泛化仍有限，且扰动 taxonomy 与 curriculum 带有人工设计色彩。
* **正文要点**:
  - 方法不是把 clean 与 perturbed data 混训，而是先学抗扰再做任务对齐。
  - 评测覆盖多个 backbone，说明作者在尝试证明训练范式而非单模型技巧。
  - 作者自己承认 unseen visual perturbation 仍是短板，鲁棒性并未被彻底解决。
* **为什么值得跟**:
  - 它提出了一个更像工程系统设计的问题表述：鲁棒性获取和任务保真可能需要不同阶段处理。
  - 如果两阶段范式成立，很多 VLA 后训练流程都能用更低改动成本迁移过去。
  - 它让多模态扰动研究从“做更多增强”转向“如何组织优化过程”。
* **风险 / 保留意见**:
  - 扰动类型和难度课程依赖人工设定，实际部署中可能不覆盖最关键的失配来源。
  - HTML 摘录没有给出各 backbone 的提升幅度和代价，当前更适合把它看成方向性证据。
* **建议先看**: 先看两阶段训练定义与扰动课程设计，因为这是整篇最可迁移的方法资产。再看跨 backbone 结果和作者承认的失败面，判断它究竟是通用范式还是特定设置下的有效 recipe。
* **关键词**: `VLA 鲁棒性` `multimodal perturbation` `decoupled fine-tuning` `LoRA` `LIBERO`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - Stage I 扰动暴露后的表示变化，是否真的提升了鲁棒特征而不是单纯牺牲任务灵敏度？
  - Stage II 在多大程度上会覆盖掉 Stage I 学到的抗扰能力，是否存在明显回退？
  - 对语言噪声与视觉污染的联合扰动，方法是否优于分别处理两类扰动的简单组合基线？
* **上传 PDF 后优先看**:
  - 方法章节：核查两阶段目标、扰动扩张机制与 clean re-alignment 的具体实现。
  - 主实验章节：优先看跨 backbone、跨 LIBERO 子任务的一致性结果。
  - 限制与附录章节：重点核查 unseen 扰动失败案例、训练成本和课程设计细节。

### [3]. AnySlot: Goal-Conditioned Vision-Language-Action Policies for Zero-Shot Slot-Level Placement [[HTML]](https://arxiv.org/html/2604.10432) [[PDF]](https://arxiv.org/pdf/2604.10432) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.10432`
* **Authors**: Zhaofeng Hu, Sifan Zhou, Qinbo Zhang, Rongtao Xu, Qi Su, Ci-Jyun Liang
* **Author Priority**: Standard
* **一句话结论**: 非常值得优先看，它把 slot-level placement 这个高难问题拆成“先生成显式目标，再做精确执行”，结构上很干净。
* **问题与切口**: AnySlot 针对的是一个比普通 pick-and-place 更难的设定：机器人不仅要理解组合语言，还要在密集候选槽位里选对具体位置，并达到接近亚厘米级的落位精度。作者认为单体 VLA 把语言 grounding 与动作控制缠在一起，模块化 VLM 管线又常因中间表示不够精确而掉链子，于是引入显式空间视觉目标作为中间变量。它先把语言转成场景中的可视化 marker，再让低层策略围绕该目标执行，从而把“选哪一格”和“如何放准”分开。
* **核心方法与证据**: HTML 摘录显示，AnySlot 将策略分解为目标推断与目标条件执行两步。目标推断模块利用现成图像生成模型在 head image 上渲染彩色球形 marker，再借助对齐深度图与相机标定把 marker 提升为世界坐标锚点，随后回投到多视角形成一致 overlays，作为 VLA 策略输入。实验侧，作者构建了基于 SAPIEN 的 SlotBench，包含九类细粒度 slot 推理任务，如行列序数、尺寸比较、垂直关系、距离关系和组合关系等，用来隔离“槽位选择”而非泛化 object-level completion。
* **正文要点**:
  - 中间目标不是文本或坐标点，而是多视角一致的显式视觉 goal overlay。
  - SlotBench 专门评估 cell-level slot selection，而非传统 object-level 成功率。
  - 作者的论点是 flat policy 与 modular pipeline 各有根本缺陷，AnySlot 试图在中间表示层重新折中。
* **为什么值得跟**:
  - 这篇抓住了工业装配和精密放置里真正痛的部分：不是抓起，而是放准。
  - 显式视觉目标可能成为连接语言 grounding 与连续控制的一种可复用接口。
  - 如果 SlotBench 被社区接受，很多宣称“语言操控很强”的 VLA 会暴露细粒度空间推理短板。
* **风险 / 保留意见**:
  - 中间 marker 依赖生成模型、深度和标定链条，任何一环不稳都可能放大误差。
  - 当前证据主要来自仿真 SlotBench，真实机器人中的视觉偏差和接触误差仍需谨慎外推。
* **建议先看**: 先看方法总览和 visual goal 生成链路，判断这套中间表示到底是不是比直接坐标或热图更合理。接着重点看 SlotBench 九类任务的失败分布，理解它究竟提升了哪类细粒度推理。
* **关键词**: `slot-level placement` `goal-conditioned VLA` `visual goal` `language grounding` `SAPIEN`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 生成式 marker 是否会引入视觉先验偏差，使策略更多依赖 marker 风格而非真实场景几何？
  - 世界坐标锚点与多视角回投的误差在密集槽位场景里如何积累，是否存在临界失败模式？
  - AnySlot 对未见语言组合和未见槽位布局的泛化，主要来自 goal inference 还是 execution policy？
* **上传 PDF 后优先看**:
  - 方法章节：核查 marker 生成、3D 提升和多视角 overlay 的完整链路。
  - 基准章节：优先看 SlotBench 九类任务定义与难度控制方式。
  - 实验/案例分析章节：重点看与 flat VLA、模块化基线的对比及失败模式可视化。

### [4]. ABot-M0: VLA Foundation Model for Robotic Manipulation with Action Manifold Learning [[HTML]](https://arxiv.org/html/2602.11236) [[PDF]](https://arxiv.org/pdf/2602.11236) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2602.11236`
* **Authors**: Yandan Yang, Shuang Zeng, Tong Lin, Xinyuan Chang, Dekang Qi, Junjin Xiao, Haoyun Liu, Ronghan Chen, Yuzhi Chen, Dongjie Huo, Feng Xiong, Xing Wei, Zhiheng Ma, Mu Xu
* **Author Priority**: Standard
* **一句话结论**: 值得看，但更适合带着证据边界去读；它押注数据统一与动作流形，方向很大，HTML 可验证细节相对有限。
* **问题与切口**: ABot-M0 试图回答“one-brain, many-forms”为什么至今难落地：不是只差一个更大的模型，而是 embodied 数据碎片化、动作表示不统一、训练目标彼此错位。作者一方面构建系统化数据整理流程，把六个公开数据集清洗、标准化和平衡成 UniACT-dataset；另一方面提出 Action Manifold Hypothesis，认为有效机器人动作并不占满高维动作空间，而是落在由物理规律和任务约束塑造的低维平滑流形上。它想做的不是单点提分，而是重新组织跨平台通用操控的底座。
* **核心方法与证据**: HTML 摘录能确认的强证据包括：UniACT-dataset 覆盖六个公开数据源，规模超过 600 万轨迹与 9500 小时；预训练只使用 OXE、AgiBot-Beta、RoboCoin，Libero 用于下游监督微调；验证集构造按不同数据集的主要多样性维度分层抽样，以避免被规模主导。作者强调不同双臂采样策略会带来结构性偏差，并在跨数据集、跨 embodiment 设定下系统评估泛化。但关于 ABot-M0 的具体架构、动作流形模块如何实现、训练损失如何设计，当前 HTML 摘录提供的信息仍不充分，因此只能保守判断其方法论很强、技术细节待 PDF 核查。
* **正文要点**:
  - 作者把问题定义为数据、表示和训练目标三者同时失配，而非单一模型能力不足。
  - UniACT-dataset 的构建强调清洗、标准化与平衡，而不是简单拼接多源数据。
  - 实验中特别讨论双臂采样策略引入的结构性偏差，这是很多 foundation policy 论文少见的角度。
* **为什么值得跟**:
  - 它把通用操控基础模型的关键瓶颈重新放回数据工程和动作表示，而不只是 backbone 规模。
  - Action Manifold 视角如果成立，可能为更稳、更高效的动作预测提供统一解释。
  - 这类工作对跨平台机器人策略训练很有现实价值，因为它优先解决数据和 embodiment 不一致问题。
* **风险 / 保留意见**:
  - 当前 HTML 信息不足以支撑对具体模型设计和实验优势做强判断，阅读时必须警惕被大叙事带走。
  - 多源大规模数据整合的质量控制极其关键，若平衡与清洗策略不稳，模型收益可能更多来自数据量而非方法本身。
* **建议先看**: 先不要急着看结果表，先核查数据管线、采样偏差分析和 Action Manifold 的形式化定义，这三处决定这篇是否真有方法贡献。随后再看预训练/微调切分与跨 embodiment 泛化证据，判断它是不是在避免数据泄漏和任务投机。
* **关键词**: `foundation manipulation model` `Action Manifold` `data curation` `cross-embodiment` `UniACT-dataset`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - Action Manifold 在模型里是显式潜变量、约束正则，还是某种解码结构假设？
  - UniACT-dataset 的标准化是否保留了不同机器人间关键控制语义，还是在统一过程中损失了可迁移细节？
  - 双臂采样策略造成的偏差，最终是如何影响下游泛化而不是仅影响训练分布统计？
* **上传 PDF 后优先看**:
  - 数据章节：重点核查六个数据源的清洗、标准化和平衡流程。
  - 方法章节：优先核查 Action Manifold Hypothesis 的建模形式与训练目标。
  - 实验章节：重点看跨数据集/跨 embodiment 评测、Libero 下游设置与采样策略消融。

### [5]. Latent Chain-of-Thought World Modeling for End-to-End Driving [[HTML]](https://arxiv.org/html/2512.10226) [[PDF]](https://arxiv.org/pdf/2512.10226) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2512.10226`
* **Authors**: Shuhan Tan, Kashyap Chitta, Yuxiao Chen, Ran Tian, Yurong You, Yan Wang, Wenjie Luo, Yulong Cao, Philipp Krahenbuhl, Marco Pavone, Boris Ivanovic
* **Author Priority**: Standard
* **一句话结论**: 很值得优先看，它把 world model 和推理链真正塞进驾驶动作生成里，而且明确抛弃了文本 CoT 的低效表示。
* **问题与切口**: LCDrive 解决的是端到端自动驾驶里一个越来越核心的问题：如果要在推理时显式“想一想”，文本型 chain-of-thought 真的是合适载体吗？作者的回答是否定的。他们提出 latent CoT，把推理表示成与动作候选对齐的潜在世界模型状态，让模型在考虑动作时同步预测其可能带来的未来结果。相较已有先输出文本解释再给驾驶动作的做法，这篇的新意在于把 reasoning 与 decision making 放进统一的 action-aligned latent space，让推理更贴近多智能体时空几何而不是自然语言描述。
* **核心方法与证据**: 从 HTML 摘录看，模型引入 ego-centric latent world model state，用在线感知得到的自车与邻近体的向量化框和姿态表示状态。每个状态窗口覆盖 1.0 秒、10Hz 的固定长度历史或未来片段，再经轻量 Transformer 编码成 world-model tokens；未来 token 由候选动作条件化生成，从而形成交替的 proposal-action 与 latent world tokens。实验使用 PhysicalAI-AV 的大规模真实驾驶日志，并采用一个场景平衡子集，训练/验证覆盖 nominal 与 eventful scenes。结论声称 latent CoT 同时带来更低推理延迟、更好轨迹质量，并能从 RL post-training 中继续获益；但具体幅度仍需 PDF 核对。
* **正文要点**:
  - 作者明确批评文本 CoT 不适合表达驾驶中的时空几何和多体互动。
  - 潜在推理状态以固定时间窗的向量化世界表示为基础，而非自由生成文本解释。
  - 实验数据强调 scenario-balanced，而不是让简单场景淹没有挑战的事件场景。
* **为什么值得跟**:
  - 它把 world model 从辅助预测器推到决策核心，方向上非常接近未来 VLA/驾驶统一体。
  - latent CoT 提供了一个比文本 reasoning 更贴合控制问题的中间表示范式。
  - 如果 RL post-training 在这种潜在推理空间里更有效，说明 reasoning 和 policy improvement 可以更深度耦合。
* **风险 / 保留意见**:
  - 潜在 token 的可解释性明显弱于文本 CoT，调试和安全审计可能更困难。
  - 当前证据集中在数据集与离线评测设定，真实闭环部署表现仍需保守看待。
* **建议先看**: 先看 latent world state 如何编码历史/未来窗口，以及 proposal-action 与 world tokens 如何交替作用，这是整篇的技术核心。然后重点看与 text-CoT baseline 的对比维度，确认优势究竟来自表示形式还是更强的训练配置。
* **关键词**: `world model` `latent CoT` `end-to-end driving` `action-aligned reasoning` `RL post-training`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - latent CoT 的收益主要来自更适合驾驶几何的表示，还是来自减少了文本自回归的推理开销？
  - 候选动作与未来 world tokens 的交替机制，是否会导致对 perception 误差的级联放大？
  - RL post-training 改善的是哪类场景能力，是否集中在 eventful scenes 而非一般驾驶？
* **上传 PDF 后优先看**:
  - 方法章节：核查 latent world state、tokenization 和 action-world interleaving 机制。
  - 数据与设置章节：重点看 PhysicalAI-AV 子集的场景平衡构造与任务定义。
  - 实验章节：优先看与 non-reasoning、text-CoT、RL post-training 的分项对比。

### [6]. Scalable and General Whole-Body Control for Cross-Humanoid Locomotion [[VIP]] [[HTML]](https://arxiv.org/html/2602.05791) [[PDF]](https://arxiv.org/pdf/2602.05791) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2602.05791`
* **Authors**: Yufei Xue, YunFeng Lin, Wentao Dong, Yang Tang, Jingbo Wang, Jiangmiao Pang, Ming Zhou, Minghuan Liu, Weinan Zhang
* **Author Priority**: Core VIP
* **一句话结论**: 这是今天最该优先跟踪的 VIP 论文之一，跨 humanoid 通用 whole-body control 做得很硬，而且真实部署证据明确。
* **问题与切口**: XHugWBC 直指 humanoid 控制里最贵的痛点：几乎每来一个新机器人就要重训一套控制器。作者试图用一次训练得到可跨本体泛化的 whole-body controller，关键做法不是简单堆形态随机化，而是把物理一致的形态随机化、语义对齐的观测/动作空间，以及能建模形态差异的策略结构放进同一训练框架。相对很多单机体最优控制路线，这篇更像在回答“能不能先有一个 humanoid 通用底座”，因此对具身基础模型和 Sim2Real 都有高参考价值。
* **核心方法与证据**: HTML 摘录显示，方法核心之一是 physics-consistent morphological randomization。作者强调惯性参数必须满足物理一致性，不能像部分仿真随机化工作那样线性缩放出不合理刚体；这对复杂 humanoid 结构尤其重要。实验问题设置也很完整，围绕未见机器人泛化、作为微调初始化的价值、对 cross-embodiment baseline 的比较、策略架构选择，以及仿真到真实差异展开。最关键的正文证据是：在 12 个训练外机器人上，通用策略实现 100% survival rate，并保持高命令跟踪精度，且作者明确做了仿真和真实世界双重验证。
* **正文要点**:
  - 作者把“物理一致性”作为形态随机化的硬约束，而不是把 morphology randomization 当作自由扰动。
  - 评测覆盖 12 个未见机器人，并把 zero-shot 泛化与 per-robot specialist policy 直接对照。
  - 整篇研究问题设置很像系统论文，既问能否泛化，也问能否作为后续微调初始化。
* **为什么值得跟**:
  - 它回应了 humanoid 规模化部署最现实的问题：控制策略如何跨平台复用。
  - 如果通用策略能稳健做初始化，机器人新机型导入成本会明显下降。
  - 这条路线把跨 embodiment 学习从动画或离线运动迁移，推进到高动态 whole-body control。
* **风险 / 保留意见**:
  - 100% survival rate 很亮眼，但仅凭 HTML 摘录仍无法判断任务难度分布和更细粒度控制质量。
  - 语义对齐的观测/动作空间若设计得过强，可能隐含较重人工先验，影响向更异质 humanoid 的继续扩展。
* **建议先看**: 先看 morphology randomization 与语义对齐空间的定义，因为这两点决定它是不是在学真正可迁移的控制规律。之后重点核查 unseen robot 结果和 real-world deployment 章节，确认泛化不是由评测任务过于保守造成。
* **关键词**: `cross-humanoid control` `whole-body control` `morphological randomization` `zero-shot generalization` `sim-to-real`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 物理一致的形态随机化具体如何参数化，是否会显著限制随机化覆盖范围？
  - 语义对齐的 observation/action space 是否要求不同 humanoid 具备较强的人工映射关系？
  - 通用策略相对 specialist 的差距主要体现在哪些高动态或长时任务上？
* **上传 PDF 后优先看**:
  - 方法章节：核查 physics-consistent morphological randomization 的约束形式。
  - 主实验章节：优先看 12 个 unseen robots 的 zero-shot 结果、baseline 对比和初始化微调实验。
  - 真实部署章节：重点看 sim-real 差距、失败案例和长时 whole-body task 表现。

## Watchlist

### [W1]. BINDER: Instantly Adaptive Mobile Manipulation with Open-Vocabulary Commands [[HTML]](https://arxiv.org/html/2511.22364) [[PDF]](https://arxiv.org/pdf/2511.22364)
* **Paper ID**: `2511.22364`
* **Authors**: Seongwon Cho, Daechul Ahn, Donghyun Shin, Hyeonbeom Choi, San Kim, Jonghyun Choi
* **Author Priority**: Standard
* **为什么还值得留意**: BINDER 进入 shortlist 的原因很充分：它把开放词汇移动操作中的连续环境监测与高成本 3D 重建解耦，系统问题抓得很准，而且有真实家庭/办公室实验支撑。之所以没进最终精选，是因为今天的主线更偏向 VLA 安全、鲁棒性、world model 和通用控制，而它更像一篇强系统集成论文；另外其核心增益更多来自双过程系统设计，而非直接推进 VLA 方法本体。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. Robotic Manipulation is Vision-to-Geometry Mapping ($f(v) \rightarrow G$): Vision-Geometry Backbones over Language and Video Models [[HTML]](https://arxiv.org/html/2604.12908) [[PDF]](https://arxiv.org/pdf/2604.12908)
* **Paper ID**: `2604.12908`
* **Authors**: Zijian Song, Qichang Li, Jiawei Zhou, Zhenlong Yuan, Tianshui Chen, Liang Lin, Guangrun Wang
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇值得持续跟踪，因为它明确反驳“语言/视频 backbone 自然最适合机器人操控”的默认前提，转而主张 vision-to-geometry backbone，是很强的方法立场。没进最终精选，主要因为当前摘录里实验证据和具体优势边界还不够展开；同时它更像对路线的宣言与重构，暂时不如最终入选几篇在评测、结构分解或部署证据上扎实。
* **证据来源**: arXiv HTML (Introduction, Method)

### [W3]. Habitat-GS: A High-Fidelity Navigation Simulator with Dynamic Gaussian Splatting [[HTML]](https://arxiv.org/html/2604.12626) [[PDF]](https://arxiv.org/pdf/2604.12626)
* **Paper ID**: `2604.12626`
* **Authors**: Ziyuan Xia, Jingyi Xu, Chong Cui, Yuanhong Yu, Jiazhao Zhang, Qingsong Yan, Tao Ni, Junbo Chen, Xiaowei Zhou, Hujun Bao, Ruizhen Hu, Sida Peng
* **Author Priority**: Standard
* **为什么还值得留意**: Habitat-GS 之所以在 watchlist，是因为高保真 3DGS 场景和动态 gaussian avatar 对 Sim2Real 导航训练很有现实意义，且它保持 Habitat 生态兼容，工具价值很高。没有进最终精选，是因为它更偏仿真平台基础设施，而不是直接面向今天聚焦的 VLA/world action model 方法突破；此外作者自己也承认视觉-导航解耦限制了更完整的物理交互。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

### [W4]. E2E-Fly: An Integrated Training-to-Deployment System for End-to-End Quadrotor Autonomy [[HTML]](https://arxiv.org/html/2604.12916) [[PDF]](https://arxiv.org/pdf/2604.12916)
* **Paper ID**: `2604.12916`
* **Authors**: Fangyu Sun, Fanxing Li, Linzuo Zhang, Yu Hu, Renbiao Jin, Shuyu Wu, Wenxian Yu, Danping Zou
* **Author Priority**: Standard
* **为什么还值得留意**: E2E-Fly 进入 shortlist 的原因是它覆盖了从训练到部署的完整 quadrotor 端到端系统，并把 differentiable simulation、RL 与真实转移放到统一框架里，工程闭环感很强。没有进最终精选，一方面它与今天的 VLA/世界模型主线关联较弱，另一方面摘录里更突出的其实是系统平台与训练管线，而非一个足够尖锐、可外溢到更广泛 embodied research 的新方法核心。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
