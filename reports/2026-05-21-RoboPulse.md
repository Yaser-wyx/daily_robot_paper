# RoboPulse | 2026-05-21

> **Focus**: VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, World Model, World Action Model
> **Pipeline**: 86 papers scanned · 10 shortlisted · 6 editor's picks

今天的主线很清晰：VLA 正在从“把视觉和语言接到动作头”转向更强的几何、未来状态、闭环交互和可复现实机评测。最终精选保留了三类互补方向：操控里的 3D/点云/高斯 world model，自动驾驶里的未来视觉锚定与 latent multi-agent rollout，以及一篇系统性 VLA recipes 论文，适合用来校准后续阅读与复现优先级。Sim2Real 的核心信号不是单篇方法宣称，而是 VLA-REPLICA 这类低成本真实评测与 GaussianDream/PointACT 的真实机器人迁移证据正在把“真实可用性”推到中心。VIP 作者方面，最终精选中没有直接命中核心名单；watchlist 里的 Dorsa Sadigh 参与 PSN，且主题涉及人机共享控制安全，值得单独跟踪。

## 今日信号

- VLA 的下一轮增益很可能来自显式 3D 几何与短时未来状态监督，而不只是更大的 VLM backbone 或更多行为克隆数据。
- 自动驾驶 VLA 的关键矛盾从开放环轨迹拟合转向闭环、反事实视觉依赖、解释一致性和交互式环境建模。
- 真实机器人评测正在成为方法可信度分水岭：低成本可复现 benchmark、真实迁移和跨装置一致性比单一仿真榜单更重要。

## Historical Rediscovery

- **Paper**: OrbiSim: World Models as Differentiable Physics Engines for Embodied Intelligence [[HTML]](https://arxiv.org/html/2605.16395) [[PDF]](https://arxiv.org/pdf/2605.16395)
  - **Paper ID**: `2605.16395`
  - **来源日期**: 2026-05-19
  - **当时可能被低估的信号**: 当时可能低估了“world model as differentiable physics engine”这一定位的范式价值，尤其是它不是单纯预测视频，而是试图服务可微仿真与 RL 优化。
  - **为什么现在值得再看**: 如果你现在关心 World Action Model 或 RL+VLA 的训练环境，这篇可作为连接世界模型、物理一致性和策略学习的基础候选。
  - **建议动作**: 加入精读
  - **关键词**: `World Model` `Differentiable Simulation` `RL` `Sim2Real`
- **Paper**: RLDX-1 Technical Report [[HTML]](https://arxiv.org/html/2605.03269) [[PDF]](https://arxiv.org/pdf/2605.03269)
  - **Paper ID**: `2605.03269`
  - **来源日期**: 2026-05-07
  - **当时可能被低估的信号**: 被低估的信号是其工程覆盖面和真实部署取向：长期记忆、物理感知和多 benchmark 评测都不是普通 VLA demo 的配置。
  - **为什么现在值得再看**: 对 VLA 走向真实部署、长时程操作和具身系统集成判断很有参考价值，尤其适合作为对照检查当前 WAM/VLA 系统到底缺什么。
  - **建议动作**: 加入精读
  - **关键词**: `VLA` `Dexterous Manipulation` `Long-term Memory` `Real Deployment`
- **Paper**: GuidedVLA: Specifying Task-Relevant Factors via Plug-and-Play Action Attention Specialization [[HTML]](https://arxiv.org/html/2605.12369) [[PDF]](https://arxiv.org/pdf/2605.12369)
  - **Paper ID**: `2605.12369`
  - **来源日期**: 2026-05-13
  - **当时可能被低估的信号**: 当时可能低估了“object grounding、skill recognition、geometry perception 分解到 action decoder 注意力”对真实泛化和鲁棒评测的诊断价值。
  - **为什么现在值得再看**: 它和 VLA 鲁棒性、真实双臂部署、几何感知到动作生成的因果绑定有关，适合重新评估其是否可作为 WAM/VLA 的可解释动作接口。
  - **建议动作**: 加入精读
  - **关键词**: `VLA` `Action Attention` `Robustness` `Bimanual Real Robot`
- **Paper**: Seeing Realism from Simulation: Efficient Video Transfer for Vision-Language-Action Data Augmentation [[HTML]](https://arxiv.org/html/2605.02757) [[PDF]](https://arxiv.org/pdf/2605.02757)
  - **Paper ID**: `2605.02757`
  - **来源日期**: 2026-05-05
  - **当时可能被低估的信号**: 被低估的是它对低成本 Sim2Real 的直接性：相比纯模型结构创新，训练数据分布的现实化可能更快影响真实泛化。
  - **为什么现在值得再看**: 如果你今天关注 Sim2Real 或真实部署前的数据扩展，它值得作为 VLA 训练数据工程与生成式仿真桥接方案重看。
  - **建议动作**: 快速浏览
  - **关键词**: `Sim2Real` `VLA Data Augmentation` `Video Transfer` `Realistic Simulation`
- **Paper**: Thinking in Text and Images: Interleaved Vision--Language Reasoning Traces for Long-Horizon Robot Manipulation [[HTML]](https://arxiv.org/html/2605.00438) [[PDF]](https://arxiv.org/pdf/2605.00438)
  - **Paper ID**: `2605.00438`
  - **来源日期**: 2026-05-04
  - **当时可能被低估的信号**: 当时可能低估了“interleaved text-image reasoning trace”作为 VLA 与长时程 action planning 接口的价值。
  - **为什么现在值得再看**: 它和长时程操作、VLA 可解释中间状态、World Action Model 的动作-视觉轨迹表达都有联系，适合用来补充底层 world model 之外的规划接口视角。
  - **建议动作**: 继续跟踪
  - **关键词**: `Long-horizon Manipulation` `VLA` `Reasoning Trace` `Planning Interface`

## Editor's Picks

### [1]. GaussianDream: A Feed-Forward 3D Gaussian World Model for Robotic Manipulation [[HTML]](https://arxiv.org/html/2605.20752) [[PDF]](https://arxiv.org/pdf/2605.20752) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.20752`
* **Authors**: Zijian Zhang, Yuqing Jiang, Qian Cheng, Si Liu, Ding Zhao, Ping Luo, Weitao Zhou, Haibao Yu
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为 GaussianDream 把 3D Gaussian world model 作为训练期插件接入 VLA，用密集几何和短时未来监督补足纯行为克隆的空间感。
* **关键词**: `VLA` `3D Gaussian` `world model` `robot manipulation` `future prediction`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

这篇针对的是语言条件操控中一个越来越明显的短板：VLA 借助 VLM 获得语义泛化，但动作学习仍主要由 demonstration imitation 驱动，对 3D 几何、深度结构和短时环境演化的显式监督不足。对精密操控来说，物体接触、遮挡、位姿和局部运动都不是文本语义能直接解决的问题；如果策略只学到图像到动作的相关性，遇到空间布局变化或长一点的执行链就容易失稳。GaussianDream 的动机是把机器人轨迹变成可渲染、可预测的空间时间监督，让 VLA 在不牺牲推理效率的前提下获得更强的物理 grounding。

#### ⚙️ 核心方法

GaussianDream 的核心是一个 feed-forward 3D Gaussian world-model plug-in。训练时，它把当前观测重建成 3D Gaussian 表示，并加入 horizon-conditioned future Gaussian prediction，要求一个紧凑的 spatio-temporal prefix 能解码为当前和未来的可渲染 3D Gaussian 状态。由此模型可以利用 dense RGB rendering、depth 和 pseudo 3D scene-flow 作为监督信号，把普通机器人视频转化为更密集的几何学习目标。关键设计是非对称的：训练期保留 Gaussian reconstruction 与 future prediction 的辅助头来塑造 prefix，推理期则丢弃这些解码头，只把学到的 prefix 用作动作生成条件，因此不需要在线渲染、视频 rollout 或额外规划器。相对已有 3D-enhanced VLA 或 world-model 路线，新意在于它不是把 3D 当作静态感知特征，而是把当前重建和短时未来预测绑定成动作前缀监督。当前摘录能确认的接口主要是 prefix conditioning 与辅助解码头；具体 Gaussian 参数化、loss 权重和动作头细节需要看 PDF。

#### 📊 实验与结果

实验覆盖仿真和真实操控。仿真部分包括 LIBERO 的 Spatial、Object、Goal、Long 协议，摘录明确写到每个设置用 50 条 human demonstrations 训练、50 次 evaluation trials；RoboCasa 使用 Human-50 few-shot 设置，覆盖 24 个长时程厨房任务，并在五个场景中每任务 50 次试验。作者设置的验证目标包括：是否优于强 VLA、3D-enhanced 和 world-model baseline，prefix 是否迁移到真实机器人，当前重建与未来预测是否互补，以及 rendering/depth loss 是否把视频转成有效几何信号。HTML 摘录没有给出具体成功率或表格数值，因此只能保守判断其证据框架较完整，真实机器人部分是进入精选的关键，但强弱结论仍需核查完整表格。

#### ⚠️ 风险 / 保留意见

- 训练期依赖 3D Gaussian 重建和未来预测，数据、相机标定或场景可观测性变化可能影响监督质量。
- HTML 摘录未给出具体性能数值，当前只能确认 benchmark 覆盖面和实验主张，不能判断提升幅度是否稳定。
- 推理期虽无解码开销，但 prefix 是否真正编码可迁移几何而非 benchmark 特定相关性，需要看消融和跨域实验。

#### 💭 结论与启发

这篇对后续系统设计的启发是：world model 不一定要在推理期 rollout 才有价值，也可以作为训练期结构化监督来改造 VLA 表征。对复现而言，优先拆解“当前重建 + 未来预测 + prefix conditioning”三者各自贡献，而不是只复现最终大模型。选题上，它提示操控 VLA 可以围绕“训练期密集几何监督、推理期轻量动作条件”形成一条实用路线。

#### 🔎 读 PDF 先核查

- GaussianDream 的 spatio-temporal prefix 在动作头中如何注入，是否与原 VLA token 表示存在明确的对齐或融合机制？
- 当前 Gaussian reconstruction 与 horizon-conditioned future prediction 的消融是否分别提升不同类型任务，例如 spatial、long-horizon 或 kitchen tasks？
- 真实机器人评测中，失败案例主要来自几何重建误差、未来预测误差，还是动作策略本身的 distribution shift？

#### 📌 上传 PDF 后优先看

- 方法章节中的 Gaussian 表示、prefix 设计与训练/推理非对称结构。
- LIBERO、RoboCasa 和真实机器人结果表，以及与 3D-enhanced/world-model baseline 的对比。
- 消融章节，尤其是 current reconstruction、future prediction、RGB/depth/scene-flow loss 的单独贡献。

### [2]. VLA-REPLICA: A Low-Cost, Reproducible Benchmark for Real-World Evaluation of Vision-Language-Action Models [[HTML]](https://arxiv.org/html/2605.20774) [[PDF]](https://arxiv.org/pdf/2605.20774) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.20774`
* **Authors**: Alex S. Huang, Jiahui Zhang, Shiqing Tang, Yu Xiang
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为 VLA-REPLICA 不是再提出一个 VLA，而是在补真实世界评测的基础设施短板。
* **关键词**: `VLA benchmark` `real-world evaluation` `reproducibility` `low-cost robotics` `OOD generalization`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

#### 📖 背景与动机

VLA 论文越来越多，但真实世界评价仍不够可复现。仿真 benchmark 可扩展、标准化，却可能高估实机表现；真实机器人 benchmark 又常受昂贵硬件、集中评测、任务多样性不足和跨实验室不一致影响。对 VLA 来说，这会导致一个危险局面：模型在论文表格中看似进步，但不同实验室无法低成本复核，也难以判断提升来自策略本身、硬件调参还是场景偶然性。VLA-REPLICA 的价值在于把评测问题前置，试图用 off-the-shelf components 搭出可复制的真实操控环境，让 in-distribution adaptation 和 out-of-distribution generalization 都能在统一协议下比较。

#### ⚙️ 核心方法

这篇的“方法”更像 benchmark/system design。VLA-REPLICA 用低成本、易组装的硬件与标准化环境设计，提供一套可在不同实验室复刻的真实 VLA 评测平台。它包含多样化操控任务，以及一个小规模 demonstration dataset，用于 target-domain adaptation；评测协议覆盖 in-distribution 和 out-of-distribution 设置。其关键接口不是某个新动作模型，而是统一硬件、场景、任务、演示数据和评测流程，使 imitation learning 方法与 state-of-the-art VLA models 能在同一真实环境中接受检验。摘录还强调 independently constructed setups 的结果一致性，这说明作者关注的不只是任务成功率，还包括 benchmark 自身的可复制性。当前摘录只能确认系统目标、协议组成和一致性主张；具体硬件 BOM、任务定义、相机/机械臂配置、评分规则和数据格式需要 PDF 核查。

#### 📊 实验与结果

实验部分从摘录可确认的是：作者比较了 imitation learning 和现有 VLA models，并在真实世界中评估其 strengths and limitations；benchmark 覆盖 target-domain adaptation 与 OOD generalization；还展示了独立搭建装置之间的 evaluation results consistent。HTML 摘录没有提供具体模型名称、任务数量、成功率或方差，因此不能引用定量结论。即便如此，这篇进入精选的原因是证据类型稀缺：它把真实评测、低成本复刻和跨装置一致性作为研究对象，而不是只在一个实验室的单套机器人上展示效果。后续需要重点看是否有足够严格的校准流程与统计报告。

#### ⚠️ 风险 / 保留意见

- benchmark 的低成本设计可能牺牲任务复杂度或操作精度，需警惕只覆盖窄域桌面操控。
- 若任务协议、环境搭建误差或人工复位流程不够严格，跨实验室一致性可能难以长期维持。
- HTML 摘录缺少具体模型结果和硬件细节，目前无法判断它对主流 VLA 排名的区分度。

#### 💭 结论与启发

这篇适合作为后续 VLA 实机复现实验的基础参考。与其继续比较不可复刻的单实验室 demo，不如优先建立低成本、可重复、可共享的真实评测协议。对阅读策略来说，我会把它和 GaussianDream、PointACT 放在一起看：前两篇回答“如何增强 VLA”，这篇回答“增强后怎样被别人验证”。如果协议足够清楚，它可能比单个模型论文更有长期价值。

#### 🔎 读 PDF 先核查

- VLA-REPLICA 的硬件和环境公差如何定义，跨实验室搭建差异如何被校准或记录？
- 小规模 demonstration dataset 在 target-domain adaptation 中扮演多大角色，是否会掩盖预训练 VLA 的真实泛化能力？
- OOD 设置具体改变了哪些因素：物体、布局、语言指令、光照，还是多项同时变化？

#### 📌 上传 PDF 后优先看

- benchmark 架构与硬件搭建章节，包括 BOM、校准和复位流程。
- 任务套件与 ID/OOD 评测协议，特别是评分指标和失败定义。
- 跨独立装置一致性实验，以及不同 VLA/IL 方法的真实世界对比表。

### [3]. Grounding Driving VLA via Inverse Kinematics [[HTML]](https://arxiv.org/html/2605.21061) [[PDF]](https://arxiv.org/pdf/2605.21061) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.21061`
* **Authors**: Junsung Park, Hyunjung Shim
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为它把 Driving VLA 的“看图却不用图”问题重新表述为 inverse kinematics 边界条件缺失，并给出未来视觉状态监督。
* **关键词**: `Driving VLA` `inverse kinematics` `future visual state` `blind planning` `counterfactual analysis`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

#### 📖 背景与动机

自动驾驶 VLA 试图用相机图像、文本命令和状态输入直接输出未来轨迹，但摘录指出一个结构性问题：许多模型虽然形式上接收视觉 token，实际规划却主要依赖 ego status 和文本命令，进入 blind planning。对安全驾驶来说，这比普通性能下降更危险，因为前车、障碍物或车道变化没有真正进入决策链。作者认为问题不只是训练不足，而是任务 formulation 不适定：从 inverse kinematics 角度看，轨迹恢复需要当前与未来视觉状态作为边界条件；现有 VLA 只给当前视觉状态，容易学到状态和命令捷径。

#### ⚙️ 核心方法

方法把 Driving VLA 改造成类似 inverse kinematics solver 的结构。第一步是 next visual state prediction objective：要求 LLM 预测未来视觉状态，使视觉 token 必须承载与下一时刻场景相关的信息，而不是被 ego status/text shortcut 替代。第二步是 Inverse Kinematics Network，它从当前视觉状态和预测的未来视觉状态解码轨迹，并通过结构设计压低对 ego-status 和文本捷径的依赖。实验设置中，作者使用 Qwen2.5-0.5B-Instruct 作为 LLM backbone，DINOv3 ViT-S/16 作为视觉编码器；IK Network 是 cross-attention-based conditional diffusion model，使用 cosine schedule，并在推理时进行 DDPM sampling。摘录还提到在 NAVSIM 上跟随 RecogDrive 的 2-stage SFT/GRPO 流程。新意在于它不把视觉依赖当作 attention 可解释性问题，而是通过未来视觉边界条件和轨迹解码结构强制模型恢复图像使用。具体未来视觉状态的表示形式、监督来源和 loss 细节需要看完整方法。

#### 📊 实验与结果

实验覆盖 NAVSIM 和 nuScenes。NAVSIM 是 closed-loop benchmark，作者在 NAVSIM-v1 和 NAVSIM-v2 上分别使用 PDMS 和 EPDMS，并报告 NC、DAC、TTC 等细分指标；nuScenes 使用 700 个 train scenes 和 150 个 val scenes，规划用 ADE 和 Collision Rate，场景理解用 nu-Caption、nu-X 和 nuScenes-QA。结论摘录声称 0.5B 模型通过 GradCAM 和 counterfactual analyses 验证了视觉特征利用，并在 NAVSIM 上达到 state-of-the-art trajectory planning。由于摘录没有给出具体分数，不能判断 SOTA 幅度；但它的证据组合值得看：闭环规划、开放环 nuScenes、视觉使用诊断和反事实测试都直接对应其核心主张。

#### ⚠️ 风险 / 保留意见

- 未来视觉状态预测可能引入新的误差源，若预测状态偏离真实环境，IK 解码轨迹可能被错误锚定。
- DDPM sampling 的推理成本和实时性需要核查，尤其是自动驾驶闭环部署。
- 摘录未给定具体 SOTA 分数，视觉利用的提升是否稳定跨场景仍需看反事实和失败案例。

#### 💭 结论与启发

这篇给 Driving VLA 一个很有用的诊断框架：不要只问模型有没有视觉输入，要问轨迹任务是否迫使视觉成为必要边界条件。对后续研究，类似思路可迁移到操控：让策略预测短时未来可观测状态，再由动作模块解码控制。复现时我会优先做 counterfactual visual intervention，而不是只看平均 ADE，因为它更能暴露模型是否真正 grounded。

#### 🔎 读 PDF 先核查

- next visual state 的监督目标具体预测什么表示，是图像 token、BEV 特征、视觉 embedding，还是其他中间状态？
- IK Network 在训练和推理中如何平衡当前视觉、未来视觉、ego status 与文本命令，是否有 ablation 证明捷径被抑制？
- GradCAM 和 counterfactual analyses 的设计是否能排除模型只对局部扰动敏感、但仍不理解场景因果关系的可能？

#### 📌 上传 PDF 后优先看

- 方法章节中的 inverse kinematics formulation 与 next visual state prediction objective。
- IK Network 架构、diffusion sampling 设置和输入模态消融。
- NAVSIM/nuScenes 主结果、GradCAM、counterfactual visual perturbation 和失败案例分析。

### [4]. PointACT: Vision-Language-Action Models with Multi-Scale Point-Action Interaction [[HTML]](https://arxiv.org/html/2605.21414) [[PDF]](https://arxiv.org/pdf/2605.21414) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.21414`
* **Authors**: Shizhe Chen, Paul Pacaud, Cordelia Schmid
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为 PointACT 直接把多尺度点云-动作交互放进 VLA 动作解码，而不是只把 3D 当附加感知特征。
* **关键词**: `3D-aware VLA` `point cloud` `action decoder` `multi-scale interaction` `robot manipulation`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

当前多数 VLA 依赖 2D 图像表示，继承了 VLM 的语义理解，却面对一个物理错配：机器人操作发生在 3D 空间，精细接触和位姿控制需要几何 grounding。仅靠多视角 RGB 或大规模数据学习 viewpoint invariance，容易在遮挡、尺度、相对位置和局部接触上失效。PointACT 关注的正是这个缺口：如何在保留预训练 VLM 语义能力的同时，让动作生成持续接收点云几何信息。它与 GaussianDream 同属 3D-aware VLA，但更偏策略架构和动作解码侧，而不是训练期 world model 监督。

#### ⚙️ 核心方法

PointACT 是 dual-system 3D-aware VLA policy。输入包括多视角 RGB、自然语言指令、机器人 proprioceptive state，以及 colored 3D point cloud；作者明确不假设点云与图像天然预对齐，但可通过标定相机位姿或多视角重建恢复。模型使用 Qwen2.5-VL 作为 VLM backbone，并引入基于 PTv3 配置的点云编码器；摘录中写到 PointACT module 包含约 300M trainable parameters，VLM backbone 默认冻结以保留已有知识。关键机制是 multi-scale point-action interaction：层级点云表示不是简单拼接到图像 token，而是在 action decoder 中持续条件化 action tokens，让动作预测能在多个几何尺度上访问空间信息。实现上还包括工作空间 bounding box 裁剪、1cm voxelization、最多 4096 点，以及点云和图像增强。当前摘录只能确认总体双系统设计和实现参数，具体交互 block、token routing 与 action head 形式需查 PDF。

#### 📊 实验与结果

实验摘录提供了较多实现信息：训练总 batch size 为 128，分布在 2 张 NVIDIA H100 GPU 上；优化 20K 到 50K gradient steps，使用 AdamW、cosine decay，并加入绕重力轴随机旋转等点云增强。评测 benchmark 名称在摘录中被截断，只能确认作者在多个实验 benchmark 上评估 PointACT。结论声称 multi-scale point-action interaction 能让几何信息持续条件化 action tokens，同时保留 VLM 语义能力。由于 HTML 摘录未给出任务列表和定量结果，当前不能判断它相对 2D VLA、monolithic 3D integration 或 dual-system baseline 的具体提升，但方法与实现可复现性线索较强。

#### ⚠️ 风险 / 保留意见

- 需要可靠点云输入、相机标定或重建流程，真实部署中的传感噪声可能显著影响动作解码。
- VLM 默认冻结有助于保留语义，但可能限制视觉-几何-动作之间的端到端适配。
- 摘录缺少主结果数值和 benchmark 细节，必须核查其优势是否来自 3D 交互而非更大动作模块容量。

#### 💭 结论与启发

PointACT 的启发是，3D 信息进入 VLA 的位置很关键：附加到视觉表示未必足够，动作 token 在解码过程中反复查询多尺度几何可能更贴近控制需求。后续如果做机器人操控系统，我会把它作为“冻结 VLM + 可训练 3D action expert”的参考架构。复现重点应放在点云预处理、交互模块和动作头，而不是盲目微调整个 VLM。

#### 🔎 读 PDF 先核查

- multi-scale point-action interaction 的具体计算方式是什么，action tokens 如何在不同点云层级间查询或融合特征？
- 与 monolithic 3D integration 和普通 dual-system modular baseline 相比，性能差异是否来自交互机制本身？
- 在点云缺失、噪声、错位或视角变化下，PointACT 的鲁棒性是否有系统评估？

#### 📌 上传 PDF 后优先看

- 模型章节中的 dual-system 设计、点云编码器和 point-action interaction block。
- 与 2D VLA、monolithic 3D 和 dual-system baseline 的对比实验。
- 点云预处理、VLM 冻结/解冻、点数/voxel size/增强策略的消融。

### [5]. MAPLE: Latent Multi-Agent Play for End-to-End Autonomous Driving [[HTML]](https://arxiv.org/html/2605.14201) [[PDF]](https://arxiv.org/pdf/2605.14201) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2605.14201`
* **Authors**: Rajeev Yasarla, Deepti Hegde, Hsin-Pai Cheng, Shizhong Han, Yunxiao Shi, Meysam Sadeghigooghari, Hanno Ackermann, Litian Liu, Pranav Desai, Fatih Porikli, Mohammad Ghavamzadeh, Hong Cai
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为 MAPLE 把 Driving VLA 的闭环训练推进到 latent multi-agent rollout，直接处理交互式交通场景。
* **关键词**: `Driving VLA` `latent rollout` `multi-agent planning` `reinforcement learning` `closed-loop driving`
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

#### 📖 背景与动机

端到端自动驾驶和 Driving VLA 近年来把感知、预测、规划统一到一个模型里，但训练多依赖 logged data 的开放环 imitation learning。这样的问题是模型只学会复现记录轨迹，却没有承受自己动作带来的状态分布变化，也没有真正建模周围车辆对 ego 行为的反应。传统闭环监督或仿真方法又面临可扩展性、环境反应真实性和成本问题。MAPLE 的目标是在不依赖完整外部模拟器的情况下，在 VLA latent space 中进行多智能体、反应式 rollout，让 ego 与邻近交通参与者共同演化，从而为闭环规划提供更丰富训练信号。

#### ⚙️ 核心方法

MAPLE 是一个 simulator-free multi-agent training framework。它把 ego vehicle 和周围 agents 表示成 compact latent tokens，编码速度、加速度、位置、地图标签和交通状态等信息；再结合高层 scenario description，在 VLA latent space 中自回归预测未来 tokens。与只回放邻车 ground-truth trajectory 的 planner 不同，MAPLE 让 ego 和 neighboring agents 独立受控，并在多步 horizon 中对彼此反应，从而产生交互式未来场景。动作规划头和运动预测头通过一系列 rewards 监督，鼓励安全和多样驾驶行为；结论摘录还提到 diversity-aware reinforcement learning，用于生成更丰富交互并提升数据稀缺设置下的鲁棒性。相对常规 VLA SFT，它的创新点是把闭环、multi-agent reactivity 和 RL-style reward 融入 latent rollout，而非直接在像素或物理模拟器中滚动。具体 reward 定义、token 动力学和 rollout 稳定性需要看 PDF。

#### 📊 实验与结果

实验主要基于 Bench2Drive 的官方闭环评估标准，指标包括 Driving Score、Success Rate、Efficiency、Comfort 和 Multi-Ability。Driving Score 综合路线完成与交通违规，Success Rate 统计无失败完成路线比例，Efficiency 和 Comfort 分别衡量速度与平顺性，Multi-Ability 覆盖五类复杂城市驾驶行为。结论声称 MAPLE 在 Bench2Drive 上达到 state-of-the-art closed-loop performance，并在 data-scarce settings 中提升鲁棒性。HTML 摘录没有提供具体分数、对比模型或消融结果，因此只能确认评估体系与作者主张。进入精选的原因是它把 VLA、closed-loop training、multi-agent world/action model 和 reinforcement learning 信号连成一条清晰路线。

#### ⚠️ 风险 / 保留意见

- latent rollout 可能无法完整表达真实交通参与者的复杂反应，错误会在多步自回归中累积。
- simulator-free 训练提高扩展性，但也可能缺少物理约束和传感反馈闭环。
- 摘录未给具体 SOTA 数值和 reward 消融，RL 信号是否稳定贡献仍需核查。

#### 💭 结论与启发

MAPLE 对选题的启发是：Driving VLA 的 world model 不一定要生成图像，latent agent token 的反应式演化也可以成为 action/world model。它尤其适合连接 VLA 与 RL，因为 rewards 可以约束安全、多样性和交互结果，而不只是拟合专家轨迹。后续阅读时，我会重点判断它的 latent rollout 是否真的替代了闭环仿真，还是只是在 Bench2Drive 上有效的训练增强。

#### 🔎 读 PDF 先核查

- MAPLE 的 latent tokens 如何从视觉和场景信息构建，是否保留足够的几何与交通语义细节？
- reactive agents 的策略是共享模型、独立头，还是通过同一自回归 token dynamics 产生？
- diversity-aware reinforcement learning 的 reward 项分别对应哪些驾驶行为，消融后哪些指标最敏感？

#### 📌 上传 PDF 后优先看

- latent multi-agent rollout 机制和 ego/agent token 表示。
- reward 设计、RL 训练流程和 data-scarce setting 实验。
- Bench2Drive 主结果、Multi-Ability 分项、闭环失败案例和消融表。

### [6]. VLANeXt: Recipes for Building Strong VLA Models [[HTML]](https://arxiv.org/html/2602.18532) [[PDF]](https://arxiv.org/pdf/2602.18532) [[ChatGPT]](https://chatgpt.com/)
* **Paper ID**: `2602.18532`
* **Authors**: Xiao-Ming Wu, Bin Fan, Kang Liao, Jian-Jian Jiang, Runze Yang, Yihang Luo, Zhonghua Wu, Wei-Shi Zheng, Chen Change Loy
* **Author Priority**: Standard
* **一句话结论**: 值得优先看，因为 VLANeXt 是一篇 VLA 设计空间校准论文，能帮助判断哪些 recipe 真正影响性能。
* **关键词**: `VLA recipes` `LIBERO` `policy coupling` `proprioception` `action temporal modeling`
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)

#### 📖 背景与动机

VLA 领域现在的问题不是缺少新架构，而是设计选择碎片化：不同论文使用不同训练协议、数据处理、动作建模、proprioception 融合和评测设置，很难判断提升来自模型思想还是工程 recipe。VLANeXt 的动机是把这些因素放进统一框架重新审视，从一个类似 RT-2 的简单 VLA baseline 出发，系统比较关键设计。对后续阅读很重要，因为 GaussianDream、PointACT、DISC 等论文都在改 VLA 某个模块；如果没有统一 recipe 参照，容易把基础训练技巧造成的增益误判为结构创新。

#### ⚙️ 核心方法

VLANeXt 不主打单一新模块，而是总结构建强 VLA 的 recipes。摘录明确指出，关键设计包括 VLM 如何与 policy module 交互，proprioception 等多模态信号如何融合，以及 action temporal structure 如何建模。结论中特别提到 soft VLM-policy coupling 和 VLM-side proprioception conditioning 这类 modest architectural refinements 可以显著影响表现，说明“信息在哪里注入”与“用什么 backbone”同等重要。实验从一个统一 VLA baseline 开始，在一致训练和评测设置下重审设计空间，从而试图区分真实有效的建模选择与不一致协议带来的噪声。当前摘录只能确认这些 recipe 类别和总体结论，不能还原每个 recipe 的具体实现、动作离散化/连续化方案、训练数据混合策略或超参。完整 PDF 中的方法表和消融表会是核心价值。

#### 📊 实验与结果

摘录显示作者在 LIBERO benchmark 上做系统比较，baseline 分为 direct policy learning 和 VLA 两类。direct policy learning 包括 Diffusion Policy、Octo、MDT；VLA 对比包括 OpenVLA、TraceVLA、SpatialVLA、WorldVLA、CoT-VLA、pi0、pi0-Fast、NORA、SmolVLA、UniVLA、FLOWER、OpenVLA-OFT 等。作者声称按其 recipes 可构建 state-of-the-art VLA，并证明设计选择有效。HTML 摘录没有提供 Table 2 的具体数值，因此不能引用提升幅度。尽管如此，这篇的价值在于对比面广、目标是统一协议下的 design-space analysis，可作为判断新 VLA 方法是否公平比较的重要基线。

#### ⚠️ 风险 / 保留意见

- recipes 可能高度依赖 LIBERO 设置，迁移到真实机器人或自动驾驶 VLA 未必同样成立。
- 系统论文容易把工程调参和结构贡献混在一起，需要仔细看每项消融是否隔离变量。
- 摘录缺少完整定量结果，当前不能判断 SOTA 是全面提升还是集中在少数任务组。

#### 💭 结论与启发

VLANeXt 应作为今天所有 VLA 方法的背景校准器。读完它可以建立一个 checklist：VLM-policy coupling、proprioception 注入位置、动作时序建模、训练协议和评测公平性。对复现来说，我会先复现其强 baseline 或 recipe 子集，再叠加 3D/world-model 方法，否则很难判断新模块是否真的带来增益。它也提醒后续写作要少宣称“架构突破”，多证明变量控制。

#### 🔎 读 PDF 先核查

- soft VLM-policy coupling 的具体形式是什么，它相比硬连接或完全端到端微调改善了哪些任务组？
- VLM-side proprioception conditioning 为什么有效，是否会影响语言/视觉语义能力或引入状态捷径？
- action temporal structure 的最佳 recipe 是预测 action chunk、diffusion、autoregressive token，还是其他形式？

#### 📌 上传 PDF 后优先看

- 统一框架和 baseline 定义，尤其是 VLM-policy 接口与 proprioception 融合位置。
- LIBERO Table 2 主结果，以及各 recipe 的逐项消融。
- 训练协议、数据处理、动作表示和与 OpenVLA-OFT 等强 baseline 的公平性说明。

## Watchlist

### [W1]. Proximal State Nudging: Reducing Skill Atrophy from AI Assistance [[VIP]] [[PDF]](https://arxiv.org/pdf/2605.20355)
* **Paper ID**: `2605.20355`
* **Authors**: Megha Srivastava, Jonathan Ouyang, Eric Zhou, Andrew Silva, Emily Sumner, Dorsa Sadigh, Yuchen Cui, Deepak Gopinath, Guy Rosman
* **Author Priority**: Core VIP
* **为什么还值得留意**: PSN 进入 watchlist 的主要原因是 Dorsa Sadigh 在作者列表中，且主题触及共享自主中的 skill atrophy 与人机安全。它提出 Proximal State Nudging，在 LunarLander 模拟学生和 CARLA 两个驾驶任务的人类实验中评估学习兼容的 shared autonomy；摘要明确给出 human study 为 n=60。没有进入最终精选，是因为它更偏 human-AI assistance/shared control，而不是今天主线里的 VLA、world model 或机器人策略架构。
* **证据来源**: Abstract fallback

### [W2]. DISC: Decoupling Instruction from State-Conditioned Control via Policy Generation [[HTML]](https://arxiv.org/html/2605.20856) [[PDF]](https://arxiv.org/pdf/2605.20856)
* **Paper ID**: `2605.20856`
* **Authors**: Hanxiang Ren, Pei Zhou, Xunzhe Zhou, Yanchao Yang
* **Author Priority**: Standard
* **为什么还值得留意**: DISC 值得跟踪，因为它把语言条件操控中的 observation leakage 表述为结构性 task-state entanglement，并用 hypernetwork 从指令生成完整任务特定 visuomotor policy 参数。这个想法对 VLA grounding 很有启发，尤其适合检查模型是否真的使用语言而不是场景捷径。未进最终精选，是因为它与今天选定的 3D/world-model/真实评测/驾驶闭环主线相比，证据和影响面需要等完整结果进一步确认。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W3]. Lost in Fog: Sensor Perturbations Expose Reasoning Fragility in Driving VLAs [[HTML]](https://arxiv.org/html/2605.21446) [[PDF]](https://arxiv.org/pdf/2605.21446)
* **Paper ID**: `2605.21446`
* **Authors**: Abhinaw Priyadershi, Jelena Frtunikj
* **Author Priority**: Standard
* **为什么还值得留意**: Lost in Fog 进入 watchlist 是因为它对 Driving VLA 做了直接的 sensor perturbation robustness 压测：Alpamayo R1、1,996 个场景、8 类扰动，并把 explanation consistency 与 trajectory reliability 联系起来。摘录中给出重噪声下均值 ADE 从 2.00 m 到 2.30 m 的 15% 变化，以及 70.6% 样本超过 5 m L2 deviation 的尾部风险，这对安全评估很有价值。未进最终精选，是因为它主要是鲁棒性诊断研究，而非提出新的 VLA/world action model 训练框架。
* **证据来源**: arXiv HTML (Introduction, Method, Experiments, Conclusion)

### [W4]. Hand-in-the-Loop: Improving VLA Policies for Dexterous Manipulation via Seamless Hand-Arm Intervention [[HTML]](https://arxiv.org/html/2605.15157) [[PDF]](https://arxiv.org/pdf/2605.15157)
* **Paper ID**: `2605.15157`
* **Authors**: Zhuohang Li, Liqun Huang, Wei Xu, Zhengming Zhu, Nie Lin, Xiao Ma, Xinjun Sheng, Ruoshi Wen
* **Author Priority**: Standard
* **为什么还值得留意**: HandITL 值得保留，因为它面向高 DoF 灵巧手 VLA 的真实部署痛点：人类介入时 teleoperation 命令与策略执行状态不匹配，会造成 gesture jumps。它提出 optimization-based relative hand retargeting 与 velocity-based shared arm control，并声称真实实验中 command discontinuity 最多降低两个数量级。未进最终精选，是因为它更偏交互式模仿学习和硬件介入接口，虽然实用，但与今天最终主线的 VLA 表征、world model 和标准评测相比覆盖面稍窄。
* **证据来源**: arXiv HTML (Introduction, Experiments, Conclusion)
