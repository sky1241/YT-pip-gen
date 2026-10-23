"""Découpe une planche d'objets (faite dans ChatGPT, sur un fond gris uni) en un fichier transparent par objet, de gauche à
droite, au ras de son trait (essai_integration.detoure_au_trait). Le gris du fond enfermé dans un objet part aussi (dans
l'anse d'une tasse) : une tache de la couleur du fond, unie comme lui ; une cuillère en argent, grise mais nuancée, reste.

  ~/venvs/kebab/bin/python pipeline/decouper_accessoire.py <planche.png> <dossier> <nom1> [<nom2> ...]

Sortie : <dossier>/<nom>_v1.png (RGBA). On n'écrase jamais un fichier existant. Un objet fait de deux morceaux qui ne se
touchent pas (une tasse et sa cuillère posée à côté) sort en deux : relancer avec un nom de plus, ou les regrouper à la main.
"""
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image

ARGS, sys.argv = sys.argv[1:], sys.argv[:1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
import essai_integration as E   # noqa: E402

AIRE_MIN = 0.01                 # un objet couvre au moins 1 % de la planche (le reste : des miettes, des traits isolés)


def trous_du_fond(image, garde, ecart=14, ecart_type=5.0, aire_min=40):
    """Les taches de la couleur du fond (à moins de `ecart`) et unies comme lui (écart type sous `ecart_type`) restées dans
    les objets : elles partent."""
    g = np.asarray(image, np.float32)
    G = np.median(np.concatenate([g[:8].reshape(-1, 3), g[:, :8].reshape(-1, 3), g[:, -8:].reshape(-1, 3)]), axis=0)
    proche = (np.abs(g - G).max(axis=2) < ecart) & garde
    n, lab, st, _ = cv2.connectedComponentsWithStats(proche.astype(np.uint8), connectivity=8)
    trous = np.zeros(garde.shape, bool)
    for k in range(1, n):
        if st[k][4] >= aire_min and g[lab == k].std(axis=0).max() < ecart_type:
            trous |= lab == k
    return cv2.dilate(trous.astype(np.uint8), np.ones((3, 3), np.uint8)).astype(bool)   # leur bord mêlé de gris aussi


def decouper(planche, noms):
    image = Image.open(planche).convert("RGB")
    alpha = E.detoure_au_trait(image, np.asarray(E.detourage_net(image), np.uint8))
    alpha[trous_du_fond(image, alpha > 0.5)] = 0
    alpha = cv2.GaussianBlur(alpha, (0, 0), 0.5)
    n, lab, st, _ = cv2.connectedComponentsWithStats((alpha > 0.5).astype(np.uint8), connectivity=8)
    objets = sorted((k for k in range(1, n) if st[k][4] >= AIRE_MIN * alpha.size), key=lambda k: st[k][0])
    if len(objets) != len(noms):
        sys.exit(f"{len(objets)} objets trouvés pour {len(noms)} noms : {[tuple(int(v) for v in st[k][:4]) for k in objets]}")
    rgba = np.dstack([np.asarray(image), (alpha * 255).astype(np.uint8)])
    sorties = []
    for nom, k in zip(noms, objets):
        x, y, w, h, _ = st[k]
        sien = cv2.dilate((lab == k).astype(np.uint8), np.ones((5, 5), np.uint8)).astype(bool)   # son bord adouci seulement
        objet = rgba.copy()
        objet[..., 3] = np.where(sien, objet[..., 3], 0)
        x0, y0 = max(x - 12, 0), max(y - 12, 0)
        x1, y1 = min(x + w + 12, image.width), min(y + h + 12, image.height)
        sorties.append((nom, Image.fromarray(objet[y0:y1, x0:x1], "RGBA")))
    return sorties


def main():
    planche, dossier, noms = Path(ARGS[0]), Path(ARGS[1]), ARGS[2:]
    dossier.mkdir(parents=True, exist_ok=True)
    for nom, objet in decouper(planche, noms):
        chemin = dossier / f"{nom}_v1.png"
        if chemin.exists():
            sys.exit(f"{chemin} existe déjà : on n'écrase pas une référence")
        objet.save(chemin)
        print(chemin, objet.size)


if __name__ == "__main__":
    main()
