# NIST: STEP B-rep and Faceted Geometry Record

## Source and reading scope

- Author / organization: National Institute of Standards and Technology (NIST)
- URL: https://www.nist.gov/news-events/news/2024/03/nist-contributes-new-modeling-capability-iso-product-data-interoperability
- Version / publication year: NIST news article, 2024-03-01
- Source language: English
- Sections actually read / date: Article text on STEP, hybrid B-rep, facet data, and precise geometry; 2026-10-07
- Usage conditions / what is saved: Short independent summary; no figures copied.

## Collected scope

| Item | Source says | Project use | Limit |
|---|---|---|---|
| B-rep | STEP geometry uses an explicit topological model organized around faces, edges, and vertices. | A native or STEP model can provide references beyond a rendered surface. | File format alone does not prove every model is valid or complete. |
| Faceted mesh | Triangular facets approximate surfaces; the article contrasts this with mathematically defined precise geometry. | Make the evidence limits of the project's STL measurements explicit. | A mesh can still support observations and approximate measurements; the article does not set project thresholds. |
| Hybrid model | Facet data can be associated with precise geometry in a hybrid model. | Allow a future record to cite both a mesh region and a precise CAD entity. | Do not assume that the current dataset uses hybrid B-rep. |

## Project decision

For current STL records, use wording such as “observed in the mesh” or “measured from mesh coordinates.” Do not claim native feature history, exact analytic surfaces, or design purpose from the mesh alone.

