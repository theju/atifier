import datetime
import multiprocessing

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from core.models import WebPage, PageScrapeResult
from core.views import scrape_url


class Command(BaseCommand):
    help = "Poll all the urls and scrape the results"
    can_import_settings = True

    def handle(self, *args, **options):
        pool = multiprocessing.Pool(multiprocessing.cpu_count() + 2)
        curr_min = datetime.datetime.now().minute
        for page in WebPage.objects.all():
            if curr_min % page.interval == 0 or settings.DEBUG:
                pool.apply_async(scrape_url, (page, ))
        pool.close()
        pool.join()
