---
category: part_example
status: mesh_based_draft
part_id: STL-rectpocket
physical_unit: unknown
source_sha256: 4f9f6ce15b5ec83a2d752372dffcc60bb90a4eb35ed6b6617d5843b0e361ca39
---
# STL例：矩形ポケットと底の厚さ

![[rectpocket_views.png]]

## 形を読む

外形は50 × 50 × 15です。上面 Z=15 に、底と四つの壁を持つ矩形のへこみがあります。へこみの範囲は X=15〜35、Y=18〜32、底は Z=9です。

| 記録 | 用語・対象 | 値と測り方 |
|---|---|---|
| F-01 | [[Pocket]] | 長さ35−15=20、幅32−18=14、深さ15−9=6。底がある |
| P-01 | [[Wall_Thickness]] | ポケットの底と部品の下面との間。Z方向に9−0=9 |

P-01 は部品の局所的な厚さの記録です。部品全体の高さ15、ポケットの深さ6、底下の厚さ9は、それぞれ対象が違います。三つを同じ「厚さ」として保存しません。

## 統一した記述

> 部品の上面に20 × 14、深さ6の矩形ポケットがある。ポケットには底があり、底の下の材料の厚さは、Z方向に測ると9である。

この例では、四角いへこみを [[Pocket]] の記述例にします。長さと幅だけから「スロットではない」とする共通の比率ルールは作りません。[[Slot]] と比較するときは、形の経路や端部、底の有無も確認します。

## 根拠と範囲

元ファイル：[ rectpocket.stl ](/home/malanya/projects/cad-structure-search/data/simple_CAD_dataset/rectpocket.stl)。寸法はすべて **input_units（入力座標の単位）** です。mmという単位は確認できていません。原点と軸は STL の座標です。金型の抜き方向や、この形の金型での用途は未確認です。

頂点と断面から直接得た形状の観察を、既存の用語に対応させた草案です。設計意図、正確な曲面、設計履歴、自交差の有無を確定したものではありません。人による正式な承認はまだありません。

数値の根拠は [[mesh_observations.json]]、検索用の構造化記録は [[Simple_CAD_Feature_Records.json]]。整理方法は [[Simple_CAD_Dataset_Study]] と [[Feature_Relations]] を参照してください。
