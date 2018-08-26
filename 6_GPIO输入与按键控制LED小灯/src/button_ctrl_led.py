'''
按键控制LED亮灭
状态转换
'''

from machine import Pin
import utime

# 按键
button = Pin(5, Pin.IN)
led = Pin(25, Pin.OUT)


# 定义按键按下的值 （取决于按键模块的设计， 有可能相反）
BTN_DOWN = 0 # 按键按下对应的取值 
BTN_UP = 1 # 按键抬起对应的状态
last_btn_status = None

while True:
    # 获取按钮状态
    btn_status = button.value()

    if btn_status == BTN_DOWN and last_btn_status == BTN_UP:
        led.value((led.value()+1)%2)
        print("按键按下,LED状态转换 LED: {}".format(led.value()))
    last_btn_status = btn_status
    # 延时500ms
    utime.sleep_ms(150)
