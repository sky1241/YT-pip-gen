# Le style de la série

**Décidé par l'auteur le 2026-10-16** : le style de la série est celui des images de référence de Sky (série 2) et de Maëlle, faites dans ChatGPT. Un anime des années 90, entre *Street Fighter II* (le film), *Evangelion* et Ghibli. L'image maître de Sky a été faite avec celle de Maëlle en référence de style : les deux vont ensemble.

## Les images de référence

- `image/persos/sky/references/master_v3.png` : Sky au kebab, lumière du matin.
- `image/persos/maelle/references/master_v1.png` : Maëlle au café, la même lumière.
- `image/persos/sky/references/pied_v1.png` : le perso seul, en pied, sur fond gris.
- `image/persos/sky/planches/emotions-1_v1.png` : les expressions, dans le même trait.

Seules les images validées de `image/persos/` et `image/decors/` font foi, jamais `image/explorations/`.

## Ce qui fait ce style (relevé sur les deux images maîtres)

- **Le trait** : des contours sombres, nets et fins, d'épaisseur régulière. Pas de lignes floues ni de contours colorés.
- **Les ombres** : de l'aplat avec une ou deux teintes d'ombre, adoucies par un léger dégradé ; pas de rendu brillant ni de reflets partout.
- **La lumière** : chaude et dorée, une source franche (le soleil par la fenêtre), des ombres longues.
- **Les couleurs** : une palette chaude et un peu passée : bruns, ocres, roux, noirs profonds, blancs cassés. Rien de saturé ni de fluo.
- **Les corps** : des proportions réalistes, des visages adultes et marqués (cernes, barbe, taches de rousseur), à la manière des animes de combat des années 90 ; pas de grands yeux ni de visage d'enfant.
- **Les décors** : peints et détaillés, à la manière de Ghibli : bois, briques, plantes, objets du quotidien.
- **La bouffe** (l'auteur, le 2026-10-23) : le rendu des plats des films Ghibli, « qui donne envie de manger » : des reflets humides sur les sauces et la viande, des couleurs chaudes et franches, un peu de vapeur, toujours en aplats nets. C'est une exception, pour la nourriture seule, à « pas de reflets » et à « rien de saturé ».

## Ce qu'on évite

- Le rendu anime moderne générique (celui d'Animagine sans aide, vu au test du LoRA de Sky v2) : peau lisse et brillante, couleurs vives, trait propre mais sans caractère.
- Le style « gacha » : effets de lumière partout, fonds flous, yeux immenses.

## Comment le tenir en production

- **Une référence de style à chaque image** : l'image maître de l'axe, donnée au modèle local avec IP-Adapter (à installer et tester sur la carte de 8 Go). C'est ce qui corrige le style qui varie d'une image à l'autre.
- **Les décors dans ce style** : un fond par axe de caméra, fait une fois ; les persos s'y intègrent.
- **Les LoRA des persos** s'entraînent sur des images dans ce style. Le passage local (étape 6 du protocole) refait leurs images de référence dans le rendu final.
- **Un LoRA de style** si ça ne suffit pas : soit un LoRA « années 90 » déjà prêt (pistes notées dans `journal.md`, 2026-10-15), soit le nôtre, entraîné sur les images de référence et les décors validés.

## Les mots-clés de prompt (à tester, rien n'est encore validé)

Pour Animagine XL 4.0, en tags Danbooru : `1990s (style), retro artstyle, anime screencap, cel shading, warm lighting, sunlight`. Le résultat de chaque essai se note dans `journal.md`, et seuls les mots-clés qui marchent restent ici.
