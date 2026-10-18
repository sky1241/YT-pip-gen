"""Plan du kebab vu de dessus, d'après la maquette (image/decors/kebab/), en mètres. y = 0 au mur du fond, la rue en bas.

  python3 pipeline/plan_kebab.py image/decors/kebab/plan_v7.png   (jamais par-dessus une version validée)
"""
from PIL import Image, ImageDraw, ImageFont
import sys
E = 90                      # pixels par mètre
MX, MY = 60, 100            # marges
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
# la devanture ouverte va jusqu'au coin de droite, sans muret : l'escalier part d'un palier à l'intérieur, derrière elle
# (l'auteur, le 2026-10-17)
d.line([p(0.6, D), p(W, D)], fill="#7fb2d9", width=3)
rect(0, D - 0.15, 0.6, D + 0.15, "#7fb2d9")
txt(W / 2, D + 0.45, "LA RUE : devanture ouverte sur toute la largeur, panneaux vitrés repliés à gauche (ils ferment le kebab le soir)", F)
# la cuisine, contre le mur gauche
rect(0, 1.4, 1.0, 6.4, "#d9d9d9")
txt(0.5, 3.0, "broche", G); txt(0.5, 3.4, "grill"); txt(0.5, 4.6, "friteuse"); txt(0.5, 5.6, "plans inox")
# le comptoir en L : petit côté devant (la caisse), long côté vers le fond (les salades)
rect(1.2, 6.2, 3.0, 7.0, "#b0b8c0")
rect(2.3, 1.8, 3.0, 6.2, "#b0b8c0"); txt(2.65, 4.6, "salades", G); txt(2.65, 5.0, "sauces")
# la caisse à l'angle du L, au bout du grand côté, juste avant les salades, tournée vers Mohamed (l'auteur, le 2026-10-17)
rect(2.4, 5.85, 2.9, 6.2, "#34343a"); d.text(p(1.25, 6.45), "CAISSE à l'angle,", fill="black", font=G)
d.text(p(1.25, 6.72), "tournée vers Mohamed ←", fill="black", font=F)
txt(2.65, 2.4, "passe")
# le frigo à boissons, au fond à gauche
rect(1.6, 0.0, 2.3, 0.7, "#9fd3e6"); txt(1.95, 0.35, "frigo")
# le miroir, au mur du fond
# le miroir sur toute la longueur de la banquette du fond, à fleur de son bout gauche (l'auteur, le 2026-10-17)
d.line([p(3.6, 0.05), p(8.6, 0.05)], fill="#6a8fb0", width=10); txt(5.6, -0.25, "MIROIR, au-dessus de toute la banquette du fond", G)
# 6 tables identiques (0,8 × 1,2 m), deux chaises de chaque long côté, face à face
# au fond, dans l'angle de la banquette, la table de Sky (« au fond, table bancale », texte du CERN, l. 14) : une table pour cinq
# (l'auteur, le 2026-10-17). Sky et Maëlle sur la banquette du fond, deux chaises en face, Patrick au bout, sur la banquette de droite
rect(7.4, 0.85, 8.6, 1.65, "#d9a066"); txt(8.0, 1.25, "table de Sky")
chaise(7.7, 1.9, "haut"); chaise(8.3, 1.9, "haut")
# au milieu : 2 tables
for ty in (3.6, 5.9):
    tx = 5.5
    rect(tx - 0.4, ty - 0.6, tx + 0.4, ty + 0.6, "#d9a066")
    for cy in (ty - 0.3, ty + 0.3):
        chaise(tx - 0.65, cy, "droite"); chaise(tx + 0.65, cy, "gauche")
# à droite : la banquette le long de la rampe, et 2 tables perpendiculaires, un petit bout contre elle (la première, près de l'angle,
# enlevée pour la table de Sky : l'auteur, le 2026-10-17)
# la banquette en L : sous le miroir, le long du mur du fond, puis le long de la rampe
rect(3.6, 0.2, 9.2, 0.8, "#b03a2e"); rect(8.6, 0.8, 9.2, 6.9, "#b03a2e"); txt(3.2, 0.5, "banquette")
for ty in (4.0, 6.2):
    rect(7.4, ty - 0.4, 8.6, ty + 0.4, "#d9a066")
    for cx in (7.7, 8.3):
        chaise(cx, ty - 0.65, "bas"); chaise(cx, ty + 0.65, "haut")
# l'escalier vers Datastream : son côté salle est fermé sous les marches et suit leur pente, la rampe au-dessus ; au fond, il
# touche le plafond et c'est un mur. La banquette de droite est adossée à ce côté ; l'escalier s'ouvre sur le palier, devant
# (l'auteur, le 2026-10-17)
# l'escalier part d'un palier, à l'intérieur, au bout de la banquette, et monte vers le fond ; la rampe s'arrête au palier
d.line([p(9.3, 0), p(9.3, 6.4)], fill="black", width=6)
rect(9.4, 0.4, 10.9, 6.4, "#e8e0d0")
for k in range(12):
    yy = 0.4 + k * 0.5; d.line([p(9.4, yy), p(10.9, yy)], fill="#a09080", width=1)
rect(9.4, 6.4, 10.9, 7.9, "#f2ece0", outline="#a09080", w=1); txt(10.15, 7.15, "palier", F)
txt(10.15, 4.2, "ESCALIER", G); txt(10.15, 4.6, "en bois, il grince"); txt(10.15, 5.0, "monte vers le fond")
rect(9.6, 0.0, 10.7, 0.12, "#8a5a2b"); txt(10.15, -0.25, "porte de Datastream (en haut)")
txt(10.15, 6.15, "pied : depuis la salle", F)
d.text((MX, 15), "Le kebab vu de dessus (plan de travail, 1 carreau = 1 m)", fill="black", font=G)
# la table de Navier-Stokes : Sky s'y assoit dans cet épisode, près de la vitrine (l'auteur, le 2026-10-17)
txt(8.0, 6.2, "Navier-Stokes", F)
# qui s'assoit où, à la table de Sky
txt(8.0, 0.5, "Sky, Maëlle", F, "white"); txt(8.9, 1.25, "P", G, "white")
d.text(p(9.45, 1.1), "← Patrick, au bout", fill="black", font=F)
img.save(sys.argv[1])

# Les axes de caméra (image/decors/kebab/axes.md) : python3 pipeline/plan_kebab.py <sortie.png> axes
# numéro : (x, y de la caméra, direction du regard en degrés : 0 = vers la droite, 90 = vers la rue, 270 = vers le fond)
AXES = {
    1: (5.0, 15.0, 270), 2: (4.6, 9.7, 265), 3: (4.8, 1.3, 95), 4: (1.65, 4.0, 345), 5: (10.15, 3.2, 160),
    6: (6.42, 2.33, 323), 7: (7.8, 0.5, 98), 8: (6.3, 2.5, 180), 9: (3.4, 3.1, 180), 10: (5.8, 7.7, 343),
    11: (10.15, 7.3, 270), 12: (4.6, 2.0, 315), 13: (7.6, 0.45, 82), 14: (6.2, 3.0, 315), 15: (6.0, 5.0, 100),
    16: (3.6, 2.4, 225), 17: (8.0, 1.25, 270), 18: (3.0, 2.4, 200), 19: (8.9, 1.7, 90),
    20: (6.95, 1.25, 0), 21: (8.95, 1.25, 180), 22: (8.0, 5.1, 90), 23: (8.0, 8.6, 270),
    24: (6.75, 6.2, 0), 25: (8.95, 6.2, 180),
}
# un seul axe, pour le joindre au prompt de son fond : python3 pipeline/plan_kebab.py <sortie.png> axe <numéro>
if len(sys.argv) > 3 and sys.argv[2] == "axe":
    import math
    x, y, a = AXES[int(sys.argv[3])]
    r = math.radians(a)
    bout = [p(x + 9 * math.cos(r + math.radians(da)), y + 9 * math.sin(r + math.radians(da))) for da in (-30, 30)]
    voile = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(voile).polygon([p(x, y), *bout], fill=(16, 96, 192, 60))
    masque = Image.new("L", img.size, 0)      # le cône s'arrête aux murs (la rue reste, pour les axes 1 et 2)
    ImageDraw.Draw(masque).rectangle([p(0, 0), p(W, D + 1.6)], fill=255)
    voile.putalpha(Image.composite(voile.getchannel("A"), Image.new("L", img.size, 0), masque))
    img = Image.alpha_composite(img.convert("RGBA"), voile).convert("RGB")
    d = ImageDraw.Draw(img)
    for da in (-30, 30):
        k = 0.0
        while k < 9 and 0 <= x + k * math.cos(r + math.radians(da)) <= W and -0.0 <= y + k * math.sin(r + math.radians(da)) <= D + 1.6:
            k += 0.05
        d.line([p(x, y), p(x + k * math.cos(r + math.radians(da)), y + k * math.sin(r + math.radians(da)))], fill="#1060c0", width=3)
    cx, cy = p(x, y)
    d.ellipse([cx - 16, cy - 16, cx + 16, cy + 16], fill="#1060c0", outline="white", width=3)
    d.text((cx, cy), sys.argv[3], fill="white", font=G, anchor="mm")
    d.text((cx + 22, cy + 6), "CAMÉRA", fill="#1060c0", font=G)
    img.save(sys.argv[1])
if len(sys.argv) > 2 and sys.argv[2] == "axes":
    import math
    for n, (x, y, a) in AXES.items():
        r = math.radians(a)
        for da, longueur, epaisseur in ((0, 1.3, 3), (-28, 1.0, 1), (28, 1.0, 1)):
            rr = r + math.radians(da)
            d.line([p(x, y), p(x + longueur * math.cos(rr), y + longueur * math.sin(rr))], fill="#1060c0", width=epaisseur)
        cx, cy = p(x, y)
        d.ellipse([cx - 13, cy - 13, cx + 13, cy + 13], fill="#1060c0", outline="white", width=2)
        d.text((cx, cy), str(n), fill="white", font=F, anchor="mm")
    img.save(sys.argv[1])
