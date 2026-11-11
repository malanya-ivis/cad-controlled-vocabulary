# CAD統制語彙プロジェクト：現状・品質・AI確認項目

- **作成日:** 2026-10-06
- **更新日:** 2026-10-07。Excel資料に基づく四項目と、CAD形状・仕様のウェブ資料補足を反映。
- **対象:** `mold-cad-vocabulary/` と、この作業で参照した CAD サンプル・作成スクリプト
- **報告の目的:** 別の AI agent が、完了した内容、根拠、未完了事項をファイルから確認できるようにする
- **確認状態:** 本報告は確認項目を定めたもの。独立したAI agentによる監査結果はまだ含まない
- **全体判定:** 調査記録、語彙草案、知識構造、および選定CADサンプルへの試適用を作成済み。概念定義・関係・観察判断の確認は継続中。正式な統制語彙、実CAD検索、RAGは未完成。

## 1. プロジェクトの目的と現在の範囲

一つの金型CAD部品に含まれる形状特徴、形状上の性質、内部構造を、CADソフトに依存しない言葉で記録するための草案を作っています。アセンブリ階層や、部品がどの組立に属するかは中心課題ではありません。特定のCAD製品や金型の種類に限定していません。射出成形の資料が多い点は、現時点の調査上の偏りです。

この範囲は、上司の説明を記録した [`Scope_Revision_2026-10-06.md`](mold-cad-vocabulary/00_Guide/Scope_Revision_2026-10-06.md) と [`Design_Policy.md`](mold-cad-vocabulary/00_Guide/Design_Policy.md) にあります。

## 2. 完了した内容

| 項目 | 現在の内容 | 主な確認先 |
|---|---|---|
| 調査記録と既存語彙の比較 | 79件の資料ノート。CAD機能、金型用語、語彙作成方法、構造例、CAD形状表現・仕様を記録し、目的・確認できた整備手順・本課題への借用候補を対照表にした | `20_Sources/`、[`Source_Coverage_and_Gaps.md`](mold-cad-vocabulary/50_Reference_Registers/Source_Coverage_and_Gaps.md)、[`Controlled_Vocabulary_Governance.md`](mold-cad-vocabulary/40_Comparative_Studies/Controlled_Vocabulary_Governance.md)、[`Candidate_Sources_JA.xlsx`](mold-cad-vocabulary/00_Guide/Candidate_Sources_JA.xlsx) |
| 概念ノート | 37ノート。うち15概念を一部品内の形状・性質・内部構造の試作語彙として整理し、残る22は背景情報として保持 | `30_Concepts/`、[`Concept_Overview.md`](mold-cad-vocabulary/00_Guide/Concept_Overview.md) |
| 記述ルールと知識構造 | 特徴の種類と、部品上の特徴ID・属性・関係・根拠を分けるルールを整理 | [`Knowledge_Structure.md`](mold-cad-vocabulary/00_Guide/Knowledge_Structure.md)、[`Feature_Description_Rules.md`](mold-cad-vocabulary/00_Guide/Feature_Description_Rules.md)、`35_Knowledge_Structure/` |
| 簡単なSTLへの適用 | 21ファイルを観察。従来4例にrib・boss・fillet_bossの3例を追加し、計7例を詳細に記述。fillet_bossの丸い環状凸部はFillet候補のみ | [`Simple_CAD_Dataset_Study.md`](mold-cad-vocabulary/45_Part_Examples/Simple_CAD_Dataset_Study.md)、`Simple_CAD_Feature_Records.json`、[`Targeted_CAD_Gap_Examples.md`](mold-cad-vocabulary/45_Part_Examples/Targeted_CAD_Gap_Examples.md)、`Supplemental_Feature_Records.json` |
| 複雑なSTLへの適用 | 93ファイルのプレビューを作成。4部品を断面で調べ、形状と関係を記述 | [`Final_Selected_Dataset_Study.md`](mold-cad-vocabulary/45_Part_Examples/Final_Selected_Dataset_Study.md)、`Final_Selected_Feature_Records.json` |
| 形状の比較 | 従来の3組に提供モデルのリブ／ボスを追加。開閉空洞を明示した教材2件で比較。教材は提供モデルと別に数える | [`Shape_Comparison_Examples.md`](mold-cad-vocabulary/35_Knowledge_Structure/Shape_Comparison_Examples.md)、[`CAD_Enclosed_Open_Void_Teaching.md`](mold-cad-vocabulary/45_Part_Examples/CAD_Enclosed_Open_Void_Teaching.md) |
| Obsidian上の表示 | 概念、記述ルール、サンプルをMarkdownリンクとCanvasで接続 | [`Knowledge_Structure.canvas`](mold-cad-vocabulary/00_Guide/Knowledge_Structure.canvas) |
| 課題3への準備 | 特徴ID等の記録に加え、19問の期待値と記録絞り込みを作成。19/19の記録上の動作を確認。CAD認識・DB・RAG評価ではない | `45_Part_Examples/*Feature_Records.json`、[`RAG_Search_Verification_Cases.md`](mold-cad-vocabulary/35_Knowledge_Structure/RAG_Search_Verification_Cases.md)、`Search_Verification_Cases.json`、`Search_Verification_Results.json` |
| 分野と根拠の確認 | ExcelにあるYamaha7項目・AutoForm2項目を追加読取し、9項目の分野比較と15概念の根拠表を作成 | [`Cross_Mold_Domain_Transfer.md`](mold-cad-vocabulary/40_Comparative_Studies/Cross_Mold_Domain_Transfer.md)、[`Claim_Evidence_Matrix.md`](mold-cad-vocabulary/40_Comparative_Studies/Claim_Evidence_Matrix.md) |

概念IDはMC-001〜MC-015です。対象はHole、Counterbore、Countersink、Pocket、Slot、Rib、Boss、Fillet、Chamfer、Draft Angle、Undercut、Wall Thickness、Internal Void、Cooling Channel、Gas Ventです。現時点では候補リストで、承認済みの標準語彙ではありません。

## 3. 複雑なCADサンプルから得た具体例

| STL ID | 観察した内容 | 記録上の意味 |
|---|---|---|
| 1400 | 直交する向きの貫通穴候補が4つ。選択断面では交差を認めない | 全体の交差・接続状態はunknown。限定した観察を不在の証明にしない |
| 4423 | +Z側に開いた空間、底、側壁がある | 同じ領域を内部空間とポケットの両方で説明しつつ、同じ特徴IDで扱う。底厚は入力座標上で約0.005 |
| 8972 | 段付き貫通長穴と、2列×3段の矩形凹部 | 6個すべてを同じ止まり穴と見なさない。右中の凹部には背面へ抜ける部分がある |
| 7145 | 外側の丸い移行と、外観だけでは見えない内部空間・仕切り | 外観表示と断面観察を分ける。断面だけで内部区画の全接続を断定しない |

根拠画像と測定情報は `80_Assets/final_selected/` にあります。生成方法は `tools/inspect_final_selected.py` と `tools/inspect_final_selected_details.py` に記録されています。元STLとSTEPは別のデータフォルダにあり、調査では読み取り専用です。

## 4. 内容の品質評価

評価は、現在の草案をレビューするためのものです。外部の専門家による承認や規格適合の判定ではありません。

| 品質面 | 評価 | 理由 |
|---|---|---|
| 課題範囲 | 範囲方針は文書化済み。上司の最終承認は未確認 | 一部品内の形状・性質・内部構造を対象とする方針を記録 |
| 知識構造 | ノート間のリンクと項目を記録済み。意味上の妥当性は未レビュー | 15概念を分類、属性、関係、部品例に接続 |
| 形状観察の追跡 | 元ファイル、ハッシュ、断面図、測定欄を記録。形状判断の正しさは独立検証していない | 提供モデル11件を詳細記述。教材2件は別枠。全93件に閉境界候補の確認を追加したが、完全な空洞検証ではない |
| 用語定義と日本語名 | 暫定 | 概念定義と日本語名は候補。資料の適用範囲を確認し、同義語や境界を人がレビューする必要がある |
| 幾何学的な確認範囲 | 限定的 | STL三角形メッシュと選択断面による観察。1400の全体交差判定はunknownであり、正確なCAD曲面・作成履歴・自動認識は確認していない |
| 用途や設計意図 | 未確認として適切に記録 | 金型用途、冷却、反り対策、加工方法などを形だけから断定していない |
| 課題3への準備 | 小規模なデータ設計と19問の記録確認例 | unknown、単位・用途・方向不足、教材除外、特徴の計数を確認。CAD検索DB・RAGを実装・評価したものではない |
| 資料の確かさ | 混在 | 一部資料は本文を確認済み。一部のISO/JISはカタログ・抄録だけ。ノートごとの閲覧範囲の確認が必要 |

## 4.1 今回の指摘を受けて明記した点

- 既存の語彙・分類の目的、確認できた整備方法、本課題への借用候補を [`Controlled_Vocabulary_Governance.md`](mold-cad-vocabulary/40_Comparative_Studies/Controlled_Vocabulary_Governance.md) に追加した。規格本文を読んでいない項目は手順を未確認とした。
- 15概念に `concept_kind` と最低限必要な使用根拠を記録した。特にCooling ChannelとGas Ventは形状だけでなく、機能を示す別の根拠を必要とする。
- 1400の6組の交差結果を `false` から `unknown` に変更した。選択断面の観察と全体の三次元判定を分けた。
- 4423ではPocketを外面の凹形状、Internal Voidを材料のない領域として区別し、一つの特徴に二つの分類観点を記録した。閉じた空洞と開口部のある領域を分けるかは未決定。
- 概念間の関係と部品内の特徴間の関係、`intersects`・`touches`・`connects_to`、部品内特徴IDと `(part_id, feature_id)` の識別範囲を記述した。
- 4423と8972の肉厚を、測定位置・方向・方法が分かる局所値として記録した。全体の最小肉厚とはしていない。
- アセット台帳に、ユーザー提供STLから作った画像と、未確認の再配布条件を記録した。

## 5. AI agent向けの確認手順

### 確認上の指示

- まず本報告の主張を、記載したファイルと元データで照合してください。
- 確認結果は `確認済み / 要修正 / 判断できない` に分け、根拠のファイル名と箇所を添えてください。
- 草案を承認済み語彙へ変更したり、ファイルを修正したりしないでください。目的・単位・用途を推定で補わないでください。
- 解析スクリプトを再実行する場合、元のCADデータは読み取り専用として扱ってください。実行環境と必要ライブラリも先に確認してください。

### 確認項目

1. **範囲:** `Scope_Revision_2026-10-06.md` と `Design_Policy.md` が、一部品の形状語彙を対象とし、ソフトウェア依存・組立中心を避けていること。
2. **ノート数と役割:** `30_Concepts/` の37ノートのうち、15が `scope_role: core`、22が `context_only` であるというREADME記載を照合する。15コア概念のIDがMC-001〜MC-015と一意に対応し、各ノートの`concept_kind`と最低限の適用根拠が本文の定義と一致すること。
3. **ソースの扱い:** ソース一覧にある規格や資料がすべて全文読了扱いになっていないこと。特にISO 25964、ISO AP 224、JIS Z 8114の読了範囲を `Source_Coverage_and_Gaps.md` と各ソースノートで確認する。
4. **簡単なSTL:** 21件の外形記録、従来4つの詳細例と追加3例が、元データのID・ハッシュ・画像と対応すること。追加例はrib、boss、fillet_bossで、Fillet候補を確定割当へ変えていないこと。
5. **複雑なSTL:** マニフェスト、`inventory.json`、93枚の個別プレビューと4枚の断面例の対応を確認する。全93件に特徴注釈があるとは扱わない。
6. **1400:** 4つの貫通穴の位置・向き、および6組の`unknown`判定を確認する。JSONが断面で「観察されなかった」ことと全体の非交差を区別し、穴の実体と入口形状も二重に数えないこと。
7. **4423:** 開口方向+Z、深さ、肉厚の測定面・位置・方向が断面と一致するか確認する。値が局所断面の値であり、最小肉厚ではないこと、`watertight`と空間の開口状態を混同していないこと。PocketとInternal Voidの二つの分類観点が一つの物理領域を数えていること。
8. **8972:** 長穴が段付きでも貫通していること、6つの矩形凹部のうち右中のみ部分開口という記述を断面と `8972_ray_observations.json` で照合する。線状レイ検査の範囲を全体形状の完全証明と誤解しないこと。
9. **7145:** 断面で丸い移行・内部空間・仕切りを確認し、「Fillet」は形状候補であってCADコマンド履歴の特定ではないことを確認する。
10. **JSONとリンク:** `Final_Selected_Feature_Records.json` が有効なJSONで、概念IDが存在すること。同じ部品内での特徴IDの一意性を確認し、部品をまたぐ照合キーが`(part_id, feature_id)`であること、参照切れ、Canvas上の不在ノート参照がないこと。
11. **課題3の状態:** 十九問の手動記録絞り込み例はあるが、実データベース、CAD認識・検索、RAGの実装や性能評価はまだ存在しないという説明が一貫していること。
12. **報告との整合:** README、知識構造、出典範囲、アセット台帳の件数・状態が、この報告と矛盾しないこと。目的・整備工程の比較が既読範囲を超えていないこと、画像の出所と再配布条件が区別されていることを確かめる。矛盾があれば場所と修正案を示すこと。

### 合格の目安

- 範囲と状態に関する主張が一次ファイルで追跡できる。
- 調査済み、草案、未確認、未実装が区別されている。
- STL上の記述が根拠画像・座標と一致し、用途や単位を勝手に確定していない。
- 参照切れやデータ形式のエラーがあれば具体的に報告される。

## 6. 明示しておく未完了事項

- 既存統制語彙の目的と確認できた整備の進め方は[`Controlled_Vocabulary_Governance.md`](mold-cad-vocabulary/40_Comparative_Studies/Controlled_Vocabulary_Governance.md)に追加済み。本文未読の資料は工程未確認のまま。概念定義・日本語の優先語・同義語・概念境界は人による確認が必要。
- 規格の正式本文や設計図面など、許可された一次資料に基づく用語・単位の確認。
- CADサンプルが実際の金型部品かどうか、STLとSTEPの単位や倍率が対応するかの確認。
- リブ／ボスの一般定義の見直し、実部品の確認済み閉鎖空洞、曲線状長穴などの追加例。リブ／ボスの提供モデル比較と空洞の教材二件は作成済み。
- 物理単位・設計目的・冷却や排気の機能を示す図面または設計者の根拠。選定断面での非観察を全体の不在としないこと。
- 検索データベースの設計・実装・検索品質評価、およびRAGの実装・評価。
- すべての93モデルへの局所形状ラベル付け。現状は一覧プレビューと閉境界候補の確認があり、詳細な意味注釈は四件だけ。

## 7. 主な確認対象ファイル

- プロジェクト案内: [`README.md`](mold-cad-vocabulary/00_Guide/README.md)
- 課題範囲: [`Scope_Revision_2026-10-06.md`](mold-cad-vocabulary/00_Guide/Scope_Revision_2026-10-06.md)、[`Design_Policy.md`](mold-cad-vocabulary/00_Guide/Design_Policy.md)
- 知識構造: [`Knowledge_Structure.md`](mold-cad-vocabulary/00_Guide/Knowledge_Structure.md)、[`Feature_Relations.md`](mold-cad-vocabulary/35_Knowledge_Structure/Feature_Relations.md)
- 実データ適用: [`Simple_CAD_Dataset_Study.md`](mold-cad-vocabulary/45_Part_Examples/Simple_CAD_Dataset_Study.md)、[`Final_Selected_Dataset_Study.md`](mold-cad-vocabulary/45_Part_Examples/Final_Selected_Dataset_Study.md)
- 構造化記録: [`Simple_CAD_Feature_Records.json`](mold-cad-vocabulary/45_Part_Examples/Simple_CAD_Feature_Records.json)、[`Final_Selected_Feature_Records.json`](mold-cad-vocabulary/45_Part_Examples/Final_Selected_Feature_Records.json)
- 比較例: [`Shape_Comparison_Examples.md`](mold-cad-vocabulary/35_Knowledge_Structure/Shape_Comparison_Examples.md)
- 出典範囲と不足: [`Source_Coverage_and_Gaps.md`](mold-cad-vocabulary/50_Reference_Registers/Source_Coverage_and_Gaps.md)
- 画像一覧: [`Asset_Register.md`](mold-cad-vocabulary/80_Assets/Asset_Register.md)
- 再生成スクリプト: `tools/inspect_simple_cad_dataset.py`、`tools/inspect_final_selected.py`、`tools/inspect_final_selected_details.py`

## 8. 2026-10-07追加分の確認

詳しい成果と資料一覧の行番号は[`Batch_F_2026-10-07.md`](mold-cad-vocabulary/60_Research_Records/Batch_F_2026-10-07.md)にあります。

- [`Cross_Mold_Domain_Transfer.md`](mold-cad-vocabulary/40_Comparative_Studies/Cross_Mold_Domain_Transfer.md)：資料を比べた九項目。実金型の三分野比較の完了とは扱わない。
- [`Claim_Evidence_Matrix.md`](mold-cad-vocabulary/40_Comparative_Studies/Claim_Evidence_Matrix.md)：十五概念の根拠と不足。Boss・Internal Voidの一般定義の不足が残っていることを確認する。
- [`Targeted_CAD_Gap_Examples.md`](mold-cad-vocabulary/45_Part_Examples/Targeted_CAD_Gap_Examples.md)：追加の提供三件と教材二件。提供モデルの総数十一件、教材二件を混ぜて数えていないことを確認する。
- `80_Assets/vocabulary_supplement/enclosed_void_candidate_screen.json`：九十三件の候補確認。7975・8448・9115は外接箱の包含候補で、閉鎖空洞の確定結果ではない。
- [`RAG_Search_Verification_Cases.md`](mold-cad-vocabulary/35_Knowledge_Structure/RAG_Search_Verification_Cases.md)：十九問とJSON結果。記録の動作を確認しただけで、RAG性能・形状ラベルの正しさを検証したと解釈しない。

再確認は、標準Pythonで`python3 tools/evaluate_vocab_search_cases.py`を実行できます。図・教材・候補確認の再作成は、既存環境の`/home/malanya/projects/cad-structure-search/.venv/bin/python tools/inspect_vocabulary_supplement.py`を使います。出力はvault内へ保存し、元の提供CADは書き換えません。

ファイル整合の結果は[`Batch_F_Verification.json`](mold-cad-vocabulary/60_Research_Records/Batch_F_Verification.json)です。Wiki・Canvasの参照、件数、元ファイルハッシュ、検索期待値、教材体積を確認しました。独立した意味・定義の監査結果とは扱いません。

### CAD形状・仕様のウェブ資料補足

今回追加した調査記録は[`Batch_G_2026-10-07.md`](mold-cad-vocabulary/60_Research_Records/Batch_G_2026-10-07.md)です。5件の資料ノートと、課題3向けの[`CAD_Geometry_Representation_and_Evidence.md`](mold-cad-vocabulary/35_Knowledge_Structure/CAD_Geometry_Representation_and_Evidence.md)を追加しました。

- ISO 10303-42、ISO 22432、ISO 1101、ISO 21920-2は公式カタログ・概要だけを確認し、規格本文は読んでいません。
- NIST記事を根拠に、STLメッシュと精密なCAD幾何の違いを記録しました。STLから設計意図・CAD履歴・厳密な形状を推定できるとはしていません。
- 課題3の項目案は提案です。STEPや3D注記を使った検索、DB、RAGの実装はまだありません。
- roughness / Ra / Rz と flatness は候補のままで、確定概念にしていません。
