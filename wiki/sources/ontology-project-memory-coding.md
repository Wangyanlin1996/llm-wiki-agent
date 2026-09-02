---
title: "MOOSEDev: 编码 Agent 的本体接地项目记忆（Ontology-Grounded Project Memory for Coding Agents）"
type: source
tags: [ontology-graph-retrieval]
sources: [ontology-project-memory-coding]
source_file: raw/papers/ontology-project-memory-coding.pdf
last_updated: 2026-08-31
arxiv_id: "2608.13662"
authors: ["James Adam"]
year: 2026
venue: "NeSy 2026 (Industry Track)"
citation_count: 0
doi: ""
---

## 概要
MOOSEDev 是一个为 coding agent 提供结构化、ontology-grounded project memory 的系统，将架构决策、教训、约束、rationale 和 anti-pattern 以 typed records 形式存入 knowledge graph，通过 Model Context Protocol (MCP) 接口暴露给 agent。Records 携带 lifecycle status、provenance 和 supersession links，由 MOOSE neurosymbolic engine 在运行时执行 ontology traversal、deterministic evidence fusion 和 ranking。在 835 条 typed records 的中立语料上对比 production vector-memory tool，MOOSEDev 在 supersession、set-completeness 和 negation 问题上返回近乎完整的答案集（0.98–1.00），而 baseline 的 top-k retrieval 仅返回 6%–27%。

## 解决的问题
Coding agent 产生大量代码变更后，团队逐渐丧失对"代码为何如此"的理解——作者称之为 "comprehension debt"（Naur 1985 的 theory building 概念的延伸）。现有方案如 notes files、Markdown specs、RAG 和 mem0 的 vector memory 能找到相近的词，但无法区分一条记录是什么类型（decision/constraint/rationale/lesson/anti-pattern）、是否当前有效、以及记录间如何关联（this decision supersedes that one）。这些区分本质上是 ontological 的，vector search 无法回答。

## 方法与技术
1. **双 ontology + SHACL shapes**：software-engineering ontology（9 classes）建模代码库结构词汇，software-architecture ontology（11 classes）建模架构知识，共 51 properties；均为 OWL ontology 配套 SHACL shapes，运行时由 MOOSE engine 推理。
2. **Typed records with lifecycle & supersession**：每条 record 携带 rationale、supersede 关系、affected component、lifecycle status、author、timestamp，形成可遍历的网络；通过 typed capture 和 SHACL 验证保证结构化。
3. **Neurosymbolic engine（LLM as unreliable sensor）**：keyword/structural matching、ontology traversal、deterministic evidence fusion、validation、execution traces 均为 symbolic 层操作；LLM 仅在 narrow、declared points 被调用（可使用 8–32B 小模型）。
4. **MCP 接口暴露四组工具**：typed capture、reading（context retrieval、natural-language query、SPARQL）、lifecycle、integrity——agent 自主决定何时调用。
5. **Temporal commit-history bootstrap**：逐 commit 遍历 repository 历史，提取带历史时间戳的 typed records，恢复 supersession chains。

## 创新点
- **Coding agent memory as ontology problem（vs. vector memory / notes files）**：将 project memory 从 note-keeping 问题重新定义为 modeling 问题——vector search 能找相近的词但不知道 record 的类型或 lifecycle role。
- **Supersession as first-class relationship（vs. flat documentation）**：superseded records 在 current-guidance retrieval 中被 construction 排除——在 40 次 reversal 试验中 100% 返回当前答案，而 B1-rag 仅在 8% 试验中返回当前答案。
- **Neurosymbolic with small models（vs. pure LLM reasoning）**：将 LLM 视为 unreliable sensor，仅在 declared points 调用，symbolic 层处理 traversal/fusion/ranking——支持 8–32B 小模型。
- **Temporal commit-history bootstrap（vs. graph from current state only）**：从当前状态构建的 graph 是 flat 的，缺少历史关系；bootstrap workflow 恢复 supersession chains。

## 效果
- Dataset: CodeGraph corpus | Metric: Set completeness | Result: 1.00 (B2 typed graph) | Baseline: 0.18 (B1-mem0) | Δ: [+455.6%]
- Dataset: CodeGraph corpus | Metric: Negation (absence) | Result: 0.98 (B2) | Baseline: 0.06 (B1-mem0) | Δ: [+1533.3%]
- Dataset: CodeGraph corpus | Metric: Supersession traversal | Result: 0.98 (B2) | Baseline: 0.27 (B1-mem0) | Δ: [+263.0%]
- Dataset: Private corpus | Metric: Set-overlap F1 | Result: 0.94 | Baseline: 0.25 (B1-rag) | Δ: [+276.0%]
- Dataset: Neutral public corpus | Metric: Set-overlap F1 | Result: 0.90 | Baseline: 0.34 (B1-rag) | Δ: [+164.7%]
- Dataset: Scale study (634 records) | Metric: hit@5 | Result: 0.84 | Baseline: 0.60 (mem0) | Δ: [+40.0%]
- Dataset: 4 reversal pairs × 40 trials | Metric: Current answer served | Result: 100% (40/40, B2 graph) | Baseline: 8% (1/13, B1-rag) | Δ: [+92pp]

## 关键引用
> "Those distinctions are fundamentally ontological. A vector search can find nearby words; it does not know what a record is or what lifecycle role it plays." — Section 1, Introduction

> "It is not caused by incomplete ingestion: B1-mem0 contains the relevant facts, but its retrieval returns a limited ranked slice, so it cannot enumerate a complete set, establish an absence, or traverse relationships." — Section 3, Evaluation

> "Each time a plausible-but-wrong conclusion almost stuck, an auditable, re-checkable process caught it: exactly the failure mode (confident, fluent, wrong) this class of system exists to reduce." — Section 4, Deployment

## 关联
- [[OntologyGraphRetrieval]] — 本体图检索核心概念
- [[AuditableStructuredRetrieval]] — 可审计结构化检索
- [[moss-auditable-agentic-memory]] — Round 15 结构化关系DB替代嵌入搜索
- [[worlddb-ontology-aware-memory]] — Round 15 本体感知图世界记忆引擎
- [[AgentMemory]] — Agent 记忆概念
