from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator


class WebPage(models.Model):
    feed_name = models.CharField(
        max_length=50,
        unique=True,
        validators=[RegexValidator(regex="[\w\-]+")]
    )
    url = models.URLField()
    selector = models.TextField()
    interval = models.PositiveIntegerField(default=5)
    max_results = models.PositiveIntegerField(default=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_on", "-created_on"]

    def __str__(self):
        return "{0} - {1}".format(self.url, self.selector)


class PageScrapeResult(models.Model):
    page = models.ForeignKey(WebPage)
    output = models.TextField(null=True)
    hash = models.TextField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_on", "-created_on"]

    def __str__(self):
        return "{0} - {1}".format(self.page.url, self.updated_on)
