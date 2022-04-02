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


admin.site.register(Profile)

