---
aliases: []
category: shape_property
scope_role: core
concept_kind: direction_dependent_geometric_property
minimum_use_evidence: "Identify the surface, pull/reference direction and coordinate frame, angle, convention, and measurement source. Without a stated or analyzed direction, record angle/slant only and leave draft status unconfirmed."
status: draft
concept_id: MC-010
label_ja: "抜き勾配"
label_ja_status: project_candidate
knowledge_group: "[[Shape_Properties]]"
concept_relations:
  - predicate: compared_with
    target: "[[Undercut_(injection_molding)]]"
---

# Draft Angle

## Use condition (draft)

- **Concept kind:** `direction_dependent_geometric_property`.
- **Minimum evidence for a part occurrence:** Identify the surface, pull/reference direction and coordinate frame, angle, convention, and measurement source. Without a stated or analyzed direction, record angle/slant only and leave draft status unconfirmed.
- If this evidence is missing, record a candidate observation or `unknown`; do not assert the concept as verified.

## Definition and scope

[Source-supported draft] The angle of a part face or local surface relative to a defined mold-pull or release direction. The property is associated with release; its value and reference direction belong to a particular part/feature occurrence.

The Japanese sources use 抜き勾配 or 勾配. Keep this geometric/design property distinct from a CAD Draft command, which is one way to create tapered faces. Current term evidence is strongest for injection-mold examples; broader mold applicability remains to be checked.

Creo describes draft angle relative to the pull direction, usually the mold-opening direction; Onshape uses a neutral plane or pull direction as the command reference. Their definitions help identify the needed reference for a recorded value, but command settings and sign conventions remain software-specific.

## Broader concept

[[Wall_Thickness]] is another shape property, but neither is a kind of the other.

## Related or distinguished concepts

- [[Undercut_(injection_molding)|Undercut]]: both concern release, but draft angle is a face-orientation property and undercut is a directional geometric obstruction/condition.
- CAD Draft operation: a modeling command, not this property.

## Shape description and relations

**Project recording proposal, based on the supporting sources below.** These are description rules for the draft vocabulary; they are not automatic recognition algorithms or new standard definitions.

| Item | Record |
|---|---|
| Identification cues | A surface angle relative to the explicitly recorded pull/reference direction; use the source or measurement convention to interpret sign. |
| Occurrence attributes | Surface reference; direction and coordinate frame; value and unit; angle/sign convention. |
| Knowledge group | [[Shape_Properties]] |
| Worked example | [[Single_Part_Description_Example]] |

Illustrative wording: The specified pocket wall has 2° draft relative to +Z; record the face and convention, not just the number. Any numbers in this wording are examples, not design recommendations.

Concept links in `concept_relations` state the association type. Actual feature locations and connections use the instance relations in [[Feature_Relations]], with feature IDs and evidence.

## Supporting sources

- [[JEED_Design_Training_D3]] — 抜き勾配 described relative to the release direction.
- [[JEED_Plastic_Mold_Glossary_Index]] — selected Draft Angle entry; design-angle context.
- [[Autodesk_Inventor_2026_Placed_Features_JA]] — 勾配 as a placed-feature operation; command/property boundary.
- [[PTC_Creo_Draft_Feature]] — pull direction and the angle between that direction and drafted surfaces.
- [[Onshape_Draft]] — mold-removal context and neutral-plane / pull-direction command references.
- [[Onshape_Draft_Analysis]] — checks draft against a selected mold-split direction; analysis context only.
- [[SOLIDWORKS_2026_Draft_Analysis_JA]] — Japanese help requires an opening direction and reference angle for draft analysis; vendor analysis context, not a universal test.
- [[Autodesk_Inventor_2026_Rib_JA]] — the Rib command offers taper settings for rib and boss geometry; parameter context only.

## Open questions

- Specify the reference direction and sign convention for a recorded value.
- Check how the term is used beyond the current injection-mold sources.

## 鋳造分野での用例

[[Yamaha_Casting_Glossary_Scope_Check]]の「抜け勾配（抜き勾配）」を確認し、[[Cross_Mold_Domain_Transfer]]でJEEDの説明と比較しました。分野を越える用例候補ですが、表記の採用と個別部品の抜き方向は未確認です。[[Claim_Evidence_Matrix]]のCL-010を参照してください。
