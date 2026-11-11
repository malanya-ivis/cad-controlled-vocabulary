---
category: evidence_rules
status: draft
updated: 2026-10-07
---
# 定義と判断の根拠はどこまであるか

資料に言葉があること、その意味を一般化できること、あるCAD部品に使えることは、それぞれ確認が必要です。この表は、15個のコア概念について、今の根拠と足りない部分を示します。承認済みの定義を示す表ではありません。

技術用語の根拠は `docs/Candidate_Sources_JA.xlsx` にある資料から選びました。既存の資料ノートは2026-10-05～06の選択読取、YamahaとAutoFormの追加読取は2026-10-07です。表の資料リンクから、実際に読んだ場所を確認してください。

## 資料の種類と、確認できる範囲

| 根拠 | 確認できること | 追加の根拠が必要なこと |
|---|---|---|
| CADヘルプの本文 | その製品の名称、操作、対象、設定項目 | 全ソフト共通の定義、他ソフトでの同義関係、STLの作成履歴 |
| 金型・製品の用語集 | その資料の分野における言葉の使い方 | 全金型への適用、目の前の部品の役割、一般的な分類階層 |
| 規格のカタログ・概要 | 規格の対象や資料を探す手掛かり | 規格本文にある定義・数値・要求事項 |
| 語彙整備の資料 | 名称、範囲、関係、変更を管理する考え方 | 金型形状そのものの正しい定義 |
| 元CAD・STLと断面 | 調べた領域の形と、方法に応じた座標上の測定 | 設計目的、加工方法、物理単位、限定断面からの全体否定 |
| 図面・設計説明 | 記載された単位、用途、参考方向、意図 | その記載と現行CADとの一致。モデルの版を確認する |
| 教材として作った形 | 作成条件から決まる形状・開閉状態 | 実際の金型部品としての妥当性、業界での用語承認 |

ISO 12165の本文は本プロジェクトの制限によりAIへ入力しません。JDMIAの会員検索も未読です。これらを定義の読了根拠に数えません。

## 15概念の根拠と未確認部分

| 根拠ID／概念 | Excel内の資料と確認場所 | 今の定義への根拠 | 部品に使うための根拠／残る境界 |
|---|---|---|---|
| CL-001／[[Hole]] MC-001 | [[PTC_Creo_Hole_Feature_JA]]の種類・方向・深さ、[[Autodesk_Inventor_2026_Hole_JA]] | 穴名称と設定の使用例。一般定義はプロジェクト草案 | 穴の領域、開口、終端を確認。Hole操作で作ったとは推定しない |
| CL-002／[[Counterbore]] MC-002 | 同じ穴資料のカウンタボア・入口形状の項目 | ソフトで主穴と入口形状を扱う例 | [[CAD_Counterbore_Example]]の円筒形入口と肩。主穴との関係を記録し、一つの通路を二つの孔と数えない |
| CL-003／[[Countersink]] MC-003 | 同じ穴資料の皿穴・入口形状の項目 | 入口に関する名称と操作の使用例 | [[CAD_Countersink_Example]]の円すい状入口。皿穴・皿ざぐりの採用表記は未確認 |
| CL-004／[[Pocket]] MC-004 | [[PTC_Creo_Machining_Features]]のPocket、[[Autodesk_Fusion_2D_Pocket_JA]] | 加工文脈の床・壁・領域の使い方 | [[CAD_Rectangular_Pocket_Example]]等の底と壁。CAM操作範囲を一般形状と同じにしない |
| CL-005／[[Slot]] MC-005 | [[PTC_Creo_Recognized_Features]]のslot例、[[PTC_Creo_Machining_Features]] | 認識・加工文脈での用例 | [[CAD_8972_Slot_and_Recesses]]の経路、幅、端部、貫通状態。細長さだけの共通しきい値は未確定 |
| CL-006／[[Rib]] MC-006 | [[JEED_Plastic_Mold_Glossary_Index]]のリブ・ボス、[[Yamaha_Casting_Glossary_Scope_Check]]のリブ | 板状形と補強の使用文脈 | [[CAD_Rib_Boss_Comparison]]の形状。実物の補強・反り対策は別の設計資料が必要 |
| CL-007／[[Boss]] MC-007 | JEEDのリブ・ボス、Creoの認識boss／加工Boss Top | 名称と分野別の用例。JEEDの例は開いた円柱状の形で、現在の「局所的な突起」全体の定義より狭い | 今回の中が詰まった円柱状突起は形の比較例。一般的なBossの境界は草案で、実例があっても資料の不足は解消しない |
| CL-008／[[Fillet]] MC-008 | [[Onshape_Fillet]]の操作説明、[[SOLIDWORKS_Fillet_Overview_2025_JA]]の確認範囲 | 丸い移行を作る操作と選択項目 | [[CAD_7145_Fillet_and_Internal_Structure]]の移行候補と[[CAD_Fillet_Boss_Name_Check]]の未確定例。曲面やファイル名だけでFillet・作成コマンドを決めない |
| CL-009／[[Chamfer]] MC-009 | [[Onshape_Chamfer]]の面取りと距離・角度の説明 | 操作と代表的な斜面の例 | [[Shape_Comparison_Examples]]の断面。数値は測定箇所・基準面を必要とする |
| CL-010／[[Draft_Angle]] MC-010 | JEEDの抜き勾配、Yamahaの抜け勾配 | 離型方向と傾斜の分野別説明 | 対象面、方向、測定方法が必要。方向不明の斜面は抜き勾配として確定しない |
| CL-011／[[Undercut_(injection_molding)|Undercut]] MC-011 | JEED・芝浦のアンダーカット、Yamahaの同項目 | 抜き方向による条件の用例 | 抜き方向と、抜けない理由の幾何・設計根拠。凹部があるだけでは確定しない |
| CL-012／[[Wall_Thickness]] MC-012 | Yamahaの肉厚 | 部品の断面の厚さという説明 | [[CAD_4423_Open_Void]]の局所測定。二面、位置、方向、単位を記録。全体の最小肉厚は未確認 |
| CL-013／[[Internal_Void]] MC-013 | 一覧内の資料には、今回確認した範囲で中立的な一般定義がない。InventorのCavityは樹脂の成形空間 | 定義はプロジェクト提案。開いた内部領域も含む案 | [[CAD_Enclosed_Open_Void_Teaching]]で開閉の記録方法を確認。教材で用語の一般性は証明できない |
| CL-014／[[Cooling_Channel]] MC-014 | [[Autodesk_Inventor_Mold_Glossary]]のCooling channel／冷却管、JEEDの冷却回路 | 冷却媒体の経路という機能を含む使用例 | 経路の幾何と、当該経路を冷却に使う資料。現在のSTLには機能の根拠がない |
| CL-015／[[Gas_Vent_(injection_mold)|Gas Vent]] MC-015 | JEEDのガス抜き・エア抜き、ガスベント | 溝の説明と排気機能の説明が別項目にある | 排気経路と排気用途の資料。すべての溝をガスベントにしない |

## 一つの判断を記録する形

将来のDBでは、出典を概念全体に付けるだけでなく、「どの説明を支えるか」も残します。次は記録例です。

```yaml
assertion_id: CL-014-definition
concept_id: MC-014
claim_scope: Inventor 2023の冷却管の用法
source_note: Autodesk_Inventor_Mold_Glossary
source_locator: English Cooling channel / Japanese 冷却管
evidence_kind: source_usage
project_definition_status: draft
```

この資料である穴の冷却用途まで確定できるわけではありません。部品の用途には別の `part_id`、`feature_id`、設計資料への参照を付けます。

[[RAG_Search_Verification_Cases]]では、根拠が足りないときに「未確認」と返す問題も用意しました。[[Feature_Description_Rules]]と[[Feature_Relations]]を併用します。
