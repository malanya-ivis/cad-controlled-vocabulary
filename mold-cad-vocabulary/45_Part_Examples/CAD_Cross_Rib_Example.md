---
category: part_example
status: mesh_based_draft
part_id: STL-rib_cross
physical_unit: unknown
source_sha256: 094221d4125521e46f2d7c36cf8e71dba2cfc4150b070e77f6a2ae98c3229e8d
---
# STL例：交差する二方向のリブ

![[rib_cross_views.png]]

## 形を読む

外形は60 × 60 × 18です。下の板状部分は Z=0〜8。その上に十字形の壁状の出っ張りがあり、Z=18まで続きます。

| ID | 用語 | 位置と値 |
|---|---|---|
| F-01 | [[Rib]] | X方向。X=5〜55、Y=28.5〜31.5、Z=8〜18。長さ50、厚さ3、高さ10 |
| F-02 | [[Rib]] | Y方向。X=28.5〜31.5、Y=5〜55、Z=8〜18。長さ50、厚さ3、高さ10 |

二つの方向に分けて説明するのは、本プロジェクトの特徴の分け方案です。STLには設計履歴がないため、CADで実際に何回の Rib 操作をしたかは分かりません。中心の重なる領域を、体積の計算で二重に数えません。

## 関係を書く

- F-01 **intersects** F-02：中央の領域で交わる。
- F-01、F-02 **located_on** base_top:z=8：同じ板の上面にある。

## 統一した記述

> 板の上面に、X方向とY方向の壁状のリブがある。どちらも長さ50、厚さ3、高さ10で、中央で交差する。

「反り対策」「補強」などの目的は unknown です。形を観察できても、設計者がその目的で作ったという資料はありません。

## 根拠と範囲

元ファイル：[ rib_cross.stl ](/home/malanya/projects/cad-structure-search/data/simple_CAD_dataset/rib_cross.stl)。寸法はすべて **input_units（入力座標の単位）** です。mmという単位は確認できていません。原点と軸は STL の座標です。金型の抜き方向や、この形の金型での用途は未確認です。

頂点と断面から直接得た形状の観察を、既存の用語に対応させた草案です。設計意図、正確な曲面、設計履歴、自交差の有無を確定したものではありません。人による正式な承認はまだありません。

数値の根拠は [[mesh_observations.json]]、検索用の構造化記録は [[Simple_CAD_Feature_Records.json]]。整理方法は [[Simple_CAD_Dataset_Study]] と [[Feature_Relations]] を参照してください。
