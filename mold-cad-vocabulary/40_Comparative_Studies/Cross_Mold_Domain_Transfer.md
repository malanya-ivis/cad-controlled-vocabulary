---
category: comparative_study
status: source_comparison_draft
updated: 2026-10-07
---
# 金型の分野が変わっても使える言葉か

目的は、射出成形で整理した言葉を、鋳造やプレス金型でも使えるか確認することです。今回は資料の説明を比べました。実際の射出・鋳造・プレス金型部品をそろえたCAD検証は、まだ行っていません。

## 今回使った資料

元の一覧は `docs/Candidate_Sources_JA.xlsx` の「資料一覧」です。行番号は見出し行を含みます。

| 分野 | Excelの行 | 読んだ範囲 | 資料ノート |
|---|---|---|---|
| 射出成形 | 11–14、21 | 既存ノートに記録したInventor、JEED、芝浦機械の選択項目。今回はJEEDのアンダーカット、抜き勾配、リブ・ボスを再確認 | [[Autodesk_Inventor_Mold_Glossary]]、[[JEED_Plastic_Mold_Glossary_Index]]、[[Shibaura_Injection_Molding_Glossary]] |
| 鋳造 | 22 | Yamahaの「あ行」「な行」「ら行」から、下表に必要な項目 | [[Yamaha_Casting_Glossary_Scope_Check]] |
| プレス成形 | 24 | AutoFormのドロービード、面ひずみの本文 | [[AutoForm_Press_Glossary_Scope_Check]] |

資料には「金型自身の形」と「金型で作る製品の形」があります。どちらについて書かれた説明かを残します。製品のリブの説明を読んだだけで、実際の金型部品の用途まで確認したことにはなりません。

## 言葉ごとの比較と判断

下の判断は本プロジェクトの案です。資料同士の正式な同義関係を決めたものではありません。

| 対象 | 資料で確認できた違い・共通点 | 今の語彙での扱い | CADに使うとき必要なこと |
|---|---|---|---|
| [[Undercut_(injection_molding)|アンダーカット]] | JEEDとYamahaは、指定した抜き方向では取り出せない形という観点を共有する | 現在のMC-011を鋳造にも使う候補。ファイル名のinjection_moldingは現在の調査履歴を示す | 抜き方向、対象面・領域、干渉の確認方法。方向不明なら未確認 |
| [[Draft_Angle|抜き勾配]] | JEEDは樹脂の離型、Yamahaは型から取り出すための傾斜を説明する。Yamahaには「抜け勾配」という表記もある | MC-010の形状条件を共通に使う候補。表記の採用は草案 | 対象面、参考方向、角度の測り方。資料の推奨角度を全金型の基準にしない |
| [[Rib|リブ]] | JEEDは製品の板状補強、Yamahaは鋳物の平面・薄い部分に付く板状の補強を説明する。Yamahaの説明には平面との直角関係がある | MC-006と比較できる。ただし、全リブに直角や補強目的を必須とする規則は作らない | 形状の厚さ・高さ・範囲と、設計目的の根拠を別に記録 |
| [[Wall_Thickness|肉厚]] | Yamahaは部品の断面の厚さとして説明する | MC-012の他分野での用例を追加できる | 二つの面、測定位置・方向、単位。局所値と最小値を区別 |
| 鋳抜き穴 | Yamahaは鋳造時に型で作られる穴を説明する | 形は[[Hole]]で表し、作り方は別の属性候補 `manufacturing_method` に記録 | 鋳造で作ったことを示す図面・工程資料。穴の外観だけでは判断しない |
| ドロービード | AutoFormは絞り時の材料流入を調整するものとして説明し、位置・長さ等を扱う | プレス分野の機能を持つ特徴候補。[[Rib]]の同義語にはしない | 金型上の位置、形状と、材料流入を調整する役割の資料。具体的な形の分類は別途確認 |
| 面ひずみ | AutoFormの説明は目標形状と実際の形状の差を扱う | 比較対象を必要とする状態・解析結果の候補。見た凹部をすべて[[Pocket]]や不良と決めない | 基準形状、測定・解析結果、比較した場所。CAD形状だけでは意図しない変形と判断できない |
| Core／中子 | Yamahaの中子は中空を作るために型内に置くもの。InventorのCoreとは使用文脈が異なる | [[Core_(mold_component)|Core]]の背景用語として意味の違いを残す。[[Internal_Void]]と同じにしない | 部品・型・製品のどれを指すか。英語表記だけで概念を統合しない |
| 冷却水／冷却管 | Yamahaの冷却水は媒体、Inventorの冷却管は媒体が通る経路 | 冷却水と[[Cooling_Channel]]を区別する | 経路の形と冷却用途の資料。媒体名だけでは特定の穴に用途を付けられない |

## この比較で変えたこと

- [[Rib]]、[[Draft_Angle]]、[[Wall_Thickness]]、[[Undercut_(injection_molding)|Undercut]]に、鋳造分野の使用例へのリンクを追加しました。定義の確認状態は草案のままです。
- 鋳抜き穴、ドロービード、面ひずみは[[Candidate_Term_Queue]]に候補として残しました。形の概念、属性、機能、解析結果のどれとして記録するかを先に確認します。
- 資料の分野、説明対象が金型か製品か、加工方法・設計目的の根拠を、将来のデータ項目候補として残します。

## 次に実物で確認すること

射出・鋳造・プレスのCAD部品を、出所と分野が分かる状態で一つずつ用意し、同じ記述ルールを適用します。現在のSTLは分野・用途が不明なので、この三分野の実物検証には数えません。今回作った[[Targeted_CAD_Gap_Examples]]は、形の記述を確かめるための例です。

## 出典の場所

- [Yamaha「あ行」](https://www.yamaha-motor.co.jp/cf/data/glossary/) — アンダーカット、鋳抜き穴。
- [Yamaha「な行」](https://www.yamaha-motor.co.jp/cf/data/glossary/0005.html) — 中子、肉厚、抜け勾配。
- [Yamaha「ら行」](https://www.yamaha-motor.co.jp/cf/data/glossary/0009.html) — リブ、冷却水。
- [AutoForm ドロービード](https://www.autoform.com/jp/glossary/drawbeads/) — 本文の役割、位置・長さの説明。
- [AutoForm 面ひずみ](https://www.autoform.com/jp/glossary/surface-defects/) — 本文冒頭の実形状と目標形状の説明。
- [JEED用語集](https://www.tetras.uitec.jeed.go.jp/plastic_mold/glossary/index.html) — 選択項目。公開ページのデータにある説明を確認。画像は未確認。
- [Inventor 2023 用語集](https://help.autodesk.com/cloudhelp/2023/JPN/Inventor-Help/files/GUID-63A5DCE8-2B43-494F-8F56-7A7CBBAD41FC.htm) — Core、冷却管。対応する英語版は資料ノートに記録。

[[Claim_Evidence_Matrix]]で、資料から言える範囲と、部品で確認する範囲を確かめます。
