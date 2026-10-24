"""Les mesures du protocole des essais (journal.md, 2026-10-24), pour une liste d'essais d'un axe :
  (a) la netteté : la silhouette entière et la bande du bord, en % du rendu sur gris collé (seuils : 95 et 90) ;
  (b) la place : l'écart entre le haut de sa silhouette et le crâne de son squelette, en têtes (seuil : 1,0 ; ses
      cheveux dépassent le crâne du squelette : de 0,40 à 0,72 tête sur les 12 images validées du 2026-10-22) ;
  (c) l'objet tenu : l'écart moyen, sur sa partie figée, entre l'image finale et le rendu sur gris collé (seuil : 6 sur 255).
Les critères à l'œil (l'anatomie, l'identité, la posture) se notent à part.

  KEBAB_AXE=<axe> ~/venvs/kebab/bin/python pipeline/mesures/protocole.py <essai> [...]
"""
import json
import os
import sys
from pathlib import Path

import cv2
import numpy as np
import yaml
from PIL import Image

RACINE = Path(__file__).resolve().parent.parent.parent
CONFIG = yaml.safe_load((RACINE / "config.yaml").read_text())
AXE = os.environ.get("KEBAB_AXE", "table-du-fond")
I = Path(CONFIG["sorties_root"]) / "essais" / "integration" / AXE
NOMS, sys.argv = sys.argv[1:], sys.argv[:1]
sys.path.insert(0, str(RACINE / "pipeline"))
import essai_integration as E  # noqa: E402


def lap(im):
    g = cv2.cvtColor(np.asarray(im.convert("RGB")), cv2.COLOR_RGB2GRAY).astype(np.float32)
    return np.abs(cv2.Laplacian(g, cv2.CV_32F, ksize=3))


def mesurer(nom):
    r = json.loads((I / f"{nom}.json").read_text())
    perso, boite = r["perso"], r["boite"]
    d = I / nom
    k = E.TRAVAIL / (boite[2] - boite[0])
    a = (np.asarray(Image.open(d / "3_detourage.png").convert("L")) > 128).astype(np.uint8)
    a2 = cv2.erode(a, np.ones((5, 5), np.uint8)).astype(bool)
    a12 = cv2.erode(a, np.ones((25, 25), np.uint8)).astype(bool)
    colle = Image.open(d / "4_colle-fond.png").convert("RGB").crop(boite).resize((E.TRAVAIL, E.TRAVAIL), Image.LANCZOS)
    final = Image.open(d / "6_apres-visage.png").convert("RGB")
    ref, fin = lap(colle), lap(final)
    nettete = 100 * fin[a2].mean() / ref[a2].mean()
    bande = a2 & ~a12
    nettete_bord = 100 * fin[bande].mean() / ref[bande].mean()
    # (b) le crâne de son squelette, dans l'image de travail
    E.POSE.pop(perso, None)
    if r.get("pose"):
        E.POSE[perso] = r["pose"]
    E.POSTURE[0] = r.get("posture") or "mange"
    camera = json.loads((E.DECORS / AXE / "camera.json").read_text())["camera"]
    c = E.corps(perso)
    (cx, cy), (mx, my) = E.projeter(camera, [c["crane"], c["menton"]])
    tete = (my - cy) * k
    ys = np.nonzero(a.any(axis=1))[0]
    haut = float(ys.min()) if len(ys) else float("nan")
    ecart_tetes = abs(haut - (cy - boite[1]) * k) / tete
    # (c) l'objet tenu
    objet = None
    if (d / "2_objet.png").exists():
        m = np.asarray(Image.open(d / "2_objet.png").convert("L")) > 128
        m = cv2.erode(m.astype(np.uint8), np.ones((5, 5), np.uint8)).astype(bool)
        if m.any():
            objet = float(np.abs(np.asarray(final, np.float32) - np.asarray(colle, np.float32))[m].mean())
    return {"essai": nom, "nettete": round(nettete), "bord": round(nettete_bord), "ecart_tetes": round(ecart_tetes, 2),
            "objet": None if objet is None else round(objet, 1),
            "ok_mesures": nettete >= 95 and nettete_bord >= 90 and ecart_tetes <= 1.0 and (objet is None or objet <= 6)}


if __name__ == "__main__":
    for nom in NOMS:
        try:
            m = mesurer(nom)
        except FileNotFoundError as e:
            print(f"{nom} : manque {Path(e.filename).name}")
            continue
        print(f"{m['essai']:28s} netteté {m['nettete']:3d} % bord {m['bord']:3d} % ; place {m['ecart_tetes']:.2f} tête ;"
              f" objet {'—' if m['objet'] is None else m['objet']} ; mesures {'OK' if m['ok_mesures'] else 'NON'}")
