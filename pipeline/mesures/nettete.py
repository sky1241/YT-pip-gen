"""La netteté sur toute la silhouette (2026-10-22) : la première mesure (nettete.py) l'excluait sur 12 px de bord, là même où
le fondu flou restait. Ici : la silhouette entière (rétrécie de 2 px seulement, pour ne pas compter le bord lui-même), et la
bande du bord seule (de 2 à 12 px du bord), en % du rendu sur gris collé au même endroit.

  python nettete2.py <perso> <graines> <variante> [...]
"""
import os
from pathlib import Path

import yaml

RACINE = Path(__file__).resolve().parent.parent.parent
CONFIG = yaml.safe_load((RACINE / "config.yaml").read_text())
AXE = os.environ.get("KEBAB_AXE", "table-du-fond")       # l'axe des essais mesurés (variable KEBAB_AXE)
import sys
from pathlib import Path

import cv2
import json
import numpy as np
from PIL import Image

I = Path(CONFIG["sorties_root"]) / "essais" / "integration" / AXE
perso, graines, variantes = sys.argv[1], [int(g) for g in sys.argv[2].split(",")], sys.argv[3:]


def lap(im):
    g = cv2.cvtColor(np.asarray(im.convert("RGB")), cv2.COLOR_RGB2GRAY).astype(np.float32)
    return np.abs(cv2.Laplacian(g, cv2.CV_32F, ksize=3))


for v in variantes:
    tout, bande = [], []
    for g in graines:
        n = f"{perso}_D_{g}_{v}"
        r = json.loads((I / f"{n}.json").read_text())
        a = (np.asarray(Image.open(I / n / "3_detourage.png").convert("L")) > 128).astype(np.uint8)
        a2 = cv2.erode(a, np.ones((5, 5), np.uint8)).astype(bool)
        a12 = cv2.erode(a, np.ones((25, 25), np.uint8)).astype(bool)
        ref = lap(Image.open(I / n / "4_colle-fond.png").convert("RGB").crop(r["boite"]).resize((1024, 1024), Image.LANCZOS))
        fin = lap(Image.open(I / n / "6_apres-visage.png"))
        tout.append(100 * fin[a2].mean() / ref[a2].mean())
        m = a2 & ~a12
        bande.append(100 * fin[m].mean() / ref[m].mean())
    print(f"{perso:7s} {v:8s} toute la silhouette {np.mean(tout):4.0f} % ({', '.join(f'{x:.0f}' for x in tout)}) ;"
          f" la bande du bord {np.mean(bande):4.0f} % ({', '.join(f'{x:.0f}' for x in bande)})")
