"""Lance le test standard d'un LoRA de perso (image/test-standard.md) dans ComfyUI, puis assemble une planche.

  ~/venvs/kebab/bin/python pipeline/test_lora.py sky sky_v1.safetensors

Le LoRA doit être dans <modeles_root>/loras/. ComfyUI doit tourner (pipeline/comfyui.py demarrer).
Sortie : <sorties_root>/comfyui/test-standard_<lora>_NN_.png et la planche test-standard_<lora>_planche.png.
"""
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

import yaml
from PIL import Image, ImageDraw

RACINE = Path(__file__).resolve().parent.parent
CONFIG = yaml.safe_load((RACINE / "config.yaml").read_text())
URL = CONFIG["comfyui_url"]
NEGATIF = ("lowres, bad anatomy, bad hands, text, error, missing finger, extra digits, fewer digits, cropped, "
           "worst quality, low quality, low score, bad score, average score, signature, watermark, username, blurry")
QUALITE = "masterpiece, high score, great score, absurdres"


def prompts_du_test(fiche):
    """Les 10 prompts, lus dans le tableau de image/test-standard.md (la seule source)."""
    texte = (RACINE / "image" / "test-standard.md").read_text()
    lignes = re.findall(r"^\| (\d+) \| [^|]+ \| (.+) \|$", texte, re.M)
    prompts = {}
    for numero, tags in lignes:
        bloc = re.findall(r"`([^`]+)`", tags)
        signature = fiche["lora"]["legendes_signatures"][fiche["lora"]["test_signature"]]
        prompts[int(numero)] = bloc[-1] if numero != "9" else f"{bloc[-1]}, {signature}"
    assert sorted(prompts) == list(range(1, 11)), prompts.keys()
    return prompts


def workflow(positif, lora, graine, largeur, hauteur, prefixe):
    return {
        "1": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": "animagine-xl-4.0.safetensors"}},
        # Le LoRA en mode « bypass » : il s'ajoute pendant le calcul sans réécrire les poids du modèle. Le chargement
        # classique garde une copie des poids d'origine sur la carte et déborde des 8 Go (journal.md, 2026-10-15).
        "2": {"class_type": "LoraLoaderBypassModelOnly", "inputs": {"model": ["1", 0], "lora_name": lora,
                                                                     "strength_model": 1.0}},
        "3": {"class_type": "CLIPTextEncode", "inputs": {"text": positif, "clip": ["1", 1]}},
        "4": {"class_type": "CLIPTextEncode", "inputs": {"text": NEGATIF, "clip": ["1", 1]}},
        "5": {"class_type": "EmptyLatentImage", "inputs": {"width": largeur, "height": hauteur, "batch_size": 1}},
        "6": {"class_type": "KSampler", "inputs": {"seed": graine, "steps": 25, "cfg": 5.0, "sampler_name": "euler_ancestral",
                                                   "scheduler": "normal", "denoise": 1.0, "model": ["2", 0],
                                                   "positive": ["3", 0], "negative": ["4", 0], "latent_image": ["5", 0]}},
        "7": {"class_type": "VAEDecode", "inputs": {"samples": ["6", 0], "vae": ["1", 2]}},
        "8": {"class_type": "SaveImage", "inputs": {"filename_prefix": prefixe, "images": ["7", 0]}},
    }


def generer(wf):
    requete = urllib.request.Request(f"{URL}/prompt", data=json.dumps({"prompt": wf}).encode(),
                                     headers={"Content-Type": "application/json"})
    prompt_id = json.load(urllib.request.urlopen(requete))["prompt_id"]
    while True:
        historique = json.load(urllib.request.urlopen(f"{URL}/history/{prompt_id}"))
        if prompt_id in historique:
            entree = historique[prompt_id]
            if entree["status"].get("status_str") != "success":
                sys.exit(json.dumps(entree["status"].get("messages"), ensure_ascii=False)[:2000])
            return [i["filename"] for s in entree["outputs"].values() for i in s.get("images", [])]
        time.sleep(2)


def main():
    slug, lora = sys.argv[1], sys.argv[2]
    fiche = json.loads((RACINE / "image" / "persos" / slug / "fiche.json").read_text())
    genre = "1girl" if fiche.get("genre") == "f" else "1boy"
    debut = f"{fiche['lora']['declencheur']}, {genre}, solo, {'male' if genre == '1boy' else 'female'} focus"
    if fiche["lora"].get("tag_yeux"):
        debut += ", " + fiche["lora"]["tag_yeux"]
    nom = lora.removesuffix(".safetensors")
    sorties = Path(CONFIG["sorties_root"]) / "comfyui"
    images = []
    for numero, tags in prompts_du_test(fiche).items():
        largeur, hauteur = (832, 1216) if numero == 5 else (1024, 1024)
        t = time.time()
        fichiers = generer(workflow(f"{debut}, {tags}, {QUALITE}", lora, 1000 + numero, largeur, hauteur,
                                    f"test-standard_{nom}_{numero:02d}"))
        images.append(sorties / fichiers[0])
        print(f"{numero:2d}/10  {time.time() - t:5.0f} s  {fichiers[0]}", flush=True)
    vignettes = [Image.open(i).convert("RGB") for i in images]
    vignettes = [v.resize((round(v.width * 400 / v.height), 400)) for v in vignettes]
    planche = Image.new("RGB", (5 * 410, 2 * 430), "white")
    dessin = ImageDraw.Draw(planche)
    for k, v in enumerate(vignettes):
        x, y = (k % 5) * 410, (k // 5) * 430
        planche.paste(v, (x + (400 - v.width) // 2, y + 25))
        dessin.text((x + 5, y + 5), str(k + 1), fill="black")
    chemin = sorties / f"test-standard_{nom}_planche.png"
    planche.save(chemin)
    print("planche :", chemin)


if __name__ == "__main__":
    main()
