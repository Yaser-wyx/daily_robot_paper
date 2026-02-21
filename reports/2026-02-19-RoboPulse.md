# 🤖 RoboPulse 机器人学学术脉动 | 2026-02-19

早上好！今日 arXiv 更新了 **67** 篇论文。今天的重头戏在 **VLA (Vision-Language-Action)** 模型的可靠性验证与 **World Model (世界模型)** 的策略化应用上。**Chelsea Finn** 团队对 VLA 的指令对齐提出了新的见解，而 **Linxi Fan (范林熙)** 与 **Yuke Zhu (朱玉可)** 团队连续推出了两篇关于世界动作模型和灵巧手操作的重磅工作，展示了从视频生成到零样本策略的强大潜力。

---

## 🌟 重点关注：名校/名家实验室新作

### [1]. Scaling Verification Can Be More Effective than Scaling Policy Learning for Vision-Language-Action Alignment
* **Title**: Scaling Verification Can Be More Effective than Scaling Policy Learning for Vision-Language-Action Alignment
* **摘要介绍**: **【VIP Author】Chelsea Finn (Stanford) & Marco Pavone** 等人新作。尽管 VLA 模型进展迅速，但生成的动作往往与自然语言指令不符（Misalignment）。本文提出一个核心观点：在推理时扩展“验证”（Verification）比单纯扩展策略学习（Policy Learning）更能有效提升 VLA 的指令遵循能力。通过引入自动化的验证器来过滤或重排序动作，大幅提升了长程任务的成功率。
* **关键词**: VLA Alignment, Verification, Robot Learning

### [2]. World Action Models are Zero-shot Policies
* **Title**: World Action Models are Zero-shot Policies
* **摘要介绍**: **【VIP Author】Linxi "Jim" Fan & Yuke Zhu & Danfei Xu** 等人新作。传统的 VLA 擅长语义泛化但缺乏物理常识。团队提出了 **DreamZero**，一种建立在视频扩散骨干网上的“世界动作模型”（WAM）。与 VLA 不同，WAM 显式学习物理动力学。最令人兴奋的是，它证明了世界模型本身就可以作为 **Zero-shot Policy** 使用，通过在潜在空间中规划未来视频来实现复杂操作，无需特定任务的动作数据。
* **关键词**: World Action Model, Zero-shot Policy, Video Diffusion

### [3]. EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data
* **Title**: EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data
* **摘要介绍**: **【VIP Author】Linxi Fan & Yuke Zhu & Danfei Xu** 团队新作。人类行为数据是物理智能最可扩展的来源。本文探讨了如何利用大规模、多样化的**人类自我中心视频（Egocentric Data）**来扩展机器人的灵巧手操作能力。EgoScale 展示了从人类视频到机器人策略的高效迁移，特别是解决了在非结构化环境下的灵巧操作难题。
* **关键词**: Dexterous Manipulation, Egocentric Video, Sim2Real

---

## 🌍 具身智能与世界模型高价值论文

### [4]. Learning to unfold cloth: Scaling up world models to deformable object manipulation
* **Title**: Learning to unfold cloth: Scaling up world models to deformable object manipulation
* **摘要介绍**: 布料等可变形物体的操作一直是机器人领域的难点。本文通过扩展 **World Model** 的能力，使其能够模拟和预测复杂的可变形物理特性。作者展示了利用世界模型进行规划，成功实现了高难度的布料展开（Unfolding Cloth）任务，验证了基于模型的强化学习在处理高维形变物体上的潜力。
* **关键词**: World Models, Deformable Objects, Cloth Manipulation

### [5]. FUTURE-VLA: Forecasting Unified Trajectories Under Real-time Execution
* **Title**: FUTURE-VLA: Forecasting Unified Trajectories Under Real-time Execution
* **摘要介绍**: 针对 VLA 模型在处理长视频流和高维未来预测时的高延迟问题，本文提出了 **FUTURE-VLA**。该模型支持在长视野历史数据上进行统一的时空推理，并能实时生成未来轨迹预测。这弥补了通用 VLA 模型在机器人实时部署时的速度短板，特别适用于动态环境下的连续操作。
* **关键词**: VLA, Spatiotemporal Reasoning, Trajectory Forecasting

### [6]. RoboGene: Boosting VLA Pre-training via Diversity-Driven Agentic Framework for Real-World Task Generation
* **Title**: RoboGene: Boosting VLA Pre-training via Diversity-Driven Agentic Framework for Real-World Task Generation
* **摘要介绍**: 机器人数据的稀缺性限制了 VLA 的泛化能力。本文提出了 **RoboGene**，一个利用 Agentic Framework 自动生成多样化现实世界任务数据的框架。通过这种方式“合成”训练数据，大幅提升了 VLA 模型的预训练效果，是一种典型的利用生成式 AI 反哺机器人学习（Sim2Real/Data Gen）的思路。
* **关键词**: VLA Pre-training, Data Generation, Agentic Framework

### [7]. MARVL: Multi-Stage Guidance for Robotic Manipulation via Vision-Language Models
* **Title**: MARVL: Multi-Stage Guidance for Robotic Manipulation via Vision-Language Models
* **摘要介绍**: 针对强化学习（RL）中密集奖励函数设计难的问题，本文提出了 **MARVL**。利用视觉语言模型（VLM）提供多阶段的指导，自动生成奖励信号，从而引导机器人完成复杂操作。这结合了 **RL + VLA** 的优势，减少了人工工程量，提升了 RL 在长程任务中的样本效率。
* **关键词**: RL, Vision-Language Models, Reward Generation

---

**编者按**：今天的论文质量极高，特别是 Linxi Fan 和 Yuke Zhu 团队关于 World Model 作为 Zero-shot Policy 的探索（DreamZero），可能会开启一个新的范式——即从“学习动作”转向“模拟未来并逆向规划”。建议重点阅读 [2] 和 [3]。

# 📚 Selected Papers Deep Dive (深度拆解)

### 💡 Scaling Verification Can Be More Effective than Scaling Policy Learning for Vision-Language-Action Alignment (Deep Dive)
> **一句话总结**: **提出 CoVer 对比验证器及 CoVer-VLA 框架，证明了在测试阶段通过扩展验证（Scaling Verification）来弥合“意图-动作差距”，比单纯在训练阶段扩展策略学习更为高效且性能更优。**

#### 📖 背景与动机 (Background & Motivation)
尽管视觉-语言-动作（VLA）模型在通用机器人领域取得了显著进展，但模型生成的动作往往无法精确对齐复杂的自然语言指令，导致“意图-动作差距”（intention-action gap）。现有的改进方向多集中在扩大预训练规模，而本文通过调查**测试时验证（test-time verification）**，探索是否能通过后处理机制更有效地提升指令跟随能力。

#### ⚙️ 核心方法 (Core Methodology)
本文的核心创新在于将重点从“训练更好的策略”转移到“更好地验证和选择策略输出”。主要包含以下几个关键点：
1.  **具身指令跟随的测试时扩展定律 (Test-time Scaling Laws)**：
    *   研究发现，联合扩展**重述指令的数量**（rephrased instructions）和**生成动作的数量**（generated actions）能极大增加测试时的样本多样性。
    *   这种联合扩展比单独扩展某一维度能更高效地恢复出正确的动作序列。
2.  **CoVer (Contrastive Verifier)**：
    *   提出了一种用于 VLA 对齐的**对比验证器**。该架构被证明能够随着计算资源和数据的增加而优雅地扩展（scale gracefully）。
3.  **CoVer-VLA 分层验证管线**：
    *   **部署流程**：首先利用视觉语言模型（VLM）预计算一组多样的重述指令；接着为每条指令重复生成动作候选；最后使用训练好的 CoVer 验证器选择最佳的**高层提示词（high-level prompt）**和**底层动作块（low-level action chunks）**。

#### 📊 实验与结果 (Experiments & Results)
-   **实验设置**：在仿真环境（SIMPLER benchmark, PolaRiS benchmark）及真实世界机器人实验中进行评估。
-   **关键指标与对比**：
    *   **相比策略预训练**：在相同数据量下，CoVer-VLA 的效果显著优于扩展策略预训练（scaling policy pre-training）。
    *   **SIMPLER 基准**：分布内（In-Distribution）性能提升 **22%**，分布外（Out-of-Distribution）性能提升 **13%**。
    *   **真实世界实验**：性能进一步提升了 **45%**。
    *   **PolaRiS 基准**：任务进度（Task Progress）提升 **14%**，成功率（Success Rate）提升 **9%**。

#### 💭 结论与影响 (Conclusion & Impact)
该工作挑战了“仅仅通过扩大训练规模来解决问题”的传统范式，强调了**测试时计算（Test-time Compute）**在具身智能中的重要性。它证明了通过构建强大的验证器来筛选最佳动作，是提升机器人对复杂指令理解与执行能力的另一条高效路径，为未来的 VLA 研究指明了“验证即扩展”（Verification as Scaling）的新方向。

#### 🏷️ 核心标签
`Vision-Language-Action (VLA)` `Test-Time Verification` `Scaling Laws` `Embodied AI`---

### 💡 World Action Models are Zero-shot Policies (Deep Dive)

> **一句话总结**: **DreamZero (WAM) 利用预训练视频生成模型作为世界模型，通过联合建模视频与动作，实现了超越 VLA 的零样本物理泛化能力与跨形态迁移。**

#### 📖 背景与动机 (Background & Motivation)
尽管最先进的视觉-语言-动作 (VLA) 模型在语义泛化方面表现出色，但在面对新环境中的**未见物理运动**时往往难以适应。现有的 VLA 缺乏对物理动力学的深刻理解。为了解决这一问题，本文提出利用视频作为世界演变的稠密表征，让模型真正“学会”物理规律，而非仅依赖重复演示。

#### ⚙️ 核心方法 (Core Methodology)
*   **世界动作模型 (World Action Model, WAM)**：提出了 **DreamZero**，这是一个建立在预训练视频扩散 (Video Diffusion) 主干网络之上的 WAM。
*   **联合建模 (Joint Modeling)**：不同于传统 VLA，DreamZero 通过预测未来的世界状态（视频帧）和动作，共同学习物理动力学。
*   **视频作为稠密表征**：利用视频数据中蕴含的丰富物理信息，从异构机器人数据中高效学习多样化技能，减少对重复演示数据的依赖。
*   **实时闭环控制**：通过模型与系统层面的优化，成功使 **14B 参数**的自回归视频扩散模型实现了 **7Hz** 的实时闭环控制。

#### 📊 实验与结果 (Experiments & Results)
*   **实验设置**：在**真实机器人 (Real Robot)** 环境下进行测试。
*   **关键指标**：
    *   **泛化性**：在未见过的任务和环境中，泛化能力相比 SOTA VLA 模型提升了 **2倍以上**。
    *   **跨形态迁移 (Cross-Embodiment)**：仅使用其他机器人或人类的**纯视频演示**（10-20分钟数据），在未见任务上的性能相对提升超过 **42%**。
    *   **少样本适应**：仅需 **30分钟** 的新形态机器人游玩数据 (Play Data)，即可完成适应，并保持零样本泛化能力。

#### 💭 结论与影响 (Conclusion & Impact)
该工作证明了基于视频生成的**世界动作模型 (WAM)** 是通向通用物理智能的一条极具潜力的路径。DreamZero 不仅突破了 VLA 在物理泛化上的瓶颈，还展示了利用大规模视频生成模型进行机器人控制的可行性（实时性与数据效率），为从视频中学习物理常识并迁移到机器人控制提供了强有力的范式。

#### 🏷️ 核心标签
`World Action Model` `Video Diffusion` `Zero-shot Generalization` `Robotics`---

### 💡 EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data (Deep Dive)
> **一句话总结**: **利用超过2万小时的第一人称人类视频训练 VLA 模型，揭示了数据规模与性能的对数线性缩放定律，证明了大规模人类数据是高自由度灵巧操作强有力的通用运动先验。**

#### 📖 背景与动机 (Background & Motivation)
灵巧操作（Dexterous Manipulation）因其高自由度和复杂的接触动力学，一直是机器人领域的难题。虽然人类行为数据是学习物理智能最可扩展的来源之一，但如何将其有效迁移到机器人上仍不明确。现有工作大多在受限设置下进行小规模迁移，**目前尚不清楚大规模人类数据是否能支持精细的、高自由度的灵巧操作学习**。

#### ⚙️ 核心方法 (Core Methodology)
作者提出了 **EgoScale** 框架，旨在通过大规模第一人称视频实现从人类到机器人的技能迁移：
- **超大规模 VLA 训练**：在超过 **20,854 小时** 的带有动作标签的第一人称人类视频上训练 Vision Language Action (VLA) 模型。这一数据量是先前同类工作的 20 倍以上。
- **发现缩放定律 (Scaling Law)**：揭示了人类数据规模与验证集损失（Validation Loss）之间存在 **对数线性 (Log-linear)** 关系。更重要的是，验证集损失与下游真实机器人的性能表现出强相关性，使人类数据成为一种可预测的监督来源。
- **两阶段迁移配方 (Two-stage Transfer Recipe)**：
    1.  **大规模人类预训练 (Large-scale Human Pretraining)**：注入通用的操作先验。
    2.  **轻量级人机对齐中间训练 (Lightweight Aligned Human-Robot Mid-training)**：使用少量数据将人类运动先验适配到具体的机器人构型上。

#### 📊 实验与结果 (Experiments & Results)
- **实验设置**：主要在真实机器人（Real Robot）上进行评估，使用 22 DoF（自由度）的灵巧机械手，同时也测试了向低自由度夹爪的迁移。
- **关键指标**：
    - **成功率提升**：相比没有预训练的基线方法，EgoScale 将平均成功率提升了 **54%**。
    - **长视程与少样本**：实现了强大的长视程（Long-horizon）灵巧操作，并具备在极少机器人监督下的 One-shot 任务适应能力。
- **跨具身迁移**：证明了该策略不仅适用于高自由度灵巧手，也能有效迁移到低自由度机器人上，表明学到的是一种与具体具身无关（Embodiment-agnostic）的运动先验。

#### 💭 结论与影响 (Conclusion & Impact)
EgoScale 的核心价值在于**量化并验证了“大力出奇迹”在灵巧操作领域的有效性**。它证明了大规模人类视频数据不仅仅是视觉特征的来源，更是包含了可复用、跨具身的运动先验（Motor Prior）。这一发现为通过扩大数据规模来解决复杂的机器人操作问题提供了一条可预测的、标准化的路径。

#### 🏷️ 核心标签
`Vision Language Action (VLA)` `Dexterous Manipulation` `Human-to-Robot Transfer` `Scaling Law`---

### 💡 Learning to unfold cloth: Scaling up world models to deformable object manipulation (Deep Dive)
> **一句话总结**: **基于改进的 DreamerV2 世界模型强化学习架构，通过引入表面法向量输入及优化数据增强，实现了布料空中展开任务的高效 Sim-to-Real 零样本泛化。**

#### 📖 背景与动机 (Background & Motivation)
布料操纵（Cloth Manipulation）因涉及复杂的物理形变特性（如多样的形状、尺寸、褶皱及外观变化），一直是机器人领域的难题，但在辅助护理和服务业中具有重要应用价值。现有方法往往难以通过单一策略应对这种物理复杂性和多样性，因此如何构建一个能有效捕捉模型结构并具备强大泛化能力的通用策略成为了关键挑战。

#### ⚙️ 核心方法 (Core Methodology)
本文提出了一种针对空中布料操纵（In-air cloth manipulation）的强化学习方法，核心在于对现有世界模型架构的改进：
1.  **架构基础**：基于 **DreamerV2**，这是一种先进的基于世界模型（World Model）的强化学习架构。
2.  **输入模态增强**：修改了网络架构以利用 **表面法向量（Surface Normals）** 作为额外输入，帮助模型更好地理解布料的几何形变特征。
3.  **训练机制优化**：
    *   **改进经验回放（Replay Buffer）**：调整数据存储与采样策略。
    *   **数据增强（Data Augmentation）**：采用了特定的数据增强程序以提高鲁棒性。
4.  **物理复杂性建模**：上述修改共同增强了机器人使用的世界模型，使其能更有效地处理可变形物体的物理复杂性。

#### 📊 实验与结果 (Experiments & Results)
- **实验设置**：在仿真环境中进行训练，并直接迁移到物理机器人系统（Physical Robot Setup）中进行评估。
- **任务场景**：执行多种不同类型布料的空中展开（In-air unfolding）任务。
- **关键结果**：
    *   实现了 **Zero-shot（零样本）** 部署，即在仿真训练后直接在真机上应用。
    *   展示了该架构在面对不同布料类型时优越的 **泛化能力（Generalisation）**，验证了改进后的世界模型在处理动态形变物体时的有效性。

#### 💭 结论与影响 (Conclusion & Impact)
该工作通过扩展和改进基于世界模型的强化学习方法（DreamerV2），成功解决了高维度的可变形物体操纵问题。其核心价值在于证明了引入几何信息（如表面法向量）和优化训练流程可以显著提升 Sim-to-Real 的泛化性能，为家庭服务机器人处理衣物等复杂柔性物体提供了可行的技术路径。

#### 🏷️ 核心标签
`Reinforcement Learning` `Deformable Object Manipulation` `World Models` `Sim-to-Real`---

### 💡 FUTURE-VLA: Forecasting Unified Trajectories Under Real-time Execution (Deep Dive)

> **一句话总结**: **提出 FUTURE-VLA 统一架构，通过时序自适应压缩和潜在空间自回归，在保持单帧推理延迟的同时实现了长视界控制与未来预测，大幅提升了机器人操作任务的成功率与实时性。**

#### 📖 背景与动机 (Background & Motivation)
通用视觉-语言模型（VLM）虽支持长视频流的复杂时空推理，但在机器人领域，处理长历史视界（Long-horizon histories）和生成高维未来预测带来的**高计算延迟**使其难以部署。现有方法无法有效平衡“长时空推理”与“实时执行”之间的矛盾。

#### ⚙️ 核心方法 (Core Methodology)
该论文提出了一种名为 FUTURE-VLA 的统一架构，核心技术点如下：
- **单体序列生成任务 (Monolithic Sequence Generation)**: 将传统的长视界控制和未来预测任务重构为一个统一的序列生成问题，简化了模型范式。
- **双向效率范式 (Dual-sided Efficiency Paradigm)**:
    - **时序自适应压缩**: 采用策略最大化时空信息密度，能够摄入广泛的多视角历史数据，同时强制保持恒定的推理延迟（Constant Inference Latency）。
    - **潜在空间自回归**: 在单次前向传播（Single Forward Pass）中，同时对齐可执行的动力学（Actionable Dynamics）与可审查的视觉未来预览（Reviewable Visual Look-aheads）。
- **预测引导的人机回环 (Prediction-guided HITL)**: 设计了交互式执行门控机制，允许操作员基于模型生成的可解释未来预览（Future Previews）动态验证机器人行为，提升安全性。

#### 📊 实验与结果 (Experiments & Results)
- **实验设置**：在仿真基准 LIBERO、RoboTwin 以及真实世界 Piper 机械臂平台上进行评估。
- **关键指标**：
    - **SOTA 性能**：LIBERO 成功率达 **99.2%**，RoboTwin 达 **75.4%**，真实世界 Piper 平台达 **78.0%**。
    - **效率突破**：在处理 **$16\times$** 扩展时空窗口的情况下，仍保持了相当于单帧基线的推理延迟。
- **核心优势**：相比基线，显著提升了长序列任务的成功率，同时解决了延迟瓶颈。

#### 💭 结论与影响 (Conclusion & Impact)
FUTURE-VLA 成功打破了 VLM 在机器人实时控制中的效率壁垒，建立了新的 SOTA 标准。其核心价值在于证明了通过高效的时空压缩，可以在不牺牲实时性的前提下利用长历史信息，并利用未来预测能力引入了直观的人机交互验证机制，为安全、高效的机器人基础模型提供了重要参考。

#### 🏷️ 核心标签
`Vision-Language-Action (VLA)` `Trajectory Forecasting` `Real-time Control` `Human-In-the-Loop`---

### 💡 RoboGene: Boosting VLA Pre-training via Diversity-Driven Agentic Framework for Real-World Task Generation (Deep Dive)

> **一句话总结**: **提出了一种基于 Agent 的自动化任务生成框架 RoboGene，通过多样性采样、自我反思和人机回环机制，解决了机器人 VLA 预训练中高质量、物理可行数据稀缺的瓶颈。**

#### 📖 背景与动机 (Background & Motivation)
通用机器人操作（General-Purpose Robotic Manipulation）的发展受限于**多样化真实世界交互数据的稀缺性**。与计算机视觉或自然语言处理中可从网络获取海量数据不同，机器人数据采集是一个物理过程，成本高昂。
*   **现有局限**：人工设计任务难以扩展且存在偏差（biased toward common tasks）；直接使用现成的基础模型（Foundation Models）生成任务往往会产生物理上不可行的指令（hallucination）。
*   **核心问题**：如何自动化地策划高价值、物理可行的任务，以最大化数据价值？

#### ⚙️ 核心方法 (Core Methodology)
RoboGene 是一个**Agentic Framework（代理框架）**，旨在自动化生成涵盖单臂、双臂及移动机器人的多样化且物理可行的操作任务。其核心由三个关键组件构成：

1.  **多样性驱动采样 (Diversity-Driven Sampling)**：
    *   设计了一套采样机制，旨在覆盖广泛的任务空间，避免生成的任务过于集中或重复，确保数据的丰富性。
2.  **自我反思机制 (Self-Reflection Mechanisms)**：
    *   这是解决“幻觉”的关键。Agent 具备自我审查能力，能够根据物理约束（Physical Constraints）对生成的任务指令进行评估和修正，确保任务在现实物理世界中是可执行的。
3.  **人机回环优化 (Human-in-the-loop Refinement)**：
    *   引入人类反馈环节，对生成过程进行持续改进，进一步提升任务的质量和合理性。

#### 📊 实验与结果 (Experiments & Results)
*   **实验设置**：进行了广泛的定量分析以及**大规模真实世界实验**（Large-scale Real-world Experiments）。
*   **数据集构建**：收集了包含 **18k 条轨迹**的数据集。
*   **对比基线**：与 SOTA 基础模型（如 GPT-4o, Gemini 2.5 Pro）进行了对比。
*   **关键结果**：
    *   **任务质量**：RoboGene 在生成任务的质量、可行性和多样性上显著优于 GPT-4o 和 Gemini 2.5 Pro。
    *   **下游性能**：使用 RoboGene 生成的数据预训练的 VLA（Vision-Language-Action）模型，在真实世界中展现了**更高的成功率**和**更强的泛化能力**。

#### 💭 结论与影响 (Conclusion & Impact)
*   **核心价值**：证明了在 VLA 模型预训练中，通过自动化手段生成高质量、多样化的任务描述，能显著提升模型在真实世界的表现。
*   **启发**：为解决具身智能（Embodied AI）数据匮乏问题提供了一条可扩展的路径，即从“被动采集”转向“主动、智能的自动化生成”。

#### 🏷️ 核心标签
`Data Generation` `VLA Pre-training` `Agentic Framework` `Robotic Manipulation`---

### 💡 MARVL: Multi-Stage Guidance for Robotic Manipulation via Vision-Language Models (Deep Dive)
> **一句话总结**: **提出 MARVL 框架，通过微调 VLM 实现空间语义一致性，并利用多阶段任务分解与方向投影生成高质量稠密奖励，显著解决了稀疏奖励下强化学习样本效率低的问题。**

#### 📖 背景与动机 (Background & Motivation)
设计稠密奖励函数（Dense Rewards）是实现高效机器人强化学习（RL）的关键，但传统方法严重依赖人工工程，限制了算法的扩展性和自动化程度。虽然视觉语言模型（VLMs）为自动化奖励设计提供了新路径，但现有的 **Naive VLM 奖励** 往往存在三大痛点：**与任务进度对齐差**、**空间锚定（Spatial Grounding）能力弱**以及**任务语义理解受限**，导致 RL 训练难以收敛或效率低下。

#### ⚙️ 核心方法 (Core Methodology)
MARVL（Multi-stAge guidance for Robotic manipulation via Vision-Language models）通过以下核心机制解决了上述问题：

1.  **VLM 空间语义微调 (VLM Fine-tuning for Consistency)**
    *   不仅利用 VLM 的通用知识，还专门针对**空间一致性**和**语义一致性**进行微调，使其能更准确地理解机器人操作场景中的物体关系和状态变化。
2.  **多阶段任务分解 (Multi-stage Subtask Decomposition)**
    *   将复杂的长程任务拆解为多个阶段性的子任务（Subtasks）。这种分层引导机制避免了单一目标带来的奖励稀疏问题，引导 Agent 逐步逼近最终目标。
3.  **轨迹敏感的任务方向投影 (Task Direction Projection)**
    *   引入了任务方向投影机制，增强了奖励函数对**轨迹敏感性**（Trajectory Sensitivity）的感知。这意味着奖励不仅反映当前状态的好坏，还能有效指引状态转移的方向。

#### 📊 实验与结果 (Experiments & Results)
- **实验设置**：在标准的 **Meta-World benchmark**（机器人操作仿真环境）上进行评估。
- **关键指标**：重点考察了算法的**样本效率（Sample Efficiency）**和在**稀疏奖励（Sparse-reward）**任务上的**鲁棒性**。
- **主要结果**：
    *   MARVL 显著优于现有的基于 VLM 的奖励生成方法（Existing VLM-reward methods）。
    *   在稀疏奖励设置下，表现出卓越的学习速度和最终成功率。

#### 💭 结论与影响 (Conclusion & Impact)
MARVL 的核心价值在于弥合了通用 VLM 知识与机器人底层控制信号之间的鸿沟。它证明了通过合理的**微调**和**结构化引导（多阶段/投影）**，VLM 可以完全替代人工设计的稠密奖励，为实现更通用、更自动化的机器人强化学习铺平了道路。

#### 🏷️ 核心标签
`Reinforcement Learning` `Vision-Language Models` `Reward Engineering` `Robotic Manipulation`