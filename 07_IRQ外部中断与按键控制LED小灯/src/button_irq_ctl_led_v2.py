'''
按键IRQ切换LED状态V2

简直完美
'''
from led import LED
from button import Button


# 创建LED对象
led = LED(0)

def callback(irq_pin):
    '''
    切换LED的状态
    '''
    global led
    led.toggle()

# 创建一个Button对象，设置回调函数为callback
button = Button(0, callback)

try:
    while True:
        pass
except:
    button.deinit()