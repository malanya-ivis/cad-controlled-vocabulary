"""Read STL examples and save mesh diagnostics and derived inspection figures.

Run using the cad-structure-search project's existing Python environment.
Original STL files are read only. Dimensions are input coordinate units.
"""
from pathlib import Path
import hashlib
import json
import numpy as np
import trimesh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

ROOT = Path(__file__).resolve().parents[1]
DATA = Path('/home/malanya/projects/cad-structure-search/data/simple_CAD_dataset')
OUT = ROOT / 'mold-cad-vocabulary/80_Assets/cad_examples'


def draw_mesh(ax, mesh):
    collection = Poly3DCollection(mesh.triangles, facecolor='#7db9d8',
                                  edgecolor='#35566b', linewidth=0.12, alpha=1)
    ax.add_collection3d(collection)
    lo, hi = mesh.bounds
    for setter, a, b in zip((ax.set_xlim, ax.set_ylim, ax.set_zlim), lo, hi):
        pad = (b-a)*0.04
        setter(a-pad, b+pad)
    ax.set_box_aspect(mesh.extents.copy())
    ax.view_init(elev=45, azim=-60)
    ax.set_xlabel('X', fontsize=7)
    ax.set_ylabel('Y', fontsize=7)
    ax.set_zlabel('Z', fontsize=7)
    ax.tick_params(labelsize=6)


def draw_section(ax, mesh, axis, position, displayed_axes, title):
    origin = mesh.bounds.mean(axis=0)
    origin[axis] = position
    normal = np.eye(3)[axis]
    section = mesh.section(plane_origin=origin, plane_normal=normal)
    if section is not None:
        for line in section.discrete:
            ax.plot(line[:, displayed_axes[0]], line[:, displayed_axes[1]],
                    color='#194d75', linewidth=1.4)
    ax.set_aspect('equal')
    ax.grid(alpha=0.25)
    ax.set_xlabel('XYZ'[displayed_axes[0]]+' (input units)')
    ax.set_ylabel('XYZ'[displayed_axes[1]]+' (input units)')
    ax.set_title(title, fontsize=10)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    meshes = {}
    records = []
    for p in sorted(DATA.glob('*.stl')):
        raw = trimesh.load_mesh(p, process=False)
        threshold = float(max(raw.extents)**2 * 1e-14)
        keep = raw.area_faces > threshold
        welded = raw.copy()
        welded.merge_vertices()
        working = trimesh.Trimesh(vertices=raw.vertices,
                                  faces=raw.faces[keep], process=True)
        meshes[p.stem] = working
        records.append({
            'file': p.name, 'source_path': str(p),
            'sha256': hashlib.sha256(p.read_bytes()).hexdigest(),
            'unit': 'input_units', 'physical_unit': 'unknown',
            'bounds': raw.bounds.tolist(), 'extents': raw.extents.tolist(),
            'raw_triangle_count': len(raw.faces),
            'discarded_near_zero_area_faces_for_figures': int((~keep).sum()),
            'area_threshold_input_units_squared': threshold,
            'watertight_after_vertex_merge_before_face_removal': bool(welded.is_watertight),
            'working_triangle_count': len(working.faces),
            'working_watertight': bool(working.is_watertight),
            'working_winding_consistent': bool(working.is_winding_consistent),
            'self_intersection_check': 'not_performed',
            'semantic_label_status': 'not_inferred_from_filename',
        })
    fig = plt.figure(figsize=(16, 18))
    for i, (name, mesh) in enumerate(meshes.items(), 1):
        ax = fig.add_subplot(7, 3, i, projection='3d')
        draw_mesh(ax, mesh)
        ax.set_title(name+'.stl', fontsize=10)
    fig.suptitle('21 STL models: mesh overview / dimensions in input coordinate units', fontsize=15)
    fig.tight_layout(rect=(0, 0, 1, 0.97))
    fig.savefig(OUT/'dataset_overview.png', dpi=150)
    plt.close(fig)

    levels = {'counterbore': 15, 'countersink': 10, 'rectpocket': 12, 'rib_cross': 12}
    for name, z in levels.items():
        mesh = meshes[name]
        fig = plt.figure(figsize=(15, 4.8))
        ax = fig.add_subplot(1, 3, 1, projection='3d')
        draw_mesh(ax, mesh)
        ax.set_title(name+'.stl: surface mesh')
        ax = fig.add_subplot(1, 3, 2)
        cx = float(mesh.bounds.mean(axis=0)[0])
        draw_section(ax, mesh, 0, cx, (1, 2), f'Vertical section: X = {cx:g}')
        ax = fig.add_subplot(1, 3, 3)
        draw_section(ax, mesh, 2, z, (0, 1), f'Horizontal section: Z = {z:g}')
        fig.suptitle('STL-derived geometry; physical unit unknown; section lines are surface intersections')
        fig.tight_layout(rect=(0, 0, 1, 0.92))
        fig.savefig(OUT/f'{name}_views.png', dpi=160)
        plt.close(fig)

    # Measure vertex geometry, rather than using the filename as a label.
    measures = {}
    for name in ['counterbore', 'countersink']:
        raw = trimesh.load_mesh(DATA/f'{name}.stl', process=False)
        vertices = np.unique(raw.vertices, axis=0)
        center = raw.bounds.mean(axis=0)[:2]
        radial = np.linalg.norm(vertices[:, :2]-center, axis=1)
        inner = vertices[radial < min(raw.extents[:2])/2]
        rings = []
        for z in np.unique(inner[:, 2]):
            r = np.linalg.norm(inner[np.isclose(inner[:, 2], z, atol=1e-7, rtol=0), :2]-center, axis=1)
            rings.append({'z': float(z), 'r_min': float(r.min()),
                          'r_max': float(r.max()), 'vertex_count': len(r)})
        measures[name] = {'center_xy': center.tolist(), 'inner_vertex_rings': rings}
    raw = trimesh.load_mesh(DATA/'rectpocket.stl', process=False)
    vertices = np.unique(raw.vertices, axis=0)
    interior = vertices[(vertices[:,0] > raw.bounds[0,0]) & (vertices[:,0] < raw.bounds[1,0])]
    lo,hi=interior.min(axis=0),interior.max(axis=0)
    measures['rectpocket'] = {'recess_bounds': [lo.tolist(),hi.tolist()],
                              'recess_size': (hi-lo).tolist(),
                              'base_below_floor': float(lo[2]-raw.bounds[0,2])}
    raw = trimesh.load_mesh(DATA/'rib_cross.stl', process=False)
    vertices = np.unique(raw.vertices,axis=0)
    measures['rib_cross']={'vertex_coordinate_levels': [np.unique(vertices[:,i]).tolist() for i in range(3)]}
    (OUT/'mesh_observations.json').write_text(json.dumps({
        'schema_version': 1, 'dataset_path': str(DATA),
        'method': 'STL vertices and in-memory surface sections; not CAD feature history or design intent',
        'files': records, 'selected_measurements': measures,
    }, ensure_ascii=False, indent=2)+'\n')
    print(f'Inspected {len(records)} STL files; wrote overview, four detail figures and measured geometry JSON.')
    for r in records:
        if r['discarded_near_zero_area_faces_for_figures']:
            print(r['file'], 'in-memory discarded faces:',r['discarded_near_zero_area_faces_for_figures'])


if __name__ == '__main__':
    main()
