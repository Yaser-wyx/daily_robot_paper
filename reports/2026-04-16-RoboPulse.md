# RoboPulse | 2026-04-16

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 68 papers scanned · 10 shortlisted · 6 editor's picks

今天这组最终精选很集中地指向一个主线：机器人系统正在从“把视觉、语言、动作端到端塞进一个大模型”转向更可解释的中间结构，包括共训机制、层级接口、像素化动作表示，以及面向规划能力的专门评测。入选论文之所以强，是因为它们不只报性能，而是在回答几个更关键的问题：Sim2Real 为什么有时有效、VLM 推理能力怎样不被控制微调破坏、世界模型到底能不能真的用于决策，以及 RL 如何借 VLA 先验补探索和信用分配短板。今天还出现了一个很清楚的趋势：动态环境与长时程任务正在逼着 VLA 从单帧反应式策略升级为具备历史、计划和恢复能力的系统。按作者线看，Yuke Zhu 和 Jiangmiao Pang 最值得优先跟踪，前者代表 co-training 机制分析，后者代表层级 VLA 系统化落地。

## 今日信号

- VLA 正从紧耦合端到端范式转向显式分层，把语义规划、视觉 grounding 和低层控制拆开，以保住底座 VLM 的推理能力。
- 世界模型路线开始重新定义动作表示与评测对象，不再满足于“视频生成得像”，而是追问动作是否像素对齐、轨迹是否可恢复、规划是否可量化。
- Sim2Real 与 RL 融合阶段的关键瓶颈正在从“多喂数据/强蒸馏”转向“如何控制域对齐强度、数据配比以及教师信号介入时机”。

## Editor's Picks

### [1]. A Mechanistic Analysis of Sim-and-Real Co-Training in Generative Robot Policies [[VIP]] [[HTML]](https://arxiv.org/html/2604.13645) [[PDF]](https://arxiv.org/pdf/2604.13645) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.13645`
* **Authors**: Yu Lei, Minghuan Liu, Abhiram Maddukuri, Zhenyu Jiang, Yuke Zhu
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，它把 sim-real 共训从经验技巧拉回到可分析的表示学习问题。
* **问题与切口**: 这篇工作不是再提一个更强策略，而是追问生成式机器人策略里最常见的 sim-and-real co-training 何时有效、为何有效。作者把问题切到“表示该多像、又该保留多少域差异”这一核心矛盾上，试图解释为什么同样的混合训练在有些任务上能显著迁移，在另一些设定下却会伤害真实域适应。相对已有主要报性能的路线，它的价值在于给出机制化分析框架。
* **核心方法与证据**: 从摘录看，论文结合理论分析与经验实验，围绕数据混合比例、表示对齐强度和域信息保留展开。实验部分至少做了 visual-physics 的 sim-and-sim 共训，并区分 balanced 与 unbalanced mixing；当两域样本更均衡时，OT、ADDA 这类偏对齐方法稳定受益，而在单域占优时会明显退化；显式保留域信息的 CFG 更稳，但峰值不一定最高。这些证据支持“对齐不是越强越好”的主张。
* **正文要点**:
  - 作者把共训收益归因于内在机制，而非把数据混合率当作纯经验超参。
  - 平衡混合下，对齐导向方法在多个任务上更稳定地促进跨域迁移。
  - 非平衡混合下，强对齐会伤害适应，说明域可辨性不能被完全抹平。
* **为什么值得跟**:
  - 它为 Sim2Real 中最常见的“多加模拟数据是否一定更好”提供了更可操作的判断框架。
  - 对生成式机器人策略而言，表示层面的诊断比单纯堆数据更接近可迁移性瓶颈。
  - 这类机制分析有机会指导后续 co-training、cross-embodiment 和数据配比设计。
* **风险 / 保留意见**:
  - 当前摘录主要展示 sim-and-sim 与若干任务现象，真实机器人外推力度还需要看完整正文。
  - 摘要提到两种内在效应，但当前 HTML 摘录对第二种效应证据不足，结论边界要保守。
* **建议先看**: 先看作者如何定义“structured representation alignment”与域可辨性的张力，再看 balanced / unbalanced mixing 下 OT、ADDA、CFG 的对照结果。若这条主线成立，这篇的价值主要在解释力而不是单点 SOTA。
* **关键词**: `Sim2Real` `co-training` `representation alignment` `domain gap` `generative robot policy`
* **证据来源**: arXiv HTML (Introduction, Experiments)
* **读 PDF 先核查**:
  - 作者提出的第二个内在效应具体是什么，它与 structured representation alignment 如何交互？
  - balanced 与 unbalanced mixing 的分界是经验设定还是可由理论量化预测？
  - CFG 保留域信息为何更稳，它保留的是语义域标识还是更一般的统计差异？
* **上传 PDF 后优先看**:
  - 理论分析章节：内在效应定义、假设与可检验推论
  - 消融实验章节：混合比例、对齐方法与域信息保留的交互
  - 真实或跨域泛化实验章节：sim-and-sim 之外是否还能成立

### [2]. HiVLA: A Visual-Grounded-Centric Hierarchical Embodied Manipulation System [[VIP]] [[HTML]](https://arxiv.org/html/2604.14125) [[PDF]](https://arxiv.org/pdf/2604.14125) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.14125`
* **Authors**: Tianshuo Yang, Guanyu Chen, Yutian Chen, Zhixuan Liang, Yitian Liu, Zanxin Chen, Chunpu Xu, Haotian Liang, Jiangmiao Pang, Yao Mu, Ping Luo
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，它代表了把 VLM 推理能力和操作控制显式拆开的清晰系统路线。
* **问题与切口**: HiVLA 瞄准当前端到端 VLA 的核心矛盾：一旦用窄控制数据微调，底座 VLM 的语义推理与泛化往往被侵蚀。它通过层级化设计把“想什么、看哪里、怎么动”拆开：高层 VLM 负责任务分解与视觉 grounding，低层 DiT Action Expert 专注执行。相较把 reasoning 和 control 紧耦合的路线，这种 visual-grounded-centric 方案更像是在保住 VLM 能力前提下做机器人落地。
* **核心方法与证据**: 从方法摘录看，高层 planner 在每一步都结合总体目标、夹爪状态、上一步子任务以及动作前后视觉历史，输出结构化计划，包括子任务指令和目标框。低层则是 DiT-based Action Expert，研究重点放在如何注入高层视觉引导。实验覆盖 RoboTwin2.0 与真实机器人，并明确考察三件事：是否优于耦合式 VLA、对高层推理错误是否鲁棒、以及不同视觉表征与 guidance injection 策略的影响。
* **正文要点**:
  - 高层输出不是自由文本，而是“子任务 + 目标框”的结构化计划。
  - planner 显式使用动作前后视觉历史与夹爪状态，而不是只看当前帧。
  - 实验设计把 planner 错误鲁棒性和 guidance 注入方式单独拿出来检验。
* **为什么值得跟**:
  - 它把 VLA 中最关键的能力冲突显式拆分，便于单独优化 reasoning 与 control。
  - 视觉 grounding 被提升为中间接口，有助于让高层决策更可诊断。
  - 如果真实机结果稳，这会是一条比端到端耦合更工程化的通用操作路线。
* **风险 / 保留意见**:
  - 层级接口质量高度依赖高层目标框与子任务分解，误差可能沿链路放大。
  - 当前摘录没有给出真实机覆盖范围与失败模式细节，泛化强度仍需核查。
* **建议先看**: 先盯住 planner 的输入输出接口，再看 DiT Action Expert 如何接收视觉引导；如果接口设计站得住，后面的鲁棒性实验就是决定它是否真优于端到端 VLA 的关键。
* **关键词**: `hierarchical VLA` `visual grounding` `VLM planner` `DiT action expert` `embodied manipulation`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)
* **读 PDF 先核查**:
  - 目标框是如何编码进低层控制器的，属于条件 token、空间 mask 还是别的注入形式？
  - 当高层 planner 子任务分解出错时，低层执行器是否仍能局部纠偏，还是只能机械跟随？
  - 动作前后视觉历史相较单帧输入究竟提升了什么，是状态估计、因果判断还是错误恢复？
* **上传 PDF 后优先看**:
  - 方法章节：planner 的结构化输出与视觉 grounding 机制
  - 消融章节：视觉表征与 guidance injection 策略
  - 鲁棒性/真实机章节：高层错误传播与恢复表现

### [3]. Action Images: End-to-End Policy Learning via Multiview Video Generation [[HTML]](https://arxiv.org/html/2604.06168) [[PDF]](https://arxiv.org/pdf/2604.06168) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.06168`
* **Authors**: Haoyu Zhen, Zixian Gao, Qiao Sun, Yilin Zhao, Yuncong Yang, Yilun Du, Pengsheng Guo, Tsun-Hsuan Wang, Yi-Ling Qiao, Chuang Gan
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把 world action model 的动作表示真正拉回了视频空间。
* **问题与切口**: 这篇工作的核心切口很明确：世界模型之所以会“视频会生成、策略却不会泛化”，一个关键原因是动作仍被当成与视觉割裂的低维控制信号。Action Images 反其道而行，把 7-DoF 动作翻译成可解释的多视角 action images / videos，让观测与动作处于同一视频模态中。相对外挂 policy head 或抽象 action token 的路线，它更彻底地复用了视频骨干的预训练知识。
* **核心方法与证据**: 作者先定义从连续 7-DoF 控制到多视角动作视频的变换，再证明这类像素化动作可被解码回连续控制且信息损失较小，随后训练统一的 world-action model 联合生成未来机器人视频与动作视频。实验主设定是文本控制、multi-view、one-trial open-loop，这一点很关键，因为它基本排除了在线重规划补救，把结果直接归因到动作表示与生成模型本身。对比对象包含多视角 policy、VLA 与其他 world-model 路线。
* **正文要点**:
  - 动作不再是额外 head 的输出，而是与观测同模态的多视角视频对象。
  - 方法强调 action image 可逆解码回连续控制，避免只生成“好看但不可执行”的视频。
  - 核心评测采用单次前向 open-loop 设定，直接检验表示本身的泛化质量。
* **为什么值得跟**:
  - 它让 world model 与 policy model 的边界更模糊，可能减少“预测强、控制弱”的结构性断层。
  - 像素对齐动作表示天然更适合跨视角迁移，这是多相机机器人系统很需要的。
  - 如果这条路成立，未来动作建模可能更多依赖通用视频模型而非专门控制 head。
* **风险 / 保留意见**:
  - open-loop 结果再强也不能替代闭环控制验证，真实部署鲁棒性仍有不确定性。
  - action image 的解码误差虽被描述为较小，但具体失真边界与失败情形需看完整正文。
* **建议先看**: 先看 7-DoF 到 action images 的编码/解码是否足够自然，再看 open-loop 对比实验是否真的把优势归因到动作表示，而不是训练规模或骨干差异。
* **关键词**: `world action model` `action images` `multiview video generation` `pixel-grounded action` `zero-shot policy`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - action images 对末端位姿、旋转和夹爪状态分别如何编码，哪些分量最容易丢失信息？
  - 多视角动作视频带来的提升主要来自几何一致性，还是来自更强的视觉预训练迁移？
  - 当任务需要闭环纠错时，这个 unified video-space policy 是否还能保持优势？
* **上传 PDF 后优先看**:
  - 方法章节：动作图像化编码与连续控制解码
  - 主实验章节：multi-view open-loop 对比与泛化设定
  - 分析章节：zero-shot policy 成立条件与失败案例

### [4]. Jump-Start Reinforcement Learning with Vision-Language-Action Regularization [[HTML]](https://arxiv.org/html/2604.13733) [[PDF]](https://arxiv.org/pdf/2604.13733) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.13733`
* **Authors**: Angelo Moroncelli, Roberto Zanetti, Marco Maccarini, Loris Roveda
* **Author Priority**: Standard
* **一句话结论**: 值得看，它不是把 VLA 当替代 RL 的大模型，而是把它降格成更实用的探索与信用分配辅助器。
* **问题与切口**: VLAJS 试图解决一个很现实的问题：RL 在长时程操作和奖励设计不理想时，往往不是控制能力不够，而是探索太慢、信用分配太弱；与此同时，VLA 虽有高层语义先验，却不适合直接承担高频闭环控制。论文的切口就是把两者拆开协作，用稀疏 VLA 指导去“跳启动”RL，而不是做重蒸馏或全程教师跟随。这比直接拿 VLA 下场控机器人更务实，也更接近工程可落地。
* **核心方法与证据**: 从摘录看，作者围绕两类坏场景验证方法：一类是长时程任务导致的延迟回报，另一类是奖励本身稀疏或塑形欠佳。实验中明确比较 PPO、Sparse RPD、VLAJS(RPD) 和完整版 VLAJS，并用成功率与成功曲线 AUC 衡量样本效率。结论部分还强调“教师信号何时用、如何用”和“教师本身强不强”同样重要，并声称支持零样本真实机器人部署；不过具体正则项、方向性损失形式仍需看正文细节。
* **正文要点**:
  - 论文把 VLA 指导限定为稀疏、辅助性的教师信号，而非连续蒸馏。
  - 实验刻意挑选长时程与次优奖励两类信用分配难题来压测方法。
  - 作者强调 transient guidance 与 directional loss，可见其关注降低教师查询依赖。
* **为什么值得跟**:
  - 这条路线保留了 RL 的高频闭环优势，同时借用 VLA 的语义先验改善探索。
  - 相较重度蒸馏，它更有机会控制计算成本和教师调用成本。
  - 如果真实机零样本部署属实，说明高层 VLA 先验能以更轻量的方式进入操作控制。
* **风险 / 保留意见**:
  - 当前 HTML 摘录没有完整展开 RPD 与 directional loss 的数学定义，复现门槛暂时不低。
  - 真实机器人结果只在结论中被提及，覆盖任务范围与稳定性还需要核查。
* **建议先看**: 先看 VLA 教师信号究竟以什么形式进入 on-policy RL，再看两类 use case 的差异化收益；这能判断它是普适框架，还是只对特定信用分配问题有效。
* **关键词**: `reinforcement learning` `VLA regularization` `exploration` `credit assignment` `robot manipulation`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
* **读 PDF 先核查**:
  - RPD 与完整版 VLAJS 的差别究竟是什么，额外正则项是否只在奖励差的场景下才必要？
  - transient guidance 终止后，策略性能能否维持，还是仍对后续教师信号敏感？
  - VLA 提供的是动作方向、子目标偏好还是价值形状，这三者对 PPO 的影响是否可分离？
* **上传 PDF 后优先看**:
  - 方法章节：VLA 指导信号与正则项定义
  - 主实验章节：长时程任务 vs 次优奖励任务的对比
  - 真实机章节：零样本部署协议与失败案例

### [5]. Towards Generalizable Robotic Manipulation in Dynamic Environments [[PDF]](https://arxiv.org/pdf/2603.15620) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.15620`
* **Authors**: Heng Fang, Shangru Li, Shuhan Wang, Xuanyang Xi, Dingkang Liang, Xiang Bai
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为它直接把 VLA 从静态操作推向动态环境，并先补齐了数据与评测缺口。
* **问题与切口**: 这篇工作抓住了当前 VLA 的一个明显短板：面对移动目标和持续变化场景，单帧观测驱动的静态操作策略很难稳定工作。作者先提出 DOMINO 数据集与基准，把动态操作问题系统化，覆盖 35 个分层任务和大规模专家轨迹；再基于这一缺口提出 dynamics-aware 的 PUMA。相较只在静态桌面任务上做泛化，这篇更像是在把“时序感知”拉成下一阶段 VLA 能力门槛。
* **核心方法与证据**: 由于目前只有摘要回退信息，可确认的证据主要有三层：第一，DOMINO 同时是数据集也是 benchmark，且作者用它系统评估现有 VLA 在动态任务上的失效；第二，论文不仅比较模型，还专门探索动态感知相关训练策略；第三，PUMA 至少明确引入了 scene-centric historical optical flow，说明方法核心在把显式时序运动线索注入 VLA。至于具体架构、损失和评测协议，现阶段只能保守等待 PDF。
* **正文要点**:
  - 论文把动态操作失败归因于数据稀缺与单帧观测范式两方面。
  - DOMINO 同时提供任务分层复杂度与多维评测，不只是多收一些动态数据。
  - PUMA 明确引入以场景为中心的历史光流，强调显式时序线索。
* **为什么值得跟**:
  - 动态环境是 VLA 真正走向现实应用前必须跨过的门槛，这篇正面切中痛点。
  - 先做 benchmark 再推新模型，使后续研究更容易在同一动态设定下比较。
  - 如果动态数据对静态外泛化也有益，它会影响未来机器人数据收集优先级。
* **风险 / 保留意见**:
  - 当前仅有摘要，PUMA 的具体设计与证据强度还不足以做更细判断。
  - 大规模数据集提升可能部分来自规模效应，动态建模本身贡献需要靠消融确认。
* **建议先看**: 这篇先别急着看模型细节，优先核对 DOMINO 的任务设计与评测维度是否真覆盖动态操作难点；若 benchmark 立得住，再判断 PUMA 的时序建模是不是必要增益。
* **关键词**: `dynamic manipulation` `VLA` `benchmark` `dataset` `optical flow`
* **证据来源**: Abstract fallback
* **读 PDF 先核查**:
  - DOMINO 的动态难度分层具体如何定义，是否能区分感知难、规划难和控制难？
  - PUMA 中历史光流如何与语言和视觉主干融合，属于前端增强还是中层交互？
  - 动态数据带来的收益主要体现在同域动态任务，还是也能迁移到静态或跨环境任务？
* **上传 PDF 后优先看**:
  - 数据集/benchmark 章节：任务分层与评测协议
  - 方法章节：PUMA 的时序感知设计与光流融合
  - 消融章节：动态数据、历史信息与训练策略各自贡献

### [6]. Target-Bench: Can Video World Models Achieve Mapless Path Planning with Semantic Targets? [[HTML]](https://arxiv.org/html/2511.17792) [[PDF]](https://arxiv.org/pdf/2511.17792) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2511.17792`
* **Authors**: Dingrui Wang, Zhihao Liang, Hongyuan Ye, Zhexiao Sun, Zhaowei Lu, Yuchen Zhang, Yuyu Zhao, Yuan Gao, Marvin Seegert, Finn Schäfer, Haotong Qin, Wei Li, Luigi Palmieri, Felix Jahncke, Mattia Piccinini, Johannes Betz
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把“视频世界模型会不会规划”第一次拆成可测的 benchmark 问题。
* **问题与切口**: Target-Bench 要解决的不是生成视频是否逼真，而是视频世界模型面对语义目标时，能不能在无地图条件下形成有用的路径规划倾向。论文把这个问题做成系统 benchmark：450 个机器人采集场景、47 类语义目标，并用 SLAM 轨迹作为运动倾向参考，再从生成视频里恢复轨迹进行评测。相较只报视觉质量或主观案例，这篇真正把世界模型的语义理解、空间估计和规划能力绑定到统一测试上。
* **核心方法与证据**: 方法上，它先用 world-decoder 从生成视频重建相机轨迹，摘录中明确列出 VGGT、SpaTracker、ViPE 三种 3D 重建工具；再用一组偏“tendency-based”而非唯一真值路径的指标打分，其中 AC 指标允许围绕参考轨迹的进度相关走廊，从而承认多条可行路径。实验结论非常克制：现成最强视频 WM 仍只有较低总体分数，但定性上往往能识别目标并给出合理运动趋势，这恰好说明“看懂了”和“真能规划”之间还有显著落差。
* **正文要点**:
  - benchmark 明确同时考 semantic reasoning、spatio-temporal consistency 和 planning。
  - 评测不是直接拿生成视频做主观判断，而是先重建轨迹再量化路径倾向。
  - AC 等指标刻意允许多解，避免把规划评估退化成单一路径拟合。
* **为什么值得跟**:
  - 它把世界模型从“会生成”推进到“能不能用于决策”的关键一步。
  - 对机器人/自动驾驶类生成模型而言，路径倾向比像素逼真度更接近真实价值。
  - 这类 benchmark 能迫使后续 WM 论文回答规划能力，而不再只展示 demo。
* **风险 / 保留意见**:
  - 轨迹恢复链路依赖外部 3D 重建器，评测上限与误差会受解码器质量影响。
  - 低分究竟来自世界模型语义失败还是几何恢复失败，可能需要更细拆解。
* **建议先看**: 优先看 benchmark 任务构成与 world-decoder 评测链路，因为这决定了分数到底在测谁；再看 tendency-based 指标设计，判断它是否足够公平地反映规划能力。
* **关键词**: `world model` `benchmark` `path planning` `semantic targets` `trajectory reconstruction`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - world-decoder 的误差会在多大程度上掩盖或放大世界模型本身的规划能力？
  - implicit semantic targets 为什么特别难，它更考语义理解还是长程时空一致性？
  - 如果模型只学到目标方向而非可执行路径，现有指标能否把两者区分开？
* **上传 PDF 后优先看**:
  - benchmark 章节：场景、目标类别与任务定义
  - 方法章节：world-decoder 与轨迹恢复流程
  - 指标章节：tendency-based 评分设计与误差分析

## Watchlist

### [W1]. RoboLab: A High-Fidelity Simulation Benchmark for Analysis of Task Generalist Policies [[PDF]](https://arxiv.org/pdf/2604.09860)
* **Paper ID**: `2604.09860`
* **Authors**: Xuning Yang, Rishit Dagli, Alex Zook, Hugo Hadfield, Ankit Goyal, Stan Birchfield, Fabio Ramos, Jonathan Tremblay
* **Author Priority**: Standard
* **为什么还值得留意**: 进入 shortlist，因为它直指通用策略在仿真评测中的饱和与伪泛化问题，且强调用受控扰动去分析真实策略行为，这对 Sim2Real 和 generalist policy 评估都很重要。没有进最终精选，主要因为当前只有摘要回退，方法链路与 benchmark 设计细节不足；同时它更偏评测基础设施，今天主线里机制解释、策略建模和世界模型能力拆解的信号更强。
* **证据来源**: Abstract fallback

### [W2]. HAMLET: Switch your Vision-Language-Action Model into a History-Aware Policy [[HTML]](https://arxiv.org/html/2510.00695) [[PDF]](https://arxiv.org/pdf/2510.00695)
* **Paper ID**: `2510.00695`
* **Authors**: Myungkyu Koo, Daewon Choi, Taeyoung Kim, Kyungmin Lee, Changyeon Kim, Younggyo Seo, Jinwoo Shin
* **Author Priority**: Standard
* **为什么还值得留意**: 进入 shortlist，因为它抓住了 VLA 单帧假设的真实短板，并用 moment tokens 加轻量记忆模块把历史信息接进现有 VLAs，方向上很对。没进最终精选，是因为相较 HiVLA、DOMINO 或 Goal2Skill，它更像对既有 VLA 的可扩展增强，而不是重新定义任务接口或评测范式；从摘录看，主增益也更集中在 history-dependent 任务。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. IGen: Scalable Data Generation for Robot Learning from Open-World Images [[VIP]] [[HTML]](https://arxiv.org/html/2512.01773) [[PDF]](https://arxiv.org/pdf/2512.01773)
* **Paper ID**: `2512.01773`
* **Authors**: Chenghao Gu, Haolan Kang, Junchao Lin, Jinghe Wang, Duo Wu, Shuzhao Xie, Fanding Huang, Junchen Ge, Ziyang Gong, Letian Li, Hongying Zheng, Changwei Lv, Zhi Wang
* **Author Priority**: Core VIP
* **为什么还值得留意**: 进入 shortlist，因为它试图把开放世界图像直接转成机器人训练数据，若成立会显著改变数据供给方式，且实验问题设置覆盖场景重建、动作生成与直接训练部署，野心很大。没有进最终精选，原因是它更偏数据生成管线，和今天以 VLA、世界模型、Sim2Real 机制为核心的主线相比稍弱一层；此外当前摘录虽提到视觉指标与无人工示教训练，但策略收益究竟来自视觉逼真度、动作对齐还是任务偏置，还需要更细证据。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

### [W4]. Goal2Skill: Long-Horizon Manipulation with Adaptive Planning and Reflection [[HTML]](https://arxiv.org/html/2604.13942) [[PDF]](https://arxiv.org/pdf/2604.13942)
* **Paper ID**: `2604.13942`
* **Authors**: Zhen Liu, Xinyu Ning, Zhe Hu, Xinxin Xie, Weize Li, Zhipeng Tang, Chongyu Wang, Zejun Yang, Hanlin Wang, Yitong Liu, Zhongzhu Pu
* **Author Priority**: Standard
* **为什么还值得留意**: 进入 shortlist，因为它把长时程操作拆成规划、执行、验证与反思闭环，和当前双系统 VLA 趋势一致，也明确瞄准 memory-dependent manipulation。没有进最终精选，主要因为今天已经有 HiVLA 和 VLAJS 分别覆盖“层级系统设计”和“长时程信用分配”两条更强主线；相比之下，Goal2Skill 在现有摘录里更像成熟工程整合，方法新意与证据边界还需要 PDF 进一步确认。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
