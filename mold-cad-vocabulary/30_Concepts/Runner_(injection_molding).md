---
aliases:
  - ランナー
category: context_only
status: draft
scope_role: context_only
---

# Runner (injection molding)

> Context only: retained from the earlier mold-component/process study; this note is outside the active single-part shape-feature set.


## Definition and scope

[Source-supported draft / injection-molding scope] This note selects an individual channel carrying melt from the sprue toward a gate. Autodesk, JEED D4/D5, MISUMI, and Shibaura support a flow-passage use; MISUMI discusses cross-section and location choices. The JEED glossary's `ランナー` entry describes a broader route from machine nozzle toward the Cavity region, while Shibaura records both passage and solidified-resin senses. JEED separately uses Runner Diameter and Runner Balance for passage-size and flow-balance design concerns; these are attributes/optimization topics, not separate passage concepts. Autodesk separately names a `Runner system`. Keep those source extents visible: `ランナー` is a same-version Autodesk label for the scoped passage, not an alias for the system-level or residue senses.

## Broader concept

Not established. The distinction between a single Runner and the complete runner system remains a design decision.

## Related or distinguished concepts

- [[Gate_(injection_molding)|Gate]]: directly related downstream passage from runner to cavity.
- [[Cavity_(injection_molding)|Cavity]]: related destination region; a runner feeds the cavity but does not form the part region itself.
- [[Cooling_Channel]]: distinguished by the transported medium and function; a shared passage-like shape is not enough to merge them.
- [[Runner_System_(injection_molding)|Runner System]]: related whole-system concept; Autodesk includes sprue, runner(s), and gate(s) in its system description.

## Supporting sources

- [[Autodesk_Inventor_Mold_Glossary]] — English `Runner and Runner system`, `Sprue`, and related Japanese `ランナー` entries; checked on 2026-10-05.
- [[JEED_Design_Training_D4]] — runner as a melt-distribution path; checked on 2026-10-05.
- [[JEED_Design_Training_D5]] — flow order from sprue through runner and gate into Cavity; checked on 2026-10-05.
- [[Shibaura_Injection_Molding_Glossary]] — ランナ passage and solidified-material senses; checked on 2026-10-05.
- [[MISUMI_Plastic_Molding_052_Runner_Cross_Section]] — runner flow path and text discussion of location/cross-section choices; figures not inspected; checked on 2026-10-05.
- [[JEED_Plastic_Mold_Glossary_Index]] — selected `ランナー` entry gives a broader nozzle-to-Cavity route than MISUMI/Shibaura's individual segment; selected entry read 2026-10-05.
- [[JEED_Plastic_Mold_Glossary_Index]] — separate selected entries treat Runner Diameter and Runner Balance as passage-design attributes; checked 2026-10-06.
- [[ISO_28238_Gating_System_Components_Record]] — catalog-level lead for gating-system component terminology; no individual terms extracted.

## Open questions

- Decide whether the solidified-resin sense needs a separate concept; retain it as a source-specific use until then.
- Resolve whether JEED's wider use is a genuine scope difference or a simplified teaching description before harmonizing the preferred definition.
- Confirm the Japanese label and the single-versus-system distinction with an independent mold-design source.
- Current evidence is injection-molding-heavy; add supported examples from other mold types before making cross-domain claims.
