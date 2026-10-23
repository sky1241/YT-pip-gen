"""Découpe une planche d'objets (faite dans ChatGPT, sur un fond gris uni) en un fichier transparent par objet, de gauche à
droite, au ras de son trait (essai_integration.detoure_au_trait). Le gris du fond enfermé dans un objet part aussi (dans
l'anse d'une tasse) : une tache de la couleur du fond, unie comme lui ; une cuillère en argent, grise mais nuancée, reste.

  ~/venvs/kebab/bin/python pipeline/decouper_accessoire.py <planche.png> <dossier> <nom1> [<nom2> ...]

Sortie : <dossier>/<nom>_v1.png (RGBA). On n'écrase jamais un fichier existant. Un objet fait de deux morceaux qui ne se
touchent pas (une tasse et sa cuillère posée à côté) sort en deux : relancer avec un nom de plus, ou les regrouper à la main.
Des objets qui se touchent ne se découpent pas : redemander la planche avec du fond gris entre eux.
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


def cle_du_fond(image, ecart=22):
    """Tout ce qui n'est pas le gris uni du fond, plein (ses creux bouchés) : le détoureur d'anime (isnet) ne garde que le
    sujet et jetait les assiettes sous les pizzas (2026-10-23) ; les deux masques sont réunis."""
    g = np.asarray(image, np.float32)
    # le gris du fond n'est pas uni sur toute la planche (plus clair en bas sur celle des pizzas) : un plan par couleur,
    # ajusté sur les quatre bords de l'image
    h, w = g.shape[:2]
    yy, xx = np.mgrid[0:h, 0:w]
    tour = np.zeros((h, w), bool); tour[:8] = tour[-8:] = True; tour[:, :8] = tour[:, -8:] = True
    A = np.stack([np.ones(tour.sum()), xx[tour], yy[tour]], axis=1)
    coefs = np.linalg.lstsq(A, g[tour], rcond=None)[0]
    G = coefs[0] + xx[..., None] * coefs[1] + yy[..., None] * coefs[2]
    m = cv2.morphologyEx((np.abs(g - G).max(axis=2) > ecart).astype(np.uint8), cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
    # le fond relié à un bord de l'image (n'importe lequel : sur la planche des pizzas, les assiettes coupent l'image en deux) ;
    # le reste du fond est enfermé dans un objet
    n, lab = cv2.connectedComponents((1 - m).astype(np.uint8), connectivity=4)
    dehors = np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))
    plein = m.copy()
    plein[(m == 0) & ~np.isin(lab, dehors[dehors > 0])] = 1
    return plein * 255


def decouper(planche, noms):
    image = Image.open(planche).convert("RGB")
    masque = np.maximum(np.asarray(E.detourage_net(image), np.uint8), cle_du_fond(image).astype(np.uint8))
    alpha = E.detoure_au_trait(image, masque)
    alpha[trous_du_fond(image, alpha > 0.5)] = 0
    alpha = cv2.GaussianBlur(alpha, (0, 0), 0.5)
    n, lab, st, _ = cv2.connectedComponentsWithStats((alpha > 0.5).astype(np.uint8), connectivity=8)
    objets = sorted((k for k in range(1, n) if st[k][4] >= AIRE_MIN * alpha.size), key=lambda k: st[k][0])
    if len(objets) != len(noms):
        # des objets qui se touchent ne se séparent pas bien : sur la planche des pizzas (2026-10-23), les assiettes se
        # chevauchaient, et chaque coupe emportait un bout du voisin. Redemander la planche avec du fond entre eux
        sys.exit(f"{len(objets)} objets trouvés pour {len(noms)} noms : {[tuple(int(v) for v in st[k][:4]) for k in objets]}")
    rgba = np.dstack([np.asarray(image), (alpha * 255).astype(np.uint8)])
    sorties = []
    for nom, k in zip(noms, objets):
        x, y, w, h, _ = st[k]
        # son bord adouci, sans déborder sur un objet qui le touche
        sien = cv2.dilate((lab == k).astype(np.uint8), np.ones((5, 5), np.uint8)).astype(bool) & ((lab == k) | (lab == 0))
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
