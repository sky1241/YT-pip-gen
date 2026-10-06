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
