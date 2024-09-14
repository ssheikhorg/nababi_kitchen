# restaurant/models.py
from django.db import models
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.models import Page
from wagtail.images.models import Image
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.snippets.models import register_snippet

class MenuItem(models.Model):
    menu = ParentalKey('MenuPage', related_name='menu_items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    panels = [
        FieldPanel('name'),
        FieldPanel('description'),
        FieldPanel('price'),
        FieldPanel('image'),
    ]

    def __str__(self):
        return self.name


class MenuPage(Page):
    introduction = models.TextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduction'),
        InlinePanel('menu_items', label="Menu Items"),
    ]
