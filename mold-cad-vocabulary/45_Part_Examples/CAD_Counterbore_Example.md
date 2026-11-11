---
category: part_example
status: mesh_based_draft
part_id: STL-counterbore
physical_unit: unknown
source_sha256: 2e57f29dd79367e1bbe9d763b92b34d94e341488fb1f864b0016fd7d40970c42
---
# STL例：穴と座ぐり

![[counterbore_views.png]]

## 形を読む

外形は50 × 50 × 20です。中心は X=25、Y=25。中央の通路は下の面まで続き、上側で円筒形に広がります。Z=11 に肩があり、Z=20 が上の開口です。表示の円筒形は STL の多角形近似です。

| ID | 用語 | メッシュから得た値・位置 |
|---|---|---|
| F-01 | [[Hole]] | 主穴の径は約6。細い部分は Z=0〜11。上の入口形状を通じて部品を貫通する |
| F-02 | [[Counterbore]] | 入口の径は約12。深さは20−11=9。円筒形の壁と平らな肩がある |

## 関係を書く

- F-02 **entrance_form_of** F-01：座ぐりは、この穴の入口形状です。
- F-02 **coaxial_with** F-01：両方の中心軸は X=25、Y=25、Z方向です。

「座ぐり付きの穴」という文を、二つの特徴と二つの関係に分けました。単にファイルに Counterbore という名前を付ける場合と比べ、入口の径・深さ・主穴を別々に検索できます。

## 統一した記述

> 部品中央に貫通する穴がある。主穴の径は約6。上側の入口に、径約12、深さ9の座ぐりがある。穴と座ぐりは同じ軸を持つ。

用途は unknown です。ねじの頭を収めるための座ぐりかどうかは、この形だけでは確認できません。

## 根拠と範囲

元ファイル：[ counterbore.stl ](/home/malanya/projects/cad-structure-search/data/simple_CAD_dataset/counterbore.stl)。寸法はすべて **input_units（入力座標の単位）** です。mmという単位は確認できていません。原点と軸は STL の座標です。金型の抜き方向や、この形の金型での用途は未確認です。

頂点と断面から直接得た形状の観察を、既存の用語に対応させた草案です。設計意図、正確な曲面、設計履歴、自交差の有無を確定したものではありません。人による正式な承認はまだありません。

数値の根拠は [[mesh_observations.json]]、検索用の構造化記録は [[Simple_CAD_Feature_Records.json]]。整理方法は [[Simple_CAD_Dataset_Study]] と [[Feature_Relations]] を参照してください。
