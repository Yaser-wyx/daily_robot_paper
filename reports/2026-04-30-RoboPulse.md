# RoboPulse | 2026-04-30

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 54 papers scanned · 10 shortlisted · 5 editor's picks

今天的主线非常清晰：VLA 与 world model 正在从“看未来”走向“为动作服务的空间化未来建模”，同时实时执行与跨场景数据扩展也开始成为同等重要的系统问题。最终精选里的五篇论文分别覆盖了 4D world action model、动作中心时空建模、实时流式 VLA、医疗机器人基础数据集，以及 real-to-real 3D 数据生成，组合起来刚好构成从模型、系统到数据的完整技术链。若按长期跟踪价值排序，VIP 作者名单里最值得优先看的仍是 Chelsea Finn 参与的 Open-H-Embodiment，因为它更像是医疗机器人 foundation model 的数据底座。其余几篇虽然没有核心 VIP 作者加持，但在 WAM、实时 VLA 和 Sim2Real 数据生成上都给出了很鲜明的新切口，值得持续追踪后续版本。

## 今日信号

- 今天最值得记住的研究信号是：World Action Model 正从 2D 像素预测升级到带深度、几何和多视角约束的 4D 空间化建模，而且目标越来越明确地服务于动作生成。
- 今天最值得记住的研究信号是：实时 VLA 的瓶颈已经不只在模型精度，采样时间表、TTFA 和流式推理接口正在变成决定真实部署可用性的核心变量。
- 今天最值得记住的研究信号是：数据侧创新重新变成主战场，无论是跨 embodiment 医疗数据集还是 real-to-real 3D 增广，大家都在试图绕开纯仿真路线的迁移损耗。

## Editor's Picks

### [1]. Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising [[HTML]](https://arxiv.org/html/2604.26694) [[PDF]](https://arxiv.org/pdf/2604.26694) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.26694`
* **Authors**: Jun Guo, Qiwei Li, Peiyan Li, Zilong Chen, Nan Sun, Yifei Su, Heyun Wang, Yuan Zhang, Xinghang Li, Huaping Liu
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把实时动作执行与高保真 4D 世界建模真正放进同一框架，而不是把视频预测当成动作模型的附属品。
* **问题与切口**: 这篇工作要解决的是统一 world model 常见的两难：一类方法擅长动作执行，但对空间结构和物理展开理解不足；另一类方法能生成未来画面，却难兼顾控制效率。X-WAM 的切口是把统一建模从 2D 像素空间推进到 4D 世界层面，用多视角 RGB-D 视频来“想象”未来，再同时输出动作与状态，从而把高保真世界建模和可执行控制放进同一套表示里。相对已有统一框架，它的新意不在简单堆更多模态，而在强调空间感知与动作效率并存。
* **核心方法与证据**: 从 HTML 摘录可确认，X-WAM 基于预训练视频扩散 Transformer 微调，输入语言指令、初始本体状态和多视角初始 RGB 观测，联合预测未来 RGB、深度、状态和动作。方法上最关键的两点是：用复制末端 DiT block 的轻量深度分支做结构适配，以及用异步噪声采样去对齐训练与推理时不同模态、不同时域的需求。证据链覆盖三部分：策略执行、4D 重建与生成、以及同时分析两类目标的消融，说明作者试图证明这不是单点优化。
* **正文要点**:
  - 正文明确把预测目标拆成未来视频/状态与未来动作两个不对称时间范围，说明模型设计首先服务于控制场景。
  - 深度不是额外拉长序列去建模，而是通过复制末端少量 DiT 模块形成交错深度分支，重点在保留视频先验。
  - 实验被分成策略评测、4D 重建生成和联合消融三条线，体现作者把“能行动”和“能建模世界”视作同等目标。
* **为什么值得跟**:
  - 它代表统一 VLA/WAM 路线开始真正吸收 3D 与深度信息，而不再停留在 2D 视频未来预测。
  - 如果这条路线成立，未来机器人策略评估可以同时利用动作成功率与空间重建质量两种信号。
  - 它对需要多视角、空间一致性和长时序物理展开的操作任务尤其有启发性。
* **风险 / 保留意见**:
  - HTML 摘录没有给出关键定量结果细节，因此目前更能确认方向完整性，难以判断各子任务上的绝对优势幅度。
  - 深度由生成的 RGB 序列恢复并配合轻量分支建模，这种耦合是否会在真实复杂场景中放大误差，还需要看 PDF 中的失败案例与消融。
* **建议先看**: 先抓方法主线：看它如何把预训练视频扩散模型改造成同时服务动作与 4D 建模的统一去噪器。再看实验是否真的证明两种目标没有彼此拖累，尤其是联合消融部分。
* **关键词**: `World Action Model` `4D world model` `video diffusion` `RGB-D` `asynchronous denoising`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 异步噪声采样究竟如何缓解动作时域与视频时域不对称带来的训练推理失配？
  - 轻量深度分支在保留视频先验与引入空间结构之间的权衡点在哪里？
  - 4D 重建质量的提升是否真正转化成了闭环策略执行上的稳健收益？
* **上传 PDF 后优先看**:
  - 方法章节里统一去噪序列与深度分支的结构设计
  - 策略执行评测章节，尤其是与 VLA/WAM 基线的对比逻辑
  - 联合消融章节，重点看动作性能与世界建模质量是否同步变化

### [2]. STARRY: Spatial-Temporal Action-Centric World Modeling for Robotic Manipulation [[HTML]](https://arxiv.org/html/2604.26848) [[PDF]](https://arxiv.org/pdf/2604.26848) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.26848`
* **Authors**: Yuxuan Tian, Yurun Jin, Bin Yu, Yukun Shi, Hao Wu, Chi Harold Liu, Kai Chen, Cong Huang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它比一般 world-model-enhanced policy 更进一步，真正把几何预测变成动作注意力里的显式调制信号。
* **问题与切口**: STARRY 关注的不是“先预测未来，再顺带帮动作”，而是动作中心的时空世界建模：未来表示必须对动作生成有选择性地起作用。作者认为现有 VLA 或带 world model 的策略虽然会预测未来，但对物体几何、接触区域和末端执行器轨迹之间的局部时空关系建模不够，导致语言条件操作里容易在挂、放、递交等任务上失稳。它的新意就在于把未来空间几何直接接进动作分支，而不是只做共享潜变量。
* **核心方法与证据**: 方法上，STARRY 联合去噪未来时空 latent 与动作序列，再通过 GASAM 把预测深度与末端执行器几何转换成 token 对齐的权重，对动作注意力做选择性调制。证据链比较完整：在 RoboTwin 2.0 的 Clean 和 Randomized 设置做大规模仿真评测，在真实环境做物理执行验证，并通过消融单独分析时空预测与 GASAM 的贡献。HTML 摘录还给出主结果，平均成功率在两种设置下都领先，真实实验平均成功率也有明显提升。
* **正文要点**:
  - 作者明确批评现有方法缺少对 action-relevant region 的选择性强调，这决定了整篇论文是“动作中心”而不是“世界中心”。
  - RoboTwin 2.0 评测把 50 个任务的数据池化联合优化，而不是逐任务训练，更接近通用操作策略设定。
  - GASAM 的作用不是简单拼接几何特征，而是把预测深度和末端执行器几何转成对齐到 token 的注意力权重。
* **为什么值得跟**:
  - 它把“世界模型如何服务动作”这件事具体化成可操作的注意力调制机制。
  - 如果几何选择性调制有效，未来 VLA 可以更自然地处理接触敏感、局部关系主导的精细操作任务。
  - 它同时报告仿真和真实执行结果，说明这条路线不是只在离线生成指标上成立。
* **风险 / 保留意见**:
  - 真实世界提升显著，但 HTML 摘录没有展开任务组成和失败分布，暂时还无法判断收益主要来自哪些任务类型。
  - 几何调制依赖预测深度和末端几何，如果前端预测误差较大，注意力可能被错误放大，这需要看 PDF 中的误差传播分析。
* **建议先看**: 优先看 GASAM 这条主线，判断它到底是新瓶装旧酒的特征融合，还是确实改变了动作生成时的关注机制。然后再看消融是否能把“联合预测”和“几何调制”的贡献拆干净。
* **关键词**: `VLA` `world-model-enhanced policy` `spatial-temporal modeling` `geometry-aware attention` `robot manipulation`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - GASAM 相比直接拼接深度或几何 token，到底提供了什么额外的动作生成优势？
  - 联合去噪未来时空 latent 与动作序列时，二者是互相促进还是存在训练竞争？
  - 在 50 任务联合训练设定下，提升主要来自空间关系复杂任务还是普遍存在于所有任务？
* **上传 PDF 后优先看**:
  - 方法章节中 GASAM 的输入、对齐方式与插入位置
  - 仿真评测章节里 Clean/Randomized 两种设置下的总体与分类结果
  - 消融章节里时空预测模块与几何调制模块的独立贡献

### [3]. FASTER: Rethinking Real-Time Flow VLAs [[HTML]](https://arxiv.org/html/2603.19199) [[PDF]](https://arxiv.org/pdf/2603.19199) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.19199`
* **Authors**: Yuxiang Lu, Zhe Liu, Xianzhe Fan, Zhenya Yang, Jinghua Hou, Junyi Li, Kaixin Ding, Hengshuang Zhao
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它不是再做一个更大的 VLA，而是抓住真实部署里最容易被忽视的反应延迟问题，给出可插拔的系统级改法。
* **问题与切口**: FASTER 针对的是 flow-based VLA 在真实执行中一个很现实的痛点：异步推理通常只改善动作块之间的平滑性，却未真正优化机器人对环境变化的反应时间。论文的核心判断是，反应能力不能只看吞吐或轨迹连续性，而应重新分析 TTFA 与执行时域共同决定的反应分布。相对已有实时 VLA 路线，它的新意是把“实时性”从工程直觉提升为可分析、可设计的采样与系统问题。
* **核心方法与证据**: 从摘录可确认，作者先分析反应时间的形成机制，指出标准常数时间表会拖慢 flow VLA 对即时动作的采样；随后提出 Horizon-Aware Schedule，使当前最需要执行的动作可以更快生成，并结合 streaming client-server 接口与 early stopping 同时降低 TTFA 和闭环控制延迟。证据主要来自两类硬件平台、两种代表性 flow VLA，以及真实机器人实验；文中还特别提到在消费级 RTX 4060 上对某基线可获得约 3 倍 TTFA 提升。
* **正文要点**:
  - 作者把反应时间写成由 TTFA 与执行 horizon 共同决定的分布问题，而不是单一延迟指标。
  - 论文指出 flow VLA 里常见的 constant timestep schedule 是实时反应的关键瓶颈。
  - 方法是插拔式的：既改采样日程，也改推理接口，因此目标是兼容现有 flow-based VLA。
* **为什么值得跟**:
  - 它提醒研究社区，真实世界部署里“多久开始反应”往往和“轨迹好不好看”同样重要。
  - 对边缘设备友好的改法比单纯追求更大模型更容易落地到机器人系统。
  - 这类方法一旦通用，可能成为未来流式 VLA 部署的默认系统设计。
* **风险 / 保留意见**:
  - HTML 摘录没有完整给出不同任务上的成功率与稳定性细节，因此目前更能确认延迟收益，较难确认任务层面的全面收益。
  - 如果 immediate action 被过度优先，是否会伤害长 horizon 轨迹质量，需要重点核查 PDF 中的质量与速度权衡实验。
* **建议先看**: 先看作者如何定义并推导 reaction time，这决定了整篇论文是否只是工程加速，还是对 action chunking 的问题重述。再看 Horizon-Aware Schedule 是否真的做到更快而不明显伤害后续动作质量。
* **关键词**: `real-time VLA` `flow matching` `reaction time` `TTFA` `streaming inference`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 作者给出的反应时间分布分析，对不同执行 horizon 和不同控制频率是否都成立？
  - Horizon-Aware Schedule 为什么能优先生成即时动作而不破坏整段动作块的一致性？
  - early stopping 与流式接口带来的收益中，哪一部分更关键，是否具有硬件依赖性？
* **上传 PDF 后优先看**:
  - 反应时间分析与问题定义部分
  - 方法章节中 Horizon-Aware Schedule 与 early stopping 的配合机制
  - 真实机器人实验与不同 GPU 平台对比结果

### [4]. Open-H-Embodiment: A Large-Scale Dataset for Enabling Foundation Models in Medical Robotics [[VIP]] [[HTML]](https://arxiv.org/html/2604.21017) [[PDF]](https://arxiv.org/pdf/2604.21017) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.21017`
* **Authors**: Open-H-Embodiment Consortium: Nigel Nelson, Juo-Tung Chen, Jesse Haworth, Xinhao Chen, Lukas Zbinden, Dianye Huang, Alaa Eldin Abdelaal, Alberto Arezzo, Ayberk Acar, Farshid Alambeigi, Carlo Alberto Ammirati, Yunke Ao, Pablo David Aranda Rodriguez, Soofiyan Atar, Mattia Ballo, Noah Barnes, Federica Barontini, Filip Binkiewicz, Peter Black, Sebastian Bodenstedt, Leonardo Borgioli, Nikola Budjak, Benjamin Calmé, Fabio Carrillo, Nicola Cavalcanti, Changwei Chen, Haoxin Chen, Sihang Chen, Qihan Chen, Zhongyu Chen, Ziyang Chen, Shing Shin Cheng, Meiqing Cheng, Min Cheng, Zih-Yun Sarah Chiu, Xiangyu Chu, Camilo Correa-Gallego, Giulio Dagnino, Anton Deguet, Jacob Delgado, Jonathan C. DeLong, Kaizhong Deng, Alexander Dimitrakakis, Qingpeng Ding, Hao Ding, Giovanni Distefano, Daniel Donoho, Anqing Duan, Marco Esposito, Shane Farritor, Jad Fayad, Zahi Fayad, Mario Ferradosa, Filippo Filicori, Chelsea Finn, Philipp Fürnstahl, Jiawei Ge, Stamatia Giannarou, Xavier Giralt Ludevid, Frederic Giraud, Aditya Amit Godbole, Ken Goldberg, Antony Goldenberg, Diego Granero Marana, Xiaoqing Guo, Tamás Haidegger, Evan Hailey, Pascal Hansen, Ziyi Hao, Kush Hari, Kengo Hayashi, Jonathon Hawkins, Shelby Haworth, Ortrun Hellig, S. Duke Herrell, Zhouyang Hong, Andrew Howe, Junlei Hu, Zhaoyang Jacopo Hu, Ria Jain, Mohammad Rafiee Javazm, Howard Ji, Rui Ji, Jianmin Ji, Zhongliang Jiang, Dominic Jones, Jeffrey Jopling, Britton Jordan, Ran Ju, Michael Kam, Luoyao Kang, Fausto Kang, Siddhartha Kapuria, Peter Kazanzides, Sonika Kiehler, Ethan Kilmer, Ji Woong Kim, Przemysław Korzeniowski, Chandra Kuchi
* **Author Priority**: Core VIP
* **一句话结论**: 非常值得优先看，这篇更像医疗机器人 foundation model 时代的基础设施论文，而不只是再加一个下游策略模型。
* **问题与切口**: Open-H-Embodiment 解决的是医疗机器人领域最根本的数据瓶颈：现有数据集小、单机构、单 embodiment 且很少开放，导致 foundation model 难以形成可迁移的手术先验。论文的核心贡献不是单一算法，而是用跨机构、跨平台、跨任务的大规模视频与运动学同步数据，把医疗机器人从“小样本定制模型”推进到“可做大模型预训练/后训练”的阶段。相较常见手术机器人论文，它的价值更接近底座建设。
* **核心方法与证据**: 从 HTML 摘录可直接确认，这个数据集包含 119 个子数据集、770 小时配对视频与运动学数据、来自 49 家以上机构，覆盖 20 种机器人平台、33 类任务和 5 种环境类型。为证明数据价值，作者在 NVIDIA 预训练 GR00T-N1.6 上后训练得到 GR00T-H，并与 base model、ACT、以及用 Open-H 子集后训练的 LingBot-VA 比较；再在小规模 embodiment/task-specific 数据上微调，评估长程缝合和多种子任务表现。
* **正文要点**:
  - 这不是单一平台资源，而是跨五类结构家族的多 embodiment 医疗机器人数据集合。
  - 作者没有只停留在数据发布，而是用 GR00T-H 做了 foundation VLA 的后训练验证。
  - 结论强调规模与多样性带来的“surgical prior”可迁移性，特别是在分布外条件和有限微调数据下。
* **为什么值得跟**:
  - 它可能成为医疗机器人版的通用预训练底座，意义超过单篇模型优化。
  - Chelsea Finn 参与使其更值得持续跟踪，因为这条线天然连接通用机器人 foundation model 与高风险应用场景。
  - 如果数据质量与标注协议足够稳健，后续 VLA、WAM 乃至 surgical world model 都会直接受益。
* **风险 / 保留意见**:
  - 大规模多机构数据的异质性既是优势也是风险，采集协议、标签规范和平台差异可能显著影响可学习性。
  - HTML 摘录给出总体规模与若干结果结论，但具体任务分布、清洗标准与跨平台迁移细节仍需 PDF 验证。
* **建议先看**: 先把它当数据论文读，优先看数据构成、平台分布和环境类型，再看 GR00T-H 的验证是否真正证明“大而杂”转化成了可迁移先验。若你做医疗 VLA，这篇的价值很可能高于单一模型创新。
* **关键词**: `medical robotics` `foundation dataset` `VLA` `cross-embodiment` `GR00T-H`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - Open-H 的跨平台异质性是如何被转化为可迁移先验，而不是训练噪声的？
  - GR00T-H 的收益主要来自数据规模、任务多样性，还是 embodiment 覆盖度？
  - 与仅用 dVRK 子集后训练的 LingBot-VA 相比，差距更能说明数据广度还是模型路线的差异？
* **上传 PDF 后优先看**:
  - 数据集章节中的平台、任务与环境覆盖说明
  - GR00T-H 后训练与小样本微调实验设置
  - 分布外条件与长程缝合任务的结果分析

### [5]. R2RGEN: Real-to-Real 3D Data Generation for Spatially Generalized Manipulation [[HTML]](https://arxiv.org/html/2510.08547) [[PDF]](https://arxiv.org/pdf/2510.08547) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2510.08547`
* **Authors**: Xiuwei Xu, Angyuan Ma, Hankun Li, Bingyao Yu, Zheng Zhu, Jie Zhou, Jiwen Lu
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它瞄准的是比传统 tabletop 更难的空间泛化问题，并尝试用 real-to-real 3D 生成绕开 sim-to-real 老难题。
* **问题与切口**: R2RGEN 聚焦视觉运动策略里最基础但也最昂贵的能力之一：空间泛化。作者的判断是，移动操作场景下相机视角、底盘位置和物体布局变化更大，单靠人工示教去覆盖分布代价太高。与多数依赖仿真增广的方法不同，这篇工作直接从真实示教出发，在 3D 观测与动作轨迹层面做 real-to-real 生成，目标是在极少源示教下合成空间多样数据，用于训练更稳健的 3D visuomotor policy。
* **核心方法与证据**: 从摘录可确认，方法假设策略直接消费点云，因此选择以 egocentric point cloud 为输入、无需相机位姿的 iDP3 作为策略骨干；生成过程直接同时增广 3D 观测与动作轨迹，而不是先合成图像再反推控制。证据主要来自真实世界实验设计：作者测试 one-shot imitation learning、增加源示教后的扩展性、若干消融，并展示方法还能扩展到外观泛化与移动操作。硬件覆盖单臂移动平台与双臂平台，但 HTML 摘录未给出关键定量结果细节。
* **正文要点**:
  - 论文明确把研究场景从固定桌面机械臂扩展到移动操作，因此空间泛化压力更真实。
  - 策略骨干选 iDP3 的关键原因是直接吃相机坐标系下的点云，不依赖相机位姿或标定。
  - 作者把 real-to-real 数据生成同时施加在 3D 观测与动作轨迹上，强调观测-动作对的一致增广。
* **为什么值得跟**:
  - 这条路线如果成立，能显著降低空间泛化所需的真人示教成本。
  - 它避开纯仿真增广常见的渲染和动力学迁移误差，更贴近真实部署需求。
  - 对移动操作和多视角变化大的任务，这种 3D 数据生成比单纯 2D 图像增广更有潜力。
* **风险 / 保留意见**:
  - HTML 摘录没有给出核心定量结果，因此目前只能确认问题设定与方法框架，效果强度仍需 PDF 佐证。
  - 方法依赖点云级 3D 增广与动作同步变换，这类几何一致性一旦处理不好，容易生成对策略有害的伪样本。
* **建议先看**: 先看它如何定义并实施 real-to-real 的 3D 观测-动作联合生成，这是论文最核心的新意。然后重点核查 one-shot 设定下到底能省掉多少真实示教，以及扩展到移动操作时收益是否仍稳定。
* **关键词**: `Sim2Real` `real-to-real generation` `3D augmentation` `spatial generalization` `mobile manipulation`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)
* **读 PDF 先核查**:
  - R2RGEN 的 3D 观测与动作轨迹联合增广，如何保证几何一致性与控制可执行性？
  - 在 one-shot 设定下，提升主要来自对对象布局的泛化，还是对视角和机器人位姿变化的泛化？
  - 当源示教增加时，这种生成框架的收益是持续累积，还是会迅速边际递减？
* **上传 PDF 后优先看**:
  - 方法章节中 3D 观测与动作联合生成流程
  - 真实实验章节里的 one-shot 与扩展性评测
  - 消融章节，尤其是外观泛化与移动操作扩展部分

## Watchlist

### [W1]. EvolvingAgent: Curriculum Self-evolving Agent with Continual World Model for Long-Horizon Tasks [[HTML]](https://arxiv.org/html/2502.05907) [[PDF]](https://arxiv.org/pdf/2502.05907)
* **Paper ID**: `2502.05907`
* **Authors**: Tongtong Feng, Xin Wang, Zekai Zhou, Ren Wang, Yuwei Zhan, Guangyao Li, Qing Li, Wenwu Zhu
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇进 shortlist 的原因很明确：它把 continual world model、self-evolving curriculum 和 long-horizon embodied agent 放在一起，和“RL + World Model”主线是贴近的。没有进最终精选，主要因为当前证据更集中在 Minecraft 与 Atari100k，和今天更关心的机器人 VLA / 操作场景还有一层转译距离；同时给定摘录里的方法细节也不够扎实，难以支持更高排序。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. Hybrid Diffusion for Simultaneous Symbolic and Continuous Planning [[HTML]](https://arxiv.org/html/2509.21983) [[PDF]](https://arxiv.org/pdf/2509.21983)
* **Paper ID**: `2509.21983`
* **Authors**: Sigmund Hennum Høeg, Aksel Vaaler, Chaoqi Liu, Olav Egeland, Yilun Du
* **Author Priority**: Standard
* **为什么还值得留意**: 它值得关注，因为同时生成符号计划与连续轨迹，正面回应了扩散式规划在长时程决策上容易混模态、难做复杂决策的问题。没有进最终精选，是因为它更偏 long-horizon planning 而非 VLA/操控主线，而且方法依赖额外的符号序列标注，落到通用机器人数据流里未必轻量。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

### [W3]. LLM-Flax : Generalizable Robotic Task Planning via Neuro-Symbolic Approaches with Large Language Models [[HTML]](https://arxiv.org/html/2604.26569) [[PDF]](https://arxiv.org/pdf/2604.26569)
* **Paper ID**: `2604.26569`
* **Authors**: Seongmin Kim, Daegyu Lee
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇进入 watchlist，主要因为它把 LLM 用在 neuro-symbolic 任务规划的规则生成、失败恢复和零样本对象打分上，确实切中了“降低人工 planner 工程成本”的痛点。没进最终精选，是因为它与今天的核心方向相比更偏 PDDL 规划基础设施，且验证集中在 MazeNamo，和 VLA、world action model、Sim2Real 的直接关联度较弱。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. ATLAS: An Annotation Tool for Long-horizon Robotic Action Segmentation [[HTML]](https://arxiv.org/html/2604.26637) [[PDF]](https://arxiv.org/pdf/2604.26637)
* **Paper ID**: `2604.26637`
* **Authors**: Sergej Stanovcic, Daniel Sliwowski, Dongheui Lee
* **Author Priority**: Standard
* **为什么还值得留意**: ATLAS 值得保留在 shortlist，因为长时程机器人动作分段标注是训练与评测的重要底层工具，尤其对 manipulation policy learning 和 action segmentation 都有实际价值。没有进入最终精选，是因为它本质上是 annotation tool 论文，研究贡献更偏数据生产效率，而不是今天优先关注的模型路线推进。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

### [W5]. 3D Generation for Embodied AI and Robotic Simulation: A Survey [[HTML]](https://arxiv.org/html/2604.26509) [[PDF]](https://arxiv.org/pdf/2604.26509)
* **Paper ID**: `2604.26509`
* **Authors**: Tianwei Ye, Yifan Mao, Minwen Liao, Jian Liu, Chunchao Guo, Dazhao Du, Quanxin Shou, Fangqi Zhu, Song Guo
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇综述值得放进 watchlist，因为它把 3D generation 在 embodied AI 里的角色拆成数据生成、仿真环境和 sim2real bridge 三块，对后续选题很有地图价值。没有进最终精选的原因也很直接：它是 survey，不提供新的方法或实验增量，更适合作为背景阅读而非今日主打论文。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
