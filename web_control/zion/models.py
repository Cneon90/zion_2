from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Расширяем класс юзер(дополнительные данные, после регистрации)
class Profile(models.Model):
    #Modeluser = models.OneToOneField(User, on_delete=models.CASCADE) #Привязываем к модели юзер
    Passport_series = models.CharField(max_length=10, blank=True)
    Passport_number = models.CharField(max_length=40, blank=True)
    Passport_received = models.CharField(max_length=60, blank=True)


    def __str__(self):
        return self.Passport_series



class main_linkes(models.Model):
    name_url = models.CharField(max_length=50, blank=True)
    url = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.name_url

class main_sub_menu(models.Model):
    name_url = models.ForeignKey(main_linkes, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    url  = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name




admin.site.register(Profile)
admin.site.register(main_linkes)
admin.site.register(main_sub_menu)
