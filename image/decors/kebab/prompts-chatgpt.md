# Le kebab — les prompts ChatGPT

Le décor principal (bible, « La géographie » : le kebab au rez-de-chaussée, le bureau à l'étage, l'escalier entre les deux). Conçu dans ChatGPT, dans le style de la série (`image/style.md`), puis repassé dans le modèle local : aucune image de production ne vient de ChatGPT. Un prompt à la fois, dans une nouvelle conversation ChatGPT réservée au kebab.

Le canon du kebab n'est pas encore tranché (Mohamed à Annemasse ou Mehmet à Clichy, CLAUDE.md). En attendant, la rue derrière la vitrine reste neutre : ni montagne, ni monument, rien de lisible.

| Prompt | Image | Où la ranger |
|---|---|---|
| KB1 | La maquette : tout le kebab vu de dessus, en coupe, sans personne : la v3 est la bonne base | `image/decors/kebab/maquette_v1.png` |
| KB1 retouche | Les quatre corrections : menu, escalier ouvert, miroir fumé, tables | `image/decors/kebab/maquette_v2.png` |

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
