# Medical Subject Headings (MeSH)

**Study status:** Structure example identified by the supervisor; the NLM introduction was reviewed selectively.

## Purpose and scope

MeSH is a controlled vocabulary produced by the U.S. National Library of Medicine for indexing, cataloging, and searching biomedical and health-related information. Its descriptors are organized hierarchically so users can browse from broad to specific subjects, while entry terms help different expressions reach the relevant descriptor. This purpose is retrieval and subject access, not direct geometric description.

## Development and maintenance

| Item | Confirmed method | Source and location | Open question |
|---|---|---|---|
| Candidate collection | The vocabulary evolves with terminology used in biomedical literature and with emerging concepts. The introduction says new descriptor proposals are considered against existing descriptors and qualifiers. | [[NLM_MeSH_Introduction]] — Prefatory Remarks; Changes to MeSH Terminology | The detailed proposal form and committee workflow were not read. |
| Inclusion / merging / splitting | A new descriptor is not needed when existing descriptors and qualifiers already characterize the literature precisely; unnecessary proliferation is avoided. The source also describes descriptors being changed or deleted, but does not provide a CAD-like merge checklist. | [[NLM_MeSH_Introduction]] — Changes to MeSH Terminology | Exact criteria for splitting one existing descriptor into several were not found in this pass. |
| Preferred labels / definitions | The usual practice is to adopt an expression commonly used by English-language authors. A descriptor record contains concepts and synonymous terms, with a preferred concept/term structure. | [[NLM_MeSH_Introduction]] — Prefatory Remarks; Concept Structure in MeSH | The project needs to decide how much of the record-level concept structure is useful in Markdown. |
| Relations / classification | Sixteen broad categories and branching tree structures organize descriptors; a descriptor can appear in multiple tree locations. Concepts group strictly synonymous terms inside a record. | [[NLM_MeSH_Introduction]] — MeSH Tree Structures; Concept Structure in MeSH | Multiple placements may be more complexity than the first CAD batch can maintain. |
| Checking / updating | Subject specialists continually update the vocabulary; descriptors and qualifiers are released annually, supplementary records are updated on a continuing schedule, and changes include additions, modifications, deletions, replacements, and hierarchy adjustments. | [[NLM_MeSH_Introduction]] — Prefatory Remarks; Changes to MeSH Terminology | The internal review roles and evidence thresholds remain unconfirmed. |

## Application to mold CAD

- What to adopt and why: keep a preferred label distinct from confirmed alternate expressions; compare a proposed term against existing concepts before creating another note; record broader/narrower evidence and maintain a visible change history.
- What not to adopt directly and why: do not copy MeSH's biomedical category tree, annual release process, or descriptor/qualifier record model into a small CAD research vault.
- Compare MeSH concept/entry-term organization with the classification structure in [[ICD-10]]. Neither system supplies the CAD feature taxonomy.
- Limits of this investigation: only the NLM introduction pages listed in the source note were read; this is a method summary, not a full MeSH data-model study.

## Supporting source

- [[NLM_MeSH_Introduction]]

