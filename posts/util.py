from celery import shared_task
from easy_thumbnails.files import generate_all_aliases


@shared_task
def generate_responsive_images(post):
    generate_all_aliases(post.image, True)
    post.image_resized = True
    post.save()