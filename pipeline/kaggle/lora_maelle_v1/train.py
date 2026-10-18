# Kebab Datastream : entraînement du LoRA de Maëlle (v1) sur Kaggle, avec kohya sd-scripts v0.12.0.
# Modèle de base : Animagine XL 4.0. Sans retournement horizontal (le côté rasé et la cicatrice à sa gauche, la bague au pouce droit).
import glob
import hashlib
import os
import subprocess
import time

DEBUT = time.time()
NOM = "maelle_v1"
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

etape("Les images")
legendes = glob.glob("/kaggle/input/**/*.txt", recursive=True)
if not legendes:
    # le jeu est envoyé en un seul zip : Kaggle ne l'a pas forcément décompressé
    archives = glob.glob("/kaggle/input/**/*.zip", recursive=True)
    assert archives, "ni légendes ni zip dans /kaggle/input"
    lancer(f"mkdir -p /tmp/jeu && unzip -q -o '{archives[0]}' -d /tmp/jeu")
    legendes = glob.glob("/tmp/jeu/**/*.txt", recursive=True)
assert legendes, "aucune légende trouvée"
dossier_images = os.path.dirname(legendes[0])
if dossier_images.startswith("/kaggle/input"):
    # /kaggle/input est en lecture seule, et kohya écrit le cache des latents à côté des images
    lancer(f"mkdir -p /tmp/jeu && cp '{dossier_images}'/*.png '{dossier_images}'/*.txt /tmp/jeu/")
    dossier_images = "/tmp/jeu"
images = glob.glob(os.path.join(dossier_images, "*.png"))
print(dossier_images, len(images), "images,", len(glob.glob(os.path.join(dossier_images, "*.txt"))), "légendes", flush=True)
assert images and len(images) == len(glob.glob(os.path.join(dossier_images, "*.txt")))

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
shuffle_caption = false
caption_extension = ".txt"
keep_tokens = 1
enable_bucket = true
bucket_no_upscale = true

[[datasets]]
resolution = 1024
batch_size = 1
min_bucket_reso = 512
max_bucket_reso = 1536
bucket_reso_steps = 64

  [[datasets.subsets]]
  image_dir = "{dossier_images}"
  num_repeats = 3
""")

etape("L'entraînement")
lancer(" ".join([
    "accelerate launch --num_processes 1 --num_machines 1 --mixed_precision fp16 --dynamo_backend no",
    "sdxl_train_network.py",
    f"--pretrained_model_name_or_path {MODELE}",
    "--dataset_config /tmp/jeu.toml",
    f"--output_dir {SORTIE} --output_name {NOM}",
    "--save_model_as safetensors --save_precision fp16 --save_every_n_epochs 2",
    "--max_train_epochs 8",
    "--network_module networks.lora --network_dim 32 --network_alpha 16",
    "--network_train_unet_only --learning_rate 1e-4 --unet_lr 1e-4",
    "--optimizer_type AdamW8bit --lr_scheduler cosine --lr_warmup_steps 100",
    "--mixed_precision fp16 --no_half_vae --gradient_checkpointing --sdpa",
    "--cache_latents --cache_latents_to_disk --cache_text_encoder_outputs",
    "--min_snr_gamma 5 --seed 42",
    "--max_data_loader_n_workers 2 --persistent_data_loader_workers",
]), cwd=SCRIPTS)

etape("Fini")
lancer(f"ls -la {SORTIE}")
