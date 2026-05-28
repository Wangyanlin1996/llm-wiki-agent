# Wiki 索引

本文件由 LLM 维护，每次 ingest 时更新。

## 概览
- [概览](overview.md) — 跨所有来源的持续综合

## 来源
- [3GPP TS 28.556 V19.0.0 — 5G 网络策略管理（Stage 2 & 3）](sources/28556-j00.md) — Policy MnS Stage 2 & 3 规范
- [3GPP TS 28.312 V19.5.0 — 移动网络意图驱动管理服务](sources/28312-j50.md) — Intent Driven MnS (IDMS) 概念、需求、Stage 2/3
- [3GPP TS 28.622 V20.2.0 — 通用 NRM IRP 信息服务（IS）](sources/28622-k20.md) — 基础 NRM，包含 Top IOC、SubNetwork、ManagedElement 及通用数据类型
- [3GPP TR 28.912 V19.0.0 — Intent Driven MnS 研究（Rel-18）](sources/28912-j00.md) — 研究报告：节能、冲突、5GC、SON、MDA、AI/ML 映射
- [3GPP TR 28.914 V19.0.0 — Intent Driven MnS 研究（Rel-19）](sources/28914-j00.md) — 研究报告：探索、协商、效用、降级、维护
- [Agent Memory Survey](sources/agent-memory-survey.md) — Agent 记忆机制综述
- [EMEM](sources/emem.md) — 经验记忆增强模型
- [Evo-Memory](sources/evo-memory.md) — 演化式记忆架构
- [Intent Communication Design](sources/intent-communication-design.md) — 意图通信设计方案
- [Intent Signal Theory](sources/intent-signal-theory.md) — 意图信号理论
- [IntentRL](sources/intentrl.md) — 基于 Intent 的强化学习框架
- [IntPro](sources/intpro.md) — Intent Profile 优化方法
- [LightMem](sources/lightmem.md) — 轻量级记忆架构
- [PASK](sources/pask.md) — 参数化主动知识检索
- [PIRA-Bench](sources/pira-bench.md) — 意图推理评估基准
- [VitaBench2](sources/vitabench2.md) — 垂直领域意图评估基准

## 实体
- [3GPP](entities/3GPP.md) — 协作电信标准化组织（7 个组织伙伴）

## 概念
- [Policy MnS](concepts/PolicyMnS.md) — 3GPP 5G 策略管理服务：生命周期管理与冲突检测
- [Policy IOC](concepts/PolicyIOC.md) — 表示网络策略的信息对象类（4 个必选属性）
- [PolicyContent](concepts/PolicyContent.md) — 条件-动作 dataType，策略逻辑核心
- [策略冲突检测](concepts/PolicyConflictDetection.md) — 检测并通知冲突策略的机制
- [Intent Driven MnS](concepts/IntentDrivenMnS.md) — 3GPP 意图驱动管理服务 (IDMS) — 声明式目标管理
- [Intent IOC](concepts/IntentIOC.md) — 意图表达的信息对象类：期望、状态、优先级
- [IntentExpectation](concepts/IntentExpectation.md) — 表达对象+目标+上下文期望的 DataType
- [Intent Report](concepts/IntentReport.md) — 六类意图报告信息的 IOC（满足、冲突、可行性等）
- [Intent Handling Function](concepts/IntentHandlingFunction.md) — 暴露 Producer 意图处理能力的 IOC
- [意图冲突解决](concepts/IntentConflictResolution.md) — 三级冲突检测（目标、期望、意图）与抢占机制
- [意图协商](concepts/IntentNegotiation.md) — 预评估与满足阶段的协商流程
- [Intent Utility Function](concepts/IntentUtilityFunction.md) — 定量满足评估的数学偏好表达
- [规则-策略-意图关系](concepts/RulePolicyIntentRelation.md) — 从"怎么做"（规则）到"要什么"（意图）的抽象层级
- [5G 网络管理](concepts/5GNetworkManagement.md) — 3GPP TS 28.x 管理与编排规范族
- [TS 28.532](concepts/TS28532.md) — 通用管理服务（Provisioning MnS）基础
- [TS 28.622](concepts/TS28622.md) — 通用 NRM IRP 信息服务 — 基础 IOC 层次与数据类型
- [Top IOC](concepts/TopIOC.md) — 所有 FNIM 合规规范的根 IOC（Top_ + TopX）
- [NRM](concepts/NRM.md) — 网络资源模型概念 — 表示被管理网络资源的 IOC 集合
- [意图驱动 SON 编排](concepts/IntentSONOrchestration.md) — 由意图期望驱动的 SON 功能，含 3 种意图类型
- [意图驱动 MDA](concepts/IntentMDA.md) — 通过能力匹配由意图期望触发的 MDA 分析
- [Agent 记忆](concepts/AgentMemory.md) — LLM Agent 记忆机制分类与设计
- [意图推荐](concepts/IntentRecommendation.md) — 基于 Intent 的推荐方法
- [意图理解](concepts/IntentUnderstanding.md) — Intent 理解与解析方法

## 综合
- [术语对照表](glossary.md) — 英文术语与中文对照，确保翻译一致性