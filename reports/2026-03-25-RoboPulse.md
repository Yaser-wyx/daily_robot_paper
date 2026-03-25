# RoboPulse | 2026-03-25

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 79 papers scanned · 10 shortlisted · 6 editor's picks

今天这组 shortlist 的主线很清楚：VLA 正在从“看懂并模仿”转向“具备空间 grounding、物理可执行性、跨模态触觉补足，以及更强的 sim2real 证据链”。最终精选之所以成立，不只是因为题目热，而是它们分别补上了当前 embodied 控制最真实的短板：移动操作的空间表示、接触场景的不可观测状态、仿真到真实的泛化机制、视频世界模型的物理对齐，以及代码代理与 VLA 的结构化互补。核心作者里，Hao Su、Cewu Lu、Yuke Zhu 这三条线今天最值得优先跟踪，分别对应空间化 VLA、视觉之外的多模态行动建模，以及 manipulation agent 评测与程序化控制框架。整体看，研究焦点正从单纯扩大模型容量，转向让动作生成真正“可落地、可解释、可迁移”。

## 今日信号

- 今天最值得记住的研究信号是：VLA/世界模型的竞争焦点正从“是否能生成动作”转向“动作是否具备空间 grounding、物理合理性与真实可执行性”。
- 今天最值得记住的研究信号是：sim2real 不再只是堆随机化技巧，受控变量拆解与 RL 后训练正在成为更可复用的经验框架。
- 今天最值得记住的研究信号是：机器人行动建模正在明显走向多模态和结构化，两端分别体现为触觉等新观测进入 world model，以及代码代理/抽象接口被系统化评测。

## Editor's Picks

### [1]. SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation [[VIP]] [[HTML]](https://arxiv.org/html/2603.22760) [[PDF]](https://arxiv.org/pdf/2603.22760) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.22760`
* **Authors**: Ruisen Tu, Arth Shukla, Sohyun Yoo, Xuanlin Li, Junxi Li, Jianwen Xie, Hao Su, Zhuowen Tu
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，它抓住了移动操作里 VLA 最缺的空间 grounding 与训练稳定性问题。
* **问题与切口**: 这篇工作瞄准的是 VLA 从桌面场景走向真实家庭移动操作时暴露出的核心断层：模型既要理解房间级布局，又要捕捉物体几何和连续控制细节，单靠标准 imitation learning 很难兼顾。SG-VLA 的切口不是盲目增大模型，而是把“空间对齐”作为第一性问题，通过多视角 RGB-D 输入和辅助任务共训，把语义理解、几何感知与动作生成绑到同一表示空间里。相对已有偏桌面、偏单视角的 VLA 路线，它更像是在补移动操作真正需要的表示基础设施。
* **核心方法与证据**: 方法上，SG-VLA 不是简单把 VLM 接到动作头，而是围绕移动操作的空间需求重组输入与训练流程：视觉侧用 DINOv2+SigLIP 融合几何与语义，多视角 RGB-D 提供全局布局与局部物体信息，语言侧用 Qwen2.5-0.5B 统一推理，并可接一个 Flow Matching 连续动作专家。正文里最关键的证据是训练稳定性观察：作者发现随机初始化的辅助解码器直接共训会以噪声梯度破坏预训练表征，因此采用 progressive training。HTML 摘录支持“显著提升”和“空间表征更可解释”的方向性结论，但不支持精确量化幅度判断。
* **正文要点**:
  - 1.3B 主干结合 DINOv2 与 SigLIP 双视觉编码，并支持多视角 RGB-D 输入。
  - 作者明确指出随机初始化辅助解码器直接共训会伤害预训练 VLM 表征，因此采用渐进式训练。
  - 结论强调辅助监督带来更可解释的空间表征，并改善移动操作中的场景理解与控制精度。
* **为什么值得跟**:
  - 它把 VLA 的瓶颈从“模型不够大”重新定义为“空间表示和训练方式不对”。
  - 如果辅助监督真的稳定提升可解释空间表征，这条路线对导航+操作一体化非常关键。
  - Hao Su 这条线值得跟，因为它直接对准家庭机器人最难扩展的移动操作场景。
* **风险 / 保留意见**:
  - 现有摘录没有给出具体任务分布与增益拆解，辅助任务是否普适仍需看完整实验。
  - 模型依赖多视角 RGB-D，真实部署中的传感器成本、同步误差与缺失模态鲁棒性仍是风险。
* **建议先看**: 先抓住它如何把“空间 grounding”变成训练目标，而不只是输入堆料。随后重点核查渐进式共训为何稳定，以及多视角深度和辅助任务各自贡献了什么。
* **关键词**: `VLA` `mobile manipulation` `spatial grounding` `multi-view depth` `auxiliary co-training`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 渐进式训练的具体切换准则是什么，何时解冻辅助分支才不会继续污染主干表征？
  - 多视角深度带来的收益主要来自全局布局恢复、遮挡缓解，还是对连续动作精度的直接约束？
  - 可选 Flow Matching 动作专家在何种任务上真正必要，哪些场景仅靠主干就足够？
* **上传 PDF 后优先看**:
  - 方法章节里总体架构与辅助解码器设计
  - 训练策略章节里 progressive co-training 的阶段划分与消融
  - 实验章节里多视角深度、辅助任务、动作专家三类 ablation

### [2]. VTAM: Video-Tactile-Action Models for Complex Physical Interaction Beyond VLAs [[VIP]] [[PDF]](https://arxiv.org/pdf/2603.23481) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.23481`
* **Authors**: Haoran Yuan, Weigang Yi, Zhenyu Zhang, Wendi Chen, Yuchen Mo, Jiashi Yin, Xinzhuo Li, Xiangyu Zeng, Chuan Wen, Cewu Lu, Katherine Driggs-Campbell, Ismini Lourentzou
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先关注，尤其适合看接触丰富任务的人，但目前证据更多停留在方向正确而非已被充分验证。
* **问题与切口**: VTAM 试图解决一个被纯视觉 VLA/VAM 持续低估的问题：在复杂物理接触中，决定动作是否稳定的关键信号往往根本不在图像里。仅靠视频世界建模，模型可以生成时序上连贯的动作，却未必真的理解接触建立、滑移、受力变化这些隐含状态。它的核心切口因此不是再强化视觉表征，而是把触觉作为与视频并行的 grounding 信号接入行动模型，让系统在接触密集任务里获得更贴近物理真实的状态估计。相较常见 VLA 路线，它代表的是“从视觉主导走向视觉+触觉联合行动建模”的升级。
* **核心方法与证据**: 从摘要可读信息看，VTAM 以 Video-Action Model 为底座，把 tactile streams 作为补充观测注入预训练视频 transformer，并采用轻量化的 modality transfer finetuning，以避免完全重训的大成本。其论证逻辑很明确：视觉 token 对力调节、接触切换和微小交互状态的编码不足，因此在复杂物理交互中容易出现动作不稳或不精确。摘要支持“触觉能作为 grounding signal 补足视觉盲区”的方法动机，但目前缺少 HTML 正文，尚无法确认融合层级、训练目标、基线强度和实验证据边界，因此对效果判断需保持保守。
* **正文要点**:
  - 论文核心主张是把触觉作为视觉之外的 grounding 信号，补足接触场景中不可见的交互状态。
  - 方法描述集中在预训练视频 transformer 上，通过轻量 modality transfer finetuning 接入 tactile streams。
  - 现有证据主要来自摘要，支持其定位为多模态 world modeling 框架，但正文级模块细节和实验拆解仍缺失。
* **为什么值得跟**:
  - 这条路线直击视觉 VLA 在接触和受力场景中的系统性盲点。
  - 如果轻量接入预训练视频模型可行，多模态升级的工程门槛会显著降低。
  - Cewu Lu 参与使其更值得跟踪，因为这可能延展到更完整的物理交互建模框架。
* **风险 / 保留意见**:
  - 当前只有摘要回退信息，方法细节和实验可信度无法像 HTML 正文论文那样充分核查。
  - 触觉模态常受硬件布置和标定影响，跨平台泛化与数据规模需求可能高于摘要呈现。
* **建议先看**: 这篇先别急着看成又一个多模态堆料模型，重点要核查触觉是被当作条件、对齐监督还是隐状态补全信号。拿到 PDF 后优先看 tactile 接入位置以及接触类任务上的失败模式变化。
* **关键词**: `video-action model` `tactile sensing` `contact-rich manipulation` `multimodal world model` `modality transfer`
* **证据来源**: Abstract fallback
* **读 PDF 先核查**:
  - 触觉流是在 token 级早融合、时序级中融合，还是仅用于后训练对齐，三者影响会很不一样。
  - 轻量 modality transfer finetuning 是否真的避免了视觉主干退化，还是只是降低了训练成本？
  - 性能提升主要来自触觉对接触转移的判别，还是对力控制连续性的改善？
* **上传 PDF 后优先看**:
  - 方法章节里 tactile token 与视频 transformer 的融合位置
  - 实验章节里 contact-rich 任务与视觉-only 基线比较
  - 误差分析章节里接触转移、力调节和失败案例类型

### [3]. Grounding Sim-to-Real Generalization in Dexterous Manipulation: An Empirical Study with Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2603.22876) [[PDF]](https://arxiv.org/pdf/2603.22876) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.22876`
* **Authors**: Ruixing Jin, Zicheng Zhu, Ruixiang Ouyang, Sheng Xu, Bo Yue, Zhizheng Wu, Guiliang Liu
* **Author Priority**: Standard
* **一句话结论**: 非常值得优先看，它不是再讲 sim2real 口号，而是在 VLA 语境下认真拆机制。
* **问题与切口**: 这篇工作的价值不在于提出一个更大的 generalist policy，而在于把“哪些 sim2real 技术真的对 VLA 有用”这件事做成了受控经验研究。作者抓住当前领域一个常见问题：大家都在谈随机化、保真度、RL 微调，但缺少落到真实灵巧操作任务上的系统比较。论文以 OpenVLA-OFT 为研究载体，围绕 zero-shot sim2real 泛化构建 benchmark，去分辨空间随机化、外观随机化、时间粒度扰动和仿真质量各自起什么作用。相对已有零散经验，它更像是在为 VLA 的 sim2real 建立可迁移的经验法则。
* **核心方法与证据**: 方法上，这篇并未提出全新 VLA 架构，而是以 OpenVLA-OFT 为主体，在真实灵巧操作任务上系统考察不同 sim2real 技术如何影响 zero-shot 泛化。HTML 摘录给出了较完整的模型链路：双视觉主干、语言融合、proprioception 投影、双向注意力并行解码、连续动作 MLP 输出、动作 chunk 预测，以及 FiLM 语言调制视觉特征。实验脉络则强调 controlled benchmark 与在线真实机器人评测平台，重点比较空间随机化、外观随机化、帧级与 episode 级扰动、仿真保真度以及 RL 微调。证据边界在于摘录没有给出各因素效应大小与统计显著性，只能确认主次排序与趋势。
* **正文要点**:
  - 基于 OpenVLA-OFT，并在视觉、语言、proprioception 与连续动作预测链路上做了完整 generalist policy 适配。
  - 结论明确指出空间 domain randomization 是主效应，appearance randomization 提供互补收益。
  - 作者还报告了 frame-wise randomization、高保真模拟器与 RL fine-tuning 对 sim2real 均有正向作用。
* **为什么值得跟**:
  - 它给 VLA 的 sim2real 讨论提供了比“多加 randomization”更细的设计依据。
  - 论文把 RL fine-tuning 拉回 sim2real 主线，提示 VLA 与 RL 的结合不只是后处理。
  - 如果 benchmark 设计扎实，这类工作会比单次 SOTA 更能影响后续实验范式。
* **风险 / 保留意见**:
  - 若真实测试集覆盖面仍有限，结论可能更适用于特定灵巧操作而非一般 VLA 场景。
  - 基于单一主干家族做结论时，部分发现可能混入 OpenVLA-OFT 自身架构偏置。
* **建议先看**: 先把它当成一篇“变量拆解论文”而不是新模型论文来读。优先核查 benchmark 设计是否真的把环境因素解耦，以及不同随机化和 RL 微调的交互是否被讲清楚。
* **关键词**: `sim2real` `VLA` `dexterous manipulation` `domain randomization` `RL fine-tuning`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 空间随机化为什么成为主导因素，具体覆盖的是相机位姿、物体布局还是接触几何扰动？
  - frame-wise 随机化优于 episode-wise 的原因，是更强的数据覆盖，还是更贴近真实观测噪声结构？
  - RL fine-tuning 的收益主要体现在 OOD 鲁棒性、动作纠偏，还是对语言条件泛化也有帮助？
* **上传 PDF 后优先看**:
  - 实验设置章节里真实测试集因素设计与解耦原则
  - 消融章节里空间/外观随机化与 frame-wise/episode-wise 比较
  - 真实机器人评测章节里 RL fine-tuning 前后及 OOD 结果

### [4]. ABot-PhysWorld: Interactive World Foundation Model for Robotic Manipulation with Physics Alignment [[PDF]](https://arxiv.org/pdf/2603.23376) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.23376`
* **Authors**: Yuzhi Chen, Ronghan Chen, Dongjie Huo, Yandan Yang, Dekang Qi, Haoyun Liu, Tong Lin, Shuang Zeng, Junjin Xiao, Xinyuan Chang, Feng Xiong, Xing Wei, Zhiheng Ma, Mu Xu
* **Author Priority**: Standard
* **一句话结论**: 值得纳入最终精选，因为它正面回答了 world model 最关键的痛点：视频好看不等于物理上能执行。
* **问题与切口**: 这篇工作切中视频 world model 在机器人里最尴尬的一点：生成结果可以非常逼真，却仍然违背最基本的物理规律，导致它既不能可靠规划，也难以转成可执行动作。ABot-PhysWorld 的新意在于不再把这类问题视为采样噪声，而是把“物理对齐”提升为后训练目标本身。它结合大规模带物理意识标注的 manipulation 视频、偏好优化式后训练和专门抑制非物理行为的判别机制，试图把视觉 realism、物理 plausibility 与 action controllability 一起拉到同一框架里。对于 World Action Model 路线，这是很关键的修正。
* **核心方法与证据**: 现有信息来自摘要，因此只能抓住方法主干。ABot-PhysWorld 以 14B Diffusion Transformer 为底座，目标是在保证视觉真实感的同时，让生成视频满足操作物理可行性与动作可控性。作者提出的关键做法是基于 physics-aware 标注数据进行后训练，并用 DPO 框架配合 decoupled discriminators，抑制物体穿透、反重力等不物理行为，同时尽量保留画面质量；另有 parallel context block 处理空间化动作注入。摘要还提到一个训练无关的 EZSbench 用于测试泛化，但在缺少 HTML 正文时，尚无法核查判别器定义、奖励来源及 benchmark 难度。
* **正文要点**:
  - 核心主张是视频世界模型需要 physics alignment，否则会生成穿模、反重力等对机器人无效的 rollout。
  - 摘要给出三项关键组件：三百万 manipulation clips 的 physics-aware 标注、基于 DPO 的后训练、以及 decoupled discriminators。
  - 另一个亮点是 parallel context block，用于更精确的空间动作注入和跨 embodiment 控制。
* **为什么值得跟**:
  - 它提醒领域不要把生成视频质量误当成机器人可用性的代理指标。
  - 若 physics alignment 方案成立，世界模型将更有机会成为真实控制前端而非演示工具。
  - 这类工作也在推动 world model 评测从感知指标转向物理与可执行性指标。
* **风险 / 保留意见**:
  - 目前只有摘要证据，三百万标注数据与 14B 模型的可复现性、成本和数据偏置无法充分判断。
  - 物理 plausibility 与控制可执行性并不完全等价，摘要尚不能证明两者都被稳健解决。
* **建议先看**: 拿到 PDF 后先验证它的 physics alignment 到底是数据标注驱动、偏好学习驱动，还是判别器约束主导。其次要看 EZSbench 是否真的避免了训练集泄漏和任务绑定。
* **关键词**: `world foundation model` `physics alignment` `diffusion transformer` `DPO post-training` `action-controllable video`
* **证据来源**: Abstract fallback
* **读 PDF 先核查**:
  - DPO 与 decoupled discriminators 分别在抑制哪类不物理行为，是否存在目标冲突？
  - parallel context block 的动作注入是对空间区域显式绑定，还是仅改善条件控制精度？
  - EZSbench 如何保证训练无关评价，而不是换一种形式的分布内测试？
* **上传 PDF 后优先看**:
  - 方法章节里 DPO post-training 与 decoupled discriminators 的目标构造
  - 数据章节里 physics-aware annotation 的来源与标注粒度
  - 评测章节里 EZSbench 的设计原则与跨 embodiment 泛化结果

### [5]. EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards [[HTML]](https://arxiv.org/html/2603.17808) [[PDF]](https://arxiv.org/pdf/2603.17808) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.17808`
* **Authors**: Ruixiang Wang, Qingming Liu, Yueci Deng, Guiliang Liu, Zhen Liu, Kui Jia
* **Author Priority**: Standard
* **一句话结论**: 这是今天最该细读的 world model 论文之一，因为它把“视频可看”真正改成了“动作可执行”。
* **问题与切口**: EVA 直指视频世界模型在机器人中的核心错位：模型可以生成视觉上连贯、语义上合理的未来视频，但这些 rollout 一旦交给逆动力学模型转成控制命令，常常会暴露出刚体约束、运动学连续性或动作稳定性上的问题。作者把这种错位定义为 executability gap，并据此提出一种更贴近控制的对齐方式。与其单纯优化像素或潜变量似然，EVA 让视频生成器对“由该视频隐含出来的动作是否平滑、是否满足机器人约束”负责，因此本质上是在把世界模型训练目标向 action feasibility 收紧。
* **核心方法与证据**: EVA 的方法脉络非常清楚：作者认为视频世界模型的问题不只是视觉失真，而是生成 rollout 与机器人可执行控制之间存在 executability gap。为此，他们先训练一个逆动力学模型，用短时窗视觉序列回归动作；再把生成视频经 IDM 解码后的动作平滑性和是否满足运动学约束，转成对视频生成器的奖励；最后用这个奖励对预训练 latent video diffusion world model 做强化式后训练。HTML 还给出 IDM 结构与执行流程，包括 spatial softmax、MLP 动作回归及 receding-horizon 执行。证据层面，论文同时报告人工 rollout 评分、仿真任务成功率和真实机器人 seen/OOD 成功率，这是比只看视频质量更扎实的评测链。
* **正文要点**:
  - EVA 用逆动力学模型把生成视频映射回动作，再把动作平滑性与运动学约束变成视频模型的奖励信号。
  - 实验设置覆盖 RoboTwin 2.0 仿真和真实双臂机器人，并采用 receding-horizon execution。
  - 评测不仅看任务成功率，还包含针对 embodiment-specific failure 的结构化人工评分。
* **为什么值得跟**:
  - 它为视频 world model 提供了一个比视觉逼真度更接近机器人目标的训练信号。
  - 这条路线天然连接 world model、IDM 与 RL post-training，是 RL+VLA/世界模型融合的代表。
  - 如果方法稳健，未来 world model 评测会更强调 executability 而非纯生成质量。
* **风险 / 保留意见**:
  - IDM 本身若存在分布偏差，奖励就可能把视频模型推向“迎合 IDM”而非真实可执行。
  - 当前证据强调任务成功与人工评分，但长期闭环稳定性和复杂接触场景泛化仍需进一步核查。
* **建议先看**: 优先顺着“executability gap”这条主线读：先看 IDM 奖励到底评估了什么，再看 RL 后训练如何改变 rollout 分布。随后核查真实机器人上的 seen/OOD 结果是否真的支持这个 gap 被缩小。
* **关键词**: `video world model` `inverse dynamics` `executability` `RL post-training` `robot planning`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - IDM 奖励对动作平滑与运动学限制的刻画是否足以覆盖接触稳定性等更复杂执行约束？
  - RL 后训练会不会牺牲视频多样性，换来更保守但更易执行的 rollout？
  - 在 receding-horizon 执行中，误差是被逐步纠正了，还是仅被重新规划掩盖？
* **上传 PDF 后优先看**:
  - 方法章节里 IDM 奖励定义与 RL post-training 目标
  - 实验章节里 human rating 维度与 embodiment-specific failure 分类
  - 真实机器人章节里 seen 与 OOD 任务、以及 receding-horizon 执行分析

### [6]. CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation [[VIP]] [[HTML]](https://arxiv.org/html/2603.22435) [[PDF]](https://arxiv.org/pdf/2603.22435) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.22435`
* **Authors**: Max Fu, Justin Yu, Karim El-Refai, Ethan Kou, Haoru Xue, Huang Huang, Wenli Xiao, Guanzhi Wang, Fei-Fei Li, Guanya Shi, Jiajun Wu, Shankar Sastry, Yuke Zhu, Ken Goldberg, Linxi "Jim" Fan
* **Author Priority**: Core VIP
* **一句话结论**: 非常值得优先看，它不是再做一个 agent demo，而是在认真测“代码代理到底差在哪”。
* **问题与切口**: CaP-X 关注的不是传统意义上的 VLA 模型训练，而是另一条越来越重要的 embodied 路线：让大模型以代码代理的形式调用感知、规划和控制模块。它的核心价值在于把这个方向从零散 demo 拉成可系统比较的研究对象。通过 CaP-Gym 和 CaP-Bench，论文追问一个更尖锐的问题：当前前沿模型究竟是在真正学会程序化机器人控制，还是高度依赖人类提供的抽象接口和脚手架。相较只报告单项成功案例的工作，这篇更像是为 manipulation coding agents 建立诊断框架。
* **核心方法与证据**: CaP-X 的贡献更偏研究基础设施，但含金量很高。论文把 Code-as-Policy 机器人代理拆成两层：CaP-Gym 提供一个可交互环境，让模型通过合成并执行程序来调用感知与控制 primitive；CaP-Bench 则系统考察不同抽象层级、交互方式和感知 grounding 下，前沿语言/视觉语言模型的表现。HTML 摘录中最有价值的证据不是某个模型胜负，而是趋势：单轮零样本 Pass@1 下，人类专家仍明显领先；高层抽象能稳定抬高表现，但会牺牲表达能力；增加多轮交互、结构化工具和 test-time compute 有助于缩小差距。这些结论对操控 agent 设计比单次 SOTA 更有指导性。
* **正文要点**:
  - CaP-X 由 CaP-Gym 与 CaP-Bench 组成，前者提供程序合成与执行环境，后者系统评测模型控制机器人操作的能力。
  - 跨 12 个模型的结果显示：人工设计抽象越强，性能越高；去掉这些先验后，前沿模型明显更依赖 scaffold。
  - 作者同时观察到，多轮交互、结构化输出和 test-time compute 扩展可以部分缩小这一差距。
* **为什么值得跟**:
  - 它让研究者能区分“模型能力提升”和“设计者先验注入”这两类常被混淆的收益来源。
  - 对 Yuke Zhu 这条线而言，这类 benchmark 会直接影响后续机器人 agent 的评测标准。
  - 它也提示代码代理与端到端 VLA 不是二选一，而可能是结构化互补关系。
* **风险 / 保留意见**:
  - 作为 benchmark 框架，它的结论受 primitive 设计和环境接口定义影响较大。
  - 若任务主要奖励可编程分解能力，结果未必能直接外推到高带宽闭环连续控制场景。
* **建议先看**: 先看 benchmark 到底如何控制 perception 与 control primitive 的抽象层级，这是理解全部结论的钥匙。然后再看单轮 zero-shot、人类专家与多轮 agentic setting 之间的差距是怎样被拆开的。
* **关键词**: `Code-as-Policy` `robot manipulation` `benchmark` `agentic test-time compute` `program synthesis`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
* **读 PDF 先核查**:
  - 抽象层级提升性能的收益，究竟来自搜索空间缩小，还是来自更强的隐式先验注入？
  - 多轮交互与结构化输出带来的提升，在不同模型家族上是否一致，还是主要利好闭源强模型？
  - CaP-Bench 的任务设置会不会天然偏好程序化控制范式，从而低估端到端 VLA 的潜力？
* **上传 PDF 后优先看**:
  - 基准设计章节里 abstraction、interaction、grounding 三个维度的定义
  - 实验章节里 12 个模型在单轮 zero-shot 与多轮设置下的对比
  - 讨论章节里 human expert gap 与 expressivity/scaffolding trade-off

## Watchlist

### [W1]. Video2Act: A Dual-System Video Diffusion Policy with Robotic Spatio-Motional Modeling [[HTML]](https://arxiv.org/html/2512.03044) [[PDF]](https://arxiv.org/pdf/2512.03044)
* **Paper ID**: `2512.03044`
* **Authors**: Yueru Jia, Jiaming Liu, Shengbang Liu, Rui Zhou, Wanhe Yu, Yuyang Yan, Xiaowei Chi, Yandong Guo, Boxin Shi, Shanghang Zhang
* **Author Priority**: Standard
* **为什么还值得留意**: Video2Act 进入 shortlist 的原因很充分：它抓住了视频 diffusion 表征里可迁移的空间与运动信息，并把这类表征显式接到 VLA 上，还提出了适合实时控制的异步双系统框架。之所以没有进入最终精选，是因为今天入选论文里已经有更直接、更尖锐地触达“可执行性”“物理对齐”与“sim2real 机制拆解”的工作；相比之下，它更像一条扎实的架构增强路线，而不是最强的研究拐点信号。
* **证据来源**: arXiv HTML (Introduction, Method)

### [W2]. Point What You Mean: Visually Grounded Instruction Policy [[HTML]](https://arxiv.org/html/2512.18933) [[PDF]](https://arxiv.org/pdf/2512.18933)
* **Paper ID**: `2512.18933`
* **Authors**: Hang Yu, Juntu Zhao, Yufeng Liu, Kaiyu Li, Cheng Ma, Di Zhang, Yingdong Hu, Guang Chen, Junyuan Xie, Junliang Guo, Junqiao Zhao, Yang Gao
* **Author Priority**: Standard
* **为什么还值得留意**: Point-VLA 值得关注，因为它把 VLA 长期存在的 referential ambiguity 问题变成了一个非常实用的接口设计问题：给语言再加显式视觉指向。HTML 里真实任务设置和自动标注管线也说明它不是只做概念展示。没有进最终精选，主要是因为它更偏任务接口与数据扩展层面的改进，研究外延不如今天几篇关于物理可执行性、触觉补全和 sim2real 机制的论文那么强。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. Agile-VLA: Few-Shot Industrial Pose Rectification via Implicit Affordance Anchoring [[HTML]](https://arxiv.org/html/2603.22899) [[PDF]](https://arxiv.org/pdf/2603.22899)
* **Paper ID**: `2603.22899`
* **Authors**: Teng Yan, Zhengyang Pei, Chengyu Shi, Yue Yu, Yikun Chen, Zilong Zhu, Zelin Fang, Kaile Guo, Zihang Wang, Peigen Tian, Bingzhuo Zhong
* **Author Priority**: Standard
* **为什么还值得留意**: Agile-VLA 有现实价值，尤其是在边缘设备、工业姿态矫正和高频控制受限场景中，它提出的隐式 affordance anchoring 与双流解耦都很有工程针对性。它没有进最终精选，是因为问题设置更垂直、应用面更偏工业 pose rectification，研究结论的普适性暂时弱于本次主线里那些能影响 broader VLA/world model 讨论的工作。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

### [W4]. Emergent Dexterity via Diverse Resets and Large-Scale Reinforcement Learning [[HTML]](https://arxiv.org/html/2603.15789) [[PDF]](https://arxiv.org/pdf/2603.15789)
* **Paper ID**: `2603.15789`
* **Authors**: Patrick Yin, Tyler Westenbroek, Zhengyu Zhang, Joshua Tran, Ignacio Dagnino, Eeshani Shilamkar, Numfor Mbiziwo-Tiapo, Simran Bagaria, Xinlei Liu, Galen Mullins, Andrey Kolobov, Abhishek Gupta
* **Author Priority**: Standard
* **为什么还值得留意**: OmniReset 值得放入 watchlist，因为它展示了大规模 RL 配合多样 reset 状态，如何在长时程、接触丰富任务中诱发更强 dexterity，并且明确对 sim-to-real 数据生成有意义。没有进入最终精选，一方面是它与今天的 VLA/world model 主线存在一步距离，另一方面当前摘录更突出 RL 配方本身，而不是它与语言条件或视觉-语言行动统一框架的直接结合。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
