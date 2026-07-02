---
title: "轨迹取证（Trajectory Forensics）"
type: concept
tags: [agent-explainability, trajectory-forensics, observability, security, closed-loop-verification]
sources: [forensic-trajectory-signatures, agent-tom-monitoring, swe-agent-mindset, redact-traces]
last_updated: 2026-07-02
---

轨迹取证（Trajectory Forensics）指从 agent 执行轨迹中提取行为不变量、心智状态画像和程序性技能特征，用于安全监控、事故归因和行为比较的 techniques。它超越结果级评测，将轨迹作为可观测的经验基底——[[forensic-trajectory-signatures]] 发现记忆投毒攻击在多个独立行为信道上留下分布式签名；[[agent-tom-monitoring]] 用心智理论推理监控隐蔽恶意行为；[[swe-agent-mindset]] 通过观察透镜投影 think-action 链使隐性决策可见。轨迹取证与 [[ExecutionProvenance]] 互补：溯源关注"谁支撑了谁"的依赖结构，取证关注"行为模式偏离了什么基线"的统计/认知信号。相关论文：[[forensic-trajectory-signatures]]、[[agent-tom-monitoring]]、[[swe-agent-mindset]]、[[redact-traces]]、[[agent-traces-to-trust]]。
