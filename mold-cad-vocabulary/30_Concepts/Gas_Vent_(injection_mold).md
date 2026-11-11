---
aliases: []
category: internal_structure
scope_role: core
concept_kind: functional_vent_path
minimum_use_evidence: "Record the groove/passage/clearance and separately cite design or process evidence establishing gas-escape use. A gap that could pass gas is not enough by itself."
status: draft
concept_id: MC-015
label_ja: "ガスベント"
label_ja_status: project_candidate
knowledge_group: "[[Internal_Structures]]"
concept_relations:
  - predicate: compared_with
    target: "[[Cooling_Channel]]"
---

# Gas Vent

## Use condition (draft)

- **Concept kind:** `functional_vent_path`.
- **Minimum evidence for a part occurrence:** Record the groove/passage/clearance and separately cite design or process evidence establishing gas-escape use. A gap that could pass gas is not enough by itself.
- If this evidence is missing, record a candidate observation or `unknown`; do not assert the concept as verified.

## Definition and scope

[Source-supported draft] A passage, groove, or designed clearance in a part that provides a route for gas to escape from a mold-filling region. The feature geometry can be described on one part; the venting role requires process or design evidence.

Current terminology evidence is from injection molding. A parting interface, an ejector pin, or a core-pin clearance is not automatically a Gas Vent merely because gas can pass there.

## Broader concept

Not established. Keep the passage/feature separate from the general venting function unless the vocabulary later models functions as distinct concepts.

## Related or distinguished concepts

- [[Internal_Void]]: a generic internal region without a specified gas-escape role.
- [[Cooling_Channel]]: may look like a passage but carries coolant for a different purpose.
- [[Parting_Line_(injection_molding)|Parting Line]]: an interface that can host a vent path but is not itself necessarily a vent.
- [[Ejector_Pin]]: clearance around a pin can contribute to venting; the component is not the vent feature by default.

## Shape description and relations

**Project recording proposal, based on the supporting sources below.** These are description rules for the draft vocabulary; they are not automatic recognition algorithms or new standard definitions.

| Item | Record |
|---|---|
| Identification cues | Groove, passage or designed clearance plus evidence of a gas-escape role; it may occur at a surface and need not be fully internal. |
| Occurrence attributes | Route; cross-section or clearance; endpoints; supporting surface; venting-role evidence. |
| Knowledge group | [[Internal_Structures]] |
| Worked example | [[Single_Part_Description_Example]] |

Illustrative wording: A shallow surface groove leads to an exterior edge; call it Gas Vent when design evidence establishes the gas-escape role. Any numbers in this wording are examples, not design recommendations.

Concept links in `concept_relations` state the association type. Actual feature locations and connections use the instance relations in [[Feature_Relations]], with feature IDs and evidence.

## Supporting sources

- [[JEED_Design_Training_D4]] — ガスベント route for air/gas escape during filling.
- [[JEED_Plastic_Mold_Glossary_Index]] — distinguishes venting from a gas-escape groove labeled Gas Vent.
- [[MISUMI_Plastic_Molding_029_Burn_and_Gas_Venting]] — describes core-pin clearance and vent/groove implementations.

## Open questions

- Separate gas vent, air vent, vent groove, and clearance only if source use and sample geometry require it.
- Compare an internal-section model with the source's functional description.
