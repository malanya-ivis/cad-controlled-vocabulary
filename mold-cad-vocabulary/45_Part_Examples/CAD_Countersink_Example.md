---
category: part_example
status: mesh_based_draft
part_id: STL-countersink
physical_unit: unknown
source_sha256: 50477bac9c997dc087c0edbb99f481abbac512131d3e80cd0f14ed05d3fb1517
---
# STL例：穴と皿ざぐり

![[countersink_views.png]]

## 形を読む

外形は50 × 50 × 12です。中央の通路は下の面まで続き、上側で円すい状に広がります。上の開口の径は約16、下の主穴の径は約6です。

| ID | 用語 | メッシュから得た値・位置 |
|---|---|---|
| F-01 | [[Hole]] | 主穴の径は約6。入口形状を通じて上下面に開く |
| F-02 | [[Countersink]] | 上側の円すい状の入口。深さは約5、角度は未記録 |

F-02 entrance_form_of F-01、F-02 coaxial_with F-01 と記録します。[[CAD_Counterbore_Example]] と関係は同じですが、入口形状が円筒形と肩ではなく、円すい状なので用語が変わります。

## メッシュの注意点

元の320三角形のうち16個は面積がゼロでした。図と断面を作るため、読み込んだ作業用メッシュだけから削除しました。元の STL は変更していません。接続部分の頂点は Z≈6.987〜7.006 に分かれているため、深さを約5と記録し、正確な設計寸法として扱いません。

## 統一した記述

> 部品中央の穴は上下面に開く。主穴の径は約6。上側の入口は円すい状に広がり、開口の径は約16、深さは約5。入口と主穴は同じ軸を持つ。

皿ざぐりという語への対応は草案です。メッシュの接続部分には不確かさがあり、寸法の精密な確認には元の設計データが必要です。

## 根拠と範囲

元ファイル：[ countersink.stl ](/home/malanya/projects/cad-structure-search/data/simple_CAD_dataset/countersink.stl)。寸法はすべて **input_units（入力座標の単位）** です。mmという単位は確認できていません。原点と軸は STL の座標です。金型の抜き方向や、この形の金型での用途は未確認です。

頂点と断面から直接得た形状の観察を、既存の用語に対応させた草案です。設計意図、正確な曲面、設計履歴、自交差の有無を確定したものではありません。人による正式な承認はまだありません。

数値の根拠は [[mesh_observations.json]]、検索用の構造化記録は [[Simple_CAD_Feature_Records.json]]。整理方法は [[Simple_CAD_Dataset_Study]] と [[Feature_Relations]] を参照してください。
