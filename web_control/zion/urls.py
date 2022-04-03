from django.conf.urls import url

from . import views
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('', views.index, name='index'),

]