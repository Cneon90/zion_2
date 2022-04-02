#### Фрейворк для создания проектов с управлением ESP8266, ESP32 (по MQTT,сокету,Teлеграм,Jabber, Windows приложением, Android) 
Данный модуль обеспечивает связь между микроконтроллерами (ESP8266, ESP32) и приложениями Delphi (для Windows), Delphi (для Android), базой данных (Postgress) 

___

**В модуле** 
   + Django - (Веб интерфейс) Возможность посмотреть все подключенные устройства, их состояние, настройки и т.п
   + python manage.py runscript zion_DB - Приложение запускается параллельно Django дает доступ к моделям Django по MQTT
   + приложение ZION

> Запуск
+ python web_control\manage.py runserver
+ python web_control\manage.py runscript zion_DB
+ python zion\__main__.py

   
ZION __Main__
```
import os
print(os.getcwd())
import zion.mqtt.mqtt as mqtt
import zion.jabber.myJabber as myJabber
import zion.telegramm.bot_telegramm as telegramm

from threading import *

def _mqtt():
    mqtt.mqtt_start()

def _jabber():
    myJabber.start()

def _telegramm():
    telegramm.start()


Tmqtt = Thread(target=_mqtt, args=())
Tjabber = Thread(target=_jabber, args=())
Ttelegramm = Thread(target=_telegramm, args=())

Tmqtt.start()
Tjabber.start()
Ttelegramm.start()

```


В данном модуле запускается 
   + MQTT - для обеспечения связи между всеми модулями (web, ESP8266,ESP32, ...) 
   + Jabber bot - 
   + Telegramm bot
    
    
Обмен сообщениями между модулями происходит по MQTT, данная схема образует единую шину обмена данными между всеми существующеми объектами системы  и позволяет
легко добавлять новые модули, новые модели для базы данных, новые устройства, расширяя функционал
