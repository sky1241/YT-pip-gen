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

## 2026-10-14 — Sky, premier essai d'image maître
- Contexte : protocole perso, étape 2. Prompt 0 de image/persos/sky/prompts-chatgpt.md, avec
  l'image maître de Maëlle jointe comme référence de style et une photo de l'auteur.
- Résultat : le style est celui de Maëlle (trait, lumière chaude, fond peint) : la référence de
  style par image jointe marche. Carrure et air pas impressionné justes.
- Ce que j'avais pris pour des défauts : son œil gauche tout blanc, sans iris (c'est voulu : il est aveugle) ; la bouteille a la couleur
  d'une bière ; la chemise porte de grands lys botaniques au lieu d'un petit motif de fleurs de
  lys ; les veines des avant-bras se voient à peine. Sont apparus des détails non demandés,
  sans doute tirés de la photo : lunettes à monture fine, barbe courte, cordon noir et chaîne à
  deux anneaux au cou, chevalière à la main droite, cernes marqués.
- Suite : l'œil aveugle, les lunettes, la barbe, les colliers, la bague et les lys sont voulus. L'auteur a
  fait retoucher les veines des avant-bras : cette version est l'image maître, le premier essai est
  supprimé. ChatGPT a écrit sa description maître (image/persos/sky/description-chatgpt.md), à coller
  en tête de chaque prompt de Sky. Leçon : avant de traiter un détail comme une erreur, demander.
- Descriptions maîtres : ChatGPT a écrit celles de Sky et de Maëlle d'après leurs images. Elles
  verrouillent l'apparence, mais il ne connaît pas l'histoire : ce qu'il ajoute de lui-même (la
  silhouette en sablier de Maëlle, « Sky dort une heure par nuit ») est marqué à valider, et pour
  le caractère la bible fait foi. L'expression par défaut qu'il donne à Maëlle (paupières un peu
  baissées) est le sourire en coin des planches ratées : à retirer des prompts d'émotions.
- Sky : ses 19 prompts de planches sont écrits (image/persos/sky/prompts-chatgpt.md), avec les leçons
  de Maëlle appliquées d'emblée : un indice physique par émotion, son air fatigué par défaut interdit,
  le bloc d'expression par défaut retiré du contexte. Son sourire de prédateur (canines un peu
  pointues) vient du sourire de Tanya dans Youjo Senki, sans le nommer dans les prompts.
- Sky, rotation : réussie du premier coup. L'œil aveugle reste le gauche dans les six vues : devant de
  trois-quarts gauche, derrière le nez de trois-quarts droit, seul visible de profil gauche, absent de
  profil droit.
- Sky, en pied : réussie (œil, bague, veines, baskets noires). ChatGPT a ouvert la chemise jusqu'au ventre
  et laissé dépasser l'élastique du caleçon : noté comme détail de l'image, pas comme look de base.
- Sky, palette de face 1 : réussie du premier coup, joie franche comprise. La ligne contre son air
  fatigué par défaut était dans le prompt dès le départ : aucune case n'y est retombée. L'œil aveugle
  reste blanc dans les six.
- Sky, palette de face 2 : bonne, sauf le mépris. Le prompt disait « on HIS RIGHT side » et ChatGPT a
  relevé le coin droit de l'image, donc son côté gauche. La rotation était juste parce que chaque côté
  y était nommé par son œil (« the blind eye side »). Leçon : nommer le côté par un détail visible
  (« the side of his blue eye »), jamais par « right » ou « left » seuls. Le mépris passe en reprise.
- Sky, palette de face 4 : bonne, sauf le désir. Le mot « Longing » l'emporte sur la consigne (« staring
  at food ») : ChatGPT dessine la nostalgie, regard en l'air et sourcils relevés. Pour la faim, écrire
  « Craving » et donner la cible et un indice visible (la galette sur la table, un filet de bave).
- Sky, palette de face 3 : bonne, sauf la confusion et le doute, le sourcil levé au-dessus de l'œil
  aveugle. Trois cases sur trois du mauvais côté avec « his right » : la règle de l'œil bleu s'impose.
  ChatGPT a séparé les cases par des traits noirs : decouper_planche.py essaie maintenant les traits
  noirs fins quand les blancs ne donnent pas le bon nombre de cases (fins, sinon le col roulé noir de
  Maëlle passerait pour un trait). Vérifié : les 14 planches déjà rangées se découpent comme avant.
- Sky, palette de face 5 : bonne, sauf le contentement. Aux yeux fermés (rire, contentement,
  soulagement), ChatGPT ferme l'œil bleu et laisse l'aveugle ouvert : on lit un clin d'œil. Or son
  œil aveugle doit cligner à l'animation, donc il faut des images où il est fermé. Leçon : écrire
  « both eyes closed, the blind one too ». Le poing du triomphe n'a pas la bague : à surveiller sur les mains.
- Sky, palette de face 6 : bonne. La malice est du bon côté : nommer le côté par l'œil bleu marche.
  Mais la fatigue et la douleur gardent l'œil aveugle ouvert malgré « the blind one too » : en
  génération, ChatGPT ne le ferme jamais. Les yeux fermés passent en retouche : Claude assemble les
  cases ratées en une planche, ChatGPT ferme l'œil aveugle (prompt 9 ter). Le neutre de cette planche
  devient le clignement, utile à l'animation.
- Sky, reprises de face : les quatre bonnes du premier coup. Avec le côté nommé par l'œil bleu, le
  mépris et les sourcils tombent juste. « Craving » et la galette sur la table donnent la faim (ChatGPT
  a ajouté la langue sur la lèvre).
- Sky, lunettes : la monture de l'auteur est plaquée or, ChatGPT l'a faite argentée (la description
  disait « thin metallic frame », sans couleur). Rien n'est à refaire : l'image maître se corrige en
  retouche (prompt 0 bis), les planches suivantes le disent, et les images déjà faites se recolorent
  avant le LoRA. Essai de recoloration par la couleur sur l'image maître : raté, sous la lumière chaude
  la monture prend la teinte de la peau et ne se sépare pas au seuil de couleur. Il faudra un masque
  des lunettes. Leçon : un détail de couleur qui compte s'écrit dès le prompt 0.
- Sky, yeux fermés, premier essai : sans l'image jointe, ChatGPT a retouché la dernière planche qui
  collait au texte (la planche 6) et fermé l'œil aveugle dans toutes les cases. La fatigue et la douleur
  sont bonnes et gardées ; le reste du visage n'a presque pas bougé. Donc : en retouche, il ferme
  l'œil aveugle ; en génération, jamais. Pour une retouche, toujours écrire « edit ONLY the image
  attached to this message » et joindre l'image dans le même message.
- Sky, lunettes, suite (vu par l'auteur) : la barre du haut du double pont est sur l'image maître, la
  rotation et la planche 1, puis disparaît à partir de la planche 3. ChatGPT simplifie un petit détail
  de planche en planche si le prompt ne le nomme pas. Le double pont est maintenant écrit dans le
  contexte, le prompt 0 bis et les prompts 10 à 19. Les planches déjà faites passeront une retouche
  « lunettes » chacune (or et barre), avant le LoRA.
- Sky, yeux fermés, deuxième essai : les quatre bons (rire, contentement, soulagement, clignement), avec
  l'image collée dans le même message. La palette de face de Sky est finie.
- Sky, image maître en or : la retouche ChatGPT a doré la monture et gardé la barre, sans toucher au reste
  (écart moyen de 2 à 4 sur 255 hors des lunettes). Elle a laissé l'ancienne barre en trait sombre entre
  les sourcils. Effacer ce trait au pixel (remplissage par la peau voisine) a laissé une trace en peigne,
  pire que le trait : pour un détail dans un visage, une retouche ChatGPT ciblée vaut mieux.
- Sky, 0 ter : le trait entre les sourcils est atténué, pas effacé ; l'auteur l'accepte. Chaque retouche
  ajoute un peu de dérive (écart moyen à la v1 : 2,8 après le 0 bis, 4,7 après le 0 ter). À surveiller :
  le trait ne doit pas passer dans les planches de trois-quarts.
- Sky, trois-quarts 1 : bonne du premier coup avec l'image maître v2 et la ligne des lunettes dans le
  prompt : monture dorée et barre partout, l'œil bleu devant. Trois-quarts léger, plus doux que la rotation.
- Sky, lunettes, vu par l'auteur : l'ancienne monture était bicolore (argent et tirets sombres). En la
  dorant, ChatGPT a gardé les tirets : des taches sombres sous les verres, sur la v2 et sur la planche 1
  de trois-quarts qui en vient. Une retouche les recopie fidèlement, défauts compris : il faut nettoyer
  l'image maître avant de s'en servir (prompt 0 quater).
- Sky, série 1 archivée (sur le disque externe, rien de supprimé). Corriger les lunettes demandait une
  dizaine de retouches sur des feuilles de 6 visages : autant d'allers-retours que tout refaire depuis une
  image maître propre, pour un résultat moins homogène. Série 2 : une nouvelle conversation ChatGPT (qu'il
  ne voie plus les anciennes lunettes), l'image maître v3, et les prompts corrigés d'emblée. L'auteur
  change aussi la barbe (3 jours) et veut l'œil aveugle de la taille de l'autre.
- Sky, image maître v3 : le trait et les taches sont partis, la barbe est passée à 3 jours. ChatGPT n'a pas
  voulu réduire l'œil aveugle à la taille de l'autre, malgré plusieurs essais de l'auteur : on garde la v3
  telle quelle, c'est la référence de la série 2. Le prompt ne dira donc rien de la taille de cet œil.
- Sky, l'œil aveugle : ChatGPT refuse aussi de baisser sa paupière, et remet les taches au-dessus des yeux.
  Il ouvre grand cet œil pour montrer le blanc, le détail qui définit le perso. On garde la v3.
- Sky, série 2, rotation : bonne du premier coup avec l'image maître v3 (le 2026-10-15).
- Sky, série 2, en pied : bonne (bague, baskets noires, pas de caleçon visible : la précision du prompt a suffi).
- Sky, série 2, palette de face 1 : bonne du premier coup, lunettes identiques dans les six cases.
- Sky, série 2, palette de face 2 : bonne du premier coup. Le rire a les deux yeux fermés, l'aveugle aussi :
  une première en génération. Le contexte de la série 2 (la règle de l'œil aveugle, le côté par l'œil bleu)
  et « the blind one too, not a wink » ont suffi ici : la retouche des yeux fermés sera peut-être plus courte.
- Sky, série 2, palette de face 3 : bonne. Le sourcil de la confusion est du bon côté du premier coup
  (« the eyebrow above his blue eye, on the left of the image »). Le doute reste discret, comme dans la série 1.
- Sky, série 2, palette de face 4 : bonne du premier coup, désir compris (« Craving » et la galette).
- Sky, série 2, palette de face 5 : bonne du premier coup. Le contentement et le soulagement ferment les deux
  yeux en génération, comme le rire : dans la série 2, « both eyes closed (the blind one too, not a wink) » marche.
- Sky, série 2, palette de face 6 : bonne, sauf la malice, sortie du côté de l'œil aveugle avec la tête penchée de
  ce côté, alors que la même formulation avait marché dans la série 1 : elle n'est pas fiable. Pour la reprise :
  « head straight and not tilted » et « the other corner stays low ». Tous les yeux fermés de la série 2 sont
  bons en génération : plus besoin de retouche pour eux. Le clignement (mi-clos, fermé) se fait dans les reprises.
- Sky, série 2, reprises : le clignement (mi-clos, fermé) est bon du premier coup. La malice résiste : deux
  essais, et ChatGPT remet le sourire du côté de l'œil aveugle. On la garde là. Le doute reste discret. La
  palette de face est finie : 36 émotions et le clignement.
- Sky, série 2, signatures 1 : quand ses deux yeux regardent de côté (le feu vert), ChatGPT donne un iris à
  l'œil aveugle. À écrire dans les prompts : « only his blue eye looks sideways, the blind eye stays entirely white ».
  Les sourcils levés d'un seul côté restent faibles en génération : on tente la retouche (prompt G bis).
- Sky, série 2, retouche G bis : trois sur quatre. En retouche, ChatGPT lève un sourcil du bon côté et enlève un
  iris de trop. Il ne change pas le côté d'un sourire : la malice reste de son côté gauche. Pour un sourcil
  d'un seul côté, la retouche marche mieux que la génération.
- Sky, série 2, signatures 2 : le haussement d'épaules est bon. Le sourire et le rire, refusés par l'auteur :
  « trop gentillet, on sent pas assez le monstre ». « Predatory, psychopathic grin » seul donne un petit malin
  qui ricane. Il faut décrire ce qui fait peur : l'ombre sur le haut du visage, la pupille minuscule, le sourire
  trop large, les crocs, le visage figé (prompt H bis).
- Sky, série 2, H bis : le monstre passe (« mieux » pour l'auteur). Ce qui a marché : décrire ce qui fait peur
  (l'ombre, la pupille minuscule, le sourire trop large, les crocs, le visage figé) et dire à ChatGPT que sa planche
  d'avant était trop gentille. Les signatures de Sky sont finies, plus le rire de trois-quarts.
- Sky, série 2, bouches : bonnes. ChatGPT redessine toute la tête à chaque case (c'est le gros plan demandé) ;
  d'une case à l'autre, le haut du visage bouge de 2 à 3 pixels (mesuré par corrélation de phase). Ce sont des
  références de forme pour le LoRA et l'inpainting local, pas des calques à coller tels quels.
- Sky, série 2, bouches du sourire : bonnes du premier coup. Sky est fait, sauf la palette de trois-quarts
  (à décider) et ce qui vient après ChatGPT : passage local, LoRA, voix. Ce qui a fait la différence par
  rapport à la série 1 : une image maître propre dans une conversation neuve, un contexte qui redit les
  règles (l'œil aveugle, le côté par l'œil bleu, les lunettes), et une retouche dès qu'un détail résiste.
- Sky, série 2 : l'auteur veut la palette de trois-quarts tout de suite (« on va pas prendre de risque »).
  Pour l'angle, on joint la vue trois-quarts droite de la rotation au lieu de l'image maître.
- Sky, série 2, trois-quarts 1 : bonne du premier coup. Avec la vue de la rotation jointe, l'angle est enfin un vrai trois-quarts.
- Sky, série 2, trois-quarts 2 : bonne, sauf le rire. De trois-quarts, l'œil aveugle (au fond) reste ouvert malgré
  « the blind one too, not a wink », alors que de face il se fermait. Retouche à la fin de la palette.
- Sky, série 2, trois-quarts 3 : bonne du premier coup, sourcils compris (du côté de l'œil bleu, devant).
- Sky, série 2, trois-quarts 4 : bonne du premier coup (main droite et bague pour la gêne, la galette dessinée pour le désir).
- Sky, série 2, trois-quarts 5 : bonne, sauf le soulagement (l'œil aveugle ouvert) et le triomphe (une chevalière gravée
  à l'index). « The bronze ring on its little finger » ne suffit pas : écrire « his only ring is a thin plain bronze band ».
- Sky, série 2, trois-quarts 6 : bonne, malice comprise (de son côté gauche, comme de face). Les bagues restent le point
  faible : deux bagues à la fatigue malgré « his only ring », une bague au mauvais doigt à l'ennui. Les mains se
  corrigeront au passage local si la retouche ne suffit pas.
- Sky, série 2, retouche K7 : trois sur quatre. La règle générale de la fin du prompt (« when Sky closes his eyes, the
  eyelid of his blind eye closes too ») a débordé sur une case où rien ne devait se fermer : le triomphe y a perdu son
  œil aveugle ouvert. Dans une retouche à plusieurs cases, écrire chaque règle dans sa case, jamais en général.
- Sky, série 2 : fini côté ChatGPT, les 50 cases de l'inventaire. Restent le passage local, le LoRA, le test standard et la voix.
