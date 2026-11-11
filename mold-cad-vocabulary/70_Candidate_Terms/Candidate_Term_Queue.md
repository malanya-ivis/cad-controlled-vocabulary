# Candidate Term Queue

**Purpose:** Keep plausible terms visible until their shape boundary, source support, or granularity is settled. New terms are expected over time; follow the repeatable addition process in [[Feature_Description_Rules]]. A queue entry is not yet a checked concept.

## Near-term single-part shape candidates

| Candidate | Source evidence | Current question |
|---|---|---|
| Spotface | [[Onshape_Hole]], [[PTC_Creo_Hole_Feature_JA]], [[Autodesk_Inventor_2026_Hole_JA]] | Is its shallow flat seating surface distinct enough from counterbore for this vocabulary? |
| Through / blind; diameter; depth | [[Onshape_Hole]], [[PTC_Creo_Hole_Feature_JA]] | Keep as properties/end conditions unless a source and task need a separate concept. |
| Overall form and geometric surfaces | Current CAD sources and [[CAD_Feature_and_Operation_Boundaries]] | Add only if the sample needs a distinction between whole-part form, a surface primitive, and a local feature. |
| Shell | [[Onshape_Shell]], [[Autodesk_Inventor_2026_Placed_Features_JA]] | Separate Shell operation, wall-thickness property, and resulting internal void. |
| Warpage-reduction purpose | [[JEED_Design_Training_D3]], future part drawing/specification or analysis | Record as a purpose relation on a particular feature occurrence only when its evidence is stated; do not infer it from the presence of a Rib. |
| Flatness / 平面度 | [[Nagumo_Press_Mold_Glossary]], [[ISO_1101_Geometrical_Tolerancing_Record]] | Candidate geometrical specification; confirm the definition, notation, and applicable standard before adding a concept. The ISO record is catalog/abstract only. |
| Surface roughness / Ra / Rz | [[Nagumo_Press_Mold_Glossary]], [[ISO_21920_2_Surface_Texture_Record]] | Candidate surface-texture properties; confirm measurement definitions and decide whether surface quality is within scope. Do not adopt the source's stated Ra/Rz ratio. ISO 21920-2 is being revised, so recheck its edition before detailed work. |
| Knock hole / ノック穴 | [[Nagumo_Press_Mold_Glossary]], [[Hole]] | A hole described by the pin it receives; decide whether this is a Hole subtype, a functional attribute, or a hole-to-pin relation. |

## Press-source boundary terms

[[Nagumo_Press_Mold_Glossary]] also records press/die clearance, press-bending methods, sheared surfaces, and press-frame opening. Keep these as source-specific context unless a single-part sample shows how a term describes part geometry or a documented feature relation.

## Context terms retained from the earlier mold-component study

Existing notes on mold bases, cores, ejectors, guides, feed systems, gate types, and machine interfaces remain useful source context. They are not the active single-part feature list. Reconsider one only when its geometry is needed to describe a part or its relation can be tied to a specific feature occurrence.

Examples: [[Mold_Base]], [[Core_(mold_component)]], [[Ejector_Plate]], [[Runner_(injection_molding)]], [[Gate_(injection_molding)]], [[Locating_Ring]], [[Parting_Line_(injection_molding)]].

## Queue rule

Before creating a note, compare the proposed term against existing concepts, subtypes, properties, and source-specific operations. Record the intended category and intended scope. If sufficient evidence exists for a bounded draft, create it in `30_Concepts/`; retain the open boundary question in that note and update [[Concept_Overview]] and [[Decision_Log]].

## 2026-10-07：Excelの他分野資料からの候補

| 候補 | 資料と確認場所 | 今回の扱い・必要なこと |
|---|---|---|
| 鋳抜き穴 | [[Yamaha_Casting_Glossary_Scope_Check]]、あ行 | 形はHole、鋳造で作ることは作り方の属性候補。工程根拠が必要 |
| ドロービード | [[AutoForm_Press_Glossary_Scope_Check]]、個別記事 | 機能を持つプレス特徴候補。形と材料流入調整の用途を分け、Ribとの同義関係を作らない |
| 面ひずみ | 同資料、個別記事 | 状態・解析結果の候補。基準形状と実形状の比較根拠が必要 |

[[Cross_Mold_Domain_Transfer]]で追加理由と範囲を比較しました。三候補は新しいコア概念として採用していません。
