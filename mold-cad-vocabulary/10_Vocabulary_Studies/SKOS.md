# SKOS (Simple Knowledge Organization System)

**Study status:** Representation-model reference; not a domain vocabulary and not counted as one of the three provisional vocabulary cases.

## Purpose and scope

SKOS is a W3C model for representing knowledge-organization systems such as thesauri and classification schemes. It separates abstract concepts from their lexical labels, supports multilingual preferred and alternative labels, and provides broader/narrower, related, documentation, and concept-scheme constructs. It does not decide which CAD or mold terms belong in the vocabulary.

## Development and maintenance

| Item | Confirmed method | Source and location | Open question |
|---|---|---|---|
| Candidate collection | Not specified as a domain editorial process; SKOS provides representation constructs after concepts have been selected. | [[W3C_SKOS_Primer]] — 2 SKOS Essentials; 2.1 Concepts | A CAD project still needs its own evidence and inclusion rules. |
| Inclusion / merging / splitting | Not specified. Concepts are identified separately from labels, so a representation does not by itself prove synonymy or identity. | [[W3C_SKOS_Primer]] — 2.1 Concepts; 2.2 Labels | The project must not use `aliases` as an automatic merge rule. |
| Preferred labels / definitions | `skos:prefLabel` and `skos:altLabel` distinguish preferred and alternative lexical labels; documentation properties distinguish scope notes, definitions, examples, and change notes. | [[W3C_SKOS_Primer]] — 2.2; 2.4 Documentation Properties | The Vault mirrors these distinctions with headings rather than RDF properties. |
| Relations / classification | `skos:broader`, `skos:narrower`, and `skos:related` express common knowledge-organization links; `skos:ConceptScheme` groups the concepts in a scheme. | [[W3C_SKOS_Primer]] — 2.3; 2.5 Concept Schemes | RDF directionality and inference are outside this phase. |
| Checking / updating | `skos:editorialNote` and `skos:changeNote` can record work reminders and fine-grained changes, but SKOS does not define who approves domain changes. | [[W3C_SKOS_Primer]] — 2.4 Documentation Properties | Decide later whether Markdown revision notes are sufficient. |

## Application to mold CAD

- What to adopt and why: keep the concept itself separate from labels; distinguish preferred names, confirmed aliases, broader relations, related relations, and change/open-question notes.
- What not to adopt directly and why: do not add RDF, URIs, inference, or a formal `ConceptScheme` implementation while the source evidence and teacher's scope remain unsettled.
- Limits of this investigation: the W3C primer was read as a representation guide, not as a full SKOS reference or validation exercise.

## Supporting source

- [[W3C_SKOS_Primer]]

