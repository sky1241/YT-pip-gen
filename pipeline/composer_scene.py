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
from essai_integration import DECORS, ESSAIS, PERSOS, TRAVAIL, avec_lisere, coller_cadre, sans_frange   # noqa: E402
from lisser_fonds import dernier_fond  # noqa: E402


def distance(perso, camera):
    return math.hypot(PERSOS[perso]["x"] - camera["x"], 0.62 - camera["y"])


def composer(axe, essais):
    recalage = json.loads((DECORS / axe / "camera.json").read_text())
    camera, devant = recalage["camera"], recalage.get("devant", ())
    image = Image.open(dernier_fond(DECORS / axe)).convert("RGB")
    reglages = [(nom, json.loads((ESSAIS / axe / f"{nom}.json").read_text())) for nom in essais]
    for nom, r in sorted(reglages, key=lambda e: -distance(e[1]["perso"], camera)):
        etapes = ESSAIS / axe / nom
        x0, y0, x1, _ = r["boite"]
        taille = (x1 - x0, x1 - x0)
        if r["methode"] in ("B", "D"):
            # comme à la fin de son essai : le perso dessiné sur gris, collé dans son cadre, puis ses pixels repassés (la
            # lumière du décor, le visage) dans sa boîte de travail
            gris = Image.open(etapes / "2_sur-gris.png").convert("RGB")
            _, image = coller_cadre(r["perso"], gris, tuple(r["cadre"]), camera, image, devant)
            alpha = etapes / "7_detourage-final.png"
        else:
            # C : le perso dessiné dans le décor, détouré (le décor autour de lui reste celui d'origine) s'il l'a été
            detoures = sorted(etapes.glob("7_detourage-toonout.png")) + sorted(etapes.glob("7_detourage-isnet.png"))
            alpha = detoures[0] if detoures else etapes / "3_zone.png"
        repasse = Image.open(etapes / "6_apres-visage.png").convert("RGB")
        if r["methode"] in ("B", "D") and r.get("lisere"):   # sa frange grise retirée et son liseré, comme à la fin de son essai
            silhouette = Image.open(etapes / "3_detourage.png")
            repasse = sans_frange(repasse, silhouette, Image.open(etapes / "2_sur-gris.png"), echelle=TRAVAIL / taille[0])
            repasse = avec_lisere(repasse, silhouette, Image.open(alpha), echelle=TRAVAIL / taille[0])
        image.paste(repasse.resize(taille, Image.LANCZOS), (x0, y0), Image.open(alpha).convert("L").resize(taille, Image.LANCZOS))
    return image


if __name__ == "__main__":
    axe, sortie, essais = sys.argv[1], Path(sys.argv[2]), sys.argv[3:]
    sortie.parent.mkdir(parents=True, exist_ok=True)
    composer(axe, essais).save(sortie)
    print(sortie)
