各位研究者，今天是 2026 年 3 月 10 日星期二。今日 arXiv 机器人学领域迎来了一波具身智能（Embodied AI）新作的高峰。整体趋势显示，研究重心正在从简单的 VLA 架构向**多尺度记忆增强、跨任务专家混合（MoE）以及交互式世界模型**演进，旨在解决长程任务中的非马尔可夫效应和物理一致性问题。值得关注的是，Sergey Levine、Chelsea Finn、He Wang 以及 Cewu Lu 等顶尖实验室均有重磅新作发布，标志着 VLA 模型进入了更加注重“思考”与“记忆”的新阶段。

### 重点关注：名校/名家实验室新作

### [1]. 多尺度具身记忆增强 VLA 模型
* **Title**: MEM: Multi-Scale Embodied Memory for Vision Language Action Models
* **摘要介绍**: 由 Sergey Levine 和 Chelsea Finn 实验室联合推出。本文指出传统 VLA 仅通过输入观测序列来构建记忆，难以处理复杂的长程多阶段任务。为此，研究团队提出 MEM 框架，构建了一个多尺度记忆系统：包括捕获抽象任务进展的长程记忆，以及保留细粒度感觉细节的短程记忆。实验证明，这种分层记忆机制能显著提升机器人在跨越数分钟、涉及多个子目标的真实场景任务中的成功率，有效解决了状态混淆问题。
* **关键词**: Vision-Language-Action, Embodied Memory, Long-horizon Manipulation, Multi-scale Representation.

### [2]. 迈向类人操作：双机灵手 MoE-VLA 模型
* **Title**: Towards Human-Like Manipulation through RL-Augmented Teleoperation and Mixture-of-Dexterous-Experts VLA
* **摘要介绍**: 上海交大卢策吾（Cewu Lu）及庞江淼等团队合作。针对现有 VLA 模型多局限于低自由度末端执行器的问题，本文将 VLA 扩展到复杂的双机灵手操作。通过强化学习增强的遥操作技术收集高质量数据，并提出 Mixture-of-Dexterous-Experts (MoE) 架构。该模型能动态路由不同操作技能的专家模块，实现了从视觉引导的抓取到精细布料折叠等多种类人操作的高度泛化，在任务复杂度和灵巧度上达到了新高度。
* **关键词**: Bimanual Dexterous Manipulation, Mixture of Experts (MoE), VLA, Reinforcement Learning.

### [3]. Seed2Scale：具身智能自演进数据引擎
* **Title**: Seed2Scale: A Self-Evolving Data Engine for Embodied AI via Small to Large Model Synergy and Multimodal Evaluation
* **摘要介绍**: 王鹤（He Wang）老师团队新作。具身智能面临严重的数据瓶颈，现有合成方法往往存在分布缺口。Seed2Scale 提出了一种大模型与小模型协同的自演进引擎：利用大型 VLM 生成初始策略并进行多模态评估，通过“从小到大”的迭代反馈过滤低信噪比数据。该引擎克服了自迭代过程中的性能退化风险，在多种具身任务中实现了数据规模与性能的协同扩展，为构建通才机器人提供了低成本、高质量的数据支撑。
* **关键词**: Data Generation, Self-evolving System, Embodied AI, Multimodal Evaluation.

### [4]. 引入视觉推理的上下文模仿学习
* **Title**: ICLR: In-Context Imitation Learning with Visual Reasoning
* **摘要介绍**: 王越（Yue Wang）等研究者提出的 ICLR 框架。尽管 In-Context Learning 允许机器人无需微调即适应新任务，但现有方法常因缺乏显式任务意图表示而失效。ICLR 通过引入视觉推理模块，显式地从少量演示中提取任务目标，并将其作为条件指导策略生成。该方法在处理环境剧烈变化和未见任务时表现出极强的鲁棒性，使机器人能够像人类一样通过“观察”迅速领悟新技能的逻辑。
* **关键词**: In-Context Learning, Imitation Learning, Visual Reasoning, Robotic Adaptation.

### [5]. TacDexGrasp：基于触觉反馈的顺应性机灵抓取
* **Title**: TacDexGrasp: Compliant and Robust Dexterous Grasping with Tactile Feedback
* **摘要介绍**: 王鹤实验室关于触觉感知的又一力作。机灵手的高维力控制一直是难题，本文提出 TacDexGrasp，利用触觉反馈解决多指间的力分布平衡。该模型能实时预测接触点的位置与压力，通过闭环反馈调整手指姿态，从而在无需精确几何模型的情况下，实现对未知物体、易碎物体的稳健抓取。触觉反馈的引入极大增强了机器人在接触密集型任务中的安全性与稳定性。
* **关键词**: Dexterous Grasping, Tactile Feedback, Force Control, Compliant Manipulation.

### 具身智能与世界模型高价值论文

### [6]. TempoFit：为长程 VLA 注入时间序列 KV 记忆
* **Title**: TempoFit: Plug-and-Play Layer-Wise Temporal KV Memory for Long-Horizon Vision-Language-Action Manipulation
* **摘要介绍**: 本文针对 VLA 推理过程中的“无记忆”痛点（Memoryless），提出了 TempoFit 插件。该方法利用层级化的时间 KV 缓存机制，使预训练 VLA 模型能够以极低的计算开销保留历史状态。这在存在遮挡、状态歧义或细微环境变化的非马尔可夫场景中至关重要。作为一种即插即用的方案，TempoFit 无需重新训练 VLA 基座即可显著增强其长程任务的执行一致性。
* **关键词**: Temporal Memory, KV Cache, Long-horizon VLA, Non-Markovian Control.

### [7]. 交互式世界模拟器：可扩展的策略训练平台
* **Title**: Interactive World Simulator for Robot Policy Training and Evaluation
* **摘要介绍**: 李云珠（Yunzhu Li）等团队开发的交互式世界模拟器。现有的世界模型（动作条件视频预测）往往难以保证长程物理一致性。本文提出了一种新型架构，能够在想象的未来空间中维持精确的物体交互逻辑。该模拟器不仅可用于策略的大规模想象训练（Imagination training），还提供了高效的闭环评估环境，大幅降低了在物理机器人上进行大规模 RL 实验的成本和风险。
* **关键词**: World Models, Video Prediction, Policy Training, Physical Consistency.

### [8]. $\pi$-StepNFT：流式 VLA 的在线强化学习加速
* **Title**: $\pi$-StepNFT: Wider Space Needs Finer Steps in Online RL for Flow-based VLAs
* **摘要介绍**: 流式（Flow-based）VLA 模型在表达能力上优于扩散模型，但在多步采样中的似然计算开销限制了在线 RL 的效率。本文提出 $\pi$-StepNFT 算法，通过步进式负样本感知微调（Step-wise Negative-aware Fine-Tuning），实现了高效的在线策略优化。该研究揭示了在更广阔的动作空间中，更细致的采样步长与判别器（Critic）协同的重要性，为 Flow-based 基础模型的在线性能提升提供了理论指导。
* **关键词**: Flow-based Models, Online Reinforcement Learning, VLA, Fine-tuning Strategy.

# 📚 Selected Papers Deep Dive (深度拆解)

### 💡 MEM: Multi-Scale Embodied Memory for Vision Language Action Models [[PDF]](https://arxiv.org/pdf/2603.03596)
> ⚠️ *该论文深度拆解失败，可能是本地 PDF 挂载失败，已拦截大模型的幻觉输出。*

---


### 💡 Towards Human-Like Manipulation through RL-Augmented Teleoperation and Mixture-of-Dexterous-Experts VLA [[PDF]](https://arxiv.org/pdf/2603.08122)
> ⚠️ *该论文深度拆解失败，可能是本地 PDF 挂载失败，已拦截大模型的幻觉输出。*

---


### 💡 Seed2Scale: A Self-Evolving Data Engine for Embodied AI via Small to Large Model Synergy and Multimodal Evaluation [[PDF]](https://arxiv.org/pdf/2603.08260)
> ⚠️ *该论文深度拆解失败，可能是本地 PDF 挂载失败，已拦截大模型的幻觉输出。*

---


### 💡 ICLR: In-Context Imitation Learning with Visual Reasoning [[PDF]](https://arxiv.org/pdf/2603.07530)
> ⚠️ *该论文深度拆解失败，可能是本地 PDF 挂载失败，已拦截大模型的幻觉输出。*

---


### 💡 TacDexGrasp: Compliant and Robust Dexterous Grasping with Tactile Feedback [[PDF]](https://arxiv.org/pdf/2603.07040)
> ⚠️ *该论文深度拆解失败，可能是本地 PDF 挂载失败，已拦截大模型的幻觉输出。*

---


### 💡 TempoFit: Plug-and-Play Layer-Wise Temporal KV Memory for Long-Horizon Vision-Language-Action Manipulation [[PDF]](https://arxiv.org/pdf/2603.07647)
> ⚠️ *该论文深度拆解失败，可能是本地 PDF 挂载失败，已拦截大模型的幻觉输出。*

---


### 💡 Interactive World Simulator for Robot Policy Training and Evaluation [[PDF]](https://arxiv.org/pdf/2603.08546)
> ⚠️ *该论文深度拆解失败，可能是本地 PDF 挂载失败，已拦截大模型的幻觉输出。*

---


### 💡 $π$-StepNFT: Wider Space Needs Finer Steps in Online RL for Flow-based VLAs [[PDF]](https://arxiv.org/pdf/2603.02083)
> ⚠️ *该论文深度拆解失败，可能是本地 PDF 挂载失败，已拦截大模型的幻觉输出。*

---
