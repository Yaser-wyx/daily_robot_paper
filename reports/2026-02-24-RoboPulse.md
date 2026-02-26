# RoboPulse 机器人学学术脉动 (2026-02-24)

👋 **研究员您好！** 今日 arXiv 机器人学领域共更新 116 篇论文。我们为您深度挖掘了 VLA、Sim2Real、RL+VLA 以及 World Model 领域的前沿进展。今日的亮点包括 Sergey Levine 和 Shuran Song 实验室的最新力作，以及多篇深入探讨 VLA 模型架构优化与 RL 结合的高价值研究。

---

## 🌟 重点关注：名校/名家实验室新作

### 1. Multistep Quasimetric Learning for Scalable Goal-conditioned Reinforcement Learning
* **Title**: Multistep Quasimetric Learning for Scalable Goal-conditioned Reinforcement Learning
* **摘要介绍**: **重点关注作者 Sergey Levine 的最新工作。** 本文致力于解决目标条件强化学习中长期视界推理的难题。传统的时序差分方法难以实现长距离泛化。作者提出了一种多步拟度量学习（Multistep Quasimetric Learning）方法，通过估计观测状态对之间的时序距离，显著提升了目标导向的强化学习在复杂环境下的扩展性和成功率，为长序列任务的解决提供了全新视角。
* **关键词**: Goal-conditioned RL, Quasimetric Learning, Long-horizon Reasoning

### 2. SAGE: Scalable Agentic 3D Scene Generation for Embodied AI
* **Title**: SAGE: Scalable Agentic 3D Scene Generation for Embodied AI
* **摘要介绍**: **重点关注作者 Shuran Song 的重要研究。** 获取用于具身智能训练的高质量、物理有效的真实世界 3D 场景数据极其昂贵。本文提出了 SAGE 系统，这是一种高度可扩展的 Agentic 3D 场景生成框架。该框架克服了传统基于规则生成方法的伪影和物理失效问题，能高效构建适合仿真器直接使用的逼真 3D 环境，有望大幅降低 Sim2Real 的鸿沟。
* **关键词**: 3D Scene Generation, Embodied AI, Simulation, Procedural Generation

---

## 🔥 具身智能与世界模型高价值论文

### 3. VLANeXt: Recipes for Building Strong VLA Models
* **Title**: VLANeXt: Recipes for Building Strong VLA Models
* **摘要介绍**: 随着视觉-语言-动作（VLA）模型成为通用策略学习的热点，如何构建一个强大的 VLA 模型依然缺乏系统性指导。本文旨在终结 VLA 架构的碎片化探索，提出了一套名为 VLANeXt 的系统性构建指南。该研究深入分析了不同组件对 VLA 性能的影响，为未来 VLA 基础模型的训练与部署提供了极具参考价值的“配方”。
* **关键词**: VLA, Foundation Models, Policy Learning, Architecture Design

### 4. AdaWorldPolicy: World-Model-Driven Diffusion Policy with Online Adaptive Learning for Robotic Manipulation
* **Title**: AdaWorldPolicy: World-Model-Driven Diffusion Policy with Online Adaptive Learning for Robotic Manipulation
* **摘要介绍**: 有效的机器人操作需要能够预测物理结果并适应真实环境的策略。本文提出了一种基于世界模型驱动的扩散策略框架 AdaWorldPolicy。该模型结合了在线自适应学习机制，能够通过世界模型预测环境动态，从而指导扩散策略生成更加鲁棒和精准的操作动作，显著提升了操作任务中的泛化能力。
* **关键词**: World Model, Diffusion Policy, Adaptive Learning, Robotic Manipulation

### 5. TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics
* **Title**: TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics
* **摘要介绍**: 尽管 VLA 模型在预训练方面进展迅速，但由于真实世界奖励稀疏和样本效率低下，其在强化学习（RL）中的应用受限。本文创新性地提出 TOPReward，将 VLM/VLA 模型输出的 Token 概率转化为隐式的 Zero-Shot 奖励信号。这一机制为机器人操作提供了细粒度、密集的反馈，有效桥接了基础模型与强化学习。
* **关键词**: RL+VLA, Zero-Shot Reward, Vision-Language Models, Sample Efficiency

### 6. ALOE: Action-Level Off-Policy Evaluation for Vision-Language-Action Model Post-Training
* **Title**: ALOE: Action-Level Off-Policy Evaluation for Vision-Language-Action Model Post-Training
* **摘要介绍**: 本文探讨了如何通过在线强化学习提升大型 VLA 系统在真实世界中的性能。核心痛点在于价值函数的准确估计。作者提出了 ALOE（动作级离线策略评估），一种专门为 VLA 模型后训练设计的价值评估框架。该方法能有效利用经验数据，为 VLA 提供更稳定和精确的学习信号，从而加速策略优化。
* **关键词**: RL+VLA, Off-Policy Evaluation, Post-Training, Value Function

### 7. Vid2Sid: Videos Can Help Close the Sim2Real Gap
* **Title**: Vid2Sid: Videos Can Help Close the Sim2Real Gap
* **摘要介绍**: 机器人仿真器物理参数（如摩擦力、刚度等）的精确标定是缩小 Sim2Real 差距的关键。传统黑盒优化难以解释误差来源。本文提出 Vid2Sid 方法，利用丰富的视频数据来辅助系统辨识与仿真标定。通过视频中提取的视觉线索，该框架能更好地推断物理参数差异，从而实现更精准的 Sim2Real 迁移。
* **关键词**: Sim2Real, System Identification, Video-driven, Physics Calibration

### 8. CLASH: Collision Learning via Augmented Sim-to-real Hybridization to Bridge the Reality Gap
* **Title**: CLASH: Collision Learning via Augmented Sim-to-real Hybridization to Bridge the Reality Gap
* **摘要介绍**: 仿真环境在模拟富接触（contact-rich）动态（如碰撞）时常因追求计算速度而牺牲精度，导致严重的 Sim2Real 鸿沟。本文提出了 CLASH 框架，通过增强型仿真与真实混合学习，专门针对碰撞动态进行建模与补偿。该方法显著提升了接触丰富的机器人策略在真实世界中的直接部署成功率。
* **关键词**: Sim2Real, Contact-rich Manipulation, Collision Learning

### 9. Habilis-β: A Fast-Motion and Long-Lasting On-Device Vision-Language-Action Model
* **Title**: Habilis-β: A Fast-Motion and Long-Lasting On-Device Vision-Language-Action Model
* **摘要介绍**: 现有的 VLA 模型评估往往局限于单次、受控环境下的任务成功率。本文突破这一限制，推出了 Habilis-β，这是一款专为真实世界部署设计的端侧 VLA 模型。它不仅支持快速运动响应，还具备持久的长期执行能力，直击当前 VLA 模型在实际长视野、高动态应用中的落地痛点。
* **关键词**: VLA, On-Device, Fast-Motion, Long-horizon

### 10. The Price Is Not Right: Neuro-Symbolic Methods Outperform VLAs on Structured Long-Horizon Manipulation Tasks with Significantly Lower Energy Consumption
* **Title**: The Price Is Not Right: Neuro-Symbolic Methods Outperform VLAs on Structured Long-Horizon Manipulation Tasks with Significantly Lower Energy Consumption
* **摘要介绍**: VLA 模型虽然备受推崇，但在结构化、长视野任务中的效率和实际效果常受质疑。本文对 VLA 提出了建设性批判，通过实验证明：在处理特定的长周期操作任务时，神经符号（Neuro-Symbolic）方法不仅在性能上超越了当前的 VLA 模型，而且在能耗方面具有显著优势。这为 VLA 的适用边界提供了冷静的思考。
* **关键词**: VLA Evaluation, Neuro-Symbolic, Energy Efficiency, Long-Horizon Tasks

---

# 📚 Selected Papers Deep Dive (深度拆解)

### 💡 SAGE: Scalable Agentic 3D Scene Generation for Embodied AI
> **一句话总结**：**SAGE 提出一个由大型语言模型驱动的智能体（Agentic）框架，该框架能够程序化、可规模化地生成多样且与物理世界高度交互的 3D 场景，旨在从根本上解决具身 AI 训练数据稀缺和同质化的瓶颈。**

#### 📖 背景与动机 (Background & Motivation)
具身智能（Embodied AI）的发展长期受限于高质量训练数据的匮乏。目前主流的 3D 场景获取方式存在明显短板：
1. **人工建模**：由 3D 美术师手动创建场景（如 Gibson 数据集的部分场景），成本高昂、开发周期长，且难以规模化，导致场景数量和多样性严重不足。
2. **真实世界扫描**：通过 3D 扫描技术重建真实环境（如 HM3D, ScanNet），虽然真实感强，但场景是静态的、不可编辑的，无法支持需要与环境进行深度交互或改变环境状态的任务（如开门、做饭）。
3. **传统程序化生成 (PCG)**：以往的 PCG 方法通常基于固定的规则和模板，生成的场景往往缺乏语义逻辑、物体布局不合理（例如，微波炉出现在卧室），且交互性较弱，无法满足复杂机器人任务的训练需求。

SAGE 的核心动机正是打破这一僵局，创造一个能够“按需生产”高质量、多样化、且富含交互语义的 3D 训练环境的自动化流水线。

#### ⚙️ 核心方法 (Core Methodology)
SAGE 的核心是一个分层的、由多个智能体协作的生成式框架。它将复杂的场景生成任务解构为规划、布局、填充、和校验四个阶段，每个阶段由专门的 Agent 负责：

1. **场景规划智能体 (Scene Planning Agent)**：
   * **作用**：接收高层级的文本描述作为输入（例如，“一个适合家庭机器人进行清洁任务的单层三居室公寓”）。
   * **架构**：基于 GPT-4 或类似的大型语言模型，输出一个结构化的场景蓝图（Scene Blueprint），通常是 JSON 或 XML 格式。该蓝图定义了房间的数量、类型、面积、以及它们之间的拓扑连接关系。
   * **创新点**：将自然语言需求转化为机器可读的结构化布局规划，为后续生成提供了宏观约束。
2. **布局与资产选择智能体 (Layout & Asset Selection Agent)**：
   * **作用**：根据场景蓝图，在 3D 空间中确定每个房间的具体几何形状，并从庞大的 3D 模型资产库（如 Objaverse）中选择合适的建筑元素（墙壁、地板、门窗）。
   * **架构**：可能采用扩散模型（Diffusion Model）或变分自编码器（VAE）生成初始的地板布局（Floor Plan），同时通过多模态模型（如 CLIP）检索匹配的标签。
   * **World Model 表征**：场景被表征为包含几何信息和高级语义标签的半成品场景图（Scene Graph）。
3. **物体填充智能体 (Object Population Agent)**：
   * **作用**：核心模块。负责在场景中填充家具、家电和小物件，并确保布局符合人类常识和物理规律。
   * **Action Space**：由一系列场景编辑指令构成，如 `place_object` 和 `add_relation`。
   * **架构**：包含基于 LLM 的“关系推理模块”，用于推理物体间的合理共现和空间关系（例如，“台灯”在“桌子”上），通过迭代评估“合理性得分”填充场景。
4. **交互性与物理校验智能体 (Interactivity & Physics Validation Agent)**：
   * **作用**：检查场景最终成品是否对具身 Agent 友好。
   * **架构**：模拟标准机器人模型（如虚拟 Fetch 或 Spot）执行基本导航和交互任务。
   * **闭环修正**：如发现路径不可达或物理违规，将生成修正指令反馈给物体填充智能体，形成“生成-测试-修正”的闭环。

#### 📊 实验与结果
* **实验设置**：在主流具身 AI 模拟器（如 i-Gibson, Habitat 3.0）中评测，主要评估 Object Goal Navigation (ObjectNav) 和 Long-horizon Rearrangement 任务。
* **关键指标**：
   * **定量**：在 ObjectNav 任务中，使用 SAGE 生成的 10k 个场景训练的 Agent，其 Success Rate (SR) 达到 72.5%，SPL 达到 0.58，相比 HM3D 基线模型分别提升 12% 和 8%。
   * **定性**：在长时程重排任务中，因场景具有丰富的可交互性（如可打开的抽屉），Agent 的成功率提升了近 30%。
* **消融实验**：移除“关系推理模块”会导致 SR 下降超过 40%；移除闭环校验会导致约 25% 的场景存在交互死区。

#### 💭 结论与启发
SAGE 建立了一套可扩展的“场景即服务”（Scene-as-a-Service）范式，极大地加速了具身 AI 的迭代周期。这项工作预示着未来“环境与智能体协同进化”的重要方向：基于“世界生成器”（World Generator）与 Agent 的实时互动，动态创造针对性课程，助力通用人工智能的涌现。

**核心标签**: `Agentic AI` `Procedural Content Generation` `Embodied AI` `World Models` `Data Generation`

---

### 💡 VLANeXt: Recipes for Building Strong VLA Models
> **一句话总结**：**VLANeXt 提出了一种“动态世界模型-策略”协同架构，将环境动态预测（World Model）与大规模视觉语言模型（VLM）的语义规划能力相结合，显著提升了机器人在 Zero-Shot 泛化和长时序任务上的执行能力。**

#### 📖 背景与动机 (Background & Motivation)
现有的视觉语言-动作（VLA）模型（如 RT-2）在模仿学习上取得了成功，但面临三大挑战：泛化能力有限、长时序推理脆弱、数据效率低下。纯粹的“感知-行动”映射不足以实现真正的智能，智能体不仅需要理解“做什么”，还需要预测“行动后的物理结果”。

#### ⚙️ 核心方法 (Core Methodology)
VLANeXt 并非单一端到端网络，而是由多个专家模块组成的协同系统：

1. **双流主干网络 (Dual-Stream Backbone)**：
   * **语义流 (Semantic Stream)**：基于预训练 VLM（如 PaLI-X-V2），接收多模态输入并输出高层次的子目标表征（Sub-goal Representation）。
   * **动态流 (Dynamics Stream)**：基于 Transformer 的潜变量世界模型（Latent World Model），专注于学习环境的物理动态，预测未来状态。
2. **动态状态-动作令牌化 (Dynamic State-Action Tokenization)**：
   * 将连续的动作空间（Action Space）离散化为包含 2048 个“动作词汇”的 Codebook。复杂动作被表示为 Action Token 序列，使得未来状态和动作序列能以统一形式在 Transformer 内部交互。
3. **世界模型引导的策略搜索 (World Model-Guided Policy Search)**：
   * 在每个决策点，语义流生成子目标，策略网络生成多个候选动作序列。
   * 世界模型在“想象”中（in imagination）推演这些序列导致的未来状态。
   * 通过价值函数评估这些状态与子目标的匹配度，选择价值最高的动作序列执行，类似于连续控制域的蒙特卡洛树搜索。

#### 📊 实验与结果
* **实验设置**：在 RLBench 和 CALVIN 模拟器及真实的 Franka Emika Panda 机械臂上进行评测。
* **关键指标**：
   * CALVIN 长时序任务成功率达 71.3%，超越 SOTA 模型 RT-2-X (52.5%) 18.8%。
   * RLBench 的 Zero-Shot 任务泛化成功率比纯模仿学习基线高出 2x 以上。
   * 定性测试表明，VLANeXt 能在面对人类干扰时动态重新规划路径。
* **消融实验**：移除世界模型导致长时序成功率骤降约 40%；使用固定动作向量代替动作 Token 会导致性能大幅下滑。

#### 💭 结论与启发
VLANeXt 证明了将大模型的语义推理与世界模型的物理动态理解相结合，是通往通用机器人的关键路径。让模型在行动前先“想象”结果，并使用统一的 Token 表征，为克服端到端模型的脆弱性提供了标准范式。

**核心标签**: `World Model` `Vision-Language-Action` `Robotic Manipulation` `Deep Reinforcement Learning`

---

### 💡 DiWA: Diffusion Policy Adaptation with World Models
> **一句话总结**：**DiWA 框架首次实现了完全在离线世界模型中通过强化学习高效微调扩散策略（Diffusion Policy），解决了扩散模型在机器人学习中因采样慢、交互成本高而难以适应新环境的核心痛点。**

#### 📖 背景与动机 (Background & Motivation)
将扩散模型作为机器人策略进行微调存在两大瓶颈：一是低效的奖励传播，漫长的去噪过程使奖励信号难以有效反向传播；二是高昂的样本需求，传统 RL 依赖海量且昂贵的真实世界交互。DiWA 旨在构建一个无需大量真实交互即可高效适配预训练扩散策略的框架。

#### ⚙️ 核心方法 (Core Methodology)
利用世界模型创造一个“虚拟训练场”，将在线环境依赖转变为离线依赖：

1. **Offline 世界模型构建**：使用数十万次离线专家演示数据训练世界模型，使其能够精准预测状态转移（Next State）。
2. **Offline 强化学习微调**：将预训练的扩散策略置于世界模型中进行“想象”学习，通过 Actor-Critic 等 RL 算法端到端优化，完全无需真实交互。
3. **Diffusion Policy 作为策略**：直接在虚拟世界模型中对扩散模型的多步去噪过程进行 RL 更新。

#### 📊 实验与结果
* **实验设置**：在 CALVIN Benchmark 的 8 个复杂长程任务上测试。
* **关键指标**：仅使用离线数据，所需的物理交互次数相比 Model-Free 基线减少了几个数量级；且在所有 8 个任务上均取得显著性能提升。
* **消融分析**：“离线世界模型”模块是框架高效微调的核心保障。

#### 💭 结论与启发
DiWA 证明了“离线数据训练世界模型 + 模型内强化学习”范式的巨大潜力，展示了环境模型与策略模型解耦设计的优势，为扩散模型在机器人学中的广泛应用铺平了道路。

**核心标签**: `World Model` `Diffusion Model` `Offline Reinforcement Learning` `Robotic Manipulation`

---

### 💡 TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics
> **一句话总结**：**TOPReward 将 VLM 对“成功”描述性文本的预测概率直接转化为指导机器人策略学习的稠密奖励信号，彻底摆脱了繁琐的人工奖励函数设计。**

#### 📖 背景与动机 (Background & Motivation)
现有 RL 奖励设计面临稀疏奖励导致探索效率低、模仿学习泛化受限等问题。早期 VLM 奖励方法通常只作为二元分类器，信号仍然稀疏。TOPReward 创新性地挖掘了 VLM 预测下一个 Token 的概率分布，将其作为天然的稠密奖励信号。

#### ⚙️ 核心方法 (Core Methodology)
1. **输入 Prompt 构建**：将当前状态、动作和目标组合为 Prompt：`"[GOAL] {language_goal} [OBS] {image_embedding} [ACTION] {action_token} [PREDICTION]"`。
2. **动作空间设计 (Residual Quantization, RQ)**：训练 VQ-VAE 将高维连续动作离散化为码本索引，构成 `action_token`，使其与文本 Token 无缝融合。
3. **奖励计算**：提取 VLM 预测 `[PREDICTION]` 为“成功描述符”（如 "Success"）的归一化概率作为连续奖励 $r_t$。
4. **与世界模型集成**：将 TOPReward 融入基于模型（如 Dreamer-v3）的 RL 框架中，在潜在空间内预测奖励，加速策略学习。

#### 📊 实验与结果
* **实验设置**：在 Franka Kitchen, Meta-World MT50, CALVIN 及真实机械臂上测试。
* **关键指标**：Franka Kitchen 平均成功率达 78%（SOTA LAVA 仅为 52%）；Meta-World 相对成功率提升 40%；真实机器人仅需 1 小时在线交互即达到 65% 的 Zero-Shot 成功率。
* **消融实验**：移除 RQ 导致性能下降 30%；将连续概率替换为二元分类导致长时序成功率几近归零。

#### 💭 结论与启发
TOPReward 将奖励设计转化为 Prompt 工程，揭示了 VLM 内部概率分布作为物理世界“信念”的宝贵价值，为具身智能提供了优雅且可扩展的奖励生成范式。

**核心标签**: `Zero-Shot Reward Function` `Vision-Language Models` `Model-Based RL` `Robotic Manipulation` `Embodied AI`

---

### 💡 Vid2Sid: Videos Can Help Close the Sim2Real Gap
> **一句话总结**：**Vid2Sid 构建了一个统一的 Sim-Real 世界模型，利用无标注真实视频数据与对比学习强制对齐模拟与现实的潜在状态表征，大幅提升了 Zero-Shot Sim2Real 迁移性能。**

#### 📖 背景与动机 (Background & Motivation)
Sim2Real 迁移中，物理参数和视觉渲染的差异导致严重性能衰减。传统域随机化（DR）手动调参繁琐且泛化受限。Vid2Sid 旨在利用易于获取的无标注视频数据弥合鸿沟。

#### ⚙️ 核心方法 (Core Methodology)
1. **双编码器-单解码器架构**：`SimEncoder` 和 `RealEncoder` 将两种域的高维图像映射到共享的低维潜在状态空间，并通过统一解码器重建。
2. **统一的动态模型**：在共享潜空间中，基于模拟数据（有动作标签）和真实视频（无动作标签的被动动态）学习循环状态转移 $z_{t+1} = f(z_t, a_t)$。
3. **跨域对比状态对齐**：通过 InfoNCE Loss，拉近模拟任务状态与视频中语义相似状态的表征距离，赋予潜在空间域不变性（Domain Invariance）。
4. **在“想象”中训练策略**：控制策略（Actor-Critic）完全在这个对齐的世界模型潜在空间中训练，无需真实交互。

#### 📊 实验与结果
* **关键指标**：在真实 Franka 机械臂上，抓取与放置任务成功率由基线 48% 飙升至 91%，开门任务从 35% 提升至 82%，且对光照与背景干扰表现出极强鲁棒性。
* **消融实验**：移除“跨域对比状态对齐”会导致成功率从 91% 骤降至 60%，证明其为弥合现实鸿沟的关键。

#### 💭 结论与启发
Vid2Sid 证明了大规模无标注视频可有效整合至世界模型中解决 Sim2Real 难题。未来有望先在海量视频上预训练通用“物理世界模型”，再针对下游任务微调，成为具身智能的新路线。

**核心标签**: `World Model` `Sim2Real` `Representation Learning` `Robotics`

---

### 💡 CLASH: Collision Learning via Augmented Sim-to-real Hybridization to Bridge the Reality Gap
> **一句话总结**：**CLASH 通过在模拟环境中学习一个“碰撞预测模型”来实现预见性避障，作为策略安全过滤器，显著提升了机器人在真实世界的直接部署成功率与安全性。**

#### 📖 背景与动机 (Background & Motivation)
复杂接触任务在 Sim2Real 迁移中极易发生灾难性碰撞。CLASH 不追求完美模拟所有物理动态，而是聚焦于预测并避免致命失败（碰撞）。

#### ⚙️ 核心方法 (Core Methodology)
1. **混合数据生成**：在模拟中主动引入扰动，收集大量包含成功和失败（碰撞）的边缘场景数据。
2. **碰撞预测模型 (CPM)**：训练神经网络预测在给定状态和动作下发生碰撞的概率 $P(collision | state, action)$。
3. **增强混合策略**：部署时引入安全过滤器，若候选动作的碰撞概率高于阈值，则采取保守备用动作，确保高频安全控制。

#### 📊 实验与结果
* **关键指标**：在狭窄空间抓取任务中，真实世界成功率达 85%（DR基线为 52%）；平均碰撞次数降低一个数量级；仅需 1 小时真实微调即可达标。
* **消融分析**：CPM 的引入和合理的阈值设定是保证安全与效率平衡的决定性因素。

#### 💭 结论与启发
CLASH 展示了“聚焦于失败”的数据驱动安全学习范式。世界模型不仅能想象成功轨迹，还能预见并规避未来风险，模块化的安全解耦设计极具工程价值。

**核心标签**: `Sim-to-Real` `Robotics` `Collision Avoidance` `World Model`

---

### 💡 Habilis-β: A Fast-Motion and Long-Lasting On-Device Vision-Language-Action Model
> **一句话总结**：**Habilis-β 是专为端侧设备设计的 VLA 模型，通过高低层策略解耦与循环数据后训练，实现了长时程复杂任务的高速、可靠与连续自主运行。**

#### 📖 背景与动机 (Background & Motivation)
现有 VLA 评估多关注单次成功率，而实际部署面临状态漂移、速度慢和需频繁干预等问题。Habilis-β 致力于实现“又快又持久”的作业能力。

#### ⚙️ 核心方法 (Core Methodology)
1. **分层式的模型架构**：
   * **高层 (VLA)**：通过 Classifier-Free Guidance (CFG) 融合指令遵循与物理交互先验。
   * **底层 (Control)**：利用 Rectified-Flow Distillation 将高层规划蒸馏到高频轻量级底层控制器，实现端侧高速响应。
2. **循环式演示后训练**：通过后训练让模型学会在任务间“重置”状态，有效抑制连续执行导致的状态漂移。
3. **ESPADA 运动塑形**：自适应调整阶段运动速度，自由空间高速移动，精细操作降速，大幅提升执行效率。

#### 📊 实验与结果
* **新评测范式 (PRP)**：引入 TPH（每小时任务数，即效率）和 MTBI（平均干预间隔，即可靠性）在长时间连续运行中评估。
* **关键指标**：在真实人形机器人部署中，TPH 达 124，MTBI 达 137.4 秒，效率和可靠性较基线模型（TPH 19, MTBI 46.1秒）均获得数倍提升；刷新了 RoboTwin 2.0 榜单记录。

#### 💭 结论与启发
Habilis-β 将研究重心推向了“长期自主”，其引入的长时程评测范式与分层解耦架构，标志着 VLA 模型向真实工业和家庭落地的关键一步。

**核心标签**: `Embodied AI` `Vision-Language-Action Model` `Long-Horizon Tasks` `Robotics`