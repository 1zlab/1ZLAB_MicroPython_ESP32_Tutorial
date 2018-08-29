'''
流水灯 RGB彩灯

版本 v2 
版本备注： 
    使用函数 led_blink() 简化代码
'''

import machine
import utime

# 定义R 红色LED的引脚
pinR = machine.Pin(18, machine.Pin.OUT)
# 定义G 绿色LED的引脚
pinG = machine.Pin(19, machine.Pin.OUT)
# 定义B 蓝色LED的引脚
pinB = machine.Pin(21, machine.Pin.OUT)


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
    # 第一步：红色LED闪烁
    led_blink(pinR)

    # 第二步：绿色LED闪烁
    led_blink(pinG)

    # 第三步：蓝色LED闪烁 时间间隔设定为1000ms = 1s
    led_blink(pinB, delay_ms=1000)