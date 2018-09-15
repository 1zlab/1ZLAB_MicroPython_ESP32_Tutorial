'''
按键IRQ(外部中断)切换LED状态V1
'''
from machine import Pin
import utime
from led import LED

# 定义按键按下的值 （取决于按键模块的设计， 有可能相反）
BTN_DOWN = 1 # 按键按下对应的取值 
BTN_UP = 0 # 按键抬起对应的状态

# 用户按键GPIO
# PyESPCar上自带的用户按键在39号管脚
USER_BTN = 39
# 引脚
button = Pin(USER_BTN, Pin.IN)

# 创建一个LED对象
led = LED(0)

def button_irq_handle(button):
    '''
    外部中断处理函数
    回调函数传入的参数为产生中断的Pin管脚对象
    '''
    global BTN_DOWN
    global led
    # 延时消抖
    utime.sleep_ms(50)
    if button.value() == BTN_DOWN:
        # 状态取反
        led.toggle()

# 下降沿触发
button.irq(trigger=Pin.IRQ_FALLING, handler=button_irq_handle)

try:
    while True:
        pass
except:
    # 释放按键的IRQ资源
    button.irq(trigger=0, handler=None)