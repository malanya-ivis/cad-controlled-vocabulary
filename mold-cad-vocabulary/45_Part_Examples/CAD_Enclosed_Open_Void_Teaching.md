---
category: part_example
status: synthetic_teaching_geometry
updated: 2026-10-07
---
# 閉じた空洞と、上に開いた空間を比べる

これは今回作った二つの教材モデルです。実際の金型部品ではありません。[[Internal_Void]]の開閉状態と、特徴を二重に数えないルールを確かめるために作りました。一般的な用語定義や製造のしやすさを証明するモデルではありません。

![[teaching_enclosed_void_views.png]]

![[teaching_open_void_views.png]]

## 作った形と確認できること

外形はどちらも(0,0,0)から(20,20,20)までです。格子状に分けた領域のうち、材料を置く領域の境界面をすべて作成しました。数値は教材のinput_unitsで、mm等の物理単位は設定していません。

| 項目 | TEACH-enclosed／F01 | TEACH-open／F01 |
|---|---|---|
| 材料がない領域 | (4,4,4)～(16,16,16) | (4,4,4)～(16,16,20)、上端が外部へ開口 |
| 閉じ方 | 六方向を材料で囲む | +Z方向へ開く |
| 記録する属性 | enclosure=enclosed | enclosure=open_to_exterior、opening_direction=+Z |
| 概念の対応案 | [[Internal_Void]] MC-013 | [[Pocket]] MC-004の形状と、Internal Void MC-013の空間という二つの説明 |
| 特徴の数 | 1 | 1。二つの概念を付けても、同じ領域を二つに数えない |
| STL材料境界のwatertight | true | true |
| 境界の連結成分 | 2（外側と内側） | 1 |
| 材料の体積 | 20³−12³=6272 | 20³−12×12×16=5696 |

この教材の開閉状態は、選択断面だけで決めたものではありません。すべての材料領域と境界を作る手順から確認できます。外部へ開くモデルでも、材料の境界メッシュはwatertightになります。watertightという値だけでは、内部空間が外部へ開いているか決まりません。

`enclosure`の幾何条件には作成根拠がありますが、Internal Voidという名称の範囲とPocketとの関係はプロジェクト草案です。[[Claim_Evidence_Matrix]]のCL-013に定義上の不足を残します。

## 実際のSTLとの区別

[[CAD_4423_Open_Void]]はユーザー提供モデルの開口例です。今回の二モデルは、作成条件が分かる教材例です。検索記録には`origin: synthetic_teaching_model`を付け、通常の提供モデル検索から除きます。教材を使うQ11・Q12だけ明示的に含めます。[[RAG_Search_Verification_Cases]]を参照してください。

提供された93モデルの閉じた空洞候補の確認は、[[Targeted_CAD_Gap_Examples]]にあります。教材ができても、実際の金型部品の閉鎖空洞例が確認済みになったわけではありません。

## ファイルと再作成

- 教材STL：[[teaching_enclosed_void.stl]]、[[teaching_open_void.stl]]。
- 作成条件、SHA-256、メッシュ体積、断面：[[supplement_mesh_observations.json]]。
- 特徴・概念・開閉状態：[[Supplemental_Feature_Records.json]]。
- スクリプト：`tools/inspect_vocabulary_supplement.py`。既存の元CADは変更しません。
