"""Assemble un plan à plusieurs persos. Chacun est généré seul à sa place, avec son seul LoRA (pipeline/essai_integration.py,
méthode B) ; ici, ils sont collés sur le fond du plus loin au plus près de la caméra : le plus proche cache les autres, et
les objets « devant » (camera.json) les cachent tous. Pas de nouvelle génération : on choisit la meilleure variante de chacun,
puis on les assemble.

  ~/venvs/kebab/bin/python pipeline/composer_scene.py <axe> <sortie.png> <essai> [<essai> ...]
  ex. : composer_scene.py table-du-fond duo.png maelle_B_2001 sky_B_2001

Un essai est le nom d'une variante dans <sorties_root>/essais/integration/<axe>/ (son image, son dossier d'étapes, ses
réglages .json).
"""
import json
import math
import sys
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from essai_integration import DECORS, ESSAIS, PERSOS, coller_cadre   # noqa: E402


def distance(perso, camera):
    return math.hypot(PERSOS[perso]["x"] - camera["x"], 0.62 - camera["y"])


def composer(axe, essais):
    recalage = json.loads((DECORS / axe / "camera.json").read_text())
    camera, devant = recalage["camera"], recalage.get("devant", ())
    image = Image.open(DECORS / axe / "fond_v1.png").convert("RGB")
    reglages = [(nom, json.loads((ESSAIS / axe / f"{nom}.json").read_text())) for nom in essais]
    for nom, r in sorted(reglages, key=lambda e: -distance(e[1]["perso"], camera)):
        etapes = ESSAIS / axe / nom
        # comme à la fin de son essai : le perso dessiné sur gris, collé dans son cadre, puis ses pixels repassés (la lumière
        # du décor, le visage) dans sa boîte de travail
        gris = Image.open(etapes / "2_sur-gris.png").convert("RGB")
        _, image = coller_cadre(r["perso"], gris, tuple(r["cadre"]), camera, image, devant)
        x0, y0, x1, _ = r["boite"]
        taille = (x1 - x0, x1 - x0)
        repasse = Image.open(etapes / "6_apres-visage.png").convert("RGB").resize(taille, Image.LANCZOS)
        alpha = Image.open(etapes / "7_detourage-final.png").convert("L").resize(taille, Image.LANCZOS)
        image.paste(repasse, (x0, y0), alpha)
    return image


if __name__ == "__main__":
    axe, sortie, essais = sys.argv[1], Path(sys.argv[2]), sys.argv[3:]
    sortie.parent.mkdir(parents=True, exist_ok=True)
    composer(axe, essais).save(sortie)
    print(sortie)
