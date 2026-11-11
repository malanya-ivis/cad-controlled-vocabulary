---
aliases: []
category: shape_property
scope_role: core
concept_kind: geometric_property
minimum_use_evidence: "Identify the part/material being measured, the two opposing surfaces, location, measurement direction/method, value, and unit. Label a local sample measurement as local; do not call it minimum or nominal without a scan/specification."
status: draft
concept_id: MC-012
label_ja: "肉厚"
label_ja_status: project_candidate
knowledge_group: "[[Shape_Properties]]"
concept_relations:
  - predicate: may_describe
    target: "[[Rib]]"
  - predicate: may_describe
    target: "[[Internal_Void]]"
---

# Wall Thickness

## Use condition (draft)

- **Concept kind:** `geometric_property`.
- **Minimum evidence for a part occurrence:** Identify the part/material being measured, the two opposing surfaces, location, measurement direction/method, value, and unit. Label a local sample measurement as local; do not call it minimum or nominal without a scan/specification.
- If this evidence is missing, record a candidate observation or `unknown`; do not assert the concept as verified.

## Definition and scope

[Project definition / source-supported candidate] Local material thickness of a part, measured between the relevant opposing surfaces. Record the value, unit, and measurement location on a part-feature occurrence; thickness may vary across a part.

This note means the wall thickness of the modeled part. MISUMI #010 also discusses the thickness of mold steel surrounding a cavity; that is a different object and must not be merged with molded-part wall thickness. A Shell command parameter is likewise not automatically a description of the finished part.

## Broader concept

Not established. Thickness is a geometric property, not a separate solid feature.

## Related or distinguished concepts

- [[Rib]]: a rib reinforces a product while sources discuss keeping nominal wall thickness low; this relation does not imply a universal ratio.
- [[Internal_Void]]: opposing surfaces may bound an internal void, but wall thickness is the material between them.
- [[Draft_Angle]]: a separate geometric property.

## Shape description and relations

**Project recording proposal, based on the supporting sources below.** These are description rules for the draft vocabulary; they are not automatic recognition algorithms or new standard definitions.

| Item | Record |
|---|---|
| Identification cues | Material thickness at a specified location between the selected opposing surfaces; identify whether the material belongs to the mold part or molded product. |
| Occurrence attributes | Material/object being measured; paired surfaces; location; value/unit; local/nominal/minimum qualifier; method. |
| Knowledge group | [[Shape_Properties]] |
| Worked example | [[Single_Part_Description_Example]] |

Illustrative wording: Record local thickness between two specified surfaces around an Internal Void; do not substitute the Shell command setting for a measurement. Any numbers in this wording are examples, not design recommendations.

Concept links in `concept_relations` state the association type. Actual feature locations and connections use the instance relations in [[Feature_Relations]], with feature IDs and evidence.

## Observed STL example

[[CAD_Rectangular_Pocket_Example]] records the local material thickness below the floor, including opposing planes and measurement direction. These examples are mesh observations with draft vocabulary mappings; physical units and mold-design roles are not established.

## Supporting sources

- [[JEED_Design_Training_D3]] — Rib/reinforcement discussion refers to nominal wall thickness of the molded product.
- [[MISUMI_Plastic_Molding_010_Cavity_Dimensions]] — wall thickness of mold steel around a cavity; used here as a boundary example, not as the definition of part wall thickness.
- [[Onshape_Shell]] — selected wall thickness is a Shell-command parameter; operation/result boundary only.
- [[PTC_Creo_Shell_Feature]] — shell thickness may differ on selected faces; this supports recording local variation but remains a CAD-command example.

## Open questions

- Compare a direct part-design or drawing source that defines nominal and local wall thickness.
- Decide how to record variable thickness and the surfaces/measurement method for a sample part.

## STLの適用例

[[CAD_4423_Open_Void]]。形に基づく草案です。用途・物理単位は未確認です。

## 鋳造分野の用法と測定の範囲

[[Yamaha_Casting_Glossary_Scope_Check]]の肉厚は、部品の断面の厚さを説明します。この短い用語説明だけでは、最小肉厚のアルゴリズムや測定方向は決まりません。[[Claim_Evidence_Matrix]]のCL-012と[[RAG_Search_Verification_Cases]]のQ14で、局所値・単位の根拠を確認します。
