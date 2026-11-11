---
category: part_example
status: illustrative
part_id: DEMO-01
---
# 一つの金型部品の記述例

これは本プロジェクトで作った教材用の記述例です。実物の CAD や図面を読み取った結果ではありません。寸法、位置、関係はすべて仮定です。実データへの取り込み時は illustrative の記録を除外します。

例の対象は一つの金型入れ子です。ここでは、面の参照を top、back、section-A と呼びます。実際のデータでは、これを CAD の面IDや図面の断面位置に置き換えます。抜き方向を使う記録では、入れ子の座標系で +Z と仮定します。

## 特徴の記録

| ID | 概念 | この例での記述 | 関係 |
|---|---|---|---|
| F-01 | [[Hole]] | top に開いた円筒形の止まり穴。径6 mm、深さ15 mm | F-02 が入口形状 |
| F-02 | [[Counterbore]] | F-01 の入口。径10 mm、深さ3 mm、円筒形の壁と肩 | entrance_form_of F-01、coaxial_with F-01 |
| F-03 | [[Pocket]] | top に開いたへこみ。底と壁があり、深さ8 mm | F-04 が境界の移行形状 |
| F-04 | [[Fillet]] | F-03 の底と壁の間の丸い移行。半径2 mmと仮定 | boundary_of F-03 |
| F-05 | [[Rib]] | back にある薄い壁状の出っ張り。厚さ3 mm | located_on back。目的は unknown |
| F-06 | [[Hole]] と [[Cooling_Channel]] の仮の用途 | 円筒形の内部通路。径8 mm、側面に開口 | connects_to F-07。冷却用途はこの例の仮定 |
| F-07 | [[Hole]] と [[Cooling_Channel]] の仮の用途 | F-06 と内部でつながる別の通路 | connects_to F-06。別特徴として識別 |

F-06 は、形の説明が Hole、用途の説明が Cooling Channel です。同じ物理的特徴のIDを使います。この例の用途と接続は仮定であり、実際には断面と冷却設計情報の両方で確認します。

## 性質を付ける

| 対象 | 性質 | 例の値と条件 |
|---|---|---|
| F-03 の壁 | [[Draft_Angle]] | +Z に対して2°と仮定。壁面と抜き方向の角として記録し、正負の定義は別に明記する |
| F-05 の指定位置 | [[Wall_Thickness]] | 対向する側面間を局所的に測る方法で3 mmと仮定 |
| F-03 | [[Undercut_(injection_molding)|Undercut]] | unknown。抜き勾配の値だけで、領域全体の干渉を判定しない |

## 一件の構造化記録

```yaml
part_id: DEMO-01
feature_id: F-02
concept_id: MC-002
concept: Counterbore
evidence_status: illustrative
geometry_ref: top/F-01/entrance
properties:
  diameter: {value: 10, unit: mm, status: assumed}
  depth: {value: 3, unit: mm, status: assumed}
relations:
  - {predicate: entrance_form_of, target_feature_id: F-01, status: assumed}
  - {predicate: coaxial_with, target_feature_id: F-01, status: assumed}
purpose: unknown
evidence:
  kind: author_created_scenario
  reference: this_note
```

## 設計目的を追加する場合

F-05 がリブだからといって「反り対策」とは記録しません。実際の図面・仕様・設計者の説明に目的があれば、F-05 serves_purpose reduce_warpage と記録し、根拠の実際の場所と stated を付けます。解析に基づく場合は analyzed、形だけから推測する場合は inferred とします。

## この構造でできる検索の例

- 「座ぐりのある穴」：MC-002 の特徴から entrance_form_of をたどり、主穴を取得する。
- 「半径2 mmのフィレットがあるポケット」：Fillet の半径と単位を確認し、boundary_of の対象を取得する。
- 「接続する冷却流路」：用途の根拠が確認できた Cooling Channel を探し、connects_to をたどる。
- 「反り対策のリブ」：Rib と serves_purpose、目的の根拠を合わせて探す。F-05 は目的が unknown なので、この条件では該当しない。

これは課題3のデータ項目と検索条件を考える例です。RAGや CAD 検索はまだ実装していません。実際の部品へ適用する際は、仮定を実測・図面・設計情報に置き換えます。
