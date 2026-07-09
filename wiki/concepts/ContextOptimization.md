---
title: "上下文优化（Context Optimization）"
type: concept
tags: ['context-management', 'compression', 'kv-cache', 'retrieval']
sources: ["coact-action-preserving-compression", "smoothagent-lookahead-context", "latent-context-compilation", "cross-family-speculative-prefill", "mia-signature-activation", "prism-intent-memory-retrieval"]
last_updated: 2026-07-09
---

上下文优化解决 LLM agent 迭代交互中上下文不断累积导致的推理成本爆炸问题。核心张力：保留信息 vs 压缩成本 vs 行为保持。

**五大范式**：
1. **动作保持压缩** — [[CoACT]] 提出 NAP 原则：压缩后的 observation 必须诱导与原始 observation 相同的下一步动作。训练轻量压缩器，token 消耗降 33%。
2. **前瞻上下文工程** — [[SmoothAgent]] 发现 context 变换的段可分解性，提前执行变换并准备 KV cache，TTFT 降 11.9x。
3. **潜在上下文编译** — [[LatentContextCompilation]] 用 disposable LoRA 将长上下文蒸馏为 buffer token，自对齐优化无需合成 QA，16x 压缩。
4. **跨族推测预填充** — [[CrossFamilySpeculativePrefill]] 用注意力估计 token 重要性跨模型族压缩 prompt，免训练，保留 90-100% 性能。
5. **激活签名压缩** — [[MiASignature]] 用次模函数选择高层概念构成全局激活签名，作为条件信号近似全激活状态。

**检索-压缩联合优化**：[[PRISM-IntentMemoryRetrieval]] 将长时程记忆视为图结构上的联合检索-压缩问题，训练免框架，一个数量级更小上下文预算取得更高准确率。

**关键洞察**：上下文优化正从"压缩文本"转向"保持行为"——衡量标准不是保留了多少信息，而是 agent 的后续行为是否一致。
