# RoboPulse 学术简报

**日期**：2026-03-06 (Friday)

尊敬的研究员，您好！

今日系统从 arXiv 筛选了 116 篇最新论文。基于您的核心研究兴趣（VLA、Sim2Real、RL+VLA 以及 World Model），结合当前具身智能领域的发展趋势，今日研究在**VLA架构的长期记忆与推理效率**、**基于世界模型的低维状态表征规划**以及**大规模Sim2Real的数据合成与策略迁移**上呈现爆发态势。

我们特别为您梳理了您重点关注的名校及名家实验室（如 Chelsea Finn、Hao Su、Cewu Lu、Jiangmiao Pang 等）的重磅新作，以及其他极具价值的前沿突破。

---

## 🌟 重点关注：名校/名家实验室新作

### 1. RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies
* **Title**: RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies
* **摘要介绍**: 记忆机制对于处理长视野和依赖历史信息的机器人操作任务至关重要。本文由 Chelsea Finn 参与合作，提出了 RoboMME 基准，专门用于评估当前视觉-语言-动作（VLA）模型中的记忆能力。该研究深入分析了 VLA 模型在处理被遮挡物体或重复性动作时的表现，指出了当前通用策略在长序列推理中的局限性，并为未来记忆增强型机器人的发展指明了方向。
* **关键词**: VLA, Memory, Benchmark, Generalist Policies

### 2. UltraDexGrasp: Learning Universal Dexterous Grasping for Bimanual Robots with Synthetic Data
* **Title**: UltraDexGrasp: Learning Universal Dexterous Grasping for Bimanual Robots with Synthetic Data
* **摘要介绍**: 庞江淼（Jiangmiao Pang）团队提出了一种利用纯合成数据学习双臂机器人通用灵巧抓取的方法。面对当前抓取策略在多指灵巧手上的泛化难题，UltraDexGrasp 成功实现了从仿真到真实世界（Sim2Real）的无缝迁移，使机器人能够根据物体属性自主选择合适的双臂抓取策略，大大降低了真实世界数据采集的成本。
* **关键词**: Dexterous Grasping, Sim2Real, Bimanual Robots, Synthetic Data

### 3. RoboPocket: Improve Robot Policies Instantly with Your Phone
* **Title**: RoboPocket: Improve Robot Policies Instantly with Your Phone
* **摘要介绍**: 卢策吾（Cewu Lu）团队针对机器人模仿学习中数据收集效率低下的痛点，开发了 RoboPocket 系统。该系统允许操作者使用智能手机不仅能够收集野外交互数据，还能即时获得策略改进的反馈结果，形成闭环。这一创新将极大地促进具身策略在真实场景下的快速迭代和部署。
* **关键词**: Imitation Learning, Data Collection, Policy Improvement, Teleoperation

### 4. Seeing the Bigger Picture: 3D Latent Mapping for Mobile Manipulation Policy Learning
* **Title**: Seeing the Bigger Picture: 3D Latent Mapping for Mobile Manipulation Policy Learning
* **摘要介绍**: 郝苏（Hao Su）团队展示了利用 3D 隐式建图进行移动操作策略学习的优势。相较于仅依赖图像输入的传统方法，系统能够直接在 3D 地图上进行空间和时间维度的深入推理。这种类似于世界模型的隐式表征，显著增强了机器人在复杂移动操作任务中的全局感知与规划能力。
* **关键词**: Mobile Manipulation, 3D Latent Mapping, Policy Learning

---

## 🚀 具身智能与世界模型高价值论文

### 5. Critic in the Loop: A Tri-System VLA Framework for Robust Long-Horizon Manipulation
* **Title**: Critic in the Loop: A Tri-System VLA Framework for Robust Long-Horizon Manipulation
* **摘要介绍**: 平衡高层语义推理与底层反应控制是 VLA 模型面临的难题。本文提出了一种创新的三系统 VLA 框架，引入了“Critic”模块来进行闭环反馈。这种 RL+VLA 的思想有效弥补了传统 VLA 在实时执行上的不足和 VLM 推理延迟，显著提升了机器人在长视野复杂操作任务中的鲁棒性。
* **关键词**: VLA, Reinforcement Learning, Long-Horizon Manipulation

### 6. PhysiFlow: Physics-Aware Humanoid Whole-Body VLA via Multi-Brain Latent Flow Matching
* **Title**: PhysiFlow: Physics-Aware Humanoid Whole-Body VLA via Multi-Brain Latent Flow Matching and Robust Tracking
* **摘要介绍**: 针对人形机器人全身控制，本文将 VLA 与物理感知进行深度融合。PhysiFlow 采用多脑潜空间流匹配（Latent Flow Matching）技术，有效解决了现有 VLA 推理效率低和缺乏语义级全身运动跟踪的问题，为人形机器人在真实世界执行复杂语义指令提供了新范式。
* **关键词**: Humanoid, VLA, Whole-Body Control, Flow Matching

### 7. Act, Think or Abstain: Complexity-Aware Adaptive Inference for Vision-Language-Action Models
* **Title**: Act, Think or Abstain: Complexity-Aware Adaptive Inference for Vision-Language-Action Models
* **摘要介绍**: 随着 VLA 模型复杂度的提升，其推理延迟问题日益凸显。本文提出了一种复杂度感知自适应推理机制，允许 VLA 模型根据当前环境和任务难度，在“行动”、“思考（深度推理）”或“弃权”之间动态切换。这在保证策略泛化性的同时，有效降低了系统的计算开销。
* **关键词**: VLA, Adaptive Inference, Efficiency, Generalization

### 8. Planning in 8 Tokens: A Compact Discrete Tokenizer for Latent World Model
* **Title**: Planning in 8 Tokens: A Compact Discrete Tokenizer for Latent World Model
* **摘要介绍**: 世界模型是实现高效决策规划的关键。本文提出了一种极其紧凑的离散 Tokenizer 设计，仅需 8 个 Token 即可有效表征隐式世界模型的状态。这种高度压缩的表征大幅加速了决策时的环境动态模拟与预测，为世界模型在资源受限的机器人系统上的实时应用扫清了障碍。
* **关键词**: World Model, Discrete Tokenizer, Action Planning, Decision Making

### 9. DDP-WM: Disentangled Dynamics Prediction for Efficient World Models
* **Title**: DDP-WM: Disentangled Dynamics Prediction for Efficient World Models
* **摘要介绍**: 现有基于 Transformer 的稠密世界模型计算代价高昂。本文提出了 DDP-WM，通过解耦环境动态预测过程，极大地提升了世界模型的计算效率。该方法突破了性能与效率之间的瓶颈，为自主机器人的实时规划提供了更轻量化、更高效的世界模型构建方案。
* **关键词**: World Model, Dynamics Prediction, Efficient Planning

### 10. PTLD: Sim-to-real Privileged Tactile Latent Distillation for Dexterous Manipulation
* **Title**: PTLD: Sim-to-real Privileged Tactile Latent Distillation for Dexterous Manipulation
* **摘要介绍**: 灵巧操作需要精细的触觉感知反馈。本文提出了一种从仿真到现实（Sim2Real）的特权触觉隐式知识蒸馏方法（PTLD）。该方法在仿真中利用全局特权信息提取隐式特征，再将其蒸馏给真实世界中的触觉策略模型，极大缓解了在现实中收集多指机械手高质量演示数据的困难。
* **关键词**: Sim2Real, Dexterous Manipulation, Tactile Sensing, Distillation

# 📚 Selected Papers Deep Dive (深度拆解)

### 💡 RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies [[PDF]](https://arxiv.org/pdf/2603.04639)
> ⚠️ *该论文深度拆解失败，可能是本地 PDF 挂载失败，已拦截大模型的幻觉输出。*

---


### 💡 UltraDexGrasp: Learning Universal Dexterous Grasping for Bimanual Robots with Synthetic Data [[PDF]](https://arxiv.org/pdf/2603.05312)
> ⚠️ *该论文深度拆解失败，可能是本地 PDF 挂载失败，已拦截大模型的幻觉输出。*

---


### 💡 RoboPocket: Improve Robot Policies Instantly with Your Phone [[PDF]](https://arxiv.org/pdf/2603.05504)
> ⚠️ *该论文深度拆解失败，可能是本地 PDF 挂载失败，已拦截大模型的幻觉输出。*

---


### 💡 Seeing the Bigger Picture: 3D Latent Mapping for Mobile Manipulation Policy Learning [[PDF]](https://arxiv.org/pdf/2510.03885)
> ⚠️ *该论文深度拆解失败，可能是本地 PDF 挂载失败，已拦截大模型的幻觉输出。*

---


### 💡 Critic in the Loop: A Tri-System VLA Framework for Robust Long-Horizon Manipulation [[PDF]](https://arxiv.org/pdf/2603.05185)
> ⚠️ *该论文深度拆解失败，可能是本地 PDF 挂载失败，已拦截大模型的幻觉输出。*

---


### 💡 PhysiFlow: Physics-Aware Humanoid Whole-Body VLA via Multi-Brain Latent Flow Matching and Robust Tracking [[PDF]](https://arxiv.org/pdf/2603.05410)
> ⚠️ *该论文深度拆解失败，可能是本地 PDF 挂载失败，已拦截大模型的幻觉输出。*

---


### 💡 Act, Think or Abstain: Complexity-Aware Adaptive Inference for Vision-Language-Action Models [[PDF]](https://arxiv.org/pdf/2603.05147)
> ⚠️ *该论文深度拆解失败，可能是本地 PDF 挂载失败，已拦截大模型的幻觉输出。*

---


### 💡 Planning in 8 Tokens: A Compact Discrete Tokenizer for Latent World Model [[PDF]](https://arxiv.org/pdf/2603.05438)
> ⚠️ *该论文深度拆解失败，可能是本地 PDF 挂载失败，已拦截大模型的幻觉输出。*

---


### 💡 DDP-WM: Disentangled Dynamics Prediction for Efficient World Models [[PDF]](https://arxiv.org/pdf/2602.01780)
> ⚠️ *该论文深度拆解失败，可能是本地 PDF 挂载失败，已拦截大模型的幻觉输出。*

---


### 💡 PTLD: Sim-to-real Privileged Tactile Latent Distillation for Dexterous Manipulation [[PDF]](https://arxiv.org/pdf/2603.04531)
> ⚠️ *该论文深度拆解失败，可能是本地 PDF 挂载失败，已拦截大模型的幻觉输出。*

---
