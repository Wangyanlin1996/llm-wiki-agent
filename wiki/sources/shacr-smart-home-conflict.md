---
title: "SHACR（智能家居 IoT 多类冲突消解的图增强 LLM 框架）"
type: source
tags: [owl2-reasoning]
sources: [shacr-smart-home-conflict]
source_file: raw/papers/shacr-smart-home-conflict.pdf
last_updated: 2026-10-21
arxiv_id: "2606.22312"
authors: ["Leena Marghalani", "Walid Aljoby", "Suayb S. Arslan"]
year: 2026
venue: "IEEE Internet of Things Journal (投稿格式)"
citation_count: 0
doi: ""
---

## 概要
智能家居用户规则孤立看无害，并发执行却经共享设备、环境变量、物理拓扑产生隐藏冲突（节能规则关插座→断电安防摄像头）。SHACR 用类型化有向知识图谱（Neo4j）把物理因果编码为可遍历的 AFFECTS 边，将三类冲突检测（逻辑/语义/物理）形式化为图遍历问题，再用 GraphRAG + MCP 工具白名单约束 LLM 做 Scan–Explain–Repair–Validate 闭环。关键发现：同一 LLM 加图 grounding 后 F1 0.59→0.79——**决定性能的是表示而非模型**。

## 解决的问题
已有方法各只覆盖一类冲突：形式规则分析器（IoTC2、TapChecker SMT）只查语法矛盾，对拓扑/环境中介冲突结构性失明；语义框架（IoTMon、IoT-Praetor、IoTMediator）需手工设备行为模型、无跨平台统一、无用户修复指引；LLM 方案（LLM-HA 等）缺拓扑信息时不可靠。缺口：没有系统同时覆盖逻辑/语义/物理三类冲突并给出可执行修复。

## 方法与技术
1. **类型化有向知识图谱**（Neo4j AuraDB）：12 种节点类型 + 12 种有向边；核心 **AFFECTS 边（Capability→State|EVar）** 把"插座断电→摄像头失能"等物理因果变为一等公民图边。
2. **三类冲突形式化**（Def.1–3）：逻辑冲突 = 两 Action 以互斥值 TARGETS 同一 State 节点（0 跳）；语义冲突 = 经单条 AFFECTS 边激活另一规则（1 跳）；物理冲突 = 多跳路径破坏安全谓词 Φ(G)——每类对应确定的图遍历模式。
3. **GraphRAG + MCP 工具白名单**：LLM（Claude Sonnet 4）只通过 5 个 MCP 工具操作（4 读 1 写）；写工具被用户批准硬性门控——LLM 不能自治改图。
4. **Scan–Explain–Repair–Validate 闭环**：检索公寓子图 → LLM 检测分类 → 图路径回溯解释 → 白名单修复动作空间（允许改触发条件/加互斥/调优先级；禁止删规则设备、发明新实体、删物理拓扑边）→ validate_repair 复检，未解决换方案，有界终止。
5. **检索架构迭代教训**：单条大 Cypher（超时）→ Cypher 内硬编码检测（只剩逻辑类）→ 最终两条并行轻查询 + Python 按 ruleId 合并，把完整图上下文交还 LLM 推理。

## 创新点
- **vs IoTC2/VISCR/TapChecker（纯规则文本形式方法）**：首次把物理因果编码为可遍历 AFFECTS 边——文本法原理上不可见的物理类冲突（其 F1 上限 0.54）可检出（F1 0.77）。
- **vs IoT-Praetor/IoTSAFE/IoTMediator（需预定义设备行为模型）**：类型图 schema + 统一 YAML 归一化实现跨平台（SmartThings/Home Assistant），并新增可执行修复 + 图上验证。
- **vs LLM-only（同模型同提示 YAML-only 基线）**：图 grounding 使 F1 0.59→0.79、错误率降 36.7%——证明表示而非模型是决定因素。
- **vs AutoIoT（LLM+形式验证生成规则）**：检测-解释-修复-验证全闭环 + 人在环写门控。

## 效果
- Dataset: 自建 testbed（203 规则、70 套公寓、63 冲突场景；真值 88 冲突规则 [38 逻辑/31 语义/19 物理]）| Metric: Zero-shot 全 SHACR | Result: **P 0.78 / R 0.80 / F1 0.79 / Acc 0.81**
- Dataset: 同上 | Metric: 图消融（同模型 Claude）| Result: YAML-only F1 **0.59** → 加图 **0.79**；总错误 60→38（**−36.7%**）
- Dataset: few-shot 校准 | Metric: F1 | Result: **7 平衡样本 → F1 0.95（P 1.00, R 0.90）**；同一校准对 YAML-only Claude 仅 0.72 后回落——few-shot 只有在图存在时才起效
- Dataset: vs 复现 baseline | Metric: F1 | Result: SHACR 0.79 vs IoTC2 **0.54**、VISCR **0.49**（后两者结构上限 43% 可表达冲突）
- **消融**：分类型 F1——逻辑 0.75 / 物理 0.77（文本法全盲的类）/ 语义 0.58（最难，漏检集中于长 EVar 依赖链）

## 关键引用
> "Even language models that can interpret natural language cannot reliably infer physical device dependencies from rule descriptions alone, because those dependencies exist in the deployment environment—not in the rule logic." — Section III-D, p.4

> "detecting conflicts becomes a graph traversal problem rather than an inference problem, and explaining it becomes a matter of returning the traversal path to the user." — Section III-D, p.5

> "Graph grounding and prompt calibration are therefore complementary rather than interchangeable, and the latter is conditional on the former." — Section VII-C, p.13

## 关联
- [[ValidationFeedbackLoop]] — Scan-Explain-Repair-Validate 闭环 + 写操作人在环门控是校验-修复闭环的 IoT 实例
- [[OntologyConstrainedGeneration]] — MCP 白名单工具约束 LLM 动作空间，禁止操作表防幻觉修复
- [[RuntimeGovernance]] — 确定性图遍历做 LLM 输出的独立后验校验，与动作级可验证治理同构
- [[governed-shared-memory]] — 同为"agent 不自治改图"的治理原语思想
- [[deontic-policies-agenticrei]] — 同为规则冲突检测+消解场景，道义逻辑 vs 图遍历两种形式化路线
