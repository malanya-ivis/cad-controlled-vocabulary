---
category: knowledge_group
status: draft
---
# 形状の特徴

部品上の局所的な形を、まず「材料がへこんでいる」「出ている」「角が変化している」の三つの観点で整理します。これは説明のための分類案です。設計履歴にどの命令があるかは、形を見分ける条件にしません。

| 整理の観点 | 概念 | 見分ける手掛かり |
|---|---|---|
| 穴と入口の形 | [[Hole]]、[[Counterbore]]、[[Countersink]] | 開口、穴の終わり、入口の円筒形／円すい形の広がり |
| へこみ・溝 | [[Pocket]]、[[Slot]] | 底と壁、開いている側、長い方向、溝の経路 |
| 出っ張り | [[Rib]]、[[Boss]] | 薄い壁のように続く形か、局所的な出っ張りか |
| 角の変化 | [[Fillet]]、[[Chamfer]] | 丸い移行面か、斜めの移行面か |

## 形の区別

- 穴の入口が円筒形に広がり、肩がある場合は [[Counterbore]] を検討します。円すい形に広がる場合は [[Countersink]] を検討します。主穴と入口形状は関連付けて記録します。
- [[Pocket]] と [[Slot]] は重なる場合があります。細長さの一律の数値を作らず、経路、幅、底、端部、貫通状態を記録し、判断が難しければ候補を残します。
- [[Rib]] と [[Boss]] は形の区別です。「反りを減らす」「ねじを固定する」などの目的は、[[Feature_Relations]] で部品上の特徴に付けます。
- [[Fillet]] と [[Chamfer]] はどちらも他の特徴の境界に現れます。ポケットの角にある Fillet は Pocket の下位語ではなく、その境界にある別の特徴として扱えます。

## 資料から得た内容

[[Onshape_Hole]] と [[Autodesk_Inventor_2026_Hole_JA]] は穴の入口形状と終端条件を分けています。[[PTC_Creo_Machining_Features]] は Pocket と Slot の加工上の用法を示します。[[PTC_Creo_Profile_Rib]] と [[JEED_Plastic_Mold_Glossary_Index]] は Rib/Boss の形と目的を比べる手掛かりです。[[Onshape_Fillet]] と [[Onshape_Chamfer]] は角の形状と操作の用法を示します。

この資料を使った記述項目は各概念ノートにあります。[[Shape_Properties]] と合わせて値を付け、[[Single_Part_Description_Example]] のように一つの部品へ適用します。

## STLで確認した例

[[CAD_Counterbore_Example]] と [[CAD_Countersink_Example]] は入口形状の違い、[[CAD_Rectangular_Pocket_Example]] は底と壁、[[CAD_Cross_Rib_Example]] は出っ張りと交差関係の記述例です。いずれも [[Simple_CAD_Dataset_Study]] のメッシュから得た観察です。

## 実例で形を比べる

[[Shape_Comparison_Examples]] を参照してください。[[CAD_8972_Slot_and_Recesses]] は、段付きの長穴と、底の状態が違う凹部を同じ部品内で比べる例です。
