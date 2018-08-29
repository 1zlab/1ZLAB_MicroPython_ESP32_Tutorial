# -*- coding:utf-8 -*-
import serial
import struct
from matplotlib import pyplot as plt
import threading, multiprocessing
import time
# 串口号 默认为 /dev/ttyUSB0
ser_dev = '/dev/ttyUSB1'

# 创建一个串口实例
ser = serial.Serial(ser_dev,115200, timeout=1, bytesize=8)


data_window = 1000 # 保留最近的400个数据点
data_buffer = [0]*data_window # 数据缓存池


def update_canvas():
    global data_buffer
    '''
    更新绘制数据
    '''
    while True:
        print("Begin 更新画面")
        plt.plot(data_buffer)
        plt.draw()
        plt.pause(0.04)
        print("END 更新画面")
    
def update_btn_status():
    global ser
    global data_buffer

    while True:
        # 读入一行数据  \n是换行符号 数据样式类似 '1\n' 或者 '0\n'
        info = ser.readline()
        # 讲接收的字节流转换成容易读取的样式
        print("Recv字符: "+info)
        # 注意接收过来的是字符串格式的数据
        # '1' -> 按键按下
        # ‘0’ -> 按键抬起
        print("按键状态 是否按下: {}".format(info[0]=='1'))
        # print("按键状态 是否按下: {}".format(int(info[0])==1))

        data_buffer.pop(0)
        btn_status = int(info[0])
        data_buffer.append(btn_status)
        time.sleep(0.001)

plt.ylim((-1, 2))
plt.ion()
plt.show()


thread_canvas = threading.Thread(target=update_canvas)
thread_canvas.start()

thread_serial = threading.Thread(target=update_btn_status)
thread_serial.start()

