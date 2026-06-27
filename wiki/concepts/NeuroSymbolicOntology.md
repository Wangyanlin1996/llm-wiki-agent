---
title: "NeuroSymbolicOntology"
type: concept
tags: [neuro-symbolic, ontology, intent-understanding, NLU]
sources: [noemmma]
last_updated: 2026-06-22
---

# NeuroSymbolicOntology

神经符号本体注入框架（Neuro-Symbolic Ontology-Enhanced Method），将结构化意图 Ontology 的符号知识嵌入神经语言模型的输入与输出表示中，实现小型 LLM 的高效多意图理解。

## 核心机制

三层注入策略：
- **Retrieval-Augmented Prompting** — 在输入端通过检索增强注入 Ontology 结构信息
- **Logit Biasing** — 在输出端通过 logits 偏置引导模型朝 Ontology 对齐的意图空间生成
- **可选分类头** — 在模型顶部添加基于 Ontology 结构的分类层

## 本体结构

`O = (V, E, F)`：V 为意图节点（如 BookHotel），F 为类型化边（is-a、related-to）。**三级层次树**：domains → categories → intent leaves。每个节点附带文本标签、规范描述、预计算嵌入（与下游 LLM 同编码器对齐）。由 **GPT-4 半自动生成**（给领域示例 + 指令模板产 JSON 树），区别于 FolkScope 等人工策划本体。

## 查询编码与多意图处理

查询用用户原始输入**整句编码**，不拆分。多意图靠 **token-level 对齐**隐式分解：不同 token 自然命中不同意图节点（如 "Order pizza and track my last order" 中 `Order`+`pizza` 命中 Restaurant Order，`order`+`track` 命中 Order Tracking），多意图在检索阶段即被隐式分解。

## 候选选择（双重筛选 + 可选扩展）

向量匹配后经**双重判据**：Top-k 截取（默认 k=5）∩ 相似度阈值（cutoff θ=0.65，正确对齐落 [0.70,0.95]、无关对 <0.30）。可选邻域扩展补父/兄弟节点保持连通性。**非分层检索**。**扩展节点不区分对待**——扩展进来的兄弟与原始 top-k 候选享受同等 +δ bias，未提降权（隐患：兄弟节点非目标却获同等加成）。

## Logit Biasing 原理

**推理时干预，不改模型参数**。softmax 之前对候选 token logit 加 +δ、其他加 -γ（默认 δ=0.3, γ=0.2）。数学等价：softmax 后候选概率 ×e^δ≈1.35、非候选 ×e^(-γ)≈0.82，双向夹击。目标：steer generation towards ontology-aligned outputs，防 semantic drift。**与 logprobs 区别**：logprobs 是 softmax 后对数概率的只读输出，Logit Biasing 是 softmax 前对 logits 的读写干预；对应 OpenAI API 的 `logit_bias`（非 `logprobs`）。已知限制：Tokenization Mismatch（长标签分片降低效果）。

## 最终意图选择（两路并集融合）

最终输出 `Y` 为意图节点集合（multi-label）。两路独立产出**取并集**（非二选一）：
- **生成路径 Y_gen**（必有）：LLM 在 biased logits 上解码出意图标签 token
- **分类路径 Y_aux**（optional）：分类头 `s=W·h_q` 在 |V| 节点上 sigmoid，超阈值 τ 的纳入
- `Y = Y_gen ∪ Y_aux`（集合去重）。互补设计：生成受 prompt 引导，分类有显式监督。**论文未讨论冲突裁决**，仅取并集，可能引入误报。

## 约束范围（仅意图层，不含槽位）

任务为 joint goal prediction（意图集 + slot-value 对，等价 joint DST），但**本体约束仅作用于意图节点 V**：四阶段 pipeline 均不对槽位做约束。槽位来自 MultiWOZ 数据集标注，Slot-F1 提升是意图约束的间接溢出。论文 §5 将"含 argument slots 的 action graph"列为 future work，当前本体无槽位 schema。

## 单轮静默消歧——不找用户澄清（关键边界）

**纯单轮 pipeline，不做澄清。** 全文零交互/澄清关键词命中。即使候选 n 个、相似度都高、真值不明，系统也强制选一个/几个输出，不回退问用户。唯一门槛是硬阈值 θ=0.65（过滤，非澄清）；若所有节点低于 0.65，论文未定义回退（可能输出空集或 LLM 幻觉）。设计动机：on-device/real-time/privacy-preserving 边缘部署排斥多轮交互；§5 future work 列了多模态/GUI 辅助消歧，但**未列 clarification dialog**。

**核心结论**：
> NOEM³A 假定 ontology + LLM 足以单轮消歧，不找用户澄清；真遇到结构性无法消解的歧义，它会"猜"一个而非"问"一个。

**失败场景**（论文未承认）：(1) 真歧义——两候选 sim 都 >0.85 且都合理，硬选一个；(2) 零候选——所有节点 sim<0.65，未定义回退。

**理论联系**：[[IntentSignalTheory]] 的"不可逆意图丢失"典型场景——I* 在 P 中缺失，ontology 结构补偿不了且无交互回路时无法恢复。这正是 [[handling-vague-user-input]] 把 NOEM³A 归在"神经符号注入"而非"澄清先行"路线的原因：它解决**可由结构消解的歧义**，对**需要用户才能消解的歧义**无能为力。

**与澄清方法的对比**：

| 维度 | NOEM³A（神经符号消歧） | [[AskBeforePlan]]/[[IntentRL]]/[[SpeakRL]]（澄清先行） |
|---|---|---|
| 处理模糊的方式 | 静默选最似意图 | 主动反问用户 |
| 交互轮数 | 1（单轮） | ≥2（先问后做） |
| 信息来源 | ontology 结构 + LLM 内部知识 | 用户二次输入 |
| 模糊输入代价 | 可能选错（silent failure） | 多一轮交互成本 |
| 论文定位 | on-device 实时 NLU | 长程研究/规划前对齐 |

## 评测指标

[[SemanticIntentSimilarity]] (SIS) — 基于层次 Ontology 深度的评测指标，捕捉语义邻近度而非词表匹配。

## 关键结果

3B Llama + Ontology 增强在 MultiWOZ 2.3 歧义对话子集上达到 GPT-4 的 85%（vs 90%），能耗与内存仅为极小比例。

## 关联
- [[IntentUnderstanding]] — 神符号本体是意图理解的符号增强方法
- [[IntentSignalTheory]] — I*→P 信息损失可通过符号结构部分补偿
- [[IntentGrasp]] — IFT fine-tuning 与 Ontology 注入的对比策略