'''
按键计数器 每按一下，数值加1

存在按键抖动的问题
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

# 记录上一次按键的状态
last_btn_status = BTN_UP
counter = 0 # 计数器

print("按下按键， 会计数哦")
while True:
    # 获取按钮状态
    btn_status = button.value()

    if btn_status == BTN_DOWN and last_btn_status == BTN_UP:
        print("按键按下")
        counter += 1
        print("Counter += 1 ; Counter = %d"%(counter))

    last_btn_status = btn_status
    # 延时100ms
    utime.sleep_ms(100)
