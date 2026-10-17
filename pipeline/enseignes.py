"""Les enseignes du kebab, posées en code sur un fond (les modèles d'image déforment les lettres : CLAUDE.md, « Méthodes de
plan »). Le fond reste sans texte dans le repo ; les enseignes se posent au montage, les mêmes de jour, de pluie et de nuit.

  python3 pipeline/enseignes.py <fond.png> <sortie.png> [axe]      (axe 1 par défaut : la façade vue d'en face)

Les lettres ne se posent que sur les pixels du panneau : ce qui passe devant (les feuilles des arbres) reste devant.
"""
import sys
from PIL import Image, ImageDraw, ImageFont
import numpy as np

POLICE = "/usr/share/fonts/truetype/lato/Lato-Black.ttf"

# par axe : le panneau (x0, y0, x1, y1, en pixels du fond 1536×1024), le texte, sa couleur, l'espacement des lettres,
# et le test « ce pixel est-il le panneau ? » (sur la luminosité moyenne, 0 à 255)
ENSEIGNES = {
    1: [
        {"boite": (205, 396, 1450, 448), "texte": "KEBAB", "couleur": (122, 28, 22), "espacement": 0.18, "taille": 0.86,
         "panneau": lambda lum: lum > 115},
        {"boite": (210, 182, 1445, 236), "texte": "DATASTREAM", "couleur": (236, 228, 210), "espacement": 0.25,
         "panneau": lambda lum: lum < 75},
    ],
}


def poser(fond, sortie, axe=1):
    image = Image.open(fond).convert("RGB")
    lum = np.asarray(image).astype(int).mean(axis=2)
    for e in ENSEIGNES[axe]:
        x0, y0, x1, y1 = e["boite"]
        hauteur = int((y1 - y0) * e.get("taille", 0.72))
        police = ImageFont.truetype(POLICE, hauteur)
        lettres = e["texte"]
        largeurs = [police.getlength(c) for c in lettres]
        pas = hauteur * e["espacement"]
        total = sum(largeurs) + pas * (len(lettres) - 1)
        calque = Image.new("L", image.size, 0)
        d = ImageDraw.Draw(calque)
        x = (x0 + x1) / 2 - total / 2
        for c, w in zip(lettres, largeurs):
            d.text((x, (y0 + y1) / 2), c, font=police, fill=255, anchor="lm")
            x += w + pas
        masque = np.asarray(calque) > 0
        masque &= e["panneau"](lum)                        # pas sur les feuilles qui passent devant
        pixels = np.asarray(image).copy()
        # la lumière du fond (les ombres des feuilles) passe aussi sur les lettres
        zone = lum[y0:y1, x0:x1][e["panneau"](lum[y0:y1, x0:x1])]
        facteur = np.clip(lum[masque] / max(1.0, float(np.median(zone))), 0.6, 1.25)[:, None]
        pixels[masque] = np.clip(np.array(e["couleur"])[None, :] * facteur, 0, 255).astype(np.uint8)
        image = Image.fromarray(pixels)
    image.save(sortie)


if __name__ == "__main__":
    poser(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 1)
