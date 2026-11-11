# 课题2工程定义：金型CAD结构统制语彙调查与设计 — Obsidian轻量版 v4

文件版本：v4（由v3精简，内容范围不变）
编制日期：2026-10-05
用途：供研究人员阅读，也可作为编码 Agent 的实施指示。
语言：工程说明用中文；概念名称、定义、模板、资料整理以英文为主；日文资料从一开始就可使用，原表记保留，日语对应词核对后补入同一概念笔记。口头汇报可用日语。

> 本文是工程定义，不代表词汇调查已完成。文中示例定义均为待核对的设计草案。

本版用 Obsidian 原生功能整理约10个核心概念，并对少量重要图示做信息整理。检查脚本、完整属性体系、多领域扩充均为后续可选，不是开始调查的前提。

**v3→v4 的主要变化**：取消 TERM/SRC/VOC 编号，文件直接用英文名；压缩资料清单、著作权和图示流程；合并重复的实施说明；去掉与"不凑数"原则矛盾的验收项。

## 1. 本次要做什么

不是把网上的CAD资料搬进Obsidian，而是回答三个问题：

1. 其他领域的统制语彙为什么建立？怎样选词、统一定义、组织关系、维护更新？
2. CAD系统和金型资料实际用哪些词描述结构？同词是否异义？异词是否同义？
3. 描述金型CAD应保留哪些概念、用什么首选名称、怎样规定粒度与关系？

最终产物：一个可追溯来源、可查看定义、可区分近义概念的 Obsidian 知识库，加一份简短的词汇设计说明。图谱只是入口，不代替定义和证据。

### 1.1 对应原任务

| 原任务要求 | 本工程产物 |
|---|---|
| 調査：各分野の統制語彙が作られた目的 | 调查笔记中的 Purpose and scope |
| 調査：統制語彙が整備された手順 | 调查笔记中的 Development and maintenance；方法比较表 |
| 既存CADシステム・資料の構造表現語彙を収集 | 每份资料的术语用法表（章节、语境、来源） |
| 整理・分類 | 概念笔记、分类、同义表达、区分关系 |
| 金型CAD向け統制語彙の設計 | 设计说明（首选名称、粒度、关系、维护规则） |

"当前已参考的统制语彙"以老师提供的提案书及参考资料为准。未获得清单前，在 README 待确认列表记录；不得把 MeSH、AAT 等写成提案书原有参考对象。

### 1.2 范围边界

**包含**：资料调查、术语收集、概念整理、重要图示的信息整理、关系设计、Obsidian展示。

**不包含**：课题3的数据库、RAG、PageIndex；现有STL处理、LLM生成、向量检索工程；向量库、服务端、MCP、模型训练、专用图数据库。

**首批范围**：先整理当前CAD样本涉及的共通结构词（hole、pocket、slot、chamfer、fillet 等），再按老师资料选**一种**金型领域扩充，不同时调查射出成形与冲压。其他领域用法可记录，不展开。不同领域同名术语须在正文注明适用范围，不得未经核对合并。

**语言方针**：英文先行，日语后补。英文先行不排除日文来源，也不把机器翻译当作已确认的同义词。*待确认*：若汇报对象和课题3下游主要使用日语，需与老师确认英文先行是否合适。

## 2. 工作顺序

| 顺序 | 做什么 | 输出 |
|---|---|---|
| 1 | 整理参考资料与研究对象 | 来源笔记、待确认清单 |
| 2 | 调查既有统制语彙的目的和建设步骤 | 调查笔记、方法比较表 |
| 3 | 从CAD资料正文、图注、重要图示摘出真实用法 | 术语用法表、图示小节 |
| 4 | 同一概念的表达归入同一概念笔记 | 概念笔记 |
| 5 | 建立有依据的概念关系 | 正文链接 |
| 6 | 检查并说明未解决问题 | 检查记录、设计说明、问题清单 |

先记录实际用法，再形成概念草案；不要先生成一堆词条再找引用。Agent 可建目录、模板、整理有依据的草案；专业含义必须有资料支持。

## 3. Obsidian工程结构

新建独立 Vault `mold-cad-vocabulary`，与现有CAD检索代码目录分开。

```text
mold-cad-vocabulary/
  00_Guide/
    README.md
    Vocabulary_Method_Comparison.md
    Design_Policy.md
  10_Vocabulary_Studies/     # 每个调查对象一篇，文件名用其名称
  20_Sources/                # 每份CAD/金型资料一篇
  30_Concepts/               # 每个概念一篇，如 Hole.md、Cylindrical_Surface.md
  80_Assets/                 # 有使用依据才存图片/PDF，可为空
  90_Templates/
    Vocabulary_Study.md
    Source.md
    Concept.md
```

具体调查对象和文件名在确认老师参考清单后确定，不预设。笔记必须标明调查状态，不能因模板存在就视为已完成。

`README.md` 集中记录：调查对象、进度、共通待确认事项、检查记录。词条自身的未确认问题写在该词条的 Open questions，不在README重复。

### 3.1 命名规则

- 文件名即标题：概念用英文首选名（`Hole.md`），来源用资料简称（`Creo_Hole_Feature.md`）。避免路径分隔符、冒号等不适合文件名的字符。
- 一个概念一篇笔记；英文首选名和后来确认的日语对应放在同一篇，不因语言复制概念。
- 同名异义概念分别建笔记，名称后加适用领域，如 `Core_(mold_component).md`；不得仅凭名称合并。
- 来源的拼写差异（mold／mould）保留原表记；选定首选写法后，确认同义的再加入 aliases。
- 资料版本变化先更新来源笔记；只有需要比较两个版本的定义时才建两条来源。
- Obsidian 重命名默认自动更新内部链接；重命名后仍抽查几条链接。
- 不建额外数据库；Markdown笔记就是维护位置。

### 3.2 日语补充

| 阶段 | 做什么 | 不确定内容放哪 |
|---|---|---|
| 第一轮：英文整理 | 英文首选名与定义；英日资料均可作依据；保存原表记 | 日英对应、定义范围问题写进 Open questions |
| 后续：日语核对 | 核对同一含义的日语名称，必要时补一段日语说明 | 未确认等价的保留为候选，不写入 aliases |

同一日语词在不同领域指不同对象时，不能因英译相同就合并。原资料出现的词不自动等于本项目首选名。

## 4. 资料怎么找、怎么记录

### 4.1 权威性分层

| 资料类型 | 用途 | 注意 |
|---|---|---|
| 标准、正式术语集 | 核对术语范围、正式名称、定义 | 记录编号、版本、条款、实际访问情况 |
| CAD系统官方帮助 | 收集系统实际用名、参数、操作语境 | 功能名不一定等于行业统一概念 |
| 金型厂商、行业机构资料 | 收集实际工程用语和功能区分 | 记录金型类型、使用场景 |
| 教材、教程、论文 | 理解背景和概念边界 | 论文自定义名称不当行业标准 |
| 自己提出的定义 | 填补本项目需要 | 标注为「設計案」，写依据与待确认项 |

冲突时保留不同用法并说明适用范围，不按"最先查到"取舍。

### 4.2 候选入口

这是入口清单，不是任务清单。先选2～3个统制语彙案例、2～3份与当前概念相关的CAD／金型资料。以下入口2026-10-01核对过可访问；这不代表全文、图示、定义、使用许可已核实。

**统制语彙建设方法**

| 对象 | 研究什么 | 入口 |
|---|---|---|
| MeSH | 为索引检索统一名称的目的；词汇组织与维护 | [NLM: Introduction to MeSH](https://www.nlm.nih.gov/mesh/introduction.html) |
| AAT | 概念、首选名、范围说明、来源依据 | [Getty: AAT Editorial Guidelines](https://www.getty.edu/publications/vocabularies-editorial-guidelines/aat-guidelines/) |
| JST科学技術用語シソーラス | 新增、合并、拆分、层级的修订过程 | [JST科学技術用語シソーラスの改訂](https://www.jstage.jst.go.jp/article/johokanri/60/5/60_365/_html/-char/ja) |
| SKOS | 首选名、别名、上下位、关联的表示原则 | [W3C: SKOS Primer](https://www.w3.org/TR/skos-primer/) |

SKOS 是知识组织的表示模型，不是金型术语集；首版只参考其概念区分，不实现RDF。厂商 Glossary 不自动等同于 MeSH/AAT 那样有建设维护机制的统制语彙。

**CAD／金型资料（英日）**

| 资料 | 优先收集 | 边界 |
|---|---|---|
| [Onshape: Fillet](https://cad.onshape.com/help/Content/PartStudio/fillet.htm)／[Chamfer](https://cad.onshape.com/help/Content/PartStudio/chamfer.htm) | fillet、chamfer 的形状与参数 | 系统参数不等于通用结构属性 |
| [PTC Creo Elements/Direct: Recognized features](https://support.ptc.com/help/creo/ced_modeling/r20.8.0.0/en/ced_modeling/OSDM_Main/Modify3D_RecognizedFeat.html) | boss、pocket、rib、slot、hole | 特定软件的识别规则，不当通用定义 |
| [PTC Creo: About Machining Features](https://support.ptc.com/help/creo/creo_pma/r12/usascii/manufacturing/expmach/about_machining_features.html) | pocket、slot、floor、wall 等加工用语 | 加工分类不无条件移植到CAD形状 |
| Autodesk Inventor 2023 Mold Glossary：[EN](https://help.autodesk.com/cloudhelp/2023/ENU/Inventor-Help/files/GUID-63A5DCE8-2B43-494F-8F56-7A7CBBAD41FC.htm)／[JA](https://help.autodesk.com/cloudhelp/2023/JPN/Inventor-Help/files/GUID-63A5DCE8-2B43-494F-8F56-7A7CBBAD41FC.htm) | cavity、core、gate、runner、cooling channel | 英日配对同版本；含工艺、材料、设备词，只选结构相关条目 |
| [PTC Creo: 穴フィーチャーについて](https://support.ptc.com/help/creo/creo_pma/r13/japanese/part_modeling/part_modeling/About_the_Hole_Feature.html) | 単純穴、皿穴、カウンタボア等 | 与上面Creo英文页不是同页翻译对 |
| [MISUMI: Plastic Molding Tutorial](https://www.misumi-techcentral.com/tt/en/mold/) | cavity、core、core pin、runner、gate、mold base | 从目录进入相关篇目，不批量收集 |
| JEED プラスチック金型教材：[用語集](https://www.tetras.uitec.jeed.go.jp/plastic_mold/glossary/index.html) | 入れ子、ガイドピン、エジェクタピン、アンダーカット | 学习图中对象与日文名称对应 |
| [ISO 12165:2019](https://www.iso.org/standard/75669.html) | 成形金型部件的术语与符号 | 仅核对了官方概要；AI使用限制见4.4 |

**其他备选入口（按需）**：[Inventor 2026 穴フィーチャ](https://help.autodesk.com/cloudhelp/2026/JPN/Inventor-Help/files/GUID-94EB6947-0347-4888-870D-4BA22DB144D8.htm)、[SOLIDWORKS Fillet](https://help.solidworks.com/2025/japanese/SolidWorks/sldworks/c_fillet_overview.htm)、[Fusion 2D Pocket](https://help.autodesk.com/cloudhelp/JPN/Fusion-CAM/files/2D-POCKET-READ.htm)、[MISUMI キャビティ・コア構造](https://jp.misumi-ec.com/tech-info/categories/plastic_mold_design/pl07/c0450.html)、[芝浦機械 用語](https://www.shibaura-machine.co.jp/jp/product/shashutsu/glossary/)、[ヤマハ発動機 鋳造用語集](https://www.yamaha-motor.co.jp/cf/data/glossary/)、[エリプス MoreStudy](https://www.cloud.ellipse.ne.jp/MoreStudy.html)、[日本金型工業会 用語](https://www.jdmia.or.jp/terminology/)、[JIS検索](https://www.jisc.go.jp/app/jis/general/GnrJISSearch.html)、[AutoForm 用語集](https://www.autoform.com/jp/glossary/)（冲压，首批不展开）。检索入口不等于全文；使用时记录实际访问范围。

**建议的第一轮顺序**

1. 用 Onshape 与 Creo 官方帮助试做约10个结构概念；每个概念有实际用法依据，不要求两套软件都查。
2. 需要金型功能词时，从 Autodesk 英日用語集或 MISUMI 选一种射出成形资料展开。
3. 日文资料从一开始可读：保留原表记，用英文解释语境；对应含义核对后才加日语别名。
4. JEED、芝浦機械等只用于补充语境或解决具体冲突。
5. ISO 等标准按可用许可人工核对，不以购买全文为前提。

### 4.3 不只摘词，还要保留用法

每篇来源笔记含下表。记录术语、技术事实和自己理解后的说明，不默认复制大段原文。

| 原资料的表记 | 页码／章节／图号 | 语境摘要 | 对应候选概念 | 核对情况 |
|---|---|---|---|---|
| 原语言表记 | 可定位的位置 | 英文说明该词指结构、参数、功能还是操作 | 已建概念填内部链接 | checked／needs checking |

例如 `pocket` 可能指实体凹腔、CAD建模命令、CAM刀路操作，三者相关但不能因同词合并。未能定位章节写"定位未确认"，不虚构页码；只报告实际核对的内容，不要求读完整本资料。

### 4.4 著作权与AI使用（精简规则）

以日本研究环境为主要考虑；具体资料的许可仍须按实际判断。

1. **可以收集**：术语名称、技术事实、自行理解后的概念说明，并保留来源定位。
2. **默认不保存**：PDF/网页全文、完整译文、完整定义表、整套词表、插图和截图。确需保存时，按许可或适用的法定例外处理。
3. **引用**：只在比较或论证必需时引用，与自己的说明明确区分，注明出处。标出处、控制字数或写"研究用"都不单独保证引用成立。
4. **不用改写替代授权判断**：逐句换词、翻译、AI摘要不当然消除版权问题；不通过大批摘要或翻译重现原资料的独创性内容。公开可访问不等于可任意复制；公司内部共享不等于私人使用。
5. **输入AI**：只输入任务所需的内容；"本地运行"或"研究用途"不自动允许输入原文。未确认条件时，不把整份付费标准、会员资料、整本手册批量送入AI。云端AI另须遵守公司外部传送规则（不为此新增匿名化、加密或审计系统）。AI输出须核对是否沿用原文表达、是否错误合并概念，且不自动成为已核对定义。
6. **ISO（已知具体限制）**：ISO官方页面使用声明限制将其内容用于AI（包括作为生成回答的输入）。未取得许可依据前，ISO 作为人工核对来源，其原文、图示、截图不送入任何LLM。购买全文不等于取得AI输入或共享许可。依据：[ISO官方页面](https://www.iso.org/standard/75669.html)，核对日期2026-10-01。其余资料各按实际条件判断。
7. 不建AI训练语料库。

**每份资料的使用记录（Source笔记里写一行即可）**：来源URL与版本；利用条件或许可链接（未查到写「未確認」）；实际保存方式（术语与事实记录／自行撰写说明／引用某一段／按许可保存图片）。条件未确认不阻止常规阅读和独立事实整理；涉及原文、图片、整表复制、对外发布时再核对。

参考：[文化庁 FAQ](https://www.bunka.go.jp/seisaku/bunka_gyosei/kibankyoka/faq/index.html)（5-⑩ 概念与表达，5-⑬ 引用）、[CRIC Q&A](https://www.cric.or.jp/qa/shigoto/sigoto5_qa.html)、[文化庁：AIと著作権に関する考え方](https://www.bunka.go.jp/seisaku/bunkashingikai/chosakuken/pdf/94037901_01.pdf)。

### 4.5 图片中的信息怎样进入Obsidian

目标：把重要图示整理成可搜索、可核对的文字证据，再连到概念。Obsidian 搜索和图谱不会识别图片里的术语，所以必须写进 Markdown。依据：[Search](https://help.obsidian.md/plugins/search)、[Graph view](https://help.obsidian.md/plugins/graph)。

**范围**：试做 3～5 张有结构说明价值的图（剖面、部件标注、形状对照、术语解释图）。这是验证方法的规模，不是配额；没有适合的图就不凑。

**流程**

1. 选图并记录来源位置：标题、URL、版本、页码／章节／图号；未编号图记录实际位置，不虚构编号。
2. 把图与图注、附近正文一起阅读；输入模型的内容按4.4判断。
3. 用现有多模态工具生成英文草稿；日文标注保留原文，未核对的英译标 provisional。
4. 重点核对：引出线指向、易混淆形状、剖面／隐藏线、单位、部件关系。
5. 写入对应 Source 笔记的一个图示小节，并链接到相关概念。

**记录规则**

- 标注看不清写 unreadable，不猜。
- 可见观察与作者解释分开；功能不得仅凭外观补造。
- 尺寸只记图中明确标出或正文给出的，不从示意图像素估算；单个剖视开口不能证明整个零件有贯通孔；单一视图不能证明完整三维结构。
- 图中"A与B接触"是图示实例关系，"A是一类金型部件"是概念关系，不互换。图示也不能为STL样本提供功能真值。
- 原图附件可选；没有附件仍可保存定位和自行整理的事实说明。AI重绘不消除版权问题。

**图示小节格式**（假设性示例，只有来源确有对应图示才填）

```markdown
## Figure 2 — Hole entrance comparison

- Location: page/section, figure identifier as printed in the source
- Original labels: Counterbore; Countersink
- Visible information: left shows a cylindrical enlarged entrance; right shows a conical one
- Source explanation: factual summary of the caption/text (not supplied → write "not supplied")
- Concepts: [[Counterbore]] — supports the entrance-shape description; [[Countersink]] — supports the comparison
- Uncertainty: the figure does not show whether the holes pass through. Draft: check labels against the original.
```

可选嵌入：`![[Creo_Hole_Feature_fig02.png|500]]`（图片放 `80_Assets/`）；合法可用的PDF可 `![[file.pdf#page=12]]`，印刷页码不同时在定位说明中注明。依据：[Embed files](https://help.obsidian.md/embeds)。概念笔记可链接到具体小节：`[[Creo_Hole_Feature#Figure 2 — Hole entrance comparison]]`。

**给多模态LLM的指示**（输入需含图、图注、附近正文、来源定位；可附现有概念名清单，不需送整个Vault）

```text
You are helping organize CAD and mold terminology evidence for an
English-first Obsidian vault. Use only the supplied figure, caption,
surrounding text, and source metadata.

Write a concise Markdown subsection with: (1) the source location as
supplied; (2) original labels in their original language; (3) visible
geometry/relationships with their visual basis; (4) explanations
explicitly supported by the caption or text; (5) relevant existing
concepts (wiki-link only names from the supplied list; otherwise give a
candidate name without a link); (6) unreadable details and open questions.

Keep observations, the author's explanations, and your tentative
interpretations separate. Do not infer hidden geometry, material,
function, dimensions, or units. Do not measure dimensions from pixels.
Mark unverified Japanese→English translations as provisional. Do not
invent locations, definitions, links, or synonym relationships. Do not
reproduce long source passages. Return a draft for checking; do not mark
it checked.
```

**自动化边界**：首批手动选图。只有重复导出图片、填写定位成为实际负担时才加小脚本。不开发图片Embedding、OCR服务、图像数据库、多模态RAG、PageIndex。

## 5. 调查既有统制语彙时研究什么

每个对象回答下表；资料没说明的写「未確認」，不让LLM补成看似完整的建设故事。

| 项目 | 要查的内容 | 对本项目的意义 |
|---|---|---|
| 目的 | 检索、索引、编目、标注还是数据交换 | 决定结构描述保留哪些信息 |
| 范围 | 收录什么、排除什么 | 防止材料、加工、缺陷混入结构词汇 |
| 候选收集 | 来自文献、标准、专家还是实际记录 | 决定候选术语需要什么证据 |
| 採否规则 | 收录、合并、拆分、不收录的理由 | 处理同义词、同名异义 |
| 定义与首选名 | 名称、范围说明、多语言表达怎么定 | 统一描述用语与粒度 |
| 关系 | 上下位和关联怎么规定 | 避免随意连线 |
| 确认与维护 | 谁确认、怎样改版、旧名称怎么处理 | 使后续修改可追溯 |

至少覆盖老师指定的对象；新增参考只选少量用途不同的。先做2～3个代表性案例。`Vocabulary_Method_Comparison.md` 最后给出"借鉴什么、为什么、哪些不适用"，不只罗列介绍（例：首选名称与来源定位可借鉴；庞大层级和审查组织不必照搬）。

## 6. CAD结构词汇的分类与粒度

### 6.1 首版分类

| category值 | 例子 | 区分重点 |
|---|---|---|
| overall_shape | plate-like body、block-like body | 整体外形，不能代替局部结构 |
| geometric_primitive | plane、cylindrical surface、conical surface | 几何曲面本身，不自动表示孔或凸台 |
| structural_feature | hole、pocket、slot、boss、chamfer、fillet | 由结构与边界关系形成的工程概念 |
| attribute | through、blind、cross-section、diameter、depth | 结构属性，不作为独立特征计数 |
| spatial_relation | coaxial、parallel、intersecting | 具体模型中结构之间的关系 |
| mold_function | cavity、core、gate、cooling channel | 可能需要用途与设计资料，不能仅凭STL形状确认 |

每个概念先给一个主要 category，跨类别联系用关系表达。分类是起点，不要求每类都有词条；不适合时先说明再调整，不勉强归类。建模、加工操作记入来源术语表并标为"操作用语"，只有比较边界需要时才建概念。

### 6.2 必须明确的边界

- cylindrical surface 是几何表面；hole 是结构特征；drilling 是加工操作，三者不是同义词。
- pocket 与 mold cavity 可能外观相似，但后者可能带金型功能意义，不能仅凭凹形等价。
- cavity 可指空间，也可指形成该空间的部件／一侧；core 也须核对所指。记录来源语境，不合并层次。
- chamfer 与 fillet 保留区别，不统一成 "edge treatment"。
- through、blind 通常是 hole 的属性；建属性词条不表示CAD里多了一个特征。
- cooling channel 与普通 hole 的区别可能无法由几何决定；定义中说明所需额外信息。

本阶段只确定"词是什么意思、怎样使用"，不新增STL识别算法。

## 7. 关系与图谱

### 7.1 最小关系集合

| 正文标题 | 意思 | 规则 |
|---|---|---|
| Broader concept | 更一般的概念 | 只用于"是一种"；有依据才链接，避免循环 |
| Related concepts | 有关但非上下位 | 不表示同义；写明相关原因 |
| Distinguished concepts | 易混淆需区分 | 写明区分依据 |
| Supporting sources | 支持定义或用法的资料 | 指向来源笔记并定位章节 |

关系先写在正文标题下，不要求YAML属性；没有对应关系不填空表。上位关系只在子概念笔记记一次；关联和区分不强制双向，查看用反向链接。以后确需程序处理时，再把正文关系迁移到 `broader`、`related` 属性，避免长期维护两份。

### 7.2 两种关系不要混

"Through hole 是一种 Hole"是词汇概念间的上下位关系；"这个CAD里孔A与孔B同轴"是具体模型中的空间关系。本Vault只整理概念与定义：可建 Coaxial 概念，但不把某个CAD实例的"孔A—孔B同轴"作为词汇链接。

### 7.3 Obsidian能力

原生图谱把笔记显示为节点、内部链接显示为连接，可用文件夹着色、局部图谱、反向链接。它不理解"上下位／同轴"等含义，关系类型靠正文标题保存。不要求 Dataview、Juggl 等插件，不为颜色布局折腾配置。参考：[Graph view](https://help.obsidian.md/plugins/graph)、[Properties](https://help.obsidian.md/properties)、[Internal links](https://help.obsidian.md/links)。

## 8. 最小模板

概念笔记只有三个属性：`aliases`、`category`、`status`。英文首选名即笔记标题，其余写正文。

### 8.1 概念笔记

| 信息 | 位置 | 要求 |
|---|---|---|
| 英文首选名 | 标题 | 当前首选名；有争议时说明 |
| 别名 | aliases | 只收已确认等价的表达，可空 |
| 分类 | category | 按第6节选主要类别 |
| 核对状态 | status | draft 或 checked |
| 定义与适用边界 | 正文 | 短定义，注明易混含义与适用范围；本项目提出的标"Project proposal"，依据资料的说明参考依据 |
| 来源 | 正文链接与章节 | 定位实际用法，不虚构 |
| 相关概念、待确认问题 | 正文 | 有内容才写 |

日语对应、记述例是可选内容。未核对译名写进 Open questions，不作为别名。

**status 含义**：`draft`＝定义或适用范围待核对；`checked`＝已根据所列资料核对当前定义的核心内容，不表示行业认证或老师批准。升级时在 Supporting sources 写一句实际核对说明和日期。AI和脚本不凭文字完整度自动升级。（状态只放在概念上；来源术语表的 checked／needs checking 仅表示该条用法是否已核对，不另设状态体系。）

```markdown
---
aliases: []
category: structural_feature
status: draft
---

# Hole

## Definition and scope
[Project proposal / not yet checked]
Short definition, intended domain and meaning.

## Broader concept
(only if there is one, with a link and a reason)

## Related or distinguished concepts
Links plus the relationship or difference.

## Supporting sources
Not yet investigated. After reading: link the source note, section/figure,
what was checked, and the date.

## Open questions
- Check the proposed definition against actual sources.
- Confirm a Japanese equivalent when needed.
```

模板占位内容不算完成词条；没有内容的章节可删。

### 8.2 资料笔记

只用正文，不加属性。图示小节（4.5）作为其中一节，不另建模板。

```markdown
# Official document title

## Source and reading scope
- Author / organization:
- URL:
- Version / publication year:
- Source language:
- Sections actually read / date:
- Usage conditions / license, and what is saved in this vault: not yet checked

## Collected terminology
| Original label | Section / figure | Usage in context | Candidate concept | Open question |
|---|---|---|---|---|

## Figure evidence
Add a figure subsection only when it contributes useful information.
```

阅读受限或仅取得摘要时，在 "Source and reading scope" 说明。

### 8.3 统制语彙调查笔记

```markdown
# Controlled vocabulary under study

## Purpose and scope
Not yet investigated.

## Development and maintenance
| Item | Confirmed method | Source and location | Open question |
|---|---|---|---|
| Candidate collection | Not yet investigated | — | — |
| Inclusion / merging / splitting | Not yet investigated | — | — |
| Preferred labels / definitions | Not yet investigated | — | — |
| Relations / classification | Not yet investigated | — | — |
| Checking / updating | Not yet investigated | — | — |

## Application to mold CAD
- What to adopt and why:
- What not to adopt directly and why:
- Limits of this investigation:
```

调查引用的来源同样建资料笔记。

## 9. 示例：怎样把词串成有意义的图谱

以下是设计示例，名称、对应、定义均须从资料核对后采用。

| 概念 | category | 关系 | 理由 |
|---|---|---|---|
| Hole | structural_feature | Distinguished → Cylindrical surface | 结构特征不能仅由曲面类型确定 |
| Through hole | structural_feature | Broader → Hole | "贯通孔是一种孔" |
| Through | attribute | Related → Hole | 表示终端属性，不是另一种孔 |
| Cylindrical surface | geometric_primitive | Related → Hole | 可作孔的表面，也出现在其他结构 |
| Cooling channel | mold_function | Related → Hole | 功能需额外依据，不只是外观分类 |

若收录 Through hole，须解释它与"Hole＋Through属性"的关系；首版可以只收 Hole 和 Through，不穷举属性组合。

```markdown
## Broader concept
[[Hole]]: The proposed concept is a type of hole.

## Supporting sources
[[Creo_Hole_Feature]]: Record the actual section and usage checked.
```

链接须对应已建立且实际支持该概念的笔记。来源笔记记"哪里怎样用这个词"，概念笔记说明"据此怎样定义"；链接本身不代替推理。

## 10. 检查方法：先目视

首批约10个概念用Obsidian原生功能检查：

1. 打开每篇概念笔记，确认定义、来源、未确认事项清楚。
2. 点击来源与概念链接，确认能找到对应笔记。
3. 用局部图谱和反向链接查看关系，检查同名词、错误合并、明显的上下位循环。
4. 试做的图示小节：核对标注、引出线对应、图注解释；推测与依据已区分。
5. 引用与自述已区分；来源笔记写了保存方式。

完成后在 `README.md` 记录检查日期与发现的问题。不要求检查程序、测试框架或 uv。只有词条增长后反复出现断链、重名等问题时，才考虑一个独立脚本检查文件名、内部链接和 category 值；脚本不得自动建词条、改定义、升级状态，也不判断定义冲突、专业正确性或版权合法性。是否增加取决于实际维护负担，不是验收条件。

## 11. 实施批次与交付物

### 11.1 小批次流程（人和Agent共用）

1. 读取本规范与老师提供的参考清单；无法确认的记入 `README.md`。
2. 创建独立Vault、目录、三个模板、README。`80_Assets` 可为空；图示小节先写在来源笔记。
3. 记录4.2入口的实际访问与阅读范围。不能访问的保留状态；不绕过会员或权限；不把目录／摘要当全文。
4. 调查2～3个既有统制语彙的目的与建设方法，写出比较。
5. 从2～3份可访问的英日资料，按当前样本需要试做约10个英文概念，每份资料记录使用条件与保存方式。证据不足就保留 draft，不生成虚假依据、页码或翻译对应；不为凑10个降低依据要求。
6. 若有适用图示，按4.5试做最多3～5个图示小节。只链接确实存在且相关的概念；新候选只记名称与问题，不自动建大量词条。区分图中标注、可见观察、作者解释、不确定项。
7. 在Obsidian中按第10节检查；默认不写检查程序、不装社区插件、不开发OCR／多模态RAG。
8. 形成方法比较与简短设计说明；如需金型领域词汇，再选一种领域扩充。
9. 交付实际完成范围、检查记录、未确认事项；日语对应作为后续补充。

原则：不自动升级 status；不以下载量、节点数、图谱密度、图片数量作质量指标；常规目录、模板、有依据的草案可直接完成，不等所有资料齐全；复制条件不明确时，改为保留链接和事实记录，继续其余工作。

### 11.2 交付清单

| 交付物 | 必须看得出 |
|---|---|
| Obsidian Vault | 资料、调查、概念笔记及内部链接 |
| 调查方法比较 | 各对象的目的、建设步骤、可借鉴部分及依据 |
| 来源术语用法表 | 原语言表记、英文语境解释、章节／图号、候选概念 |
| 图示证据小节（有适用图时，非必须） | 可见内容、作者解释、不确定项、概念链接 |
| 设计说明 | 范围、首选名称、粒度、分类、关系、确认与更新规则 |
| 未确认事项 | 词条各自记录；README记录共通问题 |
| 检查记录 | 范围、日期、未解决问题 |

不要求交付庞大的原始资料库、完整本体、RAG服务或所有语言的完整词典。

## 12. 设计说明怎样回答老师

`Design_Policy.md` 用自己的话回答，每项一至两段：

1. **目的**：这套词汇统一金型CAD结构描述的哪些内容？
2. **收录依据**：为什么选这些概念？资料中在哪里使用？
3. **名称与粒度**：为什么采用该英文首选名？哪些是属性、哪些是独立结构？日语对应如何后续核对并纳入同一概念？
4. **关系**：为什么设这些上下位、关联、区分关系？
5. **可判断范围**：哪些概念可由形状描述，哪些还需功能或设计资料？图中观察与作者解释怎样区分？
6. **维护**：遇到新词、定义冲突、改名怎么处理？还有哪些未确定？

不能只说"建立了知识图谱"，要能通过来源与词条解释"为什么这样设计"。

## 13. 验收要求

### 工程完成

- Vault可被Obsidian打开；目录和模板完整；概念、资料、调查放在对应目录。
- 概念的三个属性显示正常，内部链接能找到。
- 至少一个概念能从定义追到来源及章节；至少一组易混淆概念说明了区别。
- README 写明使用方法、实际完成范围、当前待确认项。
- 检查记录写明实际发现的问题；链接正常不等于专业定义正确。

### 调查完成

- 已调查对象的目的与建设步骤有定位依据；未知项标记明确。
- 英文首选名和已确认的语言对应有依据；未确认翻译不冒充同义词，不要求日语版同步完成。
- checked 词条注明实际核对的资料、范围、日期。
- 如使用图示：能追到资料及页码／图号；未读清的标注、未证实的结构关系已说明；AI整理的内容已按依据核对。
- 金型功能词与形状词、结构与操作没有混淆。
- 原文引用与自述已区分；每份资料有使用条件与保存方式记录。
- 设计说明能解释选择理由、局限和下一步，而不是只列词条数量。

"工程完成"不自动意味着"专业调查完成"，报告须分别说明。

---

判断标准：一个词能说明含义、适用范围、与近似概念的区别，并能追溯为什么采用它。Obsidian负责把这些笔记和依据连接起来。
