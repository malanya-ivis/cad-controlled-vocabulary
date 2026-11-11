---
category: data_design
status: proposal
updated: 2026-10-07
---
# CAD形状・仕様・根拠の分け方

ウェブで確認したISOとNISTの資料から、課題3の検索記録に必要な区別を整理しました。規格本文の定義を移したものではなく、本プロジェクトのデータ設計案です。

## まず分ける三つの記録

| 記録するもの | 例 | 根拠 |
|---|---|---|
| 形状の概念 | Hole、Rib、Pocket | [[ISO_22432_Features_Record]]は、仕様・検証に使う幾何特徴の用語と種類を扱う。金型CAD全体の用語集ではない。 |
| 実際に観察した形 | STL上の穴らしい通路、面、エッジ | [[ISO_10303_42_Geometry_Record]]と[[NIST_STEP_BRep_and_Faceted_Geometry_Record]]。STLは三角形メッシュとして記録し、正確なCAD形状と同じ扱いにしない。 |
| 設計上の要求・検査値 | 平面度、公差、表面粗さ | [[ISO_1101_Geometrical_Tolerancing_Record]]、[[ISO_21920_2_Surface_Texture_Record]]。実測形状の値と設計要求を混ぜない。 |

用途も別にします。穴の形から「冷却用」と決めず、図面・設計説明・解析など、用途を示す根拠を特徴の記録に結びます。

## 課題3に向けた追加項目案

| 項目 | 記録例 | 役割 |
|---|---|---|
| `representation_kind` | `STL_mesh`, `STEP_B_rep`, `native_CAD` | どの種類の形状データを根拠にしたかを示す |
| `geometry_ref` | `face`, `edge`, `mesh_region` とモデル内の参照 | 部品上のどの場所についての説明かを示す |
| `claim_kind` | `observed_shape`, `design_feature`, `specification`, `purpose` | 観察・概念割当・設計要求・用途を分ける |
| `value_basis` | `measured`, `specified`, `nominal` | 実測値と図面・3D注記の要求値を分ける |
| `evidence_status` | `observed`, `candidate`, `confirmed`, `unknown` | 判断の確かさを回答に戻す |
| `model_revision` | ファイル名や版ID、SHA-256 | 根拠にしたモデル版を特定する |

寸法・肉厚には、単位、測定位置、方向、測定方法も付けます。幾何参照がモデル更新後も同じ面を指すかは別途確認し、単なる face 番号だけに依存しません。

## 今のデータに当てはめると

- 提供CADのSTL例は `representation_kind: STL_mesh` とし、形状の判断を「メッシュ上で観察した」と記録します。
- 断面で交差を見つけなかった結果は、全体を調べていない限り `intersects: false` にしません。現在の[[RAG_Search_Verification_Cases]]のQ13・Q19の扱いを保ちます。
- 平面度や粗さは形状名にせず、要求・性質の候補として扱います。ISO 21920-2の改訂状況も再確認してから定義を検討します。
- CAD上の特徴IDや公差注記が使えるSTEP・ネイティブCAD例が得られたら、STL記録とは別に試します。

参照：[[ISO_10303_42_Geometry_Record]]、[[ISO_22432_Features_Record]]、[[ISO_1101_Geometrical_Tolerancing_Record]]、[[ISO_21920_2_Surface_Texture_Record]]、[[NIST_STEP_BRep_and_Faceted_Geometry_Record]]。
