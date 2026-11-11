# Concept overview

Start with [[Knowledge_Structure]] and [[Knowledge_Structure.canvas]] for the organized concept map. [[Shape_Features]], [[Shape_Properties]], [[Internal_Structures]], and [[Feature_Relations]] explain how the concepts combine in [[Single_Part_Description_Example]].

The current target is a software-independent vocabulary for **features and geometric properties inside one mold-CAD part**. A first pilot can use the strongest available examples; the current source set leans toward injection molding but does not limit the intended domain.

## Active single-part feature drafts

### Shape features

[[Hole]] · [[Counterbore]] · [[Countersink]] · [[Pocket]] · [[Slot]] · [[Rib]] · [[Boss]] · [[Fillet]] · [[Chamfer]]

CAD sources describe both resulting geometry and feature commands. The notes keep those contexts separate; see [[CAD_Feature_and_Operation_Boundaries]].

### Shape properties

[[Draft_Angle]] · [[Undercut_(injection_molding)|Undercut]] · [[Wall_Thickness]]

These describe a part or a feature relative to a direction, neighboring surface, or local material thickness. Values such as angle, thickness, depth, and through/blind status are normally instance properties, not additional shape-feature nodes.

### Internal structures

[[Internal_Void]] · [[Cooling_Channel]] · [[Gas_Vent_(injection_mold)|Gas Vent]]

Internal structures may require CAD geometry, a section view, or design documentation. Their purpose cannot be established from an exterior image alone.

## Existing context notes

The earlier injection-molding component and process vocabulary remains available as background evidence, not as the main deliverable:

- **Mold and assemblies/components:** [[Mold_(injection_molding)|Mold]], [[Mold_Base]], [[Core_(mold_component)|Core]], [[Core_Pin]], [[Slide_Core_(injection_molding)|Slide Core]], [[Mold_Insert_(injection_molding)|Mold Insert]], [[Ejector_Pin]], [[Ejector_Plate]], [[Stripper_Plate]], [[Sprue_Bushing]], [[Locating_Ring]], [[Guide_Pin]], [[Guide_Bush]], [[Angled_Pin_(injection_molding)|Angled Pin]].
- **Process passages and systems:** [[Cavity_(injection_molding)|Cavity]], [[Cooling_Circuit]], [[Gate_(injection_molding)|Gate]], [[Cold_Slug_Well]], [[Runner_(injection_molding)|Runner]], [[Runner_System_(injection_molding)|Runner System]], [[Sprue_(injection_molding)|Sprue]].
- **Part interface:** [[Parting_Line_(injection_molding)|Parting Line]].

These notes may be reconsidered if a single-part shape example needs their terminology, but assembly membership and component inventories remain outside the current focus.

## Describe feature occurrences

[[Simple_CAD_Dataset_Study]] applies the vocabulary to actual STL data: [[CAD_Counterbore_Example]], [[CAD_Countersink_Example]], [[CAD_Rectangular_Pocket_Example]] and [[CAD_Cross_Rib_Example]]. Measurements use input coordinate units and semantic mappings remain drafts.


The concept notes define terms. To describe a specific part, use the concise record pattern in [[Feature_Description_Rules]]: identify the part and feature instance, give geometric properties, record feature-to-feature relations, and attach the source of any stated purpose.

## Browse evidence

Use [[Concept_Index.base]] for concepts by current scope role. See [[Design_Policy]] for inclusion rules and [[Source_Coverage_and_Gaps]] for reading scope and access limits. All current concept notes remain `draft`.
