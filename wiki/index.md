# Wiki Index

本文件由 LLM 维护，每次 ingest 时更新。

## Overview
- [Overview](overview.md) — 跨所有来源的持续综合

## Sources

### 3GPP Standards
- [3GPP TS 28.556 V19.0.0 — 5G Network Policy Management (Stage 2 & 3)](sources/28556-j00.md) — Policy MnS Stage 2 & 3 spec for 5G networks
- [3GPP TS 28.312 V19.5.0 — Intent Driven Management Services for Mobile Networks](sources/28312-j50.md) — Intent Driven MnS (IDMS) concepts, requirements, Stage 2/3
- [3GPP TS 28.622 V20.2.0 — Generic NRM IRP Information Service (IS)](sources/28622-k20.md) — Foundation NRM with Top IOC, SubNetwork, ManagedElement, and common data types
- [3GPP TR 28.912 V19.0.0 — Study on Intent Driven MnS (Rel-18)](sources/28912-j00.md) — Study report: energy saving, conflicts, 5GC, SON, MDA, AI/ML mapping
- [3GPP TR 28.914 V19.0.0 — Study on Intent Driven MnS (Rel-19)](sources/28914-j00.md) — Study report: exploration, negotiation, utility, degradation, maintenance

### AI Agent — Agent Memory
- [Evo-Memory: Benchmarking LLM Agent Test-time Learning with Self-Evolving Memory](sources/evo-memory.md) — Streaming benchmark for self-evolving agent memory; ExpRAG + ReMem pipeline (2025, 71 citations)
- [From Storage to Experience: A Survey on the Evolution of LLM Agent Memory](sources/agent-memory-survey.md) — Survey: Storage→Reflection→Experience evolutionary framework (2026, 4 citations)
- [LightMem: Lightweight LLM Agent Memory with Small Language Models](sources/lightmem.md) — SLM-driven STM/MTM/LTM memory; F1 +2.5 over A-MEM on LoCoMo (2026, 4 citations)
- [E-mem: Multi-agent Episodic Context Reconstruction for LLM Agent Memory](sources/emem.md) — Episodic Context Reconstruction; 54% F1 surpassing GAM by 7.75% (2026, 3 citations)
- [MemCog: From Memory-as-Tool to Memory-as-Cognition](sources/memcog.md) — Paradigm shift from passive retrieval to active cognitive memory (2026)
- [MemGym: Long-Horizon Memory Environment for LLM Agents](sources/memgym.md) — Long-horizon memory evaluation environment (2026)
- [APEX-MEM: Agentic Semi-Structured Memory with Temporal Reasoning](sources/apex-mem.md) — Semi-structured memory + temporal reasoning for conversational agents (2026)
- [H-Mem: Hybrid Memory Mechanism for Evolving and Retrieving Agent Memory](sources/h-mem.md) — Hybrid representation (facts + summaries + profiles) for evolving memory (2026)
- [ENPMR-Bench: Proactive Memory Retrieval for Emotional Support Agents](sources/enpmr-bench.md) — Benchmarking proactive memory retrieval for emotional support (2026)
- [MINTEval: Memory under Multi-Target Interference](sources/minteval.md) — Evaluating memory degradation from concurrent goal interference (2026)
- [OCR-Memory: Optical Context Retrieval for Long-Horizon Agent Memory](sources/ocr-memory.md) — 视觉模态高密度记忆表示；locate-and-transcribe；ACL 2026 (2026)
- [MemoryOS: AI Agent 记忆操作系统](sources/memoryos.md) — OS启发STM/MTM/LTM；F1+49.11%；64 citations (2025)
- [Memp: Agent 程序性记忆探索](sources/memp.md) — 可学习程序性记忆；细粒度+脚本抽象；ACL 2026 Findings (2025)
- [Agent KB: 跨域经验共享知识库](sources/agentkb.md) — 跨框架记忆共享；disagreement gate；+18.7pp GAIA；53 citations (2025)
- [Mem-π: 自适应记忆生成](sources/mempi.md) — 按需生成vs检索；决策-内容解耦RL；>30%提升 (2026)
- [PEAM: 参数化具身记忆](sources/peam.md) — MoE-LoRA参数驻留技能；对比内化失败纠正；Minecraft (2026)
- [EvoMemBench: 自演化记忆评测](sources/evomembench.md) — 记忆范围×内容双轴；15方法对比；长上下文仍强 (2026)
- [A-MEM: Agentic Memory for LLM Agents](sources/amem.md) — Zettelkasten自主记忆；动态索引+链接+演化；NeurIPS 2025 (2025)
- [ScrapMem: Bio-inspired On-device Memory via Optical Forgetting](sources/scrapmem.md) — 光学遗忘+EM-Graph；93%存储节省；SOTA 51.0% (2026)
- [STALE: Can LLM Agents Know When Memories Are No Longer Valid?](sources/stale.md) — 隐式冲突检测；CUPMem状态裁决；400场景；55.2% (2026)
- [ProMem: Proactive Memory Extraction](sources/promem.md) — 自问迭代反馈循环替代静态摘要；完整性提升 (2026)
- [Memory for Autonomous LLM Agents Survey](sources/memory-autonomous-agents-survey.md) — write-manage-read循环；3D分类；5机制族；2022-2026 (2026)

### AI Agent — Intent Understanding
- [IntPro: A Proxy Agent for Context-Aware Intent Understanding](sources/intpro.md) — Retrieval-conditioned intent inference with per-user history library; SFT+GRPO (2026)
- [Intent Signal Theory: A Computational Framework for Intent-State Control](sources/intent-signal-theory.md) — IST framework: I*/I-hat/P/O; Irreversible Intent Loss theorem (2026)
- [VitaBench 2.0: Evaluating Personalized and Proactive Agents](sources/vitabench2.md) — Benchmark for personalized+proactive long-term agent evaluation (2026)
- [Designing Intent Communication for Agent-Human Collaboration](sources/intent-communication-design.md) — Transparency×Abstraction×Modality design space (MUM 2025, 2 citations)
- [IntentGrasp: Comprehensive Benchmark for Intent Understanding](sources/intentgrasp.md) — 49 corpora, 12 domains, IFT fine-tuning (2026)
- [RECAP: Rewriting Conversations for Intent Understanding in Agentic Planning](sources/recap.md) — Intent rewriting benchmark for agent planning (2025)
- [PersonalAlign: Hierarchical Implicit Intent Alignment for GUI Agents](sources/personalalign.md) — ACL 2026, HIM-Agent +15.7% execution, +7.3% proactive (2026)
- [ContextAgent: Context-Aware Proactive LLM Agents with Sensory Perceptions](sources/contextagent.md) — Wearable sensory context, 41 citations (2025)
- [Intent Detection in the Age of LLMs](sources/intent-detection-llm.md) — EMNLP 2024, hybrid routing, 41 citations (2024)
- [Satori: Proactive AR Assistant with BDI User Modeling](sources/satori.md) — BDI + multi-modal LLM for proactive AR guidance (2024)
- [NeuroSync: Intent-Aware Code-Based Problem Solving](sources/neurosync.md) — UIST 2025, direct intent-task manipulation paradigm (2025)
- [NOEM³A: Neuro-Symbolic Ontology-Enhanced Multi-Intent Understanding](sources/noemmma.md) — 神符号本体增强多意图消歧；SIS指标；3B→85% vs GPT-4 90% (2025)
- [GOOD: Flexible Agent Alignment with Goal Inference from Open-Ended Dialog](sources/good-agent-alignment.md) — OU-AGs框架+GOOD在线目标推断；三领域评测 (2025)
- [Plug-and-Play Clarifier: Zero-Shot Multimodal Egocentric Intent Disambiguation](sources/pp-clarifier.md) — 三模块零样本框架；4-8B模型+30%；AAAI 2026 (2025)
- [CoCoT: Cognitive Chain-of-Thought for Structured Multimodal Reasoning](sources/cocot.md) — 认知三阶段推理（感知→情境→规范）；SFT内化+5-6% (2025)
- [DEBATE: Dataset for Disentangling Textual Ambiguity in Mandarin Through Speech](sources/debate.md) — 首个中文语音-文本消歧数据集；1001×10说话人 (2025)
- [SII/PIWM: 看-推断-干预主动世界建模](sources/sii-piwm.md) — AIDA+BDI双重状态；五类响应；GuidanceSalesBench (2026)
- [KnowU-Bench: 交互式主动个性化移动Agent评测](sources/knowu-bench.md) — 偏好获取+同意协商+拒绝后克制；Claude<50% (2026)
- [Reward-Driven Interaction: 用户满意度驱动主动对话](sources/reward-driven-interaction.md) — 满意度预测作为奖励；对比自监督+领域意图分类；DuerOS (2025)
- [UserHarness: Harnessing User Minds for Stronger Agent ToM](sources/userharness.md) — 心智重建；观察→信念→意图→行动；95.94% macro accuracy (2026)
- [IntentVLM: Open-Vocabulary Intention Recognition](sources/intentvlm.md) — 视频语言前逆建模；两阶段意图识别；SOTA 80% (2026)
- [GUIDE: GUI User Intent Detection Evaluation](sources/guide-bench.md) — GUI意图基准；67.5h/120用户/10软件；CVPR 2026 (2026)
- [COINBench: Collective Intent Understanding](sources/coinbench.md) — 集体意图基准；群体共识/矛盾/趋势；COIN-TREE+COIN-RAG (2026)
- [Tomcat: Theory of Mind in Human-Agent Collaboration](sources/tomcat.md) — 指令推理ToM；52人类对照；Fs-CoT (2025)
- [Bayesian Social Deduction](sources/bayesian-social-deduction.md) — 贝叶斯+LLM混合推理；67%胜率击败人类；ACL 2026 (2025)
- [CICC: Conformal Intent Classification and Clarification](sources/cicc.md) — 共形预测把分类器不确定度转为有统计保证的候选集；三分支决策；保证真意图在集内 (2024)
- [GID: Generalized Intent Discovery](sources/gid.md) — 开放世界意图发现；IND+OOD同时分类+发现；EMNLP 2022 (2022)
- [Continual GID: Marching Towards Dynamic Open-world Intent Recognition](sources/continual-gid.md) — 持续增量发现新意图；多阶段OOD学习；ACL 2023 (2023)
- [DROID: Dual Representation for Out-of-Scope Intent Detection](sources/droid.md) — 双表示OOS检测；监督+对比原型；单一校准阈值 (2025)
- [Deep Unknown Intent Detection with Margin Loss](sources/deep-unknown-intent.md) — BiLSTM+margin loss+LOF；两阶段未知意图检测经典；ACL 2019, 162 citations (2019)
- [Open Intent Discovery through Unsupervised Semantic Clustering](sources/open-intent-discovery.md) — 无监督依存解析+语义聚类从零发现意图；EMNLP 2021 (2021)
- [SAGE-Agent: Structured Uncertainty guided Clarification for LLM Agents](sources/sage-agent.md) — EVPI量化澄清问题消歧价值；结构化参数域建模；ClarifyBench基准 (2025)
- [Active Task Disambiguation with LLMs](sources/active-task-disambiguation.md) — 贝叶斯实验设计框架任务消歧；最大化信息增益；元认知推理 (2025)
- [CLARA: Show, Don't Ask — Visual Disambiguation for CIR with Turn-Valid Coverage](sources/clara.md) — 共形预测多轮扩展；似然比重加权turn-valid保证；视觉原型面板消歧 (2026)
- [Neural EVPI: Ranking Clarification Questions using Neural Expected Value of Perfect Information](sources/neural-evpi.md) — EVPI驱动澄清问题排序鼻祖；StackExchange ~77K数据集；NAACL 2018 (2018)
- [Clarify When Necessary: Resolving Ambiguity Through Interaction with LMs](sources/clarify-when-necessary.md) — intent-sim意图熵判断何时澄清；三子任务框架；CICC精神前身 (2023)
- [Uncertainty Decomposition for Clarification Seeking in LLM Agents](sources/uncertainty-decomposition-clarification.md) — prompt-based分离u_t/c_t；黑箱API兼容；F1 +73%；WebShop-Clar/ALFWorld-Clar基准 (2026)

### AI Agent — Intent Recommendation
- [IntentRL: Training Proactive User-intent Agents via Reinforcement Learning](sources/intentrl.md) — RL-trained proactive intent clarification; shallow-to-deep refinement graph (2026, 4 citations)
- [PIRA-Bench: Proactive Intent Recommendation Agents on GUI](sources/pira-bench.md) — First proactive intent recommendation benchmark; PIRF framework (2026, 3 citations)
- [PASK: Intent-Aware Proactive Agents with Long-Term Memory](sources/pask.md) — DD-MM-PAS paradigm; IntentFlow; LatentNeeds-Bench (2026, 2 citations)
- [Ask-before-Plan: Proactive Language Agents for Real-World Planning](sources/ask-before-plan.md) — EMNLP 2024, CEP multi-agent framework, 12 citations (2024)
- [Proactive Conversational Agents with Inner Thoughts](sources/inner-thoughts.md) — Inner Thoughts framework, covert thought train for proactivity (2025)
- [When AI-Based Agents Are Proactive: Implications for Competence](sources/proactive-ai-implications.md) — BISE 2025, proactive help reduces competence self-esteem, 22 citations (2025)
- [AssistantX: LLM-Powered Proactive Assistant](sources/assistantx.md) — IROS 2025, 4-agent framework, real-world office deployment (2025)
- [ETAPP: Evaluating Personalized Tool-Augmented LLMs](sources/etapp.md) — ACL 2025, personalization + proactivity benchmark (2025)
- [OnePred: Next-Query Prediction via Recursive Intent Memory](sources/onepred.md) — 递归意图记忆+两阶段RL；token消耗降低22×；NQP-Bench (2026)
- [IceBreaker: Breaking the First-Message Barrier with Personalized Starters](sources/icebreaker.md) — 对话开场语生成新任务；两步握手框架；CTR+9.425%；ACL 2026 Industry (2026)
- [ProUtt: LLM-Driven Preference Data Synthesis for Proactive Prediction](sources/proutt.md) — 意图树建模+双视角推理轨迹+扰动修正偏好数据 (2026)
- [SpeakRL: Synergizing Reasoning, Speaking, and Acting with RL](sources/speakrl.md) — RL增强主动澄清意图；SpeakER数据集；完成率+20.14% (2025)
- [Target-Guided Proactive Dialogue via Scenario Modeling and Intent-Keyword Bridging](sources/target-proactive-dialogue.md) — 场景建模+意图关键词桥接；主动性与信息性改善 (2026)
- [ProAgentBench: 真实世界主动Agent评测](sources/proagentbench.md) — 28K+事件/500+小时真实数据；时机预测+辅助内容生成 (2026)
- [ProCodeBench: 主动编程助手评测](sources/procodebench.md) — 1,246开发者IDE数据；模拟vs真实差距；模拟高估性能 (2026)
- [PA-Bridge: 桥接被动与主动对话开场语推荐](sources/pa-bridge.md) — 打破回声室；对抗分布对齐+语义离散器；SIGIR 2026 (2026)
- [Ψ-Bench: Persona-Sensitive Influencing](sources/psi-bench.md) — 主动个性化影响评测；+18.24%有画像 (2026)
- [FingerTip 20K: Proactive and Personalized Mobile Agents](sources/fingertip-20k.md) — 20K真实演示；主动任务建议+个性化执行；ICLR 2026 (2025)
- [ProPerSim: Proactive+Personalized Simulation](sources/propersim.md) — 主动+个性化联合仿真；ProPerAssistant；ICLR 2026 (2025)
- [DS-IA Framework: Dual-Stage Intent-Aware](sources/ds-ia-framework.md) — 语义防火墙+级联验证器；EM 58.56%；交互频率困境解决 (2026)
- [RecGPT-Mobile: On-Device Intent Understanding](sources/recgpt-mobile.md) — 端侧LLM意图理解Agent；淘宝验证；KDD 2026 (2026)
- [CFQP: Collaborative Filtering Question Prediction](sources/cfqp.md) — 个性化记忆+图偏好传播；下一问题预测 (2025)

### AI Agent — Memory-Enhanced Intent Clarification
- [RAC: Retrieval-Augmented Clarification for Faithful Conversational Search](sources/rac.md) — RAG生成语料锚定澄清问题；对比偏好优化；ECIR 2026 (2026)
- [Corpus-informed RAG of Clarifying Questions](sources/corpus-rag-clarifying.md) — RAG联合建模query+corpus定位不确定性；数据增强对齐 (2024)
- [CoPS: Cognitive Personalized Search with Memory Mechanism](sources/cops.md) — 认知三阶记忆(感觉/工作/长期)驱动个性化搜索意图；WWW 2024 (2024)
- [JANUS: Factored Reasoning with Inner Speech and Persistent Memory](sources/janus.md) — 持久记忆三层+内部言语触发澄清；从欠明确请求恢复 (2026)
- [Sensitivity-Aware Retrieval-Augmented Intent Clarification](sources/sensitivity-aware-clarification.md) — 检索增强意图澄清+敏感域保护；攻击模型+检索级防御；ECIR 2026 Workshop (2026)
- [Fairy: Robust Agentic Systems with EMA + RGR](sources/fairy-gui-agent.md) — 演化记忆架构+目标精炼澄清；模糊任务基准+33.7%；50页 (2025)

## Entities
- [3GPP](entities/3GPP.md) — Collaborative telecom standards organization (7 organizational partners)

## Concepts

### 3GPP Management
- [Policy MnS](concepts/PolicyMnS.md) — 3GPP Policy Management Service for 5G lifecycle management & conflict detection
- [Policy IOC](concepts/PolicyIOC.md) — Information Object Class representing a network policy (4 mandatory attributes)
- [PolicyContent](concepts/PolicyContent.md) — Condition-action dataType for policy logic
- [Policy Conflict Detection](concepts/PolicyConflictDetection.md) — Mechanism for detecting and notifying conflicting policies
- [Intent Driven MnS](concepts/IntentDrivenMnS.md) — 3GPP Intent Driven Management Service (IDMS) — declarative goal-based management
- [Intent IOC](concepts/IntentIOC.md) — Information Object Class for intent representation with expectations, state, priority
- [IntentExpectation](concepts/IntentExpectation.md) — DataType for expressing object+target+context expectations
- [Intent Report](concepts/IntentReport.md) — IOC for six types of intent report information (fulfilment, conflict, feasibility, etc.)
- [Intent Handling Function](concepts/IntentHandlingFunction.md) — IOC exposing producer's intent handling capabilities
- [Intent Conflict Resolution](concepts/IntentConflictResolution.md) — Three-level conflict detection (target, expectation, intent) with preemption
- [Intent Negotiation](concepts/IntentNegotiation.md) — Pre-evaluation and fulfilment phase negotiation procedures
- [Intent Utility Function](concepts/IntentUtilityFunction.md) — Mathematical preference expression for quantitative fulfilment
- [Rule-Policy-Intent Relation](concepts/RulePolicyIntentRelation.md) — Abstraction hierarchy from "how" (rule) to "what" (intent)
- [Intent Policy Library](concepts/IntentPolicyLibrary.md) — Strategy knowledge layer mapping telecom intent templates to governable policy candidates
- [5G Network Management](concepts/5GNetworkManagement.md) — 3GPP TS 28.x management & orchestration specification family
- [TS 28.532](concepts/TS28532.md) — Generic management services (provisioning MnS) foundation
- [TS 28.622](concepts/TS28622.md) — Generic NRM IRP Information Service — foundational IOC hierarchy and data types
- [Top IOC](concepts/TopIOC.md) — Root IOC for all FNIM-conformant specifications (Top_ + TopX)
- [NRM](concepts/NRM.md) — Network Resource Model concept — IOC collection representing managed network resources
- [Intent-driven SON Orchestration](concepts/IntentSONOrchestration.md) — SON functions driven by intent expectations with 3 intent types
- [Intent-driven MDA](concepts/IntentMDA.md) — MDA analytics triggered by intent expectations via capability matching

### AI Agent Research
- [Agent Memory](concepts/AgentMemory.md) — LLM agent memory mechanisms: Storage→Reflection→Experience evolution
- [Intent Understanding](concepts/IntentUnderstanding.md) — Context-aware intent inference in human-agent interaction
- [Intent Recommendation](concepts/IntentRecommendation.md) — Proactive intent detection and recommendation by AI agents
- [PIRF](PIRF.md) — Memory-aware state-tracking framework for proactive intent recommendation on GUI
- [MemCog](concepts/MemCog.md) — Memory-as-Cognition paradigm for conversational agents
- [MemGym](concepts/MemGym.md) — Long-horizon memory evaluation environment
- [IntentGrasp](concepts/IntentGrasp.md) — Comprehensive intent understanding benchmark with IFT fine-tuning
- [AskBeforePlan](concepts/AskBeforePlan.md) — Proactive agent planning with clarification-before-execution
- [InnerThoughts](concepts/InnerThoughts.md) — Covert thought framework for proactive conversational agents
- [NeuroSymbolicOntology](concepts/NeuroSymbolicOntology.md) — 神符号本体注入框架：Retrieval-Augmented Prompting + Logit Biasing
- [AssistanceGames](concepts/AssistanceGames.md) — Assistance Games 形式化框架及其扩展到开放世界 LLM Agent
- [MultimodalIntentDisambiguation](concepts/MultimodalIntentDisambiguation.md) — 多模态意图消歧：跨文本、视觉、语音的歧义消解
- [CognitiveChainOfThought](concepts/CognitiveChainOfThought.md) — 认知 grounded 三阶段推理（感知→情境→规范）
- [SpeechTextDisambiguation](concepts/SpeechTextDisambiguation.md) — 语音-文本消歧：通过语音线索消解文本歧义
- [RecursiveIntentMemory](concepts/RecursiveIntentMemory.md) — 递归意图记忆：跨轮意图级表示而非原始 token 序列
- [ConversationStarterGeneration](concepts/ConversationStarterGeneration.md) — 对话开场语生成：零意图冷启动场景的个性化开场
- [IntentTreeModeling](concepts/IntentTreeModeling.md) — 意图树建模：将对话历史组织为层次化意图结构
- [IntentKeywordBridging](concepts/IntentKeywordBridging.md) — 意图关键词桥接：预测未来轮次意图关键词引导对话走向
- [SemanticIntentSimilarity](concepts/SemanticIntentSimilarity.md) — SIS评测指标：基于Ontology深度的意图语义邻近度度量
- [ProceduralMemory](concepts/ProceduralMemory.md) — 程序性记忆：可学习、可更新、终身化的"如何做"技能知识
- [ParametricMemory](concepts/ParametricMemory.md) — 参数化记忆：经验内化到模型参数而非外部存储
- [OpticalMemoryEncoding](concepts/OpticalMemoryEncoding.md) — 视觉记忆编码：视觉模态高密度经验表示
- [CrossFrameworkMemorySharing](concepts/CrossFrameworkMemorySharing.md) — 跨框架记忆共享：异构Agent无需重训共享经验
- [ProactiveInterventionDecisionChain](concepts/ProactiveInterventionDecisionChain.md) — 主动干预决策链：从检测意图到选择干预的完整流程
- [EchoChamberPassiveActiveBridge](concepts/EchoChamberPassiveActiveBridge.md) — 回声室效应与主动表达桥接：打破被动推荐回声室
- [SimulationRealityGap](concepts/SimulationRealityGap.md) — 真实世界vs合成评测差距：模拟数据高估真实性能
- [AIDABDIStateModel](concepts/AIDABDIStateModel.md) — AIDA-BDI双重状态建模：购买阶段+心理场
- [Memory Forgetting & Staleness](concepts/MemoryForgettingStaleness.md) — 记忆遗忘与过期：隐式冲突+光学遗忘+学习遗忘方向
- [Theory of Mind Reconstruction](concepts/TheoryOfMindReconstruction.md) — 心智理论重建：显式心理状态分解替代行为推断
- [Collective Intent Understanding](concepts/CollectiveIntentUnderstanding.md) — 集体意图理解：从个体到群体共识/矛盾/趋势
- [Proactive Personalized Influencing](concepts/ProactivePersonalizedInfluencing.md) — 主动个性化影响：从推荐到影响/说服
- [Video-Language Intent Recognition](concepts/VideoLanguageIntentRecognition.md) — 视频意图识别：前逆建模两阶段框架
- [Zettelkasten Agentic Memory](concepts/ZettelkastenAgenticMemory.md) — Zettelkasten式自主记忆：动态索引+双向链接+记忆演化
- [ConformalIntentClarification](concepts/ConformalIntentClarification.md) — 共形意图澄清：把分类器不确定度转为有统计保证的候选集+三分支决策
- [OpenWorldIntentDiscovery](concepts/OpenWorldIntentDiscovery.md) — 开放世界意图发现：从未知查询中发现新意图类别，不限于预定义意图集
- [OutOfScopeDetection](concepts/OutOfScopeDetection.md) — 越界意图检测：判断输入是否不属于任何已知意图（开放集识别核心子任务）
- [StructuredUncertaintyClarification](concepts/StructuredUncertaintyClarification.md) — 结构化不确定度澄清：EVPI在工具参数域上量化消歧价值+冗余成本建模
- [BayesianDisambiguation](concepts/BayesianDisambiguation.md) — 贝叶斯消歧：贝叶斯实验设计框架最大化信息增益+元认知推理
- [TurnValidConformalCoverage](concepts/TurnValidConformalCoverage.md) — 轮次有效共形覆盖率：似然比重加权修正反馈协变量偏移，多轮交互保证
- [IntentSimUncertainty](concepts/IntentSimUncertainty.md) — 意图相似度不确定性估计：模拟澄清Q&A→NLI聚类→意图熵，意图空间而非输出空间判断何时澄清
- [PromptBasedUncertaintyDecomposition](concepts/PromptBasedUncertaintyDecomposition.md) — Prompt驱动不确定度分解：分离行动置信度c_t与请求不确定度u_t，纯prompt兼容黑箱API
- [RetrievalAugmentedClarification](concepts/RetrievalAugmentedClarification.md) — 检索增强澄清：RAG将语料库作为外部记忆为澄清问题生成提供证据支撑
- [CognitiveMemoryMechanism](concepts/CognitiveMemoryMechanism.md) — 认知记忆机制：感觉/工作/长期三阶层次化记忆增强意图理解
- [PersistentMemoryClarification](concepts/PersistentMemoryClarification.md) — 持久记忆澄清：跨会话持久化记忆提供上下文消解歧义或触发针对性澄清
- [EvolutionaryMemoryArchitecture](concepts/EvolutionaryMemoryArchitecture.md) — 演化记忆架构：执行-演化双循环实现记忆主动演化，持续改进意图理解

## Syntheses
- [Glossary](glossary.md) — English-Chinese terminology mapping for 3GPP and AI Agent terms
- [论文洞察汇总报告](syntheses/2026-05-28-paper-insight-email.md) — 29篇论文检索与知识库汇总（2026-05-28）
- [应对用户输入模糊/歧义的技术](syntheses/handling-vague-user-input.md) — 五条技术线（澄清先行/多模态消歧/神经符号注入/有原则澄清三剑客/目标推断+防火墙）+ IST 理论支撑
