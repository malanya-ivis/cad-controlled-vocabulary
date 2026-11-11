---
aliases: []
category: shape_feature
scope_role: core
concept_kind: local_entrance_form
minimum_use_evidence: "A cylindrical enlargement and flat shoulder at an identified Hole entrance; attach as that entrance form, not as a second through-passage."
status: draft
concept_id: MC-002
label_ja: "座ぐり"
label_ja_status: project_candidate
knowledge_group: "[[Shape_Features]]"
concept_relations:
  - predicate: hole_entrance_form_of
    target: "[[Hole]]"
  - predicate: compared_with
    target: "[[Countersink]]"
---

# Counterbore

## Use condition (draft)

- **Concept kind:** `local_entrance_form`.
- **Minimum evidence for a part occurrence:** A cylindrical enlargement and flat shoulder at an identified Hole entrance; attach as that entrance form, not as a second through-passage.
- If this evidence is missing, record a candidate observation or `unknown`; do not assert the concept as verified.

## Definition and scope

[Source-supported draft] A cylindrical, flat-bottomed enlargement at the opening of a hole. The scope here is the resulting local geometry; the hole feature command and its parameter set are separate source contexts.

Japanese source labels include 座ぐり. Confirm the exact drawing-term mapping before adding it as a project alias.

## Broader concept

A hole-end form associated with [[Hole]]. A formal broader relation awaits a reviewed project taxonomy.

## Related or distinguished concepts

- [[Countersink]]: uses a conical enlargement rather than this cylindrical, flat-bottomed form.
- [[Hole]]: the enlargement modifies the opening; through/blind status remains a separate property.

## Shape description and relations

**Project recording proposal, based on the supporting sources below.** These are description rules for the draft vocabulary; they are not automatic recognition algorithms or new standard definitions.

| Item | Record |
|---|---|
| Identification cues | Cylindrical enlargement at a hole entrance, with an annular shoulder / flat-bottom region. Compare the entrance and main-hole geometry. |
| Occurrence attributes | Entrance diameter and depth; shoulder region; main-hole feature ID; axis reference. |
| Knowledge group | [[Shape_Features]] |
| Worked example | [[Single_Part_Description_Example]] |

Illustrative wording: An entrance enlargement has a cylindrical wall and shoulder; link it to the main Hole using entrance_form_of. Any numbers in this wording are examples, not design recommendations.

Concept links in `concept_relations` state the association type. Actual feature locations and connections use the instance relations in [[Feature_Relations]], with feature IDs and evidence.

## Observed STL example

[[CAD_Counterbore_Example]] measures the upper enlargement and records entrance_form_of and coaxial_with. These examples are mesh observations with draft vocabulary mappings; physical units and mold-design roles are not established.

## Supporting sources

- [[Onshape_Hole]] — distinguishes counterbore from countersink and simple hole styles.
- [[PTC_Creo_Hole_Feature_JA]] — Japanese Hole feature and listed hole types.
- [[Autodesk_Inventor_2026_Hole_JA]] — Japanese CAD command options; operation context.

## Open questions

- Check the geometric boundary and Japanese preferred term against JIS drawing terminology and a sample drawing.
- Decide whether the project records Counterbore as a standalone feature type or a Hole subtype.
