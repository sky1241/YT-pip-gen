"""Fusionne le patch d'inpainting de Fooocus (inpaint_v26.fooocus.patch) dans une copie du checkpoint Animagine XL 4.0.

Pourquoi : appliqué au chargement (nœud « Apply Fooocus Inpaint »), le patch touche 960 poids de l'UNet ; avec --highvram,
ComfyUI garde sur la carte une copie de chaque poids d'origine, et les 8 Go débordent (la même raison que le mode « bypass »
des LoRA, journal.md, 2026-10-15). Fusionné une fois pour toutes, le modèle se charge comme un checkpoint ordinaire ; au
moment de générer, il ne reste que la « tête » d'inpainting à brancher (le nœud, avec un patch vide).

Le fichier est écrit morceau par morceau (le format safetensors : un en-tête JSON, puis les tenseurs à la suite) : jamais
plus d'un tenseur en mémoire, plus le patch (1,3 Go).

  ~/venvs/kebab/bin/python pipeline/fusionner_inpaint.py
"""
import json
import struct
from pathlib import Path

import numpy as np
import torch
import yaml

RACINE = Path(__file__).resolve().parent.parent
CONFIG = yaml.safe_load((RACINE / "config.yaml").read_text())
MODELES = Path(CONFIG["modeles_root"])
SOURCE = MODELES / "checkpoints" / "animagine-xl-4.0.safetensors"
PATCH = MODELES / "inpaint" / "inpaint_v26.fooocus.patch"
SORTIE = MODELES / "checkpoints" / "animagine-xl-4.0-inpaint-fooocus.safetensors"
VIDE = MODELES / "inpaint" / "patch-vide.pth"     # pour le nœud : la tête seule, les poids sont déjà fusionnés
DTYPES = {"F16": (torch.float16, np.float16), "F32": (torch.float32, np.float32), "BF16": (torch.bfloat16, None)}


def main():
    patch = torch.load(PATCH, map_location="cpu", weights_only=True)
    with open(SOURCE, "rb") as f:
        taille_entete = struct.unpack("<Q", f.read(8))[0]
        entete = json.loads(f.read(taille_entete))
    debut_source = 8 + taille_entete
    meta = dict(entete.get("__metadata__", {}))
    meta["kebab"] = ("Animagine XL 4.0 + patch d'inpainting Fooocus v2.6 fusionné (pipeline/fusionner_inpaint.py) ; "
                     "s'utilise avec la tête d'inpainting de Fooocus")
    entete["__metadata__"] = meta
    brut = json.dumps(entete, separators=(",", ":")).encode()
    brut += b" " * (-len(brut) % 8)                  # l'en-tête aligné sur 8 octets
    tenseurs = sorted((k for k in entete if k != "__metadata__"), key=lambda k: entete[k]["data_offsets"][0])
    fusionnes = 0
    with open(SOURCE, "rb") as src, open(SORTIE.with_suffix(".part"), "wb") as out:
        out.write(struct.pack("<Q", len(brut)))
        out.write(brut)
        for nom in tenseurs:
            info = entete[nom]
            a, b = info["data_offsets"]
            src.seek(debut_source + a)
            octets = src.read(b - a)
            cle = nom.removeprefix("model.")
            if nom.startswith("model.diffusion_model.") and cle in patch:
                dtype_torch, dtype_np = DTYPES[info["dtype"]]
                poids = torch.from_numpy(np.frombuffer(octets, dtype=dtype_np).copy()).view(info["shape"])
                w1, w_min, w_max = (t.to(torch.float32) for t in patch[cle])
                if w1.shape == poids.shape:
                    delta = (w1 / 255.0) * (w_max - w_min) + w_min
                    poids = (poids.to(torch.float32) + delta).to(dtype_torch)
                    octets = poids.numpy().tobytes()
                    fusionnes += 1
                else:
                    print("forme différente, laissé tel quel :", nom, tuple(w1.shape), tuple(poids.shape))
            assert len(octets) == b - a, nom
            out.write(octets)
    SORTIE.with_suffix(".part").rename(SORTIE)
    torch.save({}, VIDE)
    print(f"{fusionnes} poids fusionnés sur {len(patch)} → {SORTIE}")


if __name__ == "__main__":
    main()
