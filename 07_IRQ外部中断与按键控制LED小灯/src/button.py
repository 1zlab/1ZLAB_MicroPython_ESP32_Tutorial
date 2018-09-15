'''
按键类Button
'''
from machine import Pin
import utime

class Button(object):
    '''
    按键对象
    '''
    def __init__(self,button_idx, callback=None):
        # 按键字典
        # 数据结构： (GPIO编号，按键抬起的电平， 按键按下的电平)
        button_list = [(39, False, True)]

        if button_idx < 0 or button_idx >= len(button_list):
            print("ERROR: Wrong Button Index")
            print("Valid Button Index: {} - {}".format(0, len(button_list)-1))
            return None

        gpio_id, self.BUTTON_RELEASE, self.BUTTON_PRESS, = button_list[button_idx]
        # 按键
        self.pin = Pin(gpio_id, Pin.IN)
        # 回调函数
        self.callback = callback
        # 设置外部中断
        if self.BUTTON_PRESS == True:
            self.pin.irq(trigger=Pin.IRQ_RISING, handler=self.irq_handler)
        else:
            self.pin.irq(trigger=Pin.IRQ_FALLING, handler=self.irq_handler)
        
        # 标志位 当前是否可以相应按键中断
        self.flag = True

    def irq_handler(self, irq_pin):
        '''
        外部中断的相应函数
        '''
        # 如果当前正在处理中断，则忽略
        if not self.flag:
            return
        # 添加软件滤波
        utime.sleep_ms(50)
        if self.pin.value() == self.BUTTON_PRESS:
            # 判断当前按键状态是不是按下，如果是，则执行回调函数
            if self.flag and self.callback is not None:
                self.flag = False
                # 执行回调函数
                self.callback(self.pin)
                self.flag = True
        
    def deinit(self):
        '''
        销毁资源
        '''
        self.pin.irq(trigger=0, handler=None) # 销毁外部中断的资源
    
