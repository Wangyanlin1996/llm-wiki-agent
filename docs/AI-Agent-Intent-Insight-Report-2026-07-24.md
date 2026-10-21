# 多智能体解决长上下文问题 论文洞察日报 — 2026-07-24

**日期**: 2026-07-24
**累计论文**: 240 篇（本轮新增 32 篇）
**知识库页面**: 378 页
**PDF 存档**: 239 篇
**概念页面**: 108 个

## 概览

| 方向 | 本轮新增 | 累计 |
|---|---|---|
| A. 核心多智能体长上下文框架 | 5 | 5 |
| B. 多智能体 RAG / 长文档 QA | 3 | 3 |
| C. 多智能体记忆与上下文管理 | 5 | 5 |
| D. 多智能体基础设施 | 5 | 5 |
| E. 多智能体特定长上下文任务 | 9 | 9 |
| F. 分析与扩展行为 | 5 | 5 |
| **合计** | **32** | **32** |

## 新增论文清单

### A. 核心多智能体长上下文框架

| #   | 论文                                                          | 年份   | Venue   | arXiv                                          | 引用  | 核心贡献                                                     |
| --- | ----------------------------------------------------------- | ---- | ------- | ---------------------------------------------- | --- | -------------------------------------------------------- |
| 1   | [Chain-of-Agents (CoA)](../wiki/sources/chain-of-agents.md) | 2024 | NeurIPS | [2406.02818](https://arxiv.org/abs/2406.02818) | 261 | 奠基性框架：worker→manager 顺序处理；interleave reading & reasoning |
| 2   | [Graph of Agents (GoA)](../wiki/sources/graph-of-agents.md) | 2025 | arXiv   | [2509.21848](https://arxiv.org/abs/2509.21848) | 1   | 信息论压缩目标；2K context 超越 128K Llama 3.1 8B                  |
| 3   | [LSTM-MAS](../wiki/sources/lstm-mas.md)                     | 2026 | arXiv   | [2601.11913](https://arxiv.org/abs/2601.11913) | 1   | LSTM 门控映射到多智能体；+97.97% NarrativeQA vs CoA                |
| 4   | [COSMIR](../wiki/sources/cosmir.md)                         | 2025 | arXiv   | [2510.04568](https://arxiv.org/abs/2510.04568) | 1   | 结构化记忆替代自由文本传递；减少传播信息损失                                   |
| 5   | [Chow-Liu CoA](../wiki/sources/chow-liu-coa.md)             | 2026 | ICLR WS | [2603.09835](https://arxiv.org/abs/2603.09835) | 0   | Chow-Liu 树学习 chunk 依赖排序优化                                |

### B. 多智能体 RAG / 长文档 QA

| # | 论文 | 年份 | Venue | arXiv | 引用 | 核心贡献 |
|---|------|------|-------|-------|------|---------|
| 6 | [SPD-RAG](../wiki/sources/spd-rag.md) | 2026 | arXiv | [2603.08329](https://arxiv.org/abs/2603.08329) | 2 | 每文档一 agent + 递归 map-reduce；LOONG Avg 58.1 |
| 7 | [SLEUTH](../wiki/sources/sleuth-long-doc.md) | 2025 | arXiv | [2511.22850](https://arxiv.org/abs/2511.22850) | 13 | Retriever + 4 协作 agent 粗到细；多模态长文档 SOTA |
| 8 | [FinLongDocAgent](../wiki/sources/finlongdoc-agent.md) | 2026 | arXiv | [2604.03664](https://arxiv.org/abs/2604.03664) | 0 | 金融长文档多智能体多轮 RAG；迭代检索+计算+验证 |

### C. 多智能体记忆与上下文管理

| # | 论文 | 年份 | Venue | arXiv | 引用 | 核心贡献 |
|---|------|------|-------|-------|------|---------|
| 9 | [MemAgent](../wiki/sources/memagent-long-context.md) | 2025 | arXiv | [2507.02259](https://arxiv.org/abs/2507.02259) | 180 | RL 记忆 agent；8K→3.5M 外推 <5% 损失；512K RULER 95%+ |
| 10 | [AMA](../wiki/sources/ama-adaptive-memory.md) | 2026 | ACL | [2601.20352](https://arxiv.org/abs/2601.20352) | 4 | 多 agent 多粒度记忆；token -80% |
| 11 | [ShardMemo](../wiki/sources/shardmemo.md) | 2026 | arXiv | [2601.21545](https://arxiv.org/abs/2601.21545) | 1 | Masked MoE 路由分片记忆；三层架构 |
| 12 | [Governed Shared Memory](../wiki/sources/governed-shared-memory.md) | 2026 | arXiv | [2606.24535](https://arxiv.org/abs/2606.24535) | 0 | fleet-memory 治理原语；MemClaw 生产级实现 |
| 13 | [Ensemble QSP](../wiki/sources/ensemble-qsp.md) | 2026 | arXiv | [2607.07666](https://arxiv.org/abs/2607.07666) | 0 | 三层层次记忆；中位 301 tokens；5 specialist agents |

### D. 多智能体基础设施

| # | 论文 | 年份 | Venue | arXiv | 引用 | 核心贡献 |
|---|------|------|-------|-------|------|---------|
| 14 | [AAFLOW+](../wiki/sources/aaflow-plus.md) | 2026 | arXiv | [2607.10987](https://arxiv.org/abs/2607.10987) | 1 | KV cache 一等分布式对象；零拷贝；TTFT -50.2x |
| 15 | [Agent Primitives](../wiki/sources/agent-primitives.md) | 2026 | arXiv | [2602.03695](https://arxiv.org/abs/2602.03695) | 6 | 可复用原语 + KV cache 通信；token -3~4x |
| 16 | [Twin Agent](../wiki/sources/twin-agent.md) | 2026 | arXiv | [2607.19595](https://arxiv.org/abs/2607.19595) | 0 | 上下文残差压缩；双 agent 特权分离 |
| 17 | [SideQuest](../wiki/sources/sidequest.md) | 2026 | arXiv | [2602.22603](https://arxiv.org/abs/2602.22603) | 7 | LRM 自驱动 KV cache 压缩；peak token -65% |
| 18 | [XFlow](../wiki/sources/xflow-multi-agent.md) | 2026 | arXiv | [2606.14790](https://arxiv.org/abs/2606.14790) | 0 | 可执行协议编程系统；约束显式可执行 |

### E. 多智能体特定长上下文任务

| # | 论文 | 年份 | Venue | arXiv | 引用 | 核心贡献 |
|---|------|------|-------|-------|------|---------|
| 19 | [SwarmResearch](../wiki/sources/swarmresearch.md) | 2026 | arXiv | [2607.02807](https://arxiv.org/abs/2607.02807) | 0 | 全局/局部上下文分离编排；15/13 任务更优 |
| 20 | [WebSwarm](../wiki/sources/webswarm.md) | 2026 | arXiv | [2607.08662](https://arxiv.org/abs/2607.08662) | 0 | 递归多智能体深度搜索；过程级经验复用 |
| 21 | [CodeWiki](../wiki/sources/codewiki.md) | 2025 | ACL | [2510.24428](https://arxiv.org/abs/2510.24428) | 6 | 递归多智能体代码库文档；超 DeepWiki 4.73% |
| 22 | [DelTA](../wiki/sources/delta-translation-agent.md) | 2024 | ICLR | [2410.08143](https://arxiv.org/abs/2410.08143) | 29 | 多级记忆文档翻译；一致性 +4.58pp |
| 23 | [DS2SC-Agent](../wiki/sources/ds2sc-agent.md) | 2026 | arXiv | [2603.21190](https://arxiv.org/abs/2603.21190) | 0 | 多智能体非结构化长文档→SystemC |
| 24 | [MemDocAgent](../wiki/sources/memdocagent.md) | 2026 | arXiv | [2605.14563](https://arxiv.org/abs/2605.14563) | 0 | 共享 RepoMemory 仓库级代码文档 |
| 25 | [MACF](../wiki/sources/macf-video.md) | 2026 | arXiv | [2605.00444](https://arxiv.org/abs/2605.00444) | 2 | 潜在多智能体协作视频理解；预算解耦 |
| 26 | [LMM-Searcher](../wiki/sources/lmm-searcher.md) | 2026 | arXiv | [2604.12890](https://arxiv.org/abs/2604.12890) | 4 | 100-turn 多模态搜索；UID 映射 |
| 27 | [Traj-Evolve](../wiki/sources/traj-evolve.md) | 2026 | arXiv | [2606.02812](https://arxiv.org/abs/2606.02812) | 0 | 自演化多智能体 EHR；ExPool + MARL |

### F. 分析与扩展行为

| # | 论文 | 年份 | Venue | arXiv | 引用 | 核心贡献 |
|---|------|------|-------|-------|------|---------|
| 28 | [SIMAS](../wiki/sources/simas.md) | 2026 | arXiv | [2606.00655](https://arxiv.org/abs/2606.00655) | 0 | MAS 扩展定律：递减回报；协调开销是主因 |
| 29 | [TEP](../wiki/sources/tep-textual-equilibrium.md) | 2026 | ICLR | [2601.21064](https://arxiv.org/abs/2601.21064) | 1 | textual gradient 爆炸/消失；平衡传播 |
| 30 | [HIPIF](../wiki/sources/hipif.md) | 2026 | arXiv | [2606.10507](https://arxiv.org/abs/2606.10507) | 1 | 层级规划 + 信息折叠；子目标历史折叠 |
| 31 | [PRIMA](../wiki/sources/prima-multi-agent.md) | 2026 | arXiv | [2605.24775](https://arxiv.org/abs/2605.24775) | 0 | 弹性多智能体研究操作模式；上下文压缩 |
| 32 | [Agentic Context Management](../wiki/sources/agentic-context-management.md) | 2026 | arXiv | [2607.21503](https://arxiv.org/abs/2607.21503) | 0 | 上下文生命周期+架构管理 |

## 新增趋势洞察

### 1. 顺序链式处理是基础范式，但持续演进

从 [Chain-of-Agents](../wiki/sources/chain-of-agents.md) 的自由文本传递 → [COSMIR](../wiki/sources/cosmir.md) 的结构化记忆 → [LSTM-MAS](../wiki/sources/lstm-mas.md) 的门控机制 → [Graph of Agents](../wiki/sources/graph-of-agents.md) 的信息论形式化 → [Chow-Liu CoA](../wiki/sources/chow-liu-coa.md) 的排序优化。每一步都在解决前一步的信息瓶颈问题。**核心张力是"压缩 vs 保留"**——如何在有限上下文中传递最大信息量。参见概念页 [多智能体长上下文建模](../wiki/concepts/MultiAgentLongContext.md) 和 [顺序智能体推理](../wiki/concepts/SequentialAgentReasoning.md)。

### 2. KV Cache 共享是系统级突破口

从"文本传递"到"KV 传递"的范式转换是最具系统级影响的突破。[AAFLOW+](../wiki/sources/aaflow-plus.md) 将 KV cache 提升为一等分布式对象（TTFT -50.2x），[Agent Primitives](../wiki/sources/agent-primitives.md) 用 KV cache 内部通信替代自然语言（token -3~4x），[SideQuest](../wiki/sources/sidequest.md) 让 LRM 自身驱动 KV 压缩（peak token -65%）。关键发现：**在中等至高带宽网络上，KV 传输优于重新计算**。参见概念页 [多智能体 KV Cache 共享](../wiki/concepts/AgentKVCacheSharing.md)。

### 3. 记忆管理是多智能体的核心挑战

[MemAgent](../wiki/sources/memagent-long-context.md)（180 citations）通过 RL 训练覆写记忆策略实现 8K→3.5M 外推，是本领域引用最高的工作。[AMA](../wiki/sources/ama-adaptive-memory.md) 用多 agent 协作管理多粒度记忆，[ShardMemo](../wiki/sources/shardmemo.md) 从分片路由角度优化，[Governed Shared Memory](../wiki/sources/governed-shared-memory.md) 提出 fleet-memory 治理原语。趋势：**从单 agent 记忆 → 多 agent 协作记忆 → 治理化共享记忆**。参见概念页 [多智能体上下文管理](../wiki/concepts/MultiAgentContextManagement.md)。

### 4. 扩展定律：递减回报打破"更多 agent 更好"假设

[SIMAS](../wiki/sources/simas.md) 发现 MAS 性能不随 agent 数单调提升而是递减回报模式，协调开销是主因而非长上下文失败。[TEP](../wiki/sources/tep-textual-equilibrium.md) 进一步识别了深度复合 AI 的 textual gradient 爆炸/消失问题。这意味着**多智能体系统设计需要在协作协同与协调开销之间找到最优平衡点**。

### 5. 从理论到实践：特定领域验证广泛有效性

多智能体长上下文方法已在代码库（[SwarmResearch](../wiki/sources/swarmresearch.md), [CodeWiki](../wiki/sources/codewiki.md), [MemDocAgent](../wiki/sources/memdocagent.md)）、搜索（[WebSwarm](../wiki/sources/webswarm.md), [LMM-Searcher](../wiki/sources/lmm-searcher.md)）、翻译（[DelTA](../wiki/sources/delta-translation-agent.md)）、视频（[MACF](../wiki/sources/macf-video.md)）、医疗（[Traj-Evolve](../wiki/sources/traj-evolve.md)）等多个领域验证有效性。**生产级应用需要将上下文管理视为生命周期和架构问题**（[Agentic Context Management](../wiki/sources/agentic-context-management.md)）。

### 6. 信息论形式化提供理论指导

[Graph of Agents](../wiki/sources/graph-of-agents.md) 将多智能体长上下文建模形式化为信息论压缩问题，仅用 2K context 超越 128K Llama 3.1 8B。这是首个用理论框架指导多智能体协作结构设计的工作，标志着该领域从经验性设计向理论指导设计的转变。

## 知识库状态

| 指标 | 值 |
|---|---|
| 累计论文 | 240 篇 |
| 本轮新增 | 32 篇 |
| 知识库页面 | 378 页 |
| PDF 存档 | 239 篇 |
| 概念页面 | 108 个 |
| 健康检查 | 0 空文件, 0 索引同步问题 |
| 本轮最高引用 | Chain-of-Agents (261), MemAgent (180), DelTA (29) |

## 高引论文 Top 5

| 排名 | 论文 | 引用 | Venue | 核心影响 |
|---|---|---|---|---|
| 1 | [Chain-of-Agents (CoA)](../wiki/sources/chain-of-agents.md) | 261 | NeurIPS 2024 | 奠基性多智能体长上下文框架 |
| 2 | [MemAgent](../wiki/sources/memagent-long-context.md) | 180 | arXiv 2025 | RL 记忆 agent 8K→3.5M 外推 |
| 3 | [DelTA](../wiki/sources/delta-translation-agent.md) | 29 | ICLR 2025 | 多级记忆文档翻译 |
| 4 | [SLEUTH](../wiki/sources/sleuth-long-doc.md) | 13 | arXiv 2025 | 多智能体长文档理解 |
| 5 | [SideQuest](../wiki/sources/sidequest.md) | 7 | arXiv 2026 | 模型驱动 KV cache 压缩 |

## 相关概念页面

- [多智能体长上下文建模](../wiki/concepts/MultiAgentLongContext.md) — 多 agent 协作处理超出单模型上下文窗口的长输入
- [顺序智能体推理](../wiki/concepts/SequentialAgentReasoning.md) — 长输入分段→worker 顺序处理→manager 综合
- [多智能体上下文管理](../wiki/concepts/MultiAgentContextManagement.md) — 多 agent 系统中上下文的管理/共享/治理
- [多智能体 KV Cache 共享](../wiki/concepts/AgentKVCacheSharing.md) — 多 agent 间复用 KV cache 避免重复 prefill
- [多智能体 RAG](../wiki/concepts/MultiAgentRAG.md) — 文档级专业化 + 中心化融合
