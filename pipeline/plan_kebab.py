"""Plan du kebab vu de dessus, d'après la maquette (image/decors/kebab/), en mètres. y = 0 au mur du fond, la rue en bas.

  python3 pipeline/plan_kebab.py image/decors/kebab/plan_v1.png
"""
from PIL import Image, ImageDraw, ImageFont
import sys
E = 90                      # pixels par mètre
MX, MY = 60, 60             # marges
W, D = 11.0, 8.0            # la salle : largeur (gauche-droite) et profondeur (fond-rue)
img = Image.new("RGB", (int(W * E + 2 * MX), int(D * E + 2 * MY + 60)), "white")
d = ImageDraw.Draw(img)
try:
    F = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 15)
    G = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 17)
except OSError:
    F = G = ImageFont.load_default()
def p(x, y): return (MX + x * E, MY + y * E)
def rect(x0, y0, x1, y1, fill, outline="black", w=2):
    d.rectangle([p(x0, y0), p(x1, y1)], fill=fill, outline=outline, width=w)
def txt(x, y, s, f=F, c="black"):
    d.text(p(x, y), s, fill=c, font=f, anchor="mm")
def chaise(x, y, vers):
    """Une chaise de 0,45 m ; « vers » : le côté où regarde la personne assise (son dossier est à l'opposé)."""
    r = 0.22
    rect(x - r, y - r, x + r, y + r, "#c96a4a", w=1)
    dos = {"bas": (x - r, y - r, x + r, y - r + 0.08), "haut": (x - r, y + r - 0.08, x + r, y + r),
           "droite": (x - r, y - r, x - r + 0.08, y + r), "gauche": (x + r - 0.08, y - r, x + r, y + r)}[vers]
    rect(*dos, "#5a2a1a", w=1)
# les murs
d.line([p(0, D), p(0, 0), p(W, 0), p(W, D)], fill="black", width=6)
# la devanture : ouverte, les panneaux vitrés repliés à gauche
d.line([p(0.6, D), p(W, D)], fill="#7fb2d9", width=3)
rect(0, D - 0.15, 0.6, D + 0.15, "#7fb2d9")
txt(W / 2, D + 0.45, "LA RUE : devanture ouverte, panneaux vitrés repliés à gauche (ils ferment le kebab le soir)", F)
# la cuisine, contre le mur gauche
rect(0, 1.4, 1.0, 6.4, "#d9d9d9")
txt(0.5, 3.0, "broche", G); txt(0.5, 3.4, "grill"); txt(0.5, 4.6, "friteuse"); txt(0.5, 5.6, "plans inox")
# le comptoir en L : petit côté devant (la caisse), long côté vers le fond (les salades)
rect(1.2, 6.2, 3.0, 7.0, "#b0b8c0"); txt(2.0, 6.6, "CAISSE", G)
rect(2.3, 1.8, 3.0, 6.2, "#b0b8c0"); txt(2.65, 4.6, "salades", G); txt(2.65, 5.0, "sauces")
txt(2.65, 2.4, "passe")
# le frigo à boissons, au fond à gauche
rect(1.6, 0.0, 2.3, 0.7, "#9fd3e6"); txt(1.95, 0.35, "frigo")
# le miroir, au mur du fond
d.line([p(3.8, 0.05), p(7.2, 0.05)], fill="#6a8fb0", width=10); txt(5.5, 0.35, "MIROIR (Sky y écrit)", G)
# les tables du milieu : 4 tables pour 4, deux chaises face à face de chaque côté
for ty in (1.3, 3.0, 4.6, 6.1):
    tx = 5.5
    rect(tx - 0.4, ty - 0.6, tx + 0.4, ty + 0.6, "#d9a066")
    for cy in (ty - 0.3, ty + 0.3):
        chaise(tx - 0.65, cy, "droite"); chaise(tx + 0.65, cy, "gauche")
# la banquette le long de la rampe, à droite, et ses 4 tables perpendiculaires
rect(8.6, 1.0, 9.2, 7.2, "#b03a2e"); txt(8.9, 0.75, "banquette")
for ty in (1.4, 3.1, 4.8, 6.5):
    rect(7.3, ty - 0.3, 8.6, ty + 0.3, "#d9a066")
    chaise(7.9, ty - 0.55, "bas"); chaise(7.9, ty + 0.55, "haut")
# la rampe ouverte et l'escalier vers Datastream
d.line([p(9.3, 0.6), p(9.3, 7.6)], fill="#8a5a2b", width=4)
rect(9.4, 0.4, 10.9, 7.8, "#e8e0d0")
for k in range(14):
    yy = 0.4 + k * 0.5; d.line([p(9.4, yy), p(10.9, yy)], fill="#a09080", width=1)
txt(10.15, 4.2, "ESCALIER", G); txt(10.15, 4.6, "monte vers le fond")
rect(9.6, 0.0, 10.7, 0.12, "#8a5a2b"); txt(10.15, -0.25, "porte de Datastream (en haut)")
txt(10.15, 7.55, "pied : depuis la rue")
d.text((MX, 15), "Le kebab vu de dessus (plan de travail, 1 carreau = 1 m)", fill="black", font=G)
img.save(sys.argv[1])
