---
title: "Agent 循环检测与消解 (Agent Loop Detection and Resolution)"
type: concept
tags: [ontology-loop-detection]
sources: [trove-trace-route-validation, gubernaut-homeostatic-controller, argus-agentic-reasoning-runtime, masc-metacognitive-self-correction, failed-trajectories-harness-flaws]
last_updated: 2026-09-08
---

Agent 循环检测与消解是指识别 LLM agent 执行中的重复/停滞/错误级联模式并触发恢复机制的运行时治理范式。核心失败模式包括：(1) continuation invalidation——中间结果使后续计划失效，agent 要么执行过时步骤要么广泛重规划（[[trove-trace-route-validation]]）；(2) perseveration——agent 卡在重复行为中无法脱困（[[gubernaut-homeostatic-controller]]）；(3) cascading errors——单 agent 错误通过协作结构传播导致系统级崩溃，预实验显示单错误可造成 over 50% 性能下降（[[masc-metacognitive-self-correction]]）；(4) harness flaws——runtime infrastructure 缺陷导致系统性失败，占开发记录的 45.3%（[[failed-trajectories-harness-flaws]]）；(5) underdefined objective——目标无法精确陈述导致 score 不可信任时需要 verified pivoting（[[argus-agentic-reasoning-runtime]]）。关键消解方法：(1) TROVE 的 Retain-Insert-Replace 三操作选择性路由编辑——保留已完成前缀仅修复无效后缀，区别于粗粒度工作流重选和细粒度逐步重规划；(2) Gubernaut 的确定性 arousal 动力学——token-free meta level 使 prompt injection 在构造上不存在攻击通道，arousal 在攻击下积分上升、停止后 valence-gated 机械衰减；(3) MASC 的 Next-Execution Reconstruction 无监督异常检测——从 history 预测下一步 embedding，anomalous steps 因违反 causal consistency 产生更大 deviation；(4) HARNESSFIX 的 HTIR 对齐+scoped repair operators——从失败轨迹诊断 responsible steps 和 failed harness layer 再做 scoped repair；(5) Argus 的 verified pivoting——将目标修正从 goal drift 中区分出来，需 evidence 支持且通过 explicit role boundary 进入。与 [[RuntimeGovernance]]（Round 8）的区别：Round 8 聚焦动作级验证/凭证/治理，本方向聚焦执行循环中的失败检测和恢复机制。与 [[RetrievalStateLockIn]]（Round 16）的呼应：后者诊断检索状态锁定（42% silent errors），本方向提供循环消解的运行时机制。
