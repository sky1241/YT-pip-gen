"""Étape 1 du premier vrai test (PLAN.md) : un perso seul, assis à sa place dans un fond du kebab, qui mange. Deux méthodes :

  A, « dans le fond » : sa place est masquée sur le fond, le modèle l'y dessine avec son LoRA (inpainting).
  B, « en calque »    : il est dessiné sur fond gris, là où son LoRA est le plus sûr, d'après une silhouette posée à sa place ;
                        puis détouré (isnet-anime), collé sur le fond, et une passe légère avec son LoRA fond sa lumière
                        dans celle du décor.

Les deux finissent par une passe sur le visage, en gros plan : sur ce plan large, sa tête fait 100 à 140 pixels, trop peu pour
que le LoRA y mette ses traits. Seul le perso détouré entre dans le fond, avec un détourage plein et net : tout le reste du
fond reste intact au pixel près, et les objets « devant » (les sauces) restent devant lui. Sa place et sa taille viennent de la
caméra recalée sur le fond (`camera.json`, pipeline/recaler_camera.py) et de sa taille dans la fiche.

  ~/venvs/kebab/bin/python pipeline/essai_integration.py <perso> <A|B> <graine> [--recomposer]

Avec --recomposer : seul le collage final est refait, depuis l'image de travail déjà générée (6_apres-visage.png).

Sortie : <sorties_root>/essais/etape1/<perso>_<méthode>_<graine>.png (le fond entier), ses étapes et ses réglages (.json).
ComfyUI doit tourner (pipeline/comfyui.py demarrer).
"""
import json
import math
import shutil
import sys
import time
from pathlib import Path

import cv2
import numpy as np
import onnxruntime
import yaml
from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lisser_fonds import dernier_fond        # noqa: E402
from recaler_camera import projeter          # noqa: E402
from test_lora import NEGATIF, QUALITE, TUILES, UNET, UNET_INPAINT, chargeurs, generer, liberer   # noqa: E402

RACINE = Path(__file__).resolve().parent.parent
CONFIG = yaml.safe_load((RACINE / "config.yaml").read_text())
ENTREE = Path(CONFIG["comfyui_dir"]) / "input"
SORTIES_COMFY = Path(CONFIG["sorties_root"]) / "comfyui"
# un dossier par axe : le fond, sa caméra recalée et ses objets « devant » (camera.json) ; les essais à part, par axe
ESSAIS = Path(CONFIG["sorties_root"]) / "essais" / "integration"
DETOUREUR = Path(CONFIG["modeles_root"]) / "segmentation" / "isnet-anime.onnx"
DECORS = RACINE / "image" / "decors" / "kebab"
AXE_PAR_DEFAUT = "table-du-fond"
TRAVAIL = 1024                      # la taille de travail du modèle

# « wrap » était trop vague : sur 4 graines, Sky a tenu une fleur, un verre, un objet doré (8e essai). Le burrito est ce que
# le modèle connaît de plus proche d'une galette de kebab
ACTION = "eating, biting, holding burrito with both hands, burrito"
DECOR = "sitting, booth, table, indoors, restaurant, warm lighting"
# leur place sur la banquette du fond, dans l'ordre du plan validé (« Sky, Maëlle », plan_kebab.py) ; la taille : la fiche
PERSOS = {
    "sky": {"lora": "sky_v2.safetensors", "taille": 1.87, "x": 7.75, "epaules": 0.44, "cheveux": (125, 68, 40),
            "habits": (226, 222, 214)},                       # sa chemise blanche
    "maelle": {"lora": "maelle_v3.safetensors", "taille": 1.65, "x": 8.3, "epaules": 0.40, "cheveux": (147, 65, 28),
               "habits": (28, 26, 26)},                       # son col roulé noir
}
GRIS = (170, 170, 170)              # le fond gris de leurs images d'entraînement
# le détourage d'isnet-anime est doux (le visage vers 200 sur 255, la table du fond vers 10, une assiette posée vers 50) et
# percé là où le perso a du noir (les feuilles de la chemise de Sky) : on le seuille, on bouche ses trous, on lisse son bord.
# Sans ça, Sky paraissait « un fantôme », effacé par endroits (l'auteur, 2026-10-20)
DETOURAGE_SEUIL = 64
# le guide de pose (modeles.yaml) : sans lui, le modèle décidait seul de la pose et de la taille (Sky 2,5 fois trop grand au
# 4e essai, journal.md)
GUIDE_POSE = "t2i-adapter-openpose-sdxl-1.0.safetensors"
GUIDE_CONTOURS = "t2i-adapter-lineart-sdxl-1.0.fp16.safetensors"
IPA_VISAGE = "ip-adapter-plus-face_sdxl_vit-h.safetensors"
IPA_ENCODEUR = "CLIP-ViT-H-14-laion2B-s32B-b79K.safetensors"
NEGATIF_EN_PLUS = []                # des tags négatifs pour tout l'essai (option --objet)
FORCE_CONTOURS, FIN_CONTOURS = 0.7, 0.6
FORCE_POSE = 0.9
TROU_MAX = 0.02                     # un trou plus petit que 2 % du perso est bouché ; au-delà (entre un bras et le corps), il reste


def corps(perso):
    """Les points de son corps assis, en mètres : proportions moyennes d'un adulte (la tête fait 1/7,5 de sa taille, le crâne
    est à 0,52 de sa taille au-dessus du siège), penché vers la table pour manger."""
    p = PERSOS[perso]
    t, x, ep = p["taille"], p["x"], p["epaules"] / 2
    siege, y = 0.45, 0.62
    crane = siege + 0.52 * t
    tete = t / 7.5
    epaules = siege + 0.34 * t
    # son squelette au format OpenPose (l'ordre COCO à 18 points), pour le guide de pose. Il regarde vers la rue (+y) ;
    # sa droite est du côté des x petits. Assis, les coudes au bord de la table, les mains à la bouche (il mange)
    mains = crane - 1.05 * tete
    squelette = [
        (x, y + 0.10, crane - 0.62 * tete),                                   # 0 le nez
        (x, 0.57, epaules + 0.02),                                            # 1 le cou
        (x - ep, 0.55, epaules), (x - ep - 0.02, 0.80, 0.80), (x - 0.05, y + 0.22, mains),   # 2-4 l'épaule, le coude, le poignet droits
        (x + ep, 0.55, epaules), (x + ep + 0.02, 0.80, 0.80), (x + 0.05, y + 0.22, mains),   # 5-7 les gauches
        (x - 0.15, 0.50, siege + 0.05), (x - 0.15, 1.00, siege + 0.07), (x - 0.13, 1.05, 0.08),  # 8-10 la hanche, le genou, la cheville droits
        (x + 0.15, 0.50, siege + 0.05), (x + 0.15, 1.00, siege + 0.07), (x + 0.13, 1.05, 0.08),  # 11-13 les gauches
        (x - 0.032, y + 0.085, crane - 0.47 * tete), (x + 0.032, y + 0.085, crane - 0.47 * tete),  # 14-15 les yeux
        (x - 0.075, y - 0.005, crane - 0.5 * tete), (x + 0.075, y - 0.005, crane - 0.5 * tete),   # 16-17 les oreilles
    ]
    return {
        "crane": (x, y, crane), "menton": (x, y + 0.02, crane - tete), "squelette": squelette,
        # le contour de sa place : les cheveux (large : au 4e essai, sa tête penchée sortait de sa place et y était
        # tranchée), les épaules, les coudes au bord de la table, les mains à la bouche, les avant-bras sur la table
        "contour": [(x - 0.16, y, crane + 0.12), (x, y, crane + 0.15), (x + 0.16, y, crane + 0.12),
                    (x - 0.26, y, crane - tete / 2), (x + 0.26, y, crane - tete / 2),
                    (x - 0.15, y + 0.32, mains), (x + 0.15, y + 0.32, mains),
                    (x - ep - 0.06, 0.55, epaules), (x + ep + 0.06, 0.55, epaules),
                    (x - ep - 0.08, 0.85, 0.75), (x + ep + 0.08, 0.85, 0.75),
                    (x - 0.3, 1.05, 0.76), (x + 0.3, 1.05, 0.76), (x, 1.0, 1.05),
                    # ses jambes, sous la table, jusqu'au sol : au 3e essai, l'auteur a vu qu'elles manquaient
                    (x - 0.2, 0.5, 0.45), (x + 0.2, 0.5, 0.45), (x - 0.18, 1.0, 0.52), (x + 0.18, 1.0, 0.52),
                    (x - 0.15, 1.05, 0.0), (x + 0.15, 1.05, 0.0), (x - 0.15, 1.2, 0.0), (x + 0.15, 1.2, 0.0)],
        # la silhouette de ses jambes, pour le guide de la méthode B : la hanche, le genou, le pied
        "jambes": [(x - 0.2, 0.5, 0.45), (x + 0.2, 0.5, 0.45), (x + 0.18, 1.0, 0.55), (x + 0.15, 1.1, 0.0),
                   (x - 0.15, 1.1, 0.0), (x - 0.18, 1.0, 0.55)],
    }


def enveloppe(points):
    """L'enveloppe convexe de points 2D (chaîne monotone)."""
    pts = sorted(map(tuple, points))
    def cote(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    bas, haut = [], []
    for p in pts:
        while len(bas) >= 2 and cote(bas[-2], bas[-1], p) <= 0:
            bas.pop()
        bas.append(p)
    for p in reversed(pts):
        while len(haut) >= 2 and cote(haut[-2], haut[-1], p) <= 0:
            haut.pop()
        haut.append(p)
    return bas[:-1] + haut[:-1]


# le dessin OpenPose (le code de l'annotateur de ControlNet, controlnet_aux > draw_bodypose) : les couleurs et les membres
# dans l'ordre où le guide de pose les a appris
COULEURS = [(255, 0, 0), (255, 85, 0), (255, 170, 0), (255, 255, 0), (170, 255, 0), (85, 255, 0), (0, 255, 0), (0, 255, 85),
            (0, 255, 170), (0, 255, 255), (0, 170, 255), (0, 85, 255), (0, 0, 255), (85, 0, 255), (170, 0, 255), (255, 0, 255),
            (255, 0, 170), (255, 0, 85)]
MEMBRES = [(1, 2), (1, 5), (2, 3), (3, 4), (5, 6), (6, 7), (1, 8), (8, 9), (9, 10), (1, 11), (11, 12), (12, 13), (1, 0), (0, 14),
           (14, 16), (0, 15), (15, 17)]


def dessin_pose(points, taille, epaisseur=8):
    """Le squelette au format OpenPose, sur fond noir : points = 18 positions en pixels (None pour un point caché) ;
    taille = un côté (carré) ou (largeur, hauteur)."""
    largeur, hauteur = (taille, taille) if isinstance(taille, int) else taille
    toile = np.zeros((hauteur, largeur, 3), np.uint8)
    for i, p in enumerate(points):
        if p is not None:
            cv2.circle(toile, (int(p[0]), int(p[1])), epaisseur, COULEURS[i], thickness=-1)
    for i, (a, b) in enumerate(MEMBRES):
        if points[a] is None or points[b] is None:
            continue
        (xa, ya), (xb, yb) = points[a], points[b]
        longueur = math.hypot(xa - xb, ya - yb)
        angle = math.degrees(math.atan2(ya - yb, xa - xb))
        calque = toile.copy()
        poly = cv2.ellipse2Poly((int((xa + xb) / 2), int((ya + yb) / 2)), (int(longueur / 2), epaisseur), int(angle), 0, 360, 1)
        cv2.fillConvexPoly(calque, poly, COULEURS[i])
        toile = cv2.addWeighted(toile, 0.4, calque, 0.6, 0)
    return Image.fromarray(toile)


CADRE = (832, 1216)                 # le format portrait de SDXL : un perso assis, des cheveux aux pieds


def cadre_perso(perso, camera):
    """Le cadre de la méthode B, sur le fond : du haut de ses cheveux à ses pieds, au format CADRE. Dessiné sur gris dans ce
    cadre, il le remplit (son LoRA a appris des persos qui remplissent l'image) : sa taille suit le cadre. Au 6e essai, dans
    un carré trop grand pour lui, il sortait 2 fois trop grand. Le haut laisse de la place à une tête d'anime, plus grosse et
    plus haute que la tête réelle du squelette (5e essai)."""
    c = corps(perso)
    pts = projeter(camera, [q for q in c["squelette"] if q is not None])
    (cx, cy), (mx, my) = projeter(camera, [c["crane"], c["menton"]])
    h = my - cy
    x0, x1 = float(pts[:, 0].min()) - 0.9 * h, float(pts[:, 0].max()) + 0.9 * h
    y0, y1 = cy - 0.8 * h, float(pts[:, 1].max()) + 0.3 * h
    rapport = CADRE[0] / CADRE[1]
    if (x1 - x0) / (y1 - y0) < rapport:
        milieu, demi = (x0 + x1) / 2, rapport * (y1 - y0) / 2
        x0, x1 = milieu - demi, milieu + demi
    else:
        y1 = y0 + (x1 - x0) / rapport
    return x0, y0, x1, y1


def forme_jambes(points, echelle, taille):
    """Sous ses hanches, il ne garde que ce qui longe ses jambes (le squelette) : sur le gris, le modèle l'asseyait sur un
    bloc gris que le détourage prenait avec lui (Maëlle, 7e essai). Jusqu'à 18 cm sous les hanches, tout reste : le bas de
    la chemise de Sky, sorti du pantalon, y tombe (coupé à 5 cm, il laissait voir la banquette à travers, 9e essai) ; le haut
    du bloc gris, dans cette bande, part avec le gris du fond (coller_cadre). echelle : pixels par mètre, à sa place."""
    forme = Image.new("L", taille, 0)
    d = ImageDraw.Draw(forme)
    hanches = min(points[8][1], points[11][1])
    d.rectangle([0, 0, taille[0], hanches + 0.18 * echelle], fill=255)
    rayon = 0.14 * echelle
    for i, j in ((8, 9), (9, 10), (11, 12), (12, 13)):
        d.line([points[i], points[j]], fill=255, width=int(2 * rayon))
        for q in (points[i], points[j]):
            d.ellipse([q[0] - rayon, q[1] - rayon, q[0] + rayon, q[1] + rayon], fill=255)
    for i in (10, 13):                                  # les pieds
        r = 0.17 * echelle
        d.ellipse([points[i][0] - r, points[i][1] - r, points[i][0] + r, points[i][1] + r], fill=255)
    return forme.filter(ImageFilter.GaussianBlur(3))


def detoure_au_trait(gris, alpha, bande=24, ecart=30, teinte_max=26, pourtour_colore=40):
    """Le perso détouré au ras de son trait (2026-10-22, à la place d'un resserrement de 3 px qui coupait le trait sombre du
    modèle et laissait un bord blanchâtre ; l'auteur : « tu débordes de partout » sur un liseré tracé au masque), comme une incrustation sur fond uni (le gris de son rendu). (1) Le gris relié
    à l'extérieur part, dans les `bande` derniers pixels : le trait sombre du modèle arrête la remontée. (2) Les trous : une
    tache grise restée dedans, près du bord, part si son pourtour est coloré (entre des mèches, dans un verre de lunettes
    cerclé d'or) ; entourée de blanc ou de gris (sa chemise), elle reste. (3) Un pixel de moins au bord (le mélange avec le
    gris), puis adouci. Rend la transparence (0 à 1)."""
    g = np.asarray(gris.convert("RGB"), np.float32)
    G = np.median(np.concatenate([g[:8].reshape(-1, 3), g[:, :8].reshape(-1, 3), g[:, -8:].reshape(-1, 3)]), axis=0)
    a = cv2.dilate((np.asarray(alpha) > 128).astype(np.uint8), np.ones((3, 3), np.uint8))
    pres = (a - cv2.erode(a, np.ones((2 * bande + 1, 2 * bande + 1), np.uint8))).astype(bool)
    teinte = g.max(axis=2) - g.min(axis=2)
    gris_like = (np.abs(g - G).max(axis=2) < ecart) & (teinte < teinte_max)
    _, comp = cv2.connectedComponents(((a == 0) | (pres & gris_like)).astype(np.uint8), connectivity=4)
    dehors = np.unique(comp[a == 0])
    garde = a.astype(bool) & ~np.isin(comp, dehors[dehors > 0])
    n, taches, stats, _ = cv2.connectedComponentsWithStats((garde & pres & gris_like).astype(np.uint8), connectivity=8)
    for k in range(1, n):
        x, y, w, h, aire = stats[k]
        if aire < 3:
            continue
        x0, y0, x1, y1 = max(x - 3, 0), max(y - 3, 0), x + w + 3, y + h + 3
        t = taches[y0:y1, x0:x1] == k
        tour = cv2.dilate(t.astype(np.uint8), np.ones((5, 5), np.uint8)).astype(bool) & ~t
        if tour.any() and teinte[y0:y1, x0:x1][tour].mean() > pourtour_colore:
            garde[y0:y1, x0:x1][t] = False
    garde = cv2.erode(garde.astype(np.uint8), np.ones((3, 3), np.uint8)).astype(np.float32)
    return cv2.GaussianBlur(garde, (0, 0), 0.7)


def coller_cadre(perso, gris, cadre, camera, fond, devant):
    """Méthode B : le perso dessiné sur gris dans son cadre, détouré, posé sur le fond entier, caché par les objets
    « devant ». Rend le masque et le fond avec le perso collé."""
    c = CADRE[1] / (cadre[3] - cadre[1])
    points = [None if q is None else ((u - cadre[0]) * c, (v - cadre[1]) * c)
              for q, (u, v) in zip(corps(perso)["squelette"],
                                    (projeter(camera, [q])[0] if q is not None else (0, 0) for q in corps(perso)["squelette"]))]
    x = PERSOS[perso]["x"]
    (_, h1), (_, h0) = projeter(camera, [(x, 0.6, 1.0), (x, 0.6, 0.0)])
    alpha = np.asarray(detourage_net(gris), np.float32) * np.asarray(forme_jambes(points, (h0 - h1) * c, CADRE), np.float32) / 255
    # sous ses hanches, le gris du fond lui-même (le bloc gris sur lequel le modèle l'assied, son ombre entre ses jambes)
    # s'en va : un gris sans couleur, pas plus clair que le fond, en grande tache ou qui touche le dehors de sa silhouette.
    # Ce qui est plus clair que le fond reste : la chemise blanche de Sky, dont le bas tombe sous ses hanches (une règle
    # « tout le gris sous les genoux » la trouait, 9e essai) ; les petits plis sombres à l'intérieur de sa silhouette aussi
    g = np.asarray(gris, np.int32)
    teinte = g.max(axis=2) - g.min(axis=2)
    lumiere = g.mean(axis=2)
    bord = np.concatenate([g[:8].reshape(-1, 3), g[:, :8].reshape(-1, 3), g[:, -8:].reshape(-1, 3)])
    gris_du_fond = (teinte < 22) & (lumiere > 70) & (lumiere < np.median(bord, axis=0).mean() + 12) & (alpha > 0)
    gris_du_fond[:int(min(points[8][1], points[11][1]))] = False
    dehors = cv2.dilate((alpha <= 0).astype(np.uint8), np.ones((7, 7), np.uint8)) > 0
    n, taches, stats, _ = cv2.connectedComponentsWithStats(gris_du_fond.astype(np.uint8), connectivity=8)
    aire = max(int((alpha > 0).sum()), 1)
    for k in range(1, n):
        tache = taches == k
        if stats[k, cv2.CC_STAT_AREA] > 0.003 * aire or (tache & dehors).any():
            alpha[tache] = 0
    # détouré au ras de son trait (detoure_au_trait) : resserré de 3 pixels, son bord perdait le trait du modèle et
    # gardait un bord blanchâtre ; avant le resserrement, un liseré du gris de fond, clair sur le miroir sombre (7e essai)
    alpha = Image.fromarray((detoure_au_trait(gris, alpha) * 255).astype(np.uint8))
    taille_cadre = (round(cadre[2] - cadre[0]), round(cadre[3] - cadre[1]))
    coin = (round(cadre[0]), round(cadre[1]))
    calque, alpha_fond = Image.new("RGB", fond.size), Image.new("L", fond.size, 0)
    calque.paste(gris.resize(taille_cadre, Image.LANCZOS), coin)
    alpha_fond.paste(alpha.resize(taille_cadre, Image.LANCZOS), coin)
    devant_fond = Image.new("L", fond.size, 0)
    for objet in devant:
        ImageDraw.Draw(devant_fond).polygon([tuple(q) for q in objet["pixels"]], fill=255)
    alpha_fond = Image.fromarray(np.minimum(np.asarray(alpha_fond), 255 - np.asarray(devant_fond)))
    colle_fond = fond.copy()
    colle_fond.paste(calque, (0, 0), alpha_fond)
    return alpha_fond, colle_fond


def masque_corps(perso, camera, boite, k, taille=TRAVAIL):
    """Méthode C : la zone à repeindre, en forme de corps autour de son squelette, dans l'image de travail. La tête est
    large et haute : une tête d'anime est plus grosse que la vraie (le modèle la dessinait au-dessus de la place prévue,
    5e essai) ; les mains ont de la place pour ce qu'elles tiennent. Les objets « devant » sont ôtés ensuite."""
    def vers(points):
        return [None if q is None else ((u - boite[0]) * k, (v - boite[1]) * k)
                for q, (u, v) in zip(points, (projeter(camera, [q])[0] if q is not None else (0, 0) for q in points))]
    c = corps(perso)
    p = vers(squelette_vu(perso, camera))
    (cx, cy), (mx, my) = vers([c["crane"], c["menton"]])
    x = PERSOS[perso]["x"]
    (_, h1), (_, h0) = projeter(camera, [(x, 0.6, 1.0), (x, 0.6, 0.0)])
    metre = (h0 - h1) * k                          # pixels par mètre, à sa place
    forme = Image.new("L", (taille, taille), 0)
    d = ImageDraw.Draw(forme)

    def trait(i, j, rayon):
        if p[i] is None or p[j] is None:
            return
        r = rayon * metre
        d.line([p[i], p[j]], fill=255, width=int(2 * r))
        for q in (p[i], p[j]):
            d.ellipse([q[0] - r, q[1] - r, q[0] + r, q[1] + r], fill=255)

    d.polygon([p[2], p[5], p[11], p[8]], fill=255)                     # le buste
    for i, j in ((1, 2), (1, 5), (2, 8), (5, 11)):
        trait(i, j, 0.10)
    for i, j in ((2, 3), (3, 4), (5, 6), (6, 7)):                       # les bras
        trait(i, j, 0.09)
    for i, j in ((8, 9), (9, 10), (11, 12), (12, 13)):                  # les jambes
        trait(i, j, 0.11)
    for i in (4, 7, 10, 13):                                            # les mains et ce qu'elles tiennent, les pieds
        r = 0.14 * metre
        d.ellipse([p[i][0] - r, p[i][1] - r, p[i][0] + r, p[i][1] + r], fill=255)
    h = my - cy                                                          # la tête, en grand
    d.ellipse([cx - 0.85 * h, cy - 0.45 * h, cx + 0.85 * h, my + 0.25 * h], fill=255)
    trait(0, 1, 0.08)
    marge = max(3, int(0.03 * metre)) | 1
    return forme.filter(ImageFilter.MaxFilter(marge)).filter(ImageFilter.GaussianBlur(6))


def place(perso, camera, taille_fond, devant=()):
    """Son masque sur le fond (blanc = sa place, bords adoucis), la boîte de travail autour, sa tête en pixels. Les objets
    « devant » (camera.json) sont ôtés du masque, nets : ils restent devant lui, intacts."""
    c = corps(perso)
    contour = projeter(camera, c["contour"])
    masque = Image.new("L", taille_fond, 0)
    ImageDraw.Draw(masque).polygon([tuple(p) for p in enveloppe(contour)], fill=255)
    # large : seul le perso détouré entre dans le fond, le modèle peut donc redessiner autour sans abîmer le décor. Trop juste
    # (21 px au 2e essai), le visage de Sky, penché vers sa galette, débordait dans le bord adouci et s'y effaçait à moitié
    masque = masque.filter(ImageFilter.MaxFilter(61)).filter(ImageFilter.GaussianBlur(12))
    for objet in devant:
        ImageDraw.Draw(masque).polygon([tuple(p) for p in objet["pixels"]], fill=0)
    (cx, cy), (mx, my) = projeter(camera, [c["crane"], c["menton"]])
    x0, y0, x1, y1 = masque.getbbox()
    cote = int(min(max(x1 - x0, y1 - y0) * 1.35, min(taille_fond)))
    centre = ((x0 + x1) / 2, (y0 + y1) / 2)
    bx = int(min(max(centre[0] - cote / 2, 0), taille_fond[0] - cote))
    by = int(min(max(centre[1] - cote / 2, 0), taille_fond[1] - cote))
    return masque, (bx, by, bx + cote, by + cote), {"crane": (cx, cy), "menton": (mx, my), "hauteur": my - cy}


def angle_vu(perso, camera):
    """L'angle sous lequel la caméra le voit, en degrés : 0 de face, positif quand elle est sur sa droite (il regarde vers la
    rue, +y ; sa droite est du côté des x petits). Sur l'axe 6 : 37° ; sur l'axe 14 : 33°."""
    dx, dy = camera["x"] - PERSOS[perso]["x"], camera["y"] - 0.62
    return math.degrees(math.atan2(-dx, dy))


def tags_angle(perso, camera):
    """L'angle en tags Danbooru. Tourné vers le bord droit de l'image, il montre son côté droit (« facing right »)."""
    a = angle_vu(perso, camera)
    cote = "facing right" if a > 0 else "facing left"
    if abs(a) < 20:
        return "facing viewer"
    if abs(a) < 60:
        return f"three-quarter view, {cote}"
    return f"profile, from side, {cote}"


def squelette_vu(perso, camera):
    """Son squelette sans l'oreille que sa tête cache à la caméra."""
    points = list(corps(perso)["squelette"])
    a = angle_vu(perso, camera)
    if a > 20:
        points[17] = None               # la caméra est sur sa droite : son oreille gauche est cachée
    elif a < -20:
        points[16] = None
    return points


RETIRES = []                        # des tags à retirer de tous les prompts (option --retirer), pour un essai
# un LoRA v3 ou plus (option --v3) : les prompts dans l'ordre de ses légendes (le genre puis le déclencheur, celui
# d'Animagine XL 4.0) et ses traits écrits (fiche.json > lora > traits), comme dans ses légendes (pipeline/jeu_lora.py)
FORMAT_V3 = []


def prompt(perso, cadrage, fond_gris=False, angle="three-quarter view, facing right"):
    fiche = json.loads((RACINE / "image" / "persos" / perso / "fiche.json").read_text())
    lora = fiche["lora"]
    if FORMAT_V3:
        genre = "1girl" if fiche.get("genre") == "f" else "1boy"
        morceaux = [genre, lora["declencheur"], "solo", "female focus" if genre == "1girl" else "male focus"]
        morceaux += lora["traits"].get("partout", []) + lora["traits"].get("visage", [])
    else:
        morceaux = [lora["declencheur"], "1girl, solo, female focus" if fiche.get("genre") == "f" else "1boy, solo, male focus"]
    if lora.get("tag_yeux"):
        morceaux.append(lora["tag_yeux"])
    if lora.get("cote_visible") and "facing right" not in angle:
        morceaux.append(lora["cote_visible"]["tag"])
    if lora.get("tenue"):
        morceaux += [lora["tenue"]["haut"], lora["tenue"]["bras"]]
    if lora.get("tags_production"):
        morceaux.append(lora["tags_production"])
    morceaux += [cadrage, angle]
    if cadrage != "portrait, close-up":
        morceaux.append(ACTION)
    morceaux.append("sitting, simple background, grey background" if fond_gris else DECOR)
    tags = ", ".join(morceaux + [QUALITE]).split(", ")
    vus = []
    for t in tags:                      # un tag une seule fois (les traits de la v3 et les tags de production se recoupent)
        if t not in RETIRES and t not in vus:
            vus.append(t)
    return ", ".join(vus)


def negatif(perso, gris=False):
    fiche = json.loads((RACINE / "image" / "persos" / perso / "fiche.json").read_text())
    en_plus = fiche["lora"].get("negatif_production")
    if gris:            # sur fond gris, pas de meuble : ce sont la banquette et la table du fond qui le portent
        en_plus = ", ".join(x for x in (en_plus, "table, desk, chair, stool, bench") if x)
    # pas d'assiette ni de bol : les accessoires de la table se posent en calques (axes.md), pas au hasard du modèle
    return (NEGATIF + ", multiple girls, multiple boys, 2girls, 2boys, plate, bowl, flower, cup, glass, drinking"
            + (f", {en_plus}" if en_plus else "") + "".join(f", {t}" for t in NEGATIF_EN_PLUS))


def etapes_pour(debruitage):
    """25 étapes pour une image dessinée de zéro ; moins pour une passe légère : à peu près 25 × débruitage × 1,25."""
    return 25 if debruitage >= 0.9 else max(10, round(25 * debruitage * 1.25))


def diffusion(image, masque, positif, lora, graine, debruitage, prefixe, negatif_texte=None, pose=None, fooocus=False,
              contours=None, reference=None, poids_reference=0.6):
    """Une passe du modèle sur une image de travail, avec le LoRA du perso ; avec un masque, seule sa zone blanche change
    (bords adoucis : DifferentialDiffusion) ; avec une pose, le guide de pose (T2I-Adapter OpenPose) impose son squelette.
    fooocus : le modèle d'inpainting (le patch de Fooocus fusionné, pipeline/fusionner_inpaint.py) et sa tête, qui lui
    montre la zone à repeindre et ce qui l'entoure : il dessine dans le décor au lieu de coller une image à part."""
    ENTREE.mkdir(exist_ok=True)
    nom = f"kebab_{prefixe}"
    image.save(ENTREE / f"{nom}.png")
    wf = {
        **chargeurs(UNET_INPAINT if fooocus else UNET),
        "2": {"class_type": "LoraLoaderBypassModelOnly", "inputs": {"model": ["1", 0], "lora_name": lora, "strength_model": 1.0}},
        "3": {"class_type": "CLIPTextEncode", "inputs": {"text": positif, "clip": ["1c", 0]}},
        "4": {"class_type": "CLIPTextEncode", "inputs": {"text": negatif_texte or NEGATIF, "clip": ["1c", 0]}},
        "10": {"class_type": "LoadImage", "inputs": {"image": f"{nom}.png"}},
        # le VAE sur la carte, en tuiles (pipeline/comfyui.py) : sur le processeur, 33 s par décodage
        "12": {"class_type": "VAEEncodeTiled", "inputs": {"pixels": ["10", 0], "vae": ["1v", 0], **TUILES}},
        # avec un débruitage partiel, ComfyUI fait quand même toutes les étapes demandées : une passe légère (le visage, à
        # 0,45) en faisait 25 au lieu d'une douzaine, 1 min 50 au lieu de 50 s (2026-10-21)
        "6": {"class_type": "KSampler", "inputs": {"seed": graine, "steps": etapes_pour(debruitage), "cfg": 5.0,
                                                   "sampler_name": "euler_ancestral",
                                                   "scheduler": "normal", "denoise": debruitage, "model": ["2", 0],
                                                   "positive": ["3", 0], "negative": ["4", 0], "latent_image": ["12", 0]}},
        "7": {"class_type": "VAEDecodeTiled", "inputs": {"samples": ["6", 0], "vae": ["1v", 0], **TUILES}},
        "8": {"class_type": "SaveImage", "inputs": {"filename_prefix": f"etape1_{prefixe}", "images": ["7", 0]}},
    }
    if pose is not None:
        pose.save(ENTREE / f"{nom}_pose.png")
        wf["20"] = {"class_type": "ControlNetLoader", "inputs": {"control_net_name": GUIDE_POSE}}
        wf["21"] = {"class_type": "LoadImage", "inputs": {"image": f"{nom}_pose.png"}}
        wf["22"] = {"class_type": "ControlNetApplyAdvanced", "inputs": {
            "positive": ["3", 0], "negative": ["4", 0], "control_net": ["20", 0], "image": ["21", 0],
            "strength": FORCE_POSE, "start_percent": 0.0, "end_percent": 1.0}}
        wf["6"]["inputs"].update({"positive": ["22", 0], "negative": ["22", 1]})
    if contours is not None:
        # le guide de contours (T2I-Adapter Lineart) : les traits de l'image de départ, blancs sur noir ; il fige la tête
        # pendant la passe du visage, jusqu'à 60 % des étapes (la recherche du 2026-10-21)
        contours.save(ENTREE / f"{nom}_contours.png")
        avant = wf["6"]["inputs"]["positive"], wf["6"]["inputs"]["negative"]
        wf["23"] = {"class_type": "ControlNetLoader", "inputs": {"control_net_name": GUIDE_CONTOURS}}
        wf["24"] = {"class_type": "LoadImage", "inputs": {"image": f"{nom}_contours.png"}}
        wf["25"] = {"class_type": "ControlNetApplyAdvanced", "inputs": {
            "positive": avant[0], "negative": avant[1], "control_net": ["23", 0], "image": ["24", 0],
            "strength": FORCE_CONTOURS, "start_percent": 0.0, "end_percent": FIN_CONTOURS}}
        wf["6"]["inputs"].update({"positive": ["25", 0], "negative": ["25", 1]})
    if masque is not None:
        masque.save(ENTREE / f"{nom}_masque.png")
        wf["11"] = {"class_type": "LoadImageMask", "inputs": {"image": f"{nom}_masque.png", "channel": "red"}}
        wf["13"] = {"class_type": "SetLatentNoiseMask", "inputs": {"samples": ["12", 0], "mask": ["11", 0]}}
        wf["9"] = {"class_type": "DifferentialDiffusion", "inputs": {"model": ["2", 0]}}
        wf["6"]["inputs"].update({"model": ["9", 0], "latent_image": ["13", 0]})
        if fooocus:
            # la tête d'inpainting de Fooocus voit l'image avec la zone à repeindre remplie de gris (comme le nœud
            # « VAE Encode & Inpaint Conditioning », mais encodée en tuiles) ; le patch vide : ses poids sont déjà fusionnés
            gris = np.asarray(image.convert("RGB"), np.float32)
            m = (np.asarray(masque.convert("L"), np.float32) / 255 > 0.5)[..., None]
            Image.fromarray(np.where(m, 127.5, gris).astype(np.uint8)).save(ENTREE / f"{nom}_gris.png")
            wf["14"] = {"class_type": "LoadImage", "inputs": {"image": f"{nom}_gris.png"}}
            wf["15"] = {"class_type": "VAEEncodeTiled", "inputs": {"pixels": ["14", 0], "vae": ["1v", 0], **TUILES}}
            wf["16"] = {"class_type": "SetLatentNoiseMask", "inputs": {"samples": ["15", 0], "mask": ["11", 0]}}
            wf["17"] = {"class_type": "INPAINT_LoadFooocusInpaint", "inputs": {"head": "fooocus_inpaint_head.pth",
                                                                                "patch": "patch-vide.pth"}}
            wf["18"] = {"class_type": "INPAINT_ApplyFooocusInpaint", "inputs": {"model": ["2", 0], "patch": ["17", 0],
                                                                                 "latent": ["16", 0]}}
            wf["9"]["inputs"]["model"] = ["18", 0]
    if reference is not None:
        # une image de référence de son visage (IP-Adapter Plus Face) : branchée entre son LoRA et la suite (2026-10-21)
        reference.save(ENTREE / f"{nom}_reference.png")
        wf["30"] = {"class_type": "IPAdapterModelLoader", "inputs": {"ipadapter_file": IPA_VISAGE}}
        wf["31"] = {"class_type": "CLIPVisionLoader", "inputs": {"clip_name": IPA_ENCODEUR}}
        wf["32"] = {"class_type": "LoadImage", "inputs": {"image": f"{nom}_reference.png"}}
        wf["33"] = {"class_type": "IPAdapterAdvanced", "inputs": {
            "model": ["2", 0], "ipadapter": ["30", 0], "image": ["32", 0], "clip_vision": ["31", 0],
            "weight": poids_reference, "weight_type": "linear", "combine_embeds": "concat", "start_at": 0.0, "end_at": 1.0,
            "embeds_scaling": "V only"}}
        for cle, noeud in wf.items():
            if cle != "33" and noeud["inputs"].get("model") == ["2", 0]:
                noeud["inputs"]["model"] = ["33", 0]
    return Image.open(SORTIES_COMFY / generer(wf)[0]).convert("RGB")


_SESSION = None
_TOONOUT = None
DETOUREUR_TOONOUT = Path(CONFIG["modeles_root"]) / "segmentation" / "birefnet-toonout-fp16.onnx"


def detourer_toonout(image):
    """Le perso détouré par ToonOut (BiRefNet affiné sur l'anime, MIT) : un masque de 0 à 255. Sur le processeur, environ
    20 s et plusieurs Go de RAM : jamais pendant une génération (journal.md, 2026-10-21)."""
    global _TOONOUT
    if _TOONOUT is None:
        onnxruntime.set_default_logger_severity(3)
        _TOONOUT = onnxruntime.InferenceSession(str(DETOUREUR_TOONOUT), providers=["CPUExecutionProvider"])
    a = np.asarray(image.convert("RGB").resize((1024, 1024), Image.BILINEAR), np.float32) / 255
    a = (a - np.array([0.485, 0.456, 0.406], np.float32)) / np.array([0.229, 0.224, 0.225], np.float32)
    m = _TOONOUT.run(None, {_TOONOUT.get_inputs()[0].name: a.transpose(2, 0, 1)[None].astype(np.float32)})[0][0, 0]
    m = np.clip(m, 0, 1)                 # déjà une probabilité (de 0 à 1, à l'arrondi du fp16 près)
    return Image.fromarray((m * 255).astype(np.uint8)).resize(image.size, Image.BILINEAR)


def detourer(image):
    """Le perso détouré : un masque de 0 à 1 (isnet-anime, préparation de l'image recopiée de rembg, dis_anime.py)."""
    global _SESSION
    if _SESSION is None:
        _SESSION = onnxruntime.InferenceSession(str(DETOUREUR), providers=["CPUExecutionProvider"])
    a = np.asarray(image.convert("RGB").resize((1024, 1024), Image.LANCZOS), np.float32)
    a = a / max(float(a.max()), 1e-6) - np.array([0.485, 0.456, 0.406], np.float32)
    sortie = _SESSION.run(None, {_SESSION.get_inputs()[0].name: a.transpose(2, 0, 1)[None].astype(np.float32)})[0][0, 0]
    sortie = (sortie - sortie.min()) / max(float(sortie.max() - sortie.min()), 1e-6)
    return Image.fromarray((sortie * 255).astype(np.uint8)).resize(image.size, Image.LANCZOS)


def detourage_net(image):
    """Le détourage plein et net : seuillé, ses encoches refermées, ses petits trous bouchés, les îlots parasites ôtés, son
    bord adouci d'un pixel."""
    m = (np.asarray(detourer(image)) >= DETOURAGE_SEUIL).astype(np.uint8)
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11)))
    aire = max(int(m.sum()), 1)
    contours, hierarchie = cv2.findContours(m, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
    for i, c in enumerate(contours):
        if hierarchie[0][i][3] >= 0 and cv2.contourArea(c) < TROU_MAX * aire:     # un trou (il a un contour parent)
            cv2.drawContours(m, contours, i, 1, thickness=-1)
    n, etiquettes, stats, _ = cv2.connectedComponentsWithStats(m, connectivity=8)
    garde = np.zeros_like(m)
    for k in range(1, n):
        if stats[k, cv2.CC_STAT_AREA] >= 0.01 * aire:
            garde[etiquettes == k] = 1
    return Image.fromarray(garde * 255).filter(ImageFilter.GaussianBlur(1))


def silhouette(perso, travail_fond, table, tete, jambes):
    """Le guide de la méthode B : le gris de l'entraînement, la table du fond à sa place (pour qu'il soit dessiné derrière),
    et une silhouette grossière du perso (la tête et les cheveux, le buste de la couleur de ses habits : au 2e essai, un buste
    noir avait donné à Sky des manches noires, et ses jambes sous la table) à sa place et à sa taille. Le modèle repart de là
    (débruitage 0,85)."""
    guide = Image.new("RGB", travail_fond.size, GRIS)
    d = ImageDraw.Draw(guide)
    (cx, cy), h = tete["crane"], tete["hauteur"]
    d.rectangle([cx - 1.1 * h, cy + 1.25 * h, cx + 1.1 * h, cy + 3.3 * h], fill=PERSOS[perso]["habits"])   # le buste
    d.ellipse([cx - 0.5 * h, cy, cx + 0.5 * h, cy + 1.05 * h], fill=PERSOS[perso]["cheveux"])       # la tête
    d.ellipse([cx - 0.28 * h, cy + 0.35 * h, cx + 0.42 * h, cy + 1.05 * h], fill=(200, 120, 70))     # le visage
    d.polygon(enveloppe(jambes), fill=(24, 24, 26))                                                 # les jambes, en noir
    if table is not None:
        zone = Image.new("L", travail_fond.size, 0)
        ImageDraw.Draw(zone).polygon(table, fill=255)
        guide.paste(travail_fond, mask=zone)                 # la table par-dessus : le buste passe derrière
    return guide


def traits(image):
    """Les traits d'une image, blancs sur noir, pour le guide de contours : une différence de flous (XDoG simplifié)."""
    g = cv2.cvtColor(np.asarray(image.convert("RGB")), cv2.COLOR_RGB2GRAY).astype(np.float32)
    dog = cv2.GaussianBlur(g, (0, 0), 0.9) - 0.98 * cv2.GaussianBlur(g, (0, 0), 1.8)
    lignes = (dog < -2.0).astype(np.uint8) * 255
    return Image.fromarray(cv2.dilate(lignes, np.ones((2, 2), np.uint8))).convert("RGB")


def net(masque, seuil=0.1, largeur=0.12, flou=2):
    """Un masque de collage net à partir d'un masque de diffusion flou (le « Denoise to Compositing Mask » d'Acly) : le bord
    flou, où l'ancienne image reste visible, n'est pas recollé ; sinon, la tête paraissait dédoublée (2026-10-21)."""
    a = np.asarray(masque, np.float32) / 255
    a = np.clip((a - seuil) / largeur, 0, 1)
    return Image.fromarray((a * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(flou))


def fondu_net(colle, fondu, alpha, rayon=24, bord=0):
    """Le fondu sans son flou (2026-10-22) : le fondu par le modèle d'inpainting à 0,45 effaçait ses traits (les mains, la
    galette, la chemise, la bouche restaient floues après la passe de la tête). Dans sa silhouette, le rendu sur gris collé
    garde ses traits et reçoit la lumière du fondu à grande échelle : l'écart de couleur entre le fondu et lui, flouté sur
    `rayon` pixels dans la silhouette seule (pas le gris du fond ni le décor). Sur un bord de `bord` pixels, le fondu tel
    quel : il raccorde le perso au décor. 1 px depuis le détourage au ras du trait (detoure_au_trait) ; à 12, ses mains, sa galette, ses bras au bord de la silhouette
    et presque tout le corps de Maëlle (plus petite) restaient flous, 19 % de Sky et 29 % de Maëlle (l'auteur, le 2026-10-22 ;
    la recherche disait 1 à 2 px) ; le liseré du gris de fond est déjà retiré au collage (coller_cadre). Remettre les traits fins par-dessus le fondu
    (essai du 2026-10-22) ne marchait pas : le fondu déplace les feuilles de la chemise et la bouche, et les deux images ne
    collaient plus."""
    a = np.asarray(alpha.convert("L"), np.float32) / 255
    c = np.asarray(colle.convert("RGB"), np.float32)
    f = np.asarray(fondu.convert("RGB"), np.float32)
    k = (0, 0)
    poids = cv2.GaussianBlur(a, k, rayon)[..., None]
    def basse(x):                       # la moyenne locale de x dans la silhouette seule
        return cv2.GaussianBlur(x * a[..., None], k, rayon) / np.maximum(poids, 1e-3)
    corrige = c + basse(f) - basse(c)
    if bord == 0:                       # sa transparence même : rien n'est pris au fondu brut (son bord avait été calculé sur
        interieur = a[..., None]        # l'ancien collage, au bord blanchâtre : un liseré clair revenait, 2026-10-22)
    else:
        interieur = (a > 0.5).astype(np.uint8)
        interieur = cv2.erode(interieur, np.ones((2 * bord + 1, 2 * bord + 1), np.uint8)).astype(np.float32)
        interieur = cv2.GaussianBlur(interieur, k, bord / 3)[..., None]
    sortie = f * (1 - interieur) + corrige * interieur
    return Image.fromarray(np.clip(sortie, 0, 255).astype(np.uint8))


def rouleau(p1, p2, largeur, taille=TRAVAIL):
    """Un rouleau factice (une galette en attendant la vraie, dessinée une fois pour toutes) : de p1 (le bout tenu, sous ses
    mains) à p2 (sa bouche), une bande de papier blanc côté mains, un trait rouge sur le papier. Rend l'image RGBA du calque."""
    import math as m
    taille = (taille, taille) if isinstance(taille, int) else taille
    calque = Image.new("RGBA", taille, (0, 0, 0, 0))
    d = ImageDraw.Draw(calque)
    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
    longueur = max(m.hypot(dx, dy), 1)
    ux, uy = dx / longueur, dy / longueur
    nx, ny = -uy, ux
    r = largeur / 2

    def bande(a, b, couleur):
        q1 = (p1[0] + ux * longueur * a, p1[1] + uy * longueur * a)
        q2 = (p1[0] + ux * longueur * b, p1[1] + uy * longueur * b)
        d.polygon([(q1[0] + nx * r, q1[1] + ny * r), (q2[0] + nx * r, q2[1] + ny * r),
                   (q2[0] - nx * r, q2[1] - ny * r), (q1[0] - nx * r, q1[1] - ny * r)], fill=couleur)

    d.ellipse([p1[0] - r, p1[1] - r, p1[0] + r, p1[1] + r], fill=(242, 238, 230, 255))
    bande(0.0, 0.55, (242, 238, 230, 255))                     # le papier
    bande(0.55, 1.0, (214, 160, 98, 255))                      # la galette
    bande(0.36, 0.42, (192, 57, 43, 255))                      # le trait rouge sur le papier
    d.ellipse([p2[0] - r, p2[1] - r, p2[0] + r, p2[1] + r], fill=(176, 92, 52, 255))     # la viande, à l'entame
    d.ellipse([p2[0] - r * 0.55, p2[1] - r * 0.55, p2[0] + r * 0.2, p2[1] + r * 0.2], fill=(110, 160, 70, 255))
    return calque


def place_objet(perso, camera, vers, metre_px, tete_px):
    """La galette factice à sa place, d'après son squelette : de sa bouche (sous le nez) vers ses mains, et au-delà (le bout
    tenu, dans son papier). vers : des pixels du fond vers les coordonnées voulues ; metre_px, tete_px : un mètre et la hauteur
    de sa tête à sa place, dans ces coordonnées. Rend le bout tenu, la bouche et la largeur."""
    sq = squelette_vu(perso, camera)
    nez, p4, p7 = (vers(*projeter(camera, [sq[i]])[0]) for i in (0, 4, 7))
    bouche = (nez[0], nez[1] + 0.28 * tete_px)
    milieu = ((p4[0] + p7[0]) / 2, (p4[1] + p7[1]) / 2)
    dx, dy = milieu[0] - bouche[0], milieu[1] - bouche[1]
    longueur = math.hypot(dx, dy) or 1.0
    total = max(0.24 * metre_px, 2.0 * longueur)
    bout = (bouche[0] + dx / longueur * total, bouche[1] + dy / longueur * total)
    return bout, bouche, 0.075 * metre_px


def masque_visage(forme, cote, x0, y0, cx, cy, h, squelette):
    """Le masque de la passe du visage, dans l'image de travail du gros plan (TRAVAIL × TRAVAIL). « carre » : tout le gros plan
    sauf un bord ; « tete » : une ellipse des cheveux au menton, ses mains protégées ; « barbe » : le bas du visage seul (la
    mâchoire, le menton, la lèvre du haut), ses mains protégées."""
    masque = Image.new("L", (TRAVAIL, TRAVAIL), 0)
    d = ImageDraw.Draw(masque)
    if forme == "carre":
        d.rectangle([80, 80, TRAVAIL - 80, TRAVAIL - 80], fill=255)
        return masque.filter(ImageFilter.GaussianBlur(40))
    k = TRAVAIL / cote
    hx, hy, hh = (cx - x0) * k, (cy - y0) * k, h * k
    if forme == "tete2":
        # la tête et une marge (le bord flou tombe sur les cheveux, le cou, le fond) ; les mains ne sont pas ôtées : elles
        # sont recollées nettes après la passe, avec ce qu'elles tiennent (la recherche du 2026-10-21)
        d.ellipse([hx - 0.95 * hh, hy - 0.4 * hh, hx + 0.95 * hh, hy + 1.8 * hh], fill=255)
        return masque.filter(ImageFilter.GaussianBlur(18))
    if forme == "tete":
        d.ellipse([hx - 0.78 * hh, hy - 0.25 * hh, hx + 0.78 * hh, hy + 1.2 * hh], fill=255)
    else:
        # le bas du visage, mesuré sur ses images : une tête d'anime est 1,5 fois plus haute que la tête réelle du
        # squelette ; depuis le haut des cheveux, ses yeux sont à 0,8 fois la hauteur de la tête du squelette, son menton à 1,5
        nx = (squelette[0][0] - x0) * k                       # le nez, pour le côté du visage
        d.ellipse([nx - 0.5 * hh, hy + 1.0 * hh, nx + 0.38 * hh, hy + 1.62 * hh], fill=255)
    for u, v in (squelette[4], squelette[7]):                 # les poignets : ses mains et ce qu'elles tiennent
        r = 0.55 * hh
        d.ellipse([(u - x0) * k - r, (v - y0) * k - r, (u - x0) * k + r, (v - y0) * k + r], fill=0)
    return masque.filter(ImageFilter.GaussianBlur(18 if forme == "tete" else 10))


def passe_visage(perso, image, tete, graine, prefixe, angle, fooocus=False, debruitage=0.45, tags=(), negatif_en_plus=(),
                 forme="carre", squelette=None, v2=False, contours=False, protege=None, sans_visage=False,
                 reference=None, poids_reference=0.6, silhouette=None):
    """Un gros plan sur sa tête, repassé par le modèle avec son LoRA, puis remis en place. Le haut de sa tête est relevé sur
    le détourage (la tête dessinée n'est pas toujours pile à la place prévue).

    v2 (la recherche du 2026-10-21, contre la tête dédoublée) : le geste écrit dans le prompt (« close-up » et ce qu'il fait,
    au lieu de « portrait »), « cigarette, smoking » en négatif, un collage net (le bord flou du masque n'est pas recollé), et
    ses mains avec ce qu'elles tiennent recollées nettes par-dessus. contours : le guide de contours fige la tête.
    protege : une zone (dans l'image de travail) que la passe ne touche pas (l'objet qu'il tient). Rend l'image et la boîte
    du gros plan."""
    h = tete["hauteur"]
    cx, cy = tete["crane"]
    alpha = np.asarray(detourer(image)) > 128
    colonnes = slice(int(max(cx - h, 0)), int(min(cx + h, image.width)))
    lignes = np.where(alpha[:, colonnes].any(axis=1))[0]
    if len(lignes) and abs(lignes[0] - cy) < 1.2 * h:
        cy = float(lignes[0])
    cote = int(max(2.8 * h, 192))
    x0 = int(min(max(cx - cote / 2, 0), image.width - cote))
    y0 = int(min(max(cy - 0.2 * h - cote * 0.12, 0), image.height - cote))
    boite = (x0, y0, x0 + cote, y0 + cote)
    gros = image.crop(boite).resize((TRAVAIL, TRAVAIL), Image.LANCZOS)
    k = TRAVAIL / cote
    hy, hh = (cy - y0) * k, h * k
    poignets = [((u - x0) * k, (v - y0) * k) for u, v in (squelette[4], squelette[7])] if squelette else []
    bouche = ((squelette[0][0] - x0) * k, hy + 1.3 * hh) if squelette else None
    neg = negatif(perso) + "".join(f", {t}" for t in negatif_en_plus)
    cadrage = "close-up" if v2 else "portrait, close-up"
    positif = prompt(perso, cadrage, angle=angle)
    if tags:                            # ses traits, écrits pour le gros plan (option --visage-tags)
        positif = positif.replace(cadrage, cadrage + ", " + ", ".join(tags), 1)
    if v2:
        neg += ", cigarette, smoking"
    visage = gros
    change = Image.new("L", (TRAVAIL, TRAVAIL), 0)
    if not sans_visage:
        # le masque (option --visage-masque) : à 0,75, le masque carré redessinait aussi ses mains et il ne mangeait plus
        # (2026-10-21) ; « tete » les protège ; « tete2 » est plus grand et les recolle nettes après ; « barbe » ne reprend
        # que le bas du visage
        bord = masque_visage(forme, cote, x0, y0, cx, cy, h, squelette)
        refait = diffusion(gros, bord, positif, PERSOS[perso]["lora"], graine, debruitage, f"{prefixe}_visage", neg,
                           fooocus=fooocus, contours=traits(gros) if contours else None, reference=reference,
                           poids_reference=poids_reference)
        if v2:
            colle = np.asarray(net(bord), np.float32) / 255
            if poignets and bouche:
                # ses mains et ce qu'elles tiennent (jusqu'à la bouche), recollées nettes par-dessus la passe
                devant = Image.new("L", (TRAVAIL, TRAVAIL), 0)
                d = ImageDraw.Draw(devant)
                for u, v in poignets:
                    d.ellipse([u - 0.6 * hh, v - 0.6 * hh, u + 0.6 * hh, v + 0.6 * hh], fill=255)
                milieu = ((poignets[0][0] + poignets[1][0]) / 2, (poignets[0][1] + poignets[1][1]) / 2)
                d.line([milieu, bouche], fill=255, width=int(0.55 * hh))
                colle *= 1 - np.asarray(devant.filter(ImageFilter.GaussianBlur(2)), np.float32) / 255
            if protege is not None:
                colle *= 1 - np.asarray(protege.crop(boite).resize((TRAVAIL, TRAVAIL), Image.LANCZOS), np.float32) / 255
            if silhouette is not None:  # le bord de sa silhouette gardé tel quel (interieur_silhouette)
                colle *= np.asarray(interieur_silhouette(silhouette).crop(boite).resize((TRAVAIL, TRAVAIL), Image.LANCZOS),
                                    np.float32) / 255
            colle_img = Image.fromarray((colle * 255).astype(np.uint8))
            visage = Image.composite(refait, gros, colle_img)
            change = colle_img
        else:
            visage = Image.composite(refait, gros, bord)
            change = bord
    sortie = image.copy()
    sortie.paste(visage.resize((cote, cote), Image.LANCZOS), boite[:2], change.resize((cote, cote), Image.LANCZOS))
    return sortie, boite


def interieur_silhouette(silhouette, bord=6):
    """Le dedans de sa silhouette (le détourage du rendu sur gris, celui du collage final), sans ses `bord` derniers pixels :
    là, les passes de la tête et des mains ne recollent rien (option --visage-garde-bord). Elles redessinaient le bord de ses
    cheveux un peu à côté de sa silhouette, et ce bord ressortait plus doux : la netteté de la bande du bord de Maëlle tombait
    de 96 % à 84 % (2026-10-22)."""
    a = (np.asarray(silhouette.convert("L")) > 128).astype(np.uint8)
    a = cv2.erode(a, np.ones((2 * bord + 1, 2 * bord + 1), np.uint8)).astype(np.float32)
    return Image.fromarray((cv2.GaussianBlur(a, (0, 0), 1.5) * 255).astype(np.uint8))


def passe_mains(perso, image, tete, graine, prefixe, angle, squelette, debruitage=0.5, silhouette=None):
    """La passe des mains (2026-10-22 ; la recherche : ADetailer et FaceDetailer font de même) : un seul gros plan sur ses deux
    mains et ce qu'elles tiennent, placé par les poignets de son squelette (sans détecteur de mains), de 3 fois la taille d'une
    main plus leur écart, agrandi à 1024, repassé par le modèle avec son LoRA (0,5, « extra arms » en négatif), recollé net
    (`net`). Sa tête n'est pas touchée : la passe de la tête l'a déjà refaite. Limite connue : l'inpainting garde la
    répartition des couleurs, il retire mal un doigt en trop ; tirer plusieurs graines. Rend l'image et la boîte."""
    if not squelette or squelette[4] is None or squelette[7] is None:
        return image, None
    h = tete["hauteur"]
    cx, cy = tete["crane"]
    (u1, v1), (u2, v2) = squelette[4], squelette[7]
    main = 0.8 * h                      # une main : à peu près la taille de son visage
    cote = max(int(max(abs(u1 - u2), abs(v1 - v2)) + 3 * main), 192)
    x0 = int(min(max((u1 + u2) / 2 - cote / 2, 0), image.width - cote))
    y0 = int(min(max((v1 + v2) / 2 - cote / 2, 0), image.height - cote))
    boite = (x0, y0, x0 + cote, y0 + cote)
    k = TRAVAIL / cote
    gros = image.crop(boite).resize((TRAVAIL, TRAVAIL), Image.LANCZOS)
    masque = Image.new("L", (TRAVAIL, TRAVAIL), 0)
    d = ImageDraw.Draw(masque)
    r = main * k
    for u, v in ((u1, v1), (u2, v2)):
        X, Y = (u - x0) * k, (v - y0) * k
        d.ellipse([X - r, Y - r, X + r, Y + r], fill=255)
    d.line([((u1 - x0) * k, (v1 - y0) * k), ((u2 - x0) * k, (v2 - y0) * k)], fill=255, width=int(r))
    masque = masque.filter(ImageFilter.MaxFilter(25))
    tete_m = Image.new("L", (TRAVAIL, TRAVAIL), 0)       # sa tête, jusqu'au menton : protégée
    ImageDraw.Draw(tete_m).ellipse([(cx - 0.9 * h - x0) * k, (cy - 0.4 * h - y0) * k, (cx + 0.9 * h - x0) * k,
                                    (cy + 1.15 * h - y0) * k], fill=255)
    masque = Image.fromarray(np.minimum(np.asarray(masque), 255 - np.asarray(tete_m))).filter(ImageFilter.GaussianBlur(8))
    positif = prompt(perso, "close-up, hands", angle=angle)
    neg = negatif(perso) + ", extra arms, extra hands, bad hands, extra digits, fused fingers, cigarette, smoking"
    refait = diffusion(gros, masque, positif, PERSOS[perso]["lora"], graine, debruitage, f"{prefixe}_mains", neg)
    colle = net(masque)
    if silhouette is not None:          # le bord de sa silhouette gardé tel quel
        colle = Image.fromarray((np.asarray(colle, np.float32) * np.asarray(
            interieur_silhouette(silhouette).crop(boite).resize((TRAVAIL, TRAVAIL), Image.LANCZOS), np.float32) / 255
            ).astype(np.uint8))
    gros = Image.composite(refait, gros, colle)
    sortie = image.copy()
    sortie.paste(gros.resize((cote, cote), Image.LANCZOS), boite[:2], colle.resize((cote, cote), Image.LANCZOS))
    return sortie, boite


LISERE = np.array([28, 18, 14], np.float32)   # un brun presque noir, celui de leurs traits


def sans_frange(image, silhouette, gris, echelle=1.0, bord=7, ecart=34, teinte_max=28):
    """Le gris du fond du rendu sur gris resté au bord de sa silhouette (entre les mèches de Maëlle, une frange gris-bleu de
    2 à 4 px que le liseré faisait ressortir, 2026-10-22) : dans les `bord` derniers pixels de sa silhouette, les pixels de
    la couleur de ce gris (à moins de `ecart`, peu colorés) sont repeints avec les couleurs de l'intérieur (cv2.inpaint).
    Le gris du fond est mesuré sur le tour de son rendu sur gris, comme au collage (coller_cadre)."""
    g = np.asarray(gris.convert("RGB"), np.int32)
    fond_gris = np.median(np.concatenate([g[:8].reshape(-1, 3), g[:, :8].reshape(-1, 3), g[:, -8:].reshape(-1, 3)]), axis=0)
    a = (np.asarray(silhouette.convert("L")) > 128).astype(np.uint8)
    e = max(1, round(bord * echelle))
    bande = (a - cv2.erode(a, np.ones((2 * e + 1, 2 * e + 1), np.uint8))).astype(bool)
    im = np.asarray(image.convert("RGB"))
    i = im.astype(np.int32)
    frange = bande & (np.abs(i - fond_gris).max(axis=2) < ecart) & (i.max(axis=2) - i.min(axis=2) < teinte_max)
    frange = cv2.dilate(frange.astype(np.uint8), np.ones((3, 3), np.uint8)) & a
    return Image.fromarray(cv2.inpaint(np.ascontiguousarray(im), frange * 255, 3, cv2.INPAINT_TELEA))


def avec_lisere(image, silhouette, vu, echelle=1.0, epaisseur=2, opacite=0.9):
    """Le liseré (l'auteur, 2026-10-22 : « pourquoi tu mets pas le liseré noir partout vu que ça a l'air de bien aider ») :
    un trait sombre de `epaisseur` px de l'image finale tout le long de sa silhouette, comme les persos des anime des années
    90 (les fonds peints n'en ont pas). Il cache aussi le bord plus doux de son collage. Pas là où un objet est devant lui :
    ce bord-là est celui de l'objet (la table). `silhouette` : son détourage (3_detourage), `vu` : ce qui se voit de lui
    (7_detourage-final), tous deux dans l'image de travail ; `echelle` : pixels de travail par pixel de l'image finale."""
    a = (np.asarray(silhouette.convert("L")) > 128).astype(np.uint8)
    v = (np.asarray(vu.convert("L")) > 128).astype(np.uint8)
    cache = cv2.dilate(((a > 0) & (v == 0)).astype(np.uint8), np.ones((7, 7), np.uint8))
    e = max(1, round(epaisseur * echelle))
    bord = (a - cv2.erode(a, np.ones((2 * e + 1, 2 * e + 1), np.uint8))) * (1 - cache)
    bord = (cv2.GaussianBlur(bord.astype(np.float32), (0, 0), 0.6 * echelle) * opacite)[..., None]
    im = np.asarray(image.convert("RGB"), np.float32)
    return Image.fromarray((im * (1 - bord) + LISERE * bord).astype(np.uint8))


def composer(methode, image, masque_travail, devant_travail, alpha_gris=None):
    """Le masque du collage final : le perso détouré, plein et net. A : dans sa place (seuillée, élargie : couper au bord
    adouci l'effaçait à moitié) ; B : le détourage fait sur fond gris, où il est seul (détourer la scène entière prenait aussi
    la plante et la table, 4e essai). Les objets « devant » le cachent."""
    alpha = np.asarray(alpha_gris if alpha_gris is not None else detourage_net(image), np.float32) / 255
    if methode == "A":
        place = masque_travail.point(lambda v: 255 if v > 10 else 0).filter(ImageFilter.MaxFilter(21))
        alpha *= np.asarray(place, np.float32) / 255
    alpha *= 1 - np.asarray(devant_travail, np.float32) / 255
    return Image.fromarray((alpha * 255).astype(np.uint8))


def main():
    global ACTION
    perso, methode, graine = sys.argv[1], sys.argv[2].upper(), int(sys.argv[3])
    options = sys.argv[4:]
    if "--lora" in options:             # un autre fichier de LoRA que celui de PERSOS (une autre version)
        PERSOS[perso]["lora"] = options[options.index("--lora") + 1]
    if "--v3" in options:
        FORMAT_V3[:] = [True]
    if "--objet" in options:
        # avec la galette factice, plus de « burrito » dans les prompts : sinon le modèle dessine le sien à côté (2 graines sur
        # 4, le 2026-10-21) ; il tient « de la nourriture », la galette posée dans le guide
        ACTION = "eating, biting, holding food with both hands"
        NEGATIF_EN_PLUS[:] = ["burrito", "sandwich", "taco", "hamburger", "cigarette"]
    recomposer = "--recomposer" in options
    axe = options[options.index("--axe") + 1] if "--axe" in options else AXE_PAR_DEFAUT
    AXE = DECORS / axe
    SORTIE = ESSAIS / axe
    SORTIE.mkdir(parents=True, exist_ok=True)
    debut = time.time()
    recalage = json.loads((AXE / "camera.json").read_text())
    camera = recalage["camera"]
    angle = tags_angle(perso, camera)
    fond_fichier = dernier_fond(AXE)    # le fond le plus récent de l'axe (v2 : lissé, pipeline/lisser_fonds.py)
    fond = Image.open(fond_fichier).convert("RGB")
    masque, boite, tete = place(perso, camera, fond.size, recalage.get("devant", ()))
    prefixe = f"{perso}_{methode}_{graine}"
    # --sur <essai> : il se pose sur l'image d'un autre essai du même axe (un autre perso déjà là, plus loin de la caméra)
    sur = options[options.index("--sur") + 1] if "--sur" in options else None
    if sur:
        fond = Image.open(SORTIE / f"{sur}.png").convert("RGB")
        prefixe += f"_sur_{sur}"
    # --variante NOM : un essai à part, à côté de l'essai de base (même perso, méthode, graine) ; --retirer « a;b » : des tags
    # retirés des prompts ; --visage-normal : la passe du visage avec le modèle ordinaire (celui du LoRA), même en C et D ;
    # --depuis-corps VARIANTE : seule la passe du visage est refaite, sur le corps d'une autre variante (« base » : l'essai
    # de base) ; --regris (D) : un nouveau rendu sur gris au lieu de celui de la méthode B
    variante = options[options.index("--variante") + 1] if "--variante" in options else None
    if variante:
        prefixe += f"_{variante}"
    if "--retirer" in options:
        RETIRES[:] = [t.strip() for t in options[options.index("--retirer") + 1].split(";")]
    visage_normal = "--visage-normal" in options
    depuis = options[options.index("--depuis-corps") + 1] if "--depuis-corps" in options else None
    # la passe du visage : sa force (--visage-debruitage) et des tags pour ses traits (--visage-tags « a;b », --visage-negatif)
    visage_debruitage = float(options[options.index("--visage-debruitage") + 1]) if "--visage-debruitage" in options else 0.45
    visage_tags = [t.strip() for t in options[options.index("--visage-tags") + 1].split(";")] if "--visage-tags" in options else []
    visage_negatif = ([t.strip() for t in options[options.index("--visage-negatif") + 1].split(";")]
                      if "--visage-negatif" in options else [])
    visage_forme = options[options.index("--visage-masque") + 1] if "--visage-masque" in options else "carre"
    # --depuis-visage VARIANTE : la passe s'applique à l'image d'une autre variante déjà passée au visage (une 2e passe)
    depuis_visage = options[options.index("--depuis-visage") + 1] if "--depuis-visage" in options else None
    if depuis_visage:
        depuis = depuis_visage
    if recomposer:                      # la boîte de travail de l'image déjà générée
        boite = tuple(json.loads((SORTIE / f"{prefixe}.json").read_text())["boite"])
    k = TRAVAIL / (boite[2] - boite[0])
    travail_fond = fond.crop(boite).resize((TRAVAIL, TRAVAIL), Image.LANCZOS)
    masque_travail = masque.crop(boite).resize((TRAVAIL, TRAVAIL), Image.LANCZOS)
    devant_travail = Image.new("L", (TRAVAIL, TRAVAIL), 0)
    for objet in recalage.get("devant", ()):
        ImageDraw.Draw(devant_travail).polygon([((u - boite[0]) * k, (v - boite[1]) * k) for u, v in objet["pixels"]], fill=255)
    tete_travail = {"crane": ((tete["crane"][0] - boite[0]) * k, (tete["crane"][1] - boite[1]) * k),
                    "hauteur": tete["hauteur"] * k}
    etapes = SORTIE / prefixe
    etapes.mkdir(parents=True, exist_ok=True)
    # son squelette, à sa place, dans l'image de travail
    points = [None if q is None else tuple((c - o) * k for c, o in zip(projeter(camera, [q])[0], boite[:2]))
              for q in squelette_vu(perso, camera)]
    pose = dessin_pose(points, TRAVAIL)
    pose.save(etapes / "0_pose.png")
    reglages = {"perso": perso, "methode": methode, "graine": graine, "lora": PERSOS[perso]["lora"], "axe": axe,
                "camera": camera, "boite": boite, "tete_px": round(tete["hauteur"], 1), "angle": angle,
                "prompt": prompt(perso, "cowboy shot", angle=angle), "fond": fond_fichier.name}
    if recomposer:
        reglages = json.loads((SORTIE / f"{prefixe}.json").read_text())
        image = Image.open(etapes / "6_apres-visage.png").convert("RGB")
        if methode in ("B", "D"):
            gris = Image.open(etapes / "2_sur-gris.png").convert("RGB")
            alpha_fond, colle_fond = coller_cadre(perso, gris, tuple(reglages["cadre"]), camera, fond, recalage.get("devant", ()))
            colle_fond.save(etapes / "4_colle-fond.png")
            alpha_fond.crop(boite).resize((TRAVAIL, TRAVAIL), Image.LANCZOS).save(etapes / "3_detourage.png")
    elif depuis:
        source = f"{perso}_{methode}_{graine}" + ("" if depuis == "base" else f"_{depuis}")
        for f in ("3_zone.png", "2_sur-gris.png", "3_detourage.png", "4_colle-fond.png"):
            if (SORTIE / source / f).exists():
                shutil.copy(SORTIE / source / f, etapes / f)
        image = Image.open(SORTIE / source / ("6_apres-visage.png" if depuis_visage else "5_avant-visage.png")).convert("RGB")
        base = json.loads((SORTIE / f"{source}.json").read_text())
        reglages.update({k: base[k] for k in ("cadre", "prompt_gris", "gris_repris_de") if k in base})
        reglages["corps_repris_de"] = source
    elif methode == "A":
        image = diffusion(travail_fond, masque_travail, reglages["prompt"], PERSOS[perso]["lora"], graine, 1.0, prefixe,
                          negatif(perso), pose)
    elif methode == "C":
        liberer()                       # un autre modèle (celui d'inpainting) : la carte vidée d'abord
        # C : dessiné directement dans le décor, avec le modèle d'inpainting de Fooocus, guidé par son squelette, dans une
        # zone en forme de corps ; les objets « devant » ne sont pas repeints. Le modèle voit la vraie banquette et la vraie
        # lumière : pas de tabouret inventé, pas de détourage (les recherches du 2026-10-21, journal.md)
        zone_c = masque_corps(perso, camera, boite, k)
        zone_c = Image.fromarray(np.minimum(np.asarray(zone_c), 255 - np.asarray(devant_travail)))
        zone_c.save(etapes / "3_zone.png")
        reglages["sur"] = sur
        image = diffusion(travail_fond, zone_c, reglages["prompt"], PERSOS[perso]["lora"], graine, 1.0, prefixe,
                          negatif(perso), pose, fooocus=True)
    else:
        # B : dessiné sur gris dans son cadre (sa taille suit le cadre), guidé par son squelette, détouré, collé sur le fond
        # derrière les objets « devant » (la vraie table cache le bas de son buste), puis fondu dans la lumière du décor
        cadre = cadre_perso(perso, camera)
        c = CADRE[1] / (cadre[3] - cadre[1])
        def vers_cadre(u, v):
            return (u - cadre[0]) * c, (v - cadre[1]) * c
        squelette = squelette_vu(perso, camera)
        pose_cadre = dessin_pose([None if q is None else vers_cadre(*projeter(camera, [q])[0]) for q in squelette], CADRE)
        pose_cadre.save(etapes / "0_pose-cadre.png")
        tete_cadre = {"crane": vers_cadre(*tete["crane"]), "hauteur": tete["hauteur"] * c}
        jambes = [vers_cadre(u, v) for u, v in projeter(camera, corps(perso)["jambes"])]
        guide = silhouette(perso, Image.new("RGB", CADRE), None, tete_cadre, jambes)
        objet_cadre = None
        if "--objet" in options:
            # la galette factice (--objet), posée dans le guide avant le rendu : le modèle dessine ses mains autour d'elle, et
            # elle reste presque telle quelle (un quart de la force) ; la même sur toutes les graines (2026-10-21). Collée
            # après coup dans le gros plan, elle flottait devant son menton, et la nourriture du modèle restait à côté
            x_p = PERSOS[perso]["x"]
            (_, h1), (_, h0) = projeter(camera, [(x_p, 0.6, 1.0), (x_p, 0.6, 0.0)])
            bout, bouche, largeur_objet = place_objet(perso, camera, vers_cadre, (h0 - h1) * c, tete["hauteur"] * c)
            calque = rouleau(bout, bouche, largeur_objet, taille=CADRE)
            guide.paste(calque, (0, 0), calque)
            objet_cadre = calque.split()[3]
            reglages["objet"] = {"bout": [round(v, 1) for v in bout], "bouche": [round(v, 1) for v in bouche],
                                 "largeur": round(largeur_objet, 1)}
        guide.save(etapes / "1_guide.png")
        reglages["cadre"] = [round(v, 1) for v in cadre]
        reglages["prompt_gris"] = prompt(perso, "full body", fond_gris=True, angle=angle)
        gris_b = SORTIE / f"{perso}_B_{graine}" / "2_sur-gris.png"
        if "--gris-de" in options:
            # --gris-de VARIANTE (D) : le rendu sur gris d'une autre variante (faite avec --gris-seul), ComfyUI redémarré entre
            # les deux : un seul modèle par appel. Au passage du modèle ordinaire à celui d'inpainting (ou l'inverse) dans le
            # même ComfyUI, le garde-fou de la RAM l'a coupé 3 fois sur 6 (2026-10-21, journal.md)
            gris_b = SORTIE / f"{perso}_{methode}_{graine}_{options[options.index('--gris-de') + 1]}" / "2_sur-gris.png"
            if not gris_b.exists():
                sys.exit(f"pas de rendu sur gris à reprendre : {gris_b}")
        if methode == "D" and gris_b.exists() and "--regris" not in options:
            # D : le même rendu sur gris que la méthode B à la même graine (le perso fidèle : son LoRA a appris sur gris)
            gris = Image.open(gris_b).convert("RGB")
            reglages["gris_repris_de"] = gris_b.parent.name
        else:
            masque_gris = None
            if objet_cadre is not None:
                a_objet = np.asarray(objet_cadre, np.float32) / 255
                masque_gris = Image.fromarray((255 * (1 - 0.75 * a_objet)).astype(np.uint8)).filter(ImageFilter.GaussianBlur(2))
            gris = diffusion(guide, masque_gris, reglages["prompt_gris"], PERSOS[perso]["lora"], graine, 0.9,
                             f"{prefixe}_gris", negatif(perso, gris=True), pose_cadre)
        gris.save(etapes / "2_sur-gris.png")
        if "--gris-seul" in options:    # le rendu sur gris seul, repris ensuite par --gris-de
            reglages["duree_s"] = round(time.time() - debut)
            (SORTIE / f"{prefixe}.json").write_text(json.dumps(reglages, ensure_ascii=False, indent=2) + "\n")
            print(f"{prefixe} : {reglages['duree_s']} s, le rendu sur gris seul → {etapes / '2_sur-gris.png'}")
            return
        objet_travail = None
        if objet_cadre is not None:
            # sa place dans l'image de travail : protégée pendant le fondu et la passe du visage
            taille_c = (round(cadre[2] - cadre[0]), round(cadre[3] - cadre[1]))
            objet_fond = Image.new("L", fond.size, 0)
            objet_fond.paste(objet_cadre.resize(taille_c, Image.LANCZOS), (round(cadre[0]), round(cadre[1])))
            objet_travail = objet_fond.crop(boite).resize((TRAVAIL, TRAVAIL), Image.LANCZOS)
            objet_travail.save(etapes / "2_objet.png")
        # sur le fond entier : le perso détouré dans son cadre, caché par les objets « devant »
        alpha_fond, colle_fond = coller_cadre(perso, gris, cadre, camera, fond, recalage.get("devant", ()))
        colle_fond.save(etapes / "4_colle-fond.png")
        # la passe qui fond sa lumière dans celle du décor, dans la boîte de travail (débruitage 0,35)
        alpha = alpha_fond.crop(boite).resize((TRAVAIL, TRAVAIL), Image.LANCZOS)
        alpha.save(etapes / "3_detourage.png")
        colle = colle_fond.crop(boite).resize((TRAVAIL, TRAVAIL), Image.LANCZOS)
        zone = alpha.filter(ImageFilter.MaxFilter(31)).filter(ImageFilter.GaussianBlur(12))
        if objet_travail is not None:   # la galette presque figée pendant le fondu aussi
            zone = Image.fromarray(np.minimum(np.asarray(zone, np.float32),
                                              255 - 0.75 * np.asarray(objet_travail, np.float32)).astype(np.uint8))
        if "--fondu-tete" in options:
            # sa tête presque gardée pendant le fondu (--fondu-tete 0.2 : un cinquième de la force) : le fondu lissait son
            # visage et effaçait la barbe du rendu sur gris avant la passe du visage (la recherche du 2026-10-21)
            force_tete = float(options[options.index("--fondu-tete") + 1])
            cx, cy = tete_travail["crane"]
            h = tete_travail["hauteur"]
            tete_m = Image.new("L", zone.size, 0)
            ImageDraw.Draw(tete_m).ellipse([cx - 0.95 * h, cy - 0.35 * h, cx + 0.95 * h, cy + 1.75 * h], fill=255)
            tete_m = np.asarray(tete_m.filter(ImageFilter.GaussianBlur(14)), np.float32) / 255
            zone = Image.fromarray((np.asarray(zone, np.float32) * (1 - (1 - force_tete) * tete_m)).astype(np.uint8))
            reglages["fondu_tete"] = force_tete
        if methode == "D":
            # D : le fondu par le modèle d'inpainting (il voit le décor autour), plus appuyé (0,45) : la lumière du décor
            # sur le perso, que la passe à 0,35 du modèle ordinaire ne donnait qu'à peine. --fondu-force F : une autre force ;
            # --fondu-net : ses traits gardés, seule sa lumière prise au fondu (fondu_net)
            force = float(options[options.index("--fondu-force") + 1]) if "--fondu-force" in options else 0.45
            liberer()
            image = diffusion(colle, zone, reglages["prompt"], PERSOS[perso]["lora"], graine, force, f"{prefixe}_fondu",
                              negatif(perso), fooocus=True)
            reglages["fondu"] = {"force": force, "net": "--fondu-net" in options}
            if "--fondu-net" in options:
                image.save(etapes / "5_fondu-brut.png")
                image = fondu_net(colle, image, alpha)
        else:
            image = diffusion(colle, zone, reglages["prompt"], PERSOS[perso]["lora"], graine, 0.35, f"{prefixe}_fondu",
                              negatif(perso))
    if not recomposer:
        image.save(etapes / "5_avant-visage.png")
        if visage_normal and methode in ("C", "D"):
            liberer()                   # le modèle ordinaire après celui d'inpainting : la carte vidée d'abord
        objet_travail = Image.open(etapes / "2_objet.png").convert("L") if (etapes / "2_objet.png").exists() else None
        silhouette = (Image.open(etapes / "3_detourage.png").convert("L")
                      if "--visage-garde-bord" in options and (etapes / "3_detourage.png").exists() else None)
        image, boite_visage = passe_visage(
            perso, image, tete_travail, graine, prefixe, angle, fooocus=methode in ("C", "D") and not visage_normal,
            debruitage=visage_debruitage, tags=visage_tags, negatif_en_plus=visage_negatif, forme=visage_forme,
            squelette=points, v2="--visage-v2" in options, contours="--visage-contours" in options,
            protege=objet_travail, sans_visage="--sans-visage" in options,
            reference=Image.open(options[options.index("--visage-reference") + 1]).convert("RGB")
            if "--visage-reference" in options else None,
            poids_reference=float(options[options.index("--visage-reference-poids") + 1])
            if "--visage-reference-poids" in options else 0.6, silhouette=silhouette)
        if "--visage-reference" in options:
            reglages["visage_reference"] = {"image": options[options.index("--visage-reference") + 1],
                                            "poids": float(options[options.index("--visage-reference-poids") + 1])
                                            if "--visage-reference-poids" in options else 0.6}
        if "--mains" in options:
            # la passe des mains (--mains [--mains-debruitage F]), après celle de la tête, avec le même modèle
            image.save(etapes / "6_avant-mains.png")
            force_mains = (float(options[options.index("--mains-debruitage") + 1]) if "--mains-debruitage" in options
                           else 0.5)
            image, boite_mains = passe_mains(perso, image, tete_travail, graine, prefixe, angle, points, force_mains,
                                             silhouette=silhouette)
            reglages["mains"] = {"debruitage": force_mains, "boite": boite_mains}
        reglages["visage_passe"] = {"debruitage": visage_debruitage, "tags": visage_tags, "negatif": visage_negatif}
        reglages["retires"] = list(RETIRES)
        reglages["visage"] = "normal" if (visage_normal or methode not in ("C", "D")) else "inpaint"
        image.save(etapes / "6_apres-visage.png")
        reglages["boite_visage_travail"] = boite_visage
    # retour sur le fond entier : seul le perso détouré y entre. Le reste de sa place revient au fond d'origine : au premier
    # essai, le modèle avait changé le miroir en fenêtre de nuit derrière lui, et ajouté une assiette sur la table
    alpha_gris = Image.open(etapes / "3_detourage.png").convert("L") if methode in ("B", "D") else None
    prefixe_sortie = prefixe
    detoureur = options[options.index("--detourer") + 1] if "--detourer" in options else None
    if methode == "C":                  # sa zone, telle quelle : le reste de l'image n'a pas été repeint
        alpha = Image.open(etapes / "3_zone.png").convert("L")
        if detoureur:
            # dans sa zone, le perso seul : le modèle y repeint aussi un peu du décor autour de lui (un halo sur le miroir,
            # une tasse ajoutée près des sauces, 2026-10-21) ; le décor d'origine revient autour de sa silhouette
            perso_seul = (detourer_toonout if detoureur == "toonout" else detourer)(image)
            perso_seul = perso_seul.point(lambda v: 255 if v > 128 else 0).filter(ImageFilter.MaxFilter(5)).filter(
                ImageFilter.GaussianBlur(1.5))
            alpha = Image.fromarray(np.minimum(np.asarray(alpha), np.asarray(perso_seul)))
            prefixe_sortie = f"{prefixe}_detoure-{detoureur}"
    else:
        alpha = composer(methode, image, masque_travail, devant_travail, alpha_gris)
    alpha.save(etapes / ("7_detourage-final.png" if prefixe_sortie == prefixe else f"7_detourage-{detoureur}.png"))
    final = Image.open(etapes / "4_colle-fond.png").convert("RGB") if methode in ("B", "D") else fond.copy()
    taille = boite[2] - boite[0]
    if methode in ("B", "D") and "--lisere" in options:   # le liseré tracé au masque : en option (il débordait, 2026-10-22)
        image = sans_frange(image, alpha_gris, Image.open(etapes / "2_sur-gris.png"), echelle=TRAVAIL / taille)
        image = avec_lisere(image, alpha_gris, alpha, echelle=TRAVAIL / taille)
        reglages["lisere"] = True
    final.paste(image.resize((taille, taille), Image.LANCZOS), boite[:2], alpha.resize((taille, taille), Image.LANCZOS))
    final.save(SORTIE / f"{prefixe_sortie}.png")
    if not recomposer:
        reglages["duree_s"] = round(time.time() - debut)
    (SORTIE / f"{prefixe_sortie}.json").write_text(json.dumps(reglages, ensure_ascii=False, indent=2) + "\n")
    print(f"{prefixe_sortie} : {reglages['duree_s']} s → {SORTIE / f'{prefixe_sortie}.png'}")


if __name__ == "__main__":
    main()
