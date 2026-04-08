# RoboPulse | 2026-04-08

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 74 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线很清楚：VLA/WAM 研究正在从“能不能做出来”转向“部署时能不能适应、推理能不能足够快、评测和安全能不能跟上”。最终精选里，TT-VLA、Fast-dVLA 和 A1 代表了部署期适应与低延迟落地的三条不同技术路径；RoboPlayground 和 DAERT 则把评测与安全从附属问题抬升为一等研究对象。Action Images 之所以入选，是因为它把动作直接搬进视频像素空间，给 world action model 提供了更统一的表征接口。VIP 作者里，今天最值得优先跟踪的是 Donglin Wang 参与的 Fast-dVLA 和 Dieter Fox 参与的 RoboPlayground，它们分别对应实时控制栈与语言化物理评测基建两条高价值主线。

## 今日信号

- 测试时适应、预算感知推理与解码加速，正在成为 VLA 从 benchmark 模型走向可部署系统的共同门槛。
- 评测不再只是固定任务成功率，语言驱动任务编排与多样化 red teaming 正在把鲁棒性和安全性前移到研究入口。
- World model / WAM 的一个明显趋势，是把动作重新表述为与视频表征对齐的统一空间，以更直接复用生成式视频主干的先验。

## Editor's Picks

### [1]. On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning [[HTML]](https://arxiv.org/html/2601.06748) [[PDF]](https://arxiv.org/pdf/2601.06748) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2601.06748`
* **Authors**: Changyu Liu, Yiyang Liu, Taowen Wang, Qiao Zhuang, James Chenhao Liang, Wenhao Yang, Renjing Xu, Qifan Wang, Dongfang Liu, Cheng Han
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为它把 VLA 从训练期优化推进到部署期在线适应，直接对准真实落地时“环境一变就失灵”的核心痛点。
* **问题与切口**: 这篇工作针对现有 VLA 在固定训练分布内表现不错、但一遇到动态环境变化和域偏移就迅速失灵的问题，提出把强化学习直接搬到测试阶段，让机器人在执行任务时边交互边修正策略。相较于常见的监督微调或训练期 RL 路线，它的关键新意不是再造一个更大的 VLA，而是把部署时适应做成框架能力，希望同一底座在未见执行扰动、视觉变化和语义变化下仍能维持有效操作；这更像面向真实场景的自适应补丁层。
* **核心方法与证据**: 正文给出的技术主线是先用 POMDP 形式刻画语言条件操控，再在 PPO 与 VLA 预备知识之上构建 TT-VLA，使策略可在测试阶段做 on-the-fly policy adaptation。实验部分明确覆盖仿真与真实机器人，并沿 Execution、Vision、Semantics 三类未见泛化扰动评估，还额外加入中途物体重定位这类过程扰动，并声称跨多种 VLA backbone 都有效。证据边界在于摘录未提供奖励设计、在线更新成本与真实机安全保护细节，因此其稳定性仍需保守判断。
* **正文要点**:
  - 论文将语言条件操控建模为带多模态观测与指令输入的 POMDP，并以此承接测试时 RL 更新。
  - 仿真评测沿 Execution、Vision、Semantics 三类未见泛化维度展开，还加入了 mid-episode object repositioning 这类过程扰动。
  - 作者明确声称方法同时在仿真与真实机器人任务上评估，并且可跨不同 VLA backbone 提升表现。
* **为什么值得跟**:
  - 它把 VLA 研究重心从“训练后一次性部署”推进到“部署中持续适应”。
  - 如果在线更新足够稳定，机器人面对任务中途变化时不必依赖人工重新微调。
  - 这种与底座相对解耦的适应层思路，可能比重新训练专用模型更容易迁移到现有系统。
* **风险 / 保留意见**:
  - 测试时 RL 天生带来样本效率与安全性问题，若奖励或探索设计不稳，适应过程可能反而破坏原策略。
  - HTML 摘录没有给出在线更新预算、延迟与失败恢复细节，实际部署成本和鲁棒性仍待核查。
* **建议先看**: 先看方法部分如何把 PPO 嵌入 VLA 测试阶段，再对照实验里 Execution、Vision、Semantics 三类扰动的设置。真正的判断点不只是是否提升成功率，而是在线适应是否足够稳、快、且可跨骨干复用。
* **关键词**: `VLA` `test-time reinforcement learning` `online adaptation` `generalization` `robot manipulation`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 测试时 RL 的奖励信号来自环境成功反馈、稠密 shaping，还是某种自监督代理目标？
  - 在线更新作用于全部 VLA 参数、动作头，还是只更新小规模适配模块？
  - 真实机器人实验中，探索受到了哪些安全约束，失败后又如何避免灾难性遗忘？
* **上传 PDF 后优先看**:
  - 测试时强化学习框架与理论分析章节
  - 未见任务中 Execution、Vision、Semantics 扰动实验设置
  - 真实机器人评测与跨 backbone 泛化结果

### [2]. Fast-dVLA: Accelerating Discrete Diffusion VLA to Real-Time Performance [[VIP]] [[HTML]](https://arxiv.org/html/2603.25661) [[PDF]](https://arxiv.org/pdf/2603.25661) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.25661`
* **Authors**: Wenxuan Song, Jiayi Chen, Shuai Chen, Jingbo Wang, Pengxiang Ding, Han Zhao, Yikai Qin, Xinhu Zheng, Donglin Wang, Yan Wang, Haoang Li
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，因为它直击 dVLA 最大的部署瓶颈之一：推理太慢，而且来自 Donglin Wang 这条核心作者线索，方法和系统价值都高。
* **问题与切口**: 这篇论文直击离散扩散式 VLA 最现实的短板之一：推理慢，难以走向在线控制。作者并不是简单减少去噪步数，而是先从正文观察中指出，代表性 dVLA 即便采用双向注意力，在全局上仍呈现隐含的块级从左到右解码倾向，再据此重构推理机制。相较于一般的推理加速技巧，它把块级结构、缓存复用和并行调度统一起来，目标是把 dVLA 从研究原型推进到更接近实时部署的系统形态。
* **核心方法与证据**: 方法主线包括四层设计：先可视化不同位置在去噪过程中的解码频率，提炼出块级 AR 动机；再用块级注意力让 KV cache 得以跨迭代复用；随后通过 diffusion forcing 支持不同噪声级别的块同时解码；训练端再用从预训练双向 dVLA 出发的非对称蒸馏配合推理时的块间并行调度。证据层面，实验围绕五个研究问题展开，覆盖 Dream-VLA、DD-VLA、UD-VLA、真实机器人、训练效率与超参数，但摘录未给出关键速度数值与精度代价。
* **正文要点**:
  - 作者先可视化代表性 dVLA 在去噪过程中不同位置的解码频率，观察到全局上隐含的左到右块级解码模式。
  - 方法由块级注意力、diffusion forcing、非对称蒸馏和块间并行解码调度组成，目标是复用 KV cache 并平衡速度与可靠性。
  - 实验围绕五个研究问题展开，覆盖多种 dVLA 架构、仿真与真实机器人任务、训练效率和超参数选择。
* **为什么值得跟**:
  - 它为离散扩散式 VLA 提供了更现实的实时部署路径。
  - 这项工作说明 bidirectional dVLA 并非完全无结构，可挖掘出可缓存、可并行的时序偏置。
  - 如果速度损失控制得当，dVLA 有机会在工程上重新与 flow-matching VLA 竞争。
* **风险 / 保留意见**:
  - 摘录里缺少具体延迟、吞吐与精度下降幅度，真实的性能/速度权衡仍需看完整结果。
  - 提供内容中的摘要与正文主线存在不完全一致之处，上传 PDF 后应优先核对任务定义与贡献描述是否对齐。
* **建议先看**: 先看 3.1 的动机观察是否真的足以支撑块级 AR 假设，再顺着 3.2 到 3.4 看缓存复用、并行解码和蒸馏如何闭环。读实验时重点不是单一成功率，而是速度收益是否跨 Dream-VLA、DD-VLA、UD-VLA 稳定成立。
* **关键词**: `dVLA` `inference acceleration` `block-wise decoding` `KV cache reuse` `diffusion forcing`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 块级解码假设在不同任务长度和动作离散化粒度下是否仍然成立？
  - inter-block parallel schedule 如何控制早期块错误对后续块的级联影响？
  - 非对称蒸馏是否只迁移解码行为，还是也改变了原 bidirectional dVLA 的策略分布？
* **上传 PDF 后优先看**:
  - 解码频率可视化与块级 AR 动机分析
  - 块级注意力、diffusion forcing 与蒸馏设计章节
  - 速度/性能 trade-off、真实机器人与训练效率实验

### [3]. RoboPlayground: Democratizing Robotic Evaluation through Structured Physical Domains [[VIP]] [[HTML]](https://arxiv.org/html/2604.05226) [[PDF]](https://arxiv.org/pdf/2604.05226) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.05226`
* **Authors**: Yi Ru Wang, Carter Ung, Evan Gubarev, Christopher Tan, Siddhartha Srinivasa, Dieter Fox
* **Author Priority**: Extended VIP
* **一句话结论**: 值得优先看，因为它不是再做一个 policy，而是在重写机器人评测范式，尤其适合 VLA/WAM 时代的语言化能力审查。
* **问题与切口**: 这篇工作把机器人操控评测从少数专家预先写好的固定 benchmark，转向用户可通过自然语言持续编排的结构化物理任务域。它解决的不是模型怎么学，而是谁能定义任务、约束和成功，以及这些定义如何被执行和复现。核心新意在于把自然语言请求编译为带资产定义、初始化分布和成功谓词的任务规范，使一条指令不只生成一个测试点，而是生成一族可比较、可回溯的相关任务，这比传统一次性 benchmark 更适合检验策略对连续语义编辑的响应。
* **核心方法与证据**: 摘录暴露出的关键机制是一个带任务历史的版本化编排流程：SteeringRouter 先做意图分类，再检测对象或版本回指、搜索历史快照，并设置不同的保留标记，以决定新请求是微调、扩展、改写还是重起任务。系统把语言请求落到显式资产、初始化分布与 success predicates 上，强调可执行性和可比性。证据边界在于 HTML 没有给出编译失败率、用户间一致性或覆盖度的系统量化，因此它更像很强的评测基础设施提案，具体可靠性仍待细查。
* **正文要点**:
  - 论文把用户请求分成 Tweak、Extend、Modify、Pivot、Fresh 五类，以决定对当前或历史任务版本的继承方式。
  - 路由阶段会结合对象引用、版本引用、加法语言和任务历史快照做语义匹配，而不是只做一次性文本解析。
  - 每条自然语言指令会被编译成包含资产定义、初始化分布和成功谓词的结构化任务规范。
* **为什么值得跟**:
  - 它把评测设计权从少数 benchmark 作者手里部分释放给更广泛的研究与应用用户。
  - 对 VLA 而言，真正的鲁棒性往往体现在约束微调和目标重述下是否仍能稳定执行。
  - 这种可执行、可回溯的任务族设计，比单点任务成功率更接近真实部署中的需求沟通过程。
* **风险 / 保留意见**:
  - 如果自然语言到任务规范的编译链条不稳，评测噪声可能来自系统本身而非被测策略。
  - 摘录未给出用户研究或大规模一致性验证，民主化评测的可重复性仍需实证支撑。
* **建议先看**: 先看系统如何把语言请求变成显式 success predicates，再看版本化路由如何处理连续修改和回指。研究者最该判断的是：它到底是在做一个新 benchmark，还是在提供一种更通用的评测编排接口。
* **关键词**: `robot evaluation` `structured physical domains` `language-driven tasks` `task compilation` `benchmarking`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)
* **读 PDF 先核查**:
  - 自然语言编译出的 success predicate 与人工手写判定相比有多大偏差？
  - 版本路由在多轮修改后会不会积累语义漂移，导致后续任务定义失真？
  - 不同用户对同一任务意图的描述差异，系统能否稳定收敛到可比较的任务族？
* **上传 PDF 后优先看**:
  - 语言到任务规范的编译与 success predicate 设计
  - SteeringRouter 的多轮版本选择与快照检索机制
  - 评测案例、失败样例与可重复性分析

### [4]. Uncovering Linguistic Fragility in Vision-Language-Action Models via Diversity-Aware Red Teaming [[HTML]](https://arxiv.org/html/2604.05595) [[PDF]](https://arxiv.org/pdf/2604.05595) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.05595`
* **Authors**: Baoshun Tong, Haoran He, Ling Pan, Yang Liu, Liang Lin
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为它把 VLA 的语言脆弱性做成了可系统搜索的问题，而且用 diversity-aware RL 避开了自动红队常见的模式坍缩。
* **问题与切口**: 这篇论文聚焦一个常被低估却很可能在真实部署中出事的问题：VLA 对语言细微变化、重述指令和无关上下文的脆弱性。作者没有停留在手工构造 prompt，而是把 embodied red teaming 形式化为强化学习问题，并显式把多样性放进目标函数，试图系统性挖出一批语义仍然合理、但足以诱发执行失败的对抗指令。相较于只追求单一最强攻击的做法，它更强调覆盖更多失效模式。
* **核心方法与证据**: 方法上，DAERT 将攻击指令生成建模为最大化失败奖励同时保持策略熵的 RL 优化，以缓解标准 RL 攻击者常见的 mode collapse。实验里目标 VLA 保持冻结，攻击器使用视觉语言模型生成指令，主要在 LIBERO 上训练，再直接迁移到 CALVIN 与 SimplerEnv 做 train-once, transfer-everywhere 式泛化评估。证据边界是摘录没有展开奖励函数、语义一致性约束和真实物理风险验证，因此目前更像鲁棒性审计框架，而不是已经闭环的安全防护方案。
* **正文要点**:
  - 论文明确指出现有 VLA 会对改写指令和无关上下文表现出显著 linguistic fragility。
  - 作者把 embodied red teaming 视为 RL 问题，并在目标中加入熵项以鼓励攻击指令分布多样化。
  - 攻击器在 LIBERO 上训练后，直接迁移到 CALVIN 和 SimplerEnv，强调 train-once, transfer-everywhere 的跨域设置。
* **为什么值得跟**:
  - 它把“语言鲁棒性”从定性担忧变成可系统搜索的失效面。
  - 多样化攻击比单一 prompt jailbreak 更接近真实人机交互中的长尾表达。
  - 这类工具可作为 VLA 上线前的压力测试层，而不是等事故发生后再补救。
* **风险 / 保留意见**:
  - 如果语义一致性约束不够强，攻击成功可能部分来自任务被偷偷改写，而非真正的语言脆弱性。
  - 摘录没有展示真实机器人闭环验证，仿真中的失败模式未必等价于物理世界风险。
* **建议先看**: 先看 4.1 和 4.2 里 RL 目标如何同时追求高攻击率与高多样性，再检查 5.1 的跨基准迁移是否真的证明了攻击策略具有可转移性。判断重点是它发现的是“语言脆弱性”，还是更一般的 benchmark prompt exploit。
* **关键词**: `VLA safety` `red teaming` `linguistic robustness` `reinforcement learning` `diversity`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 奖励函数如何区分“合法改写导致模型失败”和“语义已偏离原任务”的伪攻击？
  - 熵正则或多样性机制是否真的带来新的失效类型，而不只是表面上的措辞变化？
  - 训练在 LIBERO 上的攻击器迁移到 CALVIN/SimplerEnv 时，成功模式是否保持一致？
* **上传 PDF 后优先看**:
  - embodied red teaming 的 RL 目标与多样性机制
  - 语义一致性约束与攻击样例类型分析
  - 跨基准迁移实验与失败案例统计

### [5]. A1: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model [[HTML]](https://arxiv.org/html/2604.05672) [[PDF]](https://arxiv.org/pdf/2604.05672) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.05672`
* **Authors**: Kaidong Zhang, Jian Zhang, Rongtao Xu, Yu Sun, Shuoshuo Xue, Youpeng Wen, Xiaoyu Guo, Minghao Guo, Weijia Liufu, Liu Zihou, Kangyi Ji, Yangsong Zhang, Jiarun Zhu, Jingzhi Liu, Zihang Li, Ruiyi Chen, Meng Cao, Jingming Zhang, Shen Zhao, Xiaojun Chang, Feng Zheng, Ivan Laptev, Xiaodan Liang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为它把“开源透明 + 低成本部署 + 自适应加速”打包成一条完整工程路线，适合判断 VLA 的实用化边界。
* **问题与切口**: 这篇工作直击 VLA 落地时最现实的成本问题：大 VLM 主干加扩散或 flow 动作头让实时控制在普通硬件上过于昂贵。A1 提出一个完全开源、强调透明性的自适应截断式 VLA 框架，不只释放训练代码、数据处理和评测脚本，也把优化目标从单个模型模块扩展到整条推理流水线。它的核心卖点不是单点刷分，而是在尽量不牺牲操控成功的前提下，把吞吐、延迟和复现门槛一起拉回到更可部署的区间。
* **核心方法与证据**: 从 HTML 摘录可见，方法主线包括利用预训练 VLM 提供的 affordance priors 进行动作生成，并引入 budget-aware adaptive inference，在全流程层面同时加速视觉语言理解与动作预测，而不是只压缩 VLM 本身。实验覆盖 LIBERO、VLABench 以及四类真实机器人任务，并单独安排仿真、真实机与消融章节。证据边界在于摘录没有说明 truncated 究竟截断哪些计算路径、预算信号来自哪里，因此效率收益的来源和稳健性仍需上传 PDF 后核查。
* **正文要点**:
  - 论文强调完整开源训练栈，包括训练代码、数据处理流程、中间检查点和评测脚本，以提升端到端复现性。
  - 方法不是只压缩 VLM，而是提出 budget-aware adaptive inference，联合优化整条推理流水线。
  - 实验同时覆盖 LIBERO、VLABench 与四类真实机器人任务，表明作者把部署可用性作为核心卖点。
* **为什么值得跟**:
  - 它回应了当前 VLA 社区一个核心矛盾：泛化能力上去后，硬件与延迟成本却常常让系统难以落地。
  - 完整开源比很多只放 checkpoint 的工作更有基础设施意义。
  - 如果自适应截断足够稳定，VLA 更有机会进入资源受限的真实机器人平台。
* **风险 / 保留意见**:
  - 自适应截断如果调度不稳，可能在复杂任务上造成不可预期的精度退化或时延抖动。
  - 摘录未给出不同硬件、不同预算下的具体收益曲线，工程可迁移性仍需验证。
* **建议先看**: 先看方法里 truncated 与 adaptive inference 的定义边界，再对照实验核查效率收益是否来自合理的系统设计而不是缩小任务难度。研究者最该盯的是开源复现承诺是否真正覆盖训练到评测全链路。
* **关键词**: `open-source VLA` `adaptive inference` `efficient deployment` `truncated VLA` `robot manipulation`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 截断发生在视觉 token、语言上下文、动作解码步数，还是多处联合裁剪？
  - budget-aware 调度依赖哪些在线信号，是否会对不同任务类型产生系统性偏差？
  - 开源训练栈是否足以让第三方在不同机器人形态上重现实验结论？
* **上传 PDF 后优先看**:
  - adaptive truncated inference 的算法定义与预算控制
  - 仿真与真实机器人上的效率/性能对比
  - 开源训练栈、数据处理与复现实验说明

### [6]. Action Images: End-to-End Policy Learning via Multiview Video Generation [[HTML]](https://arxiv.org/html/2604.06168) [[PDF]](https://arxiv.org/pdf/2604.06168) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.06168`
* **Authors**: Haoyu Zhen, Zixian Gao, Qiao Sun, Yilin Zhao, Yuncong Yang, Yilun Du, Tsun-Hsuan Wang, Yi-Ling Qiao, Chuang Gan
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为它把 world action model 的动作表示直接搬进视频像素空间，可能是统一 world model 与 policy learning 的更干净路线。
* **问题与切口**: 这篇论文瞄准 world model 路线里的一个根问题：视频预测能力强，并不自动等于策略泛化强，关键瓶颈常常是动作表示仍与视频主干脱节。Action Images 的核心切口是把 7-DoF 机器人控制翻译成可解释的多视角 action images / videos，让动作和观察共享同一视频空间表征。相较于外挂 policy head 或低维 action token 的路线，它试图让预训练视频模型本体直接承担零样本策略职责。
* **核心方法与证据**: 方法由三步组成：先把连续控制转换为多视角 action videos，再将预测到的 action images 解码回连续动作，最后训练统一的 world-action model 同时生成未来观察与动作视频。主要评测设置是文本控制的动作与视频联合生成，并在 multi-view、one-trial、open-loop 条件下比较多个 policy 与 WAM 基线，刻意让结果更多反映表征本身的泛化质量。证据边界在于摘录只说明解码存在 minor information loss，未给出误差结构和闭环重规划能力，因此长期控制稳定性还不能高估。
* **正文要点**:
  - 作者明确批评现有 WAM 常依赖单独 action module 或非像素对齐动作表示，难以充分复用视频主干知识。
  - 核心表示是将 7-DoF 控制转成多视角 action images，使 observation 与 action 在统一视频空间中联合建模。
  - 主评测采用多视角、单次前向预测的 open-loop 设置，刻意放大表示本身的泛化质量而非在线重规划能力。
* **为什么值得跟**:
  - 它为 world model 到 policy 的衔接提供了比“视频主干加外挂动作头”更统一的方案。
  - 像素对齐动作表示可能更容易跨视角、跨环境迁移。
  - 如果零样本策略能力成立，WAM 的预训练价值会比单纯视频预测更直接地转化为可执行控制。
* **风险 / 保留意见**:
  - open-loop 单次预测设定很苛刻，但也可能与真实机器人依赖闭环纠错的部署方式存在偏差。
  - 多视角动作图像的构造与解码流程可能带来额外表示开销，HTML 摘录尚不足以判断其工程效率。
* **建议先看**: 先看 3.1 和 3.2 里 action image 的编码/解码是否真正保持了控制信息，再读 4.1 的 zero-shot results 判断视频空间统一表示有没有转化成策略泛化。核心问题不是视频生成得像不像，而是动作图像是否成为了可执行控制的好接口。
* **关键词**: `world action model` `action images` `video generation` `multiview` `zero-shot policy`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - action image 到连续控制的解码误差在不同动作维度上是否均匀，还是会偏向某些自由度？
  - 多视角表示带来的泛化收益，是否只是来自更多观测信息而非动作表征本身？
  - 在闭环重规划或长时序任务中，统一视频空间表示还能否保持优势？
* **上传 PDF 后优先看**:
  - action image 的编码与反解码章节
  - 文本控制的动作/视频联合生成设置与 zero-shot 对比
  - open-loop 与 multi-view 设定下的失败案例和泛化分析

## Watchlist

### [W1]. GeoPredict: Leveraging Predictive Kinematics and 3D Gaussian Geometry for Precise VLA Manipulation [[HTML]](https://arxiv.org/html/2512.16811) [[PDF]](https://arxiv.org/pdf/2512.16811)
* **Paper ID**: `2512.16811`
* **Authors**: Jingjing Qian, Boyao Han, Chen Shi, Lei Xiao, Long Yang, Shaoshuai Shi, Li Jiang
* **Author Priority**: Standard
* **为什么还值得留意**: GeoPredict 进入 shortlist，因为它把 VLA 的 2D-reactive 瓶颈明确推进到预测式 3D 运动学与 3D Gaussian geometry，且实验横跨 RoboCasa、LIBERO 和真实场景，问题意识很强。没有进最终精选，主要因为当前证据更像对几何先验的强化版 VLA，而不是对今天主线中的部署适应、评测重构或 world action model 表征做范式级推进。另一个现实限制是它依赖多视角 RGB-D 与外参，扩展性和数据门槛在摘要中已被作者自己点出。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

### [W2]. StarVLA: A Lego-like Codebase for Vision-Language-Action Model Developing [[HTML]](https://arxiv.org/html/2604.05014) [[PDF]](https://arxiv.org/pdf/2604.05014)
* **Paper ID**: `2604.05014`
* **Authors**: StarVLA Community
* **Author Priority**: Standard
* **为什么还值得留意**: StarVLA 值得进 watchlist，因为它试图统一 VLM backbone、world-model backbone 与多种 action head，并把 LIBERO、SimplerEnv、RoboTwin 等评测接口放到同一抽象层里，这对社区复现很重要。没有进最终精选，是因为这篇更像研究基础设施与代码平台论文，摘录里最强信号来自架构兼容性和 server-client 评测封装，而不是新的 VLA/WAM 核心方法突破。若后续社区采纳度高，它的长期影响力可能反而不小。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)

### [W3]. GaussFly: Contrastive Reinforcement Learning for Visuomotor Policies in 3D Gaussian Fields [[HTML]](https://arxiv.org/html/2604.05062) [[PDF]](https://arxiv.org/pdf/2604.05062)
* **Paper ID**: `2604.05062`
* **Authors**: Yuhang Zhang, Mingsheng Li, Yujing Shang, Zhuoyuan Yu, Chao Yan, Jiaping Xiao, Mir Feroskhan
* **Author Priority**: Standard
* **为什么还值得留意**: GaussFly 进入 shortlist，是因为它把 3DGS、对比表征学习和强化学习串成 real-to-sim-to-real 的闭环，解决的是单目自主飞行中表征与策略耦合过紧、sim2real gap 明显的问题。没有进最终精选，主要因为它的核心场景是 AAV 导航而非语言条件操控，和今天聚焦的 VLA/WAM 主线只有部分交叉。它更像一篇很扎实的 3D 表征加 RL 系统论文，而不是今天最强的 embodied foundation model 信号。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

### [W4]. JailWAM: Jailbreaking World Action Models in Robot Control [[HTML]](https://arxiv.org/html/2604.05498) [[PDF]](https://arxiv.org/pdf/2604.05498)
* **Paper ID**: `2604.05498`
* **Authors**: Hanqing Liu, Songping Wang, Jiahuan Long, Jiacheng Hou, Jialiang Sun, Chao Li, Yang Yang, Wei Peng, Xu Liu, Tingsong Jiang, Wen Yao, Yao Mu
* **Author Priority**: Standard
* **为什么还值得留意**: JailWAM 进入 shortlist，因为它把 world action model 的安全问题明确提出，并用 dual-path verification、visual-trajectory mapping 和 risk discriminator 组织出一套可扩展的攻击评测流程。没有进最终精选，是因为当前摘录更像对 WAM 安全缺口的早期警报与攻击框架，证据重点在高效筛查而非更完整的防御或治理闭环。即便如此，WAM 一旦走向真实机器人，这条安全线仍然值得持续盯住。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
