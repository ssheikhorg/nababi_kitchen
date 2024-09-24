from django.contrib import admin
from .models import (
    MenuItem, MenuCategory, FooterSettings, SpecialFacility, ContactInfo, SocialGalleryImage, AboutUs
)

admin.site.register(MenuCategory)
admin.site.register(MenuItem)
admin.site.register(FooterSettings)
admin.site.register(SpecialFacility)
admin.site.register(ContactInfo)
admin.site.register(SocialGalleryImage)
admin.site.register(AboutUs)
