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

## 2026-10-15 — Avant le test du LoRA de Sky : licences, location, carte AMD

Vérifié sur les pages officielles, le 2026-10-15 :
- **NoobAI-XL** (Laxhar, README de noobai-XL-Vpred-0.5) : « We prohibit any form of commercialization, including but not
  limited to monetization or commercial use of the model, derivative models, or model-generated products », et les LoRA
  doivent être publiés. Incompatible avec une chaîne monétisée, alors que CLAUDE.md le cite comme candidat : signalé à l'auteur.
- **Illustrious XL early release v0.1** (OnomaAIResearch) : Fair AI Public License 1.0-SD. La page dit « We do not restrict any
  upload or spread of the generation results », la licence ne couvre pas les sorties ; elle « décourage » la monétisation et
  interdit de monétiser un modèle dérivé fermé. Les obligations sur un dérivé (un LoRA) jouent s'il est distribué.
- **Animagine XL 4.0** (cagliostrolab) : CreativeML Open RAIL++-M, la licence de SDXL sans modification : usage commercial permis,
  avec les restrictions d'usage.
- **Location** : RunPod, une RTX 4090 (24 Go) vers 0,34 $/h en Community Cloud (computeprices.com, relevé d'août 2026), facturée
  à la seconde ; dépôt minimum de 10 $, non remboursable (documentation RunPod).
- **La carte AMD** : d'abord écrit « pas prise en charge, il faut compiler PyTorch », d'après des retours anciens. C'est faux depuis
  2026 : AMD (projet TheRock, ROCm 7.14) marque gfx1010 « Build Passing, Sanity Tested, Release Ready » sur Linux et Windows, et
  publie PyTorch pour elle (`torch[device-gfx1010]`, index https://repo.amd.com/rocm/whl-multi-arch/), installable avec pip sans
  sudo : 869 Mo de paquets pour Python 3.13 (mesuré par requêtes HEAD). Un test publié l'a fait tourner sur une RX 5700 XT, mais
  sous Windows (PR unsloth #11755, septembre 2026) ; sur Linux, pas de retour publié sur cette carte. Piège connu : ROCm 7 est
  2 à 3 fois plus lent sur gfx101x pour certaines opérations (le VAE en tuiles), corrigé par MIOPEN_FIND_MODE=TRUST_VERIFY_FULL
  (TheRock, issue #2848). Pour une image, Vulkan marche aussi sur la carte (pilote RADV), avec stable-diffusion.cpp, sans entraînement.
- **La RAM** : 15,9 Go, dont 3 réservés au démarrage en pages de 1 Go (option du noyau `hugepages=3`, rien ne s'en sert) ; avec
  VS Code, les navigateurs et Discord ouverts, il en reste 3,7 et le swap est plein aux deux tiers.
- **AniSora sur 8 Go** (vérifié le 2026-10-15) : la version la plus légère d'AniSora est la V3.1 « 12GB VRAM » (ModelScope,
  2025-09-25) ; les V3 à V3.2 sont des modèles de 14 milliards de paramètres, en fp16 et fp8 pour ComfyUI (Kijai/WanVideo_comfy),
  pas de version GGUF publiée. Son modèle de base, Wan 2.2 14B, tourne compressé (GGUF Q4) sur des cartes NVIDIA de 8 Go : environ
  111 s par clip sur une RTX 4060 (lilting.ch), 181 s pour 5 s en 480p (runflow.io), avec environ 13 Go de RAM (workflow Cordux).
  Aucun essai publié sur une carte AMD de la génération de la 5700 XT : à tester après les images, sans promesse.
- **Test de la carte AMD, le 2026-10-15** : PyTorch 2.12.0+rocm7.14.1 (paquets AMD `torch[device-gfx1010]`, 869 Mo, venv
  `/home/sky/venvs/kebab`, 5,1 Go installés, sans sudo) voit la RX 5700 XT : gfx1010, 8,57 Go. Produit de matrices fp16 4096 :
  5,6 TFLOPS ; convolution fp16 512 canaux en 128×128 : 14 ms (5,3 TFLOPS), avec MIOPEN_FIND_MODE=TRUST_VERIFY_FULL ; attention
  sur 4096 jetons : 50 ms. Résultats justes (écart relatif de 3 à 4 dix-millièmes avec le calcul du processeur, normal en fp16).
  Pas encore d'image : il faut le modèle de base.
- **Les autres options vérifiées** (le 2026-10-15) : Modal, 30 $ de calcul gratuit par mois (une L4 de 24 Go à 0,000222 $/s, soit
  environ 0,80 $/h : près de 37 h par mois), piloté par du code ; Kaggle, environ 30 h de GPU par semaine d'après les utilisateurs
  (T4 ou P100, 16 Go, sessions de 12 h, notebooks) ; Colab gratuit, sans quota publié, notebooks seulement, pas d'interface web
  comme ComfyUI sans payer ; AMD Developer Cloud, des crédits gratuits sur MI300X pour les développeurs indépendants et les projets
  open source, sur demande, carte bancaire exigée, crédits valables 30 jours selon AMD (les montants publiés varient). Hugging Face
  ZeroGPU (5 min par jour) et Paperspace gratuit (8 Go) ne servent à rien ici.
- **Modal, le 2026-10-15** : compte « ludovik1241 » créé par l'auteur, client Modal 1.6.1 dans `/home/sky/venvs/modal`, jeton dans
  `~/.modal.toml` (droits 600, hors du repo). Sans moyen de paiement, Modal ne donne que 1 $ sur les 30 $ mensuels, et refuse toute
  carte graphique (« Please add a payment method to use T4 GPU functions ») : rien n'a été facturé. Pour s'en servir : ajouter une
  carte et régler aussitôt la limite de dépense (modal.com/docs/guide/budgets).
- **Première image en local, le 2026-10-15** : ComfyUI (commit ba99487) sur la RX 5700 XT, Animagine XL 4.0, 1024×1024, 25 pas,
  euler_ancestral, cfg 5, seed 42 (`workflows/premiere-image_sdxl.json`). Échantillonnage : 3,65 s par pas, 93 s pour l'image.
  Le premier lancement a pris 505 s en tout : le chargement du modèle depuis le disque USB et la recherche des noyaux de MIOpen.
  Pièges : (1) la « dynamic VRAM » de ComfyUI échoue sur cette carte (« VBAR allocation failed », l'espace d'adresses virtuel
  refusé) : `--disable-dynamic-vram`. (2) La RAM : avec le navigateur ouvert, le chargement a rempli la mémoire, arrêté à la main ;
  navigateurs fermés, la première image est passée, mais la deuxième (avec `--cache-none`, qui recharge le modèle) a déclenché le
  tueur de mémoire du système, qui a tué VS Code et la session de Claude, ComfyUI compris. Parade : lancer ComfyUI dans son propre
  groupe mémoire (`systemd-run --user --scope -p MemoryMax=7G`, possible sans sudo, testé), garder le modèle en mémoire entre deux
  images (pas de `--cache-none`), et faire tourner Claude dans un terminal plutôt que dans VS Code (VS Code prend 2 à 4 Go).
- **Les 3 Go réservés** : l'option `hugepagesz=1G default_hugepagesz=1G hugepages=3` de `/etc/default/grub` vient du réglage du
  minage (`/opt/linux-upgrade/mining/tune_system.sh`, pour xmrig) ; ces pages ne servent à rien en ce moment. Les libérer demande
  les droits root (le compte n'est pas dans le groupe sudo).
- **Le minage désinstallé, à la demande de l'auteur, le 2026-10-15** : rien ne tournait. Supprimés : les services utilisateur
  (`mining-*`, `monerod`, `monero-wallet-rpc`) et système (`mining-gpu-power-cap`, `mining-thp-disable`), les programmes
  (`/opt/miners` : xmrig, xmrig-mo, lolMiner, SRBMiner), `/etc/sysctl.d/99-mining-hugepages.conf`, les règles sudo du minage
  (`/etc/sudoers.d/mining` et `mining-gpu-powercap`), l'option `hugepages=3` de GRUB (copie de l'ancien fichier :
  `/etc/default/grub.avant-desinstallation-minage`, puis update-grub), le module msr, et `/opt/linux-upgrade/mining`, archivé avant
  dans `/media/sky/VIDE 1To/archives/mining_opt-linux-upgrade_2026-10-15.tar.gz` (sa config et son `.env`). Pas touché : le
  portefeuille Monero et la chaîne (105 Go) sur « VIDE 1To », la règle sudo de linux-upgrade. Les 3 Go réservés sont libérés sans
  redémarrer : 11,3 Go disponibles avec VS Code ouvert.
- **Le sudo** : le compte a tous les droits root sans mot de passe (`/etc/sudoers.d/linux-upgrade`). CLAUDE.md dit « Debian sans
  sudo, installations en espace utilisateur » : signalé à l'auteur, la règle reste en place tant qu'il ne l'a pas changée.
- **Deuxième test, le 2026-10-15, minage désinstallé** : ComfyUI comme service utilisateur, plafonné à 10 Go de RAM
  (`systemd-run --user -p MemoryMax=10G`). Sans autre réglage, chaque image recopie le modèle en RAM (7,4 Go de mémoire anonyme
  au pic) et la deuxième fait déborder le plafond : c'est ComfyUI que le système arrête, plus VS Code. Avec `--highvram`, le modèle
  reste sur la carte et la RAM tient (2,8 Go), mais le VAE ne trouve plus de place sur la carte (« tried to allocate 2.25 GiB »),
  même en tuiles de 512. Ce qui marche : `--highvram --cpu-vae`. Mesuré : 204 s pour la première image (le modèle lu depuis le
  disque USB, environ 100 s), puis 130 s par image (91 s de calcul à 3,64 s par pas, le VAE sur le processeur). RAM de ComfyUI :
  2,9 à 3,8 Go ; VRAM : 5,7 à 6,5 Go ; RAM disponible pour le reste : 7,7 Go. Le lanceur : `pipeline/comfyui.py`.
- **Modèles déjà prêts, cherchés sur Hugging Face le 2026-10-15** : des LoRA de style « anime des années 90 » existent pour la
  famille SDXL, petits et sans compte : `ntc-ai/SDXL-LoRA-slider.90s-anime` (MIT), `strkyyy/anime-90s-retro` (openrail++, mot
  déclencheur `4n1m390s`), `nDimensional/Shaded-Retro-Style-Anime-with-Natural-Language-SDXL-LoRA` (creativeml-openrail-m). Les
  dépôts « Muapi » sont des copies de modèles de Civitai : leur licence affichée n'est peut-être pas celle de l'auteur d'origine.
  Éviter les LoRA qui imitent un artiste vivant ou un studio nommé (Sadamoto, Ghibli) pour une chaîne monétisée. Pour garder un
  perso sans entraînement, il existe FLUX.1 Kontext, Qwen Image Edit et Krea 2, à partir d'une image de référence, mais faits pour
  la photo, autour de 11 à 12 Go en fp8 (environ 6 Go compressés), et pas testés sur de l'anime : pour Sky et ses détails
  asymétriques, le LoRA reste la voie sûre.
- **Le LoRA de Sky, v1 : le jeu et l'entraînement, le 2026-10-15.** Le jeu : 105 images retenues (`pipeline/preparer_lora.py sky v1`),
  agrandies ×4 avec Real-ESRGAN anime 6B par tuiles de 192 pixels (d'un seul bloc, une convolution demandait 4,5 Go et débordait),
  puis ramenées à environ un mégapixel ; légendes en tags Danbooru, mot déclencheur `skykebab`, les traits fixes jamais écrits.
  Sur `<sorties_root>/lora/sky/jeu_v1/`. L'envoi vers Kaggle fichier par fichier allait à 45 Ko/s (210 fichiers, un aller-retour
  chacun) : en un seul zip, 94 Mo en 13 s, et Kaggle le décompresse tout seul. Jeu privé `skyzer/kebab-lora-sky-jeu-v1`.
  L'entraînement : notebook privé `skyzer/kebab-lora-sky-v1` sur une T4, kohya sd-scripts v0.12.0, Animagine XL 4.0, LoRA de rang 32
  (alpha 16), le UNet seul, AdamW8bit à 1e-4, cosinus, 8 époques × 2 répétitions, sans retournement, fp16 et le VAE en fp32.
  Le script et sa description : `pipeline/kaggle/lora_sky_v1/`. Lancé vers 15 h.
- **LoRA de Sky v1, résultat, le 2026-10-15.** Entraînement : 1 680 étapes en 1 h 02 (2,21 s par étape sur une T4), 68 min en tout,
  perte moyenne de 0,072 à 0,062, sans valeur aberrante ; 4 fichiers de 170 Mo (époques 2, 4, 6, 8) dans `<modeles_root>/loras/`.
  Premier lancement raté : kohya écrit le cache des latents à côté des images, et `/kaggle/input` est en lecture seule (corrigé :
  les images sont copiées dans `/tmp/jeu`). Le test standard en local (`pipeline/test_lora.py`), à part trois pièges : le chargement
  classique du LoRA garde une copie des poids d'origine sur la carte (avec `--highvram`) et déborde des 8 Go → le nœud
  `LoraLoaderBypassModelOnly`, qui ajoute le LoRA pendant le calcul ; `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True` fait échouer
  toute allocation sur cette carte (comme la « dynamic VRAM ») ; après une saturation, la carte reste bloquée jusqu'au redémarrage
  de ComfyUI. Avec le LoRA en bypass et les encodeurs de texte en fp8 : 4,5 s par pas, 2 min 25 par image.
  Ce que montre le test (planche : `<sorties_root>/comfyui/test-standard_sky_v1_planche.png`) : le visage, les cheveux, la barbe,
  les lunettes dorées et les deux colliers sont appris. L'œil aveugle n'est juste que de face (tests 1 et 8) ; de trois-quarts et en
  situation, les deux yeux deviennent blancs (2, 6) ou bleus (9). La tenue tient en buste, mais pas ailleurs : chemise noire ou veste
  en situation (6, 7, 10), et en pied (5) une autre tenue complète (long manteau, torse nu, pantalon marron, bottes) : le jeu n'avait
  qu'une seule image en pied. Pistes pour une v2 : des images en pied et en situation dans le jeu, un tag pour les yeux
  (« heterochromia ») dans les légendes, et la retouche locale de l'œil en production en dernier recours.
- **Préparé pour la v2, le 2026-10-16** : les 5 prompts en pied et en gestes de Sky, la liste de contrôle de chaque planche et la
  procédure du LoRA v2 (`image/persos/sky/prompts-chatgpt.md`, fin du fichier) ; `pipeline/preparer_lora.py` sait légender les vues
  en pied, les poses et les gestes, et ajoute le tag des yeux (`heterochromia`, `fiche.json` > `lora` > `tag_yeux`) là où les deux
  yeux sont ouverts ; `pipeline/test_lora.py` l'ajoute aux prompts ; le notebook `pipeline/kaggle/lora_sky_v2/` est prêt.
- **L1, premier essai, le 2026-10-16 : refusé.** Avec l'image maître v3 jointe (elle s'arrête au buste) et « black tracksuit
  trousers » seuls, ChatGPT a mis un pantalon de costume (pli, braguette) porté haut, la chemise rentrée dedans ; et case 3, un iris
  bleu à l'œil aveugle. Leçon : pour une image en pied, joindre l'image en pied validée (`references/pied_v1.png`) et décrire la
  façon de porter la tenue (chemise par-dessus, jogging à cordon porté bas sur les hanches, « not dress trousers »), pas seulement
  les vêtements. Fiche, prompts L1 à L5 et liste de contrôle corrigés.
- **L1, deuxième essai : validé.** Avec `references/pied_v1.png` jointe et la façon de porter la tenue décrite, la tenue est juste
  dans les trois cases, l'œil aveugle aussi. Défaut laissé passer par l'auteur : un seul anneau au collier au lieu de deux.
  Découpe : 3 cases de 512 × 1024 dans `references/`.
- **L2 : validé du premier coup.** Les profils nommés par leur œil (« we see only his blind left eye ») : chaque profil montre le bon.
  Défaut : de dos, une bague à chaque auriculaire, malgré « His only ring » ; à corriger au passage local. Les prompts suivants
  ajoutent « His left hand has no ring ».
- **L3 : validé du premier coup.** Yeux et tenue justes. Accoudé du coude gauche au lieu du droit, sans conséquence. Encore une bague
  à chaque main (assis de face) : l'auteur arrête là le contrôle des bagues, le LoRA n'apprend pas un détail de quelques pixels ;
  les ratés sont listés dans `fiche.json` > `_a_completer`, pour le passage local ou l'inpainting en production.
- **L4 : validé.** Six gestes de face, les yeux justes partout. Case 3 (la bouche pleine) : il ne mâche pas, ChatGPT a fait une bouche
  fermée aux joues plates. Gardée, avec une légende qui dit ce qu'elle montre : `preparer_lora.py` lit maintenant
  `fiche.json` > `lora` > `legendes_par_fichier` pour les gestes. Le prompt L5 insiste sur les joues gonflées.
- **L5 : validé du premier coup.** Le trois-quarts côté droit, à l'angle de `references/trois-quarts-droit_v1.png` jointe : l'œil
  bleu devant, l'œil aveugle blanc dans les six cases. Avec « both cheeks visibly puffed out », il mâche vraiment (case 3).
  La série en pied et en gestes est finie : 21 images en plus pour le jeu v2 (126 en tout).
- **LoRA de Sky v2, le 2026-10-16 : jeu préparé et entraînement lancé.** `preparer_lora.py sky v2` : 126 images (105 + les 21 en pied
  et en gestes), le tag `heterochromia` dans 107 légendes, environ 10 minutes sur la carte AMD ; sortie
  `<sorties_root>/lora/sky/jeu_v2/`. Envoyé en un zip (111 Mo, 10 s à 12 Mo/s) au jeu privé `skyzer/kebab-lora-sky-jeu-v2`, puis
  `kaggle kernels push -p pipeline/kaggle/lora_sky_v2 --accelerator NvidiaTeslaT4` : mêmes réglages que la v1, pour comparer.
- **LoRA de Sky v2 entraîné, le 2026-10-16** : 80 min sur la T4 de Kaggle (126 images × 2 répétitions × 8 époques = 2016 pas,
  perte moyenne finale 0,063). Les 4 fichiers (époques 2, 4, 6, 8) sont vérifiés et copiés dans `<modeles_root>/loras/`.
  Le journal de Kaggle est dans `<sorties_root>/lora/sky/kaggle_v2/`. Reste le test standard.
- **Le disque système de sky-master était plein (2026-10-16)** : 16 Ko libres sur 233 Go, et toutes les commandes de Claude
  échouaient (sortie impossible à écrire dans /tmp). Avec l'accord de l'auteur, on a supprimé le SDK Android (13 Go) et le dépôt
  local de la fleet multi-agent `~/.claude-channel` (30 Go, presque tout dans son `.git`, l'historique reste sur GitHub). Les
  fichiers qui n'existaient qu'en local, la crontab et les services d'avant sont archivés dans
  `/media/sky/disque 5T/archives/claude-channel_2026-10-16/`. Les tâches de la fleet sont arrêtées ; le réglage du clavier
  pour Barrier est gardé (`~/.local/bin/setxkbmap-fleet.sh`), ainsi que la mise à jour des IP du mesh. Après : 42 Go libres.
- **Test standard du LoRA de Sky v2 (`sky_v2.safetensors`), le 2026-10-16** : planche
  `<sorties_root>/comfyui/test-standard_sky_v2_planche.png`, 2 min 20 par image. Contre la v1 :
  - l'œil aveugle est juste sur les 10 images (la v1 : seulement de face, 1 et 8), y compris de trois-quarts, de profil, dans le
    sourire en monstre (9) et sous la pluie (10). Le tag `heterochromia` et les vues de plus ont marché ;
  - la chemise blanche à lys est juste sur 9 images (la v1 en ratait 3) ; il reste la nuit sous la pluie (10), en chemise noire à lys ;
  - les directions « facing left / right » ne sont pas toujours suivies, mais les yeux restent du bon côté du visage ;
  - en pied (5), la tenue reste fausse sans aide : la chemise s'allonge en pan jusqu'aux genoux, les lys passent sur le pantalon,
    des bracelets apparaissent. L'époque 6 fait pire (manteau ouvert, short) ; la légende exacte de l'entraînement aussi (pantalon
    à lys). Avec la tenue écrite (`white shirt, untucked shirt, black pants, track pants, black sneakers`, et en négatif
    `striped pants, side stripes, stripes, patterned pants, bracelet`) : juste sur deux graines, sauf un fin passepoil blanc sur le
    pantalon, que « track pants » appelle sans doute. Recette notée dans `fiche.json` > `lora` > `tags_en_pied`.
- **Le style de la série est décidé (l'auteur, le 2026-10-16)** : celui des images de référence de Sky et de Maëlle, un anime des
  années 90 entre *Street Fighter II*, *Evangelion* et Ghibli. Écrit dans `image/style.md`. Ce qui fait varier le visage au test
  du LoRA v2 : le LoRA n'a vu que du fond gris, alors dans un décor c'est Animagine qui dessine, avec son rendu moderne. Prochaine
  piste : IP-Adapter, avec l'image maître de l'axe comme référence de style à chaque image.
- **En pied, « sweatpants » au lieu de « track pants » (2026-10-16)** : la bande blanche disparaît sur les deux graines (1005,
  2005). Le jogging à cordon, la chemise par-dessus, juste. Reste : des semelles blanches. Recette mise à jour dans
  `fiche.json` > `lora` > `tags_en_pied`. IP-Adapter Plus SDXL et son encodeur téléchargés (3,4 Go, Apache 2.0, empreintes
  vérifiées, `modeles.yaml`), nœuds ComfyUI_IPAdapter_plus installés : chargés sans erreur par ComfyUI.
- **IP-Adapter, premier essai (2026-10-16)** : IP-Adapter Plus SDXL en « style transfer », poids 1,0, l'image maître v3 de Sky
  comme référence, sur les tests 1, 6, 7, 8, 10 du LoRA v2 (mêmes graines). Il tient sur la carte de 8 Go, sans temps en plus
  (2 min 26 par image). Mais le résultat est moins bon : il recopie le contenu de la référence (des lys en fond, la boisson
  orange, la nourriture, même sous la pluie), la peau pâlit et les couleurs tournent au pastel, loin du rendu chaud de l'image
  maître. Seul gain : la chemise redevient blanche sous la pluie. À essayer : un poids plus faible (0,4 à 0,6), et surtout une
  référence sans perso ni objets, un décor vide dans le style (le kebab, prompt KB1).
- **Le kebab, le 2026-10-16** : la maquette vue de dessus faite dans ChatGPT (`image/decors/kebab/maquette_v2.png`), après trois
  versions et cinq retouches. Ce qui marche : décrire le plan zone par zone, dire « 2D, NOT a 3D render », retoucher dans la case
  « Décrivez les modifications » de l'image. Ce qui rate : l'orientation des tables et des chaises, ChatGPT refait sa disposition à
  lui, même avec un plan joint, et une nouvelle conversation fait revenir ce qu'on avait enlevé. D'où un plan vu de dessus en code
  (`pipeline/plan_kebab.py`, `plan_v2.png`) qui fait foi pour la disposition. Le canon est tranché : Mohamed à Annemasse.
- **Le plan du kebab peint, du premier coup (2026-10-17)** : le plan dessiné en code (`plan_v2.png`) joint en premier, la maquette
  en second pour le style, et une vue « straight from above, exactly like the plan, as if the plan had been painted over ». Chaque
  table et chaque chaise à sa place, là où cinq retouches de la maquette en vue isométrique avaient échoué. Gardé par l'auteur
  (`image/decors/kebab/plan-peint_v1.png`) ; les autres images du kebab supprimées à sa demande (dans l'historique git).
  À réutiliser pour chaque décor : dessiner le plan, puis faire peindre la vue prise du même point.
- **Le plan du kebab v3 (2026-10-17)** : l'auteur annote le plan dans ChatGPT (outil « Annoter ») : c'est le moyen le plus rapide
  pour qu'il montre une disposition. Validé : la table de Sky dans l'angle de la banquette, pour cinq, Patrick au bout ; le miroir
  sur toute la banquette du fond ; la rampe basse, l'angle ouvert sur l'escalier ; l'herbe entre les rails du tram ; trois
  lumières par axe (jour, pluie, nuit). 21 axes (`image/decors/kebab/axes.md`). Le fond de l'axe 6, fait avant, est à refaire.
  Leçon de l'axe 6 : écrire dans chaque prompt d'où vient la lumière (la rue seule) et le miroir fumé sans reflet.
- **Le plan du kebab et ses 25 axes validés (2026-10-17)** : `plan_v5.png` (sans caméras, pour ChatGPT) et `plan-axes_v5.png`
  (avec caméras, pour Claude). Les décisions de l'auteur sur le décor sont réunies en tête de `image/decors/kebab/axes.md`, avec le
  modèle de prompt d'un axe. 45 fonds en tout (23 de jour, 12 de pluie, 10 de nuit), 9 pour le pilote. La méthode qui marche :
  l'auteur annote le plan dans ChatGPT, Claude le redessine en code, ChatGPT peint la vue prise du même point.
- **La base fixe du kebab (2026-10-17)** : le plan peint `image/decors/kebab/plan-peint_v2.png`, refait à partir du plan v5 sans
  caméras (joint en premier) et du dernier essai pour le style (« where it differs from the plan, follow the plan »), avec toutes
  les corrections écrites d'avance dans le prompt : juste du premier coup, sauf la caisse, encore tournée vers la rue. Validé par
  l'auteur ; les autres images du kebab supprimées à sa demande.
- **La vue en volumes (2026-10-17)** : pour l'axe 6, ChatGPT n'a tenu ni la place de la caméra dessinée sur le plan, ni ce
  qu'elle voit (vue de face au lieu de biais, la porte du haut visible). D'où `pipeline/vue_kebab.py` : la vue de chaque axe en
  volumes simples, en perspective, avec les mesures du plan (axes lus dans `plan_kebab.py`), sans texte. ChatGPT la peint,
  comme le plan vu de dessus. Les mêmes vues pourront guider le modèle local (ControlNet, profondeur ou contours).
- **Premier fond du kebab validé (2026-10-17)** : l'axe 6, la table de Sky (`image/decors/kebab/table-du-fond/fond_v1.png`).
  Trois essais : le plan avec une caméra (vue de face au lieu de biais), puis la vue en volumes (le bon angle du premier coup),
  puis une retouche de deux points (le mur de l'escalier, la plante de l'angle). La vue en volumes devient la méthode de tous les axes.
- **Deuxième fond du kebab validé (2026-10-17)** : l'axe 7, le contrechamp depuis la place de Sky
  (`image/decors/kebab/table-du-fond-contrechamp/fond_v1.png`). Le premier essai avait raté l'escalier parce que la vue en volumes
  ne le montrait pas : ChatGPT peint ce qu'il voit dans la vue, rien de plus. Corrigée (le côté de l'escalier suit la pente,
  sa rampe au-dessus, la voie du tram en herbe, les arbres d'en face), la vue a donné l'image juste du premier coup.
- **Les fonds 20, 21 et 8 du kebab (2026-10-17)** : 20 et 21 du premier coup, avec un fond déjà validé du même coin joint en
  troisième image (la même plante, le même miroir). Le 8 en quatre essais : l'angle redessiné par l'auteur, puis le mur de la
  cuisine pris de face (de biais, la ligne du plafond plongeait), puis la vitrine dessinée encastrée dans le comptoir (posée en
  retrait, ChatGPT la mettait derrière) et l'horloge dessinée ronde (en carré, il peignait les deux). Ce que la vue en volumes
  montre, ChatGPT le peint : chaque objet doit y avoir sa vraie forme et sa vraie place.
- **La vue en volumes avec un tampon de profondeur (2026-10-17)** : l'ancien rendu triait les boîtes du plus loin au plus
  proche et dessinait le décor dans l'ordre ; quand la cage de l'escalier est montée jusqu'à l'étage, sa porte est apparue à
  travers le plafond (à l'axe 2, là où ChatGPT l'avait mise en l'air). `pipeline/vue_kebab.py` remplit maintenant chaque face
  avec un tampon de profondeur et trace les contours là où deux faces se touchent : ce qui est caché reste caché. Vérifié :
  depuis le trottoir à gauche (axe 2), le plafond cache la porte ; du pied de l'escalier (axe 11), on la voit en haut.
- **Les fonds 2, 11, 10 et 1 du kebab, et les enseignes en code (2026-10-17)** : quatre fonds validés de plus (l'entrée,
  l'escalier jusqu'à la porte de Datastream, le pied de l'escalier, la façade). Avec deux ou trois fonds validés joints pour la
  cohérence, ChatGPT tient les mêmes objets d'un axe à l'autre. La façade : ChatGPT peint des enseignes vides, et
  `pipeline/enseignes.py` y pose « KEBAB » et « DATASTREAM » (seulement sur les pixels du panneau : les feuilles restent devant).
- **La façade en quatre lumières (2026-10-17)** : ouverte de jour, puis en retouches successives, une chose à la fois : fermée
  (même lumière), puis la pluie (depuis la fermée), puis la nuit (depuis la fermée de jour, pas depuis la pluie). Chacune du
  premier coup. Les enseignes en code : `pipeline/enseignes.py` compare chaque pixel à son voisinage (flou de 6 px) pour laisser
  passer les traits de pluie devant les lettres sans couper les lettres sous les flaques de lumière des spots, la nuit.
- **Les 9 fonds du pilote faits (2026-10-17)** : axes 1, 2, 6, 7, 8, 10, 17, 20, 21, plus l'axe 11 et la façade en quatre
  lumières (ouverte, fermée, pluie, nuit). En deux jours avec la mise en place du plan. La méthode, stable depuis l'axe 20 : la vue
  en volumes (`pipeline/vue_kebab.py`) + le plan peint + un ou deux fonds déjà validés du même coin ; une retouche de deux points
  au plus si besoin ; les textes (enseignes) en code.
- **YouTube, le 2026-10-17 (guides tiers, à confirmer sur les pages officielles)** : le programme partenaire demande 1 000 abonnés
  et 4 000 heures de visionnage sur 12 mois (ou 10 millions de vues en Shorts sur 90 jours) ; pour les nouvelles chaînes, 8 000
  heures (ou 20 millions de vues en Shorts) à partir du 1er février 2027, annoncé le 10 août 2026 (air.io, vidiq.com). RPM estimé
  en France : environ 2,5 à 2,6 $ pour 1 000 vues (dynamoi.com, tubeanalytics.net). Avec des épisodes de 5 minutes, il faut de
  l'ordre de 100 000 vues par an pour atteindre 4 000 heures : d'où une version compilée de chaque arc.
- **Depuis la salle, pas de cage d'escalier (2026-10-17)** : à l'axe 12, la vue en volumes laissait voir la porte de Datastream
  par l'ouverture du plafond au-dessus de l'escalier (juste en vrai, refusé par l'auteur : « le bug de l'escalier »).
  `pipeline/vue_kebab.py` ferme ce plafond pour les caméras de la salle (x < 9,3) ; depuis l'escalier (axe 11), la cage et la
  porte restent visibles.
