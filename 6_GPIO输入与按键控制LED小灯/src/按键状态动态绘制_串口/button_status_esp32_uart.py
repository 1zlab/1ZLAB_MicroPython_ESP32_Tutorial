# -*- coding:utf-8 -*-
'''
获取按键的状态并通过串口发送

接线：
    ESP32,TDX,D12 -> RXD,CP2102 (USB转TTL)
    ESP32,RXD,D13 -> TXD,CP2102 (USB转TTL)
'''

from machine import UART,Pin
import utime
import struct

# 初始化串口 UART
# 波特率 115200
# rx -> Pin 13
# tx -> Pin 12
uart = UART(2, baudrate=115200, rx=13,tx=12,timeout=10)
# 引脚
button = Pin(5, Pin.IN)

# 定义按键按下的值 （取决于按键模块的设计， 有可能相反）
BTN_DOWN = 0 # 按键按下对应的取值 
BTN_UP = 1 # 按键抬起对应的状态


while True:
    # 获取按钮状态
    btn_status = button.value()
    info = "{}\n".format(int(btn_status == BTN_DOWN))
    # 串口发送
    uart.write(info)
    # 打印原始的字节数据()
    print("Send字符: "+info+"\n")
    utime.sleep_ms(10)

