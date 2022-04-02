from paho.mqtt import client
import zion.mqtt.models.users as users
import zion.mqtt.models.profile as profile

# ---------------MQTT---------------------------------------
def on_connect(client, userdata, flags, rc):
    print("Connected with result code: %s" % rc)
    client.subscribe("mqtt/paho/test")

def publish(client,topic,msg):
   client.publish(topic, payload=msg)

def on_message(client, userdata, msg):
    print("%s: %s" % (msg.topic, msg.payload))

    if (msg.payload == b'Users'): #Запрос всех пользователей
        all_users = users.all_users()
        for user in all_users:
            publish(client=client,topic='mqtt/paho/test',msg=user.username)


    if (msg.payload == b'hi'): #Запрос всех пользователей
        profiles = profile.all_profile()
        print(profiles)
        for _profile in profiles:
            print('>' + _profile.Passport_number)
            publish(client=client,topic='mqtt/paho/test',msg=_profile.Passport_number)




def main():
    subscriber = client.Client()
    subscriber.on_connect = on_connect
    subscriber.on_message = on_message

    subscriber.connect("localhost")
    subscriber.loop_forever()
# ---------------MQTT---------------------------------------