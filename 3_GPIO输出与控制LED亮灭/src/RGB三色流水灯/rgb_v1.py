'''
流水灯 RGB彩灯

版本 v1 
版本备注： 
    原始的方法， 逐行， 不借助函数。
'''

import machine
import utime

# 定义R 红色LED的引脚
pinR = machine.Pin(18, machine.Pin.OUT)
# 定义G 绿色LED的引脚
pinG = machine.Pin(19, machine.Pin.OUT)
# 定义B 蓝色LED的引脚
pinB = machine.Pin(21, machine.Pin.OUT)


while True:
    # 第一步：红色LED闪烁
    pinR.value(1) # 红色LED的管脚输出高电平
    utime.sleep_ms(500) # 延时500ms
    pinR.value(0) # 红色LED的管脚输出低电平
    utime.sleep_ms(500) # 延时500ms

    # 第二步：绿色LED闪烁
    pinG.value(1) # 绿色LED管脚输出高电平
    utime.sleep_ms(500)
    pinG.value(0) # 绿色LED管脚输出低电平
    utime.sleep_ms(500)

    # 第三步：蓝色LED闪烁
    pinB.value(1) # 蓝色LED管脚输出低电平
    utime.sleep_ms(500)
    pinB.value(0) # 蓝色LED管脚输出低电平
    utime.sleep_ms(500)