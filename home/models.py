from wagtail.models import Page


class HomePage(Page):
    pass


"""
from django.db import models
from wagtail.admin.panels import FieldPanel


class MenuItem(Page):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('price'),
        FieldPanel('description'),
        FieldPanel('image'),
    ]

"""