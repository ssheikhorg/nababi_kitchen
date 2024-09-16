from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet


class MenuPage(Page):
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    description = models.TextField(blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('price'),
        FieldPanel('description'),
        FieldPanel('image'),
    ]

    # def get_context(self, request):
    #     context = super().get_context(request)
    #     context['menu_items'] = self.menu_items.all()
    #     return context
