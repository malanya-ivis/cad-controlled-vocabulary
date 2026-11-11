---
aliases: []
category: shape_feature
status: draft
scope_role: core
concept_kind: geometric_feature
minimum_use_evidence: "A localized projection from a surrounding part surface, supported by geometry; do not infer fastening or reinforcement purpose from shape."
concept_id: MC-007
label_ja: "ボス"
label_ja_status: project_candidate
knowledge_group: "[[Shape_Features]]"
concept_relations:
  - predicate: compared_with
    target: "[[Rib]]"
---

# Boss

## Use condition (draft)

- **Concept kind:** `geometric_feature`.
- **Minimum evidence for a part occurrence:** A localized projection from a surrounding part surface, supported by geometry; do not infer fastening or reinforcement purpose from shape.
- If this evidence is missing, record a candidate observation or `unknown`; do not assert the concept as verified.

## Definition and scope

[Project scope / source-supported draft] A localized projection from a surrounding part surface. Mold-design sources often describe rounded or cylindrical bosses as reinforcement, but this concept note describes the shape; a reinforcing or fastening purpose belongs on a feature occurrence with evidence.

## Broader concept

Not established. The current sources support a feature label and a machining context, not a complete hierarchy.

## Related or distinguished concepts

- [[Rib]]: distinguish a candidate localized boss from the source-supported long, thin, wall-like Rib; the Boss boundary still needs an independent definition.
- [[Pocket]]: related in the Creo machining context because a pocket floor may contain protruding bosses (islands). This is not a broader/narrower relation.

## Shape description and relations

**Project recording proposal, based on the supporting sources below.** These are description rules for the draft vocabulary; they are not automatic recognition algorithms or new standard definitions.

| Item | Record |
|---|---|
| Identification cues | Localized projection from a surrounding surface; describe whether its geometry is cylindrical or another form instead of imposing a universal cylinder rule. |
| Occurrence attributes | Base surface; height; footprint / diameter if applicable; any independently identified hole. |
| Knowledge group | [[Shape_Features]] |
| Worked example | [[Single_Part_Description_Example]] |

Illustrative wording: A cylindrical Boss projects from a pocket floor; a Hole may occur in it, but fastening purpose needs separate evidence. Any numbers in this wording are examples, not design recommendations.

Concept links in `concept_relations` state the association type. Actual feature locations and connections use the instance relations in [[Feature_Relations]], with feature IDs and evidence.

## Supporting sources

- [[PTC_Creo_Recognized_Features]] — opening list of recognized features; checked on 2026-10-05.
- [[PTC_Creo_Machining_Features]] — `Pocket`, `Boss Top`, and island wording in the feature list; checked on 2026-10-05.
- [[Autodesk_Fusion_2D_Pocket_JA]] — “area around a boss” as a CAM operation target; not a geometry definition; checked on 2026-10-05.
- [[NIST_Feature_Based_Machining_STEP]] — boss feature class in AP 224 machining context; selected sections read, 2026-10-05.
- [[JEED_Plastic_Mold_Glossary_Index]] — combined リブ・ボス entry distinguishes Boss from plate-like Rib; selected entry read 2026-10-05.
- [[Autodesk_Inventor_2026_Rib_JA]] — a Boss option adds boss geometry at selected sketch points in the Inventor Rib command; command-specific relation only, not a standalone shape definition.

## Open questions

- Compare boss shape boundaries with a representative part and an independent shape reference.
- Keep the shape term distinct from machining Boss Top/island usage and from a CAD Boss command.
- Confirm the preferred Japanese label after reviewing the scoped meaning.

## 提供STLでの比較と定義の不足

[[CAD_Rib_Boss_Comparison]]に円柱状突起の比較例を追加しました。JEEDの開いた円柱状の例より、このプロジェクトの「局所的な突起」という案は広い範囲です。実例ができても一般定義の根拠が十分になったわけではありません。[[Claim_Evidence_Matrix]]のCL-007に不足を残しました。
