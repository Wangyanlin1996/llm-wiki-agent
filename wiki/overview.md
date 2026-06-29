---
title: "Overview"
type: synthesis
tags: []
sources: [28556-j00, 28312-j50, 28622-k20, 28912-j00, 28914-j00, evo-memory, agent-memory-survey, lightmem, emem, intpro, intent-signal-theory, vitabench2, intent-communication-design, intentrl, pira-bench, pask, memcog, memgym, apex-mem, h-mem, enpmr-bench, minteval, intentgrasp, recap, personalalign, contextagent, intent-detection-llm, satori, neurosync, ask-before-plan, inner-thoughts, proactive-ai-implications, assistantx, etapp, noemmma, good-agent-alignment, pp-clarifier, cocot, debate, onepred, icebreaker, proutt, speakrl, target-proactive-dialogue, ocr-memory, memoryos, memp, agentkb, mempi, peam, evomembench, sii-piwm, knowu-bench, proagentbench, procodebench, pa-bridge, reward-driven-interaction, amem, scrapmem, stale, promem, memory-autonomous-agents-survey, userharness, intentvlm, guide-bench, coinbench, tomcat, bayesian-social-deduction, psi-bench, fingertip-20k, propersim, ds-ia-framework, recgpt-mobile, cfqp, rac, corpus-rag-clarifying, cops, janus, sensitivity-aware-clarification, fairy-gui-agent, llm-autonomous-agent-survey, agentbench, agentverse, explainable-human-ai-interaction, agent-traces-to-trust, hansel-web-agent-verification, causal-past-logic-runtime-verification, three-level-llm-xai, explainable-ai-to-whom, responsible-explainable-ai-agents, blockchain-accountability-agents, argument-is-the-explanation, causal-explanations-sequential-uncertainty, trism-agentic-ai, cema-causal-explanations-mas, triex-multi-agent-llm-explanation, counterfactual-mas-explanation, policy-explanations-marl]
last_updated: 2026-06-29
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