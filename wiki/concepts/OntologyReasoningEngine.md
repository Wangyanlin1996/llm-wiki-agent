---
title: "本体推理引擎（Ontology Reasoning Engine）"
type: concept
tags: [ontology-reasoning, reasoning-engine]
sources: [syntactic-simplification-owl, dl-ontologies-probabilistic-circuits, datalogmtl-seminaive-materialisation, meteror-metric-temporal-reasoning, datalog-first-class-facts]
last_updated: 2026-10-09
---

本体推理引擎是在形式本体上执行演绎推理（物化/查询回答/蕴含检查）的可扩展基础设施层，覆盖 tableau 演算、基于后果（consequence-based）演算、规则/Datalog 物化以及新近的神经编译路线。传统符号推理器（HermiT/Pellet/FaCT++）在大型表达性本体（SROIQ）上扩展性差，Datalog 系引擎（VLog/RDFox/Soufflé）以物化换取可扩展但受限于规则语言表达力。2022-2026 的引擎工作沿四条主线推进：时序算子支持（[[meteror-metric-temporal-reasoning]] 覆盖完整 DatalogMTL、[[datalogmtl-seminaive-materialisation]] 用半朴素物化消除冗余）、树形数据结构表达力（[[datalog-first-class-facts]] 的 DL∃!/Slog 用一等事实 + 通信避免并行）、句法层无损化简（[[syntactic-simplification-owl]] 的 CES 减少类表达式长度与推理开销）、可微编译（[[dl-ontologies-probabilistic-circuits]] 把本体编译为概率电路在 GPU 上快 3 个数量级）。引擎能力决定了上游 Agent/检索/时序应用的推理预算。相关论文：[[meteror-metric-temporal-reasoning]]、[[datalogmtl-seminaive-materialisation]]、[[datalog-first-class-facts]]、[[syntactic-simplification-owl]]、[[dl-ontologies-probabilistic-circuits]]
