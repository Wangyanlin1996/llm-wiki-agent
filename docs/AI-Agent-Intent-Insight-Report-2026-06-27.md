# 记忆增强模糊意图澄清 — 论文洞察日报

**日期**: 2026-06-27
**累计论文**: 86 篇（本轮新增 6 篇）
**知识库页面**: 163 页

## 概览

| 方向 | 累计 | 本轮新增 |
|------|------|---------|
| Agent Memory | 20 | 0 |
| Intent Understanding | 23 | 0 |
| Intent Recommendation | 19 | 0 |
| **Memory-Enhanced Intent Clarification** | **6** | **6** |

## 新增论文清单

| #   | 论文                                               | 年份   | Venue         | arXiv                                                                  | 核心贡献                           |
| --- | ------------------------------------------------ | ---- | ------------- | ---------------------------------------------------------------------- | ------------------------------ |
| 1   | [[rac]] — RAC: Retrieval-Augmented Clarification           | 2026 | ECIR 2026     | [2601.11722](https://arxiv.org/abs/2601.11722) | RAG生成语料锚定澄清问题；对比偏好优化           |
| 2   | [[corpus-rag-clarifying]] — Corpus-informed RAG of Clarifying Questions      | 2024 | -             | [2409.18575](https://arxiv.org/abs/2409.18575) | RAG联合建模query+corpus定位不确定性；数据增强 |
| 3   | [[cops]] — CoPS: Cognitive Personalized Search              | 2024 | WWW 2024      | [2402.10548](https://arxiv.org/abs/2402.10548) | 认知三阶记忆(感觉/工作/长期)驱动个性化搜索意图      |
| 4   | [[janus]] — JANUS: Factored Reasoning with Persistent Memory | 2026 | -             | [2602.00675](https://arxiv.org/abs/2602.00675) | 持久记忆+内部言语触发澄清；从欠明确请求恢复         |
| 5   | [[sensitivity-aware-clarification]] — Sensitivity-Aware RA Intent Clarification        | 2026 | ECIR Workshop | [2603.06025](https://arxiv.org/abs/2603.06025) | 敏感域检索增强意图澄清；攻击模型+防御            |
| 6   | [[fairy-gui-agent]] — Fairy: Robust Agentic Systems (EMA+RGR)          | 2025 | -             | [2509.20729](https://arxiv.org/abs/2509.20729) | 演化记忆+目标精炼澄清；模糊任务+33.7%         |

## 新增趋势洞察

### 三种互补范式
"记忆增强模糊意图澄清"形成三种互补路径：

1. **外部检索（RAG as external memory）**— [[rac]]、[[corpus-rag-clarifying]]、[[sensitivity-aware-clarification]] 将语料库作为外部记忆，为澄清问题提供证据支撑。核心洞察：澄清问题必须锚定在可用信息中。

2. **内部认知记忆（Cognitive memory as internal context）**— [[cops]]、[[janus]] 用层次化认知记忆（感觉/工作/长期 或 近期/核心/归档）提供用户上下文消解歧义。CoPS 从历史构建画像驱动个性化意图，JANUS 用内部言语触发澄清。

3. **演化记忆+目标精炼（Evolutionary memory + goal refinement）**— [[fairy-gui-agent]] 用执行-演化双循环记忆 + 人在环目标精炼确保意图对齐。

### 共同洞察
**模糊意图的歧义源于上下文缺失，记忆提供缺失的上下文来消解歧义或在不足时触发有针对性的澄清。** 这与 [[IntentSignalTheory]] 的 I*→P 信息损失定理呼应——记忆是补偿信息损失的关键机制。详见各论文：[[rac]]、[[corpus-rag-clarifying]]、[[sensitivity-aware-clarification]]、[[cops]]、[[janus]]、[[fairy-gui-agent]]。

### 新增概念
- [[RetrievalAugmentedClarification]] — 检索增强澄清
- [[CognitiveMemoryMechanism]] — 认知记忆机制
- [[PersistentMemoryClarification]] — 持久记忆澄清
- [[EvolutionaryMemoryArchitecture]] — 演化记忆架构

## 知识库状态

| 指标 | 数值 |
|------|------|
| 论文总数 | 86 |
| wiki 页面 | 163 |
| 概念页面 | 33 |
| PDF 文件 | 85 |
| Health 检查 | 0 empty, 0 sync issues |
