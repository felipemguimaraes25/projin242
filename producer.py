import paho.mqtt.client as mqtt
import random
import json

print('Conectando ao MQTT Broker...')
mqtt_client = mqtt.Client()
mqtt_client.connect('localhost', 1883)


pessoas = int(random.uniform(1, 10))
print(pessoas)


mensagem = {
    'cliente': 'Havan',
    'Pessoas Entrando': pessoas,

}

mqtt_client.publish('projin242', json.dumps(mensagem))