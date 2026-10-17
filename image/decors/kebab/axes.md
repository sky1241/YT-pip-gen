# Le kebab — les axes de caméra

Un axe = un fond vide, sans perso, fait une fois et réutilisé à chaque épisode (CLAUDE.md, « Images »). Les numéros sont ceux du plan `plan-axes_v6.png` (les cercles bleus : la caméra et la direction où elle regarde). Les positions viennent de `plan_v5.png` (le plan v3 validé par l'auteur le 2026-10-17, avec ses corrections), et les besoins des textes : le CERN (`ecriture/brouillons/cern.md`, numéros de ligne) et Navier-Stokes.

## Où on en est (2026-10-17)

- **Validé par l'auteur** : le plan `plan_v5.png` (sans caméras, à joindre dans ChatGPT) et les 25 axes `plan-axes_v6.png` (avec caméras, pour Claude). « On bougera peut-être 2 ou 3 plans un peu, mais l'idée est là. »
- **La base fixe, validée** : le plan peint `plan-peint_v2.png` (prompt KB2 v3, d'après `plan_v5.png`). Elle sert de référence de style et d'objets pour tous les axes. Seul écart accepté : la caisse y est encore tournée vers la rue ; dans chaque fond où elle se voit, le prompt la tourne vers Mohamed.
- **Ensuite** : l'auteur fait tous les fonds d'un coup, un prompt à la fois, le pilote d'abord (1, 2, 6, 7, 8, 10, 17, 20, 21), de jour. Claude ne lui montre qu'un axe à la fois (le plan de cet axe seul) ; le plan des 25 axes reste pour Claude. L'ancien fond de l'axe 6 est supprimé : l'axe 6 se refait en `fond_v1.png`.

## Les décisions de l'auteur sur le décor (2026-10-16 et 17)

- Le canon : Mohamed à Annemasse. Le style : celui des images de référence de Sky et de Maëlle (`image/style.md`).
- La devanture : pas de porte, des panneaux vitrés qui se replient en accordéon, tous à gauche, sur toute la hauteur ; ils ferment le kebab (la pluie, le soir). Ouverte sur toute la largeur, jusqu'au coin de droite, sans muret.
- Le comptoir en L : la caisse juste en entrant, sur le petit côté devant, **tournée vers Mohamed** (c'est lui qui tape dedans) ; puis la vitrine des salades (laitue, tomates, oignons, chou rouge, carottes, concombres) et les sauces le long du grand côté ; la broche, le grill, la friteuse contre le mur gauche ; une horloge ronde au mur.
- Le frigo à boissons tout au fond à gauche, qu'on voit un plan sur deux ; il ne gêne pas Sky au miroir.
- La banquette rouge en L, sous le miroir puis le long de la rampe ; le miroir sur toute la banquette du fond, à fleur de son bout gauche, en verre fumé.
- La table de Sky pour cinq, dans l'angle : Sky et Maëlle sur la banquette, deux chaises en face, Patrick au bout (« c'est l'ancien, ça résout les problèmes de champ ») ; Sky peut se lever et laisser sa place à Maëlle.
- Les tables : rectangulaires, toutes pareilles, les chaises face à face, deux de chaque long côté ; celles de droite perpendiculaires à la banquette, un petit bout contre elle. La table de devant à droite : celle de Sky dans l'épisode Navier-Stokes.
- Sur chaque table : une sauce rouge, une sauce blanche, un distributeur de serviettes (Sky griffonne dessus). Pas de plante sur les tables ; quelques grandes plantes au sol, dans les coins.
- L'escalier en bois (il grince), dans le kebab : un palier à l'intérieur, à l'avant droit, puis il monte vers le fond jusqu'à la porte de Datastream (une porte en bois simple, sans texte). Une rampe basse et ouverte entre la banquette et l'escalier.
- Dehors : la rue d'Annemasse, les rails du tram avec de l'herbe entre les rails, des potelets, un trottoir.
- Trois lumières : le jour, la pluie (rideau de verre fermé, gris), la nuit.

## Le plan, en bref (`plan_v5.png`)

- À gauche, le comptoir en L (la caisse devant, **tournée vers Mohamed**, les salades le long), la broche, le grill et la friteuse contre le mur ; le frigo à boissons au fond à gauche.
- Au fond, la banquette rouge en L : le long du mur du fond, puis le long de la rampe, à droite. **Le miroir couvre toute la banquette du fond**, à fleur de son bout gauche.
- **La table de Sky, dans l'angle de la banquette, pour cinq** : Sky et Maëlle sur la banquette du fond, deux chaises en face, **Patrick au bout, sur la banquette de droite** (c'est l'ancien). Un plan où Sky se lève et laisse sa place à Maëlle est possible.
- Au milieu, deux tables pour quatre ; le long de la banquette de droite, deux tables perpendiculaires, un petit bout contre elle. **La table de devant, à droite, est celle de Sky dans l'épisode Navier-Stokes**, près de la vitrine (l'auteur).
- À droite, **l'escalier en bois est dans le kebab** : il part d'un palier intérieur, à l'avant droit, au bout de la banquette, et monte vers le fond jusqu'à la porte de Datastream. Le palier est derrière la devanture, **sans muret** : la devanture ouverte va jusqu'au coin de droite. **Entre la banquette et l'escalier, rien qu'une rampe basse, tout droit, sans mur ni retour dans la salle : l'angle reste grand ouvert.**
- Devant, la devanture ouverte sur la rue d'Annemasse ; les panneaux vitrés repliés à gauche. **Dans la rue, les rails du tram, avec de l'herbe entre les rails**, comme à Annemasse.

## Les règles de chaque prompt

- **La seule lumière du jour vient de la devanture, côté rue ; aucune autre fenêtre.** Les ombres partent vers le fond (leçon de l'axe 6).
- **Le miroir est en verre fumé sombre, sans reflet reconnaissable** : les dessins de Sky au marqueur blanc s'y lisent.
- Aucune personne, aucun texte ni logo. Rien d'important près des bords haut et bas : l'image se recadre en 16:9.
- « À hauteur d'homme » = environ 1,60 m ; « assis » = environ 1,20 m.

## Les trois lumières

Trois lumières, dans le même cadrage (l'auteur, le 2026-10-17) :

- **Le jour** (`fond_v1.png`) : le matin, un intérieur chaud et tamisé, la rue lumineuse. Pour tous les axes, en premier.
- **La pluie** (`fond_pluie_v1.png`) : le rideau de verre est fermé, les panneaux vitrés dépliés sur toute la devanture, la pluie coule sur le verre, la lumière est grise. Navier-Stokes : « Jeudi matin. Il pleut ». Sky peut se tenir près de la vitre : d'où les axes 22 et 23, qui n'existent que sous la pluie.
- **La nuit** (`fond_nuit_v1.png`) : le kebab ouvert tard, éclairé par ses appliques et ses panneaux de menu, la rue sombre sous les lampadaires.

La pluie et la nuit se font en retouche du fond de jour : seule la lumière change, ce que ChatGPT retouche bien (contrairement à la disposition).

**Qui a besoin de quoi.** Seuls les axes qui voient la rue ou la devanture changent vraiment avec la pluie ou la nuit : 1, 2, 3, 7, 10, 13, 15, 19, 24, 25. Pour les autres, tournés vers le fond, la pluie et la nuit passent d'abord par l'étalonnage au montage (plus gris, plus sombre) et par le son ; on ne fait leur fond de pluie ou de nuit que si un texte le demande. Le compte : 23 fonds de jour (tous sauf 22 et 23), 12 de pluie (les 10 axes, plus 22 et 23), 10 de nuit, soit **45 fonds**, dont 9 pour le pilote, tous de jour. L'épisode Navier-Stokes se passe sous la pluie : ses axes (22 à 25) se font d'abord en pluie.

## Les 25 axes

| N° | Dossier | D'où, vers où | Ce qu'on voit | À quoi il sert | Quand |
|---|---|---|---|---|---|
| 1 | `exterieur/` | En face, de l'autre côté de la rue, à hauteur d'homme | La façade : un petit immeuble de deux étages, le kebab ouvert au rez-de-chaussée, les fenêtres de Datastream au premier, le trottoir, les potelets, les rails du tram et leur herbe | L'ouverture (« Annemasse. Rue du Commerce. », l. 10), « Dehors, Annemasse. Le bruit du tram » (l. 606), les transitions | pilote |
| 2 | `entree/` | Sur le trottoir, devant la devanture, à hauteur d'homme, vers le fond | Toute la salle : le comptoir à gauche, la banquette en L et le miroir au fond, la table de Sky dans l'angle, l'escalier à droite | Le plan d'ensemble, les arrivées depuis la rue | pilote |
| 3 | `salle-depuis-le-fond/` | Du fond, près du bout gauche de la banquette, à hauteur d'homme, vers la rue | La salle, le comptoir à droite de l'image, la devanture ouverte, la rue et le tram au loin | Le contrechamp du 2, les plans de groupe | épisode 1 |
| 4 | `depuis-le-comptoir/` | Derrière le comptoir, à la place de Mohamed, à hauteur d'homme, vers la droite | Le comptoir en premier plan, la salle, la table de Sky dans l'angle, la banquette, la rampe et l'escalier | Le regard de Mohamed et ses répliques « depuis le comptoir » (l. 34, 99, 254), le marqueur qui vole (l. 476) | épisode 1 |
| 5 | `depuis-l-escalier/` | Au milieu de l'escalier, en plongée, vers la salle | Les tables vues d'en haut, le comptoir au fond | Les répliques « depuis l'escalier » (Maëlle, l. 72), les arrivées | épisode 1 |
| 6 | `table-du-fond/` | Au bout gauche de la table de Sky, assis, de biais vers l'angle (dessiné par l'auteur) | La table de biais, la banquette du fond et le miroir à gauche, l'angle, la banquette de droite et la place de Patrick à droite, la rampe et le haut de l'escalier au bord droit | Le plan maître des dialogues : Sky et Maëlle sur la banquette (l. 14, 78), Patrick au bout | pilote |
| 7 | `table-du-fond-contrechamp/` | Sur la banquette du fond, à la place de Sky, assis, vers la rue | Les deux chaises face à nous, la salle, le comptoir à droite de l'image, la place de Patrick et la banquette de droite à gauche, la devanture et la rue au fond | Le contrechamp des dialogues | pilote |
| 8 | `comptoir/` | Dans la salle, devant le comptoir, à hauteur d'homme | La caisse, la vitrine des salades, la broche sous sa hotte derrière, l'horloge, les panneaux du menu | Mohamed qui essuie le comptoir (l. 20) et parle depuis là | pilote |
| 9 | `broche/` | Plus près, de l'autre côté du comptoir, vers la broche | La broche qui tourne, le grill, la hotte, la place de la théière de Patrick (l. 20) | Partie 3, « La broche » : Sky regarde la broche (l. 1078), Mohamed coupe (l. 727) | épisode 1 |
| 10 | `pied-de-l-escalier/` | Dans la salle, à l'avant droit, à hauteur d'homme, vers l'escalier | Les premières marches en bois, la rampe, la devanture à côté | Les descentes : Daria (l. 38), Théo (l. 121), Vincent (l. 703) | pilote |
| 11 | `escalier-vers-datastream/` | Au pied de l'escalier, vers le haut | L'escalier en bois, la rampe, la porte de Datastream en haut | Théo passe la tête (l. 121), Vincent remonte (l. 816), Sky monte dormir (l. 1583) | épisode 1 |
| 12 | `miroir/` | De la salle, côté gauche, à hauteur d'homme, le miroir de biais | Le grand miroir vierge sur toute la banquette du fond, la table de Sky dans l'angle | Sky dessine (l. 482), Seb et Daria s'approchent (l. 516, 518). Les dessins se posent en calque | épisode 1 |
| 13 | `depuis-le-miroir/` | Debout devant le miroir, à la place de Sky qui dessine, vers la salle | La table de Sky en plongée, la salle, le comptoir, la rue | Les visages de l'équipe qui regarde Sky dessiner (l. 498) | épisode 1 |
| 14 | `coin-de-la-banquette/` | De la salle, vers l'angle de la banquette en L | La table de Sky dans l'angle, ses deux banquettes, la rampe | Les plans de groupe autour de Sky ; Seb « assis au fond de la banquette » (l. 1470) | épisode 1 |
| 15 | `devanture/` | Dans la salle, vers la rue, à hauteur d'homme | La devanture ouverte, les panneaux repliés et le menu plastifié collé dessus, le trottoir, les potelets, le tram et l'herbe entre les rails | Mohamed corrige le menu au feutre (l. 1482) ; la pluie sur la vitrine (Navier-Stokes) | épisode 1 |
| 16 | `frigo/` | De la salle, vers le coin du fond à gauche | Le frigo à boissons, le bout du comptoir | Les boissons : l'Ayran de Daria (l. 117), « Vous voulez des boissons ? » (l. 298) | si besoin |
| 17 | `table-vue-de-dessus/` | Au-dessus de la table de Sky, vue d'en haut | Le dessus de la table, vide : les accessoires s'y posent en calques (laptop, galette, frites, téléphone sur la sauce, tasse de Patrick, grille de mots croisés, serviettes à formules) | Les inserts | pilote |
| 18 | `horloge/` | Gros plan, au-dessus du comptoir | L'horloge ronde | Maëlle regarde l'horloge (l. 1438) | épisode 1 |
| 19 | `banquette-de-droite/` | De la place de Patrick, le long de la banquette de droite, vers la rue | Les deux tables de droite en enfilade, la banquette, la rampe et l'escalier, la devanture au bout | Vincent « s'assoit dans le coin » (l. 705), les tables de l'équipe | épisode 1 |
| 20 | `bout-de-table/` | Au bout gauche de la table de Sky, assis, vers Patrick | Patrick de face, au bout de la table, sur la banquette de droite ; derrière lui, la rampe et l'escalier | Patrick et ses mots croisés (l. 16, 32), ses répliques à Sky | pilote |
| 21 | `depuis-patrick/` | De la place de Patrick, assis, le long de la table, vers la gauche | Sky et Maëlle de profil sur la banquette du fond, le miroir au-dessus d'eux ; au loin, le frigo et le bout du comptoir | Le contrechamp de Patrick : Sky qui mâche et regarde le plafond (l. 24) | pilote |
| 22 | `vitrine-fermee/` | Derrière la table de Navier-Stokes, assis, vers la rue | La table en premier plan, le rideau de verre fermé, la pluie qui coule dessus, la rue floue et grise derrière | Sky près de la vitre, les jours de pluie (Navier-Stokes) | pluie seule |
| 23 | `a-travers-la-vitre/` | Dehors, sur le trottoir, tout près du verre, vers la table de Navier-Stokes | À travers le verre mouillé : la table de Navier-Stokes, la salle chaude derrière | Sky vu de la rue, derrière la vitre, sous la pluie | pluie seule |
| 24 | `table-navier-stokes/` | Dans la salle, assis, vers la table de devant à droite | La table, le bout de la banquette où s'assoit Sky, la rampe et le palier de l'escalier derrière, la vitrine à droite de l'image | Le plan maître de l'épisode Navier-Stokes ; Théo qui descend juste à côté (l. 27 de Navier-Stokes) | Navier-Stokes |
| 25 | `table-navier-stokes-contrechamp/` | Du bout de la banquette, à la place de Sky, assis, vers la salle | Les chaises de la table, la salle, le comptoir au fond, la vitrine à gauche de l'image | Le contrechamp de Sky dans Navier-Stokes ; Mohamed depuis le comptoir (l. 17) | Navier-Stokes |

Les neuf fonds du pilote (la minute des mots croisés) : 1, 2, 6, 7, 8, 10, 17, 20, 21, de jour d'abord.

## Points à trancher avec l'auteur

1. **L'appel vidéo** (partie 2) : « Wang regarde le fond de l'image. La broche. Le comptoir. » (l. 636). Sky est sur la banquette du fond : derrière lui, la caméra du laptop voit le miroir, pas la broche. Soit Sky passe sur une chaise pour l'appel, soit le texte dit « le miroir ».
2. **L'équipe autour de Sky** : jusqu'à huit personnes et deux chats autour d'une table pour cinq. On rapproche la table du milieu ? Ou les autres restent debout autour ?
3. **L'horloge Efes** (l. 498, 1438) : une vraie marque. Une horloge sans logo, un logo inventé, ou le vrai logo ajouté en code au montage ?
4. **Le menu plastifié** : il porte du texte (des prix). Il se fait en code (`image/gabarits/`) et se pose sur le fond, comme tout texte à l'écran.
5. **Vincent « dans le coin »** : le bout de la banquette de droite, près de la rue (19) ?
6. **Sky monte dormir** : « Il passe devant le comptoir » (l. 1583). Dans le plan, l'escalier est à droite et le comptoir à gauche : de la table de Sky à l'escalier, il ne passe pas devant. Le texte peut dire « devant la broche » s'il traverse la salle, ou rien.

## Comment on fait chaque fond

Un prompt à la fois, comme pour Sky. **La vue en volumes** (depuis le 2026-10-17, leçon de l'axe 6) : avec un plan vu de dessus et une caméra, ChatGPT ne respecte ni la place de la caméra ni ce qu'elle voit. Claude dessine donc la vue elle-même en volumes simples, à la bonne place et en perspective (`python3 pipeline/vue_kebab.py <sortie> <numéro>`, mêmes mesures que le plan, les axes lus dans `plan_kebab.py`), et ChatGPT la peint, comme il a peint le plan vu de dessus. L'auteur joint : la vue en volumes, puis le plan peint, pour le style et les objets. Le prompt décrit la vue : où est la caméra, à quelle hauteur, et ce qu'on voit de gauche à droite. Claude contrôle (la disposition contre le plan, aucun texte, aucune personne, la lumière), range dans `image/decors/kebab/<dossier>/fond_v1.png` et note la provenance. Les prompts s'écrivent dans `prompts-chatgpt.md`.

Axes à revoir quand on y arrive, la vue en volumes le montre : le 10 regarde le mur de droite depuis que l'escalier part d'un palier (à tourner vers le palier et les premières marches) ; le 11 aussi.

### Le modèle de prompt d'un axe (première version, avec le plan et la caméra : remplacée par la vue en volumes, voir A6 v3 dans `prompts-chatgpt.md`)

Deux images jointes dans le même message, dans cet ordre : le plan de l'axe seul (`~/Téléchargements/kebab_pour_A<n>_camera.png`, fait avec `pipeline/plan_kebab.py <sortie> axe <n>`), puis le plan peint (`~/Téléchargements/kebab_pour_axes_plan-peint.png`, copie de `plan-peint_v2.png`). Les parties entre crochets changent d'un axe à l'autre ; le reste ne bouge pas.

```
The first attached image is the floor plan of our kebab restaurant, with one camera marked in blue (number [n]): its position and the cone of what it sees. The second attached image is the same restaurant seen from above, painted in our style; it gives the style, the materials, the colours and the objects. Paint the view from this camera, as an empty background for an anime series: a flat 2D hand-drawn background painting from a 1990s anime film, in the style of the second image (clean dark outlines, flat cel shading, muted warm palette, painted details). NOT a 3D render, NOT photorealistic. Landscape format (1536×1024); keep the important things away from the top and bottom edges, the image will be cropped to 16:9.
The camera [where it stands, at what height: seated about 1.2 m or standing about 1.6 m], and looks [where]. Normal lens, straight vertical lines, no fisheye.
What we see, from front to back:
- [element by element, with left and right of the frame named from the camera's point of view]
Light: the only daylight comes from the open shopfront on the street side; there are no other windows, the side walls are solid. [Where the street is in the frame, and where the shadows fall.] Inside, the light is warm and dim; the street is bright with warm morning sun. The mirror above the back bench is dark smoky glass, with no recognisable reflection. No people. No text, no letters and no logos anywhere.
```

Rappels selon l'axe : la caisse tournée vers Mohamed (vers l'intérieur du comptoir) ; la rampe basse et ouverte ; le palier de l'escalier dans la salle ; les panneaux vitrés repliés à gauche de la devanture (vus de la salle vers la rue, ils sont à droite de l'image) ; l'herbe entre les rails du tram ; deux sauces et un distributeur de serviettes sur chaque table ; pas de plante sur les tables.
