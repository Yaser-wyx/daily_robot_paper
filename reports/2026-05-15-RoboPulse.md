# RoboPulse | 2026-05-15

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 69 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线很清楚：VLA 正在从“图像到动作”的单步模仿，转向带有 3D 几何、历史意图、闭环 RL、世界模型验证和通用奖励的系统化训练栈。最终精选保留了 3D 观测增强、短时意图建模、统一理解-想象-行动、世界模型 benchmark、分布式 VLA-RL 基础设施和轨迹比较奖励模型这六条互补路线。Any3D-VLA 有核心 VIP 作者 He Wang，值得优先跟踪其 3D 表征与 sim-to-real 设计；Robometer 有扩展 VIP 作者 Dieter Fox，值得关注其奖励模型是否会成为后续 VLA/RL 训练的通用监督接口。整体看，今天更像是“如何让 VLA 可闭环、可评估、可扩展训练”的一组拼图，而不只是单个 policy architecture 的更新。

## 今日信号

- VLA 的薄弱环节正在从语义理解转向空间、时间一致性和闭环交互，3D 点云、历史窗口和 latent rollout 都是在补同一个短板。
- World model 研究开始更重视“生成的视频能否变成可执行行为”，RoboWM-Bench 和 Slot-MPC 这类工作把评估重心从视觉逼真推向 embodiment-grounded control。
- RL+VLA 的瓶颈不只在算法，也在系统吞吐和奖励标定，D-VLA 与 Robometer 分别从基础设施和监督信号两端补齐训练闭环。

## Historical Rediscovery

- **Paper**: LaST-R1: Reinforcing Robotic Manipulation via Adaptive Physical Latent Reasoning [[HTML]](https://arxiv.org/html/2604.28192) [[PDF]](https://arxiv.org/pdf/2604.28192)
  - **Paper ID**: `2604.28192`
  - **来源日期**: 2026-05-08
  - **当时可能被低估的信号**: 当时因不是当日新 ID、且自定义大规模数据与真实部署细节待核查而降级，但“从 latent reasoning 到 action 的优化路线”本身是强信号。
  - **为什么现在值得再看**: 如果 2026 年的 VLA 竞争开始从 imitation scaling 转向部署后自适应和强化后训练，这篇可作为 RL 改造 VLA 行为策略的重点参照。
  - **建议动作**: 加入精读
  - **关键词**: `RL+VLA` `latent reasoning` `post-training` `robotic manipulation`
- **Paper**: Learning Visual Feature-Based World Models via Residual Latent Action [[HTML]](https://arxiv.org/html/2605.07079) [[PDF]](https://arxiv.org/pdf/2605.07079)
  - **Paper ID**: `2605.07079`
  - **来源日期**: 2026-05-11
  - **当时可能被低估的信号**: 当时因和 VLA 部署/动作推理的直接关系略弱而未精选，但“DINO feature residual + latent action”的设定可能低估了它向 WAM 扩展的价值。
  - **为什么现在值得再看**: 对 World Model 和 World Action Model 都有参考意义，尤其适合判断未来机器人世界模型是否必须生成像素，还是可以在视觉特征动态上完成规划或 RL。
  - **建议动作**: 加入精读
  - **关键词**: `World Model` `latent action` `visual RL` `feature dynamics`
- **Paper**: Reconstruction or Semantics? What Makes a Latent Space Useful for Robotic World Models [[HTML]](https://arxiv.org/html/2605.06388) [[PDF]](https://arxiv.org/pdf/2605.06388)
  - **Paper ID**: `2605.06388`
  - **来源日期**: 2026-05-08
  - **当时可能被低估的信号**: 当时因更像评测研究而被压低优先级，但“世界模型不能只按视觉重建质量选择 latent”是容易被方法论文掩盖的关键判断。
  - **为什么现在值得再看**: 如果你要比较 VLA/WAM 中的视觉表征、预测目标和规划可用性，这篇能提供路线判断依据，而不只是单个模型 recipe。
  - **建议动作**: 快速浏览
  - **关键词**: `World Model` `latent representation` `robotic evaluation` `semantics`
- **Paper**: CRAFT: Counterfactual-to-Interactive Reinforcement Fine-Tuning for Driving Policies [[HTML]](https://arxiv.org/html/2605.04470) [[PDF]](https://arxiv.org/pdf/2605.04470)
  - **Paper ID**: `2605.04470`
  - **来源日期**: 2026-05-07
  - **当时可能被低估的信号**: 当时因已有 driving RL/VLA 代表论文而被放到 watchlist，但它显式落在 VLA 与 world action model 语境下的后训练问题上。
  - **为什么现在值得再看**: 对 RL+VLA、真实部署评测和 closed-loop adaptation 都相关，虽然是驾驶域，但问题结构可迁移到机器人策略从离线模仿到交互部署的转变。
  - **建议动作**: 加入精读
  - **关键词**: `RL+VLA` `closed-loop deployment` `World Action Model` `post-training`
- **Paper**: CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models [[HTML]](https://arxiv.org/html/2605.06247) [[PDF]](https://arxiv.org/pdf/2605.06247)
  - **Paper ID**: `2605.06247`
  - **来源日期**: 2026-05-08
  - **当时可能被低估的信号**: 当时被视为 teacher-student 迁移工程，但 compact context 在文本 embedding 空间迁移 WAM 知识，可能是低成本适配不同具身模型的信号。
  - **为什么现在值得再看**: 如果 WAM 开始出现多模型、多机器人、多任务版本，跨 WAM 的上下文知识迁移会变成实际部署问题，值得提前跟踪。
  - **建议动作**: 继续跟踪
  - **关键词**: `World Action Model` `knowledge transfer` `parameter-efficient adaptation` `embodiment transfer`

## Editor's Picks

### [1]. Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds [[VIP]] [[HTML]](https://arxiv.org/html/2602.00807) [[PDF]](https://arxiv.org/pdf/2602.00807) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2602.00807`
* **Authors**: Xianzhe Fan, Shengliang Deng, Xiaoyang Wu, Yuxiang Lu, Zhuoling Li, Mi Yan, Yujia Zhang, Zhizheng Zhang, He Wang, Hengshuang Zhao
* **Author Priority**: Core VIP
* **一句话结论**: 值得优先看，因为 Any3D-VLA 把 VLA 的 2D 视觉脆弱性明确落到可操作的 3D 点云融合与 sim-to-real 深度偏差问题上。
* **关键词**: `VLA` `3D point cloud` `RGB-D` `Sim2Real` `spatial robustness`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

现有 VLA 多以 2D 图像作为视觉输入，语言和语义能力随大模型扩展而提升，但空间理解仍主要继承自 2D backbone，因此在小物体、视角变化和遮挡场景中容易失稳。机器人操作恰恰依赖精确的相对位置、尺度、可达性和遮挡关系，仅靠图像 patch 很难稳定表达这些几何约束。已有路线包括给 2D backbone 注入深度预训练或空间 encoder，也包括重建式 3D 表征，但摘录指出这些隐式空间先验仍有局限。Any3D-VLA 的动机是更直接地把 RGB-D 提升为点云，并处理 3D 数据稀缺以及仿真、传感器、估计深度之间的域差。

#### ⚙️ 核心方法

方法从一个 pilot study 出发，比较不同 observation space 和 visual representation，结论倾向于显式点云能更好补充对应 2D 表征。具体流程是利用相机内参把 RGB 图像和深度图提升到相机坐标系点云，再将稀疏 3D 结构压缩后与 2D patch 表征融合，用于 VLA 操作决策。摘录能确认作者重点讨论三类深度来源：仿真可导出高质量 metric depth，真实机器人常依赖消费级深度传感器或深度估计，估计深度又可来自单/多帧深度模型或前馈 3D 几何模型。新意不只是“加深度”，而是把深度噪声、尺度漂移和跨环境偏差作为 VLA 训练的核心问题处理。当前摘录只能确认其提出 Any3D-VLA 统一仿真、传感器和估计深度下的点云输入，并强调 compressed point clouds 与 2D patch 的融合；具体网络层级、token 对齐方式和损失设计需要 PDF 进一步核查。

#### 📊 实验与结果

实验摘录给出了较清晰的数据构造：作者在仿真中合成大规模 RGB-D 数据，基于 Objaverse LVIS 子集选择 290 个类别、10,680 个实例，在桌面 cluttered layout 中随机生成物体摆放。专家轨迹由 BoDex 生成候选抓取姿态，CuRobo 做一次性避障轨迹规划，并在 MuJoCo 中验证可执行性；Isaac Sim 用于渲染，并随机化光照、材质、背景和相机外参，相机内参与 RealSense D435 匹配。深度包括 Isaac Sim 直接导出的严格对齐深度，以及由模型从 RGB 估计的 metric depth。结论摘录声称，与隐式或重建式空间先验相比，融合原生稀疏 3D 结构更直接、更稳定，但具体成功率、消融数值和真实机器人结果在当前摘录中证据不足。

#### ⚠️ 风险 / 保留意见

- 点云质量高度依赖深度来源，真实传感器噪声和估计深度尺度漂移可能直接传导到动作预测。
- 当前摘录没有提供完整网络细节和量化结果，难以判断 3D 融合收益相对计算开销是否稳定。
- 仿真数据虽有随机化，但 Objaverse 桌面抓取分布与真实长时序操作仍可能存在任务偏差。

#### 💭 结论与启发

这篇对后续 VLA 系统设计的启发是：不要只把 3D 当作一个额外 encoder，而要把深度来源、尺度校准、点云压缩和 2D token 对齐一起设计。若要复现，可先做一个轻量版本：固定 OpenVLA/类似 VLA backbone，增加 RGB-D lifting 与 sparse point token 分支，重点比较仿真真深度、RealSense 深度和估计深度的鲁棒性差异。阅读 PDF 时应优先确认它的融合接口是否足够通用，以及对 sim-to-real depth bias 是否有实质缓解。

#### 🔎 读 PDF 先核查

- Any3D-VLA 的 compressed point clouds 是如何与 2D patch 表征对齐和融合的，融合发生在视觉 encoder、LLM token 层还是 action head 前？
- 作者如何隔离验证点云收益来自 3D 几何本身，而不是额外 depth supervision 或更大的输入容量？
- 面对传感器深度噪声和估计深度尺度漂移，Any3D-VLA 是否有显式归一化、校准或域随机化机制？

#### 📌 上传 PDF 后优先看

- 方法章节中的点云压缩、2D-3D 融合接口和 action prediction pipeline。
- 实验章节中 observation space / visual representation 的对比与消融。
- sim-to-real 或真实深度相关实验，尤其是传感器深度、仿真深度、估计深度之间的鲁棒性比较。

### [2]. IntentVLA: Short-Horizon Intent Modeling for Aliased Robot Manipulation [[HTML]](https://arxiv.org/html/2605.14712) [[PDF]](https://arxiv.org/pdf/2605.14712) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.14712`
* **Authors**: Shijie Lian, Bin Yu, Xiaopeng Lin, Zhaolong Shen, Laurence Tianruo Yang, Yurun Jin, Haishan Liu, Changti Wu, Hang Yuan, Cong Huang, Kai Chen
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为 IntentVLA 把 chunked VLA 的不稳定性归因到短时意图 aliasing，并给出历史条件化的直接修正。
* **关键词**: `Intent modeling` `partial observability` `action chunking` `VLA` `AliasBench`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

机器人模仿数据天然多模态：同一视觉-语言观察后可能接不同动作 chunk，因为演示者处在不同任务阶段、选择了不同局部路径，或刚刚做过不同动作。多模态本身不是问题，问题在于标准 frame-conditioned VLA 每次重规划只看当前帧和指令，在部分可观测场景下无法知道当前 episode 已经承诺了哪条局部 continuation，于是相邻 chunk 可能反复采样不同意图，造成 inter-chunk conflict 和执行抖动。这个问题对 VLA 尤其关键，因为 action chunking 提升了控制效率，却也放大了跨 chunk 一致性的要求。IntentVLA 的核心动机是用近期视觉历史恢复短时意图，而不是强行消除演示数据中的多样性。

#### ⚙️ 核心方法

作者把 manipulation 建模为部分可观测决策过程，并引入 latent short-horizon intent 的概念，表示局部 continuation mode、任务阶段或已经承诺的路径。标准 chunk policy 近似为只根据当前观察和语言预测未来动作 chunk，因此在 aliased conditioning 下会把多个可能 continuation 混在同一条件分布里。IntentVLA 改为使用有限视觉历史窗口作为紧凑证据，提取短时 intent representation，再用它条件化动作 chunk 生成。摘录能确认作者并不显式监督 intent label，而是让近期视觉观察承担 disambiguation 的作用；这点很重要，因为真实机器人数据通常没有“当前意图”标注。方法的新意在于把 VLA 的不稳定执行从“模型容量不足”改写为“局部承诺信息缺失”，并将解决方案限制在短时历史窗口，避免完整交互历史带来的计算和记忆负担。具体 intent encoder 结构、history window 长度、与 backbone 的注入位置仍需 PDF 核查。

#### 📊 实验与结果

实验核心是 AliasBench，基于 RoboTwin2 构建，包含 12 个操作任务、匹配的仿真训练数据和 held-out evaluation environments。它不是只测任务完成率，而是专门构造当前观察近似相同、但下一步动作需求不同的状态对，用来测试 VLA 能否利用近期上下文保持决策一致性。摘录还说明任务按导致 aliasing 的 latent factor 分组，目标是覆盖常见 manipulation pattern，而不是纯合成边角案例。结论声称最终方法可用近期视觉历史提取短时意图证据，在部分可观测下稳定 chunk generation。当前摘录没有给出具体成功率、baseline 名称或消融数字，因此只能判断其 benchmark 设计和问题定义有价值，效果强度需要进一步核查。

#### ⚠️ 风险 / 保留意见

- 历史窗口长度与采样频率可能高度敏感，太短无法 disambiguate，太长又可能引入无关视觉变化。
- AliasBench 基于仿真构建，真实机器人中的遮挡、光照和接触误差是否会改变 aliasing 分布仍不明确。
- 若 intent representation 学到的是数据集偏置而非局部承诺，跨任务泛化可能受限。

#### 💭 结论与启发

这篇值得作为 action chunk VLA 的诊断工具来读。后续做 VLA 或 diffusion/flow policy 时，不能只看单步 observation 是否足够，还要检查相邻 chunk 的意图一致性。复现上，AliasBench 的思想比具体模型更可迁移：可以在自己的任务中寻找“当前帧相似但历史不同”的状态对，专门评估 policy 是否突然换路。系统设计上，短历史视觉 token 可能是低成本提升稳定性的模块，尤其适合 partial observability 和多路径操作。

#### 🔎 读 PDF 先核查

- IntentVLA 的短时 intent representation 是通过何种 encoder 从视觉历史中得到的，它与语言指令和当前帧如何融合？
- AliasBench 中 aliased state pair 的构造标准是什么，是否有定量阈值保证当前观察足够相似但动作需求不同？
- 性能提升主要来自历史条件化本身，还是来自更大的输入 token 数、更多帧或训练数据增强？

#### 📌 上传 PDF 后优先看

- AliasBench 构造章节，特别是 12 个任务和四类 aliasing 因素的定义。
- 模型方法章节中的 history window、intent encoder 和 chunk decoder 接口。
- 消融实验，尤其是无历史、不同历史长度、显式/隐式 intent 表征的对比。

### [3]. Pelican-Unified 1.0: A Unified Embodied Intelligence Model for Understanding, Reasoning, Imagination and Action [[HTML]](https://arxiv.org/html/2605.15153) [[PDF]](https://arxiv.org/pdf/2605.15153) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.15153`
* **Authors**: Yi Zhang, Yinda Chen, Che Liu, Zeyuan Ding, Jin Xu, Shilong Zou, Junwei Liao, Jiayu Hu, Xiancong Ren, Xiaopeng Zhang, Yechi Liu, Haoyuan Shi, Zecong Tang, Haosong Sun, Renwen Cui, Kuishu Wu, Wenhai Liu, Yang Xu, Yingji Zhang, Yidong Wang, Senkang Hu, Jinpeng Lu, Nga Teng Chan, Yechen Wu, Yong Dai, Jian Tang, Xiaozhu Ju
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，但要带着审稿式谨慎读，因为 Pelican-Unified 1.0 提出理解、推理、想象和行动统一闭环，野心很大而摘录细节不足。
* **关键词**: `unified embodied intelligence` `world model` `imagination` `VLA` `compositional generalization`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

这篇的出发点是反对把 embodied intelligence 拆成独立视觉模型、语言模型、世界模型和动作策略后再串联。作者认为真实物理智能需要在同一自适应循环里整合理解、任务推理、未来想象和动作执行，因为 long-horizon coherence、组合泛化和 zero-shot transfer 往往发生在模块接口处，而不是单个组件内部。对 VLA/world model 方向来说，这正对应当前碎片化趋势的痛点：VLA 能输出动作但缺少未来想象，视频世界模型能生成未来但未必能驱动控制，规划器能组合技能但接口脆弱。Pelican-Unified 1.0 的价值在于提出一个 latent world space 下的统一范式，尝试把 reason-imagine-act 做成闭环。

#### ⚙️ 核心方法

当前摘录只能确认 Pelican-Unified 1.0 主张在 latent world space 中统一 world understanding、task reasoning、future imagination 和 action execution，而不是简单拼接多个专家网络输出，也不是把独立优化模块顺序组装成 pipeline。其核心概念是：智能体先在共享潜空间中对世界与任务进行抽象和对齐，再通过 imagination 预测或构造未来变化，并将这种想象能力直接迁移到 video-action model 以产生动作。摘录还强调“coupling”比单个组件强度更关键，暗示方法可能通过联合训练或统一表征把 world model 与 action policy 紧密绑定。实验描述中出现 UR5e 机械臂和 Tienkung 人形机器人，任务包含原子技能组合与 zero-shot transfer，因此方法至少覆盖了机械臂细粒度操作和人形平台场景。但具体模型结构、训练数据规模、latent space 形式、video-action 模型接口和损失函数在给定 HTML 摘录中没有足够证据，必须保守理解为一篇统一范式和系统展示型论文。

#### 📊 实验与结果

实验部分明确说评估落在真实世界场景，平台包括 UR5e robotic arm 和 Tienkung humanoid robot。评估围绕两种能力：compositional generalisation 与 zero-shot transfer。UR5e 组合泛化测试中，摘录给出 atomic tasks 包括 plug RJ45 和 waterproof，两者单独训练，训练数据中没有完整 chained demonstration；测试时机器人接收单条自然语言指令执行组合任务。作者用这个设置验证未见组合任务的执行，以及由 imagination-based world model 引导的细粒度操作。结论摘录声称 zero-shot transfer、组合技能使用和长时序一致性难以通过孤立增强单个模块获得。但当前摘录没有提供成功率、失败案例数量、baseline 或消融，因此证据边界是：可以确认真实平台和任务设计，不能确认定量优势幅度。

#### ⚠️ 风险 / 保留意见

- 论文目标宏大，但当前摘录缺少架构、训练细节和量化结果，容易出现概念强于可复现性的风险。
- 真实机器人展示若任务数量有限，可能不足以支撑“统一 embodied foundation model”的泛化主张。
- 统一潜空间会增加调试难度，一旦失败，很难区分是理解、想象、规划还是控制接口的问题。

#### 💭 结论与启发

这篇适合作为 world model + VLA 系统路线图阅读，而不是马上照搬实现。它提醒后续选题不要只优化视频预测质量或动作成功率，而要问想象结果是否能直接改变 action policy 的选择。若上传 PDF 后细节扎实，可以重点跟踪其 latent world space 如何同时服务语言推理、视频预测和动作生成；若细节偏系统演示，则更适合作为问题 framing 和实验设计参考。

#### 🔎 读 PDF 先核查

- Pelican-Unified 的 latent world space 具体承载哪些 token 或状态，是否同时用于视频生成、任务推理和动作解码？
- imagination phase 到 unified video-action model 的 zero-shot transfer 是参数共享、表征对齐还是生成数据蒸馏？
- 真实机器人实验是否包含与模块化 pipeline、无 imagination policy 或仅 VLA baseline 的直接对比？

#### 📌 上传 PDF 后优先看

- 系统架构章节，特别是 latent world space 与各能力模块的耦合方式。
- 训练流程章节，确认 understanding、reasoning、imagination、action 是否联合训练。
- 真实机器人实验和消融，尤其是组合泛化、zero-shot transfer、无 imagination 对照。

### [4]. D-VLA: A High-Concurrency Distributed Asynchronous Reinforcement Learning Framework for Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2605.13276) [[PDF]](https://arxiv.org/pdf/2605.13276) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.13276`
* **Authors**: Yucheng Guo, Yongjian Guo, Zhong Guan, Wen Huang, Haoran Sun, Haodong Yue, Xiaolong Xiang, Shuai Di, Zhen Sun, Luqiao Wang, Junwu Xiong, Yicheng Gong
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为 D-VLA 把 VLA+RL 的扩展瓶颈从算法讨论拉回到分布式系统吞吐和资源冲突。
* **关键词**: `distributed RL` `VLA training` `asynchronous pipeline` `ManiSkill` `system throughput`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

随着 OpenVLA、GR00T 等 VLA 模型变大，把 RL 用到 embodied foundation model 上会遇到很现实的系统问题：高保真物理仿真需要大量 CPU/GPU/内存资源，深度模型训练又需要 VRAM 和通信带宽，两者在同一集群中争抢资源，导致采样、推理和优化阶段互相阻塞。对 RL+VLA 来说，吞吐不是工程细节，而是决定能否做大规模 on-policy 或近 on-policy 训练的前提。传统 orchestration framework 可能在 LLM/VLM 训练中可用，但面对高频控制、动作 chunk、仿真并发和大模型 fine-tuning 的组合负载时，execution phase inefficiency 会成为硬瓶颈。D-VLA 的动机就是为大规模 embodied RL 提供高并发、低延迟的训练框架。

#### ⚙️ 核心方法

D-VLA 的核心是 Plane Decoupling：把高频训练数据交换与低频权重控制物理隔离，减少仿真执行和模型优化之间的干扰。摘录还提到四线程 Swimlane pipeline，用于重叠 sampling、inference 和 training，从而降低 GPU idle time。这个设计对应 VLA-RL 的典型异步结构：环境侧持续产生视觉、语言、状态和奖励相关轨迹，推理侧批量输出动作 chunk，训练侧消费样本并更新大模型或 PEFT 参数，权重同步则以较低频率广播给 actor。新意在于它不是提出新的 RL objective，而是针对 embodied workload 的异构性重排数据面和控制面。实验模型覆盖 diffusion-based VLA 和 OpenVLA-OFT 这类自回归 Transformer + PEFT 代表，说明框架目标是兼容不同 action generation paradigm。当前摘录能确认系统机制与评估方向，但具体通信协议、队列实现、容错策略和一致性语义需要 PDF 核查。

#### 📊 实验与结果

实验比较 D-VLA 与若干 SOTA orchestration frameworks，关注 computational efficiency、throughput scalability 和 hardware utilization。模型架构选择了两个代表 VLA 范式：一个 diffusion-based model，另一个是 OpenVLA-OFT，自回归 Transformer 并使用 PEFT；两者都配置为 action chunking prediction，以提高环境交互率并适配高频控制。仿真环境为 ManiSkill physical simulation。结论摘录明确写到 D-VLA 通过 Plane Decoupling 和 Swimlane pipeline 缓解 simulation 与 optimization 资源竞争，并在相关模型上达到最高 86% 吞吐提升。需要注意，摘录没有给出硬件配置、并发规模、baseline 名称和任务成功率细节，因此当前只能确认系统效率主张，不能判断算法性能提升是否同等显著。

#### ⚠️ 风险 / 保留意见

- 系统收益可能强依赖硬件拓扑、网络带宽、仿真器配置和模型大小，迁移到小集群未必同幅度受益。
- 异步 RL 会引入 policy lag 和样本陈旧问题，摘录未说明其对学习稳定性的影响。
- 如果只优化吞吐而缺少任务成功率或 sample efficiency 对照，可能高估实际训练价值。

#### 💭 结论与启发

这篇对做 VLA-RL 的团队很实用：先别急着改 RL loss，必须测清楚采样、推理、训练和权重同步哪一段在堵。D-VLA 的 plane/data-control 分离思想可以迁移到自己的训练栈，即使不完整复现，也可以把 actor、inference server、trainer、weight server 的频率和资源隔离开。阅读 PDF 时应特别关注它如何处理异步更新和 action chunk，因为这决定了吞吐提升是否会换来策略滞后。

#### 🔎 读 PDF 先核查

- Plane Decoupling 的数据面和控制面具体如何部署，是否需要专用网络、共享内存或特定调度器支持？
- D-VLA 如何控制异步训练中的 policy lag，是否有 staleness 统计或对学习稳定性的消融？
- 最高 86% 吞吐提升是在什么硬件、模型大小、并发 actor 数和仿真任务下取得的？

#### 📌 上传 PDF 后优先看

- 系统架构章节中的 Plane Decoupling 和 Swimlane pipeline。
- 实验设置中的硬件配置、并发规模、baseline orchestration framework。
- 吞吐、GPU 利用率、任务成功率或 sample efficiency 的联合结果与消融。

### [5]. RoboWM-Bench: A Benchmark for Evaluating World Models in Robotic Manipulation [[HTML]](https://arxiv.org/html/2604.19092) [[PDF]](https://arxiv.org/pdf/2604.19092) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2604.19092`
* **Authors**: Feng Jiang, Yang Chen, Kyle Xu, Yuchen Liu, Haifeng Wang, Zhenhao Shen, Jasper Lu, Shengze Huang, Yuanfei Wang, Chen Xie, Ruihai Wu
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为 RoboWM-Bench 把视频世界模型的评价从“看起来真”推进到“能否转成可执行机器人行为”。
* **关键词**: `world model benchmark` `embodied execution` `real-to-sim` `manipulation` `video-to-action`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

大规模视频 world model 已能生成视觉上连贯、逼真的未来，但机器人操作不只需要 perceptual realism，还要求交互符合物理约束，并能被具体机器人执行。现有 benchmark 往往评估视觉质量、物理 plausibility 或一般视频预测，却没有系统回答一个关键问题：预测出来的人手或机器人操作视频，能否转换成 embodied action sequence，并在物理环境里完成任务。这个缺口对 VLA 和 world model 很重要，因为很多路线希望用生成视频作为机器人学习监督；如果视频无法执行，监督信号可能会误导 policy。RoboWM-Bench 的动机就是提供 manipulation-centric、embodiment-grounded 的世界模型评估。

#### ⚙️ 核心方法

RoboWM-Bench 的方法是把生成的人手和机器人 manipulation videos 转换为可执行动作序列，再放入物理约束模拟环境验证。为了可访问、可复现和可扩展，benchmark 基于开源仿真环境，并覆盖 simulation-native scenarios 与 real-to-sim reconstructions。摘录能确认它使用 LeHome simulation engine，支持家庭操作场景中的刚体、关节物体和可变形物体。real-to-sim pipeline 包括场景重建、物体建模和位姿校准：背景用 4D Gaussian 表征保持视觉真实和空间一致性，交互物体通过 3D segmentation/reconstruction 获得刚体几何，关节和可变形物体按 LeHome 相关构造，物体位姿通过 pose estimation model 估计。评估指标包含 step-level 和 task-level execution metrics。新意在于把 world model 的输出接到 embodiment validation，而不是只比较生成视频本身。

#### 📊 实验与结果

摘录表明 RoboWM-Bench 覆盖 diverse object dynamics、task horizons 和 coordination requirements，并在标准化仿真与 real-to-sim 环境中验证生成交互是否可执行。实验内容从 HTML 中可确认的是：它面向 human-hand 与 robotic manipulation videos，通过动作转换和仿真执行进行 step-level 与 task-level 评价。方法部分强调 real-to-sim 能在减少对特定物理装置依赖的同时保留受控物理动力学。结论称该 benchmark 可为视频 world model 提供更 scalable 的 embodiment-grounded evaluation。当前摘录没有给出模型榜单、具体任务数量、指标公式或各模型分数，因此不能断言哪类 world model 表现最好，只能确认 benchmark 评估范式具有方向性价值。

#### ⚠️ 风险 / 保留意见

- video-to-action 转换本身可能成为误差来源，评估结果不一定只反映 world model 质量。
- 仿真验证虽可扩展，但 LeHome 和 real-to-sim 的物理保真度会影响 task-level 结论。
- 如果不同世界模型生成视角、手部形态或机器人 embodiment 不一致，标准化比较可能需要额外适配。

#### 💭 结论与启发

这篇对后续 world model 选题非常关键：视频生成模型若要服务机器人，评价必须落到可执行性。复现或使用时，可以把它作为筛选 world model 的中间层：先不训练 policy，而是检查生成未来是否能通过几何、接触和任务完成验证。对 VLA 训练而言，它也提示我们不要盲目用生成视频做数据增强，应该先用 embodiment-grounded metrics 过滤不可执行样本。上传 PDF 后要重点确认 video-to-action 的鲁棒性和指标定义。

#### 🔎 读 PDF 先核查

- RoboWM-Bench 如何从人手或机器人视频恢复可执行动作，失败时如何区分感知误差、动作转换误差和生成模型物理错误？
- step-level 与 task-level execution metrics 的定义是什么，是否能覆盖接触、约束、长时序和多物体协调？
- real-to-sim 场景的重建误差如何校准，是否会系统性偏向某些视频模型或任务类型？

#### 📌 上传 PDF 后优先看

- benchmark pipeline 章节，尤其是 video-to-action conversion 与 simulation execution。
- 指标定义章节，包括 step-level 和 task-level execution metrics。
- real-to-sim reconstruction 与不同 object dynamics/task horizon 的覆盖范围。

### [6]. Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons [[VIP]] [[HTML]](https://arxiv.org/html/2603.02115) [[PDF]](https://arxiv.org/pdf/2603.02115) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2603.02115`
* **Authors**: Anthony Liang, Yigit Korkmaz, Jiahui Zhang, Minyoung Hwang, Abrar Anwar, Sidhant Kaushik, Aditya Shah, Alex S. Huang, Luke Zettlemoyer, Dieter Fox, Yu Xiang, Anqi Li, Andreea Bobu, Abhishek Gupta, Stephen Tu, Erdem Biyik, Jesse Zhang
* **Author Priority**: Extended VIP
* **一句话结论**: 值得优先看，因为 Robometer 用轨迹比较扩展通用机器人奖励模型，可能直接服务 VLA 的 RL、数据过滤和失败检测。
* **关键词**: `reward model` `trajectory preference` `robot RL` `VLM` `dense reward`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

通用机器人 reward model 是把 VLA 从纯 imitation 推向 RL 或自我改进的关键接口，但现有方法常依赖 expert demonstrations 的逐帧 progress label。这种监督在大规模数据上很难扩展，因为真实机器人数据里有大量次优、失败和部分完成轨迹，绝对进度也常常含糊。仅靠 trajectory-local 的点式标签，模型可能学到局部进度，却缺少跨轨迹的全局排序能力。Robometer 的动机是引入人类认知中常见的比较判断，把 intra-trajectory progress supervision 与 inter-trajectory preference supervision 结合起来，使 reward model 能从成功、次优和失败轨迹中共同学习。它对 online RL、noisy imitation、failure detection 和 offline RL 都有潜在价值。

#### ⚙️ 核心方法

Robometer 的训练 recipe 有三根支柱：多样化数据集、预训练 VLM backbone、以及结合逐帧奖励和轨迹偏好的双目标。摘录中数据集 RBM-1M 聚合 100 万条轨迹，重点不是单纯最大化数量，而是覆盖 viewpoint、scene 和 embodiment 多样性；来源包括 Open-X、AGIBotWorld 等专家机器人数据、人类视频以及失败或未标注轨迹。符号上，每条 trajectory 包含图像观察、语言指令和一个末端 progress scalar；专家 demos 设为完成，部分进度数据使用已有 score，未标注失败轨迹设为 0。训练目标一方面用 frame-level loss 把 reward magnitude 锚定到专家数据，另一方面用 trajectory-comparison preference loss 施加全局排序约束。这样模型既能输出 dense reward，又能从失败和次优数据里学到“哪条轨迹更接近成功”。具体 VLM backbone、preference pair 构造细节和 loss 权重需要 PDF 核查。

#### 📊 实验与结果

实验围绕三个问题：Robometer reward 在未见任务和 embodiment 上是否反映任务进度；各组件贡献多大；以及它对下游 robot learning 是否优于 baseline。baseline 摘录明确包括 VLAC-8B 和 GVL，其中 VLAC-8B 使用 300k 人类和机器人轨迹训练，GVL 通过预训练闭源 LLM 对打乱视频帧预测进度，摘录称使用 GPT-5 mini 作为闭源模型代表。下游实验还出现一个 play dataset：50 条轨迹，每条包含五个随机顺序执行的任务，包括 uncap the red pen、open the bottle、open the red drawer、stir the pot 和 unzip the pencil case，使用 Trossen Stationary AI bimanual setup，并有三路相机视角。当前摘录没有给出完整分数表，但能确认其评价覆盖 reward evaluation、ablation 和 policy learning。

#### ⚠️ 风险 / 保留意见

- 把未标注失败轨迹 progress 设为 0 简洁可扩展，但可能误伤包含部分有效进展的失败轨迹。
- 轨迹偏好构造若依赖启发式标签，可能把数据集偏差放大为 reward 偏差。
- 通用 reward model 部署到 RL 时可能产生 reward hacking，需要真实任务成功率和失败案例验证。

#### 💭 结论与启发

Robometer 对后续 VLA-RL 很有参考价值：大模型 policy 需要的不只是更强 actor，也需要可扩展、可比较、能处理失败数据的 reward。复现时可先从小规模轨迹比较做起，用现有 VLM backbone 训练 dense reward，再测试其是否能排序成功、部分成功和失败轨迹。系统设计上，它也可作为数据过滤器或 replay buffer scorer，用来挑选更有价值的 correction / recovery 数据。阅读 PDF 时应重点看 preference pair 的来源和下游 RL 是否真的受益。

#### 🔎 读 PDF 先核查

- Robometer 的 trajectory-comparison preference 是如何构造的，是否包含人工偏好、自动标签或基于 progress scalar 的派生排序？
- frame-level loss 与 preference loss 的权重如何影响 dense reward 的标定和跨任务泛化？
- 在下游 policy learning 中，Robometer reward 是否提升真实成功率，还是主要提升离线 reward correlation 指标？

#### 📌 上传 PDF 后优先看

- RBM-1M 数据集组成和标签规则，尤其是失败轨迹与人类视频处理方式。
- 训练目标章节，关注 frame-level reward loss 与 trajectory preference loss。
- 下游 robot learning 实验，包括 baseline、reward hacking 分析和真实/双臂平台结果。

## Watchlist

### [W1]. MAPLE: Latent Multi-Agent Play for End-to-End Autonomous Driving [[HTML]](https://arxiv.org/html/2605.14201) [[PDF]](https://arxiv.org/pdf/2605.14201)
* **Paper ID**: `2605.14201`
* **Authors**: Rajeev Yasarla, Deepti Hegde, Hsin-Pai Cheng, Shizhong Han, Yunxiao Shi, Meysam Sadeghigooghari, Hanno Ackermann, Litian Liu, Pranav Desai, Fatih Porikli, Mohammad Ghavamzadeh, Hong Cai
* **Author Priority**: Standard
* **为什么还值得留意**: MAPLE 进入 watchlist 是因为它把 VLA 自动驾驶从 open-loop imitation 推向 latent-space closed-loop multi-agent rollout，且强调 reactive agents 与 diversity-aware RL，和今天的 VLA+RL 主题高度相关。没有进最终精选主要是因为它聚焦 autonomous driving 而非通用机器人操作，且摘录只给出 Bench2Drive 指标类别和 SOTA 主张，缺少足够细节来判断其对 manipulation VLA 的直接迁移价值。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W2]. Hand-in-the-Loop: Improving Dexterous VLA via Seamless Interventional Correction [[HTML]](https://arxiv.org/html/2605.15157) [[PDF]](https://arxiv.org/pdf/2605.15157)
* **Paper ID**: `2605.15157`
* **Authors**: Zhuohang Li, Liqun Huang, Wei Xu, Zhengming Zhu, Nie Lin, Xiao Ma, Xinjun Sheng, Ruoshi Wen
* **Author Priority**: Standard
* **为什么还值得留意**: Hand-in-the-Loop 值得跟踪，因为它面向高 DoF 灵巧手 VLA 的真实部署痛点：human takeover 时的 command mismatch 和 gesture jumps。它没有进最终精选，是因为主题更偏 interactive imitation learning 与遥操作接口，虽然摘录提到真实实验和最高两个数量级的接管不连续性降低，但与今天主线中的 world model/RL/VLA 基础范式相比覆盖面稍窄。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

### [W3]. Slot-MPC: Goal-Conditioned Model Predictive Control with Object-Centric Representations [[HTML]](https://arxiv.org/html/2605.14937) [[PDF]](https://arxiv.org/pdf/2605.14937)
* **Paper ID**: `2605.14937`
* **Authors**: Jonathan Spieler, Angel Villar-Corrales, Sven Behnke
* **Author Priority**: Standard
* **为什么还值得留意**: Slot-MPC 进入 watchlist 是因为它用 object-centric slot representation 学 action-conditioned dynamics，并在推理时做 goal-conditioned MPC，和 world model + planning 的长期方向一致。没有进入最终精选主要是因为它不是 VLA 论文，且摘录中的实验集中在 Meta-World 与 robosuite 的四个操作环境，更像重要的世界模型规划补充，而非今天 VLA 系统主线的核心节点。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. WarmPrior: Straightening Flow-Matching Policies with Temporal Priors [[HTML]](https://arxiv.org/html/2605.13959) [[PDF]](https://arxiv.org/pdf/2605.13959)
* **Paper ID**: `2605.13959`
* **Authors**: Sinjae Kang, Chanyoung Kim, Kaixin Wang, Li Zhao, Kimin Lee
* **Author Priority**: Standard
* **为什么还值得留意**: WarmPrior 值得关注，因为它重新审视 diffusion/flow-matching policy 的 source distribution，用近期动作历史构造 temporal prior，并扩展到 prior-space RL，思路简单且可能很实用。未进最终精选是因为它更偏生成式 visuomotor policy 的训练技巧，虽然与 VLA action head 和 RL exploration 有潜在连接，但当前摘录显示的贡献还不是完整 VLA 或 world model 系统。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)
