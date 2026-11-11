# CAD Feature and Operation Boundaries

**Status:** Working synthesis for a software-independent, single-part shape vocabulary. CAD documentation is evidence of a product's own labels and behavior, not a limit on which CAD systems the vocabulary covers.

## Comparison matrix

| Label family | Evidence across sources | Working boundary | Next use |
|---|---|---|---|
| Hole and hole-end forms | Onshape, Inventor JA, and Creo JA document hole commands/options; sources include simple, counterbore, countersink, and spotface forms. NIST uses Hole in machining-feature contexts. | Describe the resulting opening and its local geometry separately from a command, end condition, or machining plan. Through/blind is normally a property. | Compare Counterbore and Countersink boundaries with drawing terminology; keep Spotface in the queue until its distinction is clear. |
| Pocket / Slot | Creo documents machining-feature meanings; Fusion uses Pocket for a CAM operation; Onshape describes modeling operations that can remove material. | Use source evidence for candidate geometric scopes, but do not equate CAM operations or manufacturing classes with final part shape. | State the observable geometric criteria needed to distinguish a pocket from an elongated slot. |
| Rib / Boss | Onshape and JEED use Rib in support-structure/product contexts; Boss appears in CAD recognition, machining, and molded-product contexts. | Treat the resulting local shape as the vocabulary target; record a design command or intended function separately. | Establish shape-level boundaries against a sample part and supporting source. |
| Chamfer / Fillet | Onshape and Inventor document commands and options; other sources describe edge treatments or machining features. | Keep beveled and rounded edge geometry distinct from feature-history operations. | Use shape examples to explain the distinction and record parameters as instance values. |
| Draft angle | JEED records 抜き勾配 as an angle relative to the release direction; Inventor documents a Draft command. | The angle/property belongs to the part description; the CAD Draft command is a way to construct geometry. | Compare direction, measured faces, and units in a sample part. |
| Shell / internal void | Onshape documents Shell as a command that removes material to leave hollow geometry with selected wall thickness. | Shell operation, wall-thickness value, and resulting internal void are related but distinct. | Use section/native CAD evidence before generalizing the internal-void concept. |

## STEP AP 224 boundary

The ISO catalog describes AP 224 as a representation/exchange protocol for process planning with machining features in single-piece mechanical parts. The official catalog record is not a complete feature definition. NIST papers provide accessible context, but their machining interpretation must remain distinct from the design-shape vocabulary.

Sources: [[ISO_10303_224_Machining_Features_Record]], [[NIST_Feature_Recognition_Manufacturability]], [[NIST_Feature_Based_Machining_STEP]], [[NIST_Feature_Based_Inspection_Machining_System]].

## Design consequence

For each term, record whether a source describes final geometry, a CAD feature-history operation, a machining feature, a CAM toolpath, a mold function, or a property. Keep the main concept software-independent; record system-specific commands in source notes. See [[Feature_Description_Rules]] for properties and relations on a part-feature occurrence.
