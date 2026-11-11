# Controlled Vocabulary Governance Comparison

**Status:** Updated 2026-10-06. The supervisor identified ANSI/NISO Z39.19 and ISO 25964 as construction references, and MeSH and ICD-10 as structural examples. Reading limits remain explicit.

## What the references contribute

| Reference | Contribution to the method | Limit |
|---|---|---|
| ANSI/NISO Z39.19 | Selected clauses support recording warrants, choosing terms, handling compound terms, relationships, and maintenance. | Selected sections only; the project does not claim compliance. |
| ISO 25964-1 | Main reference for thesaurus construction and maintenance; current catalog metadata and revision status are recorded in [[ISO_25964_Interoperability_Catalog_Study]]. | Full standard not read. Its information-retrieval setting must be considered when adapting advice. |
| ISO 25964-2 | Reference for mapping between vocabularies and preserving mapping decisions. | Catalog/abstract only; no mapping procedure has been adopted from the full text. |
| MeSH | Example of preferred terms, entry terms, concept organization, hierarchical browsing, and revision history. | Biomedical indexing hierarchy does not define engineering shapes. |
| ICD-10 | Example of practical classification structure and boundary notes. | A statistical medical classification; use only to compare organizing choices. |
| STEP AP 224 | Technical feature model focused on machining/process planning for single-piece parts. | Not a general-purpose shape-feature vocabulary or mold taxonomy. |
| JIS Z 8114 | Japanese drawing terms and definitions for product technical documentation. | The standard text has not been read; do not infer 3D feature coverage from its title. |

## Lightweight process

1. **Capture evidence:** record the source's wording, location, context, version, access conditions, and date in `20_Sources/`.
2. **Queue a candidate:** note whether it appears to be a shape feature, shape property, internal structure, command, function, or relation.
3. **Compare scope:** distinguish the resulting geometry from CAD operations, machining-feature interpretations, and design intent.
4. **Draft the concept:** define one meaning, a preferred label, boundaries, related concepts, and source support.
5. **Describe occurrences separately:** use [[Feature_Description_Rules]] for values, instance relations, internal visibility, and evidence for purpose.
6. **Maintain decisions:** record additions, merges, splits, and preferred-label changes in [[Decision_Log]]. Keep unconfirmed equivalents as candidates.



## 目的・整備の進め方を比べる

ここでは「既存の統制語彙・分類が何のために作られ、確認できる範囲でどう整備されるか」を、本課題への参考として整理します。手順の詳細が未読の資料は、未確認と記録します。

| 参照先 | 作られた目的 | 確認できた整備の進め方 | 本課題に使える点 | 確認範囲 |
|---|---|---|---|---|
| ANSI/NISO Z39.19 | 情報検索で語をそろえ、検索の一貫性を高める統制語彙の作成・管理を助ける指針 | 読んだ条項では、用語の選択、根拠、関係、維持管理を扱う。全体手順の網羅確認はしていない | 採用理由、優先語、関係、変更記録を残す | 選択条項を読了。規格全体の手順確認・適合評価ではない |
| ISO 25964-1 | 情報検索用シソーラスの開発と維持に関する推奨事項 | 公式概要で目的を確認。本文未読のため具体的な整備順序は未確認 | 用語・概念の管理と継続更新を比較する | 公式カタログ／概要のみ |
| ISO 25964-2 | 他の語彙との相互運用 | 公式概要では語彙間の相互運用を扱う。詳細手順は未確認 | 外部語彙との対応と確信度を別に記録する | 公式カタログ／概要のみ |
| MeSH | 生医学・健康情報の索引、目録、検索で、表記が異なる同じ主題を探せるようにする | 既存見出しで足りるかを確認して追加の必要を検討し、文献での用語使用を見て名称を選ぶ。分野専門家が継続更新し、年ごとの変更を公開 | 既存語で表せるかを先に確認し、新語の理由・優先名・別表記・変更履歴を残す | NLMの序文・導入を確認。内部審査の細部は未確認 |
| ICD-10 | 国や地域、時期を越えて死亡・疾病の統計を体系的に記録・比較する | ICD-10改訂の記録では、代替構造の検討、ICD-9の評価、各国・組織への相談、改訂会議を経ている | 分類の目的を明記し、境界・複数の分類観点を利用例と一緒に確認する | WHO Volume 2の基本構造と改訂史の該当箇所。医療分類の仕組みを移植しない |
| STEP AP 224 | 単一部品の製造計画用情報を表現・交換し、加工フィーチャ形状などを記述する | 規格のカタログ概要では策定・利用手順は分からない | 設計形状と加工・製造向け形状表現を混同しない | ISO公式概要のみ。規格本文未読 |
| JIS Z 8114 | 製品技術文書に関係する製図用語と定義 | カタログ情報だけでは用語の整備手順は分からない | 日本語表記と製図上の意味を照合する候補にする | JSA公式カタログのみ。規格本文未読 |

### 本課題で試す整備手順

上の資料から本課題に使う作業案は次の通りです。これはプロジェクトの提案で、各規格への適合を意味しません。

1. 出典、原表記、使われた範囲、確認日を記録する。
2. 既存概念に同じ意味がないか確かめ、新候補の追加理由を残す。
3. 形状、幾何属性、空間、機能を分け、定義と使用に必要な根拠を記す。
4. 優先表記、確認済みの別表記、上位・関連関係を区別する。
5. CAD例で使い、誤分類や不足を見つけたら根拠とともに改訂履歴へ記録する。

## Automation and limits

String similarity, graph proximity, software command labels, and geometry alone do not establish concept identity or design purpose. A catalog abstract supports discovery and scope, not detailed definitions. Human review remains necessary; no automated step promotes a concept to `checked`.
