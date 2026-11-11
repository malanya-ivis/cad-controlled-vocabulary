---
aliases:
  - 冷却管
category: internal_structure
scope_role: core
concept_kind: functional_internal_path
minimum_use_evidence: "Record passage geometry and separately cite a drawing, CAD metadata, specification, or designer statement establishing cooling-medium use. Geometry alone supports only a generic passage/hole/void description."
status: draft
concept_id: MC-014
label_ja: "冷却管"
label_ja_status: source_supported
knowledge_group: "[[Internal_Structures]]"
concept_relations:
  - predicate: compared_with
    target: "[[Gas_Vent_(injection_mold)]]"
---

# Cooling Channel

## Use condition (draft)

- **Concept kind:** `functional_internal_path`.
- **Minimum evidence for a part occurrence:** Record passage geometry and separately cite a drawing, CAD metadata, specification, or designer statement establishing cooling-medium use. Geometry alone supports only a generic passage/hole/void description.
- If this evidence is missing, record a candidate observation or `unknown`; do not assert the concept as verified.

## Definition and scope

[Source-supported draft] An internal passage in a part designed to carry cooling medium. For a specific occurrence, record the geometry and the evidence that establishes the cooling role; a cylindrical hole or void alone does not prove that function.

Current evidence is centered on injection molds. Keep one passage distinct from [[Cooling_Circuit]], which describes a connected route or system and may span more than one part. The alias 冷却管 is supported by the same-version Autodesk glossary; other Japanese labels remain candidates.

## Broader concept

Not established. This note classifies an internal functional structure, not an assembly or external temperature-control unit.

## Related or distinguished concepts

- [[Hole]]: a channel may be hole-like, but cooling function requires design evidence.
- [[Internal_Void]]: generic internal geometry without an asserted cooling purpose.
- [[Cooling_Circuit]]: circuit/system level rather than one passage.
- [[Gas_Vent_(injection_mold)|Gas Vent]]: a passage for gas escape rather than coolant flow.

## Shape description and relations

**Project recording proposal, based on the supporting sources below.** These are description rules for the draft vocabulary; they are not automatic recognition algorithms or new standard definitions.

| Item | Record |
|---|---|
| Identification cues | Passage geometry plus evidence of a cooling-medium role. A cylindrical passage can also have a Hole shape label under the same feature ID. |
| Occurrence attributes | Path; cross-section; ports; connections; cooling-role evidence; geometry reference. |
| Knowledge group | [[Internal_Structures]] |
| Worked example | [[Single_Part_Description_Example]] |

Illustrative wording: Two confirmed cooling passages connect inside one part; record connects_to only after the internal connection is established. Any numbers in this wording are examples, not design recommendations.

Concept links in `concept_relations` state the association type. Actual feature locations and connections use the instance relations in [[Feature_Relations]], with feature IDs and evidence.

## Supporting sources

- [[Autodesk_Inventor_Mold_Glossary]] — individual Cooling Channel and Japanese 冷却管 entries.
- [[JEED_Design_Training_D4]] — cooling-circuit context; supports a distinction between path and system, not the individual channel label.

## Open questions

- Check the scope on a single-part sample and compare drilled and conformal passages if both occur.
- Distinguish function documented in CAD metadata from function inferred from shape.
