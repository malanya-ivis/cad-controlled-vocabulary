---
aliases: []
category: shape_feature
status: draft
scope_role: core
concept_kind: geometric_feature
minimum_use_evidence: "A passage opening and its boundary in CAD, a section, or an equivalent geometry record; record through/blind/unknown and do not count an entrance enlargement as a second passage."
concept_id: MC-001
label_ja: "穴"
label_ja_status: project_candidate
knowledge_group: "[[Shape_Features]]"
concept_relations:
  - predicate: geometry_may_support_role
    target: "[[Cooling_Channel]]"
---

# Hole

## Use condition (draft)

- **Concept kind:** `geometric_feature`.
- **Minimum evidence for a part occurrence:** A passage opening and its boundary in CAD, a section, or an equivalent geometry record; record through/blind/unknown and do not count an entrance enlargement as a second passage.
- If this evidence is missing, record a candidate observation or `unknown`; do not assert the concept as verified.

## Definition and scope

[Project scope / source-supported draft] A localized opening in a part, described by the resulting geometry rather than by the CAD command that created it. A similar opening can be built through different feature histories. Counterbore and Countersink describe distinct local forms at a hole entrance; through/blind status is normally recorded as a property.

## Broader concept

Not established. `Through` and `blind` are being treated as possible attributes or combinations, not automatically as independent feature notes.

## Related or distinguished concepts

- [[Counterbore]] and [[Countersink]]: source-documented hole-end forms with different resulting geometry.
- [[Cooling_Channel]]: distinguished by function. A cooling channel may be geometrically hole-like, but a Hole label alone does not establish a mold cooling circuit.
- [[Cavity_(injection_molding)|Cavity]]: distinguished by domain and role; the Autodesk source describes Cavity as an injection-molding region/space, not a generic opening.
- Cylindrical surface: a candidate geometric-primitive distinction, not a link yet because no separate concept note has been established. A cylindrical surface can occur in a Hole without being the structural feature itself.
- Drilling: a candidate operation distinction; the current source set does not justify creating a concept note yet.

## Shape description and relations

**Project recording proposal, based on the supporting sources below.** These are description rules for the draft vocabulary; they are not automatic recognition algorithms or new standard definitions.

| Item | Record |
|---|---|
| Identification cues | Opening, termination and shape of the passage; record a circular axis only if that geometry exists. |
| Occurrence attributes | Diameter or cross-section; depth; through/blind/unknown; opening and terminal regions. |
| Knowledge group | [[Shape_Features]] |
| Worked example | [[Single_Part_Description_Example]] |

Illustrative wording: A blind hole opens on the top face; its entrance has a separately identified Counterbore. Any numbers in this wording are examples, not design recommendations.

Concept links in `concept_relations` state the association type. Actual feature locations and connections use the instance relations in [[Feature_Relations]], with feature IDs and evidence.

## Observed STL example

[[CAD_Counterbore_Example]] and [[CAD_Countersink_Example]] show measured passages and separate entrance forms. These examples are mesh observations with draft vocabulary mappings; physical units and mold-design roles are not established.

## Supporting sources

- [[PTC_Creo_Recognized_Features]] — opening list of recognized features and rule for holes passing through a part; checked on 2026-10-05.
- [[PTC_Creo_Hole_Feature_JA]] — opening description, hole types, and comparison with a cut feature; checked on 2026-10-05.
- [[Onshape_Hole]] — Hole command versus Extrude-Remove, types, end conditions, and callout behavior; checked on 2026-10-05.
- [[NIST_Feature_Recognition_Manufacturability]] — Hole in manufacturing-feature recognition context; selected sections read, 2026-10-05.
- [[NIST_Feature_Based_Machining_STEP]] — AP 224 machining-feature context; selected sections read, 2026-10-05.

## Open questions

- Compare geometry-based bounds with JIS drawing terminology and a sample part.
- Confirm whether through/blind should be attributes and how they are recorded.
- Confirm the Japanese preferred label after the scoped meaning is reviewed.

## STLの適用例

[[CAD_1400_Hole_Relations]]。形に基づく草案です。用途・物理単位は未確認です。
