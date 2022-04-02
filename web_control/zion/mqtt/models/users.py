from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def all_users():
    count = User.objects.count()
    # all = Profile.objects.get(id=4)
    users = User.objects.all() #Нaйти пользователя по id
    print('Всего пользователей:'+str(count))
    # for user in users:
    #     print('>'+user.username)
    return users













    #===========Create user============================================================
    # user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    # user.last_name = 'Lennon'
    # user.save()

    # user = authenticate(username=login.username, password='LiriK1990')
    #
    # # print('pass:') Проверка пароля
    # # if user.check_password('LiriK1990') :
    # #     print('ok')
    # # else:
    # #     print('no ok')
    #
    # # print(login.get_full_name())
    #
    # if user is not None:
    #     # the password verified for the user
    #     if user.is_active:
    #         print("User is valid, active and authenticated")
    #     else:
    #         print("The password is valid, but the account has been disabled!")
    # else:
    #     # the authentication system was unable to verify the username and password
    #     print("The username and password were incorrect.")
    # return 1
