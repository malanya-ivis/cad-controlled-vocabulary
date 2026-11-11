---
category: relation_rules
status: draft
---
# 特徴の関係

リンクには「どのような関係か」を付けます。次の関係名は、本プロジェクトの記述案です。国際標準で定められた関係名として扱いません。

## 概念を整理する関係

| 関係名 | 使い方 | 例 |
|---|---|---|
| hole_entrance_form_of | 主穴と入口形状の関連。下位語という確定ではない | [[Counterbore]] → [[Hole]]、[[Countersink]] → [[Hole]] |
| compared_with | 違いを説明する概念同士の関連 | [[Pocket]] ↔ [[Slot]]、[[Rib]] ↔ [[Boss]]、[[Fillet]] ↔ [[Chamfer]] |
| may_have_property | ある特徴に付くことのある性質。全例に必須という意味ではない | [[Rib]] → [[Wall_Thickness]]、[[Pocket]] → [[Draft_Angle]] |
| may_describe | 性質から、記述対象になり得る特徴へたどる | [[Wall_Thickness]] → [[Rib]]、[[Internal_Void]] の周囲の材料 |
| geometry_may_support_role | 同じ形に用途を付ける可能性。用途の証明は別に必要 | [[Hole]] → [[Cooling_Channel]] |

各概念の YAML の concept_relations に、関係名と相手のノートを記録します。上位・下位を確定できない関係を is_a に置き換えません。

## 一つの部品上の特徴を結ぶ関係

| 関係名 | 向き・対象 | 判断する内容 |
|---|---|---|
| entrance_form_of | 入口形状 → 主穴 | どの穴の入口を構成するか |
| coaxial_with | 対称、特徴 ↔ 特徴 | 二つの円筒等の軸が一致するか。許容差や確認方法を記録 |
| boundary_of | 移行形状 → 主特徴 | フィレット・面取りがどの特徴の境界にあるか |
| located_on | 特徴 → 面・領域 | リブやボスがどの面にあるか。単なる位置関係 |
| opens_to | 空間・通路 → 面・領域 | 開口がどこにあるか |
| intersects | 対称、特徴 ↔ 特徴 | 確認範囲内で三次元の領域が重なるか。全体について false とする場合は全体検査が必要 |
| touches | 対称、特徴 ↔ 特徴 | 境界面が接するが、領域が重ならないか |
| connects_to | 対称、通路 ↔ 通路 | 通れる連続経路があるか。intersects や touches だけからは決めない |
| has_property | 特徴・領域 → 性質の記録 | 値、単位、測定位置、方向を対応させる |
| serves_purpose | 特徴 → 目的 | 反り対策などの設計意図を根拠と結ぶ |

同じ部品内の feature_id を対象にします。面は geometry_ref で指定します。対称関係は一度だけ保存してよく、検索時に逆方向もたどります。目的は stated、analyzed、inferred の種類を記録します。根拠がなければ目的を unknown にします。

例えば、F-02 entrance_form_of F-01 は座ぐりと主穴の関係です。F-02 coaxial_with F-01 は軸の関係です。二つは別の説明なので、一つの無名リンクにまとめません。

[[Feature_Description_Rules]] と [[Single_Part_Description_Example]] に記録方法があります。

実際の STL の関係例は [[CAD_Counterbore_Example]] の入口形状・同軸、[[CAD_Cross_Rib_Example]] の交差にあります。[[Simple_CAD_Feature_Records.json]] に、関係名と対象の特徴IDを保存しました。

## 接続しないことを確認した例

[[CAD_1400_Hole_Relations]] では選択断面と概略位置を確認していますが、全体の三次元交差検査は未実施です。そのため「選択断面では交差を確認できなかった」と記録し、全体の `intersects` は unknown のままにします。[[Final_Selected_Feature_Records.json]] でも観察と全体判定を分けます。
