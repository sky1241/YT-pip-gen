"""Les fonds v2 : chaque fond_v1.png lissé, ses taches de peinture effacées, ses bords gardés (2026-10-22). Les fonds peints
par ChatGPT ont des murs et des vitres en plaques de couleur irrégulières : à côté d'un perso net, l'auteur y voyait « une
espèce de peinture abstraite » ; « l'effet pastel on le vire, tant que ça permet d'avoir une image nette ». Filtre d'OpenCV
qui lisse en gardant les bords (edgePreservingFilter, filtre récursif, sigma_s 40, sigma_r 0,25) : les murs deviennent des
dégradés, les cadres, la plante et les objets restent nets. Le v1 n'est pas touché.

  ~/venvs/kebab/bin/python pipeline/lisser_fonds.py [dossier des décors]
"""
import sys
from pathlib import Path

import cv2

RACINE = Path(__file__).resolve().parent.parent
SIGMA_S, SIGMA_R = 40, 0.25


def lisser(source, cible):
    image = cv2.imread(str(source), cv2.IMREAD_COLOR)
    cv2.imwrite(str(cible), cv2.edgePreservingFilter(image, flags=cv2.RECURS_FILTER, sigma_s=SIGMA_S, sigma_r=SIGMA_R))


def dernier_fond(dossier):
    """Le fond le plus récent d'un axe (fond_v2.png s'il existe, sinon fond_v1.png)."""
    versions = sorted(Path(dossier).glob("fond_v*.png"), key=lambda f: int(f.stem.split("_v")[1]))
    return versions[-1]


if __name__ == "__main__":
    decors = Path(sys.argv[1]) if len(sys.argv) > 1 else RACINE / "image" / "decors"
    for v1 in sorted(decors.rglob("fond_v1.png")):
        v2 = v1.with_name("fond_v2.png")
        if v2.exists():
            print("existe déjà :", v2.relative_to(RACINE)); continue
        lisser(v1, v2)
        print(v2.relative_to(RACINE))
