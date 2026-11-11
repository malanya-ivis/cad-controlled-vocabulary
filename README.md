# CAD Controlled Vocabulary

用于描述**单个金型 CAD 部件内部的形状特征、形状属性和内部结构**的统制语彙（controlled vocabulary）研究资料库。目标是让术语、概念边界、几何观察和依据可以被人和 AI agent 追溯，并为后续结构化检索与 RAG 数据设计提供基础。

当前交付物是 Obsidian 知识库、概念草案、资料阅读记录、CAD 示例和人工标注 JSON。所有概念仍为 `draft`；CAD 自动识别、搜索数据库和 RAG 尚未实现。射出成形资料是现阶段的主要研究样本，项目范围覆盖一般金型 CAD，不依赖特定 CAD 软件。

## 快速开始

- **阅读：**从下方的“Agent 阅读顺序”进入。GitHub 可直接阅读 Markdown；Obsidian 可解析库内的 `[[wikilinks]]`、Canvas 和 Bases。
- **Obsidian：**将 `mold-cad-vocabulary/` 作为独立 vault 打开，无需社区插件。该目录是当前完整研究资料的主入口。
- **运行最小验证：**在仓库根目录执行以下命令，只需要 Python 3 标准库，无需原始 CAD 数据或第三方包。

```bash
python3 tools/evaluate_vocab_search_cases.py
```

脚本读取三份人工标注记录和十九个预设用例，重写 `mold-cad-vocabulary/45_Part_Examples/Search_Verification_Results.json`，逐项打印 `PASS` / `FAIL`；全部通过时退出码为 `0`，否则为 `1`。现有记录的预期结果为 `19/19 record-behavior cases passed`。通过表示记录筛选行为符合预设，不能据此认定几何判断或概念定义正确。

## Agent 阅读顺序

| 顺序 | 入口 | 需要确认的内容 |
|---|---|---|
| 1 | [范围修订](mold-cad-vocabulary/00_Guide/Scope_Revision_2026-10-06.md) → [设计方针](mold-cad-vocabulary/00_Guide/Design_Policy.md) | 单部件范围、概念分类、证据条件；2026-10-06 的范围修订取代早期计划中冲突的假设 |
| 2 | [项目现状与 AI 检查项](PROJECT_STATUS_AI_REVIEW.md) | 已完成内容、质量限制、待审查事项；这是检查说明，不是已完成的独立审计 |
| 3 | [知识结构](mold-cad-vocabulary/00_Guide/Knowledge_Structure.md) → [特征描述规则](mold-cad-vocabulary/00_Guide/Feature_Description_Rules.md) | 概念与实例、唯一标识、属性、关系和用途证据的区分 |
| 4 | [概念总览](mold-cad-vocabulary/00_Guide/Concept_Overview.md) → [概念目录](mold-cad-vocabulary/30_Concepts/) | 当前核心概念、草案定义、适用条件和开放问题 |
| 5 | [主张与证据矩阵](mold-cad-vocabulary/40_Comparative_Studies/Claim_Evidence_Matrix.md) → [资料覆盖与缺口](mold-cad-vocabulary/50_Reference_Registers/Source_Coverage_and_Gaps.md) | 每项主张的依据、资料实际阅读范围、尚缺的验证 |
| 6 | [检索验证说明](mold-cad-vocabulary/35_Knowledge_Structure/RAG_Search_Verification_Cases.md) → [用例 JSON](mold-cad-vocabulary/45_Part_Examples/Search_Verification_Cases.json) | 结构化记录的筛选规则、预期行为和能力边界 |

早期 [v4 计划](CAD_CONTROLLED_VOCABULARY_OBSIDIAN_PHASE2_SPEC_v4.md) 保留作为历史背景。处理范围冲突时，先依据范围修订和当前设计方针，再核对具体记录及[决策日志](mold-cad-vocabulary/60_Research_Records/Decision_Log.md)。概览中的数量若与文件不一致，应按实际文件核对，并说明差异。

## 目录与职责

```text
.
├── README.md                         # 仓库入口与 agent 工作导航
├── PROJECT_STATUS_AI_REVIEW.md        # 日文现状报告及 AI 审查清单
├── CAD_CONTROLLED_VOCABULARY_OBSIDIAN_PHASE2_SPEC_v4.md
├── docs/                             # 候选资料 Excel、研究说明演示文稿
├── mold-cad-vocabulary/               # 完整研究 vault，英文为主，含日文补充
│   ├── 00_Guide/                     # 范围、方针、概念索引、描述规则、Canvas
│   ├── 10_Vocabulary_Studies/        # 既有语彙及分类体系研究
│   ├── 20_Sources/                   # 逐项资料来源、阅读范围、术语使用记录
│   ├── 30_Concepts/                  # 核心概念草案及背景概念
│   ├── 35_Knowledge_Structure/       # 分组、概念边界、实例关系、形状证据
│   ├── 40_Comparative_Studies/       # 跨资料比较、语彙治理、证据矩阵
│   ├── 45_Part_Examples/             # 部件观察笔记、结构化记录、检索用例及结果
│   ├── 50_Reference_Registers/       # 资料覆盖、ISO/JIS 检索台账
│   ├── 60_Research_Records/          # 按批次记录的研究过程、决策日志
│   ├── 70_Candidate_Terms/           # 未解决的候选术语
│   ├── 80_Assets/                    # 预览、断面图、测量 JSON、合成教学 STL
│   └── 90_Templates/                # 概念、资料、语彙研究模板
├── mold-cad-vocabulary-jp/            # 较早的日文简版：32 个概念及案内
└── tools/                            # 记录筛选验证与几何观察资产生成脚本
```

日文简版未完整反映后续的范围修订、十五核心概念和新增研究，适合作为辅助阅读材料；修改当前定义时应先核对完整 vault。根目录和 `docs/` 的报告、Excel 是背景与资料入口，具体阅读状态以资料笔记为准。

## 当前数据与概念

以下为当前文件核对得到的快照；研究记录主要更新于 2026-10-07。

| 内容 | 当前规模与边界 |
|---|---|
| 来源笔记 | `20_Sources/` 共 79 份；包含已读部分正文及仅目录／摘要记录，不能视为全部读完 |
| 概念笔记 | `30_Concepts/` 共 37 份，15 个 `core`、22 个 `context_only`，均为 `draft` |
| 简单模型 | 21 个 STL 的观察资产；7 个提供模型有详细特征记录 |
| 复杂模型 | 93 个 STL 的预览；其中 4 个模型有详细特征记录 |
| 结构化部件记录 | 11 个提供模型 + 2 个明确标记的合成教学模型，共 13 个 |
| 筛选验证 | 19 个手写预期用例；默认排除合成教学模型 |

| 分类 | 核心概念 ID 与名称 |
|---|---|
| `shape_feature` | `MC-001` Hole、`MC-002` Counterbore、`MC-003` Countersink、`MC-004` Pocket、`MC-005` Slot、`MC-006` Rib、`MC-007` Boss、`MC-008` Fillet、`MC-009` Chamfer |
| `shape_property` | `MC-010` Draft Angle、`MC-011` Undercut、`MC-012` Wall Thickness |
| `internal_structure` | `MC-013` Internal Void、`MC-014` Cooling Channel、`MC-015` Gas Vent |

分类用于组织笔记，不代表所有成员具有相同的识别条件，也不意味着类别互斥。冷却流路和排气通道需要额外的功能证据；拔模角、倒扣需要参考方向；肉厚值需要测量位置、方向、方法和单位。

### 机器可读入口

所有下列文件均位于 [45_Part_Examples/](mold-cad-vocabulary/45_Part_Examples/)：

| 文件 | 内容 |
|---|---|
| [Simple_CAD_Feature_Records.json](mold-cad-vocabulary/45_Part_Examples/Simple_CAD_Feature_Records.json) | 最初 4 个简单模型的详细记录 |
| [Final_Selected_Feature_Records.json](mold-cad-vocabulary/45_Part_Examples/Final_Selected_Feature_Records.json) | 1400、4423、8972、7145 的详细记录 |
| [Supplemental_Feature_Records.json](mold-cad-vocabulary/45_Part_Examples/Supplemental_Feature_Records.json) | 另 3 个提供模型及 2 个合成教学模型 |
| [Search_Verification_Cases.json](mold-cad-vocabulary/45_Part_Examples/Search_Verification_Cases.json) | 问题、筛选条件、来源范围、预期结果 |
| [Search_Verification_Results.json](mold-cad-vocabulary/45_Part_Examples/Search_Verification_Results.json) | 实际结果、逐项比较及输入文件 SHA-256 |

概念笔记使用 YAML front matter，例如 `concept_id`、`status`、`scope_role`、`concept_kind`、`minimum_use_evidence`、`label_ja_status`、`concept_relations`。先读字段和正文，再解释概念。

三份特征记录保留了不同阶段的数据结构，尚未统一成正式 schema。编写消费者前应检查各文件的 `schema_version` 与实际字段；可参考[现有筛选器](tools/evaluate_vocab_search_cases.py)对 `concept_id` / `concept_assignments`、`properties` / `attributes`、`relations` / `relation_assessments` 的兼容处理。

## Agent 工作规则

1. **区分概念与实例。**概念用 `concept_id` 标识；部件上的特征用 `(part_id, feature_id)` 唯一定位。概念关系放在概念笔记，实例关系放在部件记录。
2. **保留证据层次。**分别记录来源原文的用法、项目提出的定义、几何观察、分析、设计意图和推断。软件命令、最终形状、加工特征与功能不自动等价。
3. **保留未知。**`unknown` 不能改写成 `false` 或“不存在”；没有匹配记录不证明实体没有该形状。局部断面未观察到交叉，也不能证明整体不相交。
4. **保持计数一致。**一个实例可以有多个有依据的概念赋值；不要仅因描述角度不同重复计数。孔口扩大形状与连续孔道应按现有规则关联。
5. **不补造单位或用途。**`input_units` 不自动转换为 mm；网格 `watertight` 不证明内部空腔封闭；文件名和外观不能证明冷却、排气、金型用途或建模历史。
6. **保持草案状态。**未经适当资料与审查，不将 `draft` 升级为批准状态，不把候选日文标签直接当作已确认同义词。保留 `context_only` 笔记作为研究背景。
7. **遵守既有资料限制。**只读目录／摘要就按该范围引用；[ISO 12165 访问限制记录](mold-cad-vocabulary/20_Sources/ISO_12165_Access_Restriction_Record.md)要求不向 AI 提交该标准内容。原始 CAD 文件按项目规则只读。资产来源与再利用状态见[资产台账](mold-cad-vocabulary/80_Assets/Asset_Register.md)。
8. **让修改可追溯。**新增或调整概念时同步索引、相关实例和决策记录；报告变更文件、验证命令、结果和仍未解决的问题。

### 按任务定位

| 任务 | 推荐流程 |
|---|---|
| 新增术语 | 检查已有概念 → 记录来源实际用法 → 加入[候选队列](mold-cad-vocabulary/70_Candidate_Terms/Candidate_Term_Queue.md) → 使用[概念模板](mold-cad-vocabulary/90_Templates/Concept.md)起草 → 更新概念总览及决策日志 |
| 补充来源 | 使用[来源模板](mold-cad-vocabulary/90_Templates/Source.md)，注明版本、实际阅读章节／日期、术语上下文、访问和保存条件；同步资料覆盖记录 |
| 描述部件 | 先读特征描述规则和[实例关系定义](mold-cad-vocabulary/35_Knowledge_Structure/Feature_Relations.md)，再参考既有 JSON；附部件标识、证据、单位状态及观察范围 |
| 修改筛选行为 | 核对用例语义，修改记录或筛选器，运行十九个用例，检查结果 JSON 的变化；新增数据时重新审查预期值 |
| 审查研究结论 | 按项目现状报告的检查项，对照原始记录；输出“已确认／需修改／无法判断”及文件位置，不将审查直接视为批准 |
| 设计后续检索／RAG | 先读[几何表示与证据](mold-cad-vocabulary/35_Knowledge_Structure/CAD_Geometry_Representation_and_Evidence.md)，保留实例身份、来源、未知状态、单位和模型来源类型 |

检索 Markdown 时可从稳定 ID 和字段开始：

```bash
rg -n 'concept_id: MC-001|scope_role: core' mold-cad-vocabulary/30_Concepts
rg -n 'unknown|minimum_use_evidence|label_ja_status' mold-cad-vocabulary/30_Concepts
```

## 几何观察脚本与复现边界

普通阅读和记录筛选验证不需要外部模型。重新生成几何资产则依赖仓库外的原始数据，脚本当前硬编码本机路径：

```text
/home/malanya/projects/cad-structure-search/data/
├── simple_CAD_dataset/
└── final_selected/
    ├── manifest.csv
    ├── stl/
    └── step/                         # 可选的对应 STEP 文件
```

这些原始提供模型未随本仓库提交；仓库内的两个教学 STL 是显式生成的合成模型。几何脚本曾使用相邻 `cad-structure-search` 项目的 Python 环境，本仓库没有锁定依赖版本，也没有提供统一安装配置。

| 脚本 | 用途 | 主要第三方依赖／输出 |
|---|---|---|
| [inspect_simple_cad_dataset.py](tools/inspect_simple_cad_dataset.py) | 简单模型总览、选定模型视图及断面 | NumPy、trimesh、Matplotlib；写入 `80_Assets/cad_examples/` |
| [inspect_final_selected.py](tools/inspect_final_selected.py) | 复杂模型预览和清单 | PyVista、Matplotlib 及可用的离屏渲染环境；写入 `80_Assets/final_selected/` |
| [inspect_final_selected_details.py](tools/inspect_final_selected_details.py) | 选定模型断面、局部射线观察 | NumPy、trimesh、Matplotlib；写入 `80_Assets/final_selected/` |
| [inspect_vocabulary_supplement.py](tools/inspect_vocabulary_supplement.py) | 补充模型、空腔候选筛查、教学几何 | NumPy、trimesh、Matplotlib；写入 `80_Assets/vocabulary_supplement/` |

重新运行前先确认源码中的输入路径、原始文件哈希、依赖及渲染环境，并检查输出覆盖范围；生成后人工核对图像与对应观察记录。几何资产生成不会自动完成概念赋值或建立已验证的识别算法。

## 后续工作入口

优先事项是审查十五个核心草案的定义和日文标签、补足资料正文依据、确认实例几何与关系、完善开放／封闭内部空间的概念边界，并增加其他金型领域样本。当前可从[证据矩阵](mold-cad-vocabulary/40_Comparative_Studies/Claim_Evidence_Matrix.md)、[候选队列](mold-cad-vocabulary/70_Candidate_Terms/Candidate_Term_Queue.md)及[决策日志](mold-cad-vocabulary/60_Research_Records/Decision_Log.md)中的未解决问题继续。
