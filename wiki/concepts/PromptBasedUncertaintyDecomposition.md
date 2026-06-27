---
title: "PromptBasedUncertaintyDecomposition"
type: concept
tags: [uncertainty-decomposition, prompt-based, action-confidence, request-uncertainty, clarification, black-box-api, L2-L3]
sources: [uncertainty-decomposition-clarification]
last_updated: 2026-06-26
---

# PromptBasedUncertaintyDecomposition

Prompt 驱动不确定度分解——将单一置信度标量拆分为**行动置信度**（`c_t`）和**请求不确定度**（`u_t`），使 LLM agent 在任务规格模糊时主动请求澄清。纯 prompt 驱动，无需训练，兼容黑箱 API。由 [[UncertaintyDecompositionClarification]]（Matsnev 2026）提出。

## 核心思想

现有 prompt-based 方法（ReAct+UE、UAM）让 agent 输出单一置信度标量 `c_t`，**混淆了两种本质不同的不确定度**：

| 不确定度来源 | 含义 | 正确响应 |
|---|---|---|
| 行动难选 | 多个相似产品可选，不确定选哪个 | 谨慎执行（继续推理） |
| 请求模糊 | "find me a shirt" 未指定颜色尺码 | **请求用户澄清** |

单一标量无法区分两者——低置信度可能是"模型蠢"也可能是"问题模糊"，但只有后者值得问用户。

**解法**：分解为两个语义独立的信号：
- **Action confidence `c_t`** ∈ [0,1]：agent 对所选行动推动任务完成的置信度
- **Request uncertainty `u_t`** ∈ [0,1]：用户目标是否被完整规格化（0=完整，1=关键细节缺失）

**澄清触发**：`if u_t ≥ θ: request_clarification else: execute a_t`

## 打分规则

### u_t（请求不确定度）—— 三点锚定量表

| 值 | 含义 |
|---|---|
| 0 | 用户请求有唯一合理解读 |
| 0.5 | 存在未说出的偏好（如颜色未指定但有默认） |
| 1 | 多种合理解读，关键细节缺失 |

配合 "Be meticulous" 自检指令要求 agent 仔细审查。

### c_t（行动置信度）—— 自由 [0,1]

连续标量，无锚点，纯 verbalized confidence。实验显示**系统性过度自信**（ECE 0.24-0.66）。

## Prompt 结构

```
System message
  + Next-action block（任务指令 + 行动空间）
  + History-entry template:
      <u_request>u_t</u_request>
      <u_request_explanation>...</u_request_explanation>
      <action>a_t</action>
      <action_confidence>c_t</action_confidence>
  + Confidence elicitation suffix
```

**关键**：字段顺序 `u_t` 在 `a_t` 之前——确保**在承诺行动前先评估规格完整性**，给 agent 一个专用通道处理目标模糊性。

与基线 UAM 的唯一区别：prompt 中新增 `<u_request>` + `<u_request_explanation>` 两个 tag。无训练、无多采样、无 few-shot。

## 历史传播

将 `(u_t, c_t, 解释)` 全部写回 agent 历史 `H_{t+1}`，允许后续步骤推理累积不确定度——继承 UAM 的"语义传播"策略，但传播的是**双信号**而非单标量。

## 轨迹级聚合（四种策略）

| 聚合 | 公式 | 特点 |
|---|---|---|
| last | `S = s_T` | 仅最后一步 |
| avg | `S = mean(s_1...s_T)` | 均值 |
| max | `S = max(s_1...s_T)` | 峰值 |
| product | `S = ∏ s_t` | 几何均值 |

**重要发现**：product 聚合在 ALFWorld 上 ROC-AUC 最高，但这是**轨迹长度混淆**——失败任务更长，几何均值随 T 递减。用随机 U(0,1) 替换真实置信度也能达到同等 ROC-AUC。product 不是"好信号"，而是"长度代理"。

## 规格不确定度 vs 模型不确定度

本方法的核心分离与 [[SAGE-Agent]] 的规格/模型不确定度分离对应：

| 不确定度 | 本方法 | SAGE-Agent |
|---|---|---|
| 规格不确定度 | `u_t`（prompt 自报告） | 参数域信念 `B(t)` 中未指定参数 |
| 模型不确定度 | `c_t`（prompt 自报告） | LLM 预测能力限制 |
| 建模方式 | 纯 prompt，LLM 自评 | 结构化参数域显式建模 + EVPI |

两者共享"分离规格/模型不确定度"的洞察，但实现路径完全不同。

## 实验结果

### 澄清寻求（核心指标）
- F1 **+73%** over ReAct+UE，**+36%** over UAM
- WebShop-Clarification 每个后端均领先
- ALFWorld-Clarification 5 个后端中 4 个领先

### 能力稀释（副作用）
| 方法 | 平均成功率 |
|---|---|
| ReAct+UE | 28.6% |
| UAM | 27.8% |
| Proposed | 27.0% |

更多不确定度仪表化 → 成功率单调下降 1.6pp。原因：prompt 更长更复杂 → 分散模型注意力。

### 校准（结构性问题）
所有方法、所有基准、所有后端的可靠性图均**低于对角线**——预测置信度系统性高于实际成功率。这是 prompt-based 自报告置信度的**结构性偏差**：agent 已承诺行动后有"自我合理化"倾向。

## 局限

1. **系统性过度自信**：ECE 0.24-0.66，prompt-based 自报告置信度不可靠
2. **能力稀释**：prompt 复杂化降低原始任务成功率 1.6pp
3. **无统计保证**：不保证"不问就不漏"——与 [[CICC]] 的共形保证对比是关键差距
4. **product 聚合误导**：看似优秀的聚合策略实为轨迹长度代理
5. **u_t 依赖 LLM 自评质量**：无外部校准，与 [[IntentSimUncertainty]] 的模拟采样+NLI 聚类相比缺乏客观基础

## 关联
- [[UncertaintyDecompositionClarification]] — 源论文
- [[SAGE-Agent]] — 同为"分离规格/模型不确定度"，但 SAGE-Agent 在参数域显式建模 + EVPI，本方法纯 prompt 自报告
- [[IntentSimUncertainty]] — 同为"when to clarify"，但 intent-sim 用模拟采样+NLI 聚类 vs 本方法用 LLM 自评 u_t
- [[CICC]] — 同属"有原则澄清"谱系，CICC 有统计保证而本方法无
- [[StructuredUncertaintyClarification]] — 对比：结构化 EVPI 在参数域 vs prompt 自报告在语言空间
- [[handling-vague-user-input]] — prompt-based 澄清的实践派代表，L2-L3 覆盖
- [[IntentSignalTheory]] — u_t 对应 IST 中 I* 规格完整性的不确定度
