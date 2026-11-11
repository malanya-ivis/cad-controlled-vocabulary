---
category: part_example
status: mesh_based_draft
updated: 2026-10-07
---
# リブとボスを同じ大きさの部品で比べる

元データは `simple_CAD_dataset/rib.stl` と `boss.stl` です。二つとも外形は50×50×18ですが、上面の突起の形が違います。ファイル名を答えとして使わず、外観とX=25、Z=13の断面を確認しました。

![[rib_views.png]]

![[boss_views.png]]

## 形の違いと記録

数値はSTLの入力座標です。mm等の物理単位、加工方法、金型用途、設計目的は不明です。

| 項目 | STL-rib／F01 | STL-boss／F01 |
|---|---|---|
| 概念の対応候補 | [[Rib]] MC-006 | [[Boss]] MC-007 |
| 突起を支える上面 | Z=8 | Z=8 |
| 突起の上端 | Z=18 | Z=18 |
| 高さ | 18−8=10 | 18−8=10 |
| 平面での形 | X=5～45、Y=23.5～26.5の細長い矩形 | 中心(X,Y)=(25,25)、半径約6の多角形近似 |
| 長さ・幅 | 長さ40、厚さ3 | 直径約12 |
| 判断の理由 | 一方向に長く続く板状の突起 | 上面の局所的な円柱状の突起 |
| 設計目的 | unknown | unknown |

リブの値は頂点の座標差で求めました。ボスの直径は上端の外周頂点から中心までの距離の約2倍です。中央断面も円柱状の突起を示します。選択断面ではボス内部の穴は見えませんが、この観察を任意の内部欠陥がないことの証明にはしません。

## 資料と実例の境界

Excel14行の[[JEED_Plastic_Mold_Glossary_Index]]の「リブ・ボス」は、リブを板状、ボスを開いた円柱状の補強部として説明しています。この実例のボスは、確認した上端と断面では中が詰まっています。現在の「局所的な突起」というプロジェクト案で対応付けていますが、JEEDの例と完全に同じ範囲と判断したわけではありません。

Excel8・9行の[[PTC_Creo_Recognized_Features]]と[[PTC_Creo_Machining_Features]]はBoss等の使用例です。これらと実例を合わせても、一般定義が承認済みになるわけではありません。[[Claim_Evidence_Matrix]]のCL-006とCL-007を参照してください。

補強、反り対策、ねじ固定という目的は形から付けません。将来図面や設計者の説明が得られたら、同じ部品・特徴IDに用途の根拠を追加できます。

## 確認できるファイル

- 原STL：[rib.stl](/home/malanya/projects/cad-structure-search/data/simple_CAD_dataset/rib.stl)、[boss.stl](/home/malanya/projects/cad-structure-search/data/simple_CAD_dataset/boss.stl)。読み取り専用で調査しました。
- [[supplement_mesh_observations.json]]：SHA-256、断面位置、座標、ボス上端の半径範囲。
- [[Supplemental_Feature_Records.json]]：部品ID、特徴ID、対応概念、属性、根拠画像。
- 生成スクリプト：`tools/inspect_vocabulary_supplement.py`。

[[Targeted_CAD_Gap_Examples]]と[[Shape_Comparison_Examples]]から、この比較へ進めます。
