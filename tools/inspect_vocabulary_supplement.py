"""Inspect selected supplied meshes and two explicitly synthetic teaching models.

Run with cad-structure-search/.venv/bin/python. Originals are read only.
The shell screen finds candidates, not a proof of cavity absence/enclosure.
"""
from pathlib import Path
import hashlib
import json
import numpy as np
import trimesh
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from inspect_simple_cad_dataset import draw_mesh, draw_section

ROOT = Path(__file__).resolve().parents[1]
VAULT = ROOT / "mold-cad-vocabulary"
SIMPLE = Path("/home/malanya/projects/cad-structure-search/data/simple_CAD_dataset")
COMPLEX = SIMPLE.parent / "final_selected/stl"
OUT = VAULT / "80_Assets/vocabulary_supplement"


def working_mesh(path):
    raw = trimesh.load_mesh(path, process=False)
    threshold = float(max(raw.extents) ** 2 * 1e-14)
    keep = raw.area_faces > threshold
    mesh = trimesh.Trimesh(vertices=raw.vertices, faces=raw.faces[keep], process=True)
    return mesh, {
        "source_path": str(path),
        "source_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "bounds": raw.bounds.tolist(),
        "raw_triangle_count": len(raw.faces),
        "removed_near_zero_area_triangles_in_memory": int((~keep).sum()),
        "area_threshold": threshold,
        "working_watertight": bool(mesh.is_watertight),
        "working_winding_consistent": bool(mesh.is_winding_consistent),
        "self_intersection_check": "not_performed",
        "coordinate_unit": "input_units",
        "physical_unit": "unknown",
    }


def voxel_boundary(open_to_top):
    """Exact box boundaries on a 3x3x3 coordinate grid, with center removed."""
    levels = [0., 4., 16., 20.]
    occupied = {(i, j, k) for i in range(3) for j in range(3) for k in range(3)}
    occupied.remove((1, 1, 1))
    if open_to_top:
        occupied.remove((1, 1, 2))
    vertices, faces = [], []
    # Corner order gives outward normals for the occupied material.
    sides = [
        ((-1, 0, 0), [(0,0,0),(0,0,1),(0,1,1),(0,1,0)]),
        (( 1, 0, 0), [(1,0,0),(1,1,0),(1,1,1),(1,0,1)]),
        ((0,-1,0), [(0,0,0),(1,0,0),(1,0,1),(0,0,1)]),
        ((0, 1,0), [(0,1,0),(0,1,1),(1,1,1),(1,1,0)]),
        ((0,0,-1), [(0,0,0),(0,1,0),(1,1,0),(1,0,0)]),
        ((0,0, 1), [(0,0,1),(1,0,1),(1,1,1),(0,1,1)]),
    ]
    for cell in sorted(occupied):
        for offset, corners in sides:
            neighbor = tuple(cell[a] + offset[a] for a in range(3))
            if neighbor in occupied:
                continue
            start = len(vertices)
            vertices.extend([[levels[cell[a] + c[a]] for a in range(3)] for c in corners])
            faces.extend([[start,start+1,start+2],[start,start+2,start+3]])
    return trimesh.Trimesh(vertices=vertices, faces=faces, process=True)


def figure(name, mesh, planes):
    fig = plt.figure(figsize=(15, 4.8))
    ax = fig.add_subplot(1, 3, 1, projection="3d")
    draw_mesh(ax, mesh)
    ax.set_title(name + ": surface mesh")
    for i, (axis, position, displayed) in enumerate(planes, 2):
        ax = fig.add_subplot(1, 3, i)
        draw_section(ax, mesh, axis, position, displayed, f"Section {'XYZ'[axis]} = {position:g}")
    synthetic = name.startswith("teaching_")
    fig.suptitle("SYNTHETIC teaching geometry; no mold/design claim" if synthetic else
                 "Supplied STL; physical unit and design purpose unknown")
    fig.tight_layout(rect=(0,0,1,.92))
    path = OUT / f"{name}_views.png"
    fig.savefig(path, dpi=150)
    plt.close(fig)
    return str(path.relative_to(VAULT))


def screen_shells():
    results = []
    for index, path in enumerate(sorted(COMPLEX.glob("*.stl"), key=lambda p:int(p.stem)), 1):
        mesh, record = working_mesh(path)
        groups = trimesh.graph.connected_components(mesh.face_adjacency,
                                                      nodes=np.arange(len(mesh.faces)))
        shells = []
        # A closed shell needs at least four nondegenerate triangle faces.
        # Open sheets remain counted but are not enclosure candidates.
        for i, face_ids in enumerate(groups):
            if len(face_ids) < 4:
                continue
            c = mesh.submesh([face_ids], append=True, repair=False)
            if not c.is_watertight:
                continue
            volume = float(np.einsum("ij,ij->i", c.triangles[:,0],
                                     np.cross(c.triangles[:,1],c.triangles[:,2])).sum()/6)
            shells.append({"component_index":i,"bounds":c.bounds.tolist(),
                           "watertight":True,"winding_consistent":bool(c.is_winding_consistent),
                           "signed_volume":volume,"triangle_count":len(c.faces)})
        pairs = []
        eps = max(mesh.extents) * 1e-8
        for outer in shells:
            for inner in shells:
                if outer["component_index"] == inner["component_index"]:
                    continue
                o, b = np.array(outer["bounds"]), np.array(inner["bounds"])
                if np.all(b[0] > o[0] + eps) and np.all(b[1] < o[1] - eps):
                    pairs.append({"outer": outer["component_index"],
                                  "inner": inner["component_index"],
                                  "status": "strict_bounding_box_nesting_candidate_only"})
        record.update(model_id=path.stem, boundary_component_count=len(groups),
                      closed_boundary_components=shells, nested_bounds_candidates=pairs)
        results.append(record)
        if index % 10 == 0:
            print(f"Shell candidate screen: {index} files", flush=True)
    obj = {"date": "2026-10-07", "scope": "all 93 supplied complex STL files",
           "method": "working mesh boundary components and strictly nested axis-aligned bounds",
           "limits": ["No full containment or boundary-intersection proof",
                      "No candidate is not proof that no internal void exists",
                      "Disconnected surfaces may represent bodies, errors, or cavity walls",
                      "Original sources were not changed"], "files": results}
    (OUT / "enclosed_void_candidate_screen.json").write_text(json.dumps(obj, indent=2)+"\n")
    candidates = [r["model_id"] for r in results if r["nested_bounds_candidates"]]
    print("Nested-bound candidates:", candidates, flush=True)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    records = []
    for name, z in [("rib",13), ("boss",13), ("fillet_boss",10)]:
        mesh, record = working_mesh(SIMPLE / f"{name}.stl")
        cx = float(mesh.bounds.mean(axis=0)[0])
        planes = [(0,cx,(1,2)), (2,z,(0,1))]
        record.update(model_id=name, origin="user_supplied_stl",
                      section_planes=[{"axis":"XYZ"[a],"position":p} for a,p,_ in planes],
                      figure=figure(name,mesh,planes))
        if name == "rib":
            record["projection_bounds"] = [[5,23.5,8],[45,26.5,18]]
            record["vertex_coordinate_levels"] = [np.unique(mesh.vertices[:,i]).tolist() for i in range(3)]
        if name == "boss":
            center = mesh.bounds.mean(axis=0)[:2]
            v = mesh.vertices[np.isclose(mesh.vertices[:,2],18,atol=1e-7,rtol=0)]
            r = np.linalg.norm(v[:,:2]-center,axis=1)
            ring = r[r>1e-6]
            record["top_ring"] = {"center_xy":center.tolist(),"z":18,
                                  "radius_range":[float(ring.min()),float(ring.max())]}
            record["projection_height"] = 18-8
        if name == "fillet_boss":
            center = mesh.bounds.mean(axis=0)[:2]
            radial = np.linalg.norm(mesh.vertices[:,:2]-center,axis=1)
            keep = (radial > 6.2) & (mesh.vertices[:,2] > 8.01)
            rz = np.column_stack([radial[keep],mesh.vertices[keep,2]])
            design = np.column_stack([2*rz[:,0],2*rz[:,1],np.ones(len(rz))])
            answer, *_ = np.linalg.lstsq(design,(rz*rz).sum(axis=1),rcond=None)
            cc = answer[:2]
            radius = np.sqrt(answer[2]+np.dot(cc,cc))
            record["annular_ridge_radial_profile_fit"] = {
                "method":"circle fit to mesh vertices with radial>6.2 and z>8.01",
                "center_r_z":cc.tolist(),"radius":float(radius),
                "max_radial_residual":float(np.abs(np.linalg.norm(rz-cc,axis=1)-radius).max()),
                "interpretation":"rounded annular projection; Fillet assignment unconfirmed"}
        records.append(record)
    for name, opened in [("teaching_enclosed_void",False),("teaching_open_void",True)]:
        mesh = voxel_boundary(opened)
        path = OUT / f"{name}.stl"
        mesh.export(path)
        planes = [(0,10,(1,2)),(2,18,(0,1))]
        records.append({"model_id":name,"origin":"synthetic_teaching_model",
                        "source_path":str(path),"source_sha256":hashlib.sha256(path.read_bytes()).hexdigest(),
                        "construction":"exposed boundaries of occupied coordinate-grid cells",
                        "outer_bounds":[[0,0,0],[20,20,20]],
                        "void_bounds":[[4,4,4],[16,16,20 if opened else 16]],
                        "enclosure":"open_to_exterior" if opened else "enclosed",
                        "opening_direction":"+Z" if opened else None,
                        "enclosure_evidence":"explicit occupied-cell construction, all boundary faces enumerated",
                        "working_watertight":bool(mesh.is_watertight),
                        "working_winding_consistent":bool(mesh.is_winding_consistent),
                        "boundary_component_count":len(mesh.split(only_watertight=False)),
                        "expected_material_volume":8000-144*(16 if opened else 12),
                        "mesh_signed_volume":float(mesh.volume),
                        "coordinate_unit":"input_units","physical_unit":"unknown",
                        "section_planes":[{"axis":"XYZ"[a],"position":p} for a,p,_ in planes],
                        "figure":figure(name,mesh,planes)})
    (OUT / "supplement_mesh_observations.json").write_text(json.dumps({
        "date":"2026-10-07", "generator":"tools/inspect_vocabulary_supplement.py", "models":records},indent=2)+"\n")
    print("Saved three supplied-model views and two synthetic teaching models.", flush=True)
    screen_shells()


if __name__ == "__main__":
    main()
