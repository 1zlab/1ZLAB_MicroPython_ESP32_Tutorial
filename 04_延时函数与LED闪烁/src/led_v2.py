'''
功能介绍： LED闪烁例程

版本 v2
版本说明： 利用函数实现led闪烁
'''
import utime
import machine

# 声明一个引脚 例如 D12 作为LED的引脚
led_pin = machine.Pin(12, machine.Pin.OUT)

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
    led_blink(led_pin, delay_ms=500)
    # led_blink(led_pin, delay_ms=100)