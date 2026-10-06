# Inventaire des images — épisode 1

Liste établie pour « Le Miroir », la partie 1 du texte du CERN. Une case = une image validée, rangée au chemin indiqué. Claude Code coche une case dès que le fichier existe à ce chemin. Si le contenu de l'épisode 1 change, il met la liste à jour.

Les chemins partent de `image/`. Lumière de tout l'épisode : le matin, avec du soleil sur la vitrine.

## Règles pour ChatGPT

- Pars toujours de l'image maître du perso : donne-la à ChatGPT et demande une seule vue à la fois.
- Fiches persos sur fond neutre, sous la même lumière.
- Expressions : même cadrage et même pose, seul le visage change. C'est ce qui permet les transitions d'une expression à l'autre.
- Décors vides, sans persos, un par axe de caméra.
- Vérifie les détails asymétriques sur chaque image : le côté rasé de Maëlle, sa cicatrice, sa bague.
- Pas de texte dans les décors, sauf le menu. Les plans avec du texte restent des plans fixes.
- La rotation (trois-quarts, profil, dos) peut aussi se générer avec AniSora depuis l'image de face, et les bouches en inpainting local : ça économise des images ChatGPT.
- Seules les images validées entrent dans le repo. Le reste va dans `explorations/` ou sur le disque externe.

Noms communs à tous les persos :
- Rotation : `references/face_v1.png`, `trois-quarts_v1.png`, `profil_v1.png`, `dos_v1.png`, `pied_v1.png` (en pied).
- Expressions de base : `expressions/neutre_v1.png`, `joie_v1.png`, `colere_v1.png`, `surprise_v1.png`, `gene_v1.png`.
- Bouches : `bouches/face_fermee_v1.png`, `face_mi-ouverte_v1.png`, `face_ouverte_v1.png`, puis les trois mêmes en `trois-quarts_…`.

## 1. Pilote — en premier

### Sky — `persos/sky/`

- [ ] `references/master_v1.png` : image maître (training noir, chemise blanche à fleurs de lys, yeux bleus)
- [ ] Rotation
- [ ] Expressions de base
- [ ] `expressions/le-sourire_v1.png` : yeux sans reflet, joues plates, seule la bouche bouge
- [ ] `expressions/rire-degenere_v1.png` : la grimace façon Tanya
- [ ] `expressions/regard-vide_v1.png` : le mode silence, le regard qui part
- [ ] `expressions/blemit_v1.png` : « grève un mois »
- [ ] Bouches de face
- [ ] Bouches de trois-quarts
- [ ] Bouches du sourire : `bouches/sourire_ferme_v1.png`, `sourire_grimace_v1.png`, `sourire_rire_v1.png`

### Patrick — `persos/patrick/`

- [ ] `references/master_v1.png` : image maître
- [ ] Rotation
- [ ] Expressions de base
- [ ] `expressions/sourcil-millimetre_v1.png` : le sourcil qui monte d'un millimètre
- [ ] `expressions/sourire-rare_v1.png`
- [ ] `expressions/mains-qui-tremblent_v1.png` : sur sa tasse
- [ ] Bouches de face
- [ ] Bouches de trois-quarts

### Mohamed — `persos/mohamed/` (ou `mehmet/`, selon le canon)

- [ ] `references/master_v1.png` : image maître
- [ ] Rotation
- [ ] Expressions de base
- [ ] `expressions/essuie-le-comptoir_v1.png` : sans lever les yeux
- [ ] `expressions/haussement-epaules_v1.png`
- [ ] `expressions/sourire-client_v1.png`
- [ ] Bouches de face
- [ ] Bouches de trois-quarts

### Décors du pilote — `decors/kebab/`

- [ ] `table-du-fond/fond_v1.png` : la banquette, la table bancale, le grand miroir derrière
- [ ] `comptoir/fond_v1.png` : le comptoir, la broche, le menu, l'horloge

### Accessoires du pilote — `accessoires/`

- [ ] `grille-mots-croises_v1.png` : la grille et le stylo plume, en gros plan
- [ ] `tasse-patrick_v1.png` : la tasse en porcelaine et la théière
- [ ] `galette_v1.png` : la galette poulet harissa, elle revient dans chaque épisode

## 2. Le reste de l'épisode 1

### Maëlle — `persos/maelle/`

- [x] `references/master_v1.png` : image maître
- [ ] Rotation
- [ ] Expressions de base
- [ ] `expressions/regard-qui-tue_v1.png`
- [ ] `expressions/rougeur_v1.png` : elle rougit malgré elle
- [ ] `expressions/bras-croises_v1.png` : le contrôle
- [ ] Bouches de face
- [ ] Bouches de trois-quarts

### Daria — `persos/daria/`

- [ ] `references/master_v1.png` : image maître
- [ ] Rotation
- [ ] Expressions de base
- [ ] `expressions/rougit_v1.png` : jusqu'aux oreilles
- [ ] `expressions/blanche_v1.png` : terrifiée
- [ ] `expressions/collee-au-miroir_v1.png` : le nez à dix centimètres du miroir
- [ ] Bouches de face
- [ ] Bouches de trois-quarts

### Théo — `persos/theo/`

- [ ] `references/master_v1.png` : image maître
- [ ] Rotation
- [ ] Expressions de base
- [ ] `expressions/bouche-pleine_v1.png` : des frites
- [ ] `expressions/panique_v1.png` : « pas le sourire »
- [ ] `expressions/mains-sous-la-table_v1.png`
- [ ] Bouches de face
- [ ] Bouches de trois-quarts

### Seb — `persos/seb/`

- [ ] `references/master_v1.png` : image maître
- [ ] Rotation
- [ ] Expressions de base
- [ ] `expressions/tete-dans-les-mains_v1.png` : « oh non »
- [ ] `expressions/recul_v1.png` : il voit le sourire
- [ ] `expressions/fige_v1.png` : devant sa galette intacte
- [ ] Bouches de face
- [ ] Bouches de trois-quarts

### Nath — `persos/nath/`

- [ ] `references/master_v1.png` : image maître
- [ ] Rotation
- [ ] Expressions de base
- [ ] `expressions/pose-le-stylo_v1.png` : et lève les yeux
- [ ] `expressions/sourcil-leve_v1.png` : « t'es sûr ? »
- [ ] `expressions/calcul_v1.png` : le stylo qui court
- [ ] Bouches de face
- [ ] Bouches de trois-quarts

### Les chats

- [ ] Grep (`persos/grep/`) : `references/master_v1.png`, `face_v1.png`, `profil_v1.png`, gris tigré aux yeux jaunes
- [ ] Grep : `expressions/dans-le-sac_v1.png`, il sort la tête du sac de Daria
- [ ] Nmap (`persos/nmap/`) : `references/master_v1.png`, `face_v1.png`, `profil_v1.png`, design à définir (la bible ne le décrit pas)

### Décors — `decors/kebab/`

Axes provisoires, à valider avec le plan du kebab (phase 2 de `PLAN.md`).

- [ ] `exterieur/fond_v1.png` : la façade, deux étages, le kebab au rez-de-chaussée (dépend du canon : Annemasse ou Clichy)
- [ ] `salle/fond_v1.png` : la salle en vue large
- [ ] `contrechamp/fond_v1.png` : depuis la banquette, vers le comptoir et la vitrine
- [ ] `escalier/fond_v1.png` : le pied de l'escalier, pour les entrées
- [ ] `miroir/fond_v1.png` : le grand miroir en gros plan, vierge
- [ ] `vitrine/fond_v1.png` : la vitrine vue de l'intérieur, la rue et le tram

### Accessoires — `accessoires/`

- [ ] `telephone_v1.png` : le téléphone chiffré, posé sur la sauce
- [ ] `marqueur_v1.png`
- [ ] `laptop-sky_v1.png` : son portable
- [ ] `dessins-miroir_v1.png` : les deux dessins (la balle de face, la balle de côté), sur fond transparent pour les poser sur le miroir

### Gabarits — `gabarits/`

Faits en code par Claude Code, pas dans ChatGPT.

- [ ] `sms_v1.png` : le carton SMS, un seul style pour tous les messages
- [ ] `chiffres_v1.png` : le carton des chiffres clés, façon Eva

Léa et Vincent n'apparaissent pas à l'écran dans « Le Miroir » : leurs images viendront plus tard.
