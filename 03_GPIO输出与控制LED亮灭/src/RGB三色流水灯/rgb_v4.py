'''
流水灯 RGB彩灯

版本 v4
版本备注： 
    利用列表推导式，初始化数组，简化流程
'''

import machine
import utime



led_pin_nums = [18, 19, 21] # 定义led对应的管脚
# 使用Python的推到式生成 LED数组
led_pins = [machine.Pin(pin_num, machine.Pin.OUT) for pin_num in led_pin_nums]


def led_blink(led_pin, delay_ms=500):
    '''
    控制led的引脚（led_pin）进行闪烁 
    时间间隔为 delay_ms ， 默认为500ms
    '''
    led_pin.value(1) # LED的管脚输出高电平
    utime.sleep_ms(delay_ms) # 延时500ms
    led_pin.value(0) # LED的管脚输出低电平
    utime.sleep_ms(delay_ms) # 延时500ms


while True:
    
   for pin in led_pins:
        # 遍历数组led_pins中所有的pin实例，并执行闪烁函数
        led_blink(pin)