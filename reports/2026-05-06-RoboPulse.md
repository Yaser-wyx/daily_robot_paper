# RoboPulse | 2026-05-06

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 50 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线很清楚：机器人学习正在从“把视觉语言直接接到动作”转向“补齐功能能力、后训练基础设施与评测闭环”的系统竞争。最终精选的 6 篇分别覆盖了 VLA 的运动/记忆/物理感知补强、生成式控制策略的 RL 高效微调、world model 的 reward alignment 与 human corrective post-training、显式物理可行性监督，以及结构化评测体系。它们入选的共同原因，不是单纯模型更大，而是都在回答“怎样让策略更可靠、更可控、更可验证”这个更接近部署的问题。VIP 作者里今天最该优先跟踪的是 Sergey Levine，对应 OGPO 这条 RL 微调主线；扩展名单里的 Dieter Fox 也值得同步盯住，因为 RoboEval 代表了评测基础设施可能重排后续研究排序。

## 今日信号

- 今天最值得记住的研究信号是：VLA 的下一阶段不再只是扩大视觉语言先验，而是显式补上时序记忆、物理感知与可行性约束这些功能层能力。
- 今天最值得记住的研究信号是：world model 正从“生成未来视频”转向“承载奖励对齐、人类纠错和可复用后训练”的操作基础设施。
- 今天最值得记住的研究信号是：机器人研究的竞争门槛正在向评测迁移，过程质量、安全性与失败结构会越来越多地重排模型优劣。

## Editor's Picks

### [1]. RLDX-1 Technical Report [[HTML]](https://arxiv.org/html/2605.03269) [[PDF]](https://arxiv.org/pdf/2605.03269) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.03269`
* **Authors**: Dongyoung Kim, Huiwon Jang, Myungkyu Koo, Suhyeok Jang, Taeyoung Kim, Beomjun Kim, Byungjun Yoon, Changsung Jang, Daewon Choi, Dongsu Han, Donguk Lee, Heeseung Kwon, Hojin Jeon, Jaehyun Kang, Jaekyoung Bae, Jihyuk Lee, Jimin Lee, John Won, Joonwoo Ahn, Junhyeong Park, Junyoung Sung, Kyungmin Lee, Minseong Han, Minsung Yoon, Sejune Joo, Seonil Son, Seungcheol Park, Seunggeun Cho, Seungjun Moon, Seungku Kim, Yonghoon Dong, Yongjin Cho, Youngchan Kim, Chang Hwan Kim, Dohyeon Kim, Hazel Lee, Heecheol Kim, Hensen Ahn, Hyungkyu Ryu, Hyunsoo Choi, Hyunsoo Shin, Jaeheon Jung, Jaewoo Kim, Jinwook Kim, Joochul Chang, Joonsoo Kim, Junghun Park, Jungwoo Park, Junho Cho, Junhyeok Park, Junwon Lee, Kangwook Lee, Kwanghoon Kim, Kyoungwhan Choe, Manoj Bhadu, Nayoung Oh, Sangjun Kim, Sangwoo Kim, Seunghoon Shim, Seunghyun Kim, Seungjun Lee, Seungyup Ka, Sungryol Yang, Wook Jung, Yashu Shukla, Yeonjae Lee, Yeonwoo Bae, Jinwoo Shin
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它是今天最完整的“VLA 补齐功能能力”型 technical report 之一。
* **问题与切口**: 这篇 technical report 直指 VLA 只擅长“看懂场景和指令”却不够会“持续操作”的缺口，想把灵巧操作所需的运动感知、长时记忆与物理感知并入一个通用机器人策略。它的新意不是单纯换更大 backbone，而是把 VLM 的通用理解能力经过机器人 VQA 适配后，与多流动作生成结构结合，试图把 versatile intelligence 扩展成更接近真实部署所需的 functional capabilities。
* **核心方法与证据**: 从 HTML 可见，RLDX-1 以 Qwen3-VL 8B 为表征核心，加入机器人相关 VQA 训练与 cognition tokens 提取动作相关信息，再用多帧观测和记忆模块补足时序与长程推理；整体建立在 MSAT 上，并把物理感知纳入统一架构。证据链覆盖 LIBERO、SIMPLER、LIBERO-Plus、RoboCasa、GR-1 Tabletop 等仿真，以及 humanoid 和单臂真实任务；可以确认其跨基准领先，但各模块收益边界仍需 PDF 进一步核查。
* **正文要点**:
  - 通过多帧观测与记忆模块，论文显式补 motion awareness 和 long-term reasoning，而不只依赖单帧 VLM 表征。
  - 作者在 VLM 上做机器人相关 VQA 适配，并用 cognition tokens 抽取更动作相关的特征。
  - 评测同时覆盖 conventional、robustness 和更具挑战性的仿真套件，以及 humanoid 真实机器人任务。
* **为什么值得跟**:
  - 它正面回应了 VLA 从“通用理解”走向“可持续操作”时最缺的功能层能力。
  - 如果这条路线成立，灵巧操作的系统设计重心会从纯 backbone 规模转向多能力统一建模。
  - 它给出了一条把开放式 VLM 能力真正落到 humanoid 与 dexterous manipulation 上的工程路径。
* **风险 / 保留意见**:
  - 当前摘录只足以确认系统级领先，尚不足以判断 motion、memory、physical sensing 各自的独立贡献。
  - technical report 风格往往组件较多，复现成本和训练数据依赖可能都不低。
* **建议先看**: 先抓方法主轴：VLM 适配、多帧时序、记忆与物理感知是怎样在 MSAT 中汇合的。然后直接看广谱仿真评测与 humanoid 真实任务，判断它究竟是全线更强，还是主要受益于特定任务族。
* **关键词**: `VLA` `dexterous manipulation` `memory` `physical sensing` `humanoid`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - cognition tokens 相比直接使用 VLM 隐状态，具体改善了哪些动作相关信息抽取？
  - multi-frame 与 memory 模块在长程、遮挡和重抓取等场景中的贡献是否可分离？
  - physical sensing 输入是如何与视觉语言表征融合的，真实收益主要来自哪类任务？
* **上传 PDF 后优先看**:
  - 系统架构与 VLM/MSAT 接口设计
  - 广谱仿真基准比较与模块消融
  - 真实机器人 humanoid/单臂任务与失败案例

### [2]. OGPO: Sample Efficient Full-Finetuning of Generative Control Policies [[VIP]] [[HTML]](https://arxiv.org/html/2605.03065) [[PDF]](https://arxiv.org/pdf/2605.03065) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.03065`
* **Authors**: Sarvesh Patil, Mitsuhiko Nakamoto, Manan Agarwal, Shashwat Saxena, Jesse Zhang, Giri Anantharaman, Cleah Winston, Chaoyi Pan, Douglas Chen, Nai-Chieh Huang, Zeynep Temel, Oliver Kroemer, Sergey Levine, Abhishek Gupta, Hongkai Da, Paarth Shah, Max Simchowitz
* **Author Priority**: Core VIP
* **一句话结论**: 非常值得优先看，它是今天最直接命中 RL + 生成式控制策略微调主线的一篇。
* **问题与切口**: OGPO 处理的是一个很现实的问题：预训练好的 diffusion 或 flow 控制策略在部署环境里往往还不够稳，但传统 RL 微调要么样本效率差，要么只敢调局部模块。它的核心切口是把 generative control policy 当成可完整优化的策略对象，在不放弃 off-policy 数据复用的前提下做 full finetuning，试图把模仿学习得到的先验真正转化为可自主强化的鲁棒控制能力。
* **核心方法与证据**: 根据摘要与结论，OGPO 维持 off-policy critic 网络以最大化数据复用，同时用修改过的 PPO 目标，把策略梯度贯穿整个生成式动作采样过程，并把 critic 作为末端回报信号。作者把证据放在多任务操控、高精度插入和灵巧控制三类场景，并声称达到当前最佳表现。需要保守指出的是，HTML 摘录没有展开优势估计、稳定化技巧和强基线细节；作者自己也承认存在 Q 函数过度利用、性能振荡与 full finetuning 偏慢的问题。
* **正文要点**:
  - 目标不是 adapter 式小修，而是对生成式控制策略做 full-policy RL finetuning。
  - off-policy critic 被用来提高数据复用，并为整个生成过程提供可优化的终端奖励信号。
  - 结论明确承认 Q-function over-exploit、训练震荡以及数据充足时 full finetuning 偏慢。
* **为什么值得跟**:
  - 它把“生成式策略能否真正吃 RL 微调”这个问题从局部修补推进到全策略优化。
  - 这条线直接对应 Sergey Levine 所代表的高样本效率机器人 RL 主线，值得优先跟踪。
  - 若方法稳定，生成式控制策略的部署适应将不必长期停留在纯行为克隆框架内。
* **风险 / 保留意见**:
  - 摘要级证据不足以判断 sample efficiency 的真实幅度，关键算法细节仍需正文确认。
  - 作者已明确提示 Q 函数被过度利用与成功率/速度张力，部署稳定性不能先验乐观。
* **建议先看**: 先看 modified PPO 是如何把梯度穿过整条生成链的，以及 off-policy critic 为什么不会破坏优化稳定性。再看数据规模与失败模式分析，判断 full finetuning 何时真正优于更轻量的微调路线。
* **关键词**: `reinforcement learning` `generative control policies` `off-policy` `PPO` `sample efficiency`
* **证据来源**: arXiv HTML (Introduction, Conclusion)
* **读 PDF 先核查**:
  - modified PPO objective 如何在整条生成链上传梯度，同时避免高方差和 credit assignment 崩溃？
  - off-policy critics 与 full generative policy 更新之间如何做 distribution correction 或 regularization？
  - 当 replay buffer 中加入大量高质量专家数据时，为什么 full finetuning 会变慢，是否说明更新范围过大？
* **上传 PDF 后优先看**:
  - 算法目标与 full-generative policy gradient 推导
  - 多任务、插入与灵巧控制实验及 sample-efficiency 比较
  - 训练振荡、Q-function exploitation 与失败模式分析

### [3]. RoboAlign-R1: Distilled Multimodal Reward Alignment for Robot Video World Models [[HTML]](https://arxiv.org/html/2605.03821) [[PDF]](https://arxiv.org/pdf/2605.03821) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.03821`
* **Authors**: Hao Wu, Yuqi Li, Yuan Gao, Fan Xu, Fan Zhang, Kun Wang, Penghao Zhao, Qiufeng Wang, Yizhou Zhao, Weiyan Wang, Yingli Tian, Xian Wu, Xiaomeng Huang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把 robot video world model 从“像不像”拉向“对控制有没有用”。
* **问题与切口**: 这篇工作瞄准 robot video world model 的一个关键偏差：现有训练多靠重建或感知相似度，生成得像不等于对机器人决策有用。RoboAlign-R1 的新意在于把 instruction following、操作成功和物理合理性这些更接近控制价值的目标，显式转成 post-training 的 reward alignment 问题，同时连带处理长时自回归 rollout 容易积累误差的老问题。
* **核心方法与证据**: HTML 给出的主线较完整：其 backbone 采用 tokenize-predict-decode 范式，用双分支视觉 tokenizer 将条件帧编码为 context tokens、观测帧编码为 residual dynamics tokens，并与离散动作 token 交织后交给 causal Transformer。随后作者构建含 1 万条视频-指令标注的 RobotWorldBench，先训练多模态 teacher judge，再蒸馏成轻量 reward model 做 RL 式 post-training；推理阶段再用 sliding-window re-encoding 稳住长程 rollout。证据除 in-domain judge 外，还包括外部 VLM 交叉检查和小规模盲测。
* **正文要点**:
  - 双分支 tokenizer 把静态上下文与动态残差分开编码，而不是把所有视觉变化揉成单一 token 流。
  - RobotWorldBench 来自 RT-1、BridgeData V2、CALVIN 与 LIBERO 四个数据源，共 1 万条标注视频-指令对。
  - 评测同时报告语义/物理对齐指标与像素级、ROI 级指标，并用外部 VLM 与小规模人工盲测做交叉检查。
* **为什么值得跟**:
  - 它把 world model 的优化目标从视觉保真转向更接近控制价值的对齐目标。
  - reward distillation 为 world model post-training 提供了比大规模人工标注更可扩展的路径。
  - 长程 rollout 稳定化如果成立，会直接影响后续规划、策略评估与 imagined data 的可用性。
* **风险 / 保留意见**:
  - 主要排名仍依赖 in-domain judge，尽管有交叉检查，但自动评委偏置仍是核心风险。
  - 更好的视频 rollout 并不自动等于更好的闭环控制，控制层增益仍需谨慎解读。
* **建议先看**: 先读 reward alignment 管线，重点看 judge 如何定义“有用的 world model”。随后核查长程推理稳定化部分，判断其收益究竟来自奖励对齐、解码策略，还是两者叠加。
* **关键词**: `world model` `reward alignment` `robot video` `long-horizon rollout` `benchmark distillation`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - teacher judge 的六维评价里，哪些维度真正驱动了模型改进，是否会偏向特定数据域？
  - sliding-window re-encoding 在多长 rollout 上开始显著抑制误差累积，代价是什么？
  - reward-aligned post-training 提升的是语义跟随与操作成功，还是主要改善视觉合理性？
* **上传 PDF 后优先看**:
  - RobotWorldBench 与 judge/reward distillation 设计
  - 长程 rollout 推理与误差累积控制实验
  - human/VLM cross-check 与 baseline ranking 一致性

### [4]. Hi-WM: Human-in-the-World-Model for Scalable Robot Post-Training [[HTML]](https://arxiv.org/html/2604.21741) [[PDF]](https://arxiv.org/pdf/2604.21741) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.21741`
* **Authors**: Yaxuan Li, Zhongyi Zhou, Yefei Chen, Yanjiang Guo, Jiaming Liu, Shanghang Zhang, Jianyu Chen, Yichen Zhu
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它把 world model 从想象器改造成了可回滚、可分叉的人类纠错平台。
* **问题与切口**: Hi-WM 解决的是机器人后训练最贵的一环：每次失败纠正都要占用真实机器人、真实场景和人工复位。它把这一 corrective loop 迁到 learned world model 里，让人类不再围着硬件做一次性示教，而是在模型内部对失败状态反复回滚、分叉和补救。相对把 world model 仅当作 imagination 工具的路线，这篇更像把它改造成可复用的 post-training 操作系统。
* **核心方法与证据**: 从摘录可确认，流程是先让当前策略在 action-conditioned world model 中闭环 rollout；当轨迹错误或接近失败时，人类直接在模型里插入短 corrective actions。系统缓存中间状态并支持 rollback 与 branching，因此一个失败态可以衍生多条修正 continuation，围绕策略薄弱区形成更密集监督，再用于后训练。实验明确围绕四个问题组织：世界模型与真实执行的对齐、作为 policy-agnostic 框架的有效性、随场景覆盖扩展的成本优势，以及对新场景真实泛化的帮助；但量化幅度在当前摘录中不可见。
* **正文要点**:
  - 人类干预从物理世界迁到 world model 内部，而不是继续消耗真实机器人时间。
  - 失败态可被缓存、回滚并分叉复用，从一次失败中扩展出多条修正轨迹。
  - 真实机器人实验围绕对齐性、有效性、扩展性与泛化四条主线组织，而不只报告单一成功率。
* **为什么值得跟**:
  - 它把 world model 的角色推进到后训练基础设施层，而不只是辅助预测。
  - 如果失败态复用机制成立，机器人 post-training 的边际成本结构会明显改变。
  - policy-agnostic 设定意味着它有机会服务于更广泛的预训练 generalist policy。
* **风险 / 保留意见**:
  - 全部收益都建立在 world model 与真实失败模式足够对齐这一前提上。
  - 人在模拟器中的修正可能会放大学到的模型偏差，而不是单纯补足真实世界薄弱点。
* **建议先看**: 先顺着一条失败样本看完整的 rollout、介入、回滚、分叉和再训练链路。再看 world-model-to-real 对齐与成本扩展证据，判断它到底是概念漂亮还是工程上真能省下大量真实机器人时间。
* **关键词**: `world model` `post-training` `human-in-the-loop` `rollback` `branching`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - world model 何时被判定为“足够可靠”以承载人类纠错，失配状态如何识别？
  - branching 产生的多条 corrective continuation 如何筛选或加权，避免把模拟偏差放大？
  - policy-agnostic 的成立边界在哪里，不同 base policy 对 corrective data 的吸收方式是否一致？
* **上传 PDF 后优先看**:
  - 交互式 correction workflow 与状态缓存/分叉机制
  - world-model-to-real 对齐验证
  - 成本扩展与真实泛化实验

### [5]. Can Explicit Physical Feasibility Benefit VLA Learning? An Empirical Study [[HTML]](https://arxiv.org/html/2604.17896) [[PDF]](https://arxiv.org/pdf/2604.17896) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.17896`
* **Authors**: Yubai Wei, Chen Wu, Hashem Haghbayan
* **Author Priority**: Standard
* **一句话结论**: 值得看，它不是在堆模型，而是在追问 VLA 是否真的学会了“物理上能做”的动作。
* **问题与切口**: 这篇论文问的是一个基础但常被跳过的问题：VLA 若只从成功示范里学动作，能否真正学到避障、运动学可达和物理可行这些硬约束？作者没有继续在更大数据或更强模型上做文章，而是把“显式可行性监督”当作结构化学习信号，检验它能否为 VLA 提供几何层面的归纳偏置，尤其是在数据有限或环境扰动存在时改善策略行为。
* **核心方法与证据**: 根据 HTML 摘录，作者在 NVIDIA Isaac Sim 中构建单臂 Franka 的 obstacle-aware 操控设定，把它作为探测 geometry-dependent physical feasibility 的受控实验平台；策略 backbone 采用 RDT-1B，并比较不同 fine-tuning 目标。实验问题围绕三点展开：显式可行性监督如何改变策略行为、在有限数据下是否提升学习效率、监督强度如何影响效果。由此可见这是一项偏机制分析的实证研究；但证据边界也很清楚，目前主要限于仿真、单一机械臂和障碍敏感设定。
* **正文要点**:
  - 作者把物理可行性视作几何结构问题，而不是期待 VLA 仅靠示范隐式学会。
  - 实验采用 obstacle-aware manipulation 作为受控 probe，而不是直接声称适用于全部操控场景。
  - 研究问题明确围绕行为变化、数据效率与监督强度三条因果线索展开。
* **为什么值得跟**:
  - 它给 VLA 训练目标设计提供了一个可检验的结构化监督方向。
  - 对安全性、避障性和物理可达性敏感的场景，这类信号可能比单纯成功标签更有价值。
  - 即便结论最终是否定的，这类机制研究也能帮助厘清 VLA 真正在学什么。
* **风险 / 保留意见**:
  - 仿真单平台设置限制了外部效度，不能直接外推出真实机器人复杂接触任务。
  - 显式可行性标签也可能只对障碍规避类几何问题有效，而未必覆盖更广义的操作物理性。
* **建议先看**: 先看可行性监督到底如何定义，以及它怎样插入 RDT-1B 的微调目标。然后重点看有限数据与监督强度消融，判断这是不是一个真正稳定的结构化学习信号。
* **关键词**: `VLA` `physical feasibility` `geometry` `RDT-1B` `Isaac Sim`
* **证据来源**: arXiv HTML (Introduction, Experiments)
* **读 PDF 先核查**:
  - 显式可行性监督的标签或评分来自何种几何判据，是否会把任务成功与安全可行混为一谈？
  - 收益主要来自更强的避障先验，还是来自对动作分布更稳定的正则化作用？
  - 当场景从障碍规避扩展到接触丰富任务时，这种监督还会保持有效吗？
* **上传 PDF 后优先看**:
  - 可行性监督定义与训练目标
  - 有限数据与监督强度消融
  - 仿真设置、扰动协议与失败模式分析

### [6]. RoboEval: Where Robotic Manipulation Meets Structured and Scalable Evaluation [[VIP]] [[HTML]](https://arxiv.org/html/2507.00435) [[PDF]](https://arxiv.org/pdf/2507.00435) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2507.00435`
* **Authors**: Yi Ru Wang, Carter Ung, Christopher Tan, Grant Tannert, Jiafei Duan, Josephine Li, Anh Le, Rishabh Oswal, Markus Grotz, Wilbert Pumacay, Yuquan Deng, Ranjay Krishna, Dieter Fox, Siddhartha Srinivasa
* **Author Priority**: Extended VIP
* **一句话结论**: 值得进最终精选，它不是新策略论文，却可能影响后续很多策略论文该怎么被判断。
* **问题与切口**: RoboEval 不是再造一个“更难任务集”，而是重做机器人操控的评测语言。它指出二元成功率会把流畅但稳健的策略与侥幸完成、过程危险的策略混在一起，因此围绕双臂操控构建了带系统化变化、标准化行为指标和阶段性结果指标的评测框架。相对已有 benchmark，它更强调把执行质量、协调性和失败结构显式量化出来。
* **核心方法与证据**: 从摘录可确认，RoboEval 提供八个双臂任务、三千多条专家示范和模块化仿真平台；指标层面同时记录效率、协调、安全/稳定等行为量，以及能追踪阶段进展和定位失败位置的 outcome 指标。作者的证据重点不是单看谁成功率高，而是证明这些 richer metrics 一方面能预测 success，另一方面能揭露 success rate 隐藏掉的差异。结论也明确声称，这些指标帮助分析策略如何成功、为何失败，以及哪些执行因素支撑了鲁棒性。
* **正文要点**:
  - 评测核心从 binary success 扩展到行为质量与阶段性结果，而不再只看终态是否完成。
  - 任务与数据设计围绕八个双臂任务、系统化 variation 和三千多条专家示范展开。
  - 作者强调 richer metrics 既能预测 success，也能揭露 success rate 看不见的策略差异。
* **为什么值得跟**:
  - 评测瓶颈会直接塑造 VLA、world model 和 manipulation policy 的研究方向。
  - 过程级指标更适合诊断流畅性、协调性与安全性，这些往往才是部署门槛。
  - Dieter Fox 这条 benchmark 基础设施线值得跟，因为它可能改变社区的默认比较标准。
* **风险 / 保留意见**:
  - 当前平台是仿真主导，能否充分覆盖真实机器人中的顺应性、磨损与感知噪声仍需保守看待。
  - 双臂任务聚焦很有价值，但也意味着它对更广泛单臂或移动操作场景的外推有限。
* **建议先看**: 先看指标定义，确认作者怎样把 fluency、coordination、safety 转成可重复度量。然后看那些 success rate 接近但行为指标明显分叉的案例，这部分最能体现它的必要性。
* **关键词**: `evaluation` `bimanual manipulation` `behavioral metrics` `safety` `benchmark`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 哪些行为指标与最终成功最相关，它们在不同任务上的稳定性如何？
  - richer metrics 是否会改变模型排序，还是主要提升解释性而不改变结论？
  - 这些阶段性 outcome 指标能否自然迁移到真实机器人评测，而不依赖仿真特权信息？
* **上传 PDF 后优先看**:
  - 指标定义与 instrumented task design
  - 相近成功率下的策略行为差异比较
  - 任务 variation 与失败定位分析

## Watchlist

### [W1]. OmniUMI: Towards Physically Grounded Robot Learning via Human-Aligned Multimodal Interaction [[HTML]](https://arxiv.org/html/2604.10647) [[PDF]](https://arxiv.org/pdf/2604.10647)
* **Paper ID**: `2604.10647`
* **Authors**: Shaqi Luo, Yuanyuan Li, Youhao Hu, Chenhao Yu, Chaoran Xu, Jiachen Zhang, Guocai Yao, Tiejun Huang, Ran He, Zhongyuan Wang
* **Author Priority**: Standard
* **为什么还值得留意**: OmniUMI 值得进 shortlist，因为它把 tactile、抓取内力与外部 wrench 一起纳入 robot-free UMI 式数据采集，直接回应 contact-rich manipulation 里“视觉不够”的老问题。它也把“人能否自然感知并调节这些物理信号”作为系统设计核心，这点比单纯堆传感器更重要。没有进最终精选，主要因为当前证据更像一条高质量数据接口与采集管线，而不是已经证明可广泛改变 VLA 或 world model 上限的通用方法；HTML 摘录中的下游验证也更偏代表性场景。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. BifrostUMI: Bridging Robot-Free Demonstrations and Humanoid Whole-Body Manipulation [[HTML]](https://arxiv.org/html/2605.03452) [[PDF]](https://arxiv.org/pdf/2605.03452)
* **Paper ID**: `2605.03452`
* **Authors**: Chenhao Yu, Hongwu Wang, Youhao Hu, Jiachen Zhang, Yuanyuan Li, Shaqi Luo
* **Author Priority**: Standard
* **为什么还值得留意**: BifrostUMI 进入 watchlist，是因为它把 UMI 思路延展到 humanoid whole-body data collection，用便携 VR 与稀疏关键点去替代昂贵 teleoperation，这条数据扩展路线很实用。它还明确关心 wrist-view 视觉与 whole-body coordination 的联动，对 humanoid 学习有现实意义。没有进最终精选，是因为当前创新主要落在采集和表示工程，而非更通用的控制、后训练或评测机制；证据也集中在 Unitree G1 和特定任务链路，外推范围暂时偏窄。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. Bridging the Embodiment Gap: Disentangled Cross-Embodiment Video Editing [[HTML]](https://arxiv.org/html/2605.03637) [[PDF]](https://arxiv.org/pdf/2605.03637)
* **Paper ID**: `2605.03637`
* **Authors**: Zhiyuan Li, Wenyan Yang, Wenshuai Zhao, Yue Ma, Yuanpeng Tu, Pekka Marttinen, Joni Pajarinen
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇工作进入 shortlist，是因为它正面处理了“用人类视频学机器人”里最核心的 embodiment gap，并尝试把任务语义与 embodiment 表征显式解耦。若这条路线成立，互联网视频作为机器人预训练数据源的可用性会明显上升。之所以没进最终精选，是因为当前贡献更靠近生成式视频编辑而非直接闭环控制，控制可用性和物理一致性的证据仍隔了一层；从 HTML 摘录看，也还缺少足够直接的真实机器人落地强度。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. Refining Compositional Diffusion for Reliable Long-Horizon Planning [[HTML]](https://arxiv.org/html/2605.03075) [[PDF]](https://arxiv.org/pdf/2605.03075)
* **Paper ID**: `2605.03075`
* **Authors**: Kyowoon Lee, Yunhao Luo, Anh Tong, Jaesik Choi
* **Author Priority**: Standard
* **为什么还值得留意**: RCD 值得保留在 watchlist，因为它抓住了 compositional diffusion planning 在长时规划里的 mode-averaging 痛点，并用 training-free guidance 去修正全局一致性。它覆盖 locomotion、manipulation 和 pixel observation，说明方法并非只对单一环境有效。没有进最终精选，主要因为它更像规划器层面的通用技术推进，和今天的 VLA、world model、robot post-training 主线相比，连接真实机器人部署的证据还不够近；同时现有证据也主要来自 OGBench。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
