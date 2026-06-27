# 智能体自学习前沿进展与电信领域启发

**Session ID:** ses_149a9202fffe34ieHYQ6eOWUN7
**Created:** 2026/6/11 19:00:07
**Updated:** 2026/6/12 17:00:37

---

## User

# academic-search Skill

## 前置检查

在开始前，检查环境就绪状态：

```bash
bash ~/.claude/skills/academic-search/scripts/check-deps.sh
```

- **Node.js 22+**：必需（用于 CDP 浏览器模式）。仅使用 API 平台时可不检查。
- **Chrome remote-debugging**：仅在访问 Google Scholar 或其他需要浏览器自动化的平台时必需。在 Chrome 地址栏打开 `chrome://inspect/#remote-debugging`，勾选 **Allow remote debugging for this browser instance**。
- **curl**：必需，用于 API 调用。

arXiv、Semantic Scholar、PubMed、Papers with Code 等 API 平台无需 Chrome 远程调试即可使用。

**S2 API Key（强烈建议）**：无 Key 时 S2 速率上限极低，单 session 多次调用必触发 429。免费注册即可获得更高配额：https://www.semanticscholar.org/product/api#api-key-form。有 Key 时在请求头加 `x-api-key: {your_key}`。

## 搜索哲学

**明确目标，选对平台，提取结构化数据，完成即止。**

学术搜索不同于通用网页浏览——目标是获取**准确、结构化**的论文元数据，而不是浏览网页内容。

**① 明确检索目标，定义成功标准**：执行前先明确什么算完成了。

- 关键词搜索？精确论文？某作者的全部论文？某 venue 的论文列表？
- 学科是什么？是否需要使用 MeSH、JEL、MSC、ACM CCS 等受控词表？
- 文献类型是什么：期刊论文、会议论文、预印本、系统综述、临床试验、工作论文、专著/章节？
- 需要什么字段：仅标题和引用数 / 完整元数据 / PDF / BibTeX / 代码链接？
- 年份范围？领域限定？返回几篇？
- **成功标准**：用户要的是摘要表（第一遍）还是完整元数据（第二遍）？数量够了吗？字段都有了吗？这是后续所有决策的锚点。

**② 选对平台**：不同需求对应不同平台（见下方矩阵）。API 平台优先，CDP 用于无 API 的平台。

**③ 提取结构化数据，先筛后深**：搜索的时间瓶颈不在"搜"，在"筛"。默认采用两遍策略：

- **第一遍（轻量扫描）**：先拉 20-30 条结果，输出轻量摘要表——标题、作者、年份、venue、引用数、是否有开放 PDF/代码。不拉完整摘要。
- **用户或任务确认核心论文**（引用数高、venue 等级高、与目标最相关的 5-10 篇）后，**第二遍**再深入拉摘要、PDF、BibTeX 等完整信息。

所有结果输出为统一 schema（见 `references/metadata-schema.md`），不要输出原始 HTML 或非结构化文本。多平台结果用 DOI/arXiv ID 去重合并。

**④ 过程校验，用失败信号更新方向**：每一步的结果都是信息，不只是成功或失败的二元信号。

| 失败信号 | 含义 | 方向调整 |
|---------|------|---------|
| API 429 / Rate exceeded | 本次会话消耗超配额，不是暂时波动 | 等待 15s+ 或切换 CDP 模式；不要同一请求重试 |
| Jina/WebFetch 超时 | 该页面对静态抓取不友好 | 改用 curl 直接调 API 或切换 CDP |
| S2 返回结果为空 | query 措辞问题，或该平台无收录 | 换关键词组合，或换 arXiv/PubMed |
| 平台返回"内容不存在" | 未必真的不存在，可能是访问方式问题 | 检查 URL 参数是否完整，换平台验证 |
| 同一方式重试 3 次无改善 | 路径错了，不是还没找到方法 | 重新评估目标，换平台或换访问方式 |

**⑤ 完成判断**：对照①定义的成功标准确认任务完成后停止，不为"更完整"而过度操作。

## 平台选择矩阵

根据任务特征选择最合适的平台和访问方式：

| 需求 | 首选平台 | 访问方式 | 备注 |
|------|---------|---------|------|
| CS/Math/Physics/统计 论文搜索 | **arXiv** | REST API | 完全开放，PDF 直链 |
| 引用数、引用/被引关系 | **Semantic Scholar** | REST API | 免费 Key 可提升速率 |
| 作者主页、全部论文 | **Semantic Scholar** | REST API | /author/{id}/papers |
| 生物医学、生命科学 | **PubMed** | NCBI E-utilities | 完全开放 |
| 跨学科 DOI / 元数据核对 | **Crossref** | REST API | DOI、期刊、出版商、ISSN、参考文献基础信息 |
| 跨学科作者/机构/概念/引用 | **OpenAlex** | REST API | 适合作为 Semantic Scholar 的跨学科补充 |
| 开放获取状态 / OA PDF | **Unpaywall** | REST API | 判断 gold/green/hybrid/closed OA 与合法开放全文 |
| ML 论文 + 代码仓库 | **Papers with Code** | REST API | 无需鉴权 |
| ACM 顶会论文 (SIGKDD/WWW 等) | **ACM DL** | WebFetch + Jina | BibTeX 导出端点可直接访问 |
| IEEE 期刊/会议论文 | **IEEE Xplore** | WebFetch / Jina | 有机构 Key 时用官方 API |
| 广泛引用数 / 全平台覆盖 | **Google Scholar** | **CDP（必须）** | 无 API，反爬严重 |
| 论文是否存在 / 基础元数据 | **Semantic Scholar** | REST API | 支持 DOI / arXiv ID 互查 |
| **中文文献**（期刊/学位论文/会议） | **CNKI（知网）** | **CDP（必须）** | 无公开 API；机构登录后全文可得 |

**API 平台访问方式**：

- **WebSearch**：用于发现论文来源、查找 DOI/作者 ID 等信息入口
- **WebFetch / Jina**：URL 已知时从页面提取，Jina（`r.jina.ai/{url}`）节省 token，适合文章类页面
- **curl**：直接调用结构化 API，返回 JSON/XML
- **CDP**：仅 Google Scholar 必须；其他平台在 API/WebFetch 无效时作为兜底

详细 API 调用模板见 `references/api-cookbook.md`。

## 学科路由

先按用户问题判断学科，再读取对应 `references/disciplines/*.md`。如果用户问题跨学科，优先读取最核心学科的 profile，再用 OpenAlex / Crossref / Unpaywall 做跨学科补全。

| 学科 | 读取文件 | 首选方向 |
|------|----------|----------|
| 计算机 / AI | `references/disciplines/computer-science.md` | arXiv、Semantic Scholar、ACM DL、IEEE、DBLP、Papers with Code |
| 医学 / 生命科学 | `references/disciplines/biomedicine.md` | PubMed、PMC、Europe PMC、ClinicalTrials、bioRxiv、medRxiv |
| 物理 / 数学 | `references/disciplines/physics-math.md` | arXiv categories、NASA ADS、INSPIRE HEP、MSC |
| 化学 / 材料 | `references/disciplines/chemistry-materials.md` | Crossref、OpenAlex、ChemRxiv、ACS、RSC、Springer、Wiley |
| 经济 / 社科 | `references/disciplines/economics-social-science.md` | RePEc、NBER、SSRN、OSF、PsyArXiv、JEL |
| 人文 / 法律 | `references/disciplines/humanities-law.md` | Google Scholar、图书馆目录、JSTOR/Project MUSE/HeinOnline 访问状态 |

学科 profile 决定 query expansion、排序标准、输出字段和全文访问边界。不要把 CCF 或 CS 顶会规则套到非 CS 学科。

## 核心能力

### 关键词搜索

1. 先按“学科路由”读取 discipline profile：CS/ML → arXiv + Semantic Scholar；生医 → PubMed/Europe PMC；跨领域 → OpenAlex + Crossref + Semantic Scholar
2. **扩展 query**：用户自然语言输入往往只是一个切入点，需要主动展开为 2-3 个互补 query 覆盖不同命名习惯：
   - 同义词替换：`agent` → `agentic` / `multi-agent` / `autonomous`
   - 子概念拆分：`time series agent` → `time series LLM agent` + `time series agentic reasoning` + `time series automated analysis`
   - 缩写与全称并用：`TS` / `time series`，`LLM` / `large language model`
   - 学科受控词表：医学用 MeSH，经济用 JEL，数学用 MSC，计算机用 ACM CCS，化学可补 CAS/化合物同义词
   - 不同 query 结果合并去重，覆盖率比单 query 提升 30-50%
3. 构造查询：arXiv 用 `search_query` 字段前缀语法；S2 用 `query` 参数；PubMed 用 `term` 布尔表达式
4. **计划多次 S2 调用时优先用 batch API**（`/paper/batch`）而非多次 search，节省速率配额
5. **第一遍输出轻量摘要表**（必含：标题、年份、venue、引用数、是否有开放 PDF），**不默认拉完整摘要**
6. **意图判断**：用户明确说"只要前 N 篇"或"摘要表即可"时，直接输出第一遍结果，无需等待确认再停下
7. 用户需要第二遍时，再深拉完整元数据

多平台并行查询时，用子 Agent 分治（见"并行分治策略"一节）。

**轻量摘要表输出格式示例**：

| 标题 | 年份 | Venue | 引用数 | PDF |
|------|------|-------|--------|-----|
| Attention Is All You Need | 2017 | NeurIPS [CCF-A] | 120,000+ | ✓ arXiv |
| BERT: Pre-training... | 2019 | NAACL [CCF-B] | 80,000+ | ✓ arXiv |

Venue 等级标注规则：CS 会议参考 `references/venue-rankings.md`（CCF 分级）；非 CS 学科先读取 `references/disciplines/*.md` 和 `references/rankings/*.md`，按该学科的证据等级、文献类型或期刊/来源规则排序。期刊显示 JCR 分区（若可从平台字段获取）时必须标明来源。

### 结果筛选

搜索后用以下维度缩小范围，**优先帮用户筛出值得读的论文，而不是把所有结果都呈现**：

| 筛选维度 | 数据来源 | 说明 |
|---------|---------|------|
| 引用数阈值 | S2 `citationCount` | 经典论文通常引用数高；新兴方向可适当放低阈值 |
| 发表年份 | 所有平台 | 综述类需要覆盖历史；最新进展限定近 2-3 年 |
| Venue 等级 | S2 `venue` + `references/venue-rankings.md` | CS 会议参考 CCF 分级；优先 CCF-A/B |
| 学科证据等级 | discipline profile + ranking reference | 医学、社科、人文等不要套用 CCF；按学科规则排序 |
| 开放 PDF | S2 `externalIds.ArXiv` 存在即可得 | **只要有 ArXiv ID 就标 ✓**，不依赖 openAccessPdf（该字段经常为 null） |
| 代码可用性 | Papers with Code API | ML 论文用 `paperswithcode.com/api/v1/papers/?arxiv_id={id}` 自动补全代码列 |

**排序建议**：面向学术前沿性的综合排序，优先级依次为：

1. **时效性（最高权重）**：近 6 个月内发表的论文标注 `[新]` 并置顶展示，不因引用数低而降权——前沿方向的新论文引用数天然偏低，但代表最新进展
2. **引用数（次要权重）**：同一时间段内按引用数降序，高引用代表社区认可度
3. **学科评价规则（参考项）**：CS 用 CCF/顶会；医学用证据等级和研究类型；社科用期刊/工作论文体系和方法类型；人文允许专著、章节和档案来源优先于引用数。

**实操分组示例**：
- 第一组：近 6 个月论文，按引用数降序（含 `[新]` 标注）
- 第二组：更早论文，按引用数降序，CCF-A/B 同引用数时优先

**筛选后的典型结论格式**：

> 共找到 28 篇，按引用数 + venue 等级筛选后，推荐优先阅读以下 6 篇：[列表]
> 其余 22 篇可按需查阅。

### 精确论文查找

已知 DOI 或 arXiv ID 时，直接用 Semantic Scholar 精确查询：
```bash
# DOI 查询
curl -s "https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}?fields=title,authors,year,abstract,citationCount,openAccessPdf"

# arXiv ID 查询
curl -s "https://api.semanticscholar.org/graph/v1/paper/ARXIV:{arxiv_id}?fields=title,authors,year,abstract,citationCount,openAccessPdf"
```

### 元数据提取

所有提取结果必须转换为 `references/metadata-schema.md` 定义的标准 JSON schema。输出时：

- **单篇**：Markdown 表格格式，字段清晰
- **多篇**：Markdown 列表表格（标题、作者、年份、Venue、引用数、PDF 链接）
- **批量导出**：JSON 数组

### PDF / 全文获取

只获取合法可公开访问的全文。按以下优先级尝试，**每步失败后才进入下一步**，并在结果中记录 `full_text_status`：

1. **arXiv PDF 直链**：`externalIds.ArXiv` 存在时，直接构造 `https://arxiv.org/pdf/{arxiv_id}`（S2 的 `openAccessPdf` 字段经常为 null，但 arXiv PDF 实际可得，不依赖该字段）

2. **Semantic Scholar openAccessPdf**：读取 API 响应 `openAccessPdf.url`，可作 arXiv 之外的 OA 补充

3. **OpenAlex OA 检查**（有 DOI 时必须执行，不可跳过）：
   ```bash
   curl -s "https://api.openalex.org/works?filter=doi:{doi}&select=id,open_access,best_oa_location" \
     -H "User-Agent: academic-search-skill/1.x (mailto:your@email.com)"
   ```
   响应中 `best_oa_location.pdf_url` 非 null 时直接用；`open_access.is_oa=false` 时记录并进入下一步

4. **Unpaywall**（有 DOI 时必须执行）：
   ```bash
   curl -s "https://api.unpaywall.org/v2/{doi}?email=your@email.com"
   ```
   返回 `best_oa_location.url_for_pdf` 字段；`is_oa=false` 时说明出版商无授权 OA 版本

5. **领域专用预印本库**（根据论文领域判断）：
   - 地球科学 / 地质学 / 海洋 / 大气：EarthArXiv `https://eartharxiv.org/repository/search/?q={title_keywords}`
   - 生物医学：Europe PMC `https://europepmc.org/search?query=DOI:{doi}`
   - 物理 / 天文：INSPIRE-HEP `https://inspirehep.net/search?p=doi:{doi}`
   - 心理 / 社科：PsyArXiv / SocArXiv

6. **作者版预印本搜索**（前 5 步全失败时）：
   WebSearch 查 `"{first_author_last_name}" "{paper_title_keywords}" filetype:pdf` 或 `site:researchgate.net`，寻找作者自存档版本

7. **告知用户**：如以上均无法获取，明确说明：
   - 该论文无公开 OA 版本（引用步骤 3/4 的检查结果作为依据）
   - 建议通过机构图书馆、作者邮件索取、或 ILL（馆际互借）获取

**Springer HTML 全文的特殊处理**：若 PDF 路由返回 HTML 而非 PDF 二进制（Content-Type 检查），说明该论文为"HTML 全文"形式（常见于 2024+ online-first 文章）。此时：
- 记录为"HTML 全文可读，无独立 PDF"，不算获取失败
- 返回文章 HTML 页面 URL 供用户在浏览器中阅读

**Cloudflare/403 拦截处理**：Wiley、AGU/Wiley 等出版商对自动请求有强 bot 防护，CDP 浏览器模式也可能被 Cloudflare 拦截。遇到此情况：
- 不要反复重试（会触发更严格封锁）
- 直接跳到步骤 3（OpenAlex）和步骤 4（Unpaywall）检查是否有合法 OA 版本
- 步骤 7 告知用户原因

`full_text_status` 枚举：

| 状态 | 含义 |
|------|------|
| `open_pdf` | 找到可公开访问 PDF |
| `needs_institution` | 论文页可访问，但全文需要机构权限 |
| `no_open_pdf` | 没有发现合法开放全文 |
| `anti_bot_blocked` | 被 Cloudflare、验证码或反爬限制拦截 |
| `html_not_pdf` | PDF 路由返回 HTML 页面而不是 PDF |
| `unknown` | 当前证据不足，无法可靠判断 |

### 开放 PDF 下载与 manifest 导出

Academic-Search 可以下载合法开放访问 PDF，但边界必须清楚：

- 只下载 `full_text_status="open_pdf"` 且存在 `pdf_url` 的论文。
- 不得调用 Sci-Hub、LibGen、shadow library、WebVPN、CARSI、Tor 或 Cloudflare 绕过工具。
- 遇到 `needs_institution`、`no_open_pdf`、`anti_bot_blocked`、`html_not_pdf`、`unknown` 时，不下载，只写入 manifest 并说明原因。
- 批量任务先生成 manifest，再由用户确认是否下载，除非用户明确要求“下载所有开放 PDF”。

推荐流程：

1. 搜索/精确查询论文，生成标准 metadata schema。
2. 通过 arXiv、Semantic Scholar、OpenAlex、Unpaywall、PubMed Central 判断 `full_text_status` 和 `pdf_url`。
3. 调用 `scripts/oa-pdf-download.mjs --input <metadata.json> --manifest <manifest.json>` 生成下载清单。
4. 用户确认后，调用 `scripts/oa-pdf-download.mjs --input <metadata.json> --manifest <manifest.json> --download --out-dir <dir>` 下载开放 PDF。
5. 输出下载结果表：标题、DOI/arXiv ID、状态、本地路径、跳过原因。

CLI 示例：

```bash
node scripts/oa-pdf-download.mjs \
  --input /tmp/academic-search-results.json \
  --manifest /tmp/academic-search-download-manifest.json

node scripts/oa-pdf-download.mjs \
  --input /tmp/academic-search-results.json \
  --manifest /tmp/academic-search-download-manifest.json \
  --download \
  --out-dir /tmp/academic-search-pdfs
```

输出 JSON 计数字段：

```json
{"total":3,"eligible":2,"downloaded":1,"skipped":1,"failed":0,"not_pdf":1}
```

`download_status` 枚举：`not_requested`、`eligible`、`downloaded`、`skipped`、`failed`、`not_pdf`。详细字段定义见 `references/metadata-schema.md`。

分工规则：

- 用户要“找论文 / 筛论文 / 查引用 / 生成开放 PDF 清单” → 使用 Academic-Search。
- 用户要“尽可能下载这些 DOI 的 PDF / 用 WebVPN / 多源下载 / Sci-Hub / LibGen” → 明确说明这超出 Academic-Search 边界，并建议切换 scansci-pdf。

如果用户需要下载非开放获取论文，应建议使用机构图书馆、作者邮件、馆际互借，或切换到 scansci-pdf 这类专门的论文获取工具；Academic-Search 不负责绕过访问限制。

不要尝试访问任何需要绕过付费墙的第三方服务。遇到 Elsevier、Wiley、Springer、ACS、Taylor & Francis、JSTOR 等商业出版平台时，先判定开放获取状态；若需要机构访问，停止自动下载并报告 `needs_institution`。

### BibTeX 导出

优先级：

1. **arXiv**：`https://arxiv.org/bibtex/{arxiv_id}` 直接获取
2. **ACM DL**：先试 `https://dl.acm.org/action/exportCitation?doi={encoded_doi}&format=bibtex`；若返回 challenge/HTML 错页，回退 CDP
3. **Semantic Scholar**：无直接端点，根据 `references/metadata-schema.md` 的模板从字段拼装
4. **其他平台**：CDP 点击页面上的 "Export Citation" / "Cite" 按钮

### 作者主页解析

```bash
# Semantic Scholar 作者搜索
curl -s "https://api.semanticscholar.org/graph/v1/author/search?query={author_name}&fields=name,affiliations,paperCount,citationCount"

# 获取作者全部论文（分页）
curl -s "https://api.semanticscholar.org/graph/v1/author/{author_id}/papers?fields=title,year,citationCount,externalIds&limit=100&offset=0"
```

Google Scholar 作者页需 CDP，见 `references/site-patterns/scholar.google.com.md`。

## CDP 模式（Google Scholar 及其他需要浏览器自动化的平台）

通过 CDP Proxy 直连用户日常 Chrome，天然携带登录态。

所有操作在自己创建的后台 tab 中进行，不干扰用户已有 tab，完成后关闭。

### 启动

```bash
bash ~/.claude/skills/academic-search/scripts/check-deps.sh
```

脚本自动检查并启动 CDP Proxy（默认 `127.0.0.1:3456`，可通过 `CDP_PROXY_PORT` 覆盖）。

### 操作方式

进入浏览器层后，用 HTTP API 操控页面：

```bash
# 创建新 tab，导航到目标页
TARGET=$(curl -s "http://127.0.0.1:${CDP_PROXY_PORT:-3456}/new?url=https://scholar.google.com" | node -p "JSON.parse(require('fs').readFileSync(0, 'utf8')).targetId")

# 执行 JS 提取数据
curl -s -X POST "http://127.0.0.1:${CDP_PROXY_PORT:-3456}/eval?target=$TARGET" -d 'document.title'

# 点击元素（CSS 选择器）
curl -s -X POST "http://127.0.0.1:${CDP_PROXY_PORT:-3456}/click?target=$TARGET" -d 'button[type=submit]'

# 完成后关闭 tab
curl -s "http://127.0.0.1:${CDP_PROXY_PORT:-3456}/close?target=$TARGET"
```

完整 API 参考见 `references/cdp-api.md`。

**三种点击方式**：

| 方式 | 端点 | 适用场景 |
|------|------|---------|
| JS click | `/click` | 通用，速度快 |
| 真实鼠标 | `/clickAt` | 需要触发文件对话框或绕过反自动化检测 |
| 文件上传 | `/setFiles` | 直接设置 file input，绕过对话框 |

**先了解页面结构，再决定动作**：用 `/eval document.body.innerText.slice(0, 500)` 或截图快速了解当前页面状态。

## 并行分治策略

任务包含多个**独立**目标时（如同时查询 N 篇论文、N 个来源），分发子 Agent 并行执行。

**好处**：速度 = 单子任务时长；抓取内容不进入主 Agent context，节省 token。

**子 Agent Prompt 写法**：
- 必须写：`必须加载 academic-search skill 并遵循指引`
- 描述**目标**（获取/提取/查找），不要指定具体步骤
- 说明需要哪些字段（标题/引用数/PDF 等）
- **注意用词**：「搜索 BERT 的引用数」会把子 Agent 锚定到 WebSearch；应写「获取 BERT 的引用数」——描述目标，不暗示手段

**典型分治场景**：

| 适合分治 | 不适合分治 |
|---------|-----------|
| 多平台并发查同一论文（arXiv + S2 + PubMed） | 查询有依赖关系（先搜索再按结果查详情） |
| 批量查询 N 篇不相关论文 | 简单单平台单次 API 查询 |
| 多个作者主页并行抓取 | 几次 curl 就能完成的轻量任务 |

**多平台并发查同一论文时的去重**：

子 Agent 返回结果后，主 Agent 按 `references/metadata-schema.md` 中的去重规则合并：DOI 为主键 → arXiv ID 次之 → 标题+年份模糊匹配。

## 信息核实

学术搜索的一手来源是**论文本身**和**平台官方 API**，不是二手报道。

| 核实目标 | 一手来源 |
|---------|---------|
| 论文元数据（标题、作者、DOI）| 发表平台（ACM DL / IEEE / arXiv）官方页面、Crossref、OpenAlex |
| 引用数 | Google Scholar（最全）> Semantic Scholar |
| 开放获取状态 | Unpaywall > 出版商页面 > 仓储页面 |
| 代码实现 | Papers with Code / 论文官方 GitHub |
| 会议/期刊信息 | 主办方官网 |

多平台引用数不一致时正常——不同平台收录范围不同，Google Scholar 通常最高。

## 站点经验

操作中积累的特定网站经验，按域名存储在 `references/site-patterns/` 下。

已预置经验的平台：arXiv、Semantic Scholar、Google Scholar、ACM DL、IEEE Xplore、PubMed、Papers with Code、CNKI（知网），以及 ScienceDirect、Wiley、Springer、ACS 等主要出版商访问限制。

确定目标平台后，**必须**读取对应文件获取先验知识（平台特征、有效模式、已知陷阱）。经验内容标注发现日期，当作**可能有效的提示，不是保证正确的事实**——按经验操作失败时，回退通用模式，并**更新经验文件**（记录失败原因和发现日期）。操作成功后若发现了新模式或陷阱，同样主动写入。

## References 索引

| 文件 | 何时加载 |
|------|---------|
| `references/api-cookbook.md` | 需要 API 调用示例、参数说明、响应字段映射时 |
| `references/metadata-schema.md` | 整理提取结果、多平台去重合并、生成 BibTeX 时 |
| `references/cdp-api.md` | 需要 CDP 浏览器操作时（Google Scholar、CNKI 等） |
| `references/disciplines/*.md` | 需要按学科选择平台、扩展 query、排序和输出字段时 |
| `references/rankings/*.md` | 需要非 CS 学科证据等级或来源评价规则时 |
| `references/workflows/*.md` | 需要执行系统综述、核心论文清单、快速综述等研究工作流时 |
| `references/venue-rankings.md` | 标注 CS 会议/期刊等级（CCF 分级）时 |
| `references/site-patterns/{domain}.md` | 确定目标平台后，读取对应站点经验 |
| `references/site-patterns/cnki.net.md` | 知网检索时必读：登录态要求、DOM 选择器、数据库代码 |


帮我找近两年智能体自学习相关的前沿进展与技术，要求分析透彻、总结在电信领域（智能运维、ADN等）的启发。

---

## Assistant

**Tool: skill**

---

## Assistant

**Tool: read**

**Tool: read**

**Tool: read**

---

## Assistant

现在我来构建搜索计划并启动并行查询。任务要求跨学科搜索（CS/AI + 电信/网络），我将扩展多个查询维度并行检索。

**搜索计划**：

1. **Query扩展**（5组互补查询覆盖不同命名习惯）：
   - Q1: `LLM agent self-learning self-improvement` (核心概念)
   - Q2: `agent self-evolution self-play bootstrapping` (技术路线)
   - Q3: `agent self-reflection experience learning memory` (认知机制)
   - Q4: `telecom network AIOps autonomous agent` (电信领域直接相关)
   - Q5: `autonomous digital network self-healing network operations LLM` (ADN/智能运维)

2. **平台**：arXiv + Semantic Scholar + OpenAlex 并行

3. **筛选**：2024-2026年份，按引用数+venue等级排序，筛出10-15篇核心论文

4. **第二遍**：对核心论文深入分析，提炼电信领域启发

**Tool: task**

**Tool: task**

**Tool: task**

---

## Assistant

**Tool: todowrite**

---

## Assistant

**Tool: todowrite**

---

## Assistant

---

## 智能体自学习前沿进展与电信领域启发 — 研究报告

### 一、检索概况

三路并行检索：arXiv(44篇) + Semantic Scholar(30篇) + 电信专项(16篇)，去重合并后约 **90篇**候选，筛选出 **核心推荐15篇 + 电信直接相关8篇**。

---

### 二、技术脉络分类（7条主线）

#### 1. 经验蒸馏与记忆驱动自演化
| 论文 | 引用 | 关键机制 |
|------|------|---------|
| ReasoningBank (2509.25140) | 122 | 成功/失败经验蒸馏→可泛化推理策略库，MaTTS加速 |
| Evo-Memory (2511.20857) | 87 | 10+记忆模块统一评估，ReMem(action-think-refine) |
| FLEX (2511.06449) | 38 | 结构化经验库，发现经验增长scaling law，跨agent继承 |

#### 2. 技能库自演化
| 论文 | 引用 | 关键机制 |
|------|------|---------|
| SAGE (2512.17102) | 43 | RL+技能库，Sequential Rollout迭代部署 |
| SkillSmith (2606.01314) | 新 | skill-tool**协同演化**，Lotka-Volterra生态模型捕获互补/冲突 |
| GRASP (2605.29668) | 新 | 回归感知技能提议，**硬回归预算**防止技能间互相破坏 |
| CODESKILL (2605.25430) | 新 | RL训练技能提取与维护策略，混合rubric+执行反馈 |

#### 3. 自博弈与递归自改进
| 论文 | 引用 | 关键机制 |
|------|------|---------|
| Gödel Agent (2410.04444) | 19 | 受Gödel machine启发，LLM**递归修改自身逻辑** |
| Role-Agent (2606.10917) | 新 | 同一LLM同时做Agent和环境，World-In-Agent + Agent-In-World |
| SWE-RL (2512.18552) | 2025 | 自博弈训练超级智能软件Agent (Meta自改进标杆) |

#### 4. 多Agent协同自演化
| 论文 | 引用 | 关键机制 |
|------|------|---------|
| Evolve as a Team/Meta-Team (2605.29790) | 新 | **多尺度自演化**: 行为+协调+组织三层同时改进 |
| HexMachina (2506.04651) | 16 | adapter层发现(环境) + code层改进(策略)分离 |
| AgentTrust (2606.08539) | 新 | 双存储自演化信任层: 规则地板(词法) + RAG判例缓存(语义) |

#### 5. 零数据自演化与环境自构造
| 论文 | 引用 | 关键机制 |
|------|------|---------|
| Agent0 (2511.16043) | 42 | curriculum agent提出任务→executor学习→反压curriculum |
| OpenSkill (2606.06741) | 新 | 开放世界自演化：从文档/仓库构建**自建验证锚点** |
| DreamGym (2511.03773) | 19 | 合成多样经验做RL训练，sim-to-real transfer |

#### 6. Test-time / 在线自适应
| 论文 | 引用 | 关键机制 |
|------|------|---------|
| EEVEE (2606.11182) | 新 | 测试时prompt学习，**路由-提示协同演化** |
| Continual Harness (2605.09998) | 新 | reset-free在线自适应，技能+记忆+prompt同时演化 |
| Adaptive Auto-Harness (2606.01770) | 新 | 任务流持续自适应，**harness树+路由** |

#### 7. 自蒸馏与RL增强
| 论文 | 引用 | 关键机制 |
|------|------|---------|
| HERO (2606.11559) | 新 | 后验增强自蒸馏，用环境观测做局部对齐反馈 |
| SDAR (2605.15155) | 新 | 门控自蒸馏辅助目标+RL主干，防多轮不稳定 |
| SIRI (2606.02355) | 新 | 三阶段自内化：热身→自挖掘技能→蒸馏内化 |

**综合综述**: "Beyond Individual Intelligence" (2605.14892) — 提出**LIFE递进框架**: Lay基础→Integrate协作→Find归因→Evolve自改进，揭示各阶段因果依赖。

---

### 三、电信直接相关论文

| 论文 | 年份 | 核心内容 | 亮点 |
|------|------|---------|------|
| **GO-MAF** (ICCC 2025) | 2025 | 多Agent+LLM自愈5/6G | 89.3%闭环成功率，MTTR降66%，32,487告警验证 |
| Self-Healing Telecom AIOps (IJCESEN) | 2026 | RL自愈+意图网络 | 从被动到主动运维范式转变 |
| Compositional Learning for SON (ICMLCN) | 2025 | CDRL/CPDM多Agent SON | 切换失败降37.2%，有arXiv版 |
| IntelliMARVEL-6G (ICDICI) | 2025 | MARL+PPO+FedAvg自优化6G | 联邦学习隐私保护 |
| Autonomous Cyber Defence DRL+LLM (Computer Networks) | 2025 | DRL+LLM+规则混合Agent | 26引用, 网络防御标杆 |
| AIOps LILT (QRS-C) | 2025 | LoRA增量学习抗概念漂移 | 直接解决AIOps漂移痛点 |
| Self-Learning AIOps (WJARR) | 2025 | ML+DL自学习IT运维 | 企业级框架 |
| AI Telecom Anomaly Detection综述 (AIR) | 2025 | 69引用,电信异常检测 | 全景参考 |

**重要发现**: 学术界无"ADN"术语论文，对应概念为 **Autonomous Network / Self-Organizing Network (SON) / Self-Healing Network**。

---

### 四、电信领域（智能运维/ADN）启发分析

#### 启发1: 经验蒸馏 → 告警-故障知识库自演化

**痛点**: 电信告警海量且复杂，故障诊断依赖专家经验，规则库难以持续更新。
**映射**: ReasoningBank/FLEX的经验蒸馏机制 → 从每次故障处理的成功/失败轨迹中自动蒸馏可泛化诊断策略，替代人工规则维护。
**关键**: FLEX发现的**经验增长scaling law**意味着运维经验库随时间自动增长效果，无需额外人工干预。

#### 启发2: 技能库生态 → 运维流程编排自优化

**痛点**: 不同故障类型的处理流程存在互补/冲突关系，流程优化难以系统化。
**映射**: SkillSmith的Lotka-Volterra生态模型 → 把每种运维流程视为一个"物种"，用交互矩阵捕获互补/冲突关系，指导流程的增删改优先级。
**关键**: GRASP的**硬回归预算**确保新流程不会破坏已有正确流程——这对电信高可靠性要求至关重要。

#### 启发3: 自博弈 → 对抗性故障场景生成与验证

**痛点**: 网络罕见故障/连锁故障难以预测，运维Agent缺乏对极端场景的训练。
**映射**: Gödel Agent/Role-Agent的自博弈 + EvoDrive的Pareto演化 → 用自博弈生成对抗性故障场景(如级联失效、多域并发故障)，在数字孪生/仿真中训练运维Agent。
**关键**: Role-Agent的"同一LLM同时做Agent和模拟环境"思路可大幅降低电信仿真环境构建成本。

#### 启发4: 多Agent多尺度自演化 → 跨域自愈

**痛点**: 电信网跨传输/无线/核心/IT多域协调，域间协调比域内诊断更难。
**映射**: Meta-Team的**多尺度自演化**(行为+协调+组织) → 每个域Agent不仅改进自身诊断能力，还改进与其他域Agent的协调模式和组织结构。
**关键**: GO-MAF已初步验证多Agent自愈可行性(89.3%闭环率)，但缺乏Meta-Team式的**组织级自演化**能力。

#### 启发5: 零数据自演化 → 新业务/新网络场景冷启动

**痛点**: 5G/6G新场景(切片管理、边缘编排)初期缺乏历史数据，Agent冷启动困难。
**映射**: Agent0/OpenSkill的零数据自演化 → curriculum agent自动构造从简到难的任务序列，OpenSkill从技术文档/配置手册构建自建验证锚点。
**关键**: OpenSkill的**自建验证锚点**思路可直接利用电信设备厂商的技术文档和配置指南，无需历史告警数据。

#### 启发6: Test-time适应 → 网络概念漂移在线应对

**痛点**: 网络流量/告警模式随业务变化持续漂移，离线重训成本高且滞后。
**映射**: EEVEE的test-time prompt学习 + LILT的LoRA增量学习 → Agent在推理时在线适应，路由器根据告警类型自动选择最优提示配置。
**关键**: EEVEE的**路由-提示协同演化**特别适合电信多场景(核心网/无线/传输)异构任务流。

#### 启发7: World Model协同 → 数字孪生闭环验证

**痛点**: 运维策略上线风险高，需要仿真验证但仿真构建成本大。
**映射**: WebEvolver/DreamGym的世界模型 → Agent自构建轻量网络仿真，在虚拟环境中演练策略，验证后再部署真实网络。
**关键**: DreamGym的**sim-to-real transfer**能力证明了从仿真到现实的有效迁移路径。

#### ADN路线映射

| ADN自治等级 | 对应Agent自学习成熟度 | 代表技术 |
|------------|---------------------|---------|
| L0 手动 | 无自学习 | 传统运维 |
| L1 辅助 | 单次经验反思 | 简单trajectory reflection |
| L2 部分 | 经验蒸馏+技能积累 | ReasoningBank, SAGE |
| L3 条件自治 | 多尺度自演化+在线适应 | Meta-Team, EEVEE, Continual Harness |
| L4 全自治 | 零数据自演化+递归自改进 | Agent0, Gödel Agent, OpenSkill |

---

### 五、推荐优先阅读（按电信启发优先级排序）

**第一梯队（必读）**:
1. **Meta-Team** (2605.29790) — 多尺度自演化框架，直接对应跨域自愈需求
2. **ReasoningBank** (2509.25140) — 经验蒸馏标杆，122引用，Google Research
3. **SkillSmith** (2606.01314) — skill-tool协同演化，Lotka-Volterra适合运维流程生态
4. **GO-MAF** (ICCC 2025) — 电信多Agent自愈唯一实战验证
5. **FLEX** (2511.06449) — scaling law发现，证明自学习长期增益

**第二梯队（深度参考）**:
6. **Gödel Agent** (2410.04444) — 递归自改进，ADN L4全自治路线
7. **Role-Agent** (2606.10917) — Agent+环境同体，降低仿真构建成本
8. **WebEvolver** (EMNLP 2025) — World Model协同，数字孪生思路
9. **Agent0** (2511.16043) — 零数据自演化，新场景冷启动
10. **Beyond Individual Intelligence Survey** (2605.14892) — LIFE框架全景

**第三梯队（电信专题）**:
11. AIOps LILT (QRS-C 2025) — 概念漂移增量学习
12. Autonomous Cyber Defence DRL+LLM — 网络防御混合Agent
13. Evo-Memory (2511.20857) — 自演化记忆评估基准

---

### 六、后续建议

1. **将核心论文写入wiki** — 可按 `ingest` 工作流逐篇摄入到 `wiki/sources/` 并建立 `entities/` 和 `concepts/` 页面
2. **建立电信启发专题综合页** — 在 `wiki/syntheses/` 中创建结构化分析
3. **获取S2 API Key后补充搜索** — 当前429限流导致部分query失败，可补充"autonomous digital network"等关键词
4. **下载开放PDF** — 核心论文多数有arXiv版本，可批量下载后深入阅读

是否需要我将这些内容写入wiki，或对某几篇核心论文进行第二遍深度检索（获取完整摘要+BibTeX）？

---

## User

我们已经研究过意图的理解、识别、转译、意图信息补齐、智能体skill库、基于执行反思的任务规划等相关研究，在意图、智能体自学习方向还有没有什么新的研究方向

---

## Assistant

**Tool: task**

**Tool: task**

**Tool: task**

---

## Assistant

基于三路补充检索结果，以下是**超越你已有研究方向（意图理解/识别/转译、信息补齐、skill库、反思规划）**的新方向梳理：

---

## 新方向一：意图自演化/自精化 (Intent Self-Refinement)

**核心差异**：不再被动理解/转译给定意图，而是Agent**主动发现意图缺陷并自主迭代精化**。

| 论文 | 关键机制 |
|------|---------|
| **Prism** (2601.08653) | 复杂意图→分解为结构化子元素→识别逻辑依赖→生成澄清问题→**intent-aware reward驱动意图自演化调优** |
| **IntentRL** (2602.03468) | **shallow-to-deep意图精化图谱**：Agent执行前主动澄清latent intent，两阶段RL训练 |
| **PaSaMaster** (2605.14306) | 将检索从一次性匹配转变为**演化搜索过程**：排序证据揭示缺口→refine intent→引导后续搜索 |
| **PASK** (2604.08000) | **streaming IntentFlow**识别深层latent needs，从连续交互中自发现用户真实意图 |
| **Intent Formalization** (2603.17150) | 定义**intent gap**核心问题，提出意图自精化的研究议程（position paper） |

**电信启发**：网络运维中用户意图(如"保障切片SLA")往往模糊，Agent需从告警/指标反馈中**自精化意图**→从"保障SLA"精化为"当X指标>阈值时自动调整Y参数"。

---

## 新方向二：意图-能力对齐/意图缺口 (Intent-Capability Alignment / Closure Gap)

**核心差异**：不再假设Agent总能满足意图，而是**形式化意图与能力的缺口，并设计弥合机制**。

| 论文 | 关键机制 |
|------|---------|
| **Closure Gaps & Delegation Envelopes** (2604.25000) | **closure-gap向量**形式化意图-能力缺口→**delegation envelopes预授权行动空间**→区分closed-world solver vs open-world agent |
| **PersonalAlign** (2601.09636, ACL 2026) | **分层意图记忆(HIM-Agent)**：从长期用户记录解析隐含意图→分层组织偏好/惯例→对齐到Agent能力 |
| **DS-IA** (2603.16207) | 双阶段：语义防火墙过滤无效指令+解析模糊→**确定性级联验证器**逐级验证room→device→capability |
| **IntentScore** (2604.05157) | **plan-aware reward model**：在action encoder中嵌入planning intent→contrastive alignment对齐行动与意图 |
| **Project Prometheus** (2604.17464) | **Intent Gap→Specification Inference优先于代码生成**→RQA Loop用ground-truth作proxy oracle验证推断的spec |

**电信启发**：运维意图"自愈核心网"与Agent实际能力(只能调整特定参数)之间存在**closure gap**——需要delegation envelope机制预授权Agent在特定范围内自主行动，超出范围则升级。

---

## 新方向三：层级意图自发现 (Hierarchical Intent Discovery)

**核心差异**：不再只识别显式意图，而是**从低级操作经验中自发现/自提炼更高层意图模式**。

| 论文 | 关键机制 |
|------|---------|
| **HiVA** (2509.00189) | agentic workflow=**self-organized graph**→STEV算法：textual gradients作backprop代理→前向路由+诊断梯度→**语义与拓扑共同演化→自发现高层意图模式** |
| **PIRA-Bench** (2603.08013) | **PIRF**: memory-aware state-tracking→从连续视觉输入中发现可行动意图→多交错意图+噪声轨迹 |
| **DIRECT** (2604.02767) | 三层级分层：Screenwriter(全局结构)→Director(实例化adaptive editing intent)→Editor(intent-guided) |

**电信启发**：Agent处理大量低级告警/工单后，可**自发现**更高层意图模式——如"周五晚间视频业务区频繁拥塞"→提炼出"周末高峰视频业务保障"这一高层意图。

---

## 新方向四：意图漂移检测与适应 (Intent Drift Detection & Adaptation)

**核心差异**：不再假设意图是静态的，而是**在线检测意图随时间/情境的变化并主动适应**。

| 论文 | 关键机制 |
|------|---------|
| **DeepContext** (2602.16935) | **RNN-based stateful monitoring**→跨turn传播hidden state→捕获增量风险累积→F1=0.84(vs stateless 0.67)→**建模意图的时间序列演化** |
| **Intent Assurance via LLM** (2402.00715) | **intent assurance框架**→检测intent drift→LLM生成AI-driven policies适配→continuous verification |
| **Long-term Task-oriented Agent** (2601.09382) | **Intent-Conditioned Monitoring**: 从对话历史自动制定触发条件→**Event-Triggered Follow-up**: 检测环境变化后主动跟进 |

**电信启发**：网络运维意图随业务周期漂移(如从"保障视频SLA"漂移为"保障游戏低延迟"——周末vs工作日)。Agent需实时检测意图漂移并调整运维策略，而非等人工重定义意图。

---

## 新方向五：自主目标发现 (Autonomous Goal Discovery)

**核心差异**：不再只执行给定目标，而是**Agent在环境中自主发现值得追求的新目标**。

| 论文 | 关键机制 |
|------|---------|
| **SAGA** (2512.21782, 11引用) | 双层架构：外层LLM提出新目标→转化为评分函数→内层优化→**目标函数本身被自动化设计** |
| **PAE** (2412.13194, ICML, 40引用) | Proposer根据环境上下文自主提出练习任务→Agent执行→VLM Evaluator判定→RL奖励 |
| **Alita** (2505.20286, 99引用) | 极简预定义+最大化自演化，从开源自主构建MCP工具 |
| **AlphaEvolve** (2506.13131, 542引用) | DeepMind标杆：coding agent自主发现算法和科学发现 |

**电信启发**：运维Agent可能自主发现**从未被人工定义但确实重要的目标**——如"特定小区组合的能耗优化模式"或"某类告警序列的早期预警模式"。

---

## 新方向六：自建评估标准 (Self-Constructed Evaluation Criteria)

**核心差异**：不再依赖外部奖励/评分，而是**Agent自己构建评估自身行为好坏的标准**。

| 论文 | 关键机制 |
|------|---------|
| **OpenSkill** (2606.06741) | 从文档/仓库构建**自建验证锚点**→不依赖target-task supervision→验证锚与ground-truth对齐 |
| **Dynamic Alignment** (2512.05464) | **Collective Agency**自对齐→自生成训练数据+自奖励→从human-defined values转向agent自主构建对齐标准 |
| **Agent-Pro** (ACL, 20引用) | **策略级反思**：不只反思单次行动，而是反思整个决策策略→自主识别策略缺陷→优化 |

**电信启发**：运维Agent无法总是依赖人工定义"什么是好的运维结果"——需要从网络指标的历史模式中**自建评估锚点**(如"KPI波动小于3σ即视为稳定")，并与专家验证对齐。

---

## 新方向七：能力边界自感知 (Capability Boundary Self-Awareness)

**核心差异**：不再盲目行动，而是**Agent能判断自己能做什么/不能做什么，不确定时主动求助**。

| 论文 | 关键机制 |
|------|---------|
| **CaRT** (2510.08517) | **反事实轨迹对训练**：一条应终止信息收集→一条不应终止→Agent学会"什么时候已经知道够了" |
| **HiL-Bench** (2604.09408) | **Ask-F1指标**：测量Agent选择性求助技能→发现所有前沿模型在求助判断上存在巨大差距 |
| **SAAS** (2605.29796) | **搜索边界建模**：对比search-disabled和search-enabled rollouts→边界感知reward→抑制过度搜索 |

**电信启发**：运维Agent面对新型/罕见故障时，应**主动求助而非盲目操作**——电信网络高可靠性要求"不该动的不动"。CaRT的反事实训练思路可直接应用于训练运维Agent的"何时干预/何时升级"判断。

---

## 新方向八：持续身份一致性 (Persistent Identity Consistency)

**核心差异**：不再只关注技能积累，而是**确保自演化过程中Agent核心行为逻辑不退化/不失控**。

| 论文 | 关键机制 |
|------|---------|
| **Darwin Gödel Machine** (2505.22954, 117引用) | 自修改代码+实证验证→维护agent档案库→**树状多样化结构**→每次修改验证不退化 |
| **GEA** (2602.04837) | 群组经验共享→框架级bug修复1.4次迭代(vs自演化5次)→**群体经验提供身份稳定性** |
| **GRASP** (2605.29668) | **硬回归预算**：新技能仅在被验证为净改进时才纳入→防止技能间互相破坏 |

**电信启发**：运维Agent自演化时最怕"新学的技能破坏旧的正确流程"——GRASP的硬回归预算和Darwin Gödel Machine的实证验证直接对应电信的**不退化/不回退**硬约束。

---

## 新方向九：Agent-环境共同演化 (Agent-Environment Co-Evolution)

**核心差异**：不再假设环境固定不变，而是**Agent改变环境→环境变化又塑造Agent演化方向**。

| 论文 | 关键机制 |
|------|---------|
| **SkillSmith** (2606.01314) | skill-tool**协同演化**→Lotka-Volterra生态模型→技能与工具互相催生需求 |
| **FMSP** (2507.06466) | Foundation Model自博弈→对抗环境中策略创新→vFMSP/NSSP/QDSP三种演化模式 |
| **WebEvolver** (EMNLP 2025) | Agent+World Model共同演化→虚拟服务器生成自指导训练数据 |

**电信启发**：运维Agent调整网络参数(改变环境)→网络行为变化→Agent需重新适应(被塑造)→如此循环。这是电信自愈网络的**闭环本质**，但现有研究大多假设环境固定。

---

## 新方向十：IBN + Agentic AI（电信意图网络新进展）

| 论文 | Venue | 关键机制 |
|------|-------|---------|
| **CAIF** (2603.01663) | **INFOCOM 2026** | 合约式Agentic Intent→**闭环验证在actuation之前审计意图**→确定性安全保证 |
| **IntAgent/NWDAF** (2601.13114) | arXiv | NWDAF分析引擎内嵌intent tools→实时网络分析自主推理 |
| **INTA** (2501.08760) | **ICNP 2025** | 意图中间表示+语法检查→语义一致性验证→98.15%准确率 |
| **Intent Negotiation** (ICIN 2024) | 中兴+中国移动 | **意图协商机制**赋能自治网络高级操作(工业实践) |
| **Agentic IBN for 6G** (2601.06640) | arXiv | 分层multi-agent+ReAct循环自主分解意图 |
| **MARE** (2604.06856) | EU项目 | 多agent IBS+安全交互pipeline→连接MITRE/NIST外部知识库 |

---

## 综合方向图谱

```
已有研究                    新方向
─────────────────────────────────────────────────
意图理解/识别/转译    →  ① 意图自演化/自精化 (Agent主动迭代精化意图)
                     →  ③ 层级意图自发现 (从低级操作自发现高层意图)
                     →  ④ 意图漂移检测 (在线检测意图时变)
意图信息补齐          →  ② 意图-能力对齐/Closure Gap (形式化缺口+弥合机制)
                     →  ⑦ 能力边界自感知 (知道何时求助而非盲动)
Skill库               →  ⑧ 持续身份一致性 (自演化不退化/不失控)
                     →  ⑨ Agent-环境共同演化 (skill-tool/tool-skill双向催生)
反思规划              →  ⑤ 自主目标发现 (不执行给定目标而是自发现新目标)
                     →  ⑥ 自建评估标准 (不依赖外部奖励而是自建锚点)
─────────────────────────────────────────────────
电信专属              →  ⑩ IBN+Agentic AI (意图闭环验证/意图协商/合约式安全)
```

**最值得深入的方向**（按电信启发价值排序）：

1. **意图-能力Closure Gap** (2604.25000) — 直接解决"运维意图超出Agent能力边界"的根本问题
2. **意图自演化/IntentRL** (2602.03468) — 从被动转译到主动精化，电信意图天然模糊
3. **意图漂移检测** (2602.16935 + 2402.00715) — 网络业务意图随时间漂移是真实痛点
4. **CAIF合约式意图闭环** (INFOCOM 2026) — 电信意图网络最前沿，闭环验证+安全保证
5. **Darwin Gödel Machine身份一致性** (117引用) — 自演化的"不退化"是电信硬约束
6. **自主目标发现/SAGA** — Agent可能发现人工未定义但确实重要的运维目标

是否需要对其中某个方向做更深入的第二遍检索(获取完整摘要+BibTeX)，或者将这些写入wiki？

---

## User

意图和智能体自学习方向的研究方向

---

## Assistant

基于四轮检索（总计约120篇论文），我将意图+智能体自学习的研究方向体系化整理如下：

---

## 意图 + 智能体自学习：研究方向全景图

### 0. 基座方向（已有研究）

| 方向 | 核心问题 | 成熟度 |
|------|---------|--------|
| 意图理解/识别 | 从自然语言/行为信号中提取用户意图 | 较成熟 |
| 意图转译 | 将意图映射为可执行的网络配置/操作序列 | 较成熟 |
| 意图信息补齐 | 检测意图模糊/不完整之处，通过交互补充 | 发展中 |
| Skill库构建与检索 | 从经验/演示构建技能库，按需检索复用 | 发展中 |
| 执行反思+任务规划 | 从执行失败轨迹反思，改进后续规划 | 发展中 |

这些方向共同构成**"意图→行动→反馈→改进"**的单闭环范式。以下新方向突破这一范式。

---

### 1. 意图自演化 (Intent Self-Refinement/Evolution) 🆕

**范式突破**：意图不再是**输入**，而是**Agent与用户/环境共同演化的产物**。

| 子方向 | 代表论文 | 核心机制 |
|--------|---------|---------|
| 意图迭代精化 | IntentRL (2602.03468) | shallow→deep意图精化图谱，Agent执行前主动澄清latent intent |
| 意图-奖励耦合演化 | Prism (2601.08653) | intent-aware reward驱动意图自演化调优 |
| 搜索式意图精化 | PaSaMaster (2605.14306) | 排序证据揭示缺口→refine intent→引导后续搜索 |
| 流式意图发现 | PASK (2604.08000) | streaming IntentFlow识别深层latent needs |
| 意图形式化gap定义 | Intent Formalization (2603.17150) | 定义intent gap核心问题，提出自精化研究议程 |

**关键洞察**：传统做法是"先理解意图再执行"；新范式是**"意图在执行中不断被精化"**——执行反馈反写意图描述，形成意图-行动双向闭环。

---

### 2. 意图-能力对齐 / Closure Gap 🆕

**范式突破**：不再假设Agent总能满足意图，而是**形式化意图与能力的结构性缺口**。

| 子方向 | 代表论文 | 核心机制 |
|--------|---------|---------|
| Closure Gap形式化 | Closure Gaps & Delegation Envelopes (2604.25000) | closure-gap向量量化缺口→delegation envelopes预授权行动空间区域 |
| 隐含意图分层对齐 | PersonalAlign (2601.09636, ACL 2026) | 分层意图记忆→从长期用户记录解析隐含意图→对齐到Agent能力边界 |
| 意图-行动对比对齐 | IntentScore (2604.05157) | plan-aware reward→contrastive alignment对齐行动与意图 |
| 双阶段意图验证 | DS-IA (2603.16207) | 语义防火墙+确定性级联验证器逐级验证capability |
| Spec推断优先 | Project Prometheus (2604.17464) | Intent Gap→先推断spec再生成代码→RQA验证 |

**关键洞察**：区分**closed-world solver**(能力内闭环)与**open-world agent**(需要delegation envelope扩权)——这是意图自治等级分级的理论基础。

---

### 3. 层级意图自发现 (Hierarchical Intent Discovery) 🆕

**范式突破**：不再只识别**显式意图**，而是从低级操作经验中**自发现/自提炼**更高层意图模式。

| 子方向 | 代表论文 | 核心机制 |
|--------|---------|---------|
| 语义-拓扑共同演化 | HiVA (2509.00189) | textual gradients作backprop代理→语义与拓扑共同演化→自发现高层意图模式 |
| 主动意图推荐 | PIRA-Bench (2603.08013) | memory-aware state-tracking→从连续输入中发现可行动意图 |
| 分层意图实例化 | DIRECT (2604.02767) | 三层级：全局结构→adaptive editing intent→intent-guided执行 |

**关键洞察**：运维Agent处理大量低级告警后，可**自发现**高层意图(如"周末视频业务保障")——这是ADN L3-L4自治的关键能力。

---

### 4. 意图漂移检测与适应 (Intent Drift) 🆕

**范式突破**：不再假设意图静态不变，而是**在线检测意图随时间/情境的变化并主动适应**。

| 子方向 | 代表论文 | 核心机制 |
|--------|---------|---------|
| 状态化意图演化追踪 | DeepContext (2602.16935) | RNN跨turn传播hidden state→建模意图时间序列演化→F1=0.84 |
| 意图保证闭环 | Intent Assurance via LLM (2402.00715) | 检测drift→LLM生成AI-driven policies适配→continuous V&V |
| 环境触发意图跟进 | Long-term Task-oriented Agent (2601.09382) | Intent-Conditioned Monitoring→Event-Triggered Follow-up→85.19%完成率 |
| 语义偏离检测 | Context Alignment Pre-processor (2603.16052) | 测量当前prompt与历史context语义相似度→偏离时启动structured clarification |

**关键洞察**：网络运维意图随业务周期/拓扑变化漂移——意图漂移检测是**意图生命周期管理**的缺失环节。

---

### 5. 自主目标发现 (Autonomous Goal Discovery) 🆕

**范式突破**：不再只执行给定目标，而是**Agent在环境中自主发现值得追求的新目标**。

| 子方向 | 代表论文 | 核心机制 |
|--------|---------|---------|
| 目标函数自动化设计 | SAGA (2512.21782) | 外层LLM提出新目标→转化为评分函数→内层优化→**目标本身被自动设计** |
| 自主技能发现 | PAE (2412.13194, ICML, 40引用) | Proposer自主提出任务→Agent执行→VLM Evaluator判定→RL奖励 |
| 极简预定义+最大化自演化 | Alita (2505.20286, 99引用) | 从开源自主构建MCP工具→自演化覆盖几乎所有能力 |
| 开放自博弈推理 | OpenSIR (2511.00602) | Teacher-Student交替→从单种子自发现数学问题→难度+多样性共优化 |
| 科学发现自主驱动 | AlphaEvolve (2506.13131, 542引用) | coding agent自主发现算法创新(DeepMind标杆) |

**关键洞察**：运维Agent可能自主发现**从未被人工定义但确实重要的运维目标**——这是ADN L4"全自治"的理论支撑。

---

### 6. 自建评估标准 (Self-Constructed Evaluation) 🆕

**范式突破**：不再依赖外部奖励/评分，而是**Agent自建评估自身行为好坏的标准**。

| 子方向 | 代表论文 | 核心机制 |
|--------|---------|---------|
| 自建验证锚点 | OpenSkill (2606.06741) | 从文档/仓库构建验证锚→不依赖target-task supervision→锚与ground-truth对齐 |
| 自奖励对齐 | Dynamic Alignment (2512.05464) | 自生成训练数据+自奖励→从human-defined转向agent自建对齐标准 |
| 策略级反思 | Agent-Pro (ACL, 20引用) | 反思整个决策策略而非单次行动→自识别策略缺陷→优化 |
| 自蒸馏RL | HERO (2606.11559) | 后验增强→用环境观测做局部对齐反馈→自建teacher信号 |

**关键洞察**：运维场景缺乏明确奖励函数(什么是"好的运维"？)——Agent需从网络指标历史模式中**自建评估锚点**，并与专家验证对齐。

---

### 7. 能力边界自感知 (Capability Boundary Awareness) 🆕

**范式突破**：不再盲目行动或过度求助，而是**精确知道自己能做什么、何时该求助**。

| 子方向 | 代表论文 | 核心机制 |
|--------|---------|---------|
| "知道够了"训练 | CaRT (2510.08517) | 反事实轨迹对→一条应终止信息收集→一条不应→学会"何时已经知道够了" |
| 选择性求助评估 | HiL-Bench (2604.09408) | Ask-F1指标→发现所有前沿模型求助判断有巨大差距→RL训练可改善且跨域迁移 |
| 搜索边界自感知 | SAAS (2605.29796) | 对比search-disabled/enabled rollouts→边界感知reward→抑制过度搜索 |
| 意图条件化监控 | Long-term Agent (2601.09382) | 从对话历史自动制定触发条件→检测环境变化后主动跟进 |

**关键洞察**：电信高可靠性要求"不该动的不动"——**能力边界自感知是运维Agent安全部署的前提**。

---

### 8. 持续身份一致性 / 自演化不退化 (Identity Consistency) 🆕

**范式突破**：不再只关注技能积累，而是**确保自演化过程中核心行为逻辑不退化/不失控**。

| 子方向 | 代表论文 | 核心机制 |
|--------|---------|---------|
| 实证验证树 | Darwin Gödel Machine (2505.22954, 117引用) | 自修改代码→每次修改实证验证→树状多样化agent库→不退化 |
| 群组经验共享 | GEA (2602.04837) | 群体演化而非个体→经验共享提供稳定性→bug修复1.4次迭代(vs 5次) |
| 硬回归预算 | GRASP (2605.29668) | 新技能仅验证为净改进才纳入→硬回归预算防止技能间互相破坏 |
| Harness更新≠收益 | Harness Updating ≠ Benefit (2605.30621) | harness-updating能力平坦(不同模型产生相似更新)→harness-benefit非单调→应投资task-solving而非evolver |

**关键洞察**：电信"不退化"硬约束 → GRASP硬回归预算 + Darwin Gödel Machine实证验证是**最直接的保障机制**。

---

### 9. Agent-环境共同演化 (Agent-Environment Co-Evolution) 🆕

**范式突破**：不再假设环境固定，而是**Agent改变环境→环境变化塑造Agent→双向闭环**。

| 子方向 | 代表论文 | 核心机制 |
|--------|---------|---------|
| skill-tool协同演化 | SkillSmith (2606.01314) | 反思产生原子bundle同时修改skill和tool→Lotka-Volterra生态模型→技能与工具互相催生 |
| 基础模型自博弈 | FMSP (2507.06466) | vFMSP/NSSP/QDSP→对抗环境中策略创新→环境对手进化→Agent必须进化 |
| Agent+World Model协同 | WebEvolver (EMNLP 2025) | World Model做虚拟服务器→生成自指导训练数据→推理时做想象引擎 |
| 自演化仿真闭环 | DreamGym (2511.03773) | 合成多样经验→sim-to-real transfer→Agent和仿真共同演化 |
| 持续harness在线适应 | Continual Harness (2605.09998) | reset-free→prompt+skill+memory同时演化→Agent与harness(微环境)共同演化 |

**关键洞察**：运维Agent调整网络参数(改变环境)→网络行为变化→Agent需重新适应——**这是电信自愈网络的闭环本质**，但现有研究大多假设环境固定。

---

### 10. IBN + Agentic AI（电信意图网络前沿）🆕

**范式突破**：将意图网络与Agentic AI结合，**意图不再是静态policy而是Agent持续演化的驱动信号**。

| 子方向 | 代表论文 | Venue | 核心机制 |
|--------|---------|-------|---------|
| 合约式意图闭环验证 | CAIF (2603.01663) | **INFOCOM 2026** | 合约审计→actuation前验证意图→确定性安全保证 |
| NWDAF意图Agent | IntAgent (2601.13114) | arXiv | 实时网络分析+intent tools→自主推理和工具选择 |
| 意图中间表示+语义验证 | INTA (2501.08760) | **ICNP 2025** | 语法检查引导增量生成→语义一致性→98.15%准确率 |
| 意图协商(工业实践) | Intent Negotiation (ICIN 2024) | ICIN | 中兴+中国移动→意图协商机制赋能自治网络 |
| 分层multi-agent意图分解 | Agentic IBN 6G (2601.06640) | arXiv | ReAct循环+RAN/Core specialist→自主分解意图 |
| 安全意图pipeline | MARE (2604.06856) | EU项目 | 多agent+MITRE/NIST知识库→冲突发现+安全审计 |
| 意图冲突博弈 | Direct-Conflict (2401.08341) | EW | KSBS/Jain公平指数→最公平冲突仲裁 |
| 逆学习意图推断 | Inverse Learning V2I (2606.13091) | arXiv | 从观测行为推断底层意图效用函数→ATIL/FICNNIL |

**关键洞察**：**INFOCOM 2026的CAIF是电信意图网络+Agentic AI的最前沿**——合约式闭环验证在actuation前审计意图，提供确定性安全保证，这直接对齐ADN的"意图保证"需求。

---

## 方向间关系图谱

```
                    ┌─────────────────────────────────────┐
                    │          自主目标发现 (#5)            │
                    │   "不执行给定目标，自发现新目标"       │
                    └──────────────┬──────────────────────┘
                                   │ 自发现的目标需要
                    ┌──────────────▼──────────────────────┐
                    │      自建评估标准 (#6)                │
                    │   "不依赖外部奖励，自建锚点"          │
                    └──────────────┬──────────────────────┘
                                   │ 评估结果反馈到
         ┌─────────────────────────▼──────────────────────────┐
         │                    意图自演化 (#1)                   │
         │           "意图不再是输入，而是演化产物"             │
         └────────────┬───────────────────────┬───────────────┘
                      │                       │
     ┌────────────────▼────────┐    ┌─────────▼──────────────────┐
     │  层级意图自发现 (#3)     │    │  意图-能力对齐 (#2)         │
     │  "从低级操作自发现       │    │  "形式化意图与能力gap        │
     │   高层意图模式"          │    │   +弥合机制"                │
     └─────────────────────────┘    └────────────┬────────────────┘
                                                  │ gap需要感知边界
                    ┌─────────────────────────────▼──────────────┐
                    │     能力边界自感知 (#7)                      │
                    │     "知道自己能做什么/何时求助"               │
                    └────────────────────┬───────────────────────┘
                                         │ 边界内行动需
                    ┌─────────────────────▼──────────────────────┐
                    │    Agent-环境共同演化 (#9)                    │
                    │    "Agent改变环境，环境塑造Agent"             │
                    └────────────────────┬───────────────────────┘
                                         │ 演化过程需保证
                    ┌─────────────────────▼──────────────────────┐
                    │   持续身份一致性 (#8)                         │
                    │   "自演化不退化/不失控"                       │
                    └────────────────────────────────────────────┘
                    
                    ┌────────────────────────────────────────────┐
                    │   意图漂移检测 (#4)                          │
                    │   "在线检测意图时变并适应" ← 横切所有方向     │
                    └────────────────────────────────────────────┘
                    
                    ┌────────────────────────────────────────────┐
                    │   IBN + Agentic AI (#10) ← 电信领域锚定     │
                    │   "意图→合约→闭环→安全"                      │
                    └────────────────────────────────────────────┘
```

---

## 对电信(智能运维/ADN)的映射

| 新方向 | 电信痛点映射 | ADN自治等级 |
|--------|-------------|------------|
| #1 意图自演化 | 运维意图天然模糊，需从告警反馈自精化 | L2→L3 |
| #2 意图-能力对齐 | "保障SLA"意图与Agent实际能力的结构性缺口 | L2→L3 |
| #3 层级意图自发现 | 从大量告警自发现高层运维意图模式 | L3→L4 |
| #4 意图漂移检测 | 业务意图随时间漂移(周末/工作日/节假日) | L3 |
| #5 自主目标发现 | Agent可能发现人工未定义但重要的运维目标 | L4 |
| #6 自建评估标准 | 缺乏明确运维奖励函数→自建"稳定"评估锚点 | L3→L4 |
| #7 能力边界自感知 | 电信"不该动的不动"→精确知道何时求助 | L2→L3 |
| #8 身份一致性 | 自演化不退化/不回退(电信硬约束) | 全等级 |
| #9 Agent-环境共演化 | 自愈网络闭环本质(调参→网变→再适应) | L3→L4 |
| #10 IBN+Agentic AI | 意图→合约→闭环验证→确定性安全保证 | L3→L4 |

---

## 开放问题与交叉机会

1. **意图漂移 × Agent-环境共演化**：网络意图漂移与网络拓扑变化是**同一过程的两面**——能否统一建模？
2. **Closure Gap × 能力边界自感知**：delegation envelope的大小应由Agent的能力边界自感知**动态调整**
3. **层级意图自发现 × 自主目标发现**：从告警自发现的"高层意图"和自主发现的"新运维目标"是**同一机制的不同层级**
4. **身份一致性 × IBN合约**：CAIF的合约审计可视为**外部强制的身份一致性保障**——能否内化为Agent自感知？
5. **自建评估标准 × 意图自演化**：Agent自建评估锚点的同时，意图也在演化——**评估标准和意图需同步演化**

---

这些是当前检索能覆盖的方向。如需对某个方向做更深度的第二遍检索（拉完整摘要+BibTeX+引用网络），或将整体写入wiki，可以继续推进。

---

## User

Agent自学习方向有什么发力点？

---

## Assistant

基于已检索的~120篇论文密度分布和电信痛点匹配度，Agent自学习的发力点分析如下：

---

## 发力点判断框架

| 维度 | 说明 |
|------|------|
| **空白度** | 该方向现有论文数量，空白=机会 |
| **电信刚需度** | 是否直接解决电信/ADN痛点 |
| **可行性** | 能否在现有技术栈上验证 |
| **可区分度** | 是否能产出非增量贡献 |

---

## 第一梯队发力点（空白度高 + 电信刚需）

### 🔴 发力点A：意图-能力Closure Gap形式化与弥合

**空白度**：极高。仅1篇形式化论文(Closure Gaps & Delegation Envelopes, 2604.25000)，且是position paper尚未实证。

**电信刚需**：核心痛点。运维意图("保障切片SLA")与Agent实际能力(只能调特定参数)之间的**结构性缺口**是ADN自治等级跃迁的根本障碍——L2到L3的关键在于能否形式化并弥合这个gap。

**可行性**：高。可在现有IBN框架上引入closure-gap向量量化意图-能力缺口，用delegation envelope定义预授权行动范围，闭环验证验证弥合效果。

**可区分度**：极高。这是**意图研究从"理解"到"对齐"的范式跃迁**，不是增量改进。

**建议路径**：
1. 定义电信运维场景的closure-gap分类体系(信息gap/权限gap/能力gap/时域gap)
2. 设计delegation envelope的分级授权机制(对应ADN L0→L4)
3. 在数字孪生/仿真环境中实证验证gap弥合的闭环效果
4. 建立intent-capability alignment benchmark

---

### 🔴 发力点B：意图漂移在线检测与适应

**空白度**：极高。仅2篇直接相关(DeepContext 2602.16935, Intent Assurance 2402.00715)，且均非电信场景。

**电信刚需**：真实痛点。网络运维意图随业务周期漂移——工作日"保障企业专线SLA"→周末"保障视频低延迟"→节假日"保障即时消息高并发"。现有IBN假设意图静态，**完全缺失漂移处理能力**。

**可行性**：高。DeepContext的RNN状态化意图追踪可直接迁移——将网络KPI时间序列作为意图漂移信号源，Intent Assurance的LLM policy适配机制可做漂移后的策略调整。

**可区分度**：极高。**意图漂移是IBN领域公认但无人解决的开放问题**。

**建议路径**：
1. 定义电信意图漂移分类(周期型/趋势型/突变型/隐含型)
2. 构建意图漂移检测器(KPI时间序列→意图效用函数变化率)
3. 设计漂移适应机制(意图重参数化+策略微调+delegation envelope动态扩缩)
4. 用真实网络KPI数据验证检测灵敏度和适应延迟

---

### 🔴 发力点C：自演化不退化保障(身份一致性)

**空白度**：中等偏高。Darwin Gödel Machine(117引用)开了方向，但**无人将实证验证机制引入电信运维场景**。GRASP的硬回归预算思路直接匹配电信需求但尚未被关注。

**电信刚需**：硬约束。电信网络"不退化/不回退"是零容忍——运维Agent自学习新技能后绝不能破坏已有正确流程。现有skill库/反思方法**无回归保护机制**。

**可行性**：高。GRASP的"硬回归预算"可直接迁移——对每个新运维技能在held-out probe上验证净改进才纳入；Darwin Gödel Machine的实证验证树可确保每次策略修改经过真实/仿真网络验证。

**可区分度**：高。**将"不退化"从运维常识上升为可形式化、可验证的理论机制**。

**建议路径**：
1. 定义运维技能回归的形式化度量(回归预算=允许的性能下降上限)
2. 设计技能纳入门控机制(held-out probe + 硬回归预算验证)
3. 构建运维策略版本树(每次修改保留前版本，实证验证后才切换)
4. 在仿真网络中验证门控机制对关键运维流程的保护效果

---

## 第二梯队发力点（空白度中高 + 电信强相关）

### 🟡 发力点D：层级意图自发现（从告警自提炼运维意图）

**空白度**：中高。HiVA(2509.00189)提出语义-拓扑共演化框架，PIRA-Bench(2603.08013)有benchmark，但**无人将"从低级操作自发现高层意图"应用于电信告警场景**。

**电信刚需**：强相关。运维Agent处理大量低级告警/工单后，应能自发现"周五晚间视频业务区频繁拥塞"→提炼出"周末高峰视频业务保障"这一高层运维意图。当前完全依赖人工定义运维意图。

**建议路径**：从告警序列聚类→时序模式挖掘→意图语义提升的三层pipeline，在真实告警数据上验证意图发现的准确率和覆盖率。

---

### 🟡 发力点E：Agent-环境共同演化（运维闭环本质）

**空白度**：中高。SkillSmith(skill-tool协同演化)、WebEvolver(Agent+World Model协同)、Continual Harness(在线适应)提供了技术组件，但**无人将Agent-环境共演化整体框架化**并应用于电信自愈场景。

**电信刚需**：强相关。运维Agent调整网络参数→网络行为变化→Agent需重新适应——这是电信自愈网络的**闭环本质**，但几乎所有AIOps研究假设环境固定或只做一次性适应。

**建议路径**：将SkillSmith的Lotka-Volterra生态模型引入运维技能-工具生态，建模运维技能间互补/冲突关系，在网络仿真中验证skill-tool协同演化对闭环自愈效果的增益。

---

## 第三梯队发力点（空白度低但电信空白）

### 🟢 发力点F：IBN + Agentic AI闭环验证

**空白度**：IBN领域空白但Agent自学习领域拥挤。CAIF(INFOCOM 2026)是唯一将合约式闭环验证引入IBN的论文，INTA(ICNP 2025)有意图中间表示+语义验证。

**电信刚需**：直接对应。ADN的"意图保证"需要闭环验证——当前IBN框架缺乏actuation前的确定性安全审计。

**风险**：IBN领域已有大量传统工作(不涉及Agent自学习)，增量贡献可能有限。建议聚焦CAIF的**合约式验证+Agent自学习**交叉点，而非纯IBN方向。

---

### 🟢 发力点G：自建评估标准（运维奖励函数自构建）

**空白度**：中等。OpenSkill(自建验证锚点)、Dynamic Alignment(自奖励对齐)提供了机制，但**无人将"自建评估"引入运维场景解决奖励函数缺失问题**。

**电信刚需**：中等。运维缺乏明确奖励函数("什么是好的运维？")，但可从网络KPI历史模式自建评估锚点。

**风险**：运维场景有天然评估信号(KPI波动、告警数量、MTTR)，自建评估的必要性不如意图漂移/closure gap那么紧迫。

---

## 发力点优先级矩阵

```
              电信刚需度
              高        中        低
         ┌──────────┬──────────┬──────────┐
   高    │  A Closure │  D 层级  │          │
空白度   │    Gap     │  自发现  │          │
         │  B 意图漂移│  E 共演化│          │
         ├──────────┼──────────┼──────────┤
   中    │  C 不退化  │  G 自建  │  自博弈  │
         │   保障     │  评估    │  自蒸馏  │
         ├──────────┼──────────┼──────────┤
   低    │  F IBN+   │  Skill库 │  经验蒸馏│
         │   Agent   │  (拥挤)  │  (拥挤)  │
         └──────────┴──────────┴──────────┘
```

---

## 总结：三个核心发力点

| 发力点 | 一句话定位 | 为什么是最佳发力点 |
|--------|-----------|------------------|
| **A. Closure Gap形式化与弥合** | 意图从"理解"到"对齐"的范式跃迁 | 空白度最高+直接解决ADN自治等级跃迁障碍+可产出非增量理论贡献 |
| **B. 意图漂移在线检测与适应** | 意图从"静态"到"时变"的范式跃迁 | IBN领域公认但无人解决+电信真实痛点+可直接在真实KPI数据上验证 |
| **C. 自演化不退化保障** | 自学习从"积累"到"受控演化"的范式跃迁 | 电信零容忍硬约束+GRASP/Darwin Gödel已有技术组件可迁移+可形式化可验证 |

**三者共同构成"受控意图驱动自学习"的理论框架**：
- Closure Gap → **界定自学习边界**（学什么、不学什么）
- 意图漂移 → **驱动自学习方向**（何时该学、学什么方向）
- 不退化保障 → **约束自学习过程**（学到的东西不能破坏已有能力）

这三个发力点的组合，恰好是ADN从L2条件自治跃迁到L3/L4全自治所缺失的**三个理论基石**。

---

是否需要我对某个发力点制定详细的研究路线图（含milestone、验证方案、论文目标），或者先对A/B/C做更深入的第二遍检索（拉核心论文完整摘要+引用网络+BibTeX）？

---

