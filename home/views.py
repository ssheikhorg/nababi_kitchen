# templateview
from django.views.generic import TemplateView

from .models import MenuCategory, FooterSettings, SpecialFacility, ContactInfo, SocialGalleryImage


class HomeView(TemplateView):
    template_name = 'home/home_page.html'

    def get_context_data(self, **kwargs):
        categories = MenuCategory.objects.all()
        footer_settings = FooterSettings.objects.first()
        facilities = SpecialFacility.objects.all()
        contact_info = ContactInfo.objects.first()
        gallery_images = SocialGalleryImage.objects.all()
        context = super().get_context_data(**kwargs)
        context['categories'] = categories
        context['footer_settings'] = footer_settings
        context['facilities'] = facilities
        context['contact_info'] = contact_info
        context['gallery_images'] = gallery_images
        return context
