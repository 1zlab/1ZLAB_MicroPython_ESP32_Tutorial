'''
[功能描述]
按键外部中断 记录中断的次数

[备注]
按键模块 未按下的电平是1, 按下电平是0, 所以要检测是电平的下降沿 IRQ_FALLING

[存在问题]
按下一次，但是计数器增加多个，这个是因为按键在按下的时候产生了 抖动
所以我们需要做消抖操作！！！
'''
from machine import Pin

# 用户按键GPIO
# PyESPCar上自带的用户按键在39号管脚
USER_BTN = 39
# 引脚
button = Pin(USER_BTN, Pin.IN)

counter = 0 # 中断计数器
def button_irq_handle(pin):
    '''
    外部中断处理函数
    回调函数传入的参数为产生中断的Pin管脚对象
    '''
    global counter
    print('外部中断 下降沿触发， 中断计数:{}'.format(counter))
    print('当前管脚电平 ： {}'.format(pin.value()))
    counter += 1

# 下降沿触发
button.irq(trigger=Pin.IRQ_RISING, handler=button_irq_handle)


try:
    while True:
        pass
except:
    # 释放按键的IRQ资源
    button.irq(trigger=0, handler=None)