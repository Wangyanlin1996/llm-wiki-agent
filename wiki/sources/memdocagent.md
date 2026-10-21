---
title: "MemDocAgent：记忆引导的长程仓库级代码文档生成框架"
type: source
tags: [multi-agent-long-context]
sources: [memdocagent]
source_file: raw/papers/memdocagent.pdf
last_updated: 2026-07-24
arxiv_id: "2605.14563"
authors: ["Suyoung Bae", "Jaehoon Lee", "Changkyu Choi", "YunSeok Choi", "Jee-Hyong Lee"]
year: 2026
venue: "arXiv.org"
citation_count: 0
doi: "10.48550/arXiv.2605.14563"
---

## 概要
MemDocAgent 是一个长程 agentic 框架，在跨越整个仓库的单一集成上下文中生成文档。结合两个组件：(i) Dependency-Aware Traversal Guiding 预定遵守依赖和粒度层次结构的遍历顺序；(ii) Memory-Guided Agentic Interaction，agent 通过 read/write/verify 操作与共享记忆 RepoMemory 交互，积累先前工作痕迹。在多标准评估中超越开源和闭源基线。

## 关键贡献
- 单一集成上下文跨整个仓库生成文档
- Dependency-Aware Traversal + RepoMemory 共享记忆交互
- read/write/verify 操作积累工作痕迹，避免冗余检索和矛盾描述

## 关键引用
> "MemDocAgent, a long-horizon agentic framework that generates documentation within a single, integrated context spanning the entire repository."

## 关联
- [[CodeWiki]] — CodeWiki 用递归多智能体，MemDocAgent 用共享记忆
- [[SharedAgentMemory]] — 共享智能体记忆
- [[MultiAgentLongContext]] — 多智能体长程仓库级处理

## 矛盾
- (暂无)
