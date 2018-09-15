'''
打印按键的状态
'''
from machine import Pin
import utime

# 用户按键GPIO
# PyESPCar上自带的用户按键在39号管脚
USER_BTN = 39
# 按键引脚对象
button = Pin(USER_BTN, Pin.IN)

# 定义按键按下的值 （取决于按键模块的设计， 有可能相反）
BTN_DOWN = 0 # 按键按下对应的取值 
BTN_UP = 1 # 按键抬起对应的状态

while True:
    # 获取按钮状态
    btn_status = button.value()

    if btn_status == BTN_DOWN:
        print("按键状态：按下 <<<<<<<<")
    else:
        print("按键状态：抬起 ========")
    # 延时500ms
    utime.sleep_ms(100)
