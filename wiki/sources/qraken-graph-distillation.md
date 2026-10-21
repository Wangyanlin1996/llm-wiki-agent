---
title: "QRAKEN（图蒸馏+语义自愈的 Text-to-SPARQL）"
type: source
tags: [owl2-reasoning]
sources: [qraken-graph-distillation]
source_file: raw/papers/qraken-graph-distillation.pdf
last_updated: 2026-10-21
arxiv_id: "2610.08095"
authors: ["Remo Grillo", "Lukas Klic", "Giovanni Colavizza"]
year: 2026
venue: "GLOW @ ISWC 2026 Workshop"
citation_count: 0
doi: ""
---

## 概要
QRAKEN 是 training-free 的神经符号 Text-to-SPARQL 管线：离线蒸馏器穷举构建类-属性共现矩阵与 TTQL 描述（图实际观测到的多跳模式+条件频率+字面量示例），在线用 TTQL 引导 LLM 生成查询，再经三级确定性校验（语法→词法→数据模型）失败反馈修复。核心洞察：对预训练分布外的图，主导失败模式不是语法而是**图接地正确性**——而描述"数据实际长什么样"的经验性内容比 SHACL 形状（"数据应当长什么样"）更能接地 LLM：TTQL 0.643 vs SHACL-auto 0.376（+64%）。

## 解决的问题
RDF KG 自然语言问答中，主要失败是查询能解析、用真实词表、却悄悄歪曲图的实际数据模型（幻觉谓词、边方向颠倒）。已有三族方法不足：① 在线 agentic 探索（ARUQULA，~1 分钟/题，每题重新理解图）；② 微调/经验池（需问题-查询对，不适应 schema 漂移）；③ shape/metadata 提示（AIFB 等）基于"图应当包含什么"而非"图实际填充了什么"。

## 方法与技术
1. **离线图蒸馏器**：枚举 SPARQL endpoint 的类，穷举构建类-属性-目标类共现矩阵 M（非采样，M[c,p,c′]=0 是边不存在的**确定性证明**）；按 Borda 式星级得分排名类，分层抽样种子实例，收割 ≤H 跳模式并标注条件频率与字面量示例。
2. **TTQL 描述语言**：Turtle 风格但描述性而非规范性——报告图实际观测到的多跳模式（含隐藏中间 join）、条件频率（Markov 式）、路径条件化字面量示例（如国家写作 "ITA"/"Italy"/wd:Q38 的词法约定）。与 SHACL/ShEx 的区别：shape 节点中心、可脱离数据从 schema 编写；TTQL 永远从已填充数据导出。
3. **三级确定性校验管线**：Stage 1 语法（rdflib 解析 + 前缀自动补全）；Stage 2 词法（类/属性对照 TTQL 经验词表防造词）；Stage 3 数据模型（查询中每个 (class, property, target) 三元组对照共现矩阵，零支持即拒绝——保证必然返回空绑定的查询不会执行）。
4. **校验失败反馈修复（自愈循环）**：某级失败 → 确定性诊断消息 → refinement prompt 回传 LLM 修改，最多 5 轮；模型只根据外部接地的确定性诊断修改，避免上下文漂移。
5. **机器侧/提示侧分工**：TTQL 注入 prompt（约 12% 于图体积，~8× 压缩）；共现矩阵 M 仅留在机器侧供校验，不占上下文。

## 创新点
- **vs ARUQULA（同基座 gpt-4.1-mini 最近对照）**：离线蒸馏+在线确定性校验替代在线探索——strict F1 **0.643 vs 0.493**（+30%），1.43 次 LLM 调用/3.5s vs 9.92 agent 步/59.6s。
- **vs auto-derived SHACL 形状基线（shexer 自动生成）**：TTQL 0.643 vs SHACL-auto **0.376**（相对 +64%）——给 LLM 正面经验描述的收益约是暴露同等 schema 结构约束的 4.5×。
- **vs 微调/记忆型（mKGQAgent，挑战赛冠军）**：training-free 且更便宜（$1.18/100q vs $3.06/100q）而 F1 更高（0.617 vs 0.333）。
- **vs ABSTAT 一族单跳摘要**：TTQL 保留多跳路径条件性与路径条件化字面量，同时服务 LLM 提示与确定性校验双目的。

## 效果
- Dataset: CK25（First Text2SPARQL Challenge，50 题、13 类/30 属性/~26.5K 三元语句，QLever 快照）| Metric: strict F1 | Result: **0.643±0.026**（gpt-4.1-mini）、**0.652±0.012**（gpt-5.4）| Baseline: 最强重算参赛者 ARUQULA 0.493 | Δ: +30%/+32%
- Dataset: 同上 | Metric: 消融 2×2 | Result: TTQL 模式块贡献 +0.309（4.1-mini）/+0.153（5.4）；自愈循环 −0.009~+0.067（校验器放行 ~94% 首轮查询，是"确定性失败过滤器"）；SHACL-auto 仅 0.376
- Dataset: 开源权重 | Metric: strict F1 | Result: Qwen3.6-35B 4-bit 本地 **0.491±0.036**——与最强重算参赛者持平，零边际成本
- 成本：$1.18/100q、1.00 次 LLM 调用/题、中位延迟 5.0s；蒸馏一次 ~15 分钟
- 局限：单基准 50 题；失败集中在多约束组合（superlative+聚合+多 filter）、字面量规范化、聚合作用域错误

## 关键引用
> "the dominant failure mode, on graphs outside the LLM pretraining distribution, is not syntax but graph-grounded correctness: queries that parse, use real vocabulary, and still silently misrepresent the data model of the target graph." — Section 1

> "The core conceptual shift is therefore to treat LLM output not as authoritative but as a candidate hypothesis that must survive transparent, deterministic verification against all three layers." — Section 3

> "Because M is built by exhaustive enumeration rather than sampling, M[c,p,c′]=0 is not a low-support heuristic but a proof of class-level graph-impossibility: any triple pattern requiring such an edge is guaranteed to return an empty binding on the live endpoint." — Section 4.4

## 关联
- [[ValidationFeedbackLoop]] — 三级校验+确定性诊断+定向修复 prompt 是校验-修复闭环的最干净实例
- [[OntologyConstrainedGeneration]] — "描述性经验内容优于规范性 SHACL 形状"修正了纯 schema 约束路线
- [[nlkgq-nl-ontology-query]] — 同为 OWL/RDF 本体引导 LLM 生成结构化查询，NLKGQ 用 schema、QRAKEN 用经验分布
- [[retrieval-state-lock-in]] — 同关注"查询看似合法却系统性偏离数据模型"的隐蔽失败
- [[ontology-hybrid-prompt-kgqa]] — 同为本体 verbalization 注入 prompt 的 KGQA 路线
