---
aliases: []
category: shape_feature
status: draft
scope_role: core
concept_kind: geometric_feature
minimum_use_evidence: "A planar beveled transition visible in the resulting geometry; a mesh may support a bevel candidate but not a specific CAD command."
concept_id: MC-009
label_ja: "面取り"
label_ja_status: project_candidate
knowledge_group: "[[Shape_Features]]"
concept_relations:
  - predicate: compared_with
    target: "[[Fillet]]"
---

# Chamfer

## Use condition (draft)

- **Concept kind:** `geometric_feature`.
- **Minimum evidence for a part occurrence:** A planar beveled transition visible in the resulting geometry; a mesh may support a bevel candidate but not a specific CAD command.
- If this evidence is missing, record a candidate observation or `unknown`; do not assert the concept as verified.

## Definition and scope

[Project scope / source-supported draft] A beveled transition at a part edge, formed by replacing or truncating a sharp corner with a slanted face. CAD Chamfer commands and machining labels are recorded separately from this resulting geometry.

## Broader concept

Not established. A broader edge-treatment concept is not required until an independent source supports it.

## Related or distinguished concepts

- [[Fillet]]: distinguished in the current source set because Chamfer uses a bevel/new surface while Fillet rounds or blends an edge; neither is treated as an alias of the other.
- [[Pocket]]: the Creo machining source uses `Top Chamfer` as a machining feature type, but that operation context is not a subtype of the general Pocket concept.

## Shape description and relations

**Project recording proposal, based on the supporting sources below.** These are description rules for the draft vocabulary; they are not automatic recognition algorithms or new standard definitions.

| Item | Record |
|---|---|
| Identification cues | Beveled transition at an edge; record the transition face and adjacent geometry. Do not infer a deburring purpose from its shape. |
| Occurrence attributes | Boundary references; host feature ID; distance / angle convention; extent. |
| Knowledge group | [[Shape_Features]] |
| Worked example | [[Single_Part_Description_Example]] |

Illustrative wording: A Chamfer runs along a specified external edge; its distance and angle reference are recorded separately. Any numbers in this wording are examples, not design recommendations.

Concept links in `concept_relations` state the association type. Actual feature locations and connections use the instance relations in [[Feature_Relations]], with feature IDs and evidence.

## Supporting sources

- [[Onshape_Chamfer]] — page title, feature description, steps, and measurement options; checked on 2026-10-05.
- [[PTC_Creo_Machining_Features]] — `Top Chamfer` in the machining feature list; checked on 2026-10-05.
- [[Autodesk_Inventor_2026_Placed_Features_JA]] — chamfer as a placed feature with modeling options; checked on 2026-10-05.
- [[NIST_Feature_Based_Machining_STEP]] — chamfer in the AP 224 machining-feature context; selected sections read, 2026-10-05.

## Open questions

- Compare edge, corner, and face-chamfer cases in a sample part.
- Determine whether bevel is a confirmed alternate label or a related term.
- Confirm the preferred Japanese label after the shape boundary is reviewed.

## STLの適用例

[[Shape_Comparison_Examples]]。形に基づく草案です。用途・物理単位は未確認です。
