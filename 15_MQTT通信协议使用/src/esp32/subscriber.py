from umqtt.simple import MQTTClient
import time

SERVER = '192.168.43.16'
CLIENT_ID = 'PYESPCAR_A0'
TOPIC = b'pyespcar_ctl_msg'

def mqtt_callback(topic, msg):
	print('topic: {}'.format(topic))
	print('msg: {}'.format(msg))


client = MQTTClient(CLIENT_ID, SERVER)
client.set_callback(mqtt_callback)
client.connect()

client.subscribe(TOPIC)


while True:
	# 查看是否有数据传入
	# 有的话就执行 mqtt_callback
	client.check_msg()
	time.sleep(1)
