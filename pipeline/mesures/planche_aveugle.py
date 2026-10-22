"""Une planche à l'aveugle : par ligne (une graine), sa référence, puis les gros plans de deux variantes, à gauche ou à droite
au hasard. La clé (qui est A, qui est B) est écrite à part, jamais sur la planche.

  python planche_aveugle.py <variante1> <variante2> <graines> <sortie.png> <cle.json> [graine_du_hasard]
"""
import os
from pathlib import Path

import yaml

RACINE = Path(__file__).resolve().parent.parent.parent
CONFIG = yaml.safe_load((RACINE / "config.yaml").read_text())
AXE = os.environ.get("KEBAB_AXE", "table-du-fond")       # l'axe des essais mesurés (variable KEBAB_AXE)
import json
import random
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

I = Path(CONFIG["sorties_root"]) / "essais" / "integration" / AXE
REF = Path(CONFIG["sorties_root"]) / "essais" / "integration" / "reference_visage_sky.png"
REF2 = RACINE / "image" / "persos" / "sky" / "references" / "trois-quarts-droit_v1.png"
F = ImageFont.truetype("/usr/share/fonts/truetype/lato/Lato-Black.ttf", 26)


def gros_plan(nom):
    r = json.loads((I / f"{nom}.json").read_text())
    x0, y0, x1, y1 = r["boite_visage_travail"]
    return Image.open(I / nom / "6_apres-visage.png").convert("RGB").crop((x0, y0, x1, y1))


v1, v2, graines, sortie, cle = sys.argv[1], sys.argv[2], [int(g) for g in sys.argv[3].split(",")], sys.argv[4], sys.argv[5]
hasard = random.Random(int(sys.argv[6]) if len(sys.argv) > 6 else 7)
T = 380
p = Image.new("RGB", (4 * (T + 10) + 120, len(graines) * (T + 20) + 60), "white")
d = ImageDraw.Draw(p)
d.text((130, 12), "référence", font=F, fill="black"); d.text((130 + T + 10, 12), "sa vue de 3/4", font=F, fill="black")
d.text((130 + 2 * (T + 10), 12), "A", font=F, fill="black"); d.text((130 + 3 * (T + 10), 12), "B", font=F, fill="black")
ref, ref2 = Image.open(REF).convert("RGB").resize((T, T)), Image.open(REF2).convert("RGB").resize((T, T))
lignes = {}
for i, g in enumerate(graines):
    y = 50 + i * (T + 20)
    d.text((10, y + T // 2), f"ligne {i + 1}", font=F, fill="black")
    p.paste(ref, (120, y)); p.paste(ref2, (120 + T + 10, y))
    a, b = (v1, v2) if hasard.random() < 0.5 else (v2, v1)
    lignes[f"ligne {i + 1}"] = {"graine": g, "A": a, "B": b}
    p.paste(gros_plan(f"sky_D_{g}_{a}").resize((T, T), Image.LANCZOS), (120 + 2 * (T + 10), y))
    p.paste(gros_plan(f"sky_D_{g}_{b}").resize((T, T), Image.LANCZOS), (120 + 3 * (T + 10), y))
p.save(sortie)
json.dump(lignes, open(cle, "w"), indent=1)
print(sortie)
