"""Le garde-fou de la mémoire vive, lancé avec ComfyUI (pipeline/comfyui.py) : si la RAM disponible du système passe sous
un seuil, il tue ComfyUI avant que la machine ne gèle. Le 2026-10-20, sky-master a gelé en pleine génération et l'auteur a
dû le redémarrer de force (journal.md). Le plafond du service (MemoryMax) ne suffit pas : il ne compte ni la RAM des autres
programmes (VS Code, Firefox), ni celle que le pilote de la carte prend sur la RAM.

Il note la RAM disponible toutes les 10 secondes dans <sorties_root>/comfyui/garde.log : de quoi savoir, après coup,
ce qui a mangé la mémoire.
"""
import subprocess
import time
from datetime import datetime
from pathlib import Path

import yaml

RACINE = Path(__file__).resolve().parent.parent
CONFIG = yaml.safe_load((RACINE / "config.yaml").read_text())
JOURNAL = Path(CONFIG["sorties_root"]) / "comfyui" / "garde.log"
SEUIL_MO = 1200


def memoire_mo():
    valeurs = {}
    for ligne in open("/proc/meminfo"):
        cle, valeur = ligne.split(":", 1)
        valeurs[cle] = int(valeur.split()[0]) // 1024
    return valeurs["MemAvailable"], valeurs["SwapTotal"] - valeurs["SwapFree"]


def noter(texte):
    with open(JOURNAL, "a") as f:
        f.write(f"{datetime.now():%Y-%m-%d %H:%M:%S} {texte}\n")


def main():
    noter(f"garde lancé, seuil {SEUIL_MO} Mo")
    dernier = 0
    while True:
        dispo, swap = memoire_mo()
        if dispo < SEUIL_MO:
            noter(f"RAM disponible {dispo} Mo, swap utilisé {swap} Mo : ComfyUI tué")
            subprocess.run(["systemctl", "--user", "kill", "--signal=SIGKILL", "comfyui.service"])
            return
        if time.time() - dernier >= 10:
            noter(f"RAM disponible {dispo} Mo, swap utilisé {swap} Mo")
            dernier = time.time()
        time.sleep(0.5)


if __name__ == "__main__":
    main()
