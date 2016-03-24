from django.contrib import admin
from django.utils.text import mark_safe

from .models import WebPage, PageScrapeResult


class PageScrapeResultAdmin(admin.ModelAdmin):
    list_display = ["page_name", "updated_on", "link"]

    def page_name(self, obj):
        return obj.page.feed_name

    def link(self, obj):
        url = obj.page.url
        return mark_safe('<a href="{0}" target="_blank">{0}</a>'.format(url))


admin.site.register(WebPage)
admin.site.register(PageScrapeResult, PageScrapeResultAdmin)
