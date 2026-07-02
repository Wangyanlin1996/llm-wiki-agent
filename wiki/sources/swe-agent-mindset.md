---
title: "Projecting the Emerging Mindset of SWE Agent（SWE Agent 涌现心智的投影）"
type: source
tags: [agent-explainability, behavioral-profiling, trajectory-analysis, observability]
sources: [swe-agent-mindset]
source_file: raw/papers/swe-agent-mindset.pdf
last_updated: 2026-07-02
arxiv_id: "2606.08500"
authors: ["Zhengyi Zhuo", "Yan Liu"]
year: 2026
venue: "arXiv preprint"
citation_count: pending
---

## 概要

软件工程 agent（SWE agent）通过工具中介轨迹在真实代码库中工作，但其行为难以用具体可观测术语刻画——轨迹记录了工具使用、中间推理、证据选择和自主停止，却不解释为何选择特定动作、信任了什么证据、何时判定理解充分。本文引入 **Ada**，一个限定范围的代码理解装置：通过有界工具接口进入真实代码库，选择查看何处、精读什么、何时整合部分理解、何时关闭对仓库的认知账户。通过观察透镜投影 think-action 链，使导航、证据选择、综合、接地和停止变得可见，而不将行为归约为原始工具计数或臆测隐藏意图。

## 关键贡献

- **忠实可重放轨迹作为行为研究基底**：将轨迹数据从"有限且有价值"转化为可比较的行为画像经验基底
- **观察透镜使隐性决策可见**：导航/证据选择/综合/接地/停止五个透镜，不臆测隐藏意图——直接支撑 AgentLoop 信息转换节点的可观测性
- **408 条轨迹跨模型/仓库/任务族**：揭示效率、轨迹多样性、认知接地和干预边界的差异

## 关键引用

> "Faithful, replayable traces can become an empirical substrate for studying agent behavior when interpreted through disciplined observation."

## 关联

- [[ExecutionProvenance]] — 观察透镜是执行溯源的行为画像投影
- [[AgentExplainability]] — 使"为何选择"可见是过程级解释的核心
- [[TrajectoryForensics]] — 行为画像为轨迹取证提供比较基线
- [[agent-traces-to-trust]] — 与执行溯源综述的"过程级问责"目标一致

## 矛盾

无已知矛盾。
