---
title: "Overview"
type: synthesis
tags: []
sources: [28556-j00, 28312-j50, 28622-k20, 28912-j00, 28914-j00, evo-memory, agent-memory-survey, lightmem, emem, intpro, intent-signal-theory, vitabench2, intent-communication-design, intentrl, pira-bench, pask, memcog, memgym, apex-mem, h-mem, enpmr-bench, minteval, intentgrasp, recap, personalalign, contextagent, intent-detection-llm, satori, neurosync, ask-before-plan, inner-thoughts, proactive-ai-implications, assistantx, etapp, noemmma, good-agent-alignment, pp-clarifier, cocot, debate, onepred, icebreaker, proutt, speakrl, target-proactive-dialogue, ocr-memory, memoryos, memp, agentkb, mempi, peam, evomembench, sii-piwm, knowu-bench, proagentbench, procodebench, pa-bridge, reward-driven-interaction]
last_updated: 2026-06-04
---

# Overview

## 5G Network Management: Policy and Intent

The wiki covers two complementary 3GPP management specifications for 5G networks:

- **TS 28.556** ([[PolicyMnS]]) — Policy-based management: "what action to take when condition occurs"
- **TS 28.312** ([[IntentDrivenMnS]]) — Intent-based management: "what outcome to achieve, without specifying how"

### Abstraction Hierarchy

The [[RulePolicyIntentRelation]] describes a progressive shift in management paradigm:

```
Rule (explicit logic) → Policy (condition+action) → Intent (declarative goal)
        "how"                          "how+what"                "what"
```

Policy ([[PolicyIOC]]) uses a simple **condition-action** model ([[PolicyContent]]). Intent ([[IntentIOC]]) uses a richer **ExpectationObject + ExpectationTarget + Context** model ([[IntentExpectation]]). Intent can be translated to policies for closed-loop automation, but the reverse is not true — policies cannot express abstract goals.

### Policy Management (TS 28.556)

A [[PolicyIOC]] instance has four mandatory attributes: policyPriority (LOW/Medium/High), policyStatus (ACTIVATED/DEACTIVATED), policyType, and policyContent. Lifecycle managed via generic provisioning MnS from [[TS28532]]. [[PolicyConflictDetection]] provides single-level conflict notification (notifyPolicyConflict).

### Intent Management (TS 28.312)

An [[IntentIOC]] instance carries intentExpectations, intentAdminState, intentPriority, intentReportControl, and advanced features (intentPreemptionCapability, implicitIntentIndex, intentUtilityFormulaRef). Intent lifecycle has six states: ACKNOWLEDGED → COMPLIANT → FULFILLED → DEGRADED (with SUSPENDED and FULFILLMENT_FAILED as alternate paths).

Intent expectations are categorized by user role:
- **Intent-CSC** — Communication Service Customer expresses service expectations
- **Intent-CSP** — Communication Service Provider expresses network expectations
- **Intent-NOP** — Network Operator expresses subnetwork expectations

Intent translation chains across roles: CSC→CSP→NOP→NEP.

### Conflict Handling Comparison

| Feature | Policy (TS 28.556) | Intent (TS 28.312) |
|---|---|---|
| Conflict levels | Single (policy vs policy) | Three (target, expectation, intent) |
| Resolution | Notification only | Preemption, recommendations, negotiation |
| Notification | notifyPolicyConflict | IntentReport with conflictReports |

### Intent Advanced Features

- **[[IntentNegotiation]]** — Pre-evaluation (feasibility check, exploration) and fulfilment phase (alternative outcomes, best possible outcome)
- **[[IntentUtilityFunction]]** — Mathematical preference expression (variables, weights, function, result) for quantitative solution selection
- **[[IntentReport]]** — Six report types: fulfilment, conflict, feasibility, exploration, negotiation, utility
- **[[IntentHandlingFunction]]** — Producer capability exposure (supported objects, targets, value ranges)

### Standards Context

Both specifications are part of the [[5GNetworkManagement]] family (TS 28.x series), produced by [[3GPP]] TSG SA5. They reuse generic provisioning MnS from [[TS28532]] and inherit from [[TopIOC]] defined in [[TS28622]].

### Foundation: Generic NRM (TS 28.622)

TS 28.622 provides the foundational [[NRM]] information model. The [[TopIOC]] is the root of the IOC inheritance hierarchy — all domain-specific IOCs (Policy, Intent, IntentReport, IntentHandlingFunction) inherit from it via TopX (mandatory objectClass + objectInstance attributes). Key foundation IOCs include SubNetwork, ManagedElement, ManagedFunction, NtfSubscriptionControl, and common data types (GeoArea, TimeWindow, SchedulingTime).

### Study Reports: TR 28.912 (Rel-18) and TR 28.914 (Rel-19)

- **TR 28.912** (Rel-18): Studied intent-driven RAN energy saving, three-level conflict classification, 5GC expectations, [[IntentReport]] IOC, closed-loop composition, [[IntentHandlingFunction]], [[IntentSONOrchestration]], [[IntentMDA]], AI/ML capability mapping
- **TR 28.914** (Rel-19): Studied enhanced radio service/network expectations, implicit intent report, intent degradation, [[IntentUtilityFunction]], [[IntentNegotiation]] during fulfilment, intent exploration, feasibility check, network maintenance intent, vendor extension guidelines

---

## AI Agent Research: Memory, Understanding, and Recommendation

The wiki now covers three interconnected sub-areas in AI Agent research, all published 2025-2026:

### Agent Memory ([[AgentMemory]])

LLM agent memory has evolved from passive trajectory storage to active experience abstraction:

```
Storage (trajectory preservation) → Reflection (trajectory refinement) → Experience (trajectory abstraction)
          "save history"                    "summarize/compress"               "abstract/transfer knowledge"
```

Three core drivers: **long-range consistency**, **dynamic environments**, **continual learning** ([[wiki/sources/agent-memory-survey]]).

Key approaches:
- **[[EvoMemory]]** (2025, 71 citations) — first streaming benchmark for self-evolving memory; proposes ExpRAG (experience retrieval) and ReMem (action-think-memory refine) pipeline
- **[[wiki/sources/lightmem]]** (2026) — SLM-driven lightweight memory with STM/MTM/LTM three-tier; F1 +2.5 over A-MEM on LoCoMo, 83ms retrieval latency
- **[[wiki/sources/emem]]** (2026) — Episodic Context Reconstruction shifting from preprocessing to context preservation; master+assistant multi-agent; 54% F1 surpassing GAM by 7.75%, >70% token reduction

**Key challenge**: Memory preprocessing causes destructive de-contextualization — compressing sequential dependencies into static structures severs contextual integrity ([[wiki/sources/emem]]).

### Intent Understanding ([[IntentUnderstanding]])

Intent understanding has shifted from static recognition to dynamic, context-aware, personalized reasoning:

- **[[IntentSignalTheory]]** (2026) — formalizes four distinct objects: I* (latent intent), I-hat (observable proxy), P (encoded carrier), O (model output). **Irreversible Intent Loss theorem**: private intent absent from carrier cannot be recovered beyond generic substitution
- **[[wiki/sources/intpro]]** (2026) — proxy agent with retrieval-conditioned inference; per-user intent history library; SFT + GRPO training
- **[[wiki/sources/vitabench2]]** (2026) — benchmark revealing substantial gap between SOTA and practical personalization
- Intent Communication Design (2025) — Transparency × Abstraction × Modality design space

**Key challenge**: Latent source intent (I*) is often absent from the observable prompt (P), creating an irrecoverable information gap ([[IntentSignalTheory]]).

### Intent Recommendation ([[IntentRecommendation]])

The paradigm has shifted from reactive (explicit instruction required) to proactive (agent anticipates needs):

```
Reactive Agent (wait for instruction) → Proactive Agent (detect & recommend intent)
        "tell me what to do"                  "I understand what you need"
```

Key approaches:
- **[[wiki/sources/intentrl]]** (2026, 4 citations) — RL-trained proactive intent clarification before deep research; shallow-to-deep refinement graph + two-stage RL
- **[[PIRABench]]** (2026, 3 citations) — first proactive intent recommendation benchmark on GUI; proposes [[PIRF]] memory-aware state-tracking framework
- **[[wiki/sources/pask]]** (2026, 2 citations) — DD-MM-PAS paradigm (Demand Detection → Memory Modeling → Proactive Agent System); [[IntentFlow]] matching Gemini3-Flash under latency constraints

**Key challenge**: Real-world intent is fragmented and interleaved across multiple threads — agents must disambiguate noise from actionable events while maintaining preference-aware recommendations ([[PIRABench]]).

### Cross-direction Convergence

All three sub-areas converge on three shared themes:

| Shared Theme | Agent Memory | Intent Understanding | Intent Recommendation |
|---|---|---|---|
| **Long-term memory** | STM/MTM/LTM (LightMem), episodic (E-mem) | Per-user intent history (IntPro) | Hybrid memory (PASK), state-tracking (PIRF) |
| **User profile modeling** | Multi-user memory (LightMem) | Context-aware personalization (IntPro, VitaBench2) | Preference-aware detection (PIRA-Bench, PASK) |
| **Proactivity** | Proactive exploration (survey), ReMem pipeline | Proactive info acquisition (VitaBench2) | Proactive intent clarification (IntentRL), recommendation (PIRA-Bench, PASK) |

This convergence reflects AI agents evolving from "tools" to "personalized partners" that remember, understand, and anticipate user needs.

### Expanded Landscape (Second Round Ingest)

#### Agent Memory — 6 New Papers

Six papers expand the evaluation landscape beyond the initial LoCoMo-centric benchmarks:

- **MemCog** (2026) — paradigm shift from memory-as-tool (passive retrieval) to memory-as-cognition (active cognitive memory)
- **MemGym** (2026) — long-horizon memory evaluation environment, pushing beyond single-session benchmarks
- **APEX-MEM** (2026) — semi-structured memory representation combined with temporal reasoning for conversational agents
- **H-Mem** (2026) — hybrid representation (facts + summaries + profiles) for evolving memory across time
- **ENPMR-Bench** (2026) — benchmarking proactive memory retrieval specifically for emotional support agents
- **MINTEval** (2026) — evaluating memory degradation under concurrent goal interference (multi-target scenarios)

**Key trend**: Evaluation diversity explosion — from LoCoMo-only to specialized benchmarks covering emotional support, multi-target interference, long-horizon environments, and temporal reasoning.

#### Intent Understanding — 7 New Papers

Seven papers push intent understanding from text-only classification to multimodal rewriting and direct manipulation:

- **IntentGrasp** (2026) — comprehensive 12-domain benchmark (49 corpora) revealing severe LLM deficits in intent understanding; proposes IFT fine-tuning
- **RECAP** (2025) — intent rewriting benchmark for agent planning — shifting from detection to reformulation
- **PersonalAlign** (ACL 2026) — hierarchical implicit intent alignment for GUI agents; HIM-Agent achieves +15.7% execution, +7.3% proactive
- **ContextAgent** (2025, 41 citations) — wearable sensory context for proactive LLM agents — sensory-aware proactivity
- **Intent Detection in the Age of LLMs** (EMNLP 2024, 41 citations) — classic hybrid routing framework for intent detection
- **Satori** (2024) — BDI user modeling + multi-modal LLM for proactive AR guidance — intent understanding in augmented reality
- **NeuroSync** (UIST 2025) — direct intent-task manipulation paradigm — bypassing intermediate representations

**Key trend**: Intent understanding expands from text-only to multimodal (sensory, AR, GUI) and from classification to rewriting/manipulation. The I*→P gap identified in [[IntentSignalTheory]] now has concrete intervention strategies.

#### Intent Recommendation — 5 New Papers

Five papers introduce clarification-first planning and reveal human factors risks:

- **Ask-before-Plan** (EMNLP 2024, 12 citations) — CEP multi-agent framework: clarification-before-execution paradigm
- **Inner Thoughts** (2025) — covert thought training framework for proactive conversational agents
- **Proactive AI Implications** (BISE 2025, 22 citations) — human factors research: proactive AI help can reduce user competence self-esteem
- **AssistantX** (IROS 2025) — 4-agent proactive framework deployed in real-world office environment
- **ETAPP** (ACL 2025) — benchmark evaluating personalization+proactivity trade-offs in tool-augmented LLMs

**Key trend**: Human factors research reveals proactive AI can reduce user competence — proactivity must be balanced with autonomy. The clarification-first approach (Ask-before-Plan) and covert thought mechanism (Inner Thoughts) offer concrete design patterns for responsible proactivity.

### Expanded Landscape (Third Round Ingest)

#### Intent Understanding — 5 New Papers

五篇论文将意图理解推向神经符号融合、形式化对齐、多模态消歧和语音模态：

- **NOEM³A** (2025) — 神符号本体增强多意图消歧框架；Retrieval-Augmented Prompting + Logit Biasing + 分类头三层注入；SIS 评测指标；3B Llama → 85% vs GPT-4 90%
- **GOOD** (2025) — 将 Assistance Games 扩展到开放对话场景的 OU-AGs 框架；GOOD 方法从对话提取并排序候选目标；LLM 模拟用户概率推断；三领域评测
- **Plug-and-Play Clarifier** (AAAI 2026) — 三模块零样本多模态意图消歧框架（文本/视觉/跨模态澄清器）；4-8B 小模型 +30% 意图澄清性能
- **CoCoT** (2025) — 认知 grounded 三阶段推理（Perception→Situation→Norm）；SFT 后模型内化推理模式无需显式提示；多任务平均 +5-6%
- **DEBATE** (2025) — 首个中文语音-文本消歧数据集（1001×10说话人）；揭示机器与人类口语意图理解的巨大差距

**关键趋势**: 意图消歧从单一文本模态扩展到多模态（视觉、语音、指示手势）与神经符号融合。消歧策略的模块化设计（PP-Clarifier）和认知结构化推理（CoCoT）代表两种互补路径。[[IntentSignalTheory]] 的 I*→P 信息损失现在有了更丰富的补偿机制。

#### Intent Recommendation — 5 New Papers

五篇论文引入递归意图记忆、冷启动开场、意图树建模、RL 澄清和场景建模：

- **OnePred** (2026) — 递归意图记忆作为跨轮上下文；两阶段 RL 管线（先教预测→再教压缩）；token 消耗降低 22×；NQP-Bench 基准
- **IceBreaker** (ACL 2026 Industry) — 定义对话开场语生成新任务（零意图冷启动）；两步握手框架（共振感知兴趣蒸馏+交互导向生成）；CTR +9.425%
- **ProUtt** (2026) — 意图树建模对话历史；exploitation+exploration 双视角推理轨迹；扰动修正构造偏好数据；4 基准评测
- **SpeakRL** (2025) — RL 增强主动澄清意图能力；奖励"问对的澄清问题"；SpeakER 合成数据集；任务完成率 +20.14%
- **Target-Guided Proactive Dialogue** (2026) — 会话场景建模（用户画像+领域知识）+ 意图关键词桥接；主动性与信息性显著改善

**关键趋势**: 意图推荐从"检测已有意图"演进到"生成未来意图"（OnePred 预测下一查询、IceBreaker 生成开场语、ProUtt 预测下一 utterance）。递归意图记忆（[[RecursiveIntentMemory]]）和意图树建模（[[IntentTreeModeling]]）代表从扁平序列到层次结构的关键转变。RL 训练主动澄清（SpeakRL）与 [[wiki/sources/intentrl]] 的两阶段 RL 形成呼应。

#### Cross-direction Convergence (Updated)

| 共享主题 | Agent Memory | Intent Understanding | Intent Recommendation |
|---|---|---|---|
| **层次化记忆结构** | STM/MTM/LTM (LightMem), episodic (E-mem) | Ontology 层次 (NOEM³A), 递归意图 (IntentSignalTheory) | 递归意图记忆 (OnePred), 意图树 (ProUtt) |
| **符号结构注入** | 语义结构 (APEX-MEM), 事实+摘要+画像 (H-Mem) | 神符号本体 (NOEM³A), 认知结构 (CoCoT) | 意图树 (ProUtt), 场景建模 (Target-Guided) |
| **小模型效率** | SLM 驱动 (LightMem) | 3B Llama + Ontology (NOEM³A), 4-8B + PP-Clarifier | 递归记忆压缩 22× (OnePred) |
| **主动生成** | 主动探索 (survey), ReMem | 主动信息获取 (VitaBench2) | 开场语生成 (IceBreaker), 下一查询预测 (OnePred), RL 澄清 (SpeakRL) |

### Expanded Landscape (Fourth Round Ingest)

#### Agent Memory — 7 New Papers

七篇论文将Agent记忆推向视觉编码、参数化内化、程序性记忆、跨框架共享、自适应生成和系统化评测：

- **OCR-Memory** (ACL 2026) — 视觉模态作为高密度记忆表示；将轨迹渲染为带视觉锚点的图像；locate-and-transcribe检索范式避免自由生成和幻觉
- **MemoryOS** (2025, 64 citations) — OS启发的STM/MTM/LTM三级存储系统；FIFO对话链+分段页面组织策略；LoCoMo F1+49.11%
- **Memp** (ACL 2026 Findings, 38 citations) — 程序性记忆探索；细粒度步骤指令+脚本抽象两种蒸馏形式；跨模型迁移（强→弱仍有增益）
- **Agent KB** (2025, 53 citations) — 跨框架共享记忆基础设施；planning seeds+feedback fixes两阶段检索；disagreement gate防知识干扰；+18.7pp GAIA
- **Mem-π** (2026) — 自适应记忆：从检索到生成的范式转换；决策-内容解耦RL决定何时+生成什么指导；>30%相对提升
- **PEAM** (2026) — 参数化具身记忆：MoE-LoRA物理隔离适配器；失败-纠正轨迹对比内化；parameterization-worthiness score+自触发整合
- **EvoMemBench** (2026) — 自演化记忆评测：记忆范围×内容双轴；15方法对比；发现长上下文基线仍竞争力强、无单一记忆形式通用有效

**关键趋势**: Agent记忆从"外部存储检索"演进到"参数化内化"和"按需生成"两种新范式。程序性记忆（Memp）和参数驻留技能（PEAM）代表记忆从被动存储到主动技能的转变。视觉编码（OCR-Memory）开辟了文本之外的高密度信息通道。跨框架共享（Agent KB）从单Agent记忆扩展到集体智能。

#### Intent Understanding — 3 New Papers

三篇论文将意图理解推向主动干预决策、偏好获取和满意度驱动：

- **SII/PIWM** (2026) — See-Infer-Intervene三阶段框架；AIDA购买阶段+BDI心理场双重状态表示；五类响应（包括"等待"）；发现video-to-state grounding是部署瓶颈
- **KnowU-Bench** (2026) — 交互式+主动性+个性化移动Agent评测；偏好获取+同意协商+拒绝后克制；Claude Sonnet 4.6在模糊指令下<50%
- **Reward-Driven Interaction** (2025) — 用户满意度作为内在奖励信号驱动主动澄清；对比自监督+领域意图分类辅助任务；DuerOS工业验证

**关键趋势**: 意图理解从"推断意图"深化到"决定是否干预"——SII引入"等待"选项，KnowU-Bench评测同意协商和拒绝后克制。这是[[IntentSignalTheory]]的I*→P信息损失的新回应：不仅推断意图，还要决定是否、如何、何时干预。

#### Intent Recommendation — 4 New Papers

四篇论文引入真实世界评测、编程场景主动意图和回声室打破：

- **ProAgentBench** (2026) — 真实世界主动Agent评测基准；28K+事件/500+小时真实数据；时机预测+辅助内容生成两阶段分解
- **ProCodeBench** (2026) — 1,246位工业开发者IDE交互数据；发现模拟vs真实轨迹的系统性差距；模拟评估高估真实性能
- **PA-Bridge** (SIGIR 2026) — 打破对话开场语推荐的回声室效应；对抗分布对齐弥合被动与主动表达差距；语义离散器去偏
- **Reward-Driven Interaction** (已在IU中归档) — 满意度预测作为奖励触发主动澄清

**关键趋势**: 意图推荐评测从合成数据转向真实世界数据——ProAgentBench和ProCodeBench都发现合成数据高估真实性能。PA-Bridge从推荐角度打破[[ConversationStarterGeneration]]（IceBreaker）的开场语质量问题——回声室效应使推荐偏向泛化建议。

#### Cross-direction Convergence (Updated Round 4)

| 共享主题 | Agent Memory | Intent Understanding | Intent Recommendation |
|---|---|---|---|
| **参数化 vs 检索** | 参数驻留技能 (PEAM), 按需生成 (Mem-π) | 用户满意度内化为奖励 (Reward-Driven) | 时机预测内化为习惯 (ProAgentBench) |
| **真实 vs 合成** | 合成轨迹 ≠ 真实行为 (EvoMemBench) | 模拟画像 ≠ 真实偏好 (KnowU-Bench) | 合成数据高估真实性能 (ProAgentBench, ProCodeBench) |
| **跨框架共享** | Agent KB 集体智能 | KnowU-Bench 多Agent同意协商 | PA-Bridge 跨来源意图桥接 |
| **视觉/多模态** | 视觉编码 (OCR-Memory) | 视频推断 (SII/PIWM) | IDE+仓库上下文 (ProCodeBench) |

### Connection to 3GPP Intent Management

The 3GPP [[IntentDrivenMnS]] concept (declarative goal expression) and the AI Agent intent research share the same foundational principle: **expressing "what" rather than "how"**. The [[RulePolicyIntentRelation]] hierarchy (Rule→Policy→Intent) in telecom parallels the Agent evolution (Reactive→Context-Aware→Proactive). Both domains formalize intent as a higher abstraction layer that enables autonomous goal pursuit.