# Le kebab — les prompts ChatGPT

Le décor principal (bible, « La géographie » : le kebab au rez-de-chaussée, le bureau à l'étage, l'escalier entre les deux). Conçu dans ChatGPT, dans le style de la série (`image/style.md`), puis repassé dans le modèle local : aucune image de production ne vient de ChatGPT. Un prompt à la fois, dans une nouvelle conversation ChatGPT réservée au kebab.

Le canon du kebab n'est pas encore tranché (Mohamed à Annemasse ou Mehmet à Clichy, CLAUDE.md). En attendant, la rue derrière la vitrine reste neutre : ni montagne, ni monument, rien de lisible.

| Prompt | Image | Où la ranger |
|---|---|---|
| KB1 | La maquette : tout le kebab vu de dessus, en coupe, sans personne : supprimée, remplacée par KB2 | (dans l'historique git) |
| KB1 retouches | Le menu, l'escalier ouvert, le miroir fumé, les panneaux, la porte de Datastream, les tables : supprimée, remplacée par KB2 | (dans l'historique git) |
| Plan | Vu de dessus, en code (`pipeline/plan_kebab.py`) : la disposition exacte | `image/decors/kebab/plan_v2.png` (la v1 sans la banquette en L) |
| KB2 | Le plan peint, d'après le plan v2 : remplacé par KB2 v3 | (supprimé) |
| A6 | L'axe 6, d'après le plan v2 : dépassé par le plan v3, supprimé | (supprimé) |
| A7 v2 | L'axe 7 : depuis la place de Sky, vers la rue, la rampe à gauche : **fait** | `image/decors/kebab/table-du-fond-contrechamp/fond_v1.png` |
| A20 | L'axe 20 : Patrick au bout de la table, vu de l'autre bout : **fait** | `image/decors/kebab/bout-de-table/fond_v1.png` |
| A21 | L'axe 21 : depuis la place de Patrick, le long de la table, vers le comptoir : **fait** | `image/decors/kebab/depuis-patrick/fond_v1.png` |
| A8 v3 | L'axe 8 : le comptoir et la cuisine, le mur de face : **fait** (après une retouche) | `image/decors/kebab/comptoir/fond_v1.png` |
| A2 | L'axe 2 : l'entrée, toute la salle depuis le trottoir : **fait** (deux retouches ; l'angle ne convainc pas l'auteur) | `image/decors/kebab/entree/fond_v1.png` |
| A11 | L'axe 11 : du palier, l'escalier qui monte à la porte de Datastream : **fait** (une retouche) | `image/decors/kebab/escalier-vers-datastream/fond_v1.png` |
| A10 | L'axe 10 : le pied de l'escalier, vu de la salle : **fait** | `image/decors/kebab/pied-de-l-escalier/fond_v1.png` |
| A1 | L'axe 1 : l'extérieur, la façade depuis le trottoir d'en face : **fait** (une retouche ; les enseignes en code) | `image/decors/kebab/exterieur/fond_v1.png` |
| A17 | L'axe 17 : la table de Sky vue d'en haut, pour les inserts : **fait** | `image/decors/kebab/table-vue-de-dessus/fond_v1.png` |
| A4 | L'axe 4 : depuis le comptoir, le regard de Mohamed : **fait** (une retouche) | `image/decors/kebab/depuis-le-comptoir/fond_v1.png` |
| A12 | L'axe 12 : le grand miroir de biais : **fait** (une retouche) | `image/decors/kebab/miroir/fond_v1.png` |
| A13 | L'axe 13 : depuis le miroir, la table de Sky en plongée : **fait** (deux retouches) | `image/decors/kebab/depuis-le-miroir/fond_v1.png` |
| A14 | L'axe 14 : l'angle de la banquette, debout : **fait** (la retouche gardée, sans le bout d'escalier) | `image/decors/kebab/coin-de-la-banquette/fond_v1.png` |
| A18 | L'axe 18 : l'horloge, en gros plan : **fait** (les aiguilles en code) | `image/decors/kebab/horloge/fond_v1.png` |
| A9 | L'axe 9 : la broche, de près : **fait** (une retouche) | `image/decors/kebab/broche/fond_v1.png` |
| A15 | L'axe 15 : la devanture vue de dedans, les panneaux repliés : **fait** | `image/decors/kebab/devanture/fond_v1.png` |
| A5 | L'axe 5 : depuis l'escalier, en plongée : **fait** (une retouche) | `image/decors/kebab/depuis-l-escalier/fond_v1.png` |
| A19 | L'axe 19 : le long de la banquette de droite, vers la rue : **fait** | `image/decors/kebab/banquette-de-droite/fond_v1.png` |
| A24 pluie | L'axe 24 : la table de Sky dans Navier-Stokes, rideau fermé, sous la pluie | `image/decors/kebab/table-navier-stokes/fond_pluie_v1.png` |
| KB2 v2 | Le plan peint, d'après le plan v3 : bonne disposition, mais l'escalier sur la rue, la lumière de côté | (supprimé) |
| KB2 v3 | Le plan peint, d'après le plan v5 sans caméras : **la base fixe, validée** | `image/decors/kebab/plan-peint_v2.png` |
| A6 v3 | L'axe 6 : la table de Sky dans l'angle, la banquette, le miroir, la plante : **fait** (la vue en volumes, puis une retouche) | `image/decors/kebab/table-du-fond/fond_v1.png` |

La suite (un fond vide par axe de caméra) s'écrit d'après KB1 et d'après les scènes du texte.

## Prompt KB1 — La maquette du kebab

Joins l'image maître de Sky (`~/Téléchargements/kebab_pour_KB1_style_master-sky-v3.png`), pour le style seulement : son arrière-plan est déjà un kebab.

```
Use the attached image only as a reference for the art style and the light (1990s anime: clean dark outlines, flat cel shading, warm golden morning light, muted warm palette, painted detailed backgrounds), not for the camera angle. Draw a cutaway isometric view, seen from above at about 45 degrees, of the whole interior of a small kebab restaurant, like a dollhouse with the front wall and the ceiling removed, so that the whole floor plan can be read. Landscape format (1536×1024). No people at all. The room is about 6 by 10 metres and contains:
- along one long wall, a counter with a glass display of salads and sauces, and behind it a vertical kebab spit in front of its grill, a cash register and a drinks fridge;
- in a back corner, a staircase going up to an office on the floor above, its first steps visible;
- a large wall mirror, big enough to write on with a marker, on the wall next to the back table;
- four or five simple tables with chairs, and at the back table a long padded bench against the wall;
- on the street side, the shop window and the entrance door, with a plain street outside: no landmark, no mountain, no readable sign;
- lived-in details: a teapot, napkin dispensers, sauce bottles, a plant, a menu board on the wall.
No text, no letters and no logos anywhere, not even on the menu board.
```

À contrôler à la reprise : tous les éléments de la liste (comptoir, broche, escalier, miroir, banquette, vitrine) ; le style et la lumière de l'image maître ; aucune personne ; aucun texte lisible ; un plan qu'on peut lire, pour en tirer les axes de caméra.

Premier essai, le 2026-10-16 (vu sur une capture d'écran, pas rangé) : un plan lisible, mais pas celui de l'auteur, et pas dans notre style.
- **Le rendu** : une image 3D photoréaliste, de nuit, sous des appliques. Ni anime, ni lumière du matin : la vue isométrique tire vers le rendu 3D, le prompt doit dire « 2D, pas de 3D ».
- **Le plan** : la vitrine et la porte devant (porte au centre droit) ; un comptoir en îlot rectangulaire au centre gauche, la caisse au coin avant gauche, loin de la porte, les salades sur la face avant, la broche sous sa hotte sur la face gauche, les plans inox au fond ; une banquette rouge en L le long du mur du fond et du mur gauche, une autre le long du mur droit ; l'escalier le long du mur droit, de l'avant vers le fond ; des cadres, des appliques et des plantes.
- **Ce qui ne va pas pour l'auteur** : des tables presque toutes carrées (il les veut toutes rectangulaires) ; un îlot au lieu d'un comptoir en L ; la caisse loin de l'entrée (il la veut juste en entrant, puis les salades plus loin). Il manque aussi le grand miroir.

## Prompt KB1 v2 — La maquette, avec le plan de l'auteur

Dans la même conversation, avec la même image jointe.

```
Redraw this kebab restaurant cutaway with the following changes. Style first: a flat 2D hand-drawn background painting from a 1990s anime film, in the style of the attached image (clean dark outlines, flat cel shading, muted warm palette, painted details). NOT a 3D render, NOT photorealistic. Daytime: warm golden morning sunlight coming in through the shop window.
Same cutaway isometric view from above at about 45 degrees, with the front wall (the street side, at the bottom of the image) and the ceiling removed. Landscape format (1536×1024). No people. No text, no letters and no logos anywhere.
The floor plan, as seen from the street:
- The entrance door is in the shop window, on the left of the front wall.
- Right inside the door, on the left, an L-shaped counter starts. Its long side runs along the left wall, from the entrance toward the back: first the cash register, the first thing you reach when you come in; then, further along, the refrigerated salad display under a glass sneeze guard, with trays of lettuce, tomatoes, onions, red cabbage, carrots and cucumbers, and the sauce bottles. At the back, the counter turns at a right angle toward the middle of the room: this short side is where the food is handed over.
- Behind the counter, against the left wall: the vertical kebab spit in front of its grill, a fryer, and a drinks fridge with glass doors.
- Every table is rectangular, with simple wooden chairs. Along the right wall, between the shop window and the staircase, three rectangular tables for four, with a red padded bench against the wall.
- At the back wall, the biggest rectangular table, for six, with a long red padded bench against the back wall, and above it a large plain wall mirror, wide and clean, big enough to write on with a marker.
- In the back right corner, a staircase going up to an office on the floor above, with a handrail.
- Lived-in details: a teapot, napkin dispensers and sauce bottles on the tables, a few plants, a menu board above the counter with no readable text.
```

À contrôler à la reprise : le style 2D (pas de 3D) et la lumière du matin ; la porte à gauche, la caisse juste après, puis les salades, le comptoir en L ; toutes les tables rectangulaires ; la table du fond avec sa banquette et le miroir ; l'escalier au fond à droite ; aucune personne, aucun texte.

Corrections de l'auteur avant d'envoyer la v2, le 2026-10-16 : pas de porte, une devanture en panneaux vitrés qui se replient ; la broche à gauche, c'est bon ; pas de grande table, des petites tables rectangulaires pour 4 partout ; tout au fond à gauche, le frigo, qu'on voit un plan sur deux, et qui ne gêne pas Sky quand il écrit sur le miroir. Claude garde la banquette le long du mur droit : la bible dit que Sky y dort le mardi.

## Prompt KB1 v3 — La maquette, avec les corrections de l'auteur

Dans la même conversation, avec la même image jointe. Remplace la v2, qui n'a pas été envoyée.

```
Redraw this kebab restaurant with the following changes. Style first: a flat 2D hand-drawn background painting from a 1990s anime film, in the style of the attached image (clean dark outlines, flat cel shading, muted warm palette, painted details). NOT a 3D render, NOT photorealistic. Daytime: warm golden morning sunlight coming in from the street.
Isometric view from above at about 45 degrees, with the ceiling removed and the walls cut low, so that the whole floor plan can be read. The street side is at the bottom of the image. Landscape format (1536×1024). No people. No text, no letters and no logos anywhere.
The floor plan, as seen from the street:
- There is no door: the whole street side is a glass shopfront made of folding panels, folded open like an accordion, so the shop opens wide onto the street.
- Right inside, on the left, an L-shaped counter starts. Its long side runs along the left wall, from the street toward the back: first the cash register, the first thing you reach when you come in; then, further along, the refrigerated salad display under a glass sneeze guard, with trays of lettuce, tomatoes, onions, red cabbage, carrots and cucumbers, and the sauce bottles. Near the back, the counter turns at a right angle toward the middle of the room: this short side is where the food is handed over.
- Behind the counter, against the left wall: the vertical kebab spit in front of its grill, and a fryer.
- In the back left corner, beyond the end of the counter: a tall drinks fridge with glass doors.
- Small rectangular tables for four, all the same, with simple wooden chairs, spread over the room. Along the right wall, a long red padded bench, with the tables in front of it.
- On the back wall, a large plain wall mirror, wide and clean, big enough to write on with a marker, with nothing in front of it but one table, so that someone can stand and write on it.
- In the back right corner, a staircase going up to an office on the floor above, with a handrail.
- Lived-in details: a teapot, napkin dispensers and sauce bottles on the tables, a few plants, a menu board above the counter with no readable text.
```

À contrôler à la reprise : le style 2D (pas de 3D) et la lumière du matin ; la devanture en panneaux repliés, sans porte ; la caisse juste en entrant à gauche, puis les salades, le comptoir en L, la broche derrière ; le frigo au fond à gauche ; des tables rectangulaires pour 4, toutes pareilles ; la banquette à droite ; le miroir au fond, dégagé ; l'escalier au fond à droite ; aucune personne, aucun texte.

Résultat de la v3, le 2026-10-16 : **la bonne base**, pour l'auteur (« c'est exactement ce genre de truc que je voyais »), avec des choses à corriger. Vue sur une capture d'écran, pas encore rangée.
- Juste : un rendu peint, la lumière du matin ; la devanture en panneaux repliés aux deux bouts, sans porte ; la caisse juste en entrant, puis les salades sous leur vitre, la broche sous sa hotte derrière le comptoir ; le frigo à boissons au fond à gauche ; des tables rectangulaires pour 4 ; la banquette rouge à droite ; le grand miroir au fond, une table devant.
- Différent du prompt, sans gêne : le L du comptoir a son petit côté devant (la caisse, face à la rue) et son long côté vers le fond.
- Relevé par Claude : des lettres sur le premier panneau de menu, en haut à gauche ; l'escalier est derrière le mur de la banquette, son pied près de la devanture, à droite, et on ne le voit pas depuis les tables ; le miroir reflète la salle, et dans chaque plan où on le verra, il faudra y refléter les persos.

## Prompt KB1 retouche — Les quatre corrections

L'auteur valide les trois corrections de Claude et ajoute la sienne : des tables un peu plus rectangulaires. Retouche : joins l'image v3 téléchargée dans le même message.

```
Edit ONLY the image attached to this message. Keep everything else exactly as it is: the same view, the same layout, the same style and the same light. Make only these four changes:
1. The first menu board on the left wall, at the top left: remove all the letters on it, keep only the picture of the food.
2. The wall between the red bench and the staircase, on the right: replace it with a low open wooden railing, so that the staircase can be seen from the dining room. The staircase stays where it is.
3. The large mirror on the back wall: make its glass slightly smoky, with only a soft, blurred, dim reflection instead of a clear reflection of the room. It keeps its size and its place.
4. Every table: make it a little longer, clearly rectangular (longer than wide), still a table for four with its four chairs.
```

À contrôler à la reprise : les quatre changements, un par un ; et rien d'autre de changé (le comptoir, la broche, le frigo, la devanture, la banquette, le style, la lumière).

Résultat de la retouche, le 2026-10-16 : mieux, l'ambiance est la bonne pour l'auteur (« l'ambiance du kebab c'est vraiment ça »). Le menu n'a plus de lettres, le miroir est fumé, les tables sont plus longues, et une rampe ouverte remplace le mur de l'escalier. Reste un défaut : les panneaux vitrés repliés sont en deux paquets, à gauche et à droite, et celui de droite bouche le pied de l'escalier. L'auteur : l'escalier est au bon endroit ; c'est son accès qui ne va pas, il mène à l'étage, chez Datastream, la boîte de Sky. Tous les panneaux repliés vont à gauche.

## Prompt KB1 retouche 2 — Les panneaux à gauche, l'accès à l'escalier

Dans ChatGPT, ouvre l'image retouchée et tape le prompt dans la case « Décrivez les modifications » : la retouche porte sur cette image-là.

```
Edit ONLY this image. Keep everything else exactly as it is: the same view, the same layout, the same style and the same light. Make only this change: the stack of folded glass panels at the right end of the shopfront, in front of the bottom of the staircase, moves to the left end of the shopfront, next to the other stack, so that all the folded panels are together on the left. The front right corner is then completely open: the bottom of the staircase can be reached directly from the street and from the dining room.
```

À contrôler à la reprise : tous les panneaux repliés à gauche ; le pied de l'escalier dégagé, accessible depuis la rue et la salle ; rien d'autre de changé.

Résultat de la retouche 2, le 2026-10-16 : les panneaux sont tous à gauche, le pied de l'escalier est dégagé. L'auteur demande encore : les panneaux vitrés sur toute la hauteur (ce sont eux qui ferment le kebab) ; les chaises toujours face à face (plus simple pour placer les persos) ; en haut de l'escalier, une porte, celle de Datastream, les bureaux de Sky.

## Prompt KB1 retouche 3 — Les panneaux, les chaises, la porte de Datastream

Comme la retouche 2 : dans la case « Décrivez les modifications » de l'image retouchée.

```
Edit ONLY this image. Keep everything else exactly as it is: the same view, the same layout, the same style and the same light. Make only these three changes:
1. The folded glass panels at the left end of the shopfront: make them full height, from the floor up to the top of the shopfront opening, because they close the whole shop at night.
2. The chairs: at every table in the middle of the room, two chairs on each long side, facing each other, and no chair at the ends. At every table along the red bench, the bench is on one long side and two chairs face it on the other side.
3. At the top of the staircase: a plain closed wooden door, the entrance of the office upstairs, with no sign and no text on it.
```

À contrôler à la reprise : les panneaux du sol au haut de la devanture ; les chaises face à face partout ; la porte en haut de l'escalier, sans texte ; rien d'autre de changé.

Ce que Claude garde pour les fonds par axe, plutôt qu'en retouche de la maquette : moins de petits objets (une plante par table, des sauces sur chaque table, une douzaine de plantes en tout) ; chacun devrait revenir identique d'un axe à l'autre. La maquette fixe le plan ; ce sont les fonds par axe qui feront foi.

Résultat de la retouche 3, le 2026-10-16 : les panneaux vont du sol au haut de la devanture, la porte de Datastream est en haut de l'escalier, les chaises du milieu sont face à face. L'auteur demande encore : à droite, les tables collées à la banquette, et les chaises de l'autre côté ; plus de plantes sur les tables. Les sauces blanche et rouge restent : si elles changent de place d'un plan à l'autre, ça passe pour quelqu'un qui s'en est servi (dans un même plan, le fond ne bouge pas). Claude garde aussi les distributeurs de serviettes : Sky griffonne ses formules sur les serviettes, et Maëlle les ramasse (bible).

## Prompt KB1 retouche 4 — Les tables de la banquette, les tables sans plantes

Comme la retouche 3 : dans la case « Décrivez les modifications » de l'image retouchée.

```
Edit ONLY this image. Keep everything else exactly as it is: the same view, the same layout, the same style and the same light. Make only these three changes:
1. The tables along the red bench on the right: push each table right against the bench, remove the chairs between the tables and the bench, and keep two chairs on the other long side of each table, facing the bench.
2. Every table: remove the small plant on it. The large plants standing on the floor stay.
3. Every table keeps only a red sauce bottle, a white sauce bottle and a napkin dispenser.
```

À contrôler à la reprise : les tables de droite collées à la banquette, deux chaises face à elle ; plus de plantes sur les tables, les grandes plantes au sol toujours là ; sur chaque table, deux sauces et des serviettes ; rien d'autre de changé.

Avant d'envoyer la retouche 4, l'auteur la corrige, le 2026-10-16 : les plantes, les sauces et les serviettes, c'est bon ; mais pour les chaises de droite, la v3 les a mises contre la banquette et au bout des tables. Il faut les faire pivoter d'un quart de tour : deux chaises côte à côte du côté de l'allée, tournées vers la banquette. Les retouches intermédiaires sont rangées hors du repo : `<sorties_root>/decors/kebab/maquette_retouche-1.png` à `-3`.

## Prompt KB1 retouche 4 v2 — Les chaises face à la banquette

Remplace la retouche 4, qui n'a pas été envoyée. Dans la case « Décrivez les modifications » de l'image de la retouche 3.

```
Edit ONLY this image. Keep everything else exactly as it is: the same view, the same layout, the same style and the same light. Make only these three changes:
1. The four tables along the red bench on the right: each table stays pushed against the bench. Its two chairs stand side by side on the aisle side of the table, the side opposite the bench, and both chairs are turned to face the bench across the table, like people sitting in front of someone on the bench. No chair between a table and the bench, no chair at the ends of these tables.
2. Every table: remove the small plant on it. The large plants standing on the floor stay.
3. Every table keeps only a red sauce bottle, a white sauce bottle and a napkin dispenser.
```

À contrôler à la reprise : à droite, deux chaises par table, côté allée, tournées vers la banquette, aucune contre la banquette ni au bout ; plus de plantes sur les tables ; deux sauces et des serviettes par table ; rien d'autre de changé.

La v2 de la retouche 4 n'était pas la bonne idée (non envoyée). L'auteur, le 2026-10-16 : faire pivoter les chaises d'un quart de tour par rapport à la table, pour que deux personnes soient assises face à face et une troisième sur la banquette, au bout de la table.

## Prompt KB1 retouche 4 v3 — Deux chaises face à face, la banquette au bout

```
Edit ONLY this image. Keep everything else exactly as it is: the same view, the same layout, the same style and the same light. Make only these three changes:
1. The four tables along the red bench on the right: each table keeps one short end against the bench. Put one chair on each long side of the table, the two chairs facing each other across the table, so two people sit face to face and a third person sits on the bench at the end of the table. No chair between a table and the bench.
2. Every table: remove the small plant on it. The large plants standing on the floor stay.
3. Every table keeps only a red sauce bottle, a white sauce bottle and a napkin dispenser.
```

À contrôler à la reprise : à droite, par table, une chaise de chaque long côté, face à face, la banquette au bout ; plus de plantes sur les tables ; deux sauces et des serviettes par table ; les tables du milieu inchangées ; rien d'autre de changé.

Résultat de la retouche 4 v3, le 2026-10-16 : les plantes ont quitté les tables, les sauces et les serviettes sont là. Mais les tables de droite sont devenues étroites, parallèles à la banquette, avec les deux chaises côté allée, tournées vers elle : ChatGPT n'a pas suivi la consigne. Capture rangée hors du repo (`<sorties_root>/decors/kebab/maquette_retouche-4_capture.png`).

Les mots ne suffisent plus pour la disposition : Claude a dessiné un plan vu de dessus, en code (`pipeline/plan_kebab.py`), d'après la maquette et les consignes de l'auteur. Il servira aussi pour les axes de caméra, et à chaque prompt de fond. À faire valider par l'auteur.

## Prompt KB1 retouche 5 — Les tables de droite, d'après le plan

Joins deux images dans le même message : l'image retouchée (la dernière) et le plan (`~/Téléchargements/kebab_plan-vu-de-dessus.png`).

```
Edit ONLY the first attached image, the kebab restaurant. The second attached image is a floor plan of the same restaurant seen from above; it is only a guide, do not copy its colours, its labels or its style. Keep everything else in the restaurant exactly as it is: the same view, the same style, the same light. Make only this change: arrange the four tables along the red bench on the right exactly as in the plan. Each table is turned perpendicular to the bench, one short end touching the bench. One chair on each long side of the table, the two chairs facing each other across the table. No chair between a table and the bench. No text anywhere.
```

À contrôler à la reprise : les quatre tables de droite perpendiculaires à la banquette, une chaise de chaque côté, face à face ; rien du plan recopié (ni couleurs, ni étiquettes) ; rien d'autre de changé.

L'auteur sur le plan, le 2026-10-16 : bon, sauf les tables : six tables rectangulaires identiques, quatre chaises à chacune. Plan redessiné : trois tables au milieu (la première devant le miroir) et trois le long de la banquette, perpendiculaires, un petit bout contre elle ; à chaque table, deux chaises de chaque long côté, face à face.

## Prompt KB1 retouche 5 v2 — Les six tables, d'après le plan

Remplace la retouche 5, qui n'a pas été envoyée. Deux images jointes dans le même message : l'image retouchée (la dernière) et le plan (`~/Téléchargements/kebab_plan-vu-de-dessus.png`).

```
Edit ONLY the first attached image, the kebab restaurant. The second attached image is a floor plan of the same restaurant seen from above; it is only a guide, do not copy its colours, its labels or its style. Keep everything else in the restaurant exactly as it is: the same view, the same style, the same light, the same counter, bench, staircase, mirror and plants. Make only this change: arrange the tables and chairs exactly as in the plan. There are six identical rectangular wooden tables, each with four chairs, two on each long side, facing each other across the table. Three tables stand in a row in the middle of the room, the first one in front of the mirror. Three tables stand along the red bench on the right, each turned perpendicular to the bench, one short end touching the bench. Each table keeps a red sauce bottle, a white sauce bottle and a napkin dispenser. No text anywhere.
```

À contrôler à la reprise : six tables identiques, quatre chaises chacune, face à face ; trois au milieu, trois perpendiculaires à la banquette ; rien du plan recopié ; rien d'autre de changé.

Résultat de la retouche 5 v2, le 2026-10-16, dans une nouvelle conversation : six tables, mais celles de droite restent parallèles à la banquette, avec des chaises des deux côtés, et les plantes sont revenues sur les tables. Capture hors du repo (`maquette_retouche-5_capture.png`). Cinq retouches n'ont pas suffi : les modèles d'images placent mal les meubles et leur orientation. Claude propose d'arrêter les retouches : la maquette fixe l'ambiance et le plan général, et `plan_v1.png` (rangé dans le repo) fixe la disposition exacte. Les tables de droite se règlent dans les fonds par axe, avec le plan joint ; et si ça rate encore, dans le modèle local, guidé par le plan (ControlNet).

**Maquette retenue, le 2026-10-16** : l'auteur a enlevé lui-même les plantes des tables et garde cette version (`maquette_v2.png`) : « toi tu as compris et tu sais comment on s'en servira ». Les tables de droite y restent parallèles à la banquette et un peu carrées ; `plan_v1.png` fait foi pour la disposition.

**Écart avec le texte du CERN, signalé à l'auteur** : le texte met le grand miroir « derrière la banquette » (l. 482), Sky « au fond, table bancale » (l. 14), Seb et Maëlle sur la banquette (l. 460, 466). Dans la maquette, la banquette longe le mur de droite et le miroir est au mur du fond, sans banquette devant. Le texte cite aussi l'horloge Efes au-dessus du comptoir (l. 498), le menu plastifié sur la vitrine (l. 606), le chat sur le comptoir (l. 703), l'escalier qui grince (l. 121) : à reprendre dans les fonds par axe.

**Décisions de l'auteur, le 2026-10-16** : le canon est Annemasse (`ecriture/canon.yaml`) ; la banquette en L sous le miroir lui va ; l'escalier sera en bois. Le texte peut s'adapter au décor si besoin : à l'origine, c'était une histoire, pas un script. `plan_v2.png` reprend tout ça : la banquette en L, la table de Sky au fond avec la banquette derrière elle et le miroir au-dessus, deux tables au milieu, trois le long de la rampe, l'escalier en bois. La maquette (`maquette_v2.png`) n'est plus retouchée : ces changements iront dans les fonds par axe.

## Prompt KB2 — Le plan peint, vu exactement d'en haut

L'idée : ChatGPT respecte mal une disposition décrite en mots, mais une vue prise du même point que le plan n'a qu'à le recouvrir de peinture. Deux images jointes dans le même message, dans cet ordre : le plan (`~/Téléchargements/kebab_pour_KB2_1_plan.png`) et la maquette pour le style (`~/Téléchargements/kebab_pour_KB2_2_style.png`). Dans une nouvelle conversation, ou dans celle du kebab.

```
The first attached image is the exact floor plan of a small kebab restaurant, seen straight from above. The second attached image shows the same restaurant and gives the art style, the materials and the light. Paint this restaurant seen straight from above, exactly like the plan: the same layout, every element at the same place, with the same size and the same orientation, as if the plan had been painted over. Style: a flat 2D hand-drawn background painting from a 1990s anime film, like the second image (clean dark outlines, flat cel shading, muted warm palette, warm golden morning light coming from the street, at the bottom of the image). NOT a 3D render, NOT photorealistic. Do not copy the colours or the labels of the plan. No people. No text, no letters and no logos anywhere. Landscape format (1536×1024).
What is where, as in the plan:
- At the bottom, the street; the shopfront is fully open, and at the bottom left the folding glass panels are folded together, full height.
- On the left, the L-shaped stainless steel counter: the cash register on its short side at the front, then the refrigerated salad display and the sauces along its long side. Behind it, against the left wall, the vertical kebab spit under its hood, the grill, the fryer and the worktops. A round clock on the wall above the counter.
- In the back left corner, the tall drinks fridge with glass doors.
- On the back wall, the large plain mirror, slightly smoky, above a long red padded bench. The bench runs along the back wall, then turns and runs along the right side: an L-shaped bench.
- At the back, in front of the bench, one rectangular wooden table with two chairs on its front side, facing the bench.
- In the middle of the room, two identical rectangular wooden tables, each with two chairs on each long side, facing each other.
- On the right, three identical rectangular wooden tables, each perpendicular to the bench with one short end against it, and two chairs on each long side, facing each other.
- On the far right, behind a low open wooden railing, a wooden staircase going up from the street side toward the back, to a plain closed wooden door at the top.
- On every table, a red sauce bottle, a white sauce bottle and a napkin dispenser. A few large plants on the floor, in the corners; no plant on the tables.
```

À contrôler à la reprise : la vue d'en haut, droite ; chaque élément à sa place du plan, surtout les six tables et leurs chaises ; la banquette en L sous le miroir ; l'escalier en bois et sa porte ; rien du plan recopié (couleurs, étiquettes) ; aucun texte.

**Résultat de KB2, le 2026-10-17 : réussi du premier coup**, gardé par l'auteur, qui fait supprimer les autres images du kebab. Chaque élément est à sa place du plan : le comptoir en L (la caisse devant, les salades le long), la broche, le grill et la friteuse contre le mur gauche, l'horloge, le frigo au fond à gauche, le miroir au-dessus de la banquette en L, la table de Sky au fond, deux chaises face à la banquette, deux tables au milieu, trois perpendiculaires à la banquette, quatre chaises face à face, l'escalier en bois derrière sa rampe et la porte en haut, les panneaux repliés en bas à gauche. Aucun texte. La leçon : pour une disposition exacte, dessiner le plan en code et faire peindre la vue prise du même point, plutôt que de la décrire.

Ce qui fait foi pour le kebab : `plan-peint_v1.png` pour l'image, `plan_v2.png` pour les mesures (en code, `pipeline/plan_kebab.py`).

## Les fonds par axe

Les axes : `axes.md`. Pour chacun, deux images jointes dans le même message, dans cet ordre : le plan avec la seule caméra de l'axe (`python3 pipeline/plan_kebab.py <sortie> axe <numéro>`), puis le plan peint. Dans une nouvelle conversation ChatGPT réservée aux fonds du kebab, un prompt à la fois.

### Prompt A6 — La table de Sky, la banquette, le miroir

Joins `~/Téléchargements/kebab_pour_A6_1_camera.png` puis `~/Téléchargements/kebab_pour_A6_2_plan-peint.png`.

```
The first attached image is the floor plan of our kebab restaurant, with one camera marked in blue (number 6): its position and the cone of what it sees. The second attached image is the same restaurant seen from above, painted in our style; it gives the style, the materials, the colours and the objects. Paint the view from this camera, as an empty background for an anime series: a flat 2D hand-drawn background painting from a 1990s anime film, in the style of the second image (clean dark outlines, flat cel shading, muted warm palette, painted details). NOT a 3D render, NOT photorealistic. Landscape format (1536×1024); keep the important things away from the top and bottom edges, the image will be cropped to 16:9.
The camera stands in the aisle, about two metres in front of the back table, at the eye level of a seated person (about 1.2 m), and looks straight at the back wall. Normal lens, straight vertical lines, no fisheye.
What we see, from front to back:
- At the bottom of the frame, the tops of the backs of the two empty wooden chairs of the back table, turned away from us.
- The rectangular wooden table, with a red sauce bottle, a white sauce bottle and a napkin dispenser.
- Behind the table, the long red padded bench along the back wall, empty.
- Above the bench, the large plain mirror, slightly smoky, with only a soft, blurred, dim reflection of the bright street behind the camera. It is wide: it fills most of the width of the frame.
- On the left edge, the end of the bench; on the right edge, the bench continues toward the corner where it turns.
Morning: warm golden sunlight comes from the street, behind the camera, and falls on the bench and the wall in long warm patches. No people. No text, no letters and no logos anywhere.
```

À contrôler à la reprise : la caméra à hauteur d'une personne assise, face au mur du fond ; les dossiers des deux chaises en bas ; la table et ses deux sauces et ses serviettes ; la banquette vide ; le miroir large et fumé, sans reflet net ; rien d'important près des bords haut et bas (recadrage en 16:9) ; aucune personne, aucun texte ; le style du plan peint.

Résultat de A6, le 2026-10-17 : le bon angle, pour l'auteur. La table, ses sauces et ses serviettes, la banquette vide qui tourne à droite, les dossiers des chaises en bas, le style du plan peint. Deux défauts, relevés par l'auteur : le miroir reflète une scène nette (des fenêtres à petits bois, des arbres, un plafond à poutres) qui n'est pas notre devanture ; et la lumière est fausse, avec une grande tache de soleil et des ombres de feuilles sur le mur de gauche, comme s'il y avait une fenêtre sur le côté. Capture hors du repo (`<sorties_root>/decors/kebab/table-du-fond_essai-1_capture.png`).

La règle pour tous les axes, désormais écrite dans chaque prompt : **la seule lumière du jour vient de la devanture ouverte, côté rue ; il n'y a aucune autre fenêtre** ; et **le miroir est en verre fumé sombre, sans reflet reconnaissable**.

### Prompt A6 retouche — Le miroir et la lumière

Dans la case « Décrivez les modifications » de l'image.

```
Edit ONLY this image. Keep everything else exactly as it is: the same view, the same table, chairs, bench, plant, style and colours. Make only these two changes:
1. The mirror: make its glass dark and smoky, almost opaque, with only a very faint, blurred warm glow. No recognisable reflection: no windows, no trees, no ceiling, no lamps in it.
2. The light: there is no window on the left. Remove the bright patch of sunlight and the leaf shadows on the left wall. The only daylight comes from the open shopfront behind the camera: a soft, warm morning light on the back wall and the bench, with the shadows of the chairs and of the table falling toward the back wall.
```

À contrôler à la reprise : le miroir fumé, sans reflet ; plus de fenêtre implicite à gauche ; la lumière qui vient de derrière la caméra ; rien d'autre de changé.

Résultat de la retouche A6, le 2026-10-17 : validée par l'auteur (« pas parfait mais c'est juste »). Le miroir est devenu un verre sombre et fumé, avec des lueurs chaudes floues : les dessins de Sky au marqueur blanc s'y liront bien. Plus de fenêtre implicite. La lumière est plus sombre que le matin du plan peint ; elle s'harmonisera à l'étalonnage, ce qui n'est pas possible pour une erreur de disposition. Les axes suivants gardent cette ambiance : intérieur chaud et tamisé, la rue lumineuse.

### Prompt A7 — Depuis la place de Sky, vers la rue

Joins `~/Téléchargements/kebab_pour_A7_camera.png` puis `~/Téléchargements/kebab_pour_axes_plan-peint.png` (le même plan peint pour tous les axes).

```
The first attached image is the floor plan of our kebab restaurant, with one camera marked in blue (number 7): its position and the cone of what it sees. The second attached image is the same restaurant seen from above, painted in our style; it gives the style, the materials, the colours and the objects. Paint the view from this camera, as an empty background for an anime series: a flat 2D hand-drawn background painting from a 1990s anime film, in the style of the second image (clean dark outlines, flat cel shading, muted warm palette, painted details). NOT a 3D render, NOT photorealistic. Landscape format (1536×1024); keep the important things away from the top and bottom edges, the image will be cropped to 16:9.
The camera sits on the red bench at the back, in the place of someone seated at the back table, at the eye level of a seated person (about 1.2 m), and looks toward the street. Normal lens, straight vertical lines, no fisheye.
What we see, from front to back:
- At the bottom of the frame, the near edge of the back table, with a red sauce bottle, a white sauce bottle and a napkin dispenser.
- On the other side of that table, its two empty wooden chairs, facing us.
- Further away, the two tables in the middle of the room, one behind the other, each with two chairs on each long side.
- On the right of the frame, the stainless steel counter seen from the side, with the salad display, and at its front end the cash register; the kebab spit is behind it, against the wall.
- On the left of the frame, the tables along the red bench and the low wooden railing of the staircase.
- At the far end, the shopfront fully open onto the sunny street: the sidewalk, the bollards, the tram rails, and the facade of a plain building across the street.
Light: the only daylight comes from the open shopfront at the far end, on the street side; there are no other windows. The street is bright with warm morning sun; inside, the light is warm and dim, as in the second image, and the shadows of the tables and chairs fall toward the camera. No people. No text, no letters and no logos anywhere, including on the building across the street.
```

À contrôler à la reprise : la caméra assise sur la banquette, vers la rue ; la table de Sky en bas, ses deux chaises face à nous ; les deux tables du milieu ; le comptoir à droite de l'image, la banquette et la rampe à gauche (c'est le contrechamp : la gauche et la droite s'inversent) ; la devanture ouverte et la rue au fond ; la lumière qui vient de la rue ; aucune personne, aucun texte.

**Le plan v3, le 2026-10-17** : l'auteur a annoté le plan v2 dans ChatGPT (la première table de droite barrée, l'angle de la banquette entouré). Validé : la table de Sky dans l'angle de la banquette, pour cinq, Sky et Maëlle sur la banquette du fond, deux chaises en face, Patrick au bout sur la banquette de droite (« c'est l'ancien, ça résout les problèmes de champ ») ; le miroir sur toute la banquette du fond, à fleur de son bout gauche ; entre la banquette et l'escalier, une rampe basse et droite, l'angle grand ouvert ; de l'herbe entre les rails du tram ; trois lumières par axe (jour, pluie, nuit). Le fond A6 et le plan peint sont à refaire ; A7 n'a pas été envoyé. Les 21 axes : `axes.md`.

### Prompt KB2 v2 — Le plan peint, d'après le plan v3

Joins `~/Téléchargements/kebab_pour_KB2v2_1_plan.png` puis `~/Téléchargements/kebab_pour_KB2v2_2_ancien-plan-peint.png`. Dans la conversation de KB2, ou une nouvelle.

```
The first attached image is the exact floor plan of a small kebab restaurant, seen straight from above. The second attached image is an older painting of the same restaurant: take from it only the art style, the materials, the colours and the light; its layout is out of date, so follow only the plan. Paint this restaurant seen straight from above, exactly like the plan: the same layout, every element at the same place, with the same size and the same orientation, as if the plan had been painted over. Style: a flat 2D hand-drawn background painting from a 1990s anime film (clean dark outlines, flat cel shading, muted warm palette, warm golden morning light coming from the street, at the bottom of the image). NOT a 3D render, NOT photorealistic. Do not copy the colours or the labels of the plan. No people. No text, no letters and no logos anywhere. Landscape format (1536×1024).
What is where, as in the plan:
- At the bottom, the street with the tram rails and grass growing between the rails; the shopfront is fully open, and at the bottom left the folding glass panels are folded together, full height.
- On the left, the L-shaped stainless steel counter: the cash register on its short side at the front, then the refrigerated salad display and the sauces along its long side. Behind it, against the left wall, the vertical kebab spit under its hood, the grill, the fryer and the worktops. A round clock on the wall above the counter.
- In the back left corner, the tall drinks fridge with glass doors.
- An L-shaped red padded bench: it runs along the back wall, then turns in the back right corner and runs along the right side. Above the whole back part of the bench, a long plain mirror, dark and smoky, from the left end of the bench to the corner.
- In the back right corner, in the angle of the bench, one rectangular wooden table: its back long side against the back bench, its right short end against the right bench, and two chairs on its front long side.
- In the middle of the room, two identical rectangular wooden tables, each with two chairs on each long side, facing each other.
- Along the right bench, further toward the street, two identical rectangular wooden tables, each perpendicular to the bench with one short end against it, and two chairs on each long side.
- On the far right, a wooden staircase going up from the street side toward the back, to a plain closed wooden door at the top. Between the bench and the staircase there is only a low, straight, open wooden railing: no wall, nothing that juts into the room.
- On every table, a red sauce bottle, a white sauce bottle and a napkin dispenser. A few large plants on the floor, in the corners; no plant on the tables.
```

À contrôler à la reprise : la table de Sky dans l'angle, contre les deux banquettes ; le miroir sur toute la banquette du fond ; deux tables au milieu, deux le long de la banquette de droite ; la rampe basse et droite, sans mur ; l'herbe entre les rails ; rien de l'ancien plan peint recopié ; rien du plan (couleurs, étiquettes) ; aucun texte.

Résultat de KB2 v2, le 2026-10-17 : la disposition du plan v3 est là (la table de Sky dans l'angle, le miroir sur la banquette du fond, deux tables au milieu, deux à droite, l'herbe entre les rails). L'auteur relève trois erreurs : l'escalier donne directement sur la rue (il le veut dans le kebab) ; la lumière arrive encore de biais, comme par une fenêtre sur le côté ; la caisse est tournée vers le client, alors que c'est Mohamed qui tape dedans. Claude ajoute : la rampe est un haut panneau, pas une rampe basse. D'où `plan_v4.png` (façade pleine devant l'escalier, un palier à l'intérieur, la banquette de droite raccourcie pour y passer) et une retouche. Capture hors du repo (`plan-peint_v2_essai-1_capture.png`). L'auteur fera tous les fonds d'un coup.

### Prompt KB2 v2 retouche — L'escalier, la lumière, la caisse

Dans la case « Décrivez les modifications » de l'image.

```
Edit ONLY this image. Keep everything else exactly as it is: the same top view, the same layout, the same style and colours. Make only these four changes:
1. The staircase must not open onto the street. Close the front of the building in front of the staircase with a plain solid wall, from the end of the shopfront to the right corner. The staircase now starts from a small landing inside the restaurant, at the front right, reached from the dining room past the end of the red bench; from there it goes up toward the back as now, to the door.
2. Between the red bench and the staircase, a low open wooden railing only, no tall panel.
3. The light: the sunlight comes only from the open shopfront at the bottom of the image. The shadows of the tables, chairs and counter point straight up toward the back wall. No light comes from the left or the right: the side walls are solid, with no windows.
4. The cash register on the front of the counter: turn it around so that its screen and keypad face the inside of the counter, toward the kitchen, where the cook stands; its back faces the street.
```

À contrôler à la reprise : l'escalier fermé côté rue, son palier dans la salle ; la rampe basse ; les ombres droites vers le fond, sans lumière de côté ; la caisse tournée vers l'intérieur du comptoir ; rien d'autre de changé.

L'auteur, sur le plan des axes v4 annoté, le 2026-10-17 : pas de muret devant l'escalier (« il saute ») ; la table de devant à droite est celle de Sky dans l'épisode Navier-Stokes, avec deux angles de plus ; deux plans, un sans caméras (pour ChatGPT), un avec (pour Claude). D'où `plan_v5.png` et `plan-axes_v5.png`, 25 axes. Le point 1 de la retouche ci-dessus change : pas de mur, le palier derrière la devanture ouverte.

### Prompt KB2 v2 retouche, corrigée — Le palier, la rampe, la lumière, la caisse

Remplace la retouche précédente si elle n'a pas été envoyée.

```
Edit ONLY this image. Keep everything else exactly as it is: the same top view, the same layout, the same style and colours. Make only these four changes:
1. The staircase must not start on the sidewalk. Its bottom step now starts from a small landing inside the restaurant, at the front right, a little back from the street, reached from the dining room past the end of the red bench. The open shopfront continues across the whole front, up to the right corner, with no wall in front of the landing. From the landing, the staircase goes up toward the back as now, to the door.
2. Between the red bench and the staircase, a low open wooden railing only, no tall panel.
3. The light: the sunlight comes only from the open shopfront at the bottom of the image. The shadows of the tables, chairs and counter point straight up toward the back wall. No light comes from the left or the right: the side walls are solid, with no windows.
4. The cash register on the front of the counter: turn it around so that its screen and keypad face the inside of the counter, toward the kitchen, where the cook stands; its back faces the street.
```

L'auteur, le 2026-10-17 : pas de retouche, on refait le plan peint à partir du plan v5 sans caméras, pour avoir une base fixe et revalidée ; les axes, Claude les garde pour lui et n'en montre qu'un à la fois.

### Prompt KB2 v3 — Le plan peint, d'après le plan v5

Joins `~/Téléchargements/kebab_pour_KB2v3_1_plan.png` (le plan v5, sans caméras) puis `~/Téléchargements/kebab_pour_KB2v3_2_style.png` (l'essai KB2 v2, pour le style seulement).

```
The first attached image is the exact floor plan of a small kebab restaurant, seen straight from above. The second attached image is an earlier painting of the same restaurant: take from it only the art style, the materials and the colours; where it differs from the plan, follow the plan. Paint this restaurant seen straight from above, exactly like the plan: the same layout, every element at the same place, with the same size and the same orientation, as if the plan had been painted over. Style: a flat 2D hand-drawn background painting from a 1990s anime film (clean dark outlines, flat cel shading, muted warm palette). NOT a 3D render, NOT photorealistic. Do not copy the colours or the labels of the plan. No people. No text, no letters and no logos anywhere. Landscape format (1536×1024).
Light: warm golden morning sunlight comes only from the street, at the bottom of the image, through the open shopfront. The shadows of the tables, chairs and counter point straight up toward the back wall. No light comes from the left or the right: the side walls are solid, with no windows.
What is where, as in the plan:
- At the bottom, the sidewalk and the street with the tram rails and grass growing between the rails. The shopfront is fully open across the whole width, up to the right corner, with no wall; at the bottom left, the folding glass panels are folded together, full height.
- On the left, the L-shaped stainless steel counter. On its short side at the front, the cash register, turned toward the inside of the counter: its screen and keypad face the kitchen, where the cook stands, and its back faces the street. Then, along its long side, the refrigerated salad display and the sauces. Behind the counter, against the left wall, the vertical kebab spit under its hood, the grill, the fryer and the worktops. A round clock on the wall above the counter.
- In the back left corner, the tall drinks fridge with glass doors.
- An L-shaped red padded bench: it runs along the back wall, then turns in the back right corner and runs along the right side. Above the whole back part of the bench, a long plain mirror, dark and smoky, from the left end of the bench to the corner.
- In the back right corner, in the angle of the bench, one rectangular wooden table: its back long side against the back bench, its right short end against the right bench, and two chairs on its front long side.
- In the middle of the room, two identical rectangular wooden tables, each with two chairs on each long side, facing each other.
- Along the right bench, further toward the street, two identical rectangular wooden tables, each perpendicular to the bench with one short end against it, and two chairs on each long side.
- On the far right, a wooden staircase. It starts from a small landing inside the restaurant, at the front right, a little back from the street, reached from the dining room past the end of the red bench; from there it goes up toward the back, to a plain closed wooden door at the top. Between the bench and the staircase there is only a low, straight, open wooden railing: no wall, no tall panel.
- On every table, a red sauce bottle, a white sauce bottle and a napkin dispenser. A few large plants on the floor, in the corners; no plant on the tables.
```

À contrôler à la reprise : chaque élément contre le plan v5 ; le palier de l'escalier dans la salle, la devanture ouverte jusqu'au coin, sans mur ; la rampe basse ; les ombres droites vers le fond ; la caisse tournée vers l'intérieur du comptoir ; aucun texte.

**Résultat de KB2 v3, le 2026-10-17 : la base fixe, validée par l'auteur** (« on l'a enfin ! »), rangée en `plan-peint_v2.png`. Chaque élément du plan v5 est à sa place : le palier de l'escalier dans la salle et la devanture ouverte jusqu'au coin, la rampe basse, les ombres droites vers le fond, la table de Sky dans l'angle, l'herbe entre les rails. Seul écart accepté : la caisse reste tournée vers la rue. À la demande de l'auteur, toutes les autres images du kebab sont supprimées (repo, disque externe, Téléchargements) ; elles restent dans l'historique git. Les fonds par axe commencent : `axes.md`, « Le modèle de prompt d'un axe ».

### Prompt A6 (plan v5) — La table de Sky dans l'angle

Le modèle de `axes.md`. Joins `~/Téléchargements/kebab_pour_A6_camera.png` puis `~/Téléchargements/kebab_pour_axes_plan-peint.png`, dans une nouvelle conversation ChatGPT réservée aux fonds du kebab.

```
The first attached image is the floor plan of our kebab restaurant, with one camera marked in blue (number 6): its position and the cone of what it sees. The second attached image is the same restaurant seen from above, painted in our style; it gives the style, the materials, the colours and the objects. Paint the view from this camera, as an empty background for an anime series: a flat 2D hand-drawn background painting from a 1990s anime film, in the style of the second image (clean dark outlines, flat cel shading, muted warm palette, painted details). NOT a 3D render, NOT photorealistic. Do not copy the labels of the plan. Landscape format (1536×1024); keep the important things away from the top and bottom edges, the image will be cropped to 16:9.
The camera stands in the room, about two metres in front of the table in the back right corner, at the eye level of a seated person (about 1.2 m), and looks straight at the back wall. Normal lens, straight vertical lines, no fisheye.
What we see, from front to back:
- At the bottom of the frame, the tops of the backs of the two empty wooden chairs of that table, turned away from us.
- The rectangular wooden table, with a red sauce bottle, a white sauce bottle and a napkin dispenser.
- Behind the table, the red padded bench along the back wall, empty, and above it the long dark smoky mirror, which fills the left and the middle of the frame.
- On the right of the frame, the bench turns in the corner and comes toward us along the right side: the right short end of the table touches it (that is the seat at the head of the table). Beyond it, a low open wooden railing, and behind the railing the wooden staircase going up toward the back, to a plain closed wooden door at the top, on the far right.
Light: the only daylight comes from the open shopfront behind the camera; there are no other windows, the side walls are solid. The shadows of the chairs and of the table fall toward the back wall. Inside, the light is warm and dim. The mirror is dark smoky glass, with no recognisable reflection. No people. No text, no letters and no logos anywhere.
```

À contrôler à la reprise : la caméra assise, face au mur du fond ; les dossiers des deux chaises en bas ; la table et ses deux sauces et ses serviettes ; la banquette vide qui tourne dans l'angle, le bout de la table contre elle ; le miroir fumé à gauche et au milieu ; la rampe basse, l'escalier et la porte à droite ; la lumière de derrière la caméra ; aucune personne, aucun texte.

L'auteur redessine l'axe 6 dans ChatGPT, le 2026-10-17 : la caméra au bout gauche de la table, de biais vers l'angle (« ça me paraît plus juste »). Le prompt A6 ci-dessus est remplacé par celui-ci, non envoyé.

### Prompt A6 v2 — La table de Sky, de biais vers l'angle

Joins `~/Téléchargements/kebab_pour_A6_camera.png` (refait) puis `~/Téléchargements/kebab_pour_axes_plan-peint.png`.

```
The first attached image is the floor plan of our kebab restaurant, with one camera marked in blue (number 6): its position and the cone of what it sees. The second attached image is the same restaurant seen from above, painted in our style; it gives the style, the materials, the colours and the objects. Paint the view from this camera, as an empty background for an anime series: a flat 2D hand-drawn background painting from a 1990s anime film, in the style of the second image (clean dark outlines, flat cel shading, muted warm palette, painted details). NOT a 3D render, NOT photorealistic. Do not copy the labels of the plan. Landscape format (1536×1024); keep the important things away from the top and bottom edges, the image will be cropped to 16:9.
The camera stands just in front of the left end of the table in the back right corner, at the eye level of a seated person (about 1.2 m), and looks diagonally into that corner. Normal lens, straight vertical lines, no fisheye.
What we see:
- At the bottom right of the frame, the near chair of the table, seen from behind, empty.
- The rectangular wooden table, seen at an angle, with a red sauce bottle, a white sauce bottle and a napkin dispenser.
- On the left and at the back of the frame, the red padded bench along the back wall, empty, and above it the long dark smoky mirror.
- In the corner, the bench turns and comes toward us on the right of the frame: the right short end of the table touches it; that is the seat at the head of the table.
- On the far right, beyond that bench, a low open wooden railing, and behind it the upper part of the wooden staircase, going up to a plain closed wooden door.
Light: the only daylight comes from the open shopfront, behind the camera; there are no other windows, the side walls are solid. The shadows of the chairs and of the table fall toward the back wall. Inside, the light is warm and dim. The mirror is dark smoky glass, with no recognisable reflection. No people. No text, no letters and no logos anywhere.
```

À contrôler à la reprise : la vue de biais vers l'angle, assise ; la chaise vide en bas à droite ; la table de biais, ses deux sauces et ses serviettes ; la banquette du fond et le miroir fumé à gauche ; l'angle et la banquette de droite, le bout de la table contre elle ; la rampe basse, l'escalier et la porte au bord droit ; la lumière de derrière ; aucune personne, aucun texte.

Résultat de A6 v2, le 2026-10-17 : raté, pour l'auteur. La caméra est de face devant la table, pas au bout gauche, de biais ; la porte de Datastream se voit en haut de l'escalier, alors que d'en bas on ne la voit pas ; la banquette doit continuer tout du long. Capture hors du repo (`table-du-fond_essai-2_capture.png`). Leçon : un plan vu de dessus avec une caméra ne suffit pas, ChatGPT ne tient pas la place de la caméra. Claude dessine désormais la vue elle-même en volumes simples (`pipeline/vue_kebab.py`), comme le plan qu'il a peint du premier coup. La caméra 6 reculée de 60 cm, même direction, pour laisser de l'air autour de la table.

### Prompt A6 v3 — La table de Sky, d'après la vue en volumes

Joins `~/Téléchargements/kebab_pour_A6_1_vue.png` (la vue en volumes) puis `~/Téléchargements/kebab_pour_axes_plan-peint.png`, dans la conversation des fonds.

```
The first attached image is a rough 3D layout of one view of our kebab restaurant, made of simple flat-coloured volumes: it fixes the camera, the perspective, the framing and the place of every object. The second attached image is the same restaurant seen from above, painted in our style: it gives the art style, the materials, the colours and the objects. Paint exactly the view of the first image, as an empty background for an anime series: keep the same camera, the same perspective and framing, and every object at the same place, with the same size and angle, as if the layout had been painted over. Replace the simple volumes with the real objects:
- the dark rectangle with a brown frame on the left is the long mirror, in dark smoky glass, with no recognisable reflection;
- the red volumes are one continuous L-shaped red padded bench, with no break: it runs along the back wall, turns in the corner and comes toward us on the right;
- the light wood slab is the rectangular wooden table, with a red sauce bottle, a white sauce bottle and a napkin dispenser;
- the brown upright panels at the bottom right are the backs of two empty wooden chairs with red seats, turned away from us;
- the brown blocks at the top right are the underside of the wooden staircase, going up toward the back through an opening in the ceiling; we see no door, the office upstairs is out of sight;
- the beige surfaces are the walls, the corner is between them.
Style: a flat 2D hand-drawn background painting from a 1990s anime film, in the style of the second image (clean dark outlines, flat cel shading, muted warm palette, painted details). NOT a 3D render, NOT photorealistic, and do not keep the flat colours of the layout. Light: the only daylight comes from the open shopfront, behind the camera; there are no windows, the side walls are solid; the shadows fall toward the back wall. Inside, the light is warm and dim. No people. No text, no letters and no logos anywhere. Landscape format (1536×1024).
```

À contrôler à la reprise : le cadrage et la perspective de la vue en volumes ; la banquette d'un seul tenant, du bord gauche à l'angle puis vers nous ; le miroir fumé ; la table, ses sauces et ses serviettes ; les dossiers des deux chaises en bas à droite ; le dessous de l'escalier en haut à droite, sans porte ; aucune personne, aucun texte.

Résultat de A6 v3 (la vue en volumes), le 2026-10-17 : le bon angle et la bonne disposition. Reste l'angle de la pièce : l'auteur ne veut pas voir l'escalier, qui monte derrière un mur (« c'est un mur tout simplement »), et il manque la grande plante de l'angle. Plan v6 et vue en volumes corrigés (le mur de l'escalier, la plante). Capture hors du repo (`table-du-fond_essai-3_capture.png`).

### Prompt A6 v3 retouche — Le mur de l'escalier, la plante de l'angle

Dans la case « Décrivez les modifications » de l'image.

```
Edit ONLY this image. Keep everything else exactly as it is: the same view, the same table, bench, chairs, mirror, style and light. Make only these two changes:
1. At the top right, remove the wooden staircase completely: there is no staircase in this view, only the plain wall, the same as the rest of the wall, up to the top of the frame.
2. In the corner where the red bench turns, add a large green potted plant standing behind the corner of the bench, its broad leaves rising above the backrest against the two walls.
```

À contrôler à la reprise : plus d'escalier, un mur uni ; la plante dans l'angle, derrière le coin de la banquette ; rien d'autre de changé.

**Résultat de la retouche A6 v3, le 2026-10-17 : validé par l'auteur** (« c'est parfait »), rangé en `table-du-fond/fond_v1.png`. Le mur uni à droite, la plante dans l'angle. La recette qui marche pour un axe : la vue en volumes (`pipeline/vue_kebab.py`) jointe en premier, le plan peint en second, la liste « tel volume = tel objet » ; puis, s'il reste un détail, une retouche de deux points au plus.

### Prompt A7 — Depuis la place de Sky, vers la rue

La caméra 7 tournée de 18° vers le comptoir (à 90°, le comptoir sortait du cadre). Joins `~/Téléchargements/kebab_pour_A7_1_vue.png` puis `~/Téléchargements/kebab_pour_axes_plan-peint.png`, dans la conversation des fonds.

```
The first attached image is a rough 3D layout of one view of our kebab restaurant, made of simple flat-coloured volumes: it fixes the camera, the perspective, the framing and the place of every object. The second attached image is the same restaurant seen from above, painted in our style: it gives the art style, the materials, the colours and the objects. Paint exactly the view of the first image, as an empty background for an anime series: keep the same camera, the same perspective and framing, and every object at the same place, with the same size and angle, as if the layout had been painted over. The camera is seated on the red bench at the back of the restaurant and looks toward the street. Replace the simple volumes with the real objects:
- at the bottom of the frame, the near edge of our wooden table, with a red sauce bottle, a white sauce bottle and a napkin dispenser at the bottom left;
- the brown upright panels with red seats are empty wooden chairs: the two nearest ones belong to our table and face us;
- on the left edge, the red padded bench along the right side of the room, backed against a plain beige wall (a staircase is hidden behind that wall), with its two rectangular tables and their chairs;
- in the middle, the two rectangular wooden tables of the middle of the room, each with two chairs on each long side;
- on the right, the stainless steel counter seen from the side, with the glass salad display on top and, at its front end, the cash register; the light blue upright block next to it is the stack of folded glass panels of the shopfront;
- at the far end, the shopfront fully open onto the sunny street: the sidewalk, the tram rails with grass growing between them, and the plain facade of the building across the street (the dark bars are its windows); the band above the opening is the top of the shopfront;
- the large surface at the top is the ceiling.
Style: a flat 2D hand-drawn background painting from a 1990s anime film, in the style of the second image (clean dark outlines, flat cel shading, muted warm palette, painted details). NOT a 3D render, NOT photorealistic, and do not keep the flat colours of the layout. Light: the only daylight comes from the open shopfront at the far end; there are no other windows, the side walls are solid. The street is bright with warm morning sun; inside, the light is warm and dim, and the shadows of the tables and chairs fall toward the camera. No people. No text, no letters and no logos anywhere, including on the building across the street. Landscape format (1536×1024).
```

À contrôler à la reprise : le cadrage de la vue en volumes ; la table en bas et ses sauces ; les deux chaises face à nous ; la banquette et le mur à gauche, sans escalier ; les tables du milieu ; le comptoir, les salades et la caisse à droite ; la devanture ouverte, les rails et leur herbe ; aucune personne, aucun texte.

Résultat de A7, le 2026-10-17 : « pas mal », mais il manque l'escalier : la vue en volumes ne le montrait pas. L'auteur l'a dessiné sur la vue : la rampe monte au-dessus de la banquette, à gauche. Et dans la rue, de l'herbe sur la voie du tram, pas des pavés, et un arbre de plus. Le côté de l'escalier suit donc la pente des marches, sa rampe au-dessus (vue en volumes corrigée ; à l'axe 6, l'escalier touche le plafond et reste un mur), la caméra 7 un peu plus large (80°), la voie du tram en herbe, des arbres sur le trottoir d'en face. Capture hors du repo (`table-du-fond-contrechamp_essai-1_capture.png`).

### Prompt A7 v2 — Depuis la place de Sky, avec la rampe de l'escalier

Joins `~/Téléchargements/kebab_pour_A7_1_vue.png` (refaite) puis `~/Téléchargements/kebab_pour_axes_plan-peint.png`.

```
The first attached image is a rough 3D layout of one view of our kebab restaurant, made of simple flat-coloured volumes: it fixes the camera, the perspective, the framing and the place of every object. The second attached image is the same restaurant seen from above, painted in our style: it gives the art style, the materials, the colours and the objects. Paint exactly the view of the first image, as an empty background for an anime series: keep the same camera, the same perspective and framing, and every object at the same place, with the same size and angle, as if the layout had been painted over. The camera is seated on the red bench at the back of the restaurant and looks toward the street. Replace the simple volumes with the real objects:
- at the bottom of the frame, the near edge of our wooden table, with a white sauce bottle, a red sauce bottle and a napkin dispenser at the bottom left;
- the brown upright panels with red seats are empty wooden chairs: the two nearest ones belong to our table and face us;
- on the left, the red padded bench along the right side of the room; behind it, the side of the wooden staircase: closed below the steps, its top follows the slope of the stairs, and above it a wooden banister with its handrail goes up from the far end toward us and out of the top of the frame. We see the banister and the side of the stairs, not the steps themselves;
- in the middle, the rectangular wooden tables of the room, each with its chairs on both long sides;
- on the right, the stainless steel counter seen from the side, with the glass salad display on top and, at its front end, the cash register; the light blue upright block next to it is the stack of folded glass panels of the shopfront;
- at the far end, the shopfront fully open onto the sunny street: the sidewalk, then the tram track laid on a strip of green grass, with grass between and around the rails and no paving stones there; across the street, a row of trees along the sidewalk, and behind them the plain facade of a building (the dark bars are its windows); the band above the opening is the top of the shopfront;
- the large surface at the top is the ceiling.
Style: a flat 2D hand-drawn background painting from a 1990s anime film, in the style of the second image (clean dark outlines, flat cel shading, muted warm palette, painted details). NOT a 3D render, NOT photorealistic, and do not keep the flat colours of the layout. Light: the only daylight comes from the open shopfront at the far end; there are no other windows, the side walls are solid. The street is bright with warm morning sun; inside, the light is warm and dim, and the shadows of the tables and chairs fall toward the camera. No people. No text, no letters and no logos anywhere, including on the building across the street. Landscape format (1536×1024).
```

À contrôler à la reprise : la rampe de l'escalier qui monte vers nous au-dessus de la banquette, à gauche ; la voie du tram en herbe, sans pavés ; les arbres d'en face ; le comptoir et la caisse à droite ; les deux chaises face à nous ; aucune personne, aucun texte.

**Résultat de A7 v2, le 2026-10-17 : validé par l'auteur** (« on l'a »), rangé en `table-du-fond-contrechamp/fond_v1.png`, du premier coup avec la vue en volumes corrigée.

### Prompt A20 — La place de Patrick, au bout de la table

Trois images jointes, dans cet ordre : `~/Téléchargements/kebab_pour_A20_1_vue.png` (la vue en volumes), `~/Téléchargements/kebab_pour_axes_plan-peint.png`, et `~/Téléchargements/kebab_pour_A20_3_angle6.png` (le fond validé de l'axe 6 : le même coin, pour que la banquette, la plante et le mur soient les mêmes).

```
The first attached image is a rough 3D layout of one view of our kebab restaurant, made of simple flat-coloured volumes: it fixes the camera, the perspective, the framing and the place of every object. The second attached image is the same restaurant seen from above, painted in our style: it gives the art style, the materials and the objects. The third attached image is another view of the same corner of the restaurant, already painted and approved: the bench, the plant, the walls, the table and the light must look exactly the same. Paint exactly the view of the first image, as an empty background for an anime series: keep the same camera, the same perspective and framing, and every object at the same place, with the same size and angle, as if the layout had been painted over. The camera is seated at the left end of the table in the corner and looks along the table toward its far end. Replace the simple volumes with the real objects:
- at the bottom, our rectangular wooden table, seen from its near end and running away from us; in its middle, a red sauce bottle, a white sauce bottle and a napkin dispenser;
- at the far end of the table, the red padded bench of the right side of the room, empty: the seat at the head of the table;
- on the left, the red padded bench along the back wall, seen from its end, running to the corner, and above it, in the corner, the same large green potted plant as in the third image;
- on the right edge, the back of an empty wooden chair with a red seat;
- behind the far bench, a plain beige wall: the side of the staircase, which goes up behind it, out of sight; at the top right, only the top of a wooden banister shows.
Style: a flat 2D hand-drawn background painting from a 1990s anime film, in the style of the second and third images (clean dark outlines, flat cel shading, muted warm palette, painted details). NOT a 3D render, NOT photorealistic, and do not keep the flat colours of the layout. Light: the only daylight comes from the open shopfront, out of frame on the right; there are no windows; the light is warm and dim, as in the third image, and the shadows fall to the left. No people. No text, no letters and no logos anywhere. Landscape format (1536×1024).
```

À contrôler à la reprise : la table vue de son bout ; la banquette vide au bout, la place de Patrick ; la banquette du fond à gauche et la même plante que l'axe 6 ; le dossier d'une chaise à droite ; le mur derrière, sans escalier visible, juste le haut d'une rampe ; la lumière de droite ; aucune personne, aucun texte.

**Résultat de A20, le 2026-10-17 : validé par l'auteur du premier coup.** Le fond de l'axe 6 joint en troisième image a gardé la même plante, la même banquette, le même mur.

### Prompt A21 — Depuis la place de Patrick

Trois images jointes, dans cet ordre : `~/Téléchargements/kebab_pour_A21_1_vue.png`, `~/Téléchargements/kebab_pour_axes_plan-peint.png`, `~/Téléchargements/kebab_pour_A21_3_angle6.png` (le fond de l'axe 6 : la même banquette, le même miroir).

```
The first attached image is a rough 3D layout of one view of our kebab restaurant, made of simple flat-coloured volumes: it fixes the camera, the perspective, the framing and the place of every object. The second attached image is the same restaurant seen from above, painted in our style: it gives the art style, the materials and the objects. The third attached image is another view of the same table and bench, already painted and approved: the bench, the mirror, the walls, the table and the light must look exactly the same. Paint exactly the view of the first image, as an empty background for an anime series: keep the same camera, the same perspective and framing, and every object at the same place, with the same size and angle, as if the layout had been painted over. The camera is seated at the head of the table, on the bench in the corner, and looks along the table toward the other side of the restaurant. Replace the simple volumes with the real objects:
- at the bottom, our rectangular wooden table, seen from its end and running away from us, with a red sauce bottle, a white sauce bottle and a napkin dispenser;
- on the right, the red padded bench along the back wall, empty, running away from us, and above it, on the wall, the long dark smoky mirror of the third image, with no recognisable reflection;
- at the far end of the bench, a large green potted plant, and in the far corner, the tall drinks fridge with glass doors;
- on the left edge, a rectangular wooden table of the middle of the room with its chairs;
- in the middle distance, the stainless steel counter seen from the side, with the glass salad display on top; behind it, against the far wall, the kitchen: the vertical kebab spit (the brown block), its hood above (the grey block), and a round clock on the wall (the small light square);
- the large surface at the top is the ceiling.
Style: a flat 2D hand-drawn background painting from a 1990s anime film, in the style of the second and third images (clean dark outlines, flat cel shading, muted warm palette, painted details). NOT a 3D render, NOT photorealistic, and do not keep the flat colours of the layout. Light: the only daylight comes from the open shopfront, out of frame on the left; there are no windows; the light is warm and dim, as in the third image, and the shadows fall to the right. No people. No text, no letters and no logos anywhere, including on the clock and the counter. Landscape format (1536×1024).
```

À contrôler à la reprise : la table vue de son bout ; la banquette du fond et le même miroir fumé à droite ; la plante et le frigo au fond ; le comptoir, les salades, la broche, la hotte et l'horloge ; la lumière de gauche ; aucune personne, aucun texte.

**Résultat de A21, le 2026-10-17 : validé par l'auteur du premier coup.**

### Prompt A8 — Le comptoir, vu de la salle

La caméra 8 reculée entre les deux tables du milieu, un peu inclinée vers le bas (de trop près, la vitrine des salades bouchait tout). Trois images jointes, dans cet ordre : `~/Téléchargements/kebab_pour_A8_1_vue.png`, `~/Téléchargements/kebab_pour_axes_plan-peint.png`, `~/Téléchargements/kebab_pour_A8_3_angle21.png` (le fond de l'axe 21 : le même comptoir, la même broche, la même horloge, le même frigo).

```
The first attached image is a rough 3D layout of one view of our kebab restaurant, made of simple flat-coloured volumes: it fixes the camera, the perspective, the framing and the place of every object. The second attached image is the same restaurant seen from above, painted in our style: it gives the art style, the materials and the objects. The third attached image is another view of the same counter and kitchen, already painted and approved: the counter, the salad display, the kebab spit, the hood, the clock, the fridge, the walls and the light must look exactly the same. Paint exactly the view of the first image, as an empty background for an anime series: keep the same camera, the same perspective and framing, and every object at the same place, with the same size and angle, as if the layout had been painted over. The camera stands in the dining room, between two tables, and looks at the counter. Replace the simple volumes with the real objects:
- in the foreground, the backs of empty wooden chairs with red seats, at the bottom left and the bottom right, and the corner of a wooden table at the bottom right;
- across the middle of the frame, the long stainless steel counter, its customer side facing us; on top, the glass refrigerated salad display, with trays of lettuce, tomatoes, onions, red cabbage, carrots and cucumbers, and the sauces;
- at the left end of the counter, the cash register, its back turned to us: its screen faces the cook's side, behind the counter; next to it, a large green plant;
- behind the counter, against the far wall: the vertical kebab spit (the brown block) in front of its grill, the stainless steel hood above it (the grey block), and a round clock on the wall (the small light square);
- on the right, the corner with the back wall and the tall drinks fridge with glass doors;
- the surface at the top is the ceiling.
Style: a flat 2D hand-drawn background painting from a 1990s anime film, in the style of the second and third images (clean dark outlines, flat cel shading, muted warm palette, painted details). NOT a 3D render, NOT photorealistic, and do not keep the flat colours of the layout. Light: the only daylight comes from the open shopfront, out of frame on the left; there are no windows; the light is warm and dim, as in the third image, and the shadows fall to the right. No people. No text, no letters and no logos anywhere, including on the clock, the counter and the cash register. Landscape format (1536×1024).
```

À contrôler à la reprise : le comptoir de face, la vitrine des salades ; la caisse à gauche, le dos tourné vers nous ; la broche, la hotte, l'horloge derrière ; le frigo à droite ; les mêmes que l'axe 21 ; aucune personne, aucun texte.

L'auteur redessine l'axe 8 sur le plan, le 2026-10-17 : la caméra derrière la première table du milieu, vers le fond gauche, du bout du comptoir au frigo. Le prompt A8 ci-dessus, non envoyé, est remplacé.

### Prompt A8 v2 — Le comptoir et la cuisine, vers le frigo

Les mêmes trois images : `~/Téléchargements/kebab_pour_A8_1_vue.png` (refaite), `~/Téléchargements/kebab_pour_axes_plan-peint.png`, `~/Téléchargements/kebab_pour_A8_3_angle21.png`.

```
The first attached image is a rough 3D layout of one view of our kebab restaurant, made of simple flat-coloured volumes: it fixes the camera, the perspective, the framing and the place of every object. The second attached image is the same restaurant seen from above, painted in our style: it gives the art style, the materials and the objects. The third attached image is another view of the same counter and kitchen, already painted and approved: the counter, the kebab spit, the hood, the clock, the fridge, the plant, the walls and the light must look exactly the same. Paint exactly the view of the first image, as an empty background for an anime series: keep the same camera, the same perspective and framing, and every object at the same place, with the same size and angle, as if the layout had been painted over. The camera stands in the dining room and looks toward the kitchen and the back corner. Replace the simple volumes with the real objects:
- on the left, in the foreground, the stainless steel counter seen from its back end: the end close to us is where the food is handed over, and its long side runs away to the left; at the far left edge, the end of the glass salad display;
- behind the counter, against the far wall: the kitchen worktops, the vertical kebab spit (the brown block) in front of its grill, the stainless steel hood above it (the grey block), and a round clock on the wall (the small light square);
- on the right, the back corner of the room: the tall drinks fridge with glass doors facing us, full of bottles, and in front of it a large green potted plant;
- in the middle, the tiled floor; at the top, the ceiling.
Style: a flat 2D hand-drawn background painting from a 1990s anime film, in the style of the second and third images (clean dark outlines, flat cel shading, muted warm palette, painted details). NOT a 3D render, NOT photorealistic, and do not keep the flat colours of the layout. Light: the only daylight comes from the open shopfront, out of frame on the left, behind; there are no windows; the light is warm and dim, as in the third image, and the shadows fall to the right. No people. No text, no letters and no logos anywhere, including on the clock, the fridge and the counter. Landscape format (1536×1024).
```

À contrôler à la reprise : le bout du comptoir en premier plan à gauche ; la broche, la hotte, l'horloge derrière ; le frigo et la plante à droite ; les mêmes que l'axe 21 ; aucune personne, aucun texte.

Résultat de A8 v2, le 2026-10-17 : le bon angle. L'auteur relève : l'horloge est un carré blanc, la sienne est ronde ; la vitrine des salades est posée au fond, elle doit être sur le comptoir en inox. Capture hors du repo (`comptoir_essai-1_capture.png`).

### Prompt A8 v2 retouche — L'horloge, la vitrine des salades

Dans la case « Décrivez les modifications » de l'image.

```
Edit ONLY this image. Keep everything else exactly as it is: the same view, the same counter, kitchen, kebab spit, hood, fridge, plant, style and light. Make only these two changes:
1. The plain white square on the wall, to the left of the hood: replace it with a round wall clock, with a light face, a dark round frame, two hands and simple tick marks, no numbers and no text.
2. The glass refrigerated salad display: it stands on top of the stainless steel counter in the foreground, along its long side, from the left edge of the frame to about the middle of that counter, with its trays of lettuce, tomatoes, onions, red cabbage, carrots and cucumbers under the glass. Remove it from the back worktop.
```

À contrôler à la reprise : une horloge ronde, sans chiffres ; la vitrine sur le comptoir du premier plan ; rien d'autre de changé.

Résultat de la retouche A8 v2, le 2026-10-17 : « on se rapproche ». L'horloge est ronde, la vitrine sur le comptoir. Mais la ligne du plafond plonge vers le coin (la caméra de biais par rapport au mur de la cuisine), et la vitrine va trop à droite : il ne reste plus de place libre sur le comptoir (la place de la théière de Patrick). La caméra 8 passe de face au mur de la cuisine, un peu reculée, à l'horizontale, pour garder le frigo et la plante. Capture hors du repo (`comptoir_essai-2_capture.png`).

### Prompt A8 v3 — Le comptoir, le mur de la cuisine de face

Les mêmes trois images : `~/Téléchargements/kebab_pour_A8_1_vue.png` (refaite), `~/Téléchargements/kebab_pour_axes_plan-peint.png`, `~/Téléchargements/kebab_pour_A8_3_angle21.png`.

```
The first attached image is a rough 3D layout of one view of our kebab restaurant, made of simple flat-coloured volumes: it fixes the camera, the perspective, the framing and the place of every object. The second attached image is the same restaurant seen from above, painted in our style: it gives the art style, the materials and the objects. The third attached image is another view of the same counter and kitchen, already painted and approved: the counter, the kebab spit, the hood, the round clock, the fridge, the plant, the walls and the light must look exactly the same. Paint exactly the view of the first image, as an empty background for an anime series: keep the same camera, the same perspective and framing, and every object at the same place, with the same size and angle, as if the layout had been painted over. The camera stands in the dining room, level, facing the kitchen wall squarely: the line where the ceiling meets the kitchen wall is straight and horizontal. Replace the simple volumes with the real objects:
- in the foreground, the stainless steel counter: its long side runs across the frame, and its end is on the right, near us; at the bottom left, the top of the back of an empty wooden chair;
- the coloured patches on the top of the counter, on its left part only, are the trays of the refrigerated salad display, built into the stainless steel counter top itself, flush with it: lettuce, tomatoes, onions, red cabbage, carrots and cucumbers; above them, along the customer side, a low glass sneeze guard (the light blue outline). The salad display is part of this front counter, not on the back worktop. The right part of the counter top, up to its end, stays clear and empty;
- behind the counter, against the kitchen wall: the kitchen worktops, the vertical kebab spit (the brown block) in front of its grill, the stainless steel hood above it (the grey block), and a round wall clock with a light face and a dark frame, no numbers (the small light square);
- on the right, the back corner of the room: the tall drinks fridge with glass doors facing us, full of bottles, and in front of it a large green potted plant;
- in the middle, the tiled floor; at the top, the ceiling.
Style: a flat 2D hand-drawn background painting from a 1990s anime film, in the style of the second and third images (clean dark outlines, flat cel shading, muted warm palette, painted details). NOT a 3D render, NOT photorealistic, and do not keep the flat colours of the layout. Light: the only daylight comes from the open shopfront, out of frame on the left, behind; there are no windows; the light is warm and dim, as in the third image, and the shadows fall to the right. No people. No text, no letters and no logos anywhere, including on the clock, the fridge and the counter. Landscape format (1536×1024).
```

À contrôler à la reprise : la ligne du plafond droite ; la vitrine encastrée dans le comptoir du premier plan, sur sa partie gauche seulement, pas sur le plan de travail du fond ; le bout du comptoir libre ; l'horloge ronde ; la broche, la hotte ; le frigo et la plante à droite ; aucune personne, aucun texte.

L'auteur, avant d'envoyer A8 v3, le 2026-10-17 : dans la vue en volumes, la vitrine (un bloc bleu posé en retrait) a l'air derrière le comptoir, « ça va refaire le même bug ». Corrigé : la vitrine est encastrée dans le comptoir, les bacs de couleur à fleur du dessus, une vitre basse en contour seulement, côté salle. Le prompt A8 v3 ci-dessus est mis à jour en conséquence.

Résultat de A8 v3, le 2026-10-17 : « c'est mieux ». La ligne du plafond droite, la vitrine encastrée dans le comptoir, le bout libre. À corriger : ChatGPT a fait l'horloge ronde et, à côté, un carré (le carré de la vue en volumes) ; et il a ajouté des blocs de cuisine gris à gauche. La vue en volumes dessine désormais l'horloge ronde. Capture hors du repo (`comptoir_essai-3_capture.png`).

### Prompt A8 v3 retouche — L'horloge à la place du carré, sans les blocs de gauche

Dans la case « Décrivez les modifications » de l'image.

```
Edit ONLY this image. Keep everything else exactly as it is: the same view, the same counter, salad trays, kebab spit, hood, fridge, plant, style and light. Make only these two changes:
1. Remove the plain grey square panel on the wall, and move the round clock to exactly where that square was, between its current place and the hood. Only one clock, no square.
2. On the left, remove the grey kitchen appliances and the stacks on top of them, behind the salad display: there is only the plain wall and the back worktop there, as on the rest of the wall.
```

À contrôler à la reprise : une seule horloge ronde, à la place du carré ; plus de blocs gris à gauche ; rien d'autre de changé.

**Résultat de la retouche A8 v3, le 2026-10-17 : validé par l'auteur.** Une seule horloge ronde, plus de blocs gris. Leçon : tout ce que la vue en volumes dessine, ChatGPT le peint ; un objet doit y avoir sa vraie forme (l'horloge ronde, la vitrine encastrée), sinon il en fait un deuxième.

### Prompt A2 — L'entrée, toute la salle depuis le trottoir

La caméra 2 sur le trottoir, côté gauche, un peu tournée vers le comptoir, champ large : la caisse en premier plan, toute la salle, la rampe de l'escalier à droite. Quatre images jointes, dans cet ordre : `~/Téléchargements/kebab_pour_A2_1_vue.png`, `~/Téléchargements/kebab_pour_axes_plan-peint.png`, `~/Téléchargements/kebab_pour_A2_3_angle7.png` (le fond de l'axe 7), `~/Téléchargements/kebab_pour_A2_4_angle8.png` (le fond de l'axe 8).

```
The first attached image is a rough 3D layout of one view of our kebab restaurant, made of simple flat-coloured volumes: it fixes the camera, the perspective, the framing and the place of every object. The second attached image is the same restaurant seen from above, painted in our style: it gives the art style, the materials and the objects. The third and fourth attached images are two other views of the same restaurant, already painted and approved: the tables, chairs, bench, banister, counter, salad trays, kebab spit, hood, round clock, fridge, plants, walls and light must look exactly the same. Paint exactly the view of the first image, as an empty background for an anime series: keep the same camera, the same perspective and framing, and every object at the same place, with the same size and angle, as if the layout had been painted over. The camera stands on the sidewalk, in front of the fully open shopfront, and looks into the restaurant. Replace the simple volumes with the real objects:
- on the left, the L-shaped stainless steel counter: in the foreground its short front side, plain and clear; at the corner of the L, at the near end of the long side, the cash register (the dark block), its screen turned toward the inside of the counter, where the cook stands, its back to the dining room; then, further along the long side running away from us, the salad trays built into its top and a low glass sneeze guard;
- behind the counter, on the left wall: the kitchen worktops, the vertical kebab spit (the brown block), the stainless steel hood (the grey block) and the round clock;
- in the back left corner, the tall drinks fridge with glass doors and a large green plant;
- on the back wall, the long dark smoky mirror above the red padded bench, which runs along the back wall and turns in the back right corner to come toward us along the right side; a large plant stands in that corner;
- the rectangular wooden tables with their chairs: two in the middle of the room, one in the corner of the bench, and others along the right bench; on each table a red sauce bottle, a white sauce bottle and a napkin dispenser;
- at the top right, the side of the wooden staircase with its banister, going up toward the back;
- the large surface at the top is the ceiling, plain and flat, the same colour as in the other views.
Style: a flat 2D hand-drawn background painting from a 1990s anime film, in the style of the other images (clean dark outlines, flat cel shading, muted warm palette, painted details). NOT a 3D render, NOT photorealistic, and do not keep the flat colours of the layout. Light: warm morning sunlight comes from the street, behind the camera, through the open shopfront, and falls on the floor in long warm patches; the shadows of the tables and chairs point toward the back wall. There are no other windows; the side walls are solid. No people. No text, no letters and no logos anywhere, including on the clock, the counter and the cash register. Landscape format (1536×1024).
```

À contrôler à la reprise : la caisse à l'angle du L, juste avant les salades, tournée vers la cuisine ; le comptoir en L, la vitrine encastrée ; la cuisine, l'horloge ronde ; le frigo ; le miroir fumé au-dessus de la banquette en L ; la table de Sky dans l'angle ; la rampe en haut à droite ; un plafond uni (pas un ciel) ; les ombres vers le fond ; aucune personne, aucun texte.

L'auteur, sur la vue en volumes de l'axe 2, avant de l'envoyer, le 2026-10-17 : la caisse à l'angle du L, au bout du grand côté, juste avant les salades (il l'a entourée en rouge). Plan v7, vue en volumes et prompt A2 mis à jour.

Résultat de A2, le 2026-10-17 : « pas mal ». La caisse à l'angle, le comptoir, la cuisine, le frigo, le miroir, la banquette, les tables, la rampe. L'auteur relève : la plante de droite n'est pas la bonne (pas celle de l'axe 6 : un pot brun et des feuilles de palmier) ; il manque la porte en haut de l'escalier. Claude relève aussi, sans le corriger : le miroir laisse voir un reflet un peu net (une forme de porte, des arbres). Capture hors du repo (`entree_essai-1_capture.png`).

### Prompt A2 retouche — La plante de l'angle, la porte en haut de l'escalier

Dans la case « Décrivez les modifications » de l'image.

```
Edit ONLY this image. Keep everything else exactly as it is: the same view, the same counter, kitchen, tables, chairs, bench, mirror, style and light. Make only these two changes:
1. The plant in the back right corner, behind the corner of the red bench: replace it with a large plant with broad, pointed, dark green leaves streaked with light green, in a plain grey metal pot, standing behind the corner of the bench, its leaves rising above the backrest against the two walls.
2. At the top right, where the wooden staircase reaches the top at the back: add a plain closed wooden door with a metal handle at the head of the stairs, the entrance of the office upstairs, with no sign and no text.
```

À contrôler à la reprise : la plante de l'angle, larges feuilles striées, pot gris ; la porte en bois en haut de l'escalier, sans texte ; rien d'autre de changé.

Résultat de la retouche A2, le 2026-10-17 : la plante est la bonne, mais posée trop haut ; la porte est en l'air, au-dessus du plafond, l'angle complètement faux (l'auteur). Claude : depuis le trottoir, la porte, à l'étage, est cachée par le plafond ; la rampe qui monte dans le plafond, comme au premier essai, est juste. La porte se montrera aux axes 10 et 11. Capture hors du repo (`entree_essai-2_capture.png`).

### Prompt A2 retouche 2 — Sans la porte, la plante plus bas

Dans la case « Décrivez les modifications » de la dernière image.

```
Edit ONLY this image. Keep everything else exactly as it is: the same view, the same counter, kitchen, tables, chairs, bench, mirror, style and light. Make only these two changes:
1. At the top right, remove the floating door and the posts around it. The door is upstairs, at the head of the staircase, and from here it is hidden: the wooden banister and the side of the staircase go up toward the back and hide the top of the stairs and the door. We see only the banister, rising and disappearing into the ceiling.
2. The plant in the back right corner: lower it so that its grey pot is hidden behind the backrest of the red bench, standing on the floor in the corner; only its leaves rise above the backrest, against the two walls.
```

À contrôler à la reprise : plus de porte, la rampe qui entre dans le plafond ; le pot de la plante caché derrière le dossier, seules les feuilles dépassent ; rien d'autre de changé.

L'auteur, avant d'envoyer la retouche 2, le 2026-10-17 : la porte est à l'étage, en haut de l'escalier, comme sur le plan peint ; depuis l'entrée, c'est la rampe de droite qui la cache. Le point 1 de la retouche 2 le dit ainsi.

Résultat de la retouche 2 de A2, le 2026-10-17 : plus de porte en l'air, la plante plus bas. L'auteur veut quand même voir qu'il y a la porte en haut : « que le mur se creuse », en haut à droite. Claude : de face, depuis le trottoir, le plafond cache l'étage, la porte ne peut pas se voir en vrai ; c'est une triche de décor, courante dans les animes, limitée au coin en haut à droite. À l'axe 10 et 11, la porte se verra pour de bon.

### Prompt A2 retouche 3 — La trémie de l'escalier, la porte en haut

Dans la case « Décrivez les modifications » de la dernière image.

```
Edit ONLY the top right corner of this image. Keep everything else exactly as it is: the same view, counter, kitchen, tables, chairs, bench, mirror, plant, style and light. In the top right corner, above the wooden staircase and its banister: cut an opening into the ceiling, a stairwell going up to the floor above. Through that opening we see the last steps of the wooden staircase continuing up, and at the top, on the small landing of the upper floor, a plain closed wooden door with a metal handle, in soft shadow. No sign and no text on the door. The opening is the same warm wall colour inside, with a wooden edge.
```

À contrôler à la reprise : une ouverture dans le plafond au-dessus de l'escalier, les dernières marches et la porte en haut ; le reste inchangé.

**Résultat de la retouche 2 de A2, le 2026-10-17 : validé par l'auteur**, sans enthousiasme pour l'angle. La retouche 3 (la trémie) n'a pas été envoyée : l'auteur voulait la porte au bout de l'escalier, dans son mur, pas dans le plafond ; elle se voit à l'axe 11.

### Prompt A11 — Du palier, l'escalier qui monte à la porte de Datastream

La vue en volumes validée par l'auteur. Trois images jointes, dans cet ordre : `~/Téléchargements/kebab_pour_A11_1_vue.png`, `~/Téléchargements/kebab_pour_axes_plan-peint.png`, `~/Téléchargements/kebab_pour_A11_3_angle2.png` (le fond de l'axe 2 : le même escalier, la même rampe).

```
The first attached image is a rough 3D layout of one view of our kebab restaurant, made of simple flat-coloured volumes: it fixes the camera, the perspective, the framing and the place of every object. The second attached image is the same restaurant seen from above, painted in our style: it gives the art style, the materials and the objects. The third attached image is another view of the same restaurant, already painted and approved: the wooden staircase, its banister, the walls, the red bench and the light must look exactly the same. Paint exactly the view of the first image, as an empty background for an anime series: keep the same camera, the same perspective and framing, and every object at the same place, with the same size and angle, as if the layout had been painted over. The camera stands on the small landing at the bottom of the staircase and looks up the stairs. Replace the simple volumes with the real objects:
- in the middle, the straight wooden staircase going up away from us, step after step, worn wood that creaks;
- on the left, the wooden banister with its handrail and its balusters, going up along the stairs; below it and beyond it, a glimpse of the restaurant: the red padded bench and the long dark smoky mirror on the back wall;
- on the right, the plain warm wall of the stairwell, going up;
- at the top of the stairs, at the far end, a small landing and, in the wall at the end, a plain closed wooden door with a metal handle: the door of the office upstairs, with no sign and no text;
- above, the ceiling of the stairwell.
Style: a flat 2D hand-drawn background painting from a 1990s anime film, in the style of the second and third images (clean dark outlines, flat cel shading, muted warm palette, painted details). NOT a 3D render, NOT photorealistic, and do not keep the flat colours of the layout. Light: warm morning daylight comes from the street, behind the camera, and lights the lower steps; the stairwell gets dimmer as it goes up, and the door at the top is in soft shadow. No people. No text, no letters and no logos anywhere. Landscape format (1536×1024).
```

À contrôler à la reprise : l'escalier droit qui monte, la rampe à gauche, le mur à droite ; la porte au bout, en haut, dans son mur, sans texte ; un aperçu de la banquette et du miroir à gauche ; la lumière de derrière, plus sombre en haut ; aucune personne, aucun texte.

Résultat de A11, le 2026-10-17 : « pas mal ». L'escalier, la porte au bout, le mur à droite, la banquette et le miroir à gauche. Reste, pour l'auteur : la rampe est coupée en bas (un poteau isolé et une autre main courante au premier plan) ; elle doit descendre proprement jusqu'en bas. Capture hors du repo (`escalier-vers-datastream_essai-1_capture.png`).

### Prompt A11 retouche — La rampe d'un seul tenant jusqu'en bas

Dans la case « Décrivez les modifications » de l'image.

```
Edit ONLY this image. Keep everything else exactly as it is: the same view, the same stairs, door, walls, bench, mirror, style and light. Make only this change: the wooden banister on the left must be one continuous banister, from the top of the stairs down to the bottom step. Its handrail follows the slope of the stairs without any break, and ends at the bottom on a single newel post standing on the first step, at the bottom left. Remove the separate short railing and the extra post in the foreground at the bottom left.
```

À contrôler à la reprise : une seule rampe, d'un seul tenant, du haut jusqu'au poteau de la première marche ; plus de bout de rampe isolé au premier plan ; rien d'autre de changé.

**Résultat de la retouche A11, le 2026-10-17 : validé par l'auteur.**

### Prompt A10 — Le pied de l'escalier, vu de la salle

La caméra 10 replacée : l'ancienne regardait le mur de droite. Du devant de la salle, près de la devanture, vers le palier : on voit descendre Daria, Théo, Vincent. La vue en volumes a maintenant une main courante en pente et un poteau en bas. Quatre images jointes, dans cet ordre : `~/Téléchargements/kebab_pour_A10_1_vue.png`, `~/Téléchargements/kebab_pour_axes_plan-peint.png`, `~/Téléchargements/kebab_pour_A10_3_angle11.png` (le fond de l'axe 11 : le même escalier, la même rampe), `~/Téléchargements/kebab_pour_A10_4_angle7.png` (le fond de l'axe 7 : la même rue, la même banquette, les mêmes tables).

```
The first attached image is a rough 3D layout of one view of our kebab restaurant, made of simple flat-coloured volumes: it fixes the camera, the perspective, the framing and the place of every object. The second attached image is the same restaurant seen from above, painted in our style: it gives the art style, the materials and the objects. The third and fourth attached images are two other views of the same restaurant, already painted and approved: the wooden staircase, its banister, the red bench, the tables, chairs, walls, the street and the light must look exactly the same. Paint exactly the view of the first image, as an empty background for an anime series: keep the same camera, the same perspective and framing, and every object at the same place, with the same size and angle, as if the layout had been painted over. The camera stands in the front of the dining room, near the open shopfront, and looks toward the bottom of the staircase. Replace the simple volumes with the real objects:
- in the foreground, a rectangular wooden table with its chairs, a red sauce bottle, a white sauce bottle and a napkin dispenser, its short end against the red padded bench;
- the red padded bench runs from the left to the middle of the frame, along the side of the staircase, and ends there;
- above and behind the bench, the wooden staircase comes down toward us from the top left: its side is closed below the steps, a plain warm wall; its wooden banister follows the slope without a break, with its balusters, down to a single newel post at the bottom step;
- at the bottom of the stairs, on the right of the bench end, a small wooden landing on the floor, with a large green potted plant in its far corner;
- the plain warm wall on the right of the landing; at the far right, the open shopfront and the sunny street: the sidewalk, then the tram track on its strip of grass, as in the fourth image;
- the surface at the top is the ceiling, plain and flat.
Style: a flat 2D hand-drawn background painting from a 1990s anime film, in the style of the other images (clean dark outlines, flat cel shading, muted warm palette, painted details). NOT a 3D render, NOT photorealistic, and do not keep the flat colours of the layout. Light: warm morning sunlight comes from the open shopfront on the right; the shadows fall to the left; there are no other windows. No people. No text, no letters and no logos anywhere. Landscape format (1536×1024).
```

À contrôler à la reprise : l'escalier qui descend vers nous, la rampe d'un seul tenant jusqu'au poteau ; la banquette qui s'arrête ; le palier en bois et sa plante ; la rue à droite, la voie en herbe ; la table au premier plan ; un plafond uni ; aucune personne, aucun texte.

**Résultat de A10, le 2026-10-17 : validé par l'auteur du premier coup.** L'escalier manque de profondeur, sans gêne pour un plan fixe (les persos qui descendent se posent en bas des marches ou sur le palier : pas de gros gestes, CLAUDE.md).

### Prompt A1 — L'extérieur, la façade depuis le trottoir d'en face

L'auteur : « faire simple, la baie vitrée vue depuis la rue, sur le trottoir d'en face, et basta ». La rue est élargie dans la vue en volumes (le trottoir d'en face, puis l'immeuble d'en face, plus loin) pour que la caméra ait du recul. Quatre images jointes, dans cet ordre : `~/Téléchargements/kebab_pour_A1_1_vue.png`, `~/Téléchargements/kebab_pour_axes_plan-peint.png`, `~/Téléchargements/kebab_pour_A1_3_angle7.png` (le fond de l'axe 7 : la même rue, les mêmes arbres, la même voie en herbe), `~/Téléchargements/kebab_pour_A1_4_angle2.png` (le fond de l'axe 2 : la même salle).

```
The first attached image is a rough 3D layout of one view of our kebab restaurant, made of simple flat-coloured volumes: it fixes the camera, the perspective, the framing and the place of every object. The second attached image is the same restaurant seen from above, painted in our style: it gives the art style, the materials and the objects. The third and fourth attached images are two views already painted and approved: the street, the trees, the grass tram track, the interior of the restaurant and the light must look exactly the same. Paint exactly the view of the first image, as an empty background for an anime series: keep the same camera, the same perspective and framing, and every object at the same place, with the same size and angle, as if the layout had been painted over. The camera stands on the opposite sidewalk, under the trees, and looks across the street at the building, slightly upward. Replace the simple volumes with the real objects:
- the building: a small, plain three-level building in a French town, warm beige rendered walls; on the upper floors, regular tall windows with simple frames (the grey rectangles), the office of a small company on the first floor; no balconies, no sign;
- on the ground floor, across the whole width, the shopfront of the kebab restaurant, fully open: its folding glass panels are folded together at the left end (the light blue upright block); above the opening, a plain dark wooden fascia band, with no sign and no letters;
- through the open shopfront, the inside of the restaurant, as in the fourth image: on the left, the stainless steel counter with the cash register and the salad display, the kebab spit and the hood behind; at the back, the long dark smoky mirror above the red bench; the tables and chairs; on the right, the wooden staircase going up; large green plants in the corners;
- on both sides, the neighbouring buildings, with their ground floors closed (the dark grey rectangles are plain shutters);
- in front of the building, the sidewalk, and in the foreground the tram track laid on a strip of green grass, with grass between and around the rails;
- in the top corners, the leaves of the trees of the sidewalk where the camera stands.
Style: a flat 2D hand-drawn background painting from a 1990s anime film, in the style of the other images (clean dark outlines, flat cel shading, muted warm palette, painted details). NOT a 3D render, NOT photorealistic, and do not keep the flat colours of the layout. Light: warm morning sunlight on the facade; the inside of the restaurant is warm and a little darker. No people. No text, no letters, no logos and no numbers anywhere: no sign, no shop names, no street signs. Landscape format (1536×1024).
```

À contrôler à la reprise : trois niveaux, la devanture grande ouverte sur toute la largeur, les panneaux repliés à gauche ; la salle dedans, comme à l'axe 2 ; le bandeau sans enseigne ; la voie du tram en herbe au premier plan ; les feuilles des arbres en haut ; aucune personne, aucun texte.

L'enseigne, si l'auteur en veut une, se pose en code au montage (`image/gabarits/`), comme tout texte à l'écran.

Résultat de A1, le 2026-10-17 : « pas mal du tout, c'est propre ». Mais l'auteur voyait plutôt un immeuble un peu moderne : des baies vitrées teintées aux étages, une enseigne « KEBAB » assez grande au-dessus de la devanture, et un panneau « DATASTREAM » sur la façade vitrée, entre les deux étages. Claude : les deux panneaux se peignent vides, les lettres se posent en code (CLAUDE.md : les modèles déforment le texte ; le modèle local repassera sur l'image). Capture de cette première version hors du repo (`exterieur_essai-1_capture.png`).

### Prompt A1 retouche — L'immeuble moderne, les deux enseignes vides

Dans la case « Décrivez les modifications » de l'image.

```
Edit ONLY the upper part of the building in this image. Keep everything else exactly as it is: the same view, the same ground floor, the open shopfront and everything inside the restaurant, the neighbouring buildings, the sidewalk, the grass tram track, the trees, the style and the light. Make only these three changes:
1. The two floors above the restaurant become a simple modern facade: large tinted glass panels, dark blue-grey, in thin dark metal frames, from one side of the building to the other, on both floors; the glass reflects the sky and the trees softly, and we cannot see inside.
2. Above the open shopfront, replace the wooden fascia band with a clean sign box across the shopfront, light coloured, with nothing written on it: a blank sign.
3. On the glass facade, at the level between the first and the second floor, a long horizontal sign panel across the building, dark, with nothing written on it: a blank sign.
No letters, no words, no logos anywhere.
```

À contrôler à la reprise : les deux étages en verre teinté, cadres fins ; l'enseigne vide au-dessus de la devanture ; le panneau vide entre les étages ; le rez-de-chaussée, la salle, la rue et les arbres inchangés.

**Résultat de la retouche A1, le 2026-10-17 : validé par l'auteur** (« parfait »). Les enseignes vides reçoivent leurs lettres en code : `pipeline/enseignes.py` (Lato Black ; KEBAB rouge sombre sur le caisson clair, DATASTREAM crème sur le bandeau sombre ; les feuilles restent devant les lettres, les ombres des feuilles passent dessus).

### Prompt A1 fermé — La devanture fermée, même lumière

Le premier des fonds « rideau fermé » : les panneaux vitrés dépliés sur toute la devanture, la porte au milieu (`axes.md`, « Le rideau de verre fermé »). Retouche de l'image validée de l'axe 1, dans sa conversation, case « Décrivez les modifications ». La pluie et la nuit viendront ensuite, à partir de cette version.

```
Edit ONLY the shopfront on the ground floor of this image. Keep everything else exactly as it is: the same view, the glass floors above, the two blank signs, the neighbouring buildings, the sidewalk, the grass tram track, the trees, the style and the light. Make only this change: the shopfront is now closed. The folding glass panels that are folded together at the left end are unfolded across the whole width of the shopfront, from the left end to the right end: a row of tall, clear glass panels in thin dark metal frames, from the floor up to the sign box. The panel in the middle is the entrance door, the same glass and frame as the others, with a long vertical metal handle. Through the clean glass we still see the inside of the restaurant exactly as now, a little darker, with soft reflections of the trees and the street on the glass. No letters, no words, no logos anywhere, not even on the glass or the door.
```

À contrôler à la reprise : les panneaux sur toute la largeur, du sol au caisson ; la porte au milieu, sa poignée ; la salle visible derrière le verre, la même ; les reflets doux ; le reste inchangé ; aucun texte.

**Résultat de A1 fermé, le 2026-10-17 : validé par l'auteur du premier coup** (`exterieur/fond_ferme_v1.png`). Les enseignes se posent aux mêmes positions que sur `fond_v1`.

### Prompt A1 pluie — La devanture fermée sous la pluie

Retouche de l'image fermée, dans la même conversation. Seuls le temps et la lumière changent (Navier-Stokes : « Jeudi matin. Il pleut », la pluie qui fait un bruit de friture sur la vitrine).

```
Edit ONLY the weather and the light of this image. Keep everything exactly where it is: the same view, the same building, the closed glass shopfront and its door, the two blank signs, the inside of the restaurant, the neighbouring buildings, the sidewalk, the tram track and the trees. Make only this change: it is a grey, rainy morning with heavy rain. The sky is overcast and grey; there is no sunlight and no leaf shadows anymore. Rain falls in thin slanted streaks across the whole image; drops and trickles of water run down the glass of the shopfront and of the upper floors; the sidewalk is wet and shiny, with small puddles reflecting the warm light of the restaurant; the grass of the tram track is dark and wet; the leaves of the trees are darker and drip. Inside, the restaurant is lit by its warm ceiling lights, so it glows warmly behind the wet glass. No people, no umbrellas. No letters, no words, no logos anywhere.
```

À contrôler à la reprise : le même cadrage et les mêmes objets ; le ciel gris, plus de soleil ; la pluie en traits fins ; l'eau sur les vitres ; le trottoir mouillé, les flaques ; la salle éclairée derrière le verre ; aucune personne, aucun texte.

**Résultat de A1 pluie, le 2026-10-17 : validé par l'auteur.** ChatGPT a ajouté des spots au plafond de la salle, accepté. Les enseignes : `pipeline/enseignes.py` laisse passer les traits de pluie devant les lettres.

### Prompt A1 nuit — La devanture fermée, la nuit

Retouche de l'image fermée de jour (`fond_ferme_v1`), pas de celle de la pluie : dans ChatGPT, cliquer sur l'image fermée de jour, puis « Modifier ». Le kebab est ouvert 24 h sur 24 : de nuit, le rideau est fermé (`axes.md`), la salle allumée.

```
Edit ONLY the time of day and the light of this image. Keep everything exactly where it is: the same view, the same building, the closed glass shopfront and its door, the two blank signs, the inside of the restaurant, the neighbouring buildings, the sidewalk, the tram track and the trees. Make only this change: it is late at night, dry weather. The sky is dark blue, almost black; there is no sunlight and no leaf shadows. The street is lit by warm orange street lamps out of frame, from the left and the right, which light the sidewalk and the leaves of the trees from below. The restaurant is open and fully lit inside by its warm ceiling lights: it glows warmly behind the glass, and its light spills onto the sidewalk in front. The glass floors above are dark, with only one office window faintly lit. The two blank signs are lit softly from below. No people. No letters, no words, no logos anywhere.
```

À contrôler à la reprise : le même cadrage et les mêmes objets ; le ciel de nuit ; les réverbères hors champ, la lumière orange sur le trottoir et les feuilles ; la salle allumée, sa lumière sur le trottoir ; les étages sombres ; aucune personne, aucun texte.

**Résultat de A1 nuit, le 2026-10-17 : validé par l'auteur du premier coup.** La façade a ses quatre fonds : ouverte de jour, fermée de jour, fermée sous la pluie, fermée la nuit. Les enseignes se posent sur les quatre (`pipeline/enseignes.py` reconnaît les traits de pluie, fins, et laisse les lettres entières sous les flaques de lumière de nuit).

### Prompt A17 — La table de Sky vue d'en haut

Le fond des inserts : les accessoires (le laptop, la galette, les frites, le téléphone sur la sauce, la tasse de Patrick, la grille de mots croisés, les serviettes à formules) s'y posent en calques. Trois images jointes, dans cet ordre : `~/Téléchargements/kebab_pour_A17_1_vue.png`, `~/Téléchargements/kebab_pour_axes_plan-peint.png`, `~/Téléchargements/kebab_pour_A17_3_angle6.png` (le fond de l'axe 6 : la même table, le même bois, les mêmes sauces, la même banquette).

```
The first attached image is a rough 3D layout of one view of our kebab restaurant, made of simple flat-coloured volumes: it fixes the camera, the framing and the place of every object. The second attached image is the same restaurant seen from above, painted in our style: it gives the art style, the materials and the objects. The third attached image is another view of the same table, already painted and approved: the wooden table top, the sauce bottles, the napkin dispenser, the red bench and the light must look exactly the same. Paint exactly the view of the first image, as an empty background for an anime series: keep the same framing, and every object at the same place, with the same size, as if the layout had been painted over. The camera looks straight down at the table from above. Replace the simple volumes with the real objects:
- in the middle of the frame, the rectangular wooden table top seen from directly above: warm, slightly worn wood with a visible grain, a few faint old stains and scratches, clean and empty;
- in the middle of the table, seen from above: a red sauce bottle with its pointed cap, a white sauce bottle with its pointed cap, and a metal napkin dispenser with paper napkins;
- at the top and on the right, the red padded bench around the table, seen from above: the seat cushions;
- at the bottom, the seats of two empty wooden chairs with red cushions; at the bottom left, a little of the tiled floor.
Style: a flat 2D hand-drawn background painting from a 1990s anime film, in the style of the second and third images (clean dark outlines, flat cel shading, muted warm palette, painted details). NOT a 3D render, NOT photorealistic, and do not keep the flat colours of the layout. Light: warm and dim, coming softly from the bottom of the image (the street side); short soft shadows toward the top. No people, no plates, no food, no other objects on the table. No text, no letters and no logos anywhere. Landscape format (1536×1024).
```

À contrôler à la reprise : la vue droit d'en haut ; la table vide, le bois avec son grain ; les deux sauces et les serviettes au milieu ; la banquette en haut et à droite ; les assises des chaises en bas ; rien d'autre sur la table ; aucun texte.

**Résultat de A17, le 2026-10-17 : validé par l'auteur du premier coup. Les 9 fonds du pilote sont faits.**

### Prompt A4 — Depuis le comptoir, le regard de Mohamed

Les fonds de l'épisode 1, après le pilote. Mohamed parle « depuis le comptoir » tout au long du « Miroir » (l. 34, 99, 254). La caméra à sa place, derrière le grand côté du comptoir, un peu inclinée vers le bas : les salades au premier plan, la salle au-delà. Quatre images jointes, dans cet ordre : `~/Téléchargements/kebab_pour_A4_1_vue.png`, `~/Téléchargements/kebab_pour_axes_plan-peint.png`, `~/Téléchargements/kebab_pour_A4_3_angle2.png` (le fond de l'axe 2 : la même salle), `~/Téléchargements/kebab_pour_A4_4_angle8.png` (le fond de l'axe 8 : le même comptoir, les mêmes salades).

```
The first attached image is a rough 3D layout of one view of our kebab restaurant, made of simple flat-coloured volumes: it fixes the camera, the perspective, the framing and the place of every object. The second attached image is the same restaurant seen from above, painted in our style: it gives the art style, the materials and the objects. The third and fourth attached images are two other views of the same restaurant, already painted and approved: the counter, the salad trays, the red bench, the mirror, the tables, chairs, plants, the staircase side and its banister, the walls and the light must look exactly the same. Paint exactly the view of the first image, as an empty background for an anime series: keep the same camera, the same perspective and framing, and every object at the same place, with the same size and angle, as if the layout had been painted over. The camera stands behind the stainless steel counter, where the cook stands, and looks over the counter into the dining room. Replace the simple volumes with the real objects:
- in the foreground, the top of the stainless steel counter; the coloured rectangles are the trays of the refrigerated salad display built into it, seen from the cook's side: lettuce, tomatoes, onions and the others further right; the thin light blue outline is the low glass sneeze guard on the customer side, we see the room through it;
- beyond the counter, the dining room: the rectangular wooden tables with their chairs, each with a red sauce bottle, a white sauce bottle and a napkin dispenser;
- on the left, the long red padded bench along the back wall, with the long dark smoky mirror above it; in the back corner, the table of the corner and a large green potted plant;
- on the right of the back, the side of the wooden staircase with its banister going up, above the bench that runs along the right side;
- the surface at the top is the ceiling, plain and flat.
Style: a flat 2D hand-drawn background painting from a 1990s anime film, in the style of the other images (clean dark outlines, flat cel shading, muted warm palette, painted details). NOT a 3D render, NOT photorealistic, and do not keep the flat colours of the layout. Light: warm morning daylight comes from the open shopfront, out of frame on the left, behind the camera; there are no windows; the inside light is warm and dim. No people. No text, no letters and no logos anywhere. Landscape format (1536×1024).
```

À contrôler à la reprise : le dessus du comptoir et les bacs de salades au premier plan, la vitre basse ; la salle au-delà ; la banquette et le miroir à gauche, la plante de l'angle ; la rampe de l'escalier à droite ; un plafond uni ; aucune personne, aucun texte.

Résultat de A4, le 2026-10-17 : deux essais, l'auteur garde le second (capture hors du repo, `depuis-le-comptoir_essai-1_capture.png`). À corriger : au fond, le bout de l'escalier finit en un grand pan de mur vertical jusqu'au plafond, qu'il ne veut pas ; et la vitre basse dépasse à gauche, au-delà des bacs.

### Prompt A4 retouche — Le bout de l'escalier, la vitre des salades

Dans la case « Décrivez les modifications » du second essai.

```
Edit ONLY this image. Keep everything else exactly as it is: the same view, the same counter, salad trays, tables, chairs, bench, mirror, plant, style and light. Make only these two changes:
1. At the back, the left end of the staircase: remove the tall vertical piece of wall that rises from the top step up to the ceiling. The side of the staircase ends with its top steps, and behind it there is only the back wall of the room, plain, the same as the rest of the wall; the banister keeps going up into the ceiling.
2. The low glass sneeze guard above the salad trays: shorten it on the left so that it starts exactly above the first tray (the lettuce) and runs only above the trays. On the left of the trays, the plain stainless steel counter top has no glass above it.
```

À contrôler à la reprise : plus de pan de mur vertical au bout de l'escalier ; la vitre seulement au-dessus des bacs ; rien d'autre de changé.

**Résultat de la retouche A4, le 2026-10-17 : validé par l'auteur.** Le haut de l'escalier reste un peu faux à l'angle du plafond, accepté.

### Prompt A12 — Le grand miroir de biais

Le miroir où Sky dessine (« Le Miroir », l. 482 : Seb et Daria s'approchent, l. 516 et 518). Il doit rester vierge et sombre : les dessins de Sky se poseront en calque. Quatre images jointes, dans cet ordre : `~/Téléchargements/kebab_pour_A12_1_vue.png`, `~/Téléchargements/kebab_pour_axes_plan-peint.png`, `~/Téléchargements/kebab_pour_A12_3_angle6.png` (le fond de l'axe 6 : le même miroir, la même banquette, la même plante, la même table), `~/Téléchargements/kebab_pour_A12_4_angle21.png` (le fond de l'axe 21 : le même miroir de côté).

```
The first attached image is a rough 3D layout of one view of our kebab restaurant, made of simple flat-coloured volumes: it fixes the camera, the perspective, the framing and the place of every object. The second attached image is the same restaurant seen from above, painted in our style: it gives the art style, the materials and the objects. The third and fourth attached images are two other views of the same corner, already painted and approved: the mirror, its frame, the red bench, the plant, the table, the walls and the light must look exactly the same. Paint exactly the view of the first image, as an empty background for an anime series: keep the same camera, the same perspective and framing, and every object at the same place, with the same size and angle, as if the layout had been painted over. The camera stands in the room and looks at the back wall at an angle. Replace the simple volumes with the real objects:
- across most of the frame, the long mirror on the back wall, seen at an angle, in its thin brown frame: dark smoky glass, clean and empty, with only a faint blurred warm glow and no recognisable reflection; nothing is drawn or written on it;
- below the mirror, the long red padded bench, empty, running toward the corner on the right;
- in the corner, the same large green potted plant as in the third image, behind the corner of the bench;
- at the bottom right, the corner of the wooden table, with a red sauce bottle and a white sauce bottle;
- at the top right, the ceiling, and through the stairwell opening a glimpse of the top of the wooden staircase and its closed wooden door upstairs, in shadow;
- on the right, the plain warm wall of the side of the room.
Style: a flat 2D hand-drawn background painting from a 1990s anime film, in the style of the other images (clean dark outlines, flat cel shading, muted warm palette, painted details). NOT a 3D render, NOT photorealistic, and do not keep the flat colours of the layout. Light: warm, dim light from the open shopfront behind the camera; there are no windows. No people. No text, no letters, no drawings and no logos anywhere, and nothing on the mirror. Landscape format (1536×1024).
```

À contrôler à la reprise : le miroir de biais, vierge, sombre, sans reflet reconnaissable ; la banquette dessous ; la même plante qu'à l'axe 6 ; le coin de la table ; le haut de l'escalier et la porte dans l'ombre, en haut à droite ; aucune personne, aucun texte.

Résultat de A12, le 2026-10-17 : le miroir, la banquette, la plante, le coin de la table sont justes. L'auteur relève : la lumière n'est pas bonne (une grande tache de soleil en haut à gauche, comme une fenêtre) ; et en haut à droite, la porte vue par une ouverture du plafond, « le bug de l'escalier ». Depuis la salle, la cage ne doit jamais se voir : la vue en volumes ferme maintenant le plafond au-dessus de l'escalier pour les caméras de la salle. Capture hors du repo (`miroir_essai-1_capture.png`).

### Prompt A12 retouche — La lumière, le plafond au-dessus de l'escalier

```
Edit ONLY this image. Keep everything else exactly as it is: the same view, the same mirror, frame, bench, plant, table and style. Make only these two changes:
1. The light: there is no window in this room. Remove the bright patches of sunlight on the upper wall at the top left. The only daylight comes softly from the open shopfront behind the camera: the wall and the mirror frame get an even, warm, dim light, with no sharp light shapes on the wall.
2. At the top right: remove the opening in the ceiling and the door seen through it. The ceiling is plain and closed there, the same as the rest of the ceiling, and the wall below it is plain.
```

À contrôler à la reprise : plus de tache de soleil, une lumière douce et égale ; un plafond plein en haut à droite, sans porte ni ouverture ; rien d'autre de changé.

**Résultat de la retouche A12, le 2026-10-17 : validé par l'auteur.**

### Prompt A13 — Depuis le miroir, la table de Sky en plongée

Ce que voit Sky quand il dessine sur le miroir : l'équipe autour de sa table, qui le regarde (« Le Miroir », l. 498). La caméra reculée sur la table de Sky et inclinée vers le bas. Quatre images jointes, dans cet ordre : `~/Téléchargements/kebab_pour_A13_1_vue.png`, `~/Téléchargements/kebab_pour_axes_plan-peint.png`, `~/Téléchargements/kebab_pour_A13_3_angle7.png` (le fond de l'axe 7 : la même salle vers la rue), `~/Téléchargements/kebab_pour_A13_4_angle6.png` (le fond de l'axe 6 : la même table).

```
The first attached image is a rough 3D layout of one view of our kebab restaurant, made of simple flat-coloured volumes: it fixes the camera, the perspective, the framing and the place of every object. The second attached image is the same restaurant seen from above, painted in our style: it gives the art style, the materials and the objects. The third and fourth attached images are two other views of the same restaurant, already painted and approved: the tables, chairs, bench, the side of the staircase and its banister, the street and the light must look exactly the same. Paint exactly the view of the first image, as an empty background for an anime series: keep the same camera, the same perspective and framing, and every object at the same place, with the same size and angle, as if the layout had been painted over. The camera stands with its back to the mirror, above the table in the corner, and looks down at it, toward the room and the street. Replace the simple volumes with the real objects:
- at the bottom, our rectangular wooden table seen from above at an angle, with a napkin dispenser, a white sauce bottle and a red sauce bottle;
- just beyond it, the two empty wooden chairs of our table, their backs facing us;
- on the left, the long red padded bench running away from us along the right side of the room, and above it the closed side of the wooden staircase with its banister going up into the ceiling;
- in the middle and on the right, the other rectangular wooden tables with their chairs, each with its sauce bottles and napkin dispenser;
- at the far end, the open shopfront and the sunny street: the sidewalk, the tram track on its strip of grass, the trees across the street and the facade behind them, as in the third image.
Style: a flat 2D hand-drawn background painting from a 1990s anime film, in the style of the other images (clean dark outlines, flat cel shading, muted warm palette, painted details). NOT a 3D render, NOT photorealistic, and do not keep the flat colours of the layout. Light: the only daylight comes from the open shopfront at the far end; there are no windows; inside, the light is warm and dim, and the shadows of the tables and chairs fall toward the camera. No people. No text, no letters and no logos anywhere. Landscape format (1536×1024).
```

À contrôler à la reprise : la plongée sur la table ; les deux chaises de dos ; la banquette et le côté de l'escalier à gauche, la rampe dans le plafond ; les tables ; la rue au fond, comme à l'axe 7 ; aucune personne, aucun texte.

Résultat de A13, le 2026-10-17 : la plongée, la table, la banquette, les tables sont justes. Mais la rue n'est pas celle des fonds validés (l'auteur) : ChatGPT a lu les troncs des arbres d'en face, dans la vue en volumes, comme deux poteaux en bois plantés dans la devanture, et il a refait la rue à sa façon. Capture hors du repo (`depuis-le-miroir_essai-1_capture.png`). À écrire désormais dans chaque prompt qui voit la rue : « les barres sombres au loin sont les troncs des arbres d'en face, pas des poteaux ; la devanture n'a aucun poteau ».

### Prompt A13 retouche — La rue des fonds validés, sans poteaux

Dans la case « Décrivez les modifications », dans la même conversation (elle a encore l'image de l'axe 7, jointe au message précédent).

```
Edit ONLY the view through the open shopfront at the top of this image. Keep everything else exactly as it is: the same view, the same tables, chairs, bench, staircase, floor, style and light. Make only these two changes:
1. Remove the two tall wooden posts standing in the shopfront: the shopfront is one wide opening with no posts or pillars at all, only its plain top edge.
2. The street seen through the opening must be exactly the street of the third image of my previous message: the pale sidewalk, then the tram track laid on a strip of green grass, with grass between and around the rails, then the row of leafy trees along the opposite sidewalk, and behind them the plain beige facade with its large regular windows, in the same warm morning light.
```

À contrôler à la reprise : plus de poteaux ; la même rue que l'axe 7 ; le reste inchangé.

Résultat de la retouche A13, le 2026-10-17 : plus de poteaux, une rue proche de celle de l'axe 7. Mais trop d'arbres (l'auteur) : sept arbres serrés, une haie de buissons devant la façade. À l'axe 7, sur toute la largeur de la devanture, il y en a quatre, grands et espacés, sans haie ; d'ici, la caméra voit une partie de la rue seulement, soit deux arbres (la vue en volumes en a deux).

### Prompt A13 retouche 2 — Deux arbres, sans haie

```
Edit ONLY the street seen through the open shopfront at the top of this image. Keep everything else exactly as it is. Make only this change: there are too many trees. Keep only two large leafy trees, spaced far apart, the same kind and size as in the third image of my previous message: one in the middle of the opening, one near its right end. Remove all the other trees and the row of bushes along the facade: between the two trees we see the plain beige facade with its large regular windows, and the grass of the tram track in front.
```

À contrôler à la reprise : deux arbres, espacés ; plus de haie ; la façade visible entre eux ; le reste inchangé.

**Résultat de la retouche 2 de A13, le 2026-10-17 : validé par l'auteur.** Les deux arbres sont un peu petits à côté de ceux de l'axe 7, accepté.

### Prompt A14 — L'angle de la banquette, debout

Proche de l'axe 6, mais debout et plus loin : pour les plans de groupe autour de la table de Sky (Seb « assis au fond de la banquette », l. 1470). Quatre images jointes, dans cet ordre : `~/Téléchargements/kebab_pour_A14_1_vue.png`, `~/Téléchargements/kebab_pour_axes_plan-peint.png`, `~/Téléchargements/kebab_pour_A14_3_angle6.png` (le fond de l'axe 6 : le même coin), `~/Téléchargements/kebab_pour_A14_4_angle12.png` (le fond de l'axe 12 : le même miroir, la même plante, la même lumière).

```
The first attached image is a rough 3D layout of one view of our kebab restaurant, made of simple flat-coloured volumes: it fixes the camera, the perspective, the framing and the place of every object. The second attached image is the same restaurant seen from above, painted in our style: it gives the art style, the materials and the objects. The third and fourth attached images are two other views of the same corner, already painted and approved: the mirror, its frame, the red bench, the plant, the table, the walls and the light must look exactly the same. Paint exactly the view of the first image, as an empty background for an anime series: keep the same camera, the same perspective and framing, and every object at the same place, with the same size and angle, as if the layout had been painted over. The camera stands in the room, a few steps from the corner, and looks into the corner of the bench. Replace the simple volumes with the real objects:
- on the left, the long dark smoky mirror on the back wall, in its thin brown frame, empty, with no recognisable reflection;
- the red padded bench in one continuous L: along the back wall, then turning in the corner and coming toward us along the right wall;
- in the corner, the same large green potted plant as in the other images, behind the corner of the bench;
- in the angle of the bench, our rectangular wooden table with a red sauce bottle, a white sauce bottle and a napkin dispenser; at the bottom right, the backs of its two empty chairs;
- on the right, the plain warm wall above the bench, which is the closed side of the staircase; at the top right, the top of that side and the wooden banister going up into the ceiling;
- the surface at the top is the ceiling, plain and closed.
Style: a flat 2D hand-drawn background painting from a 1990s anime film, in the style of the other images (clean dark outlines, flat cel shading, muted warm palette, painted details). NOT a 3D render, NOT photorealistic, and do not keep the flat colours of the layout. Light: warm, dim, even light from the open shopfront behind the camera; there are no windows, no sharp patches of sunlight on the walls. No people. No text, no letters and no logos anywhere. Landscape format (1536×1024).
```

À contrôler à la reprise : le coin vu debout ; le miroir à gauche ; la banquette d'un seul tenant ; la même plante ; la table et ses chaises ; le haut du côté de l'escalier et la rampe en haut à droite, le plafond fermé ; une lumière douce, sans tache de soleil ; aucune personne, aucun texte.

Résultat de A14, le 2026-10-18 : faux pour l'auteur. Derrière la plante, le côté de l'escalier sort du coin comme un bloc ; en haut à droite, son sommet en marches et les barreaux apparaissent sous le plafond. La faute vient de la vue en volumes : vers le fond, le côté de l'escalier s'arrêtait sous les marches, à 2,75 m, et laissait un vide jusqu'au plafond. Corrigé dans `pipeline/vue_kebab.py` : là où la rampe touche le plafond, le côté monte jusqu'au plafond ; l'angle est un coin simple. Capture hors du repo (`coin-de-la-banquette_essai-1_capture.png`).

### Prompt A14 retouche — Un coin simple, un mur plein jusqu'au plafond

```
Edit ONLY the right part of this image, above the red bench. Keep everything else exactly as it is: the same view, the same mirror, plant, bench, table, chairs, style and light. Make only this change: the wall on the right is one plain, flat wall from the bench up to the ceiling, meeting the back wall in a simple straight vertical corner just behind the plant. Remove the block that sticks out of the corner, the stepped shapes at the top right and the vertical posts under the ceiling: no staircase, no steps, no banister and no door can be seen in this view.
```

À contrôler à la reprise : un mur plein à droite, du dossier au plafond ; un angle droit, simple, derrière la plante ; plus de marches ni de barreaux en haut ; rien d'autre de changé. Si la retouche rate : la vue en volumes corrigée est dans `~/Téléchargements/kebab_pour_A14_1_vue.png`, avec le prompt A14.

Résultat de la retouche A14, le 2026-10-18 : le coin est juste, un mur plein derrière la plante. Mais l'auteur veut voir « le petit bout d'escalier » : la caméra 14 tournée vers la droite et élargie (78°) ; à droite, le côté de l'escalier descend le long de la banquette avec sa rampe. Dans la vue en volumes, les morceaux d'un même groupe (le côté de l'escalier) ne forment plus qu'un pan, sans fentes. Capture hors du repo (`coin-de-la-banquette_essai-2_capture.png`).

### Prompt A14 v2 — L'angle de la banquette et le bout d'escalier

Les mêmes images : `~/Téléchargements/kebab_pour_A14_1_vue.png` (refaite), `~/Téléchargements/kebab_pour_axes_plan-peint.png`, `~/Téléchargements/kebab_pour_A14_3_angle6.png`, `~/Téléchargements/kebab_pour_A14_4_angle12.png`.

```
The first attached image is a rough 3D layout of one view of our kebab restaurant, made of simple flat-coloured volumes: it fixes the camera, the perspective, the framing and the place of every object. The second attached image is the same restaurant seen from above, painted in our style: it gives the art style, the materials and the objects. The third and fourth attached images are two other views of the same corner, already painted and approved: the mirror, its frame, the red bench, the plant, the table, the walls and the light must look exactly the same. Paint exactly the view of the first image, as an empty background for an anime series: keep the same camera, the same perspective and framing, and every object at the same place, with the same size and angle, as if the layout had been painted over. The camera stands in the room and looks into the corner of the bench, a little toward the right. Replace the simple volumes with the real objects:
- on the left, the long dark smoky mirror on the back wall, in its thin brown frame, empty, with no recognisable reflection;
- the red padded bench in one continuous L: along the back wall, then turning in the corner and running toward the right along the right wall, all the way to the right edge;
- in the corner, the same large green potted plant as in the other images, behind the corner of the bench; behind it, a simple straight vertical corner;
- just right of the corner, a plain flat wall from the bench up to the ceiling;
- further right, this wall is the closed side of the wooden staircase: its top edge steps down toward the right, following the steps, and above it a wooden banister with its handrail and balusters goes up from the right toward the back and disappears into the ceiling; we see the edges of a few steps above the wall, not the stairs from the front;
- in the angle of the bench, the rectangular wooden table with a red sauce bottle, a white sauce bottle and a napkin dispenser, and its two empty chairs; at the bottom right, the chairs and the corner of the next table along the bench;
- the surface at the top is the ceiling, plain and closed: no opening, no door.
Style: a flat 2D hand-drawn background painting from a 1990s anime film, in the style of the other images (clean dark outlines, flat cel shading, muted warm palette, painted details). NOT a 3D render, NOT photorealistic, and do not keep the flat colours of the layout. Light: warm, dim, even light from the open shopfront behind the camera; there are no windows, no sharp patches of sunlight on the walls. No people. No text, no letters and no logos anywhere. Landscape format (1536×1024).
```

À contrôler à la reprise : un coin simple derrière la plante ; le mur plein jusqu'au plafond près du coin ; plus à droite, le côté de l'escalier en marches et la rampe qui monte dans le plafond ; la banquette d'un seul tenant ; aucune porte, aucune ouverture ; aucune personne, aucun texte.

**A14, le 2026-10-18 : l'auteur garde la retouche** (« ça me fait chier, on garde ça, tant pis ») ; A14 v2 n'est pas envoyé, la caméra 14 revient à sa place.

### Prompt A18 — L'horloge, en gros plan

Un insert : Maëlle regarde l'horloge (« Le Miroir », l. 1438). L'heure change d'une scène à l'autre : le cadran est peint sans aiguilles, et les aiguilles se posent en code, à l'heure de la scène, comme les enseignes. Le logo Efes du texte reste un point à trancher : pas de logo. Trois images jointes, dans cet ordre : `~/Téléchargements/kebab_pour_A18_1_vue.png`, `~/Téléchargements/kebab_pour_axes_plan-peint.png`, `~/Téléchargements/kebab_pour_A18_3_angle8.png` (le fond de l'axe 8 : la même horloge, la même hotte, le même mur).

```
The first attached image is a rough 3D layout of one view of our kebab restaurant, made of simple flat-coloured volumes: it fixes the camera, the framing and the place of every object. The second attached image is the same restaurant seen from above, painted in our style. The third attached image is another view of the same kitchen wall, already painted and approved: the round wall clock, the stainless steel hood, the wall and the light must look exactly the same. Paint exactly the view of the first image, as an empty background for an anime series: a close-up of the clock on the kitchen wall above the counter, keeping the same framing, the same size and place of the clock. Replace the simple volumes with the real objects:
- in the middle, the round wall clock seen straight on: a light cream face with a thin dark round frame and simple tick marks around the edge; the face is empty: no hands, no numbers, no text, no logo;
- on the right edge, the corner of the stainless steel hood above the kebab spit;
- everywhere else, the warm textured wall of the kitchen.
Style: a flat 2D hand-drawn background painting from a 1990s anime film, in the style of the third image (clean dark outlines, flat cel shading, muted warm palette, painted details). NOT a 3D render, NOT photorealistic, and do not keep the flat colours of the layout. Light: warm, dim light from the dining room on the left; a soft shadow of the clock on the wall to the right. No people. No text, no letters, no numbers, no logos anywhere. Landscape format (1536×1024).
```

À contrôler à la reprise : l'horloge ronde, la même qu'à l'axe 8, de face ; le cadran vide, sans aiguilles ni chiffres ; le bord de la hotte à droite ; le mur ; aucun texte.

**Résultat de A18, le 2026-10-18 : du premier coup**, le cadran vide. Les aiguilles : `pipeline/aiguilles.py` (exemple : 10:13, l'heure du message de Léa).

### Prompt A9 — La broche, de près

La partie 3 du texte s'appelle « La broche » : Sky la regarde, Mohamed coupe (l. 727, 1078). La caméra derrière le comptoir, face à la broche contre le mur. Quatre images jointes, dans cet ordre : `~/Téléchargements/kebab_pour_A9_1_vue.png`, `~/Téléchargements/kebab_pour_axes_plan-peint.png`, `~/Téléchargements/kebab_pour_A9_3_angle8.png` (le fond de l'axe 8 : la même broche, la même hotte, le même plan de travail), `~/Téléchargements/kebab_pour_A9_4_angle21.png` (le fond de l'axe 21 : la même cuisine).

```
The first attached image is a rough 3D layout of one view of our kebab restaurant, made of simple flat-coloured volumes: it fixes the camera, the perspective, the framing and the place of every object. The second attached image is the same restaurant seen from above, painted in our style. The third and fourth attached images are two other views of the same kitchen, already painted and approved: the kebab spit, its grill, the hood, the worktop, the clock, the wall and the light must look exactly the same. Paint exactly the view of the first image, as an empty background for an anime series: keep the same camera, the same perspective and framing, and every object at the same place, with the same size and angle, as if the layout had been painted over. The camera stands behind the counter, in the cook's place, and looks at the kebab spit against the kitchen wall. Replace the simple volumes with the real objects:
- in the middle, the vertical kebab spit: a tall cone of golden-brown grilled meat turning on its metal rod, in front of its vertical grill with glowing heating elements, in a stainless steel frame;
- in the foreground, the stainless steel worktop along the kitchen wall, clean, with a long knife and a metal tray near the spit;
- at the top, the stainless steel hood above the spit, partly out of frame;
- at the top left, the edge of the round wall clock, partly out of frame;
- everywhere else, the warm kitchen wall.
Style: a flat 2D hand-drawn background painting from a 1990s anime film, in the style of the third and fourth images (clean dark outlines, flat cel shading, muted warm palette, painted details). NOT a 3D render, NOT photorealistic, and do not keep the flat colours of the layout. Light: warm, dim light from the dining room behind the camera, and the warm orange glow of the grill on the meat. No people. No text, no letters and no logos anywhere. Landscape format (1536×1024).
```

À contrôler à la reprise : la broche de face, au milieu, la même qu'à l'axe 8 ; le grill qui rougeoie ; le plan de travail devant ; la hotte en haut ; l'horloge coupée en haut à gauche ; aucune personne, aucun texte.

Résultat de A9, le 2026-10-18 : la broche, le grill, la hotte, l'horloge sont justes. Il manque, à gauche de la broche sur le plan de travail, le grand bol en métal et l'évier avec son robinet, qu'on voit sur le fond de l'axe 8 (l'auteur). Ajoutés à la vue en volumes pour les axes suivants. Capture hors du repo (`broche_essai-1_capture.png`).

### Prompt A9 retouche — Le bol et l'évier

```
Edit ONLY the worktop on the left of the kebab spit. Keep everything else exactly as it is: the same view, the same spit, grill, hood, clock, knife, tray, wall, style and light. Make only this change: on the stainless steel worktop, to the left of the spit, add the same objects as in the third image of my previous message: first, close to the spit, a large round stainless steel bowl; then, further left, a small stainless steel sink set into the worktop, with a tall curved tap behind it against the wall.
```

À contrôler à la reprise : le bol près de la broche, l'évier et son robinet plus à gauche, comme à l'axe 8 ; rien d'autre de changé.

**Résultat de la retouche A9, le 2026-10-18 : validé par l'auteur.**

### Prompt A15 — La devanture vue de dedans

Mohamed s'approche du menu plastifié sur la vitrine et corrige un prix au feutre (« Le Miroir », l. 1482). Le menu, avec ses prix, se posera en code sur les panneaux repliés. La caméra dans la salle, près du comptoir, tournée vers l'avant gauche. Quatre images jointes, dans cet ordre : `~/Téléchargements/kebab_pour_A15_1_vue.png`, `~/Téléchargements/kebab_pour_axes_plan-peint.png`, `~/Téléchargements/kebab_pour_A15_3_angle7.png` (le fond de l'axe 7 : la même rue, les mêmes arbres), `~/Téléchargements/kebab_pour_A15_4_angle2.png` (le fond de l'axe 2 : le même comptoir, la même caisse, les mêmes panneaux).

```
The first attached image is a rough 3D layout of one view of our kebab restaurant, made of simple flat-coloured volumes: it fixes the camera, the perspective, the framing and the place of every object. The second attached image is the same restaurant seen from above, painted in our style. The third and fourth attached images are two other views of the same restaurant, already painted and approved: the street, the trees, the facade across the street, the counter, the cash register, the folded glass panels, the plants and the light must look exactly the same. Paint exactly the view of the first image, as an empty background for an anime series: keep the same camera, the same perspective and framing, and every object at the same place, with the same size and angle, as if the layout had been painted over. The camera stands inside the restaurant, near the counter, and looks out through the fully open shopfront. Replace the simple volumes with the real objects:
- across most of the frame, the wide open shopfront, with no posts or pillars, only its plain top edge; through it, the sunny street: the pale sidewalk, the tram track on its strip of green grass with grass between the rails, and across the street two large leafy trees spaced far apart in front of the plain beige facade with its large windows (the dark brown bars are the tree trunks, not posts);
- on the right, at the end of the opening, the folded glass panels of the shopfront, stacked together, full height, clear glass in thin dark metal frames;
- at the bottom right, the front end of the stainless steel counter, with the dark cash register and, behind its low glass sneeze guard, the first salad tray; next to the counter, a large green potted plant;
- at the bottom left, the tiled floor of the restaurant; at the top, the ceiling.
Style: a flat 2D hand-drawn background painting from a 1990s anime film, in the style of the other images (clean dark outlines, flat cel shading, muted warm palette, painted details). NOT a 3D render, NOT photorealistic, and do not keep the flat colours of the layout. Light: warm morning sunlight outside; inside, warm and dimmer; the sunlight falls on the floor near the opening. No people. No text, no letters and no logos anywhere, including on the panels and the facade. Landscape format (1536×1024).
```

À contrôler à la reprise : la devanture grande ouverte, sans poteaux ; la rue comme à l'axe 7, deux arbres ; les panneaux repliés à droite ; le bout du comptoir, la caisse, la plante ; aucun texte.

**Résultat de A15, le 2026-10-18 : validé par l'auteur du premier coup.**

### Prompt A5 — Depuis l'escalier, en plongée

Maëlle parle depuis l'escalier (« Le Miroir », l. 72) ; Daria et Théo descendent. La caméra sur les premières marches, juste au-dessus de la rampe, en plongée sur la salle. Quatre images jointes, dans cet ordre : `~/Téléchargements/kebab_pour_A5_1_vue.png`, `~/Téléchargements/kebab_pour_axes_plan-peint.png`, `~/Téléchargements/kebab_pour_A5_3_angle4.png` (le fond de l'axe 4 : la même salle, la même banquette, le même miroir), `~/Téléchargements/kebab_pour_A5_4_angle8.png` (le fond de l'axe 8 : le même comptoir, la même cuisine, le même frigo).

```
The first attached image is a rough 3D layout of one view of our kebab restaurant, made of simple flat-coloured volumes: it fixes the camera, the perspective, the framing and the place of every object. The second attached image is the same restaurant seen from above, painted in our style. The third and fourth attached images are two other views of the same restaurant, already painted and approved: the tables, chairs, red bench, mirror, counter, salad trays, kebab spit, hood, fridge, plants, walls and light must look exactly the same. Paint exactly the view of the first image, as an empty background for an anime series: keep the same camera, the same perspective and framing, and every object at the same place, with the same size and angle, as if the layout had been painted over. The camera stands on the lower steps of the wooden staircase, just above its banister, and looks down into the dining room, toward the back. Replace the simple volumes with the real objects:
- on the right, in the foreground, the wooden handrail and balusters of the staircase banister, going down toward us;
- below, the rectangular wooden tables with their chairs, seen from above, each with a red sauce bottle, a white sauce bottle and a napkin dispenser;
- at the back, the long dark smoky mirror above the red padded bench, which runs along the back wall;
- on the left, the stainless steel counter with the salad trays built into it and the low glass sneeze guard, the kebab spit and the hood behind, against the left wall;
- in the back left corner, the tall drinks fridge with glass doors and a large green potted plant;
- at the top, the ceiling, plain and closed.
Style: a flat 2D hand-drawn background painting from a 1990s anime film, in the style of the other images (clean dark outlines, flat cel shading, muted warm palette, painted details). NOT a 3D render, NOT photorealistic, and do not keep the flat colours of the layout. Light: warm morning daylight from the open shopfront, out of frame behind the camera on the left; inside, warm and dim; no windows, no sharp patches of sunlight on the walls. No people. No text, no letters and no logos anywhere. Landscape format (1536×1024).
```

À contrôler à la reprise : la plongée depuis l'escalier ; la rampe au premier plan à droite ; les tables vues d'en haut ; le miroir et la banquette au fond ; le comptoir, la broche, la hotte à gauche ; le frigo et la plante ; aucune personne, aucun texte.

Résultat de A5, le 2026-10-18 : « pas mal ». À corriger (l'auteur) : allonger un peu le comptoir des bacs à légumes, à son bout droit ; Claude : les bacs y vont jusqu'au bout, alors que le bout du comptoir, côté fond, doit rester libre (la place de la théière de Patrick, axe 8). Capture hors du repo (`depuis-l-escalier_essai-1_capture.png`).

### Prompt A5 retouche — Le comptoir plus long, son bout libre

```
Edit ONLY the stainless steel counter with the salad trays, on the left. Keep everything else exactly as it is: the same view, the same trays, kebab spit, hood, fridge, plant, tables, chairs, bench, mirror, staircase, style and light. Make only this change: the counter is a little longer on its right end, toward the fridge: after the last salad tray, the stainless steel counter continues with a plain, clear and empty top, about as long as two trays, and its low glass sneeze guard stops above the last tray. The end of the counter stays a short step away from the fridge.
```

À contrôler à la reprise : le comptoir plus long ; un bout libre, en inox, après les bacs ; la vitre seulement au-dessus des bacs ; un petit passage avant le frigo ; rien d'autre de changé.

**Résultat de la retouche A5, le 2026-10-18 : validé par l'auteur.**

### Prompt A19 — Le long de la banquette de droite, vers la rue

Vincent « s'assoit dans le coin » (« Le Miroir », l. 705) ; les tables de l'équipe. La caméra assise sur la banquette de droite, près de la place de Patrick, regarde le long de la banquette vers la rue. Quatre images jointes, dans cet ordre : `~/Téléchargements/kebab_pour_A19_1_vue.png`, `~/Téléchargements/kebab_pour_axes_plan-peint.png`, `~/Téléchargements/kebab_pour_A19_3_angle7.png` (le fond de l'axe 7 : la même rue, la même banquette, la même rampe), `~/Téléchargements/kebab_pour_A19_4_angle10.png` (le fond de l'axe 10 : le même côté d'escalier, la même rampe, vus de l'autre bout).

```
The first attached image is a rough 3D layout of one view of our kebab restaurant, made of simple flat-coloured volumes: it fixes the camera, the perspective, the framing and the place of every object. The second attached image is the same restaurant seen from above, painted in our style. The third and fourth attached images are two other views of the same restaurant, already painted and approved: the red bench, the side of the staircase and its banister, the tables, chairs, the street, the trees and the light must look exactly the same. Paint exactly the view of the first image, as an empty background for an anime series: keep the same camera, the same perspective and framing, and every object at the same place, with the same size and angle, as if the layout had been painted over. The camera sits on the red bench along the right side of the room and looks along it toward the street. Replace the simple volumes with the real objects:
- on the left, the long red padded bench running away from us toward the street, empty; above it, the closed side of the wooden staircase, plain warm wall, its top edge stepping down toward the street, and the wooden banister with its balusters going down along it to a newel post at the far end;
- on the right, the rectangular wooden tables along the bench and in the middle of the room, with their chairs, each with a red sauce bottle, a white sauce bottle and a napkin dispenser; in the foreground at the bottom right, the backs of two empty chairs;
- at the far end, the wide open shopfront, with no posts, and the sunny street: the sidewalk, the tram track on its strip of grass, and across the street three large leafy trees spaced far apart in front of the plain beige facade (the dark brown bars are their trunks, not posts);
- at the top, the ceiling, plain and closed.
Style: a flat 2D hand-drawn background painting from a 1990s anime film, in the style of the other images (clean dark outlines, flat cel shading, muted warm palette, painted details). NOT a 3D render, NOT photorealistic, and do not keep the flat colours of the layout. Light: the only daylight comes from the open shopfront at the far end; inside, warm and dim; the shadows of the tables and chairs fall toward the camera. No people. No text, no letters and no logos anywhere. Landscape format (1536×1024).
```

À contrôler à la reprise : la banquette qui file vers la rue ; le côté de l'escalier et la rampe jusqu'au poteau ; les tables ; la devanture sans poteaux, la rue comme à l'axe 7, trois arbres ; un plafond plein ; aucune personne, aucun texte.

**Résultat de A19, le 2026-10-18 : validé par l'auteur du premier coup.**

### Prompt A19 fermé — Le rideau de verre fermé, vu de dedans

Le premier fond « rideau fermé » vu de l'intérieur, en retouche de l'image validée de l'axe 19, même lumière (la pluie et la nuit viendront ensuite, à partir de lui, comme pour la façade). Le rideau : les panneaux vitrés dépliés sur toute la devanture, la porte au milieu (`axes.md`).

```
Edit ONLY the shopfront at the far end of this image. Keep everything else exactly as it is: the same view, the bench, the staircase side and banister, the tables, chairs, ceiling, style and light. Make only this change: the shopfront is now closed. The folding glass panels are unfolded across the whole width of the opening: a row of tall, clear glass panels in thin dark metal frames, from the floor up to the top of the opening; the panel in the middle is the entrance door, the same glass and frame, with a long vertical metal handle on the inside. Through the clean glass we still see the same sunny street, the tram track on its grass, the trees and the facade, a little softer, with faint reflections of the warm room on the glass. No letters, no words, no logos anywhere, not even on the glass or the door.
```

À contrôler à la reprise : les panneaux sur toute la largeur, du sol au haut de l'ouverture ; la porte au milieu, sa poignée côté salle ; la rue derrière le verre, la même ; des reflets légers ; le reste inchangé ; aucun texte.

**Résultat de A19 fermé, le 2026-10-18 : validé par l'auteur du premier coup** (`banquette-de-droite/fond_ferme_v1.png`).

### Prompt A19 pluie — La salle, le rideau fermé, sous la pluie

Retouche de l'image fermée, dans la même conversation. Navier-Stokes : « Jeudi matin. 9h47. Il pleut. La grosse. Celle qui rebondit sur le trottoir et qui fait un bruit de friture sur la vitrine. »

```
Edit ONLY the weather and the light of this image. Keep everything exactly where it is: the same view, the bench, the staircase side and banister, the tables, chairs, sauces, ceiling lights, the closed glass shopfront and its door. Make only this change: it is a grey, rainy morning with heavy rain. Outside, the sky is overcast and the street is grey and wet: rain falls in thin slanted streaks, the sidewalk shines with puddles, the grass of the tram track and the trees are dark and wet. On the glass of the shopfront, drops and trickles of water run down. Inside, there is no sunlight and no leaf shadows anymore: the room is lit by its warm ceiling lights, cosy against the grey outside; the bench and the tables keep their colours, with soft warm light. No people. No letters, no words, no logos anywhere.
```

À contrôler à la reprise : le même cadrage ; plus de soleil ni d'ombres de feuilles dedans ; les plafonniers allumés ; la pluie dehors et l'eau sur le verre ; la rue grise ; aucune personne, aucun texte.

L'auteur, le 2026-10-18 : le prompt A19 pluie ne sert à rien, Sky est à la table de devant dans Navier-Stokes. Non envoyé ; l'axe 19 reste de jour (ouvert et fermé).

### Prompt A24 pluie — La table de Sky dans Navier-Stokes

La caméra 24 replacée : assise dans la salle, vers la table de devant le long de la banquette, la vitrine fermée derrière elle (Navier-Stokes, l. 9 : « Jeudi matin. 9h47. Kebab d'en bas. Il pleut. La grosse. Celle qui rebondit sur le trottoir et qui fait un bruit de friture sur la vitrine »). Directement sous la pluie, avec la vue en volumes rideau fermé. Quatre images jointes, dans cet ordre : `~/Téléchargements/kebab_pour_A24_1_vue.png`, `~/Téléchargements/kebab_pour_A24_2_angle10.png` (le fond de l'axe 10 : la même table, la même banquette, la même rampe, le même palier), `~/Téléchargements/kebab_pour_A24_3_angle19-ferme.png` (le rideau de verre fermé, vu de dedans), `~/Téléchargements/kebab_pour_A24_4_facade-pluie.png` (la pluie sur la façade : la même lumière grise, le même verre mouillé).

```
The first attached image is a rough 3D layout of one view of our kebab restaurant, made of simple flat-coloured volumes: it fixes the camera, the perspective, the framing and the place of every object. The other three attached images are views of the same restaurant, already painted and approved: the second shows the same table, red bench, staircase side, banister and landing on a sunny day; the third shows the glass shopfront closed, seen from inside; the fourth shows the same building under heavy rain. Paint exactly the view of the first image, as an empty background for an anime series: keep the same camera, the same perspective and framing, and every object at the same place, with the same size and angle, as if the layout had been painted over. The camera is seated in the dining room and looks at the front table along the red bench, with the closed shopfront behind it. Replace the simple volumes with the real objects:
- in the middle, the rectangular wooden table, its far short end against the red padded bench, with a napkin dispenser, a white sauce bottle and a red sauce bottle; its empty wooden chairs with red seats around it, and other chairs in the foreground on the left;
- behind the table, on the left, the long red padded bench, empty, and above it the closed side of the wooden staircase, plain warm wall, with the wooden banister going down to a newel post near the landing; on the landing, a large green potted plant;
- on the right, the closed glass shopfront: tall clear glass panels in thin dark metal frames (the dark grey bars), from the floor to the top of the opening;
- through the glass, the street under heavy rain, as in the fourth image: grey sky, the wet sidewalk shining with puddles, the tram track on its dark wet grass, a large leafy tree across the street, dark and dripping, and the facade behind it (the dark brown bar is the tree trunk);
- drops and trickles of water run down the glass; the surface at the top is the ceiling.
Style: a flat 2D hand-drawn background painting from a 1990s anime film, in the style of the other images (clean dark outlines, flat cel shading, muted palette, painted details). NOT a 3D render, NOT photorealistic, and do not keep the flat colours of the layout. Light: a grey, rainy morning: no sunlight and no shadows of leaves inside; the room is lit by its warm ceiling lights, cosy against the cold grey light coming through the glass. No people. No text, no letters and no logos anywhere. Landscape format (1536×1024).
```

À contrôler à la reprise : la table devant la banquette, son bout contre elle ; la rampe jusqu'au poteau, le palier et sa plante ; le rideau de verre fermé à droite, ses cadres ; la pluie dehors, l'eau sur le verre ; pas de soleil dedans, les plafonniers ; aucune personne, aucun texte.
