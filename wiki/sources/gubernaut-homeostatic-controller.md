---
title: "Gubernaut: LLM Agent 的确定性恒温控制器（Deterministic Homeostatic Controller for Affect-Regulated LLM Agents）"
type: source
tags: [ontology-loop-detection]
sources: [gubernaut-homeostatic-controller]
source_file: raw/papers/gubernaut-homeostatic-controller.pdf
last_updated: 2026-09-08
arxiv_id: "2607.24339"
authors: ["Dushyant Sharma"]
year: 2026
venue: "arXiv preprint"
citation_count: 0
---

## 概要
Gubernaut Cognitive Controller (GCC) 是模型无关的运行时控制层，采用 Nelson-Narens 监控-控制循环：object level 读写文本，deterministic meta level（HRL）仅读取数值遥测{intensity, valence, repetition}并返回调节 posture。因 meta level 零 token 输入，prompt injection 对控制器在构造上不存在攻击通道。在 4×4 frontier 模型矩阵的 pre-registered 评估中，regulated arm 在 15/16 格子表现更冷静（13/16 达 p<.05），homeostatic 恢复特征在 4/4 模型家族中复制。

## 解决的问题
LLM agent 继承 reactive failure modes——受挑衅时升级、受奉承时 sycophantic drift、卡住时 perseveration——这些是 behavioral propensity 而非 capability 的失败。Training-time alignment 有两个运行时结构性限制：不透明（无可检查信号解释调节了什么）和纠缠（调节机制与生成机制是同一网络，操纵生成的输入也可操纵调节）。基于第二 LLM pass 的 runtime guardrail 继承同样纠缠——governor 由被治理的 substrate 构成。

## 方法与技术
1. **Nelson-Narens 双级架构**：Object level（IGL 情感评估+EAU 仲裁+PEV 情景记忆+SMM 自我模型）读写文本；Meta level（HRL 确定性控制器）仅读取 3 个数值/turn，返回 posture（调节指令+温度 bound），每 tick 的 {telemetry, state, posture} 全部日志记录。
2. **Arousal 动力学（核心定律）**：provocation drive P = I·max(0,−v)（仅敌意 valence 的 intensity 驱动），arousal 为一阶累积器带恒定衰减 `arousal ← clip(arousal + g·P − d)`，实现持续攻击下积分上升、停止后机械衰减的 homeostatic 特性。
3. **离散 posture 词汇**：DEFAULT（标准温度冷静推理）、INHIBIT（高/spike arousal 时低温钳制，不镜像敌意）、REGROUND（perseveration 检测时重新 grounding）、Recovery window（INHIBIT 后固定 tick 数，valence 非负时指示 fresh engagement）。
4. **Instant trigger**：独立于累积器，单个 intensity≥阈值且负 valence 输入立即触发 INHIBIT。
5. **Pre-registered generate-once/judge-many 协议**：4×4 矩阵，generator 输出一次并 SHA-256 哈希冻结，4 个 judge 各 3-sample panel 评分。

## 创新点
- **Token-free meta level**——控制器输入接口仅接受 3 个数值/tick，无 prompt/context window/text channel，prompt injection 对控制器在构造上不存在攻击通道（vs 基于第二 LLM pass 的 guardrail 继承同样纠缠）。
- **确定性控制定律（无采样/无学习参数）**——给定相同 telemetry 序列，state trajectory 和 posture 序列完全可复现，使 recovery 结果成为机械预测而非统计 artifact。
- **Homeostatic recovery signature**——arousal 在攻击下积分上升、de-escalation 后 valence-gated 机械衰减，stateless 的"stay calm"指令无法产生此动态。
- **Headroom gradient 发现**——控制层效果与 host 内在 reactivity 成反比：GPT-5.5（near-saturated）几乎无 headroom，Gemini 3.5 Flash（最 reactive）增益最大（+1.48）。

## 效果
- Dataset: 4×4 matrix (n=17 per cell) | Metric: cells favoring regulated | Result: 15/16 by sign, 13/16 at p<.05
- Dataset: Gemini×Opus cell | Metric: Δ eval reactivity | Result: +1.80 | t 8.2 | p<.05 (largest effect)
- Dataset: GPT×Gemini cell | Metric: Δ reactivity | Result: −0.04 | n.s. (the single null)
- Judges-avg per cook: Gemini +1.48 (4/4 p<.05) | Opus +0.61 (4/4) | Grok +0.47 (4/4) | GPT +0.10 (1/4)
- Recovery: GPT arousal 0.293→0.222→0.142; full recovery by T8, 4/4 cooks
- Endurance: GPT +0.22; Opus +0.42; Gemini +1.06 (all p<.05)
- **Ablation**: S3 ego-drift reversed on 3/4 cooks; perseveration detection (REGROUND) effective

## 关键引用
> "Training-time methods share two structural limits at runtime. First, they are opaque... Second, they are entangled: the mechanism that moderates behavior is the same network that generates it." — Section 1, p.2

> "The meta level's input interface accepts three numbers per tick. It has no prompt, no context window, and no text channel of any kind: there is no code path by which a token sequence reaches it." — Section 3.3, p.6

> "This is the cleanest and most portable result in the record, and the architecture's signature: a system whose guard rises under attack and then mechanically stands down when the attack ends, with no carried-forward defensiveness." — Section 6.3, p.15

## 关联
- [[RuntimeGovernance]] — Round 8 运行时治理
- [[PolicyContestability]] — Round 8 策略可争议性
- [[TrajectoryForensics]] — Round 8 轨迹取证
- [[trove-trace-route-validation]] — 本轮 TROVE 轨迹路由验证
- [[argus-agentic-reasoning-runtime]] — 本轮 Agent 推理 runtime
