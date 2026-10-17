# Kebab Datastream — Checklist épisode 1

Version du 6 octobre 2026, mise à jour le 17 octobre 2026. C'est ce fichier qui fait foi : on coche ici, plus dans le doc claude.ai.

## Où on en est (17 octobre 2026)

- **Fait** : les fondations du repo, la palette des émotions et l'outil de découpe. Maëlle et Sky ont toutes leurs planches de référence (Sky : la série 2, les 50 cases de son inventaire). La chaîne d'images marche de bout en bout : ComfyUI sur la carte AMD de sky-master (`pipeline/comfyui.py`), le modèle Animagine XL 4.0, le premier LoRA de Sky entraîné sur Kaggle en une heure et testé (`image/test-standard.md`). Le minage est désinstallé, et Claude se lance depuis un terminal (icône « Kebab Datastream »). Le style de la série est décidé (`image/style.md`), le canon aussi (Mohamed à Annemasse). Le kebab a son plan validé (`image/decors/kebab/plan_v6.png`), sa base peinte (`plan-peint_v2.png`), ses 25 axes (`axes.md`) et huit fonds, les axes 6, 7, 20, 21, 8, 2, 11 et 10, faits avec la vue en volumes (`pipeline/vue_kebab.py`).
- **En cours** : les fonds du kebab, un axe à la fois : 7 des 9 du pilote faits (6, 7, 20, 21, 8, 2, 10), puis 1 et 17. Le LoRA de Sky. La v1 reconnaît son visage, ses cheveux, sa barbe, ses lunettes dorées, ses colliers et son sourire de monstre ; l'auteur en est content. Elle rate l'œil aveugle hors de face, et la tenue hors des gros plans (une seule image en pied dans le jeu).
- **Ensuite** : l'avis de l'auteur sur la v2 du LoRA de Sky (faite et testée le 2026-10-16 : l'œil aveugle est appris). Puis Maëlle : ses 4 planches en pied et en gestes, et son LoRA. Chaque nouveau perso aura ces planches dès le départ.
- **Décisions qui attendent l'auteur** : ce que couvre l'épisode 1, s'il faut un LoRA de style (années 90 tout fait, ou le nôtre) en plus de l'IP-Adapter ; le style lui-même est décidé (`image/style.md`), garder ou non la règle « sans sudo » de CLAUDE.md (le compte a sudo).
- **Pas commencé** : l'écriture de l'épisode 1 (phase 1), Patrick, Mohamed et les autres persos, les voix, la vidéo, le pilote.

## Mode d'emploi

Objectif : un épisode 1 complet de 15 minutes, monté et prêt à publier.

Ordre : la phase 0, puis les phases 1 et 2 en parallèle, puis le pilote (phase 3). Tout ce qui suit attend le bilan du pilote : phases 4, 5, 6 et 7. À l'intérieur d'une phase, tu coches dans l'ordre que tu veux, sauf mention contraire.

- Chaque phase dit quand elle est terminée.
- Dans chaque scène, trois validations restent à toi : l'animatic, le choix des images clés et le montage final.
- On n'automatise que ce qui a déjà marché une fois à la main.

## Phase 0 — Fondations

Terminée quand une image, une phrase de voix et un clip de 5 secondes sortent de ta machine, en local.

- [x] Créer le repo GitHub
- [x] Mettre à jour `CLAUDE.md` pour le repo unique (zones `ecriture/`, `image/`, `audio/`, `production/`, `continuite.md`, tags git)
- [x] Poser le contenu du dossier de départ à la racine du repo, puis premier commit
- [x] Vérifier avec `/context` que Claude Code charge bien `CLAUDE.md`
- [x] Lancer le « premier lancement » de `CLAUDE.md` (dossiers, `config.yaml`, `canon.yaml`, fiches de Sky et Maëlle)
- [x] Vérifier la carte graphique et sa VRAM, et noter le résultat : AMD Radeon RX 5700 XT, 8 Go, aucune carte NVIDIA sur le parc (`config.yaml`)
- [ ] Choisir la machine de production. Pour les images : sky-master, 2 min 30 par image avec un LoRA (testé le 2026-10-15). Pour entraîner les LoRA : Kaggle, gratuit, environ 1 h par perso. Pour la vidéo : AniSora demande 12 Go et la carte en a 8, donc une version compressée à essayer, sans garantie, sinon Modal ou Kaggle (gratuits), puis une location. Voir `CLAUDE.md` > À trancher
- [x] Choisir le modèle de base d'images d'après sa licence : Animagine XL 4.0 (usage commercial permis), pris pour les premiers tests le 2026-10-15 ; Illustrious XL v0.1 (images libres, la monétisation « découragée »), 6,9 Go chacun. NoobAI-XL est exclu si la chaîne est monétisée : sa licence interdit de commercialiser ses images (détail dans `journal.md`, 2026-10-15)
- [x] Créer les comptes de calcul de secours, le 2026-10-15 : Kaggle (30 h de GPU par semaine, relié à sky-master, a servi au LoRA de Sky) et Modal (relié, mais ses cartes graphiques demandent une carte bancaire, même pour les crédits gratuits)
- [x] Préparer le disque externe (`sorties/`, `modeles/`) et noter ses chemins dans `config.yaml`
- [x] Vérifier qu'aucune variable `ANTHROPIC_API_KEY` ne traîne sur la machine
- [x] Installer Python (venv), ffmpeg et ComfyUI, en espace utilisateur sur la Debian sans sudo (le venv, le PyTorch d'AMD et ComfyUI le 2026-10-15 ; ffmpeg 5.1.9 était déjà là)
- [x] Générer une première image dans ComfyUI : le 2026-10-15, avec Animagine XL 4.0, puis le test standard du LoRA de Sky (`<sorties_root>/comfyui/`)
- [ ] Installer Kdenlive (AppImage)
- [ ] Installer Qwen3-TTS et générer une phrase test
- [ ] Tester AniSora : un clip de 5 secondes depuis une image. Sur sky-master, la version 12 Go ne tient pas (8 Go) : une version compressée à essayer après les images ; sinon sur Modal ou Kaggle

## Phase 1 — Écriture

Terminée quand l'épisode 1 est figé dans le repo avec le tag `ep01-v1`. Cette phase peut avancer en parallèle de la phase 2.

- [ ] Trancher le canon : Mohamed à Annemasse ou Mehmet à Clichy
- [ ] Choisir ce que couvre l'épisode 1 dans le texte du CERN (environ 15 minutes) et où tombe la coupure du milieu
- [ ] Corriger la science avec `ecriture/corrections-cern.md`, pour la partie retenue :
  - [ ] CERN : 25 États membres, budget 2026 d'environ 1,5 milliard de CHF
  - [ ] Langues : remplacer l'explication de Maëlle par la transparence des nombres
  - [ ] Nucléaire : l'antimatière transporte l'énergie sans la produire ; Sky ne promet jamais « la fin du nucléaire »
  - [ ] Pivot vers l'espace à la place de la comparaison avec le lithium
  - [ ] Chiffres du consortium reconstruits sur un marché spatial sourcé
- [ ] Réduire le tic « vient de »
- [ ] Trancher les points en suspens : la théorie du tout (ambiguë ou révélée), les quenelles, la vanne sur la sodomie, le briefing de guerre (cet épisode ou le suivant)
- [ ] Trancher les écarts entre `bible-ecriture.md` et la bible ou le texte : le couple (« Sky = soumis content »), Mehmet à Istanbul ou Mohamed à Alger, Sky à 87 ou 92 kg (l'auteur a dit 92 le 2026-10-14 : reste à aligner le texte du CERN et la bible), Yamauchi ou Asai, l'explication des langues que `corrections-cern.md` remplace
- [ ] Fact-check final : chaque chiffre sourcé et daté, chaque comparaison faite sur la même base
- [ ] Lire l'épisode à voix haute, chrono en main : viser 15 minutes
- [ ] Déposer l'épisode dans `ecriture/episodes/ep01/episode.md`
- [ ] Remplir `ecriture/continuite.md` : running gags et leur phase, boucles ouvertes, qui sait quoi
- [ ] Poser le tag `ep01-v1`

## Phase 2 — Direction artistique

Terminée quand `image/style.md` est validé et que le kebab a son plan d'axes de caméra.

- [x] Image maître de Maëlle
- [x] Décider le style de la série : celui des images de référence de Sky et de Maëlle, un anime des années 90 entre *Street Fighter II*, *Evangelion* et Ghibli (l'auteur, le 2026-10-16)
- [ ] Explorer le style dans ChatGPT : une vue large du kebab et Sky, dans le même rendu
- [ ] Écrire `image/style.md` : mots-clés de prompt, palette, 3 à 5 images de référence (écrit le 2026-10-16 : la décision, les références et ce qui fait le style ; les mots-clés restent à tester, puis l'auteur valide)
- [x] Dessiner le plan du kebab vu de dessus : tables, comptoir, broche, miroir, escalier, vitrine (le 2026-10-17 : `image/decors/kebab/plan_v6.png` en code, et sa version peinte `plan-peint_v2.png`, la base fixe validée par l'auteur)
- [x] Lister les 6 à 8 axes de caméra et qui s'assoit où (Claude peut le préparer depuis le script) : 25 axes, validés par l'auteur le 2026-10-17, sur le plan v6 (`image/decors/kebab/axes.md`, `plan-axes_v7.png`), trois lumières (jour, pluie, nuit), 45 fonds en tout dont 9 pour le pilote ; 6 points du texte à trancher
- [ ] Définir les cartons texte façon Eva (chiffres clés) et le carton SMS : police, couleurs, durée à l'écran
- [x] Tester une première planche de la palette des émotions sur Maëlle, dont l'image maître existe, puis sa découpe en fichiers (`pipeline/decouper_planche.py`)

## Phase 3 — Pilote d'une minute, à la main

Terminée quand la minute des mots croisés est montée et que le temps passé à chaque étape est noté. Trois persos : Sky, Patrick et Mohamed. Les images à faire sont listées une par une dans `image/INVENTAIRE.md`, section 1.

- [ ] Fiches des trois persos : compléter le look, d'après la liste « à compléter » de chaque fiche (rôle, énergie et signatures sont déjà posés)
- [x] Image maître de Sky : chemise blanche à lys, training noir, lunettes aviateur, œil gauche aveugle (`image/persos/sky/description-chatgpt.md`) ; la monture est plaquée or (v2), et la v3 est la référence de la série 2
- [ ] Image maître de Patrick
- [ ] Image maître de Mohamed
- [ ] Expressions du pilote, marquées « · pilote » dans `image/INVENTAIRE.md`, dont le sourire de Sky : yeux sans reflet, joues plates, seule la bouche bouge (celles de Sky sont faites ; restent Patrick et Mohamed)
- [ ] Bouches fermée, mi-ouverte et ouverte pour les trois (celles de Sky sont faites)
- [ ] Les 9 fonds du pilote, de jour (axes 1, 2, 6, 7, 8, 10, 17, 20, 21 de `image/decors/kebab/axes.md`) : 6 (la table de Sky), 7 (son contrechamp), 20 (la place de Patrick), 21 (son contrechamp), 8 (le comptoir), 2 (l'entrée) et 10 (le pied de l'escalier) faits et validés le 2026-10-17
- [ ] Voix des trois persos : compléter et valider leur description dans `audio/voix/` (énergie et 3 répliques déjà posées)
- [ ] Découpage de la scène en `plans.json` (Claude)
- [ ] Voix générées, puis animatic → validation
- [ ] Images clés en 2 ou 3 variantes → choix
- [ ] Mouvement : les bouches en calques, un plan en image-to-video, un test AniSora
- [ ] Ambiance sonore : la broche, le tram
- [ ] Montage dans Kdenlive → validation
- [ ] Bilan dans `journal.md` : temps par étape, ce qui a été pénible
- [ ] Estimer le temps d'un épisode : le temps de la minute × 15

## Phase 4 — Automatisation

Terminée quand la scène du pilote se refait en automatique et que tu as comparé les deux versions. Commence par les étapes que le journal du pilote note comme pénibles.

- [ ] Figer le schéma de `plans.json`
- [ ] Découpage automatique : script → `plans.json`
- [ ] Voix en batch, avec les durées réelles reportées dans `plans.json`
- [ ] Animatic automatique : images fixes posées sur la piste audio
- [ ] Images clés via l'API de ComfyUI (workflows exportés au format API)
- [ ] Mouvement : appels à AniSora ou Wan selon le champ `methode`
- [ ] Bouches automatiques selon le volume de la voix (mode `calques`)
- [ ] Timeline OpenTimelineIO, importée dans Kdenlive
- [ ] Outil de choix des variantes : une grille, un clic par plan
- [ ] Refaire le pilote en automatique et comparer avec la version à la main

## Phase 5 — Tous les persos et les décors

Terminée quand chaque perso de l'épisode 1 a coché son protocole et que chaque axe de caméra a son fond. La liste suit « Le Miroir », à ajuster selon ce que couvre l'épisode.

Le protocole, pour chaque perso, est dans `CLAUDE.md`. Ici, une case par étape. Le détail fichier par fichier est dans `image/INVENTAIRE.md`, et ce qui manque à chaque fiche est dans sa liste « à compléter ».

La palette des émotions, la même pour tous : 36 émotions en 6 planches, définies dans `image/emotions.md`.

- [ ] Sky (série 2 : la série 1, monture argentée, est archivée sur le disque externe le 2026-10-14)
  - [ ] Fiche : relever les codes couleur sur l'image maître v3 (ceux de la fiche viennent de la v1), puis les faire valider
  - [x] Image maître (v1, puis v2 en or)
  - [x] Image maître v3 : sans le trait entre les sourcils ni les taches autour des yeux, barbe de 3 jours (l'œil aveugle reste un peu plus grand : ChatGPT refuse de le retoucher, l'auteur garde la v3)
  - [x] Rotation : face, trois-quarts et profil des deux côtés, dos
  - [x] Image en pied
  - [x] En pied et en gestes : les 5 planches, le 2026-10-16 (prompts L1 à L5 de `prompts-chatgpt.md`, avec la liste de contrôle de chaque planche et la procédure du LoRA v2), pour le LoRA v2
  - [x] Palette des émotions de face : les 6 planches, les reprises et le clignement (mi-clos, fermé)
  - [x] Palette des émotions de trois-quarts : les 6 planches et leur retouche (deux bagues restent à corriger au passage local)
  - [x] Signatures : les 9, dont le jeu du sourire en monstre, plus le rire du dégénéré de trois-quarts
  - [x] Bouches : les 6 de base et les 6 du sourire (sourire fermé, grimace, rire ouvert, sous les deux angles)
  - [ ] LoRA : passage local, entraînement, test standard
    - [x] v1, le 2026-10-15 : 105 images de ChatGPT sans passage local, entraînée sur Kaggle en 1 h, testée (planche : `<sorties_root>/comfyui/test-standard_sky_v1_planche.png`). Visage, lunettes, colliers et sourire appris ; l'œil aveugle seulement de face, la tenue seulement en buste
    - [ ] v2, entraînée et testée le 2026-10-16, en attente de l'avis de l'auteur (planche : `<sorties_root>/comfyui/test-standard_sky_v2_planche.png`). L'œil aveugle juste sur les 10 tests (la v1 : 2 sur 10), la chemise juste sur 9 ; en pied, il faut écrire la tenue dans le prompt (`fiche.json` > `lora` > `tags_en_pied`)
    - [ ] Corriger les bagues ratées au passage local (la liste : `fiche.json` > `_a_completer` ; l'auteur ne les fait plus refaire dans ChatGPT)
  - [ ] Voix : compléter et valider `audio/voix/sky/`
- [ ] Maëlle
  - [ ] Fiche : valider les codes couleur relevés (1m65, côtés asymétriques confirmés, le reste du look est posé)
  - [x] Image maître
  - [x] Rotation : face, trois-quarts et profil des deux côtés, dos
  - [x] Image en pied
  - [ ] En pied et en gestes : les 4 planches, avant son LoRA (elle n'a qu'une image en pied, comme Sky en v1)
  - [x] Palette des émotions de trois-quarts, sous l'angle de son image maître : les 6 planches et les reprises (la version retenue de chaque émotion est dans `provenance.json`)
  - [x] Signatures : les 4
  - [x] Bouches : les 6 (références de forme ; les calques se feront en local sur une seule image de base)
  - [ ] Taches de rousseur à simplifier au passage local : sur les planches, elles restent nombreuses
  - [ ] LoRA : passage local, entraînement sans retournement horizontal, test standard
  - [ ] Voix : compléter et valider `audio/voix/maelle/`
- [ ] Patrick
  - [ ] Fiche : compléter le look
  - [ ] Image maître
  - [ ] Rotation : face, trois-quarts et profil des deux côtés, dos
  - [ ] Image en pied
  - [ ] En pied et en gestes : les 4 planches
  - [ ] Palette des émotions : les 6 planches
  - [ ] Signatures : les 5
  - [ ] Bouches : les 6
  - [ ] LoRA : passage local, entraînement, test standard
  - [ ] Voix : compléter et valider `audio/voix/patrick/`
- [ ] Mohamed
  - [ ] Fiche : trancher le canon (Mohamed ou Mehmet), puis compléter le look
  - [ ] Image maître
  - [ ] Rotation : face, trois-quarts et profil des deux côtés, dos
  - [ ] Image en pied
  - [ ] En pied et en gestes : les 4 planches
  - [ ] Palette des émotions : les 6 planches
  - [ ] Signatures : les 3
  - [ ] Bouches : les 6
  - [ ] LoRA : passage local, entraînement, test standard
  - [ ] Voix : compléter et valider `audio/voix/mohamed/`
- [ ] Seb
  - [ ] Fiche : compléter le look, dont le costard
  - [ ] Image maître
  - [ ] Rotation : face, trois-quarts et profil des deux côtés, dos
  - [ ] Image en pied
  - [ ] En pied et en gestes : les 4 planches
  - [ ] Palette des émotions : les 6 planches
  - [ ] Signatures : les 3
  - [ ] Bouches : les 6
  - [ ] LoRA : passage local, entraînement, test standard
  - [ ] Voix : compléter et valider `audio/voix/seb/`
- [ ] Nath
  - [ ] Fiche : compléter le look
  - [ ] Image maître
  - [ ] Rotation : face, trois-quarts et profil des deux côtés, dos
  - [ ] Image en pied
  - [ ] En pied et en gestes : les 4 planches
  - [ ] Palette des émotions : les 6 planches
  - [ ] Signatures : les 4
  - [ ] Bouches : les 6
  - [ ] LoRA : passage local, entraînement, test standard
  - [ ] Voix : compléter et valider `audio/voix/nath/`
- [ ] Théo
  - [ ] Fiche : compléter le look
  - [ ] Image maître
  - [ ] Rotation : face, trois-quarts et profil des deux côtés, dos
  - [ ] Image en pied
  - [ ] En pied et en gestes : les 4 planches
  - [ ] Palette des émotions : les 6 planches
  - [ ] Signatures : les 3
  - [ ] Bouches : les 6
  - [ ] LoRA : passage local, entraînement, test standard
  - [ ] Voix : compléter et valider `audio/voix/theo/`
- [ ] Daria
  - [ ] Fiche : compléter le look
  - [ ] Image maître
  - [ ] Rotation : face, trois-quarts et profil des deux côtés, dos
  - [ ] Image en pied
  - [ ] En pied et en gestes : les 4 planches
  - [ ] Palette des émotions : les 6 planches
  - [ ] Signatures : les 4
  - [ ] Bouches : les 6
  - [ ] LoRA : passage local, entraînement, test standard
  - [ ] Voix : compléter et valider `audio/voix/daria/`
- [ ] Grep, le chat de Daria : fiche (le motif du pelage), image maître, rotation, 2 signatures
- [ ] Nmap, le chat de Sky et Maëlle : fiche (tout le design), image maître, rotation
- [ ] LoRA de style : d'abord essayer les LoRA « années 90 » déjà prêts sur Hugging Face, notés dans `journal.md` (2026-10-15)
- [ ] Un fond par axe de caméra du kebab, plus l'escalier : 45 fonds (23 de jour, 12 de pluie, 10 de nuit), la liste dans `image/decors/kebab/axes.md` et les cases dans `image/INVENTAIRE.md`
- [ ] Une image maître par axe, avec les persos à leur place habituelle

## Phase 6 — Production scène par scène

Terminée quand toutes les scènes de l'épisode 1 sont dans la timeline. Une fois l'épisode découpé, Claude ajoute ici une liste par scène, sur le modèle de s02.

- [ ] Découper l'épisode 1 en scènes d'une à deux minutes (Claude)
- [ ] s01 — Les mots croisés : reprise du pilote avec les LoRA, si le rendu a changé
- [ ] s02 — titre après découpage
  - [ ] `plans.json`
  - [ ] Voix
  - [ ] Animatic → validation
  - [ ] Images clés → choix
  - [ ] Mouvement
  - [ ] Ajout à la timeline

## Phase 7 — Finition et publication

Terminée quand l'épisode est exporté, revu en entier, et que le bilan est écrit.

- [ ] Montage complet dans Kdenlive : le rythme des vannes, la coupure du milieu
- [ ] Musique et bruitages : la broche, la plaque chaude, la pluie, le tram
- [ ] Mixage des voix à des niveaux homogènes
- [ ] Cartons texte façon Eva pour les chiffres clés
- [ ] Générique de début et de fin
- [ ] Visionnage complet, puis corrections
- [ ] Vérifier les licences des modèles utilisés (`modeles.yaml`)
- [ ] Vérifier les règles actuelles de YouTube sur les contenus générés par IA
- [ ] Export final
- [ ] Mettre à jour `ecriture/continuite.md` et `journal.md`, poser le tag `ep01-final`
- [ ] Décider : publier tout de suite, ou attendre d'avoir trois ou quatre épisodes d'avance
