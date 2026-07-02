---
title: "验证协同演化（Verification Co-Evolution）"
type: concept
tags: [agent-explainability, verification, reward-hacking, runtime-verification, causal-discovery]
sources: [verification-horizon, grounded-continuation, raider-robot, causalab]
last_updated: 2026-07-02
---

验证协同演化（Verification Co-Evolution）指验证器必须与生成器（策略能力）共同演化、且验证本身面临"可扩展性×忠实度×鲁棒性"三重困境的闭环验证观。[[verification-horizon]] 论证"验证比生成更难"的逆转趋势——每个验证器都只是意图代理，优化扩大代理-意图差距（reward hacking）；[[grounded-continuation]] 以依赖图+四形式主义实现线性时间运行时验证；[[raider-robot]] 覆盖检测→解释→恢复完整闭环；[[causalab]] 揭示预测成功≠因果理解。该概念挑战 AgentLoop 方向3"验证是廉价环节"的假设，将验证定位为需形式化保证（soundness）+经验忠实度（faithfulness）分解的一等公民。相关论文：[[verification-horizon]]、[[grounded-continuation]]、[[raider-robot]]、[[causalab]]、[[causal-past-logic-runtime-verification]]。
