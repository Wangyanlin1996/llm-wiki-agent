---
title: "运行时治理（Runtime Governance）"
type: concept
tags: [agent-explainability, runtime-governance, machine-readable-credential, closed-loop-verification]
sources: [proof-carrying-agent, agentbound, kya-trust-layer, provenance-authorization, agentriskbom, redact-traces]
last_updated: 2026-07-02
---

运行时治理（Runtime Governance）指在 agent 执行期间对其每个动作进行可验证的授权、合规和证据捕获的治理范式，区别于部署时配置或事后审计。其核心是将治理从"必须被信任的过程"转变为"可被独立验证的过程"——通过动作证书（[[proof-carrying-agent]]）、治理回执（[[agentbound]]）、信任评分（[[kya-trust-layer]]）、溯源-授权对齐（[[provenance-authorization]]）和能力物料清单（[[agentriskbom]]）等机器可读凭证实现。这与 synthesis 报告方向5"机器可读解释凭证"的最大空白直接对应——无电信标准当前定义形式化解释序列化，而运行时治理原语提供了桥接 W3C PROV-O 与 3GPP [[IntentReport]] 的工程构件。相关论文：[[proof-carrying-agent]]、[[agentbound]]、[[kya-trust-layer]]、[[provenance-authorization]]、[[agentriskbom]]、[[redact-traces]]、[[blockchain-accountability-agents]]。
