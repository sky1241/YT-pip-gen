# Patrick — les prompts ChatGPT

Pour faire ses planches de référence dans ChatGPT. Ce qu'il faut au total, image par image, est dans `image/INVENTAIRE.md` (section Patrick) : c'est la liste à cocher, la même pour chaque perso. Les 36 émotions sont décrites dans `image/emotions.md`. Les prompts sont en anglais.

L'ordre, le même que pour Maëlle (le protocole de `CLAUDE.md`) :

| Prompt | Image | Où la ranger |
|---|---|---|
| — | L'image maître : faite le 2026-10-18 (la v2, en polo de rugby) | `references/master_v2.png` |
| — | Sa description : écrite par l'auteur | `description-auteur.md` |
| P1 | La rotation, 6 vues | `planches/rotation_v1.png` |
| P2 | En pied | `references/pied_v1.png` |
| P3 à P6 | En pied et en gestes : 4 planches | `planches/pied-1_v1.png`, `pied-2_v1.png`, `poses_v1.png`, `gestes_v1.png` |
| P7 à P12 | La palette des émotions : 6 planches | `planches/emotions-1_v1.png` à `emotions-6_v1.png` |
| P13 | Ses 5 signatures | `planches/signatures_v1.png` |
| P14 | Les bouches | `planches/bouches_v1.png` |

Les leçons de Sky et de Maëlle, appliquées à chaque prompt :
- chaque prompt est complet (toute sa description y est) : il marche dans une conversation neuve, avec l'image maître jointe ;
- un défaut se corrige tout de suite, en retouche, case par case, en nommant les mains et les côtés par leur place dans l'image ;
- vue de dos, ne pas demander un détail caché (le pouce, une bague) ;
- aucun texte dans les planches : ni sur la tasse, ni sur un écran.
- sa tasse est une tasse de thé en porcelaine, jamais un mug (l'auteur, le 2026-10-18 : le mug « COBOL FOREVER » de l'image maître vient de ChatGPT) ;
- pas de bague, et un seul détail d'un côté : la poche de chemise et ses deux stylos.

## La description de Patrick, pour chaque prompt

Tirée de la description de l'auteur (`description-auteur.md`) et de l'image maître v2, par Claude, le 2026-10-18. Elle est déjà dans chaque prompt ci-dessous.

```
Patrick is a man in his sixties, about 1.75 m tall, heavy and generously built: a prominent round belly, broad shoulders slightly hunched, a thick neck, still solid arms. His head is largely bald on top, with a crown of thin, sparse white and grey hair around the sides and the back. A wide face with full, slightly sagging cheeks, deep wrinkles around the eyes, the forehead and the mouth, and a pronounced double chin. Rectangular glasses with a thin dark frame. Brown eyes, tired but attentive, heavy eyelids, slightly drooping eyebrows. His smile is discreet: it starts with a slight crinkle of the eyes before reaching his lips. He wears a navy blue rugby polo shirt with a white collar and a short button placket, a white band and a red band running across the chest, and a small red rooster embroidered on HIS LEFT side of the chest (on the right of the image when he faces us), never mirrored; loose dark grey pleated trousers with a black belt and a silver buckle; black leather shoes. No ring, no watch, no jewelry. He never holds a mug: when he drinks, it is always tea from a delicate white porcelain teacup on its saucer.
```

## Prompt P1 — La rotation, 6 vues

Joins l'image maître (`~/Téléchargements/patrick_pour_P_1_image-maitre.png`). Découpe : `--noms face,trois-quarts-gauche,trois-quarts-droit,profil-gauche,profil-droit,dos --dossier references`.

```
Make a turnaround sheet of Patrick, the man in the attached image: a regular grid of 3 columns and 2 rows, landscape format (1536×1024), six equal cells separated by thin white gaps. The same head-and-shoulders framing in every cell, neutral calm expression, same soft light, plain light-grey background. Only the camera angle changes. Patrick is a man in his sixties, about 1.75 m tall, heavy and generously built: a prominent round belly, broad shoulders slightly hunched, a thick neck, still solid arms. His head is largely bald on top, with a crown of thin, sparse white and grey hair around the sides and the back. A wide face with full, slightly sagging cheeks, deep wrinkles around the eyes, the forehead and the mouth, and a pronounced double chin. Rectangular glasses with a thin dark frame. Brown eyes, tired but attentive, heavy eyelids, slightly drooping eyebrows. His smile is discreet: it starts with a slight crinkle of the eyes before reaching his lips. He wears a navy blue rugby polo shirt with a white collar and a short button placket, a white band and a red band running across the chest, and a small red rooster embroidered on HIS LEFT side of the chest (on the right of the image when he faces us), never mirrored; loose dark grey pleated trousers with a black belt and a silver buckle; black leather shoes. No ring, no watch, no jewelry. He never holds a mug: when he drinks, it is always tea from a delicate white porcelain teacup on its saucer. Cells read left to right, then top to bottom:

1. Front view.
2. Three-quarter view showing HIS LEFT side: the red rooster on his chest is nearer to us.
3. Three-quarter view showing HIS RIGHT side: the red rooster is on the far side of his chest.
4. Profile showing HIS LEFT side.
5. Profile showing HIS RIGHT side.
6. Back view: no face visible.

No text, no letters, no logos other than the small rooster, and no labels anywhere.
```
