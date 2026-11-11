# Feature Description Rules

## Two levels of description

1. **Vocabulary concept:** what a term means, what it excludes, and which sources support that scope. One concept note describes one meaning.
2. **Part-feature occurrence:** where a feature appears on one part, its values, and its relations to other features. An occurrence is not a new vocabulary concept.

Do not use an assembly tree as the feature description. Keep the part identity only as context for the occurrence being described.

## Minimum fields for a feature occurrence

| Field | Record |
|---|---|
| Part | Stable part/sample identifier |
| Feature ID | Identifier unique within that part; the lookup key is `(part_id, feature_id)` |
| Concept assignment(s) | Link each supported description to its concept; when one occurrence has different views, label the view (shape, spatial region, or confirmed function) instead of implying synonymy |
| Geometry / extent | The surfaces, region, or evidence that locates the feature; use a section or CAD selection for hidden geometry |
| Evidence | Geometry source, checked region, method, and whether the statement is observed, specified, analyzed, or still unknown |
| Properties | Values with units, such as diameter, depth, draft angle, or wall thickness; indicate measured, specified, or unknown |
| Relations | A named relation to another feature on the same part, with direction and target |
| Purpose | Optional design purpose, linked to a source and marked stated, analyzed, or inferred |

Do not infer an internal passage from an exterior view. Record the geometry source used: native CAD, drawing, section view, scan, or other evidence. If no source shows the inside, mark the feature as unknown rather than absent.

## Relation rules

Use relations that say what connects two instances. Start with a small set: `opens_to`, `connects_to`, `intersects`, `coaxial_with`, `has_property`, and `serves_purpose`. State the relation's direction and its evidence. Do not make every relation a new concept.

[[Feature_Relations]] gives the project relation definitions, including `entrance_form_of`, `boundary_of`, and `located_on`. [[Single_Part_Description_Example]] applies them to identified occurrences. This is an illustrative example; a real part still needs CAD/drawing evidence.

Concept notes use stable `concept_id` values and typed `concept_relations`; occurrence records use `part_id` and `feature_id`. The same physical passage may have a Hole shape description and a confirmed Cooling Channel functional description under one occurrence ID. Record the descriptions as separately typed assignments with their own evidence. Do not create two passage occurrences solely because there are two descriptions. A passage and its geometrically distinct entrance form may have linked occurrence IDs, but the model still counts one continuous passage.

A relation between two feature types is different from a relation between two occurrences. `Rib` may be related to `Wall` as vocabulary concepts; a specific rib being adjacent to a specific wall is an instance relation.

Purpose is not geometry. For example, an anti-warpage statement must point to the design note, drawing, designer statement, or analysis that supports it. If purpose is only inferred from geometry, label it as an inference and keep it separate from confirmed facts.

## Worked example (illustrative record only)

    part_id: mold-part-01
    feature_id: F-07
    term: Rib
    geometry_source: native CAD model
    properties:
      nominal_thickness: unknown
    relations:
      - predicate: serves_purpose
        target: reduce_warpage
        evidence: design specification DS-04
        evidence_kind: stated_intent

This example does not assert that every rib reduces warpage or that the named part exists in the source corpus. It shows how to add purpose without baking a process claim into the definition of Rib.

## Add a missing term

1. Add the original wording, source location, and short use summary to a source note.
2. Search existing concepts for a match, homograph, subtype, or attribute before creating a note.
3. Put an unresolved candidate in [[Candidate_Term_Queue]]. State why it may be a separate concept.
4. Choose a category, preferred label, and bounded meaning. Keep a CAD command distinct from the geometry it creates.
5. Link source evidence, related concepts, and one open question. Leave the status `draft` until reviewed.
6. Record a merge, split, or new-term decision in [[Decision_Log]]. Update [[Concept_Overview]] and [[Concept_Index.base]].

The initial list is allowed to be incomplete. The maintenance rule is part of the deliverable: later terms are added by this process, with their scope and evidence recorded.


## Keep concept links and geometry links separate

This distinction follows the basic modeling idea in [[W3C_SKOS_Primer]]: identify a concept separately from its preferred/alternative labels and its semantic links. The vault uses this only as a documentation guide; it does not claim a SKOS implementation.

- **Concept relation:** relates vocabulary meanings, for example `Counterbore hole_entrance_form_of Hole` or `Fillet compared_with Chamfer`. It does not assert that two geometries touch in a particular part.
- **Occurrence relation:** relates feature IDs in one part, for example `F02 entrance_form_of F01`, `F01 intersects F02`, or `F03 connects_to F04`. It needs evidence for that specific part.
- **Unique key:** a feature ID only needs to be unique within its part. `part_id=STL-1400, feature_id=F01` is distinct from `part_id=STL-8972, feature_id=F01`.
- **Different spatial claims:** `intersects` means the represented geometric regions overlap; `touches` means their boundaries meet without overlap; `connects_to` means a continuous passable path exists between passage regions. Do not infer one predicate from another. Add `touches` only when the source geometry supports checking it.
- **Three-valued check:** use `true` or `false` only after a check appropriate to the whole stated geometry and method. If only selected sections/rays were inspected, record `unknown` for the whole-part claim and put the limited observation in an `observation` field. “Not seen in checked sections” is not the same as “does not exist.”

## Apply the evidence and search examples

[[Claim_Evidence_Matrix]] maps the fifteen core drafts to the evidence that supports their usage and the evidence still needed for a part occurrence. [[Cross_Mold_Domain_Transfer]] checks the source contexts of injection molding, casting and press forming.

The supplemental records in [[Supplemental_Feature_Records.json]] distinguish `origin: user_supplied_stl` from `origin: synthetic_teaching_model`. Put unconfirmed labels in `candidate_concept_ids`, not supported `concept_assignments`. A filename is a source identifier, not classification evidence; see [[CAD_Fillet_Boss_Name_Check]].

[[RAG_Search_Verification_Cases]] checks nineteen authored cases against the manual records. A missing supported record is not physical absence, a synthetic example is excluded from supplied-model searches by default, and required units/directions/purposes remain unknown when no evidence exists. This is a record-filter demonstration, not a CAD search database or RAG system.
