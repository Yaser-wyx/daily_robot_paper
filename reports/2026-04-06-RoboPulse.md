# RoboPulse | 2026-04-06

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 53 papers scanned · 10 shortlisted · 5 editor's picks

今天这组最终精选围绕一条很清晰的主线展开：机器人系统正在从“单次大模型决策”转向“可验证、可预测、可迁移”的执行范式，重点落在 VLA 推理效率、3D 时空建模、动作表示瓶颈、世界模型迁移，以及可解释策略结构化五个切口。入选论文之所以突出，是因为它们都不是单纯堆模型规模，而是在真实部署约束下重新设计控制闭环、表示接口或训练监督，研究信号比单点性能更强。相较之下，今天的 VIP 作者并未占据最终精选核心席位，但扩展名单里的 Pulkit Agrawal，以及核心名单里的 Jiangmiao Pang 仍值得优先跟踪，因为他们分别对应“控制接口如何影响学习”和“跨平台部署基础设施”两条很可能继续放大的系统线。整体判断是：本日最有价值的不是某个单一 SOTA，而是 VLA/世界模型/控制系统之间边界正在被重新划分。

## 今日信号

- 今天最值得记住的研究信号是：VLA 的下一阶段竞争点正在从“能不能做”转向“能否在低延迟闭环里稳定做对”，因此验证器、异步补偿和系统层重构会越来越重要。
- 今天最值得记住的研究信号是：3D 时空视频预测和世界模型式表征正在重新进入机器人主线，但它们的价值更体现在可解释规划与泛化，而非立刻取代所有端到端策略。
- 今天最值得记住的研究信号是：动作表示本身正在成为 VLA 缩放的新瓶颈，离散 token、控制器增益、执行中间件这些过去被当作工程细节的接口，正在决定模型扩展收益能否真正落到机器人性能上。

## Editor's Picks

### [1]. Open-Loop Planning, Closed-Loop Verification: Speculative Verification for VLA [[HTML]](https://arxiv.org/html/2604.02965) [[PDF]](https://arxiv.org/pdf/2604.02965) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.02965`
* **Authors**: Zihua Wang, Zhitao Lin, Ruibo Li, Yu Zhang, Xu Yang, Siya Mi, Xiu-Shen Wei
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它抓住了 VLA 落地里最现实的问题之一：如何在不牺牲闭环反应能力的前提下，把长 action chunk 的效率收益真正用起来。
* **问题与切口**: 这篇工作针对 action chunking VLA 的核心矛盾下手：长时域开环执行能显著减轻大模型推理负担，但一旦环境发生偏移，就容易因缺少反馈而累计误差。作者提出 SV-VLA，用“低频宏规划 + 高频轻量验证”的解耦框架替代单一重模型持续闭环控制。其新意不在再造一个更大的 VLA，而在于指出标准 speculative decoding 并不能直接照搬到 embodied control，并据此把“推测”改写为“计划先行、执行中持续核验”的控制范式。
* **核心方法与证据**: 从 HTML 摘录看，方法主干包括一个重型 Macro-Planner 负责低频生成长 action chunk，一个轻量 verifier 基于实时观测高频检查执行偏离，并通过 deviation-based replanning 在需要时触发重新规划。训练部分还专门设计了 verifier 的学习策略。证据主要来自 LIBERO 三个任务套件上的在线 rollout，对比指标是任务成功率与推理延迟；实现上以 OpenVLA-OFT、chunk size 64 为重模型基座，并在统一 GPU 条件下评估效率与可靠性的权衡。现有摘录足以支持“系统设计有效”，但不足以细判 verifier 学到的是何种偏差判别边界。
* **正文要点**:
  - 作者明确论证标准 speculative decoding 与 embodied control 的闭环响应需求存在错配，这是方法设计的直接出发点。
  - 系统被拆成重型长时域规划器与轻量高频验证器两层，而不是让单个 VLA 同时承担所有控制职责。
  - 实验聚焦 LIBERO 在线 rollout，并同时报告成功率与推理延迟，强调的是效率-可靠性折中而非单一性能。
* **为什么值得跟**:
  - 它把 VLA 部署问题从“如何更快生成动作”推进到“如何在快的同时保住闭环鲁棒性”。
  - 如果验证器足够轻，这类架构有机会成为大模型控制在真实机器人上的通用加速模板。
  - 它也提示后续 VLA 研究应把控制系统设计纳入核心贡献，而不只比较 backbone 或数据规模。
* **风险 / 保留意见**:
  - 当前证据主要来自仿真 LIBERO，真实机器人中的观测噪声、控制延迟和验证误判代价仍未在摘录中展开。
  - verifier 何时触发 replanning、阈值如何设定、误检漏检如何影响整体稳定性，现有 HTML 证据还不够充分。
* **建议先看**: 先沿着“为何标准 speculative decoding 不适用于 embodied control”这条论证线读，再看 decoupled architecture 和 deviation-based replanning 如何把这个论点落成系统。最后再用主实验判断它到底是在买到真实闭环鲁棒性，还是只是更聪明地做了 action chunking。
* **关键词**: `VLA` `action chunking` `speculative verification` `closed-loop control` `LIBERO`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - verifier 判定“偏离”的具体监督信号和时序输入是什么，它更像二分类守门器还是连续风险估计器？
  - replanning 的触发频率与 chunk 长度之间是否存在稳定工作区间，还是需要对任务/环境单独调参？
  - 在成功率提升之外，验证器是否主要修复了少量关键失误模式，还是普遍改善了长链条执行稳定性？
* **上传 PDF 后优先看**:
  - 方法章节中关于 speculative decoding 与 embodied control 不匹配的分析部分
  - 系统设计章节里 Macro-Planner、verifier 与 deviation-based replanning 的接口定义
  - 主实验与消融章节中成功率-延迟权衡、chunk 长度和 verifier 作用的对比结果

### [2]. Multi-View Video Diffusion Policy: A 3D Spatio-Temporal-Aware Video Action Model [[HTML]](https://arxiv.org/html/2604.03181) [[PDF]](https://arxiv.org/pdf/2604.03181) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.03181`
* **Authors**: Peiyan Li, Yixiang Chen, Yuan Xu, Jiabing Yang, Xiangnan Wu, Jun Guo, Nan Sun, Long Qian, Xinghang Li, Xin Xiao, Jing Liu, Nianfeng Liu, Tao Kong, Yan Huang, Liang Wang, Tieniu Tan
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它代表了机器人策略里一条更少见但很有潜力的路线：把 3D 结构先验和视频生成式表征真正绑到动作建模里。
* **问题与切口**: MV-VDP 试图解决两个长期割裂的问题：操控策略常用 2D 观测学习 3D 物理动作，同时又大量依赖静态图文预训练 backbone，导致时空动态理解不足、数据需求偏高。作者提出 multi-view video diffusion policy，通过同时预测多视角 heatmap 视频与 RGB 视频，去对齐“视频预训练表征”和“机器人动作后果预测”这两件事。从摘要与正文摘录看，它更像一个 3D spatio-temporal-aware video action model，而不只是把扩散策略换成多摄像头输入。
* **核心方法与证据**: 现有摘录显示，方法核心是利用 3D-aware multi-view projections 引入结构先验，并以视频基础模型作为 backbone，在生成未来视频的同时建模动作。实验设计覆盖模拟与真实场景，并明确围绕七个问题展开：与视频预测类方法、3D 输入类方法、VLA 方法的比较；对背景、物体高度、光照、类别等未见条件的泛化；扩散步数鲁棒性；架构关键设计是否必要；预测视频是否忠实反映动作后果。结论部分还给出一个重要边界：生成 24 帧 action chunk 的推理仍较慢。
* **正文要点**:
  - 作者把“多视角 heatmap 视频 + RGB 视频联合预测”作为统一表示，强调其既承接视频预训练，又显式编码 3D 结构。
  - 实验问题设计非常完整，不只比性能，还专门检查泛化、超参数鲁棒性、模块必要性与预测可解释性。
  - 结论明确承认推理速度仍是瓶颈，说明该路线当前更强在表征与泛化，不一定已适合高频实时控制。
* **为什么值得跟**:
  - 它把视频世界建模与机器人动作策略更紧密地耦合起来，接近 world action model 的方向。
  - 若多视角视频预测确实忠实对应执行结果，这类方法有望同时提供控制能力与可解释中间表征。
  - 它也在挑战当前 VLA 过度依赖静态图文预训练的默认做法，提示视频预训练可能更契合操控动态。
* **风险 / 保留意见**:
  - 从摘录可见推理较慢，因此在高频闭环或延迟敏感任务上的部署成本可能很高。
  - HTML 片段没有展开多视角投影、heatmap 构造和动作解码细节，当前还难判断工程复杂度与复现门槛。
* **建议先看**: 先看作者如何定义“3D 时空状态”的建模对象，再重点核查多视角 heatmap/RGB 联合预测为何能比单纯视频预测或 3D 输入法更有效。读实验时优先关注泛化和预测真实性，而不只是平均成功率。
* **关键词**: `video diffusion policy` `multi-view` `3D spatio-temporal modeling` `robot manipulation` `video foundation model`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - heatmap 视频承担的是几何对齐、关键状态压缩，还是对 RGB 预测的训练稳定器作用？
  - 多视角信息带来的收益主要来自显式 3D 投影，还是仅仅来自更多观测冗余？
  - 预测视频与动作输出之间的耦合方式会不会让模型更可解释，但也更难满足实时部署要求？
* **上传 PDF 后优先看**:
  - 方法章节中 multi-view heatmap 视频、RGB 视频与动作建模之间的具体接口
  - 实验章节里与视频预测类、3D 表征类和 VLA 类基线的分组对比
  - 泛化、扩散步数鲁棒性与预测视频真实性分析相关的小节

### [3]. The Compression Gap: Why Discrete Tokenization Limits Vision-Language-Action Model Scaling [[HTML]](https://arxiv.org/html/2604.03191) [[PDF]](https://arxiv.org/pdf/2604.03191) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.03191`
* **Authors**: Takuya Shiba
* **Author Priority**: Standard
* **一句话结论**: 非常值得优先看，这是今天最强的“研究判断型”论文之一：它不靠堆新模型，而是直接解释了为什么很多 VLA 缩放直觉会失灵。
* **问题与切口**: 这篇论文的核心贡献是提出 Compression Gap：在 visuomotor pipeline 里，扩展收益由最紧的信息瓶颈决定，而不是简单由上游视觉编码器质量决定。作者用这个视角解释一个常被默认成立的假设为何失效：把视觉编码器从普通模型升级到更强表征，并不一定会提升离散动作 token 化 VLA 的操控表现。相对已有工作，它的新意在于把“VLA 为什么没吃到视觉 scaling 红利”从经验现象提升为动作表示层面的结构性问题，并把连续动作与离散动作路线放到同一受控框架下比较。
* **核心方法与证据**: 从摘录可见，作者在同一代码库、训练流程和评估协议下做了一个三因素 factorial 实验，核心变量包括动作表示方式、编码器质量和模型规模，以隔离交互效应。连续路线用 Diffusion Policy，离散路线用 OAT 与固定容量 FSQ codebook；同时还做了两个补充实验：沿编码器质量梯度检查性能敏感性，以及改变 codebook size 测试离散瓶颈放松后是否恢复对编码器升级的响应。摘要中还明确给出一条较强证据：编码器升级可显著提升连续动作策略，而离散路线收益被明显削弱。
* **正文要点**:
  - 论文把性能缩放失败定位为“瓶颈位置错误”问题，而不是简单归因于模型不够大或训练不够久。
  - 实验设计强调受控比较：相同代码库、相同训练协议，只替换动作表示、编码器质量和模型规模等关键变量。
  - 作者不仅比较离散与连续路线，还进一步通过 codebook size 变化来检验离散瓶颈是否真是关键解释变量。
* **为什么值得跟**:
  - 它直接影响 VLA 研究的资源分配：如果动作离散化本身卡住信息流，单纯升级 vision encoder 可能回报有限。
  - 这为连续动作、扩散策略和更高容量 action tokenizer 提供了更坚实的论据。
  - 从研究方法上看，它示范了如何把“缩放失灵”这种模糊现象转成可验证的结构性假说。
* **风险 / 保留意见**:
  - 当前证据集中于 LIBERO 与特定 OAT/DP 实例，结论是否能外推到更广泛 VLA 架构仍需谨慎。
  - Compression Gap 是很强的统一解释，但 HTML 摘录不足以判断是否还有训练稳定性或优化细节等替代因素同样重要。
* **建议先看**: 先把它当成一篇“动作表示决定缩放收益”的论文来读，而不是单纯的 baseline 对比。最值得优先核查的是 factorial design 与两个补充实验是否真的把信息瓶颈解释钉实。
* **关键词**: `VLA scaling` `action tokenization` `Compression Gap` `Diffusion Policy` `information bottleneck`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 作者如何排除离散路线性能受限其实来自优化难度、训练步数或解码策略，而不只是 codebook 容量？
  - encoder quality gradient 是否表现为连续单调趋势，还是只是在少数编码器切换点上出现跳变？
  - 增大 codebook 后若恢复了 encoder sensitivity，这种恢复是否伴随训练或推理成本显著上升？
* **上传 PDF 后优先看**:
  - Compression Gap 理论动机与信息瓶颈分析章节
  - factorial experiment 的变量定义、控制条件与主结果表述
  - encoder quality gradient 与 codebook size variation 两个补充实验小节

### [4]. Learning Task-Invariant Properties via Dreamer: Enabling Efficient Policy Transfer for Quadruped Robots [[HTML]](https://arxiv.org/html/2604.02911) [[PDF]](https://arxiv.org/pdf/2604.02911) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.02911`
* **Authors**: Junyang Liang, Yuxuan Liu, Yabin Chang, Junfan Lin, Junkai Ji, Hui Li, Changxin Huang, Jianqiang Li
* **Author Priority**: Standard
* **一句话结论**: 值得看，尤其适合关注 world model 与 sim2real 交叉的人；它的亮点不是更强 locomotion trick，而是把任务不变属性显式塞进 Dreamer 式世界模型。
* **问题与切口**: DreamTIP 关注四足机器人跨地形 locomotion 的 sim-to-real 转移难题。与常见的 domain randomization、domain adaptation 或单纯改进模拟器不同，它试图在 Dreamer 世界模型框架中显式学习 Task-Invariant Properties，用那些跨环境、跨域更稳定的属性来支撑策略迁移。摘要里举到的接触稳定性等线索说明，作者希望把“哪些因素对任务本质重要”从隐式表征里拉出来，并借助大语言模型引导这些属性的识别。新意因此在于：不是只让世界模型预测未来，而是让它更偏向抓住对迁移最有用的不变量。
* **核心方法与证据**: HTML 摘录显示，方法建立在 Dreamer 类 latent dynamics prediction 路线上，并结合 Task-Invariant Properties 学习来增强跨域泛化；作者把这项设计放在世界模型支持预测与规划的脉络中来论证。实验同时覆盖 Isaac Gym 仿真和真实 Unitree Go2 部署，观测包含本体感觉与深度图像，特权信息则额外包括线速度、高程图、摩擦系数、质心位置和足端接触力等。真实部署直接运行在 Go2 机载 Orin Nano 上，并用 D435i 深度相机配合时空滤波减轻视觉 sim-to-real gap。就摘录而言，系统设定较完整，但不变量提取如何被 LLM 实际指导还需要 PDF 核查。
* **正文要点**:
  - 作者把世界模型用于跨域泛化问题，而不仅是提高样本效率或做短期预测。
  - Task-Invariant Properties 被作为显式学习对象引入，摘要中点到接触稳定性等跨任务稳定属性。
  - 实验链路覆盖 Isaac Gym 到真实 Go2 机载部署，说明方法目标是直接服务 sim-to-real 而非只做仿真验证。
* **为什么值得跟**:
  - 它代表 world model 正在从“学环境”走向“学可迁移结构”，这对 sim2real 很关键。
  - 若任务不变属性真能被显式抽出，策略迁移可能不再那么依赖大规模真实微调。
  - 四足 locomotion 是高频、强动力学任务，若此思路有效，其方法价值可能外溢到更广的具身控制。
* **风险 / 保留意见**:
  - LLM 如何识别或约束 Task-Invariant Properties 在摘录中仍较模糊，方法可靠性可能高度依赖这一步定义质量。
  - 实验设定里使用了特权信息，最终真实部署时这些信号如何影响训练-部署差距，需要仔细核查。
* **建议先看**: 先盯住 Task-Invariant Properties 在世界模型里的角色：它究竟是辅助表征、训练正则，还是直接进入规划/策略头。然后再看 sim-to-real 结果是否真的来自不变量学习，而不是常规工程增强。
* **关键词**: `Dreamer` `world model` `sim-to-real` `quadruped locomotion` `task-invariant properties`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)
* **读 PDF 先核查**:
  - LLM 在 TIP 发现流程中到底提供了语义先验、属性候选，还是直接参与训练目标构造？
  - TIP 表征与 Dreamer latent state 的关系是什么，是否存在显式解耦或专门监督？
  - 真实迁移收益主要出现在地形变化、视觉差异，还是动力学参数偏移这几类 gap 中？
* **上传 PDF 后优先看**:
  - 方法章节中 TIP 与 Dreamer latent dynamics 结合的具体机制
  - 实验章节里仿真到真实部署的训练/评测协议与特权信息使用方式
  - 真实机器人结果与跨地形泛化分析相关的章节或可视化

### [5]. Learning Structured Robot Policies from Vision-Language Models via Synthetic Neuro-Symbolic Supervision [[HTML]](https://arxiv.org/html/2604.02812) [[PDF]](https://arxiv.org/pdf/2604.02812) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.02812`
* **Authors**: Alessandro Adami, Tommaso Tubaldo, Marco Todescato, Ruggero Carli, Pietro Falco
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，如果你关心安全关键机器人系统，这篇比典型端到端 VLA 更有研究辨识度，因为它把结构化策略学习重新拉回主舞台。
* **问题与切口**: 这篇工作要解决的不是“怎样从视觉学动作”本身，而是“怎样让 foundation model 产出的机器人策略具备可分析、可约束、可反应的结构”。作者以 Behavior Tree 作为目标策略形式，试图把 VLM/VLA 的多模态感知能力与经典机器人中的模块化执行逻辑接起来。路径上并没有依赖真实示教，而是用 synthetic neuro-symbolic supervision 生成结构化监督，再通过监督微调把通用视觉语言模型专门化为 BT 合成器。相对现有黑箱 visuomotor policy，这篇更像是在问：能否让基础模型学会输出机器人可执行的程序化策略。
* **核心方法与证据**: 从摘录可见，训练被形式化为一个 SFT 任务，输入包含视觉观测、语言意图、系统约束，输出是目标 symbolic execution trace。基础模型选用 Pixtral-12B，并采用内存高效的适配策略，以在边缘部署约束下完成专门化。实验上，除了标准的 causal cross-entropy，还专门监控 Perplexity 来衡量模型对 JSON-BT 语法的掌握程度，并同时关注显存峰值等训练代价指标。结论宣称模型学到的是结构先验而非模板记忆，并能迁移到新场景配置和不同机器人平台；但摘录尚不足以验证其功能正确性是否和语法正确性同步提升。
* **正文要点**:
  - 论文把结构化 JSON-Behavior Tree 生成视为核心输出，而不是直接预测低层连续动作。
  - 监督来自程序化生成的 synthetic neuro-symbolic 数据，而非真实机器人演示。
  - 评估不只看损失，还显式检查 BT 语法掌握程度与训练资源开销，说明作者重视可部署性。
* **为什么值得跟**:
  - 它为“基础模型 + 可解释机器人控制”提供了一条不同于端到端 VLA 的替代路线。
  - 若合成监督足够有效，安全关键场景中结构化策略学习可能比黑箱动作策略更可审计。
  - 这也提示机器人基础模型未必都要输出动作 token，输出符号程序同样可能是强接口。
* **风险 / 保留意见**:
  - syntactic validity 不等于 task-level correctness，模型可能学会生成结构上正确但执行上脆弱的 BT。
  - 完全依赖合成监督的分布能否覆盖真实世界约束，现有摘录只能支持初步乐观判断。
* **建议先看**: 先看 synthetic neuro-symbolic supervision 是如何构造出有效 BT 学习信号的，再看模型是否真学到了可迁移结构先验而不是格式模板。读实验时要区分“语法正确”与“任务成功”两类证据。
* **关键词**: `Vision-Language Model` `Behavior Tree` `synthetic supervision` `neuro-symbolic` `structured robot policy`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 合成数据里的场景、约束和执行 trace 是如何生成的，是否足以逼出真正的组合泛化？
  - BT 输出在不同机器人平台间迁移时，哪些部分是通用逻辑，哪些部分仍需平台特定适配？
  - 模型学到的究竟是结构化任务分解能力，还是对合成语料模板的高精度拟合？
* **上传 PDF 后优先看**:
  - 数据生成与 synthetic neuro-symbolic supervision 的构造章节
  - 模型与 SFT 设置章节中 Pixtral-12B 适配和输出格式约束部分
  - 实验章节里语法有效性、跨场景迁移与跨平台迁移相关结果

## Watchlist

### [W1]. ARM: Advantage Reward Modeling for Long-Horizon Manipulation [[HTML]](https://arxiv.org/html/2604.03037) [[PDF]](https://arxiv.org/pdf/2604.03037)
* **Paper ID**: `2604.03037`
* **Authors**: Yiming Mao, Zixi Yu, Weixin Mao, Yinhao Li, Qirui Hu, Zihan Lan, Minzhao Zhu, Hua Chen
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇进入 shortlist，是因为它把长时程操作中的奖励工程问题抓得很准：用 relative advantage 而不是绝对进度做监督，并配上 tri-state 标注、全局进度重建和 AW-BC，整体方法链条相当完整。它也和“RL + manipulation + 长链条恢复行为”这条线高度相关，且有真实双臂毛巾折叠场景支撑。没有进入最终精选，主要是因为它更偏 reward modeling 与离线/模仿增强式优化，和今天 VLA / world model / world action model 主线相比相关性略次一档。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. Tune to Learn: How Controller Gains Shape Robot Policy Learning [[VIP]] [[HTML]](https://arxiv.org/html/2604.02523) [[PDF]](https://arxiv.org/pdf/2604.02523)
* **Paper ID**: `2604.02523`
* **Authors**: Antonia Bronars, Younghyo Park, Pulkit Agrawal
* **Author Priority**: Extended VIP
* **为什么还值得留意**: 这篇值得保留在 watchlist，核心原因是它提出了一个很重要但常被忽略的判断：位置控制器增益不是简单的执行参数，而是会改变策略学习接口的 inductive bias。Pulkit Agrawal 也使它具备持续跟踪价值。之所以未进最终精选，是因为它更像机器人学习中的控制接口研究，而不是直接推进 VLA、世界模型或 sim2real 新范式；但从长期看，它对“动作接口如何限制学习收益”的启发性很强。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

### [W3]. F2F-AP: Flow-to-Future Asynchronous Policy for Real-time Dynamic Manipulation [[HTML]](https://arxiv.org/html/2604.02408) [[PDF]](https://arxiv.org/pdf/2604.02408)
* **Paper ID**: `2604.02408`
* **Authors**: Haoyu Wei, Xiuwei Xu, Ziyang Cheng, Hang Yin, Angyuan Ma, Bingyao Yu, Jie Zhou, Jiwen Lu
* **Author Priority**: Standard
* **为什么还值得留意**: F2F-AP 进入 shortlist，是因为它抓住了异步推理在动态操作中的真实痛点：动作永远落后于环境，于是作者用预测 object flow 合成未来观测来补偿系统延迟。这个思路与今天的“低延迟闭环”主线很贴近，也覆盖固定机械臂和移动四足机械臂两类平台。没有进入最终精选，主要因为它目前更像一个面向动态抓取的延迟补偿专用方案，方法外延和理论解释力还不如 SV-VLA 与 Compression Gap 那么强。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. FSUNav: A Cerebrum-Cerebellum Architecture for Fast, Safe, and Universal Zero-Shot Goal-Oriented Navigation [[HTML]](https://arxiv.org/html/2604.03139) [[PDF]](https://arxiv.org/pdf/2604.03139)
* **Paper ID**: `2604.03139`
* **Authors**: Mingao Tan, Yiyang Li, Shanze Wang, Xinming Zhang, Wei Zhang
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇有入围价值，因为它把 VLM 高层语义与 DRL 低层局部规划解耦成 cerebrum-cerebellum 架构，目标直指零样本导航中的实时性、安全性和跨平台兼容。其“高层多模态意图 + 低层通用局部规划”的结构在 embodied navigation 里是合理且有工程吸引力的。未进最终精选，是因为它更偏导航系统整合，和今天聚焦的 VLA manipulation、world model、sim2real 主线不完全同轴。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W5]. UniCon: A Unified System for Efficient Robot Learning Transfers [[VIP]] [[HTML]](https://arxiv.org/html/2601.14617) [[PDF]](https://arxiv.org/pdf/2601.14617)
* **Paper ID**: `2601.14617`
* **Authors**: Yunfeng Lin, Li Xu, Yong Yu, Jiangmiao Pang, Weinan Zhang
* **Author Priority**: Core VIP
* **为什么还值得留意**: UniCon 被放入 watchlist，主要因为它代表了一条容易被低估但很重要的系统层路线：跨机器人部署真正卡住的常常不是算法本身，而是状态接口、控制流和中间件效率。Jiangmiao Pang 的出现也让它具备额外跟踪价值。没有进入最终精选，是因为这篇更像统一部署基础设施论文，虽然和 transfer 高度相关，但它解决的是“最后一公里系统集成”，而不是今天最核心的 VLA / 世界模型研究问题。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
