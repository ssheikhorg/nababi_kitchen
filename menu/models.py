from django.db import models


class MenuCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Menu Categories'


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="media/menu")
    category = models.ForeignKey(MenuCategory, related_name="menu_item", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
