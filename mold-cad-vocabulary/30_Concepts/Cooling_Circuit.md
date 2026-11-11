---
aliases: []
category: context_only
status: draft
scope_role: context_only
---

# Cooling Circuit

> Context only: retained from the earlier mold-component/process study; this note is outside the active single-part shape-feature set.


## Definition and scope

[Source-supported draft / injection-molding scope] A mold-internal route for water or oil used in temperature control. Autodesk describes individual Cooling Channels connected in serial or parallel circuits, and JEED D4 uses 冷却回路 in a system-design context; however, JEED's selected glossary entry describes it simply as an internal water/oil passage without specifying topology. JEED separately identifies a temperature-control unit as external equipment that pumps conditioned fluid through the mold. This note keeps the connected-circuit reading as a project draft and records the single-passage wording as unresolved source scope.

## Broader concept

Not established. A broader mold temperature-control system could include more than the circuit described here.

## Related or distinguished concepts

- [[Cooling_Channel]]: an individual passage; a circuit is the connected system formed by one or more such passages.
- [[Runner_(injection_molding)|Runner]]: both may be connected channels within a mold, but they carry different media and serve different functions.
- [[Gas_Vent_(injection_mold)|Gas Vent]]: a passage for escaping air/gas rather than circulating coolant.

## Supporting sources

- [[Autodesk_Inventor_Mold_Glossary]] — Cooling channel entry, which describes channel connections as serial or parallel circuits; checked 2026-10-05.
- [[JEED_Design_Training_D4]] — 冷却回路 section; checked 2026-10-05.
- [[JEED_Plastic_Mold_Glossary_Index]] — 冷却回路 entry describes an internal water/oil route without specifying connected topology; selected entry read 2026-10-05.
- [[JEED_Plastic_Mold_Glossary_Index]] — 金型温度調節機 entry distinguishes external circulating equipment from the mold-internal route; selected entry read 2026-10-06.

## Open questions

- Confirm whether “cooling circuit” means one mold passage, a connected circuit of passages, or a broader loop including external hoses. Keep the temperature-control unit outside this concept unless the system boundary is expanded.
- Validate 冷却回路 as the preferred Japanese label before adding an alias.
