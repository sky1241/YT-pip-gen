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

## 2026-10-14 — Maëlle, premières planches ChatGPT
- Contexte : protocole perso, étapes 3 et 4. Les prompts sont dans
  image/persos/maelle/prompts-chatgpt.md.
- Réglages : une conversation ChatGPT rien que pour elle, l'image maître jointe,
  un prompt de contexte (prompt 0) qui fixe ses trois détails asymétriques et les
  règles des planches, puis une planche par prompt. Format paysage 1536 × 1024,
  grille de 3 × 2, fines lignes blanches entre les cases.
- Résultat : la planche d'émotions 1 et la rotation sont réussies du premier coup.
  Le visage reste le même d'une case à l'autre, et les côtés sont justes dans toutes
  les cases, y compris de dos (le côté rasé passe à gauche de l'image). Les lignes
  blanches suffisent : pipeline/decouper_planche.py découpe la planche tout seul.
- Ce qui a dévié : la planche d'émotions demandée de face est sortie de trois-quarts,
  sous l'angle de l'image maître. La rotation, elle, a bien donné une vraie vue de
  face. La joie est sortie en sourire en coin, proche de la malice.
- Pourquoi : sans doute l'image maître jointe, que ChatGPT recopie quand l'angle
  n'est pas le sujet de la planche. C'est une hypothèse, pas un fait vérifié.
- En pied : réussie du premier coup, avec la bague au bon pouce. Les yeux y tirent un peu
  sur le noisette : le visage est petit, ce sont les gros plans qui fixent leur couleur.
- Planche d'émotions 2 : réussie, cicatrice comprise sous la veine de colère. Mais côte à côte,
  le mépris et la joie de la planche 1 sont presque le même sourire en coin : la joie est à
  refaire, bouche ouverte et les deux coins qui montent.
- Planche d'émotions 3 : cicatrice et sourcil gauche justes partout. Deux doublons : la stupeur refait
  la surprise, la concentration ressemble à une colère légère. Les reprises se regroupent en une
  seule planche à la fin, au lieu d'une image par émotion.
- Planche d'émotions 4 : réussie. Mais ChatGPT ramène toute émotion positive vers le regard de
  l'image maître, paupières mi-closes et sourire en coin : la tendresse refait presque la joie de
  la planche 1. Les prompts des planches 5 et 6 demandent maintenant des expressions clairement
  différentes et décrivent chacune plus fort (yeux fermés, joues gonflées, bouche ouverte).
- Planche d'émotions 5 : le renfort n'a pas suffi. Le contentement garde le sourire en coin, le
  soulagement sort sans souffle ni joues gonflées, et l'émerveillement refait la surprise. La case
  du soulagement est reprise comme contentement (v2) ; soulagement et émerveillement rejoignent les
  reprises. L'exaltation et le triomphe, eux, sont enfin des sourires ouverts.
- Planche d'émotions 6 : réussie, sauf la malice, qui refait le sourire en coin du mépris. Les
  émotions franches (rire, rage, larmes, triomphe, bâillement) sortent du premier coup ; les subtiles
  retombent sur deux images toutes faites, le sourire en coin et la surprise. Les six ratées se
  refont dans une seule planche de reprises (prompt 11), qui interdit ces deux images.
- Signatures : réussies. ChatGPT a cadré à la poitrine plutôt qu'à mi-corps, mais les bras croisés
  tiennent. Sur les bras croisés, la main visible est la gauche, sans bague : c'est juste.
- Bouches : réussies, expression neutre, seule la bouche change. À l'œil le visage reste stable dans
  une rangée, mais pas au pixel près (l'écart mesuré sur la zone des yeux vaut celui de la bouche) :
  ce sont des références de forme. Les calques se feront en local, par inpainting sur une seule
  image de base. Les taches de rousseur restent nombreuses sur toutes les planches : à simplifier
  au passage local.
- Reprises (prompt 11, qui interdit le sourire en coin de l'image maître et donne des indices
  physiques impossibles à confondre) : 5 sur 6 réussies, chacune enfin distincte de ce qu'elle
  remplace. Le soulagement sort lèvres poussées, yeux fermés, sans joues gonflées : on lit un
  baiser. À refaire seul, bouche ouverte qui soupire (prompt 12).
- Soulagement (prompt 12) : réussi, bouche ouverte, tête en arrière, goutte de sueur. Les planches
  ChatGPT de Maëlle sont finies : 72 images, toutes reliées à leur prompt dans
  image/persos/maelle/provenance.json, avec la version retenue pour chaque émotion. Les prompts
  d'origine de l'image maître y sont aussi : ils comptent gauche et droite depuis l'image, la
  fiche depuis elle, et tout concorde.
- Suite : la palette de Maëlle reste de trois-quarts, et les prompts demandent
  désormais cet angle. Les émotions trop proches d'une autre se refont toutes dans une
  planche de reprises, à la fin (liste dans image/persos/maelle/prompts-chatgpt.md).
