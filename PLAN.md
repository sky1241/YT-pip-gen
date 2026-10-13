# Kebab Datastream — Checklist épisode 1

Version du 6 octobre 2026. C'est ce fichier qui fait foi : on coche ici, plus dans le doc claude.ai.

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
- [ ] Choisir la machine de production : aucune ne fait tourner la vidéo en l'état, voir `CLAUDE.md` > À trancher
- [x] Préparer le disque externe (`sorties/`, `modeles/`) et noter ses chemins dans `config.yaml`
- [x] Vérifier qu'aucune variable `ANTHROPIC_API_KEY` ne traîne sur la machine
- [ ] Installer Python (venv), ffmpeg et ComfyUI, en espace utilisateur sur la Debian sans sudo
- [ ] Générer une première image dans ComfyUI
- [ ] Installer Kdenlive (AppImage)
- [ ] Installer Qwen3-TTS et générer une phrase test
- [ ] Tester AniSora sur ta carte (la version 12 Go si besoin) : un clip de 5 secondes depuis une image

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
- [ ] Trancher les écarts entre `bible-ecriture.md` et la bible ou le texte : le couple (« Sky = soumis content »), Mehmet à Istanbul ou Mohamed à Alger, Sky à 87 ou 92 kg, Yamauchi ou Asai, l'explication des langues que `corrections-cern.md` remplace
- [ ] Fact-check final : chaque chiffre sourcé et daté, chaque comparaison faite sur la même base
- [ ] Lire l'épisode à voix haute, chrono en main : viser 15 minutes
- [ ] Déposer l'épisode dans `ecriture/episodes/ep01/episode.md`
- [ ] Remplir `ecriture/continuite.md` : running gags et leur phase, boucles ouvertes, qui sait quoi
- [ ] Poser le tag `ep01-v1`

## Phase 2 — Direction artistique

Terminée quand `image/style.md` est validé et que le kebab a son plan d'axes de caméra.

- [x] Image maître de Maëlle
- [ ] Décider si le rendu de Maëlle devient la référence de style de toute la série
- [ ] Explorer le style dans ChatGPT : une vue large du kebab et Sky, dans le même rendu
- [ ] Écrire `image/style.md` : mots-clés de prompt, palette, 3 à 5 images de référence
- [ ] Dessiner le plan du kebab vu de dessus : tables, comptoir, broche, miroir, escalier, vitrine
- [ ] Lister les 6 à 8 axes de caméra et qui s'assoit où (Claude peut le préparer depuis le script)
- [ ] Définir les cartons texte façon Eva (chiffres clés) et le carton SMS : police, couleurs, durée à l'écran
- [ ] Tester une première planche de la palette des émotions sur Maëlle, dont l'image maître existe, puis sa découpe en fichiers

## Phase 3 — Pilote d'une minute, à la main

Terminée quand la minute des mots croisés est montée et que le temps passé à chaque étape est noté. Trois persos : Sky, Patrick et Mohamed. Les images à faire sont listées une par une dans `image/INVENTAIRE.md`, section 1.

- [ ] Fiches des trois persos : compléter le look, d'après la liste « à compléter » de chaque fiche (rôle, énergie et signatures sont déjà posés)
- [ ] Image maître de Sky : training noir, chemise blanche à fleurs de lys, baskets, yeux bleus
- [ ] Image maître de Patrick
- [ ] Image maître de Mohamed
- [ ] Expressions du pilote, marquées « · pilote » dans `image/INVENTAIRE.md`, dont le sourire de Sky : yeux sans reflet, joues plates, seule la bouche bouge
- [ ] Bouches fermée, mi-ouverte et ouverte pour les trois
- [ ] Fonds de la table du fond et du comptoir
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

- [ ] Sky
  - [ ] Fiche : compléter le look
  - [ ] Image maître
  - [ ] Rotation : face, trois-quarts, profil, dos, en pied
  - [ ] Palette des émotions de face : les 6 planches
  - [ ] Palette des émotions de trois-quarts : les 6 planches
  - [ ] Signatures : les 9, dont le jeu du sourire
  - [ ] Bouches : les 6 de base et les 6 du sourire (sourire fermé, grimace, rire ouvert, sous les deux angles)
  - [ ] LoRA : passage local, entraînement, test standard
  - [ ] Voix : compléter et valider `audio/voix/sky/`
- [ ] Maëlle
  - [ ] Fiche : compléter le look, dont le côté de chaque détail asymétrique
  - [x] Image maître
  - [ ] Rotation : face, trois-quarts, profil, dos, en pied
  - [ ] Palette des émotions : les 6 planches
  - [ ] Signatures : les 4
  - [ ] Bouches : les 6, taches de rousseur simplifiées
  - [ ] LoRA : passage local, entraînement sans retournement horizontal, test standard
  - [ ] Voix : compléter et valider `audio/voix/maelle/`
- [ ] Patrick
  - [ ] Fiche : compléter le look
  - [ ] Image maître
  - [ ] Rotation : face, trois-quarts, profil, dos, en pied
  - [ ] Palette des émotions : les 6 planches
  - [ ] Signatures : les 5
  - [ ] Bouches : les 6
  - [ ] LoRA : passage local, entraînement, test standard
  - [ ] Voix : compléter et valider `audio/voix/patrick/`
- [ ] Mohamed
  - [ ] Fiche : trancher le canon (Mohamed ou Mehmet), puis compléter le look
  - [ ] Image maître
  - [ ] Rotation : face, trois-quarts, profil, dos, en pied
  - [ ] Palette des émotions : les 6 planches
  - [ ] Signatures : les 3
  - [ ] Bouches : les 6
  - [ ] LoRA : passage local, entraînement, test standard
  - [ ] Voix : compléter et valider `audio/voix/mohamed/`
- [ ] Seb
  - [ ] Fiche : compléter le look, dont le costard
  - [ ] Image maître
  - [ ] Rotation : face, trois-quarts, profil, dos, en pied
  - [ ] Palette des émotions : les 6 planches
  - [ ] Signatures : les 3
  - [ ] Bouches : les 6
  - [ ] LoRA : passage local, entraînement, test standard
  - [ ] Voix : compléter et valider `audio/voix/seb/`
- [ ] Nath
  - [ ] Fiche : compléter le look
  - [ ] Image maître
  - [ ] Rotation : face, trois-quarts, profil, dos, en pied
  - [ ] Palette des émotions : les 6 planches
  - [ ] Signatures : les 4
  - [ ] Bouches : les 6
  - [ ] LoRA : passage local, entraînement, test standard
  - [ ] Voix : compléter et valider `audio/voix/nath/`
- [ ] Théo
  - [ ] Fiche : compléter le look
  - [ ] Image maître
  - [ ] Rotation : face, trois-quarts, profil, dos, en pied
  - [ ] Palette des émotions : les 6 planches
  - [ ] Signatures : les 3
  - [ ] Bouches : les 6
  - [ ] LoRA : passage local, entraînement, test standard
  - [ ] Voix : compléter et valider `audio/voix/theo/`
- [ ] Daria
  - [ ] Fiche : compléter le look
  - [ ] Image maître
  - [ ] Rotation : face, trois-quarts, profil, dos, en pied
  - [ ] Palette des émotions : les 6 planches
  - [ ] Signatures : les 4
  - [ ] Bouches : les 6
  - [ ] LoRA : passage local, entraînement, test standard
  - [ ] Voix : compléter et valider `audio/voix/daria/`
- [ ] Grep, le chat de Daria : fiche (le motif du pelage), image maître, rotation, 2 signatures
- [ ] Nmap, le chat de Sky et Maëlle : fiche (tout le design), image maître, rotation
- [ ] LoRA de style
- [ ] Un fond par axe de caméra du kebab, plus l'escalier
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
