---
title: "XFlow：可靠多智能体工作流的可执行协议编程系统"
type: source
tags: [multi-agent-long-context]
sources: [xflow-multi-agent]
source_file: raw/papers/xflow-multi-agent.pdf
last_updated: 2026-07-24
arxiv_id: "2606.14790"
authors: ["Hanqi Li", "Jing Peng", "Zijian Wang", "Lu Chen", "Kai Yu"]
year: 2026
venue: "arXiv preprint"
citation_count: 0
doi: ""
---

## 概要
XFlow 占据 prompt-only 编排和标记式工作流描述之间的中间位置。XPF 协议格式作为文学协议可读，但被编译并作为程序执行。通过生命周期管理的符号（typed state cells with validation and commit states）处理不确定性，actor 输出在被中介后才成为共享状态。实验覆盖约束交互、长上下文推理和智能体软件工程，显示 XFlow 通过使约束、证据处理和流程要求显式可执行来提升可靠性。

## 关键贡献
- XPF 协议编程语言：可读文学协议 + 可编译执行的程序
- 生命周期管理符号：typed state cells with validation/commit states
- 约束/证据/流程要求显式可执行，长上下文推理实验验证

## 关键引用
> "XFlow occupies a middle position between prompt-only orchestration and markup-like workflow descriptions. XPF remains readable as a literate protocol, but it is compiled and executed as a program."

## 关联
- [[MultiAgentWorkflowReliability]] — 多智能体工作流可靠性
- [[ExecutableProtocol]] — 可执行协议编程
- [[MultiAgentLongContext]] — 多智能体长上下文推理的可靠性保障

## 矛盾
- (暂无)
