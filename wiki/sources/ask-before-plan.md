---
title: Ask-before-Plan
type: source
tags:
- intent-recommendation
- proactive-planning
- multi-agent
- EMNLP
date: 2024-06-18
source_file: raw/papers/ask-before-plan.pdf
last_updated: 2026-06-23
arxiv_id: '2406.12639'
authors:
- Xuan Zhang
- Yang Deng
- Zifeng Ren
year: 2024
venue: EMNLP 2024 Findings
citation_count: 12
doi: 10.18653/v1/2024.findings-emnlp.636
---
## 概要
Ask-before-Plan（EMNLP 2024 Findings）引入 Proactive Agent Planning（主动式智能体规划），要求 agents 预测澄清需求、调用工具获取信息并生成规划。CEP（Clarification-Execution-Planning，澄清-执行-规划）多 agent 框架配合 trajectory tuning（轨迹调优）和 memory recollection（记忆回溯）在 Ask-before-Plan benchmark 上超越基线方法。

## 覆盖的模糊层级（关键边界）

**只覆盖 L3：意图确定但参数缺失/不可行**。不处理 L1（意图本身未知）和 L2（意图多候选歧义）——假设意图已知（旅行规划域），只处理意图的参数模糊。澄清判据 prompt 原文（附录）：
> "A request needs clarification if the user's intention contains missing or unfeasible details based on the tool parameters and call results"

## 模糊的二分类（L3 内部）

基于 TravelPlanner 数据集构造，每条指令注入 0–3 个 indefinite details（10% 无模糊，30% 各 1/2/3 个），11 种类型：

- **missing details（欠定/缺失）**：从完整指令删除属性——origin、destination by arrival days、number of people、duration、departure date、budget
- **unfeasible details（过定/不可行）**：穷举环境值选无匹配的改写——accommodation/cuisine/transportation preferences、destination by arrival days、budget（低于最低可行预算）

两类澄清策略不同：缺失→补全，不可行→协商。**unfeasible 只能通过环境工具调用发现**（用户说了预算但只有查环境才知道不可行）。

## 核心论点
- 主动式 agents 应在模糊指令上先提问再规划
- CEP 多 agent 框架分离澄清、执行和规划
- 澄清判据需结合**对话 + 环境观察**，不只看对话（核心创新）
- 拓扑排序按依赖顺序安排澄清（如"出发地"未定则无法查"航班"）
- Trajectory tuning + memory recollection 改善主动式规划
- 新 benchmark 用于真实主动式规划评估

## CEP 框架与迭代流程

三 agent 分工：
- **Clarification Agent**：基于 `(C_{t-1}, E_{t-1})` 二值判断 `b_t`（是否需澄清）；若 true，针对 `d_t` 生成问题 `a_t`
- **Execution Agent**：调用工具与环境交互（static 一次性 / dynamic 多步），收集信息反馈给澄清智能体
- **Planning Agent**：澄清全部完成后，基于 `C_T` + `E_T` 生成 JSON 计划

迭代流程：初始指令 `q0`（含 T 个 indefinite details，已拓扑排序）→ 每轮 Execution 交互得 `E_t`，Clarification 看 `(C_{t-1}, E_t)` 判断 → **迭代直到所有 indefinite details 被 recovered** → Planning 生成计划。停止条件不是固定轮数，而是全部模糊点被澄清。

## Trajectory Tuning（§4.1）

**动机**：直接 prompt LLM 让它"该问就问"效果差——LLM 不会自发澄清用户意图（Deng et al., 2023b），工具调用易幻觉（Li et al., 2024b），即使 instruction tuning 或精心设计 prompt 也不够。

**方法**：用轨迹 `(C_{t-1}, E_{t-1})` 微调 Clarification Agent 和 Static Execution Agent。按拓扑顺序采样 t-1 个细节构造 `C_{t-1}`，从 ground truth 派生 `E_{t-1}`，构造序列 `[f_prompt(C_{t-1}, E_{t-1}, b_t), a_t|b_t=1]` 并 tokenize 为 `x_t`。自回归训练：

```
L = max_θ (1/T) Σ_{t=1}^{T} Σ_{i=1}^{N_t} log P_θ(x_i^t | x_{<i}^t)
```

其中 θ 为模型参数，T 为总对话轮数，N_t 为第 t 轮 token 数。

**两步分离**：
1. Clarification Need Prediction：生成布尔值 `b_t` 预测是否需澄清
2. Clarification Question Generation：若 `b_t=true`，针对细节 `d_t` 生成问题 `a_t`

## Memory Recollection（§4.2）

**动机**：Dynamic Execution Agent 用 Reflexion 时，多轮对话中可能遇到**相似类型的异常**并**重复生成相同 rationale**，增加推理时间且引入噪声。

**机制**：累积前轮反思反馈跨轮复用。给定第 t 轮对话 `C_t`，执行智能体基于前序交互 `E_{t-1}^i` 和记忆库 `R_t^i` 生成工具调用 `f_i`：
```
f_i = LLM(C_t, E_{t-1}^i, R_t^i)
```
若 `f_i` 无效，生成 rationale `r_i` 存入 `R_t^{i+1}`：
```
R_t^{i+1} = R_t^i          if f_i is valid
            concat(R_t^i, r_i)  else
```
**跨轮累积**：`R_{t+1} = R_t`——因 `C_t` 跨轮共享已澄清细节，记忆复用避免重复犯错并降低推理时间。

## Static vs Dynamic Execution（§4）

两种执行智能体与环境交互模式：

| 维度 | Static（静态） | Dynamic（动态） |
|---|---|---|
| 推理方式 | 一次性生成完整工具调用链 `E_t` | 多步推理，每步一个 action |
| 输入 | 当前对话 `C_t` | `C_t` + 前序交互历史 `E_{t-1}^i` |
| 训练 | Trajectory Tuning | 无微调，用 Memory Recollection |
| 框架类比 | — | ReAct / Reflexion 式 |
| 适用 | 简单工具链 | 复杂多步推理 |

## 依赖图与拓扑排序（§3.1, Appendix A.1）

Indefinite details 间有**依赖关系**（如"出发地"未定则无法查"航班"）。论文构建**依赖图**（Figure 5），用拓扑排序重排细节顺序，按依赖优先级澄清。同优先级随机处理。

依赖图节点为 Missing Details 和 Unfeasible Details，边表示"必须先澄清 A 才能检测/澄清 B"。例：budget (missing) → budget (unfeasible)，因为只有先知道用户预算才能检测是否低于最低可行值。

## Baseline 方法对比

| 方法 | 描述 | 特点 |
|---|---|---|
| Proactive (GPT-3.5) | 纯对话主动澄清 | 倾向过度澄清，无环境观察 |
| ProCoT (GPT-3.5) | 对话+CoT | 倾向直接执行不澄清（幻觉） |
| Direct (GPT-3.5/Mistral/LLaMA) | 直接 prompt | 无法区分是否需澄清 |
| ICL (GPT-3.5) | In-context learning | 需预测好但问题生成差 |
| Environment-only | 仅环境观察 | 过度澄清但优于纯对话 |
| ReAct / Reflexion | 动态推理基线 | 长 context 下性能骤降 |
| **CEP** | 三 agent + trajectory tuning + memory recollection | 结合对话+环境，精准判断 |

## 关键引述
> "Proactive agents should ask before planning on ambiguous instructions" — 核心原则

> "This process continues iteratively until all indefinite details have been recovered by the clarification agent" — 停止条件

> "predicting a binary label b_t, indicating the need for clarification based on the vagueness and feasibility of environmental responses E_{t-1}" — 澄清判据需环境观察

## 关键实验结论

- Clarification Need Prediction：CEP (LLaMA-3-8B) 99.4 Micro / 98.2 Macro Acc
- environment-only（70.4）> conversation-only（62.3），证明环境是更强澄清信号源
- w/o Clarification：Planning Final Pass Rate 0；w/ Clarification：0.1（TravelPlanner 本身极难）——澄清是规划的前置必要条件
- 过度澄清风险：conversation-only 和 environment-only 都倾向过度问，CEP 结合两者精准判断

## 关联
- [[IntentRecommendation]] — 主动式规划作为意图推荐
- [[AskBeforePlan]] — 引入的 CEP 框架
- [[IntentRL]] — 强化学习与 trajectory tuning 相关
- [[PIRABench]] — 主动式意图推荐评测基准关联
- [[NOEM³A]] — 互补关系：NOEM³A 处理 L2（多意图歧义，静默选），Ask-before-Plan 处理 L3（参数模糊，主动问）
- [[handling-vague-user-input]] — 模糊输入三层层级框架中，本方法覆盖 L3