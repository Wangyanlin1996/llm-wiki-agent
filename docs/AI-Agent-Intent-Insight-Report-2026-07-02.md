# Agent 闭环可解释性 — 论文洞察日报

**日期**: 2026-07-02
**累计论文**: 122 篇（本轮新增 18 篇：Round 8 Agent 闭环可解释性）
**知识库页面**: 216 页

## 概览

| 方向 | 累计 | 本轮新增 |
|------|------|---------|
| Agent Memory | 20 | 0 |
| Intent Understanding | 23 | 0 |
| Intent Recommendation | 19 | 0 |
| Memory-Enhanced Intent Clarification | 6 | 0 |
| Agent Explainability | 36 | 18 |

## 本轮重点：AgentLoop 框架 6 方向空白填补

Round 7（2026-06-29）引文核查发现用户提供的 15 篇论文中 11 篇为幻觉（73%），Phase B 补入 14 篇真实论文建立 T1-T4 四主线。本轮（Round 8）聚焦 **AgentLoop 框架兼容性**，通过 arXiv 5 路布尔检索（95 候选→去重→排除已入库→筛选 18 篇），按 6 方向精准填补 synthesis 报告识别的两大空白：

1. **方向 2 空白**：LLM 编排 vs 经典 HTN/PDDL — 由 VADAOrchestra（LLM+Datalog+/- 解耦）填补
2. **方向 5 空白**：机器可读凭证标准化 — 由 6 篇论文（PCAA/AgentBound/KYA/AuthGraph/AgentRiskBOM/RedAct）构成全生命周期凭证栈填补

### T1 信息转换可观测性 / 轨迹取证（3 篇）

| # | 论文 | 年份 | Venue | arXiv | 核心贡献 |
|---|------|------|-------|-------|---------|
| 1 | [[forensic-trajectory-signatures]] — 记忆投毒轨迹取证签名 | 2026 | arXiv | [2606.07938](https://arxiv.org/abs/2606.07938) | 行为不变量签名（memory_recall_fact→email_send_email）；AUC 0.9904；前缀仅变体 AUC 0.934 支持实时阻断 |
| 2 | [[agent-tom-monitoring]] — 心智理论推理监控 | 2026 | arXiv | [2606.16654](https://arxiv.org/abs/2606.16654) | Reason-Verify-Refine 管线；持久语义护栏记忆跨 episode 复用；两调用超越 SOTA 集成 |
| 3 | [[swe-agent-mindset]] — SWE Agent 涌现心智投影 | 2026 | arXiv | [2606.15943](https://arxiv.org/abs/2606.15943) | 导航/证据/综合/接地/停止五观察透镜；408 轨迹跨模型/仓库；不臆测隐藏意图 |

### T2 Skill/Tool 选择可解释性（3 篇）

| # | 论文 | 年份 | Venue | arXiv | 核心贡献 |
|---|------|------|-------|-------|---------|
| 4 | [[looking-not-picking]] — 工具选择失败的注意力段解释 | 2026 | arXiv | [2606.06551](https://arxiv.org/abs/2606.06551) | 反驳"拥挤脚手架"直觉：80% 注意到正确工具却选错；读出侧干预恢复 59-91% vs 提示修复 ≤23% |
| 5 | [[skillcat]] — 对比评估与拓扑感知 Skill 自演化 | 2026 | arXiv | [2606.04522](https://arxiv.org/abs/2606.04522) | 对比因果提取+补丁合并前验证+拓扑感知路由；+40.40% |
| 6 | [[vadaorchestra]] — 神经符号自适应推理编排 | 2026 | KR 2026 | [2606.18690](https://arxiv.org/abs/2606.18690) | LLM 编排+Datalog+/- 符号引擎解耦；可验证推理轨迹；**填补方向 2 空白** |

### T3 闭环验证与溯因（4 篇）

| # | 论文 | 年份 | Venue | arXiv | 核心贡献 |
|---|------|------|-------|-------|---------|
| 7 | [[grounded-continuation]] — LLM 对话线性时间运行时验证器 | 2026 | arXiv | [2606.09334](https://arxiv.org/abs/2606.09334) | 依赖图+四形式主义（DEL/溯因/意识/论证）8 更新操作；形式化无冲突保证；撤回微秒级 |
| 8 | [[verification-horizon]] — 编码 Agent 奖励的验证地平线 | 2026 | arXiv | [2606.14845](https://arxiv.org/abs/2606.14845) | "验证比生成更难"逆转；可扩展性×忠实度×鲁棒性三重困境；验证须与生成器协同演化——**挑战方向 3 假设** |
| 9 | [[raider-robot]] — 机器人动作问题检测/解释/恢复 | 2025 | arXiv | [2512.04749](https://arxiv.org/abs/2512.04749) | Ground-Ask&Answer-Issue 完整闭环；解释增强恢复成功率——**少数覆盖 AgentLoop 完整闭环** |
| 10 | [[causalab]] — 面向 AI 科学家的可扩展交互因果发现 | 2026 | arXiv | [2606.15417](https://arxiv.org/abs/2606.15417) | SCM 采样因果发现；92% 任务准确率 vs 0.471 全边 F1；预测成功≠因果理解 |

### T4 人机交互 / 可争议性（2 篇）

| # | 论文 | 年份 | Venue | arXiv | 核心贡献 |
|---|------|------|-------|-------|---------|
| 11 | [[contestability-layer]] — 可争议性层 | 2026 | arXiv | [2606.12568](https://arxiv.org/abs/2606.12568) | 可废止规则+显式冲突/优先级；诊断→修订闭环；控制器级可争议性 |
| 12 | [[intent-centric-se]] — 意图为中心软件工程 | 2026 | arXiv | [2606.10204](https://arxiv.org/abs/2606.10204) | 反思性主题分析；代码为中心→意图为中心；意图规格化+验证+溯源+治理——**与 3GPP IntentDrivenMnS 跨域呼应** |

### T5 机器可读凭证 / 溯源治理（6 篇）— 填补最大空白

| # | 论文 | 年份 | Venue | arXiv | 核心贡献 |
|---|------|------|-------|-------|---------|
| 13 | [[proof-carrying-agent]] — 携证 Agent 动作 | 2026 | arXiv | [2606.10839](https://arxiv.org/abs/2606.10839) | 动作证书+5 检查点；外部性感知；显式 enforceability classes——**桥接 PROV-O 与 IntentReport** |
| 14 | [[agentbound]] — 可验证行为治理 | 2026 | arXiv | [2606.15772](https://arxiv.org/abs/2606.15772) | 三权威保守组合（委托×宪章×契约）；密码学可验证治理回执；常设委托 |
| 15 | [[kya-trust-layer]] — 框架无关信任层 | 2026 | arXiv | [2606.12478](https://arxiv.org/abs/2606.12478) | 5 原语；15+ 框架适配；only-tighten 组合代数；亚毫秒 p99；检测 89% 对抗探测 |
| 16 | [[provenance-authorization]] — 溯源授权双图防御 | 2026 | arXiv | [2606.12391](https://arxiv.org/abs/2606.12391) | 注入推理图 vs 授权图双图对齐；信息论不可注入基线；40%→1% 攻击成功率 |
| 17 | [[agentriskbom]] — Agent 风险范围安全 BOM | 2026 | IEEE Cyber-AI 2026 | [2606.11513](https://arxiv.org/abs/2606.11513) | JSON-schema BOM；16 能力维度 14 分 vs SBOM 1 分；差异检测 33 种部署变异 |
| 18 | [[redact-traces]] — 能力轨迹脱敏 | 2026 | arXiv | [2606.10378](https://arxiv.org/abs/2606.10378) | 轨迹脱敏+行为水印；NST 44.7-67.1%→基线下；水印 93.6-100% 检测——**揭示问责-隐私张力** |

## 新增趋势洞察

### 五条关键趋势

1. **从信任到验证**（T5 六篇）— 治理范式从"必须被信任的过程"转为"可独立验证的过程"。动作证书（PCAA）、治理回执（AgentBound）、信任评分（KYA）、双图对齐（AuthGraph）、能力 BOM（AgentRiskBOM）、行为水印（RedAct）构成全生命周期凭证栈。这直接填补 synthesis 报告 [[closed-loop-explainability-telecom-autonomous-networks]] 识别的"无电信标准定义解释序列化"最大空白。

2. **LLM 编排可解释性的解耦范式**（[[vadaorchestra]]）— LLM 灵活规划 + 符号可验证执行，超越"经典 HTN/PDDL vs 纯 LLM"二元对立。Datalog+/- 引擎按需构造合成，推理轨迹可形式化验证——填补 synthesis 方向 2 空白。

3. **验证地平线逆转**（[[verification-horizon]]）— "验证比生成容易"的经典直觉在编码 agent 领域已逆转。验证须与生成器协同演化，不可作为廉价环节——挑战 AgentLoop 方向 3"验证廉价"假设。

4. **轨迹作为安全接口**（[[forensic-trajectory-signatures]], [[redact-traces]]）— 轨迹既是问责证据又是技能泄露载体，催生"选择性脱敏+行为水印"的轨迹治理新范式。Forensic Signatures 证明行为不变量可实时阻断投毒，RedAct 揭示问责与隐私的结构性张力。

5. **意图为中心问责**（[[intent-centric-se]] + [[contestability-layer]]）— 问责基线从动作层上移到意图规格化层，与 3GPP [[IntentDrivenMnS]] "what vs how" 跨域共鸣。可废止规则提供争议解决机制，将"解释"从被动交付转为主动可争议。

### 新增概念（6 个）

- [[RuntimeGovernance]] — 运行时治理：从外部审计到嵌入式治理（PCAA/AgentBound/KYA/AuthGraph）
- [[TrajectoryForensics]] — 轨迹取证：行为不变量签名作为安全接口
- [[NeurosymbolicOrchestration]] — 神经符号编排：LLM 灵活+符号可验证解耦范式
- [[VerificationCoEvolution]] — 验证协同演化：验证须与生成器同步演化
- [[PolicyContestability]] — 策略可争议性：可废止规则+诊断修订闭环
- [[IntentCentricAccountability]] — 意图为中心问责：从动作问责到意图规格化问责

## 跨方向收敛

| 共享主题 | T1 轨迹取证 | T2 Skill 编排 | T3 闭环验证 | T5 机器可读凭证 |
|---|---|---|---|---|
| **行为不变量** | 分布式签名 (Forensic) | 读出瓶颈 (Looking) | 依赖图 (Grounded) | 动作证书 (PCAA) |
| **神经+符号** | ToM 推理 (Agent-ToM) | LLM+Datalog (VADAOrchestra) | SCM 因果 (CausaLab) | 逻辑规则凭证 (AgentBound) |
| **闭环完整性** | 监控→检测 | 选择→评估 | 检测→解释→恢复 (RAIDER) | 授权→执行→回执 |
| **意图对齐** | 意图假设 (Agent-ToM) | 任务相关节点 (SkillCAT) | 意图代理 vs 意图 (Verification Horizon) | 授权图源自意图 (AuthGraph) |
| **隐私 vs 问责** | - | - | - | 脱敏+水印 (RedAct) |

## 与电信自智网络的跨域共鸣

本轮 3 个关键发现与 3GPP 意图管理标准形成跨域呼应：

- **[[intent-centric-se]] ↔ [[IntentDrivenMnS]]** — 软件工程从"代码为中心"到"意图为中心"的转变，与 3GPP TS 28.312 从"策略（condition+action）"到"意图（declarative goal）"的抽象层级提升完全同构。两者都表达"what"而非"how"。
- **[[proof-carrying-agent]] ↔ [[IntentReport]]** — PCAA 的动作证书+5 检查点机制，为 3GPP IntentReport 的六类报告（fulfilment/conflict/feasibility/exploration/negotiation/utility）提供了工程化的凭证序列化构件。
- **[[contestability-layer]] ↔ [[IntentNegotiation]]** — 可废止规则+诊断修订闭环，为 3GPP 意图协商（预评估+履约阶段）提供了形式化的争议解决机制。

## 知识库状态

| 指标 | 数值 |
|------|------|
| 论文总数 | 122 |
| wiki 页面 | 216 |
| 概念页面 | 81 |
| PDF 文件 | 121 |
| Health 检查 | 0 empty, 0 sync issues |

## 下一步

- S2 citation_count 持续 429（无 API key），18 篇引用数待补
- 考虑对 T5 六篇凭证论文做深度 PDF 全文分析，提取可工程化的凭证 schema
- 可扩展方向：将 T5 凭证栈映射到 3GPP IntentReport IOC，形成电信场景的闭环可解释性实施蓝图
