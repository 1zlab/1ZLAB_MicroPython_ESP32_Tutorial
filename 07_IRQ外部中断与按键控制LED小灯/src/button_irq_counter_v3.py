'''
按键IRQ计数器 V3
'''
from button import Button

counter = 0
def callback(irq_pin):
    '''
    切换LED的状态
    '''
    global counter

    counter += 1
    


# 创建一个Button对象，设置回调函数为callback
button = Button(0, callback)

# 记录上一次counter的取值
old_counter = counter
try:
    while True:
        if old_counter != counter:
            print('Counter: {}'.format(counter))
            old_counter = counter
except:
    button.deinit()