# RoboPulse 学术简报 (2026-03-11)

各位研究同仁，大家好。今天是 2026年3月11日，星期三。在今日检索到的 117 篇 arXiv 机器人学论文中，我们发现 **Vision-Language-Action (VLA)** 模型与**世界模型 (World Models)** 的融合正成为该领域的绝对主流，同时 **Sim2Real** 和强化学习 (RL) 在复杂操作中的应用也在不断突破。本期简报特别为您甄选了匹配您研究兴趣（VLA, Sim2Real, RL+VLA, World Model）的高质量论文，并重点解析了 Pieter Abbeel、Huazhe Xu、He Wang 等名家实验室的最新成果。

## 🌟 重点关注：名校/名家实验室新作

### 1. RL-100: Performant Robotic Manipulation with Real-World Reinforcement Learning
* **Title**: RL-100: Performant Robotic Manipulation with Real-World Reinforcement Learning
* **摘要介绍**: 真实世界中的机器人操作需要极高的可靠性与鲁棒性。本文（由 Huazhe Xu 等人提出）构建了一个基于扩散视觉运动策略的现实世界强化学习框架 RL-100。该工作直击真实物理环境中数据采集与探索安全的痛点，将模仿学习与强化学习无缝结合，在复杂操作任务中实现了接近甚至超越人类专家的表现，为 RL+VLA 的实际部署提供了极具价值的范式。
* **关键词**: Reinforcement Learning, Real-World Manipulation, Diffusion Policy

### 2. EgoMI: Learning Active Vision and Whole-Body Manipulation from Egocentric Human Demonstrations
* **Title**: EgoMI: Learning Active Vision and Whole-Body Manipulation from Egocentric Human Demonstrations
* **摘要介绍**: 尽管从人类演示中进行模仿学习潜力巨大，但第一人称数据存在显著的具身鸿沟。来自 Pieter Abbeel 团队的这项研究 EgoMI 攻克了这一难题。论文深入探讨了人类在操作中如何主动协调头部与手部运动，并提出了一种有效的方法，将主动视觉与全身控制的策略转移至机器人平台，大幅提升了机器人在未知环境中的灵巧操作与适应能力。
* **关键词**: Imitation Learning, Active Vision, Whole-Body Manipulation

### 3. Emerging Extrinsic Dexterity in Cluttered Scenes via Dynamics-aware Policy Learning
* **Title**: Emerging Extrinsic Dexterity in Cluttered Scenes via Dynamics-aware Policy Learning
* **摘要介绍**: 在杂乱环境中利用环境接触实现非抓取式操作一直是机器人操作的难点。He Wang 团队的这项工作通过动力学感知策略学习，赋予了机器人“外部灵巧性”（Extrinsic Dexterity）。该方法通过选择性利用多个交互物体之间的接触力学，成功绕过了传统预抓取操作的限制，为复杂场景下的强化学习控制带来了新突破。
* **关键词**: Extrinsic Dexterity, Dynamics-aware Policy, Reinforcement Learning

### 4. SPAN-Nav: Generalized Spatial Awareness for Versatile Vision-Language Navigation
* **Title**: SPAN-Nav: Generalized Spatial Awareness for Versatile Vision-Language Navigation
* **摘要介绍**: 同样来自 He Wang 团队的工作。当前基于视觉语言模型（VLM）的具身导航由于空间感知不足，在复杂环境中的路径规划可靠性受限。本文提出了 SPAN-Nav，通过增强模型对广义空间信息的理解，有效提升了跨场景与指令的泛化能力，为基于视觉语言的大型导航模型确立了新基准。
* **关键词**: Vision-Language Navigation, Spatial Awareness, Embodied AI

## 🔥 具身智能与世界模型高价值论文

### 5. PlayWorld: Learning Robot World Models from Autonomous Play
* **Title**: PlayWorld: Learning Robot World Models from Autonomous Play
* **摘要介绍**: 建立通用的机器人模拟器需要准确的物理规律预测，但当前基于大规模数据集的视频模型在物理交互一致性上仍表现挣扎。本文提出了 PlayWorld 框架，通过机器人的自主探索收集交互数据，训练动作条件下的视频世界模型。该模型直击物理规律一致性的痛点，显著提升了预测与生成的可靠性。
* **关键词**: World Model, Autonomous Play, Video Generation

### 6. Pri4R: Learning World Dynamics for Vision-Language-Action Models with Privileged 4D Representation
* **Title**: Pri4R: Learning World Dynamics for Vision-Language-Action Models with Privileged 4D Representation
* **摘要介绍**: 现有的 VLA 模型擅长语义理解，但在捕捉物理交互的时空动态时往往失效。本文创新性地引入了特权 4D 表示来为 VLA 模型学习世界动态。通过联合建模机器人的自身运动和环境的物理反馈，Pri4R 极大地提升了模型在复杂接触与动态环境中的推断与控制能力。
* **关键词**: Vision-Language-Action, World Dynamics, 4D Representation

### 7. DexHiL: A Human-in-the-Loop Framework for Vision-Language-Action Model Post-Training in Dexterous Manipulation
* **Title**: DexHiL: A Human-in-the-Loop Framework for Vision-Language-Action Model Post-Training in Dexterous Manipulation
* **摘要介绍**: 将 VLA 模型部署于特定且复杂的下游灵巧操作任务时，往往需要高效的后训练。本文提出了 DexHiL，一个“人在回路”的微调框架，通过利用人类反馈有效地解决模型在精细动作执行中的误差累积问题。该框架为提高 VLA 模型的微操精度和数据效率提供了系统性方案。
* **关键词**: Vision-Language-Action, Human-in-the-Loop, Dexterous Manipulation

### 8. A Distributional Treatment of Real2Sim2Real for Object-Centric Agent Adaptation in Vision-Driven Deformable Linear Object Manipulation
* **Title**: A Distributional Treatment of Real2Sim2Real for Object-Centric Agent Adaptation in Vision-Driven Deformable Linear Object Manipulation
* **摘要介绍**: 柔性物体的操作一直是 Sim2Real 迁移的重灾区。本文针对基于视觉的形变线状物体（DLO）操作，提出了一个端到端的 Real2Sim2Real 框架。通过免似然推理（LFI）计算物理参数的后验分布，该方法极大地缓解了仿真器参数与真实物理之间的差异，为高难度柔性物体的 Sim2Real 落地提供了坚实理论与实践基础。
* **关键词**: Sim2Real, Deformable Object Manipulation, Likelihood-Free Inference

### 9. NS-VLA: Towards Neuro-Symbolic Vision-Language-Action Models
* **Title**: NS-VLA: Towards Neuro-Symbolic Vision-Language-Action Models
* **摘要介绍**: 尽管 VLA 模型取得了长足进展，但其在学习可重用基元和降低对庞大数据依赖方面仍面临挑战。NS-VLA 探索了神经符号学方法与 VLA 模型的结合路径，试图利用符号逻辑增强模型的抽象泛化和推理能力。此方法有望大幅度降低端到端 VLA 模型的数据饥渴问题，提升其透明度和可靠性。
* **关键词**: Neuro-Symbolic, Vision-Language-Action, Robotic Manipulation

### 10. Latent Policy Steering with Embodiment-Agnostic Pretrained World Models
* **Title**: Latent Policy Steering with Embodiment-Agnostic Pretrained World Models
* **摘要介绍**: 学习型机器人策略高度依赖于训练数据的规模与质量，但异构的具身差异限制了数据集的复用。本文提出了一种利用具身不可知的预训练世界模型在隐空间内进行策略引导的方法。它能够有效地克服不同机械臂或机器人形态间的动作空间不匹配，实现策略的高效迁移。
* **关键词**: World Model, Policy Steering, Embodiment-Agnostic

# 📚 Selected Papers Deep Dive (深度拆解)

### 💡 RL-100: Performant Robotic Manipulation with Real-World Reinforcement Learning [[PDF]](https://arxiv.org/pdf/2510.14830)
> ⚠️ *该论文深度拆解失败，可能是本地 PDF 挂载失败，已拦截大模型的幻觉输出。*

---


### 💡 EgoMI: Learning Active Vision and Whole-Body Manipulation from Egocentric Human Demonstrations [[PDF]](https://arxiv.org/pdf/2511.00153)
> ⚠️ *该论文深度拆解失败，可能是本地 PDF 挂载失败，已拦截大模型的幻觉输出。*

---


### 💡 Emerging Extrinsic Dexterity in Cluttered Scenes via Dynamics-aware Policy Learning [[PDF]](https://arxiv.org/pdf/2603.09882)
> ⚠️ *该论文深度拆解失败，可能是本地 PDF 挂载失败，已拦截大模型的幻觉输出。*

---


### 💡 SPAN-Nav: Generalized Spatial Awareness for Versatile Vision-Language Navigation [[PDF]](https://arxiv.org/pdf/2603.09163)
> ⚠️ *该论文深度拆解失败，可能是本地 PDF 挂载失败，已拦截大模型的幻觉输出。*

---


### 💡 PlayWorld: Learning Robot World Models from Autonomous Play [[PDF]](https://arxiv.org/pdf/2603.09030)
> ⚠️ *该论文深度拆解失败，可能是本地 PDF 挂载失败，已拦截大模型的幻觉输出。*

---


### 💡 Pri4R: Learning World Dynamics for Vision-Language-Action Models with Privileged 4D Representation [[PDF]](https://arxiv.org/pdf/2603.01549)
> ⚠️ *该论文深度拆解失败，可能是本地 PDF 挂载失败，已拦截大模型的幻觉输出。*

---


### 💡 DexHiL: A Human-in-the-Loop Framework for Vision-Language-Action Model Post-Training in Dexterous Manipulation [[PDF]](https://arxiv.org/pdf/2603.09121)
> ⚠️ *该论文深度拆解失败，可能是本地 PDF 挂载失败，已拦截大模型的幻觉输出。*

---


### 💡 A Distributional Treatment of Real2Sim2Real for Object-Centric Agent Adaptation in Vision-Driven Deformable Linear Object Manipulation [[PDF]](https://arxiv.org/pdf/2502.18615)
> ⚠️ *该论文深度拆解失败，可能是本地 PDF 挂载失败，已拦截大模型的幻觉输出。*

---


### 💡 NS-VLA: Towards Neuro-Symbolic Vision-Language-Action Models [[PDF]](https://arxiv.org/pdf/2603.09542)
> ⚠️ *该论文深度拆解失败，可能是本地 PDF 挂载失败，已拦截大模型的幻觉输出。*

---


### 💡 Latent Policy Steering with Embodiment-Agnostic Pretrained World Models [[PDF]](https://arxiv.org/pdf/2507.13340)
> ⚠️ *该论文深度拆解失败，可能是本地 PDF 挂载失败，已拦截大模型的幻觉输出。*

---
