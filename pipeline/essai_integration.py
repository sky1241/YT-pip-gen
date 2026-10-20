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
import sys
import time
from pathlib import Path

import cv2
import numpy as np
import onnxruntime
import yaml
from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, str(Path(__file__).resolve().parent))
from recaler_camera import projeter          # noqa: E402
from test_lora import NEGATIF, QUALITE, generer   # noqa: E402

RACINE = Path(__file__).resolve().parent.parent
CONFIG = yaml.safe_load((RACINE / "config.yaml").read_text())
ENTREE = Path(CONFIG["comfyui_dir"]) / "input"
SORTIES_COMFY = Path(CONFIG["sorties_root"]) / "comfyui"
SORTIE = Path(CONFIG["sorties_root"]) / "essais" / "etape1"
DETOUREUR = Path(CONFIG["modeles_root"]) / "segmentation" / "isnet-anime.onnx"
AXE = RACINE / "image" / "decors" / "kebab" / "table-du-fond"
TRAVAIL = 1024                      # la taille de travail du modèle

# sur l'axe 6, la caméra est devant eux, sur leur droite : on voit leur côté droit (le calcul : journal.md, 2026-10-20)
ANGLE = "three-quarter view, facing right"
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
        (x - 0.075, y - 0.005, crane - 0.5 * tete), None,                     # 16 l'oreille droite ; la gauche est cachée
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
    bloc gris que le détourage prenait avec lui (Maëlle, 7e essai). Au-dessus des hanches, tout reste. echelle : pixels par
    mètre, à sa place."""
    forme = Image.new("L", taille, 0)
    d = ImageDraw.Draw(forme)
    hanches = min(points[8][1], points[11][1])
    d.rectangle([0, 0, taille[0], hanches + 0.05 * echelle], fill=255)
    rayon = 0.14 * echelle
    for i, j in ((8, 9), (9, 10), (11, 12), (12, 13)):
        d.line([points[i], points[j]], fill=255, width=int(2 * rayon))
        for q in (points[i], points[j]):
            d.ellipse([q[0] - rayon, q[1] - rayon, q[0] + rayon, q[1] + rayon], fill=255)
    for i in (10, 13):                                  # les pieds
        r = 0.17 * echelle
        d.ellipse([points[i][0] - r, points[i][1] - r, points[i][0] + r, points[i][1] + r], fill=255)
    return forme.filter(ImageFilter.GaussianBlur(3))


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
    # sous les genoux, il n'y a que ses tibias et ses chaussures, sombres : ce qui est gris clair ou moyen, sans couleur (le
    # fond, l'ombre portée sur le fond, entre ses jambes), s'en va. Plus haut, non : les plis ombrés de la chemise blanche de
    # Sky sont de ce gris-là (7e essai)
    g = np.asarray(gris, np.int32)
    teinte = g.max(axis=2) - g.min(axis=2)
    lumiere = g.mean(axis=2)
    genoux = int(min(points[9][1], points[12][1]))
    gris_fond = (teinte < 22) & (lumiere > 85) & (lumiere < 235)
    gris_fond[:genoux] = False
    alpha[gris_fond] = 0
    # resserré de 3 pixels : son bord gardait un liseré du gris de fond, clair sur le miroir sombre (7e essai)
    alpha = Image.fromarray(alpha.astype(np.uint8)).filter(ImageFilter.MinFilter(7)).filter(ImageFilter.GaussianBlur(1))
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


def prompt(perso, cadrage, fond_gris=False):
    fiche = json.loads((RACINE / "image" / "persos" / perso / "fiche.json").read_text())
    lora = fiche["lora"]
    morceaux = [lora["declencheur"], "1girl, solo, female focus" if fiche.get("genre") == "f" else "1boy, solo, male focus"]
    if lora.get("tag_yeux"):
        morceaux.append(lora["tag_yeux"])
    if lora.get("cote_visible") and "facing right" not in ANGLE:
        morceaux.append(lora["cote_visible"]["tag"])
    if lora.get("tenue"):
        morceaux += [lora["tenue"]["haut"], lora["tenue"]["bras"]]
    if lora.get("tags_production"):
        morceaux.append(lora["tags_production"])
    morceaux += [cadrage, ANGLE]
    if cadrage != "portrait, close-up":
        morceaux.append(ACTION)
    morceaux.append("sitting, simple background, grey background" if fond_gris else DECOR)
    return ", ".join(morceaux + [QUALITE])


def negatif(perso, gris=False):
    fiche = json.loads((RACINE / "image" / "persos" / perso / "fiche.json").read_text())
    en_plus = fiche["lora"].get("negatif_production")
    if gris:            # sur fond gris, pas de meuble : ce sont la banquette et la table du fond qui le portent
        en_plus = ", ".join(x for x in (en_plus, "table, desk, chair, stool, bench") if x)
    # pas d'assiette ni de bol : les accessoires de la table se posent en calques (axes.md), pas au hasard du modèle
    return (NEGATIF + ", multiple girls, multiple boys, 2girls, 2boys, plate, bowl, flower, cup, glass, drinking"
            + (f", {en_plus}" if en_plus else ""))


def diffusion(image, masque, positif, lora, graine, debruitage, prefixe, negatif_texte=None, pose=None):
    """Une passe du modèle sur une image de travail, avec le LoRA du perso ; avec un masque, seule sa zone blanche change
    (bords adoucis : DifferentialDiffusion) ; avec une pose, le guide de pose (T2I-Adapter OpenPose) impose son squelette."""
    ENTREE.mkdir(exist_ok=True)
    nom = f"kebab_{prefixe}"
    image.save(ENTREE / f"{nom}.png")
    wf = {
        "1": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": "animagine-xl-4.0.safetensors"}},
        "2": {"class_type": "LoraLoaderBypassModelOnly", "inputs": {"model": ["1", 0], "lora_name": lora, "strength_model": 1.0}},
        "3": {"class_type": "CLIPTextEncode", "inputs": {"text": positif, "clip": ["1", 1]}},
        "4": {"class_type": "CLIPTextEncode", "inputs": {"text": negatif_texte or NEGATIF, "clip": ["1", 1]}},
        "10": {"class_type": "LoadImage", "inputs": {"image": f"{nom}.png"}},
        # le VAE d'un bloc : par tuiles, ComfyUI le passe trois fois (trois découpages moyennés), et sur le processeur
        # (--cpu-vae) une variante prenait 13 minutes au lieu de 5 (2026-10-20)
        "12": {"class_type": "VAEEncode", "inputs": {"pixels": ["10", 0], "vae": ["1", 2]}},
        "6": {"class_type": "KSampler", "inputs": {"seed": graine, "steps": 25, "cfg": 5.0, "sampler_name": "euler_ancestral",
                                                   "scheduler": "normal", "denoise": debruitage, "model": ["2", 0],
                                                   "positive": ["3", 0], "negative": ["4", 0], "latent_image": ["12", 0]}},
        "7": {"class_type": "VAEDecode", "inputs": {"samples": ["6", 0], "vae": ["1", 2]}},
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
    if masque is not None:
        masque.save(ENTREE / f"{nom}_masque.png")
        wf["11"] = {"class_type": "LoadImageMask", "inputs": {"image": f"{nom}_masque.png", "channel": "red"}}
        wf["13"] = {"class_type": "SetLatentNoiseMask", "inputs": {"samples": ["12", 0], "mask": ["11", 0]}}
        wf["9"] = {"class_type": "DifferentialDiffusion", "inputs": {"model": ["2", 0]}}
        wf["6"]["inputs"].update({"model": ["9", 0], "latent_image": ["13", 0]})
    return Image.open(SORTIES_COMFY / generer(wf)[0]).convert("RGB")


_SESSION = None


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


def passe_visage(perso, image, tete, graine, prefixe):
    """Un gros plan sur sa tête, repassé par le modèle avec son LoRA (débruitage 0,45), puis remis en place. Le haut de sa
    tête est relevé sur le détourage (la tête dessinée n'est pas toujours pile à la place prévue)."""
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
    bord = Image.new("L", (TRAVAIL, TRAVAIL), 0)
    ImageDraw.Draw(bord).rectangle([80, 80, TRAVAIL - 80, TRAVAIL - 80], fill=255)
    bord = bord.filter(ImageFilter.GaussianBlur(40))
    refait = diffusion(gros, bord, prompt(perso, "portrait, close-up"), PERSOS[perso]["lora"], graine, 0.45,
                       f"{prefixe}_visage", negatif(perso))
    sortie = image.copy()
    sortie.paste(refait.resize((cote, cote), Image.LANCZOS), boite[:2], bord.resize((cote, cote), Image.LANCZOS))
    return sortie, boite


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
    perso, methode, graine = sys.argv[1], sys.argv[2].upper(), int(sys.argv[3])
    recomposer = "--recomposer" in sys.argv[4:]
    debut = time.time()
    recalage = json.loads((AXE / "camera.json").read_text())
    camera = recalage["camera"]
    fond = Image.open(AXE / "fond_v1.png").convert("RGB")
    masque, boite, tete = place(perso, camera, fond.size, recalage.get("devant", ()))
    prefixe = f"{perso}_{methode}_{graine}"
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
    points = [None if p is None else ((u - boite[0]) * k, (v - boite[1]) * k)
              for p, (u, v) in zip(corps(perso)["squelette"],
                                    (projeter(camera, [q]) [0] if q is not None else (0, 0) for q in corps(perso)["squelette"]))]
    pose = dessin_pose(points, TRAVAIL)
    pose.save(etapes / "0_pose.png")
    reglages = {"perso": perso, "methode": methode, "graine": graine, "lora": PERSOS[perso]["lora"], "camera": camera,
                "boite": boite, "tete_px": round(tete["hauteur"], 1), "prompt": prompt(perso, "cowboy shot")}
    if recomposer:
        reglages = json.loads((SORTIE / f"{prefixe}.json").read_text())
        image = Image.open(etapes / "6_apres-visage.png").convert("RGB")
        if methode == "B":
            gris = Image.open(etapes / "2_sur-gris.png").convert("RGB")
            alpha_fond, colle_fond = coller_cadre(perso, gris, tuple(reglages["cadre"]), camera, fond, recalage.get("devant", ()))
            colle_fond.save(etapes / "4_colle-fond.png")
            alpha_fond.crop(boite).resize((TRAVAIL, TRAVAIL), Image.LANCZOS).save(etapes / "3_detourage.png")
    elif methode == "A":
        image = diffusion(travail_fond, masque_travail, reglages["prompt"], PERSOS[perso]["lora"], graine, 1.0, prefixe,
                          negatif(perso), pose)
    else:
        # B : dessiné sur gris dans son cadre (sa taille suit le cadre), guidé par son squelette, détouré, collé sur le fond
        # derrière les objets « devant » (la vraie table cache le bas de son buste), puis fondu dans la lumière du décor
        cadre = cadre_perso(perso, camera)
        c = CADRE[1] / (cadre[3] - cadre[1])
        def vers_cadre(u, v):
            return (u - cadre[0]) * c, (v - cadre[1]) * c
        squelette = corps(perso)["squelette"]
        pose_cadre = dessin_pose([None if q is None else vers_cadre(*projeter(camera, [q])[0]) for q in squelette], CADRE)
        pose_cadre.save(etapes / "0_pose-cadre.png")
        tete_cadre = {"crane": vers_cadre(*tete["crane"]), "hauteur": tete["hauteur"] * c}
        jambes = [vers_cadre(u, v) for u, v in projeter(camera, corps(perso)["jambes"])]
        guide = silhouette(perso, Image.new("RGB", CADRE), None, tete_cadre, jambes)
        guide.save(etapes / "1_guide.png")
        reglages["cadre"] = [round(v, 1) for v in cadre]
        reglages["prompt_gris"] = prompt(perso, "full body", fond_gris=True)
        gris = diffusion(guide, None, reglages["prompt_gris"], PERSOS[perso]["lora"], graine, 0.9, f"{prefixe}_gris",
                         negatif(perso, gris=True), pose_cadre)
        gris.save(etapes / "2_sur-gris.png")
        # sur le fond entier : le perso détouré dans son cadre, caché par les objets « devant »
        alpha_fond, colle_fond = coller_cadre(perso, gris, cadre, camera, fond, recalage.get("devant", ()))
        colle_fond.save(etapes / "4_colle-fond.png")
        # la passe qui fond sa lumière dans celle du décor, dans la boîte de travail (débruitage 0,35)
        alpha = alpha_fond.crop(boite).resize((TRAVAIL, TRAVAIL), Image.LANCZOS)
        alpha.save(etapes / "3_detourage.png")
        colle = colle_fond.crop(boite).resize((TRAVAIL, TRAVAIL), Image.LANCZOS)
        zone = alpha.filter(ImageFilter.MaxFilter(31)).filter(ImageFilter.GaussianBlur(12))
        image = diffusion(colle, zone, reglages["prompt"], PERSOS[perso]["lora"], graine, 0.35, f"{prefixe}_fondu",
                          negatif(perso))
    if not recomposer:
        image.save(etapes / "5_avant-visage.png")
        image, boite_visage = passe_visage(perso, image, tete_travail, graine, prefixe)
        image.save(etapes / "6_apres-visage.png")
        reglages["boite_visage_travail"] = boite_visage
    # retour sur le fond entier : seul le perso détouré y entre. Le reste de sa place revient au fond d'origine : au premier
    # essai, le modèle avait changé le miroir en fenêtre de nuit derrière lui, et ajouté une assiette sur la table
    alpha_gris = Image.open(etapes / "3_detourage.png").convert("L") if methode == "B" else None
    alpha = composer(methode, image, masque_travail, devant_travail, alpha_gris)
    alpha.save(etapes / "7_detourage-final.png")
    final = Image.open(etapes / "4_colle-fond.png").convert("RGB") if methode == "B" else fond.copy()
    taille = boite[2] - boite[0]
    final.paste(image.resize((taille, taille), Image.LANCZOS), boite[:2], alpha.resize((taille, taille), Image.LANCZOS))
    final.save(SORTIE / f"{prefixe}.png")
    if not recomposer:
        reglages["duree_s"] = round(time.time() - debut)
    (SORTIE / f"{prefixe}.json").write_text(json.dumps(reglages, ensure_ascii=False, indent=2) + "\n")
    print(f"{prefixe} : {reglages['duree_s']} s → {SORTIE / f'{prefixe}.png'}")


if __name__ == "__main__":
    main()
