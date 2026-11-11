# Art & Architecture Thesaurus (AAT)

**Study status:** Supplementary comparison; not identified as a core reference in the supervisor clarification.

## Purpose and scope

AAT is a thesaurus for terminology and relationships used to catalog, discover, and retrieve information about art, architecture, and visual cultural heritage. It uses concept records, terms, notes, sources, hierarchies, and associative relationships. Its scope and facet structure are intentionally domain-specific; it is useful here as an editorial method example rather than as a CAD classification to copy.

## Development and maintenance

| Item | Confirmed method | Source and location | Open question |
|---|---|---|---|
| Candidate collection | Contributions must be in scope, include minimum information, follow the prescribed format, and come from an authorized contributor. Sources and contributor information are retained as part of editorial processing. | [[Getty_AAT_Editorial_Guidelines]] — 1.2 Contributions and Editorial Control; 3.3 Terms | The current contribution form and minimum field list were not separately captured. |
| Inclusion / merging / splitting | Records representing exactly the same concept may be merged only after comparing term, parent context, meaning, definition, and scope. If the meaning is uncertain, the guideline says not to merge. | [[Getty_AAT_Editorial_Guidelines]] — 2.2 Merging Records | The project needs a lightweight equivalent of this same-concept check. |
| Preferred labels / definitions | Terms have preferred and non-preferred roles, languages, sources, and other editorial flags. Scope notes describe one intended concept, not every dictionary sense; homographs are kept as separate records and disambiguated with qualifiers. | [[Getty_AAT_Editorial_Guidelines]] — 3.3 Terms; 3.4 Scope Note | The vault uses only `aliases`, `category`, and `status`; detailed term fields remain in prose. |
| Relations / classification | Parents provide broader contexts; AAT is polyhierarchical, while most hierarchical links are genus/species-like. Related Concepts are direct, useful associations that are neither equivalent nor hierarchical; “distinguished from” is used where confusion is significant. | [[Getty_AAT_Editorial_Guidelines]] — 3.1 Hierarchical Relationships; 3.5 Associative Relationships | A CAD relation must pass the “is a kind of” test before being written as Broader concept. |
| Checking / updating | Getty maintains final editorial control, reviews contributions, may merge or reposition records, and aims to keep identifiers persistent. Administrative flags and revision fields preserve problems and changes. | [[Getty_AAT_Editorial_Guidelines]] — 1.2 Contributions and Editorial Control; 2.2; 3.8 | The vault does not yet have a separate reviewer or persistent identifier system. |

## Application to mold CAD

- What to adopt and why: write one scope-limited definition per concept; separate homographs by domain or qualifier; record the source and the reason for each relation; use explicit distinguished concepts for likely CAD confusions such as Pocket versus mold Cavity.
- What not to adopt directly and why: do not reproduce AAT's facets, numeric IDs, contribution workflow, or full polyhierarchy in the first lightweight Vault. They would increase maintenance without evidence that the current CAD sample needs them.
- Limits of this investigation: the editorial guidelines were read selectively; this note does not claim to describe the entire AAT data model or current editorial system.

## Supporting source

- [[Getty_AAT_Editorial_Guidelines]]

