---
title: "本体辅助技能路由 (Ontology-Assisted Skill Routing)"
type: concept
tags: [ontology-skill-routing]
sources: [scx-router-task-ontology, domain-grounded-tool-orchestration, skillnet-ai-skills, generative-ontology, workflow-to-skill]
last_updated: 2026-09-08
---

本体辅助技能路由是指利用形式本体（ontology）的类型/层次/关系结构指导 LLM agent 的技能选择、工具编排和工作流路由的范式。核心洞察是：flat prompt-based routing 将 admissible concepts 和 action sequences 隐含在 prompt 中，无法提供可检查的 semantic-procedural contract；而本体将"何时应用"(Routing)、"如何执行"(Workflow)、"如何决策"(Semantics)、"运行时约束"(Attachments) 显式分离，使路由决策可审计、可验证。关键方法包括：(1) Task Ontology 三层结构（family→task type→routable subtype）驱动多标签 suitability 预测（[[scx-router-task-ontology]]）；(2) Domain Ontology 五字段 schema（phenomenon/indicators/tools/follow-ups/significance）约束 Plan-Execute-Interpret 闭环（[[domain-grounded-tool-orchestration]]）；(3) 三层 Skill Ontology（taxonomy+relation graph+package library）建模技能积累与组合（[[skillnet-ai-skills]]）；(4) Ontology 作为生成语法约束 LLM 创造（[[generative-ontology]]）；(5) Skill-IR 的 WSA 分解（Routing+Workflow+Semantics+Attachments）作为结构化运行时规范（[[workflow-to-skill]]）。与 [[ModelRouting]]（Round 11）的区别：后者是 LLM 推理层的模型选择，本体辅助技能路由是用本体结构化约束整个技能生命周期。

---

本体精准检索推理是指利用形式本体的类型/关系/约束结构实现超越纯向量相似度的精准检索导向推理。与"判断向"推理（verdict-oriented，如分类/判断）不同，本方向聚焦"检索向"（retrieval-oriented）——推理过程本身是检索-验证的迭代，本体的角色是提供约束满足的 binding requirements 而非 soft signals。关键方法包括：(1) 约束满足检索（SMT→关系代数投影，[[satir-constraint-ir-clinical]]）；(2) 层次化推理+过程监督（DeepSeek R1+RAG-Gym MDP，[[deeprag-hierarchical-reasoning]]）；(3) RAG 增强事件 KB+证明助手（RDF→Coq 翻译管线，[[ragged-events-reasoning]]）；(4) 迭代 RAG 本体生成（FK-Guided Traversal+Judge-LLM 验证，[[rag-ontology-relational-db]]）；(5) 知识内化自主推理（RERS 从失败轨迹学习，[[raredxr1-rare-disease]]）。核心发现：Inverse Calibration Principle——enhancement 效果与模型能力反向相关（[[ragged-events-reasoning]]），挑战"更多检索必然更好"假设。与 [[OntologyGraphRetrieval]]（Round 15-16）的区别：后者聚焦本体图增强检索精度，本方向聚焦本体驱动推理过程的约束满足和过程监督。

---

Agent 循环检测与消解是指识别 LLM agent 执行中的重复/停滞/错误级联模式并触发恢复机制的运行时治理范式。核心失败模式包括：(1) continuation invalidation——中间结果使后续计划失效（[[trove-trace-route-validation]]）；(2) perseveration——agent 卡在重复行为中（[[gubernaut-homeostatic-controller]]）；(3) cascading errors——单 agent 错误通过协作结构传播（[[masc-metacognitive-self-correction]]）；(4) harness flaws——runtime infrastructure 缺陷导致系统性失败（[[failed-trajectories-harness-flaws]]）；(5) underdefined objective——目标无法精确陈述导致 score 不可信任（[[argus-agentic-reasoning-runtime]]）。关键方法：(1) TROVE 的 Retain-Insert-Replace 三操作选择性路由编辑（保留已完成前缀仅修复无效后缀）；(2) Gubernaut 的确定性 arousal 动力学（token-free meta level，prompt injection 免疫）；(3) MASC 的 Next-Execution Reconstruction 无监督异常检测；(4) HARNESSFIX 的 HTIR 对齐+scoped repair operators；(5) Argus 的 verified pivoting + verification-gated admission。与 [[RuntimeGovernance]]（Round 8）的区别：Round 8 聚焦动作级验证/凭证/治理，本方向聚焦执行循环中的失败检测和恢复机制。与 [[RetrievalStateLockIn]]（Round 16）的呼应：后者诊断检索状态锁定，本方向提供循环消解的运行时机制。
