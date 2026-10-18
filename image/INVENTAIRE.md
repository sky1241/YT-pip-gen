# Inventaire des images — épisode 1

Liste établie pour « Le Miroir », la partie 1 du texte du CERN. Une case = une image validée, rangée au chemin indiqué. Claude Code coche une case dès que le fichier existe à ce chemin. Si le contenu de l'épisode 1 change, il met la liste à jour.

Les chemins partent de `image/`. Lumière de tout l'épisode : le matin, avec du soleil sur la vitrine.

## Règles pour ChatGPT

- Pars toujours de l'image maître du perso : donne-la à ChatGPT.
- Une planche par type suffit : la rotation, la palette des émotions (le détail est dans `emotions.md`), les signatures, les bouches. Une grille régulière, des cases de même taille, le même cadrage dans chaque case, un fond neutre, aucun texte. Range la planche dans `persos/<slug>/planches/` : Claude la découpe et nomme les fichiers. Si une case rate, refais cette vue seule.
- Fiches persos sur fond neutre, sous la même lumière.
- Expressions : même cadrage et même pose, seul le visage change. C'est ce qui permet les transitions d'une expression à l'autre.
- Décors vides, sans persos, un par axe de caméra.
- Vérifie les détails asymétriques sur chaque image : le côté rasé de Maëlle, sa cicatrice, sa bague.
- Pas de texte dans les décors, sauf le menu. Les plans avec du texte restent des plans fixes.
- La rotation (trois-quarts, profil, dos) peut aussi se générer avec AniSora depuis l'image de face, et les bouches en inpainting local : ça économise des images ChatGPT.
- Seules les images validées entrent dans le repo. Le reste va dans `explorations/` ou sur le disque externe.

## Ce que chaque perso demande

- **Une image maître**, puis **la rotation** : face, trois-quarts et profil des deux côtés, dos, en pied. Les deux côtés comptent : un perso asymétrique s'entraîne sans retournement horizontal, son LoRA doit voir chacun.
- **En pied et en gestes** : la rotation est en buste, il faut aussi le corps entier et les mains, sinon le LoRA n'apprend que le buste (leçon du premier LoRA de Sky, le 2026-10-15). Quatre planches sur fond gris clair : en pied de face et de trois-quarts des deux côtés, en pied de profil des deux côtés et de dos, trois poses (assis de face, assis de côté, debout accoudé), et six gestes en plan moyen avec ses accessoires (`fiche.json` > `accessoires`). Ici aussi, une case = une planche.
- **La palette des émotions**, la même pour tous : 36 émotions en 6 planches, définies dans [`emotions.md`](emotions.md). Ici, une case = une planche : Claude la découpe en 6 fichiers `expressions/<émotion>_v1.png`. La joie est un vrai sourire ; « le sourire » de Sky est une signature à part.
- **Les signatures** : les expressions que la bible ou le texte décrivent, identiques à chaque fois. Celles marquées « hors Le Miroir » ne servent pas dans cet épisode, mais elles comptent pour le LoRA et pour la suite.
- **Les bouches** : fermée, mi-ouverte, ouverte, de face et de trois-quarts.
- **Sky en a plus**, parce que c'est le protagoniste : sa palette des émotions aussi de trois-quarts, neuf signatures, les bouches du sourire sous les deux angles, et ses gestes aussi de trois-quarts.
- **Les chats** n'ont ni palette des émotions ni bouches : une image maître, la rotation et leurs gags.
- « · pilote » marque ce qu'il faut pour la minute des mots croisés.

Noms des fichiers :
- Rotation : `references/face_v1.png`, `trois-quarts-gauche_v1.png`, `trois-quarts-droit_v1.png`, `profil-gauche_v1.png`, `profil-droit_v1.png`, `dos_v1.png`, `pied_v1.png`. « Gauche » et « droit » désignent le côté du perso qu'on voit, pas celui de l'image : `profil-gauche` montre sa joue gauche.
- En pied et poses : `references/pied-face_v1.png`, `pied-trois-quarts-gauche_v1.png`, `pied-trois-quarts-droit_v1.png`, `pied-profil-gauche_v1.png`, `pied-profil-droit_v1.png`, `pied-dos_v1.png`, `assis-face_v1.png`, `assis-cote_v1.png`, `accoude_v1.png`. Gestes : `gestes/<geste>_v1.png`. Planches : `planches/pied-1_v1.png`, `pied-2_v1.png`, `poses_v1.png`, `gestes_v1.png`.
- Expressions : `expressions/<nom>_v1.png` pour la face. De trois-quarts, le nom prend le préfixe `trois-quarts_`.
- Bouches : `bouches/<angle>_<forme>_v1.png`, l'angle étant `face` ou `trois-quarts`.
- Planches de la palette : `planches/emotions-<n>_v1.png`, découpées en `expressions/<fichier>_v1.png` avec les noms de `emotions.md`.
- Les autres planches : `planches/rotation_v1.png`, `planches/signatures_v1.png` et `planches/bouches_v1.png`, découpées en `references/`, `expressions/` et `bouches/`.

## 1. Pilote — en premier

### Sky — `persos/sky/`

La série 1, faite avec la monture argentée, est archivée sur le disque externe : `<sorties_root>/persos/sky/archive_serie-1_2026-10-14/`. La série 2 repart de l'image maître v3, dans une nouvelle conversation ChatGPT.

- [x] `references/master_v1.png` : l'image maître de départ (chemise blanche à lys, training noir, lunettes aviateur, œil gauche aveugle), monture argentée : gardée comme historique
- [x] `references/master_v2.png` : la même, monture plaquée or, avec des taches sous les verres et un trait entre les sourcils
- [x] `references/master_v3.png` : la référence de la série 2 : ni trait ni taches, barbe de 3 jours · pilote

**Rotation**
- [x] `references/face_v1.png`
- [x] `references/trois-quarts-gauche_v1.png`
- [x] `references/trois-quarts-droit_v1.png`
- [x] `references/profil-gauche_v1.png`
- [x] `references/profil-droit_v1.png`
- [x] `references/dos_v1.png`
- [x] `references/pied_v1.png`

**En pied et en gestes** (pour son LoRA)
- [x] `planches/pied-1_v1.png` : en pied, de face et de trois-quarts des deux côtés
- [x] `planches/pied-2_v1.png` : en pied, de profil des deux côtés et de dos
- [x] `planches/poses_v1.png` : assis de face, assis de côté, debout accoudé
- [x] `planches/gestes_v1.png` : il mange sa galette, boit son Fanta, la bouche pleine, regarde son téléphone, écrit au marqueur sur une vitre, sur son laptop
- [x] `planches/trois-quarts_gestes_v1.png` : les mêmes gestes de trois-quarts, côté droit (son œil bleu devant)

**Palette des émotions, de face** (l'œil droit garde son reflet, comme en temps normal ; le gauche est aveugle)
- [x] `planches/emotions-1_v1.png` : neutre, joie, tristesse, colère, peur, surprise · pilote
- [x] `planches/emotions-2_v1.png` : dégoût, mépris, rire, pleurs, rage, terreur
- [x] `planches/emotions-3_v1.png` : stupeur, intérêt, concentration, confusion, doute, méfiance
- [x] `planches/emotions-4_v1.png` : gêne, honte, fierté, jalousie, tendresse, désir
- [x] `planches/emotions-5_v1.png` : contentement, soulagement, exaltation, triomphe, émerveillement, déception
- [x] `planches/emotions-6_v1.png` : inquiétude, agacement, malice, ennui, fatigue, douleur
- [x] `planches/reprises_v2.png` : les reprises de face et les deux images du clignement. La malice et le doute n'y sont pas meilleurs : leurs versions 1 restent
- [x] `expressions/clignement-mi-clos_v1.png` : le neutre, les deux yeux mi-clos : le milieu du clignement, pour l'animation (sort des reprises)
- [x] `expressions/clignement_v1.png` : le neutre, les deux yeux fermés : le clignement, pour l'animation (sort des reprises)

**Palette des émotions, de trois-quarts** (côté droit : son œil bleu devant). L'angle vient de `references/trois-quarts-droit_v1.png`, joint au prompt : dans la série 1, sans lui, le trois-quarts était à peine tourné.
- [x] `planches/trois-quarts_emotions-1_v1.png` : neutre, joie, tristesse, colère, peur, surprise
- [x] `planches/trois-quarts_emotions-2_v1.png` : dégoût, mépris, rire, pleurs, rage, terreur
- [x] `planches/trois-quarts_emotions-3_v1.png` : stupeur, intérêt, concentration, confusion, doute, méfiance
- [x] `planches/trois-quarts_emotions-4_v1.png` : gêne, honte, fierté, jalousie, tendresse, désir
- [x] `planches/trois-quarts_emotions-5_v1.png` : contentement, soulagement, exaltation, triomphe, émerveillement, déception
- [x] `planches/trois-quarts_emotions-6_v1.png` : inquiétude, agacement, malice, ennui, fatigue, douleur
- [x] `planches/trois-quarts_retouche_v2.png` : la retouche de trois-quarts : le rire et le soulagement ferment l'œil aveugle, la fatigue ne garde qu'une bague. Le triomphe garde sa v1 : la retouche lui a fermé l'œil aveugle (un clin d'œil)

**Signatures**
- [x] `expressions/regard-plafond_v1.png` : « Mâche. Regarde le plafond. », juste avant « merde » · pilote
- [x] `expressions/bouche-pleine_v1.png` : « Bouche pleine. Pas impressionné. » · pilote
- [x] `expressions/sourcil-leve_v2.png` : il regarde Daria en levant un sourcil
- [x] `expressions/haussement-epaules_v1.png` : « comme si elle venait de lui dire qu'il avait du sel sur la table »
- [x] `expressions/blemit_v1.png` : « grève un mois », il avale sa bouchée d'un coup et pose les mains à plat
- [x] `expressions/regard-vide_v1.png` : le mode silence, les yeux fixent un point que personne voit
- [x] `expressions/le-sourire_v2.png` : le prédateur. L'œil droit perd son reflet, joues plates, seule la bouche bouge, une ombre sur le haut du visage, la pupille minuscule, des crocs (la version « monstre », validée le 2026-10-15) · pilote
- [x] `expressions/trois-quarts_le-sourire_v2.png` : le même, de trois-quarts
- [x] `expressions/rire-degenere_v2.png` : le rire qui monte du ventre, des crocs, l'œil droit exorbité, quand il dessine sur le miroir
- [x] `expressions/trois-quarts_rire-degenere_v1.png` : le même rire, de trois-quarts : il dessine sur le miroir en riant
- [x] `expressions/cherche-feu-vert_v2.png` : il regarde Maëlle, « le regard du mec qui vérifie »
- [x] `planches/retouche-1_v2.png` : la retouche : le sourcil levé, le feu vert (l'œil aveugle avait un iris), et le doute de la palette

**Bouches**
- [x] `bouches/face_fermee_v1.png` · pilote
- [x] `bouches/face_mi-ouverte_v1.png` · pilote
- [x] `bouches/face_ouverte_v1.png` · pilote
- [x] `bouches/trois-quarts_fermee_v1.png`
- [x] `bouches/trois-quarts_mi-ouverte_v1.png`
- [x] `bouches/trois-quarts_ouverte_v1.png`
- [x] `bouches/face_sourire-ferme_v1.png`
- [x] `bouches/face_sourire-grimace_v1.png`
- [x] `bouches/face_sourire-rire_v1.png`
- [x] `bouches/trois-quarts_sourire-ferme_v1.png`
- [x] `bouches/trois-quarts_sourire-grimace_v1.png`
- [x] `bouches/trois-quarts_sourire-rire_v1.png`

### Patrick — `persos/patrick/`

- [ ] `references/master_v1.png` : image maître · pilote

**Rotation**
- [ ] `references/face_v1.png`
- [ ] `references/trois-quarts-gauche_v1.png`
- [ ] `references/trois-quarts-droit_v1.png`
- [ ] `references/profil-gauche_v1.png`
- [ ] `references/profil-droit_v1.png`
- [ ] `references/dos_v1.png`
- [ ] `references/pied_v1.png`

**En pied et en gestes** (pour son LoRA)
- [ ] `planches/pied-1_v1.png` : en pied, de face et de trois-quarts des deux côtés
- [ ] `planches/pied-2_v1.png` : en pied, de profil des deux côtés et de dos
- [ ] `planches/poses_v1.png` : assis de face, assis de côté, debout accoudé
- [ ] `planches/gestes_v1.png` : six gestes avec ses accessoires (`fiche.json` > `accessoires`), à fixer avec l'auteur avant les prompts

**Palette des émotions** (les 36 de `emotions.md`, en 6 planches)
- [ ] `planches/emotions-1_v1.png` : neutre, joie, tristesse, colère, peur, surprise · pilote
- [ ] `planches/emotions-2_v1.png` : dégoût, mépris, rire, pleurs, rage, terreur
- [ ] `planches/emotions-3_v1.png` : stupeur, intérêt, concentration, confusion, doute, méfiance
- [ ] `planches/emotions-4_v1.png` : gêne, honte, fierté, jalousie, tendresse, désir
- [ ] `planches/emotions-5_v1.png` : contentement, soulagement, exaltation, triomphe, émerveillement, déception
- [ ] `planches/emotions-6_v1.png` : inquiétude, agacement, malice, ennui, fatigue, douleur

**Signatures**
- [ ] `expressions/sans-lever-les-yeux_v1.png` : le regard sur la grille, le stylo plume en l'air · pilote
- [ ] `expressions/fronce-les-sourcils_v1.png` : sur son COBOL, « depuis 3 jours »
- [ ] `expressions/sourcil-millimetre_v1.png` : le sourcil qui monte d'un millimètre
- [ ] `expressions/mains-qui-tremblent_v1.png` : sur sa tasse, quand Sky dit qu'il a la théorie
- [ ] `expressions/sourire-rare_v1.png` : le vrai sourire, une fois par mois (hors Le Miroir)

**Bouches**
- [ ] `bouches/face_fermee_v1.png` · pilote
- [ ] `bouches/face_mi-ouverte_v1.png` · pilote
- [ ] `bouches/face_ouverte_v1.png` · pilote
- [ ] `bouches/trois-quarts_fermee_v1.png`
- [ ] `bouches/trois-quarts_mi-ouverte_v1.png`
- [ ] `bouches/trois-quarts_ouverte_v1.png`

### Mohamed — `persos/mohamed/` (ou `mehmet/`, selon le canon)

- [ ] `references/master_v1.png` : image maître · pilote

**Rotation**
- [ ] `references/face_v1.png`
- [ ] `references/trois-quarts-gauche_v1.png`
- [ ] `references/trois-quarts-droit_v1.png`
- [ ] `references/profil-gauche_v1.png`
- [ ] `references/profil-droit_v1.png`
- [ ] `references/dos_v1.png`
- [ ] `references/pied_v1.png`

**En pied et en gestes** (pour son LoRA)
- [ ] `planches/pied-1_v1.png` : en pied, de face et de trois-quarts des deux côtés
- [ ] `planches/pied-2_v1.png` : en pied, de profil des deux côtés et de dos
- [ ] `planches/poses_v1.png` : assis de face, assis de côté, debout accoudé
- [ ] `planches/gestes_v1.png` : six gestes avec ses accessoires (`fiche.json` > `accessoires`), à fixer avec l'auteur avant les prompts

**Palette des émotions** (les 36 de `emotions.md`, en 6 planches)
- [ ] `planches/emotions-1_v1.png` : neutre, joie, tristesse, colère, peur, surprise · pilote
- [ ] `planches/emotions-2_v1.png` : dégoût, mépris, rire, pleurs, rage, terreur
- [ ] `planches/emotions-3_v1.png` : stupeur, intérêt, concentration, confusion, doute, méfiance
- [ ] `planches/emotions-4_v1.png` : gêne, honte, fierté, jalousie, tendresse, désir
- [ ] `planches/emotions-5_v1.png` : contentement, soulagement, exaltation, triomphe, émerveillement, déception
- [ ] `planches/emotions-6_v1.png` : inquiétude, agacement, malice, ennui, fatigue, douleur

**Signatures**
- [ ] `expressions/essuie-le-comptoir_v1.png` : sans lever les yeux · pilote
- [ ] `expressions/haussement-epaules_v1.png` : quand Patrick lui dit qu'il fait de la science
- [ ] `expressions/tete-penchee_v1.png` : devant le miroir, « C'est plus joli que d'habitude »

**Bouches**
- [ ] `bouches/face_fermee_v1.png` · pilote
- [ ] `bouches/face_mi-ouverte_v1.png` · pilote
- [ ] `bouches/face_ouverte_v1.png` · pilote
- [ ] `bouches/trois-quarts_fermee_v1.png`
- [ ] `bouches/trois-quarts_mi-ouverte_v1.png`
- [ ] `bouches/trois-quarts_ouverte_v1.png`

### Décors du pilote — `decors/kebab/`

Les axes et leurs numéros : `decors/kebab/axes.md` et le plan `decors/kebab/plan-axes_v1.png`.

- [x] `plan_v5.png` : le plan en code, validé par l'auteur ; `plan-axes_v5.png` : les 25 axes
- [x] `plan-peint_v2.png` : le plan v5 peint, vu exactement d'en haut : la base fixe du kebab
- [x] `exterieur/fond_v1.png` (1)
- [x] `exterieur/fond_ferme_v1.png` (1) : la devanture fermée, la porte au milieu, même lumière ; puis la pluie et la nuit à partir d'elle : la façade, deux étages, le kebab au rez-de-chaussée, Datastream au premier, la rue d'Annemasse et le tram
- [x] `exterieur/fond_pluie_v1.png` (1) : la devanture fermée sous la pluie (Navier-Stokes)
- [x] `exterieur/fond_nuit_v1.png` (1) : la devanture fermée, la nuit
- [x] `entree/fond_v1.png` (2) : depuis le trottoir, toute la salle
- [x] `table-du-fond/fond_v1.png` (6) : la table de Sky dans l'angle, la banquette, le grand miroir au-dessus, la plante de l'angle
- [x] `table-du-fond-contrechamp/fond_v1.png` (7) : depuis la banquette, les deux chaises, la salle, la rue
- [x] `comptoir/fond_v1.png` (8) : la caisse, les salades, la broche, l'horloge, le menu
- [x] `pied-de-l-escalier/fond_v1.png` (10) : les premières marches, pour les descentes
- [x] `table-vue-de-dessus/fond_v1.png` (17) : le dessus de la table de Sky, pour les inserts
- [x] `bout-de-table/fond_v1.png` (20) : Patrick de face, au bout de la table, la rampe et l'escalier derrière lui
- [x] `depuis-patrick/fond_v1.png` (21) : Sky et Maëlle de profil sur la banquette, le miroir au-dessus

Chaque fond a aussi sa version pluie et sa version nuit, dans le même cadrage (`axes.md`, « Les trois lumières ») : `<dossier>/fond_pluie_v1.png` et `<dossier>/fond_nuit_v1.png`. Leurs cases s'ajoutent ici quand le fond de jour est fait.

### Accessoires du pilote — `accessoires/`

- [ ] `grille-mots-croises_v1.png` : la grille et le stylo plume, en gros plan
- [ ] `tasse-patrick_v1.png` : la tasse en porcelaine et la théière
- [ ] `galette_v1.png` : la galette poulet harissa, elle revient dans chaque épisode
- [ ] `plateau-frites_v1.png` : le plateau de frites de Sky, posé à côté du laptop

## 2. Le reste de l'épisode 1

### Maëlle — `persos/maelle/`

- [x] `references/master_v1.png` : image maître

**Rotation**
- [x] `references/face_v1.png`
- [x] `references/trois-quarts-gauche_v1.png`
- [x] `references/trois-quarts-droit_v1.png`
- [x] `references/profil-gauche_v1.png`
- [x] `references/profil-droit_v1.png`
- [x] `references/dos_v1.png`
- [x] `references/pied_v1.png`

**En pied et en gestes** (pour son LoRA)
- [ ] `planches/pied-1_v1.png` : en pied, de face et de trois-quarts des deux côtés
- [ ] `planches/pied-2_v1.png` : en pied, de profil des deux côtés et de dos
- [ ] `planches/poses_v1.png` : assis de face, assis de côté, debout accoudé
- [ ] `planches/gestes_v1.png` : elle boit son café, tient sa tasse à deux mains, bras croisés, ramasse une serviette sur la table, regarde son téléphone, sur un laptop

**Palette des émotions, de trois-quarts** (les 36 de `emotions.md`, sous l'angle de son image maître, côté gauche)
- [x] `planches/trois-quarts_emotions-1_v1.png` : neutre, joie, tristesse, colère, peur, surprise
- [x] `planches/trois-quarts_emotions-2_v1.png` : dégoût, mépris, rire, pleurs, rage, terreur
- [x] `planches/trois-quarts_emotions-3_v1.png` : stupeur, intérêt, concentration, confusion, doute, méfiance
- [x] `planches/trois-quarts_emotions-4_v1.png` : gêne, honte, fierté, jalousie, tendresse, désir
- [x] `planches/trois-quarts_emotions-5_v1.png` : contentement, soulagement, exaltation, triomphe, émerveillement, déception
- [x] `planches/trois-quarts_emotions-6_v1.png` : inquiétude, agacement, malice, ennui, fatigue, douleur
- [x] `planches/trois-quarts_reprises_v2.png` : joie, stupeur, concentration, soulagement, émerveillement, malice, en version 2 (le soulagement reste à refaire seul)
- [x] `expressions/trois-quarts_soulagement_v3.png` : le soulagement, seul, bouche ouverte qui soupire

**Signatures**
- [x] `expressions/regard-qui-tue_v1.png` : « T'as compris quoi exactement Daria. »
- [x] `expressions/bras-croises_v1.png` : elle s'adosse et s'efface quand le sourire arrive
- [x] `expressions/mode-ciso_v1.png` : « C'est pas la femme qui parle », la voix basse quand elle classifie le miroir
- [x] `expressions/rougeur_v1.png` : elle rougit malgré elle (hors Le Miroir)

**Bouches**
- [x] `bouches/face_fermee_v1.png`
- [x] `bouches/face_mi-ouverte_v1.png`
- [x] `bouches/face_ouverte_v1.png`
- [x] `bouches/trois-quarts_fermee_v1.png`
- [x] `bouches/trois-quarts_mi-ouverte_v1.png`
- [x] `bouches/trois-quarts_ouverte_v1.png`

### Daria — `persos/daria/`

- [ ] `references/master_v1.png` : image maître

**Rotation**
- [ ] `references/face_v1.png`
- [ ] `references/trois-quarts-gauche_v1.png`
- [ ] `references/trois-quarts-droit_v1.png`
- [ ] `references/profil-gauche_v1.png`
- [ ] `references/profil-droit_v1.png`
- [ ] `references/dos_v1.png`
- [ ] `references/pied_v1.png`

**En pied et en gestes** (pour son LoRA)
- [ ] `planches/pied-1_v1.png` : en pied, de face et de trois-quarts des deux côtés
- [ ] `planches/pied-2_v1.png` : en pied, de profil des deux côtés et de dos
- [ ] `planches/poses_v1.png` : assis de face, assis de côté, debout accoudé
- [ ] `planches/gestes_v1.png` : six gestes avec ses accessoires (`fiche.json` > `accessoires`), à fixer avec l'auteur avant les prompts

**Palette des émotions** (les 36 de `emotions.md`, en 6 planches)
- [ ] `planches/emotions-1_v1.png` : neutre, joie, tristesse, colère, peur, surprise
- [ ] `planches/emotions-2_v1.png` : dégoût, mépris, rire, pleurs, rage, terreur
- [ ] `planches/emotions-3_v1.png` : stupeur, intérêt, concentration, confusion, doute, méfiance
- [ ] `planches/emotions-4_v1.png` : gêne, honte, fierté, jalousie, tendresse, désir
- [ ] `planches/emotions-5_v1.png` : contentement, soulagement, exaltation, triomphe, émerveillement, déception
- [ ] `planches/emotions-6_v1.png` : inquiétude, agacement, malice, ennui, fatigue, douleur

**Signatures**
- [ ] `expressions/incredule_v1.png` : « Elle fixe la galette. Puis Sky. Puis la galette. »
- [ ] `expressions/blanche_v1.png` : terrifiée, « Tu l'*as*. »
- [ ] `expressions/collee-au-miroir_v1.png` : elle s'approche du miroir et regarde les dessins
- [ ] `expressions/rougit_v1.png` : jusqu'aux oreilles (hors Le Miroir)

**Bouches**
- [ ] `bouches/face_fermee_v1.png`
- [ ] `bouches/face_mi-ouverte_v1.png`
- [ ] `bouches/face_ouverte_v1.png`
- [ ] `bouches/trois-quarts_fermee_v1.png`
- [ ] `bouches/trois-quarts_mi-ouverte_v1.png`
- [ ] `bouches/trois-quarts_ouverte_v1.png`

### Théo — `persos/theo/`

- [ ] `references/master_v1.png` : image maître

**Rotation**
- [ ] `references/face_v1.png`
- [ ] `references/trois-quarts-gauche_v1.png`
- [ ] `references/trois-quarts-droit_v1.png`
- [ ] `references/profil-gauche_v1.png`
- [ ] `references/profil-droit_v1.png`
- [ ] `references/dos_v1.png`
- [ ] `references/pied_v1.png`

**En pied et en gestes** (pour son LoRA)
- [ ] `planches/pied-1_v1.png` : en pied, de face et de trois-quarts des deux côtés
- [ ] `planches/pied-2_v1.png` : en pied, de profil des deux côtés et de dos
- [ ] `planches/poses_v1.png` : assis de face, assis de côté, debout accoudé
- [ ] `planches/gestes_v1.png` : six gestes avec ses accessoires (`fiche.json` > `accessoires`), à fixer avec l'auteur avant les prompts

**Palette des émotions** (les 36 de `emotions.md`, en 6 planches)
- [ ] `planches/emotions-1_v1.png` : neutre, joie, tristesse, colère, peur, surprise
- [ ] `planches/emotions-2_v1.png` : dégoût, mépris, rire, pleurs, rage, terreur
- [ ] `planches/emotions-3_v1.png` : stupeur, intérêt, concentration, confusion, doute, méfiance
- [ ] `planches/emotions-4_v1.png` : gêne, honte, fierté, jalousie, tendresse, désir
- [ ] `planches/emotions-5_v1.png` : contentement, soulagement, exaltation, triomphe, émerveillement, déception
- [ ] `planches/emotions-6_v1.png` : inquiétude, agacement, malice, ennui, fatigue, douleur

**Signatures**
- [ ] `expressions/bouche-pleine_v1.png` : il parle avec des frites dans la bouche
- [ ] `expressions/panique_v1.png` : « Oh non. Non non non. Pas le sourire. »
- [ ] `expressions/mains-sous-la-table_v1.png` : elles tremblent à « 600 millions le gramme » (hors Le Miroir, c'est dans le call)

**Bouches**
- [ ] `bouches/face_fermee_v1.png`
- [ ] `bouches/face_mi-ouverte_v1.png`
- [ ] `bouches/face_ouverte_v1.png`
- [ ] `bouches/trois-quarts_fermee_v1.png`
- [ ] `bouches/trois-quarts_mi-ouverte_v1.png`
- [ ] `bouches/trois-quarts_ouverte_v1.png`

### Seb — `persos/seb/`

- [ ] `references/master_v1.png` : image maître, en costard

**Rotation**
- [ ] `references/face_v1.png`
- [ ] `references/trois-quarts-gauche_v1.png`
- [ ] `references/trois-quarts-droit_v1.png`
- [ ] `references/profil-gauche_v1.png`
- [ ] `references/profil-droit_v1.png`
- [ ] `references/dos_v1.png`
- [ ] `references/pied_v1.png`

**En pied et en gestes** (pour son LoRA)
- [ ] `planches/pied-1_v1.png` : en pied, de face et de trois-quarts des deux côtés
- [ ] `planches/pied-2_v1.png` : en pied, de profil des deux côtés et de dos
- [ ] `planches/poses_v1.png` : assis de face, assis de côté, debout accoudé
- [ ] `planches/gestes_v1.png` : six gestes avec ses accessoires (`fiche.json` > `accessoires`), à fixer avec l'auteur avant les prompts

**Palette des émotions** (les 36 de `emotions.md`, en 6 planches)
- [ ] `planches/emotions-1_v1.png` : neutre, joie, tristesse, colère, peur, surprise
- [ ] `planches/emotions-2_v1.png` : dégoût, mépris, rire, pleurs, rage, terreur
- [ ] `planches/emotions-3_v1.png` : stupeur, intérêt, concentration, confusion, doute, méfiance
- [ ] `planches/emotions-4_v1.png` : gêne, honte, fierté, jalousie, tendresse, désir
- [ ] `planches/emotions-5_v1.png` : contentement, soulagement, exaltation, triomphe, émerveillement, déception
- [ ] `planches/emotions-6_v1.png` : inquiétude, agacement, malice, ennui, fatigue, douleur

**Signatures**
- [ ] `expressions/fige_v1.png` : devant sa galette mixte intacte, « Elle sera intacte dans une heure »
- [ ] `expressions/recul_v1.png` : il voit le sourire en premier et recule sur la banquette
- [ ] `expressions/tete-dans-les-mains_v1.png` : « oh non » (hors Le Miroir)

**Bouches**
- [ ] `bouches/face_fermee_v1.png`
- [ ] `bouches/face_mi-ouverte_v1.png`
- [ ] `bouches/face_ouverte_v1.png`
- [ ] `bouches/trois-quarts_fermee_v1.png`
- [ ] `bouches/trois-quarts_mi-ouverte_v1.png`
- [ ] `bouches/trois-quarts_ouverte_v1.png`

### Nath — `persos/nath/`

- [ ] `references/master_v1.png` : image maître

**Rotation**
- [ ] `references/face_v1.png`
- [ ] `references/trois-quarts-gauche_v1.png`
- [ ] `references/trois-quarts-droit_v1.png`
- [ ] `references/profil-gauche_v1.png`
- [ ] `references/profil-droit_v1.png`
- [ ] `references/dos_v1.png`
- [ ] `references/pied_v1.png`

**En pied et en gestes** (pour son LoRA)
- [ ] `planches/pied-1_v1.png` : en pied, de face et de trois-quarts des deux côtés
- [ ] `planches/pied-2_v1.png` : en pied, de profil des deux côtés et de dos
- [ ] `planches/poses_v1.png` : assis de face, assis de côté, debout accoudé
- [ ] `planches/gestes_v1.png` : six gestes avec ses accessoires (`fiche.json` > `accessoires`), à fixer avec l'auteur avant les prompts

**Palette des émotions** (les 36 de `emotions.md`, en 6 planches)
- [ ] `planches/emotions-1_v1.png` : neutre, joie, tristesse, colère, peur, surprise
- [ ] `planches/emotions-2_v1.png` : dégoût, mépris, rire, pleurs, rage, terreur
- [ ] `planches/emotions-3_v1.png` : stupeur, intérêt, concentration, confusion, doute, méfiance
- [ ] `planches/emotions-4_v1.png` : gêne, honte, fierté, jalousie, tendresse, désir
- [ ] `planches/emotions-5_v1.png` : contentement, soulagement, exaltation, triomphe, émerveillement, déception
- [ ] `planches/emotions-6_v1.png` : inquiétude, agacement, malice, ennui, fatigue, douleur

**Signatures**
- [ ] `expressions/plisse-les-yeux_v1.png` : devant les dessins, « Celui de gauche c'est le chaos »
- [ ] `expressions/pose-le-stylo_v1.png` : le stylo immobile, elle lève les yeux
- [ ] `expressions/sourcil-leve_v1.png` : « t'es sûr ? » (hors Le Miroir)
- [ ] `expressions/calcul_v1.png` : le stylo qui court (hors Le Miroir)

**Bouches**
- [ ] `bouches/face_fermee_v1.png`
- [ ] `bouches/face_mi-ouverte_v1.png`
- [ ] `bouches/face_ouverte_v1.png`
- [ ] `bouches/trois-quarts_fermee_v1.png`
- [ ] `bouches/trois-quarts_mi-ouverte_v1.png`
- [ ] `bouches/trois-quarts_ouverte_v1.png`

### Les chats

**Grep — `persos/grep/`** : gris tigré, yeux jaunes, air de propriétaire
- [ ] `references/master_v1.png`
- [ ] `references/face_v1.png`
- [ ] `references/trois-quarts-gauche_v1.png`
- [ ] `references/trois-quarts-droit_v1.png`
- [ ] `references/profil-gauche_v1.png`
- [ ] `references/profil-droit_v1.png`
- [ ] `references/dos_v1.png`
- [ ] `expressions/dans-le-sac_v1.png` : il sort la tête du sac de Daria
- [ ] `expressions/proteste_v1.png` : « Grep tombe. Grep proteste. »

**Nmap — `persos/nmap/`** : design à définir, la bible ne le décrit pas
- [ ] `references/master_v1.png`
- [ ] `references/face_v1.png`
- [ ] `references/trois-quarts-gauche_v1.png`
- [ ] `references/trois-quarts-droit_v1.png`
- [ ] `references/profil-gauche_v1.png`
- [ ] `references/profil-droit_v1.png`
- [ ] `references/dos_v1.png`

### Décors — `decors/kebab/`

Les axes de l'épisode 1, en plus de ceux du pilote (`decors/kebab/axes.md`, à valider par l'auteur).

- [ ] `salle-depuis-le-fond/fond_v1.png` (3) : vers la rue, le contrechamp de l'entrée
- [x] `depuis-le-comptoir/fond_v1.png` (4) : le regard de Mohamed
- [x] `depuis-l-escalier/fond_v1.png` (5) : en plongée, depuis le milieu de l'escalier
- [x] `broche/fond_v1.png` (9) : la broche, le grill, la hotte
- [x] `escalier-vers-datastream/fond_v1.png` (11) : l'escalier et la porte de Datastream en haut
- [x] `miroir/fond_v1.png` (12) : le grand miroir de biais, vierge
- [x] `depuis-le-miroir/fond_v1.png` (13) : la salle vue par Sky qui dessine
- [x] `coin-de-la-banquette/fond_v1.png` (14) : l'angle de la banquette, les plans de groupe
- [x] `devanture/fond_v1.png` (15) : la devanture, les panneaux, le menu plastifié, la rue et le tram
- [x] `horloge/fond_v1.png` (18) : l'horloge au-dessus du comptoir
- [x] `banquette-de-droite/fond_v1.png` (19)
- [x] `banquette-de-droite/fond_ferme_v1.png` (19) : le rideau de verre fermé, même lumière
- [ ] `frigo/fond_v1.png` (16) : le frigo à boissons, si besoin

Comme pour le pilote : la pluie et la nuit de chaque axe s'ajoutent quand son fond de jour est fait.

Les deux axes de la pluie seule, le rideau de verre fermé :

- [x] `vitrine-fermee/fond_pluie_v1.png` (22) : de l'intérieur, la pluie sur le verre
- [x] `a-travers-la-vitre/fond_pluie_v1.png` (23) : de la rue, la salle derrière le verre mouillé

La table de Navier-Stokes (la table de devant, à droite) :

- [x] `table-navier-stokes/fond_pluie_v1.png` (24) : la table de Sky dans Navier-Stokes, le rideau fermé, la pluie
- [x] `table-navier-stokes-contrechamp/fond_pluie_v1.png` (25)

### Accessoires — `accessoires/`

- [ ] `telephone_v1.png` : le téléphone chiffré, posé sur la sauce
- [ ] `marqueur_v1.png`
- [ ] `laptop-sky_v1.png` : son portable
- [ ] `bouteille-fanta_v1.png` : la bouteille de Sky, dans sa main droite au miroir
- [ ] `sac-daria_v1.png` : son sac à dos, Grep dedans
- [ ] `dessins-miroir_v1.png` : les deux dessins (la balle de face, la balle de côté), sur fond transparent pour les poser sur le miroir

### Gabarits — `gabarits/`

Faits en code par Claude Code, pas dans ChatGPT.

- [ ] `sms_v1.png` : le carton SMS, un seul style pour tous les messages
- [ ] `chiffres_v1.png` : le carton des chiffres clés, façon Eva

Léa et Vincent n'apparaissent pas à l'écran dans « Le Miroir » : leurs images viendront plus tard.
