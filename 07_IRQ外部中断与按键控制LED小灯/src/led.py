'''
LED类
v2 添加LED亮度控制 
'''
from machine import Pin, PWM

class LED:
    def __init__(self, led_id):
        # LED字典 
        # 数据结构： (gpio管脚编号， LED灭的电平， LED亮的电平)
        led_list = [(2, False, True),(13, True, False)]

        if led_id >= len(led_list) or led_id < 0:
            print('ERROR：LED编号无效， 有效ID：{} - {}'.format(0, len(led_list-1)))
            return None
        
        gpio_id, self.LED_OFF, self.LED_ON = led_list[led_id]
        self.pin = Pin(gpio_id, Pin.OUT)
        self.pwm = PWM(self.pin, freq=1000)

    def on(self):
        '''
        打开LED
        '''
        self.pin.value(self.LED_ON)
    
    def off(self):
        '''
        关闭LED
        '''
        self.pin.value(self.LED_OFF)
    
    def toggle(self):
        '''
        切换LED的状态
        OFF -> ON
        ON  -> OFF
        '''
        self.pin.value(not self.pin.value())

    def intensity(self, value):
        '''
        设置LED的亮度
        '''
        if self.LED_ON == True:
            self.pwm.duty(value)
        else:
            self.pwm.duty(1023 - value)
    
    def deinit(self):
        '''
        销毁资源
        '''
        self.pwm.deinit()