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
        pool = multiprocessing.Pool(multiprocessing.cpu_count())
        today = int(datetime.date.today().strftime("%s"))
        now = datetime.datetime.now()
        curr_time = int(now.strftime("%s")) - now.second
        mins_passed = int((curr_time - today) / 60.0)
        intervals = WebPage.objects.filter(interval__lte=mins_passed)\
                                   .values_list('interval', flat=True).\
                                   order_by('interval').distinct()
        for interval in intervals:
            if mins_passed % interval == 0 or settings.DEBUG:
                for page in WebPage.objects.filter(interval=interval):
                    pool.apply_async(scrape_url, (page, ))
        pool.close()
        pool.join()
