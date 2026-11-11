---
aliases: []
category: internal_structure
scope_role: core
concept_kind: empty_geometric_region
minimum_use_evidence: "Show the material-free region using CAD or section evidence and record enclosed/open/unknown plus openings and known connections. This draft includes an internally located region that opens to the exterior; openness is an attribute, not a separate meaning."
status: draft
concept_id: MC-013
label_ja: "内部空洞"
label_ja_status: project_candidate
knowledge_group: "[[Internal_Structures]]"
concept_relations:
  - predicate: compared_with
    target: "[[Cooling_Channel]]"
---

# Internal Void

## Use condition (draft)

- **Concept kind:** `empty_geometric_region`.
- **Minimum evidence for a part occurrence:** Show the material-free region using CAD or section evidence and record enclosed/open/unknown plus openings and known connections. This draft includes an internally located region that opens to the exterior; openness is an attribute, not a separate meaning.
- If this evidence is missing, record a candidate observation or `unknown`; do not assert the concept as verified.

## Definition and scope

[Project proposal / not yet checked across systems] A volume inside a single part from which material is absent, whether fully enclosed or connected to the exterior through an opening or narrow passage. The occurrence should be supported by native CAD geometry, a section, or equivalent evidence.

This is a geometric description of the part. It is not the injection-molding Cavity, which names the resin-forming space between mold surfaces, and it is not the CAD Shell operation that may create a hollow result.

## Broader concept

Not established. Whether enclosed voids and open internal cavities need separate concepts is unresolved.

## Related or distinguished concepts

- [[Hole]]: an opening through or into material; an internal void may be enclosed and have no direct exterior opening.
- [[Cooling_Channel]]: a functionally named internal passage; geometry alone does not establish cooling purpose.
- [[Cavity_(injection_molding)|Cavity]]: a process/mold-space sense, not the empty region within a single solid part.
- [[Wall_Thickness]]: material thickness between relevant surfaces around a void.

## Shape description and relations

**Project recording proposal, based on the supporting sources below.** These are description rules for the draft vocabulary; they are not automatic recognition algorithms or new standard definitions.

| Item | Record |
|---|---|
| Identification cues | Material-free interior region established by CAD or section evidence. State whether it is enclosed or has openings and which regions it connects to. |
| Occurrence attributes | Region reference; enclosed/open/unknown; opening locations; neighboring material surfaces; connectivity. |
| Knowledge group | [[Internal_Structures]] |
| Worked example | [[Single_Part_Description_Example]] |

Illustrative wording: A section shows an enclosed Internal Void; no cooling or venting purpose is assigned from that geometry alone. Any numbers in this wording are examples, not design recommendations.

Concept links in `concept_relations` state the association type. Actual feature locations and connections use the instance relations in [[Feature_Relations]], with feature IDs and evidence.

## Supporting sources

- [[Onshape_Shell]] — describes a CAD operation that leaves hollow geometry; supports the need to distinguish resulting void from command, not a complete generic definition.
- [[Autodesk_Inventor_2026_Placed_Features_JA]] — Shell operation and hollow result context.
- [[PTC_Creo_Shell_Feature]] — describes both an enclosed hollow result and results opened by removing selected surfaces; operation example only.

## Open questions

- Compare a neutral geometry reference and decide whether “internal void,” “cavity,” or another term is preferred.
- Define enclosure and connectivity boundaries using a representative part sample.

## STLの適用例

[[CAD_4423_Open_Void]]、[[CAD_7145_Fillet_and_Internal_Structure]]。形に基づく草案です。用途・物理単位は未確認です。

## 開閉状態を確かめる教材

[[CAD_Enclosed_Open_Void_Teaching]]に、すべての材料領域を作った閉鎖空洞と開口空間を用意しました。開閉の幾何条件を確認する教材で、一般名称や実金型の妥当性を証明するものではありません。[[Claim_Evidence_Matrix]]のCL-013に、Excel内資料の今回確認範囲には中立的な一般定義が見つかっていないことを残しました。実物の候補確認は[[Targeted_CAD_Gap_Examples]]です。
