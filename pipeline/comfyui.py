"""Démarre, arrête ou montre ComfyUI sur sky-master, avec les réglages qui marchent sur la carte AMD.

ComfyUI tourne comme un service de l'utilisateur, dans son propre groupe mémoire : s'il déborde, c'est
lui que le système arrête, pas VS Code. Les réglages viennent du journal (2026-10-15).

  ~/venvs/kebab/bin/python pipeline/comfyui.py demarrer
  ~/venvs/kebab/bin/python pipeline/comfyui.py arreter
  ~/venvs/kebab/bin/python pipeline/comfyui.py etat
"""
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

import yaml

RACINE = Path(__file__).resolve().parent.parent
CONFIG = yaml.safe_load((RACINE / "config.yaml").read_text())
SERVICE = "comfyui"

# Les options testées sur la RX 5700 XT (journal.md, 2026-10-15)
OPTIONS = [
    "--disable-dynamic-vram",   # la « dynamic VRAM » échoue sur cette carte (VBAR allocation failed) ; pour la même
                                # raison, jamais PYTORCH_CUDA_ALLOC_CONF=expandable_segments : toute allocation échoue
    "--disable-pinned-memory",  # la mémoire épinglée pose problème sur gfx1010
    "--highvram",               # garde le modèle sur la carte : sinon il se recopie en RAM à chaque image
    "--cpu-vae",                # le VAE sur le processeur : sur la carte, il ne tient plus à côté du modèle
    "--fp8_e4m3fn-text-enc",    # les encodeurs de texte en fp8 : sinon un LoRA ne tient plus sur les 8 Go
]


def demarrer():
    if etat(silencieux=True):
        print("ComfyUI tourne déjà :", CONFIG["comfyui_url"])
        return
    dossier = Path(CONFIG["comfyui_dir"])
    sorties = Path(CONFIG["sorties_root"]) / "comfyui"
    sorties.mkdir(parents=True, exist_ok=True)
    journal = sorties / "comfyui.log"
    python = Path(CONFIG["python_venv"]) / "bin" / "python"
    subprocess.run(["systemctl", "--user", "reset-failed", SERVICE], stderr=subprocess.DEVNULL)
    subprocess.run([
        "systemd-run", "--user", f"--unit={SERVICE}",
        "-p", "MemoryMax=10G", "-p", "MemorySwapMax=3G",
        "-p", f"StandardOutput=append:{journal}", "-p", f"StandardError=append:{journal}",
        "--setenv=MIOPEN_FIND_MODE=TRUST_VERIFY_FULL",
        f"--working-directory={dossier}",
        str(python), "main.py", "--listen", "127.0.0.1", "--port", "8188", *OPTIONS,
        "--extra-model-paths-config", str(dossier / "extra_model_paths.yaml"),
        "--output-directory", str(sorties),
    ], check=True)
    for _ in range(120):
        if etat(silencieux=True):
            print("ComfyUI est prêt :", CONFIG["comfyui_url"])
            return
        time.sleep(1)
    sys.exit(f"ComfyUI ne répond pas : voir {journal}")


def arreter():
    subprocess.run(["systemctl", "--user", "stop", SERVICE])
    print("ComfyUI arrêté")


def etat(silencieux=False):
    try:
        urllib.request.urlopen(CONFIG["comfyui_url"] + "/system_stats", timeout=2)
        actif = True
    except OSError:
        actif = False
    if not silencieux:
        print("ComfyUI :", "en marche" if actif else "arrêté")
    return actif


if __name__ == "__main__":
    {"demarrer": demarrer, "arreter": arreter, "etat": etat}[sys.argv[1]]()
