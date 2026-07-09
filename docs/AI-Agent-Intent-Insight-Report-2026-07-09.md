# LLM 推理与服务优化 — Round 11 日报

**日期**: 2026-07-09  
**论文数**: 31 篇 (全部 2025-2026)  
**概念页**: 6 个新增  
**PDF**: 31 个新增  
**健康检查**: ✅ 0 空文件, 0 索引同步问题

---

## 总览

本轮聚焦 **LLM 推理与服务优化**，覆盖 agent 系统优化的完整链路。31 篇论文按 5 个方向组织，从单 token 级的上下文压缩到集群级的 GPU 路由，构建了全栈优化图谱。

| 方向 | 论文数 | 核心范式 |
|---|---|---|
| A. 上下文优化 | 6 | 文本压缩→动作保持→段可分解预计算→LoRA编译→跨族推测→激活签名 |
| B. Prompt优化 | 6 | 全局字符串→动态数据分层→离散codebook→Agent式→多目标→持续可靠性 |
| C. 执行调度 | 6 | 请求级→工作流级→图分区→JIT编译→OS式runtime→统一架构 |
| D. 缓存复用 | 7 | LRU均匀→语义感知→缓存编辑→集体共享→调度协同→有状态→RL策略→无损压缩 |
| E. 模型路由 | 6 | 二元强/弱→多维能力匹配→基础设施感知→路由上限→RL校准→步级评估→goodput |

---

## A. 上下文优化 (Context Optimization)

### 核心问题
LLM agent 迭代交互中 observation 不断累积，成为推理成本主要来源。现有压缩方法不建模压缩对 agent 后续行为的影响。

### 六篇论文

| # | 论文 | 问题 | 方法 | 效果 |
|---|---|---|---|---|
| 1 | CoACT (2607.02911) | 压缩后 agent 可能做出不同动作 | NAP 原则：压缩后下一步动作必须一致；teacher 生成候选→NAP 过滤→长度选择→训练压缩器 | token -33%, 效果接近未压缩 |
| 2 | SmoothAgent (2607.00151) | context 变换使 KV cache 失效, TTFT 暴涨 | 段可分解性：前缀变换独立于未来 token；lookahead 异步预计算变换后 KV | TTFT -11.9x |
| 3 | Latent Context (2602.21221) | TTT 修改权重产生有状态参数阻碍并发 | 从"适应"到"编译"：disposable LoRA 蒸馏为 buffer token；自对齐优化无需合成 QA | 16x 压缩保持推理能力 |
| 4 | Cross-Family (2603.02631) | speculative prefill 假设同族模型 | 跨族注意力估计：Qwen/LLaMA/DeepSeek 互为 draft-target | 免训练, 保留 90-100% |
| 5 | MiA-Signature (2605.06416) | 全局激活计算不可行 | 次模函数选择高层概念构成激活签名；条件信号近似全激活 | 多个长上下文任务一致提升 |
| 6 | PRISM (2605.12260) | 长时程记忆累积超窗口 | 图结构记忆联合检索-压缩：Bundle Search+Edge Costing+Compression+Intent Routing | 10x 更小预算更高准确率 |

### 关键洞察
**行为保持优于信息保留** — CoACT 的 NAP 原则标志着上下文优化的范式转换：衡量标准不是保留多少信息，而是 agent 后续行为是否一致。

---

## B. Prompt 优化 (Prompt Optimization)

### 核心问题
自动 prompt 优化存在搜索空间巨大、评估成本高、泛化性差、忽略成本和可靠性等问题。

### 六篇论文

| # | 论文 | 问题 | 方法 | 效果 |
|---|---|---|---|---|
| 7 | APEX (2606.11459) | 静态数据集浪费评估预算 | Easy/Hard/Mixed 动态分层；addressable + rank-sensitive frontier 采样 | +11.2% (5000 次预算) |
| 8 | Prompt Codebooks (2605.28360) | 全局字符串脆弱不可复用 | 离散"本能"词汇表；per-instance 路由；min-max 联合训练 | +30.36pp vs 零样本 |
| 9 | SPEAR (2605.26275) | 固定管线无法结构化错误分析 | CodeAct 范式优化器：4 工具+Python sandbox 做混淆矩阵/错误聚类 | BBH-7 0.938 vs GEPA 0.628 |
| 10 | MO-CAPO (2605.18869) | 只优化性能忽略成本 | 部署导向成本目标（完整计算特征）；多目标发现 trade-off 解集 | 12 case 中 8 个更优 |
| 11 | MASPO (2605.06623) | 局部 agent 目标≠全局系统目标 | 联合评估机制：看 prompt 促进下游 agent 成功的能力；进化 beam search | 平均 +2.9, 无需标签 |
| 12 | PRISM (2605.15665) | LLM 行为漂移导致 prompt 回归 | 持续可靠性工程：自动生成测试→模拟多轮→judge→诊断→外科手术修复 | 99% 可靠性, 2 天→30 分钟 |

### 关键洞察
**优化器从固定管线→agent 式自主决策** — SPEAR 将优化器本身 agent 化，自主编写 Python 做错误分析。**评估从一次性→持续监控** — PRISM 将 prompt 工程转为持续可靠性工程。

---

## C. 执行调度优化 (Execution Scheduling)

### 核心问题
GPU 调度器将每个 LLM 调用视为独立，在步骤间丢弃 GB 级中间状态，端到端延迟膨胀 3-8x。

### 六篇论文

| # | 论文 | 问题 | 方法 | 效果 |
|---|---|---|---|---|
| 13 | SAGA (2605.00528) | 请求级调度丢弃中间状态 | 程序级调度：Agent Execution Graph 预测 KV 复用+session-affinity batching+Agent Fair Share | 1.64x 加速, 99.2% SLO |
| 14 | DynAMO (2606.19382) | 串行执行延迟高 | Plan-then-Execute：SequentialWorkflow+ParallelWorkflow 依赖感知并发 | 延迟 -1.6x |
| 15 | Co-Coder (2606.00953) | 通信开销抵消并行化增益 | 图分区：依赖图→hub 隔离→社区检测分区→依赖感知调度 | pass +14%, 2.10x 加速 |
| 16 | Agent JIT (2605.21470) | 多步规划累积延迟 | JIT 编译：识别高频规划模式→预编译模板→运行时匹配直接执行 | 降低规划延迟 |
| 17 | TypeGo (2607.05482) | LLM 在关键路径上与实时控制矛盾 | OS 式 runtime：多时间尺度异步循环+Skill Kernel+speculative streaming+fast first-action | 每步 -50%, 首动作 -73% |
| 18 | ICA (2606.00288) | 各层缺乏统一架构模型 | 六层架构+双平面（概率执行+确定性控制）+三个 Amdahl 启发式 | 统一设计框架 |

### 关键洞察
**OS 类比是统一设计语言** — LLM=CPU、KV cache=处理器缓存、上下文窗口=主存、agent 框架=OS。调度粒度从请求级→工作流级→程序级。

---

## D. 缓存复用 (Cache Reuse)

### 核心问题
Agent 工作负载打破 chatbot 假设：缓存不是仅追加的、token 不是均匀的、prompt 不是一次性的。

### 七篇论文

| # | 论文 | 问题 | 方法 | 效果 |
|---|---|---|---|---|
| 19 | SAECache (2605.18825) | LRU 均匀对待缓存块 | 多队列架构+语义感知 token 权重+全自适应在线学习 | TTFT 1.4-2.7x, 756x 复用率差异 |
| 20 | Leyline (2606.01065) | Agent 需要主动编辑缓存 | 声明式 4-tuple+闭式 RoPE 旋转校正；in-place splice / prefix-trimmed re-prefill | cache-hit +11.2pp, solve +14.3pp |
| 21 | TokenDance (2604.03143) | 多 agent All-Gather 产生冗余 KV | KV Collector 集体复用（成本只付一次）+Diff-Aware Storage 块稀疏 diff | 17.5x 压缩, 2.7x 并发 |
| 22 | PRISM (2605.08581) | 调度与 KV 管理不对齐 | QAS+DART 联合设计：请求接入与精确前缀 KV 保留对齐 | P99 TTFT -37.1% |
| 23 | Stateful (2605.26289) | 每轮从头重新处理 85-95% 相同 prompt | O(n_t)→O(Δ_t) delta-only；持久 KV 跨轮+radix 扩展+推测解码 | 35 轮 4.2x 加速 |
| 24 | KVPolicy (2602.10238) | 启发式淘汰是间接代理 | RL 问题：per-head agent 学习淘汰策略；仅用 key/value 向量训练 | 零推理开销, 零样本泛化 |
| 25 | VeriCache (2605.17613) | 有损压缩导致代码/工具灾难性失败 | 草拟-验证：压缩 KV 草拟+全 KV 验证；并行执行+长草拟范围 | 4x 吞吐, 输出完全相同 |

### 关键洞察
**Agent 工作负载打破所有 chatbot 假设** — 缓存需要主动编辑（Leyline）、集体共享（TokenDance）、跨轮持久（StatefulInference）。从"LRU 均匀淘汰"→"语义感知+学习驱动"。

---

## E. 模型动态路由 (Model Dynamic Routing)

### 核心问题
异构模型池成本差异跨数量级，路由准确率存在上限。

### 六篇论文

| # | 论文 | 问题 | 方法 | 效果 |
|---|---|---|---|---|
| 26 | HyDRA (2605.17106) | 二元强/弱决策+参数耦合模型身份 | 多维能力评分（4 维 sigmoid 头）+shortfall 匹配+解耦模型身份 | iso-quality 省 54.1%, 86ms CPU |
| 27 | INFRAMIND (2606.11440) | 基础设施盲性导致资源利用不足 | 全栈感知：planner 条件化拓扑+executor 每步观察+scheduler 重排+层次化 CMDP | 高负载 99.9% SLO |
| 28 | Routing Plateau (2606.07587) | 路由准确率是否存在上限 | 21 方法×5 基准广泛研究：发现 plateau 现象+可预测性瓶颈根因 | 突破方向: 数据/编码器/E2E |
| 29 | ReCal (2606.12479) | 多目标聚合导致模糊信用分配 | 分层奖励分解+component-wise advantage+方差感知重加权+per-dataset 标准化 | 7 数据集一致提升 |
| 30 | TwinRouterBench (2605.18859) | one-shot 评估不反映 agent 步级路由 | 双轨：静态 970 前缀确定性评分+动态 500 SWE-bench 端到端验证 | 首次步级路由评估 |
| 31 | GoodServe (2605.16867) | 异构 GPU 上 goodput 优化 | Predict-and-rectify：just-enough selection+运行时请求迁移 | goodput +27.4% |

### 关键洞察
**路由准确率存在 plateau** — 21 种方法收敛到相似准确率，根因是可预测性瓶颈：路由器学习全局趋势而非实例特定信号。突破需要更大数据、更强编码器、端到端微调。

---

## 跨方向收敛

| 收敛主题 | 涉及方向 | 代表论文 |
|---|---|---|
| **OS 类比** | 上下文/调度/缓存 | SmoothAgent (段可分解), TypeGo (OS runtime), ICA (统一架构) |
| **KV cache 为中心** | 上下文/调度/缓存 | LatentContext (buffer token), SAGA (工作流 KV), SAECache (语义淘汰) |
| **行为保持 vs 信息压缩** | 上下文/缓存/路由 | CoACT (NAP), VeriCache (无损), HyDRA (质量保持) |
| **Agent 工作负载特性** | 全部 | CoACT (observation), SAGA (链式调用), Stateful (85-95% 重复) |
| **学习驱动** | 上下文/缓存/路由 | LatentContext (LoRA), KVPolicy (RL), SAECache (在线), ReCal (RL) |

---

## 累计统计

| 维度 | Round 10 后 | Round 11 后 | 增量 |
|---|---|---|---|
| 论文 | 177 | 208 | +31 |
| 页面 | 288 | 324 | +36 (31 source + 6 concept - 1 overview) |
| 概念 | 97 | 103 | +6 |
| PDF | 176 | 207 | +31 |

---

## 五大关键洞察

1. **OS 类比是统一设计语言** — LLM=CPU、KV=cache、上下文=RAM、agent=OS，贯穿上下文优化、调度、缓存三个方向
2. **Agent 工作负载打破所有 chatbot 假设** — 缓存非追加、token 非均匀、prompt 非一次性
3. **行为保持优于信息保留** — CoACT NAP 原则标志上下文优化范式转换
4. **路由准确率存在 plateau** — 可预测性瓶颈是根因，突破需实例特定信号
5. **调度-缓存-路由三者需协同** — 独立优化不够，调度决定缓存命中、缓存决定延迟、延迟决定路由
