---
title: ProMem：主动记忆提取替代静态摘要
type: source
tags:
- agent-memory
sources:
- promem
source_file: raw/papers/promem.pdf
last_updated: 2026-06-08
arxiv_id: '2601.04463'
authors:
- Chengyuan Yang
- Zequn Sun
- Wei Wei
- Wei Hu
year: 2026
---
## 概要
ProMem 提出"主动记忆提取"替代传统静态摘要。基于循环处理理论指出两大局限：摘要是"提前的"盲目前馈过程（不知道未来任务需求），且提取通常是"一次性的"缺乏验证反馈。ProMem 将提取视为迭代认知过程，引入自问反馈循环：Agent 主动探测对话历史，恢复遗漏信息并纠正错误。

## 关键贡献
- 自问反馈循环：Agent 主动用自我提问探测对话历史而非被动压缩
- 迭代认知过程：提取不再是前馈而是有反馈的循环
- 完整性-成本权衡：显著提升记忆完整性同时保持 token 效率

## 关键引用
> "Summarization is 'ahead-of-time', acting as a blind 'feed-forward' process that misses important details because it doesn't know future tasks" — 对静态摘要的根本批评

## 关联
- [[AgentMemory]] — ProMem 将 Storage→Reflection→Experience 的 Reflection 阶段从被动摘要升级为主动提取
- [[MemCog]] — ProMem 的"主动提取"与 MemCog 的"主动认知"形成互补：提取面向写入端，认知面向读取端
- [[Mem-π]] — ProMem 在写入端主动提取，Mem-π 在读取端主动生成——两端互补

## 矛盾
- ProMem 批评"摘要不知道未来任务"，但 [[EvoMemBench]] 发现长上下文基线仍竞争力强——可能因为长上下文保留了原始信息而非压缩