from django.contrib import admin

from .models import MenuItem, MenuCategory


admin.site.register(MenuCategory)
admin.site.register(MenuItem)
