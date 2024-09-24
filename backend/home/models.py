from django.db import models

from .utils import resize_image


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

        # Check if an image exists
        if self.image:
            resize_image(self.image, 100, 100)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class FooterSettings(models.Model):
    site_name = models.CharField(max_length=255, default="CaterServ")
    description = models.TextField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.site_name


class SpecialFacility(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Special Facilities'


class ContactInfo(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    service_hours = models.CharField(max_length=100)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name_plural = 'Contact Information'


class SocialGalleryImage(models.Model):
    image = models.ImageField(upload_to='social_gallery')

    def save(self, *args, **kwargs) -> None:
        if self.image:
            resize_image(self.image, 100, 100)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Social Gallery Images'


class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    image = models.ImageField(upload_to='about_us')
    description = models.TextField()

    # Additional dynamic sections
    feature_1 = models.CharField(max_length=255, blank=True, null=True)
    feature_2 = models.CharField(max_length=255, blank=True, null=True)
    feature_3 = models.CharField(max_length=255, blank=True, null=True)
    feature_4 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "About Us Content"
        verbose_name_plural = "About Us Content"

    def __str__(self):
        return self.title
