from django.contrib import admin

from .models import WebPage, PageScrapeResult


admin.site.register(WebPage)
admin.site.register(PageScrapeResult)
