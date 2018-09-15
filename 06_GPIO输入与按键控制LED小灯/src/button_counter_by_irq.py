'''
利用按键中断， 实现按键计数器 每按一下，数值加1
'''

from machine import Pin
import utime

# 用户按键GPIO
# PyESPCar上自带的用户按键在39号管脚
USER_BTN = 39
# 引脚
button = Pin(USER_BTN, Pin.IN)

# 定义按键按下的值 （取决于按键模块的设计， 有可能相反）
# BTN_DOWN = 0 # 按键按下对应的取值 
# BTN_UP = 1 # 按键抬起对应的状态

counter = 0 # 计数器

def counter_callback(pin):
    '''
    计数器回调函数
    '''
    
    global counter
    
    # 添加软件消抖
    utime.sleep_ms(150)
    if pin.value() == 0:
        counter += 1
        print("Counter += 1 ; Counter = %d"%(counter))
    

button.irq(trigger=Pin.IRQ_FALLING, handler=counter_callback)
print("按下按键， 会计数哦")

while True:
    print("do something...")
    utime.sleep_ms(500)


