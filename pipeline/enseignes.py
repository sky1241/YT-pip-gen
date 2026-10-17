"""Les enseignes du kebab, posées en code sur un fond (les modèles d'image déforment les lettres : CLAUDE.md, « Méthodes de
plan »). Le fond reste sans texte dans le repo ; les enseignes se posent au montage, les mêmes de jour, de pluie et de nuit.

  python3 pipeline/enseignes.py <fond.png> <sortie.png> [axe]      (axe 1 par défaut : la façade vue d'en face)

Les lettres ne se posent que sur les pixels du panneau : ce qui passe devant (les feuilles des arbres) reste devant.
"""
import sys
from PIL import Image, ImageDraw, ImageFont
import numpy as np

POLICE = "/usr/share/fonts/truetype/lato/Lato-Black.ttf"

# par axe : les panneaux. Un panneau : sa boîte (x0, y0, x1, y1, en pixels du fond 1536×1024), le test « ce pixel est-il
# le panneau ? » (sur la luminosité moyenne, 0 à 255), et ses textes : chacun centré à une fraction de la largeur, avec sa
# taille (une fraction de la hauteur), l'espacement de ses lettres et sa couleur
ROUGE, BRUN, CREME = (122, 28, 22), (58, 40, 28), (236, 228, 210)
ENSEIGNES = {
    1: [
        {"boite": (205, 396, 1450, 448), "panneau": lambda lum: lum > 115, "textes": [   # l'enseigne du kebab (l'auteur)
            {"texte": "CHEZ MOMO", "centre": 0.19, "taille": 0.6, "espacement": 0.12, "couleur": BRUN},
            {"texte": "KEBAB", "centre": 0.5, "taille": 0.86, "espacement": 0.18, "couleur": ROUGE},
            {"texte": "24/24 · 7/7", "centre": 0.81, "taille": 0.6, "espacement": 0.1, "couleur": BRUN}]},
        {"boite": (210, 182, 1445, 236), "panneau": lambda lum: lum < 75, "textes": [
            {"texte": "DATASTREAM", "centre": 0.5, "taille": 0.72, "espacement": 0.25, "couleur": CREME}]},
    ],
}


def poser(fond, sortie, axe=1):
    image = Image.open(fond).convert("RGB")
    lum = np.asarray(image).astype(int).mean(axis=2)
    pixels = np.asarray(image).copy()
    for panneau in ENSEIGNES[axe]:
        x0, y0, x1, y1 = panneau["boite"]
        zone = lum[y0:y1, x0:x1][panneau["panneau"](lum[y0:y1, x0:x1])]
        reference = max(1.0, float(np.median(zone)))
        for e in panneau["textes"]:
            hauteur = int((y1 - y0) * e["taille"])
            police = ImageFont.truetype(POLICE, hauteur)
            largeurs = [police.getlength(c) for c in e["texte"]]
            pas = hauteur * e["espacement"]
            total = sum(largeurs) + pas * (len(largeurs) - 1)
            calque = Image.new("L", image.size, 0)
            d = ImageDraw.Draw(calque)
            x = x0 + (x1 - x0) * e["centre"] - total / 2
            for c, w in zip(e["texte"], largeurs):
                d.text((x, (y0 + y1) / 2), c, font=police, fill=255, anchor="lm")
                x += w + pas
            masque = (np.asarray(calque) > 0) & panneau["panneau"](lum)    # pas sur les feuilles qui passent devant,
            masque &= lum < reference + 25                                 # ni sur les traits de pluie
            # la lumière du fond (les ombres des feuilles) passe aussi sur les lettres
            facteur = np.clip(lum[masque] / reference, 0.6, 1.25)[:, None]
            pixels[masque] = np.clip(np.array(e["couleur"])[None, :] * facteur, 0, 255).astype(np.uint8)
    Image.fromarray(pixels).save(sortie)


if __name__ == "__main__":
    poser(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 1)
