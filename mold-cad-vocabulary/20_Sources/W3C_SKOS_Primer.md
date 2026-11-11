# W3C: SKOS Simple Knowledge Organization System Primer

## Source and reading scope

- Author / organization: World Wide Web Consortium (W3C)
- URL: https://www.w3.org/TR/skos-primer/
- Version / publication year: W3C SKOS Primer, online technical specification
- Source language: English
- Sections actually read / date: SKOS Essentials; Concepts; Preferred and Alternative Lexical Labels; Documentation Properties; Concept Schemes; broader/narrower and related concept examples / 2026-10-05
- Usage conditions / license and what is saved in this vault: W3C document conditions were not separately recorded in this pass. This note saves vocabulary-property names and an independent implementation summary; the vault does not implement RDF or store the full examples.

## Collected terminology

| Original label | Section / figure | Usage in context | Candidate concept | Open question |
|---|---|---|---|---|
| `skos:Concept` | 2.1 Concepts | A concept is an abstract unit of thought identified separately from the lexical labels used for it. | [[10_Vocabulary_Studies/SKOS]] | SKOS is a representation model, not one of the domain vocabularies selected for the method comparison. |
| `skos:prefLabel` | 2.2.1 Preferred Lexical Labels | Provides a preferred lexical label, with language tags allowing multilingual labels. | [[10_Vocabulary_Studies/SKOS]] | The vault keeps preferred English names in filenames and uses YAML aliases only for confirmed equivalents. |
| `skos:altLabel` | 2.2.2 Alternative Lexical Labels | Represents synonyms, near-synonyms, abbreviations, or acronyms associated with a concept. | [[10_Vocabulary_Studies/SKOS]] | A source expression is not automatically an alias until semantic equivalence is checked. |
| `skos:broader` / `skos:narrower` | 2.3.1-2.3.2 Hierarchical Links | Expresses a broader/narrower relation; the direction and inverse relation must be handled consistently. | [[10_Vocabulary_Studies/SKOS]] | The project records only supported “is a kind of” links and does not implement RDF inference. |
| `skos:related` | 2.3.3 Associative Links | Represents an associative relation that is not hierarchical. | [[10_Vocabulary_Studies/SKOS]] | The project writes the reason in the note rather than using a plugin or RDF property. |
| `skos:scopeNote`, `skos:definition`, `skos:changeNote` | 2.4 Documentation Properties | Separates intended usage, full definition, and maintenance history from lexical labels and links. | [[10_Vocabulary_Studies/SKOS]] | These distinctions inform Markdown headings, not a new property system in this phase. |
| `skos:ConceptScheme` | 2.5 Concept Schemes | Groups concepts into a compiled thesaurus or other knowledge-organization system. | [[10_Vocabulary_Studies/SKOS]] | The Vault itself is the working container; a formal scheme URI is out of scope. |

## Figure evidence

No figure evidence was saved. SKOS examples were read as text describing the representation model, not copied into the vault as RDF data.

