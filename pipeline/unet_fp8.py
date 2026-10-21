"""Extrait l'UNet d'un checkpoint SDXL et range ses poids en fp8 (e4m3fn) : un fichier de 2,6 Go au lieu des 6,9 Go du
checkpoint entier.

Pourquoi (journal.md, 2026-10-21) : ComfyUI charge un fichier en le recopiant en RAM ; avec le checkpoint entier sur le
disque externe (un disque mécanique, 19 Mo/s en lecture mmap), la RAM chutait de 6,5 Go d'un coup et le garde-fou devait
couper ComfyUI. Découpé (UNet en fp8, CLIP, VAE) et posé sur le disque interne, le pic tombe à la taille du plus gros
fichier, et la carte garde 2,5 Go de plus. Les poids à une dimension (biais, normalisations) restent en fp16.

  ~/venvs/kebab/bin/python pipeline/unet_fp8.py <checkpoint.safetensors> <sortie.safetensors>

Écrit morceau par morceau (le format safetensors : un en-tête JSON, puis les tenseurs à la suite).
"""
import json
import struct
import sys

import numpy as np
import torch

TYPES = {"F16": np.float16, "F32": np.float32}


def convertir(source, sortie):
    with open(source, "rb") as f:
        taille = struct.unpack("<Q", f.read(8))[0]
        entete = json.loads(f.read(taille))
    debut = 8 + taille
    noms = sorted((k for k in entete if k.startswith("model.diffusion_model.")), key=lambda k: entete[k]["data_offsets"][0])
    nouvel, decalage, plan = {}, 0, []
    for nom in noms:
        info = entete[nom]
        n = int(np.prod(info["shape"])) if info["shape"] else 1
        fp8 = len(info["shape"]) >= 2
        dtype, octets = ("F8_E4M3", n) if fp8 else ("F16", 2 * n)
        nouvel[nom] = {"dtype": dtype, "shape": info["shape"], "data_offsets": [decalage, decalage + octets]}
        plan.append((nom, info, fp8))
        decalage += octets
    nouvel["__metadata__"] = {"kebab": f"UNet de {source.rsplit('/', 1)[-1]}, poids en fp8 e4m3fn (pipeline/unet_fp8.py)"}
    brut = json.dumps(nouvel, separators=(",", ":")).encode()
    brut += b" " * (-len(brut) % 8)
    with open(source, "rb") as src, open(sortie + ".part", "wb") as out:
        out.write(struct.pack("<Q", len(brut)))
        out.write(brut)
        for nom, info, fp8 in plan:
            a, b = info["data_offsets"]
            src.seek(debut + a)
            t = torch.from_numpy(np.frombuffer(src.read(b - a), dtype=TYPES[info["dtype"]]).copy()).view(info["shape"])
            if fp8:
                t = t.to(torch.float32).clamp(-448, 448).to(torch.float8_e4m3fn)
                out.write(t.view(torch.uint8).numpy().tobytes())
            else:
                out.write(t.to(torch.float16).numpy().tobytes())
    import os
    os.replace(sortie + ".part", sortie)
    print(f"{len(plan)} tenseurs, {sum(1 for p in plan if p[2])} en fp8 → {sortie} ({decalage / 1e9:.2f} Go)")


if __name__ == "__main__":
    convertir(sys.argv[1], sys.argv[2])
