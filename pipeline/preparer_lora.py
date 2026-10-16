"""Prépare le jeu d'entraînement du LoRA d'un perso : ses images retenues, agrandies, chacune avec sa légende.

Les images viennent de provenance.json (les versions retenues), les légendes de leur nom de fichier : l'angle,
l'expression, le cadrage. Les traits fixes du perso ne sont jamais écrits : le mot déclencheur (fiche.json > lora)
les absorbe. Les petites images (les cases des planches, environ 510 pixels) sont agrandies avec Real-ESRGAN anime,
puis ramenées à environ un mégapixel, la taille de travail du modèle.

  ~/venvs/kebab/bin/python pipeline/preparer_lora.py sky v1

Sortie : <sorties_root>/lora/<perso>/jeu_<version>/ (images PNG et légendes .txt du même nom).
"""
import json
import math
import sys
from pathlib import Path

import numpy as np
import spandrel
import torch
import yaml
from PIL import Image

RACINE = Path(__file__).resolve().parent.parent
CONFIG = yaml.safe_load((RACINE / "config.yaml").read_text())
AGRANDISSEUR = Path(CONFIG["modeles_root"]) / "upscale_models" / "RealESRGAN_x4plus_anime_6B.pth"
AIRE = 1024 * 1024

# La palette commune (image/emotions.md), en tags Danbooru
EMOTIONS = {
    "neutre": "expressionless, closed mouth",
    "joie": "smile, happy, open mouth, teeth",
    "tristesse": "sad, frown",
    "colere": "angry, frown, closed mouth",
    "peur": "scared, worried, open mouth",
    "surprise": "surprised, open mouth, raised eyebrows",
    "degout": "disgust, wrinkled nose",
    "mepris": "smirk, contempt, looking down",
    "rire": "laughing, open mouth, closed eyes",
    "pleurs": "crying, tears, sad",
    "rage": "furious, angry, anger vein, clenched teeth, shouting",
    "terreur": "terrified, constricted pupils, open mouth, pale skin, sweat",
    "stupeur": "shocked, open mouth, wide-eyed, constricted pupils",
    "interet": "curious, head tilt",
    "concentration": "serious, looking down, focused",
    "confusion": "confused, raised eyebrow, head tilt",
    "doute": "skeptical, raised eyebrow, looking to the side",
    "mefiance": "suspicious, narrowed eyes, side glance",
    "gene": "embarrassed, blush, hand on own neck, nervous smile",
    "honte": "ashamed, looking down, head down",
    "fierte": "proud, smirk, chin up",
    "jalousie": "jealous, side glance, frown",
    "tendresse": "gentle smile, half-closed eyes",
    "desir": "drooling, hungry, looking down, food",
    "contentement": "closed eyes, smile, relaxed",
    "soulagement": "relieved, sigh, closed eyes, sweatdrop, head back",
    "exaltation": "excited, grin, open mouth",
    "triomphe": "grin, open mouth, clenched hand, raised fist",
    "emerveillement": "looking up, awe, parted lips",
    "deception": "disappointed, pout, looking down",
    "inquietude": "worried, frown",
    "agacement": "annoyed, rolling eyes",
    "malice": "mischievous, smirk, grin, raised eyebrow",
    "ennui": "bored, head rest, hand on own cheek, half-closed eyes",
    "fatigue": "tired, yawning, hand over mouth, closed eyes",
    "douleur": "pain, closed eyes, clenched teeth",
    "clignement": "closed eyes, expressionless",
    "clignement-mi-clos": "half-closed eyes, expressionless",
}
BOUCHES = {
    "fermee": "closed mouth, expressionless",
    "mi-ouverte": "parted lips, talking",
    "ouverte": "open mouth, talking",
    "sourire-ferme": "evil smile, closed mouth, shaded face, constricted pupils",
    "sourire-grimace": "evil grin, clenched teeth, sharp teeth, fangs, shaded face, constricted pupils",
    "sourire-rire": "evil laugh, open mouth, sharp teeth, fangs, shaded face, constricted pupils",
}
VUES = {
    "face": "upper body, facing viewer",
    "trois-quarts-gauche": "upper body, three-quarter view, facing left",
    "trois-quarts-droit": "upper body, three-quarter view, facing right",
    "profil-gauche": "upper body, profile, from side, facing left",
    "profil-droit": "upper body, profile, from side, facing right",
    "dos": "upper body, from behind",
    "pied": "full body, standing",
    "pied-face": "full body, standing, facing viewer",
    "pied-trois-quarts-gauche": "full body, standing, three-quarter view, facing left",
    "pied-trois-quarts-droit": "full body, standing, three-quarter view, facing right",
    "pied-profil-gauche": "full body, standing, profile, from side, facing left",
    "pied-profil-droit": "full body, standing, profile, from side, facing right",
    "pied-dos": "full body, standing, from behind",
    "assis-face": "full body, sitting, chair, facing viewer",
    "assis-cote": "full body, sitting, chair, from side, facing right",
    "accoude": "full body, standing, leaning, elbow rest",
}
# Les gestes en plan moyen (gestes/), d'après fiche.json > accessoires ; ceux de Sky pour l'instant
GESTES = {
    "mange": "eating, biting, holding food with both hands, wrap",
    "boit": "drinking, holding bottle, soda bottle",
    "bouche-pleine": "chewing, mouth full, puffy cheeks, unimpressed",
    "telephone": "holding phone, looking at phone, smartphone",
    "ecrit-marqueur": "writing, holding marker, raised hand, glass",
    "laptop": "using laptop, typing, laptop, table",
}
# Le tag des yeux (fiche.json > lora > tag_yeux) ne va que là où les deux yeux sont ouverts et visibles
SANS_YEUX = {"dos", "pied-dos", "profil-gauche", "profil-droit", "pied-profil-gauche", "pied-profil-droit", "assis-cote",
             "rire", "contentement", "soulagement", "fatigue", "douleur", "clignement", "clignement-mi-clos"}
FOND = "simple background, grey background"


def legende(chemin, fiche):
    """La légende d'une image, tirée de son chemin dans le dossier du perso."""
    dossier, nom = chemin.split("/")
    base = nom.rsplit("_v", 1)[0]
    tq = base.startswith("trois-quarts_")
    cle = base.removeprefix("trois-quarts_")
    angle = "three-quarter view, facing right" if tq else "facing viewer"
    yeux = fiche["lora"].get("tag_yeux")
    yeux = f"{yeux}, " if yeux and cle not in SANS_YEUX else ""
    if dossier == "references":
        if base.startswith("master"):
            return yeux + fiche["lora"]["legende_maitre"]
        return f"{VUES[base]}, {yeux}{FOND}"
    if dossier == "bouches":
        cle = base.split("_", 1)[1]
        return f"portrait, close-up, {angle}, {yeux}{BOUCHES[cle]}, {FOND}"
    if dossier == "gestes":
        return f"upper body, {angle}, {yeux}{GESTES[cle]}, {FOND}"
    tags = EMOTIONS.get(cle) or fiche["lora"]["legendes_signatures"][cle]
    cadrage = "upper body" if cle != "haussement-epaules" else "upper body, cowboy shot"
    return f"{cadrage}, {angle}, {yeux}{tags}, {FOND}"


def images_retenues(perso):
    prov = json.loads((perso / "provenance.json").read_text())
    fichiers = []
    for cle in ("palette_retenue", "palette_retenue_trois_quarts", "signatures_retenues", "bouches_retenues", "gestes_retenus"):
        fichiers += prov.get(cle, {}).values()
    for chemin, info in prov["images"].items():
        if chemin.startswith("references/") and info.get("retenue"):
            fichiers.append(chemin)
    return sorted(set(fichiers))


def charger_agrandisseur():
    modele = spandrel.ModelLoader().load_from_file(str(AGRANDISSEUR)).eval()
    appareil = "cuda" if torch.cuda.is_available() else "cpu"
    return modele.to(appareil).half() if appareil == "cuda" else modele, appareil


@torch.no_grad()
def agrandir(image, modele, appareil, tuile=192, marge=16):
    """Agrandit ×4 par tuiles : en un seul bloc, une convolution demande plus de 4 Go sur la carte de 8 Go."""
    x = torch.from_numpy(np.asarray(image.convert("RGB"), dtype=np.float32) / 255).permute(2, 0, 1)[None]
    _, _, h, w = x.shape
    sortie = torch.zeros(1, 3, h * 4, w * 4)
    for y0 in range(0, h, tuile):
        for x0 in range(0, w, tuile):
            ya, yb = max(y0 - marge, 0), min(y0 + tuile + marge, h)
            xa, xb = max(x0 - marge, 0), min(x0 + tuile + marge, w)
            bloc = x[:, :, ya:yb, xa:xb].to(appareil)
            bloc = modele(bloc.half() if appareil == "cuda" else bloc).float().cpu()
            hy, hx = (y0 - ya) * 4, (x0 - xa) * 4
            ty, tx = min(tuile, h - y0) * 4, min(tuile, w - x0) * 4
            sortie[:, :, y0 * 4:y0 * 4 + ty, x0 * 4:x0 * 4 + tx] = bloc[:, :, hy:hy + ty, hx:hx + tx]
    y = sortie.clamp(0, 1)[0].permute(1, 2, 0).numpy()
    return Image.fromarray((y * 255).round().astype(np.uint8))


def main():
    slug = sys.argv[1]
    version = sys.argv[2] if len(sys.argv) > 2 else "v1"
    perso = RACINE / "image" / "persos" / slug
    fiche = json.loads((perso / "fiche.json").read_text())
    declencheur = fiche["lora"]["declencheur"]
    sortie = Path(CONFIG["sorties_root"]) / "lora" / slug / f"jeu_{version}"
    if sortie.exists() and any(sortie.iterdir()):
        sys.exit(f"{sortie} existe déjà : on n'écrase pas un jeu d'entraînement, prends une autre version")
    sortie.mkdir(parents=True, exist_ok=True)
    modele, appareil = charger_agrandisseur()
    fichiers = images_retenues(perso)
    for i, chemin in enumerate(fichiers, 1):
        image = Image.open(perso / chemin).convert("RGB")
        w, h = image.size
        if w * h < 0.9 * AIRE:
            image = agrandir(image, modele, appareil)
            k = math.sqrt(AIRE / (w * h))
            image = image.resize((round(w * k / 8) * 8, round(h * k / 8) * 8), Image.LANCZOS)
        nom = chemin.replace("/", "__").removesuffix(".png")
        image.save(sortie / f"{nom}.png")
        texte = f"{declencheur}, 1boy, solo, male focus, {legende(chemin, fiche)}"
        (sortie / f"{nom}.txt").write_text(texte + "\n")
        print(f"{i:3d}/{len(fichiers)}  {image.size[0]}x{image.size[1]}  {nom}")
    print(f"jeu prêt : {sortie} ({len(fichiers)} images)")


if __name__ == "__main__":
    main()
