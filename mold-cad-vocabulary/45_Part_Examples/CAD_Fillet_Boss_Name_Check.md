---
category: part_example
status: candidate_geometry_review
updated: 2026-10-07
---
# fillet_boss.stl：ファイル名と断面を確かめる

このファイルの名前にはfilletがあります。しかし、名前だけで[[Fillet]]を付けることはできません。X=20とZ=10の断面では、中央の円柱状突起の周りに、輪の形で丸い凸部が見えます。

![[fillet_boss_views.png]]

## 今回記録した二つの領域

| 特徴ID | 観察した形 | 語彙の対応 | 根拠と状態 |
|---|---|---|---|
| STL-fillet_boss／F01 | 中心(X,Y)=(20,20)、半径約6の円柱状突起。上端Z=16 | [[Boss]] MC-007の草案 | 中央断面と上端の頂点形状 |
| STL-fillet_boss／F02 | 突起の周囲の環状の丸い凸部。およその半径範囲6～14、Z=8～12 | Filletは候補のみ。確定した概念割当は空欄 | 領域の形は観察済み。二面の角を置き換える移行面としての対応は未確認 |

断面の輪の凸部を、中央円柱から基面へつながる通常の丸い角と同じにするには根拠が足りません。今回の特徴間の `F02 boundary_of F01` はunknownです。これは部品に一切フィレットがないという全体否定ではありません。

輪の凸部について、中心からの距離rとZ座標を使い、頂点を円へ当てはめました。中心はおよそ(r,Z)=(10,8)、半径は約4、頂点からの最大残差は約0.0000018 input_unitsです。この結果は丸い輪の断面の記録であり、CADのFillet操作や設計意図の証明ではありません。STLの平面三角形間の曲線は近似です。

## 資料のルールを適用する

Excel6行の[[Onshape_Fillet]]は、角を丸くする操作を説明しています。今回の形をその結果として扱うには、角と移行面の対応を確認する必要があります。Excel8行の[[PTC_Creo_Recognized_Features]]の認識名称やファイル名だけでは、対応が確定しません。

[[RAG_Search_Verification_Cases]]のQ10は、F02の候補を検索の確定結果に混ぜないことを確認します。ファイル名にfilletが含まれていることを、自動的なラベル付けの根拠にしません。

## 確認できるファイル

- 原データ：[fillet_boss.stl](/home/malanya/projects/cad-structure-search/data/simple_CAD_dataset/fillet_boss.stl)。単位、用途、履歴は不明。
- [[supplement_mesh_observations.json]]の`fillet_boss`：ハッシュ、断面、円の当てはめ方法と結果。
- [[Supplemental_Feature_Records.json]]：F01の草案と、F02の候補・unknown関係を別に記録。
- [[Claim_Evidence_Matrix]]のCL-008：定義の資料と実例の確認範囲。
