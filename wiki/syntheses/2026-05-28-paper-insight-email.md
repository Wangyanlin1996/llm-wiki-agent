Subject: AI Agent 领域论文洞察汇总 — Agent Memory / Intent Understanding / Intent Recommendation (2024-2026)

---

# AI Agent 领域论文洞察汇总

**日期**: 2026-05-28
**覆盖范围**: Agent Memory、Intent Understanding、Intent Recommendation 三个子方向
**时间窗口**: 2024-2026 年近两年
**总计论文**: 29 篇（含 4 篇经典高引用论文）

---

## 一、Agent Memory（智能体记忆） — 10 篇

### 核心进化框架

LLM Agent 记忆从被动存储到主动经验抽象：

```
Storage（轨迹保存） → Reflection（轨迹提炼） → Experience（轨迹抽象）
      "存历史"             "总结/压缩"              "抽象/迁移知识"
```

三大驱动力：长程一致性、动态环境、持续学习。

### 第一轮论文 (4)

| # | 论文 | 年份 | 引用 | 核心贡献 |
|---|------|------|------|---------|
| 1 | Evo-Memory | 2025 | 71 | 首个流式记忆评测基准；ExpRAG + ReMem 管线 |
| 2 | From Storage to Experience (Survey) | 2026 | 4 | Storage→Reflection→Experience 三阶段综述框架 |
| 3 | LightMem | 2026 | 4 | SLM驱动轻量记忆 STM/MTM/LTM；F1+2.5；83ms延迟 |
| 4 | E-mem | 2026 | 3 | 情景上下文重构；master+assistant多agent；54% F1超过GAM 7.75% |

### 第二轮论文 (6)

| # | 论文 | 年份 | 核心贡献 |
|---|------|------|---------|
| 5 | MemCog | 2026 | 范式转换：Memory-as-Tool → Memory-as-Cognition |
| 6 | MemGym | 2026 | 长视野记忆评测环境，超越单会话基准 |
| 7 | APEX-MEM | 2026 | 半结构化记忆 + 时间推理 |
| 8 | H-Mem | 2026 | 混合表示（事实+摘要+画像）渐进记忆 |
| 9 | ENPMR-Bench | 2026 | 主动记忆检索基准（情感支持场景） |
| 10 | MINTEval | 2026 | 多目标干扰下记忆评测 |

**趋势洞察**: 评测多样化爆发 — 从 LoCoMo 单一基准扩展到情感支持、多目标干扰、长视野环境等专用场景；范式从 Memory-as-Tool → Memory-as-Cognition。

---

## 二、Intent Understanding（人机交互意图理解） — 11 篇

### 核心理论框架

IST (Intent Signal Theory) 区分四个对象：
- I*（潜在源意图） → I-hat（可观察代理） → P（编码载体） → O（模型输出）
- **不可逆意图丢失定理**: 载体中缺失的私有意图无法恢复

### 第一轮论文 (4)

| # | 论文 | 年份 | 引用 | 核心贡献 |
|---|------|------|------|---------|
| 1 | Intent Signal Theory | 2026 | — | IST计算框架；I*/I-hat/P/O四对象；不可逆丢失定理 |
| 2 | IntPro | 2026 | 0 | 代理意图理解；检索条件化推理 + SFT+GRPO |
| 3 | VitaBench 2.0 | 2026 | 0 | 个性化+主动性评测基准；揭示SOTA与实际需求差距 |
| 4 | Intent Communication Design | 2025 | 2 | Transparency×Abstraction×Modality 三维设计空间 |

### 第二轮论文 (7)

| # | 论文 | 年份 | 引用 | 核心贡献 |
|---|------|------|------|---------|
| 5 | IntentGrasp | 2026 | 0 | 12域49语料全面基准；17/20 LLM低于随机基线；IFT微调+30F1 |
| 6 | RECAP | 2025 | — | 意图改写基准：歧义/漂移/模糊 → 精炼目标表示 |
| 7 | PersonalAlign | 2026(ACL) | 0 | 隐式意图对齐+HIM-Agent；+15.7%执行 +7.3%主动 |
| 8 | ContextAgent | 2025 | 41 | 可穿戴感知+意图理解；ContextAgentBench 9场景20工具 |
| 9 | Intent Detection in Age of LLMs | 2024(EMNLP) | 41 | Hybrid路由框架（LLM+SetFit）；OOS检测+5% |
| 10 | Satori | 2024 | — | BDI框架+多模态LLM → 主动AR助手 |
| 11 | NeuroSync | 2025(UIST) | 0 | 直接意图-任务匹配新范式；知识蒸馏提取LLM理解 |

**趋势洞察**: 意图理解从纯文本扩展到多模态（感知/AR/GUI），从分类到改写/操控。IntentGrasp揭示LLM意图理解严重不足（17/20低于随机），IFT微调提供改进路径。

---

## 三、Intent Recommendation（意图推荐） — 8 篇

### 范式转换

```
Reactive Agent（等待指令） → Proactive Agent（主动推荐）
     "告诉我做什么"              "我知道你需要什么"
```

### 第一轮论文 (3)

| # | 论文 | 年份 | 引用 | 核心贡献 |
|---|------|------|------|---------|
| 1 | IntentRL | 2026 | 4 | RL训练主动意图澄清；浅→深意图精炼图+两阶段RL |
| 2 | PIRA-Bench | 2026 | 3 | GUI主动意图推荐基准；PIRF记忆感知框架 |
| 3 | PASK | 2026 | 2 | DD-MM-PAS范式；IntentFlow；LatentNeeds-Bench |

### 第二轮论文 (5)

| # | 论文 | 年份 | 引用 | 核心贡献 |
|---|------|------|------|---------|
| 4 | Ask-before-Plan | 2024(EMNLP) | 12 | CEP多agent框架：先澄清再执行范式 |
| 5 | Inner Thoughts | 2025 | 2 | 内隐思想框架：连续隐层思维驱动主动参与 |
| 6 | When AI Agents Are Proactive | 2025(BISE) | 22 | **人因风险**：主动帮助降低用户能力感 |
| 7 | AssistantX | 2025(IROS) | 3 | 4-agent主动框架；真实办公环境1.5月部署验证 |
| 8 | ETAPP | 2025(ACL) | 1 | 个性化+主动性权衡评测基准 |

**趋势洞察**: 人因研究揭示主动AI可能降低用户能力感（22引用BISE论文），主动性必须与自主性平衡。Clarification-first（Ask-before-Plan）和内隐思想（Inner Thoughts）提供负责任主动性的设计模式。

---

## 四、跨方向共性趋势

| 共性维度 | Agent Memory | Intent Understanding | Intent Recommendation |
|---------|-------------|--------------------|--------------------|
| **长期记忆** | STM/MTM/LTM(LightMem)、情景(E-mem)、半结构化(APEX-MEM) | 用户意图历史(IntPro)、层级记忆(HIM-Agent) | 混合记忆(PASK)、状态跟踪(PIRF) |
| **用户画像建模** | 多用户记忆(LightMem) | 上下文感知(IntPro/VitaBench2)、感官感知(ContextAgent) | 偏好感知(PIRA-Bench/PASK)、个性化(ETAPP) |
| **主动性** | 主动探索(Survey)、ReMem、主动检索(ENPMR-Bench) | 主动信息获取(VitaBench2)、BDI(Satori) | 主动澄清(IntentRL/Ask-before-Plan)、主动推荐(PIRA-Bench) |

**核心结论**: 三个方向均围绕"长期记忆 + 用户画像 + 主动性"收敛，反映了AI Agent从"工具"向"个性化伙伴"的演进趋势。

---

## 五、知识库存档状态

| 项目 | 数量 |
|------|------|
| 论文总数 | 29 篇 |
| PDF原文件 | 27 个（106.5 MB） |
| 元数据 .md 文件 | 29 个 |
| Wiki source页面 | 34 页（含5篇3GPP标准） |
| Wiki concept页面 | 28 页 |
| Wiki总页面 | 66 页 |
| 索引同步 | ✓ 0脱同步 |
| 空文件 | ✓ 0空文件 |

所有PDF和元数据存储在: D:\workspace\llm-wiki-agent\raw\papers\
Wiki知识库路径: D:\workspace\llm-wiki-agent\wiki/

---

*此汇总由 AI Agent 知识库系统自动生成，基于 Semantic Scholar + arXiv 多平台搜索结果。*