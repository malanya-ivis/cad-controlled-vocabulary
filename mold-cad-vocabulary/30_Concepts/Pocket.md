---
aliases: []
category: shape_feature
status: draft
scope_role: core
concept_kind: geometric_feature
minimum_use_evidence: "A recessed region with a floor and bounding wall(s); if the floor is partial or open, record that state and the section/geometry evidence."
concept_id: MC-004
label_ja: "ポケット"
label_ja_status: project_candidate
knowledge_group: "[[Shape_Features]]"
concept_relations:
  - predicate: compared_with
    target: "[[Slot]]"
  - predicate: may_have_property
    target: "[[Draft_Angle]]"
---

# Pocket

## Use condition (draft)

- **Concept kind:** `geometric_feature`.
- **Minimum evidence for a part occurrence:** A recessed region with a floor and bounding wall(s); if the floor is partial or open, record that state and the section/geometry evidence.
- If this evidence is missing, record a candidate observation or `unknown`; do not assert the concept as verified.

## Definition and scope

[Project scope / source-supported draft] A recessed region of a part with a floor and one or more bounding walls. This note names the resulting shape. Creo's closed machining-feature definition, Fusion's 2D Pocket toolpath, and CAD removal commands are source-specific contexts and do not by themselves define every recess.

## Broader concept

Not established. A broader subtraction-feature concept has not been supported by the current sources.

## Related or distinguished concepts

- [[Cavity_(injection_molding)|Cavity]]: distinguished by context and function. the cited Creo Pocket use is a machining volume, while the scoped Cavity is an injection-molding region/space; similar concavity is not enough to merge them.
- [[Slot]]: distinguished in the same Creo page by Slot's elongated volume and full radii on two opposite ends.
- [[Boss]]: related in the machining context because a Pocket floor may contain a protruding boss/island; this is not a hierarchy relation.

## Shape description and relations

**Project recording proposal, based on the supporting sources below.** These are description rules for the draft vocabulary; they are not automatic recognition algorithms or new standard definitions.

| Item | Record |
|---|---|
| Identification cues | Recess with a floor and bounding walls; record open sides and distinguish source-specific Through Pocket use. |
| Occurrence attributes | Extent; floor and wall references; depth; open sides; boundary transitions. |
| Knowledge group | [[Shape_Features]] |
| Worked example | [[Single_Part_Description_Example]] |

Illustrative wording: A top-face Pocket has a floor 8 mm below the opening; a Fillet forms part of its floor-to-wall boundary. Any numbers in this wording are examples, not design recommendations.

Concept links in `concept_relations` state the association type. Actual feature locations and connections use the instance relations in [[Feature_Relations]], with feature IDs and evidence.

## Observed STL example

[[CAD_Rectangular_Pocket_Example]] locates the floor and walls and measures length, width and depth from STL coordinates. These examples are mesh observations with draft vocabulary mappings; physical units and mold-design roles are not established.

## Supporting sources

- [[PTC_Creo_Recognized_Features]] — `pockets` listed as recognized features; checked on 2026-10-05.
- [[PTC_Creo_Machining_Features]] — `Pocket` and `Through Pocket` definitions in the machining feature list; checked on 2026-10-05.
- [[Autodesk_Fusion_2D_Pocket_JA]] — 2D Pocket as CAM toolpath operation; checked on 2026-10-05.
- [[Onshape_Extrude]] — extrude command can remove material; operation/result boundary context; checked on 2026-10-05.
- [[NIST_Feature_Recognition_Manufacturability]] — Pocket as a machining-feature interpretation; selected sections read, 2026-10-05.

## Open questions

- Use a sample part to define how open recesses, through pockets, and enclosed pockets are distinguished.
- Decide which observed boundaries belong in the definition versus instance properties.
- Confirm the preferred Japanese label against drawing terminology.

## STLの適用例

[[CAD_4423_Open_Void]]、[[CAD_8972_Slot_and_Recesses]]。形に基づく草案です。用途・物理単位は未確認です。
