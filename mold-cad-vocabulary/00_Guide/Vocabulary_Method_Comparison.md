# Vocabulary Method Comparison

**Status:** Revised to reflect the references identified by the supervisor. Reading depth is stated per source; no formal compliance is claimed.

| Reference | Role in this project | Current reading status | What to compare or adapt | Limit |
|---|---|---|---|---|
| ANSI/NISO Z39.19 | Controlled-vocabulary construction and maintenance | Selected clauses read in [[NISO_Z39_19]] | Warrant, term choice, compound terms, relationships, and revision records | Guidance does not decide mold-CAD scope or approve a term automatically |
| ISO 25964-1 | Thesaurus development and maintenance | Official catalog/abstract reviewed; full text not read; a second edition is in development | Vocabulary structure, concept/term handling, definitions, and maintenance | Designed for information retrieval thesauri; do not assume every recommendation fits feature description |
| ISO 25964-2 | Interoperability among vocabularies | Official catalog/abstract reviewed; full text not read; revision work is listed | Mapping and recording match confidence between this vocabulary and external sources | Not a source of feature definitions |
| MeSH | Biomedical controlled vocabulary example | Selected introduction sections read in [[MeSH]] | Preferred terms, entry terms, hierarchy, and maintenance history | Retrieval vocabulary, not a geometry taxonomy |
| ICD-10 | Medical classification example named by the supervisor | WHO Volume 2 structure section reviewed; see [[ICD-10]] | Grouping, hierarchical browsing, inclusion/exclusion notes, and practical classification boundaries | Statistical disease classification; do not import its categories or coding purposes |
| STEP AP 224 | Technical reference for machining-feature representation | Official ISO abstract and selected NIST papers reviewed; standard text not read | Compare machining-feature classes and parameters with designed shape features | Process-planning representation, not a complete mold-CAD shape vocabulary |
| JIS Z 8114:1999 | Japanese drawing-terminology reference | Official JSA catalog page reviewed; standard text not read | Japanese terms, definitions, and drawing-document context | Not assumed to cover all 3D CAD feature geometry |
| AAT / JST / SKOS | Supplementary examples and representation references | Existing selective studies retained | Scope notes, change history, labels, and simple concept relations | Supplementary; not the supervisor-designated core set |

## Working synthesis

- Keep a preferred concept label distinct from source expressions and software command names.
- Give every concept a scope statement, evidence, and a boundary with likely confusions.
- Use broader/narrower relations only for supported kind-of claims. Record actual feature-instance relations separately under [[Feature_Description_Rules]].
- Capture design purpose as an evidence-bearing relation, not as a property inferred from shape alone.
- A recognized or machinable feature can differ from the feature used to explain a designer's shape. Compare the layers; do not merge them because their labels match.
- Preserve source versions and actual reading scope. Catalog abstracts support scope discovery, not detailed term definitions.

## Open method work

Read the required standards and cases only to the depth needed to answer the assignment: what they classify, how they name concepts, how they state boundaries and relations, and how they maintain revisions. Keep each claim linked to the actual section read.

The initial comparison of each reference's purpose, confirmed development/maintenance observations, project takeaway, and reading limits is in [[Controlled_Vocabulary_Governance]].
