from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.template import Template, Context

from .models import WebPage, PageScrapeResult


class LatestEntriesFeed(Feed):
    def get_object(self, request, *args, **kwargs):
        feed_name = kwargs["feed_name"]
        self.page = WebPage.objects.get(feed_name=feed_name)
        return self.page

    def title(self):
        tmpl = Template(_("Latest updates for {{ obj.feed_name }} feed"))
        context = self.get_context_data(item=self.page)
        return tmpl.render(Context(context))

    def description(self):
        tmpl = Template(_("Latest updates for {{ obj.feed_name }} feed"))
        context = self.get_context_data(item=self.page)
        return tmpl.render(Context(context))

    def items(self):
        results = PageScrapeResult.objects.filter(page=self.page)
        return results.order_by('-updated_on')[:self.page.max_results]

    def link(self):
        return reverse("feed", kwargs={"feed_name": self.page.feed_name})

    def item_title(self, item):
        return self.page.feed_name

    def item_link(self, item):
        return self.link()

    def item_description(self, item):
        return item.output
