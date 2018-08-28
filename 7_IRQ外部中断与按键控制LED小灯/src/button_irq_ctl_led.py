'''
按键中断控制LED的开关
'''
from machine import Pin
import utime

led_pin = Pin(12, Pin.OUT) # LED按键
button = Pin(22, Pin.IN) # 按键
led_status = False # LED的开关状态

# 定义按键按下的值 （取决于按键模块的设计， 有可能相反）
BTN_DOWN = 0 # 按键按下对应的取值 
BTN_UP = 1 # 按键抬起对应的状态


def button_irq_handle(pin):
    '''
    外部中断处理函数
    回调函数传入的参数为产生中断的Pin管脚对象
    '''
    global led_status
    global BTN_DOWN

    # 延时消抖
    utime.sleep_ms(150)

    if pin.value() == BTN_DOWN:
        # 状态取反
        led_status = not led_status
        led_pin.value(led_status)


# 下降沿触发
button.irq(trigger=Pin.IRQ_FALLING, handler=button_irq_handle)

try:
    while True:
        pass
except:
    # 释放按键的IRQ资源
    button.irq(trigger=0, handler=None)