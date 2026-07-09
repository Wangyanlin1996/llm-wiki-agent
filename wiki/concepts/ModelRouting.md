---
title: "模型动态路由（Model Dynamic Routing）"
type: concept
tags: ['model-routing', 'cost-quality-tradeoff', 'heterogeneous-models', 'slo', 'infrastructure-aware']
sources: ["hydra-dynamic-routing", "inframind-infra-aware", "routing-plateau", "recal-reward-calibration", "twinrouterbench-step-routing", "goodserve-goodput-serving"]
last_updated: 2026-07-09
---

模型动态路由解决异构模型池的成本-质量 trade-off 问题。核心挑战：如何在运行时为每个查询选择最合适的模型，平衡质量、成本、延迟。

**六大方向**：
1. **多维能力匹配** — [[HyDRA]] 预测查询的细粒度多维能力需求（推理、代码、调试、工具），与模型 profile 通过 shortfall 匹配，解耦模型身份，iso-quality 省 54.1%。
2. **基础设施感知编排** — [[INFRAMIND]] 让整个多 agent 栈感知实时系统负载，planner 条件化拓扑、executor 每步观察队列深度、scheduler 重排优先级，高负载 99.9% SLO 合规。
3. **路由准确率上限** — [[RoutingPlateau]] 21 种方法×5 基准发现"routing plateau"——多种方法收敛到相似准确率，根因是可预测性瓶颈：路由器学习全局趋势而非实例特定信号。
4. **RL 奖励校准** — [[ReCal]] 分层奖励分解+component-wise advantage estimation+方差感知重加权，解决多目标聚合的模糊信用分配，7 个数据集一致提升。
5. **步级路由评估** — [[TwinRouterBench]] 双轨设计：静态轨 970 个路由可见前缀（确定性评分）+ 动态轨完整 SWE-bench Verified（端到端验证），首次评估 agent 中间步骤路由。
6. **Goodput 优化** — [[GoodServe]] predict-and-rectify 路由：just-enough instance selection + 运行时请求迁移，goodput 提升 27.4%。

**关键发现**：路由准确率存在 plateau——突破需要更大训练数据、更强编码器、端到端微调。从"二元强/弱"→"多维能力匹配"；从"模型路由"→"全栈感知编排"；从"one-shot 评估"→"步级评估"。
