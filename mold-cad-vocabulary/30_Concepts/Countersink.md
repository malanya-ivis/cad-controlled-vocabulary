---
aliases: []
category: shape_feature
scope_role: core
concept_kind: local_entrance_form
minimum_use_evidence: "A conical enlargement at an identified Hole entrance; attach as that entrance form, not as a second through-passage."
status: draft
concept_id: MC-003
label_ja: "皿ざぐり"
label_ja_status: project_candidate
knowledge_group: "[[Shape_Features]]"
concept_relations:
  - predicate: hole_entrance_form_of
    target: "[[Hole]]"
  - predicate: compared_with
    target: "[[Counterbore]]"
---

# Countersink

## Use condition (draft)

- **Concept kind:** `local_entrance_form`.
- **Minimum evidence for a part occurrence:** A conical enlargement at an identified Hole entrance; attach as that entrance form, not as a second through-passage.
- If this evidence is missing, record a candidate observation or `unknown`; do not assert the concept as verified.

## Definition and scope

[Source-supported draft] A conical enlargement at the opening of a hole. The scope here is the resulting local geometry; CAD commands and countersink parameters are recorded separately.

Japanese source labels include 皿ざぐり / 皿穴. Confirm the exact drawing-term mapping before adding one as a project alias.

## Broader concept

A hole-end form associated with [[Hole]]. A formal broader relation awaits a reviewed project taxonomy.

## Related or distinguished concepts

- [[Counterbore]]: uses a cylindrical, flat-bottomed enlargement rather than this conical form.
- [[Hole]]: the enlargement modifies the opening; through/blind status remains a separate property.

## Shape description and relations

**Project recording proposal, based on the supporting sources below.** These are description rules for the draft vocabulary; they are not automatic recognition algorithms or new standard definitions.

| Item | Record |
|---|---|
| Identification cues | Conical enlargement at a hole entrance; distinguish this surface form from the cylindrical Counterbore. |
| Occurrence attributes | Entrance diameter; included cone angle and angle convention; main-hole feature ID; axis reference. |
| Knowledge group | [[Shape_Features]] |
| Worked example | [[Single_Part_Description_Example]] |

Illustrative wording: A hole entrance widens along a conical surface; record its included angle instead of assuming a standard angle. Any numbers in this wording are examples, not design recommendations.

Concept links in `concept_relations` state the association type. Actual feature locations and connections use the instance relations in [[Feature_Relations]], with feature IDs and evidence.

## Observed STL example

[[CAD_Countersink_Example]] shows a conical entrance and explicitly records the raw-mesh issue and approximate transition depth. These examples are mesh observations with draft vocabulary mappings; physical units and mold-design roles are not established.

## Supporting sources

- [[Onshape_Hole]] — distinguishes countersink from counterbore and simple hole styles.
- [[PTC_Creo_Hole_Feature_JA]] — Japanese Hole feature and listed hole types.
- [[Autodesk_Inventor_2026_Hole_JA]] — Japanese CAD command options; operation context.

## Open questions

- Check the geometric boundary and Japanese preferred term against JIS drawing terminology and a sample drawing.
- Decide whether the project records Countersink as a standalone feature type or a Hole subtype.
