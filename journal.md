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
  pas de version GGUF publiée (faux, corrigé le 2026-10-21 : des GGUF de la communauté existent, V3 10,9 Go
  woctordho/AniSora-v3-GGUF, 2025-09 ; V3.2 10,1 Go youcef079/Index-Anisora-V3.2-GGUF, 2026-03). Son modèle de base, Wan 2.2 14B, tourne compressé (GGUF Q4) sur des cartes NVIDIA de 8 Go : environ
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
- **Le côté de l'escalier jusqu'au plafond (2026-10-18)** : à l'axe 14, le côté de l'escalier s'arrêtait au-dessus des
  dernières marches, à 2,75 m ; le vide jusqu'au plafond laissait voir des marches et des barreaux, et le côté sortait du coin
  comme un bloc. `pipeline/vue_kebab.py` monte maintenant ce côté jusqu'au plafond là où la rampe touche le plafond, et ferme le
  bout sous le palier du haut : l'angle de la banquette est un coin simple.
- **Les fonds du kebab, le 2026-10-18** : 14 de plus en une journée (axes 4, 5, 9, 12, 13, 14, 15, 18, 19, l'axe 19 rideau fermé,
  et les quatre axes de Navier-Stokes sous la pluie, 22 à 25), 27 sur 45. Presque tous du premier coup ou en une retouche,
  avec deux ou trois fonds validés joints. Ce qui a coincé : la vue en volumes (le côté de l'escalier qui s'arrêtait sous le
  plafond, la cage visible depuis la salle, les troncs d'arbres pris pour des poteaux, un montant du rideau de verre pile devant
  la place de Sky) ; corrigée à chaque fois dans `pipeline/vue_kebab.py`, qui a maintenant un mode « rideau fermé ». Les
  aiguilles de l'horloge se posent en code (`pipeline/aiguilles.py`). Un fond peut s'enregistrer depuis l'image collée dans la
  conversation : elle est à la taille d'origine, identique au téléchargement.
- **Le LoRA de Maëlle, v1 (2026-10-18)** : sa série en pied et en gestes finie (M1 à M4, 4 planches, plusieurs retouches pour la
  bague : ChatGPT la met au mauvais doigt ou au mauvais pouce ; vue de dos, le pouce est caché, ne pas la demander). Jeu :
  69 images (`pipeline/preparer_lora.py maelle v1`), légendes avec `1girl, solo, female focus` (fiche > `genre` = f) et son angle
  de trois-quarts « facing left » (fiche > lora > `angle_trois_quarts`, `angle_signatures`) : son côté gauche, à l'inverse de
  Sky. Entraînement sur Kaggle (`pipeline/kaggle/lora_maelle_v1`), 3 répétitions × 8 époques (≈ 1 650 pas), sans retournement.
- **Kaggle, la file d'attente (2026-10-18)** : le LoRA de Maëlle est resté 1 h 30 en « QUEUED » sur T4 sans démarrer. Relancé
  sur une P100 (version 2 du notebook), avec l'optimiseur AdamW ordinaire au lieu d'AdamW8bit (bitsandbytes n'est pas sûr sur
  la P100) : démarré en moins de 2 minutes. La P100 n'a pas les cœurs tensoriels de la T4 : l'entraînement peut être plus long.
- **LoRA de Maëlle v1 entraîné (2026-10-18)** : 61 min sur une P100 (plus vite que prévu), 69 images × 3 répétitions × 8 époques
  = 1 656 pas, perte moyenne finale 0,057. Les 4 fichiers (époques 2, 4, 6, 8) vérifiés et copiés dans `<modeles_root>/loras/`.
- **Le test du LoRA de Maëlle v1 (2026-10-18)** (`maelle_v1.safetensors`, planche
  `<sorties_root>/comfyui/test-standard_maelle_v1_planche.png`) : reconnaissable sur les 10, la cicatrice au sourcil gauche,
  le côté rasé à sa gauche de face et de trois-quarts gauche, le style tient (pluie, resto). Quatre défauts. **1. Le côté
  rasé passe à sa droite dès qu'elle se tourne vers la droite de l'image** : le profil (test 4) la tourne à droite avec un
  côté rasé, donc du mauvais côté ; « facing right » (test 2) la tourne à gauche ; même avec « facing right » au profil, pareil
  (essai à part). La cause : 4 images sur 69 montrent son côté droit (les cheveux longs), une cinquantaine son côté gauche
  (toute la palette, les signatures, les gestes) ; le déclencheur a appris « le côté rasé se voit toujours ». **2. La tenue
  en pied perdue** (test 5 : pantalon caramel, col roulé sans manches, une chaîne). **3. Les manches courtes et un bracelet
  noir aux deux poignets** (tests 5 à 8) : sur toutes ses références, les manches sont remontées et font un bourrelet à
  l'avant-bras, lu (hypothèse) comme une manche courte plus un bracelet. **4. La bague au pouce droit pas apprise** (quelques
  pixels sur les images d'entraînement). Essai : écrire la tenue dans le prompt (`black turtleneck, long sleeves, sleeves
  pushed up, black pants, high-waist pants, black ankle boots`) règle le 2 et le 3 en partie (le pantalon noir, les manches
  longues ; un bracelet reste au resto) ; ne règle pas le 1. Images : `<sorties_root>/comfyui/essai_maelle_v1_*`.
- **Le LoRA de Maëlle v2 (2026-10-18)**, pour le défaut 1 sans nouvelle image : ses 4 vues du côté droit dans un sous-dossier
  répété 10 fois (contre 3 pour les 65 autres : 17 % des pas au lieu de 6 %), et deux sortes de tags en plus dans les
  légendes (`pipeline/preparer_lora.py` > `tags_en_plus`, réglés dans `fiche.json` > `lora`) : `undercut` sur les images où
  le côté rasé se voit, jamais sur celles du côté droit ; la tenue là où elle se voit. Le déclencheur garde le visage et les
  cheveux. En production, ces tags s'écrivent dans le prompt ; le test standard aussi les écrit désormais
  (`comme_en_production`). Mêmes réglages d'entraînement que la v1 (`pipeline/kaggle/lora_maelle_v2`), 8 × 235 = 1 880 pas.
  Si le côté rasé passe encore à droite : faire faire par l'auteur une planche de son côté droit (trois-quarts droit, quelques
  expressions et gestes), le seul vrai remède à un jeu déséquilibré. La bague se posera en production.
- **Le test du LoRA de Maëlle v2 (2026-10-18)** (`maelle_v2.safetensors`, planche
  `<sorties_root>/comfyui/test-standard_maelle_v2_planche.png`, comparée à la v1 dans
  `~/Téléchargements/maelle_lora_v1_contre_v2.png`). Entraînée en 73 min sur une P100, 1 880 pas, perte moyenne finale 0,061.
  **La tenue juste sur les 10** : col roulé, manches longues remontées, pantalon noir taille haute, bottines ; plus de bracelet.
  **Le côté rasé** : juste aux tests 1, 2, 3, 4, 5, 7, 8, 9. Le 2 (« facing right », sans `undercut`) montre enfin son côté
  droit, cheveux longs ; le 4 (profil) la tourne vers la gauche, côté rasé devant, juste. Faux aux tests 6 et 10, qui
  n'écrivent pas l'angle : elle se tourne vers la droite avec le côté rasé devant. Repris avec l'angle écrit
  (`essai_maelle_v2_*`) : le 6 « facing viewer » juste, le 10 « facing right » sans `undercut` juste, mais le 10
  « facing viewer » encore faux. Les ratées sont un miroir complet d'elle (le côté rasé et la cicatrice tous deux à sa droite),
  pas un mélange : une image retournée horizontalement redevient juste (utile pour un calque seul, pas quand le sens du regard
  compte). Bilan : 10 justes sur 13. Utilisable en production si l'angle est toujours écrit et qu'on génère 2 ou 3 variantes ;
  le remède de fond reste plus d'images de son côté droit (prompt M5, pour une v3). La bague : toujours pas apprise, comme prévu.
- **Le LoRA de Maëlle v3 (2026-10-20)** : le prompt M5 (six bustes de trois-quarts côté droit, sans les mains, avec sa vue
  `references/trois-quarts-droit_v1.png` jointe pour l'angle) est sorti bon du premier coup : joindre une image de l'angle
  voulu, et dire où vont les mèches et la cicatrice en termes de bord de l'image, suffit à ChatGPT. Les six cases s'appellent
  `expressions/cote-droit_<émotion>_v1.png` ; `preparer_lora.py` leur donne l'angle « facing right » et pas de `undercut`.
  Jeu v3 : 75 images, dont 10 du côté droit répétées 6 fois (25 % des pas), contre 3 pour les 65 autres.
- **Le test du LoRA de Maëlle v3 (2026-10-20)** (`maelle_v3.safetensors`, 83 min sur une P100, 2 040 pas, perte 0,058), les
  mêmes 13 images et graines que la v2 (`~/Téléchargements/maelle_lora_v2_contre_v3.png`) : **11 justes sur 13** (v2 : 10).
  La seule différence : le 10 « facing viewer » sous la pluie, faux en v2, juste en v3. Les deux ratées sont les mêmes qu'en
  v2 : le 6 (resto) et le 10 (pluie), les deux prompts qui n'écrivent pas l'angle ; elle s'y tourne vers la droite avec le
  côté rasé devant. Avec l'angle écrit : 10 sur 10. Un écart d'une image sur 13 ne prouve pas que les six bustes du côté droit
  ont servi : la v3 est au moins aussi bonne que la v2 partout, on la garde. La tenue est juste sur les 13, le fond du
  test 9 n'est plus le décor d'orage de la v2. **Décision : on arrête de réentraîner pour le côté.** En production, l'angle
  est toujours écrit (`fiche.json` > `lora` > `_note_production`), 2 ou 3 variantes par plan, les miroirs écartés au choix.
- **Étape 1 du premier vrai test : les critères, fixés avant les images (2026-10-20).** Un perso seul, assis à sa place sur
  la banquette du fond de l'axe 6, qui mange une galette. Deux méthodes (`pipeline/essai_integration.py`) : A, dessiné
  directement dans le fond (inpainting avec son LoRA) ; B, dessiné sur fond gris d'après une silhouette posée à sa place,
  détouré (isnet-anime), collé, puis fondu par une passe légère. Les deux finissent par une passe sur le visage en gros plan.
  4 graines par perso et par méthode (2001 à 2004). Une image passe si elle a les six : 1. reconnaissable, comparé à ses
  références ; 2. ses détails du bon côté (Sky : l'œil aveugle à sa gauche, côté du fond sur cet axe, et ses lunettes ;
  Maëlle : le côté rasé caché, les mèches longues devant, la cicatrice au sourcil gauche) ; 3. assis à sa place, à sa taille
  (la tête à la hauteur calculée, derrière la table) ; 4. dans la lumière du kebab, sans air collé ; 5. le décor intact hors de
  sa place, les sauces devant lui ; 6. il mange, les mains acceptables. Une méthode est bonne si au moins 2 graines sur 4
  passent, pour chacun des deux.
- **La caméra recalée sur le fond peint (2026-10-20)** : le fond de l'axe 6 suit la vue en volumes à quelques centimètres
  près, pas au pixel (la caméra peinte est 8 cm plus bas que celle de la vue). `pipeline/recaler_camera.py` retrouve la caméra
  du fond à partir de 5 points repérés à la main (les 4 coins du dessus de la table, l'angle de la banquette) : écart moyen
  8 px, au pire 16 px. Fichier : `image/decors/kebab/table-du-fond/camera.json`, avec les objets qui restent devant (les
  sauces). Sur cet axe, la caméra est devant eux, sur leur droite : on voit leur côté droit (« facing right »), le bon angle
  pour Sky (celui de sa palette) et pour Maëlle (les cheveux longs, 2 sur 2 en v3). La tête calculée : 142 px pour Sky, 103 pour
  Maëlle, sur le fond de 1536 × 1024.
- **Le gel de sky-master pendant l'étape 1 (2026-10-20, 12 h 07)** : la RAM pleine. VS Code avec ses extensions (environ
  4 Go), Firefox et Codex ouverts, il restait 4,8 Go ; ComfyUI en demande environ 6 pendant une génération (le modèle,
  le VAE sur le processeur). Le plafond du service (MemoryMax 10 Go) ne protège pas : il ne compte pas les autres
  programmes. Ajouté : `pipeline/garde_memoire.py`, lancé avec ComfyUI, qui le tue si la RAM disponible passe sous 1,2 Go
  (il a servi une fois, à 12 h 15 : ComfyUI tué, la machine n'a pas gelé), et note la RAM toutes les 10 s dans
  `<sorties_root>/comfyui/garde.log`. L'erreur du pilote `init_user_pages: Failed to get user pages: -16` revient à chaque
  chargement du modèle, sans dégât (déjà vue le 18) : ce n'est pas elle. Le VAE par tuiles prend moins de RAM mais ComfyUI
  le passe trois fois : 13 min au lieu de 5 par variante. Gardé d'un bloc.
- **Étape 1, ce que les quatre premiers essais ont appris (2026-10-20)** :
  1. Dans un décor, le déclencheur ne suffit plus : la chemise de Sky sort sombre, ses lunettes disparaissent, ses manches
     remontent au-dessus du coude (elles s'arrêtent juste sous le coude, coudes couverts : tenue_canonique), sa barbe
     s'efface. Écrits dans le prompt (`fiche.json` > `lora` > `tags_production`, `negatif_production`) : réglé.
  2. Le collage final ne prend que le perso détouré (isnet-anime) : le reste du fond reste celui d'origine (au 1er essai,
     le modèle avait changé le miroir en fenêtre de nuit). Le détourage brut est percé là où le perso a du noir (les feuilles
     de la chemise) et coupé au bord flou de sa place : Sky paraissait « un fantôme » (l'auteur). Réglé : seuil, trous
     bouchés, bord net (`detourage_net`). Les objets qui restent devant lui (les sauces, le chant et le pied de la table)
     sont relevés au pixel dans `camera.json` > `devant`.
  3. L'auteur : il manquait ses jambes. Sa place descend maintenant jusqu'au sol, sous la table.
  4. **Le vrai problème des deux méthodes : le modèle décide seul de la pose et de la taille.** A (dessiné dans le fond) :
     Sky se penche plus que prévu, sa tête sort de sa place et y est tranchée ; il redessine la table (un 2e chant, une
     assiette), et ses jambes tombent derrière le vrai chant. B (sur gris d'après une silhouette, débruitage 0,85) : Sky
     juste (lunettes, œil bleu à sa droite, barbe, manches, jambes en noir), mais 2,5 fois trop grand, comme assis au bout
     de la table, et le détourage d'une scène entière prend aussi la plante et la table. Remède standard : un guide de pose
     (T2I-Adapter openpose SDXL, TencentARC, 316 Mo, Apache 2.0) : son squelette, calculé à sa place avec la caméra
     recalée, imposé au modèle. À télécharger avec l'accord de l'auteur.
- **Étape 1, la méthode qui marche (2026-10-20, 14 h 30) : B cadrée, guidée par le squelette.** Le guide de pose
  (T2I-Adapter OpenPose, force 0,9) fait suivre au modèle le corps du squelette (épaules, bras, mains, hanches, jambes),
  pas la tête : il dessine une tête d'anime plus grosse et plus haute que la tête réelle du squelette. Dans un carré trop
  grand pour lui, sur fond gris, il grossit tout le perso (2 fois trop grand). La parade : le cadre. Sky est dessiné sur fond
  gris dans un cadre portrait 832 × 1216 qui va de ses cheveux à ses pieds, à sa place (`cadre_perso`) ; il remplit le cadre,
  comme les images de son LoRA, donc sa taille suit le cadre. Sur gris, le détourage est net (sur la scène entière, isnet
  prenait aussi la banquette, la table et la plante). Collé sur le fond derrière les objets « devant » (la vraie table cache
  le bas de son buste), fondu (débruitage 0,35), visage repassé : `sky_B_2001` passe les six critères (les lunettes, l'œil
  bleu à sa droite, la barbe, les manches sous le coude, les jambes en noir sous la table, il croque sa galette, le décor
  intact). Le prompt sur gris dit « full body, sitting » sans table, et interdit les meubles (au 6e essai, une table blanche
  dessinée sur le gris passait au collage). La méthode A guidée (dessiné dans le fond) : Maëlle propre (`maelle_A_2001`),
  Sky avec des restes de décor redessiné (une lampe dans le miroir, un 2e chant de table), faute d'un détourage net dans la
  scène.
- **Méthode B, le collage nettoyé (2026-10-20)** : sur le gris, le modèle assied le perso sur un bloc gris (malgré
  « chair, stool, bench » en négatif) et dessine son ombre ; le détourage les garde. Sous ses hanches, il ne reste que ce qui
  longe les jambes du squelette (`forme_jambes`, 14 cm de rayon) ; sous ses genoux, le gris sans couleur (le fond, l'ombre)
  s'en va (`coller_cadre`). Pas plus haut : les plis ombrés de la chemise blanche de Sky sont de ce gris-là. `--recomposer`
  refait le collage depuis l'image sur gris, sans régénérer.
- **Méthode B, le liseré (2026-10-20)** : le bord du détourage sur gris gardait un liseré du gris de fond, clair sur le miroir
  sombre (autour des cheveux, de la nourriture). Le masque est resserré de 3 pixels (`coller_cadre`) : réglé.
- **Étape 1, le bilan de la méthode B cadrée (2026-10-20, 15 h 25)** : 4 graines par perso (2001 à 2004), planche
  `~/Téléchargements/etape1_bilan_methode-B.png`, images dans `<sorties_root>/essais/etape1/`. Critères 1 à 5
  (reconnaissable, détails du bon côté, à sa place et à sa taille, dans la lumière, décor intact) : **8 sur 8**. Le critère 6
  (il mange) : Sky 1 sur 4 (une fleur, un verre, un objet doré flou), Maëlle 2 sur 4 (une fois la nourriture ne se voit pas,
  une fois ses mains ne sont pas à sa bouche). Passent les six : Sky 1 sur 4, Maëlle 2 sur 4. Selon la règle fixée avant
  (2 sur 4 pour chacun), la méthode passe pour Maëlle, pas encore pour Sky, et ce qui rate est l'objet dans ses mains, pas le
  perso : « wrap » est trop vague. Essai suivant : « burrito, biting » et, en négatif, « flower, cup, glass, drinking »
  (graines 2003 et 2004 de Sky ; les versions « wrap » gardées dans `v7_wrap/`). Temps : 8 min 20 par image sur la carte.
  La bague de Maëlle apparaît parfois à la main gauche : le LoRA ne la connaît pas (prévu).
- **« burrito » au lieu de « wrap » (2026-10-20, 15 h 45)**, graines 2003 et 2004 de Sky : la 2004 croque une vraie galette,
  la garniture se voit ; la 2003 tient le papier contre sa bouche, comme une serviette. Le geste de manger tient donc à peu
  près une image sur deux : en production, 2 ou 3 variantes par plan (CLAUDE.md), ou la galette posée en calque d'accessoire
  (`image/accessoires/`) si le geste doit être sûr.
- **Étape 2, à deux, axe 6 (2026-10-20, 18 h)** : `pipeline/composer_scene.py` assemble des variantes déjà générées, chacune
  seule avec son LoRA : du plus loin au plus près de la caméra (Maëlle, puis Sky devant), les objets « devant » par-dessus.
  Aucune nouvelle génération : on choisit la meilleure variante de chacun, puis on assemble (3 duos,
  `~/Téléchargements/etape2_duos_axe6.png`). L'échelle entre eux suit la caméra (la tête de Maëlle à 0,75 fois celle de Sky :
  plus petite, et plus loin). Défaut trouvé et corrigé : le bas de la chemise de Sky troué sur le côté (la règle « tout le gris
  sous les genoux » prenait ses plis blancs ombrés) ; la règle est maintenant : sous les hanches, le gris pas plus clair que
  le fond, en grande tache ou touchant le dehors. Reste : sur la graine 2004 de Sky, un bout de banc en bois sous sa hanche
  (le modèle l'assied sur un banc sur le gris ; la couleur bois passe le filtre).
- **Les essais rangés par axe (2026-10-20)** : `<sorties_root>/essais/integration/<axe>/` (ceux de l'axe 6, avant dans
  `essais/etape1/`), les plans assemblés dans `essais/plans/<axe>/`. `essai_integration.py` prend `--axe` ; l'angle des tags
  se calcule (`tags_angle`, d'après la caméra recalée et la place du perso), comme l'oreille cachée du squelette.
- **Axe 14 (coin de la banquette)** : sa caméra recalée (`coin-de-la-banquette/camera.json`, écart 4 à 14 px), ses objets
  « devant » relevés (les sauces, la boîte, le dessus de la table et ses chants). Sky et Maëlle y sont vus à 35° et 43° de face,
  de leur côté droit. La série n'a pas tourné : le garde-fou a tué ComfyUI au chargement du modèle (RAM disponible 1,2 Go ;
  Firefox rouvert, 1,9 Go). Le chargement du modèle est le pic (environ 6,5 Go) ; il faut environ 8,5 Go disponibles avant de
  lancer.
- **Les quatre recherches du 2026-10-21** (l'auteur : « avant de tâter dans le vide, tu as été regarder sur internet ? » ; non,
  la méthode de l'étape 1 avait été construite sans chercher ce qui existe). Quatre agents en parallèle, sources datées :
  1. **Ce qu'on garde** : un perso et un seul LoRA par génération (deux LoRA dans la même passe mélangent les persos, partout
     où c'est testé ; les modèles d'édition, Qwen-Image-Edit, Kontext, redessinent les persos) ; la pose et la taille depuis la
     caméra du décor (Mickmumpitz fait pareil avec une maquette 3D) ; l'assemblage en calques ; l'animation sans modèle vidéo
     (trois bouches, le standard de l'animation japonaise ; Rhubarb Lip Sync a un mode phonétique pour toute langue), les
     modèles vidéo seulement pour quelques gros plans (« talking » en négatif chez Wan pour qui écoute).
  2. **Ce qu'on change** : dessiner le perso directement dans le fond avec un vrai modèle d'inpainting (le patch de Fooocus,
     comme le fait Krita AI Diffusion pour SDXL), au lieu de le dessiner sur gris pour le découper : le modèle voit la vraie
     banquette (plus de tabouret) et la vraie lumière. La méthode A de l'étape 1 en était la version naïve (l'inpainting avec le
     modèle ordinaire). Pour les détourages qui restent : ToonOut (BiRefNet affiné sur l'anime, MIT).
  3. **Maëlle** : sa v3 applique déjà tout ce qui se conseille pour un perso asymétrique ; le texte ne sait pas dire gauche ou
     droite (l'encodeur de texte de SDXL est mauvais là-dessus). Reste : l'angle écrit, 2 ou 3 variantes, l'inpainting des
     ratés ; essayer le tag `sidecut` (le tag Danbooru exact pour « rasé d'un seul côté »).
  4. **À éviter** : LayerDiffuse (échoue sur Animagine 4.0), IC-Light (SD1.5, ombres fausses sur l'anime), tout ce qui repose
     sur FLUX.1-dev (Kontext, Fill, Insert Anything : licence qui exclut l'usage commercial, d'après la lecture de l'agent),
     Qwen-Image-2.1 (licence de recherche), les modèles vidéo payants (environ 80 $ la minute finie).
  5. **Kaggle, à trancher par l'auteur** : ses conditions d'utilisation (2025-06-22) réservent le service à un usage
     « personnel, non commercial » ; produire pour une chaîne monétisée s'accorde mal avec ça, y compris les LoRA déjà
     entraînés là-bas. Lu par l'agent, pas vérifié ici ; une location ponctuelle d'une carte (quelques euros) serait l'autre voie.
- **La machine, mesuré le 2026-10-21 par l'agent** : la chute de RAM au chargement venait du checkpoint de 6,9 Go lu sur le disque
  externe (un disque mécanique : 123 Mo/s en lecture suivie, 19 Mo/s en mmap) ; un fichier recopié sur la carte devient de la RAM
  ordinaire jusqu'à sa fermeture. Le VAE sur le processeur prenait 33 s par décodage d'une image 1024², 16 s par encodage ; en
  tuiles de 512 sur la carte, en fp16, 11 s et 6 s. Le VAE d'Animagine 4.0 est déjà le « fp16-fix » : `--fp16-vae` est sûr.
  Fait : le modèle découpé (`pipeline/unet_fp8.py` : l'UNet en fp8, 2,6 Go ; les encodeurs de texte et le VAE à part) sur le
  disque interne (`/home/sky/kebab-modeles/`, config.yaml > `modeles_rapides`), `--cpu-vae` remplacé par `--fp16-vae` et des
  nœuds en tuiles. Résultat : même image à la même graine (vérifié sur deux prompts du test standard de Sky), 1 min 57 par image
  au lieu de 2 min 30, la RAM ne descend plus sous 4,3 Go au chargement. Les poids restent en fp8 sur la carte
  (`weight_dtype` fp8_e4m3fn : 2,5 Go au lieu de 4,9), sinon deux UNet ne tiennent pas ensemble ; `liberer()` vide la carte
  avant de changer de modèle. Restent à essayer : fusionner le LoRA d'un perso dans son UNet (le mode « bypass » coûte jusqu'à
  19 % du temps), TunableOp sans hipBLASLt (3 à 5 %), TAESDXL pour trier les variantes.
- **Méthode C, le patch d'inpainting de Fooocus** : appliqué au chargement par le nœud, il touche 960 poids de l'UNet, et avec
  `--highvram` ComfyUI garde une copie de chaque poids d'origine sur la carte : il est fusionné une fois pour toutes dans une
  copie d'Animagine (`pipeline/fusionner_inpaint.py`, puis en fp8) ; le nœud « Apply Fooocus Inpaint » ne branche plus que sa
  tête (un patch vide, `inpaint/patch-vide.pth`). Nœuds : comfyui-inpaint-nodes (Acly, GPL-3.0, v1.4.4).
- **Erreur de ma part (2026-10-21, 08 h 15)** : le test de ToonOut (sur le processeur, plusieurs Go de RAM) lancé pendant le
  chargement du modèle dans ComfyUI ; le garde-fou a coupé ComfyUI. Règle : rien de lourd sur le processeur pendant une
  génération.
- **Le plan de tests du 2026-10-21 (l'auteur au sport ; critères fixés avant les images)**. Une seule chose à la fois sur la
  machine (rien de lourd sur le processeur pendant une génération). Chaque cas sur 4 graines (2001 à 2004), les mêmes pour
  toutes les méthodes, pour comparer image à image.
  1. **Méthode C, chacun seul**, Sky et Maëlle, axe 6 (table-du-fond) et axe 14 (coin-de-la-banquette) : 16 images. Les six
     critères de l'étape 1 (reconnaissable ; détails du bon côté ; à sa place et à sa taille ; dans la lumière du décor, sans
     air collé ; le décor intact hors de sa zone et les objets devant lui ; il mange, les mains acceptables). Un cas passe à
     2 graines sur 4. Comparé à la méthode B (axe 6, mêmes graines, déjà faites) : le nombre d'images qui passent, le temps.
  2. **À deux, méthode C** : Maëlle d'abord, Sky posé sur son image (`--sur`), axes 6 et 14, 2 paires de graines par axe.
     Critères en plus : chacun passe les six ; Sky devant Maëlle là où ils se chevauchent ; la table et les sauces devant eux ;
     l'écart de taille entre eux fidèle à la caméra (Maëlle plus loin et plus petite).
  3. **Maëlle, `sidecut` contre `undercut`** : les prompts 6 et 10 du test standard (ceux où elle sortait en miroir : l'angle
     n'y est pas écrit), 3 graines chacun, les deux tags : 12 images. On compte le côté rasé juste.
  4. **ToonOut contre isnet-anime** (processeur, ComfyUI arrêté) : les 8 rendus sur gris de la méthode B ; on mesure ce qui
     reste du fond gris dans le détourage, les trous dans le perso, et on regarde les cheveux.
- **Les résultats des tests du 2026-10-21** (planches dans `~/Téléchargements/bilan*.png`, images dans
  `<sorties_root>/essais/integration/<axe>/` et `essais/plans/<axe>/`) :
  1. **Méthode C** (dessiné directement dans le décor, modèle d'inpainting de Fooocus, guidé par le squelette) : 4 min 30 par
     image. Assis sur la vraie banquette, dans la vraie lumière, plus de tabouret ; il mange vraiment sur 14 images sur 16. Mais
     le modèle repeint aussi le décor autour du perso, dans sa zone : un halo sur le miroir derrière la tête de Sky (sur ses
     8 images : des feuilles, des fleurs), une tasse ajoutée près des sauces. **Remède testé : ne garder, dans la zone, que le
     perso détouré** (`--detourer toonout`), le décor d'origine autour : halos et objets ajoutés partis sur toutes les images ;
     ToonOut un peu plus net qu'isnet autour des cheveux. Avec ce détourage, les six critères : **Sky 1 sur 4 (axe 6) et 2 sur 4
     (axe 14), Maëlle 3 sur 4 et 3 sur 4.** Ce qui rate : la fidélité au perso, plus fragile dessiné dans le décor que sur le
     gris de son entraînement (Sky : des cheveux longs et noirs, l'œil aveugle avec un iris, un œil vert, une bande sur le
     pantalon malgré le négatif ; Maëlle : une fois absente, une fois sans manches). Méthode B sur l'axe 6, mêmes graines (le
     2026-10-20) : Sky 2 sur 4, Maëlle 2 sur 4 ; le perso y est plus fidèle, mais la lumière plus plate et la nourriture moins sûre.
  2. **À deux, enchaînés** (Sky dessiné dans l'image où Maëlle est déjà, `--sur`) : **les 4 ratent**. Le modèle voit Maëlle
     juste à côté de la zone et se mélange : Sky avec les cheveux roux de Maëlle, les corps fondus, Sky pas dessiné du tout, un
     fantôme d'un autre homme. À ne pas refaire. **À deux, en calques** (chacun dessiné seul dans le décor vide, détouré,
     superposé du plus loin au plus près, `composer_scene.py`) : marche ; Sky devant Maëlle, la table et les sauces devant eux,
     l'écart de taille juste. Un duo réussit quand ses deux images seules réussissent (3 sur 8 aux mêmes graines ; en
     choisissant la meilleure variante de chacun, un duo propre par axe à coup sûr ici).
  3. **Maëlle, `sidecut` contre `undercut`**, l'angle non écrit, 6 paires aux mêmes graines : undercut 3 justes, 3 en miroir ;
     sidecut 4 justes, 0 en miroir, 2 où le côté rasé est caché par les cheveux ; sidecut n'a jamais empiré une image. Peu
     d'images : encourageant, pas prouvé. Adopté dans sa fiche (`lora` > `cote_visible` > `tag`).
  4. **ToonOut** : sa sortie est déjà une probabilité ; mon code la repassait dans une sigmoïde (une règle « si hors de 0 à 1 »
     déclenchée par l'arrondi du fp16) : le premier test ToonOut contre isnet est faux, refait à la fin. Les détourages de la
     méthode C, eux, ont été faits après la correction.
- **La régression vue par l'auteur (2026-10-21, 11 h)** : « le modèle a perdu la forme des lunettes » et la peau de Sky a
  foncé (« on dirait qu'il est devenu arabe »). Mesuré sur les visages (la médiane des tons chair) : son LoRA seul, sur gris,
  rouge 210 et luminosité 129 ; sa vue de trois-quarts de référence 187 et 122 ; la méthode B 193/122 (graine 2001) et 180/113
  (2004) ; la méthode C 173/120 et 157/99, une peau plus brune et plus terne. Les lunettes : le LoRA seul dessine ses
  aviateurs avec la barre du haut ; avec les tags « glasses, yellow-framed eyewear » ajoutés le 2026-10-20 (`tags_production`),
  des lunettes rectangulaires génériques, en B comme en C. **Erreur de ma part** : ces deux tags, ajoutés pour que les lunettes
  ne disparaissent pas, ont écrasé leur forme. Test (`--retirer`, sans toucher à la fiche avant le résultat), Sky, axe 6,
  graines 2001 à 2004, critères fixés avant : les lunettes passent si ce sont des aviateurs (verres en goutte, plus larges en
  haut, la barre au-dessus du nez) ; la peau passe si sa médiane a un rouge d'au moins 180 et une luminosité d'au moins 113
  (le plus foncé de la méthode B, que l'auteur n'a pas relevé). Trois variantes, pour séparer les causes : C sans les tags ;
  le même corps avec la passe du visage refaite par le modèle ordinaire ; D (le rendu sur gris refait sans les tags, fondu par
  le modèle d'inpainting, visage ordinaire).
- **Méthode D (hybride, 2026-10-21)** : le rendu sur gris de la méthode B (aux mêmes graines, déjà fait), collé, puis fondu
  par le modèle d'inpainting à 0,45 (au lieu du modèle ordinaire à 0,35) et le visage repassé par le modèle d'inpainting :
  3 min 40 par image en reprenant le rendu sur gris (5 min 30 en le refaisant). Les six critères, axe 6 : **Sky 3 sur 4,
  Maëlle 2 sur 4** (`~/Téléchargements/bilan6_methodeD_hybride_axe6.png`). La peau de Sky reste celle de son LoRA (rouge
  184, luminosité 119 à la graine 2001), la lumière du décor mieux prise qu'en B. Ce qui rate : la nourriture (un papier, un
  anneau de pain), une fois Maëlle qui tient sa galette sans la manger, des traces sur une main de Sky.
- **La régression, premier résultat (graine 2001)** : sans les tags « glasses, yellow-framed eyewear », Sky retrouve ses
  aviateurs fins avec la barre du haut, en C comme avec le visage refait par le modèle ordinaire. La peau, elle, reste trop
  foncée en C (rouge 171, puis 166 avec le visage ordinaire) : c'est la passe du corps dans le décor (le modèle d'inpainting à
  1,0, « warm lighting », la lumière sombre de la scène) qui la fonce ; la passe du visage à 0,45 garde la couleur qu'elle
  reçoit.
- **La régression, résultat complet (2026-10-21, 12 h 15)**, Sky, axe 6, graines 2001 à 2004 (`~/Téléchargements/bilan7_*`,
  `bilan8_*`) :
  - **Les lunettes** : avec « glasses, yellow-framed eyewear », 0 aviateur sur 8 (B et D) ; sans ces deux tags, ses aviateurs
    fins à barre reviennent sur 7 images sur 7 où le visage se voit (C : 3 sur 3, une image où ses mains cachent son visage ;
    D : 4 sur 4). Plus fines et plus discrètes qu'avec les tags, comme sur sa référence. **Corrigé dans sa fiche**
    (`lora` > `tags_production`, l'ancienne valeur notée).
  - **La peau** (critère fixé avant : rouge ≥ 180 et luminosité ≥ 113) : B 4 sur 4 ; C 1 sur 4 dans ses trois variantes (avec
    les tags, sans, et avec le visage refait par le modèle ordinaire) ; D 3 sur 4 ; D sans les tags 2 sur 4 (les deux autres à
    1 et 3 points de luminosité du seuil, rouge 184 et 185). **C'est la méthode C qui fonce la peau de Sky**, par sa passe du
    corps (le modèle d'inpainting à 1,0 dans la lumière sombre et orangée du décor) ; ni les tags ni la passe du visage n'y
    changent rien. Maëlle, elle, sort juste en C (3 sur 4 sur les deux axes).
  - D sans les tags, les six critères : 3 sur 4 hors peau (la graine 2003 tient un papier) ; avec le seuil de peau, 1 sur 4
    strictement, 3 sur 4 si l'on accepte les deux à 1 et 3 points.
- **ToonOut contre isnet, refait après la correction** : aucun des deux ne garde de fond (bord à 0) ; ToonOut laisse un peu
  moins de pixels à moitié transparents dans le perso (97,6 à 98,4 % pleins contre 96,7 à 98,0 %), garde un peu plus de mèches
  fines ; 18 s par image sur le processeur contre 2 s. Les deux suffisent ; ToonOut pour les plans finaux.
- **Ce que ces tests tranchent, et ce qu'ils ne tranchent pas** (4 graines par cas : un écart d'une image sur 4 ne prouve
  rien) : nets, les tags des lunettes (0 sur 8 contre 7 sur 7), la peau de Sky en C (3 sur 12 contre 9 sur 12 en B et D), les
  duos enchaînés (4 ratés sur 4), le halo de C autour du perso (parti sur toutes les images une fois le perso détouré). À
  confirmer sur plus d'images : `sidecut` (0 miroir sur 6 contre 3 sur 6), C contre D pour Maëlle (3 contre 2 sur 4).
- **La planche 3 refusée par l'auteur (2026-10-21, 13 h)** : « Sky a un contour blanc lumineux autour de lui, ce qu'il mange
  change à chaque image, sa chemise change entre les images ; Maëlle a l'air bien intégrée, Sky pas du tout ». Juste.
  **Erreur de ma part** : je jugeais chaque image seule, avec les six critères, sans comparer Sky d'une image à l'autre ni
  regarder ses bords. Désormais, un critère de plus pour chaque perso : **la cohérence**, jugée côte à côte avec sa référence
  sur toutes les images de l'essai (la même chemise et le même motif, les mêmes couleurs de peau et de cheveux, pas de liseré
  ni de halo autour de lui, le même aliment). Vérifié, sans nouvelle génération (`~/Téléchargements/bilan9_sky_coherence.png`,
  `bilan10_duos_sky-hybride.png`) : avec la méthode C, Sky change d'une image à l'autre (le motif de la chemise noir, puis
  bleu-vert, puis bleu ; les cheveux et la peau ; une fois un autre homme) et garde un liseré clair autour des cheveux et des
  épaules (le décor repeint autour de lui, que le détourage dilaté de 5 pixels reprend) ; avec la méthode D sans les tags des
  lunettes, collé dans le même duo, **la même chemise sur 4 images sur 4** (blanche, feuilles noires clairsemées, comme sa
  référence), les mêmes couleurs, pas de liseré. Reste : **l'aliment change à chaque image** (un sandwich dans du papier, une
  serviette, un burrito) : à faire en accessoire fixe, dessiné une fois et le même dans tous les plans ; sa barbe, plus légère
  que sur sa référence.
- **Sky « un ado de 14 ans » (l'auteur, 2026-10-21, 13 h 50)** : « tous les traits physiques du perso ont disparu, la barbe
  n'existe jamais, la couleur de peau dérive ». Suivi étape par étape sur la graine 2001 de la méthode D : son LoRA seul en
  gros plan (le test standard) dessine le bon Sky (barbe de 3 jours marquée, cernes, mâchoire carrée, l'âge) ; le rendu sur
  gris en pied (sa tête à 160 px) garde une barbe plus légère ; **le fondu par le modèle d'inpainting lisse le visage, puis ma
  passe du visage à 0,45 le rajeunit** (elle « nettoie » un visage flou en visage d'anime générique). Ce n'est pas la limite
  du modèle : c'est le pipeline. Test (critères avant les images, jugés côte à côte avec sa référence, sur les 4 graines) : la
  barbe de 3 jours visible (mâchoire, menton, lèvre du haut) ; un homme adulte (la trentaine), pas un ado ; les cernes ; ses
  aviateurs ; la peau (rouge ≥ 180, luminosité ≥ 113) ; le même Sky sur les 4. Variantes de la passe du visage, sur les mêmes
  corps : 0,6 sans tags ; 0,6 avec « mature male, stubble, bags under eyes » (« aged down, child » en négatif) ; 0,75 avec.
- **La passe du visage, le résultat** (2026-10-21, 14 h 40 ; `~/Téléchargements/bilan11_sky_visage.png`) : notée par l'auteur
  70/100 à 0,6 comme à 0,75 (contre 60 pour la passe à 0,45 ; son LoRA seul en gros plan : 90) : « c'est vraiment la barbe et
  les cernes qui donnent le caractère au personnage, il manque encore un peu de barbe ». À 0,75, la passe redessinait aussi
  ses mains (sur 3 images sur 4, il ne mangeait plus) : **la passe sur la tête seule** (`--visage-masque tete` : une ellipse des
  cheveux au menton, ses poignets protégés d'après le squelette) garde le geste sur les 4 et le vieillit autant. Suivant :
  « stubble » renforcé dans le prompt, à 1,4 puis 1,7.
- **« stubble » renforcé** (`(stubble:1.4)`, `(stubble:1.7)`, la passe de la tête seule à 0,75, mêmes graines ;
  `~/Téléchargements/bilan12_sky_barbe.png`) : aucune différence visible avec « stubble » simple, sur les 4 graines. À ce
  débruitage, la barbe vient de l'image de départ et du LoRA, pas du poids du mot. Essai suivant : une 2e passe sur le bas du
  visage seul (`--visage-masque barbe`, `--depuis-visage`), 0,8. Le détecteur de visages d'anime (lbpcascade) ne sert à rien
  ici : OpenCV 5 n'a plus le `CascadeClassifier` ; le bas du visage se place d'après les proportions mesurées sur ses images
  (une tête d'anime 1,5 fois plus haute que la tête réelle du squelette).
- **La 2e passe sur le bas du visage** (0,8, « (stubble:1.3), facial hair, beard stubble », « clean-shaven » en négatif ;
  `~/Téléchargements/bilan13_sky_passe_barbe.png`) : à peine plus de barbe sur la joue, sur les 4 graines. Quand il mange,
  ses mains et la galette couvrent sa bouche et son menton, et le masque les protège : il ne reste que la joue. Pas le bon
  levier. Le seul qui a marché jusqu'ici : la force de la passe (0,45 → 0,75 : 60 → 70/100). Essai suivant : la tête seule à
  0,85 et 0,95 (son gros plan à 90/100 est dessiné de zéro).
- **La tête seule à 0,85 et 0,95** (`~/Téléchargements/bilan14_sky_tete_forte.png`) : le visage se rapproche de son gros plan
  (plus mûr, plus de barbe), mais le geste casse : la tête se relève, la bouche quitte la galette, et sur 3 graines le modèle
  lui met une cigarette (un petit trait blanc au coin de la bouche, là où le masque protège ses mains). **À retenir : 0,75 pour
  un plan où il mange ou tient quelque chose à la bouche ; 0,85 à 0,95 à essayer sur un plan de dialogue**, rien devant la
  bouche. Les duos du meilleur réglage du jour (Maëlle en C détourée, Sky en D sans les tags des lunettes, la tête seule à 0,75 ;
  `bilan15_duos_meilleur_reglage.png`) : 3 sur 4 utilisables (la graine 2003 de Maëlle ratée), Sky le même sur les 4 (la
  chemise, les couleurs, pas de liseré). Restent : l'aliment, qui change à chaque image ; la barbe, plus légère que sur sa
  référence (70/100 pour l'auteur à 0,75).
- **La tête dédoublée, d'après la recherche (2026-10-21, 16 h 30)** : un défaut de ma passe, pas du LoRA. Avec Differential
  Diffusion, un pixel du bord flou du masque ne change qu'aux dernières étapes : à 0,85-0,95, le cœur dessine une tête qui a
  bougé, le bord garde l'ancienne mâchoire ; puis je recollais avec ce même bord flou (Acly : « utiliser le même masque pour le
  collage annule l'effet »). Et le prompt disait « portrait, close-up » sans le geste : la tête se relevait, et « stubble »
  appelle souvent « cigarette » (4,9 % des images « stubble » de Danbooru). Corrections testées (`passe_visage`, options
  `--visage-v2`, `--visage-masque tete2`, `--visage-contours`) : un masque plus grand, un collage net (`net`), ses mains et ce
  qu'elles tiennent recollées nettes par-dessus, « close-up » et le geste dans le prompt, « cigarette, smoking » en négatif ;
  le guide de contours (T2I-Adapter Lineart SDXL, 158 Mo, Apache 2.0 ; force 0,7 jusqu'à 60 % des étapes) qui fige la tête.
- **L'objet identique d'un plan à l'autre, d'après la recherche** : aucun modèle ouvert ne redessine un objet à l'identique
  depuis une référence ; ce qui tient : coller les vrais pixels de l'objet dans ses mains, puis ne repeindre que ses doigts
  autour. Test avec un rouleau factice dessiné en code (`rouleau`, option `--objet`) : posé de ses mains (repérées sur l'image)
  à sa bouche, ses doigts repeints dans une bande autour (0,55), le cœur du rouleau gardé. Critères : le même rouleau sur les
  4 graines, ses doigts devant, sa bouche dessus, aucune fleur, verre ni cigarette, le même Sky.
- **Les premiers résultats (graine 2001, 16 h 45)** : la passe v2 à 0,75 ne dédouble plus la tête et garde le geste (il mord
  sa galette). À 0,9 avec le guide de contours, la tête reste en place (pas de double, la bouche sur la galette, plus de barbe),
  mais ses cheveux sortent plus clairs et frisés (mon guide de contours, une différence de flous, relève chaque mèche). **Le
  rouleau collé dans le gros plan, raté** : posé d'après la peau sous sa bouche, il est parti de sa poitrine (la chemise est
  ouverte) et flottait devant son menton, et la nourriture dessinée par le modèle restait à côté, dans ses mains. **Refait
  autrement** : la galette factice posée dans le guide avant le rendu sur gris, de sa bouche vers ses mains d'après le
  squelette (`place_objet`), presque figée pendant le rendu (un quart de la force, Differential Diffusion) : le modèle dessine
  ses mains autour d'elle ; puis protégée pendant le fondu et la passe du visage (`2_objet.png`).
- **La passe v2 sur les 4 graines** (`~/Téléchargements/bilan16_sky_visage_v2.png`) : à 0,75, **plus de tête dédoublée sur
  les 4**, le geste gardé (il mord la galette), plus de cigarette ; la barbe au niveau de la passe précédente (70/100), pas
  au-delà. À 0,9 avec le guide de contours : la tête reste en place sur les 4, mais les cheveux sortent frisés et plus clairs
  sur les 4 (le guide relève chaque mèche) : pas utilisable tel quel.
- **La galette factice dans le guide du rendu sur gris** (`bilan17_galette_factice.png`) : un rouleau proche du factice (le
  papier, le trait rouge) sur 2 graines sur 4 ; sur les 2 autres, le modèle dessine sa propre nourriture à côté (un burrito,
  un taco), et la galette factice s'efface. Le prompt disait « holding burrito » : il veut son burrito. 2e essai lancé : plus
  de « burrito » dans les prompts quand la galette est posée (« holding food », « burrito, sandwich, taco, hamburger » en
  négatif).
- **Son gros plan en référence** (IP-Adapter Plus Face SDXL, 848 Mo, Apache 2.0 ; la référence : le visage de son test
  standard 2, noté 90/100, `essais/integration/reference_visage_sky.png`) : branché dans la passe du visage v2, poids 0,5 et
  0,8 (`--visage-reference`). Les critères : sa barbe et ses cernes plus proches de la référence, le même Sky, le geste gardé,
  la peau. 3 min 40 par image (contre 2 min 30 sans).
- **Son gros plan en référence (IP-Adapter Plus Face), le résultat** (`~/Téléchargements/bilan18_sky_visage_reference.png`) :
  **pire**. À 0,5 comme à 0,8, sur les 4 graines, le visage pâlit et rosit, les cheveux virent au rose, les cernes s'effacent ;
  la barbe n'augmente pas. L'adaptateur reprend surtout la lumière plate et grise du gros plan. Abandonné.
- **La galette factice, 2e essai** (sans « burrito » dans les prompts ; `bilan19_galette_factice_2.png`) : **le même objet sur
  3 graines sur 4** (un rouleau de papier blanc, tenu à deux mains à la bouche, qui part vers la droite ; contre 2 sur 4 au 1er
  essai) ; la 4e tient un petit pain rond. Mais ça ne marche pas encore : la partie galette est cachée par ses mains, on ne voit
  que le papier, et il a l'air de tenir une serviette plutôt que de manger ; le papier, presque figé, reste d'un blanc plat qui
  ne prend pas la lumière chaude de la salle (il a l'air collé). Suite possible : coller l'objet exact tout à la fin, puis une
  passe légère (0,3) sur l'objet et les mains pour la lumière ; un objet factice dont la nourriture se voit.
- **Bilan du réglage de Sky, le 2026-10-21 au soir** : réglés, la tête dédoublée (la passe v2), ses lunettes (sans les tags),
  sa peau et sa cohérence d'une image à l'autre (la méthode D) ; bloquée à 70/100, sa barbe (ni le poids du mot, ni une 2e
  passe, ni son gros plan en référence n'y font rien). Le levier qui reste, d'après la recherche : son LoRA. Ses traits n'ont
  jamais été écrits dans ses légendes, le mot déclencheur les absorbe, et le LoRA ne les a vus presque qu'en buste ; un LoRA v3
  avec `beard_stubble`, `bags_under_eyes`, `mature_male` dans les légendes les rendrait demandables dans le prompt (non prouvé
  pour un petit visage).
- **Le LoRA de Sky v3 (2026-10-21, 20 h), d'après trois recherches** (agents en parallèle, sources datées) :
  1. **Les légendes** : ses traits n'ont jamais été écrits dans ses légendes, le déclencheur les absorbait ; un tag absent des
     légendes n'a aucun lien appris avec son visage, d'où « stubble » à 1,7 sans effet, et les lunettes génériques avec
     « glasses ». v3 : « mature male » partout, « stubble, bags under eyes » là où son visage se voit (pas de dos) ; ses
     lunettes, sa chemise et son cordon restent sans tag (ils marchent ainsi). L'ordre d'Animagine XL 4.0 (sa fiche) : le genre
     puis le nom du perso en tête : « 1boy, skykebab, … ». Les tags mélangés à chaque passage (`shuffle_caption`,
     `keep_tokens 2` : les deux premiers restent en tête), 10 % retirés au hasard (`caption_tag_dropout_rate 0.1`). Avec le
     mélange, sd-scripts refuse le cache des encodeurs de texte : il saute (environ 1,6 Go de plus sur la carte).
  2. **Le jeu** : 97 images sur 126 sont des bustes ou des gros plans de bouche, 10 en pied. Real-ESRGAN anime garde sa barbe
     sur les bustes (vérifié à 100 %) mais l'amincit en traits durs sur les petites têtes (en pied, gestes) : le LoRA a appris
     « Sky petit = barbe légère ». v3 : les 22 images à petite tête reprises de leur fichier d'origine, agrandies en Lanczos ;
     répétées plus (en pied × 4, gestes × 3, bustes × 1 : 180 images par époque).
  3. **Le fond gris** : un masque alpha par image (ToonOut, dilaté de 12 px, le fond à 15 % ; à 0, des corps en trop
     apparaissent d'après OneTrainer) : l'entraînement regarde le perso. Ne corrige pas la lumière de studio, que portent ses
     propres pixels.
  4. **Réglages** inchangés (rang 32 / alpha 16, UNet seul, AdamW sur P100, 1e-4 cosinus, min_snr 5) : la v2 n'est pas sous-
     entraînée (90/100 en gros plan) et changer d'optimiseur ne comble pas un trou dans les données. 12 époques, chacune
     sauvegardée, des images d'essai toutes les 3 époques. Écartés pour la v3 : des copies dézoomées (elles apprendraient
     « petit = sans barbe »), de nouvelles images à demander à l'auteur, changer le déclencheur (`skykebab` se découpe en
     « sky » + « kebab »). Pour la v4 ou la v5, une chose à la fois selon la v3 : sans min_snr (il affaiblit les étapes qui
     dessinent les textures fines), les encodeurs de texte entraînés à 1e-5, LoKr facteur 8.
  Script : `pipeline/jeu_lora.py` (le jeu), `pipeline/kaggle/lora_sky_v3/` (l'entraînement).
- **Le protocole de test des versions de Sky (fixé avant les images de la v3)**. Le même déroulé pour la v2, la v3, la v4,
  la v5 ; l'UNet fp8, CFG 5, euler_a, 25 étapes, le LoRA à 1,0 ; les prompts de chaque version dans l'ordre de ses légendes.
  - (a) Le test standard (10 prompts, graines 1001 à 1010) : un contrôle. Rejet si l'œil aveugle passe du mauvais côté aux
    prompts 1 à 3, ou si le fond gris apparaît aux prompts 6 à 8 et 10.
  - (b) 8 rendus sur gris de la méthode D, qui mange (graines 2001 à 2008) : sa tenue, ses lunettes, le même Sky d'une image
    à l'autre. Rejet si la chemise ou les couleurs changent sur 2 images ou plus.
  - (c) La passe de la tête v2 à 0,75 (masque « tete2 », « mature male, stubble, bags under eyes ») sur 8 corps figés (les
    corps de la v2 dans le kebab, axe 6, graines 2001 à 2008, après le fondu), avec le LoRA de la version : isole ce que le
    LoRA apporte à la barbe. Rejet si les lunettes manquent sur 2 images ou plus, ou l'œil aveugle du mauvais côté.
  - Les mesures : un tagueur d'anime (WD SwinV2 v3) sur les gros plans de (c) : la présence de « stubble », « bags under
    eyes », « mature male », calibrée d'abord sur ses images de référence (un tag ne compte que s'il sort sur au moins 80 %
    d'entre elles) ; la peau (médiane des tons chair).
  - Le jugement : des planches à l'aveugle (v2 et la version à gauche ou à droite au hasard, la clé cachée) jugées par un agent
    indépendant, ligne par ligne (barbe, âge, cernes, lunettes, le même Sky), puis par l'auteur. Une version remplace la v2 si
    elle gagne au moins 12 lignes sur 16 en (b) + (c), ou 6 sur 8 en (c) avec la barbe détectée sur 6 images sur 8. Moins,
    c'est une égalité : on garde la v2.
- **Le tagueur d'anime, calibré sur Sky (2026-10-21, 20 h 10)** (`pipeline/tagueur.py` : WD SwinV2 v3, SmilingWolf, Apache 2.0,
  467 Mo, environ 1 s par image sur le processeur) : sur ses 15 images de référence, « facial hair » 0,98, **« beard » 0,93**,
  « mature male » 0,87, « stubble » 0,21 seulement, « bags under eyes » 0 (ses cernes sont dessinées en ombre : le tagueur ne
  les voit pas) ; sur ses gros plans de production trop jeunes (60/100) « beard » 0,61, sur la passe à 0,75 (70/100) 0,75 ;
  sur Maëlle 0 partout. **La probabilité de « beard » suit la note de l'auteur** : c'est la mesure de la barbe. Les tags du
  tagueur sur ses références : « facial hair, beard, mature male, muscular male, dark-skinned male, brown hair, short hair,
  white shirt, collared shirt, floral print, necklace ». Pour le modèle, sa barbe de 3 jours est une « beard » courte ;
  « stubble » seul tire vers un duvet plus léger. D'où « facial hair, beard, stubble » dans ses légendes v3 (le jeu refait).
  Les cernes ne se mesurent pas : à l'œil seulement.
- **La relecture indépendante avant le lancement de la v3 (un agent, 2026-10-21, 20 h 30)** : lancer, une fois le jeu envoyé
  sur Kaggle. Vérifié contre le code de sd-scripts v0.12.0 : la configuration (`alpha_mask` par sous-dossier ; le « masked
  loss » s'active seul avec des images à transparence), le refus du cache des encodeurs avec le mélange des tags, le format
  des images d'essai ; les 126 légendes lues (le genre et le déclencheur en tête partout, les 4 tags du visage sur 124, la plus
  longue à 74 jetons CLIP sur 75) ; 37 masques regardés (mains, lunettes, galette, téléphone, ordinateur dedans). Corrigé
  avant l'envoi : les images Lanczos étaient plus molles que les bustes (un léger renforcement des contours) ; les répétitions
  ramenées à en pied × 3, gestes × 2 (à × 4, chaque image en pied revenait 48 fois) : 158 images par époque, 1 896 pas ;
  l'optimiseur choisi selon la carte (Kaggle donne une T4 même quand on demande une P100 : AdamW8bit, comme la v2) ; une image
  d'essai de plus (petit dans un restaurant, là où la v2 lâchait) et une au départ. Reconnu : la v3 change plusieurs choses à
  la fois ; elle dira si l'ensemble aide, pas lequel. Lancée sur Kaggle à 20 h 42.
- **Le protocole, complété avant les images de la v3** (d'après la relecture) :
  - La passe de la tête (c) se fait, pour toutes les versions, avec « mature male, facial hair, beard, stubble, bags under
    eyes » : la base v2 est la variante « v2barbe ». En plus, (d) : le pipeline entier de la version (méthode D, son rendu sur
    gris, le fondu dans le kebab, la passe de la tête), 8 graines : le vrai cas, Sky petit dans le kebab.
  - La mesure de la barbe : la probabilité moyenne de « beard » (le tagueur) sur les 8 gros plans, et le nombre au-dessus de
    0,85 (ses références : 0,96 au 20e centile ; la passe v2 à 0,75 : 0,73 à 0,76). Limite connue : son gros plan noté 90/100
    par l'auteur ne fait que 0,76 en « beard » (le tagueur y voit plutôt « stubble », 0,80) : le tagueur mesure la ressemblance
    avec la barbe courte de ses références ChatGPT, pas la note de l'auteur. Il s'ajoute au jugement, il ne le remplace pas.
  - Le jugement à l'aveugle : par ligne (une graine), sa référence puis les deux gros plans (v2 et la version, à gauche ou à
    droite au hasard) ; l'agent choisit le plus proche de la référence (barbe, âge, cernes, lunettes) ou l'égalité, et note
    les défauts. 16 lignes : (c) × 8 et (d) × 8. La version remplace la v2 si elle gagne au moins 12 lignes sur 16 (une
    chance sur 25 d'y arriver par hasard), si sa barbe moyenne dépasse celle de la v2 d'au moins 0,05, et sans critère de
    rejet. En cas de désaccord entre l'agent et l'auteur, l'auteur tranche.
  - Le choix de l'époque : d'abord les images d'essai de Kaggle (au départ, puis aux époques 3, 6, 9, 12) : on écarte une
    époque à l'œil aveugle du mauvais côté, au fond gris dans les prompts de restaurant, à l'anatomie cassée. Puis (c) avec
    l'époque 12 et l'époque 9 ; la meilleure (barbe moyenne, jugement) passe au test standard (a) et à (d).
  - Les gros plans ne doivent pas régresser : au test standard (a), prompts 1 à 4, la version ne doit pas perdre 3 des 4
    lignes contre la v2 au jugement à l'aveugle. La peau : médiane des tons chair, rouge au moins 180 et luminosité au moins
    113, comptée sur (c) et (d).
