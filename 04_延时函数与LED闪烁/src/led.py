from machine import Pin

class LED:
    def __init__(self, led_id):
        # LED字典 
        # 数据结构： (gpio管脚编号， LED灭的电平， LED亮的电平)
        led_list = [(2, False, True),(13, True, False)]

        if led_id >= len(led_list) or led_id < 0:
            print('ERROR：LED编号无效， 有效ID：{} - {}'.format(0, len(led_list-1)))
            return None
        
        gpio_id, self.LED_OFF, self.LED_ON = led_list[led_id]
        self.led_pin = Pin(gpio_id, Pin.OUT)
        
    def on(self):
        '''
        打开LED
        '''
        self.led_pin.value(self.LED_ON)
    
    def off(self):
        '''
        关闭LED
        '''
        self.led_pin.value(self.LED_OFF)
    
    def toggle(self):
        '''
        切换LED的状态
        OFF -> ON
        ON  -> OFF
        '''
        self.led_pin.value(not self.led_pin.value())