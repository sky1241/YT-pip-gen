"""Étape 1 du premier vrai test (PLAN.md) : un perso seul, assis à sa place dans un fond du kebab, qui mange. Deux méthodes :

  A, « dans le fond » : sa place est masquée sur le fond, le modèle l'y dessine avec son LoRA (inpainting).
  B, « en calque »    : il est dessiné sur fond gris, là où son LoRA est le plus sûr, d'après une silhouette posée à sa place ;
                        puis détouré (isnet-anime), collé sur le fond, et une passe légère avec son LoRA fond sa lumière
                        dans celle du décor.

Les deux finissent par une passe sur le visage, en gros plan : sur ce plan large, sa tête fait 100 à 140 pixels, trop peu pour
que le LoRA y mette ses traits. Hors de sa place, le fond reste intact au pixel près. Sa place et sa taille viennent de la
caméra recalée sur le fond (`camera.json`, pipeline/recaler_camera.py) et de sa taille dans la fiche.

  ~/venvs/kebab/bin/python pipeline/essai_integration.py <perso> <A|B> <graine>

Sortie : <sorties_root>/essais/etape1/<perso>_<méthode>_<graine>.png (le fond entier), ses étapes et ses réglages (.json).
ComfyUI doit tourner (pipeline/comfyui.py demarrer).
"""
import json
import sys
import time
from pathlib import Path

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
ACTION = "eating, holding food with both hands, wrap"
DECOR = "sitting, booth, table, indoors, restaurant, warm lighting"
# leur place sur la banquette du fond, dans l'ordre du plan validé (« Sky, Maëlle », plan_kebab.py) ; la taille : la fiche
PERSOS = {
    "sky": {"lora": "sky_v2.safetensors", "taille": 1.87, "x": 7.75, "epaules": 0.44, "cheveux": (125, 68, 40)},
    "maelle": {"lora": "maelle_v3.safetensors", "taille": 1.65, "x": 8.3, "epaules": 0.40, "cheveux": (147, 65, 28)},
}
GRIS = (170, 170, 170)              # le fond gris de leurs images d'entraînement


def corps(perso):
    """Les points de son corps assis, en mètres : proportions moyennes d'un adulte (la tête fait 1/7,5 de sa taille, le crâne
    est à 0,52 de sa taille au-dessus du siège), penché vers la table pour manger."""
    p = PERSOS[perso]
    t, x, ep = p["taille"], p["x"], p["epaules"] / 2
    siege, y = 0.45, 0.62
    crane = siege + 0.52 * t
    tete = t / 7.5
    epaules = siege + 0.34 * t
    return {
        "crane": (x, y, crane), "menton": (x, y + 0.02, crane - tete),
        # le contour de sa place : les cheveux, les épaules, les coudes au bord de la table, les avant-bras dessus
        "contour": [(x - 0.12, y, crane + 0.06), (x, y, crane + 0.1), (x + 0.12, y, crane + 0.06),
                    (x - 0.19, y, crane - tete / 2), (x + 0.19, y, crane - tete / 2),
                    (x - ep - 0.06, 0.55, epaules), (x + ep + 0.06, 0.55, epaules),
                    (x - ep - 0.08, 0.85, 0.75), (x + ep + 0.08, 0.85, 0.75),
                    (x - 0.3, 1.05, 0.76), (x + 0.3, 1.05, 0.76), (x, 1.0, 1.05)],
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


def place(perso, camera, taille_fond, devant=()):
    """Son masque sur le fond (blanc = sa place, bords adoucis), la boîte de travail autour, sa tête en pixels. Les objets
    « devant » (camera.json) sont ôtés du masque, nets : ils restent devant lui, intacts."""
    c = corps(perso)
    contour = projeter(camera, c["contour"])
    masque = Image.new("L", taille_fond, 0)
    ImageDraw.Draw(masque).polygon([tuple(p) for p in enveloppe(contour)], fill=255)
    masque = masque.filter(ImageFilter.MaxFilter(21)).filter(ImageFilter.GaussianBlur(10))
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
    morceaux += [cadrage, ANGLE]
    if cadrage == "upper body":
        morceaux.append(ACTION)
    morceaux.append("sitting, table, simple background, grey background" if fond_gris else DECOR)
    return ", ".join(morceaux + [QUALITE])


def diffusion(image, masque, positif, lora, graine, debruitage, prefixe):
    """Une passe du modèle sur une image de travail, avec le LoRA du perso ; avec un masque, seule sa zone blanche change
    (bords adoucis : DifferentialDiffusion)."""
    ENTREE.mkdir(exist_ok=True)
    nom = f"kebab_{prefixe}"
    image.save(ENTREE / f"{nom}.png")
    wf = {
        "1": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": "animagine-xl-4.0.safetensors"}},
        "2": {"class_type": "LoraLoaderBypassModelOnly", "inputs": {"model": ["1", 0], "lora_name": lora, "strength_model": 1.0}},
        "3": {"class_type": "CLIPTextEncode", "inputs": {"text": positif, "clip": ["1", 1]}},
        "4": {"class_type": "CLIPTextEncode", "inputs": {"text": NEGATIF + ", multiple girls, multiple boys, 2girls, 2boys",
                                                         "clip": ["1", 1]}},
        "10": {"class_type": "LoadImage", "inputs": {"image": f"{nom}.png"}},
        "12": {"class_type": "VAEEncode", "inputs": {"pixels": ["10", 0], "vae": ["1", 2]}},
        "6": {"class_type": "KSampler", "inputs": {"seed": graine, "steps": 25, "cfg": 5.0, "sampler_name": "euler_ancestral",
                                                   "scheduler": "normal", "denoise": debruitage, "model": ["2", 0],
                                                   "positive": ["3", 0], "negative": ["4", 0], "latent_image": ["12", 0]}},
        "7": {"class_type": "VAEDecode", "inputs": {"samples": ["6", 0], "vae": ["1", 2]}},
        "8": {"class_type": "SaveImage", "inputs": {"filename_prefix": f"etape1_{prefixe}", "images": ["7", 0]}},
    }
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


def silhouette(perso, travail_fond, table, tete):
    """Le guide de la méthode B : le gris de l'entraînement, la table du fond à sa place (pour qu'il soit dessiné derrière),
    et une silhouette grossière du perso (la tête et les cheveux, le buste en noir) à sa place et à sa taille. Le modèle
    repart de là (débruitage 0,85)."""
    guide = Image.new("RGB", travail_fond.size, GRIS)
    d = ImageDraw.Draw(guide)
    (cx, cy), h = tete["crane"], tete["hauteur"]
    d.rectangle([cx - 1.1 * h, cy + 1.25 * h, cx + 1.1 * h, cy + 3.3 * h], fill=(28, 26, 26))       # le buste
    d.ellipse([cx - 0.5 * h, cy, cx + 0.5 * h, cy + 1.05 * h], fill=PERSOS[perso]["cheveux"])       # la tête
    d.ellipse([cx - 0.28 * h, cy + 0.35 * h, cx + 0.42 * h, cy + 1.05 * h], fill=(200, 120, 70))     # le visage
    zone = Image.new("L", travail_fond.size, 0)
    ImageDraw.Draw(zone).polygon(table, fill=255)
    guide.paste(travail_fond, mask=zone)                     # la table par-dessus : le buste passe derrière
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
    refait = diffusion(gros, bord, prompt(perso, "portrait, close-up"), PERSOS[perso]["lora"], graine, 0.45, f"{prefixe}_visage")
    sortie = image.copy()
    sortie.paste(refait.resize((cote, cote), Image.LANCZOS), boite[:2], bord.resize((cote, cote), Image.LANCZOS))
    return sortie, boite


def main():
    perso, methode, graine = sys.argv[1], sys.argv[2].upper(), int(sys.argv[3])
    debut = time.time()
    recalage = json.loads((AXE / "camera.json").read_text())
    camera = recalage["camera"]
    fond = Image.open(AXE / "fond_v1.png").convert("RGB")
    masque, boite, tete = place(perso, camera, fond.size, recalage.get("devant", ()))
    k = TRAVAIL / (boite[2] - boite[0])
    travail_fond = fond.crop(boite).resize((TRAVAIL, TRAVAIL), Image.LANCZOS)
    masque_travail = masque.crop(boite).resize((TRAVAIL, TRAVAIL), Image.LANCZOS)
    tete_travail = {"crane": ((tete["crane"][0] - boite[0]) * k, (tete["crane"][1] - boite[1]) * k),
                    "hauteur": tete["hauteur"] * k}
    prefixe = f"{perso}_{methode}_{graine}"
    etapes = SORTIE / prefixe
    etapes.mkdir(parents=True, exist_ok=True)
    reglages = {"perso": perso, "methode": methode, "graine": graine, "lora": PERSOS[perso]["lora"], "camera": camera,
                "boite": boite, "tete_px": round(tete["hauteur"], 1), "prompt": prompt(perso, "upper body")}
    if methode == "A":
        image = diffusion(travail_fond, masque_travail, reglages["prompt"], PERSOS[perso]["lora"], graine, 1.0, prefixe)
    else:
        # la table de Sky (le dessus, à 0,75 m, et sa tranche), dans l'image de travail
        coins = [(x, y, z) for x in (7.4, 8.6) for y in (0.85, 1.65) for z in (0.71, 0.75)]
        table = [((u - boite[0]) * k, (v - boite[1]) * k) for u, v in enveloppe(projeter(camera, coins))]
        guide = silhouette(perso, travail_fond, table, tete_travail)
        guide.save(etapes / "1_guide.png")
        reglages["prompt_gris"] = prompt(perso, "upper body", fond_gris=True)
        gris = diffusion(guide, None, reglages["prompt_gris"], PERSOS[perso]["lora"], graine, 0.85, f"{prefixe}_gris")
        gris.save(etapes / "2_sur-gris.png")
        alpha = detourer(gris)
        alpha = Image.fromarray(np.minimum(np.asarray(alpha), np.asarray(masque_travail)))
        alpha.save(etapes / "3_detourage.png")
        colle = travail_fond.copy()
        colle.paste(gris, (0, 0), alpha)
        colle.save(etapes / "4_colle.png")
        zone = alpha.filter(ImageFilter.MaxFilter(31)).filter(ImageFilter.GaussianBlur(12))
        image = diffusion(colle, zone, reglages["prompt"], PERSOS[perso]["lora"], graine, 0.4, f"{prefixe}_fondu")
    image.save(etapes / "5_avant-visage.png")
    image, boite_visage = passe_visage(perso, image, tete_travail, graine, prefixe)
    image.save(etapes / "6_apres-visage.png")
    reglages["boite_visage_travail"] = boite_visage
    # retour sur le fond entier : seule sa place change
    final = fond.copy()
    taille = boite[2] - boite[0]
    final.paste(image.resize((taille, taille), Image.LANCZOS), boite[:2], masque.crop(boite))
    final.save(SORTIE / f"{prefixe}.png")
    reglages["duree_s"] = round(time.time() - debut)
    (SORTIE / f"{prefixe}.json").write_text(json.dumps(reglages, ensure_ascii=False, indent=2) + "\n")
    print(f"{prefixe} : {reglages['duree_s']} s → {SORTIE / f'{prefixe}.png'}")


if __name__ == "__main__":
    main()
