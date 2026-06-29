# Agent 闭环可解释性 — 论文洞察日报

**日期**: 2026-06-29
**累计论文**: 104 篇（本轮新增 18 篇：Phase A 4 篇 + Phase B 14 篇）
**知识库页面**: 192 页

## 概览

| 方向 | 累计 | 本轮新增 |
|------|------|---------|
| Agent Memory | 20 | 0 |
| Intent Understanding | 23 | 0 |
| Intent Recommendation | 19 | 0 |
| Memory-Enhanced Intent Clarification | 6 | 0 |
| **Agent Explainability** | **18** | **18** |

## 本轮重点：引文核查 + 真实替代论文检索

### Phase A：引文核查批次（4/15 真实，11 篇幻觉）

用户提供 15 篇支撑"Agent 闭环可解释性"框架的论文，经 arXiv ID 直查 + 标题检索核查：**11 篇为幻觉（73%）**。

**核查要点**：
- 2 个 arXiv ID 指向完全不相关论文（2504.01485→图论；2405.18023→编码论）——LLM 编造引用的标志性手法
- 9 篇标题在 arXiv 全检索 0 命中（CHI/NAACL/AAAI/ICSE/KR/AIJ/JAIR/NeurIPS WS/FAccT 等 venue 标注均无法证实）
- 2 篇作者归属有误
- 拒绝将幻觉论文入库，避免污染知识库

**入库 4 篇**：

| # | 论文 | 年份 | Venue | arXiv | 核心贡献 |
|---|------|------|-------|-------|---------|
| 1 | [[llm-autonomous-agent-survey]] — LLM Agent 统一架构综述 | 2024 | Frontiers of CS | [2308.11432](https://arxiv.org/abs/2308.11432) | 解释列为可信度核心维度；3137 citations |
| 2 | [[agentbench]] — AgentBench 多维评测 | 2024 | ICLR 2024 | [2308.03688](https://arxiv.org/abs/2308.03688) | 8环境评测；长程推理失败主因；951 citations |
| 3 | [[agentverse]] — AgentVerse 多智能体协作 | 2024 | ICLR 2024 | [2308.10848](https://arxiv.org/abs/2308.10848) | 动态重组；社会行为涌现 |
| 4 | [[explainable-human-ai-interaction]] — 可解释人机交互 | 2024 | Morgan & Claypool | [2405.15804](https://arxiv.org/abs/2405.15804) | "解释即规划"范式；心智模型对齐 |

### Phase B：14 篇真实替代论文入库

通过 arXiv API 按四主题布尔检索，找到 14 篇真实近期论文填补 Phase A 中四个框架方向的空缺。

#### T1 信息转换可观测性（3 篇）

| # | 论文 | 年份 | Venue | arXiv | 核心贡献 |
|---|------|------|-------|-------|---------|
| 1 | [[agent-traces-to-trust]] — 执行溯源与证据追踪综述 | 2026 | arXiv | [2606.04990](https://arxiv.org/abs/2606.04990) | 执行溯源=typed graph；证据追踪=evidence-support projection；过程级问责统一框架 |
| 2 | [[hansel-web-agent-verification]] — HANSEL 交互式验证 | 2026 | arXiv | [2606.18671](https://arxiv.org/abs/2606.18671) | 验证从被动阅读→交互导航；83.7% precision/88.8% recall；轨迹-61.6% |
| 3 | [[causal-past-logic-runtime-verification]] — CPL 运行时验证 | 2026 | arXiv | [2605.20923](https://arxiv.org/abs/2605.20923) | 分布式agent运行时验证嵌入协调语言；向量时钟监控器 |

#### T2 双受众分层解释（2 篇）

| # | 论文 | 年份 | Venue | arXiv | 核心贡献 |
|---|------|------|-------|-------|---------|
| 4 | [[three-level-llm-xai]] — 三层 XAI 框架 | 2025 | Information Systems Frontiers | [2506.05887](https://arxiv.org/abs/2506.05887) | 算法/领域→以人为中心→社会三层；LLM 跨层中介 |
| 5 | [[explainable-ai-to-whom]] — 解释给谁？ | 2021 | AI in Healthcare | [2106.05568](https://arxiv.org/abs/2106.05568) | 利益相关者星座；差异化解释需求；COVID-19 ICU 案例 |

#### T3 闭环验证溯因（4 篇）

| # | 论文 | 年份 | Venue | arXiv | 核心贡献 |
|---|------|------|-------|-------|---------|
| 6 | [[responsible-explainable-ai-agents]] — 共识驱动推理 | 2025 | arXiv | [2512.21699](https://arxiv.org/abs/2512.21699) | 多模型共识→分歧暴露→结构化整合；可审计决策 |
| 7 | [[blockchain-accountability-agents]] — 区块链问责 | 2024 | arXiv | [2403.09567](https://arxiv.org/abs/2403.09567) | 区块链防篡改黑箱+LLM生成解释；ROS机器人验证 |
| 8 | [[argument-is-the-explanation]] — 论证即解释 | 2025 | IAAI-26 submission | [2510.03442](https://arxiv.org/abs/2510.03442) | 结构化论证图；每步可验证；自动幻觉检测；94.44 F1 |
| 9 | [[causal-explanations-sequential-uncertainty]] — SCM 因果解释 | 2022 | arXiv | [2205.15462](https://arxiv.org/abs/2205.15462) | SCM因果解释基础；单一框架多语义解释；MDP因果推理 |

#### T4 多智能体解释（5 篇）

| # | 论文 | 年份 | Venue | arXiv | 核心贡献 |
|---|------|------|-------|-------|---------|
| 10 | [[trism-agentic-ai]] — TRiSM 综述 | 2025 | arXiv | [2506.04133](https://arxiv.org/abs/2506.04133) | AMAS信任/风险/安全管理；TRiSM五支柱；CSS+TUE指标 |
| 11 | [[cema-causal-explanations-mas]] — CEMA 因果解释 | 2023 | AAMAS 2024 | [2302.10809](https://arxiv.org/abs/2302.10809) | 不假设固定因果结构；反事实世界模拟；HEADD数据集 |
| 12 | [[triex-multi-agent-llm-explanation]] — TriEx 三视角 | 2026 | ACL 2026 | [2604.20043](https://arxiv.org/abs/2604.20043) | 三视角（自我推理/信念/预言机）；揭示说/信/做不匹配 |
| 13 | [[counterfactual-mas-explanation]] — AXIS 反事实 | 2025 | arXiv | [2505.17801](https://arxiv.org/abs/2505.17801) | LLM盘问模拟器；正确性+7.7%；目标预测+23% |
| 14 | [[policy-explanations-marl]] — MARL 策略解释 | 2022 | IJCAI 2022 | [2204.12568](https://arxiv.org/abs/2204.12568) | 策略摘要+语言解释；用户研究验证 |

## 新增趋势洞察

### 五条关键趋势

1. **从被动阅读到交互验证**（[[hansel-web-agent-verification]]）— 验证不是读日志而是导航证据。HANSEL 将验证重构为交互活动，不可追溯时显式标记缺口，而非生成可能不忠实的解释。

2. **从自我解释到外部验证**（[[triex-multi-agent-llm-explanation]], [[responsible-explainable-ai-agents]]）— TriEx 揭示 agent 说什么/信什么/做什么的系统性不匹配，挑战依赖 LLM 自我解释的方法。共识架构通过跨模型比较提供外部验证。

3. **从结果解释到过程溯源**（[[agent-traces-to-trust]], [[causal-past-logic-runtime-verification]]）— 过程级问责要求类型化图+运行时验证。CPL 将验证嵌入协调语言本身，而非事后检查日志。

4. **因果解释适用性扩大**（SCM→CEMA→AXIS）— 从固定因果结构到仅需前向模拟到 LLM 盘问模拟器。[[causal-explanations-sequential-uncertainty]]→[[cema-causal-explanations-mas]]→[[counterfactual-mas-explanation]] 展示适用性逐步扩大。

5. **问责 = 不可篡改记录 + 可审计理据 + 责任执行** — [[blockchain-accountability-agents]]（区块链）+ [[responsible-explainable-ai-agents]]（共识治理）+ [[argument-is-the-explanation]]（可验证论证）三路径互补。

### 引文核查教训

**LLM 编造引用的标志性手法**：
- arXiv ID 真实但指向完全不相关论文（图论/编码论）
- 标题在 arXiv 全检索 0 命中，但标注知名 venue（CHI/NAACL/AAAI 等）
- 作者归属错误（将真实论文的第一作者替换为他人）

**防护措施**：arXiv ID 直查 + 标题全文检索 + 作者核验三重核查，拒绝将未验证论文入库。

### 新增概念（10 个）

- [[AgentExplainability]] — Agent 可解释性（更新，+14 sources，T1-T4 四主线展开）
- [[ExecutionProvenance]] — 执行溯源与证据追踪
- [[StakeholderExplainability]] — 利益相关者分层解释
- [[CausalExplanation]] — 因果解释
- [[StructuredArgumentation]] — 结构化论证解释
- [[MultiAgentExplainability]] — 多智能体可解释性
- [[AgentAccountability]] — Agent 问责架构
- [[ConsensusDrivenReasoning]] — 共识驱动推理
- [[ExplainablePlanning]] — 可解释规划（Phase A）
- [[LLMAutonomousAgent]] — LLM 自主智能体（Phase A）

## 跨方向收敛

| 共享主题 | T1 信息转换可观测性 | T2 双受众分层 | T3 闭环验证溯因 | T4 多智能体解释 |
|---|---|---|---|---|
| **过程级 vs 结果级** | 执行溯源 typed graph | 三层框架分层交付 | 论证图每步可验证 | TriEx 三视角对齐 |
| **交互式验证** | HANSEL 证据导航 | LLM 对话式解释 | 论证测试时反馈 | AXIS LLM 盘问模拟器 |
| **因果/反事实** | CPL 因果可见性 | - | SCM 因果解释 | CEMA/AXIS 反事实 |
| **信任校准** | 过程级问责 | 利益相关者差异化 | 区块链+共识治理 | TRiSM 五支柱 |
| **幻觉检测** | 不可追溯标记缺口 | - | 论证事实节点攻击 | TriEx 说/信/做不匹配 |

## 知识库状态

| 指标 | 数值 |
|------|------|
| 论文总数 | 104 |
| wiki 页面 | 192 |
| 概念页面 | 43 |
| PDF 文件 | 103 |
| Health 检查 | 0 empty, 0 sync issues |

## 下一步

- S2 citation_count 持续 429（无 API key），14 篇 + AgentVerse 引用数待补
- 考虑对 Phase B 论文做深度 PDF 全文分析（当前基于摘要+arXiv metadata）
- 可扩展方向：Agent 可解释性 × 电信自智网络闭环（连接 [[closed-loop-explainability-telecom-autonomous-networks]]）
