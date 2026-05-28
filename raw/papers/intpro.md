---
title: "IntPro"
type: paper
tags: [intent-understanding, proxy-agent, retrieval-conditioned, GRPO, context-aware]
authors: [Guan Liu, Meng Wu, Peng Zhang]
year: 2026
venue: arXiv
citation_count: 0
arxiv_id: "2603.03325"
doi: null
pdf_url: "https://arxiv.org/pdf/2603.03325"
sub_area: intent-understanding
---

## Abstract
Large language models (LLMs) have become integral to modern Human-AI collaboration workflows, where accurately understanding user intent serves as a crucial step for generating satisfactory responses. Context-aware intent understanding, which involves inferring user intentions from situational environments, is inherently challenging because it requires reasoning over both the immediate context and the user's underlying motivations that drive their behavior. Moreover, existing approaches often treat intent understanding as a static recognition task, overlooking users' accumulated intent patterns that could provide valuable references for more accurate and generalizable understanding. To address this gap, we propose IntPro, a proxy agent that learns to adapt to individual users via retrieval-conditioned intent inference. We design intent explanations that abstract how contextual signals connect to expressed intents, and store them in an individual intent history library for retrieval. We train IntPro through supervised fine-tuning on retrieval-conditioned trajectories and multi-turn Group Relative Policy Optimization (GRPO) with tool-aware reward functions, enabling the agent to learn when to leverage historical intent patterns and when to infer directly. Experiments across three diverse scenarios (Highlight-Intent, MIntRec2.0, and Weibo Post-Sync) demonstrate that IntPro achieves strong intent understanding performance with effective context-aware reasoning capabilities across different scenarios and model types.

## Key Contributions
- Proxy agent for context-aware intent understanding
- Intent explanations design
- Individual intent history library
- SFT + GRPO training
- Cross-scenario evaluation (Highlight-Intent, MIntRec2.0, Weibo Post-Sync)