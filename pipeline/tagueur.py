"""Le tagueur d'anime WD SwinV2 v3 (SmilingWolf, Apache 2.0) : la probabilité de quelques tags sur une image, pour compter un
trait sur une série d'images (la barbe, les cernes, l'âge de Sky) au lieu de le juger à l'œil seul. Sur le processeur,
environ 1 s par image ; jamais pendant une génération (la RAM).

  ~/venvs/kebab/bin/python pipeline/tagueur.py <image.png> [...]

La préparation de l'image recopie celle de la démo de SmilingWolf : fond blanc sous la transparence, carré complété en blanc,
448 × 448 en bicubique, BGR, valeurs de 0 à 255.
"""
import csv
import sys
from pathlib import Path

import numpy as np
import onnxruntime
import yaml
from PIL import Image

RACINE = Path(__file__).resolve().parent.parent
CONFIG = yaml.safe_load((RACINE / "config.yaml").read_text())
DOSSIER = Path(CONFIG["modeles_root"]) / "segmentation"
TAGS_SUIVIS = ["stubble", "beard_stubble", "facial_hair", "beard", "bags_under_eyes", "mature_male", "glasses",
               "heterochromia", "white_eyes", "cigarette"]
_SESSION, _NOMS = None, None


def charger():
    global _SESSION, _NOMS
    if _SESSION is None:
        onnxruntime.set_default_logger_severity(3)
        _SESSION = onnxruntime.InferenceSession(str(DOSSIER / "wd-swinv2-tagger-v3.onnx"), providers=["CPUExecutionProvider"])
        with open(DOSSIER / "wd-swinv2-tagger-v3_selected_tags.csv") as f:
            _NOMS = [ligne["name"] for ligne in csv.DictReader(f)]
    return _SESSION, _NOMS


def probabilites(image, tags=TAGS_SUIVIS):
    session, noms = charger()
    image = image.convert("RGBA")
    blanc = Image.new("RGBA", image.size, (255, 255, 255, 255))
    blanc.alpha_composite(image)
    image = blanc.convert("RGB")
    cote = max(image.size)
    carre = Image.new("RGB", (cote, cote), (255, 255, 255))
    carre.paste(image, ((cote - image.width) // 2, (cote - image.height) // 2))
    taille = session.get_inputs()[0].shape[1]
    carre = carre.resize((taille, taille), Image.BICUBIC)
    donnees = np.asarray(carre, np.float32)[:, :, ::-1][None]
    sortie = session.run(None, {session.get_inputs()[0].name: np.ascontiguousarray(donnees)})[0][0]
    return {t: float(sortie[noms.index(t)]) for t in tags}


if __name__ == "__main__":
    for chemin in sys.argv[1:]:
        p = probabilites(Image.open(chemin))
        print(Path(chemin).name, " ".join(f"{t}={v:.2f}" for t, v in p.items()))
