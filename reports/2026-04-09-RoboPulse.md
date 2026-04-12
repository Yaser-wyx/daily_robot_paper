# RoboPulse | 2026-04-09

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 47 papers scanned · 10 shortlisted · 6 editor's picks

今天这组最终精选的主线很清晰：VLA 不再只比谁的 backbone 更大，而是同时往“可部署、可复现、可诊断、可扩数”四个方向补齐短板。入选论文覆盖了低成本 VLA 推理、双手灵巧抓取数据与生成、单张全景到仿真场景重建、野外人体数据采集、VLM 失败分析前端，以及 foundation model 在导航决策上的失效诊断，形成了一条从数据到模型到评测的完整链条。在给定 shortlist 里，最值得优先跟踪的 VIP 作者是 He Wang，他参与的 BiDexGrasp 代表了几何/尺度自适应双手抓取数据基础设施这条线。若从研究投资回报看，今天最强信号不是再造一个更大的通用模型，而是把 VLA 周边的场景生成、数据采集、证据压缩和可靠性分析做成可复用基础件。

## 今日信号

- 今天最值得记住的研究信号是：VLA 的竞争焦点正在从“大模型能力上限”转向“整条推理链路的成本、透明度与部署效率”。
- 今天最值得记住的研究信号是：高价值机器人数据基础设施正在向双手抓取、野外全身动作和触觉闭环等更难采集但更接近真实执行的问题聚焦。
- 今天最值得记住的研究信号是：failure analysis 与诊断性评测正在成为 foundation model 进入机器人闭环前的必要环节，而不再只是附属 benchmark。

## Editor's Picks

### [1]. A1: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model [[HTML]](https://arxiv.org/html/2604.05672) [[PDF]](https://arxiv.org/pdf/2604.05672) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.05672`
* **Authors**: Kaidong Zhang, Jian Zhang, Rongtao Xu, Yu Sun, Shuoshuo Xue, Youpeng Wen, Xiaoyu Guo, Minghao Guo, Weijia Liufu, Liu Zihou, Kangyi Ji, Yangsong Zhang, Jiarun Zhu, Jingzhi Liu, Zihang Li, Ruiyi Chen, Meng Cao, Jingming Zhang, Shen Zhao, Xiaojun Chang, Feng Zheng, Ivan Laptev, Xiaodan Liang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看；如果你关心 VLA 何时能真正跑在普通硬件上，这篇把“开源透明”和“全链路加速”放到了同一个设计目标里。
* **问题与切口**: 这篇工作瞄准的是 VLA 落地时最现实的瓶颈：大规模 VLM 骨干与迭代式动作头带来的延迟和算力成本。它提出一个完全开源、强调透明性的截断式 VLA 框架，不只压缩视觉语言部分，而是把感知到动作生成整条推理链路一起做预算感知优化。相较常见“堆更大 backbone 或更重生成头”的路线，它更像是在回答一个部署问题：如何在尽量不牺牲操作成功率的前提下，把 VLA 变成低成本、高吞吐的系统。
* **核心方法与证据**: 从摘录可见，方法核心是利用预训练 VLM 的隐式 affordance 先验，并引入一个 budget-aware 的自适应推理机制，联合加速 VLM 与动作头，而不是只做单点裁剪。证据上，论文覆盖了 LIBERO、VLABench 两类仿真基准，并给出四类真实机器人任务与消融实验，说明作者试图同时验证多步操作、视觉语言理解与真实部署可行性。但 HTML 摘录没有给出关键延迟、吞吐或成功率提升幅度，因此现阶段更适合把它视为一篇系统路线清晰、数值细节仍待核验的工程型 VLA 论文。
* **正文要点**:
  - 论文明确把优化对象定义为“完整 VLA 推理流水线”，而不只是视觉语言骨干网络。
  - 仿真评测覆盖 LIBERO 与 VLABench，强调多步操作和视觉语言理解两类能力。
  - 正文包含真实机器人、仿真和消融三类证据，但摘录未提供核心性能增益的具体数值。
* **为什么值得跟**:
  - 它击中了 VLA 从论文走向部署时最关键的现实约束：延迟、算力和复现门槛。
  - 完整开源训练栈的承诺很重要，因为当前不少 VLA 工作的真正瓶颈恰恰是训练和评测不可复现。
  - 如果其自适应截断策略稳定成立，它对边缘部署和低成本机器人平台会有直接价值。
* **风险 / 保留意见**:
  - 摘录没有展示速度与成功率之间的定量 trade-off，方法是否真有稳定收益仍需看正文表格。
  - “透明”和“开源”能提升可复现性，但也意味着方法创新可能更多在系统整合，而非全新学习范式。
* **建议先看**: 先沿着“为什么要优化整条 VLA 链路而非单个模块”这条主线读，再核查自适应推理到底在哪些计算路径上发生。随后重点看真实机器人部分，判断它是否真解决了部署而不是只在仿真中省算力。
* **关键词**: `VLA` `高效推理` `开源复现` `自适应截断` `机器人操作`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 预算感知的自适应推理究竟如何在 VLM 与动作头之间分配计算，而不是只做简单早退或裁剪？
  - 利用预训练 VLM 的隐式 affordance 先验时，动作生成阶段保留了多少任务特异性，而不会被通用语义先验拖偏？
  - 真实机器人实验里的加速收益，主要来自骨干截断、动作头简化，还是两者联合调度？
* **上传 PDF 后优先看**:
  - 方法章节里关于 adaptive inference / truncation 的设计与推理路径说明
  - 实验章节中的真实机器人设置、硬件条件与延迟或吞吐报告
  - 消融章节里各加速组件分别带来的性能与成本变化

### [2]. BiDexGrasp: Coordinated Bimanual Dexterous Grasps across Object Geometries and Sizes [[VIP]] [[HTML]](https://arxiv.org/html/2604.06589) [[PDF]](https://arxiv.org/pdf/2604.06589) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.06589`
* **Authors**: Mu Lin, Yi-Lin Wei, Jiaxuan Chen, Yuhao Lin, Shuoyu Chen, Jiangran Lyu, Jiayi Chen, Yansong Tang, He Wang, Wei-Shi Zheng
* **Author Priority**: Core VIP
* **一句话结论**: 非常值得优先看；这是今天最像“可直接沉淀成长期数据资产”的论文，也是给双手操作补基础设施的一篇硬货。
* **问题与切口**: BiDexGrasp 直指双手灵巧抓取长期缺的两样东西：大规模高质量数据，以及能显式处理双手协同、物体几何和尺度变化的生成模型。与很多把单手抓取流程硬扩展到双手的做法不同，它把问题拆成“怎么可靠合成物理可行数据”和“怎么学到几何/尺度自适应的双手协同策略”两层。这个切口很扎实，因为双手抓取的难点本来就不只是接触点多，而是左右手之间的约束与物体尺寸变化同时存在。
* **核心方法与证据**: 方法上，作者先提出一个双阶段抓取合成流程，用区域级初始化降低高维搜索难度，再通过解耦的 force-closure 优化生成物理可行标注；在此基础上构建大规模数据集，并训练一个显式建模双手协调且适配物体几何与尺度的生成框架。证据比较充足：摘录给出了 6,351 个物体、970 万抓取标注的数据规模，也说明了仿真合成评测、桌面数据子集训练/测试划分，以及在多尺度对象上的评测设置。即便不看 PDF，也能确认它不是只报几个可视化例子，而是把数据构建与生成建模做成了完整闭环。
* **正文要点**:
  - 数据合成采用“区域初始化 + 解耦 force-closure 优化”的两阶段策略，以处理双手抓取的高维难题。
  - 论文构建了包含 6,351 个多样物体和 970 万双手抓取标注的大规模数据集。
  - 生成框架显式建模双手协调，并强调对物体几何形状与尺寸变化的适应能力。
* **为什么值得跟**:
  - 双手操作若没有规模化数据支撑，很难稳定进入通用 manipulation 学习的主流。
  - 这类数据资产不仅能服务抓取生成，也可能成为后续双手 VLA 或世界模型的重要预训练来源。
  - He Wang 在作者列表中，使这条以几何和手物交互为核心的数据路线更值得持续跟踪。
* **风险 / 保留意见**:
  - 当前证据主要来自 MuJoCo 合成与离线评测，真实机器人抓取迁移能力仍需核查。
  - 物理可行不等于任务可行，force-closure 优化生成的抓取是否覆盖真实任务中的操作约束还不明确。
* **建议先看**: 先看数据合成流程，因为这决定了整篇工作的可信度上限；再看生成模型如何把双手协调与几何/尺度条件显式编码进去。若你更关心可复用价值，优先核对数据集构成与评测协议。
* **关键词**: `双手灵巧抓取` `数据集` `抓取生成` `几何自适应` `He Wang`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 区域级初始化具体如何缩小双手抓取的搜索空间，并避免偏向某些物体几何类型？
  - 解耦的 force-closure 优化在双手之间如何分配约束，是否会牺牲部分协同性以换取求解稳定性？
  - 生成模型对“尺度变化”的处理是通过显式尺度条件、归一化机制，还是依赖数据分布覆盖？
* **上传 PDF 后优先看**:
  - 数据合成章节中两阶段 pipeline 的细节与失败模式分析
  - 实验章节里多尺度对象与跨几何类型的泛化结果
  - 数据集统计章节中对象来源、标注分布与训练测试切分方式

### [3]. Genie Sim PanoRecon: Fast Immersive Scene Generation from Single-View Panorama [[HTML]](https://arxiv.org/html/2604.07105) [[PDF]](https://arxiv.org/pdf/2604.07105) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.07105`
* **Authors**: Zhijun Li, Yongxin Su, Di Yang, Jichao Wang, Zheyuan Xing, Qian Wang, Maoqing Yao
* **Author Priority**: Standard
* **一句话结论**: 值得优先看；它不是直接做策略学习，但很可能是低成本 sim 侧场景扩展的一块高杠杆基础件。
* **问题与切口**: 这篇工作解决的是机器人仿真里一个常被低估的瓶颈：如何从极低采集成本的输入，快速生成足够真实且几何一致的 3D 场景。它从单张全景图出发，做前馈式 Gaussian splatting 重建，并把全景拆成六个 cubemap 面并行处理，再无缝拼回。相对传统依赖密集多视角、逐场景优化的 3DGS 路线，它的关键新意不是再追求极限重建质量，而是追求“几秒级、可批量、可用于 manipulation simulation”的成本性能比。
* **核心方法与证据**: 方法主线较清楚：先用 DA360 获取全景级、尺度更一致的深度，再用 DepthPro 提供高分辨率细节深度，通过逆深度的拉普拉斯金字塔融合保留全局尺度与局部纹理；随后再用一个 training-free 的 depth injection 模块去约束前馈式 Gaussian 预测，降低各 cubemap 面之间的尺度漂移和接缝问题。证据边界也很明确：HTML 强调的是系统模式对比、接缝一致性、极区稳定性、几何一致性、运行时间和显存，而不是大规模 benchmark 上的标准化分数，因此更像一篇偏系统工程与仿真生产力的论文。
* **正文要点**:
  - 全景图被拆成六个不重叠 cubemap 面并行重建，以换取速度和分辨率。
  - 深度融合同时结合 DA360 的全局尺度一致性和 DepthPro 的细粒度细节。
  - 评测重点放在接缝一致性、几何连贯性、运行时间和显存，而非大规模标准 benchmark。
* **为什么值得跟**:
  - 单视角全景到可用仿真场景的链路一旦稳定，会直接降低合成数据和 sim-to-real 场景搭建成本。
  - 它把重建目标对齐到了机器人仿真的需求，而不是纯视觉社区常见的离线重建指标。
  - 若和生成式场景扩增结合，这类方法可能成为世界模型或策略训练的数据工厂前端。
* **风险 / 保留意见**:
  - 论文摘录没有给出统一 benchmark 上的量化对比，因此泛化上限和真实仿真收益仍需保守判断。
  - 训练自由的深度注入设计很实用，但也可能受上游单目深度误差和场景类型分布强烈影响。
* **建议先看**: 先顺着“单张全景如何被拆分、融合、再重建”这条方法链读，确认作者真正解决的是接缝和尺度一致性。然后重点看运行时间、显存和 novel-view 质量的证据，因为这决定它是否真适合作为仿真生产工具。
* **关键词**: `仿真场景生成` `Gaussian Splatting` `全景重建` `单目深度融合` `Sim2Real`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - DA360 与 DepthPro 的逆深度融合在极区和跨面边界上是否有稳定的误差控制机制？
  - training-free depth injection 是如何插入前馈 Gaussian 预测网络而不引入额外优化的？
  - 对于桌面操作场景，几何一致性改善是否真正转化成了更可靠的物理仿真和交互可用性？
* **上传 PDF 后优先看**:
  - 方法章节中全景深度融合与 depth injection 的具体实现描述
  - 实验章节里不同系统模式对接缝一致性和几何稳定性的对比
  - 运行时间与峰值显存报告，以及与逐场景优化方法的成本比较

### [4]. RoSHI: A Versatile Robot-oriented Suit for Human Data In-the-Wild [[HTML]](https://arxiv.org/html/2604.07331) [[PDF]](https://arxiv.org/pdf/2604.07331) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.07331`
* **Authors**: Wenjing Margaret Mao, Jefferson Ng, Luyang Hu, Daniel Gehrig, Antonio Loquercio
* **Author Priority**: Standard
* **一句话结论**: 值得优先看；如果你关心 humanoid 学习的“数据入口”而不是单一算法，这篇是今天最实用的一篇。
* **问题与切口**: RoSHI 要解决的是：怎样在不依赖昂贵动捕房间的前提下，采集可用于 humanoid policy learning 的、带全局坐标的全身人类动作数据。它把低成本稀疏 IMU 与 Project Aria 眼镜结合起来，用 IMU 对抗遮挡和高速动作，用自中心 SLAM 锚定长时程的全局轨迹。与纯视觉或纯惯导方案相比，它的切口并不追求逐帧最精细重建，而是强调长序列稳定性、可移植性和在野外环境中的可用性。
* **核心方法与证据**: 从方法摘录看，系统由九个低成本 IMU 和 Aria 提供的广角 egocentric 视频组成，先获得头显 6-DoF 轨迹，再结合 EgoAllo 扩散模型估计相机坐标系下的人体姿态，并通过头显轨迹变换到全局坐标。关键改动是不用视频手部估计去引导扩散，而是直接用来自 IMU 的骨骼朝向作为条件。证据上，作者在室内外采集了 11 段动作序列，由两位采集者完成，并围绕姿态质量、机器人重定向，以及是否能支撑 whole-body policy transfer 到实体 humanoid 三个问题展开验证。
* **正文要点**:
  - 系统把九个低成本 IMU 与 Project Aria 眼镜组合，目标是便携、低成本的野外全身动作采集。
  - 作者用 IMU 骨骼朝向替代视频手部估计来引导 EgoAllo 扩散式姿态生成。
  - 评测不仅看姿态质量，还看动作是否能重定向到机器人并支持实体 humanoid 策略迁移。
* **为什么值得跟**:
  - 机器人学习若想真正扩到野外长时程行为，低摩擦的人体数据采集系统是绕不开的基础设施。
  - 全局坐标一致的全身数据比只看局部姿态更接近 humanoid 控制和模仿学习的实际需求。
  - 这类系统一旦稳定，会把“收数据”从实验室专用流程变成日常化、可持续的研究能力。
* **风险 / 保留意见**:
  - 作者明确优先保证序列稳定性而非逐帧精度，因此某些精细动作细节可能仍不够可靠。
  - 目前摘录显示的数据规模仍较小，是否足以支撑大规模泛化学习还需要看后续扩展。
* **建议先看**: 先看传感器融合与坐标变换链路，确认全局一致性是如何建立的；再看机器人重定向和实体策略迁移部分，因为这决定它是“好看的动捕”还是“真能用于机器人学习的数据系统”。
* **关键词**: `humanoid` `人体数据采集` `IMU` `Project Aria` `模仿学习`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 用 IMU 骨骼朝向替代视频手部条件后，EgoAllo 的扩散先验在哪些动作类型上最受益或最受损？
  - SLAM 轨迹漂移在长时程室外序列里如何影响全身姿态的全局一致性？
  - 机器人重定向成功更多来自采集系统本身，还是来自后处理与 retargeting 管线的补偿？
* **上传 PDF 后优先看**:
  - 系统章节中传感器同步、坐标系定义与姿态生成流程
  - 实验章节里室内外三类数据集划分及各自失败模式
  - 重定向与实体 humanoid policy transfer 的验证设置和案例

### [5]. KITE: Keyframe-Indexed Tokenized Evidence for VLM-Based Robot Failure Analysis [[HTML]](https://arxiv.org/html/2604.07034) [[PDF]](https://arxiv.org/pdf/2604.07034) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.07034`
* **Authors**: Mehdi Hosseinzadeh, King Hang Wong, Feras Dayoub
* **Author Priority**: Standard
* **一句话结论**: 值得优先看；它不是再训练一个更强 VLM，而是把长视频失败分析先变成模型更容易吃下去的证据表示。
* **问题与切口**: KITE 关注的是机器人长时程执行失败分析里的一个现实问题：原始视频太长、线索太散，通用 VLM 很难同时抓住什么时候出错、空间关系怎么错、以及任务目标是什么。它提出一个训练自由、模型无关的前端，把长视频压缩成少量运动显著关键帧、开放词汇检测结果、伪 BEV 布局图，以及机器人和场景上下文 token。相比直接把整段视频喂给 VLM，这条路线的价值在于把“何时、何地、为何”显式结构化出来。
* **核心方法与证据**: 方法由三部分组成：关键帧选择负责提取时间上的异常或动作转折，伪 BEV 负责把相对布局、坐标轴、时间戳与检测置信度可视化，序列化 token 则把机器人 profile、场景关系和接触转移信息统一到同一提示结构中。证据上，论文以 RoboFAC 为主评测，核心对比是 vanilla Qwen2.5-VL 与 KITE + Qwen2.5-VL，并补充伪 BEV 和关键帧选择的消融，以及实验室单臂/双臂案例说明跨场景迁移。不过摘录没有给出各题型的具体提升幅度，因此现阶段更能确认的是思路的可解释性，而非最终上限。
* **正文要点**:
  - KITE 是训练自由、模型无关的前端，目标是让通用 VLM 更稳定地做机器人失败分析。
  - 表示由关键帧、开放词汇检测、伪 BEV、接触转移 token 和场景上下文共同构成。
  - 主评测使用 RoboFAC，并将 KITE + Qwen2.5-VL 与原始 Qwen2.5-VL 直接比较。
* **为什么值得跟**:
  - 它说明机器人失败分析不一定要靠重训练专用模型，前端证据结构化本身就可能带来显著收益。
  - 伪 BEV 和接触转移 token 这类设计，把机器人最关心的空间与交互关系显式暴露给 VLM。
  - 这条路线对故障诊断、恢复建议乃至自动数据标注都可能有外溢价值。
* **风险 / 保留意见**:
  - 前端质量高度依赖检测、深度和关键帧筛选，任何上游误差都可能被结构化后放大。
  - RoboFAC 是 QA 式基准，能否完全代表真实闭环机器人诊断场景仍需谨慎。
* **建议先看**: 先看证据表示设计，而不是先看 benchmark 分数；这篇真正有价值的部分在于它把长视频压缩成可解释 token 的方式。然后再看消融，判断哪些结构化信号是必需的。
* **关键词**: `失败分析` `VLM` `关键帧` `伪BEV` `可解释前端`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 关键帧预算很小的条件下，运动显著性选择是否会漏掉那些真正决定失败的低运动关键瞬间？
  - 伪 BEV 的布局编码在单目相对深度不可靠时，是否会对空间关系推理产生系统性误导？
  - 接触转移 token 的定义有多粗粒度，它是否足以支持解释复杂双臂交互失败？
* **上传 PDF 后优先看**:
  - 方法章节中 keyframe selection 与 pseudo-BEV 构造细节
  - RoboFAC 实验里的题型分解结果与前端消融
  - 实验室真实机器人案例中单臂与双臂失败的迁移表现

### [6]. Before We Trust Them: Decision-Making Failures in Navigation of Foundation Models [[HTML]](https://arxiv.org/html/2601.05529) [[PDF]](https://arxiv.org/pdf/2601.05529) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2601.05529`
* **Authors**: Jua Han, Jaeyoon Seo, Jungbin Min, Sieun Choi, Huichan Seo, Jihie Kim, Jean Oh
* **Author Priority**: Standard
* **一句话结论**: 值得优先看；它不是教模型更会导航，而是在提醒你别被高平均分误导，以为 foundation model 已经可靠。
* **问题与切口**: 这篇工作的价值在于把研究视角从“导航任务做成了没有”转向“决策在不完整、带风险信息时还是否可靠”。作者没有再造一个追分 benchmark，而是设计六个诊断任务，覆盖完整空间信息、不完整空间信息和安全相关信息三类场景，用来揭示 foundation model 在 embodied decision making 中被平均指标掩盖的失效。对机器人来说，这个切口尤其重要，因为看起来合理的输出并不等于可以安全执行的决定。
* **核心方法与证据**: 从摘录可见，论文与传统 VLN 等标准评测形成对照：后者擅长衡量路径误差、成功率和轨迹匹配，但不足以暴露模型在空间结构保持、上下文缺失推断和安全优先级权衡上的脆弱性。作者因此用六个诊断任务做 failure-focused analysis，并报告模型在未知单元、视觉空间对齐和安全线索竞争下出现不同类型的崩塌。需要保守的是，HTML 没给出具体模型名单与分项数值，因此现阶段更适合把它当成“评测框架与失效画像”来读。
* **正文要点**:
  - 论文核心目标不是刷新导航成绩，而是诊断 foundation model 的决策可靠性缺口。
  - 六个诊断任务覆盖完整信息、不完整信息和安全相关信息三类设置。
  - 作者明确对比了传统 VLN 聚合指标与 failure-focused analysis 的差异。
* **为什么值得跟**:
  - 这类工作能直接校正 embodied AI 里“高成功率等于可信”这一常见误判。
  - 它提供的不是又一个任务，而是一套更贴近部署风险的分析框架。
  - 对任何想把 LLM/VLM 接入机器人规划闭环的人来说，先做失败诊断比继续追平均分更重要。
* **风险 / 保留意见**:
  - 如果诊断任务与真实机器人执行链条脱节，它可能更像认知测验而不是部署测验。
  - 摘录没有展示模型覆盖范围与统计显著性，结论外推到不同 foundation model 仍需谨慎。
* **建议先看**: 先抓住作者为什么批评现有导航指标不够，再看六类诊断任务分别在揭示什么失败模式。真正值得学的是它的评测设计逻辑，而不只是某个模型输赢。
* **关键词**: `导航` `foundation model` `可靠性` `失败分析` `诊断评测`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 六个诊断任务之间是否能明确分离“空间表征失败”和“语言推理失败”两类误差来源？
  - 在安全相关设置里，模型失败主要来自忽视风险线索，还是来自空间结构本身先崩掉？
  - 这些诊断任务与真实机器人导航闭环中的可观测失效之间，是否建立了足够强的对应关系？
* **上传 PDF 后优先看**:
  - 任务设计章节中六个诊断任务的构造原则与目标能力映射
  - 实验章节里不同信息条件下的失效模式拆解
  - 讨论章节中对 VLN 标准指标局限性的分析与案例

## Watchlist

### [W1]. TAMEn: Tactile-Aware Manipulation Engine for Closed-Loop Data Collection in Contact-Rich Tasks [[HTML]](https://arxiv.org/html/2604.07335) [[PDF]](https://arxiv.org/pdf/2604.07335)
* **Paper ID**: `2604.07335`
* **Authors**: Longyan Wu, Jieji Ren, Chenghang Jiang, Junxi Zhou, Shijia Peng, Ran Huang, Guoying Gu, Li Chen, Hongyang Li
* **Author Priority**: Standard
* **为什么还值得留意**: TAMEn 进入 shortlist 的理由很充分：它把双臂接触丰富操作中的触觉、可执行性在线检查、AR 恢复遥操作和分层数据组织放进了同一个闭环数据采集系统里，这对 visuo-tactile manipulation 很有现实价值。之所以没有进入最终精选，是因为今天的主线更偏 VLA / world-model / failure-analysis 的通用基础件，而它更像一套面向特定接触任务的数据采集与恢复系统。另一个原因是摘录虽说明了任务套件与系统构成，但对核心学习算法和增益幅度的证据仍偏有限。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. Apple: Toward General Active Perception via Reinforcement Learning [[HTML]](https://arxiv.org/html/2505.06182) [[PDF]](https://arxiv.org/pdf/2505.06182)
* **Paper ID**: `2505.06182`
* **Authors**: Tim Schneider, Cristiana de Farias, Roberto Calandra, Liming Chen, Jan Peters
* **Author Priority**: Standard
* **为什么还值得留意**: APPLE 值得关注，因为它试图用统一的 RL 框架处理主动感知，并且覆盖了分类与回归、低维与高维触觉观测等不同任务设定。这条线和“感知为了行动服务”的长期主题一致，也能和未来的 VLA 主动探索能力形成连接。没有进最终精选，主要因为它离今天的核心焦点稍远，更偏通用主动感知 RL；同时提供的 HTML 摘录里方法细节相对稀薄，暂时不够支撑更高优先级。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. Exploring Conditions for Diffusion models in Robotic Control [[HTML]](https://arxiv.org/html/2510.15510) [[PDF]](https://arxiv.org/pdf/2510.15510)
* **Paper ID**: `2510.15510`
* **Authors**: Heeseong Shin, Byeongho Heo, Dongyoon Han, Seungryong Kim, Taekyung Kim
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇之所以进 watchlist，是因为它问了一个很有价值的问题：预训练文生图 diffusion 的条件到底怎样才能真正变成机器人控制里任务自适应的视觉表征，而不是在别的视觉任务上有效、到了控制里就失灵。它对“文本条件未必有效、视觉条件可能更关键”的判断，和具身表征学习的现实经验相当一致。没进最终精选，是因为摘录里更像一篇表示条件设计研究，离完整 VLA / world action model 主线还有一步，而且方法证据在当前材料中不够展开。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

### [W4]. LeLaR: The First In-Orbit Demonstration of an AI-Based Satellite Attitude Controller [[HTML]](https://arxiv.org/html/2512.19576) [[PDF]](https://arxiv.org/pdf/2512.19576)
* **Paper ID**: `2512.19576`
* **Authors**: Kirill Djebko, Tom Baumann, Erik Dilger, Frank Puppe, Sergio Montenegro
* **Author Priority**: Standard
* **为什么还值得留意**: LeLaR 进入 shortlist 的核心原因是它给出了一个极强的 sim2real 叙事：基于深度强化学习的姿态控制器实现了在轨演示，并且正面讨论了训练仿真与真实卫星行为之间的偏差。这个“真实部署优先于离线高分”的姿态非常值得机器人社区借鉴。之所以没有进最终精选，是因为应用域更偏航天控制，和今天以 VLA、操作与世界模型为中心的主题距离较远，可迁移性更多体现在方法精神而不是直接技术复用。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)
