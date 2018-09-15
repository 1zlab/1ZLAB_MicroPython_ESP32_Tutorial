'''
功能介绍： LED闪烁例程

版本 v2
版本说明： 利用函数实现led闪烁
'''
import utime
from led import LED

# 声明一个LED （P2）
led = LED(0)

def led_blink(led_pin, delay_ms=500):
    '''
    控制led的引脚（led_pin）进行闪烁 
    时间间隔为 delay_ms ， 默认为500ms
    '''
    global led
    led.toggle() # 切换LED的状态
    utime.sleep_ms(delay_ms) # 延时500ms

while True:
    led_blink(led_pin, delay_ms=500)
    # led_blink(led_pin, delay_ms=100)