---
title: "Domain-Grounded Tool Orchestration: 领域本体约束科学分析工具编排（LLM-Guided Scientific Analysis）"
type: source
tags: [ontology-skill-routing]
sources: [domain-grounded-tool-orchestration]
source_file: raw/papers/domain-grounded-tool-orchestration.pdf
last_updated: 2026-09-08
arxiv_id: "2608.30696"
authors: ["Jeff Lee", "Sebastien Jourdain", "Cory Quammen", "Patrick O'Leary", "Berk Geveci"]
year: 2026
venue: "arXiv preprint"
citation_count: 0
---

## 概要
本文提出把 LLM 的 intent interpretation、确定性 domain tool 的 execution、LLM 的 explanation 三者分离的架构，由 Model Context Protocol (MCP) 连接、由 domain ontology 约束规划到合法分析链。架构在同一个 ParaView server 上实例化了两个领域——CFD 后处理与基于 Topology ToolKit (TTK) 的拓扑数据分析——且新增第二领域只需一个 ontology 加现有 filter 的 tool wrapper。通过构造，该设计消除了脚本生成整类失败（如 API hallucination），并把残留的战略性错误收窄到 ontology 边界内。

## 解决的问题
科学分析工作流把深层领域知识编码在紧耦合的操作序列中，正确性依赖工具选择、执行顺序与参数化。现有 LLM 辅助科学可视化方法（如 VizGenie、ChatVis）生成脚本隐式编码这些知识且常常错误，产生"能执行但结果错误"的代码——最危险的失败模式无法靠更好的代码生成解决。这些系统还多为 solver-specific、缺领域 ontology 约束规划、且不返回结构化结果供 LLM 解读。

## 方法与技术
1. **Plan–Execute–Interpret 闭环**：Plan 阶段 LLM 查 ontology 把现象映射到 indicator 量与工具；Execute 阶段 MCP 把确定性 domain workflow 派发到 ParaView pipeline 并返回结构化定量数据；Interpret 阶段 LLM 结合 ontology 的 follow-ups 字段做量化解释。
2. **五字段 domain ontology schema**：每条 entry 含 phenomenon（可观测特征）、indicators（揭示它的量）、tools（提取操作）、follow-ups（下一步查什么）、significance（为何重要）。
3. **两层 MCP 工具 + 动态字段解析**：domain workflow 工具封装多步专家流程；工具接受语义字段名并用 pattern matching + alias table 在运行时解析到 solver-specific 数组名，杜绝静默跨求解器错误。
4. **安全 pipeline 管理**：consumer-aware deletion 防止破坏下游 filter 依赖，基础设施 filter 自动复用已有匹配实例。
5. **Client-server 部署 + in-situ 控制**：pvserver 持全部数据并渲染，浏览器只收压缩 JPEG 帧；in-situ 模式经 Catalyst Live 协议连接运行中求解器。

## 创新点
- **结构化返回驱动闭环 vs 一次性脚本**（vs VizGenie/ChatVis 生成脚本 fire-and-forget 只返回图像）——工具返回结构化定量数据，使 Interpret 阶段能做量化推理。
- **Domain ontology 约束规划到物理合法链**（vs ParaView-MCP 仅 MCP 直接工具调用无 ontology 约束）——ontology 把可观测现象映射到物理量与工具。
- **按构造消除整类失败**——API hallucination（LLM 不发 API）与 module error（工具预实现）按构造消除。
- **跨领域同栈复用 + 量化边际成本**——新增 TTK 领域仅需 60 行 JSON ontology + 约 400 行 Python，架构/协议/部署零改动。

## 效果
- Dataset: 34-case interpretation | Metric: Accuracy | Result: 0.91 (with ontology) | Baseline: 0.41 (unaided) | Δ: [+122%]
- **Ablation**: Bulk ontology dump: 0.56 | Tool-response mined: 0.74 | Single scoped fact: 0.91 — bulk dump 衰退向无辅助基线
- **Ablation (null result)**: Tool selection precision/recall: unchanged with vs without ontology — 选择已可靠、ontology 无关
- TTK: Critical points 342→213 (38% reduction); persistence diagram 138 birth-death pairs

## 关键引用
> "The LLM should decide what to analyze and explain what it means; domain tools should handle how." — Section 7, p.22

> "ontology grounding does not measurably affect tool selection... We report this as a null result; selection is reliable and ontology-independent." — Section 8.2, p.23

> "The guiding principle is straightforward: the LLM is the interface, not the engine. Domain workflows are the engine. MCP is the protocol. The ontology is the knowledge." — Section 11, p.25

## 关联
- [[OntologyGuidedQueryGeneration]] — 本体引导查询构造
- [[dynamic-ontology-llm-agents]] — Round 16 动态本体内核
- [[ontology-project-memory-coding]] — Round 16 编码 Agent 本体记忆
- [[NeurosymbolicOrchestration]] — Round 8 神经符号编排
- [[SkillNet]] — 本轮技能网络
