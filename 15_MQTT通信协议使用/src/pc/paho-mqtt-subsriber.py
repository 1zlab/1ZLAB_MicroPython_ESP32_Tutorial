import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    '''处理message回调'''
    print('topic: {}'.format(msg.topic))
    print('message: {}'.format(str(msg.payload)))

# 建立一个MQTT的客户端
client = mqtt.Client()
# 绑定数据接收回调函数
client.on_message = on_message

HOST_IP = 'localhost' # Server的IP地址
HOST_PORT = 1883 # mosquitto 默认打开端口
TOPIC_ID = 'pyespcar_basic_control' # TOPIC的ID

# 连接MQTT服务器
client.connect(HOST_IP, HOST_PORT, 60)
# 订阅主题
client.subscribe(TOPIC_ID)

# 阻塞式， 循环往复，一直处理网络数据，断开重连
client.loop_forever()