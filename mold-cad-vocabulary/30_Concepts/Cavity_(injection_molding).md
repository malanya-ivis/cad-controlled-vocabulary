---
aliases: []
category: context_only
status: draft
scope_role: context_only
---

# Cavity (injection molding)

> Context only: retained from the earlier mold-component/process study; this note is outside the active single-part shape-feature set.


## Definition and scope

[Source-supported draft / injection-molding scope] In this note, the Cavity is the region or space in an injection mold occupied by melt to form the plastic part. Autodesk, MISUMI #029, and the JEED `金型構造` glossary entry use the space/region sense. JEED's separate `キャビティ部` glossary entry instead uses that label for the mold portion comprising both the Core (male) and Cavity (female) sides; JEED's design page and Shibaura also record the female-component sense. MISUMI discusses cavity/core as forming components that can be integral or split. This note currently selects the space sense and records JEED's own differing uses; it does not merge the female component, the combined `キャビティ部` assembly, an insert, or an arbitrary CAD recess into that concept.

## Broader concept

Not established. A broader mold-structure concept has not been selected for the first batch.

## Related or distinguished concepts

- [[Core_(mold_component)|Core]]: related complementary mold context, not an equivalence or broader/narrower relation in this note.
- [[Pocket]]: distinguished because the PTC source uses Pocket for a machining volume, while this source uses Cavity for an injection-molding region/space with a process role. Similar appearance is insufficient for merging.
- [[Cooling_Channel]]: related mold-function term; a cooling channel serves temperature control and is not the cavity space.
- [[Mold_Base]]: the supporting assembly houses mold-forming components; it is not the forming space.
- [[Mold_Insert_(injection_molding)|Mold Insert]]: a divided/fitted mold portion can form a Cavity surface, but is not the empty Cavity space.

## Supporting sources

- [[Autodesk_Inventor_Mold_Glossary]] — English `Cavity` entry; checked on 2026-10-05.
- [[JEED_Design_Training_D5]] — Cavity as the concave mold part and as part of the space formed with Core; checked on 2026-10-05.
- [[Shibaura_Injection_Molding_Glossary]] — キャビティ entry explicitly reports space and female-component uses; checked on 2026-10-05.
- [[MISUMI_Cavity_Core_Split_Structure]] — cavity/core forming components and integral/split construction; checked on 2026-10-05.
- [[MISUMI_Plastic_Molding_010_Cavity_Dimensions]] — cavity as a machined concave shape in a steel block, in dimensioning context; checked on 2026-10-05.
- [[MISUMI_Plastic_Molding_029_Burn_and_Gas_Venting]] — explicitly identifies the Cavity as the internal mold space into which melt flows; checked on 2026-10-05.
- [[JEED_Plastic_Mold_Glossary_Index]] — records both a combined Core+Cavity sense for `キャビティ部` and a product-shaped-space sense in the separate `金型構造` entry; selected entries read 2026-10-05 and 2026-10-06.

## Open questions

- Decide whether to create a separately qualified concept for the female Cavity component; do not merge it with the space sense without an explicit design decision.
- Confirm the standalone Japanese glossary correspondence for `Cavity`; the readable Japanese page uses キャビティ in surrounding entries but was not treated as a verified one-to-one entry in this pass.
- Current evidence is injection-molding-heavy; add supported examples from other mold types before making cross-domain claims.
