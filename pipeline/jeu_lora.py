"""Construit le jeu d'entraînement d'une nouvelle version d'un LoRA à partir d'un jeu déjà agrandi (pipeline/preparer_lora.py),
sans refaire l'agrandissement. D'après les recherches du 2026-10-21 (journal.md) :

1. les légendes : le genre puis le mot déclencheur en tête (l'ordre d'Animagine XL 4.0 : « 1boy, nom du perso, … »), puis
   ses traits fixes (fiche.json > lora > traits) là où ils se voient. Jamais écrits jusqu'à la v2, ils étaient absorbés par
   le déclencheur : « stubble » dans un prompt ne commandait rien ;
2. un masque alpha par image : le perso détouré par ToonOut (pipeline/essai_integration.py, detourer_toonout), dilaté de
   12 pixels (le masque agit à 1/8, la taille des latents), le fond gris à 15 % : l'entraînement regarde le perso, à peine
   le fond (« masked loss », `alpha_mask = true` dans sd-scripts) ;
3. les images à petite tête (en pied, assis, accoudé, gestes) reprises de leur fichier d'origine et agrandies sans
   Real-ESRGAN, qui y amincissait la barbe en traits durs ;
4. trois sous-dossiers, répétés différemment (en pied × 3, gestes × 2, bustes × 1) : 104 bustes contre 22 petites têtes.

  ~/venvs/kebab/bin/python pipeline/jeu_lora.py sky v3 --depuis jeu_v2 --masques masques_toonout

Sortie : <sorties_root>/lora/<perso>/jeu_<version>/{buste,taille,pied}/ (PNG avec alpha et légendes .txt) et
repetitions.json.
"""
import argparse
import json
import math
from pathlib import Path

import numpy as np
import yaml
from PIL import Image, ImageFilter

import preparer_lora as P

RACINE = Path(__file__).resolve().parent.parent
CONFIG = yaml.safe_load((RACINE / "config.yaml").read_text())
# les petites têtes répétées plus, mais pas trop : à × 4, chaque image en pied revenait 48 fois en 12 époques (risque de figer
# ces poses, la relecture du 2026-10-21) ; le masque n'étant pas normalisé par sa surface, une image en pied compte déjà moins
REPETITIONS = {"buste": 1, "taille": 2, "pied": 3}
FOND_ALPHA = 38                         # le fond gris compte à 15 % (sans rien, des corps en trop apparaissent : OneTrainer)
DILATATION = 12
DOS = {"dos", "pied-dos"}               # des vues sans visage : pas de traits du visage dans leur légende


def groupe(chemin):
    dossier, nom = chemin.split("/")
    base = nom.rsplit("_v", 1)[0]
    if dossier == "gestes":
        return "taille"
    if dossier == "references" and base.split("-")[0] in ("pied", "assis", "accoude"):
        return "pied"
    return "buste"


def legende_v3(chemin, fiche):
    lora = fiche["lora"]
    base = chemin.split("/")[1].rsplit("_v", 1)[0]
    genre = "1girl" if fiche.get("genre") == "f" else "1boy"
    focus = "female focus" if genre == "1girl" else "male focus"
    traits = list(lora["traits"].get("partout", []))
    if base not in DOS:
        traits += lora["traits"].get("visage", [])
    return ", ".join([genre, lora["declencheur"], "solo", focus, *traits, *P.tags_en_plus(chemin, fiche), P.legende(chemin, fiche)])


def taille_cible(w, h):
    """La taille du jeu agrandi (preparer_lora.py) : environ un mégapixel, des côtés multiples de 8."""
    if w * h >= 0.9 * P.AIRE:
        return w, h
    k = math.sqrt(P.AIRE / (w * h))
    return round(w * k / 8) * 8, round(h * k / 8) * 8


def alpha(masque, taille):
    m = masque.convert("L").resize(taille, Image.LANCZOS).point(lambda v: 255 if v > 128 else 0)
    m = m.filter(ImageFilter.MaxFilter(2 * DILATATION + 1)).filter(ImageFilter.GaussianBlur(2))
    a = np.asarray(m, np.float32) / 255
    return Image.fromarray((FOND_ALPHA + (255 - FOND_ALPHA) * a).astype(np.uint8))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("perso")
    ap.add_argument("version")
    ap.add_argument("--depuis", required=True, help="le jeu déjà agrandi, dans <sorties_root>/lora/<perso>/")
    ap.add_argument("--masques", required=True, help="les masques ToonOut de ce jeu, même dossier")
    a = ap.parse_args()
    perso = RACINE / "image" / "persos" / a.perso
    fiche = json.loads((perso / "fiche.json").read_text())
    racine = Path(CONFIG["sorties_root"]) / "lora" / a.perso
    sortie = racine / f"jeu_{a.version}"
    if sortie.exists() and any(sortie.iterdir()):
        raise SystemExit(f"{sortie} existe déjà : on n'écrase pas un jeu d'entraînement")
    for g in REPETITIONS:
        (sortie / g).mkdir(parents=True, exist_ok=True)
    compte = {g: 0 for g in REPETITIONS}
    for chemin in P.images_retenues(perso):
        nom = chemin.replace("/", "__").removesuffix(".png")
        g = groupe(chemin)
        if g == "buste":
            image = Image.open(racine / a.depuis / f"{nom}.png").convert("RGB")
        else:
            # le fichier d'origine, agrandi en Lanczos à la taille du jeu (la même que celle de l'image Real-ESRGAN)
            origine = Image.open(perso / chemin).convert("RGB")
            image = origine.resize(taille_cible(*origine.size), Image.LANCZOS)
            # un léger renforcement des contours : en Lanczos seul, les traits sortaient plus mous que ceux des bustes
            # (Real-ESRGAN), et le LoRA aurait pu lier les plans moyens au flou (la relecture du 2026-10-21)
            image = image.filter(ImageFilter.UnsharpMask(radius=1.6, percent=70, threshold=2))
        masque = Image.open(racine / a.masques / f"{nom}.png")
        rgba = image.copy()
        rgba.putalpha(alpha(masque, image.size))
        rgba.save(sortie / g / f"{nom}.png")
        (sortie / g / f"{nom}.txt").write_text(legende_v3(chemin, fiche) + "\n")
        compte[g] += 1
    (sortie / "repetitions.json").write_text(json.dumps(REPETITIONS) + "\n")
    pas = sum(compte[g] * REPETITIONS[g] for g in compte)
    print(f"jeu prêt : {sortie} ; {compte} ; {pas} images par époque")


if __name__ == "__main__":
    main()
