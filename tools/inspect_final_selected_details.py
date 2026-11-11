"""Mesh sections for four complex models and a simple chamfer comparison."""
from pathlib import Path
import json
import numpy as np
import trimesh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from inspect_simple_cad_dataset import draw_section

ROOT = Path(__file__).resolve().parents[1]
DATA = Path('/home/malanya/projects/cad-structure-search/data/final_selected/stl')
OUT = ROOT / 'mold-cad-vocabulary/80_Assets/final_selected'


def circle_loops(mesh, axis, side):
    origin = mesh.bounds.mean(axis=0)
    origin[axis] = mesh.bounds[side, axis] + (1 if side == 0 else -1)*mesh.extents[axis]*1e-4
    section = mesh.section(plane_origin=origin, plane_normal=np.eye(3)[axis])
    other = [i for i in range(3) if i != axis]
    records = []
    for curve in section.discrete:
        if len(curve) < 12:
            continue
        xy = curve[:-1, other]
        # Least-squares circle of the actual section outline, not its filename.
        design = np.column_stack([2*xy[:,0], 2*xy[:,1], np.ones(len(xy))])
        answer, *_ = np.linalg.lstsq(design, np.sum(xy*xy, axis=1), rcond=None)
        center = answer[:2]
        radius = np.sqrt(answer[2]+np.dot(center,center))
        residual = np.max(np.abs(np.linalg.norm(xy-center,axis=1)-radius))
        if residual > radius*0.01:
            continue
        records.append({'axis':axis,'exterior_side':side,'plane_position':float(origin[axis]),
                        'center_in_plane':center.tolist(),'displayed_axes':other,
                        'radius':float(radius),'max_radial_residual':float(residual)})
    return records


def main():
    records=[]
    for name in ['1400','4423','8972','7145','simple_chamfer']:
        source = DATA/f'{name}.stl' if name != 'simple_chamfer' else DATA.parents[1]/'simple_CAD_dataset/chamfer.stl'
        raw=trimesh.load_mesh(source,process=False)
        area_threshold=float(max(raw.extents)**2*1e-14)
        keep=raw.area_faces>area_threshold
        mesh=trimesh.Trimesh(vertices=raw.vertices,faces=raw.faces[keep],process=True)
        center=mesh.bounds.mean(axis=0)
        if name=='1400':
            planes=[(0,0,(1,2)),(1,0.022225,(0,2)),(1,0.034925,(0,2))]
        else:
            planes=[(0,float(center[0]),(1,2)),(1,float(center[1]),(0,2)),(2,float(center[2]),(0,1))]
        fig, axes=plt.subplots(1,4,figsize=(18,4.6))
        if name == 'simple_chamfer':
            axes[0].axis('off')
            axes[0].text(0.05, 0.5, 'Comparison source:\nsimple_CAD_dataset/chamfer.stl\n\nPlanar edge transition\nseen in the section below.', va='center')
        else:
            axes[0].imshow(plt.imread(OUT/f'{name}_overview.png'))
            axes[0].axis('off');axes[0].set_title(name+'.stl: full mesh')
        for ax,(axis,pos,displayed) in zip(axes[1:],planes):
            draw_section(ax,mesh,axis,pos,displayed,f'{"XYZ"[axis]} = {pos:.6g}')
        fig.suptitle('Original STL coordinate units; section curves are mesh surface intersections')
        fig.tight_layout(rect=(0,0,1,0.92));fig.savefig(OUT/f'{name}_sections.png',dpi=145);plt.close(fig)
        # Plane normals expose planar bevel candidates without inferring CAD operations.
        normals, counts = np.unique(np.round(mesh.face_normals,6),axis=0,return_counts=True)
        major = sorted(zip(normals.tolist(),counts.tolist()),key=lambda p:p[1],reverse=True)[:20]
        record={'model_id':name,'source_path':str(source),'bounds':raw.bounds.tolist(),'extents':raw.extents.tolist(),
                'raw_triangle_count':len(raw.faces),'discarded_near_zero_area_faces':int((~keep).sum()),
                'working_watertight':bool(mesh.is_watertight),
                'working_winding_consistent':bool(mesh.is_winding_consistent),
                'section_planes':[{'normal_axis':'XYZ'[a],'position':p} for a,p,_ in planes],
                'largest_repeated_face_normals':[{'normal':n,'triangle_count':c} for n,c in major],
                'physical_unit':'unknown','self_intersection_check':'not_performed'}
        if name=='1400':
            record['exterior_circle_fits']=[fit for axis in [0,2] for side in [0,1] for fit in circle_loops(mesh,axis,side)]
        if name=='4423':
            record['vertex_z_levels']=np.unique(mesh.vertices[:,2]).tolist()
        if name=='8972':
            rays=[]
            for z in [.0133,.0195,.0257]:
                for x in [-.0031,.0031]:
                    hits, _, _ = mesh.ray.intersects_location(
                        ray_origins=np.array([[x,-.04,z]]),
                        ray_directions=np.array([[0,1,0]]))
                    rays.append({'x':x,'z':z,'ray_origin_y':-.04,
                                 'ray_direction':[0,1,0],
                                 'surface_intersection_y':sorted(hits[:,1].tolist())})
            (OUT/'8972_ray_observations.json').write_text(json.dumps({
                'source_path':str(source),
                'method':'Six +Y rays through centers of observed recess openings; coordinates in input_units',
                'rays':rays},indent=2)+'\n')
            fig, axes=plt.subplots(1,3,figsize=(14,5))
            for ax,(axis,pos,displayed) in zip(axes,[(2,.0133,(0,1)),(2,.0195,(0,1)),(1,-.0307,(0,2))]):
                draw_section(ax,mesh,axis,pos,displayed,f'{"XYZ"[axis]} = {pos:.6g}')
            fig.suptitle('8972: recess floors / positive-X middle opening crosses the rear wall')
            fig.tight_layout(rect=(0,0,1,.92))
            fig.savefig(OUT/'8972_recess_review.png',dpi=145)
            plt.close(fig)
        records.append(record)
    (OUT/'selected_sections.json').write_text(json.dumps({'method':'Independent STL sections; draft semantic mapping requires image review','models':records},indent=2)+'\n')
    print('Saved five detailed section figures and mesh evidence JSON.')
    for r in records:
        print(r['model_id'],'watertight',r['working_watertight'],'removed_faces',r['discarded_near_zero_area_faces'])


if __name__=='__main__':
    main()
