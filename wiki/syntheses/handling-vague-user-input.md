---
title: "应对用户输入模糊/歧义的技术"
type: synthesis
tags: [intent-disambiguation, clarification, multimodal, neuro-symbolic, vague-input]
sources: [ask-before-plan, intentrl, speakrl, pp-clarifier, cocot, debate, noemmma, good-agent-alignment, ds-ia-framework, intent-signal-theory, cicc, gid, continual-gid, droid, deep-unknown-intent, open-intent-discovery, sage-agent, active-task-disambiguation, clara, neural-evpi, clarify-when-necessary, uncertainty-decomposition-clarification]
last_updated: 2026-06-25
---

# 应对用户输入模糊/歧义的技术

**查询问题**：当前知识库中，有没有应对用户输入非常模糊的技术？

本综合跨 [[AskBeforePlan]]、[[IntentRL]]、[[SpeakRL]]、[[PP-Clarifier]]、[[CoCoT]]、[[DEBATE]]、[[noemmma]]、[[good-agent-alignment]]、[[ds-ia-framework]]、[[intent-signal-theory]]、[[CICC]]、[[SAGE-Agent]]、[[CLARA]]、[[active-task-disambiguation]]、[[neural-evpi]]、[[clarify-when-necessary]]、[[uncertainty-decomposition-clarification]]、[[IntentSimUncertainty]]、[[PromptBasedUncertaintyDecomposition]] 等来源，归纳出五条技术线 + 一条理论支撑 + 一条谱系。

## 模糊输入的三层层级（关键框架）

"模糊输入"并非单一概念，不同方法覆盖不同层级。选型前必须先判断模糊发生在哪一层：

| 层级                   | 描述             | 例子                               | 谁覆盖                                                                                                                                       | 谁不覆盖                                  |
| -------------------- | -------------- | -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| **L1 意图本身未知**        | 连"用户想做什么"都识别不出 | "我有点烦"（订票？诉苦？推荐音乐？）              | [[CICC]]（共形预测+澄清，有保证）、[[GID]]（开放世界发现新意图）、[[DROID]]（OOS检测）、[[deep-unknown-intent]]（经典OOS检测）、[[open-intent-discovery]]（从零发现意图）、[[good-agent-alignment]]（开放目标推断） | NOEM³A（需候选集非空）、Ask-before-Plan（需意图已知） |
| **L2 意图已知但多个候选/歧义**  | 意图域可枚举但具体指向不明  | "book"（BookFlight 还是 BookHotel？） | [[noemmma]]（静默选）、[[CICC]]（交互问有保证）、[[SAGE-Agent]]（EVPI 选问题）、[[CLARA]]（多轮视觉+turn-valid 保证）、[[PP-Clarifier]]（多模态消歧）、[[clarify-when-necessary]]（intent-sim 熵判断）、[[uncertainty-decomposition-clarification]]（u_t/c_t 分解）                  | Ask-before-Plan（假设意图单一确定）             |
| **L3 意图确定但参数缺失/不可行** | 意图明确但属性/约束不全   | "订机票"（从哪？到哪？哪天？预算？）              | [[AskBeforePlan]]（核心场景）、[[ds-ia-framework]]（状态检查）、[[SAGE-Agent]]（EVPI 结构化参数域）、[[neural-evpi]]（EVPI 鼻祖）、[[uncertainty-decomposition-clarification]]（u_t 触发澄清）                                                                                         | [[noemmma]]（不处理参数）                     |

**关键边界**：
- [[AskBeforePlan]] **不处理 L1 和 L2**——它假设意图已知（旅行规划），只处理意图的参数缺失（missing）或不可行（unfeasible）。澄清判据 prompt 原文："needs clarification if the user's intention contains missing or unfeasible details"。
- [[noemmma]] **不处理 L1**——需候选集非空（top-k ∩ θ=0.65），若所有意图节点 sim<0.65 则未定义回退。
- **L1 现有多条技术路线**（详见第 5 节）：OOS 检测（[[DROID]]/[[deep-unknown-intent]]）、意图发现（[[GID]]/[[open-intent-discovery]]）、共形澄清（[[CICC]]）、开放目标推断（[[good-agent-alignment]]）。
- **L1 在 [[intent-signal-theory]] 中被证明为"不可逆意图丢失"**——I* 在 P 中缺失且不可恢复，但 CICC 的覆盖率保证（1-α）和 GID 的群体意图发现可部分缓解。

## 1. 澄清先行（Clarification-first）

核心原则：**行动前先澄清**，而非在模糊指令上盲目自主执行。覆盖 **L3**（意图已知但参数模糊）。

- [[AskBeforePlan]] — CEP 多智能体框架：Clarification Agent 识别模糊点 → Execution Agent 收集信息 → Planning Agent 生成计划。模糊分两类：**missing details**（出发地/人数/日期/预算等缺失）和 **unfeasible details**（预算低于最低可行/偏好无匹配等不可行）。用**拓扑排序**按依赖顺序安排澄清，迭代直到所有 indefinite details 被 recovered。核心创新：澄清判据基于**对话 + 环境观察**二值判断（`b_t`），环境观察是检测 unfeasible 的唯一途径。**关键边界**：不处理 L1/L2，假设意图已知（旅行规划域），只处理 L3 参数模糊。
- [[IntentRL]] — 针对"对模糊查询高自主性 → 冗长执行 + 不满意结果"的自主性-交互困境，用 shallow-to-deep intent refinement graph + 两阶段 RL（offline dialogues + online simulator），在长程研究前主动澄清潜在意图，超越闭源 DR agents 的内置 clarify modules。
- [[SpeakRL]] — RL 奖励"问对的澄清问题"而非只奖励执行结果，推理 → 说话 → 行动三者协同，任务完成率绝对 +20.14%。构建 SpeakER 合成数据集覆盖澄清策略。

## 2. 多模态意图消歧

当文本不充分时，引入视觉/语音/手势等模态消解歧义，见 [[MultimodalIntentDisambiguation]]。

- [[PP-Clarifier]] — 三模块零样本框架（文本澄清器 / 视觉澄清器 / 跨模态澄清器），让 4-8B 小模型意图澄清 +30%。明确指出单体 VLM 面对多模态歧义输入会"静默失败或产生幻觉"。
- [[CoCoT]] — 认知三阶段推理（感知 → 情境 → 规范），通过 SFT 内化认知结构，多任务 +5-6%。
- [[DEBATE]] — 首个中文语音-文本消歧数据集，通过语音线索（声调、韵律）消解文本歧义。

## 3. 神经符号本体注入

用结构化意图 Ontology 给小模型"补结构"，应对多意图歧义。

- [[noemmma]] / [[NeuroSymbolicOntology]] — Retrieval-Augmented Prompting + Logit Biasing + 可选分类头三层注入策略，将意图 Ontology 嵌入 3B Llama 的输入与输出表示，在 MultiWOZ 2.3 歧义子集上达 GPT-4 的 85%（vs 90%）。并提出基于层次 Ontology 深度的 Semantic Intent Similarity (SIS) 评测指标，捕捉词表匹配遗漏的语义邻近度。**关键边界**：NOEM³A 是纯单轮静默消歧，不找用户澄清——假定 ontology + LLM 足以单轮消歧，真遇到结构性无法消解的歧义时"猜"一个而非"问"一个。它只解决**可由结构消解的歧义**，对**需要用户才能消解的歧义**无能为力，这是它与第 1 类"澄清先行"路线的根本区别。

## 3b. 共形预测意图澄清（L2 交互式，有统计保证）

填补 NOEM³A（L2 静默猜，无保证）和 Ask-before-Plan（L3 参数澄清，不选意图）之间的空白——**多候选歧义时，不猜而问，且问得有保证**。

- [[CICC]] / [[ConformalIntentClarification]] — 用 Conformal Prediction 把任意意图分类器的不确定度转为有统计保证的预测集 `C(X)`，保证 `P(真意图 ∈ C) ≥ 1-α`。三分支决策：|C|=1 直接执行 / 1<|C|≤th 生成澄清问题 / |C|>th 拒绝（太模糊或 OOS）。**分类器无关，无需重训**，仅需校准集。两个超参数 α（错误率，控制置信 vs 集大小）和 th（阈值，建议 ≤7，Miller 认知科学）均有直觉解释。7 个数据集上 CICC 生成最小澄清问题且满足覆盖保证。CICC-OOS 变体 F1=0.90。**独特价值**：唯一在 L2 层提供统计保证的交互式澄清方法。**关键局限**：覆盖率保证仅在**第一轮**成立——多轮交互后自适应选择导致反馈协变量偏移（见 [[CLARA]]）。

## 3c. 有原则澄清三剑客（L2/L3 交互式，信息论判据）

CICC 用共形预测给覆盖率保证，但"问什么问题"由预测集大小隐式决定。以下三篇论文各自用不同的信息论/统计学原则**显式**选择最优澄清问题，构成"有原则澄清"谱系：

### 三剑客对比

| 维度 | [[CICC]]（共形预测） | [[SAGE-Agent]]（EVPI） | [[active-task-disambiguation]]（贝叶斯实验设计） |
|---|---|---|---|
| **理论框架** | 共形预测 | 期望完美信息价值（贝叶斯决策论） | 贝叶斯实验设计 |
| **不确定度空间** | 意图分类 softmax | 工具参数域 | 解空间 |
| **问题选择** | 预测集大小（隐式） | EVPI - 冗余成本（显式） | 最大化信息增益（显式） |
| **停止判据** | 预测集收敛 | 净增益 < α·max π | 信息增益低于阈值 |
| **统计保证** | 覆盖率 1-α（单轮） | 无（期望值） | 无（信息增益） |
| **多轮** | 单轮 | 是 | 是 |
| **领域** | 意图分类 | 工具调用 | 通用任务 |
| **分离规格/模型不确定度** | 否 | **是** | 否 |
| **训练信号** | 否 | **是**（GRPO 奖励） | 否 |

- [[SAGE-Agent]] / [[StructuredUncertaintyClarification]] — 在**工具参数域**上直接建模信念状态，用 EVPI（`E_r[max_c π_c(t|q,r)] - max_c π_c(t)`）量化每个问题的消歧价值，配合 aspect-based 冗余成本（`λ·Σ n_a(t)`）防止重复提问。干净分离**规格不确定度**（用户想要什么）与**模型不确定度**（LLM 预测什么）。ClarifyBench 基准（716 样本/5 域/92 工具）上覆盖率 +7-39%，问题数减少 1.5-2.7x。还可作为训练信号：uncertainty-weighted GRPO 将 When2Call 准确率从 36.5% 提升到 65.2%。
- [[active-task-disambiguation]] / [[BayesianDisambiguation]] — 将任务消歧形式化为**贝叶斯实验设计**：每个澄清问题是一个"实验"，选择最大化**信息增益**的问题。关键发现：有效问题生成需要**元认知推理**——显式推理可行解空间而非仅在问题空间内推理。信息增益导向 > 问题空间内推理。
- [[CLARA]] / [[TurnValidConformalCoverage]] — 将 CICC 的共形预测扩展到**多轮交互**。揭示关键理论问题：CICC 的覆盖率保证在自适应交互后失效（**反馈协变量偏移**）。用选择诱导的**似然比重加权**恢复每一轮的覆盖率保证（turn-valid coverage: `Pr(I_T ∈ C) ≥ 1-α` 在每一轮成立）。同时用**生成式视觉消歧**（展示原型图面板让用户选）代替文本提问，消除答案模型循环。

## 3d. 澄清问题选择的谱系（EVPI / intent-sim / 共形 / prompt 分解）

上述方法并非孤立出现，而是沿着两条谱系演进。理解谱系有助于选型时判断"需要哪个世代的方法"。

### 谱系 A：EVPI 驱动（信息论问题选择）

```
Neural EVPI (2018) — EVPI 排序澄清问题的概念起源
  │  StackExchange ~77K 帖子；神经网络隐式近似 EVPI
  ↓
SAGE-Agent (2025) — 在工具参数域上显式 EVPI + 冗余成本 + 停止判据
     结构化信念状态；分离规格/模型不确定度；GRPO 训练信号
```

- [[neural-evpi]] / [[SAGE-Agent]] — EVPI 的核心思想："好问题 = 其答案的期望信息价值高"。Neural EVPI 用神经网络从数据中学习这个价值函数；SAGE-Agent 在结构化参数域上显式计算 `EVPI = E_r[max_c π_c(t|q,r)] - max_c π_c(t)`，并加入冗余成本防止重复提问。

### 谱系 B：不确定性估计驱动（何时澄清）

```
Clarify When Necessary (2023) — intent-sim 估计意图熵判断何时澄清
  │  三子任务框架 (when/what/how)；10% 预算翻倍；任务无关
  ↓
CICC (2024) — 用共形预测替代 intent-sim，提供统计保证
  │  覆盖率 1-α；分类器无关；三分支决策
  ↓
CLARA (2026) — 多轮扩展 + turn-valid coverage
  │  似然比重加权修正反馈协变量偏移；视觉消歧
  ↓
Uncertainty Decomposition (2026) — prompt-based 分离 u_t / c_t
     纯 prompt 无需训练；黑箱 API 兼容；F1 +73%
```

- [[clarify-when-necessary]] → [[CICC]]：intent-sim 只能排序哪些样例需要澄清（无保证），CICC 的共形预测能保证真意图在候选集内（覆盖率 1-α）。
- [[CICC]] → [[CLARA]]：CICC 的覆盖率保证仅在第一轮成立，多轮交互后反馈协变量偏移导致漂移最多 10pp；CLARA 用似然比重加权恢复每轮保证。
- [[clarify-when-necessary]] → [[uncertainty-decomposition-clarification]]：intent-sim 需要意图聚类后估计熵，UncertaintyDecomposition 直接让 LLM 自报告 `u_t`（请求不确定度），更简单但依赖 LLM 自评质量（受过度自信影响）。

### 谱系交叉

| 维度 | 谱系 A（EVPI） | 谱系 B（不确定性估计） |
|---|---|---|
| **核心问题** | 问什么问题？ | 何时问？ |
| **理论工具** | 期望完美信息价值 | 意图熵 / 共形预测 / prompt 分解 |
| **代表** | [[neural-evpi]] → [[SAGE-Agent]] | [[clarify-when-necessary]] → [[CICC]] → [[CLARA]] / [[uncertainty-decomposition-clarification]] |
| **统计保证** | 无（期望值） | CICC/CLARA 有覆盖率保证 |
| **分离规格/模型不确定度** | SAGE-Agent 有 | UncertaintyDecomposition 有 |
| **需要训练** | SAGE-Agent 可选 GRPO | 均无需训练（除 SAGE-Agent） |
| **黑箱 API 兼容** | SAGE-Agent 推理时兼容 | 全部兼容 |

**选型启示**：如果核心需求是"问什么问题最有价值"→ 谱系 A（EVPI）；如果是"该不该问"→ 谱系 B（不确定性估计）。实践中两者互补——先判断是否需要澄清（谱系 B），再选择最优问题（谱系 A）。[[SAGE-Agent]] 是唯一同时覆盖两者的方法（EVPI 既决定"问什么"也隐含"何时停"）。

## 4. 开放对话目标推断 + 双阶段语义防火墙

- [[good-agent-alignment]] / [[AssistanceGames]] — Open-Universe Assistance Games (OU-AGs) 框架，把偏好视为"动态构建"而非固定预设，用 LLM 模拟用户对候选目标做概率推断。适合目标在开放对话中逐步修正、自然语言表达的场景，无需大规模离线偏好数据集。
- [[ds-ia-framework]] — Stage 1 语义防火墙：通过家居状态检查解决模糊命令 + 过滤无效指令；Stage 2 确定性级联验证器（房间 → 设备 → 能力）。解决"交互频率困境"，自主成功率从 42.86% 提升到 71.43%，无效指令拒绝率 87.04%。

## 5. L1 开放世界意图发现与 OOS 检测

当意图完全不在已知意图集中（L1），有四条递进的技术路线，见 [[OpenWorldIntentDiscovery]] 和 [[OutOfScopeDetection]]：

### 5a. OOS 检测——识别"不属于已知"

只判断输入是否不属于任何已知意图，不发现新意图也不澄清：

- [[DROID]] — 双表示端到端框架：监督分类器 + 对比原型网络，单一校准阈值区分已知/OOS，无需后处理打分。已知意图 +3-8%、OOS +8-20%。
- [[deep-unknown-intent]] — 经典两阶段：BiLSTM + margin loss 特征提取 → LOF 密度新颖性检测。ACL 2019，162 引用。

### 5b. 意图发现——从未知中发现新类别

不仅检测 OOS，进一步将未知查询聚类为新意图类别并扩展分类器：

- [[GID]] — Generalized Intent Discovery 开山作：同时分类 IND 意图 + 发现 OOD 新意图。两种框架（pipeline / joint）。EMNLP 2022。
- [[continual-gid]] — 持续版：多阶段增量发现新意图，解决灾难性遗忘。ACL 2023。
- [[open-intent-discovery]] — 从零发现：无监督依存解析 + 语义聚类，不假设任何预定义意图。EMNLP 2021。

### 5c. 共形澄清——有保证地缩小范围

- [[CICC]] — 详见第 3b 节。预测集为空 = OOS 检测，预测集多候选 = 澄清问题，有覆盖率保证。

### 5d. 开放目标推断——不预设意图集

- [[good-agent-alignment]] — 详见第 4 节。在开放对话中动态推断目标，候选目标不预设。

### L1 技术路线对比

| 路线 | 输出 | 后续动作 | 代表 | 与 I* 的关系 |
|---|---|---|---|---|
| OOS 检测 | 二元（已知/未知） | 拒绝/转人工 | [[DROID]]、[[deep-unknown-intent]] | 识别 I* 缺失 |
| 意图发现 | 新意图类别 | 扩展分类器 | [[GID]]、[[open-intent-discovery]] | 从群体行为推断潜在 I* |
| 共形澄清 | 澄清问题 | 用户选择 | [[CICC]] | 有保证地恢复 I* |
| 开放目标推断 | 候选目标 | 概率推断 | [[good-agent-alignment]] | 动态逼近 I* |

## 理论支撑

[[intent-signal-theory]]（IST）的**不可逆意图丢失定理（Irreversible Intent Loss）** 形式化了模糊输入的本质：用户潜在源意图 I* 常在可观测载体 P 中缺失，且该缺失不可恢复。这解释了为何上述四类策略都试图从不同模态和交互中补偿信息缺口——

| 技术线 | 补偿路径 |
|---|---|
| 澄清先行 | 通过多轮交互重新获取 I* |
| 多模态消歧 | 从非文本模态恢复 I* |
| 神经符号注入 | 用 Ontology 结构约束 P 的解码空间 |
| 目标推断/防火墙 | 用环境状态 + 概率推断逼近 I* |
| OOS 检测 | 识别 I* 缺失（不恢复，只标记） |
| 意图发现 | 从群体行为推断潜在 I*，扩展意图集 |
| 共形澄清 | 有保证地恢复 I*（覆盖率 1-α） |
| EVPI 结构化澄清 | 在参数域上量化消歧价值，EVPI 驱动问题选择 |
| 贝叶斯消歧 | 最大化信息增益缩小解空间，元认知推理 |
| 多轮共形澄清 | 似然比重加权恢复每轮覆盖率，turn-valid 保证 |
| intent-sim 熵估计 | 在意图空间估计不确定性分布熵，判断何时澄清 |
| prompt 不确定度分解 | 分离行动置信度与请求不确定度，黑箱 API 可用 |

## 选型建议（按模糊层级）

**L1 意图本身未知**：
- 只需识别"不属于已知"（OOS 检测）→ [[DROID]]（最新 SOTA，双表示+单一阈值）或 [[deep-unknown-intent]]（经典基线）
- 需从未知中发现新意图类别 → [[GID]]（已有 IND 基础上发现 OOD）或 [[open-intent-discovery]]（从零发现）
- 需有保证地缩小意图范围 → [[CICC]]（共形预测，保证真意图在候选集内，生成澄清问题）
- 开放对话中目标动态漂移 → [[good-agent-alignment]]（开放目标推断）
- 持续涌现新意图 → [[continual-gid]]（多阶段增量发现）

**L2 意图已知但多候选/歧义**：
- 可由结构消解 → [[noemmma]]（单轮静默消歧，不反问用户；真歧义/零候选时会"猜"而非"问"）
- **需统计保证的交互式澄清** → [[CICC]]（共形预测保证真意图在候选集内，三分支决策；唯一在 L2 提供单轮统计保证的交互方法）
- **需多轮交互且保证每轮有效** → [[CLARA]]（turn-valid coverage，似然比重加权修正反馈协变量偏移；视觉消歧比文本更高效）
- **工具调用场景需显式问什么/何时停** → [[SAGE-Agent]]（EVPI 量化每个问题价值，结构化参数域建模，分离规格/模型不确定度）
- **通用任务需最大化信息增益** → [[active-task-disambiguation]]（贝叶斯实验设计，元认知推理显式推理解空间）
- **有限澄清预算下选对"问哪些"** → [[clarify-when-necessary]]（intent-sim 意图熵排序，10% 预算翻倍；CICC 的精神前身，无统计保证）
- **黑箱 API + 无训练 + 需分离"行动难"vs"请求模糊"** → [[uncertainty-decomposition-clarification]]（prompt-based u_t/c_t 分解，F1 +73%；但伴随能力稀释 -1.6pp 成功率）
- 需多模态信息消解 → [[PP-Clarifier]] 最直接
- 需用户裁决 → [[AskBeforePlan]] / [[IntentRL]]（交互式澄清）

**L3 意图确定但参数缺失/不可行**：
- 参数缺失（missing）或不可行（unfeasible）→ [[AskBeforePlan]]（拓扑排序有序澄清，环境观察检测不可行）
- 工具调用参数模糊需有原则选择 → [[SAGE-Agent]]（EVPI 在参数域上量化消歧价值，冗余成本防止重复问）
- **EVPI 问题排序的概念起源** → [[neural-evpi]]（StackExchange 数据集，神经网络近似 EVPI；SAGE-Agent 的直接前身）
- **黑箱 API + 需判断规格是否完整** → [[uncertainty-decomposition-clarification]]（u_t ≥ θ 触发澄清，纯 prompt 无训练）
- 物理环境指令歧义 → [[ds-ia-framework]]（状态检查 + 级联验证）

## 关联
- [[IntentUnderstanding]] — 意图理解是消歧的上游概念
- [[MultimodalIntentDisambiguation]] — 多模态消歧的概念聚合页
- [[IntentRecommendation]] — 澄清先行可视为意图推荐的特例（推荐"澄清"这个动作）
