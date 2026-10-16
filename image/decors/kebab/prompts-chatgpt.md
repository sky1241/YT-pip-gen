# Le kebab — les prompts ChatGPT

Le décor principal (bible, « La géographie » : le kebab au rez-de-chaussée, le bureau à l'étage, l'escalier entre les deux). Conçu dans ChatGPT, dans le style de la série (`image/style.md`), puis repassé dans le modèle local : aucune image de production ne vient de ChatGPT. Un prompt à la fois, dans une nouvelle conversation ChatGPT réservée au kebab.

Le canon du kebab n'est pas encore tranché (Mohamed à Annemasse ou Mehmet à Clichy, CLAUDE.md). En attendant, la rue derrière la vitrine reste neutre : ni montagne, ni monument, rien de lisible.

| Prompt | Image | Où la ranger |
|---|---|---|
| KB1 | La maquette : tout le kebab vu de dessus, en coupe, sans personne : la v3 est la bonne base | `image/decors/kebab/maquette_v1.png` |
| KB1 retouches | Le menu, l'escalier ouvert, le miroir fumé, les panneaux, la porte de Datastream, les tables : faite, choisie par l'auteur | `image/decors/kebab/maquette_v2.png` |
| Plan | Vu de dessus, en code (`pipeline/plan_kebab.py`) : la disposition exacte | `image/decors/kebab/plan_v2.png` (la v1 sans la banquette en L) |

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
