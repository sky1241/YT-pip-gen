# CLAUDE.md — Kebab Datastream

## Le projet

Mini-série anime en français, style années 90 (entre *Le Voyage de Chihiro* et *Evangelion*). Comédie de dialogue qui fait passer de vraies notions de science, de business et de géopolitique. Diffusion sur YouTube. Objectif : un épisode de 15 à 20 minutes par semaine, éventuellement publié en deux moitiés (coupure façon eyecatch). Chaque épisode est découpé en scènes d'une à deux minutes.

- **« Sky » désigne à la fois l'auteur et le personnage principal.** Dans ce fichier, « l'auteur » = l'utilisateur, « Sky » = le personnage.
- **L'auteur écrit les épisodes. Claude ne les écrit jamais.** Il ne réécrit un passage que sur demande explicite : il liste d'abord les passages touchés et ce qu'il propose, l'auteur valide, puis il réécrit. Un problème repéré (science, canon, cohérence) se signale à l'auteur, il ne se corrige pas en silence.
- **Claude pilote la production.** Il tient ce repo à jour comme table de référence, envoie les commandes aux modèles de génération et améliore le pipeline en continu. L'auteur dirige et valide.
- Qualité visée : propre et cohérente, pas parfaite. Agréable à regarder, drôle à l'oral : on ne fait pas du Miyazaki. La cohérence d'un plan à l'autre prime sur la beauté d'une image isolée.

## Avant tout travail

1. Lire `PLAN.md` : c'est la checklist de référence. Cocher une case quand la tâche est faite et validée par l'auteur. En phase 6, ajouter une liste par scène une fois l'épisode découpé.
2. Lire `ecriture/continuite.md` (l'anti-dérive) : running gags et leur phase (plant, callback, subversion, payoff), boucles ouvertes, qui sait quoi, objets récurrents. Le mettre à jour à la fin de chaque épisode.
3. Pour un callback ou un doute de canon, aller relire les épisodes précédents dans `ecriture/episodes/`.

## Règles de contenu (non négociables)

1. **Faux en pratique, jamais faux en théorie.** Les solutions de Sky peuvent être irréalisables, jamais fausses sur le principe. Ce qui est inventé reste invérifiable.
2. **Comparer des choses comparables** : mêmes unités, même base.
3. **Aucun chiffre sans source ni date de vérification.** Si ce n'est pas vérifiable, le signaler. Ne jamais inventer.
4. **Toujours finir par le bas** : Sky lance, un perso technique reformule, Mohamed ou Théo résume en une phrase que tout le monde comprend.
5. **La bible fait foi** (`ecriture/bible/bible.md`) : voix, tics, règles des persos. Sky ne dit jamais un terme scientifique propre, sauf s'il touche à la destruction. Le même dossier contient la bible d'écriture (`bible-ecriture.md` : format, voix de Sky, outils de réaction, pièges à répétition), la recette d'un épisode (`recette-episode.md`) et la stratégie de traduction (`traduction-anglaise.md`). Ces trois fichiers sont plus anciens que la bible : quand ils la contredisent, ou contredisent le texte d'un épisode, c'est la bible et le texte qui priment, et Claude signale l'écart à l'auteur.
6. **Ne jamais modifier les noms présents dans les scripts de l'auteur.** Les références à des personnes et à des événements réels sont un choix assumé (satire volontairement ambiguë). Claude ne reproduit pas pour autant le visage d'une personne réelle : pour les personnes réelles qui apparaissent à l'écran, des designs inventés.
7. **Textes en chantier :**
   - Le texte du CERN (`ecriture/brouillons/cern.md`) est en cours de correction scientifique (`ecriture/corrections-cern.md`). À part la scène d'ouverture (les mots croisés), ne génère pas ses voix avant que l'auteur ait validé les corrections.
   - Le texte Navier-Stokes (`ecriture/brouillons/navier-stokes.md`) est à reprendre avant toute production. L'argument de Sky (borner la vitesse par le budget d'énergie) est faux en théorie : Tao (2014) a construit une équation moyennée qui respecte ce budget et explose quand même en temps fini. Et en septembre 2026, OpenAI a annoncé une explosion en temps fini avec une force extérieure ; la version sans force reste ouverte.

## Circulation entre les zones

- `ecriture/` alimente `production/`, jamais l'inverse : la production ne modifie jamais l'écriture.
- Un épisode prêt est figé par un tag git (`ep01-v1`). La production travaille sur ce tag. Si le texte change, nouveau tag (`ep01-v2`) : Claude compare les deux versions et liste les plans à refaire.

## Le workflow d'une scène (l'ordre ne change pas)

1. **Découpage** : `ecriture/episodes/epNN/episode.md` (version taguée) → scènes → `production/epNN/sNN/plans.json`, scène par scène, validé avec l'auteur.
2. **Voix** : TTS de chaque réplique avec son intention. La durée réelle des fichiers audio fixe la durée des plans (mise à jour de `plans.json`).
3. **Animatic** : images fixes posées sur la piste audio. → **Validation de l'auteur.**
4. **Images clés** : 2 ou 3 variantes par plan. → **Choix de l'auteur.**
5. **Mouvement**, selon le champ `methode` du plan (voir plus bas).
6. **Timeline** : export OpenTimelineIO, import dans Kdenlive. → **Montage final par l'auteur.**

On n'automatise que ce qui a déjà marché une fois à la main.

## Méthodes de plan (champ `methode`)

| Valeur | Principe | Quand |
|---|---|---|
| `fixe` | Image fixe + mouvement de caméra au montage | Plans contemplatifs, et **tout plan avec du texte à l'écran** (les modèles vidéo déforment les lettres) |
| `calques` | Fond fixe + persos en calques ; seul celui qui parle bouge (3 bouches selon le volume de la voix) | Dialogues, plans de groupe |
| `i2v` | Image-to-video, petits mouvements uniquement | Respiration, clignements, cheveux, pluie, vapeur, léger mouvement de tête |
| `s2v` | Speech-to-video depuis l'image et la voix | Gros plans de dialogue |
| `zone` | Animation d'une seule zone de l'image (masque) | Plans de groupe où un seul perso bouge |

- Pas de gros gestes : se lever, traverser la pièce, manipuler des objets.
- Sky qui mange : mastication en plan moyen, la bouchée suggérée par une coupe (un plan avant, un plan après).
- Plans de groupe : partir de l'image maître de l'axe, ne modifier que le perso qui joue (inpainting avec son LoRA), mettre les autres en flou ou de dos quand c'est possible.
- Changement d'expression : coupe sèche par défaut. La transition générée (une image de début, une image de fin) est réservée aux moments clés, comme le sourire de Sky. Les deux images doivent être le même plan : même cadrage, même pose, même fond, seul le visage change (inpainting sur la même image de base).

## Images

- **ChatGPT sert uniquement à la conception** : fiches persos, fonds, exploration du style. Aucune image clé de production ne vient de ChatGPT : elles sortent toutes du modèle local, pour la cohérence.
- **Fonds fixes** : un fond par axe de caméra, fait une fois et réutilisé. Les persos s'intègrent dedans. Le kebab fonctionne comme un décor de sitcom : quelques axes fixes, les mêmes places qui reviennent.
- Un LoRA par perso + un LoRA de style. `image/style.md` est la référence visuelle.
- Contexte par image selon le besoin : image-to-image (composition, couleurs), ControlNet (pose, structure), IP-Adapter (style ou identité). Le prompt ne doit jamais contredire l'image de référence.
- `image/explorations/` contient des essais non validés. Ils ne servent jamais de référence de production.

### Protocole de création d'un perso

Dans l'ordre. Un perso n'entre en production que quand les 8 étapes sont faites.

1. **Fiche texte** (`image/persos/<slug>/fiche.json`), tirée de la bible : rôle, énergie, silhouette, palette (codes couleur), tenue canonique, détails asymétriques avec le côté exact, accessoires, ce qu'il ne porte jamais.
2. **Image maître**, conçue dans ChatGPT et validée par l'auteur.
3. **Planche de rotation** : face, trois-quarts, profil, dos, en pied, sur fond neutre et sous la même lumière. AniSora peut générer une rotation à 360° depuis l'image de face.
4. **Expressions** : la palette des émotions, la même pour tous : 36 émotions en 6 planches (`image/emotions.md`), + 2 à 4 signatures tirées de la bible ou du texte. Sky, le protagoniste, en a plus : sa palette aussi de trois-quarts, et toutes ses signatures. La liste fichier par fichier est dans `image/INVENTAIRE.md`.
5. **Bouches** : fermée, mi-ouverte, ouverte, sous les angles principaux.
6. **Passage local** : tout repasse dans le modèle local (image-to-image), dans le style final. C'est le jeu d'entraînement du LoRA.
7. **LoRA + test standard** : les mêmes 10 prompts de test pour chaque perso. Retournement horizontal (flip) désactivé pour tout perso aux détails asymétriques.
8. **Voix** (`audio/voix/<slug>/`) : description tirée de la table des énergies de la bible, 3 répliques types, validation. Sky a la voix de l'auteur, faite par lui. Les autres partent d'une voix de base choisie d'après leur description, retouchée au montage si besoin.

## Stack (gratuite, à confirmer selon la VRAM)

- **ComfyUI** en local, piloté par son API HTTP. Les workflows sont exportés au format API dans `workflows/`. Ne jamais utiliser les « API nodes » (modèles fermés payants).
- **Images** : checkpoint anime SDXL (NoobAI-XL ou Illustrious).
- **Vidéo** : AniSora (V3.x, construit sur Wan 2.2 ; une version de la V3.1 tourne avec 12 Go de VRAM) pour l'image-to-video, l'interpolation entre images clés, l'animation par masque, le guidage audio, la rotation à 360° d'un perso et la super-résolution. Wan 2.2 en complément (speech-to-video). LTX si la VRAM le permet.
- **Voix** : Qwen3-TTS. Sky a la voix de l'auteur. Les autres partent d'une voix de base choisie d'après leur description, retouchée au montage si besoin.
- **Montage** : Kdenlive (AppImage), timeline via OpenTimelineIO.
- **Outils** : Python, ffmpeg.
- La licence de chaque modèle est notée dans `modeles.yaml` : la série est publiée sur YouTube. AniSora est sous Apache 2.0 avec des restrictions d'usage à lire avant de monétiser.
- Budget outils, hors abonnement Claude : environ 10 par semaine maximum.
- Pas de variable `ANTHROPIC_API_KEY` sur la machine : elle ferait facturer l'API au lieu d'utiliser l'abonnement.
- Sur la Debian sans sudo : installations en espace utilisateur uniquement (venv, pip, AppImage).

## Fichiers

**Le repo est la table de référence** : tout ce qui sert à générer y est, images de référence comprises. **Le disque externe reçoit tout ce qui est généré**, plus les poids des modèles.

```
kebab-datastream/              (git : tout ce qui sert de référence)
├── CLAUDE.md
├── PLAN.md                    la checklist de l'épisode en cours
├── config.yaml                chemins et URL (ComfyUI, racines du disque externe)
├── modeles.yaml               modèles : lien, empreinte, licence
├── journal.md                 ce qui marche et ce qui rate : réglages, prompts, pièges
├── ecriture/
│   ├── bible/
│   │   ├── bible.md           persos, relations, dynamiques, espaces, craft : fait foi
│   │   ├── bible-ecriture.md  format, voix de Sky, outils de réaction, pièges
│   │   ├── recette-episode.md ce que chaque épisode doit enseigner et mélanger
│   │   └── traduction-anglaise.md   la stratégie pour la version anglaise
│   ├── canon.yaml             noms, lieux, âges : la seule vérité
│   ├── continuite.md          l'état de la série, mis à jour à chaque épisode
│   ├── corrections-cern.md    brief de corrections du texte du CERN
│   ├── brouillons/            textes en cours
│   ├── sources/               textes d'origine du JDR (lulz, institut, Léa) : ne font pas foi
│   └── episodes/epNN/         episode.md : la version figée par un tag
├── image/
│   ├── INVENTAIRE.md          la liste image par image, à cocher
│   ├── emotions.md            la palette des émotions, commune à tous les persos
│   ├── style.md               le style visuel de référence
│   ├── persos/<slug>/         fiche.json, planches/, references/, expressions/, bouches/
│   ├── decors/<lieu>/<axe>/   fonds fixes validés
│   ├── accessoires/           objets récurrents : galette, tasse, téléphone…
│   ├── gabarits/              cartons texte et SMS, faits en code
│   └── explorations/          essais non validés
├── audio/
│   └── voix/<slug>/           description, référence audio, réglages
├── production/epNN/sNN/       plans.json
├── workflows/                 workflows ComfyUI au format API
└── pipeline/                  le code, avec une seule commande d'entrée

<disque externe>/              (hors git : tout ce qui est généré ou lourd)
├── sorties/                   variantes d'images, clips, voix générées, montages
└── modeles/                   poids des modèles
```

### Conventions

- **Aucun chemin en dur** : tout passe par `config.yaml` (`sorties_root`, `modeles_root`, `comfyui_url`). Les chemins de référence sont relatifs à la racine du repo.
- **Seules les versions validées entrent dans git.** Les variantes générées restent sur le disque externe jusqu'à ce que l'auteur les valide.
- **Identifiants partout** : `ep01_s01_p003_v2.png`. Slugs en minuscules, sans accents ni espaces.
- **Une seule source de vérité par sujet** : `ecriture/canon.yaml` (noms, lieux), `image/persos/<slug>/fiche.json` (look d'un perso), `audio/voix/<slug>/` (sa voix), `image/style.md` (style visuel), `PLAN.md` (avancement).
- **Tout ce qui est généré est reproductible** : modèle, LoRA et poids, prompt, seed et références sont notés dans `plans.json`.
- **On n'écrase jamais une référence validée** : les nouvelles versions s'ajoutent (`_v2`, `_v3`).
- **Dans `image/INVENTAIRE.md`, une case = un fichier** : dès qu'un fichier validé existe au chemin indiqué, cocher la case.
- **Tenir `journal.md`** : après chaque session de génération, noter les réglages et les prompts qui marchent, ceux qui ratent, et pourquoi. C'est ce qui fait progresser le pipeline d'une scène à l'autre.
- **Surveiller la taille du repo** : GitHub bloque tout fichier de plus de 100 Mo. Si le repo devient lourd, passer les images en Git LFS.
- **Avant tout téléchargement lourd ou toute suppression, demander à l'auteur.** Annoncer la taille et la licence avant de télécharger un modèle.

### Schéma d'un plan (`plans.json`)

```json
{
  "id": "ep01_s01_p003",
  "axe": "kebab/table-du-fond",
  "persos": ["patrick", "sky"],
  "locuteur": "patrick",
  "replique": "Mais ça rentre aussi.",
  "intention": "flegme, satisfaction discrète",
  "cadrage": "plan rapproché sur Patrick",
  "methode": "calques",
  "duree_s": null,
  "prompt": "",
  "references": ["image/persos/patrick/references/face_v1.png"],
  "lora": [{"nom": "patrick", "poids": 0.8}],
  "seed": null,
  "variantes": [],
  "choix": null,
  "statut": "a_generer"
}
```

Statuts : `a_generer` → `genere` → `valide` ou `rejete`. Les répliques sont copiées telles quelles depuis `episode.md`.

## À trancher avec l'auteur (ne pas décider seul)

- **Canon du kebab** : Mohamed à Annemasse (texte du CERN) ou Mehmet à Clichy (texte Navier-Stokes). Ça décide un LoRA et tous les décors.
- **Ce que couvre l'épisode 1** : « Le Miroir » seul, ou avec le call.
- **La machine de génération.** Aucune machine du parc n'a de carte NVIDIA (relevé du 13 octobre 2026, détail dans `config.yaml`). La mieux équipée, sky-master, a une AMD Radeon RX 5700 XT de 8 Go : c'est trop peu pour AniSora, qui demande 12 Go dans sa version légère, et ROCm ne prend pas officiellement en charge cette génération de puce. Options : tester les images sur cette carte, puis louer ou acheter une carte NVIDIA pour la vidéo.- **Le style définitif** (`image/style.md`), et si le rendu de l'image maître de Maëlle devient la référence de toute la série.

## Premier lancement

1. Lire ce fichier et `PLAN.md`, puis dire à l'auteur où on en est.
2. Créer ce qui manque : `audio/`, `production/`, `workflows/`, `pipeline/`, `image/decors/` ; le `.gitignore` (vidéos, audio généré, caches, fichiers temporaires, `.env`) ; `config.yaml` (demander le chemin du disque externe) ; `ecriture/canon.yaml` avec les points à trancher ; `ecriture/continuite.md` avec ses rubriques ; `modeles.yaml` et `journal.md` vides.
3. Créer les fiches de Maëlle et de Sky avec ce qui est déjà décidé :
   - **Maëlle** (`image/persos/maelle/fiche.json`) : image maître `references/master_v1.png`. Roux en undercut, taches de rousseur (à simplifier en production), petite cicatrice au sourcil, bague, col roulé noir, café à la main. Détails asymétriques : côtés à fixer avec l'auteur, flip désactivé au LoRA.
   - **Sky** (`image/persos/sky/fiche.json`) : training noir, chemise blanche à fleurs de lys, yeux bleus, 87 kg. En temps normal, ses yeux ont des reflets. Le sourire : les reflets disparaissent, pas de plis aux yeux, joues plates, seule la bouche bouge. Le rire du dégénéré : grimace façon Tanya (*Youjo Senki*). Bouches en plus : sourire fermé, grimace, rire ouvert.
4. Premier commit.
5. Ne rien télécharger de lourd sans accord.

## Plus tard

- Version anglaise : sous-titres d'abord, puis doublage en TTS avec les mêmes voix. La stratégie déjà décidée pour le texte est dans `ecriture/bible/traduction-anglaise.md` : le français brut de Sky reste, avec sa traduction. Les jeux de mots (dont les mots croisés de Patrick) se réécrivent, ils ne se traduisent pas.
