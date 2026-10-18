# Maëlle — les prompts ChatGPT

Pour faire ses planches de référence dans ChatGPT. Ce qu'il faut au total est dans `image/INVENTAIRE.md`, et les 36 émotions sont décrites dans `image/emotions.md`.

Les prompts sont en anglais, parce que les termes de planche (« turnaround », « expression sheet ») y sont plus précis. Tu peux parler en français à ChatGPT entre deux images.

## L'image maître : les prompts d'origine

L'image maître (`references/master_v1.png`) est sortie de ChatGPT en deux temps, avec ces deux prompts de l'auteur, copiés tels qu'il les a donnés.

**A — Le portrait réaliste**

```
yo tu me fait une image realiste de cette fewmme stp Assise côté fenêtre. Cheveux châtain foncé coupés court, asymétrique — plus long à gauche, rasé au-dessus de l'oreille droite. Taches de rousseur sur les pommettes, le nez, jusque sous les yeux. Mâchoire carrée. Pas de maquillage sauf un trait d'eye-liner noir, précis comme tracé au scalpel. Fine cicatrice sur l'arcade sourcilière droite — boxe, ou quelque chose qui cogne.

Pull col roulé noir. Épaules de nageuse. Bras toniques, avant-bras posés sur la table, on voit les tendons quand elle tourne sa tasse. Bague en argent au pouce gauche. Ongles courts, pas vernis.
```

**B — Le passage en manga**

```
comment tu la représenterais dans un style manga des année 90 style street fightter evangélio studio gibly ?
```

Deux choses à savoir en les relisant :
- **Gauche et droite y sont vus depuis l'image.** « Rasé au-dessus de l'oreille droite », c'est sa gauche à elle ; « l'arcade sourcilière droite », son sourcil gauche ; « le pouce gauche », son pouce droit. Ça concorde avec l'image maître et avec toutes les planches : seule la façon de compter change. Les prompts de ce fichier, eux, comptent depuis elle, pour qu'un modèle ne la retourne pas.
- **Les cheveux** : le prompt A dit châtain foncé, mais l'image maître validée est cuivrée. C'est l'image qui fait foi.

## Avant de commencer

Vérifie ces trois côtés, relevés sur son image maître. « Gauche » et « droit », c'est sa gauche à elle, pas celle de l'image :
- **l'undercut** : le côté rasé est sur sa gauche, les longues mèches tombent sur sa droite ;
- **la cicatrice** : une petite cicatrice verticale traverse son sourcil gauche ;
- **la bague** : un large anneau d'argent à son pouce droit.

S'ils sont bons, tous les prompts ci-dessous les reprennent. Sinon, dis-le-moi avant de lancer quoi que ce soit.

## Le mode d'emploi

1. Ouvre une nouvelle conversation ChatGPT, rien que pour Maëlle.
2. Joins `references/master_v1.png` et colle le prompt 0. Il dit qui elle est et fixe les règles de toutes les planches.
3. Ensuite, une image par prompt, dans l'ordre. Joins de nouveau l'image maître à chaque fois : sur une longue conversation, ChatGPT dérive.
4. À chaque image, vérifie les trois côtés, la grille régulière, l'absence de texte, le même cadrage dans chaque case. Si une case rate, demande de refaire seulement cette case.
5. Télécharge l'image en taille réelle et range-la sous le nom indiqué. Dis-le-moi : je découpe la planche et je nomme les fichiers.

La planche 1 est faite (2026-10-14). ChatGPT l'a dessinée de trois-quarts, sous l'angle de l'image maître, au lieu de face : on garde cet angle pour toute sa palette, les prompts le demandent maintenant. La rotation est faite aussi, avec les bons côtés partout. L'image en pied aussi. Les six planches d'émotions aussi. Tout est fait (2026-10-14), soulagement compris. Quelle image vient de quel prompt, et quelle version sert pour chaque émotion : `provenance.json`. ChatGPT ramène toute émotion positive vers son regard d'image maître, paupières mi-closes et sourire en coin : les prompts 7 et 8 le lui interdisent maintenant, sauf là où une case le demande. Les émotions ratées ne se refont pas une à une : elles s'ajoutent à la liste des reprises, en fin de fichier, et on les fait toutes en une seule planche à la fin.

Au départ : commence par le prompt 1, la première planche d'émotions. C'est le test prévu dans `PLAN.md` : on valide la planche et la découpe avant de faire le reste. En tout, 10 images.

| Prompt | Image | Où la ranger |
|---|---|---|
| 1 | Émotions, planche 1 (le test) : faite | `planches/trois-quarts_emotions-1_v1.png` |
| 2 | Rotation, 6 vues : faite | `planches/rotation_v1.png` |
| 3 | En pied : faite | `references/pied_v1.png` |
| 4 à 8 | Émotions, planches 2 à 6 : faites | `planches/trois-quarts_emotions-2_v1.png` à `trois-quarts_emotions-6_v1.png` |
| 9 | Signatures : faite | `planches/signatures_v1.png` |
| 10 | Bouches : faite | `planches/bouches_v1.png` |
| 11 | Les reprises : faite | `planches/trois-quarts_reprises_v2.png` |
| 12 | Soulagement, seul : faite | `expressions/trois-quarts_soulagement_v3.png` |
| M1 | En pied, de face et de trois-quarts : faite (une retouche) | `planches/pied-1_v1.png` |
| M2 | En pied, de profil et de dos : faite | `planches/pied-2_v1.png` |
| M3 | Trois poses : faite | `planches/poses_v1.png` |
| M4 | Six gestes (à valider par l'auteur avant) | `planches/gestes_v1.png` |

Les chemins partent de `image/persos/maelle/`.

## Prompt 0 — Le contexte

À coller avec l'image maître jointe.

```
This is Maëlle, a character from my 1990s-style anime series. I'm attaching her master image. I will ask you for several reference sheets of her, one at a time. In every image, keep her exactly as in the master image:

- Same art style as the master: 1990s anime, clean ink lines, cel shading.
- A woman around thirty, athletic build, broad shoulders, warm tanned skin.
- Copper-red hair with an undercut: the shaved side is on HER LEFT; the long messy strands fall over her right side.
- A small vertical scar through HER LEFT eyebrow.
- Green eyes, a fine winged eyeliner.
- Light freckles on the nose and upper cheeks, simplified: a small sprinkle, always in the same places.
- A black turtleneck sweater, sleeves pushed up to the forearms.
- A wide silver ring on HER RIGHT THUMB, whenever her right hand is visible.

Rules for every sheet: plain light-grey background, soft even light with no strong shadows, no text, no labels, no numbers. Cells are separated only by thin white gaps. From one cell to the next, only the thing I ask for changes.

Don't generate anything yet: just confirm you understand.
```

## Prompt 1 — Émotions, planche 1 : les universelles

```
Make an expression sheet of Maëlle: a regular grid of 3 columns and 2 rows, landscape format (1536×1024), six equal cells. In each cell, the same head-and-shoulders bust, in the same three-quarter angle as her master image (we see her left side), same framing, same pose, same light. Only her facial expression changes. Cells read left to right, then top to bottom:

1. Neutral: relaxed face, straight gaze, mouth closed.
2. Joy: a genuine smile, cheeks raised, eyes slightly squinting.
3. Sadness: inner ends of the eyebrows raised, heavy eyelids, corners of the mouth turned down.
4. Anger: eyebrows drawn down and together, a hard stare, lips pressed.
5. Fear: eyebrows raised and pulled together, eyes wide open, mouth stretched back.
6. Surprise: eyebrows high and rounded, eyes wide, mouth open.

No text or labels anywhere.
```

## Prompt 2 — La rotation, 6 vues

```
Make a turnaround sheet of Maëlle: a regular grid of 3 columns and 2 rows, landscape format (1536×1024), six equal cells. The same head-and-shoulders framing in every cell, neutral expression, same light. Only the camera angle changes. Cells read left to right, then top to bottom:

1. Front view.
2. Three-quarter view showing HER LEFT side (the shaved side).
3. Three-quarter view showing HER RIGHT side (the long hair side).
4. Profile showing HER LEFT side.
5. Profile showing HER RIGHT side.
6. Back view.

In every cell, the shaved side and the eyebrow scar stay on her left. No text or labels anywhere.
```

## Prompt 3 — En pied

Le bas de sa tenue n'est écrit nulle part. Je propose un pantalon noir ajusté et des bottines noires : change la ligne si tu veux autre chose, puis note-le dans sa fiche.

```
Make a full-body image of Maëlle, standing, facing the viewer, neutral expression, arms relaxed, portrait format (1024×1536). On top, her usual outfit: black turtleneck, sleeves pushed up, silver ring on her right thumb. Below: black slim trousers and black ankle boots. Plain light-grey background, soft even light, no text.
```

## Prompts 4 à 8 — Émotions, planches 2 à 6

Chaque prompt est complet : colle-le tel quel.


### Prompt 4 — Planche 2 : les universelles, suite, et leurs pics

```
Make an expression sheet of Maëlle: a regular grid of 3 columns and 2 rows, landscape format (1536×1024), six equal cells. In each cell, the same head-and-shoulders bust, in the same three-quarter angle as her master image (we see her left side), same framing, same pose, same light. Only her facial expression changes; her hands may enter the frame only when the expression needs them. Cells read left to right, then top to bottom:

1. Disgust: wrinkled nose, upper lip raised.
2. Contempt: only one corner of the mouth raised, on HER LEFT side, looking down on someone.
3. Laughter: mouth wide open, eyes closed or squinting, head tilted back.
4. Crying: tears, distressed eyebrows, trembling mouth.
5. Rage: eyebrows very low, clenched teeth or a shouting mouth, an anime anger vein on the temple.
6. Terror: bulging eyes, tiny pupils, open mouth, pale face.

No text or labels anywhere.
```

### Prompt 5 — Planche 3 : l'esprit

```
Make an expression sheet of Maëlle: a regular grid of 3 columns and 2 rows, landscape format (1536×1024), six equal cells. In each cell, the same head-and-shoulders bust, in the same three-quarter angle as her master image (we see her left side), same framing, same pose, same light. Only her facial expression changes; her hands may enter the frame only when the expression needs them. Cells read left to right, then top to bottom:

1. Shock: jaw dropped, round frozen eyes.
2. Interest: head slightly tilted, eyebrows slightly raised, an attentive gaze.
3. Concentration: slightly furrowed brows, a fixed gaze, pursed lips.
4. Confusion: her left eyebrow higher than the right, head tilted, a crooked mouth.
5. Doubt: her left eyebrow raised, pursed lips, a sideways glance.
6. Suspicion: narrowed eyes, a sideways look, chin tucked in.

No text or labels anywhere.
```

### Prompt 6 — Planche 4 : les émotions sociales

```
Make an expression sheet of Maëlle: a regular grid of 3 columns and 2 rows, landscape format (1536×1024), six equal cells. In each cell, the same head-and-shoulders bust, in the same three-quarter angle as her master image (we see her left side), same framing, same pose, same light. Only her facial expression changes; her hands may enter the frame only when the expression needs them. Cells read left to right, then top to bottom:

1. Embarrassment: a forced smile, eyes escaping downward, red cheeks.
2. Shame: head down, eyes on the floor, shoulders hunched.
3. Pride: head high, chin up, a slight smile, upright posture.
4. Jealousy: a side-eye, clenched jaw, low eyebrows.
5. Tenderness: a soft gaze, relaxed eyelids, a light smile.
6. Longing: a lingering gaze, half-closed eyelids, lips slightly parted. Subtle, never explicit.

No text or labels anywhere.
```

### Prompt 7 — Planche 5 : les nuances

```
Make an expression sheet of Maëlle: a regular grid of 3 columns and 2 rows, landscape format (1536×1024), six equal cells. In each cell, the same head-and-shoulders bust, in the same three-quarter angle as her master image (we see her left side), same framing, same pose, same light. Only her facial expression changes; her hands may enter the frame only when the expression needs them. Each expression must be clearly different from the others: avoid her usual half-lidded smirk unless a cell asks for it. Cells read left to right, then top to bottom:

1. Contentment: eyes gently closed, a small peaceful smile, a relaxed face.
2. Relief: a big exhale with puffed cheeks, eyes closed, eyebrows lifted, shoulders dropping.
3. Elation: a beaming open-mouthed smile, sparkling eyes, eyebrows high: overflowing joy.
4. Triumph: a big open-mouthed grin, chin up, a clenched fist raised in the frame.
5. Awe: eyes wide, mouth open, eyebrows raised, no fear.
6. Disappointment: a pout, eyes lowered, inner brows slightly raised.

No text or labels anywhere.
```

### Prompt 8 — Planche 6 : l'humeur et le corps

```
Make an expression sheet of Maëlle: a regular grid of 3 columns and 2 rows, landscape format (1536×1024), six equal cells. In each cell, the same head-and-shoulders bust, in the same three-quarter angle as her master image (we see her left side), same framing, same pose, same light. Only her facial expression changes; her hands may enter the frame only when the expression needs them. Each expression must be clearly different from the others: avoid her usual half-lidded smirk unless a cell asks for it. Cells read left to right, then top to bottom:

1. Worry: eyebrows raised and pulled together, biting her lip or a tense mouth.
2. Annoyance: furrowed brows, rolling her eyes, sighing.
3. Mischief: a smirk on HER LEFT side, her left eyebrow raised, a knowing look.
4. Boredom: heavy eyelids, head resting on her hand, an empty gaze.
5. Tiredness: dark circles, half-closed eyes, maybe a yawn.
6. Pain: eyes squeezed shut, clenched teeth, a grimace.

No text or labels anywhere.
```

## Prompt 9 — Ses quatre signatures

Cadrées à mi-corps, pour que les bras croisés tiennent dans la case.

```
Make a sheet of Maëlle's four signature expressions: a regular grid of 2 columns and 2 rows, landscape format (1536×1024), four equal cells. The same waist-up framing in every cell, in the same three-quarter angle as her master image, same light. Cells read left to right, then top to bottom:

1. The killing look: a cold sideways glance, eyelids slightly lowered, a hint of a smile that is anything but friendly.
2. Arms crossed: leaning back, arms crossed, silent; she withdraws.
3. Security-chief mode: cold and surgical, a neutral face, a steady direct gaze, jaw set. Not the wife: the security chief.
4. Blushing despite herself: red cheeks, looking away, annoyed at herself, trying to keep a straight face.

No text or labels anywhere.
```

## Prompt 10 — Les bouches

```
Make a mouth sheet of Maëlle: a regular grid of 3 columns and 2 rows, landscape format (1536×1024), six equal cells. A close-up of her face, neutral expression, the same framing within each row. Only the mouth changes.

Top row, front view: 1. mouth closed, 2. mouth half open, 3. mouth open, as when speaking.
Bottom row, three-quarter view showing her left side, as in the master image: 4. closed, 5. half open, 6. open.

No text or labels anywhere.
```

## Les reprises

Les émotions sorties trop proches d'une autre. On les refait toutes en une seule planche, après la dernière planche de Maëlle, et elles se rangent en `_v2` à côté des premières. La liste est complète : c'est le prompt 11, ci-dessous. Il se découpe avec `--noms joie,stupeur,concentration,soulagement,emerveillement,malice`, et les fichiers sortent en `_v2`.

| Émotion | Le problème | Ce qu'il faut |
|---|---|---|
| Joie (planche 1) | Un sourire en coin, presque le même que le mépris | Open, genuine joy: a broad smile showing her teeth, cheeks raised, eyes crinkling at the corners. Both corners of the mouth rise. |
| Stupeur (planche 3) | La même image que la surprise | Frozen shock, stronger than surprise: jaw dropped low, mouth hanging open in a tall oval, tiny pupils, the whole face frozen. |
| Concentration (planche 3) | On dirait une colère légère, elle fixe le spectateur | Calm focus: eyes looking down at a document just out of frame, brows slightly knit, lips pressed. Not angry. |
| Soulagement (planche 5) | Ni souffle ni joues gonflées : c'est un contentement | Relief: a big exhale through pursed lips, cheeks puffed, eyes closed, eyebrows lifted, head dropping slightly. |
| Émerveillement (planche 5) | La même image que la surprise et la stupeur | Wonder: looking slightly upward, eyes shining, lips parted in a faint smile, eyebrows raised. No shock, no fear. |
| Malice (planche 6) | Le même sourire en coin que le mépris | Mischief: a playful, teasing grin showing a little of her teeth on her left side, her left eyebrow arched high, eyes sparkling. Warm and cheeky, not cold. |

Le contentement de la planche 5 est sorti en sourire en coin, mais la case du soulagement est exactement le contentement voulu (yeux fermés, petit sourire paisible) : elle est copiée en `expressions/trois-quarts_contentement_v2.png`, et le contentement n'est plus à refaire.

## Prompt 11 — Les reprises

```
Make a sheet of Maëlle's expressions: a regular grid of 3 columns and 2 rows, landscape format (1536×1024), six equal cells. In each cell, the same head-and-shoulders bust, in the same three-quarter angle as her master image (we see her left side), same framing, same light. Her master image shows a half-lidded smirk: do not reuse it in any cell, and make every expression unmistakable. Cells read left to right, then top to bottom:

1. Joy: a broad, genuine smile showing her upper teeth, cheeks pushed up, eyes crinkled with laugh lines, eyebrows relaxed. Both corners of the mouth rise.
2. Shock: far stronger than surprise. Jaw dropped all the way down, mouth hanging open in a tall oval, pupils shrunk to tiny dots, eyebrows shot up, the whole face frozen and pale.
3. Concentration: calm focus. Eyes looking down at a document just below the frame, brows slightly knit, lips pressed together. She is not looking at the viewer and she is not angry.
4. Relief: a big exhale through pursed lips, cheeks puffed out with air, eyes closed, eyebrows lifted, head tipping back slightly.
5. Wonder: looking up at something above the frame, eyes wide and shining, lips parted in a faint smile, eyebrows raised. No shock, no fear.
6. Mischief: a playful, teasing grin showing a little of her teeth on HER LEFT side, her left eyebrow arched high, eyes sparkling. Warm and cheeky, not cold.

No text or labels anywhere.
```

## Prompt 12 — Le soulagement, seul

Dans les reprises, il est sorti lèvres poussées et yeux fermés, sans joues gonflées : on lit un baiser. Celui-ci soupire bouche ouverte.

```
Make a single image of Maëlle with the same framing as her expression sheets: one head-and-shoulders bust, in the same three-quarter angle as her master image (we see her left side), plain light-grey background, soft even light, square format (1024×1024). Expression: relief. Eyes closed, head tilted back, mouth open in a big sigh, as if saying "phew", shoulders dropping, a small anime sweat drop on her temple. Not a kiss, not a smirk. No text.
```

## La série en pied et en gestes, pour son LoRA

La leçon du premier LoRA de Sky (2026-10-15) : avec une seule image en pied, le LoRA n'apprend que le buste et invente le reste. Ces quatre planches le comblent avant son premier LoRA, sur le même fond gris clair que ses autres planches. Pas de décor : en production, elle est intégrée dans nos fonds. Chaque prompt M est complet (toute sa description y est) : il marche dans n'importe quelle conversation, même neuve. Pour chacun, joindre deux images : son image maître (`~/Téléchargements/maelle_pour_M_1_image-maitre.png`) et son image en pied (`~/Téléchargements/maelle_pour_M_2_en-pied.png`), préparées par Claude.

### Prompt M1 — En pied, de face et de trois-quarts

Joins les deux images (l'image maître, puis l'image en pied). Découpe : `--noms pied-face,pied-trois-quarts-gauche,pied-trois-quarts-droit --dossier references`.

```
Make a full-body sheet of Maëlle: a regular grid of 3 columns and 1 row, landscape format (1536×1024), three equal tall cells separated by thin white gaps. In each cell, Maëlle stands full body from head to feet, neutral watchful expression, arms relaxed, same scale, same light, plain light-grey background. Her usual outfit, exactly as in the attached full-body image: the black fitted turtleneck sweater in a matte, slightly textured fabric, its sleeves pushed up to the forearms; black slim high-waisted trousers, fitted but practical; sturdy black ankle boots with a square heel. One wide silver ring on HER RIGHT THUMB only; her left hand has no ring; no other jewelry. Short unpainted nails. Her copper-red hair: HER LEFT side shaved, the longer, messy strands falling over HER RIGHT side of the face. A small vertical scar through HER LEFT eyebrow. Fine black winged eyeliner, a light dusting of freckles on the nose and upper cheeks, green eyes. Broad swimmer's shoulders, toned forearms, an athletic hourglass build, 1.65 m. Cells, left to right:

1. Front view.
2. Three-quarter view showing HER LEFT side, as in her master image: the shaved side of her head and the scar on her left eyebrow are nearer to us.
3. Three-quarter view showing HER RIGHT side: the long strands of hair fall on this side, nearer to us; her shaved left side is farther away.

No text or labels anywhere.
```

Premier essai de M1, le 2026-10-18 (`<sorties_root>/persos/maelle/pied-1_essai-1.png`) : la tenue, les bottines, la bague au pouce droit, l'undercut à sa gauche, justes. Mais la case 3 montre le même angle que la case 2 (son côté gauche, l'undercut devant), au lieu de son côté droit. Retouche de la case 3, dans la case « Décrivez les modifications » :

```
Edit ONLY the third cell, on the right. Keep the first two cells exactly as they are. In the third cell, redraw Maëlle in the same outfit, at the same scale and in the same light, but turned the other way: her face and body turn toward the RIGHT edge of the image, in a three-quarter view. The long, messy copper strands that fall over HER RIGHT side are now on the side of her face nearer to us (the left part of her head in the image); the shaved side of her head is turned away from us, on the far side, almost hidden. The silver ring stays on her right thumb.
```

Résultat de la retouche, le 2026-10-18 : la case 3 montre son côté droit, validée. La bague y est passée au pouce gauche : gardée, comme la règle fixée pour Sky (une bague ratée ne fait pas refaire une planche), et notée dans `fiche.json` pour le passage local. Pour M2 et M3, la phrase sur la bague dit aussi que la main gauche n'en a pas.

L'auteur veut quand même la case juste, pour que le LoRA apprenne la bague au bon pouce. Retouche de la bague, case 3, dans la case « Décrivez les modifications » :

```
Edit ONLY the hands in the third cell, on the right. Keep everything else exactly as it is, in all three cells. In the third cell, remove the silver ring from the thumb of the hand on the RIGHT of the image (her left hand, farther from us), and put the same wide silver ring on the thumb of the hand on the LEFT of the image (her right hand, nearer to us). Only one ring in the cell.
```

Résultat, le 2026-10-18 : la bague au pouce droit, validée (`planches/pied-1_v2.png`). Seule sa case 3 sert : `references/pied-trois-quarts-droit_v2.png` ; la v1 de cette case est marquée non retenue, le jeu du LoRA ne la prend pas.

### Prompt M2 — En pied, de profil et de dos

Joins les deux mêmes images. Découpe : `--noms pied-profil-gauche,pied-profil-droit,pied-dos --dossier references`.

```
Make a full-body sheet of Maëlle: a regular grid of 3 columns and 1 row, landscape format (1536×1024), three equal tall cells separated by thin white gaps. In each cell, Maëlle stands full body from head to feet, neutral watchful expression, arms relaxed, same scale, same light, plain light-grey background. Her usual outfit, exactly as in the attached full-body image: the black fitted turtleneck sweater in a matte, slightly textured fabric, its sleeves pushed up to the forearms; black slim high-waisted trousers, fitted but practical; sturdy black ankle boots with a square heel. One wide silver ring on HER RIGHT THUMB only; her left hand has no ring; no other jewelry. Short unpainted nails. Her copper-red hair: HER LEFT side shaved, the longer, messy strands falling over HER RIGHT side of the face. A small vertical scar through HER LEFT eyebrow. Fine black winged eyeliner, a light dusting of freckles on the nose and upper cheeks, green eyes. Broad swimmer's shoulders, toned forearms, an athletic hourglass build, 1.65 m. Cells, left to right:

1. Profile showing HER LEFT side: we see the shaved side of her head and her left eyebrow with its scar.
2. Profile showing HER RIGHT side: the long strands of hair fall over this side of her face.
3. Back view: no face visible; the shaved side is on HER LEFT, which is on the left of the image.

No text or labels anywhere.
```

Résultat de M2, le 2026-10-18 : bonne pour l'auteur ; contrôlé par Claude : l'undercut à sa gauche dans le profil gauche et de dos (à gauche de l'image), les longues mèches sur le profil droit. De dos, la bague manque. Retouche, dans la case « Décrivez les modifications » :

```
Edit ONLY the hands in the third cell, the back view on the right. Keep everything else exactly as it is, in all three cells. In the back view, her right hand is the hand on the RIGHT of the image: add one wide silver ring on its thumb, visible from behind. The hand on the left of the image stays without any ring.
```

La retouche a mis la bague au petit doigt. Erreur de Claude : de dos, les bras le long du corps, le pouce est caché devant la main ; ne pas voir la bague est juste. L'auteur garde donc le premier essai, sans bague de dos (`planches/pied-2_v1.png`).

### Prompt M3 — Trois poses

Joins les deux mêmes images. Découpe : `--noms assis-face,assis-cote,accoude --dossier references`.

```
Make a full-body sheet of Maëlle: a regular grid of 3 columns and 1 row, landscape format (1536×1024), three equal tall cells separated by thin white gaps. In each cell, Maëlle full body from head to feet, neutral watchful expression, same scale, same light, plain light-grey background, no other furniture than the one named. Her usual outfit, exactly as in the attached full-body image: the black fitted turtleneck sweater in a matte, slightly textured fabric, its sleeves pushed up to the forearms; black slim high-waisted trousers, fitted but practical; sturdy black ankle boots with a square heel. One wide silver ring on HER RIGHT THUMB only; her left hand has no ring; no other jewelry. Short unpainted nails. Her copper-red hair: HER LEFT side shaved, the longer, messy strands falling over HER RIGHT side of the face. A small vertical scar through HER LEFT eyebrow. Fine black winged eyeliner, a light dusting of freckles on the nose and upper cheeks, green eyes. Broad swimmer's shoulders, toned forearms, an athletic hourglass build, 1.65 m. Cells, left to right:

1. Sitting on a simple wooden chair, facing the viewer, one leg crossed over the other, her hands resting on her knee, the silver ring visible on her right thumb.
2. Sitting on the same chair, in profile showing HER LEFT side: we see the shaved side of her head.
3. Standing, leaning with her right elbow on a plain light-grey block at counter height, a coffee cup in her left hand.

No text or labels anywhere.
```

Résultat de M3, le 2026-10-18 : les poses et les côtés justes, la bague à l'index (cases 1 et 3). Claude propose de ne plus courir après la bague dans ChatGPT : il la change de doigt à chaque retouche, et le LoRA n'apprendra pas un doigt précis de toute façon (un détail de quelques pixels, que le modèle redessine à chaque image). En production, elle se corrige par inpainting sur les plans où sa main droite se voit de près. Si l'auteur veut quand même la retouche :

```
Edit ONLY the hands. Keep everything else exactly as it is, in all three cells. In each cell, the wide silver ring is on HER RIGHT hand, around the THUMB, the short thick finger set apart from the four others: move it there from the finger it is on now. In the first cell, her right hand is the upper hand on her knee; in the third cell, it is the hand hanging over the grey block. Her left hand has no ring.
```

### Prompt M4 — Six gestes

À écrire quand l'auteur aura validé les six gestes (l'inventaire : « à fixer avec l'auteur avant les prompts »). L'inventaire en avait déjà une liste : boire son café, tenir sa tasse à deux mains, les bras croisés, ramasser une serviette sur la table, regarder son téléphone, travailler sur un laptop ; sans manger, alors que le premier test la fait manger à côté de Sky. Proposition de Claude, d'après le texte du CERN, Navier-Stokes et le test prévu (Sky et Maëlle qui mangent côte à côte) : boire son café, croquer dans une galette, mâcher la bouche pleine, prendre une photo avec son téléphone (Navier-Stokes, l. 411), plier une serviette et la glisser dans sa poche (CERN, l. 540), donner un ordre, l'index levé (« Monte. Dors. Je gère. »).
