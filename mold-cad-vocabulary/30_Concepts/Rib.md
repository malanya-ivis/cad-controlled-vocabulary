---
aliases: []
category: shape_feature
status: draft
scope_role: core
concept_kind: geometric_feature
minimum_use_evidence: "A thin, elongated wall-like projection joined to the part, supported by geometry; record reinforcement purpose only with separate design evidence."
concept_id: MC-006
label_ja: "リブ"
label_ja_status: project_candidate
knowledge_group: "[[Shape_Features]]"
concept_relations:
  - predicate: compared_with
    target: "[[Boss]]"
  - predicate: may_have_property
    target: "[[Wall_Thickness]]"
---

# Rib

## Use condition (draft)

- **Concept kind:** `geometric_feature`.
- **Minimum evidence for a part occurrence:** A thin, elongated wall-like projection joined to the part, supported by geometry; record reinforcement purpose only with separate design evidence.
- If this evidence is missing, record a candidate observation or `unknown`; do not assert the concept as verified.

## Definition and scope

[Project scope / source-supported draft] A thin, elongated wall-like projection joined to a part surface. Sources commonly describe it as a support or reinforcement, but the feature's purpose should be recorded separately on the part occurrence. The geometry is the vocabulary target; the Rib modeling command is a source context.

## Broader concept

Not established. The sources support feature recognition and a plastic-part use, but do not establish a project-wide broader concept.

## Related or distinguished concepts

- [[Boss]]: distinguish by the source-supported geometry and role: a rib is wall-like and elongated, while the current sources do not yet give a general Boss definition.

## Shape description and relations

**Project recording proposal, based on the supporting sources below.** These are description rules for the draft vocabulary; they are not automatic recognition algorithms or new standard definitions.

| Item | Record |
|---|---|
| Identification cues | Thin wall-like projection joined to a part surface; identify its extent and attachment region. Geometry does not establish a warpage-reduction purpose. |
| Occurrence attributes | Path / extent; thickness at specified locations; height; base surface; taper. |
| Knowledge group | [[Shape_Features]] |
| Worked example | [[Single_Part_Description_Example]] |

Illustrative wording: A Rib is located on the back face, with local thickness 3 mm; its design purpose remains unknown without design evidence. Any numbers in this wording are examples, not design recommendations.

Concept links in `concept_relations` state the association type. Actual feature locations and connections use the instance relations in [[Feature_Relations]], with feature IDs and evidence.

## Observed STL example

[[CAD_Cross_Rib_Example]] describes two direction-based rib regions and their intersection without recovering a CAD feature history. These examples are mesh observations with draft vocabulary mappings; physical units and mold-design roles are not established.

## Supporting sources

- [[PTC_Creo_Recognized_Features]] — opening list of recognized features and rib example; checked on 2026-10-05.
- [[Onshape_Rib]] — feature command and wider support-structure contexts; checked on 2026-10-05.
- [[JEED_Design_Training_D3]] — リブ as molded-product reinforcement; checked on 2026-10-05.
- [[JEED_Plastic_Mold_Glossary_Index]] — combined Rib/Boss entry distinguishes plate-like reinforcement from a rounded/cylindrical Boss; selected entry read 2026-10-05.
- [[PTC_Creo_Profile_Rib]] — describes a rib as a thin fin/web attached to part surfaces; strengthening and bending prevention are source-stated purposes, not automatic instance facts.
- [[Autodesk_Inventor_2026_Rib_JA]] — Japanese help distinguishes command options for リブ and ウェブ and shows a Boss tab on the Rib command; this is vendor terminology, not a project synonym rule.

## Open questions

- Compare Rib with web, wall, and stiffening-feature terminology using a part sample.
- Check whether Autodesk's リブ / ウェブ distinction is also used in drawing or other CAD vocabulary before assigning preferred terms.
- Record a reinforcement or warpage-reduction purpose only when a drawing, specification, designer statement, or analysis supports it.
- Confirm the preferred Japanese label after the shape scope is set.

## 他分野と新しい比較例

[[Yamaha_Casting_Glossary_Scope_Check]]の鋳物のリブを[[Cross_Mold_Domain_Transfer]]で比較しました。補強目的と資料内の直角条件は全例の必須条件にしません。[[CAD_Rib_Boss_Comparison]]に提供STLの単独リブを追加し、厚さ3 input_unitsを記録しました。[[Claim_Evidence_Matrix]]のCL-006で根拠の範囲を確認します。
