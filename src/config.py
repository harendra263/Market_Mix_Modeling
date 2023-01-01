import pathlib

BASE_DIR = pathlib.Path().resolve().parent
DATASET_DIR = BASE_DIR / "input"
DATASET_DIR.mkdir(exist_ok=True, parents=True)

IMAGE_DIR = BASE_DIR / "images"
IMAGE_DIR.mkdir(exist_ok=True, parents=True)
