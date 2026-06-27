---
title: "持久记忆澄清（Persistent Memory Clarification）"
type: concept
tags: [memory-intent-clarification, persistent-memory]
sources: [janus, fairy-gui-agent]
last_updated: 2026-06-27
---

持久记忆澄清是指利用持久化记忆（跨会话保持的用户上下文、历史交互、核心记忆）增强模糊/欠明确意图的澄清能力。核心洞察是：模糊意图的歧义往往源于缺乏上下文，而持久记忆可以提供缺失的上下文来消解歧义，或在上下文不足时触发有针对性的澄清。

[[janus]]（JANUS）在 HRI 场景中用持久记忆三层架构从欠明确请求恢复——记忆提供用户上下文，内部言语验证参数完整性并决定是否澄清。[[fairy-gui-agent]]（Fairy）的 Runtime Goal Refinement 用知识约束精炼+人在环澄清确保意图对齐，Evolutionary Memory Architecture 提供跨会话的记忆演化支撑。与 [[AskBeforePlan]] 的"澄清先于执行"同构，但增加了持久记忆作为澄清决策的信息源。与 [[RecursiveIntentMemory]]（OnePred）的递归意图记忆互补——后者在轮次间维护意图级表示，持久记忆澄清在会话间维护用户级上下文。
