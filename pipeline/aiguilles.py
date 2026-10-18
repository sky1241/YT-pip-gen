"""Les aiguilles de l'horloge du kebab, posées en code à l'heure de la scène : le cadran est peint vide dans le fond (axe 18),
pour que l'heure change d'une scène à l'autre sans repeindre le fond.

  python3 pipeline/aiguilles.py <fond.png> <sortie.png> <HH:MM> [axe]      (axe 18 par défaut : le gros plan)
"""
import math
import sys
from PIL import Image, ImageDraw, ImageFilter

# par axe : le centre du cadran et le rayon des repères, en pixels du fond 1536×1024 (mesurés sur le fond validé)
CADRANS = {18: {"centre": (763, 416), "rayon": 128}}
ENCRE = (40, 34, 30)


def poser(fond, sortie, heure, axe=18):
    h, m = (int(v) for v in heure.split(":"))
    c = CADRANS[axe]
    cx, cy, r = c["centre"][0], c["centre"][1], c["rayon"]
    image = Image.open(fond).convert("RGB")
    # dessinées en grand puis réduites : des bords lisses
    k = 4
    calque = Image.new("RGBA", (image.width * k, image.height * k), (0, 0, 0, 0))
    ombre = Image.new("RGBA", calque.size, (0, 0, 0, 0))
    d, o = ImageDraw.Draw(calque), ImageDraw.Draw(ombre)
    for angle, longueur, epaisseur in ((math.radians((h % 12 + m / 60) * 30), 0.5, 9), (math.radians(m * 6), 0.78, 6)):
        x = cx + longueur * r * math.sin(angle)
        y = cy - longueur * r * math.cos(angle)
        queue = (cx - 0.12 * r * math.sin(angle), cy + 0.12 * r * math.cos(angle))
        for dessin, decalage, couleur in ((o, 4, (0, 0, 0, 70)), (d, 0, ENCRE + (255,))):
            dessin.line([((queue[0] + decalage) * k, (queue[1] + decalage) * k), ((x + decalage) * k, (y + decalage) * k)],
                        fill=couleur, width=epaisseur * k)
    d.ellipse([(cx - 7) * k, (cy - 7) * k, (cx + 7) * k, (cy + 7) * k], fill=ENCRE + (255,))
    ombre = ombre.filter(ImageFilter.GaussianBlur(3 * k)).resize(image.size, Image.LANCZOS)
    calque = calque.resize(image.size, Image.LANCZOS)
    image = Image.alpha_composite(Image.alpha_composite(image.convert("RGBA"), ombre), calque)
    image.convert("RGB").save(sortie)


if __name__ == "__main__":
    poser(sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]) if len(sys.argv) > 4 else 18)
