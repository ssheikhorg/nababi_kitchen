from django.shortcuts import render

from .models import MenuItem

def menu_list(request) -> None:
    menu_list = MenuItem.objects.all()
    context = {
        'menu_list': menu_list
    }
    return render(request, 'menu/menu_list.html', context)
