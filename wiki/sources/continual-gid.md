---
title: 'Continual Generalized Intent Discovery: Marching Towards Dynamic and Open-world
  Intent Recognition'
type: source
tags:
- intent-discovery
- open-world
- continual-learning
- OOD
- L1-unknown-intent
date: 2023-10-16
source_file: raw/papers/continual-gid.pdf
last_updated: 2026-06-23
arxiv_id: '2310.10184'
authors:
- Xiaoshuai Song
- Yutao Mou
- Keqing He
year: 2023
venue: ACL 2023
doi: 10.48550/arXiv.2310.10184
---
## 概要
CGID（Continual Generalized Intent Discovery）扩展 GID 到持续学习场景：不再假设所有已知和未知意图数据同时可用，而是**增量地在不同阶段发现新意图**。解决真实世界中意图逐步涌现的动态需求，面向动态开放世界意图识别。

## 覆盖的模糊层级

**覆盖 L1（意图本身未知）**。与 GID 的区别：GID 是一次性发现，CGID 是**多阶段持续发现**——更接近真实场景（用户需求逐步涌现，非一次性全部出现）。

## 核心论点
- GID 假设所有数据同时可用，不满足真实世界的动态需求
- 意图发现应是增量的：新意图在不同阶段逐步涌现
- 持续发现面临**灾难性遗忘**挑战：学习新意图时不能忘记旧意图

## 核心机制：PLRD

提出 **PLRD**（Prototype-guided Learning with Replay and Distillation）方法，由主模块（encoder + joint classifier）和三个子模块组成：

1. **Memory module（数据回放）** — 每个学习阶段结束后，memory module M 为每个类存储极少量样本（IND 阶段按真标签、OOD 阶段按伪标签，默认 n=5）。下一阶段训练时，每个 batch 从 M 取等量旧类样本与新类样本一起输入 BERT，防止灾难性遗忘。相比 GID 存全量数据，PLRD 仅存极小比例样本，**有隐私优势**。
2. **Class prototype module（伪标签引导）** — 通过线性投影层构建类原型，为新 OOD 样本生成伪标签，缓解 OOD 噪声传播。
3. **Feature distillation（特征蒸馏）** — 对 encoder 做特征蒸馏，进一步缓解旧类灾难性遗忘。

Joint classifier 由 old class head 与 new class head 组成；每个阶段结束后 new head 合并入 old head，下一阶段创建新维度的新 head。

### 关键边界：Memory module ≠ 智能体记忆

PLRD 的 memory module 属于 **continual learning 的 replay buffer**（训练态、参数空间），**不是智能体运行态记忆**：

| 维度 | PLRD Memory module M | 智能体记忆（agent memory） |
|---|---|---|
| 存什么 | 训练样本（每类 5 条） | 对话历史、用户偏好、经验轨迹 |
| 何时用 | 模型**训练**阶段 | 智能体**推理/运行**阶段 |
| 目的 | 防止梯度更新覆盖旧类参数 | 跨会话经验积累、检索复用 |
| 范式 | Replay-based Class-Incremental Learning | Episodic / Semantic / Working memory |
| 可见性 | 对用户透明，无交互 | 影响智能体行为决策 |

因此 CGID 在 L1 路线中是最接近"记忆"的机制，但层级在模型参数空间而非 agent 认知空间——**不构成对 L1 智能体记忆能力空白的填补**。

## 关联
- [[IntentUnderstanding]] — CGID 是意图理解中的持续开放世界发现
- [[handling-vague-user-input]] — 覆盖 L1，持续发现新意图
- [[GID]] — 前序工作：GID 的一次性发现 → CGID 的持续发现
