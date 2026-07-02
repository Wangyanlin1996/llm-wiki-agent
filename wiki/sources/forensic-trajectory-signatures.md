---
title: "Forensic Trajectory Signatures for Agent Memory Poisoning Detection（Agent 记忆投毒的轨迹取证签名）"
type: source
tags: [agent-explainability, trajectory-forensics, memory-poisoning, closed-loop-verification]
sources: [forensic-trajectory-signatures]
source_file: raw/papers/forensic-trajectory-signatures.pdf
last_updated: 2026-07-02
arxiv_id: "2606.30566"
authors: ["Jun Wen Leong"]
year: 2026
venue: "arXiv preprint (companion to arXiv:2605.08442)"
citation_count: pending
---

## 概要

本文发现 LLM agent 在持久记忆投毒（persistent memory poisoning）下存在一个**行为不变量**：在通过可观测记忆工具调用检索路由信息的架构中，成功的攻击必然在 `email_send_email` 之前调用 `memory_recall_fact`——这是非窃密会话极少出现的转移。该不变量源于攻击的信息检索依赖（而非经验相关），抑制它即破坏攻击。仅凭此不变量的简单规则即达 AUC=0.9563；基于 19 个轨迹特征的随机森林分类器将其提升至 AUC=0.9904，且签名是**过确定的**（移除全部 recall 相关特征后 AUC 仍 0.990）。

## 关键贡献

- **行为不变量作为可观测信号**：记忆投毒攻击在多个独立行为信道上留下分布式轨迹签名，而非单一异常——支撑 AgentLoop 闭环验证层的可观测性
- **前缀仅变体支持实时阻断**：strictly prefix-only 变体达 AUC=0.934，表明实时阻断可行（性能中度退化）
- **取证边界可区分攻击类型**：记忆信道攻击（score 0.956）vs 提示注入攻击（score 0.541）产生不同轨迹，事件响应者可仅凭工具调用日志区分

## 关键引用

> "The signature is overdetermined: removing all recall-related features (half the feature set) leaves AUC unchanged at 0.990, confirming that memory poisoning induces a distributed trajectory signature rather than a single observable anomaly."

## 关联

- [[ExecutionProvenance]] — 轨迹签名是执行溯源在安全维度的投影
- [[AgentAccountability]] — 取证签名为事故归因提供可观测证据
- [[AgentExplainability]] — 行为不变量是过程级可解释性的安全实例
- [[TrajectoryForensics]] — 本文是该概念的代表实现
- [[agent-traces-to-trust]] — 与执行溯源综述的过程级问责框架互补

## 矛盾

无已知矛盾。
