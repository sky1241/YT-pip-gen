# Kebab Datastream

Mini-série anime en français (style années 90, entre *Chihiro* et *Evangelion*),
comédie de dialogue qui fait passer de vraies notions de science, business et
géopolitique. Diffusion YouTube, un épisode de 15-20 min par semaine.

Ce repo est la **table de référence** : tout ce qui sert à générer (écriture,
fiches persos, images de référence, workflows, code du pipeline). Tout ce qui est
**généré ou lourd** (variantes, clips, voix, montages, poids de modèles) vit sur le
disque externe, hors git.

## Par où commencer

- **[CLAUDE.md](CLAUDE.md)** — les règles : rôles, contenu, workflow d'une scène, stack, conventions de fichiers.
- **[PLAN.md](PLAN.md)** — la checklist de l'épisode en cours (8 phases). C'est ce fichier qui fait foi.
- **[ecriture/canon.yaml](ecriture/canon.yaml)** — noms, lieux, âges + les points à trancher.
- **[ecriture/continuite.md](ecriture/continuite.md)** — l'anti-dérive, mis à jour à chaque épisode.

## Structure

```
ecriture/     bible, canon, continuité, brouillons, épisodes figés
image/        style, fiches persos, décors, explorations
audio/        voix par perso
production/   plans.json par scène (epNN/sNN/)
workflows/    workflows ComfyUI au format API
pipeline/     le code, une seule commande d'entrée
```

L'auteur écrit et valide. Claude pilote la production, ne réécrit jamais sans demande explicite.
