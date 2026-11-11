---
category: dataset_study
status: mesh_based_draft
physical_unit: unknown
---
# STLを用語と関係で記述する

対象は `/home/malanya/projects/cad-structure-search/data/simple_CAD_dataset` の21個のSTLです。元ファイルのメッシュを読み、外形、頂点、断面を確認しました。これは実際にファイルを読み取った例です。[[Single_Part_Description_Example]] の仮定による教材とは別に管理します。このデータが実際の金型部品かどうかは未確認です。

![[dataset_overview.png]]

## 今回の四つの例

| 例 | 記述する知識 | ファイルから確認した内容 |
|---|---|---|
| [[CAD_Counterbore_Example]] | [[Hole]] と [[Counterbore]]、同軸、入口形状 | 主穴の径約6、入口の径約12、入口の深さ9 |
| [[CAD_Countersink_Example]] | [[Hole]] と [[Countersink]]、座ぐりとの差 | 円すい状の入口。原メッシュの退化面と寸法の不確かさも記録 |
| [[CAD_Rectangular_Pocket_Example]] | [[Pocket]] と [[Wall_Thickness]] | 20 × 14、深さ6。底下の局所厚さ9 |
| [[CAD_Cross_Rib_Example]] | [[Rib]] の特徴分けと交差関係 | 二方向の壁状領域。厚さ3、高さ10、中央で交差 |

## このように作る

1. **外観と断面を見る。** ファイル名から正解を決めず、材料のある領域と空いた領域を区別する。
2. **特徴を分ける。** 主穴、入口形状、ポケット、リブなどに部品内のIDを付ける。STLには元のCADフィーチャIDがないので、こちらで記述用のIDを付ける。
3. **用語を選ぶ。** 円筒形の入口と肩なら Counterbore、円すい状の入口なら Countersink の草案に対応させる。
4. **属性を測る。** 径、深さ、位置、方向と、その測り方を記録する。物理単位は unknown、座標値は input_units とする。
5. **関係を書く。** 座ぐり → 主穴、同軸、リブ同士の交差などを [[Feature_Relations]] の関係名で記録する。
6. **確認できないことを残す。** 冷却用途、反り対策、抜き方向、設計履歴は、このデータだけから確定しない。

## 課題3の検索に使う

[[Simple_CAD_Feature_Records.json]] に、四つの部品のID、概念ID、属性、関係、根拠を保存しました。例えば「深さ8以上の座ぐり」は、Counterbore のIDで特徴を探し、深さと単位を確認します。この四例では counterbore.stl の F-02 が深さ9で該当します。

「交差するリブ」は Rib と intersects、「底下の厚さ9のポケット」は Pocket と局所厚さの記録を使えます。これらは記録を使った検索条件の例です。データベースやRAG検索はまだ実装していません。

用途を含む「冷却用の穴」「反り対策のリブ」は、用途の資料がないため、この四例では確認済みの結果として返せません。

## 根拠とメッシュの範囲

実行したプログラムは [inspect_simple_cad_dataset.py](/home/malanya/projects/cad-controlled-vocabulary/tools/inspect_simple_cad_dataset.py) です。図はユーザーのSTLから生成しました。原ファイルは読み取りのみです。countersink.stl の16個の面積ゼロの面は、図と断面を作る作業用メッシュの中だけで除きました。

[[mesh_observations.json]] に全21件のファイルパス、SHA-256、外形、三角形数、作業用メッシュの状態、選んだ四例の頂点測定を記録しました。watertight の結果はメッシュの診断であり、実物の部品の正確さや自交差のない有効なCADソリッドを保証しません。

## 全ファイルの外形記録

以下は入力座標の単位です。名前は資料を見つけるための表示であり、用語の正解ラベルではありません。この表は2026-10-06の外形記録です。2026-10-07にrib・boss・fillet_bossの三例を[[Targeted_CAD_Gap_Examples]]で追加記述し、簡単なデータセットの詳細例は計七件になりました。

| ファイル | 外形 X × Y × Z | 元の三角形数 | 作業用図で除いた退化面 |
|---|---|---|---|
| boss.stl | 50 × 50 × 18 | 142 | 0 |
| bracket.stl | 80 × 50 × 15 | 436 | 0 |
| bracket_rot.stl | 79.7782 × 55.422 × 70.6916 | 436 | 0 |
| bracket_scaled.stl | 120 × 75 × 22.5 | 436 | 0 |
| chamfer.stl | 40 × 40 × 20 | 16 | 0 |
| concentric.stl | 50 × 50 × 24 | 400 | 0 |
| counterbore.stl | 50 × 50 × 20 | 272 | 0 |
| countersink.stl | 50 × 50 × 12 | 320 | 16 |
| dimple.stl | 40 × 40 × 15 | 2702 | 0 |
| fillet_boss.stl | 40 × 40 × 16 | 1422 | 0 |
| groove.stl | 50 × 40 × 15 | 28 | 0 |
| keyway.stl | 50 × 40 × 15 | 28 | 0 |
| plate.stl | 60 × 40 × 10 | 276 | 0 |
| rectpocket.stl | 50 × 50 × 15 | 28 | 0 |
| rib.stl | 50 × 50 × 18 | 28 | 0 |
| rib_cross.stl | 60 × 60 × 18 | 66 | 0 |
| slot.stl | 60 × 40 × 12 | 152 | 0 |
| slot_diag.stl | 60 × 60 × 12 | 152 | 0 |
| sphere.stl | 50 × 50 × 50 | 1280 | 0 |
| spotface.stl | 50 × 50 × 20 | 272 | 0 |
| step.stl | 60 × 40 × 20 | 24 | 0 |

## 2026-10-07の追加

[[CAD_Rib_Boss_Comparison]]は板状突起と円柱状突起の比較、[[CAD_Fillet_Boss_Name_Check]]は名前だけではFilletにできない例です。追加の値と根拠は[[Supplemental_Feature_Records.json]]に保存しました。[[RAG_Search_Verification_Cases]]で既存四例と一緒に記録検索を試せます。用途・単位・CAD履歴は引き続き未確認です。
