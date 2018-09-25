import paho.mqtt.client as mqtt
import time

HOST_IP = 'localhost' # Server的IP地址
HOST_PORT = 1883 # mosquitto 默认打开端口
TOPIC_ID = 'pyespcar_basic_control' # TOPIC的ID

# 创建一个客户端
client = mqtt.Client()
# 连接到服务器（本机）
client.connect(HOST_IP, HOST_PORT, 60)

count = 0
while True:
    count += 1
    # 待发送的数据
    message = 'MOVE FRORWORD,{}'.format(count)   
    # 通过mqtt协议发布数据给server
    client.publish(TOPIC_ID, message)
    # 打印日志
    print('SEND: {}'.format(message))
    # 延时1s
    time.sleep(1)