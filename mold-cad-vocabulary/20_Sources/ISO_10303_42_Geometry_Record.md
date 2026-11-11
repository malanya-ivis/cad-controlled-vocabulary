# ISO 10303-42:2025 Geometry and Topology Record

## Source and reading scope

- Author / organization: International Organization for Standardization (ISO), ISO/TC 184/SC 4
- URL: https://www.iso.org/standard/91386.html
- Version / publication year: ISO 10303-42:2025, edition 9
- Source language: English catalog record and abstract
- Sections actually read / date: Official catalog record and abstract only; standard text was not read; 2026-10-07
- Usage conditions / what is saved: Catalog-level scope summary only; no standard clauses, tables, or figures copied.

## Collected scope

| Item | Official abstract says | Project use | Limit |
|---|---|---|---|
| Geometry and topology | The part covers geometric and topological representation, including points, curves, surfaces, and solid models. | Keep geometry representation separate from a vocabulary label such as Hole or Pocket. | This is a data-representation standard, not a mold-feature vocabulary. |
| Topological references | The listed entities include vertex, edge, face, path, loop, and shell. | Supports a proposed `geometry_ref` field for pointing to CAD regions when the source model provides usable references. | Do not assume these references stay stable after a model revision. |
| Model forms | The abstract lists B-rep, tessellated geometry, and association between tessellated and exact geometry. | Record whether evidence came from a mesh, precise CAD geometry, or both. | The abstract does not define the project's recognition or measurement rules. |
| Outside scope | The 2025 abstract excludes geometric tolerances and implicit feature-based representations. | Do not expect this part alone to define tolerances or feature vocabulary. | Confirm clause-level details from authorized access before making standards claims. |

## Project decision

Use this record to guide data-layer separation, not to import a list of mold concepts. The current STL examples are mesh observations; they do not recover native CAD feature history or prove design intent.

