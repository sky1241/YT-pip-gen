"""Recale la caméra d'un fond peint : la position, la hauteur, le cap et le champ qui envoient des points connus du plan
(en mètres, ceux de pipeline/plan_kebab.py) sur les pixels où ChatGPT les a peints. Le fond suit la vue en volumes à
quelques centimètres près, pas au pixel : pour poser un perso à sa place et à sa taille, on calcule avec la caméra recalée.

  python3 pipeline/recaler_camera.py image/decors/kebab/table-du-fond/camera.json

Le fichier donne les points repérés sur le fond (« points ») et le départ (« depart », la caméra de pipeline/vue_kebab.py) ;
le script y écrit la caméra recalée (« camera ») et l'écart de chaque point, en pixels. L'inclinaison reste à 0 (les
verticales du fond sont verticales) ; sinon, l'ajouter aux inconnues.
"""
import json
import math
import sys

import numpy as np

LARGEUR, HAUTEUR = 1536, 1024
INCONNUES = ("x", "y", "hauteur", "cap", "champ")


def projeter(camera, points):
    """Les pixels d'un ou plusieurs points du plan (x, y, z en mètres), avec la caméra d'un fond (un dict de INCONNUES)."""
    a = math.radians(camera["cap"])
    avant = np.array([math.cos(a), math.sin(a), 0.0])
    droite = np.array([-math.sin(a), math.cos(a), 0.0])    # le plan a y vers le bas (comme pipeline/vue_kebab.py)
    focale = (LARGEUR / 2) / math.tan(math.radians(camera["champ"]) / 2)
    v = np.atleast_2d(np.asarray(points, float)) - np.array([camera["x"], camera["y"], camera["hauteur"]])
    x, y, z = v @ droite, v[:, 2], v @ avant
    z = np.where(z > 0.05, z, np.nan)
    return np.stack([LARGEUR / 2 + focale * x / z, HAUTEUR / 2 - focale * y / z], axis=1)


def nelder_mead(f, depart, pas, iterations=4000):
    sommets = [np.array(depart, float)] + [np.array(depart, float) + np.eye(len(depart))[i] * pas[i]
                                          for i in range(len(depart))]
    valeurs = [f(s) for s in sommets]
    for _ in range(iterations):
        ordre = np.argsort(valeurs)
        sommets, valeurs = [sommets[i] for i in ordre], [valeurs[i] for i in ordre]
        centre = np.mean(sommets[:-1], axis=0)
        r = centre + (centre - sommets[-1]); fr = f(r)
        if fr < valeurs[0]:
            e = centre + 2 * (centre - sommets[-1]); fe = f(e)
            sommets[-1], valeurs[-1] = (e, fe) if fe < fr else (r, fr)
        elif fr < valeurs[-2]:
            sommets[-1], valeurs[-1] = r, fr
        else:
            k = centre + 0.5 * (sommets[-1] - centre); fk = f(k)
            if fk < valeurs[-1]:
                sommets[-1], valeurs[-1] = k, fk
            else:
                sommets = [sommets[0] + 0.5 * (s - sommets[0]) for s in sommets]
                valeurs = [f(s) for s in sommets]
    i = int(np.argmin(valeurs))
    return sommets[i], valeurs[i]


def recaler(chemin):
    donnees = json.loads(open(chemin).read())
    plan = np.array([p["plan"] for p in donnees["points"]], float)
    pixels = np.array([p["pixel"] for p in donnees["points"]], float)

    def erreur(v):
        ecart = projeter(dict(zip(INCONNUES, v)), plan) - pixels
        return float(np.nansum(ecart ** 2)) + 1e9 * int(np.isnan(ecart).any())

    depart = [donnees["depart"][k] for k in INCONNUES]
    meilleur = None
    # plusieurs départs autour de la caméra de la vue en volumes, pour ne pas rester dans un creux local
    for decalage in ([0, 0, 0, 0, 0], [-0.4, 0.4, 0.1, 7, -6], [0.4, -0.4, -0.1, -8, 6], [-0.9, 0.7, 0, -3, -11]):
        v, e = nelder_mead(erreur, np.array(depart) + decalage, [0.3, 0.3, 0.1, 5, 5])
        if meilleur is None or e < meilleur[1]:
            meilleur = (v, e)
    camera = {k: round(float(c), 3) for k, c in zip(INCONNUES, meilleur[0])}
    calcules = projeter(camera, plan)
    for p, c in zip(donnees["points"], calcules):
        p["ecart_px"] = round(float(np.hypot(*(c - np.array(p["pixel"])))), 1)
    donnees["camera"] = camera
    open(chemin, "w").write(json.dumps(donnees, ensure_ascii=False, indent=2) + "\n")
    print("caméra recalée :", camera)
    for p in donnees["points"]:
        print(f"  {p['quoi']} : écart {p['ecart_px']} px")


if __name__ == "__main__":
    recaler(sys.argv[1])
