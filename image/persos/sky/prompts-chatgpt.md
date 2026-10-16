# Sky — les prompts ChatGPT, série 2

La série 1, faite avec la monture argentée, est archivée sur le disque externe avec ses prompts : `<sorties_root>/persos/sky/archive_serie-1_2026-10-14/prompts-chatgpt_serie-1.md`. Ce qu'on en a appris est aussi dans `journal.md`. La série 2 repart d'une image maître propre, dans une nouvelle conversation ChatGPT, avec les prompts corrigés d'emblée :
- le côté se dit par son œil bleu, jamais par « right » ou « left » seuls ;
- les yeux fermés se font en retouche : quand ChatGPT génère une image, il laisse toujours l'œil aveugle ouvert ;
- le désir se dit « Craving », et il regarde la bouffe ;
- la monture est plaquée or, avec son double pont, et chaque prompt le redit ;
- pour une retouche, l'image part dans le même message que le prompt, qui commence par « Edit ONLY the image attached to this message ».

## Le mode d'emploi

1. Ouvre une nouvelle conversation ChatGPT, rien que pour la série 2 de Sky.
2. Un prompt à la fois. Claude met l'image à joindre dans ton presse-papiers (Ctrl+V) et dans tes Téléchargements.
3. Envoie chaque image à Claude : il la contrôle, la range et met le suivi à jour avant le prompt suivant.

| Prompt | Image | Où la ranger |
|---|---|---|
| A | L'image maître v3, en retouche de la v2 | `references/master_v3.png` |
| B | Le contexte, avec l'image maître v3 jointe | |
| C | La rotation, 6 vues : faite | `planches/rotation_v1.png` |
| D | En pied : faite | `references/pied_v1.png` |
| E1 à E6 | Palette de face, planches 1 à 6 : faites | `planches/emotions-1_v1.png` à `emotions-6_v1.png` |
| F | Les reprises de face et le clignement : faites | `planches/reprises_v2.png` |
| G | Signatures 1 : ses six manies : faite | `planches/signatures-1_v1.png` |
| G bis | Retouche : le sourcil levé, le feu vert, le doute, la malice : faite | `planches/retouche-1_v2.png` |
| H | Signatures 2 : « l'autre » : faite, seul le haussement d'épaules est gardé | `planches/signatures-2_v1.png` |
| H bis | « L'autre », en monstre : faite | `planches/signatures-2_v2.png` |
| I | Les bouches : faite | `planches/bouches_v1.png` |
| J | Les bouches du sourire : faite | `planches/bouches-sourire_v1.png` |
| K1 à K6 | Palette de trois-quarts, planches 1 à 6 : faites | `planches/trois-quarts_emotions-1_v1.png` à `trois-quarts_emotions-6_v1.png` |
| K7 | La retouche de trois-quarts : deux yeux, deux bagues : faite | `planches/trois-quarts_retouche_v2.png` |
| L1 | En pied : de face, de trois-quarts des deux côtés | `planches/pied-1_v1.png` |
| L2 | En pied : de profil des deux côtés, de dos | `planches/pied-2_v1.png` |
| L3 | Trois poses : assis de face, assis de côté, debout accoudé | `planches/poses_v1.png` |
| L4 | Six gestes de face | `planches/gestes_v1.png` |
| L5 | Les six gestes de trois-quarts | `planches/trois-quarts_gestes_v1.png` |

La suite du tableau s'écrit au fil de la série. Les chemins partent de `image/persos/sky/`.

## Prompt A — L'image maître v3

Ce que veut l'auteur, le 2026-10-14 : gommer le trait entre les sourcils et les taches autour des yeux (les restes des tirets de l'ancienne monture), passer à une barbe de 3 jours, et donner à l'œil aveugle la taille de l'autre. Les cernes restent : c'est un de ses traits. Joins l'image maître v2 dans le même message.

```
Edit ONLY the image attached to this message. Change only these details of his face, and keep everything else exactly as it is (pose, clothes, hands, bottle, background, light, framing, style):
1. Remove the thin dark line between his eyebrows.
2. Remove the small dark spots and dashes around his eyes and along the lower rims of his glasses. Keep his dark circles under the eyes. The gold frame stays one clean, continuous, thin line, with its double bridge.
3. Turn his beard into a three-day stubble: short little hairs evenly all over the jaw, chin, upper lip and cheeks, same color, no longer a full beard.
4. His blind left eye (on the right of the image) must be exactly the same size and shape as his right eye, with the same eyelids: just entirely milky white, with no iris and no pupil, dead and natural.
```

Résultat, le 2026-10-14 : le trait et les taches sont partis, la barbe est passée à 3 jours. ChatGPT n'a pas voulu réduire l'œil aveugle, malgré plusieurs essais de l'auteur. L'auteur garde cette image : c'est `references/master_v3.png`, la référence de la série 2.

Un dernier essai de l'auteur, en parlant de la paupière et non plus de la taille (« lower the upper eyelid of his blind left eye to the same height as the upper eyelid of his right eye ») : refusé, et ChatGPT a remis les taches au-dessus des yeux. On garde la v3.

## Prompt B — Le contexte

Dans la nouvelle conversation, ChatGPT ne connaît pas la description maître : elle est dans le prompt, corrigée pour la série 2 (barbe de 3 jours, monture plaquée or avec son double pont). Le bloc « DEFAULT PERSONALITY / EXPRESSION » n'y est pas : il ramenait toutes les émotions vers son air fatigué. La taille de l'œil aveugle n'y est pas non plus, pour ne pas contredire l'image. Joins l'image maître v3.

```
I'm going to ask you for reference sheets of Sky, the main character of my 1990s-style anime series, one at a time. I'm attaching his master image: keep him exactly as in it, and as in this description.

SKY — MASTER CHARACTER DESCRIPTION
Sky is a 32-year-old man, 1.87 m tall and 92 kg, with a very muscular, lean physique and very low body fat: very broad shoulders, thick upper back and chest, powerful arms, large hands, and especially large, dense forearms with clearly visible veins. His musculature looks functional and heavy, not bodybuilder-stage exaggerated.
His face is masculine and angular, with a strong square jaw, pronounced cheekbones and a straight nose. His skin has a warm, lightly tanned complexion.
His hair is short, messy and slightly spiked, light chestnut / dark sandy blond, exactly between brown and blond. His eyebrows are similar in tone, straight and strong.
He has a three-day stubble: short, even little hairs all over the jaw, chin, upper lip and cheeks, a little lighter than his hair, with some white hairs mixed in. Not a full beard, not clean-shaven.
His right eye is a very deep, vivid blue, with a bright reflective highlight. His left eye is completely blind: entirely milky white, with no iris and no pupil. It looks naturally blind, never glowing or supernatural.
He wears large aviator prescription glasses with a thin, clean, gold-plated metal frame and a double bridge: a thin straight bar between the tops of the lenses, above the nose bridge. The lenses are completely clear, never tinted, and his eyes stay clearly visible through them.
He has extremely pronounced dark circles under both eyes, deep brown-black shadows that make him look chronically sleep-deprived. They stay visible through his glasses.
Around his neck: a very thin black leather cord worn tight like a minimalist choker, and below it a longer thin metal chain ending in two interlocking metal rings.
One bronze ring on his right little finger only. No other rings.
His outfit: a white long-sleeved button-up shirt, slightly loose but stretched across his chest and shoulders, sleeves pushed up to just below the elbows so his forearms show, worn slightly open at the chest. A sparse black-and-white botanical lily pattern (real lily flowers and leaves, not fleur-de-lis), mostly on the torso; the collar and sleeves stay almost plain. Black tracksuit trousers in a soft matte fabric, with no logo, lettering or stripes.

ART STYLE
A high-quality 1990s hand-drawn anime character: strong but clean ink lines, realistic adult anatomy, slightly angular facial construction, traditional cel shading with one or two hard shadow tones, no glossy modern digital rendering. The look blends 1990s fighting-anime character construction, late-1990s psychological-anime facial design and warm hand-painted animation-film colors, with subtle film grain.

RULES FOR EVERY SHEET
Plain light-grey background, soft even light with no strong shadows. No text, no labels, no numbers. Cells are separated only by thin white gaps. From one cell to the next, only the thing I ask for changes.
His left eye stays blind in every image: only its eyelid and brow move, and every pupil effect (a tiny pupil, a highlight, a wide eye) applies to his right eye.
When I say "his right side", I mean the side of his blue eye.
His glasses, with their gold frame and double bridge, his stubble and his dark circles stay identical in every cell.
Never redesign him, never make him younger, never remove the dark circles, never give the blind eye an iris or a pupil, never tint the glasses.

Don't generate anything yet: just confirm you understand.
```

## Prompt C — La rotation, 6 vues

La même que dans la série 1, qui avait marché du premier coup, avec la ligne des lunettes en plus. Joins l'image maître v3. Découpe : `--noms face,trois-quarts-gauche,trois-quarts-droit,profil-gauche,profil-droit,dos --dossier references`.

```
Make a turnaround sheet of Sky: a regular grid of 3 columns and 2 rows, landscape format (1536×1024), six equal cells. The same head-and-shoulders framing in every cell, neutral expression, same light. Only the camera angle changes. Cells read left to right, then top to bottom:

1. Front view.
2. Three-quarter view showing HIS LEFT side (the blind eye side).
3. Three-quarter view showing HIS RIGHT side (the blue eye side).
4. Profile showing HIS LEFT side.
5. Profile showing HIS RIGHT side.
6. Back view.

In every cell, the blind eye stays his left one. His glasses keep their thin gold-plated frame and their double bridge (a thin straight bar between the tops of the lenses, above the nose bridge). No text or labels anywhere.
```

Résultat, le 2026-10-15 : bonne du premier coup. L'œil aveugle reste le gauche dans toutes les vues, la monture dorée et sa barre partout, la barbe de 3 jours.

## Prompt D — En pied

Le corps entier : sa silhouette, sa carrure, ses chaussures. Dans la série 1, ChatGPT avait ouvert la chemise jusqu'au ventre et montré l'élastique du caleçon : le prompt le précise maintenant. Joins l'image maître v3.

```
Make a full-body image of Sky, standing, facing the viewer, neutral expression, arms relaxed, portrait format (1024×1536). His usual outfit: white shirt with the sparse black-and-white lily pattern, open only at the top of the chest, no underwear visible; sleeves pushed up just below the elbows; both necklaces; the bronze ring on his right little finger; black tracksuit trousers; black sneakers. His glasses keep their thin gold-plated frame and their double bridge. Plain light-grey background, soft even light, no text.
```

Résultat, le 2026-10-15 : bonne, « parfaite » pour l'auteur. La bague est à l'auriculaire droit, les baskets sont noires, et on ne voit pas de caleçon. Le bas de la chemise s'ouvre un peu sur le ventre.

## Prompt E1 — Palette de face, planche 1 : les universelles

Les six émotions qu'on retrouve partout dans le monde (Ekman). Le neutre sert aussi de base aux bouches et au clignement. Joins l'image maître v3. Découpe : `--emotions 1`.

```
Make an expression sheet of Sky: a regular grid of 3 columns and 2 rows, landscape format (1536×1024), six equal cells. In each cell, the same head-and-shoulders bust, facing the viewer (front view, both eyes visible), same framing, same pose, same light. Only his facial expression changes; his hands may enter the frame only when the expression needs them. Each expression must be clearly different from the others: avoid his usual tired, heavy-lidded, unimpressed look unless a cell asks for it. Cells read left to right, then top to bottom:

1. Neutral: relaxed face, straight gaze, mouth closed.
2. Joy: a broad, genuine smile showing his upper teeth, cheeks pushed up, eyes crinkled with laugh lines. Both corners of the mouth rise.
3. Sadness: inner ends of the eyebrows raised, heavy eyelids, corners of the mouth turned down.
4. Anger: eyebrows drawn down and together, a hard stare, jaw clenched, lips pressed.
5. Fear: eyebrows raised and pulled together, his right eye wide open, mouth stretched back.
6. Surprise: eyebrows high and rounded, eyes wide, mouth open in an O.

His glasses keep their thin gold-plated frame and their double bridge (a thin straight bar between the tops of the lenses, above the nose bridge). No text or labels anywhere.
```

Résultat, le 2026-10-15 : bonne du premier coup. La monture dorée et sa barre dans les six cases, pas de taches, l'œil aveugle blanc partout.

## Prompt E2 — Palette de face, planche 2 : les universelles, suite, et leurs pics

Le dégoût et le mépris, puis les versions fortes : le rire, les pleurs, la rage, la terreur. Le mépris se met du côté de l'œil bleu, dit comme dans les reprises de la série 1, qui avaient marché. Pour le rire, ChatGPT laissera sans doute l'œil aveugle ouvert : on le fermera en retouche à la fin (prompt F). Joins l'image maître v3. Découpe : `--emotions 2`.

```
Make an expression sheet of Sky: a regular grid of 3 columns and 2 rows, landscape format (1536×1024), six equal cells. In each cell, the same head-and-shoulders bust, facing the viewer (front view, both eyes visible), same framing, same pose, same light. Only his facial expression changes; his hands may enter the frame only when the expression needs them. Each expression must be clearly different from the others: avoid his usual tired, heavy-lidded, unimpressed look unless a cell asks for it. Cells read left to right, then top to bottom:

1. Disgust: wrinkled nose, upper lip raised.
2. Contempt: only one corner of the mouth raised, on HIS RIGHT side, the side of his blue eye (the left of the image); the other corner stays flat. Looking down his nose at someone.
3. Laughter: mouth wide open, both eyes squeezed nearly shut (the blind one too, not a wink), head tilted back.
4. Crying: tears running down, distressed eyebrows, trembling mouth.
5. Rage: eyebrows very low, teeth clenched or a shouting mouth, an anime anger vein on the temple.
6. Terror: his right eye bulging with a tiny pupil, mouth open, the face drained pale.

His glasses keep their thin gold-plated frame and their double bridge (a thin straight bar between the tops of the lenses, above the nose bridge). No text or labels anywhere.
```

Résultat, le 2026-10-15 : bonne du premier coup. Le mépris est du côté de l'œil bleu. Pour le rire, les deux yeux sont fermés, l'aveugle aussi : c'est la première fois en génération (avec le contexte de la série 2 et « the blind one too, not a wink »). Quelques points minuscules au bord bas des verres, les mêmes que sur l'image maître v3.

## Prompt E3 — Palette de face, planche 3 : l'esprit

La stupeur, puis les émotions de la pensée : l'intérêt, la concentration, la confusion, le doute, la méfiance. La confusion et le doute lèvent le sourcil de l'œil bleu, dit comme dans les reprises de la série 1, qui avaient marché (dans la série 1, cette planche les avait mis du côté de l'œil aveugle). Joins l'image maître v3. Découpe : `--emotions 3`.

```
Make an expression sheet of Sky: a regular grid of 3 columns and 2 rows, landscape format (1536×1024), six equal cells. In each cell, the same head-and-shoulders bust, facing the viewer (front view, both eyes visible), same framing, same pose, same light. Only his facial expression changes; his hands may enter the frame only when the expression needs them. Each expression must be clearly different from the others: avoid his usual tired, heavy-lidded, unimpressed look unless a cell asks for it. Cells read left to right, then top to bottom:

1. Shock: far stronger than surprise. Jaw dropped all the way down, mouth hanging open in a tall oval, a tiny pupil in his right eye, the whole face frozen.
2. Interest: head slightly tilted, eyebrows slightly raised, an attentive gaze.
3. Concentration: calm focus. Eyes looking down at a laptop screen just below the frame, brows slightly knit, lips pressed. Not angry, not looking at the viewer.
4. Confusion: the eyebrow above his blue eye (on the left of the image) raised higher than the other one, head tilted, a crooked mouth.
5. Doubt: the eyebrow above his blue eye (on the left of the image) raised, the other one stays low, pursed lips, a sideways glance.
6. Suspicion: narrowed eyes, a sideways look, chin tucked in.

His glasses keep their thin gold-plated frame and their double bridge (a thin straight bar between the tops of the lenses, above the nose bridge). No text or labels anywhere.
```

Résultat, le 2026-10-15 : bonne. La confusion lève bien le sourcil de l'œil bleu. Le doute est plus faible : les sourcils restent presque à la même hauteur, il se lit par le regard de côté et les lèvres pincées. Gardé ; une reprise reste possible à la fin.

## Prompt E4 — Palette de face, planche 4 : les émotions sociales

La gêne, la honte, la fierté, la jalousie, la tendresse et le désir. Pour lui, le désir est celui de la bouffe : la ligne vient des reprises de la série 1, qui avaient marché (« Longing » donnait de la nostalgie, le regard en l'air). Joins l'image maître v3. Découpe : `--emotions 4`.

```
Make an expression sheet of Sky: a regular grid of 3 columns and 2 rows, landscape format (1536×1024), six equal cells. In each cell, the same head-and-shoulders bust, facing the viewer (front view, both eyes visible), same framing, same pose, same light. Only his facial expression changes; his hands may enter the frame only when the expression needs them. Each expression must be clearly different from the others: avoid his usual tired, heavy-lidded, unimpressed look unless a cell asks for it. Cells read left to right, then top to bottom:

1. Embarrassment: a forced smile, eyes escaping downward, red cheeks, a hand rubbing the back of his neck.
2. Shame: head down, eyes on the floor, shoulders hunched.
3. Pride: head high, chin up, a slight smile, chest out.
4. Jealousy: a side-eye, clenched jaw, low eyebrows.
5. Tenderness: a soft gaze, relaxed eyelids, a light warm smile.
6. Craving: staring hungrily at a chicken wrap on the table just below the frame, eyes locked on it, lips parted, a drop of drool at the corner of his mouth. Hunger, not nostalgia.

His glasses keep their thin gold-plated frame and their double bridge (a thin straight bar between the tops of the lenses, above the nose bridge). No text or labels anywhere.
```

Résultat, le 2026-10-15 : bonne du premier coup. La gêne a la main sur la nuque et les joues rouges, le désir regarde la galette et bave. La tendresse reste retenue (paupières détendues, petit sourire fermé), ce qui colle à Sky.

## Prompt E5 — Palette de face, planche 5 : les nuances

Le contentement, le soulagement, l'exaltation, le triomphe, l'émerveillement et la déception. Le contentement et le soulagement ferment les deux yeux, l'aveugle aussi : la formulation qui a marché pour le rire de la planche 2. Le poing du triomphe porte la bague (dans la série 1, elle manquait). Joins l'image maître v3. Découpe : `--emotions 5`.

```
Make an expression sheet of Sky: a regular grid of 3 columns and 2 rows, landscape format (1536×1024), six equal cells. In each cell, the same head-and-shoulders bust, facing the viewer (front view, both eyes visible), same framing, same pose, same light. Only his facial expression changes; his hands may enter the frame only when the expression needs them. Each expression must be clearly different from the others: avoid his usual tired, heavy-lidded, unimpressed look unless a cell asks for it. Cells read left to right, then top to bottom:

1. Contentment: both eyes gently closed (the blind one too, not a wink), a small peaceful smile, a relaxed face.
2. Relief: both eyes closed (the blind one too, not a wink), head tilted back, mouth open in a big sigh, as if saying "phew", shoulders dropping, a small anime sweat drop on his temple.
3. Elation: a beaming open-mouthed smile, eyebrows high, overflowing joy.
4. Triumph: a big open-mouthed grin, chin up, his right fist clenched and raised in the frame, the bronze ring on its little finger.
5. Wonder: looking up at something above the frame, his right eye shining, lips parted in a faint smile, eyebrows raised. No shock, no fear.
6. Disappointment: a pout, eyes lowered, inner brows slightly raised.

His glasses keep their thin gold-plated frame and their double bridge (a thin straight bar between the tops of the lenses, above the nose bridge). No text or labels anywhere.
```

Résultat, le 2026-10-15 : bonne du premier coup. Le contentement et le soulagement ferment les deux yeux, l'aveugle aussi. Le poing du triomphe porte la bague.

## Prompt E6 — Palette de face, planche 6 : l'humeur et le corps

L'inquiétude, l'agacement, la malice, l'ennui, la fatigue et la douleur. La malice se met du côté de l'œil bleu (dans la série 1, c'est cette formulation qui l'a mise du bon côté). La fatigue et la douleur ferment les deux yeux, comme le rire et le contentement. Les mains de l'ennui et de la fatigue portent la bague. Joins l'image maître v3. Découpe : `--emotions 6`.

```
Make an expression sheet of Sky: a regular grid of 3 columns and 2 rows, landscape format (1536×1024), six equal cells. In each cell, the same head-and-shoulders bust, facing the viewer (front view, both eyes visible), same framing, same pose, same light. Only his facial expression changes; his hands may enter the frame only when the expression needs them. Each expression must be clearly different from the others: avoid his usual tired, heavy-lidded, unimpressed look unless a cell asks for it. Cells read left to right, then top to bottom:

1. Worry: eyebrows raised and pulled together, a tense mouth.
2. Annoyance: furrowed brows, rolling his eyes, sighing.
3. Mischief: a playful, teasing grin showing a little of his teeth on HIS RIGHT side, the side of his blue eye (the left of the image), and the eyebrow above his blue eye arched high. Warm and cheeky, not cold.
4. Boredom: heavy eyelids, head resting on his right hand (the bronze ring on its little finger), an empty gaze.
5. Tiredness: both eyes half closed (the blind one too), a big yawn, his right hand rising toward his mouth, the bronze ring on its little finger.
6. Pain: both eyes squeezed shut (the blind one too, not a wink), clenched teeth, a grimace.

His glasses keep their thin gold-plated frame and their double bridge (a thin straight bar between the tops of the lenses, above the nose bridge). No text or labels anywhere.
```

Résultat, le 2026-10-15 : bonne, sauf la malice. Le sourire et le sourcil levé sont du côté de l'œil aveugle, avec la tête penchée de ce côté, alors que la même formulation avait marché dans la série 1. La douleur ferme les deux yeux. Pour la fatigue, l'œil bleu est fermé et l'aveugle mi-clos : avec le bâillement, ça se lit, on garde. Les mains de l'ennui et de la fatigue portent la bague.

Avec le rire, le contentement, le soulagement et la douleur, tous les yeux fermés de la série 2 sont sortis bons en génération : la retouche des yeux fermés n'est plus utile. Le clignement se fait dans les reprises.

## Prompt F — Les reprises de face et le clignement

La malice, refaite avec la tête droite et l'autre coin de la bouche qui reste bas. Le doute, refait avec le sourcil nettement levé. Et les deux images du clignement, pour l'animation : les yeux mi-clos, puis fermés. Joins l'image maître v3. Découpe : `--noms malice,doute,clignement-mi-clos,clignement` ; tout sort en `_v2`, puis `clignement-mi-clos_v2.png` et `clignement_v2.png` se renomment en `_v1`, puisque c'est leur première version.

```
Make an expression sheet of Sky: a regular grid of 2 columns and 2 rows, square format (1024×1024), four equal cells. In each cell, the same head-and-shoulders bust as in his previous expression sheets, facing the viewer (front view, both eyes visible), head straight and not tilted, same framing, same light. Only his facial expression changes. Here, "his right side" always means the side of his blue eye, on the LEFT of the image. Cells read left to right, then top to bottom:

1. Mischief: a playful, teasing grin. Only the corner of his mouth on HIS RIGHT side (the blue eye side, on the left of the image) rises and shows a little of his teeth; the other corner stays low. The eyebrow above his blue eye is arched high; the other eyebrow stays level. Warm and cheeky, not cold.
2. Doubt: the eyebrow above his blue eye (on the left of the image) clearly raised, the other one stays low, pursed lips, a sideways glance.
3. Blink, halfway: his neutral face, both eyes half closed (the blind one too), as in the middle of a blink.
4. Blink, closed: his neutral face, both eyes gently closed (the blind one too, not a wink).

His glasses keep their thin gold-plated frame and their double bridge (a thin straight bar between the tops of the lenses, above the nose bridge). No text or labels anywhere.
```

Résultat, le 2026-10-15 : le clignement est bon, mi-clos puis fermé, les deux yeux ensemble. La malice a la tête droite, mais son sourire, plus sage, penche encore du côté de l'œil aveugle ; le doute n'est pas plus net. On garde les versions 1 des deux : la malice reste de son côté gauche, c'est là que ChatGPT la met.

## Prompt G — Signatures 1 : ses six manies

Les moments propres à Sky, tirés de la bible et du texte : il mâche en regardant le plafond, bouche pleine pas impressionné, le sourcil levé, il blêmit, le regard vide du mode silence, et le regard qui cherche le feu vert de Maëlle. Le sourcil se lève du côté de l'œil bleu. Joins l'image maître v3. Découpe : `--noms regard-plafond,bouche-pleine,sourcil-leve,blemit,regard-vide,cherche-feu-vert`.

```
Make a sheet of Sky's signature expressions: a regular grid of 3 columns and 2 rows, landscape format (1536×1024), six equal cells. In each cell, the same head-and-shoulders bust, facing the viewer, same framing, same light. Each expression must be clearly different from the others. Cells read left to right, then top to bottom:

1. Chewing, looking up at the ceiling, thinking, one cheek slightly full.
2. Mouth full of food, cheeks slightly puffed, a completely unimpressed stare.
3. The eyebrow above his blue eye (on the left of the image) raised, the other one stays level, unimpressed, looking at someone.
4. Turning pale: the color drains from his face, he swallows hard, frozen, as if he just heard the one word that scares him.
5. The silent mode: his gaze drifts to a point no one else sees, the face completely still, absent.
6. A quick sideways glance at someone just out of frame, checking for approval, like a kid waiting for a green light.

His glasses keep their thin gold-plated frame and their double bridge (a thin straight bar between the tops of the lenses, above the nose bridge). No text or labels anywhere.
```

Résultat, le 2026-10-15 : quatre bonnes (le plafond, la bouche pleine, il blêmit, le regard vide). Pour le feu vert, ses deux yeux regardent de côté, et ChatGPT a donné un iris bleu à l'œil aveugle : à corriger. Le sourcil levé se voit à peine.

## Prompt G bis — La retouche : le sourcil levé, le feu vert, le doute, la malice

En retouche, ChatGPT corrige un détail sans toucher au reste : c'est ce qui a marché pour les yeux fermés et pour les lunettes. Il faut corriger le feu vert de toute façon, alors on y joint les trois cases qui résistent en génération : le sourcil levé, le doute et la malice. Claude a assemblé les quatre cases en un carré : `<sorties_root>/persos/sky/retouche-1_a-retoucher.png`, dans l'ordre sourcil levé, feu vert, doute (v1), malice (v1). Joins cette image seule, dans le même message. Découpe dans un dossier de travail, puis rangement : `sourcil-leve_v2`, `cherche-feu-vert_v2`, `doute_v3`, `malice_v3` (les v2 du doute et de la malice existent déjà).

```
Edit ONLY the image attached to this message. It is a sheet of four of Sky's expressions. Keep everything exactly as it is (faces, expressions, framing, colors, glasses, grid, white gaps), except these details:
1. Cell 1: raise the eyebrow above his blue eye (on the left of the image) clearly higher; the other eyebrow stays level.
2. Cell 2: his left eye (on the right of the image) is blind: remove its blue iris, so it is entirely milky white, with no iris and no pupil, like in the other cells.
3. Cell 3: raise the eyebrow above his blue eye (on the left of the image) clearly higher; the other eyebrow stays low.
4. Cell 4: make the grin one-sided on the left of the image: only the corner of his mouth on the left of the image rises and shows a little of his teeth; the corner on the right of the image comes down. Keep the rest of his face as it is.
No text or labels anywhere.
```

Résultat, le 2026-10-15 : trois corrections sur quatre. Le sourcil levé et celui du doute montent nettement du côté de l'œil bleu, et l'œil aveugle du feu vert est redevenu blanc. La malice n'a pas changé de côté : on garde sa v1. Rangement : `sourcil-leve_v2`, `cherche-feu-vert_v2`, `doute_v3` (retenues), `malice_v3` (pas retenue).

## Prompt H — Signatures 2 : « l'autre »

« L'autre », c'est Sky quand le sourire arrive : le reflet de son œil bleu s'éteint, seule la bouche bouge, les canines s'affinent en pointe (référence de l'auteur : le sourire de Tanya dans Youjo Senki, qu'on ne nomme pas). Puis le rire du dégénéré. Et le haussement d'épaules, « comme si on lui disait qu'il a du sel sur la table ». L'œil aveugle reste blanc dans chaque case : le feu vert a montré qu'il peut prendre un iris. Joins l'image maître v3. Découpe : `--noms haussement-epaules,le-sourire,trois-quarts_le-sourire,rire-degenere`.

```
Make a sheet of Sky's signature expressions: a regular grid of 2 columns and 2 rows, landscape format (1536×1024), four equal cells. In each cell, the same head-and-shoulders bust, same light. In every cell his left eye stays blind: entirely milky white, with no iris and no pupil. Cells read left to right, then top to bottom:

1. A shrug, facing the viewer, framed a little wider so his hands show: shoulders raised, palms slightly up, the bronze ring on his right little finger, as if someone just told him there is salt on the table.
2. Facing the viewer: the smile of "the other one": a slow, predatory, psychopathic grin. Lips pulled thin and wide, teeth showing and clenched, his canines slightly pointed like a predator's. Only the mouth moves: no crinkles at the eyes, flat cheeks. His blue right eye loses its highlight and goes flat and dead. Head slightly lowered, looking straight at the viewer from under his brows. Cold, not joyful.
3. The same smile, in a three-quarter view showing HIS RIGHT side (his blue eye nearer to us).
4. Facing the viewer, the degenerate laugh: a manic laugh from the belly, mouth wide open, teeth bared with slightly pointed canines, his blue right eye wide with a tiny pupil, head tilted, unhinged.

His glasses keep their thin gold-plated frame and their double bridge (a thin straight bar between the tops of the lenses, above the nose bridge). No text or labels anywhere.
```

Résultat, le 2026-10-15 : le haussement d'épaules est bon (la bague à l'auriculaire droit). Le sourire et le rire sont refusés par l'auteur : « trop gentillet, on sent pas assez le monstre par rapport à Youjo Senki ». On lit un petit malin qui ricane, pas le prédateur.

## Prompt H bis — « L'autre », en monstre

Ce qui fait le monstre du sourire de Tanya, décrit sans la nommer : l'ombre qui tombe sur le haut du visage, l'œil qui brille dedans avec une pupille minuscule, le sourire beaucoup trop large, les crocs, et le reste du visage qui ne bouge pas. La bible le veut froid (« la version calme du berserker », les guerriers-loups, « seule la bouche bouge, joues plates ») : on garde ça, on pousse le reste. Le rire du dégénéré, lui, part complètement. On ajoute le rire de trois-quarts : dans « Le Miroir », il rit en dessinant sur le miroir. Joins l'image maître v3. Découpe : `--noms le-sourire,trois-quarts_le-sourire,rire-degenere,trois-quarts_rire-degenere` ; tout sort en `_v2`, puis `trois-quarts_rire-degenere_v2.png` se renomme en `_v1`.

```
Your last sheet was too friendly: here Sky must look like a monster, a predator that has just found its prey. Make a new sheet of Sky: a regular grid of 2 columns and 2 rows, landscape format (1536×1024), four equal cells, same light. In every cell his left eye stays blind: entirely milky white, with no iris and no pupil. His glasses keep their thin gold-plated frame and their double bridge. Cells read left to right, then top to bottom:

1. Facing the viewer: the smile of "the other one". His head tilted down, he stares straight at the viewer from under his brows. A heavy dark shadow falls over the upper half of his face, and his blue right eye glints out of it: wide open, the pupil shrunk to a pinpoint, flat and dead, without its highlight. The rest of his face stays completely still, cheeks flat, no crinkles at the eyes: only the mouth moves, stretched far too wide, almost from ear to ear, into a thin crescent grin, teeth bared and clenched, the canines sharp and pointed like fangs. Cold, calm, terrifying. Not joyful, not friendly.
2. The same smile, in a three-quarter view showing HIS RIGHT side (his blue eye nearer to us), with the same shadow and the same fangs.
3. Facing the viewer: the degenerate laugh, a manic laugh rising from the belly. Head thrown back and tilted, mouth gaping wide open, every tooth bared, the canines sharp and pointed like fangs, deep creases around the mouth, his blue right eye bulging with a pinpoint pupil, eyebrows twisted, sweat on his temple, a dark shadow over his forehead. Unhinged, possessed by an idea, no warmth.
4. The same degenerate laugh, in a three-quarter view showing HIS RIGHT side (his blue eye nearer to us).

No text or labels anywhere.
```

Résultat, le 2026-10-15 : « mieux » pour l'auteur. L'ombre sur le haut du visage, l'œil bleu à pupille minuscule, le sourire trop large, des crocs en haut et en bas. L'œil aveugle reste blanc dans les quatre cases, le trois-quarts montre bien son côté droit. Ce qui a marché : décrire ce qui fait peur, et dire à ChatGPT que sa planche d'avant était trop gentille.

## Prompt I — Les bouches

Pour la méthode des calques : seul celui qui parle bouge, avec trois bouches selon le volume de la voix, de face et de trois-quarts. Le prompt ramène son visage normal, sans crocs ni ombre : dans la même conversation, la planche d'avant était le monstre. Joins l'image maître v3. Découpe : `--noms face_fermee,face_mi-ouverte,face_ouverte,trois-quarts_fermee,trois-quarts_mi-ouverte,trois-quarts_ouverte --dossier bouches`.

```
Make a mouth sheet of Sky: a regular grid of 3 columns and 2 rows, landscape format (1536×1024), six equal cells. A close-up of his face, back to his normal face as in his master image: neutral expression, normal teeth, no fangs, no shadow over his face, his blue eye with its usual highlight. The same framing within each row. Only the mouth changes: his stubble, his eyes and the rest of his face stay exactly the same from one cell to the next. In every cell his left eye stays blind: entirely milky white, with no iris and no pupil.

Top row, front view: 1. mouth closed, 2. mouth half open, 3. mouth open, as when speaking.
Bottom row, three-quarter view showing HIS RIGHT side (his blue eye nearer to us): 4. closed, 5. half open, 6. open.

His glasses keep their thin gold-plated frame and their double bridge (a thin straight bar between the tops of the lenses, above the nose bridge). No text or labels anywhere.
```

Résultat, le 2026-10-15 : bonne. ChatGPT redessine toute la tête dans chaque case : c'est ce que le prompt demande (un gros plan du visage), comme pour Maëlle. Mesuré par Claude : d'une case à l'autre d'une rangée, le haut du visage bouge de 2 à 3 pixels, la bouche seule change vraiment. Visage normal, sans crocs, l'œil aveugle blanc, le trois-quarts montre son côté droit.

## Prompt J — Les bouches du sourire

Les bouches de « l'autre », dans la version monstre validée (H bis) : sourire fermé, grimace, rire ouvert, de face et de trois-quarts. La tête reste dans la même pose d'une case à l'autre : seule la bouche change. Joins l'image maître v3. Découpe : `--noms face_sourire-ferme,face_sourire-grimace,face_sourire-rire,trois-quarts_sourire-ferme,trois-quarts_sourire-grimace,trois-quarts_sourire-rire --dossier bouches`.

```
Make a mouth sheet of Sky as "the other one", the monster of his smile sheet: a regular grid of 3 columns and 2 rows, landscape format (1536×1024), six equal cells. A close-up of his face, the same framing and the same head pose within each row. In every cell, the same face of "the other one": a heavy dark shadow over the upper half of his face, his blue right eye glinting out of it with a pinpoint pupil, flat and dead, no crinkles at the eyes, flat cheeks. Only the mouth changes. In every cell his left eye stays blind: entirely milky white, with no iris and no pupil.

Top row, front view: 1. the smile with lips closed, stretched far too wide into a thin crescent; 2. the grin: teeth bared and clenched, the canines sharp and pointed like fangs; 3. the open laugh: mouth gaping wide open, fangs bared.
Bottom row, three-quarter view showing HIS RIGHT side (his blue eye nearer to us): 4. lips closed, 5. the grin, 6. the open laugh.

His glasses keep their thin gold-plated frame and their double bridge (a thin straight bar between the tops of the lenses, above the nose bridge). No text or labels anywhere.
```

Résultat, le 2026-10-15 : bonne du premier coup. Le visage de « l'autre » dans les six cases, l'œil aveugle blanc, le trois-quarts du côté de l'œil bleu, la tête qui bouge de 1 à 3 pixels d'une case à l'autre.

## Bilan de la série 2

Le 2026-10-15, en une conversation : 24 prompts, de A à K7, dont 5 de reprise ou de retouche (A, F, G bis, H bis, K7), sans compter les essais de l'auteur sur l'œil aveugle. L'auteur a voulu la palette de trois-quarts dans la foulée : prompts K1 à K7, plus bas.

## Prompt K1 — Palette de trois-quarts, planche 1 : les universelles

Dans la série 1, le trois-quarts était à peine tourné, presque de face. Cette fois, on joint la vue trois-quarts droite de sa rotation (`references/trois-quarts-droit_v1.png`) pour donner l'angle ; l'image maître est déjà dans la conversation. Découpe : `--emotions 1` (les fichiers prennent le préfixe `trois-quarts_`).

```
Make an expression sheet of Sky, in a three-quarter view: a regular grid of 3 columns and 2 rows, landscape format (1536×1024), six equal cells. The attached image is the three-quarter view from his turnaround sheet: use it for the angle. In each cell, the same head-and-shoulders bust at exactly that angle, turned as much as in the attached image (his face turned toward the right of the image, his right ear visible on the left, his blue right eye nearer to us, his blind left eye farther away), same framing, same pose, same light. Keep him exactly as in his master image. Only his facial expression changes; his hands may enter the frame only when the expression needs them. Each expression must be clearly different from the others: avoid his usual tired, heavy-lidded, unimpressed look unless a cell asks for it. In every cell his left eye stays blind: entirely milky white, with no iris and no pupil. Cells read left to right, then top to bottom:

1. Neutral: relaxed face, straight gaze, mouth closed.
2. Joy: a broad, genuine smile showing his upper teeth, cheeks pushed up, eyes crinkled with laugh lines. Both corners of the mouth rise.
3. Sadness: inner ends of the eyebrows raised, heavy eyelids, corners of the mouth turned down.
4. Anger: eyebrows drawn down and together, a hard stare, jaw clenched, lips pressed.
5. Fear: eyebrows raised and pulled together, his right eye wide open, mouth stretched back.
6. Surprise: eyebrows high and rounded, eyes wide, mouth open in an O.

His glasses keep their thin gold-plated frame and their double bridge (a thin straight bar between the tops of the lenses, above the nose bridge). No text or labels anywhere.
```

Résultat, le 2026-10-15 : bonne du premier coup. Un vrai trois-quarts cette fois, l'oreille droite visible, l'œil bleu devant, l'œil aveugle blanc au fond. Joindre la vue de la rotation a suffi.

## Prompt K2 — Palette de trois-quarts, planche 2 : les universelles, suite, et leurs pics

Joins la même vue trois-quarts droite de la rotation. Découpe : `--emotions 2`.

```
Make an expression sheet of Sky, in a three-quarter view: a regular grid of 3 columns and 2 rows, landscape format (1536×1024), six equal cells. The attached image is the three-quarter view from his turnaround sheet: use it for the angle. In each cell, the same head-and-shoulders bust at exactly that angle, as in your last sheet (his face turned toward the right of the image, his right ear visible on the left, his blue right eye nearer to us, his blind left eye farther away), same framing, same pose, same light. Keep him exactly as in his master image. Only his facial expression changes; his hands may enter the frame only when the expression needs them. Each expression must be clearly different from the others: avoid his usual tired, heavy-lidded, unimpressed look unless a cell asks for it. In every cell his left eye stays blind: entirely milky white, with no iris and no pupil. Cells read left to right, then top to bottom:

1. Disgust: wrinkled nose, upper lip raised.
2. Contempt: only one corner of the mouth raised, on HIS RIGHT side, the side of his blue eye, nearer to us; the other corner stays flat. Looking down his nose at someone.
3. Laughter: mouth wide open, both eyes squeezed nearly shut (the blind one too, not a wink), head tilted back.
4. Crying: tears running down, distressed eyebrows, trembling mouth.
5. Rage: eyebrows very low, teeth clenched or a shouting mouth, an anime anger vein on the temple.
6. Terror: his blue right eye bulging with a tiny pupil, mouth open, the face drained pale.

His glasses keep their thin gold-plated frame and their double bridge (a thin straight bar between the tops of the lenses, above the nose bridge). No text or labels anywhere.
```

Résultat, le 2026-10-15 : bonne, sauf le rire : l'œil bleu se ferme, l'aveugle reste ouvert au fond, on lit un clin d'œil. Il ira dans une retouche à la fin de la palette, avec les autres cases à corriger. Le mépris est du bon côté, celui de l'œil bleu.

## Prompt K3 — Palette de trois-quarts, planche 3 : l'esprit

Joins la même vue trois-quarts droite de la rotation. Pour le doute et la méfiance, il regarde de côté : le prompt redit que l'œil aveugle reste blanc (au feu vert, il avait pris un iris). Découpe : `--emotions 3`.

```
Make an expression sheet of Sky, in a three-quarter view: a regular grid of 3 columns and 2 rows, landscape format (1536×1024), six equal cells. The attached image is the three-quarter view from his turnaround sheet: use it for the angle. In each cell, the same head-and-shoulders bust at exactly that angle, as in your last sheet (his face turned toward the right of the image, his right ear visible on the left, his blue right eye nearer to us, his blind left eye farther away), same framing, same pose, same light. Keep him exactly as in his master image. Only his facial expression changes; his hands may enter the frame only when the expression needs them. Each expression must be clearly different from the others: avoid his usual tired, heavy-lidded, unimpressed look unless a cell asks for it. In every cell his left eye stays blind: entirely milky white, with no iris and no pupil. Cells read left to right, then top to bottom:

1. Shock: far stronger than surprise. Jaw dropped all the way down, mouth hanging open in a tall oval, a tiny pupil in his blue right eye, the whole face frozen.
2. Interest: head slightly tilted, eyebrows slightly raised, an attentive gaze.
3. Concentration: calm focus. Eyes looking down at a laptop screen just below the frame, brows slightly knit, lips pressed. Not angry, not looking at the viewer.
4. Confusion: the eyebrow above his blue eye (nearer to us) raised higher than the other one, head tilted, a crooked mouth.
5. Doubt: the eyebrow above his blue eye (nearer to us) clearly raised, the other one stays low, pursed lips, a sideways glance of his blue eye; his blind eye stays entirely white.
6. Suspicion: narrowed eyes, a sideways look of his blue eye, chin tucked in; his blind eye stays entirely white.

His glasses keep their thin gold-plated frame and their double bridge (a thin straight bar between the tops of the lenses, above the nose bridge). No text or labels anywhere.
```

Résultat, le 2026-10-15 : bonne du premier coup. La confusion et le doute lèvent le sourcil de l'œil bleu, l'œil aveugle reste blanc quand il regarde de côté.

## Prompt K4 — Palette de trois-quarts, planche 4 : les émotions sociales

Joins la même vue trois-quarts droite de la rotation. La main de la gêne est la droite, avec la bague. Découpe : `--emotions 4`.

```
Make an expression sheet of Sky, in a three-quarter view: a regular grid of 3 columns and 2 rows, landscape format (1536×1024), six equal cells. The attached image is the three-quarter view from his turnaround sheet: use it for the angle. In each cell, the same head-and-shoulders bust at exactly that angle, as in your last sheet (his face turned toward the right of the image, his right ear visible on the left, his blue right eye nearer to us, his blind left eye farther away), same framing, same pose, same light. Keep him exactly as in his master image. Only his facial expression changes; his hands may enter the frame only when the expression needs them. Each expression must be clearly different from the others: avoid his usual tired, heavy-lidded, unimpressed look unless a cell asks for it. In every cell his left eye stays blind: entirely milky white, with no iris and no pupil. Cells read left to right, then top to bottom:

1. Embarrassment: a forced smile, eyes escaping downward, red cheeks, his right hand rubbing the back of his neck, the bronze ring on its little finger.
2. Shame: head down, eyes on the floor, shoulders hunched.
3. Pride: head high, chin up, a slight smile, chest out.
4. Jealousy: a side-eye of his blue eye, clenched jaw, low eyebrows; his blind eye stays entirely white.
5. Tenderness: a soft gaze, relaxed eyelids, a light warm smile.
6. Craving: staring hungrily at a chicken wrap on the table just below the frame, eyes locked on it, lips parted, a drop of drool at the corner of his mouth. Hunger, not nostalgia.

His glasses keep their thin gold-plated frame and their double bridge (a thin straight bar between the tops of the lenses, above the nose bridge). No text or labels anywhere.
```

Résultat, le 2026-10-15 : bonne du premier coup. La gêne a la main droite sur la nuque, avec la bague, et les joues rouges ; pour le désir, ChatGPT a dessiné la galette dans le cadre, et il bave.

## Prompt K5 — Palette de trois-quarts, planche 5 : les nuances

Joins la même vue trois-quarts droite de la rotation. Le contentement et le soulagement ferment les deux yeux : de trois-quarts, l'œil aveugle risque de rester ouvert, comme au rire de la planche 2 ; s'il le reste, la case ira dans la retouche de la fin. Découpe : `--emotions 5`.

```
Make an expression sheet of Sky, in a three-quarter view: a regular grid of 3 columns and 2 rows, landscape format (1536×1024), six equal cells. The attached image is the three-quarter view from his turnaround sheet: use it for the angle. In each cell, the same head-and-shoulders bust at exactly that angle, as in your last sheet (his face turned toward the right of the image, his right ear visible on the left, his blue right eye nearer to us, his blind left eye farther away), same framing, same pose, same light. Keep him exactly as in his master image. Only his facial expression changes; his hands may enter the frame only when the expression needs them. Each expression must be clearly different from the others: avoid his usual tired, heavy-lidded, unimpressed look unless a cell asks for it. In every cell his left eye stays blind: entirely milky white, with no iris and no pupil. Cells read left to right, then top to bottom:

1. Contentment: both eyes gently closed (the blind one too, not a wink), a small peaceful smile, a relaxed face.
2. Relief: both eyes closed (the blind one too, not a wink), head tilted back, mouth open in a big sigh, as if saying "phew", shoulders dropping, a small anime sweat drop on his temple.
3. Elation: a beaming open-mouthed smile, eyebrows high, overflowing joy.
4. Triumph: a big open-mouthed grin, chin up, his right fist clenched and raised in the frame, the bronze ring on its little finger.
5. Wonder: looking up at something above the frame, his blue right eye shining, lips parted in a faint smile, eyebrows raised. No shock, no fear.
6. Disappointment: a pout, eyes lowered, inner brows slightly raised.

His glasses keep their thin gold-plated frame and their double bridge (a thin straight bar between the tops of the lenses, above the nose bridge). No text or labels anywhere.
```

Résultat, le 2026-10-15 : bonne, sauf deux cases. Le contentement ferme bien les deux yeux, mais le soulagement laisse l'œil aveugle ouvert. Au triomphe, ChatGPT a mis une grosse chevalière gravée, à l'index, au lieu de la bague fine à l'auriculaire. Les deux iront dans la retouche de la fin.

## Prompt K6 — Palette de trois-quarts, planche 6 : l'humeur et le corps

Joins la même vue trois-quarts droite de la rotation. La malice se met de son côté gauche, celui de l'œil aveugle, au fond : c'est là qu'elle est de face (ChatGPT l'y remettait à chaque essai), et le côté d'une expression ne doit pas changer d'un plan à l'autre. Les mains portent la bague fine, à l'auriculaire. Découpe : `--emotions 6`.

```
Make an expression sheet of Sky, in a three-quarter view: a regular grid of 3 columns and 2 rows, landscape format (1536×1024), six equal cells. The attached image is the three-quarter view from his turnaround sheet: use it for the angle. In each cell, the same head-and-shoulders bust at exactly that angle, as in your last sheet (his face turned toward the right of the image, his right ear visible on the left, his blue right eye nearer to us, his blind left eye farther away), same framing, same pose, same light. Keep him exactly as in his master image. Only his facial expression changes; his hands may enter the frame only when the expression needs them. Each expression must be clearly different from the others: avoid his usual tired, heavy-lidded, unimpressed look unless a cell asks for it. In every cell his left eye stays blind: entirely milky white, with no iris and no pupil. Cells read left to right, then top to bottom:

1. Worry: eyebrows raised and pulled together, a tense mouth.
2. Annoyance: furrowed brows, rolling his blue eye upward, sighing; his blind eye stays entirely white.
3. Mischief: a playful, teasing grin rising on HIS LEFT side (the side of his blind eye, farther from us) and showing a little of his teeth, the eyebrow above his blind eye arched high. Warm and cheeky, not cold.
4. Boredom: heavy eyelids, head resting on his right hand, an empty gaze. His only ring is a thin plain bronze band on the little finger of that hand.
5. Tiredness: both eyes half closed (the blind one too), a big yawn, his right hand rising toward his mouth. His only ring is a thin plain bronze band on its little finger.
6. Pain: both eyes squeezed shut (the blind one too, not a wink), clenched teeth, a grimace.

His glasses keep their thin gold-plated frame and their double bridge (a thin straight bar between the tops of the lenses, above the nose bridge). No text or labels anywhere.
```

Résultat, le 2026-10-15 : bonne. La malice est de son côté gauche, comme de face. La douleur ferme les deux yeux. Mais à la fatigue, ChatGPT a mis deux bagues, malgré « his only ring ». À l'ennui, la bague fine semble à l'index ou au majeur : gardé, le détail est trop fin pour une retouche fiable.

## Prompt K7 — La retouche de trois-quarts

Les quatre cases à corriger, assemblées par Claude en un carré : `<sorties_root>/persos/sky/trois-quarts_retouche_a-retoucher.png`, dans l'ordre rire (K2), soulagement (K5), triomphe (K5), fatigue (K6). Joins cette image seule, dans le même message, sans l'image maître. Découpe : `--noms rire,soulagement,triomphe,fatigue` (le préfixe `trois-quarts_` s'ajoute tout seul) ; les fichiers sortent en `_v2`.

```
Edit ONLY the image attached to this message. It is a sheet of four of Sky's expressions in a three-quarter view. Keep everything exactly as it is (faces, expressions, mouths, hands, framing, colors, glasses, grid, white gaps), except these details:
1. Cell 1 (top left): his blue eye is closed, but his blind eye (the milky white one, farther away, on the right of his face) was left open. Close it the same way as his blue eye: a shut eyelid, no white visible.
2. Cell 2 (top right): the same: close his blind eye like his blue eye, no white visible.
3. Cell 3 (bottom left): replace the big engraved ring with a thin plain bronze band, worn on his little finger.
4. Cell 4 (bottom right): he wears only one ring: keep a single thin plain bronze band, on his little finger, and remove the other ring.
When Sky closes his eyes, the eyelid of his blind eye closes too: this is the only exception to the blind-eye rule. No text or labels anywhere.
```

Résultat, le 2026-10-15 : trois cases sur quatre. Le rire et le soulagement ferment l'œil aveugle, la fatigue ne garde qu'une bague (et ferme les deux yeux). Le triomphe a une bague fine, mais la retouche lui a fermé l'œil aveugle alors que l'œil bleu reste ouvert : un clin d'œil. On garde sa v1 ; sa chevalière se corrigera au passage local, avec la bague de l'ennui.

Sky est fini côté ChatGPT : les 50 cases de son inventaire.

## La série en pied et en gestes, pour le LoRA v2

Le test du LoRA v1 (le 2026-10-15) a montré le trou du jeu : une seule image en pied, alors le LoRA n'apprend que le buste et invente le reste de la tenue. Ces cinq planches le comblent, toutes sur le fond gris clair des autres (pas de blanc : l'outil de découpe repère les cases par leurs fines bandes blanches). Pas de décor : en production, Sky est intégré dans nos propres fonds. Dans la conversation de la série 2 ; si elle est perdue, refaire d'abord le prompt B avec l'image maître v3.

### Prompt L1 — En pied, de face et de trois-quarts

Joins l'image maître v3. Découpe : `--noms pied-face,pied-trois-quarts-gauche,pied-trois-quarts-droit --dossier references`.

```
Make a full-body sheet of Sky: a regular grid of 3 columns and 1 row, landscape format (1536×1024), three equal tall cells separated by thin white gaps. In each cell, Sky stands full body from head to feet, neutral expression, arms relaxed, same scale, same light, plain light-grey background. His usual outfit, exactly as in his master image: the white long-sleeved shirt with the sparse black-and-white lily pattern, sleeves pushed up just below the elbows, open only at the top of the chest, no underwear visible; both necklaces; black tracksuit trousers in a soft matte fabric, no logo, no stripes; black sneakers. His only ring is a thin plain bronze band on his right little finger. His glasses keep their thin gold-plated frame and their double bridge (a thin straight bar between the tops of the lenses). His left eye stays blind: entirely milky white, with no iris and no pupil. Cells, left to right:

1. Front view.
2. Three-quarter view showing HIS LEFT side (the blind eye side).
3. Three-quarter view showing HIS RIGHT side (the blue eye side).

No text or labels anywhere.
```

### Prompt L2 — En pied, de profil et de dos

Joins l'image maître v3. Découpe : `--noms pied-profil-gauche,pied-profil-droit,pied-dos --dossier references`.

```
Make a full-body sheet of Sky: a regular grid of 3 columns and 1 row, landscape format (1536×1024), three equal tall cells separated by thin white gaps. In each cell, Sky stands full body from head to feet, neutral expression, arms relaxed, same scale, same light, plain light-grey background. His usual outfit, exactly as in his master image: the white long-sleeved shirt with the sparse black-and-white lily pattern, sleeves pushed up just below the elbows, open only at the top of the chest, no underwear visible; both necklaces; black tracksuit trousers in a soft matte fabric, no logo, no stripes; black sneakers. His only ring is a thin plain bronze band on his right little finger. His glasses keep their thin gold-plated frame and their double bridge (a thin straight bar between the tops of the lenses). His left eye stays blind: entirely milky white, with no iris and no pupil. Cells, left to right:

1. Profile showing HIS LEFT side.
2. Profile showing HIS RIGHT side.
3. Back view.

No text or labels anywhere.
```

### Prompt L3 — Trois poses

Joins l'image maître v3. Découpe : `--noms assis-face,assis-cote,accoude --dossier references`.

```
Make a full-body sheet of Sky: a regular grid of 3 columns and 1 row, landscape format (1536×1024), three equal tall cells separated by thin white gaps. In each cell, Sky full body from head to feet, neutral expression, same scale, same light, plain light-grey background, no other furniture than the one named. His usual outfit, exactly as in his master image: the white long-sleeved shirt with the sparse black-and-white lily pattern, sleeves pushed up just below the elbows, open only at the top of the chest, no underwear visible; both necklaces; black tracksuit trousers in a soft matte fabric, no logo, no stripes; black sneakers. His only ring is a thin plain bronze band on his right little finger. His glasses keep their thin gold-plated frame and their double bridge (a thin straight bar between the tops of the lenses). His left eye stays blind: entirely milky white, with no iris and no pupil. Cells, left to right:

1. Sitting on a simple wooden chair, facing the viewer, forearms resting on his thighs.
2. Sitting on the same chair, seen from HIS RIGHT side.
3. Standing, leaning with his right elbow on a plain light-grey block at counter height.

No text or labels anywhere.
```

### Prompt L4 — Six gestes de face

Joins l'image maître v3. Découpe : `--noms mange,boit,bouche-pleine,telephone,ecrit-marqueur,laptop --dossier gestes`.

```
Make a sheet of Sky's gestures: a regular grid of 3 columns and 2 rows, landscape format (1536×1024), six equal cells separated by thin white gaps. In each cell, Sky from the waist up, facing the viewer, same framing, same light, plain light-grey background. Only his pose and his hands change; his face keeps his usual calm look unless a cell asks otherwise. His usual outfit, exactly as in his master image: the white long-sleeved shirt with the sparse black-and-white lily pattern, sleeves pushed up just below the elbows, open only at the top of the chest, no underwear visible; both necklaces; black tracksuit trousers in a soft matte fabric, no logo, no stripes; black sneakers. His only ring is a thin plain bronze band on his right little finger. His glasses keep their thin gold-plated frame and their double bridge (a thin straight bar between the tops of the lenses). His left eye stays blind: entirely milky white, with no iris and no pupil. Cells read left to right, then top to bottom:

1. Biting into a chicken wrap held in both hands.
2. Drinking from a bottle of orange soda, with no logo and no text on it.
3. Chewing with his mouth full, cheeks puffed, unimpressed.
4. Looking at a smartphone held in his right hand, the bronze ring visible.
5. Writing with a black marker on a transparent glass pane in front of him, his right hand raised.
6. Typing on a laptop set on a small plain table in front of him.

No text or labels anywhere.
```

### Prompt L5 — Les six gestes de trois-quarts

Joins la vue trois-quarts droite de la rotation (`references/trois-quarts-droit_v1.png`), pour l'angle. Découpe : la même que L4, le préfixe `trois-quarts_` s'ajoute tout seul.

```
Make a sheet of Sky's gestures: a regular grid of 3 columns and 2 rows, landscape format (1536×1024), six equal cells separated by thin white gaps. In each cell, Sky from the waist up, in a three-quarter view showing HIS RIGHT side, exactly at the angle of the attached image (his blue right eye nearer to us, his blind left eye farther away), same framing, same light, plain light-grey background. Only his pose and his hands change; his face keeps his usual calm look unless a cell asks otherwise. His usual outfit, exactly as in his master image: the white long-sleeved shirt with the sparse black-and-white lily pattern, sleeves pushed up just below the elbows, open only at the top of the chest, no underwear visible; both necklaces; black tracksuit trousers in a soft matte fabric, no logo, no stripes; black sneakers. His only ring is a thin plain bronze band on his right little finger. His glasses keep their thin gold-plated frame and their double bridge (a thin straight bar between the tops of the lenses). His left eye stays blind: entirely milky white, with no iris and no pupil. Cells read left to right, then top to bottom:

1. Biting into a chicken wrap held in both hands.
2. Drinking from a bottle of orange soda, with no logo and no text on it.
3. Chewing with his mouth full, cheeks puffed, unimpressed.
4. Looking at a smartphone held in his right hand, the bronze ring visible.
5. Writing with a black marker on a transparent glass pane in front of him, his right hand raised.
6. Typing on a laptop set on a small plain table in front of him.

No text or labels anywhere.
```

### La reprise : ce que Claude contrôle et fait après chaque planche

L'auteur demande un prompt à la fois (« donne-moi le prompt 1 de Sky ») et envoie l'image. Claude met l'image à joindre dans le presse-papiers (`setsid -f xclip -selection clipboard -t image/png -i <fichier>`) : l'image maître v3 pour L1 à L4 (`~/Téléchargements/sky_pour_L1-L4_image-maitre_v3.png`), la vue trois-quarts droite pour L5 (`~/Téléchargements/sky_pour_L5_trois-quarts-droit.png`). Puis, pour chaque planche reçue :

1. **Ranger** : copier l'image reçue en `planches/<nom>_v1.png` (`cp -n`), puis découper avec la commande du prompt (`python3 pipeline/decouper_planche.py image/persos/sky/planches/<nom>_v1.png --noms … --dossier …`). Les découpes d'essai se font d'abord dans le scratchpad.
2. **Contrôler en zoomant**, sur chaque case :
   - **l'œil aveugle** : son œil gauche est blanc laiteux, sans iris ni pupille, partout où il se voit. De face, il est à droite de l'image. L'œil bleu garde son reflet ;
   - **les lunettes** : la monture dorée fine, avec la barre du haut, sans taches sous les verres ni trait entre les sourcils ;
   - **la barbe de 3 jours** et les cernes ;
   - **la tenue** : la chemise blanche aux lys noirs et blancs (des lys, pas des fleurs de lys), manches sous le coude, ouverte en haut ; les deux colliers (le cordon de cuir serré, la chaîne et ses deux anneaux) ; le pantalon de training noir mat, sans bande ni logo ; les baskets noires ;
   - **la bague** : une seule, une bande fine en bronze, à l'auriculaire droit. Deux bagues et une chevalière à l'index sont déjà arrivées ;
   - **la carrure** : 1m87, 92 kg, les avant-bras épais aux veines visibles ;
   - aucun texte, le fond gris clair, les cases séparées.
   Et selon le prompt :
   - **L1** : les pieds entiers dans le cadre ; case 2, son côté gauche (l'œil aveugle devant) ; case 3, son côté droit (l'œil bleu devant).
   - **L2** : le profil gauche montre l'œil aveugle, le profil droit l'œil bleu ; le dos sans visage.
   - **L3** : une chaise en bois simple et rien d'autre ; accoudé du coude droit ; assis de côté, c'est son côté droit qu'on voit.
   - **L4** : la galette à deux mains, la bouteille sans logo, le téléphone et le marqueur dans la main droite, la bague visible ; des mains bien formées.
   - **L5** : un vrai trois-quarts, à l'angle de `references/trois-quarts-droit_v1.png`, l'œil bleu devant.
3. **Si une case rate** : la mettre dans une retouche, en assemblant les cases ratées (4 au plus) dans `<sorties_root>/persos/sky/`, avec une consigne écrite case par case, jamais une règle générale en fin de prompt (leçon du K7). L'image part dans le même message que le prompt, qui commence par « Edit ONLY the image attached to this message ».
4. **Noter** : la case de l'inventaire (Sky > En pied et en gestes), « faite » dans le tableau des prompts, `provenance.json` (la planche et ses cases ; les vues en pied et les poses comme des `references/` retenues ; les gestes dans une clé `gestes_retenus`), une ligne au journal. Push à la fin de la série, ou quand l'auteur le demande.

### Après les cinq planches : le LoRA v2

1. Libérer la carte (`~/venvs/kebab/bin/python pipeline/comfyui.py arreter`), puis préparer le jeu : `MIOPEN_FIND_MODE=TRUST_VERIFY_FULL ~/venvs/kebab/bin/python pipeline/preparer_lora.py sky v2`. Environ 130 images, avec le tag `heterochromia` là où les deux yeux sont ouverts (`fiche.json` > `lora` > `tag_yeux`).
2. Envoyer le jeu à Kaggle en un seul zip (fichier par fichier, ça va à 45 Ko/s) : `zip -0 -r jeu_v2.zip .` dans le dossier du jeu, le zip seul dans un dossier avec un `dataset-metadata.json` (`skyzer/kebab-lora-sky-jeu-v2`), puis `~/venvs/kaggle/bin/kaggle datasets create -p <ce dossier>`. Attendre `kaggle datasets status` → `ready`.
3. Lancer : `~/venvs/kaggle/bin/kaggle kernels push -p pipeline/kaggle/lora_sky_v2 --accelerator NvidiaTeslaT4`, environ 1 h 15. Suivre avec `kaggle kernels status`, et la progression avec `kaggle kernels logs -f` (la barre de kohya y passe).
4. Récupérer : `kaggle kernels output skyzer/kebab-lora-sky-v2 -p <sorties_root>/lora/sky/kaggle_v2`, puis copier les `.safetensors` dans `<modeles_root>/loras/`.
5. Tester : `pipeline/comfyui.py demarrer`, puis `pipeline/test_lora.py sky sky_v2.safetensors` (environ 25 min, le LoRA en mode bypass). Comparer la planche avec celle de la v1, l'œil aveugle et la tenue en premier, et noter le résultat au journal et au plan.
