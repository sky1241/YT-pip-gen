# Patrick — les prompts ChatGPT

Pour faire ses planches de référence dans ChatGPT. Ce qu'il faut au total, image par image, est dans `image/INVENTAIRE.md` (section Patrick) : c'est la liste à cocher, la même pour chaque perso. Les 36 émotions sont décrites dans `image/emotions.md`. Les prompts sont en anglais.

L'ordre, le même que pour Maëlle (le protocole de `CLAUDE.md`) :

| Prompt | Image | Où la ranger |
|---|---|---|
| — | L'image maître : faite le 2026-10-18 | `references/master_v1.png` |
| P0 | Sa description maître, écrite par ChatGPT | `description-chatgpt.md` |
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

## Prompt P0 — Sa description maître

Dans la conversation où l'image maître a été faite (sinon, une neuve avec l'image maître jointe).

```
Write the MASTER CHARACTER DESCRIPTION of Patrick, the man in the attached image, in English, to paste at the top of every future prompt so that he always looks exactly the same. Describe only what is visible, precisely and concretely: approximate age, height and build; face shape and features; hair (where it is, where it is not, its colour and length); his glasses (shape, frame, colour); his eyes and eyebrows; his skin; every item of his outfit with its colour, cut and fabric (shirt, the breast pocket and the pens in it, the open cardigan, trousers, belt, shoes); his hands; his usual posture and expression at rest. Name every detail that is on one side only as HIS LEFT or HIS RIGHT (for example the breast pocket, a watch, a part in the hair), and say it must never be mirrored. End with a short list of what he never wears. Do not invent any story or personality, and do not mention any text or logo.
```
