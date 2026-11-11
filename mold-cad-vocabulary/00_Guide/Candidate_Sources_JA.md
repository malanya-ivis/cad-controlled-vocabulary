# 調査資料と優先順位

**更新:** 2026-10-06。上司の回答を受け、対象を「特定ソフトの機能」や「特定種類の金型部品」に限定せず、金型CADの単一部品に含まれる形状フィーチャ・形状上の性質・内部構造に改めました。最初の調査例が一系統に偏っても、それは作業上の試行であり、最終範囲の制限ではありません。詳しくは [[Scope_Revision_2026-10-06]] と [[Design_Policy]] を参照してください。

## 1. 統制語彙の整備方法

上司が指定した方法参照です。条項ごとの読取状況は個別ノートで確認してください。

- [ANSI/NISO Z39.19](../10_Vocabulary_Studies/NISO_Z39_19.md) — 用語の採用根拠、優先語、複合語、関係、維持。
- [ISO 25964-1](../10_Vocabulary_Studies/ISO_25964_Interoperability_Catalog_Study.md) — シソーラスの構築・維持。現在の版と改訂状況は資料ノートに記録。
- [ISO 25964-2](../10_Vocabulary_Studies/ISO_25964_Interoperability_Catalog_Study.md) — 他の語彙との対応付けと、その維持。

## 2. 構造の参考例

- [MeSH](../10_Vocabulary_Studies/MeSH.md) — 優先語、同義表現、概念の分類と階層の例。
- [ICD-10](../10_Vocabulary_Studies/ICD-10.md) — 実務的な分類階層と区分注記の例。

いずれも医療分野の体系です。構造・運用の比較に使い、金型形状の分類をそのまま移植しません。

## 3. 形状・製造フィーチャの技術資料

- [STEP AP 224](../20_Sources/ISO_10303_224_Machining_Features_Record.md) — 単一機械部品の加工フィーチャ表現。設計上の形状フィーチャと加工計画上のフィーチャを比べる資料です。
- [JIS Z 8114:1999 製図―製図用語](../20_Sources/JIS_Z_8114_Technical_Drawing_Terms_Record.md) — 日本語の製図用語。現時点では公式書誌情報のみ確認し、規格本文は読んでいません。
- [Onshape / PTC Creo / Autodesk Inventor / SOLIDWORKS のCADヘルプ](../50_Reference_Registers/Source_Coverage_and_Gaps.md) — Hole、座ぐり、ポケット、Slot、リブ、フィレット、面取りに加え、抜き勾配・抜き方向分析・Shellの使い方を確認。特定ソフトの操作を一般定義にしません。今回確認したページは [[PTC_Creo_Draft_Feature]]、[[PTC_Creo_Profile_Rib]]、[[PTC_Creo_Shell_Feature]]、[[Autodesk_Inventor_2026_Rib_JA]]、[[Onshape_Draft]]、[[Onshape_Draft_Analysis]]、[[Onshape_Slot_Sketch]]、[[SOLIDWORKS_Fillet_Overview_2025_JA]]。

## 4. 金型の用例資料

既存の資料は射出成形に偏っています。これを初期例として利用しつつ、他の金型分野に広げるときは同じ用語の適用範囲を再確認します。

- [Autodesk Inventor 金型用語集](../20_Sources/Autodesk_Inventor_Mold_Glossary.md)
- [JEED 用語集・設計教材](../20_Sources/JEED_Plastic_Mold_Glossary_Index.md)、[D3](../20_Sources/JEED_Design_Training_D3.md)、[D4](../20_Sources/JEED_Design_Training_D4.md)
- [MISUMI 技術記事](../50_Reference_Registers/Source_Coverage_and_Gaps.md)
- [芝浦機械 用語集](../20_Sources/Shibaura_Injection_Molding_Glossary.md)
- [南雲製作所 プレス金型用語集](../20_Sources/Nagumo_Press_Mold_Glossary.md) — プレス金型用語の追加例。平面度・表面粗さ・ノック穴など、単一部品の形状や性質に関係する項目を選び、部品名・加工法・機械用語と区別します。

金型部品名を増やすこと自体を目標にせず、単一部品上の形状・属性・内部構造の記述に関係する箇所を選んで読みます。

## 5. 初回調査の進め方

1. Z39.19、ISO 25964、MeSH、ICD-10から、語彙の採用・分類・関係・更新に使えるルールを整理する。
2. AP 224、JIS Z 8114、CADヘルプを照合し、形状フィーチャ・属性・加工用語の境界を記録する。
3. Hole、座ぐり、皿ざぐり、Pocket、Slot、Rib、Boss、Fillet、Chamfer、Draft Angle、Undercut、Wall Thickness、内部流路の例を単一部品の視点で整理する。
4. 各フィーチャの位置・寸法・内部可視性・他フィーチャとの関係をどう記述するか、例を作る。設計目的は図面・仕様・解析などの根拠と結び付ける。
5. 用語に漏れがあれば [[Feature_Description_Rules]] に従って追加し、最初の一覧を網羅的な辞典とは見なさない。

## 確認済み範囲

資料ごとのアクセス状況、版、利用条件、実際に読んだ箇所は [[Source_Coverage_and_Gaps]] と `20_Sources/` の個別ノートに記録しています。カタログ抄録は規格本文の定義と区別してください。

## 2026-10-07：Excel追加候補の利用

`docs/Candidate_Sources_JA.xlsx`の22行Yamahaと24行AutoFormを選び、関連項目の本文を読みました。[[Yamaha_Casting_Glossary_Scope_Check]]は7項目、[[AutoForm_Press_Glossary_Scope_Check]]は2項目です。資料の範囲確認だけだった状態から、選択項目の読取に進みました。

[[Cross_Mold_Domain_Transfer]]で用語の適用範囲を比較し、[[Claim_Evidence_Matrix]]で15概念の根拠を整理しました。実形状の追加は[[Targeted_CAD_Gap_Examples]]、課題3への適用例は[[RAG_Search_Verification_Cases]]です。
