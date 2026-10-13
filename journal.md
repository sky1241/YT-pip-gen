# Journal — Kebab Datastream

Ce qui marche et ce qui rate : réglages, prompts, pièges. À tenir après **chaque
session de génération** (CLAUDE.md > Conventions). C'est ce qui fait progresser le
pipeline d'une scène à l'autre.

Format d'une entrée :

```
## AAAA-MM-JJ — <sujet>
- Contexte : <plan / perso / étape>
- Réglages : <modèle, LoRA, poids, seed, prompt>
- Résultat : <ce qui marche / ce qui rate>
- Pourquoi : <diagnostic>
- Suite : <ce qu'on change>
```

---

## 2026-10-06 — Mise en place du repo
- Contexte : Phase 0, fondations.
- Fait : contenu de départ posé à la racine, structure complète créée
  (dossiers, config.yaml, canon.yaml, continuite.md, modeles.yaml, fiches Sky + Maëlle).
- Résultat : repo prêt, premier commit. Rien installé, rien téléchargé.
- Suite : trancher le canon (voir ecriture/canon.yaml), vérifier la VRAM (nvidia-smi),
  choisir la machine de production.

## 2026-10-13 — Resynchronisation avec la conversation claude.ai, inventaire des machines
- Contexte : Phase 0. Relecture complète de la conversation claude.ai d'où vient le repo
  (« Programmes gratuits génération images », du 27 septembre au 6 octobre) et du doc
  « Checklist épisode 1 ».
- Résultat : CLAUDE.md, PLAN.md, image/INVENTAIRE.md et ecriture/corrections-cern.md sont
  identiques aux dernières versions écrites dans la conversation. La bible et les deux
  brouillons sont identiques aux textes collés le 27 septembre. Le doc claude.ai n'a qu'une
  case cochée (l'image maître de Maëlle) et un commentaire ouvert : l'épisode 1 s'arrête-t-il
  au miroir, sans le call ?
- Machines : aucune carte NVIDIA, alors que la conversation en supposait une (nvidia-smi, CUDA).
  - sky-master : AMD Radeon RX 5700 XT (gfx1010), 8 Go de VRAM, ROCm 6.2.2 installé et qui
    voit la carte. 15 Go de RAM, dont 2,6 Go disponibles et 8,2 Go de swap utilisés au moment
    du relevé. Pas de sudo pour sky : c'est donc la « Debian sans sudo » de la conversation.
  - pc1 : GeForce GTX 770 (2013), sans pilote NVIDIA. pc2 : portable, Mobility Radeon HD 5650,
    7 Go de RAM. pc3 : portable, Intel HD Graphics 620, 7 Go de RAM.
- Déjà sur sky-master : ffmpeg 5.1.9 ; Kdenlive 22.12.3 (paquet Debian, sans l'import
  OpenTimelineIO natif arrivé en 25.04 : l'AppImage reste nécessaire) ; torch 2.11 en version
  CUDA dans le Python par défaut, inutilisable sur cette carte (ComfyUI aura son propre venv).
- Le repo reste public, c'est voulu : ce qui ne va pas sur git, ce sont les épisodes montés
  en vidéo, trop lourds.
- Suite : trancher la machine de génération (CLAUDE.md > À trancher).
