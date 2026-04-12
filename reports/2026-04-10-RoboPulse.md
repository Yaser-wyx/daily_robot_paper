# RoboPulse | 2026-04-10

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 74 papers scanned · 10 shortlisted · 5 editor's picks

今天这组最终精选围绕两条主线收敛得很清楚：一条是用更可扩展的人类数据、主动感知和物理对齐仿真去解决机器人数据瓶颈，另一条是把时间建模重新带回 VLA 与机器人决策，补上长时程任务里最容易失真的“未来后果”建模。入选论文之所以成立，不只是因为话题热，而是它们分别在数据平台、采集系统、sim2real 数据引擎、视频生成式价值建模和运动中心世界模型这五个关键接口上给出了较完整的方法闭环与实验问题设定。VIP 作者里，Xiaolong Wang、Shuran Song、Danfei Xu、Cewu Lu、Jiangmiao Pang、Donglin Wang 这几条线尤其值得优先跟踪，因为他们分别卡在大规模人类数据、主动视觉采集、物理对齐仿真和长时程 VLA 的核心交叉点上。整体看，今天不是单点模型刷分的一天，而是“如何把可扩展数据、可解释中间表示和长时程控制真正接起来”的一天。

## 今日信号

- 今天最值得记住的研究信号是：VLA 的下一阶段竞争点正在从“静态感知到动作映射”转向“谁能更稳地建模时间、价值与未来运动”。
- 今天最值得记住的研究信号是：sim2real 在变形物体场景里开始从常见的随机化思路转向几何、动力学、动作三者共同对齐的物理落地路线。
- 今天最值得记住的研究信号是：真实机器人数据依然稀缺，但人类第一视角数据、主动视觉采集和生成式教师信号正在成为扩大监督来源的三种主流补口。

## Editor's Picks

### [1]. EgoVerse: An Egocentric Human Dataset for Robot Learning from Around the World [[VIP]] [[HTML]](https://arxiv.org/html/2604.07607) [[PDF]](https://arxiv.org/pdf/2604.07607) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.07607`
* **Authors**: Ryan Punamiya, Simar Kareer, Zeyi Liu, Josh Citron, Ri-Zhao Qiu, Xiongyi Cai, Alexey Gavryushin, Jiaqi Chen, Davide Liconti, Lawrence Y. Zhu, Patcharapong Aphiwetsa, Baoyu Li, Aniketh Cheluva, Pranav Kuppili, Yangcen Liu, Dhruv Patel, Aidan Gao, Hye-Young Chung, Ryan Co, Renee Zbizika, Jeff Liu, Xiaomeng Xu, Haoyu Xiong, Geng Chen, Sebastiano Oliani, Chenyu Yang, Xi Wang, James Fort, Richard Newcombe, Josh Gao, Jason Chong, Garrett Matsuda, Aseem Doriwala, Marc Pollefeys, Robert Katzschmann, Xiaolong Wang, Shuran Song, Judy Hoffman, Danfei Xu
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，它不是单纯再发一个数据集，而是在“人类第一视角数据如何真正服务机器人学习”上给出了平台化与跨机构协作的更完整答案。
* **问题与切口**: EgoVerse要解决的是机器人数据难以规模化采集的老问题，但切口不是再堆一批零散人类视频，而是把“采集、处理、访问、联合训练”做成一个可持续扩展的协作框架。它的新意在于把人类第一视角数据视为机器人学习的共享上游资源，并明确讨论了跨机构贡献、跨 embodiment 联训以及人机对齐数据在扩展中的作用，因此更像一个面向社区的数据基础设施方案，而不是一次性的 benchmark 发布。
* **核心方法与证据**: 从HTML摘录看，方法层面它采用共享编码器加浅层模态 stem 的 encoder-decoder 架构，把人类与机器人观测映射到共享 token 空间，再用 transformer 编码上下文，并以 flow matching 动作解码器输出动作序列。证据上，作者并未只停在离线分析，而是在四个代表性任务上做了 ID/OOD rollout，对比不同数据来源与场景多样性影响；同时正文明确强调，人类数据能带来提升，但要想有效扩展，仍需要与机器人数据对齐来“锚定”学习。
* **正文要点**:
  - 架构上共享第一视角 RGB stem，同时为机器人腕部相机与本体感觉保留独立 stem，以支持多 embodiment 联合训练。
  - 动作头采用 flow matching 解码思路，说明作者关注的是连续动作序列建模而非仅做离散行为克隆。
  - 实验设计明确区分 in-domain 与 out-of-domain rollout，且结论直接讨论了人机对齐与场景多样性各自的作用。
* **为什么值得跟**:
  - 这篇工作的真正价值在于把“人类数据可扩展、机器人数据可锚定”这件事从口号推进到可操作的平台层面。
  - 如果其协作式数据机制能持续增长，它可能成为未来人类到机器人迁移研究的重要公共底座。
  - 它也提醒研究者，扩大人类数据规模本身不够，关键在于如何设计跨 embodiment 的共享表示与对齐接口。
* **风险 / 保留意见**:
  - HTML摘录没有充分展开不同任务上的详细误差分解，因此目前更能确认方向有效，尚难精确判断收益主要来自数据规模、场景多样性还是模型设计。
  - 作为平台型工作，后续外部复现与长期维护质量会直接影响其学术影响力，这部分从当前摘录中还看不够清楚。
* **建议先看**: 先抓两条主线：一是平台层面如何组织跨机构人类数据，二是模型层面如何把人类与机器人观测对齐到统一动作学习接口。随后重点看作者关于“只加人类数据不够，还需要对齐机器人数据”的论证。
* **关键词**: `egocentric human data` `robot learning` `cross-embodiment` `flow matching` `data scaling`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 人类与机器人数据的对齐具体依赖哪些监督或时间同步假设，若对齐更弱时性能会如何退化？
  - 共享视觉 stem 与独立机器人 stem 的边界是如何确定的，是否存在更强或更弱共享带来的性能拐点？
  - 场景多样性提升带来的收益，和任务语义多样性提升带来的收益，作者是否在正文中做了可分离分析？
* **上传 PDF 后优先看**:
  - 方法章节里关于跨 embodiment 表示与动作解码器设计的部分。
  - 实验章节中人类数据、机器人数据与对齐设置的比较实验。
  - 附录或协议章节里 rollout 评分定义、任务细节与 OOD 设置说明。

### [2]. ActiveGlasses: Learning Manipulation with Active Vision from Ego-centric Human Demonstration [[VIP]] [[HTML]](https://arxiv.org/html/2604.08534) [[PDF]](https://arxiv.org/pdf/2604.08534) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.08534`
* **Authors**: Yanwen Zou, Chenyang Shi, Wenye Yu, Han Xue, Jun Lv, Ye Pan, Chuan Wen, Cewu Lu
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，它抓住了一个很少被认真处理的问题：人类演示里“看哪里”本身就是操控策略的一部分。
* **问题与切口**: ActiveGlasses试图把自然人类操作中的主动视觉行为直接带入机器人学习，而不是继续依赖手持设备或额外桥接器件。它把佩戴式双目相机作为唯一感知设备，让操作者用裸手完成任务，再把人类头部视角变化与物体操作轨迹一起变成机器人策略学习对象。相对已有从人类演示到机器人迁移的路线，它的核心新意不只是采集更轻量，而是明确把“视角调节”也当作可学习控制量纳入策略，而非把相机视角当固定外参。
* **核心方法与证据**: 方法上作者把任务拆成 pre-grasp、motion planning、termination 三阶段：抓取阶段用 AnyGrasp 或固定策略，运动阶段由于单个主动视觉相机导致 2D 视角不稳定，因此改用世界坐标系点云输入，并同步预测目标物体轨迹与头部运动。一个关键设计是不给操纵扩散头额外输入当前物体位姿，以减少记忆轨迹的捷径。证据上，实验围绕可扩展性、主动视觉价值、策略设计和跨 embodiment 零样本迁移四个问题展开，说明作者不是只验证单点成功率，而是在检验整套系统设定是否成立。
* **正文要点**:
  - 作者明确把头部运动预测作为策略输出之一，而不是把视角变化当采集噪声处理。
  - 为应对单主动视觉相机带来的空间不一致，策略输入选择世界坐标系点云而非直接图像平面特征。
  - 实验问题设置覆盖数据采集效率、固定相机对比、策略头设计以及跨平台零样本迁移。
* **为什么值得跟**:
  - 这篇工作把主动感知重新拉回机器人学习主问题，尤其适合需要视角搜索与精细放置的操作场景。
  - 如果这套采集方式足够稳，它能显著降低人类演示系统的穿戴与操作门槛，从而提升真实数据获取效率。
  - 它也提示未来 VLA 不应只学“手怎么动”，还应显式建模“传感器该怎么动”。
* **风险 / 保留意见**:
  - 当前摘录没有展开头部运动预测与操纵轨迹预测之间的耦合稳定性，因此两者是否会互相放大误差还需要看正文细节。
  - 系统依赖单相机点云与特定分阶段设计，若任务包含强遮挡或复杂接触，泛化边界需要更谨慎判断。
* **建议先看**: 建议先读任务分阶段设计，再看为什么作者坚持用世界系点云和双头预测。真正值得核查的是主动视觉到底贡献了多少，以及这种贡献是否独立于采集便利性。
* **关键词**: `active vision` `egocentric demonstration` `point cloud policy` `cross-embodiment` `manipulation`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 头部运动预测是独立优化还是与操纵目标共享时序表示，二者冲突时如何处理？
  - 去掉当前物体位姿输入后性能为何更好，正文是否证明模型确实避免了捷径而非损失必要状态信息？
  - 在跨 embodiment 零样本迁移中，不做 robot masking 依然成立的关键条件是什么？
* **上传 PDF 后优先看**:
  - 方法章节中三阶段任务分解与双输出策略结构。
  - 主动视觉与固定相机对比实验，以及单头/双头、绝对/相对表示的消融。
  - 跨 embodiment 迁移实验与失败案例分析。

### [3]. SIM1: Physics-Aligned Simulator as Zero-Shot Data Scaler in Deformable Worlds [[VIP]] [[HTML]](https://arxiv.org/html/2604.08544) [[PDF]](https://arxiv.org/pdf/2604.08544) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.08544`
* **Authors**: Yunsong Zhou, Hangxu Liu, Xuekun Jiang, Xing Shen, Yuanzhen Zhou, Hui Wang, Baole Fang, Yang Tian, Mulin Yu, Qiaojun Yu, Li Ma, Hengjie Li, Hanqing Wang, Jia Zeng, Jiangmiao Pang
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，它是今天最接近“把变形物体 sim2real 做成数据引擎”而不是单次技巧整合的一篇。
* **问题与切口**: SIM1聚焦一个长期被低估的痛点：在衣物等变形物体操作里，仿真之所以常常失效，不只是因为它是合成数据，而是因为它在几何、动力学和动作先验三个层面都没有真正贴住真实世界。作者提出的不是普通意义上的数据增强，而是一个 real-to-sim-to-real 数据引擎，试图把高精度场景数字化、软体动力学校准和动作生成统一起来，让纯仿真训练出来的策略也能作为真实等价的数据来源去用。
* **核心方法与证据**: HTML摘录给出的技术主线很完整：先用高精度扫描和对象导入建立 metric-accurate 数字场景，再在对齐仿真器中用形变稳定求解器与参数校准复现实验动力学，随后把仿真遥操作演示分解为动作片段，并通过 diffusion 合成与视觉随机化扩展训练数据。证据边界也比较清楚，实验主要回答三件事：纯仿真训练能否接近真实数据训练、仿真多样性能否提升 OOD 鲁棒性、以及合成数据扩展是否更高效。作者结论是支持零样本 sim-to-real，但这一判断仍应以具体任务范围理解。
* **正文要点**:
  - 作者明确采用 R2S2R 范式，强调不是单向从真到仿或从仿到真，而是贯通几何、动力学与动作三层对齐。
  - 方法中特别强调 deformation-stabilized solver 与参数校准基础设施，说明其核心卖点是物理一致性而非仅靠视觉随机化。
  - 实验问题围绕 S2R transfer、跨域泛化和数据扩展效率展开，且声明可用纯仿真训练策略做零样本迁移。
* **为什么值得跟**:
  - 在变形物体操作上，这篇工作比许多通用 sim2real 方法更直面根因，因为它把误差来源拆回到物理与几何层。
  - 如果其数据引擎思路可靠，未来变形操作不必完全依赖昂贵真实示教就能扩大训练分布。
  - 它也可能影响 world model 与 action model 研究，因为高保真模拟数据本身就是构建预测模型的重要前提。
* **风险 / 保留意见**:
  - 当前摘录虽给出零样本迁移结论，但任务集中在 garment folding，外推到更复杂拓扑变化或接触模式时仍需保守。
  - 物理对齐流程包含扫描、参数校准和求解器工程，复现门槛可能较高，不一定适合所有实验室快速部署。
* **建议先看**: 先看作者如何定义“仿真失效的根因”，再追 R2S2R 三个阶段如何分别补几何、动力学和动作分布。最后重点核查纯仿真训练与真实训练的对比边界。
* **关键词**: `sim2real` `deformable manipulation` `physics alignment` `garment folding` `synthetic data scaling`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 几何对齐、动力学校准和动作合成三部分里，哪一部分对零样本迁移最关键，正文是否做了分离消融？
  - 动作片段分解再做 diffusion 合成，相比直接学习长时序策略究竟带来了什么优势或偏差？
  - OOD 鲁棒性的提升主要来自视觉随机化还是来自物理一致的状态覆盖扩展？
* **上传 PDF 后优先看**:
  - 场景数字化与物理参数校准章节。
  - 纯仿真训练、真实训练与混合设置的主结果对比。
  - 跨域泛化与数据规模扩展曲线相关实验。

### [4]. ViVa: A Video-Generative Value Model for Robot Reinforcement Learning [[HTML]](https://arxiv.org/html/2604.08168) [[PDF]](https://arxiv.org/pdf/2604.08168) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.08168`
* **Authors**: Jindi Lv, Hao Li, Jie Li, Yifei Nie, Fankun Kong, Yang Wang, Xiaofeng Wang, Zheng Zhu, Chaojun Ni, Qiuping Deng, Hengtao Li, Jiancheng Lv, Guan Huang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它提供了一个很有代表性的方向：把视频生成模型的时序先验直接改造成机器人 RL 所需的价值模型。
* **问题与切口**: ViVa处理的是 VLA 在真实部署里常见但常被弱化的问题：当前观测并不足以判断任务是否正在朝成功推进，而传统基于 VLM 的价值模型又往往缺乏长时序动态理解。作者的切口不是再做一个更强判别器，而是把预训练视频生成器改造成价值估计器，让模型在看当前观测和本体状态时，同时预测未来本体变化与当前状态价值。相较常规 value head，这种设计的核心新意在于把“能否想象未来动作后果”作为价值可靠性的来源。
* **核心方法与证据**: 从HTML摘录可确认的方法主张是：ViVa以当前观测和 proprioception 为输入，联合预测未来 proprioception 与标量价值，借用预训练视频生成骨干的时空先验来得到更具时间感的价值表征。证据上，论文在三类真实世界双臂任务上训练和评估，包括衬衫折叠、盒子装配和卷纸整理，并特别强调长时程、部分可观测和延迟反馈场景。结论层面，作者声称在 box assembly 上显著优于先前方法，并通过三任务定性分析说明其价值信号更稳定；但从摘录看，定量细节与 RL 集成方式仍需在正文中核查。
* **正文要点**:
  - 核心思想是把预训练视频生成器的时空先验转译成价值估计能力，而不是单独训练静态评分器。
  - 模型不仅输出标量价值，还联合预测未来本体状态，说明作者把 embodiment dynamics 作为价值锚点。
  - 实验任务都具有较长时间跨度与多阶段结构，契合其针对 delayed feedback 的设定。
* **为什么值得跟**:
  - 这篇工作把 world model 风格的未来预测与 RL 价值函数重新接上，对机器人长时程决策很有启发性。
  - 如果价值确实能从生成式时序先验中获益，它可能成为 VLA 与 RL 结合的一条更自然路径。
  - 它也说明未来机器人基础模型未必只靠动作监督提升，任务进度建模本身就是关键能力层。
* **风险 / 保留意见**:
  - HTML摘录没有清楚展开其 RL 训练闭环、价值监督来源与稳定性细节，因此方法是否易于迁移到其他任务还需谨慎判断。
  - 论文当前更强的证据似乎集中在少数真实任务与定性分析，泛化范围和计算代价边界还不够透明。
* **建议先看**: 先抓住一个核心问题：作者究竟如何把视频生成骨干转成价值模型。然后重点查它在 box assembly 这类长时程任务上为什么比传统 VLM value model 更稳。
* **关键词**: `video-generative value model` `robot RL` `VLA` `temporal dynamics` `long-horizon manipulation`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 价值监督是如何构造的，联合预测未来 proprioception 是否直接改善了 credit assignment？
  - 视频生成先验在训练时是冻结、微调还是部分适配，这对稳定性和样本效率有什么影响？
  - 作者报告的价值优势是否主要出现在长时程失败恢复场景，而不是短时单步可见任务？
* **上传 PDF 后优先看**:
  - 方法章节中视频生成骨干到价值模型的改造方式。
  - 真实机器人三任务实验，尤其是长时程失败/纠错案例。
  - 与基于 VLM 的价值模型比较及消融分析。

### [5]. HiF-VLA: Hindsight, Insight and Foresight through Motion Representation for Vision-Language-Action Models [[VIP]] [[HTML]](https://arxiv.org/html/2512.09928) [[PDF]](https://arxiv.org/pdf/2512.09928) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2512.09928`
* **Authors**: Minghui Lin, Pengxiang Ding, Shu Wang, Zifeng Zhuang, Yang Liu, Xinyang Tong, Wenxuan Song, Shangke Lyu, Siteng Huang, Donglin Wang
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，它是今天最清晰把“运动表示”提升为 VLA 时序建模核心中介的一篇。
* **问题与切口**: HiF-VLA针对多数 VLA 只看当前观测、因此在长时程任务里出现 temporal myopia 的问题，提出以运动而非原始像素历史作为时序上下文主表示。作者把 motion 看成更紧凑、也更贴近世界动态的中间变量，用 hindsight、insight、foresight 三类线索扩展动作执行前的时间感受野。相对已有简单拼历史帧或堆更长上下文窗口的路线，它的新意在于把“历史变化”和“未来变化”都压缩进低维结构化运动向量，再统一接入 VLA。
* **核心方法与证据**: 根据HTML摘录，HiF-VLA建立在 vanilla VLA 之上：训练时输入历史信息先验，并联合预测未来若干步 motion 与对应动作；推理时 motion 解码可以按下游需求选择性省略。实验问题设计也比较完整，既看在 LIBERO-Long 与 CALVIN ABC-D 这类长时程 benchmark 上的整体表现，也专门检查冗余效率、随时间尺度增长的推理可扩展性、组件消融以及真实机器人可行性。正文结论强调的是，以低维结构化运动向量实现双向时间扩展，从而改善时序一致性与因果连贯性。
* **正文要点**:
  - 作者把 motion 明确界定为比像素历史更紧凑且更有信息密度的时序上下文表示。
  - 训练阶段联合做未来 motion 预测与动作预测，说明它更接近轻量 world model 与 policy 的耦合框架。
  - 实验问题不只关心成功率，还把时域增长下的推理效率与真实机器人部署单独拎出来分析。
* **为什么值得跟**:
  - 它为 VLA 长时程推理提供了一个很有工程吸引力的折中方案，不必完全转向重型视频 world model。
  - 如果 motion 表示确实足够稳定，它可能成为 VLA、world model 与 action model 之间的统一接口。
  - Donglin Wang 这条线值得跟，因为它抓的是长时程机器人系统里最难补的时间一致性问题。
* **风险 / 保留意见**:
  - 当前摘录没有解释 motion 表示在强遮挡、接触突变或视觉错觉场景中的脆弱性，因此鲁棒性边界需要看更多正文证据。
  - 推理时可省略 motion 解码虽提高灵活性，但也可能导致训练与部署目标不完全一致，这一点需要核查。
* **建议先看**: 优先读作者如何定义 hindsight、insight、foresight 以及它们如何共同扩展 temporal receptive field。其次重点看长时程 benchmark 上的效率与性能是否同时成立。
* **关键词**: `VLA` `motion representation` `world model` `long-horizon manipulation` `temporal reasoning`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - motion 向量相对直接堆叠历史图像，究竟在哪些任务类型上优势最大，正文是否有任务级拆分？
  - 联合预测未来 motion 与动作时，motion 分支是否主要提供表示约束还是直接改善规划能力？
  - 推理阶段可选省略 motion 解码会不会削弱模型在长时程任务中的稳定收益？
* **上传 PDF 后优先看**:
  - 方法章节中 motion-centric world model 与 HiF 三线索定义。
  - LIBERO-Long 与 CALVIN ABC-D 的主结果和时域扩展实验。
  - 真实机器人实验与关键消融章节。

## Watchlist

### [W1]. UniLACT: Depth-Aware RGB Latent Action Learning for Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2602.20231) [[PDF]](https://arxiv.org/pdf/2602.20231)
* **Paper ID**: `2602.20231`
* **Authors**: Manish Kumar Govind, Dominick Reilly, Pu Wang, Srijan Das
* **Author Priority**: Standard
* **为什么还值得留意**: UniLACT进入 shortlist 的原因很直接：它把 latent action 预训练从纯 RGB 推向 RGB+depth 的几何感知版本，切口贴近 VLA 数据效率与空间先验这两个核心问题。没有进入最终精选，主要是因为从当前摘录看，贡献更像对现有 latent action 预训练范式的稳健增强，而不是对 VLA 时序、world modeling 或 sim2real 路线的结构性推进。若后续 PDF 里对真实任务收益和几何先验来源有更强证据，它仍值得回捞。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. WorldMAP: Bootstrapping Vision-Language Navigation Trajectory Prediction with Generative World Models [[HTML]](https://arxiv.org/html/2604.07957) [[PDF]](https://arxiv.org/pdf/2604.07957)
* **Paper ID**: `2604.07957`
* **Authors**: Hongjin Chen, Shangyun Jiang, Tonghua Su, Chen Gao, Xinlei Chen, Yong Li, Zhibo Chen
* **Author Priority**: Standard
* **为什么还值得留意**: WorldMAP值得关注，因为它把生成式 world model 产生的未来视频转成可规划、可监督的导航轨迹教师信号，这个“teacher 化”思路很有启发性。之所以停在 watchlist，是因为它更偏视觉语言导航而非今天主线里的机器人操作 VLA，而且当前证据也明确是“有边界的支持结论”，说明作者自己对外推保持克制。若后续想补 world model 在 embodied planning 中的中间表示设计，这篇可以重点看。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. BLaDA: Bridging Language to Functional Dexterous Actions within 3DGS Fields [[HTML]](https://arxiv.org/html/2604.08410) [[PDF]](https://arxiv.org/pdf/2604.08410)
* **Paper ID**: `2604.08410`
* **Authors**: Fan Yang, Wenrui Chen, Guorun Yan, Ruize Liao, Wanjun Jia, Dongsheng Luo, Kailun Yang, Zhiyong Li, Yaonan Wang
* **Author Priority**: Standard
* **为什么还值得留意**: BLaDA之所以进 shortlist，在于它把语言、3DGS 场、功能接触点和灵巧手执行串成了一个可解释零样本链路，这对 dexterous manipulation 很有吸引力。没有进最终精选，是因为它更偏模块化功能抓取与开放词汇 grounding，而不是今天最核心的 VLA 时间建模、sim2real 数据扩展或 RL 结合主线。若 PDF 中对 TriLocation 与 KGT3D+ 的接口做得足够扎实，它会是一篇很好的“解释型系统”补充阅读。
* **证据来源**: arXiv HTML (Introduction, Experiments)

### [W4]. HEX: Humanoid-Aligned Experts for Cross-Embodiment Whole-Body Manipulation [[HTML]](https://arxiv.org/html/2604.07993) [[PDF]](https://arxiv.org/pdf/2604.07993)
* **Paper ID**: `2604.07993`
* **Authors**: Shuanghao Bai, Meng Li, Xinyuan Lv, Jiawei Wang, Xinhua Wang, Fei Liao, Chengkai Hou, Langzhe Gu, Wanqi Zhou, Kun Wu, Ziluo Ding, Zhiyuan Xu, Lei Sun, Shanghang Zhang, Zhengping Che, Jian Tang, Badong Chen
* **Author Priority**: Standard
* **为什么还值得留意**: HEX具备进入讨论区的资格，因为它正面处理了 humanoid whole-body manipulation 中最难的跨肢体耦合与高维本体状态建模问题，而且“高层 VLA + 低层 RL 控制器”的结构也很符合落地需求。最终没进精选，主要是它更像 humanoid 全身操作专线，而不是今天更广义的 VLA/world model/sim2real 交叉主战场；另外从摘录看，其主要亮点仍集中在 state-centric 设计与系统集成。后续若你要补 humanoid 方向，这篇优先级会升高。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W5]. Sumo: Dynamic and Generalizable Whole-Body Loco-Manipulation [[HTML]](https://arxiv.org/html/2604.08508) [[PDF]](https://arxiv.org/pdf/2604.08508)
* **Paper ID**: `2604.08508`
* **Authors**: John Z. Zhang, Maks Sorokin, Jan Brüdigam, Brandon Hung, Stephen Phillips, Dmitry Yershov, Farzad Niroui, Tong Zhao, Leonor Fermoselle, Xinghao Zhu, Chao Cao, Duy Ta, Tao Pang, Jiuguang Wang, Preston Culbertson, Zachary Manchester, Simon Le Cléac'h
* **Author Priority**: Standard
* **为什么还值得留意**: Sumo进入 watchlist，是因为它展示了一条很务实的路线：用预训练全身控制策略配合测试时采样规划，实现动态且可泛化的 whole-body loco-manipulation。没有进入最终精选，原因是它虽然属于 sim2real 和 whole-body manipulation 重要工作，但与今天重点关注的 VLA、world model 和 RL+VLA 主线耦合不够紧，且当前摘录主要展示能力而非更深的表示层创新。若后续关注动态接触与 test-time planning 的组合，这篇很值得补读。
* **证据来源**: arXiv HTML (Introduction, Experiments)
