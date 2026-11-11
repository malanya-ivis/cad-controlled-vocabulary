---
aliases: []
category: shape_property
scope_role: core
concept_kind: direction_dependent_geometric_condition
minimum_use_evidence: "Identify the candidate region and mold-pull/extraction direction, then cite a geometry-based release assessment. A recess or sloped face alone is insufficient; without direction or assessment, status is unknown."
status: draft
concept_id: MC-011
label_ja: "アンダーカット"
label_ja_status: project_candidate
knowledge_group: "[[Shape_Properties]]"
concept_relations:
  - predicate: compared_with
    target: "[[Draft_Angle]]"
---

# Undercut

## Use condition (draft)

- **Concept kind:** `direction_dependent_geometric_condition`.
- **Minimum evidence for a part occurrence:** Identify the candidate region and mold-pull/extraction direction, then cite a geometry-based release assessment. A recess or sloped face alone is insufficient; without direction or assessment, status is unknown.
- If this evidence is missing, record a candidate observation or `unknown`; do not assert the concept as verified.

## Definition and scope

[Source-supported draft / project scope] A part-shape condition that obstructs removal along a specified mold-pull or extraction direction unless the part deforms or the removal path changes. The boundary is directional: the same geometry may or may not be an undercut relative to a different direction.

The current direct source evidence is mainly injection-molding material. This note treats undercut as a single-part geometric/release condition, not as the slide, lifter, or other mechanism used to remove it, and not as a production release defect.

## Broader concept

Not established. Keep it as a shape property/condition until a broader moldability classification is supported.

## Related or distinguished concepts

- [[Draft_Angle]]: both relate to release; draft angle describes surface orientation, while undercut describes a directional obstruction.
- [[Slide_Core_(injection_molding)|Slide Core]]: a mechanism that can release some undercuts; not the part feature itself.
- release defect described in [[MISUMI_Plastic_Molding_108_Mold_Release]]: a production outcome, not a geometric condition.

## Shape description and relations

**Project recording proposal, based on the supporting sources below.** These are description rules for the draft vocabulary; they are not automatic recognition algorithms or new standard definitions.

| Item | Record |
|---|---|
| Identification cues | A release obstruction assessed for a stated direction and region. Minimum-draft failure alone does not establish this condition. |
| Occurrence attributes | Region; pull direction and frame; present/absent/unknown; assessment method and evidence. |
| Knowledge group | [[Shape_Properties]] |
| Worked example | [[Single_Part_Description_Example]] |

Illustrative wording: Undercut status is unknown when a surface angle is available but the relevant release obstruction has not been assessed. Any numbers in this wording are examples, not design recommendations.

Concept links in `concept_relations` state the association type. Actual feature locations and connections use the instance relations in [[Feature_Relations]], with feature IDs and evidence.

## Supporting sources

- [[JEED_Design_Training_D3]] — アンダーカット処理; ordinary opening/ejection may not release the shape.
- [[JEED_Plastic_Mold_Glossary_Index]] — product geometry that cannot release in the mold-opening direction without a changed shape or structure.
- [[Shibaura_Injection_Molding_Glossary]] — アンダーカット entry.
- [[MISUMI_Plastic_Molding_123_Removable_Insert]] — undercut examples and release routes; checked 2026-10-06.
- [[Onshape_Draft_Analysis]] — identifies undercut regions after the mold-split direction is selected; supports direction-dependent recording, not a universal analysis rule.

## Open questions

- Refine geometric criteria on a sample part and record the relevant pull direction.
- Check whether the same preferred scope transfers to other mold processes.

## 鋳造分野への適用候補

[[Yamaha_Casting_Glossary_Scope_Check]]にも、引き抜き方向によって取り出せない部分という用例があります。[[Cross_Mold_Domain_Transfer]]で射出成形の資料と比較しました。ファイル名は既存の調査履歴を残す名前であり、この比較だけで三分野の実物検証が済んだとはしません。[[Claim_Evidence_Matrix]]のCL-011を参照してください。
