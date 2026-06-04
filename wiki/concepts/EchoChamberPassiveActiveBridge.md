---
title: "回声室效应与主动表达桥接（Echo Chamber & Passive-Active Bridge）"
type: concept
tags: [intent-recommendation]
sources: [pa-bridge]
last_updated: 2026-06-04
---

对话开场语推荐中的回声室效应：封闭曝光-点击循环导致系统偏向流行但泛化的建议，无法捕捉开放世界的动态意图。PA-Bridge 提出利用用户主动表达（自由输入查询）打破回声室，通过对抗分布对齐器弥合被动推荐与主动查询的分布差距，语义离散器使流行度去偏算法可部署。这与 [[ConversationStarterGeneration]]（IceBreaker定义的开场语生成任务）形成互补——PA-Bridge 从推荐角度解决开场语质量问题。

相关论文：[[pa-bridge]], [[icebreaker]], [[ConversationStarterGeneration]]