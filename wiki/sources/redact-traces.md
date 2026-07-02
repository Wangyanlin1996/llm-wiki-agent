---
title: "RedAct: Redacting Agent Capability Traces for Procedural Skill Protection（为程序性技能保护脱敏 Agent 能力轨迹）"
type: source
tags: [agent-explainability, trace-redaction, capability-leakage, watermark, accountability-privacy-tradeoff]
sources: [redact-traces]
source_file: raw/papers/redact-traces.pdf
last_updated: 2026-07-02
arxiv_id: "2606.10813"
authors: ["Shuwen Xu", "Zhitao He", "Yi R. Fung"]
year: 2026
venue: "arXiv preprint"
citation_count: pending
---

## 概要

用户依赖执行轨迹观察 agent 行为、诊断失败、确保问责。这些轨迹包含丰富程序性细节（工具调用、中间决策、错误恢复逻辑），却可暴露私有程序性技能——允许下游方法在无模型权重或技能文件访问下恢复关键公式、阈值和策略。为量化此风险并评估保护，本文构建 **CapTraceBench**（75 个长时程任务、154 个跨 7 域策划技能的基准），并引入 **RedAct**——一个受保护轨迹发布框架：定位受保护关键信息、重写轨迹同时保留验证器关键证据、嵌入行为水印用于下游溯源分析。RedAct 将归一化技能迁移（NST）从原始轨迹的 44.7-67.1% 降至无技能基线以下，同时保留审计证据；独立行为水印达 93.6-100.0% 真检测、≤1.9% 误报。

## 关键贡献

- **轨迹作为安全接口**：将公共 agent 轨迹重构为安全接口——为 AgentLoop 方向5（凭证）和方向1（可观测性）的隐私-问责权衡提供框架
- **选择性脱敏保留审计证据**：脱敏关键信息同时保留验证器证据——解决问责与技能保护的张力
- **行为水印溯源**：嵌入水印支持下游溯源——为轨迹凭证提供真实性证明

## 关键引用

> "Public agent traces as security interfaces and show that selective redaction can reduce procedural capability leakage without removing audit evidence."

## 关联

- [[ExecutionProvenance]] — 脱敏轨迹是执行溯源的隐私保护投影
- [[AgentAccountability]] — 问责-隐私权衡是 AgentLoop 治理的关键张力
- [[TrajectoryForensics]] — 行为水印为轨迹取证提供真实性证明
- [[forensic-trajectory-signatures]] — 取证签名（检测）与 RedAct 脱敏（保护）互补
- [[agent-traces-to-trust]] — RedAct 细化了执行溯源综述中"可观测性 vs 隐私"的开放挑战

## 矛盾

揭示"轨迹透明度"的内在张力：问责所需的轨迹细节恰是技能泄露的载体——挑战"越透明越好"的直觉。
