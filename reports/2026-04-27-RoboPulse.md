# RoboPulse | 2026-04-27

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 49 papers scanned · 10 shortlisted · 5 editor's picks

今天这组最终精选的主线非常清晰：VLA 正从“会做动作”转向“能否在长时程、杂乱环境、可扩展评估与安全约束下可靠工作”，对应地 world model、显式状态、RL 精修和物理安全评测四条线同时升温。入选的 5 篇里，dWorldEval 抓住了大模型机器人最缺的可扩展评估，CodeGraphVLP 与 OBEYED-VLA 分别切中非马尔可夫长任务与 clutter grounding，RedVLA 把物理红队测试单独抬成核心问题，OmniVLA-RL 则代表 RL 再次回到 VLA 精度和稳健性改进的中心。就作者跟踪价值看，这批最终精选里没有直接命中你给定的核心 VIP 作者名单，因此今天更应该优先追踪的是方向信号而不是作者品牌。若后续同主题工作出现 Sergey Levine、Chelsea Finn、Pieter Abbeel、Shuran Song、Yuke Zhu、Xiaolong Wang、Huazhe Xu 一线作者跟进，值得立即提高优先级。

## 今日信号

- 今天最值得记住的研究信号是：VLA 的下一阶段竞争点不再只是离线成功率，而是能否显式处理历史依赖、视觉干扰、评估代理可信度与部署安全。
- 今天最值得记住的研究信号是：world model 正在从“生成未来”转向“可作为评价器与决策接口”，其中统一 token 化、进度建模和长时程一致性成为关键设计。
- 今天最值得记住的研究信号是：将感知 grounding、程序化规划、在线 RL 或安全红队机制模块化插入 VLA，很可能比继续把一切压进单体端到端策略更快产生可验证收益。

## Editor's Picks

### [1]. dWorldEval: Scalable Robotic Policy Evaluation via Discrete Diffusion World Model [[HTML]](https://arxiv.org/html/2604.22152) [[PDF]](https://arxiv.org/pdf/2604.22152) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.22152`
* **Authors**: Yaxuan Li, Zhongyi Zhou, Yefei Chen, Yaokai Xue, Yichen Zhu
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它不是再做一个更强策略，而是试图把机器人策略评测本身做成可扩展且更可信的 world-model 代理。
* **问题与切口**: 这篇工作瞄准的是当前通用机器人策略最现实却最少被解决的瓶颈：评估太贵、太慢、也难覆盖大规模任务与环境。作者提出 dWorldEval，用离散扩散 world model 充当策略评估代理，把视觉、语言和动作统一映射到同一 token 空间，再联合预测未来观测与任务进度。相对已有世界模型更偏生成或仿真替代的路线，它的切口更明确：不是追求视觉逼真，而是追求“评估结论是否跟真实执行对齐”。
* **核心方法与证据**: 从 HTML 可见，方法核心有三层：一是统一 token 化后用单一 transformer 去噪建模多模态序列；二是加入 sparse keyframe memory 维持长时程时空一致性；三是显式引入 progress token，把任务完成度变成可预测变量，用于自动判定成功。作者强调现有模型常因只见成功演示而在 OOD 动作上“幻觉成功”，而 dWorldEval 试图通过动作纳入建模与一致性约束缓解这一问题。证据边界上，HTML 只明确提到 predicted success rate 与真实执行更对齐，以及使用 LPIPS 度量 rollout 一致性。
* **正文要点**:
  - 统一 token 空间同时编码视觉、语言与机器人动作，而不是把动作当成外接条件。
  - 用 sparse keyframe memory 维持长时程 rollout 的时空一致性，这是作者处理物理不一致的重要手段。
  - 推理时联合预测未来观测和 progress token，使评估输出不止是画面生成，还包含任务完成度判断。
* **为什么值得跟**:
  - 它把机器人 world model 的价值从“辅助想象”推进到“可扩展评测基础设施”。
  - 如果评估代理足够对齐真实执行，VLA 迭代速度会比依赖大规模真机回放更快。
  - 显式建模 progress 为后续自动 curriculum、筛选数据和安全闸门提供了接口。
* **风险 / 保留意见**:
  - HTML 证据主要支持“相关性更高”，但对跨机器人、跨任务分布外泛化边界描述仍有限。
  - LPIPS 与进度预测能否真正覆盖物理接触失败模式，单从摘录还不能完全确认。
* **建议先看**: 先抓住作者的问题定义：为什么现有 world model 不适合做评估代理，而不是只看生成质量。随后重点看统一 token 化、keyframe memory 和 progress token 三者如何共同支撑“评估对齐真实执行”这一主张。
* **关键词**: `world model` `policy evaluation` `discrete diffusion` `progress token` `robotics`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - progress token 的监督信号具体来自人工标注、轨迹启发式，还是任务终止规则外推？
  - 统一 token 化后，动作 token 如何避免被视觉先验淹没，尤其在 OOD 失败动作下？
  - keyframe memory 提升的是视觉连贯性，还是确实提升了成功率预测与真实执行的一致性？
* **上传 PDF 后优先看**:
  - 方法章节里关于统一 token 化与去噪网络输入输出定义的部分。
  - 长时程一致性与 progress prediction 的消融实验或误差分析章节。
  - 评估对齐真实执行的主结果表、相关性分析和失败案例可视化。

### [2]. CodeGraphVLP: Code-as-Planner Meets Semantic-Graph State for Non-Markovian Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2604.22238) [[PDF]](https://arxiv.org/pdf/2604.22238) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.22238`
* **Authors**: Khoa Vo, Sieu Tran, Taisei Hanyu, Yuki Ikebe, Duy Nguyen, Bui Duy Quoc Nghi, Minh Vu, Anthony Gunderman, Chase Rainwater, Anh Nguyen, Ngan Le
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它抓住了 VLA 在非马尔可夫长任务里最常见但常被弱化的问题：当前帧不够，必须显式保存状态并可执行地规划。
* **问题与切口**: CodeGraphVLP 解决的是长时程操控中的历史依赖与 clutter 干扰问题。许多 VLA 默认“最新观测足够决定下一步”，但在物体被遮挡、场景相似或关键证据只在过去出现过时，这个假设会直接失效。作者提出把 persistent semantic graph state、可执行代码规划器和 progress-guided visual-language prompting 组合起来，让策略不是只盯当前图像，而是围绕持续更新的语义状态做分层决策。相对普通 memory-augmented VLA，新意在于把记忆组织成可规划、可解释的图结构。
* **核心方法与证据**: HTML 显示其框架由三部分构成：先从多视角 RGB 与本体信息中维护 persistent semantic-graph state；再通过 code-as-planner 在图状态上做程序化规划；执行阶段再用 progress-guided visual-textual prompting 提高在 clutter 中的视觉落点与动作推理。实验明确围绕三个问题展开：是否比强基线更可靠完成非马尔可夫长任务、是否能降低规划延迟、以及进度引导提示是否提升 clutter 鲁棒性。证据范围上，HTML 提到是真实桌面三类任务，并强调成功率与规划时延双重收益。
* **正文要点**:
  - 论文直接把长时程任务定义为 non-Markovian 问题，而不是简单扩大观察窗口。
  - 作者将可执行代码规划建立在 persistent semantic graph 上，意图用结构化状态替代模糊历史记忆。
  - 实验问题设计同时考察成功率、规划效率和 progress-guided prompting 的实际增益。
* **为什么值得跟**:
  - 这条路线为 VLA 引入了比“更长上下文”更强的状态表示与可解释规划接口。
  - 在真实桌面任务里强调 clutter 和历史依赖，贴近部署而非只在干净基准上提分。
  - 如果代码规划与图状态稳定，可为任务监控、纠错和人机协作提供更透明的中间层。
* **风险 / 保留意见**:
  - 框架依赖 foundation models 做语义图构建与程序合成，整体稳健性可能受上游误差级联影响。
  - 目前摘录只覆盖三类真实任务，状态图和代码规划对更开放环境的扩展性仍需核查。
* **建议先看**: 建议先看问题设定和 semantic-graph state 的定义，再看 code planner 如何消费这份状态。最后再核查 progress-guided prompting 到底提升的是视觉定位、计划推进判断，还是两者都有。
* **关键词**: `VLA` `non-Markovian` `semantic graph` `code-as-planner` `long-horizon manipulation`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 语义图中的节点与边是如何更新和遗忘的，错误记忆会不会持续污染后续规划？
  - 代码规划器输出的是高层子任务、条件分支，还是可直接映射到动作调用的程序骨架？
  - progress-guided prompting 的收益主要来自文本重提示还是来自图状态提供的结构化上下文？
* **上传 PDF 后优先看**:
  - 方法章节中 semantic-graph state 的构建、更新和查询机制。
  - 实验章节里与 memory-enabled VLA、VLM-in-the-loop 层级方法的对比设置。
  - 延迟、成功率与 clutter 条件下失败案例分析的结果部分。

### [3]. RedVLA: Physical Red Teaming for Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2604.22591) [[PDF]](https://arxiv.org/pdf/2604.22591) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.22591`
* **Authors**: Yuhao Zhang, Borong Zhang, Jiaming Fan, Jiachen Shen, Yishuai Cai, Yaodong Yang, Jiaming Ji
* **Author Priority**: Standard
* **一句话结论**: 非常值得看，它把 VLA 安全从口头风险讨论推进到可系统挖掘脆弱性的物理红队框架。
* **问题与切口**: RedVLA 的价值在于它不再把 VLA 安全理解为离线审查或语言层约束，而是直接问：在任务仍然可执行的前提下，怎样系统性构造初始物理场景去诱发危险行为？作者固定任务指令，只扰动初始状态，并注入单一 risk factor，以两阶段流程自动寻找会触发安全违规的风险场景。相对已有 LLM/VLM red teaming，这里真正新的是把“红队”从符号攻击迁移到物理交互层，并要求风险场景既危险又不破坏任务可行性。
* **核心方法与证据**: HTML 给出的框架较完整。第一阶段 Risk Scenario Synthesis 先通过 benign rollout 的末端执行器轨迹定位关键交互区域，再实例化目标安全违规与风险因子，使风险物体出现在更可能被策略接触或忽视的位置。第二阶段 Risk Amplification 再做 trajectory-driven iterative optimization，持续提高安全违规发生概率。实验围绕四个问题展开：能否在多类 VLA 上诱发多样不安全行为、模型能力与多模态扰动如何影响结果、关键组件是否必要，以及暴露出的漏洞是否具有现实可行性。
* **正文要点**:
  - 作者只扰动初始场景而不改任务指令，强调评测的是物理安全脆弱性而非语言越狱。
  - 风险区域定位依赖 benign 轨迹中的末端执行器位置、速度和夹爪状态。
  - 实验覆盖六个代表性 VLA，并明确关注不同安全代价类型下的失效。
* **为什么值得跟**:
  - 这为 VLA 部署前安全测试提供了比常规成功率评测更接近真实风险的工具。
  - 通过任务可行前提下诱发失效，更容易区分策略脆弱性和纯环境不可解。
  - 红队框架本身也能反向服务于安全数据收集、对抗训练和上线门禁。
* **风险 / 保留意见**:
  - HTML 摘录没有充分展开风险因子空间与场景分布，泛化到更复杂现实安全问题的边界仍需确认。
  - 若红队过程高度依赖已有 benign 轨迹质量，低质量参考轨迹可能限制其发现能力。
* **建议先看**: 先看作者如何界定“物理安全风险”以及为何只改初始状态。随后重点核查两阶段流程是否真的既保持任务可行，又能稳定放大危险行为。
* **关键词**: `VLA safety` `red teaming` `physical risk` `risk scenario synthesis` `trajectory optimization`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 风险因子的类型库是固定集合还是可组合生成，覆盖面到底有多广？
  - trajectory-driven optimization 优化的目标信号来自模型内部响应、外部成本函数，还是混合指标？
  - 六个 VLA 家族间的脆弱性差异，更多来自动作表示不同还是感知与推理能力差异？
* **上传 PDF 后优先看**:
  - 方法章节里 Risk Scenario Synthesis 与 Risk Amplification 的具体接口定义。
  - 实验章节中跨模型、跨安全代价类型的主比较结果。
  - 真实世界可行性验证与失败案例分析部分。

### [4]. OmniVLA-RL: A Vision-Language-Action Model with Spatial Understanding and Online RL [[HTML]](https://arxiv.org/html/2604.17706) [[PDF]](https://arxiv.org/pdf/2604.17706) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.17706`
* **Authors**: Haoxiang Jie, Yaoyuan Yan, Xiangyu Wei, Kailin Wang, Hongjie Yan, Zhiyou Heng, Daocheng Chen
* **Author Priority**: Standard
* **一句话结论**: 值得看，但要带着验证心态读；它试图把空间理解和在线 RL 更紧地接到 VLA 里，命题重要，证据细节则需要你在 PDF 里重点核实。
* **问题与切口**: OmniVLA-RL 试图同时处理三类常见短板：VLA 空间感知不准、多模态融合不够专门化，以及 RL 微调阶段训练不稳定。作者提出 Mix-of-Transformers 结构，把 reasoning、spatial 和 action expert 分开建模，再用 Flow-GSPO 把 flow matching 改写为 SDE 过程并与 GSPO 结合，以提高动作精度和训练稳健性。相对单一主干加轻量动作头的常见路线，它更强调专家分工与在线 RL 对动作质量的二次修正。
* **核心方法与证据**: 从 HTML 可见，训练被组织成三阶段渐进式范式。第一阶段先做 multimodal spatial perception pre-training：VLM 由 PaLiGemma 初始化，Spatial Expert 随机初始化，Action Expert 冻结，以大规模 3D 数据学习结构与几何关系，避免过早形成动作偏置。随后再进入动作生成与 RL 强化阶段。摘要和结论声称在 LIBERO 与 LIBERO-Plus 上整体表现较强并优于主流方法，但摘录中的实验数字和真实机器人证据都较有限，因此当前更适合作为结构思路而非已完全坐实的结论。
* **正文要点**:
  - MoT 设计显式拆分 reasoning、spatial 与 action expert，而不是让单一干线同时承担所有功能。
  - Flow-GSPO 把 flow matching 与基于分组的策略优化结合，目标是提升动作精度与训练稳定性。
  - 三阶段训练里第一阶段冻结 Action Expert，优先学习空间表示，说明作者非常在意空间偏差的前置纠正。
* **为什么值得跟**:
  - 它代表 RL 正重新进入 VLA 主线，不只是做后处理，而是直接参与动作生成范式。
  - 把空间专家单独做强，回应了 VLM 迁移到机器人后最常见的 3D 感知短板。
  - 若该路线成立，VLA 可能从“大模型统一表示”转向“专家化分工加在线校正”。
* **风险 / 保留意见**:
  - HTML 对 Flow-GSPO 的优化细节和稳定性证据披露有限，方法真实性能提升幅度需要看正文细节。
  - 目前摘录只显示 benchmark 结果，缺少真实部署或 sim2real 证据，外推要保守。
* **建议先看**: 先看三阶段训练与专家分工是否自洽，再看 Flow-GSPO 到底解决了什么训练不稳问题。若时间有限，优先核查空间专家带来的增益是否独立于模型规模增长。
* **关键词**: `VLA` `online RL` `spatial understanding` `Mix-of-Transformers` `Flow-GSPO`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments)
* **读 PDF 先核查**:
  - Spatial Expert 的输入输出形式是什么，它如何与 VLM 表征对齐而不过度冗余？
  - Flow-GSPO 相比普通 flow matching 或常规 RL 微调，主要改善的是收敛稳定性、动作精度还是样本效率？
  - 三阶段训练中各阶段的性能贡献是否通过严格消融拆开验证？
* **上传 PDF 后优先看**:
  - 方法章节里 MoT 架构与各专家之间的信息流。
  - 训练章节中三阶段范式与 Flow-GSPO 优化目标的定义。
  - LIBERO 与 LIBERO-Plus 的主表、消融和稳定性曲线。

### [5]. Clutter-Robust Vision-Language-Action Models through Object-Centric and Geometry Grounding [[HTML]](https://arxiv.org/html/2512.22519) [[PDF]](https://arxiv.org/pdf/2512.22519) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2512.22519`
* **Authors**: Khoa Vo, Taisei Hanyu, Yuki Ikebe, Trong Thang Pham, Nhat Chung, Minh Nhat Vu, Duy Nguyen Ho Minh, Anh Nguyen, Anthony Gunderman, Chase Rainwater, Ngan Le
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，它对“端到端 VLA 为何在杂乱现实场景里容易失焦”给出了很直接的结构性回答。
* **问题与切口**: 这篇论文的核心判断很鲜明：现有 VLA 把感知和控制过度纠缠在一起，结果是语言条件视觉 grounding 被动作目标侵蚀，在 clutter、背景变化和目标缺失时容易过抓、误抓或被干扰。作者提出 OBEYED-VLA，把 object-centric grounding 与 geometry grounding 从动作推理里解耦出来，用模块化、冻结的感知流水线先产出任务相关且几何聚焦的观察，再交给任意 VLA 做动作生成。新意不在更大模型，而在更干净的接口设计。
* **核心方法与证据**: HTML 摘录显示方法由两级感知模块组成。首先是 VLM 驱动的 object-centric grounding，通过多视角 set-of-mark prompting 找到与指令相关的区域；随后几何 grounding 把这些区域转成 masked depth 表示，让动作模型接收更聚焦的空间信号。实验问题设计也很扎实，直接检验六件事：对细粒度语言指令的服从、对背景与布局变化的稳健性、对未见目标和干扰物的泛化，以及 object-centric、两阶段解耦和 geometry-aware grounding 各自的贡献。证据上，HTML 明确来自真实 UR10e 双视角桌面实验。
* **正文要点**:
  - 作者明确批评单体端到端 VLA 会侵蚀语言条件 visual grounding。
  - OBEYED-VLA 将冻结感知模块接到任意 VLA 前，强调模块化增强而非替换整个策略。
  - 几何 grounding 使用 masked depth，而不只依赖 RGB 语义区域。
* **为什么值得跟**:
  - 它给 clutter-robust VLA 提供了一条很实用的工程路径：先把看清楚做好，再谈动作泛化。
  - 模块化接口意味着该方法可能作为通用前端插入现有 VLA，而不必重训整套系统。
  - 真实机器人双视角实验让结论更接近部署问题，而非纯模拟改分。
* **风险 / 保留意见**:
  - 感知前端冻结虽然稳定，但在任务分布明显变化时可能引入不可学习的上限。
  - 多模块串联会增加系统复杂度，错误若出现在 grounding 前端，后端动作模型未必能补救。
* **建议先看**: 建议先看作者列出的失败模式，再看 object-centric 与 geometry grounding 分别修复了哪些失效。上传 PDF 后，优先核查各类干扰设置是否足够严格，以及模块化增益是否跨 VLA 一致。
* **关键词**: `clutter robustness` `object-centric grounding` `geometry grounding` `masked depth` `OBEYED-VLA`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
* **读 PDF 先核查**:
  - set-of-mark prompting 在多视角之间如何做一致性约束，是否会出现跨视角目标错配？
  - masked depth 的收益来自去背景噪声，还是来自显式几何信号本身？
  - 该模块化前端对不同底座 VLA 的增益是否稳定，还是只对特定动作头有效？
* **上传 PDF 后优先看**:
  - 真实机器人实验设置与干扰场景构造部分。
  - object-centric、两阶段解耦和 geometry grounding 的消融章节。
  - 跨背景、未见物体与目标缺失等失败案例可视化与误差分析。

## Watchlist

### [W1]. PokeVLA: Empowering Pocket-Sized Vision-Language-Action Model with Comprehensive World Knowledge Guidance [[HTML]](https://arxiv.org/html/2604.20834) [[PDF]](https://arxiv.org/pdf/2604.20834)
* **Paper ID**: `2604.20834`
* **Authors**: Yupeng Zheng, Xiang Li, Songen Gu, Yuhang Zheng, Shuai Tian, Weize Li, Linbo Wang, Senyu Fei, Pengfei Li, Yinfeng Gao, Zebin Xing, Yilun Chen, Qichao Zhang, Haoran Li, Wenchao Ding
* **Author Priority**: Standard
* **为什么还值得留意**: PokeVLA 进入 shortlist，主要因为它踩中了“轻量 VLA + 显式世界知识/空间感知注入”这条很现实的落地方向，而且 HTML 给出的两阶段训练范式相对完整，数据规模、预训练目标和 LIBERO/LIBERO-Plus 评测也比较清楚。它没有进最终精选，是因为叙事更偏“做一个更小但更强的基础模型”，研究锋利度不如 dWorldEval 的评估代理、CodeGraphVLP 的非马尔可夫状态建模，或 RedVLA 的安全红队新问题定义。换句话说，它是值得持续跟踪的工程型强作，但今天不是最强的研究信号承载者。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. GazeVLA: Learning Human Intention for Robotic Manipulation [[HTML]](https://arxiv.org/html/2604.22615) [[PDF]](https://arxiv.org/pdf/2604.22615)
* **Paper ID**: `2604.22615`
* **Authors**: Chengyang Li, Kaiyi Xiong, Yuan Xu, Lei Qian, Yizhou Wang, Wentao Zhu
* **Author Priority**: Standard
* **为什么还值得留意**: GazeVLA 值得保留在 watchlist，因为它把 human intention 作为跨 embodiment 的中间表示，这对“如何从大规模人类数据迁移到机器人”是很有潜力的方向。HTML 里给出的大规模第一视角数据聚合、手与 gaze 联合建模、以及 VLIA 架构都说明它不是简单做人类模仿。之所以没进最终精选，是因为今天主线更集中在 VLA 本体的长时程状态、评估代理、安全与 clutter grounding，而 GazeVLA 更像一条很有前景但尚未完全并入当前主线的学习范式分支。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. LeHome: A Simulation Environment for Deformable Object Manipulation in Household Scenarios [[HTML]](https://arxiv.org/html/2604.22363) [[PDF]](https://arxiv.org/pdf/2604.22363)
* **Paper ID**: `2604.22363`
* **Authors**: Zeyi Li, Yushi Yang, Shawn Xie, Kyle Xu, Tianxing Chen, Yuran Wang, Zhenhao Shen, Yan Shen, Yue Chen, Wenjun Li, Yukun Zheng, Chaorui Zhang, Siyi Lin, Fei Teng, Hongjun Yang, Ming Chen, Steve Xie, Ruihai Wu
* **Author Priority**: Standard
* **为什么还值得留意**: LeHome 进入 shortlist 的理由很明确：它补的是 household deformable manipulation 这一长期缺位的模拟基础设施，而且作者明确强调高保真模拟与 sim-to-real 支持，这对后续世界模型、策略学习和评测都重要。没有进入最终精选，主要是因为它更偏平台与环境建设，而不是今天最核心的 VLA/world model 方法创新本身。若你后续要追 sim2real 或可变形家居任务，这篇的跟踪优先级会明显上升。
* **证据来源**: arXiv HTML (Introduction, Experiments)

### [W4]. Wiggle and Go! System Identification for Zero-Shot Dynamic Rope Manipulation [[HTML]](https://arxiv.org/html/2604.22102) [[PDF]](https://arxiv.org/pdf/2604.22102)
* **Paper ID**: `2604.22102`
* **Authors**: Arthur Jakobsson, Abhinav Mahajan, Karthik Pullalarevu, Krishna Suresh, Yunchao Yao, Yuemin Mao, Bardienus Duisterhof, Shahram Najam Syed, Jeffrey Ichnowski
* **Author Priority**: Standard
* **为什么还值得留意**: Wiggle and Go! 值得进 watchlist，因为它把系统辨识前置到高风险动态绳索操作之前，这种“先探再做”的思想与 sim2real、world-aware control 都高度相关。HTML 里还给出了从安全 probing 到下游抛掷/搭放的迁移主张，说明它不是单任务技巧。它没进最终精选，是因为主题更偏动态绳索操控和系统辨识，和今天以 VLA、world action model、长时程操控为中心的主线相比略偏，但作为 sim2real 支线很值得继续盯。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W5]. Learning-augmented robotic automation for real-world manufacturing [[HTML]](https://arxiv.org/html/2604.22235) [[PDF]](https://arxiv.org/pdf/2604.22235)
* **Paper ID**: `2604.22235`
* **Authors**: Yunho Kim, Quan Nguyen, Taewhan Kim, Youngjin Heo, Joonho Lee
* **Author Priority**: Standard
* **为什么还值得留意**: 这篇制造业部署论文进入 shortlist，是因为它提供了一个少见的强现实检验：学习控制器与神经 3D 安全监控如何嵌进真实产线，而不是停留在实验室 demo。HTML 的信息表明作者非常重视 FSM、预教动作段、可插拔 learned primitive 和安全回退，这些都很有工业参考价值。没有进入最终精选，是因为其创新更偏系统集成与部署验证，不像最终入选论文那样直接推动 VLA/world model 的方法前沿。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
