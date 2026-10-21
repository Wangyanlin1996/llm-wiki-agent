---
title: "DS2SC-Agent：芯片模型快速生成的多智能体自动化管线"
type: source
tags: [multi-agent-long-context]
sources: [ds2sc-agent]
source_file: raw/papers/ds2sc-agent.pdf
last_updated: 2026-07-24
arxiv_id: "2603.21190"
authors: ["Yiwei Wu", "Yifan Wu", "Yun Xiong", "Dengwei Zhao", "Jiaxuan Shen", "Jianfei Jiang", "Guanghui He", "Shikui Tu", et al.]
year: 2026
venue: "arXiv.org"
citation_count: 0
doi: "10.48550/arXiv.2603.21190"
---

## 概要
DS2SC-Agent 是首个端到端全自动生成管线，将原始 datasheet 直接转换为 SystemC chiplet 模型。通过解耦复杂建模任务，编排全自动工作流：非结构化长文档解析、SystemC 核心代码构建、测试激励生成和自适应闭环调试。解决了从原始 datasheet 直接可靠代码生成时上下文消失和逻辑幻觉的严重挑战。

## 关键贡献
- 首个端到端 datasheet→SystemC 全自动多智能体管线
- 解耦建模任务：长文档解析 + 代码构建 + 测试生成 + 闭环调试
- 解决非结构化长文档的上下文消失和逻辑幻觉问题

## 关键引用
> "By decoupling the intricate modeling tasks, the proposed pipeline orchestrates a fully automated workflow encompassing unstructured long-document parsing, SystemC core code construction, testbench stimulus generation, and adaptive closed-loop debugging."

## 关联
- [[MultiAgentLongContext]] — 多智能体处理非结构化长文档
- [[UnstructuredLongDocument]] — 非结构化长文档解析
- [[ClosedLoopDebugging]] — 自适应闭环调试

## 矛盾
- (暂无)
