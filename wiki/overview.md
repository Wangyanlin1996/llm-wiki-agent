---
title: "Overview"
type: synthesis
tags: []
sources: [28556-j00, 28312-j50, 28622-k20, 28912-j00, 28914-j00, evo-memory, agent-memory-survey, lightmem, emem, intpro, intent-signal-theory, vitabench2, intent-communication-design, intentrl, pira-bench, pask, memcog, memgym, apex-mem, h-mem, enpmr-bench, minteval, intentgrasp, recap, personalalign, contextagent, intent-detection-llm, satori, neurosync, ask-before-plan, inner-thoughts, proactive-ai-implications, assistantx, etapp, noemmma, good-agent-alignment, pp-clarifier, cocot, debate, onepred, icebreaker, proutt, speakrl, target-proactive-dialogue, ocr-memory, memoryos, memp, agentkb, mempi, peam, evomembench, sii-piwm, knowu-bench, proagentbench, procodebench, pa-bridge, reward-driven-interaction, amem, scrapmem, stale, promem, memory-autonomous-agents-survey, userharness, intentvlm, guide-bench, coinbench, tomcat, bayesian-social-deduction, psi-bench, fingertip-20k, propersim, ds-ia-framework, recgpt-mobile, cfqp, rac, corpus-rag-clarifying, cops, janus, sensitivity-aware-clarification, fairy-gui-agent, llm-autonomous-agent-survey, agentbench, agentverse, explainable-human-ai-interaction, agent-traces-to-trust, hansel-web-agent-verification, causal-past-logic-runtime-verification, three-level-llm-xai, explainable-ai-to-whom, responsible-explainable-ai-agents, blockchain-accountability-agents, argument-is-the-explanation, causal-explanations-sequential-uncertainty, trism-agentic-ai, cema-causal-explanations-mas, triex-multi-agent-llm-explanation, counterfactual-mas-explanation, policy-explanations-marl, forensic-trajectory-signatures, agent-tom-monitoring, swe-agent-mindset, looking-not-picking, skillcat, vadaorchestra, grounded-continuation, verification-horizon, raider-robot, causalab, contestability-layer, intent-centric-se, proof-carrying-agent, agentbound, kya-trust-layer, provenance-authorization, agentriskbom, redact-traces, cog-rag, coact-action-preserving-compression, smoothagent-lookahead-context, latent-context-compilation, cross-family-speculative-prefill, mia-signature-activation, prism-intent-memory-retrieval, apex-dynamic-data-selection, prompt-codebooks-pco, spear-code-augmented-prompt, mo-capo-multi-objective, maspo-joint-mas-prompt, prism-prompt-reliability, saga-workflow-scheduling, dynamo-asset-orchestration, co-coder-task-partitioning, agent-jit-compilation, typego-os-runtime, model-native-architecture, saecache-semantic-eviction, leyline-kv-directives, tokendance-collective-sharing, prism-scheduling-memory, stateful-inference-multi-agent, kv-policy-learning-evict, vericache-lossless-compression, hydra-dynamic-routing, inframind-infra-aware, routing-plateau, recal-reward-calibration, twinrouterbench-step-routing, goodserve-goodput-serving]
last_updated: 2026-08-03
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

### Expanded Landscape (Fifth Round Ingest)

#### Agent Memory — 5 New Papers

五篇论文将Agent记忆推向遗忘机制、主动提取、自主组织和全面综述：

- **A-MEM** (NeurIPS 2025) — Zettelkasten式自主记忆系统：动态索引+双向链接+记忆演化，6基础模型超越SOTA
- **ScrapMem** (2026) — 生物启发光学遗忘：渐进降分辨率压缩旧记忆+EM-Graph因果时序；93%存储节省；SOTA 51.0%
- **STALE** (2026) — 首次系统研究记忆过期：隐式冲突（无显式否定的失效）；CUPMem状态裁决；400场景；最佳仅55.2%
- **ProMem** (2026) — 主动记忆提取替代静态摘要：自问迭代反馈循环；提升完整性和QA准确率
- **Memory for Autonomous LLM Agents Survey** (2026) — write-manage-read循环形式化；3D分类；5机制族；2022-2026全覆盖

**关键趋势**: Agent记忆从"如何组织存储"演进到"如何遗忘"和"如何主动提取"两个新维度。遗忘不再是被动的上下文溢出而是主动的选择性过期（STALE, ScrapMem）。提取不再是盲目的前馈压缩而是带反馈的迭代认知过程（ProMem）。A-MEM的Zettelkasten互联网络与[[AgentMemory]]的Storage→Reflection→Experience层次结构形成方法论对比。

#### Intent Understanding — 6 New Papers

六篇论文将意图理解推向心智重建、视频语言、集体意图和社交推理：

- **UserHarness** (2026) — ToM→用户心智重建：跟踪观察→信念→意图→行动链；95.94% macro accuracy，+15%超越现有推理
- **IntentVLM** (2026) — 视频语言前逆建模两阶段意图识别；SOTA 80%；达到人类水平
- **GUIDE** (CVPR 2026) — GUI意图检测评测基准：67.5h/120用户/10软件；用户上下文+50.2pp帮助预测
- **COINBench** (2026) — 首个集体意图理解基准：群体共识/矛盾/趋势推断；COIN-TREE层次认知结构
- **Tomcat/Instruction Inference** (2025) — 人-Agent协作ToM推理；52人类对照；Fs-CoT达人类水平
- **Bayesian Social Deduction** (ACL 2026) — 贝叶斯+LLM混合社交推理；首个Agent击败人类（67%胜率）

**关键趋势**: 意图理解从"推断行为意图"深化到"重建心理状态链"（UserHarness）和"推断群体共识"（COINBench）。[[IntentSignalTheory]]的I*→P信息损失现在有了三种新回应：心智重建（UserHarness）、概率信念推断（Bayesian Social Deduction）、共享上下文推理（Tomcat）。视频语言（IntentVLM）和GUI（GUIDE）开辟了文本之外的两个新通道。

#### Intent Recommendation — 6 New Papers

六篇论文将意图推荐推向主动影响、主动+个性化联合和意图安全验证：

- **Ψ-Bench** (2026) — 主动个性化影响评测：角色敏感说服；+18.24%有画像
- **FingerTip 20K** (ICLR 2026) — 20K真实人类演示；主动任务建议+个性化执行轨迹
- **ProPerSim** (ICLR 2026) — 主动+个性化联合仿真；ProPerAssistant持续学习适应；32画像
- **DS-IA Framework** (2026) — 双阶段意图感知：语义防火墙+确定性级联验证器；解决交互频率困境
- **RecGPT-Mobile** (KDD 2026) — 端侧LLM意图理解Agent；淘宝实时推荐验证
- **CFQP** (2025) — 协同过滤下一问题预测：个性化记忆+图偏好传播

**关键趋势**: 意图推荐从"检测已有意图"演进到"主动影响意图"（Ψ-Bench）和"联合主动+个性化"（ProPerSim, FingerTip 20K）。DS-IA引入"主动拒绝"维度：不仅推荐还要验证意图的可行性。端侧部署（RecGPT-Mobile）和协同过滤（CFQP）代表了IR的两个工程方向。

#### Cross-direction Convergence (Updated Round 5)

| 共享主题 | Agent Memory | Intent Understanding | Intent Recommendation |
|---|---|---|---|
| **遗忘/过期** | 光学遗忘 (ScrapMem), 隐式冲突 (STALE), 学习遗忘 (survey) | 记忆过期影响意图推断 (STALE) | 主动拒绝过期意图 (DS-IA) |
| **主动提取 vs 被动存储** | 主动提取 (ProMem), 按需生成 (Mem-π) | 主动信息获取 (UserHarness, Tomcat) | 主动影响 (Ψ-Bench), 主动+个性化 (ProPerSim) |
| **心理状态重建** | 用户画像构建 (ScrapMem EM-Graph) | 心智重建 (UserHarness), 贝叶斯信念推断 (Bayesian) | 用户画像驱动 (Ψ-Bench +18.24%) |
| **群体 vs 个体** | 跨框架共享 (Agent KB) | 集体意图 (COINBench) | 协同过滤 (CFQP), 多画像适应 (ProPerSim) |
| **视觉/多模态** | 光学遗忘 (ScrapMem), 视觉编码 (OCR-Memory) | 视频意图 (IntentVLM), GUI意图 (GUIDE) | 移动端真实演示 (FingerTip 20K) |

The 3GPP [[IntentDrivenMnS]] concept (declarative goal expression) and the AI Agent intent research share the same foundational principle: **expressing "what" rather than "how"**. The [[RulePolicyIntentRelation]] hierarchy (Rule→Policy→Intent) in telecom parallels the Agent evolution (Reactive→Context-Aware→Proactive). Both domains formalize intent as a higher abstraction layer that enables autonomous goal pursuit.

---

### Expanded Landscape (Sixth Round Ingest)

#### Memory-Enhanced Intent Clarification — 6 New Papers

六篇论文开辟了"记忆增强模糊意图澄清"这一交叉方向，展示三种互补路径：

**路径一：检索增强澄清（RAG as external memory）**
- **RAC** (ECIR 2026) — RAG 生成语料锚定的澄清问题；对比偏好优化偏向有证据支撑的问题；4 基准显著超越基线。核心洞察：澄清问题必须锚定在可用语料中，否则系统会问出无法回答的问题。
- **Corpus-informed RAG** (2024) — RAG 联合建模 query+corpus 端到端定位不确定性；发现现有数据集的意图-语料不对齐问题并提出数据增强方案。
- **Sensitivity-Aware RA** (ECIR 2026 Workshop) — 在敏感域（医疗/政府/法律）中限制检索范围；攻击模型+检索级防御+保护-效用权衡。

**路径二：认知记忆驱动意图理解（Cognitive memory as internal context）**
- **CoPS** (WWW 2024) — 认知三阶记忆（感觉/工作/长期）驱动个性化搜索意图；从历史交互构建用户画像排序查询意图；零样本超越基线。
- **JANUS** (2026) — 持久记忆三层（近期缓冲+核心记忆+归档检索）+ 内部言语触发澄清；从欠明确请求恢复；POMDP 形式化；HRI 场景验证。

**路径三：演化记忆 + 目标精炼（Evolutionary memory + goal refinement）**
- **Fairy** (2025) — Runtime Goal Refinement（知识约束精炼+人在环澄清）+ Evolutionary Memory Architecture（执行-演化双循环）；模糊任务基准 RealMobile-Eval +33.7%；50 页系统设计。

**关键趋势**: "记忆增强模糊意图澄清"形成三种互补范式——外部检索（RAC/Corpus-RAG/Sensitivity-Aware）、内部认知记忆（CoPS/JANUS）、演化记忆+目标精炼（Fairy）。三条路径的共同洞察是：**模糊意图的歧义源于上下文缺失，记忆提供缺失的上下文来消解歧义或在不足时触发有针对性的澄清**。这与 [[IntentSignalTheory]] 的 I*→P 信息损失定理呼应——记忆是补偿信息损失的关键机制。

#### Cross-direction Convergence (Updated Round 6)

| 共享主题 | Agent Memory | Intent Understanding | Memory-Enhanced Clarification |
|---|---|---|---|
| **认知层次化记忆** | STM/MTM/LTM (LightMem), episodic (E-mem) | 用户画像记忆 (IntPro) | 认知三阶 (CoPS), 持久三层 (JANUS) |
| **检索作为记忆** | ExpRAG (Evo-Memory), Agent KB | 检索增强推断 (IntPro) | RAG 澄清 (RAC, Corpus-RAG, Sensitivity-Aware) |
| **记忆演化** | 按需生成 (Mem-π), 主动提取 (ProMem) | 递归意图 (OnePred) | 执行-演化双循环 (Fairy EMA) |
| **澄清触发机制** | - | EVPI (SAGE-Agent), intent-sim (Clarify-When-Necessary) | 内部言语 (JANUS), 人在环 (Fairy RGR) |

---

### Expanded Landscape (Seventh Round Ingest)

#### Agent Explainability — 4 Verified Papers (引文核查批次)

本轮为"引文核查批次"：用户提供 15 篇支撑"Agent 闭环可解释性"框架的论文，经 arXiv ID 直查 + 标题检索核查，**11 篇为幻觉（73%）**，仅 4 篇真实存在并入库。本批引入知识库新方向"Agent 可解释性"。

**核查要点**：两个"arXiv ID"指向完全不相关论文（2504.01485→图论；2405.18023→编码论），是 LLM 编造引用的标志性手法；另有 9 篇标题在 arXiv 全检索 0 命中。已拒绝将幻觉论文入库，避免污染知识库与制造虚假 wikilink。

**入库 4 篇**：
- **LLM Autonomous Agent Survey** (Frontiers of CS 2024, 3137 citations) — 提出感知-规划-记忆-工具统一架构，明确将"解释"列为 agent 可信度核心维度，呼吁覆盖全生命周期的解释框架。是本方向的理论背书。
- **AgentBench** (ICLR 2024, 951 citations) — 8 环境多维评测基准，实证 agent 行为多阶段性，单步解释不足以诊断长程推理失败。支撑"解释必须沿信息转换节点展开"。
- **AgentVerse** (ICLR 2024) — 动态重组多智能体协作，揭示社会行为涌现；论证群体决策源头追溯需对"中间决策"做可解释性记录。支撑"跨域协商需要解释凭证"。
- **Explainable Human-AI Interaction: A Planning Perspective** (Morgan & Claypool 2024, Sreedharan/Kulkarni/Kambhampati) — 唯一直接命中主题的强相关项。提出"解释即规划"范式：agent 须考虑回路中人类心智模型，解释性通信可顺应或改变人类期望。直接支撑方向四"交互式解释/意图共创"。

**关键趋势**: 真实文献集中于"agent 行为多阶段性→解释须沿信息转换节点展开"与"心智模型对齐→解释即规划"两条主线。用户框架中的"双受众分层解释""闭环溯因形式化保障""机器可读凭证"等核心方向的支撑文献在本批几乎全为幻觉——需在 Phase B 用 academic-search 检索真实替代论文补充（主题：Agent可解释性框架 / 双受众分层 / 闭环溯因 / 多智能体解释）。

#### Cross-direction Convergence (Updated Round 7)

| 共享主题 | Agent Explainability | Agent Memory | Intent Understanding |
|---|---|---|---|
| **多阶段行为需多阶段解释** | AgentBench 多阶段评测, AgentVerse 中间决策追溯 | 长程记忆支撑长程解释 | 多步意图推断需过程级解释 |
| **心智模型对齐** | Sreedharan 心智模型顺应/改变 | 用户画像即心智模型快照 | UserHarness 心智重建 |
| **解释作为可信度维度** | Survey 将解释列为核心维度 | 记忆可审计性 | 意图透明度 (intent-communication-design) |
| **解释即规划** | Sreedharan 范式 | - | 意图共创可视为规划问题 |

#### Agent Explainability — Phase B: 14 Replacement Papers (真实替代论文)

Phase A 核查发现用户提供的 15 篇论文中 11 篇为幻觉（73%），四个框架方向（T1 信息转换可观测性 / T2 双受众分层解释 / T3 闭环验证溯因 / T4 多智能体解释）的支撑文献几乎全为编造。Phase B 通过 arXiv API 按四主题布尔检索，找到 14 篇真实近期论文填补空缺，全部下载 PDF 并入库。

**T1 信息转换可观测性（3 篇）**：
- **From Agent Traces to Trust** (2026) — 综述系统定义执行溯源（typed graph）与证据追踪（evidence-support projection），统一检索接地/声明支撑/工具安全/记忆谱系/可观测性/调试/审计/恢复为过程级问责框架
- **HANSEL** (2026) — 将验证从被动阅读重构为交互式证据导航；83.7% precision/88.8% recall；轨迹体积-61.6%；不可追溯时显式标记缺口
- **Causal Past Logic** (2026) — 分布式 LLM agent 运行时验证；CPL 守卫嵌入协调语言本身，向量时钟监控器证明本地值=指称语义

**T2 双受众分层解释（2 篇）**：
- **Three-Level Framework for LLM-Enhanced XAI** (Information Systems Frontiers 2025) — 三层框架（算法/领域→以人为中心→社会）；LLM 担任跨层中介，将技术输出转化为情境叙述
- **Explainable AI, but explainable to whom?** (2021) — 经验基础：COVID-19 ICU 案例揭示"利益相关者星座"（开发/专家/决策者/受众）差异化解释需求

**T3 闭环验证溯因（4 篇）**：
- **Responsible and Explainable AI Agents** (2025) — 多模型共识架构：异构 LLM/VLM 独立生成→分歧暴露→推理 agent 结构化整合；可解释性=跨模型比较+保留中间输出
- **Blockchain Accountability** (2024) — 区块链防篡改黑箱 + LLM 从问责数据生成解释；ROS 移动机器人三场景验证
- **The Argument is the Explanation** (2025) — 结构化论证图；每步推理可验证；Bipolar ABA 实现自动幻觉检测；AAEC 94.44 F1 (+5.7)
- **Causal Explanations for Sequential Decision Making Under Uncertainty** (2022) — SCM 因果解释基础；单一框架识别多个语义不同解释；MDP 因果推理精确+近似方法

**T4 多智能体解释（5 篇）**：
- **TRiSM for Agentic AI** (2025) — AMAS 信任/风险/安全管理综述；TRiSM 五支柱适配；CSS+TUE 新指标；风险分类法
- **CEMA** (AAMAS 2024) — 不假设固定因果结构；反事实世界模拟识别显著原因；HEADD 数据集；用户研究验证信任提升
- **TriEx** (ACL 2026) — 三视角（自我推理/信念状态/预言机审计）；揭示 agent 说什么/信什么/做什么的系统性不匹配
- **AXIS** (2025) — LLM 用"whatif"/"remove"盘问模拟器生成反事实解释；正确性+7.7%；目标预测+23%
- **Policy Explanations for MARL** (IJCAI 2022) — MARL 策略解释基础；策略摘要+语言解释；用户研究验证

**关键趋势**：
1. **从被动阅读到交互验证**（HANSEL）— 验证不是读日志而是导航证据
2. **从自我解释到外部验证**（TriEx, 共识架构）— LLM 自我叙述不可信，需跨模型比较或三视角审计
3. **从结果解释到过程溯源**（执行溯源综述, CPL）— 过程级问责要求类型化图+运行时验证
4. **因果解释的适用性扩大**（SCM→CEMA→AXIS）— 从固定结构到仅需前向模拟到 LLM 盘问
5. **问责 = 不可篡改记录 + 可审计理据 + 责任执行**（区块链+共识+论证三路径互补）

#### Cross-direction Convergence (Updated Round 7 Phase B)

| 共享主题 | T1 信息转换可观测性 | T2 双受众分层 | T3 闭环验证溯因 | T4 多智能体解释 |
|---|---|---|---|---|
| **过程级 vs 结果级** | 执行溯源 typed graph | 三层框架分层交付 | 论证图每步可验证 | TriEx 三视角对齐 |
| **交互式验证** | HANSEL 证据导航 | LLM 对话式解释 | 论证测试时反馈 | AXIS LLM 盘问模拟器 |
| **因果/反事实** | CPL 因果可见性 | - | SCM 因果解释 | CEMA/AXIS 反事实 |
| **信任校准** | 过程级问责 | 利益相关者差异化 | 区块链+共识治理 | TRiSM 五支柱 |
| **幻觉检测** | 不可追溯标记缺口 | - | 论证事实节点攻击 | TriEx 说/信/做不匹配 |

### Expanded Landscape (Eighth Round Ingest)

#### Agent Closed-Loop Interpretability — 18 New Papers

本轮聚焦"智能体闭环可解释性 + AgentLoop 框架兼容"，18 篇论文按 AgentLoop 6 方向填补 Round 7 识别的空白（特别是方向2 LLM 编排 vs 经典 HTN/PDDL、方向5 机器可读凭证标准化空白）。

**T1 信息转换可观测性 / 轨迹取证（3 篇）**：
- **Forensic Trajectory Signatures** (2026) — 发现记忆投毒的行为不变量（memory_recall_fact 必先于 email_send_email）；AUC 0.9904；签名过确定（移除半数特征 AUC 不变）；前缀仅变体 AUC 0.934 支持实时阻断；记忆攻击 vs 提示注入可区分
- **Agent-ToM** (2026) — 心智理论推理监控隐蔽恶意行为；Reason-Verify-Refine 管线；持久语义护栏记忆跨 episode 复用信念/意图条件化约束；两调用即超越 SOTA 集成
- **SWE Agent Mindset** (2026) — 观察透镜投影 think-action 链；导航/证据选择/综合/接地/停止五透镜；408 轨迹跨模型/仓库；不臆测隐藏意图

**T2 Skill/Tool 选择可解释性（3 篇）**：
- **Looking Is Not Picking** (2026) — 反驳"拥挤脚手架"直觉：80% 时间注意到正确工具却选错；失败在读出而非感知；读出侧干预恢复 59-91% vs 提示修复 ≤23%；免训练选择器 +11.9 分
- **SkillCAT** (2026) — 对比因果提取（成功/失败对）+评估增强演化（补丁合并前验证）+拓扑感知路由（仅加载相关节点）；+40.40%
- **VADAOrchestra** (KR 2026) — LLM 编排+Datalog+/- 符号引擎解耦；可验证推理轨迹；按需逻辑构造合成——**填补 synthesis 方向2"LLM 编排 vs HTN/PDDL"空白**

**T3 闭环验证与溯因（4 篇）**：
- **Grounded Continuation** (2026) — 依赖图+四形式主义（DEL/溯因/意识/论证）8 更新操作；线性时间；形式化无冲突保证；撤回微秒级
- **Verification Horizon** (2026) — "验证比生成更难"逆转趋势；可扩展性×忠实度×鲁棒性三重困境；验证须与生成器协同演化——**挑战方向3"验证廉价"假设**
- **RAIDER** (2025) — Ground-Ask&Answer-Issue 流程；检测→解释→恢复完整闭环；解释增强恢复成功率——**少数覆盖 AgentLoop 完整闭环**
- **CausaLab** (2026) — SCM 采样因果发现；92% 任务准确率 vs 0.471 全边 F1；预测成功≠因果理解；过早停止为主要弱点

**T4 人机交互 / 可争议性（2 篇）**：
- **Machine-Coached Policy Revision** (2026) — 可废止规则+显式冲突/优先级；诊断→修订闭环；控制器级可争议性
- **Intent-Centric SE** (2026) — 反思性主题分析；代码为中心→意图为中心；意图规格化+验证+溯源+治理问责——**与 3GPP IntentDrivenMnS "what vs how" 跨域呼应**

**T5 机器可读凭证 / 溯源治理（6 篇）**——填补 synthesis 识别的"最大空白"：
- **Proof-Carrying Agent Actions** (2026) — 动作证书+5 检查点（可准入/开启/假设/批准/闭环）；外部性感知；显式 enforceability classes——**桥接 PROV-O 与 IntentReport 的工程构件**
- **AgentBound** (2026) — 三权威保守组合（委托授权×行为宪章×动作契约）；密码学可验证治理回执；常设委托
- **KYA** (2026) — 5 原语框架无关信任层；15+ 框架适配；only-tighten 组合代数；亚毫秒 p99；检测 89% 对抗探测
- **AuthGraph** (2026) — 注入推理图 vs 授权图双图对齐；参数源级检测；信息论不可注入基线；40%→1% 攻击成功率
- **AgentRiskBOM** (IEEE Cyber-AI 2026) — Agent 安全 BOM（JSON-schema）；16 能力维度 14 分 vs SBOM 1 分；差异检测 33 种部署变异
- **RedAct** (2026) — 轨迹脱敏+行为水印；NST 44.7-67.1%→基线下；审计证据保留；水印 93.6-100% 检测——**揭示问责-隐私张力**

**关键趋势**：
1. **从信任到验证**（T5 六篇）— 治理从"必须被信任的过程"转为"可独立验证的过程"：动作证书/治理回执/信任评分/双图对齐/BOM/水印构成全生命周期凭证栈。这直接填补 synthesis 报告识别的"无电信标准定义解释序列化"最大空白
2. **LLM 编排可解释性的解耦范式**（VADAOrchestra）— LLM 灵活规划+符号可验证执行，超越"经典 HTN/PDDL vs 纯 LLM"二元对立
3. **验证地平线逆转**（Verification Horizon）— "验证比生成容易"的经典直觉在编码 agent 领域已逆转；验证须与生成器协同演化，不可作为廉价环节
4. **轨迹作为安全接口**（Forensic Signatures, RedAct）— 轨迹既是问责证据又是技能泄露载体，催生"选择性脱敏+行为水印"的轨迹治理
5. **意图为中心问责**（Intent-Centric SE + Contestability）— 问责基线从动作上移到意图规格化，与 3GPP IntentDrivenMnS 跨域共鸣

#### Cross-direction Convergence (Updated Round 8)

| 共享主题 | T1 轨迹取证 | T2 Skill 编排 | T3 闭环验证 | T5 机器可读凭证 |
|---|---|---|---|---|
| **行为不变量** | 分布式签名 (Forensic) | 读出瓶颈 (Looking) | 依赖图 (Grounded) | 动作证书 (PCAA) |
| **神经+符号** | ToM 推理 (Agent-ToM) | LLM+Datalog (VADAOrchestra) | SCM 因果 (CausaLab) | 逻辑规则凭证 (AgentBound) |
| **闭环完整性** | 监控→检测 | 选择→评估 | 检测→解释→恢复 (RAIDER) | 授权→执行→回执 |
| **意图对齐** | 意图假设 (Agent-ToM) | 任务相关节点 (SkillCAT) | 意图代理 vs 意图 (Verification Horizon) | 授权图源自意图 (AuthGraph) |
| **隐私 vs 问责** | - | - | - | 脱敏+水印 (RedAct) |

---

## 第9轮：语义检索全景（2024-2026）— 26篇论文 × 7子方向

第9轮聚焦语义检索（Semantic Retrieval）领域，覆盖7个子方向共26篇论文（2024-2026），构建从基础检索到Agent驱动的完整技术图谱。

### 跨方向趋势

| 子方向 | 核心范式演进 | 关键论文 |
|---|---|---|
| **T1 稠密检索** | 双编码器→自回归建模→约束感知 | [[dream-dense-retrieval]]、[[scaling-dense-retrieval]]、[[coder-constraint-retrieval]] |
| **T2 RAG架构** | ICL→RAG→GraphRAG→CausalRAG | [[rag-comprehensive-survey]]、[[beyond-parameters-survey]]、[[rag-security-privacy]] |
| **T3 混合检索** | 稀疏+稠密融合；BM25在特定领域仍占优 | [[telco-orag]]、[[bm25-corrective-rag]]、[[hakari-bench]] |
| **T4 嵌入模型** | 对比学习→生成式嵌入→软提示解耦 | [[teleembedbench]]、[[llm2vec-gen]]、[[promptembedder]] |
| **T5 检索评估** | nDCG/Recall@k→统计估计→冗余感知 | [[coverage-not-averages]]、[[rare-redundancy-eval]]、[[rag-evaluation-survey]] |
| **T6 GraphRAG** | 文档建图→可解释子图检索→本体引导→主题对齐双超图 | [[is-graphrag-needed]]、[[ex-graphrag]]、[[omd-graphrag]]、[[cog-rag]] |
| **T7 Agent驱动检索** | System 1预定义管线→System 2自主编排 | [[reasoning-agentic-rag-survey]]、[[r2-searcher]]、[[metaresearcher]] |

### 与现有Wiki的连接

- **电信场景填补**：三篇电信专用论文（[[telco-orag]]、[[teleembedbench]]、[[armor-telecom-retriever]]）直接针对3GPP/O-RAN，填补了wiki最大的场景空白
- **AgentLoop框架对应**：[[AgenticRetrieval]]与现有综合[[closed-loop-explainability-telecom-autonomous-networks]]中定义的AgentLoop框架（用户意图→编排器→Skill执行→结果整合→闭环验证）直接对应——检索是Skill执行的核心环节
- **神经符号编排呼应**：[[GraphRAG]]与[[NeurosymbolicOrchestration]]呼应——LLM灵活规划+符号可验证执行
- **评估维度扩展**：[[RetrievalEvaluation]]为wiki的[[VerificationCoEvolution]]三重困境（可扩展×忠实×鲁棒）提供了检索侧的评估方法论

### 关键洞察

1. **检索-生成差距**（[[is-graphrag-needed]]）：扩展检索不比例提升生成质量——GraphRAG的价值在于多跳推理而非单跳事实查询
2. **BM25的持久生命力**（[[bm25-corrective-rag]]）：在金融/法律等高术语密度领域，BM25仍超越SOTA稠密检索——混合检索是工程最优解
3. **System 1 vs System 2**（[[reasoning-agentic-rag-survey]]）：Agentic RAG正从预定义推理管线向自主工具编排演进，与AgentLoop框架的Skill编排层直接对应
4. **评估的形式化**（[[coverage-not-averages]]）：检索评估从经验平均指标走向统计估计理论——这与电信网络中SLA可验证性的思路一致
5. **结构对齐优于扩展检索**（[[cog-rag]]）：Cog-RAG 用主题超图+实体超图双结构+认知两阶段检索，从全局主题到局部细节实现语义对齐——部分修正洞察2"扩展检索无益"的结论：在检索-生成差距中，**对齐**比**扩展**是更有效的杠杆。消融亦揭示主题超图在跨域稀疏开放场景引入噪声，提示全局主题组织需动态过滤

---

## 第10轮：本体应用在人机交互问答与任务执行（2021-2026）— 28篇论文 × 5维度

第10轮聚焦"本体应用在计算机/AI领域，尤其是人机交互问答场景和任务执行场景"，覆盖2021-2026年共28篇论文，按用户要求的5个维度（本体建模、用户输入实体抽取、实体链接、本体推理、任务完成）进行精读分析。这是wiki首次系统性覆盖本体（Ontology）在HCI中的应用方向。

### 跨方向趋势

| 子方向 | 核心范式演进 | 关键论文 |
|---|---|---|
| **A. 本体驱动KGQA** | 固定本体约束→动态本体构建→多维立方体 | [[opi-ontology-kgqa]]、[[oracle-ontology-multihop]]、[[multicube-rag-multihop-qa]] |
| **B. 本体在TOD** | 固定slot-value本体→描述驱动schema→无本体/开放词汇 | [[opal-ontology-aware-tod]]、[[d3st-description-driven-tod]]、[[beyond-ontology-dst]] |
| **C. 本体任务执行** | 动作本体规划→统一任务/动作/环境/能力本体→分层超图 | [[husky-language-agent]]、[[ontobot-robotics-ontology]]、[[hear-hypergraph-enterprise]] |
| **D. 对话流管理** | 话题本体对话管理→社交规范本体 | [[knowledge-grounded-dialogue-flow]]、[[socialdial-socially-aware]] |
| **E. 综述** | 不一致KG推理三方向；LLM-KG协同四方向 | [[inconsistency-kg-reasoning-survey]]、[[llm-kg-research-trends]] |

### 五维分析核心发现

#### 本体建模（Ontology Modeling）
本体建模经历了从"静态预定义"到"动态自动构建"的范式转变。传统方法依赖领域专家预定义本体（如 [[ontology-enhanced-slot-filling]] 的 MultiWOZ slot-value 列表），而新方法让 LLM 根据任务自动构建：[[oracle-ontology-multihop]] 为每个问题动态构建特定本体，[[teqodo-tod-ontology]] 用 SQL 能力从零构建 TOD 本体，[[lom-large-ontology-model]] 融合结构化数据库和非结构化文本构建双层企业本体。关键创新还有关系中心本体图（[[opi-ontology-kgqa]]）、正交多维本体立方体（[[multicube-rag-multihop-qa]]）、分层超图本体（[[hear-hypergraph-enterprise]]）。

#### 用户输入实体抽取（Entity Extraction）
实体抽取从"基于本体的 slot filling"演进到"QA 式抽取"和"LLM 直接推断"。[[ontology-enhanced-slot-filling]] 用本体匹配跨轮命名实体；[[d3st-description-driven-tod]] 将 DST 重新表述为基于 schema 描述的问题回答；[[zero-shot-open-vocab-dst]] 和 [[beyond-ontology-dst]] 让 LLM 直接从对话推断状态，不依赖固定本体。在 KGQA 中，[[ort-ontology-reverse-kgqa]] 提取目的标签和条件标签作为逆向推理起点。

#### 实体链接（Entity Linking）
实体链接方法呈现多元化：本体约束匹配（[[ontology-enhanced-slot-filling]]）、嵌入规范化（[[neuro-symbolic-kg-ontology]]）、双重角色交叉验证（[[vlk-rl-cross-domain-tod]]）、SPARQL 查询（[[kg-gap-overlap-benchmark]]）、图执行器遍历（[[titan-graph-reasoning-cti]]）。核心张力是"可靠约束 vs 开放泛化"——固定本体提供可靠链接但限制新实体，开放词汇提供灵活性但牺牲一致性。

#### 本体推理（Ontology Reasoning）
推理方法涵盖双向路径推理（[[opi-ontology-kgqa]]）、逆向思维推理（[[ort-ontology-reverse-kgqa]]）、一阶逻辑推理链（[[oracle-ontology-multihop]]）、维度分解-征服（[[multicube-rag-multihop-qa]]）、知识模块组合（[[kml-procedural-video-qa]]）、路径规划+图执行（[[titan-graph-reasoning-cti]]）、证据驱动推理循环（[[hear-hypergraph-enterprise]]）。神经符号分离是共同主题——LLM 负责灵活规划，符号引擎负责确定性执行。

#### 任务完成（Task Completion）
任务完成维度覆盖从 DST 到企业推理的完整谱系。关键发现：正摩擦提升任务成功率（[[positive-friction-dialogue]]）、约束感知状态提升长程行为（[[vlk-rl-cross-domain-tod]]）、统一动作本体使7B模型匹配GPT-4（[[husky-language-agent]]）、超图本体达94.7%企业推理准确率（[[hear-hypergraph-enterprise]]）。本体对任务完成的价值在于"结构化约束提升可靠性"——但好的本体设计（描述驱动、模块化）能兼顾约束和泛化。

### 与现有Wiki的连接

- **与3GPP意图管理呼应**：本体建模的"what vs how"抽象层次与 [[IntentDrivenMnS]] 的声明式目标表达跨域共鸣——本体定义"是什么"，推理引擎决定"怎么做"
- **与神经符号编排呼应**：[[NeuroSymbolicKGModule]] 与已有 [[NeurosymbolicOrchestration]]（VADAOrchestra）呼应——LLM灵活规划+符号可验证执行
- **与意图澄清互补**：[[PositiveFrictionOntology]] 从对话节奏角度补充了已有意图澄清策略（[[ConformalIntentClarification]]、[[BayesianDisambiguation]]）
- **与GraphRAG连接**：本体引导的KGQA（[[OntologyGuidedKGQA]]）与已有 [[GraphRAG]] 和 [[OMD-GraphRAG]]（本体引导提取）形成方法论互补

### 关键洞察

1. **本体从静态先验到动态推导**（[[DynamicOntologyConstruction]]）：LLM 使自动本体构建成为可能，降低本体工程成本，但需权衡自动构建的质量与专家本体的精确性
2. **固定vs开放本体的张力**（[[DialogueStateTrackingOntology]]）：从严格依赖固定本体（[[ontology-enhanced-slot-filling]]）到完全无本体（[[beyond-ontology-dst]]），谱系上的最优解可能是"描述驱动"（[[d3st-description-driven-tod]]）——保留本体约束但用自然语言描述增强泛化
3. **神经符号分离是推理可靠性关键**（[[NeuroSymbolicKGModule]]）：LLM负责"理解要查什么"，符号引擎负责"确定性地查"——这种分离确保了推理的灵活性和可验证性
4. **本体不只是约束，更是任务执行的结构化基础**（[[ActionOntologyAgent]]）：动作本体将agent行为空间结构化，使规划可分解、执行可委托、结果可验证
5. **正摩擦悖论**（[[PositiveFrictionOntology]]）：策略性减速反而提升任务成功率——挑战了"无摩擦=更好"的传统直觉

---

## 第11轮：LLM 推理与服务优化全景（2025-2026）— 31篇论文 × 5方向

第11轮聚焦"LLM 推理与服务优化"，覆盖 agent 系统优化的完整链路：从上下文管理到 prompt 优化，从执行调度到缓存复用，再到模型动态路由。31篇论文全部为 2025-2026 年最新工作，构建了从单 token 到集群级的全栈优化图谱。

### 跨方向趋势

| 方向 | 核心范式演进 | 关键论文 |
|---|---|---|
| **A. 上下文优化** | 文本压缩→动作保持→段可分解预计算→LoRA编译→跨族推测→激活签名 | [[coact-action-preserving-compression]]、[[smoothagent-lookahead-context]]、[[latent-context-compilation]] |
| **B. Prompt优化** | 全局字符串→动态数据分层→离散codebook→Agent式优化→多目标→持续可靠性 | [[apex-dynamic-data-selection]]、[[prompt-codebooks-pco]]、[[spear-code-augmented-prompt]] |
| **C. 执行调度** | 请求级→工作流级→图分区→JIT编译→OS式runtime→统一架构 | [[saga-workflow-scheduling]]、[[co-coder-task-partitioning]]、[[typego-os-runtime]] |
| **D. 缓存复用** | LRU均匀淘汰→语义感知→缓存编辑→集体共享→调度协同→有状态→RL策略→无损压缩 | [[saecache-semantic-eviction]]、[[leyline-kv-directives]]、[[tokendance-collective-sharing]] |
| **E. 模型路由** | 二元强/弱→多维能力匹配→基础设施感知→路由上限分析→RL校准→步级评估→goodput | [[hydra-dynamic-routing]]、[[inframind-infra-aware]]、[[routing-plateau]] |

### 五维分析核心发现

#### A. 上下文优化（Context Optimization）
上下文优化正从"压缩文本"转向"保持行为"。[[CoACT]] 提出 NAP 原则——衡量标准不是保留多少信息，而是 agent 后续行为是否一致。[[SmoothAgent]] 发现 context 变换的段可分解性，将问题从"压缩什么"转向"何时变换"。[[LatentContextCompilation]] 从"适应"转向"编译"——生成无状态、可移植的记忆制品。[[MiASignature]] 借鉴认知科学全局点火理论，用次模函数构建激活签名。[[PRISM-IntentMemoryRetrieval]] 将检索-压缩联合优化为图结构上的搜索问题。

**关键洞察**：上下文优化的核心矛盾是"信息保留 vs 行为保持 vs 计算成本"——三者不可同时最优，需根据场景权衡。

#### B. Prompt 优化（Prompt Optimization）
Prompt 优化正从"优化一个全局字符串"转向"per-instance 路由+多目标+持续监控"。[[APEX]] 打破静态数据集假设，动态分层采样。[[PromptCodebooks]] 将 prompt 重构为离散本能词汇表上的学习。[[SPEAR]] 将优化器本身 agent 化——自主编写 Python 做错误分析。[[MO-CAPO]] 引入部署导向成本目标。[[MASPO]] 用联合评估机制弥合局部与全局。[[PRISM-PromptReliability]] 将 prompt 工程转为持续可靠性工程——LLM 行为漂移是一等关切。

**关键洞察**：优化器自身从固定管线→agent 式自主决策；评估从一次性→持续监控；目标从单一性能→性能+成本+可靠性。

#### C. 执行调度优化（Execution Scheduling）
调度粒度正从"请求级"→"工作流级"→"程序级"。[[SAGA]] 将整个 agent 工作流视为可调度单元，预测跨工具调用边界的 KV 复用。[[CoCoder]] 将多 agent 编排形式化为图分区问题——通信-计算 tradeoff 是核心。[[TypeGo]] 将 LLM 移出关键路径——OS 式异步架构。[[ModelNativeArchitecture]] 提出统一架构框架——LLM=CPU、KV=cache、上下文=RAM、agent=OS 的类比提供设计语言。

**关键洞察**：OS 类比为 agent 系统设计提供了统一语言——缓存层次、调度公平性、资源仲裁等经典 OS 概念直接迁移。

#### D. 缓存复用（Cache Reuse）
缓存管理正从"LRU 均匀淘汰"→"语义感知+学习驱动"。[[SAECache]] 发现 token 类型复用率差异达 756x。[[Leyline]] 打破"缓存仅追加"假设——agent 需要主动编辑缓存。[[TokenDance]] 将共享从单 agent 内扩展到多 agent 间——集体复用+diff 压缩。[[StatefulInference]] 从 O(n_t) 转为 O(Δ_t) delta-only 推理。[[KVPolicy]] 用 RL 学习淘汰策略——per-head 专门化。[[VeriCache]] 用草拟-验证范式实现无损压缩。

**关键洞察**：agent 工作负载打破 chatbot 假设——缓存需要主动编辑（Leyline）、集体共享（TokenDance）、跨轮持久（StatefulInference）。

#### E. 模型动态路由（Model Dynamic Routing）
路由正从"二元强/弱"→"多维能力匹配+全栈感知"。[[HyDRA]] 预测四维能力需求与模型 profile shortfall 匹配。[[INFRAMIND]] 让整个多 agent 栈感知基础设施状态。[[RoutingPlateau]] 发现路由准确率存在 plateau——根因是可预测性瓶颈。[[TwinRouterBench]] 首次评估 agent 中间步骤的路由——one-shot 评估不够。

**关键洞察**：路由 plateau 的根因是路由器学习全局趋势而非实例特定信号——突破需要更大数据、更强编码器、端到端微调。

### 跨方向收敛

| 收敛主题 | 上下文优化 | 执行调度 | 缓存复用 | 模型路由 |
|---|---|---|---|---|
| **OS类比** | 段可分解预计算 (SmoothAgent) | OS式runtime (TypeGo), ICA架构 | 缓存=处理器缓存 (ICA) | - |
| **KV cache为中心** | 压缩为buffer token (LatentContext) | 工作流级KV复用预测 (SAGA) | 语义淘汰/编辑/共享/持久 | - |
| **行为保持vs信息压缩** | NAP原则 (CoACT) | - | 无损草拟-验证 (VeriCache) | 路由质量保持 (HyDRA) |
| **Agent工作负载特性** | observation累积 (CoACT) | 链式调用 (SAGA) | 85-95%重复 (StatefulInference) | 多步调用 (TwinRouterBench) |
| **学习驱动** | LoRA编译 (LatentContext) | - | RL淘汰 (KVPolicy), 在线学习 (SAECache) | RL路由 (ReCal) |

### 与现有Wiki的连接

- **与Agent Memory呼应**：上下文优化（[[ContextOptimization]]）与 Agent Memory（[[AgentMemory]]）共享"压缩vs保留"张力——CoACT 的 NAP 原则与 STALE 的记忆过期机制互补
- **与AgentLoop框架对应**：执行调度（[[ExecutionScheduling]]）直接对应 AgentLoop 的 Skill 编排层——SAGA 的工作流调度和 TypeGo 的 OS 式 runtime 是编排层的系统化实现
- **与可解释性连接**：缓存编辑指令（Leyline）的声明式 4-tuple 与 Proof-Carrying Agent Actions 的动作证书在"声明式治理"上方法论一致
- **与3GPP意图管理呼应**：模型路由的多维能力匹配（HyDRA）与 3GPP IntentHandlingFunction 的能力暴露在"能力 profile 匹配"上跨域共鸣

### 关键洞察

1. **OS类比是统一设计语言**（[[ModelNativeArchitecture]]）：LLM=CPU、KV cache=处理器缓存、上下文窗口=主存、agent框架=OS——这一类比贯穿上下文优化、调度、缓存三个方向
2. **Agent工作负载打破所有chatbot假设**（[[SAECache]]、[[Leyline]]、[[StatefulInference]]）：缓存不是仅追加的、token不是均匀的、prompt不是一次性的——需要全新的缓存管理范式
3. **行为保持优于信息保留**（[[CoACT]]）：压缩的衡量标准不是保留了多少信息，而是 agent 的后续行为是否一致——这是上下文优化的范式转换
4. **路由准确率存在plateau**（[[RoutingPlateau]]）：21种方法收敛到相似准确率——突破需要从全局趋势学习转向实例特定信号学习
5. **调度-缓存-路由三者协同**（[[PRISM-SchedulingMemory]]、[[INFRAMIND]]、[[GoodServe]]）：独立优化任一维度都不够——调度决定缓存命中、缓存决定延迟、延迟决定路由选择

---

## Round 12: 多智能体解决长上下文问题 (2024-2026)

### 概览

本轮聚焦多智能体（Multi-Agent）方法解决长上下文（Long-Context）问题，涵盖 32 篇论文，分为 6 大方向。核心洞察是：**多智能体协作是突破单一 LLM 上下文窗口限制的重要范式**，通过分段处理、共享记忆、KV cache 复用和递归委派实现超长上下文的有效建模。

### A. 核心框架：从链式到图到门控

多智能体长上下文处理的基础范式演进：

| 框架 | 核心机制 | 关键突破 | 引用 |
|---|---|---|---|
| [[ChainOfAgents]] (CoA) | worker 顺序处理 → manager 综合 | 奠基性框架；interleave reading & reasoning | 261 |
| [[GraphOfAgents]] (GoA) | 信息论压缩目标 + 动态协作图 | 2K context 超越 128K Llama 3.1 8B | 1 |
| [[LSTMMAS]] | LSTM 门控映射（input/forget/CEC/output gate） | +97.97% NarrativeQA vs CoA | 1 |
| [[COSMIR]] | 结构化记忆替代自由文本传递 | 减少传播阶段信息损失 | 1 |
| [[ChowLiuCoA]] | Chow-Liu 树学习 chunk 依赖排序 | ICLR 2026 Workshop | 0 |

**演进脉络**：自由文本传递(CoA) → 结构化记忆(COSMIR) → 门控机制(LSTM-MAS) → 信息论形式化(GoA) → 排序优化(Chow-Liu)。每一步都在解决前一步的信息瓶颈问题。

### B. 多智能体 RAG：文档级专业化

[[SPDRAG]] 的"每文档一 agent"范式与 [[SLEUTH]] 的"retriever + 4 协作 agent 粗到细"代表了多智能体 RAG 的两个方向：前者沿文档轴分解实现聚焦检索，后者沿证据处理流程分解实现多模态证据过滤。[[FinLongDocAgent]] 在金融领域验证了迭代检索+中间计算+验证的必要性。

### C. 记忆管理：多智能体的核心挑战

[[MemAgent]]（180 citations）通过 RL 训练单 agent 的覆写记忆策略实现 8K→3.5M 外推，是本领域引用最高的工作。[[AMA]] 用 Constructor/Retriever/Judge/Refresher 多 agent 协作管理多粒度记忆。[[ShardMemo]] 从分片路由角度用 masked MoE 优化记忆访问。[[GovernedSharedMemory]] 提出 fleet-memory 治理原语。[[EnsembleQSP]] 用三层层次记忆保持上下文有界（中位 301 tokens）。

### D. 基础设施：KV Cache 共享是系统级突破口

从"文本传递"到"KV 传递"的范式转换：
- [[AAFLOWPlus]]：KV cache 作为一等分布式对象，TTFT -50.2x
- [[AgentPrimitives]]：KV cache 内部通信替代自然语言，token -3~4x
- [[SideQuest]]：LRM 自身驱动 KV cache 压缩，peak token -65%
- [[TwinAgent]]：上下文残差压缩，仅传递紧凑 hint

### E. 特定任务：从代码到视频到医疗

多智能体长上下文方法已扩展到多个领域：[[SwarmResearch]] 和 [[CodeWiki]]（代码库）、[[WebSwarm]] 和 [[LMM-Searcher]]（搜索）、[[DelTA]]（翻译）、[[MACF]]（视频）、[[Traj-Evolve]]（医疗 EHR）。每个领域都验证了多智能体方法在处理超长上下文时的有效性。

### F. 分析洞察：扩展定律与深度失效

[[SIMAS]] 发现 MAS 性能不随 agent 数单调提升而是递减回报，协调开销是主因。[[TEP]] 识别了深度复合 AI 的 textual gradient 爆炸/消失问题。[[HIPIF]] 提出信息折叠减少长上下文干扰。[[PRIMA]] 总结了弹性多智能体操作模式。

### 与现有 Wiki 的连接

- **与 Agent Memory 呼应**：[[MultiAgentLongContext]] 与 [[AgentMemory]] 共享"压缩vs保留"张力——MemAgent 的覆写策略与 A-MEM 的 Zettelkasten 互补
- **与上下文优化连接**：[[AgentKVCacheSharing]] 是 [[ContextOptimization]] 的多智能体扩展——AAFLOW+ 的分布式 KV 复用与 SAECache 的语义淘汰互补
- **与可解释性呼应**：[[MultiAgentContextManagement]] 的治理原语与 [[RuntimeGovernance]] 的动作级验证在"显式治理"上方法论一致

### 关键洞察

1. **顺序链式处理是基础范式**（CoA → COSMIR → LSTM-MAS → Chow-Liu）：从自由文本到结构化记忆到门控机制到排序优化的渐进演进
2. **信息论形式化**（GoA）：将多智能体长上下文建模形式化为压缩问题，2K context 超越 128K——理论指导实践
3. **KV cache 共享是系统级突破口**（AAFLOW+/Agent Primitives）：从文本传递到 KV 传递，TTFT -50.2x——系统层优化比算法层更有效
4. **记忆管理是多智能体核心挑战**（MemAgent/AMA/ShardMemo）：粒度对齐/分片路由/治理原语三管齐下
5. **扩展定律：递减回报**（SIMAS）：MAS 性能不随 agent 数单调提升——协调开销是主因而非长上下文失败
6. **深度复合 AI 的梯度失效**（TEP）：textual gradient 爆炸/消失是长程工作流的核心挑战——需要平衡传播而非全局反向传播

---

## 第13轮：本体推理、LLM Agent本体增强与本体语义层（2023-2026）— 22篇论文 × 3方向

第13轮聚焦"本体推理、LLM Agent使用本体提升能力、本体用于语义层"，覆盖2023-2026年共22篇论文，按三个方向构建从推理技术到Agent增强到语义基础设施的完整技术图谱。这是 wiki 继 Round 10（本体应用在HCI）后再次系统性覆盖本体方向，但本轮聚焦的是本体推理技术本身、LLM Agent 的本体增强综合性技术，以及本体作为语义层的基础设施角色——与 Round 10 的 HCI/KGQA/TOD 场景互补。

### 跨方向趋势

| 方向 | 核心范式演进 | 关键论文 |
|---|---|---|
| **A. 本体推理** | 符号推理器→LLM增强推理→代数投影→同伦类型论推广 | [[neurowl]]、[[fuzzy-owl2-reasoning]]、[[hott-nesy-neurosymbolic]]、[[algebraic-ontology-projection]] |
| **B. LLM Agent+本体增强** | 本体作为知识源→本体作为工具层→本体作为架构基础→本体作为治理层 | [[agentic-redux]]、[[semantic-training-gap]]、[[virf-verifiable-embodied]]、[[deontic-policies-agenticrei]] |
| **C. 本体语义层** | 数据集成→虚拟本体层→对象中心建模→因果智能层→显式世界模型 | [[umodel-observability]]、[[causely-causal-intelligence]]、[[daoql-explicit-world-model]]、[[intent-6g-orchestration]] |

### A. 本体推理（Ontology Reasoning）

本体推理正从纯符号推理器向 LLM 增强的神经符号推理演进。[[neurowl]] 将 LLM 文本语义与本体嵌入结合，统一了包含验证与本体溯因——解决了不完整本体中经典推理器无法推断"合理但未被蕴含"关系的难题。[[algebraic-ontology-projection]] 从另一个角度切入，将 LLM 隐状态投影到 Galois 域 F2，发现 LLM 内部确实编码了可形式验证的代数本体结构，但存在"Late-layer Collapse"——最终层系统性逻辑一致性退化。[[hott-nesy-neurosymbolic]] 用同伦类型论推广神经符号推理，保留集合遗忘的对称性和证明计数信息。[[ontolearner]] 提供了首个统一本体学习基准（180本体×22域），发现瓶颈不是模型能力而是模型编码知识与本体组织方式的结构不匹配。

### B. LLM Agent使用本体提升能力

本方向的核心洞察是**本体从"知识源"提升为"架构基础层"**。[[agentic-redux]] 提出 Ontology-First Agent Design 方法论，用 BFO 本体化问题域+类型 lambda 演算证明语义正确性。[[deontic-policies-agenticrei]] 用 OWL 道义策略语言在 LLM 外部实现义务/豁免/冲突解决治理。[[semantic-training-gap]] 形式化"语义训练鸿沟"概念，将本体嵌入工具层实现 43%→0% 幻觉率。[[virf-verifiable-embodied]]（ICLR 2026）用形式安全本体驱动 tutor-apprentice 计划修复，HAR=0%。[[auto-ontology-construction-llm]] 构建 LLM+外部本体记忆层，生成-验证-修正管线。[[cybercane-neuro-symbolic-rag]] 引入 PhishOnt OWL 本体通过形式推理链实现可验证攻击分类。[[neuron-clinical-explainability]] 集成 SNOMED CT 本体+ML+RAG 三层。[[bdi-ontology]] 将 BDI 模型形式化为本体设计模式，通过 Logic Augmented Generation 与 LLM 耦合。

### C. 本体用于语义层

本方向展示本体作为异构数据/系统/agent 间的统一语义接口层。[[umodel-observability]] 在阿里云将可观测性从数据中心转向对象中心，百万级 OPS。[[causely-causal-intelligence]] 构建因果智能层，MTTD-63%、token-60%、根因100%。[[intent-6g-orchestration]] 用 TMF 意图本体+SHACL 验证驱动 6G 编排，幻觉-26pp。[[security-ontology-autonomous-networks]] 规范 TM Forum 安全本体 v4.0.0，RDFS 声明式安全管理。[[discoverable-agent-knowledge-aap]] 提出四维形式化框架和 Agent 可供性配置文件作为 VoID/DCAT 之上的语义层。[[ontology-aware-design-patterns-clinical]] 提出 7 种本体感知设计模式。[[autonomous-fair-digital-objects]] 用 RDF-star/PROV-O/SHACL/ODRL 三层增强 FAIR 数字对象。[[daoql-explicit-world-model]] 将确定性知识移入显式本体世界模型，反事实可分解性 94% vs GPT-4o 单独 45%。[[obda-query-abstraction]] 在 KR 2025 研究本体数据访问中的查询抽象。

### 跨方向收敛

| 收敛主题 | 本体推理 | LLM Agent+本体 | 本体语义层 |
|---|---|---|---|
| **神经符号分离** | LLM+嵌入 (NeurOWL), HoTT推广 | LLM+符号引擎 (VIRF, CyberCane) | 因果层+本体 (Causely) |
| **LLM外推理** | 代数投影 (AOP) | OWL道义策略 (AgenticRei) | SHACL验证 (6G), 逻辑引擎 (DaoQL) |
| **幻觉抑制** | F2约束 (AOP) | 本体工具层 43%→0% (Semantic Gap) | 目录接地 -26pp (6G) |
| **可验证性** | 形式验证+溯因 (NeurOWL) | 类型lambda证明 (Agentic Redux) | 审计账本+凭证 (Agentic Redux) |
| **从知识到架构** | 本体学习基础设施 (OntoLearner) | 本体优先设计 (Ontology-First) | 对象中心建模 (UModel) |

### 与现有Wiki的连接

- **与Round 10互补**：Round 10 聚焦本体在 HCI/KGQA/TOD 场景的应用，本轮聚焦本体推理技术本身、LLM Agent 的本体增强方法论、以及本体作为语义基础设施——两轮形成"应用场景×技术方法"的完整矩阵
- **与3GPP意图管理呼应**：[[intent-6g-orchestration]] 和 [[security-ontology-autonomous-networks]] 直接用 TM Forum 本体扩展了 [[IntentDrivenMnS]] 的"what vs how"抽象——本体定义"是什么"，推理引擎/agent决定"怎么做"
- **与AgentLoop框架对应**：[[OntologyFirstAgentDesign]] 的"本体→角色→agent→治理"与 [[RuntimeGovernance]] 的"动作级可验证授权"直接对应——本体提供机器可验证的治理基础
- **与神经符号编排呼应**：[[neurowl]] 和 [[virf-verifiable-embodied]] 与已有 [[NeurosymbolicOrchestration]]（VADAOrchestra）共享"LLM灵活规划+符号可验证执行"范式
- **与可观测性/因果连接**：[[umodel-observability]] 和 [[causely-causal-intelligence]] 为 [[CausalExplanation]] 提供了生产级语义基础设施实例

### 关键洞察

1. **本体从知识源到架构基础层**（[[OntologyFirstAgentDesign]]）：本体不再仅作为 RAG 的外部知识源，而是 agent 架构的基础层——提供类型约束、语义验证、审计凭证和治理边界
2. **LLM内隐编码可形式验证的本体结构**（[[algebraic-ontology-projection]]）：LLM 隐状态投影到 F2 域后展现 93.33% 零样本本体包含准确率——但存在 Late-layer Collapse，需 prompt+instruction tuning 联合防止
3. **本体语义层是生产级AI的基础设施**（[[umodel-observability]]、[[causely-causal-intelligence]]）：阿里云百万级 OPS 和 MTTD-63% 证明本体语义层不是学术概念而是工程必需
4. **神经符号分离是可靠性关键**（[[neurowl]]、[[virf-verifiable-embodied]]）：LLM 负责灵活推理，符号引擎/本体约束负责确定性验证——这种分离在医疗、安全、网络管理等高精度领域不可或缺
5. **本体学习瓶颈是结构而非模型**（[[ontolearner]]）：180本体×22域大规模评测发现，失败模式随本体复杂度而非模型规模扩展——"模型编码知识与本体组织方式的结构不匹配"是核心挑战

---

## Round 14: 本体用于意图理解与语义对齐 (2024-2026)

### 搜索方向

三个子方向交叉搜索：(A) 本体驱动的意图表示与对齐——用本体结构化约束将NL意图映射到可执行结构化表示；(B) LLM+本体协同意图理解——LLM借助本体做意图推理/grounding/消歧；(C) 本体对齐/匹配用于语义对齐——异构本体/schema间建立语义等价映射。

### A. 本体驱动的意图表示与对齐

本方向核心是利用形式本体（ISA-95、TMF Intent Ontology等）的结构化语义约束，将自然语言意图精确映射到可执行的结构化表示。[[intent-driven-smart-manufacturing]] 在 MaaS 生态中将 LLM 意图翻译为 ISA-95 对齐的 Neo4j KG 节点，89.33% EM。[[treerec-intent-artifacts]] 用本体语义树组织制品层次，实现意图-功能对齐并缩小候选空间。[[geospatial-kg-multi-agent]] 用统一元数据本体作为语义中介层对齐跨平台异构标准，多 Agent 架构执行意图解析→KG检索→答案合成。[[rag-intent-reasoning-network]] 指出为每个应用手工构建本体语言不可扩展，提出 MR+RAG 替代方案。[[usage-centric-intent-ecommerce]]（EMNLP 2024）反思产品本体的类别刚性和属性模糊局限，提出本体无关的意图理解范式。

### B. LLM+本体协同意图理解

本方向研究 LLM 借助本体进行意图推理、grounding 和消歧。[[birgat-multi-intent-slu]]（ICASSP 2024）用双关系图注意力网络编码本体项层次结构，配合3层语义框架解决多意图对齐和分配问题。[[usd-scene-ontology-grounding]]（ICRA 2026 WS）证明 LLM 可零样本完成场景对象到 SOMA-HOME 本体的 grounding（90-96%），但消融实验揭示 LLM 依赖场景图语义线索而非几何信息。[[sam-ner-semantic-archetype]]（ACL 2026 Findings）通过从本体抽象蒸馏的中间原型空间稳定跨域 NER 迁移，避免标签定义与 LLM 内在语义不对齐导致的系统性漂移。

### C. 本体对齐/匹配用于语义对齐

本方向聚焦异构本体/schema间的语义等价映射技术。[[open-ontologies-stable-matching]] 的核心发现是稳定 1:1 匹配是对齐质量主导因素（OAEI F1=0.832），信号权重在稳定匹配下无关紧要（F1变化<0.004）。反直觉发现：LLM 读原始 OWL 文件（F1=0.323）比不读文件（F1=0.431）更差，MCP 工具结构化访问（F1=0.717）提供质变模式。[[anchor-schema-agnostic-ontology]] 的混合本体发现机制动态探索大本体 schema，SHACL 验证确保合规。[[blinkg-llm-kg-benchmark]] 评估 LLM schema-本体映射能力，发现复杂场景仍有限。[[llm-ontology-engineering-legal-kg]]（SEMANTiCS 2026）用两阶段开放-封闭提取策略构建法律 KG。[[cortex-ontological-corpus-graph]] 的三层 OCG 统一内容/本体/跨域对齐，发布 24.14B token 精炼语料。[[concepte-event-ontology-expansion]] 用 LLM 概念化提取概念级语义，BCubed-F1 +12.37%。[[virtualset-typed-ontology-worlds]] 用类型化本体世界替代 SQL 作为 LLM 生成目标，GCP 预执行语义检查。

### 跨方向收敛

| 收敛主题 | 意图对齐 (A) | LLM+本体 (B) | 本体匹配 (C) |
|---|---|---|---|
| **稳定匹配/对齐** | TreeRec层次语义树 | SAM-NER原型中介 | Open Ontologies稳定1:1匹配 |
| **grounding** | ISA-95 KG节点映射 | USD场景→SOMA-HOME | ANCHOR schema→本体发现 |
| **本体局限性** | 类别刚性/属性模糊 | 标签语义不对齐 | LLM读原始OWL更差 |
| **工具层vs原始访问** | MR+RAG替代手工本体 | 冻结LLM+约束推理 | MCP工具>F1=0.717 |
| **幻觉抑制** | 本体约束操作对齐 | 定义对齐推理 | GCP类型错误预执行 |

### 与现有Wiki的连接

- **与Round 10/13互补**：Round 10 聚焦本体在 HCI/KGQA/TOD 场景应用，Round 13 聚焦本体推理/语义层基础设施，本轮聚焦本体与意图理解/语义对齐的交叉——形成"应用场景×技术方法×意图交叉"三维矩阵
- **与NOEM³A直接呼应**：[[noemmma]] 用本体注入+解码先验增强多意图理解，本轮 [[birgat-multi-intent-slu]] 用图注意力编码本体层次解决多意图对齐，[[intent-driven-smart-manufacturing]] 用 ISA-95 本体对齐意图翻译——三者从不同角度验证"本体结构化约束提升意图理解精度"
- **与3GPP意图管理呼应**：[[rag-intent-reasoning-network]] 和 [[intent-driven-smart-manufacturing]] 为 [[IntentDrivenMnS]] 的"what vs how"抽象提供了工业实践案例——本体定义"是什么"的语义约束
- **与语义检索连接**：[[treerec-intent-artifacts]] 的语义树和 [[cortex-ontological-corpus-graph]] 的三层OCG为 [[RetrievalAugmentedGeneration]] 提供了本体驱动的语义组织方案

### 关键洞察

1. **本体结构化约束是意图对齐的操作语义保证**（[[intent-driven-smart-manufacturing]]、[[geospatial-kg-multi-agent]]）：领域标准本体（ISA-95/TMF）确保意图翻译结果与实际系统资源和约束一致，而非仅语义相似
2. **稳定匹配主导本体对齐质量**（[[open-ontologies-stable-matching]]）：信号权重在稳定匹配下无关紧要——这一发现简化了本体对齐的工程实践
3. **LLM本体grounding依赖语义线索而非几何信息**（[[usd-scene-ontology-grounding]]）：匿名化语义线索后准确率降至0-6%，揭示LLM的grounding本质是语义推理
4. **本体刚性是双刃剑**（[[usage-centric-intent-ecommerce]]）：本体提供结构化约束但也限制跨类别对齐——需要本体无关的推理作为补充
5. **工具结构化访问是LLM本体交互的质变模式**（[[open-ontologies-stable-matching]]）：MCP工具访问（F1=0.717）远超原始OWL文件读取（F1=0.323），证明LLM需要结构化而非原始语法访问本体

---

## 第15轮：本体图增强精准检索（2024-2026）— 17篇论文 × 4子方向

第15轮聚焦"类似 ANCHOR 的本体图增强精准检索"，覆盖从输入转本体图到本体约束检索的完整管线。17篇论文按四条技术路线组织，核心问题是：如何利用形式本体的类型/层次/关系/约束结构实现超越纯向量相似度的精准语义检索。

### 跨方向趋势

| 子方向 | 核心范式演进 | 关键论文 |
|---|---|---|
| **A. 本体图直接增强检索** | 向量相似度→本体超图最小集→层次感知双曲嵌入→多锚点并行→FAIR约束KG | [[og-rag-ontology-grounded]]、[[hyem-hyperbolic-ontology-retrieval]]、[[omagr-ontology-multi-anchor-retrieval]] |
| **B. 本体感知图/记忆引擎** | flat向量库→递归图组合→写入时协调→可审计结构化DB | [[worlddb-ontology-aware-memory]]、[[moss-auditable-agentic-memory]] |
| **C. 本体引导查询构造** | 手工SPARQL→零样本LLM生成→迭代自修正→本体知识查询扩展 | [[nlkgq-nl-ontology-query]]、[[researcher-agents-kgqa]]、[[bmqexpander-ontology-query-expansion]] |
| **D. 本体构建/验证支撑** | LLM提取→类型规范化+去重→FCA符号验证→多agent生成 | [[ontology-dedup-kg-construction]]、[[verifiable-knowledge-expansion-fca]]、[[automated-ontology-generation-multi-agent]] |

### 四维分析核心发现

#### A. 本体图直接增强检索精度

这是本轮的核心方向——直接用本体结构约束检索过程。[[og-rag-ontology-grounded]] 的 OG-RAG 将领域文档构建为本体超图，用最小超边集优化算法检索精准上下文，recall+55%、correctness+40%，是本体图检索的标杆方法。[[evidence-units-ontology-retrieval]] 从文档组织层入手，用本体grounding将结构化文档组织为语义完整 Evidence Units，修复元素级索引的碎片化问题。[[hyem-hyperbolic-ontology-retrieval]] 的 HyEm 将本体 is-a 层次编码为双曲嵌入，查询自适应切换双曲/欧式检索——解决层次感知检索的双曲/欧式两难。[[omagr-ontology-multi-anchor-retrieval]] 的 OMAGR 用本体定义多锚点并行图检索，打破单轴压缩瓶颈。[[fair-graphrag-semantic-data]] 将 FAIR 原则嵌入 GraphRAG。[[ontologyrag-biomedical-code-mapping]] 和 [[cyberbot-ontology-grounded-rag]] 分别在生物医学和网络安全领域验证本体grounding RAG 的精准检索效果。

**关键洞察**：本体图检索的核心优势不是"找到更多"，而是"找对概念"——通过类型约束和关系结构确保检索结果概念一致，而非仅表面相似。

#### B. 本体感知图/记忆引擎

这一方向挑战 RAG 的基础设施——flat 向量库。[[worlddb-ontology-aware-memory]] 的 WorldDB 用递归可组合图+本体感知写入时协调替代 flat chunk，在写入时而非读取时解决矛盾/替代。[[moss-auditable-agentic-memory]] 的 MOSS 将 RAG 的"不透明"从固有特性重新定义为可解决的结构缺陷，用结构化关系 DB 让 agent 主动构造查询，实现可审计检索。[[rag-autoconfig-industrial-fieldbus]] 用 ECLASS 本体图+混合稠密稀疏检索在工业场景验证。

**关键洞察**：从"读取时向量匹配"到"写入时结构化协调+读取时精确查询"的范式转变——flat 向量库的根本缺陷（碎片化、无身份、无矛盾感知）需在存储层解决。

#### C. 本体引导查询构造

这一方向用本体 schema 作为 LLM 生成精准查询的"语义契约"。[[nlkgq-nl-ontology-query]] 证明 OWL 本体足以让 LLM 零样本生成准确结构化查询——无需微调/RAG/多agent。[[researcher-agents-kgqa]] 的 Researcher Agent 在验证集上迭代自修正本体grounding和提示/工具配置。[[bmqexpander-ontology-query-expansion]] 用 UMLS 本体知识+LLM 做查询扩展。[[kroma-ontology-matching-rag]] 用 RAG 管线增强本体匹配。

**关键洞察**：本体 schema 是 NL→结构化查询的"语义契约"——足够好的本体可以让 LLM 零样本生成精准查询，降低对微调和 RAG 的依赖。

#### D. 本体构建/验证支撑检索

这一方向解决"输入→本体图"的前端问题。[[ontology-dedup-kg-construction]] 用本体引导去重+类型规范化将文档流转为验证 KG。[[verifiable-knowledge-expansion-fca]] 用 FCA 符号验证循环确保 LLM 本体扩展的可验证性。[[automated-ontology-generation-multi-agent]] 系统研究多 agent LLM 本体生成的架构设计选择。

**关键洞察**：本体构建的质量直接决定检索精度——"垃圾进，垃圾出"在本体图检索中尤为突出。去重、类型规范化、符号验证是保证本体质量的三道防线。

### 与现有Wiki的连接

- **与ANCHOR直接呼应**：[[anchor-schema-agnostic-ontology]] 解决"输入→本体图"构建（schema-agnostic 本体发现+SHACL验证），本轮解决"本体图→精准检索"查询——两者构成完整管线
- **与Round 10/13/14互补**：Round 10 聚焦本体在 KGQA/TOD/HCI 场景应用，Round 13 聚焦本体推理/语义层基础设施，Round 14 聚焦本体与意图对齐，本轮聚焦本体图增强检索精度——形成"场景×基础设施×意图×检索"四维矩阵
- **与GraphRAG连接**：[[GraphRAG]] 从文档提取 KG 增强检索但不一定用形式本体约束，[[OntologyGraphRetrieval]] 用形式本体 schema 作为"语义契约"约束全管线——是 GraphRAG 的形式化升级
- **与语义检索Round 9连接**：Round 9 的 [[omd-graphrag]]（本体引导提取）和 [[cog-rag]]（主题对齐双超图）为本轮提供了语义检索基础，本轮用本体图进一步精确化

### 关键洞察

1. **本体图检索的核心价值是"概念一致"而非"表面相似"**（[[og-rag-ontology-grounded]]、[[cyberbot-ontology-grounded-rag]]）：通过本体类型/关系约束，检索结果锚定到概念层次，确保域适切——在事实推理场景中显著优于 vanilla RAG
2. **flat 向量库是可解决的结构缺陷**（[[moss-auditable-agentic-memory]]、[[worlddb-ontology-aware-memory]]）：碎片化、无身份、无矛盾感知不是 RAG 的固有特性，而是 flat 存储的工程选择——结构化图存储+写入时协调可解决
3. **本体 schema 是 NL→结构化查询的"语义契约"**（[[nlkgq-nl-ontology-query]]、[[researcher-agents-kgqa]]）：足够好的本体可以让 LLM 零样本生成精准查询，降低对微调和 RAG 的依赖
4. **本体层次结构需要几何感知编码**（[[hyem-hyperbolic-ontology-retrieval]]）：is-a 层次树的双曲嵌入天然适配指数体积增长，查询自适应机制解决双曲/欧式两难
5. **本体质量是检索精度的天花板**（[[ontology-dedup-kg-construction]]、[[verifiable-knowledge-expansion-fca]]）：去重、类型规范化、符号验证是保证本体质量的三道防线——"垃圾进，垃圾出"
