# RoboPulse | 2026-04-02

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 64 papers scanned · 10 shortlisted · 5 editor's picks

今天的主线很明确：VLA 已从“能不能做”进入“能否在长时程、未见场景和扰动下稳定做”的检验期，而世界模型与RL正在成为补强这条路线的两大接口。入选的5篇论文分别卡住了五个关键杠杆：WAM 对 VLA 的鲁棒性正面对比、agentic VLA 的数据与执行闭环、可泛化稠密奖励、可高频交互的潜变量世界模型，以及跨 embodiment 的灵巧手共设计。它们进入最终精选，不是因为都在堆更大的模型，而是都在回答“系统如何跨分布落地”这个更硬的问题。VIP 作者里，今天最值得优先跟踪的是 Hao Su 与 Xiaolong Wang 领衔的 House of Dextra；在这批论文中，它代表了把形态、控制与 sim-to-real 一起推进的高价值方向。

## 今日信号

- 今天最值得记住的研究信号是：VLA 的竞争焦点正从单次任务成功率转向对未见场景、扰动和长时程执行稳定性的系统性检验。
- 今天最值得记住的研究信号是：RL 正以“基础模型给奖励、世界模型给想象环境”的方式重新接入机器人，而不是回到手工奖励或纯模拟器路线。
- 今天最值得记住的研究信号是：具身系统开始把数据闭环、控制策略和硬件形态一起优化，下一阶段优势很可能来自系统协同而非单个大模型本身。

## Editor's Picks

### [1]. Do World Action Models Generalize Better than VLAs? A Robustness Study [[HTML]](https://arxiv.org/html/2603.22078) [[PDF]](https://arxiv.org/pdf/2603.22078) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.22078`
* **Authors**: Zhanguang Zhang, Zhiyuan Li, Behnam Rahmati, Rui Heng Yang, Yintao Ma, Amir Rasouli, Sajjad Pakdamansavoji, Yangzheng Wu, Lingfeng Zhang, Tongtong Cao, Feng Wen, Xinyu Wang, Xingyue Quan, Yingxue Zhang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为它没有继续堆模型，而是直接把 World Action Model 与 VLA 放到泛化和鲁棒性这个最关键的问题上做正面对照。
* **问题与切口**: 这篇工作抓住了一个现在最关键但常被回避的问题：当机器人离开训练分布、遭遇干扰或上下文变化时，世界动作模型是否比VLA更稳。相较继续堆更大的感知或动作头，它把焦点放在“先预测世界如何因动作而变，再决定怎么行动”的路线是否天然更利于泛化，并试图把世界模型在机器人中的几种常见用法放到统一鲁棒性视角下审视。
* **核心方法与证据**: 从摘录可见，作者先把机器人中的世界模型区分为学习式模拟器、规划辅助模块以及经改造后直接充当策略的模型，再围绕泛化与扰动鲁棒性组织比较。摘要和导论明确点名VLA的弱点是对未见场景与上下文扰动敏感，但当前HTML摘录没有给出完整基准、指标或数值，因此能确认的是研究问题和比较框架，具体优势幅度仍需后续核对正文实验部分。
* **正文要点**:
  - 作者把世界模型在机器人中的角色拆成学习式模拟器、规划辅助模块和改造后的策略本体。
  - 研究动机直接来自VLA在未见场景泛化不足、对干扰和上下文变化脆弱这两类痛点。
  - 问题设定覆盖导航、操作和运动等真实机器人语境，而非单一离线任务。
* **为什么值得跟**:
  - 它提供了 WAM 与 VLA 的直接比较框架，而不是各说各话地展示单点性能。
  - 如果结论成立，机器人策略研究的重心可能从“直接出动作”转向“先建模动作后果”。
  - 这类鲁棒性研究对真实部署比单次平均成功率更有决策价值。
* **风险 / 保留意见**:
  - 当前摘录缺少实验协议、数据划分与量化结果，结论强度暂时只能保守解读。
  - 若两类方法的训练数据、模型规模或动作接口不完全对齐，比较公平性会成为核心争议。
* **建议先看**: 先读导论里作者如何界定VLA的失效模式，再看世界模型三种用法的梳理，这会决定后面实验对照是否站得住。拿到PDF后，优先核查鲁棒性评测协议，而不是先看结论性表述。
* **关键词**: `World Action Model` `VLA` `鲁棒性` `泛化` `对比研究`
* **证据来源**: arXiv HTML (Introduction, Method)
* **读 PDF 先核查**:
  - WAM 与 VLA 的比较是否在训练数据规模、动作接口和计算预算上严格对齐？
  - 所谓鲁棒性测试具体覆盖了视觉干扰、动力学变化、任务组合偏移中的哪些维度？
  - 观察到的优势究竟来自世界预测本身，还是来自不同的模型容量与训练目标？
* **上传 PDF 后优先看**:
  - 实验设置与未见场景/扰动划分方式
  - 鲁棒性与泛化结果表格或主要定量比较
  - 对世界模型不同使用方式的讨论或消融章节

### [2]. RoboClaw: An Agentic Framework for Scalable Long-Horizon Robotic Tasks [[HTML]](https://arxiv.org/html/2603.11558) [[PDF]](https://arxiv.org/pdf/2603.11558) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.11558`
* **Authors**: Ruiying Li, Yunlang Zhou, YuYao Zhu, Kylin Chen, Jingyuan Wang, Sukai Wang, Kongtao Hu, Minhui Yu, Bowen Jiang, Zhan Su, Jiayao Ma, Xin He, Yongjian Shen, Yang Yang, Guanghui Ren, Maoqing Yao, Wenhao Wang, Yao Mu
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为它瞄准的是长时程机器人系统最真实的瓶颈：人工重置、失败回收和多策略编排，而不是只提升单个技能。
* **问题与切口**: RoboClaw解决的不是单个操作技能不够强，而是长时程机器人系统被“采集、训练、部署”三段式流程割裂后，既依赖人工重置，又难把失败重新纳入学习闭环。它的新意在于让同一个VLM驱动控制器同时负责高层推理、数据采集和策略编排，并用可自复位的动作对把短技能连成可持续迭代的长期任务流水线。
* **核心方法与证据**: 方法主线很清晰：在策略层引入Entangled Action Pairs，把正向操作与逆向恢复动作绑定成自重置回路，用于持续的on-policy数据采集与迭代改进；部署时仍由同一代理做高层决策并动态调用已学原语。证据来自真实Agibot G01双臂移动操作平台，实验围绕数据效率、子任务成功率、复杂长程任务表现和从失败中学习四个问题展开；作者也明确承认云端大模型时延与“可逆复位动作”假设是限制。
* **正文要点**:
  - Entangled Action Pairs把前向操作和逆向恢复动作绑定成可持续自重置的数据回路。
  - 同一VLM驱动代理同时承担数据采集、策略学习支撑与部署期高层编排。
  - 真实机器人实验明确围绕数据效率、子任务成功率、长时程任务表现和失败学习四个问题展开。
* **为什么值得跟**:
  - 它把长时程VLA系统中最昂贵的人力环节直接纳入算法设计。
  - 失败不再只是离线筛掉的脏数据，而被转化为持续改进策略的学习资源。
  - 如果这条路线稳定，agentic robotics 会比单一 policy learning 更接近可运营系统。
* **风险 / 保留意见**:
  - 框架依赖可实现的逆向复位行为，很多现实任务未必天然满足这一假设。
  - 云端大模型的时延会直接影响闭环反应速度和系统工程可用性。
* **建议先看**: 先抓住作者统一“采集-训练-执行”三段流程的系统图，再看EAP如何把失败恢复变成数据来源。之后重点检查四类实验问题是否都真正对应到框架主张。
* **关键词**: `VLA` `长时程操作` `Agentic Robotics` `自重置` `数据闭环`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 高层VLM在部署时如何决定原语切换与异常恢复，是否存在显式状态机或提示模板依赖？
  - EAP 会不会因为偏向可逆动作而压缩任务覆盖面，导致采到的数据分布失真？
  - 从失败中学习的机制具体如何避免把低质量恢复轨迹反向强化进策略？
* **上传 PDF 后优先看**:
  - 系统框架与代理循环设计章节
  - 数据效率与复杂长时程任务实验
  - 失败案例、恢复机制与局限性讨论

### [3]. Generalizable Dense Reward for Long-Horizon Robotic Tasks [[HTML]](https://arxiv.org/html/2604.00055) [[PDF]](https://arxiv.org/pdf/2604.00055) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.00055`
* **Authors**: Silong Yong, Stephen Sheng, Carl Qi, Xiaojie Wang, Evan Sheehan, Anurag Shivaprasad, Yaqi Xie, Katia Sycara, Yesh Dattatreya
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为它把长时程机器人RL最难泛化的瓶颈从“策略”转回到“奖励接口”，而且方案明显可迁移。
* **问题与切口**: 这篇工作切入的是长时程机器人RL里最难泛化的一环：奖励。面对预训练基础策略在长链条任务中因分布偏移和误差累积而失效，作者没有再为每个任务手工写reward，而是提出VLLR，用LLM+VLM生成子目标级稠密外部奖励，再叠加基于策略自我确定性的内在奖励，把“可迁移奖励接口”做成核心贡献。
* **核心方法与证据**: 方法上，VLLR以预训练策略为起点，用PPO做微调，并按FLaRe式做价值函数配套。LLM接收任务指令和结构化场景图，先把任务拆成有序且落地的子目标；VLM再根据视觉观测判断每一步是否推进了子目标，从而形成进度式外部奖励；同时再加入基于策略自我确定性的内在奖励。摘录中的实验证据集中在CHORES，作者声称相对基线提升成功率与效率，并能泛化到预训练集之外的未见任务。
* **正文要点**:
  - 外部奖励以“任务分解后的子目标进度”作为基本监督单位，而不是只看终局成功。
  - 任务分解依赖 LLM 读取指令与结构化场景图，进度识别依赖 VLM 读取视觉观测。
  - 作者在 CHORES 上报告了成功率、效率和未见任务泛化三类收益。
* **为什么值得跟**:
  - 它把基础模型从“直接出动作”换成“提供可泛化监督”，更容易与现有RL管线对接。
  - 长时程任务最缺的就是中间反馈，这篇工作正面补了这一层。
  - 如果奖励接口足够稳，预训练策略的后续RL微调会更像系统化工程而不是逐任务调参。
* **风险 / 保留意见**:
  - 奖励质量强依赖 LLM 的分解正确性与 VLM 的进度判断稳定性，误判可能被系统性放大。
  - 方法要求结构化场景图，转到观测更噪或缺少结构先验的环境时可能掉性能。
* **建议先看**: 先看奖励是如何被拆成外部进度信号和内部确定性信号，再看作者怎样把它接到PPO微调里。拿到PDF后，最值得先查的是对奖励来源和组成部分的消融。
* **关键词**: `长时程RL` `稠密奖励` `LLM` `VLM` `CHORES`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)
* **读 PDF 先核查**:
  - 策略自我确定性的定义、校准方式和时序聚合方式是什么？
  - 若 LLM 任务分解出错或顺序不合理，VLLR 是否有纠偏机制？
  - 当场景图不完整或有噪声时，这套奖励接口还能否稳定迁移？
* **上传 PDF 后优先看**:
  - 奖励构建与两阶段优化方法章节
  - CHORES 上的主结果与未见任务泛化实验
  - 外部奖励、内在奖励和价值函数设计的消融分析

### [4]. DreamerAD: Efficient Reinforcement Learning via Latent World Model for Autonomous Driving [[HTML]](https://arxiv.org/html/2603.24587) [[PDF]](https://arxiv.org/pdf/2603.24587) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.24587`
* **Authors**: Pengxuan Yang, Yupeng Zheng, Deheng Qian, Zebin Xing, Qichao Zhang, Linbo Wang, Yichen Zhang, Shaoyu Guo, Zhongpu Xia, Qiang Chen, Junyu Han, Lingyun Xu, Yifeng Pan, Dongbin Zhao
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为它把“世界模型适合做RL”从概念层推进到了交互频率真正可用的工程层。
* **问题与切口**: DreamerAD瞄准的是世界模型用于自动驾驶RL时最现实的瓶颈：像素级扩散世界模型虽然安全、可解释，但采样太慢，根本支撑不了高频交互。它把训练舞台搬到潜变量空间，用一步采样替代传统多步扩散，同时保留可视化解释能力，把“世界模型能不能真给RL提速”从概念验证推进到可运行系统。
* **核心方法与证据**: 摘要与方法摘录给出了三条清晰机制：用shortcut forcing做递归多分辨率压缩，把扩散采样从100步压到1步；在潜表示上训练自回归稠密奖励模型，改善细粒度credit assignment；再用Gaussian vocabulary sampling约束GRPO探索的物理合理性。证据来自NavSim闭环评测，场景含8相机与LiDAR，指标覆盖安全、舒适、合规与进度；作者在结论中报告NavSim v2上87.7 EPDMS，但更细的消融边界仍需看全文。
* **正文要点**:
  - 核心加速来自 shortcut forcing，把扩散采样复杂度从多步压到一步。
  - 奖励不是在像素空间上做后验打分，而是直接在潜表示上做自回归稠密建模。
  - 评测采用 NavSim 闭环环境，指标显式覆盖碰撞、舒适性、合规性和自车进度。
* **为什么值得跟**:
  - 它回应了世界模型用于高频决策时最致命的时延问题。
  - 潜空间奖励建模说明世界模型不只是生成器，也可以成为信用分配接口。
  - 即便场景是自动驾驶，这套“快世界模型+RL”的组合对机器人世界模型研究同样有启发。
* **风险 / 保留意见**:
  - 场景聚焦自动驾驶而非通用机器人操作，向VLA或操作任务外推需要谨慎。
  - 结果高度依赖基础世界模型与闭环评测环境，真实开放道路迁移证据在当前摘录中不足。
* **建议先看**: 先盯住三条机制分别解决的瓶颈：采样速度、奖励密度和探索物理性。随后再看闭环指标是否真的支持“更快且不牺牲安全语义”这个主张。
* **关键词**: `World Model` `潜变量RL` `自动驾驶` `扩散模型` `NavSim`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 一步采样会在多步滚动想象中累积多大误差，是否影响长时程规划稳定性？
  - 潜表示上的稠密奖励与安全关键指标之间是否存在可解释对应关系？
  - Gaussian vocabulary sampling 在探索效率与物理约束之间的权衡是如何体现的？
* **上传 PDF 后优先看**:
  - 潜变量世界模型与采样压缩机制章节
  - 奖励建模与RL训练目标章节
  - NavSim 闭环主结果及三项机制的消融实验

### [5]. House of Dextra: Cross-embodied Co-design for Dexterous Hands [[VIP]] [[HTML]](https://arxiv.org/html/2512.03743) [[PDF]](https://arxiv.org/pdf/2512.03743) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2512.03743`
* **Authors**: Kehlani Fay, Darin Anthony Djapri, Anya Zorin, James Clinton, Ali El Lahib, Hao Su, Michael T. Tolley, Sha Yi, Xiaolong Wang
* **Author Priority**: Core VIP
* **一句话结论**: 必须优先看，因为它把灵巧手的形态设计、控制共享和 sim-to-real 制造链条真正合成了一个跨 embodiment 的研究框架。
* **问题与切口**: 这篇论文把灵巧手研究里长期分离的两件事重新绑在一起：硬件形态设计与控制策略学习。它不是在固定手型上再追更强policy，而是用跨embodiment协同设计去同时搜索手指、关节与手掌结构，并训练能感知形态差异的共享控制器；相较传统共设计，新意在于既强调大规模形态搜索，也明确面向可制造、可落地的sim-to-real流程。
* **核心方法与证据**: 方法上，作者先按程序化设计规则随机生成大量手部形态，再根据共享运动学结构把设计归入不同family，在family内用形态编码条件化控制策略，实现跨embodiment共享学习。物理grammar显式编码碰撞几何、关节限制和可制造部件规格，减少“仿真里好看、现实里做不出”的设计。实验覆盖三项灵巧操作任务，并在in-hand rotation上给出仿真到真实部署；摘录还给出了50轮、每轮40个设计、每个设计128个随机环境的评测规模。
* **正文要点**:
  - 形态搜索空间不仅包含手指与关节，还覆盖手掌结构生成，设计自由度很高。
  - 控制策略显式接收形态编码，从而在同一家族的不同 embodiment 间共享经验。
  - 物理 grammar 预先编码碰撞、关节极限与制造规格，目标是让候选设计直接具备落地约束。
* **为什么值得跟**:
  - 它把灵巧操作中的“硬件上限”重新拉回主问题，而不是默认手型固定不变。
  - 跨 embodiment 控制让大规模形态搜索不再需要为每个设计单独训练策略。
  - 有真实制造与 sim-to-real 部署，这让论文价值明显高于纯仿真形态搜索。
* **风险 / 保留意见**:
  - 当前摘录中的任务范围仍以三类灵巧操作为主，更广泛任务泛化能力还需核查。
  - family 划分和 grammar 规则带有人为先验，可能在提升效率的同时限制开放式设计发现。
* **建议先看**: 先看 physical grammar 和 morphology-conditioned policy 这两块，因为它们决定了这篇工作是不是“真共设计”而不是更快的搜索。随后重点核查 sim-to-real 的 in-hand rotation 证据，以及基线比较是否公平。
* **关键词**: `灵巧手` `Co-design` `Cross-embodiment` `Sim2Real` `Hao Su`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)
* **读 PDF 先核查**:
  - 不同 embodiment family 的划分方式对搜索结果和控制泛化有多敏感？
  - 形态条件化控制是否会因数据分布不均而偏向某些家族，从而影响设计评估公平性？
  - 哪些制造约束最显著地改变了最优设计，相比纯仿真最优解损失了什么？
* **上传 PDF 后优先看**:
  - 形态生成 grammar 与设计空间定义章节
  - 跨 embodiment 控制器与形态编码训练章节
  - sim-to-real 部署、基线比较与失败案例分析

## Watchlist

### [W1]. Learning Humanoid Navigation from Human Data [[HTML]](https://arxiv.org/html/2604.00416) [[PDF]](https://arxiv.org/pdf/2604.00416)
* **Paper ID**: `2604.00416`
* **Authors**: Weizhuo Wang, Yanjie Ze, C. Karen Liu, Monroe Kennedy III
* **Author Priority**: Standard
* **为什么还值得留意**: EgoNav 进入 shortlist 的原因很充分：它用纯人类步行数据、360°视觉记忆和扩散式轨迹分布建模，直接做到了 humanoid 零样本导航部署，这在“跨 embodiment 学习”上很有辨识度。没有进入最终精选，主要是因为它更偏导航先验与人类数据迁移，和今天最核心的 VLA/WAM/RL+VLA 主线连接稍弱；同时当前摘录虽给出真实部署与部分指标定义，但对系统级比较和扩展边界的展开还不够完整。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. Multi-Camera View Scaling for Data-Efficient Robot Imitation Learning [[HTML]](https://arxiv.org/html/2604.00557) [[PDF]](https://arxiv.org/pdf/2604.00557)
* **Paper ID**: `2604.00557`
* **Authors**: Yichen Xie, Yixiao Wang, Shuqi Zhao, Cheng-En Wu, Masayoshi Tomizuka, Jianwen Xie, Hao-Shu Fang
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇工作进入 shortlist，是因为它抓住了 imitation learning 里一个很实用的扩展点：不用增加人工示范，只靠多相机同步视角就生成伪示范、提升数据效率与视角不变性。没有进入最终精选，是因为它更像高性价比的数据工程与训练技巧，而不是今天关注的 VLA、世界模型或RL接口层创新；从摘录看，方法价值明确，但概念外延相对有限。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

### [W3]. Functional Force-Aware Retargeting from Virtual Human Demos to Soft Robot Policies [[HTML]](https://arxiv.org/html/2604.01224) [[PDF]](https://arxiv.org/pdf/2604.01224)
* **Paper ID**: `2604.01224`
* **Authors**: Uksang Yoo, Mengjia Zhu, Evan Pezent, Jom Preechayasomboon, Jean Oh, Jeffrey Ichnowski, Amir Memar, Ben Abbatematteo, Homanga Bharadhwaj, Ashish Deshpande, Harsha Prahlad
* **Author Priority**: Standard
* **为什么还值得留意**: SoftAct 值得保留在 watchlist，因为它把软体手技能迁移从“关节轨迹对齐”改成“接触力与功能意图对齐”，这条力感知 retargeting 路线很有研究味道。之所以没进最终精选，是因为它的核心贡献更偏软体手控制与接触建模，而不是本轮最想抓的 VLA、world model 或 RL+VLA 汇合点；另外当前摘录中的主证据重心放在跟踪与任务成功，和更广义的系统泛化主张之间还需要全文补证。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. DreamControl-v2: Simpler and Scalable Autonomous Humanoid Skills via Trainable Guided Diffusion Priors [[HTML]](https://arxiv.org/html/2604.00202) [[PDF]](https://arxiv.org/pdf/2604.00202)
* **Paper ID**: `2604.00202`
* **Authors**: Sudarshan Harithas, Sangkyung Kwak, Pushkal Katara, Srujan Deolasee, Dvij Kalaria, Srinath Sridhar, Sai Vemprala, Ashish Kapoor, Jonathan Chung-Kuan Huang
* **Author Priority**: Standard
* **为什么还值得留意**: DreamControl-v2 被列入 shortlist，是因为它把扩散先验直接训练到 robot space，并讨论训练数据规模与采样规模如何影响 humanoid 技能学习，这与“生成先验+RL”方向高度相关。没有进入最终精选，主要是因为它更偏 humanoid motion prior 与 autonomy recipe 的简化，而不是今天更核心的 VLA 对比、世界动作模型鲁棒性或奖励接口问题；从现有摘录看，部署与系统闭环证据也不如入选论文那么扎实。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)

### [W5]. Deep Reinforcement Learning for Robotic Manipulation under Distribution Shift with Bounded Extremum Seeking [[HTML]](https://arxiv.org/html/2604.01142) [[PDF]](https://arxiv.org/pdf/2604.01142)
* **Paper ID**: `2604.01142`
* **Authors**: Shaifalee Saxena, Rafael Fierro, Alexander Scheinker
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇论文进入 shortlist 的原因是它非常直接地针对分布偏移下的 manipulation 鲁棒性，把 DDPG 和 bounded extremum seeking 结合成在线自适应控制器，在接触变化场景下有明确问题指向。没有进入最终精选，是因为它整体仍属于较经典的“RL+自适应控制”混合路线，和今天强调的 foundation-model、VLA、world model 主线距离更远；而且当前摘录展示的证据主要集中在特定摩擦变化案例，外推范围暂时有限。
* **证据来源**: arXiv HTML (Introduction, Experiments)
