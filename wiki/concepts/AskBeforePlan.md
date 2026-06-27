---
title: "AskBeforePlan"
type: concept
tags: [intent-recommendation, proactive-planning, multi-agent, clarification-first]
sources: [ask-before-plan]
last_updated: 2026-06-23
---

# 澄清先行（Ask-before-Plan）

澄清先行（Ask-before-Plan）引入主动智能体规划（Proactive Agent Planning） — 要求智能体在制定计划前预测澄清需求、调用工具收集信息，然后再生成计划。CEP（Clarification-Execution-Planning，澄清-执行-规划）多智能体框架将这些角色分离。

## 覆盖的模糊层级（关键边界）

Ask-before-Plan 只覆盖 **L3：意图确定但参数缺失/不可行**。它**不处理 L1（意图本身未知）和 L2（意图多候选歧义）**——假设意图已知（论文用旅行规划域），只处理意图的参数模糊。澄清判据 prompt 原文："needs clarification if the user's intention contains missing or unfeasible details"。

## 模糊的二分类（L3 内部）

- **missing details（缺失）**：出发地、人数、日期、预算等属性被删除
- **unfeasible details（不可行）**：预算低于最低可行值、偏好无匹配等——只能通过环境工具调用发现

## CEP 框架

- **澄清智能体（Clarification Agent）**：基于对话 `C_{t-1}` + 环境观察 `E_{t-1}` 二值判断 `b_t`（是否需澄清）；若 true，针对具体未澄清细节 `d_t` 生成问题 `a_t`
- **执行智能体（Execution Agent）**：调用工具与环境交互（static 一次性 / dynamic 多步 ReAct 式），收集信息反馈给澄清智能体
- **规划智能体（Planning Agent）**：澄清全部完成后，基于完整对话 `C_T` + 环境交互 `E_T` 生成 JSON 计划
- **轨迹调优（Trajectory tuning）**：用 `(C_{t-1}, E_{t-1})` 轨迹微调澄清/执行智能体，自回归训练
- **记忆回溯（Memory recollection）**：累积前轮反思反馈传给下一轮，避免 dynamic 执行重复犯错

## 澄清迭代流程

初始指令 `q0`（含 T 个 indefinite details）→ 按拓扑排序顺序逐轮澄清 → 每轮 Execution 交互得 `E_t`，Clarification 看 `(C_{t-1}, E_t)` 判断是否问 → 迭代**直到所有 indefinite details 被 recovered** → Planning 生成计划。**拓扑排序**处理细节间依赖（如"出发地"未定则无法查"航班"），同优先级随机。

## 环境观察的核心作用

区别于传统纯对话澄清：**unfeasible detail 只能从环境发现**（用户说了预算 $2,401，但只有查环境才知道最低 $2,642）。实验中 environment-only 方法（70.4 Micro Clarif. Acc）超过 conversation-only（62.3），证明环境是更强澄清信号源。

## 与 [[IntentRecommendation]] 的关联

澄清先行是 **澄清先行主动规划（clarification-first proactive planning）** 的奠基工作，确立了智能体应在行动前解决模糊性的原则。这直接支撑了 [[IntentRL]]（深度研究前的主动意图澄清），并通过提供规划骨架补充了 [[PIRABench]]（GUI 上的主动意图推荐）。

## 与 [[NOEM³A]] 的对比

两者处理不同层级的模糊，形成互补：[[NOEM³A]] 处理 L2（多意图歧义，单轮静默选），Ask-before-Plan 处理 L3（参数模糊，多轮主动问）。根本对立：NOEM³A 假定单轮可消歧、"猜"而非"问"；Ask-before-Plan 假定模糊需用户补全、"问"而非"猜"。