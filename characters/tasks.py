from characters.scraper import sync_characters_with_api
from celery import shared_task


@shared_task
def sync_with_api():
    sync_characters_with_api()
