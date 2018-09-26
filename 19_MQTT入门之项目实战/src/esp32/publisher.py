from umqtt.simple import MQTTClient
import time

SERVER = '192.168.43.16'
CLIENT_ID = 'PYESPCAR_A0'
TOPIC = b'pyespcar_basic_control'

client = MQTTClient(CLIENT_ID, SERVER)
client.connect()


while True:
    client.publish(TOPIC, 'helloworld')
    time.sleep(1)
