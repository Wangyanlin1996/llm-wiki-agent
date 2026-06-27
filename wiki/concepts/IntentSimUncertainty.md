---
title: "IntentSimUncertainty"
type: concept
tags: [intent-sim, uncertainty-estimation, clarification, entropy, NLI-clustering, L2-L3]
sources: [clarify-when-necessary]
last_updated: 2026-06-26
---

# IntentSimUncertainty

意图相似度不确定性估计——通过**模拟澄清问答**在**意图空间**（而非输出空间）估计用户意图分布的熵，以此判断是否需要澄清。由 [[ClarifyWhenNecessary]]（Zhang & Choi 2023）提出。

## 核心思想

传统不确定性方法（softmax entropy、semantic entropy）在**输出空间**操作——多个不同输出 = 高熵 = 不确定。但输出不同可能只是"措辞不同"（同一意思的不同表述），不一定是真歧义。

IntentSim 转而在**意图空间**估计熵：先通过澄清问题锁定"歧义点"，再模拟用户回答并聚类为独立意图，最后计算意图簇分布的熵。

**关键洞察**：如果模型是因为"无知"而不确定（epistemic），它**无法生成具体的澄清问题**，或模拟回答是噪声（被 NLI 过滤），自然低熵不触发澄清。只有真歧义（aleatoric）才会产生分散的意图簇。

## 四步算法

### 步骤 1：生成澄清问题（贪心解码）
```
q ← GreedySample(M, [x])    # few-shot prompt 让 LLM 生成一个澄清问题
```
例：输入 "There, on the trunk" → 生成 "What type of trunk are you referring to?"

### 步骤 2：模拟用户回答（温度采样）
```
for i in {1,...,S}:         # S=10
    a_i ← TempSample(M, [x; q], T=0.5)   # LLM 扮演用户，采样 S 个回答
```
例：得到 ["汽车后备箱", "大型储物箱", "大象鼻子", "汽车后部", ...]

### 步骤 3：NLI 聚类（语义等价分组）
用 **DeBERTa-large NLI 模型**（MNLI 微调）两两判断回答是否语义等价：
```
for each pair (a_i, a_j):
    left  = NLI([q; a_i], [q; a_j])   # a_i 蕴含 a_j？
    right = NLI([q; a_j], [q; a_i])   # a_j 蕴含 a_i？
    if left == entailment or right == entailment:
        # 语义等价 → 同一簇
```
DFS 找连通分量 → 每个连通分量 = 一个独立用户意图。

**为何用 NLI 而非 embedding？** 在小样本（S=10）高精度场景下，NLI 的 cross-encoder能更准确判断逻辑关系。Embedding 会把"我赢了"和"我输了"这种结构相似但语义相反的句子拉近，在判断歧义时是致命的。

### 步骤 4：计算意图熵
```
P̂(c|x) = |c| / S         # 每个意图簇的概率
u(x) = Entropy(P̂(·|x))   # 香农熵
```

- **高熵**（回答分散到多个意图簇）→ 真模糊 → **问！**
- **低熵**（回答集中在一个意图簇）→ 有主导解读 → **直接答**

## 与传统不确定性方法的对比

| 方法 | 估计空间 | 歧义检测原理 | 局限 |
|---|---|---|---|
| Softmax entropy | 输出概率 | top-1 确信度低 → 不确定 | 只看 top-1，不区分歧义 vs 无知 |
| Semantic entropy | 输出空间 | 采样多个输出，语义聚类后算熵 | 不同措辞可能被误判为不同语义 |
| **IntentSim** | **意图空间** | **模拟澄清 Q&A → NLI 聚类 → 意图熵** | 延迟高（S=10 采样 + O(S²) NLI） |

## 三子任务框架

IntentSim 是 [[ClarifyWhenNecessary]] 三子任务框架中 **"When"（何时澄清）** 子任务的解法：

| 子任务 | 问题 | 本文方法 |
|---|---|---|
| **When** | 是否需要问用户？ | **IntentSim**（核心贡献） |
| What | 问哪个澄清问题？ | 从候选中选择/生成（本文用 oracle） |
| How | 拿到答案后如何改进？ | 用澄清信息重新推理 |

## 实验结果

- **10% 澄清预算下性能翻倍**（vs 随机选择）
- 在 6 个（任务×模型）设置中 4 个 AUROC 最高
- 跨任务（QA/MT/NLI）和跨模型均持续有效——任务无关

**意外发现**：Q&A 交互比完美指令（disambig）效果更好——chat 模型训练分布更匹配对话格式而非手动改写的生硬长句。

## 局限

1. **延迟灾难**：运行时 S=10 采样 + C(10,2)×2=90 次 NLI 调用，不适合实时对话
2. **需要 oracle 生成澄清问题**：论文 Task 2 用的是 oracle（已知所有解读），实际部署中澄清问题质量无法保证
3. **无统计保证**：只能排序哪些样例需要澄清，不保证"不问就不漏"——这是 [[CICC]] 用共形预测替代的动机

## 谱系定位

```
IntentSim (2023) — 意图空间熵估计，无保证
  ↓
CICC (2024) — 共形预测替代 intent-sim，提供覆盖率 1-α 保证
  ↓
CLARA (2026) — 多轮扩展，turn-valid coverage 修正反馈协变量偏移
```

IntentSim 是"不确定性估计驱动澄清"谱系（谱系B）的起点。

## 关联
- [[ClarifyWhenNecessary]] — 源论文
- [[CICC]] — 直接继承者：用共形预测替代 intent-sim，从"排序"升级为"有统计保证"
- [[CLARA]] — 谱系延续：多轮 turn-valid coverage
- [[SAGE-Agent]] — 谱系A（EVPI）对比：EVPI 排序问题 vs intent-sim 估计意图熵
- [[PromptBasedUncertaintyDecomposition]] — 同为"when to clarify"，但纯 prompt 自报告 vs 模拟采样+NLI
- [[handling-vague-user-input]] — 谱系B 起点，L2-L3 覆盖
- [[IntentSignalTheory]] — intent-sim 的意图熵对应 IST 中 I* 的不确定度
