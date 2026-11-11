"""Generate full-mesh previews and inventory for the supplied 93 STL samples."""
from pathlib import Path
import csv
import hashlib
import json
import pyvista as pv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = Path('/home/malanya/projects/cad-structure-search/data/final_selected')
OUT = ROOT / 'mold-cad-vocabulary/80_Assets/final_selected'


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = {r['model_id']: r for r in csv.DictReader((DATA/'manifest.csv').open())}
    records = []
    plotter = pv.Plotter(off_screen=True, window_size=(480, 360))
    plotter.set_background('white')
    for i, source in enumerate(sorted((DATA/'stl').glob('*.stl'), key=lambda p: int(p.stem)), 1):
        mesh = pv.read(source)
        plotter.clear()
        plotter.enable_lightkit()
        plotter.add_mesh(mesh, color='#9dc5dc', smooth_shading=False)
        plotter.view_isometric()
        plotter.reset_camera()
        plotter.render()
        preview = OUT/f'{source.stem}_overview.png'
        plotter.screenshot(str(preview))
        b = list(mesh.bounds)
        step = DATA/'step'/f'{source.stem}.step'
        records.append({
            'model_id': source.stem,
            'source_path': str(source),
            'sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
            'manifest_class': manifest.get(source.stem, {}).get('assigned_class'),
            'triangle_count': int(mesh.n_cells),
            'bounds': [[b[0], b[2], b[4]], [b[1], b[3], b[5]]],
            'extents': [b[1]-b[0], b[3]-b[2], b[5]-b[4]],
            'coordinate_unit': 'input_units',
            'stl_physical_unit': 'unknown',
            'step_peer_exists': step.exists(),
            'step_peer_path': str(step) if step.exists() else None,
            'preview_path': str(preview.relative_to(ROOT/'mold-cad-vocabulary')),
            'local_feature_annotation': 'not_yet_reviewed',
        })
        if i % 20 == 0:
            print(f'Rendered {i} STL models', flush=True)
    plotter.close()
    for page in range((len(records)+23)//24):
        batch = records[page*24:(page+1)*24]
        fig, axes = plt.subplots(6, 4, figsize=(16, 19))
        for ax in axes.flat:
            ax.axis('off')
        for ax, record in zip(axes.flat, batch):
            ax.imshow(plt.imread(OUT/f'{record["model_id"]}_overview.png'))
            ax.set_title(record['model_id']+'.stl', fontsize=12)
        fig.suptitle(f'Full STL surface meshes — page {page+1}; local features not inferred from IDs', fontsize=16)
        fig.tight_layout(rect=(0, 0, 1, 0.97))
        fig.savefig(OUT/f'overview_page_{page+1}.png', dpi=125)
        plt.close(fig)
    (OUT/'inventory.json').write_text(json.dumps({
        'dataset_path': str(DATA/'stl'),
        'manifest_path': str(DATA/'manifest.csv'),
        'manifest_sha256': hashlib.sha256((DATA/'manifest.csv').read_bytes()).hexdigest(),
        'method': 'Full STL surface render; no triangle decimation; bounds in original coordinates',
        'files': records,
    }, ensure_ascii=False, indent=2)+'\n')
    print(f'Saved {len(records)} previews, four overview pages and input inventory.', flush=True)


if __name__ == '__main__':
    main()
