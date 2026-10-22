"""Mesure les gros plans de Sky d'une ou plusieurs variantes (axe 6) : « beard », « stubble », « mature male », la peau. Écrit
un JSON et affiche un résumé par variante."""
import os
from pathlib import Path

import yaml

RACINE = Path(__file__).resolve().parent.parent.parent
CONFIG = yaml.safe_load((RACINE / "config.yaml").read_text())
AXE = os.environ.get("KEBAB_AXE", "table-du-fond")       # l'axe des essais mesurés (variable KEBAB_AXE)
import json, sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(RACINE / "pipeline"))
import tagueur as T
from PIL import Image
I = Path(CONFIG["sorties_root"]) / "essais" / "integration" / AXE


def gros_plan(nom):
    r = json.loads((I / f"{nom}.json").read_text())
    x0, y0, x1, y1 = r["boite_visage_travail"]
    return Image.open(I / nom / "6_apres-visage.png").convert("RGB").crop((x0, y0, x1, y1))


def peau(im):
    a = np.asarray(im.resize((300, 300)), np.float32)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    m = (r > g + 15) & (g > b + 5) & (r > 90) & (r < 250)
    return np.median(a[m], axis=0)


sortie, graines, variantes = sys.argv[1], [int(g) for g in sys.argv[2].split(",")], sys.argv[3].split(",")
res = {}
for v in variantes:
    lignes = []
    for g in graines:
        nom = f"sky_D_{g}_{v}"
        im = gros_plan(nom)
        p = T.probabilites(im)
        m = peau(im)
        lignes.append({"graine": g, **{k: round(p[k], 3) for k in ("beard", "stubble", "facial_hair", "mature_male", "glasses", "cigarette")},
                       "peau_rouge": round(float(m[0]), 1), "peau_lum": round(float(m.mean()), 1)})
    res[v] = lignes
    b = [l["beard"] for l in lignes]
    print(f"{v:22s} beard moy {np.mean(b):.3f} (≥0,85 : {sum(x >= 0.85 for x in b)}/{len(b)}) ; stubble moy "
          f"{np.mean([l['stubble'] for l in lignes]):.2f} ; mature {np.mean([l['mature_male'] for l in lignes]):.2f} ; "
          f"peau ok {sum(l['peau_rouge'] >= 180 and l['peau_lum'] >= 113 for l in lignes)}/{len(lignes)} ; "
          f"cigarette {sum(l['cigarette'] >= 0.35 for l in lignes)}", flush=True)
json.dump(res, open(sortie, "w"), indent=1)
