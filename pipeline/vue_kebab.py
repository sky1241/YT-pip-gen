"""La vue d'un axe du kebab en volumes simples (une maquette « blockout »), à joindre au prompt de son fond : ChatGPT peint
par-dessus, comme il a peint le plan vu de dessus. Les mesures sont celles de pipeline/plan_kebab.py (plan v5), en mètres ;
les axes sont lus dans plan_kebab.py, qui reste la seule source.

  python3 pipeline/vue_kebab.py <sortie.png> <numéro d'axe>
"""
import ast
import math
import sys
from pathlib import Path
from PIL import Image, ImageDraw

LARGEUR, HAUTEUR = 1536, 1024
_source = Path(__file__).with_name("plan_kebab.py").read_text()
_debut = _source.index("AXES = {") + len("AXES = ")
AXES = ast.literal_eval(_source[_debut:_source.index("}", _debut) + 1])

# la hauteur de l'œil (m), l'inclinaison (degrés, négatif = vers le bas) et le champ horizontal (degrés), par axe
ASSIS, DEBOUT = 1.2, 1.6
CAMERAS = {n: (ASSIS, 0, 66) for n in (6, 7, 20, 21, 22, 24, 25)}
CAMERAS.update({n: (DEBOUT, 0, 66) for n in (1, 2, 3, 4, 8, 9, 10, 12, 14, 15, 16, 19, 23)})
CAMERAS[2] = (DEBOUT, -3, 76)         # du trottoir : toute la devanture dans le cadre, la caisse et la rampe comprises
CAMERAS[10] = (DEBOUT, 0, 72)        # du devant de la salle, vers le palier et l'escalier : on voit descendre
CAMERAS[1] = (DEBOUT, 8, 84)         # du trottoir d'en face, un peu vers le haut : la devanture et les étages
CAMERAS[8] = (DEBOUT, 0, 70)          # le mur de la cuisine de face : la ligne du plafond reste droite (l'auteur)
CAMERAS[7] = (ASSIS, 0, 80)          # plus large : la rampe de l'escalier à gauche et la caisse à droite (l'auteur)
CAMERAS.update({5: (2.1, -25, 70), 11: (DEBOUT, 18, 66), 13: (DEBOUT, -15, 66), 17: (2.2, -89, 60), 18: (DEBOUT, 10, 30)})

FOND, OBJETS = [], []   # les surfaces plates du décor, et les boîtes ; tout passe par un tampon de profondeur (vue)


def boite(x0, y0, x1, y1, z0, z1, couleur, liste=OBJETS, morceau=99, trait=True, groupe=None):
    """Une boîte, en coordonnées du plan (x vers la droite, y vers la rue, z vers le haut). « morceau » la coupe en
    morceaux, dont les jointures se dessinent (les coussins des banquettes) ; trait=False : pas de jointures."""
    groupe = len(OBJETS) + len(FOND) if groupe is None else groupe
    nx = max(1, math.ceil((x1 - x0) / morceau - 1e-9))
    ny = max(1, math.ceil((y1 - y0) / morceau - 1e-9))
    for i in range(nx):
        for j in range(ny):
            liste.append(("boite", (x0 + (x1 - x0) * i / nx, y0 + (y1 - y0) * j / ny,
                                    x0 + (x1 - x0) * (i + 1) / nx, y0 + (y1 - y0) * (j + 1) / ny, z0, z1), couleur, trait, groupe))


def plaque(points, normale, couleur):
    """Une surface plate du décor (sol, mur, plafond) : ses coins, et le côté d'où elle se voit."""
    FOND.append(("plaque", (points, normale), couleur, True))


# --- la rue, en face ---
plaque([(-8, 8, 0), (19, 8, 0), (19, 15.5, 0), (-8, 15.5, 0)], (0, 0, 1), "#b4aa96")
plaque([(-8, 8, 0.01), (19, 8, 0.01), (19, 9.8, 0.01), (-8, 9.8, 0.01)], (0, 0, 1), "#cdc1aa")      # le trottoir
plaque([(-8, 10.2, 0.02), (19, 10.2, 0.02), (19, 12.0, 0.02), (-8, 12.0, 0.02)], (0, 0, 1), "#6f8f4a")  # la voie du tram, en herbe
for yr in (10.7, 11.5):                                                                         # les rails du tram
    plaque([(-8, yr - 0.04, 0.03), (19, yr - 0.04, 0.03), (19, yr + 0.04, 0.03), (-8, yr + 0.04, 0.03)], (0, 0, 1), "#55524c")
plaque([(-8, 12.4, 0.01), (19, 12.4, 0.01), (19, 15.5, 0.01), (-8, 15.5, 0.01)], (0, 0, 1), "#cdc1aa")  # le trottoir d'en face
plaque([(-8, 15.5, 0), (19, 15.5, 0), (19, 15.5, 9), (-8, 15.5, 9)], (0, -1, 0), "#c8b796")              # l'immeuble d'en face
for xf in range(-7, 19, 3):
    for zf in (3.6, 6.4):
        plaque([(xf, 15.48, zf), (xf + 1.4, 15.48, zf), (xf + 1.4, 15.48, zf + 1.6), (xf, 15.48, zf + 1.6)], (0, -1, 0), "#8a7d66")
# --- la salle ---
plaque([(0, 0, 0), (11, 0, 0), (11, 8, 0), (0, 8, 0)], (0, 0, 1), "#c9a27a")                    # le sol
plaque([(0, 0, 0), (11, 0, 0), (11, 0, 3), (0, 0, 3)], (0, 1, 0), "#e2cda3")                    # le mur du fond
plaque([(0, 0, 0), (0, 8, 0), (0, 8, 3), (0, 0, 3)], (1, 0, 0), "#dcc69c")                      # le mur de gauche
plaque([(11, 0, 0), (11, 8, 0), (11, 8, 3), (11, 0, 3)], (-1, 0, 0), "#dcc69c")                 # le mur de droite
for x0, y0, x1, y1 in ((0, 0, 9.3, 8), (9.3, 6.4, 11, 8)):    # le plafond ; au-dessus de l'escalier, la cage monte à l'étage
    plaque([(x0, y0, 3), (x1, y0, 3), (x1, y1, 3), (x0, y1, 3)], (0, 0, -1), "#d6c29e")
# la cage de l'escalier, jusqu'à l'étage : on monte, et au fond, en haut, la porte de Datastream dans son mur (l'auteur)
plaque([(9.3, 0, 3), (11, 0, 3), (11, 0, 6), (9.3, 0, 6)], (0, 1, 0), "#d8c49c")              # le mur du haut, au fond
plaque([(11, 0, 3), (11, 6.4, 3), (11, 6.4, 6), (11, 0, 6)], (-1, 0, 0), "#d2bd94")           # le mur de droite, en haut
plaque([(9.3, 0, 6), (11, 0, 6), (11, 6.4, 6), (9.3, 6.4, 6)], (0, 0, -1), "#cdb88f")         # le plafond de la cage
plaque([(9.3, 0, 3), (9.3, 6.4, 3), (9.3, 6.4, 6), (9.3, 0, 6)], (1, 0, 0), "#d2bd94")          # le mur gauche, en haut
plaque([(9.3, 6.4, 3), (11, 6.4, 3), (11, 6.4, 6), (9.3, 6.4, 6)], (0, -1, 0), "#cdb88f")     # au-dessus du palier
plaque([(9.3, 0, 3.0), (11, 0, 3.0), (11, 0.6, 3.0), (9.3, 0.6, 3.0)], (0, 0, 1), "#b07a45")   # le palier du haut
plaque([(9.75, 0.01, 3.0), (10.65, 0.01, 3.0), (10.65, 0.01, 5.05), (9.75, 0.01, 5.05)], (0, 1, 0), "#7a4a24")  # la porte
plaque([(10.45, 0.005, 3.95), (10.55, 0.005, 3.95), (10.55, 0.005, 4.05), (10.45, 0.005, 4.05)], (0, 1, 0), "#c9c9c9")
plaque([(0, 8, 2.7), (11, 8, 2.7), (11, 8, 3), (0, 8, 3)], (0, -1, 0), "#cdb88f")               # le linteau, vu de dedans
# la façade, vue de la rue : un petit immeuble de deux étages (texte du CERN, l. 10) : le kebab, Datastream au premier,
# un étage au-dessus ; la devanture vitrée sur toute la largeur du rez-de-chaussée (l'auteur, axe 1)
plaque([(0, 8, 2.7), (11, 8, 2.7), (11, 8, 9.4), (0, 8, 9.4)], (0, 1, 0), "#d8c6a2")
plaque([(-0.1, 8.0, 9.4), (11.1, 8.0, 9.4), (11.1, 8.35, 9.4), (-0.1, 8.35, 9.4)], (0, 0, -1), "#b9a47e")   # la corniche
plaque([(-0.1, 8.35, 9.4), (11.1, 8.35, 9.4), (11.1, 8.35, 9.7), (-0.1, 8.35, 9.7)], (0, 1, 0), "#b9a47e")
plaque([(0, 8.02, 2.7), (11, 8.02, 2.7), (11, 8.02, 3.0), (0, 8.02, 3.0)], (0, 1, 0), "#8a5a2b")  # le bandeau, sans enseigne
for zf in (3.7, 6.7):                                                    # les fenêtres : Datastream au premier, puis le deuxième
    for xf in (0.8, 3.5, 6.2, 8.9):
        plaque([(xf, 8.02, zf), (xf + 1.4, 8.02, zf), (xf + 1.4, 8.02, zf + 1.7), (xf, 8.02, zf + 1.7)], (0, 1, 0), "#7d8a94")
# les immeubles voisins, de part et d'autre, leurs rez-de-chaussée fermés
for x0, x1, hauteur, teinte in ((-9, 0, 10.5, "#c9b391"), (11, 20, 9.0, "#cbbba0")):
    plaque([(x0, 8, 0), (x1, 8, 0), (x1, 8, hauteur), (x0, 8, hauteur)], (0, 1, 0), teinte)
    for xf in range(int(x0) + 1, int(x1) - 1, 3):
        for zf in (3.7, 6.7):
            plaque([(xf, 8.02, zf), (xf + 1.4, 8.02, zf), (xf + 1.4, 8.02, zf + 1.7), (xf, 8.02, zf + 1.7)], (0, 1, 0), "#7d8a94")
        plaque([(xf, 8.02, 0.3), (xf + 2.2, 8.02, 0.3), (xf + 2.2, 8.02, 2.4), (xf, 8.02, 2.4)], (0, 1, 0), "#8f8676")
# le ciel, loin derrière
plaque([(-200, -60, 0), (200, -60, 0), (200, -60, 120), (-200, -60, 120)], (0, 1, 0), "#a9c7d8")

# --- la cuisine et le comptoir en L, à gauche ---
INOX = "#aeb3b8"
boite(0, 1.4, 0.9, 6.4, 0, 0.9, INOX, morceau=0.5)                   # le plan de travail contre le mur
boite(0.35, 2.65, 0.65, 2.95, 0.9, 1.6, "#8b5a2b")       # la broche
boite(0, 2.3, 1.0, 3.3, 2.1, 2.5, INOX)                   # la hotte
plaque([(0.01, 3.95 + 0.17 * math.cos(k * math.pi / 8), 2.25 + 0.17 * math.sin(k * math.pi / 8)) for k in range(16)],
       (1, 0, 0), "#f2efe6")                                # l'horloge, ronde (un carré, ChatGPT en faisait un panneau)
boite(1.2, 6.2, 3.0, 7.0, 0, 1.0, INOX)                   # le petit côté, devant
boite(2.3, 1.8, 3.0, 6.2, 0, 1.0, INOX, morceau=0.5)                 # le long côté
# la vitrine des salades, encastrée dans le comptoir (l'auteur, axe 8) : les bacs à fleur du dessus, une vitre basse côté salle
for k, bac in enumerate(("#6aa84f", "#cc3b2b", "#efe6d2", "#7b3f8c", "#e08a2c", "#9bc46a")):
    boite(2.4, 3.6 + k * 0.37, 2.9, 3.6 + k * 0.37 + 0.33, 0.97, 1.005, bac)
boite(2.98, 3.6, 3.02, 5.8, 1.0, 1.35, "verre")
# la caisse, à l'angle du L, au bout du grand côté, juste avant les salades (l'auteur, axe 2) ; son écran tourné vers Mohamed,
# vers l'intérieur du comptoir (vers la gauche), son dos vers la salle
boite(2.45, 5.88, 2.85, 6.18, 1.0, 1.15, "#34343a")
boite(2.45, 5.9, 2.51, 6.16, 1.15, 1.38, "#34343a")
boite(1.6, 0, 2.3, 0.7, 0, 2.0, "#c8ccd0")                # le frigo à boissons
boite(1.62, 0.7, 2.28, 0.72, 0.1, 1.9, "#9fd3e6")
boite(0, 7.8, 0.6, 8.0, 0, 2.7, "#9fc7d6")                # les panneaux vitrés repliés

# --- la banquette en L et le miroir ---
ROUGE = "#a8342b"
boite(3.55, 0, 8.65, 0.02, 1.05, 1.95, "#6b4a2b")          # le cadre du miroir
boite(3.6, 0.02, 8.6, 0.04, 1.1, 1.9, "#2f343c")           # le miroir, en verre fumé
boite(3.6, 0.1, 9.2, 0.3, 0, 1.0, ROUGE, morceau=0.5)                 # le dossier du fond
boite(3.6, 0.3, 8.6, 0.8, 0, 0.45, ROUGE, morceau=0.5)                # l'assise du fond
boite(9.0, 0.3, 9.2, 6.9, 0, 1.0, ROUGE, morceau=0.5)                 # le dossier de droite
boite(8.6, 0.3, 9.0, 6.9, 0, 0.45, ROUGE, morceau=0.5)                # l'assise de droite


def table(x0, y0, x1, y1):
    boite(x0, y0, x1, y1, 0.71, 0.75, "#c58a4f")
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    boite(cx - 0.05, cy - 0.05, cx + 0.05, cy + 0.05, 0, 0.71, "#3a3a3a")
    boite(cx - 0.12, cy - 0.04, cx - 0.06, cy + 0.02, 0.75, 0.95, "#c0392b")     # la sauce rouge
    boite(cx - 0.04, cy - 0.04, cx + 0.02, cy + 0.02, 0.75, 0.95, "#efe8d8")     # la sauce blanche
    boite(cx + 0.05, cy - 0.05, cx + 0.15, cy + 0.03, 0.75, 0.87, "#8d9196")     # les serviettes


def chaise(x, y, vers):
    """« vers » : le côté où regarde la personne assise ; le dossier est à l'opposé (comme dans plan_kebab.py)."""
    r = 0.21
    for dx in (-r + 0.02, r - 0.06):
        for dy in (-r + 0.02, r - 0.06):
            boite(x + dx, y + dy, x + dx + 0.04, y + dy + 0.04, 0, 0.43, "#6b4423")
    boite(x - r, y - r, x + r, y + r, 0.43, 0.48, ROUGE)
    dos = {"haut": (x - r, y + r - 0.04, x + r, y + r), "bas": (x - r, y - r, x + r, y - r + 0.04),
           "droite": (x - r, y - r, x - r + 0.04, y + r), "gauche": (x + r - 0.04, y - r, x + r, y + r)}[vers]
    boite(*dos, 0.48, 0.92, "#8a5a2b")


table(7.4, 0.85, 8.6, 1.65)                                # la table de Sky, dans l'angle
chaise(7.7, 1.9, "haut"); chaise(8.3, 1.9, "haut")
for ty in (3.6, 5.9):                                       # les deux tables du milieu
    table(5.1, ty - 0.6, 5.9, ty + 0.6)
    for cy in (ty - 0.3, ty + 0.3):
        chaise(4.85, cy, "droite"); chaise(6.15, cy, "gauche")
for ty in (4.0, 6.2):                                       # les deux tables de la banquette de droite
    table(7.4, ty - 0.4, 8.6, ty + 0.4)
    for cx in (7.7, 8.3):
        chaise(cx, ty - 0.65, "bas"); chaise(cx, ty + 0.65, "haut")

# --- l'escalier en bois, à droite, derrière un mur : on ne le voit pas depuis la salle, il ne s'ouvre que sur le palier,
# devant (l'auteur, le 2026-10-17) ---
BOIS = "#8a5a2b"
# le côté de l'escalier, côté salle : fermé sous les marches, il suit leur pente ; la rampe monte au-dessus de la banquette
# (l'auteur, le 2026-10-17). Au fond, l'escalier touche le plafond : de là, on ne voit qu'un mur.
for k in range(11):                                         # monte du palier (y = 6,4) vers le fond, 25 cm par marche ;
                                                            # la 12e marche, c'est le palier du haut
    y0, y1, dessus = 6.4 - 0.5 * (k + 1), 6.4 - 0.5 * k, 0.25 * (k + 1)
    boite(9.4, y0, 10.9, y1, max(0, dessus - 0.55), dessus, "#9c6b3c")                 # la marche et son limon
    boite(9.3, y0, 9.4, y1, 0, dessus, "#dcc69c", trait=False, groupe="cote-escalier")   # le côté fermé, sous les marches
    boite(9.33, (y0 + y1) / 2 - 0.02, 9.37, (y0 + y1) / 2 + 0.02, dessus, dessus + 0.9, BOIS)  # les barreaux
boite(9.4, 6.4, 10.9, 7.9, 0, 0.03, "#b07a45")              # le palier
for xr, nr in ((9.32, (-1, 0, 0)), (9.38, (1, 0, 0))):     # la main courante, en pente avec l'escalier, jusqu'au poteau du bas
    plaque([(xr, 6.45, 1.1), (xr, 0.4, 3.9), (xr, 0.4, 4.0), (xr, 6.45, 1.2)], nr, BOIS)
boite(9.29, 6.35, 9.41, 6.5, 0, 1.25, BOIS)                 # le poteau du bas, sur la première marche

# --- les arbres de la rue, sur le trottoir d'en face ---
for xa in (-2.0, 2.5, 7.0, 11.5):
    boite(xa - 0.12, 13.0, xa + 0.12, 13.24, 0, 2.6, "#5a4030")
    boite(xa - 1.0, 12.6, xa + 1.0, 13.6, 2.6, 4.6, "#4f7f3c")
# --- les grandes plantes, au sol ---
boite(9.0, 0.05, 9.3, 0.35, 1.0, 1.25, "#9a5b3a")            # la plante de l'angle, au-dessus du coin de la banquette
boite(8.85, 0.02, 9.3, 0.5, 1.25, 1.95, "#3f7a3a")
for px, py in ((2.75, 0.4), (0.75, 7.3), (10.55, 7.55)):
    boite(px - 0.18, py - 0.18, px + 0.18, py + 0.18, 0, 0.4, "#9a5b3a")
    boite(px - 0.3, py - 0.3, px + 0.3, py + 0.3, 0.4, 1.1, "#3f7a3a")


def ombre(couleur, f):
    c = couleur.lstrip("#")
    return tuple(min(255, int(int(c[i:i + 2], 16) * f)) for i in (0, 2, 4))


def faces(forme):
    """Les faces d'une boîte : (coins, normale)."""
    x0, y0, x1, y1, z0, z1 = forme
    return [([(x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)], (0, 0, 1)),
            ([(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0)], (0, 0, -1)),
            ([(x0, y0, z0), (x1, y0, z0), (x1, y0, z1), (x0, y0, z1)], (0, -1, 0)),
            ([(x0, y1, z0), (x1, y1, z0), (x1, y1, z1), (x0, y1, z1)], (0, 1, 0)),
            ([(x0, y0, z0), (x0, y1, z0), (x0, y1, z1), (x0, y0, z1)], (-1, 0, 0)),
            ([(x1, y0, z0), (x1, y1, z0), (x1, y1, z1), (x1, y0, z1)], (1, 0, 0))]


ECLAIRAGE = {(0, 0, 1): 1.0, (0, 0, -1): 0.8, (0, 1, 0): 0.9, (0, -1, 0): 0.8, (1, 0, 0): 0.75, (-1, 0, 0): 0.85}


def vue(numero, sortie):
    """La vue d'un axe : chaque face est remplie avec un tampon de profondeur (ce qui est caché reste caché), puis les
    contours se tracent là où deux faces se touchent à l'écran."""
    import numpy as np
    cx, cy, angle = AXES[numero]
    h, inclinaison, champ = CAMERAS[numero]
    camera = (cx, cy, h)
    a, t = math.radians(angle), math.radians(inclinaison)
    avant = (math.cos(a) * math.cos(t), math.sin(a) * math.cos(t), math.sin(t))   # en coordonnées du plan (y vers la rue)
    # le plan a y vers le bas : la droite de la caméra est (−sin a, cos a, 0), le haut est droite × avant, ramené vers z > 0
    droite = (-math.sin(a), math.cos(a), 0.0)
    haut = (droite[1] * avant[2] - droite[2] * avant[1], droite[2] * avant[0] - droite[0] * avant[2],
            droite[0] * avant[1] - droite[1] * avant[0])
    if haut[2] < 0:
        haut = tuple(-v for v in haut)
    focale = (LARGEUR / 2) / math.tan(math.radians(champ) / 2)

    def vers_camera(p):
        v = (p[0] - camera[0], p[1] - camera[1], p[2] - camera[2])
        return (sum(v[i] * droite[i] for i in range(3)), sum(v[i] * haut[i] for i in range(3)),
                sum(v[i] * avant[i] for i in range(3)))

    def couper(pts):                                        # on coupe ce qui passe derrière la caméra
        coupe = []
        for i, p in enumerate(pts):
            q = pts[(i + 1) % len(pts)]
            if p[2] >= 0.05:
                coupe.append(p)
            if (p[2] >= 0.05) != (q[2] >= 0.05):
                s = (0.05 - p[2]) / (q[2] - p[2])
                coupe.append(tuple(p[k] + s * (q[k] - p[k]) for k in range(3)))
        return coupe

    def ecran(cam):
        return [(LARGEUR / 2 + focale * x / z, HAUTEUR / 2 - focale * y / z) for x, y, z in cam]

    def visible(points, normale):
        c = [sum(p[k] for p in points) / len(points) for k in range(3)]
        return sum(normale[k] * (camera[k] - c[k]) for k in range(3)) > 0

    profondeur = np.full((HAUTEUR, LARGEUR), np.inf)
    image = np.zeros((HAUTEUR, LARGEUR, 3), np.uint8)
    image[:] = ombre("#e8dcc4", 1.0)
    idents = np.full((HAUTEUR, LARGEUR), -1, np.int32)
    cles, verres, sol = {}, [], []

    def remplir(points, normale, couleur, cle):
        if couleur == "verre":
            verres.append(points)
            return
        if not visible(points, normale):
            return
        brut = [vers_camera(p) for p in points]
        cam = couper(brut)
        if len(cam) < 3:
            return
        poly = ecran(cam)
        x0 = max(0, int(math.floor(min(u for u, _ in poly)))); x1 = min(LARGEUR, int(math.ceil(max(u for u, _ in poly))) + 1)
        y0 = max(0, int(math.floor(min(v for _, v in poly)))); y1 = min(HAUTEUR, int(math.ceil(max(v for _, v in poly))) + 1)
        if x0 >= x1 or y0 >= y1:
            return
        masque = Image.new("L", (x1 - x0, y1 - y0), 0)
        ImageDraw.Draw(masque).polygon([(u - x0, v - y0) for u, v in poly], fill=1)
        m = np.asarray(masque, bool)
        if not m.any():
            return
        q0, q1, q2 = (np.array(p, float) for p in brut[:3])
        n = np.cross(q1 - q0, q2 - q0)
        if not n.any():
            return
        uu, vv = np.meshgrid(np.arange(x0, x1) + 0.5, np.arange(y0, y1) + 0.5)
        rx, ry = (uu - LARGEUR / 2) / focale, -(vv - HAUTEUR / 2) / focale
        with np.errstate(divide="ignore", invalid="ignore"):
            z = float(n @ q0) / (n[0] * rx + n[1] * ry + n[2])
        tampon = profondeur[y0:y1, x0:x1]
        ok = m & (z > 0.04) & (z < tampon - 1e-4)
        tampon[ok] = z[ok]
        image[y0:y1, x0:x1][ok] = ombre(couleur, ECLAIRAGE.get(normale, 0.85))
        idents[y0:y1, x0:x1][ok] = cles.setdefault(cle, len(cles))

    for k, (_, (points, normale), couleur, _trait) in enumerate(FOND):
        remplir(points, normale, couleur, ("plaque", k))
        if normale == (0, 0, 1) and points[0][:2] == (0, 0):
            sol.append(cles.get(("plaque", k)))
    for k, (_, forme, couleur, trait, groupe) in enumerate(OBJETS):
        for f, (points, normale) in enumerate(faces(forme)):
            remplir(points, normale, couleur, ("boite", k, f) if trait else ("groupe", groupe, normale))

    # les carreaux du sol, tous les 50 cm, retrouvés depuis la profondeur
    if sol and sol[0] is not None:
        ys, xs = np.nonzero(idents == sol[0])
        z = profondeur[ys, xs]
        rx, ry = (xs + 0.5 - LARGEUR / 2) / focale, -(ys + 0.5 - HAUTEUR / 2) / focale
        wx = camera[0] + z * (rx * droite[0] + ry * haut[0] + avant[0])
        wy = camera[1] + z * (rx * droite[1] + ry * haut[1] + avant[1])
        seuil = 0.9 * z / focale
        ligne = (np.abs(wx / 0.5 - np.round(wx / 0.5)) * 0.5 < seuil) | (np.abs(wy / 0.5 - np.round(wy / 0.5)) * 0.5 < seuil)
        image[ys[ligne], xs[ligne]] = ombre("#c9a27a", 0.8)
    # les contours, là où deux faces se touchent
    bord = np.zeros((HAUTEUR, LARGEUR), bool)
    bord[:, :-1] |= idents[:, :-1] != idents[:, 1:]
    bord[:-1, :] |= idents[:-1, :] != idents[1:, :]
    image[bord] = (image[bord] * 0.45).astype(np.uint8)
    img = Image.fromarray(image)
    d = ImageDraw.Draw(img)
    for points in verres:                                   # le verre : son contour seulement, on voit à travers
        cam = couper([vers_camera(p) for p in points])
        if len(cam) >= 3:
            poly = ecran(cam)
            d.line(poly + [poly[0]], fill=(110, 170, 195), width=3)
    img.save(sortie)


if __name__ == "__main__":
    vue(int(sys.argv[2]), sys.argv[1])
