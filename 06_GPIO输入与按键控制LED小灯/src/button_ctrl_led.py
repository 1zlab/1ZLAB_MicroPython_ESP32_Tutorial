'''
按键控制LED亮灭
状态转换
'''
from machine import Pin
import utime
from led import LED
# 按键
# 用户按键GPIO
# PyESPCar上自带的用户按键在39号管脚
USER_BTN = 39
# 按键引脚对象
button = Pin(USER_BTN, Pin.IN)
# 创建一个LED对象
led = LED(0)


# 定义按键按下的值 （取决于按键模块的设计， 有可能相反）
BTN_DOWN = 0 # 按键按下对应的取值 
BTN_UP = 1 # 按键抬起对应的状态
last_btn_status = None

while True:
    # 获取按钮状态
    btn_status = button.value()

    if btn_status == BTN_DOWN and last_btn_status == BTN_UP:
        # 切换LED状态
        led.toggle()
        print("按键按下,LED状态转换 LED: {}".format(led.pin.value() == led.LED_ON))
        
    last_btn_status = btn_status
    # 延时500ms
    utime.sleep_ms(150)
