---
aliases: []
category: shape_feature
status: draft
scope_role: core
concept_kind: geometric_feature
minimum_use_evidence: "An elongated groove or opening with its path, end shape, floor, and termination visible in geometry; keep uncertain boundaries marked candidate."
concept_id: MC-005
label_ja: "スロット"
label_ja_status: project_candidate
knowledge_group: "[[Shape_Features]]"
concept_relations:
  - predicate: compared_with
    target: "[[Pocket]]"
---

# Slot

## Use condition (draft)

- **Concept kind:** `geometric_feature`.
- **Minimum evidence for a part occurrence:** An elongated groove or opening with its path, end shape, floor, and termination visible in geometry; keep uncertain boundaries marked candidate.
- If this evidence is missing, record a candidate observation or `unknown`; do not assert the concept as verified.

## Definition and scope

[Project scope / source-supported draft] An elongated groove or opening in a part. The cited machining reference specifies a floor, surrounding walls, and rounded ends; treat those as source-specific criteria until a shape-level boundary is checked against a part sample.

Onshape's Sketch Slot command can create a 2D slot profile around straight or curved sketch curves and sets its width with a diameter dimension. This is additional evidence for a CAD sketch operation and profile, not a general definition of a three-dimensional slot feature.

## Broader concept

Not established. A broader elongated-recess concept has not been supported by the current sources.

## Related or distinguished concepts

- [[Pocket]]: distinguished by the source-supported elongated geometry and rounded ends of Slot; Pocket is described as a closed machining volume without that specific shape condition.
- [[Rib]]: distinguish a recessed/removed elongated feature from a wall-like reinforcing feature; the distinction needs another source if both are to be used in the same model vocabulary.

## Shape description and relations

**Project recording proposal, based on the supporting sources below.** These are description rules for the draft vocabulary; they are not automatic recognition algorithms or new standard definitions.

| Item | Record |
|---|---|
| Identification cues | Elongated recessed or open region; describe a straight or curved path, ends, and floor before assigning a type. No universal length/width threshold is adopted. |
| Occurrence attributes | Path; length and width; depth; end shape; through/blind/unknown. |
| Knowledge group | [[Shape_Features]] |
| Worked example | [[Single_Part_Description_Example]] |

Illustrative wording: A curved Slot follows a stated path with a stated width; rounded ends are recorded when present, rather than assumed from the name. Any numbers in this wording are examples, not design recommendations.

Concept links in `concept_relations` state the association type. Actual feature locations and connections use the instance relations in [[Feature_Relations]], with feature IDs and evidence.

## Supporting sources

- [[PTC_Creo_Recognized_Features]] — opening list, slot example, and recognition conditions; checked on 2026-10-05.
- [[PTC_Creo_Machining_Features]] — `Slot` and `Through Slot` definitions in the machining feature list; checked on 2026-10-05.
- [[NIST_Feature_Recognition_Manufacturability]] — Slot in machining-feature recognition context; selected sections read, 2026-10-05.
- [[NIST_Feature_Based_Machining_STEP]] — AP 224 machining-feature context; selected sections read, 2026-10-05.
- [[Onshape_Slot_Sketch]] — slot sketch profile can follow selected straight or curved sketch curves; width is a command dimension, not a 3D feature definition.

## Open questions

- Compare an elongated recess and a through slot in a sample part.
- Decide whether end shape and through/blind status are defining criteria or instance properties.
- Confirm the preferred Japanese label after the shape scope is set.

## STLの適用例

[[CAD_8972_Slot_and_Recesses]]。形に基づく草案です。用途・物理単位は未確認です。
