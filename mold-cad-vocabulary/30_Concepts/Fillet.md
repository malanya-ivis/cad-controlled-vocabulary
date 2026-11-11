---
aliases: []
category: shape_feature
status: draft
scope_role: core
concept_kind: geometric_feature
minimum_use_evidence: "A curved transition visible in the resulting geometry; a mesh may support a rounded-transition candidate but not a specific CAD command or exact radius."
concept_id: MC-008
label_ja: "フィレット"
label_ja_status: project_candidate
knowledge_group: "[[Shape_Features]]"
concept_relations:
  - predicate: compared_with
    target: "[[Chamfer]]"
---

# Fillet

## Use condition (draft)

- **Concept kind:** `geometric_feature`.
- **Minimum evidence for a part occurrence:** A curved transition visible in the resulting geometry; a mesh may support a rounded-transition candidate but not a specific CAD command or exact radius.
- If this evidence is missing, record a candidate observation or `unknown`; do not assert the concept as verified.

## Definition and scope

[Project scope / source-supported draft] A rounded transition between part faces or along an edge that replaces a sharp corner. CAD Fillet commands, radius options, and machining-feature labels are source contexts, not the definition of the resulting geometry.

## Broader concept

Not established. A broader edge-treatment concept is not required until an independent source supports it.

## Related or distinguished concepts

- [[Chamfer]]: distinguished in the current source set because Fillet rounds or blends while Chamfer creates a bevel/new surface; they are not aliases.
- [[Pocket]]: the Creo machining source uses `Top Round` as a machining feature type, but this operation context is not a subtype of the general Pocket concept.

## Shape description and relations

**Project recording proposal, based on the supporting sources below.** These are description rules for the draft vocabulary; they are not automatic recognition algorithms or new standard definitions.

| Item | Record |
|---|---|
| Identification cues | Rounded transition between the referenced faces / edges. Describe concave or convex form and constant or variable radius only when supported. |
| Occurrence attributes | Boundary references; host feature ID; radius where applicable; extent. |
| Knowledge group | [[Shape_Features]] |
| Worked example | [[Single_Part_Description_Example]] |

Illustrative wording: A Fillet forms the boundary between a Pocket floor and wall; boundary_of identifies that Pocket. Any numbers in this wording are examples, not design recommendations.

Concept links in `concept_relations` state the association type. Actual feature locations and connections use the instance relations in [[Feature_Relations]], with feature IDs and evidence.

## Supporting sources

- [[Onshape_Fillet]] — page title, feature description, steps, and fillet variants; checked on 2026-10-05.
- [[PTC_Creo_Machining_Features]] — `Top Round` in the machining feature list; checked on 2026-10-05.
- [[Autodesk_Inventor_2026_Placed_Features_JA]] — fillet as a placed feature with modeling options; checked on 2026-10-05.
- [[SOLIDWORKS_Fillet_Overview_2025_JA]] — official indexed Japanese description and listed operation variants reviewed 2026-10-06; direct page body did not render.
- [[NIST_Feature_Based_Machining_STEP]] — fillet in the AP 224 machining-feature context; selected sections read, 2026-10-05.

## Open questions

- Compare concave and convex edge transitions in a sample part and a second shape reference.
- Decide whether full-round forms are subtypes or separate geometry.
- Confirm the preferred Japanese label after the shape boundary is reviewed.

## STLの適用例

[[CAD_7145_Fillet_and_Internal_Structure]]。形に基づく草案です。用途・物理単位は未確認です。

## 名前だけで決められない例

[[CAD_Fillet_Boss_Name_Check]]の環状凸部は、ファイル名にfilletがあっても、この概念の確定した割当にはしていません。[[Claim_Evidence_Matrix]]のCL-008と[[RAG_Search_Verification_Cases]]のQ10で、丸い形・候補・対応根拠を確認します。
