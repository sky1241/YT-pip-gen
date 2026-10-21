# Kebab Datastream : entraînement du LoRA de Sky (v4) sur Kaggle, avec kohya sd-scripts v0.12.0.
# v4 = la v3 (le même jeu, kebab-lora-sky-jeu-v3) sans min_snr_gamma : min_snr 5 affaiblit les étapes de faible bruit, celles
# qui dessinent les textures fines comme la barbe (la recherche du 2026-10-21) ; une seule chose change.
# Modèle de base : Animagine XL 4.0. Sans retournement horizontal (l'œil aveugle à sa gauche).
# Par rapport à la v2, d'après les recherches du 2026-10-21 (journal.md) : ses traits écrits dans les légendes (« mature male,
# facial hair, beard, stubble, bags under eyes ») ; le genre puis le déclencheur en tête, le reste mélangé à chaque passage
# (keep_tokens 2), 10 % des tags retirés au hasard ; un masque alpha par image (le fond à 15 %) ; ses images à petite tête
# reprises sans Real-ESRGAN et répétées plus (en pied × 3, gestes × 2, bustes × 1 : repetitions.json) ; 12 époques, chacune
# sauvegardée, des images d'essai au départ puis toutes les 3 époques. Les encodeurs de texte ne sont plus mis en cache :
# sd-scripts le refuse avec le mélange des tags. Plusieurs changements à la fois : la v3 dira si l'ensemble aide, pas lequel.
import json
import glob
import hashlib
import os
import subprocess
import time

DEBUT = time.time()
NOM = "sky_v4"
MODELE_URL = "https://huggingface.co/cagliostrolab/animagine-xl-4.0/resolve/main/animagine-xl-4.0.safetensors"
MODELE_SHA256 = "1d5b43ff75b6ab598502d4c779d2fbfa3dceca51c60c3b609640a60772333916"
MODELE = "/tmp/modele/animagine-xl-4.0.safetensors"
SCRIPTS = "/tmp/sd-scripts"
SORTIE = "/kaggle/working/lora"


def etape(titre):
    print(f"\n===== {titre} ({(time.time() - DEBUT) / 60:.1f} min) =====", flush=True)


def lancer(commande, **options):
    print("$", commande, flush=True)
    subprocess.run(commande, shell=True, check=True, **options)


etape("La carte")
lancer("nvidia-smi --query-gpu=name,memory.total --format=csv")
# Kaggle donne une T4 même quand on demande une P100 (tous les journaux précédents) : AdamW8bit comme la v2 sur une T4 ;
# AdamW ordinaire sur une P100 (bitsandbytes n'y est pas sûr)
CARTE = subprocess.run("nvidia-smi --query-gpu=name --format=csv,noheader", shell=True, capture_output=True, text=True).stdout
OPTIMISEUR = "AdamW" if "P100" in CARTE else "AdamW8bit"
print("carte :", CARTE.strip(), "; optimiseur :", OPTIMISEUR, flush=True)

etape("Les images")
legendes = glob.glob("/kaggle/input/**/*.txt", recursive=True)
if not legendes:
    # le jeu est envoyé en un seul zip : Kaggle ne l'a pas forcément décompressé
    archives = glob.glob("/kaggle/input/**/*.zip", recursive=True)
    assert archives, "ni légendes ni zip dans /kaggle/input"
    lancer(f"mkdir -p /tmp/jeu && unzip -q -o '{archives[0]}' -d /tmp/jeu")
    legendes = glob.glob("/tmp/jeu/**/*.txt", recursive=True)
assert legendes, "aucune légende trouvée"
dossiers = sorted({os.path.dirname(l) for l in legendes})
racine = os.path.dirname(dossiers[0]) if len(dossiers) > 1 else dossiers[0]
repetitions = {}
for r in glob.glob(os.path.join(racine, "**", "repetitions.json"), recursive=True):
    repetitions = json.load(open(r))
if racine.startswith("/kaggle/input"):
    # /kaggle/input est en lecture seule, et kohya écrit le cache des latents à côté des images
    for d in dossiers:
        lancer(f"mkdir -p /tmp/jeu/{os.path.basename(d)} && cp '{d}'/*.png '{d}'/*.txt /tmp/jeu/{os.path.basename(d)}/")
    dossiers = [f"/tmp/jeu/{os.path.basename(d)}" for d in dossiers]
sous_ensembles = []
for d in dossiers:
    images = glob.glob(os.path.join(d, "*.png"))
    assert images and len(images) == len(glob.glob(os.path.join(d, "*.txt"))), d
    n = repetitions[os.path.basename(d)]
    print(d, len(images), "images ×", n, "répétitions", flush=True)
    sous_ensembles.append(f"""
  [[datasets.subsets]]
  image_dir = "{d}"
  num_repeats = {n}
  alpha_mask = true
""")
assert {os.path.basename(d) for d in dossiers} == set(repetitions), (dossiers, repetitions)

etape("kohya sd-scripts v0.12.0")
lancer(f"git clone -q --depth 1 --branch v0.12.0 https://github.com/kohya-ss/sd-scripts {SCRIPTS}")
lancer("pip install -q -r requirements.txt", cwd=SCRIPTS)

etape("Le modèle de base")
os.makedirs(os.path.dirname(MODELE), exist_ok=True)
lancer(f"curl -sL --fail -o {MODELE} {MODELE_URL}")
h = hashlib.sha256()
with open(MODELE, "rb") as f:
    for bloc in iter(lambda: f.read(1 << 24), b""):
        h.update(bloc)
assert h.hexdigest() == MODELE_SHA256, "empreinte du modèle différente"
print("empreinte vérifiée", flush=True)

etape("La configuration")
with open("/tmp/jeu.toml", "w") as f:
    f.write(f"""[general]
shuffle_caption = true
caption_extension = ".txt"
keep_tokens = 2
caption_tag_dropout_rate = 0.1
enable_bucket = true
bucket_no_upscale = true

[[datasets]]
resolution = 1024
batch_size = 1
min_bucket_reso = 512
max_bucket_reso = 1536
bucket_reso_steps = 64
{''.join(sous_ensembles)}""")

etape("Les images d'essai")
NEGATIF = ("lowres, bad anatomy, bad hands, text, error, missing finger, extra digits, fewer digits, cropped, worst quality, "
           "low quality, low score, bad score, average score, signature, watermark, username, blurry")
QUALITE = "masterpiece, high score, great score, absurdres"
DEBUT_PROMPT = "1boy, skykebab, solo, male focus"
ESSAIS = [
    (f"{DEBUT_PROMPT}, mature male, facial hair, beard, stubble, bags under eyes, heterochromia, portrait, close-up, three-quarter view, facing right, "
     f"expressionless, simple background, grey background, {QUALITE}", 1024, 1024, 2001),
    (f"{DEBUT_PROMPT}, heterochromia, portrait, close-up, three-quarter view, facing right, expressionless, simple background, "
     f"grey background, {QUALITE}", 1024, 1024, 2001),
    (f"{DEBUT_PROMPT}, mature male, facial hair, beard, stubble, bags under eyes, heterochromia, white shirt, leaf print, cowboy shot, three-quarter "
     f"view, facing right, eating, biting, holding burrito with both hands, burrito, sitting, booth, table, indoors, restaurant, "
     f"warm lighting, {QUALITE}", 1024, 1024, 2002),
    (f"{DEBUT_PROMPT}, mature male, facial hair, beard, stubble, bags under eyes, heterochromia, white shirt, leaf print, black pants, sweatpants, "
     f"black sneakers, full body, standing, facing viewer, simple background, grey background, {QUALITE}", 832, 1216, 2003),
    # la tête petite, dans un restaurant : là où la v2 perdait ses traits
    (f"{DEBUT_PROMPT}, mature male, facial hair, beard, stubble, bags under eyes, white shirt, leaf print, wide shot, full body, "
     f"sitting, booth, table, indoors, restaurant, warm lighting, {QUALITE}", 1216, 832, 2004),
]
with open("/tmp/essais.txt", "w") as f:
    for texte, w, h, graine in ESSAIS:
        f.write(f"{texte} --n {NEGATIF} --w {w} --h {h} --d {graine} --l 5 --s 25\n")
print(open("/tmp/essais.txt").read(), flush=True)

etape("L'entraînement")
lancer(" ".join([
    "accelerate launch --num_processes 1 --num_machines 1 --mixed_precision fp16 --dynamo_backend no",
    "sdxl_train_network.py",
    f"--pretrained_model_name_or_path {MODELE}",
    "--dataset_config /tmp/jeu.toml",
    f"--output_dir {SORTIE} --output_name {NOM}",
    "--save_model_as safetensors --save_precision fp16 --save_every_n_epochs 1",
    "--max_train_epochs 12",
    "--sample_prompts /tmp/essais.txt --sample_every_n_epochs 3 --sample_sampler euler_a --sample_at_first",
    "--network_module networks.lora --network_dim 32 --network_alpha 16",
    "--network_train_unet_only --learning_rate 1e-4 --unet_lr 1e-4",
    f"--optimizer_type {OPTIMISEUR} --lr_scheduler cosine --lr_warmup_steps 100",
    "--mixed_precision fp16 --no_half_vae --gradient_checkpointing --sdpa",
    "--cache_latents --cache_latents_to_disk",
    "--seed 42",
    "--max_data_loader_n_workers 2 --persistent_data_loader_workers",
]), cwd=SCRIPTS)

etape("Fini")
lancer(f"ls -la {SORTIE}")
