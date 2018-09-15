'''
按键IRQ计数器 V2
'''
from button import Button

counter = 0
def callback(irq_pin):
    '''
    切换LED的状态
    '''
    global counter

    counter += 1
    print('Counter: {}'.format(counter))


# 创建一个Button对象，设置回调函数为callback
button = Button(0, callback)

try:
    while True:
        pass
except:
    button.deinit()