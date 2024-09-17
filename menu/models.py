from PIL import Image
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
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs) -> None:
        # create or update slug
        self.slug = self.name.replace(" ", "-").lower()
        super().save(*args, **kwargs)

        # open uploaded image
        img_path = self.image.path
        img = Image.open(img_path)

        width, height = img.size
        # resize image
        if width == 100 and height == 100:
            return
        target_size = (100, 100)
        img = img.resize(target_size)
        img.save(img_path)

    def __str__(self):
        return self.name
