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

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, str(Path(__file__).resolve().parent))
from essai_integration import DECORS, ESSAIS, PERSOS, TRAVAIL, avec_lisere, coller_cadre, sans_frange   # noqa: E402
import essai_integration as EI  # noqa: E402
from lisser_fonds import dernier_fond  # noqa: E402
from recaler_camera import projeter  # noqa: E402

RACINE = Path(__file__).resolve().parent.parent


def distance(perso, camera, pose=None):
    """Sa distance à la caméra : à sa place debout (--pose, notée dans ses réglages), sinon sur la banquette du fond."""
    if pose:
        return math.hypot(pose["x"] - camera["x"], pose["y"] - camera["y"])
    return math.hypot(PERSOS[perso]["x"] - camera["x"], 0.62 - camera["y"])


def poser_objet(image, camera, fichier, x, y, largeur, z=0.75, ancre=0.5, ombre=0.35, teinte=0.55, plat=0.0, vue=45):
    """Un objet découpé (image/accessoires/…) posé sur une surface du décor (2026-10-24) : en (x, y, z) dans le plan, large de
    `largeur` mètres, son point `ancre` (la part de sa hauteur, depuis le haut, qui touche la surface) sur ce point. Une ombre
    de contact dessous (une ellipse floue, l'empreinte vue par la caméra) ; ses couleurs un peu tirées vers la lumière du décor
    (`teinte`). L'objet reste l'image validée : pas de nouvelle génération. Les objets sont dessinés vus d'en haut (`vue`,
    l'angle en degrés ; une pizza vers 58°) ; la caméra d'un plan assis les voit plus à plat : l'image est tassée en hauteur
    du rapport des sinus, à la puissance `plat` (1 : un objet plat comme une pizza ; 0 : une bouteille, rien ne change)."""
    objet = Image.open(fichier).convert("RGBA")
    objet = objet.crop(objet.split()[3].point(lambda v: 255 if v > 128 else 0).getbbox())
    a = math.radians(camera["cap"])
    droite, avant = (-math.sin(a), math.cos(a)), (math.cos(a), math.sin(a))
    r = largeur / 2
    (ug, vg), (ud, vd), (ua, va), (ur, vr), (uc, vc) = projeter(camera, [
        (x - droite[0] * r, y - droite[1] * r, z), (x + droite[0] * r, y + droite[1] * r, z),
        (x + avant[0] * r, y + avant[1] * r, z), (x - avant[0] * r, y - avant[1] * r, z), (x, y, z)])
    largeur_px = math.hypot(ud - ug, vd - vg)
    k = largeur_px / objet.width
    distance = math.hypot(x - camera["x"], y - camera["y"])
    elevation = math.atan2(camera["hauteur"] - z, distance)
    tasse = (max(math.sin(elevation), 0.05) / math.sin(math.radians(vue))) ** plat
    objet = objet.resize((max(1, round(objet.width * k)), max(1, round(objet.height * k * min(tasse, 1.0)))), Image.LANCZOS)
    coin = (round(uc - objet.width / 2), round(vc - ancre * objet.height))
    # l'ombre de contact : l'empreinte de l'objet sur la surface, vue de la caméra
    hauteur_ombre = max(abs(vr - va), 4)
    calque = Image.new("L", image.size, 0)
    ImageDraw.Draw(calque).ellipse([uc - 0.48 * largeur_px, vc - 0.5 * hauteur_ombre, uc + 0.48 * largeur_px,
                                    vc + 0.5 * hauteur_ombre], fill=int(255 * ombre))
    calque = calque.filter(ImageFilter.GaussianBlur(max(2, largeur_px / 30)))
    image = Image.composite(Image.new("RGB", image.size, (25, 15, 10)), image, calque)
    # la lumière du décor : la couleur moyenne de la surface sous l'objet, en teinte douce
    zone = image.crop((coin[0], coin[1], coin[0] + objet.width, coin[1] + objet.height))
    moyenne = np.asarray(zone, np.float32).reshape(-1, 3).mean(axis=0)
    gain = (moyenne / max(float(moyenne.mean()), 1)) ** teinte
    rgb = np.clip(np.asarray(objet, np.float32)[..., :3] * gain, 0, 255).astype(np.uint8)
    objet = Image.fromarray(np.dstack([rgb, np.asarray(objet)[..., 3]]), "RGBA")
    image.paste(objet, coin, objet)
    return image


def ombre_pieds(image, camera, pose, force=0.55):
    """Debout (--pose) : une ombre de contact sous ses pieds, posée sur le sol avant lui (2026-10-24 : sans elle, Sky et
    Maëlle sur le palier de l'axe 10 avaient l'air collés). Une ellipse floue de 64 × 50 cm sous ses pieds, à leur hauteur."""
    a = math.radians(camera["cap"])
    droite, avant = (-math.sin(a), math.cos(a)), (math.cos(a), math.sin(a))
    x, y, z = pose["x"], pose["y"], pose["z"]
    (ug, vg), (ud, vd), (ua, va), (ur, vr), (uc, vc) = projeter(camera, [
        (x - droite[0] * 0.32, y - droite[1] * 0.32, z), (x + droite[0] * 0.32, y + droite[1] * 0.32, z),
        (x + avant[0] * 0.25, y + avant[1] * 0.25, z), (x - avant[0] * 0.25, y - avant[1] * 0.25, z), (x, y, z)])
    largeur, hauteur = math.hypot(ud - ug, vd - vg), max(abs(vr - va), 4)
    calque = Image.new("L", image.size, 0)
    ImageDraw.Draw(calque).ellipse([uc - largeur / 2, vc - hauteur / 2, uc + largeur / 2, vc + hauteur / 2],
                                   fill=int(255 * force))
    calque = calque.filter(ImageFilter.GaussianBlur(max(3, largeur / 12)))
    return Image.composite(Image.new("RGB", image.size, (30, 18, 10)), image, calque)


def composer(axe, essais):
    recalage = json.loads((DECORS / axe / "camera.json").read_text())
    camera, devant = recalage["camera"], recalage.get("devant", ())
    image = Image.open(dernier_fond(DECORS / axe)).convert("RGB")
    reglages = [(nom, json.loads((ESSAIS / axe / f"{nom}.json").read_text())) for nom in essais]
    for nom, r in sorted(reglages, key=lambda e: -distance(e[1]["perso"], camera, e[1].get("pose"))):
        etapes = ESSAIS / axe / nom
        if r.get("pose"):                   # debout : son ombre de contact d'abord, sur le sol
            image = ombre_pieds(image, camera, r["pose"])
        x0, y0, x1, _ = r["boite"]
        taille = (x1 - x0, x1 - x0)
        if r["methode"] in ("B", "D"):
            # comme à la fin de son essai : le perso dessiné sur gris, collé dans son cadre, puis ses pixels repassés (la
            # lumière du décor, le visage) dans sa boîte de travail
            gris = Image.open(etapes / "2_sur-gris.png").convert("RGB")
            # sa posture, comme dans son essai : debout (--pose) ou assis ; sinon coller_cadre lui prenait les jambes d'un
            # perso assis
            EI.POSE.pop(r["perso"], None)
            if r.get("pose"):
                EI.POSE[r["perso"]] = r["pose"]
            EI.POSTURE[0] = r.get("posture") or "mange"
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
    objets = []
    if "--objets" in essais:            # --objets <fichier.json> : [{"fichier", "x", "y", "largeur", "ancre"}…], posés après les persos
        i = essais.index("--objets")
        objets = json.loads(Path(essais[i + 1]).read_text())
        essais = essais[:i] + essais[i + 2:]
    image = composer(axe, essais)
    camera = json.loads((DECORS / axe / "camera.json").read_text())["camera"]
    for o in sorted(objets, key=lambda o: -math.hypot(o["x"] - camera["x"], o["y"] - camera["y"])):
        image = poser_objet(image, camera, RACINE / o["fichier"], o["x"], o["y"], o["largeur"], o.get("z", 0.75),
                            o.get("ancre", 0.5), plat=o.get("plat", 0.0), vue=o.get("vue", 45))
    image.save(sortie)
    print(sortie)
