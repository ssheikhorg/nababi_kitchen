#templateview
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView

from menu.models import MenuCategory


class HomeView(TemplateView):
    template_name = 'home/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch all categories
        categories = MenuCategory.objects.all()
        context['categories'] = categories
        return context
    