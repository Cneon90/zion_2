'''
Данный скрипт выполняет связь между базой данных и основной программой zion (zion\zion\__main__.py)
Связь осуществляется по MQTT протоколу!
Для запуска данного скрипта в терминале выполните команду
   >python manage.py runscript zion_DB

   Реализация в файле zion.mqtt.main
'''
from zion.mqtt.__main__ import *


def run():
    #zion>mqtt>mqtt.py
    main()






