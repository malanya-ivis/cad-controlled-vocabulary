# Design Policy

**Status:** Revised 2026-10-06 from supervisor clarification. Vocabulary definitions remain drafts until supported and reviewed.

## Purpose and scope

Describe geometric features, shape properties, and internal structures of a **single part** represented in mold CAD. The target vocabulary is independent of CAD software. Vendor help is useful evidence for the labels and parameters a product uses, but a vendor command is not automatically a general feature definition.

The intended domain is mold CAD broadly. Existing source material is strongest for injection molding, so it can supply the initial examples; this is a practical pilot, not a decision to exclude other mold types. Do not center this vocabulary on assembly trees, part membership, mold-component inventories, or machine hardware.

The vocabulary describes feature types. A separate part-feature record describes an occurrence of a feature on one part, its values, location, relations, and documented purpose. See [[Feature_Description_Rules]].

## Inclusion and evidence

Create or retain a concept when it helps name a shape feature, a shape property, or an internal structure in a single part and its scope can be explained. Keep the source's actual use, the project's proposed meaning, and unresolved questions distinct. A term appearing in CAD help, a standard catalog, or a mold article is evidence to investigate, not automatic proof of a universal definition.

A feature may be recognizable by geometry while its function is not. For example, a hole-like passage is not a cooling channel unless design or other evidence establishes that role. Mark evidence as observed geometry, drawing/specification statement, designer intent, or analysis result. Do not infer a functional purpose from appearance alone.

## Concept kinds and evidence conditions

The `category` field is a filing group. Concepts in different groups do not use one identical recognition rule. The active pilot contains these semantic kinds:

| Kind | Current concepts | Evidence needed for a part occurrence |
|---|---|---|
| Geometric feature | Hole, Pocket, Slot, Rib, Boss, Fillet, Chamfer | The resulting surfaces/region must be visible in CAD, a section, or equivalent geometry evidence. Do not infer the modeling command or purpose. |
| Local entrance form | Counterbore, Countersink | Show the cylindrical/flat-shoulder or conical entrance form and link it to one identified Hole passage. Do not count the entrance as another through-passage. |
| Geometric property / condition | Draft Angle, Undercut, Wall Thickness | Draft and Undercut need an identified pull/reference direction. Wall Thickness needs paired surfaces, measurement location and direction/method. Record the unit and scope of the value. |
| Empty geometric region | Internal Void | Show the material-free region and record whether it is enclosed, open to the exterior, or unknown. The current working definition includes open interior regions, but whether to split open and enclosed cases remains unresolved. Openness does not make the term a synonym for Pocket. |
| Functional path | Cooling Channel, Gas Vent | Show the path geometry and separately cite design/process evidence for its cooling or gas-escape role. Without that evidence, use a geometric description only. |

These are different kinds of description, not mutually exclusive taxonomic classes. A physical region may have a shape description and a spatial/function description when each is supported. Record the descriptions as separate assignments on one occurrence; do not silently equate the concepts. The per-concept notes state the minimum evidence and open boundaries. `unknown` means not established, not absent.

## Categories

| Category | Use | Current examples |
|---|---|---|
| `shape_feature` | Local geometric feature of a part | [[Hole]], [[Counterbore]], [[Countersink]], [[Pocket]], [[Slot]], [[Rib]], [[Boss]], [[Fillet]], [[Chamfer]] |
| `shape_property` | Geometric condition or value associated with a part or feature | [[Draft_Angle]], [[Undercut_(injection_molding)|Undercut]], [[Wall_Thickness]]; through/blind as possible hole attributes |
| `internal_structure` | Internal void, channel, or vent geometry whose role may need design evidence | [[Internal_Void]], [[Cooling_Channel]], [[Gas_Vent_(injection_mold)|Gas Vent]] |
| `context_only` | Existing process, assembly, component, or interface notes retained as background | [[Mold_(injection_molding)|Mold]], [[Mold_Base]], [[Core_(mold_component)|Core]], [[Runner_(injection_molding)|Runner]], and other mold-system notes |

A category is a filing aid, not a claim that all members share a broader-concept relation. Dimensions and parameter values normally belong on a feature instance, not in a separate concept note. A subtype such as Counterbore gets its own note only when its shape boundary and use justify that granularity.

## Names and granularity

Use a concise preferred label for the engineering concept, not a software command name, where evidence supports one. Qualify homographs when needed. Keep confirmed alternate labels separate from unverified translations or source spellings. Record language-specific labels in the source note until equivalent scope is checked.

Separate these layers when they differ:

- resulting part geometry;
- a CAD feature-history command;
- a machining feature used for process planning;
- a manufacturing or mold function;
- a property/value applied to a feature.

A shared word does not collapse these layers. The same geometric feature can have different CAD construction histories.

## Relations

Concept notes may use `Broader concept` only for an evidenced kind-of relation, `Related concepts` for a named association, and `Distinguished concepts` for a boundary. These are relations between vocabulary concepts.

Relations between feature instances belong in a part-feature record, not in the concept graph. Use a small, explicit predicate and record its evidence. Useful starting predicates include `opens_to`, `connects_to`, `intersects`, `coaxial_with`, `has_property`, and `serves_purpose`.

For a statement such as “this rib is intended to reduce warpage,” record the part and rib instance, the purpose, and whether the link comes from a drawing/specification, designer statement, simulation, or an inference. Do not present an inferred purpose as an observed fact.

## Reference roles

- ANSI/NISO Z39.19 and ISO 25964 inform vocabulary construction, term control, definitions, relations, and maintenance. Selected reading is not formal compliance.
- MeSH and ICD-10 are structural examples from other domains. Compare their ways of grouping concepts, labels, notes, and boundaries; do not import a medical taxonomy.
- STEP AP 224 is a machining-feature reference for single-piece mechanical-part information. It helps compare manufacturing features with designed part geometry; it is not a complete mold-feature vocabulary.
- JIS Z 8114 is a Japanese drawing-terminology reference. Use it to check terminology and scope, not as an assumed exhaustive 3D CAD taxonomy.
- CAD vendor documentation records software-specific use and is not the scope of the controlled vocabulary.

## Limits and maintenance

Current injection-mold component and process notes are retained for provenance and comparison, but marked `context_only`; they are not part of the active single-part feature set. Do not delete prior research solely because its subject is now peripheral.

When a new term is needed, capture its original label, source location, use, and candidate category in [[Candidate_Term_Queue]]. Compare it with existing notes, write a bounded draft, link evidence, and record the decision in [[Decision_Log]]. Preserve uncertainty. Promote a note from `draft` only after its meaning and scope have been reviewed against suitable sources.

## Open work

- A first purpose/process comparison and proposed local workflow are recorded in [[Controlled_Vocabulary_Governance]]. Review authorized full-text clauses before adopting detailed standard procedures.
- Review single-part shapes and source terms for the initial pilot list, including the remaining hole forms and wall-thickness use.
- Apply the draft rules in [[Feature_Relations]] and [[Single_Part_Description_Example]] to a real sample and revise them using its actual geometry and design evidence.
- Add non-injection-molding examples when a source and sample are available; do not treat the current evidence bias as a domain boundary.
