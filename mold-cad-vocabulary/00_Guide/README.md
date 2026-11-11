# Mold CAD Controlled Vocabulary

This independent Obsidian vault records source usage and draft concepts for a software-independent vocabulary of features and shape properties **within a single mold-CAD part**. The initial vault structure followed the v4 project plan, but the scope was revised after the supervisor's clarification on 2026-10-06; see [[Scope_Revision_2026-10-06]] and the current [[Design_Policy]].

## Current state

- **Knowledge structure:** [[Knowledge_Structure]] connects four organizing/rule notes, the fifteen core concepts, and [[Single_Part_Description_Example]]. Each core concept now has an ID, a candidate Japanese label, typed concept links, identification cues, and occurrence attributes.

- **Concept notes:** 37 total; all remain `draft`. Fifteen are in the active single-part pilot: nine shape features, three shape properties, and three internal-structure concepts. Twenty-two earlier mold-component, assembly, process, and interface notes remain marked `context_only`.
- **Core examples:** Hole, Counterbore, Countersink, Pocket, Slot, Rib, Boss, Fillet, Chamfer; Draft Angle, Undercut, Wall Thickness; Internal Void, Cooling Channel, Gas Vent.
- **Source inventory:** 74 source notes with mixed reading status. See [[Source_Coverage_and_Gaps]] before treating an entry as term-level evidence.
- **Methods and technical references:** ANSI/NISO Z39.19 and ISO 25964 for controlled-vocabulary method; MeSH and ICD-10 as structure examples; STEP AP 224 and JIS Z 8114 for feature/manufacturing and Japanese drawing terminology. [[Controlled_Vocabulary_Governance]] now compares purpose and the process confirmed from each source; unread standards remain explicitly limited to catalog/abstract evidence.
- **Domain:** the intended scope is mold CAD generally. Existing mold examples lean toward injection molding as a practical pilot, not a permanent domain restriction. No CAD vendor defines the scope.
- **STL application:** [[Simple_CAD_Dataset_Study]] records 21 simple meshes and four detailed cases. [[Final_Selected_Dataset_Study]] adds 93 complex mesh previews and four detailed cases, with sections, structured feature records and [[Shape_Comparison_Examples]]. Physical units, mold use and design intent are unknown.
- **2026-10-07 additions:** [[Cross_Mold_Domain_Transfer]] compares selected Excel-listed sources; [[Claim_Evidence_Matrix]] documents evidence limits for all fifteen core drafts. [[Targeted_CAD_Gap_Examples]] adds three supplied-model records and two explicitly synthetic teaching models, plus a shell-candidate screen of the 93 complex meshes. The detailed supplied-model total is eleven. [[RAG_Search_Verification_Cases]] contains nineteen locally checked record-filter cases; this is preparation for task 3, not CAD recognition or an implemented DB/RAG.
- **Visual assets:** `80_Assets/cad_examples/` and `80_Assets/final_selected/` contain mesh overviews, section figures and measured geometry JSON generated from user-provided STL files. No vendor-source image or standards PDF was copied.
- **Obsidian:** no community plugins are enabled. Use the built-in Bases view or Markdown links.

## Folder map

| Folder | Purpose |
|---|---|
| `00_Guide/` | Scope, description rules, concept overview, candidate terms, and method synthesis |
| `10_Vocabulary_Studies/` | Controlled-vocabulary and classification examples with reading status |
| `20_Sources/` | One source/access note per CAD, technical, or methods reference |
| `30_Concepts/` | Active feature/property drafts and context-only terminology notes |
| `35_Knowledge_Structure/` | Shape groups, cross-concept distinctions, properties, and explicit relation rules |
| `40_Comparative_Studies/` | Cross-source boundaries and governance synthesis |
| `45_Part_Examples/` | Eleven detailed supplied-model records, two synthetic teaching records, dataset guides, search cases and a separate illustrative scenario |
| `50_Reference_Registers/` | Source coverage and standards discovery records |
| `60_Research_Records/` | Dated research batches and decision log |
| `70_Candidate_Terms/` | Unresolved feature terms and next candidates |
| `80_Assets/` | Asset register; no source files copied in this batch |
| `90_Templates/` | Source, concept, and vocabulary-study templates |

## Start here

1. Open `mold-cad-vocabulary` as an Obsidian vault.
2. Open [[Knowledge_Structure]] and [[Knowledge_Structure.canvas]], then read [[Simple_CAD_Dataset_Study]] and [[Final_Selected_Dataset_Study]]. [[Single_Part_Description_Example]] is the separate hypothetical teaching scenario.
3. Use [[Concept_Index.base]] to view active drafts separately from context notes.
4. Read the linked source note before using a concept definition; catalog-only evidence is not a term definition.
5. Read [[Design_Policy]] and [[Feature_Description_Rules]]; keep a concept's status `draft` until reviewed. Japanese `label_ja` values are candidates unless marked source-supported; they do not automatically become aliases.

## Evidence conventions

- Source notes state what was actually read, where, when, and what was saved. “Catalog/abstract only” is not equivalent to reading the standard.
- A source's label is usage evidence, not automatic proof of a system-independent concept.
- `draft` means the concept or its cross-source boundary still needs review; it does not mean teacher approval or industry certification.
- CAD feature commands, final geometry, machining features, functions, shape properties, and feature-instance relations are recorded as separate layers unless evidence supports a precise mapping.
- Internal geometry requires suitable evidence such as native CAD, a drawing, or section view. Do not infer absence or purpose from an exterior image alone.
- ISO 12165 remains subject to the project restriction: do not submit its content to AI. JDMIA's member-only terminology search was not accessed.

## Current decisions and open work

- Assembly hierarchy and part-to-assembly membership are not the target; this vocabulary describes features on one part.
- CAD software is not a scope boundary. Software help is collected to understand vendor labels and operations.
- The initial list may be incomplete. Add terms using the repeatable process in [[Feature_Description_Rules]] and queue unresolved terms in [[Candidate_Term_Queue]].
- A feature's design purpose (for example, a rib intended to reduce warpage) must be attached to an instance with evidence and marked stated, analyzed, or inferred.
- A first comparison of method references and candidate practices is recorded in [[Controlled_Vocabulary_Governance]]. Read authorized full-text clauses before making detailed claims or claiming compliance.

## Research record

- [[Batch_B_2026-10-05]] records earlier source additions and reading scope.
- [[Decision_Log]] records category, scope, and evidence-handling decisions, including the 2026-10-06 revision.
- [[Batch_F_2026-10-07]] records the four additions, Excel provenance and verification boundaries. Start with its four linked outputs to review this batch.
- [[Batch_G_2026-10-07]] records the web-checked geometry-representation and specification supplement. It adds five source notes and one task-3 data-design note; standards are catalog-only.
- [[CAD_Geometry_Representation_and_Evidence]] summarizes a web-checked supplement on STEP geometry, mesh evidence, geometrical specifications, and task-3 data fields. The linked ISO records are catalog/abstract only; NIST article text was read.
- [[Knowledge_Structure.canvas]] is the current single-part knowledge map. [[CAD_Structure_Term_Map.canvas]] is an earlier prototype.
