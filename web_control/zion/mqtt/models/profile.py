from zion.models import *  #Импорт моделей из Django приложений


def all_profile():
    all = Profile.objects.all()
    return all

