from .celery import celery
from pathlib import Path
from PIL import Image


@celery.task
def process_pic(
    path: str,
):
    img_path = Path(path)
    img = Image.open(img_path)

    img_huge_resized = img.resize((1000, 500))
    img_small_resized = img.resize((200, 100))

    img_huge_resized.save(f"app/static/images/huge_resized_{img_path.name}")
    img_small_resized.save(f"app/static/images/small_resized_{img_path.name}")
