---
aliases:
  - ゲート
category: context_only
status: draft
scope_role: context_only
---

# Gate (injection molding)

> Context only: retained from the earlier mold-component/process study; this note is outside the active single-part shape-feature set.


## Definition and scope

[Source-supported draft / injection-molding scope] A mold feed passage or entrance through which molten polymer enters a Cavity from the runner. Autodesk and JEED describe the flow connection and process context; JEED also lists gate types and separately defines Gate Seal (resin solidification in the gate) and Gate Seal Time (the duration until it solidifies). Those process terms are related to the Gate but are not its geometry. MISUMI discusses tunnel/submarine-gate separation during opening/ejection and an in-mold gate-cutting mechanism that rotates the gate region along a spiral path while the parting surface remains closed. The cutting unit/operation is not the Gate passage. These sources use `gate` in a mold-feed context, not as a generic mechanical gate or CAD command. `ゲート` is a same-version Autodesk source label.

## Broader concept

Not established. A broader feed-system concept has not yet been modeled.

## Related or distinguished concepts

- [[Runner_(injection_molding)|Runner]]: directly related upstream flow passage; the source distinguishes the runner system from the gate.
- [[Cavity_(injection_molding)|Cavity]]: directly related receiving region; a Gate is not the cavity space itself.
- [[Hole]]: distinguished by injection-flow function; a cylindrical opening alone is insufficient evidence for Gate.
- [[Runner_System_(injection_molding)|Runner System]]: a system-level feed structure that includes the sprue, runner(s), and gate(s) in the Autodesk glossary; an individual Gate is one part of that system.
- Gate-cutting unit: a separate mechanism can cut the gate region in the mold; it is not part of the Gate passage definition.

## Supporting sources

- [[Autodesk_Inventor_Mold_Glossary]] — English `Gate`, Japanese `ゲート`, and `Runner and Runner system` entries; checked on 2026-10-05.
- [[JEED_Design_Training_D3]] — ゲート as the entry from sprue/runner toward Cavity; checked on 2026-10-05.
- [[JEED_Design_Training_D4]] — gate shapes and design context; checked on 2026-10-05.
- [[JEED_Design_Training_D5]] — fill sequence through gate into Cavity; checked on 2026-10-05.
- [[JEED_Plastic_Mold_Glossary_Index]] — Gate as entry into Cavity from the sprue/runner route; the same entry discusses sealing/process roles; selected entry read 2026-10-05.
- [[JEED_Plastic_Mold_Glossary_Index]] — separate selected entry distinguishes Gate Seal from Gate Seal Time and records gate-type labels; selected text read 2026-10-06.
- [[MISUMI_Plastic_Molding_112_Tunnel_Gates]] — tunnel/submarine gate source labels and detachment context; checked on 2026-10-05.
- [[MISUMI_Plastic_Molding_124_In_Mold_Gate_Cutting]] — separates the Gate passage from a mechanism that cuts it inside the mold; checked on 2026-10-06.
- [[ISO_28238_Gating_System_Components_Record]] — catalog abstract identifies a gating-system component terminology standard; metadata only, not term-level evidence.

## Open questions

- Confirm whether gate, gate insert, gate mark, and tunnel/submarine variants need separate concepts in the selected domain; the paired MISUMI labels do not establish synonymy.
- Compare the source's Gate scope with a dedicated injection-mold design reference.
- Confirm the Japanese alias against an independent source before treating it as stable project terminology.
