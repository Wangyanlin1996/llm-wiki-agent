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

### AI Agent — Agent Explainability
- [A Survey on Large Language Model based Autonomous Agents](sources/llm-autonomous-agent-survey.md) — LLM自主智能体统一架构综述；解释列为可信度核心维度；Frontiers of CS 2024, 3137 citations (2024)
- [AgentBench: Evaluating LLMs as Agents](sources/agentbench.md) — 8环境多维度agent评测基准；长程推理/决策/指令遵循为失败主因；ICLR 2024, 951 citations (2024)
- [AgentVerse: Facilitating Multi-Agent Collaboration](sources/agentverse.md) — 动态重组多智能体协作框架；社会行为涌现；ICLR 2024 (2024)
- [Explainable Human-AI Interaction: A Planning Perspective](sources/explainable-human-ai-interaction.md) — "解释即规划"范式；心智模型对齐；顺应/改变人类期望；Morgan & Claypool 2024 (2024)
- [From Agent Traces to Trust](sources/agent-traces-to-trust.md) — 执行溯源+证据追踪分类法综述；过程级问责统一框架 (2026)
- [HANSEL: Interactive Verification of Web Agent Trajectories](sources/hansel-web-agent-verification.md) — 交互式证据导航；83.7% precision/88.8% recall；轨迹体积-61.6% (2026)
- [Causal Past Logic for Runtime Verification](sources/causal-past-logic-runtime-verification.md) — 分布式LLM agent运行时验证；向量时钟监控器；验证嵌入协调语言 (2026)
- [Three-Level Framework for LLM-Enhanced XAI](sources/three-level-llm-xai.md) — 三层XAI（算法/领域→以人为中心→社会）；LLM跨层中介；Information Systems Frontiers 2025 (2025)
- [Explainable AI, but explainable to whom?](sources/explainable-ai-to-whom.md) — 利益相关者星座；差异化解释需求；COVID-19 ICU案例 (2021)
- [Towards Responsible and Explainable AI Agents](sources/responsible-explainable-ai-agents.md) — 多模型共识+推理层治理；异构LLM/VLM独立生成→结构化整合 (2025)
- [Blockchain Accountability for Autonomous Agents](sources/blockchain-accountability-agents.md) — 区块链防篡改黑箱+LLM生成解释；ROS移动机器人三场景验证 (2024)
- [The Argument is the Explanation](sources/argument-is-the-explanation.md) — 结构化论证图；可验证推理链；自动幻觉检测；AAEC 94.44 F1 (2025)
- [Causal Explanations for Sequential Decision Making Under Uncertainty](sources/causal-explanations-sequential-uncertainty.md) — SCM因果解释基础；单一框架多语义解释；MDP因果推理 (2022)
- [TRiSM for Agentic AI](sources/trism-agentic-ai.md) — AMAS信任/风险/安全管理综述；TRiSM五支柱；CSS+TUE新指标 (2025)
- [CEMA: Causal Explanations for MAS](sources/cema-causal-explanations-mas.md) — 不假设固定因果结构；反事实世界模拟；AAMAS 2024；HEADD数据集 (2023)
- [TriEx: Tri-View Framework for Multi-Agent LLMs](sources/triex-multi-agent-llm-explanation.md) — 三视角（自我推理/信念状态/预言机审计）；揭示说/信/做不匹配；ACL 2026 (2026)
- [AXIS: Counterfactual Explanations for MAS](sources/counterfactual-mas-explanation.md) — LLM盘问模拟器生成反事实解释；正确性+7.7%；目标预测+23% (2025)
- [Toward Policy Explanations for MARL](sources/policy-explanations-marl.md) — MARL策略解释基础；策略摘要+语言解释；IJCAI 2022 (2022)

### AI Agent — Closed-Loop Interpretability (Round 8)
- [Forensic Trajectory Signatures for Agent Memory Poisoning Detection](sources/forensic-trajectory-signatures.md) — 记忆投毒行为不变量；AUC 0.9904；过确定签名；前缀仅实时阻断 (2026)
- [Agent-ToM: Monitor Autonomous LLM Agents via Theory-of-Mind](sources/agent-tom-monitoring.md) — ToM推理监控隐蔽恶意行为；Reason-Verify-Refine；语义护栏记忆 (2026)
- [Projecting the Emerging Mindset of SWE Agent](sources/swe-agent-mindset.md) — 观察透镜投影think-action链；408轨迹；导航/证据/接地/停止可见 (2026)
- [Looking Is Not Picking: Attention-Segment Account of Tool-Selection Failures](sources/looking-not-picking.md) — 看对却选错；读出而非感知瓶颈；免训练选择器+11.9分 (2026)
- [SkillCAT: Contrastive Assessment and Topology-Aware Skill Self-Evolution](sources/skillcat.md) — 对比因果提取+评估增强演化+拓扑感知路由；+40.40% (2026)
- [VADAOrchestra: Neurosymbolic Orchestration of Adaptive Reasoning Workflows](sources/vadaorchestra.md) — LLM编排+Datalog+/-符号引擎；可验证推理轨迹；KR 2026 (2026)
- [Grounded Continuation: Linear-Time Runtime Verifier for LLM Conversations](sources/grounded-continuation.md) — 依赖图+四形式主义8更新操作；线性时间；无冲突保证 (2026)
- [The Verification Horizon: No Silver Bullet for Coding Agent Rewards](sources/verification-horizon.md) — 验证比生成更难逆转；可扩展性×忠实度×鲁棒性三重困境 (2026)
- [RAIDER: Tool-Equipped LLM Agent for Action Issue Detection, Explanation and Recovery](sources/raider-robot.md) — Ground-Ask&Answer-Issue；检测→解释→恢复完整闭环 (2025)
- [CausaLab: Scalable Environment for Interactive Causal Discovery](sources/causalab.md) — SCM采样因果发现；预测成功≠因果理解；92%任务准确率vs 0.471 F1 (2026)
- [Machine-Coached Policy Revision: Controller-Level Contestability Layer](sources/contestability-layer.md) — 可废止规则+诊断→修订闭环；策略可争议性 (2026)
- [From Code-Centric to Intent-Centric Software Engineering](sources/intent-centric-se.md) — 反思性主题分析；意图规格化+验证+溯源+治理问责 (2026)
- [Proof-Carrying Agent Actions: Model-Agnostic Runtime Governance](sources/proof-carrying-agent.md) — 动作证书+5检查点；跨运行时一致治理；外部性感知 (2026)
- [AgentBound: Verifiable Behavioral Governance for Autonomous AI Agents](sources/agentbound.md) — 三权威保守组合；密码学可验证治理回执；常设委托 (2026)
- [KYA: Framework-Agnostic Trust Layer with Verifiable Provenance](sources/kya-trust-layer.md) — 5原语信任层；15+框架适配；only-tighten组合代数；亚毫秒 (2026)
- [Aligning Provenance with Authorization: Dual-Graph Defense](sources/provenance-authorization.md) — AuthGraph注入推理图vs授权图对齐；参数源级检测；40%→1% (2026)
- [AgentRiskBOM: Risk-Scoping Security Bill of Materials](sources/agentriskbom.md) — Agent安全BOM；JSON-schema；16能力维度14分vs SBOM 1分；IEEE Cyber-AI 2026 (2026)
- [RedAct: Redacting Agent Capability Traces for Procedural Skill Protection](sources/redact-traces.md) — 轨迹脱敏+行为水印；NST降至基线下；审计证据保留 (2026)

### Semantic Retrieval — Round 9 (2024-2026)
- [DREAM: 自回归建模统一稠密检索 (2024)](sources/dream-dense-retrieval.md) — 自回归query建模替代双编码器；MS MARCO nDCG@10=0.441 (2024)
- [Scaling Dense Retrieval: LLM标注训练数据挖掘 (2024)](sources/scaling-dense-retrieval.md) — 从LLM标注挖掘高质量训练数据；SIGIR 2026 E-Commerce Workshop (2024)
- [Coder-Constraint Retrieval: 约束感知代码检索 (2025)](sources/coder-constraint-retrieval.md) — 约束感知检索器；代码检索新范式 (2025)
- [RAG Comprehensive Survey: 检索增强生成综述 (2025)](sources/rag-comprehensive-survey.md) — retriever/generator/hybrid/robust四类架构分类法 (2025)
- [Beyond Parameters Survey: ICL→RAG→GraphRAG→CausalRAG演进 (2025)](sources/beyond-parameters-survey.md) — RAG范式演进路径全景综述 (2025)
- [RAG Security & Privacy: 三阶段安全威胁 (2025)](sources/rag-security-privacy.md) — 检索/上下文构建/生成三阶段安全与隐私综述 (2025)
- [RAG Evaluation Survey: RAG评估方法 (2025)](sources/rag-evaluation-survey.md) — 系统性能/事实准确性/安全/计算效率四维评估 (2025)
- [Telecom ORAG: 电信场景混合检索+神经路由 (2025)](sources/telco-orag.md) — 3GPP检索+Web混合+神经路由；45%内存节省；开源LLM达GPT-4水平 (2025)
- [BM25 Corrective RAG: 金融文档BM25超越稠密检索 (2025)](sources/bm25-corrective-rag.md) — BM25+神经重排两阶段；Recall@5=0.816 (2025)
- [HAKARI-Bench: 五族检索模型统一对比 (2025)](sources/hakari-bench.md) — 稀疏/稠密/混合/重排/LLM五族统一基准 (2025)
- [TeleEmbedBench: 电信领域嵌入基准 (2025)](sources/teleembedbench.md) — 电信首个嵌入基准；LLM embedder显著优于sentence-transformer (2025)
- [LLM2Vec-Gen: 生成式嵌入 (2025)](sources/llm2vec-gen.md) — 在LLM输出空间直接生成嵌入；推理时无额外编码 (2025)
- [PromptEmbedder: 双LLM软提示解耦嵌入知识 (2025)](sources/promptembedder.md) — 软提示解耦嵌入知识与主干权重 (2025)
- [HTEB: 更难的嵌入基准 (2025)](sources/hteb-harder-embedding-bench.md) — MTEB多维度动态鲁棒性扩展 (2025)
- [Coverage Not Averages: 语义分层检索评估 (2025)](sources/coverage-not-averages.md) — 评估形式化为统计估计；形式化覆盖保证 (2025)
- [Rare-Redundancy Eval: 高冗余语料评估 (2025)](sources/rare-redundancy-eval.md) — 原子事实分解+冗余感知评估；ACL 2026 (2025)
- [Is GraphRAG Needed? 9种RAG场景对比 (2025)](sources/is-graphrag-needed.md) — 检索-生成差距；扩展检索不比例提升生成质量；ACL 2026 GEM Workshop (2025)
- [Multimodal GraphRAG: 视觉富文档知识图谱 (2025)](sources/multimodal-graphrag.md) — GraphRAG扩展到多模态视觉富文档 (2025)
- [Ex-GraphRAG: 可解释图检索 (2025)](sources/ex-graphrag.md) — M-GNAN精确分解节点贡献；可解释性 (2025)
- [OMD-GraphRAG: 本体引导提取 (2025)](sources/omd-graphrag.md) — 本体引导提升领域特定实体/关系精度 (2025)
- [Reasoning Agentic RAG Survey: System 1 vs System 2 (2025)](sources/reasoning-agentic-rag-survey.md) — 预定义推理管线vs自主工具编排双范式 (2025)
- [R2-Searcher: 多跳推理检索-推理边界校准 (2025)](sources/r2-searcher.md) — 多跳推理中检索-推理边界校准 (2025)
- [KBSD Knowledge Boundary: 知识边界校准三决策 (2025)](sources/kbsd-knowledge-boundary.md) — 信任记忆/依赖检索/弃答三决策 (2025)
- [MetaResearcher: 对抗虚拟环境+自反思RL (2025)](sources/metaresearcher.md) — 对抗虚拟环境扩展深度研究能力 (2025)
- [SimpleSearch-VL: 多模态agentic搜索 (2025)](sources/simplesearch-vl.md) — 仅需5K SFT+2K RL实现多模态agentic搜索 (2025)
- [ARMOR: 电信查询侧检索器自适应优化 (2025)](sources/armor-telecom-retriever.md) — 查询侧检索器自适应优化；低资源电信场景 (2025)
- [Cog-RAG: 认知启发主题对齐双超图 RAG (2025)](sources/cog-rag.md) — 主题超图+实体超图；认知两阶段检索；AAAI 2026 (2025)

### Ontology Applications in HCI — Round 10 (2021-2026)
- [OPI: 本体引导证据路径推理用于多跳KGQA](sources/opi-ontology-kgqa.md) — 关系中心本体图+双向检索+迭代精炼 (2026)
- [ORT: 本体引导逆向思维增强KGQA](sources/ort-ontology-reverse-kgqa.md) — 逆向思维从目的到条件构建推理路径 (2025)
- [ORACLE: 本体驱动多跳推理框架](sources/oracle-ontology-multihop.md) — 动态本体构建→FOL推理链→子问题分解 (2025)
- [MultiCube-RAG: 本体立方体多跳问答](sources/multicube-rag-multihop-qa.md) — 正交多维本体立方体；查询分解-征服 (2026)
- [Better Later Than Sooner: 本体引导后提取纠错KG构建](sources/neuro-symbolic-kg-ontology.md) — 神经符号KG；嵌入规范化；SPARQL查询 (2026)
- [KML: 程序化视频问答神经符号知识推理](sources/kml-procedural-video-qa.md) — 神经知识模块组合推理；COIN本体+ConceptNet (2025)
- [TITAN: 网络威胁情报图可执行推理](sources/titan-graph-reasoning-cti.md) — TITAN本体(MITRE)；路径规划器+图执行器 (2025)
- [KG表示用于LLM政策合规推理](sources/kg-policy-compliance.md) — 两种本体schema；LLM自发现schema匹配形式化本体 (2026)
- [LOM: 面向企业知识管理大本体模型](sources/lom-large-ontology-model.md) — 双层本体；construct-align-reason三阶段；4B超越DeepSeek (2026)
- [QIME: 本体驱动可解释医学嵌入](sources/qime-ontology-embeddings.md) — 每维度对应临床yes/no问题；免训练嵌入 (2026)
- [VLK-RL: LLM知识验证RL跨域TOD](sources/vlk-rl-cross-domain-tod.md) — 约束验证→本体对齐slot-value→RL策略 (2026)
- [TeQoDO: Text-to-SQL TOD本体构建](sources/teqodo-tod-ontology.md) — LLM用SQL自主从零构建TOD本体 (TACL 2025)
- [Better Slow than Sorry: 正摩擦提升对话可靠性](sources/positive-friction-dialogue.md) — 正摩擦本体；策略性减速提升任务成功率 (2025)
- [约束CoT解码的对话本体关系抽取](sources/dialogue-ontology-relation-extraction.md) — CoT多分支解码+本体约束；降幻觉 (SIGDIAL 2024)
- [OPAL: 本体感知预训练端到端TOD](sources/opal-ontology-aware-tod.md) — 本体三元组恢复+下一文本生成预训练 (TACL 2022)
- [D3ST: 描述驱动任务型对话建模](sources/d3st-description-driven-tod.md) — schema描述替代名称；index-picking零样本迁移 (2022)
- [本体增强Slot Filling](sources/ontology-enhanced-slot-filling.md) — 跨轮本体实体匹配；约束检查 (2021)
- [零样本开放词汇对话理解管线](sources/zero-shot-open-vocab-dst.md) — DST即QA；不依赖固定本体值域 (NAACL 2025)
- [Beyond Ontology: 无本体目标导向DST](sources/beyond-ontology-dst.md) — 指令调优+VGAE；无预定义本体DST SOTA (ICKG 2024)
- [NLU++: 多标签细粒度本体TOD NLU数据集](sources/nlu-plus-plus.md) — intent模块化；跨域复用 (NAACL 2022)
- [HEAR: 分层超图本体企业Agent推理器](sources/hear-hypergraph-enterprise.md) — 基础图层+超边层；证据驱动推理循环 (2026)
- [OntoBOT: 服务机器人任务/动作/环境/能力统一本体](sources/ontobot-robotics-ontology.md) — 扩展SOMA/DOLCE；能力推理；四agent评估 (2025)
- [Husky: 统一开源语言Agent多步推理](sources/husky-language-agent.md) — 统一动作本体+专家模型执行；7B匹配GPT-4 (2024)
- [KG任务就绪性基准: 本体驱动Gap/Overlap分析](sources/kg-gap-overlap-benchmark.md) — TBox+ABox；SPARQL场景；可审计 (2026)
- [知识驱动对话流管理: 社交机器人本体](sources/knowledge-grounded-dialogue-flow.md) — 话题本体+对话管理算法；100人评估 (2022)
- [SocialDial: 社交感知对话系统基准](sources/socialdial-socially-aware.md) — 社交规范本体；本体驱动合成数据生成 (SIGIR 2023)
- [处理不一致KG推理: 综述](sources/inconsistency-kg-reasoning-survey.md) — 三方向：检测/修复/容忍推理 (2025)
- [LLM与KG交互研究趋势: 综述](sources/llm-kg-research-trends.md) — KG QA/本体生成/验证；LLM-KG协同分类法 (2024)

### LLM Inference Optimization — Round 11 (2025-2026)

#### A. 上下文优化 (Context Optimization)
- [CoACT: 动作保持的观测压缩](sources/coact-action-preserving-compression.md) — NAP原则：压缩后下一步动作一致；token -33% (2026)
- [SmoothAgent: 前瞻上下文工程](sources/smoothagent-lookahead-context.md) — 段可分解性+异步预计算KV；TTFT -11.9x (2026)
- [Latent Context Compilation](sources/latent-context-compilation.md) — Disposable LoRA编译长上下文为buffer token；16x压缩 (2026)
- [Cross-Family Speculative Prefill](sources/cross-family-speculative-prefill.md) — 跨模型族注意力估计压缩prompt；免训练 (ICLR 2026 WS)
- [MiA-Signature: 全局激活签名](sources/mia-signature-activation.md) — 次模函数选择高层概念；条件信号近似全激活 (2026)
- [PRISM: 意图感知记忆检索](sources/prism-intent-memory-retrieval.md) — 图结构记忆联合检索-压缩；训练免；10x更小预算更高准确率 (2026)

#### B. Prompt 优化 (Prompt Optimization)
- [APEX: 动态数据选择](sources/apex-dynamic-data-selection.md) — Easy/Hard/Mixed分层+frontier采样；+11.2% (2026)
- [Prompt Codebooks (PCO)](sources/prompt-codebooks-pco.md) — 离散本能词汇表+per-instance路由；+30.36pp vs零样本 (2026)
- [SPEAR: 代码增强Agent式优化](sources/spear-code-augmented-prompt.md) — CodeAct范式优化器+Python错误分析；BBH-7 0.938 (EMNLP 2026)
- [MO-CAPO: 多目标成本感知](sources/mo-capo-multi-objective.md) — 联合优化性能+部署成本；发现trade-off解集 (2026)
- [MASPO: 多Agent联合Prompt优化](sources/maspo-joint-mas-prompt.md) — 联合评估机制+进化beam search；+2.9 (ICML 2026)
- [PRISM: Prompt可靠性工程](sources/prism-prompt-reliability.md) — 持续可靠性+自动测试+漂移检测；99%可靠性 (2026)

#### C. 执行调度优化 (Execution Scheduling)
- [SAGA: 工作流原子化调度](sources/saga-workflow-scheduling.md) — 程序级调度+KV复用预测+公平性；1.64x加速 (2026)
- [DynAMO: 动态资产管理编排](sources/dynamo-asset-orchestration.md) — Plan-then-Execute+依赖感知并行；延迟-1.6x (2026)
- [Co-Coder: 内聚感知任务分区](sources/co-coder-task-partitioning.md) — 图分区+社区检测+通信-计算tradeoff；2.10x加速 (2026)
- [Agent JIT Compilation](sources/agent-jit-compilation.md) — JIT编译常用规划模式+按需执行 (2026)
- [TypeGo: OS式Agent运行时](sources/typego-os-runtime.md) — LLM移出关键路径+Skill Kernel+speculative streaming；延迟-50% (2026)
- [模型原生计算架构 (ICA)](sources/model-native-architecture.md) — 六层架构+双平面+三个Amdahl启发式 (2026)

#### D. 缓存复用 (Cache Reuse)
- [SAECache: 语义感知淘汰](sources/saecache-semantic-eviction.md) — 多队列+在线学习token权重；756x复用率差异；TTFT 1.4-2.7x (2026)
- [Leyline: KV缓存编辑指令](sources/leyline-kv-directives.md) — 声明式4-tuple+闭式RoPE校正；solve rate +14.3pp (2026)
- [TokenDance: 集体KV共享](sources/tokendance-collective-sharing.md) — KV Collector+Diff-Aware Storage；17.5x压缩 (2026)
- [PRISM: 调度-内存协同](sources/prism-scheduling-memory.md) — QAS+DART联合设计；P99 TTFT -37.1% (2026)
- [有状态推理多Agent工具调用](sources/stateful-inference-multi-agent.md) — O(Δ_t) delta-only+持久KV+推测解码；4.2x加速 (2026)
- [KV Policy: RL淘汰](sources/kv-policy-learning-evict.md) — Per-head RL agent学习淘汰策略；零推理开销 (ICML 2026)
- [VeriCache: 无损压缩](sources/vericache-lossless-compression.md) — 压缩KV草拟+全KV验证；4x吞吐；输出完全相同 (2026)

#### E. 模型动态路由 (Model Dynamic Routing)
- [HyDRA: 混合动态路由](sources/hydra-dynamic-routing.md) — 多维能力匹配+shortfall算法；iso-quality省54.1% (2026)
- [INFRAMIND: 基础设施感知编排](sources/inframind-infra-aware.md) — 全栈感知+层次化CMDP；高负载99.9% SLO (2026)
- [The Routing Plateau](sources/routing-plateau.md) — 21方法×5基准发现路由准确率上限；可预测性瓶颈 (2026)
- [ReCal: RL路由奖励校准](sources/recal-reward-calibration.md) — 分层奖励分解+方差感知重加权；7数据集一致提升 (2026)
- [TwinRouterBench: 步级路由基准](sources/twinrouterbench-step-routing.md) — 双轨设计(静态+动态)；首次评估agent中间步骤路由 (2026)
- [GoodServe: Goodput优化服务](sources/goodserve-goodput-serving.md) — Predict-and-rectify+请求迁移；goodput +27.4% (2026)

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

### Agent Explainability
- [Agent Explainability](concepts/AgentExplainability.md) — Agent可解释性：覆盖推理/工具/决策/闭环的多维解释，而非仅单步输出
- [Explainable Planning](concepts/ExplainablePlanning.md) — 可解释规划：解释即规划范式，对齐回路中人类心智模型
- [LLM Autonomous Agent](concepts/LLMAutonomousAgent.md) — LLM自主智能体：感知-规划-记忆-工具-行动统一架构
- [Execution Provenance](concepts/ExecutionProvenance.md) — 执行溯源与证据追踪：agent执行类型化图+证据支撑投影；过程级问责基础
- [Stakeholder Explainability](concepts/StakeholderExplainability.md) — 利益相关者分层解释：多元受众差异化解释需求；三层XAI框架
- [Causal Explanation](concepts/CausalExplanation.md) — 因果解释：SCM/反事实模拟为序贯决策提供"为什么"的因果回答
- [Structured Argumentation](concepts/StructuredArgumentation.md) — 结构化论证解释：论证图+每步推理可验证+自动幻觉检测
- [Multi-Agent Explainability](concepts/MultiAgentExplainability.md) — 多智能体可解释性：MAS协作/竞争/涌现行为的解释方法
- [Agent Accountability](concepts/AgentAccountability.md) — Agent问责架构：区块链防篡改+共识治理+可验证论证
- [Consensus-Driven Reasoning](concepts/ConsensusDrivenReasoning.md) — 共识驱动推理：异构模型独立生成→分歧暴露→结构化整合

### Agent Explainability (Round 8)
- [Runtime Governance](concepts/RuntimeGovernance.md) — 运行时治理：动作级可验证授权/合规/证据捕获，凭证驱动而非信任驱动
- [Trajectory Forensics](concepts/TrajectoryForensics.md) — 轨迹取证：行为不变量+心智画像+技能特征，超越结果级的安全监控
- [Neurosymbolic Orchestration](concepts/NeurosymbolicOrchestration.md) — 神经符号编排：LLM灵活规划+符号可验证执行+对比选择归因
- [Verification Co-Evolution](concepts/VerificationCoEvolution.md) — 验证协同演化：验证器须与生成器共演化；可扩展×忠实×鲁棒三重困境
- [Policy Contestability](concepts/PolicyContestability.md) — 策略可争议性：可废止规则+诊断→修订闭环；解释/质疑/重评
- [Intent-Centric Accountability](concepts/IntentCentricAccountability.md) — 意图为中心问责：问责基线从动作上移到意图规格化+验证+溯源

### Semantic Retrieval Concepts
- [稠密检索 Dense Retrieval](concepts/DenseRetrieval.md) — 神经编码器向量空间相似度检索；从双编码器到自回归建模与约束感知
- [检索增强生成 RAG](concepts/RetrievalAugmentedGeneration.md) — retrieve→augment→generate核心范式；从ICL到CausalRAG演进
- [混合检索 Hybrid Retrieval](concepts/HybridRetrieval.md) — 稀疏+稠密融合；BM25在特定领域仍超越SOTA稠密检索
- [嵌入模型 Embedding Models](concepts/EmbeddingModels.md) — 从对比学习双编码器到生成式嵌入与软提示解耦
- [检索评估 Retrieval Evaluation](concepts/RetrievalEvaluation.md) — 超越nDCG/Recall@k的多维统计估计与冗余感知评估
- [知识图谱检索 GraphRAG](concepts/GraphRAG.md) — 知识图谱增强检索支持多跳推理；可解释性与本体引导
- [Agent驱动检索 Agentic Retrieval](concepts/AgenticRetrieval.md) — LLM Agent自主决定何时/检索什么/如何反思；System 1 vs System 2
- [主题对齐双超图检索](concepts/ThemeAlignedDualHypergraph.md) — 主题超图+实体超图双结构；认知两阶段检索；跨chunk主题对齐

### Ontology in HCI Concepts
- [本体引导KGQA](concepts/OntologyGuidedKGQA.md) — 利用本体类型约束和关系层次引导KG问答推理路径搜索
- [动态本体构建](concepts/DynamicOntologyConstruction.md) — LLM根据任务/查询自动推断和构建本体结构
- [神经符号知识模块](concepts/NeuroSymbolicKGModule.md) — KG关系类别学习为可组合神经模块+符号引擎执行
- [动作本体Agent](concepts/ActionOntologyAgent.md) — 本体定义动作/任务空间结构化agent行为规划和执行
- [本体感知TOD](concepts/OntologyAwareTOD.md) — 利用本体slot类型/值域/约束结构化对话状态追踪和响应生成
- [对话状态追踪本体](concepts/DialogueStateTrackingOntology.md) — 本体定义的slot/值域/约束用于DST表示、更新和验证
- [正摩擦本体](concepts/PositiveFrictionOntology.md) — 对话系统策略性减速行为的结构化分类
- [LLM-KG本体协同](concepts/LLMKGOntologySynergy.md) — LLM与KG/本体双向增强：生成/验证/推理

### LLM Inference Optimization
- [上下文优化 Context Optimization](concepts/ContextOptimization.md) — 五大范式：动作保持/前瞻工程/潜在编译/跨族推测/激活签名
- [Prompt优化 Prompt Optimization](concepts/PromptOptimization.md) — 六大方向：动态数据/离散codebook/Agent式/多目标/多Agent/持续可靠性
- [执行调度优化 Execution Scheduling](concepts/ExecutionScheduling.md) — 工作流级调度+OS类比+图分区+JIT编译
- [缓存复用 Cache Reuse](concepts/CacheReuse.md) — 语义淘汰/缓存编辑/集体共享/调度协同/有状态/RL策略/无损压缩
- [模型动态路由 Model Routing](concepts/ModelRouting.md) — 多维能力匹配/基础设施感知/路由上限/RL校准/步级评估/goodput
- [推测解码 Speculative Decoding](concepts/SpeculativeDecoding.md) — 草拟-验证范式扩展到预填充和缓存压缩

## Syntheses
- [Glossary](glossary.md) — English-Chinese terminology mapping for 3GPP and AI Agent terms
- [论文洞察汇总报告](syntheses/2026-05-28-paper-insight-email.md) — 29篇论文检索与知识库汇总（2026-05-28）
- [应对用户输入模糊/歧义的技术](syntheses/handling-vague-user-input.md) — 五条技术线（澄清先行/多模态消歧/神经符号注入/有原则澄清三剑客/目标推断+防火墙）+ IST 理论支撑
- [电信自智网络闭环可解释性深度研究报告](syntheses/closed-loop-explainability-telecom-autonomous-networks.md) — 6方向技术沙箱（意图理解/Skill编排/闭环溯因/交互解释/机器可读凭证/评估保障）×15篇引用
