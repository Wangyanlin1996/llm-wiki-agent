---
title: "Policy Conflict Detection"
type: concept
tags: [policy, conflict, notification, 5g]
sources: [28556-j00]
last_updated: 2026-05-22
---

## 概要

Policy 冲突检测是 3GPP Policy MnS 中的机制，MnS Producer 将新传入的或更新的 Policy 与先前存储的 Policy 进行冲突检查。当检测到冲突时，Producer 通过 notifyPolicyConflict 通知告知 Consumer。

## 通知: notifyPolicyConflict

| 参数 | 限定符 | 描述 |
|---|---|---|
| objectClass | M | ManagedEntity 类名 |
| objectInstance | M | ManagedElement 实例的 DN |
| notificationId | M | 唯一通知标识符 |
| eventTime | M | 事件发生时间（ITU-T Generalised Time） |
| systemDN | C | 管理服务 Producer 的 DN |
| notificationType | M | "notifyPolicyConflict" |
| conflictDescription | M | Policy 冲突详情（冲突的事件、条件、动作） |

## RESTful HTTP 映射

该通知通过 HTTP POST 交付至 `/notificationSink`，参数映射到请求体中的 JSON 属性（href、notificationId、notificationType、eventTime、systemDN、conflictDescription，以及可选的 correlatedNotifications、additionalText、sourceIndicator、attributeList）。

## 关联

- [[PolicyMnS]] — 执行冲突检测的服务
- [[PolicyIOC]] — 被检查冲突的 Policy 对象
- [[3GPP]] — 定义标准组织