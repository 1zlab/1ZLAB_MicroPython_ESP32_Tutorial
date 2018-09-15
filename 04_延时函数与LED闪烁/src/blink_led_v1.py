'''
功能介绍： LED闪烁例程

版本： v1
版本说明： 
    逐行控制高低电平与延迟
'''
import utime
from led import LED

# 声明一个LED对象 （P2）
led = LED(0)

while True:
    # 点亮LED
    led.on()
    # 延时 500ms
    utime.sleep_ms(500)
    # 关闭LED
    led.off()
    # 延时500ms
    utime.sleep_ms(500)