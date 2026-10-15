# La palette des émotions

La fiche globale : les mêmes 36 émotions pour tous les persos, en 6 planches de 6. Elle couvre les expressions du visage que la recherche retrouve partout dans le monde, plus les états dont une comédie a besoin.

## D'où vient la liste

- **Les 7 expressions universelles d'Ekman** : joie, tristesse, colère, peur, surprise, dégoût, mépris.
- **Les 16 expressions de l'étude de Cowen et Keltner**, retrouvées dans 6 millions de vidéos de 144 pays (Nature, publiée en ligne en décembre 2020, vérifié le 2026-10-13) : amusement, colère, émerveillement, concentration, confusion, mépris, contentement, désir, déception, doute, exaltation, intérêt, douleur, tristesse, surprise, triomphe.
- **Les émotions sociales qui ont une expression propre** : gêne, honte, fierté.
- **Les pics**, pour que l'émotion se lise à l'écran : rire, pleurs, rage, terreur, stupeur.
- **Les états dont la série a besoin** : neutre, méfiance, jalousie, tendresse, soulagement, inquiétude, agacement, malice, ennui, fatigue.

Certaines émotions n'ont pas de case, parce qu'aucune expression du visage ne leur est propre. On les joue avec la plus proche, et le contexte fait le reste :
- la culpabilité : la honte ;
- l'espoir : l'intérêt ;
- la nostalgie : une tristesse légère, le regard au loin ;
- la gratitude et la compassion : la tendresse.

## Comment faire une planche

- Une grille de 3 colonnes sur 2 rangées, au format paysage (1536 × 1024 dans ChatGPT).
- Le même buste dans chaque case, de face, avec le même fond neutre et la même lumière. Sky a aussi une série de trois-quarts.
- Les cases se lisent de gauche à droite, puis de haut en bas, dans l'ordre des tableaux ci-dessous.
- Aucun texte, pas même le nom de l'émotion.
- La planche se range dans `persos/<slug>/planches/emotions-<n>_v1.png`. Claude la découpe en `expressions/<fichier>_v1.png`. De trois-quarts, les deux noms prennent le préfixe `trois-quarts_`.
- Si une case rate, on refait cette émotion seule, dans le même cadrage.

## Les 6 planches

### Planche 1 — Les universelles

| Case | Émotion | Fichier | Ce qui la rend lisible |
|---|---|---|---|
| 1 | Neutre | `neutre` | Visage détendu, regard droit, bouche fermée |
| 2 | Joie | `joie` | Le vrai sourire : joues remontées, yeux plissés |
| 3 | Tristesse | `tristesse` | Intérieur des sourcils relevé, paupières lourdes, coins de la bouche vers le bas |
| 4 | Colère | `colere` | Sourcils froncés et bas, regard dur, lèvres serrées |
| 5 | Peur | `peur` | Sourcils relevés et rapprochés, yeux grands ouverts, bouche tirée vers l'arrière |
| 6 | Surprise | `surprise` | Sourcils hauts et arrondis, yeux ronds, bouche ouverte |

### Planche 2 — Les universelles, suite, et leurs pics

| Case | Émotion | Fichier | Ce qui la rend lisible |
|---|---|---|---|
| 1 | Dégoût | `degout` | Nez plissé, lèvre du haut relevée |
| 2 | Mépris | `mepris` | Un seul coin de la bouche relevé, regard de haut |
| 3 | Rire | `rire` | Bouche grande ouverte, yeux fermés ou plissés, tête en arrière |
| 4 | Pleurs | `pleurs` | Larmes, sourcils en détresse, bouche qui tremble |
| 5 | Rage | `rage` | Sourcils très bas, dents serrées ou bouche qui crie, veine sur la tempe |
| 6 | Terreur | `terreur` | Yeux exorbités, pupilles minuscules, bouche ouverte, teint blême |

### Planche 3 — L'esprit

| Case | Émotion | Fichier | Ce qui la rend lisible |
|---|---|---|---|
| 1 | Stupeur | `stupeur` | Mâchoire qui tombe, yeux ronds et figés : le choc |
| 2 | Intérêt | `interet` | Tête un peu penchée, sourcils légèrement relevés, regard attentif |
| 3 | Concentration | `concentration` | Sourcils un peu froncés, regard fixe, lèvres pincées |
| 4 | Confusion | `confusion` | Un sourcil plus haut que l'autre, tête penchée, bouche de travers |
| 5 | Doute | `doute` | Un sourcil levé, lèvres pincées, regard de côté |
| 6 | Méfiance | `mefiance` | Yeux plissés, regard en coin, menton rentré |

### Planche 4 — Les émotions sociales

| Case | Émotion | Fichier | Ce qui la rend lisible |
|---|---|---|---|
| 1 | Gêne | `gene` | Sourire contraint, regard qui fuit vers le bas, joues rouges |
| 2 | Honte | `honte` | Tête baissée, regard au sol, épaules rentrées |
| 3 | Fierté | `fierte` | Tête haute, menton levé, léger sourire, buste droit |
| 4 | Jalousie | `jalousie` | Regard en coin, mâchoire serrée, sourcils bas |
| 5 | Tendresse | `tendresse` | Regard doux, paupières détendues, sourire léger |
| 6 | Désir | `desir` | Regard appuyé, paupières mi-closes, lèvres entrouvertes : l'envie d'une galette ou d'une personne |

### Planche 5 — Les nuances

| Case | Émotion | Fichier | Ce qui la rend lisible |
|---|---|---|---|
| 1 | Contentement | `contentement` | Petit sourire calme, yeux fermés ou mi-clos, visage détendu |
| 2 | Soulagement | `soulagement` | Il expire, yeux fermés, épaules qui tombent, demi-sourire |
| 3 | Exaltation | `exaltation` | Grand sourire, yeux brillants, sourcils hauts : la joie qui déborde |
| 4 | Triomphe | `triomphe` | Grand sourire bouche ouverte, menton levé, poing serré |
| 5 | Émerveillement | `emerveillement` | Yeux grands ouverts, bouche entrouverte, sourcils levés, sans peur |
| 6 | Déception | `deception` | Moue, regard baissé, intérieur des sourcils un peu relevé |

### Planche 6 — L'humeur et le corps

| Case | Émotion | Fichier | Ce qui la rend lisible |
|---|---|---|---|
| 1 | Inquiétude | `inquietude` | Sourcils relevés et rapprochés, lèvre mordue ou bouche crispée |
| 2 | Agacement | `agacement` | Sourcils froncés, yeux au ciel ou mi-clos, soupir |
| 3 | Malice | `malice` | Sourire en coin, un sourcil levé, regard complice |
| 4 | Ennui | `ennui` | Paupières lourdes, tête appuyée sur la main, regard vide |
| 5 | Fatigue | `fatigue` | Yeux cernés et mi-clos, bâillement possible |
| 6 | Douleur | `douleur` | Yeux serrés, dents serrées, grimace |

## Le jeu de chaque perso

- **La même palette pour tous, pas la même intensité.** La bible le dit : Patrick parle plus bas quand c'est important, Mohamed ne crie jamais et ne chuchote jamais, Nath reste plate, Daria devient froide sous pression. Chez eux, la rage reste froide et le rire reste court.
- **Sky garde le reflet de son œil droit sur toute la palette** (le gauche est aveugle). Seul « le sourire », une de ses signatures, l'éteint.
- **Les expressions asymétriques** (mépris, confusion, doute, malice) : le côté se fixe une fois par perso, comme ses détails asymétriques. Sinon, il change d'un plan à l'autre.
- **Le désir reste du sous-entendu**, comme le veut la bible : une envie de galette ou un regard appuyé, jamais plus.
- Les signatures restent à part : ce sont les moments propres à chaque perso, décrits dans sa fiche.

## Sources

- Ekman et Friesen (1986), « A new pan-cultural facial expression of emotion », *Motivation and Emotion* : le mépris, septième expression universelle.
- Cowen, Keltner et al. (2021), « Sixteen facial expressions occur in similar contexts worldwide », *Nature* 589 : https://research.google/pubs/sixteen-facial-expressions-occur-in-similar-contexts-worldwide/
- Keltner (1995), sur les expressions de la gêne et de la honte, et Tracy et Robins (2004), sur celle de la fierté.
