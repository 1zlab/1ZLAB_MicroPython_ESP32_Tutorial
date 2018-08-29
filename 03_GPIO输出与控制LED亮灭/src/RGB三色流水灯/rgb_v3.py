'''
流水灯 RGB彩灯

版本 v3
版本备注： 
    通过设定跑马灯的数组，简化流程
'''

import machine
import utime


'''
# -------静态初始化led_pins数组---------
# 定义R 红色LED的引脚
pinR = machine.Pin(18, machine.Pin.OUT)
# 定义G 绿色LED的引脚
pinG = machine.Pin(19, machine.Pin.OUT)
# 定义B 蓝色LED的引脚
pinB = machine.Pin(21, machine.Pin.OUT)

# 初始化led数组
led_pins = [pinR, pinG, pinB]
'''

# -----动态加载led_pins数组-----

led_pin_nums = [18, 19, 21] # 定义led对应的管脚
led_pins = [] # 存储引脚对象数组

for pin_num in led_pin_nums:
    # 声明一个新的pin对象
    pin = machine.Pin(pin_num, machine.Pin.OUT)
    # 将pin添加到数组led_pins的末尾
    led_pins.append(pin)


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