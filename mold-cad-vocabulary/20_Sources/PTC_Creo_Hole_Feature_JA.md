# PTC Creo: 穴フィーチャーについて

## Source and reading scope

- Author / organization: PTC
- URL: https://support.ptc.com/help/creo/creo_pma/r13/japanese/part_modeling/part_modeling/About_the_Hole_Feature.html
- Version / publication year: Creo Parametric r13 Japanese online help
- Source language: Japanese, with English UI labels in parentheses
- Sections actually read / date: Opening description; listed hole types; “穴フィーチャーとカットフィーチャーの比較” / 2026-10-05
- Usage conditions / license and what is saved in this vault: Not yet checked. This note preserves Japanese labels and English UI labels with independent summaries only; no screenshots or extended source text are saved.

## Collected terminology

| Original label | Section / figure | Usage in context | Candidate concept | Open question |
|---|---|---|---|---|
| 穴 / Hole | Opening description and page title | The Hole tool adds simple, custom, and industry-standard holes to a model; placement, direction, depth, and hole-specific properties are defined in the feature. | [[Hole]] | This is a Creo feature-tool description, not by itself a system-independent definition. |
| 単純 / Simple | Hole types | A hole made from an extrusion or revolved cut not directly associated with an industry standard; the page lists flat, drilled, and sketched subtypes. | [[Hole]] | Subtype labels are retained as source usage, not separate project concepts. |
| 標準 / Standard | Hole types | A hole made from a revolved cut based on an industry-standard fastener table, with tap or clearance diameters available. | [[Hole]] | The standard-hole parameter model should not be generalized to all CAD systems. |
| タップ穴 / Tapped; ドリル穴 / Drilled; クリアランス穴 / Clearance | Standard hole types | UI labels for standard hole variants. | [[Hole]] | Japanese correspondences are source labels; they are not added as aliases to Hole until terminology scope is reviewed. |
| 穴フィーチャー / Hole feature | Comparison with cut feature | The page distinguishes the Hole feature from a generic cut by its placement scheme and by usually not requiring a sketch. | [[Hole]] | Confirm whether the project should record feature-history semantics separately from resulting geometry. |

## Figure evidence

No figure evidence recorded. Images were not used to infer hole geometry; only the readable text and labels were recorded.

