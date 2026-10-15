"""Découpe une planche ChatGPT en fichiers séparés.

La planche est une grille de cases séparées par de fines lignes blanches ou noires. Le script
trouve ces lignes tout seul, puis range chaque case sous son nom, de gauche à droite
puis de haut en bas, dans le dossier du perso. Il n'écrase jamais un fichier existant.

Exemples, depuis la racine du repo :
  python3 pipeline/decouper_planche.py image/persos/maelle/planches/trois-quarts_emotions-1_v1.png --emotions 1
  python3 pipeline/decouper_planche.py image/persos/maelle/planches/rotation_v1.png \\
      --noms face,trois-quarts-gauche,trois-quarts-droit,profil-gauche,profil-droit,dos --dossier references
"""
import argparse
import re
import sys
from pathlib import Path

from PIL import Image

RACINE = Path(__file__).resolve().parent.parent


def gouttieres(im, axe, noires=False):
    """Les bandes de pixels presque blancs qui traversent toute l'image.

    Avec noires=True, les fines lignes presque noires à la place : un col roulé noir
    traverse aussi l'image, mais en bande épaisse, donc on ne garde que les traits fins.
    """
    W, H = im.size
    n, m = (W, H) if axe == "x" else (H, W)
    px = im.load()
    pas = range(0, m, 4)

    def separe(i, k):
        p = px[i, k] if axe == "x" else px[k, i]
        return max(p) < 80 if noires else min(p) > 235

    plein = [sum(separe(i, k) for k in pas) / len(pas) > 0.9 for i in range(n)]
    bandes, i = [], 0
    while i < n:
        if plein[i]:
            j = i
            while j < n and plein[j]:
                j += 1
            bandes.append((i, j))
            i = j
        else:
            i += 1
    if noires:
        bandes = [(a, b) for a, b in bandes if b - a <= 8]
    return bandes


def cases(n, bandes, mini=50):
    bords = [0] + [b for bande in bandes for b in bande] + [n]
    return [(a, b) for a, b in zip(bords[::2], bords[1::2]) if b - a > mini]


def noms_emotions(numero):
    texte = (RACINE / "image" / "emotions.md").read_text()
    bloc = texte.split(f"### Planche {numero} ")[1].split("\n### ")[0]
    return re.findall(r"^\| \d \| [^|]+ \| `([a-z-]+)` \|", bloc, re.M)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("planche", help="la planche, rangée dans image/persos/<slug>/planches/")
    noms = ap.add_mutually_exclusive_group(required=True)
    noms.add_argument("--emotions", type=int, help="le numéro de la planche dans image/emotions.md")
    noms.add_argument("--noms", help="les noms des cases, séparés par des virgules")
    ap.add_argument("--dossier", default="expressions", help="où ranger les cases dans le dossier du perso")
    a = ap.parse_args()

    planche = Path(a.planche)
    perso = planche.parent.parent
    prefixe = "trois-quarts_" if planche.name.startswith("trois-quarts_") else ""
    version = re.search(r"_v(\d+)\.png$", planche.name)
    version = version.group(1) if version else "1"
    liste = noms_emotions(a.emotions) if a.emotions else a.noms.split(",")

    im = Image.open(planche).convert("RGB")
    W, H = im.size

    def grille(noires):
        return [(x0, y0, x1, y1)
                for (y0, y1) in cases(H, gouttieres(im, "y", noires))
                for (x0, x1) in cases(W, gouttieres(im, "x", noires))]

    boites = grille(noires=False)
    if len(boites) != len(liste):
        # ChatGPT sépare parfois les cases par un trait noir au lieu d'un blanc
        boites = grille(noires=True)
    if len(boites) != len(liste):
        sys.exit(f"{len(boites)} cases trouvées pour {len(liste)} noms : rien n'est écrit")

    sortie = perso / a.dossier
    fichiers = [sortie / f"{prefixe}{nom}_v{version}.png" for nom in liste]
    deja = [str(f) for f in fichiers if f.exists()]
    if deja:
        sys.exit("déjà là, on n'écrase jamais une référence : " + ", ".join(deja))
    sortie.mkdir(exist_ok=True)
    for f, b in zip(fichiers, boites):
        case = im.crop(b)
        case.save(f)
        print(f"{f}  {case.size[0]}x{case.size[1]}")


if __name__ == "__main__":
    main()
