# Le test standard d'un LoRA de perso

Les mêmes 10 prompts pour chaque perso (CLAUDE.md, protocole, étape 7), les mêmes graines, les mêmes réglages : c'est ce qui permet de comparer deux versions d'un LoRA, ou deux persos entre eux.

## Les réglages

- Modèle de base : Animagine XL 4.0. LoRA du perso à 1,0.
- 1024 × 1024 (832 × 1216 pour le prompt 5, en pied), 25 pas, euler_ancestral, cfg 5.
- Graine : 1000 + le numéro du prompt (1001 pour le prompt 1, et ainsi de suite).
- Prompt négatif : `lowres, bad anatomy, bad hands, text, error, missing finger, extra digits, fewer digits, cropped, worst quality, low quality, low score, bad score, average score, signature, watermark, username, blurry`.
- Chaque prompt commence par `<déclencheur>, 1boy, solo, male focus` (ou `1girl` pour un perso féminin) et finit par `masterpiece, high score, great score, absurdres`. Le déclencheur est dans la fiche du perso (`fiche.json` > `lora`).

## Les 10 prompts

| N° | Ce qu'il vérifie | Tags |
|---|---|---|
| 1 | Le visage de face, au calme | `upper body, facing viewer, expressionless, simple background, grey background` |
| 2 | Le trois-quarts, un côté | `upper body, three-quarter view, facing right, expressionless, simple background, grey background` |
| 3 | Le trois-quarts, l'autre côté : les détails asymétriques ne doivent pas passer de l'autre côté | `upper body, three-quarter view, facing left, expressionless, simple background, grey background` |
| 4 | Le profil | `upper body, profile, from side, facing left, simple background, grey background` |
| 5 | En pied : la silhouette, la tenue, les chaussures | `full body, standing, simple background, grey background` |
| 6 | Dans son décor, comme dans l'épisode | `upper body, sitting, table, indoors, restaurant, morning, sunlight, food` |
| 7 | Une émotion forte et gaie | `upper body, facing viewer, smile, happy, open mouth, teeth, indoors, restaurant` |
| 8 | Une émotion forte et sombre | `upper body, facing viewer, angry, frown, clenched teeth, indoors, restaurant` |
| 9 | Sa signature, celle de `fiche.json` > `lora` > `test_signature` (pour Sky : le sourire), dont les tags s'ajoutent à la fin | `upper body, facing viewer` |
| 10 | Une situation qu'il n'a jamais vue à l'entraînement : il doit rester lui-même | `upper body, night, street, rain, holding umbrella, city lights` |

Quand la fiche d'un perso donne sa tenue ou un détail d'un seul côté (`fiche.json` > `lora` > `tenue`, `cote_visible` : Maëlle depuis sa v2), le test les écrit comme en production (`pipeline/test_lora.py`, `comme_en_production`) : le haut sur les 10, les bras à partir du 5, le bas au 5, le détail d'un seul côté sauf quand le perso regarde à droite. Un LoRA testé avec ces tags ne se compare pas à un test fait sans.

## Ce qu'on regarde

- Le perso est reconnaissable sur les 10 images, sans hésiter.
- Ses détails asymétriques restent du bon côté (pour Sky : l'œil aveugle à gauche, la bague à la main droite).
- Ses traits fixes sont là sans qu'on les écrive (pour Sky : les lunettes dorées avec leur barre, la barbe de 3 jours, la chemise à lys).
- Le style ne se dégrade pas : pas de traits flous, pas de couleurs délavées, pas d'arrière-plan gris recopié partout.
- Le résultat se note dans `journal.md`, avec le nom du fichier du LoRA testé.
