from django.shortcuts import render
from .models import *


def index(request):
    data = {}
    data['outside_temperature'] = 20;
    link = main_linkes.objects.get(name_url='instagram')
    data['instagram_url'] = link.url


    link = main_linkes.objects.get(name_url='vk')
    data['vk_url'] = link.url

    link = main_linkes.objects.all
    data['main_urls'] = link

    link = main_sub_menu.objects.all
    data['main_sub_urls'] = link

    print(data['main_sub_urls'])



    return render(request, "zion/index.html",data)
# Create your views here.
