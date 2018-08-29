'''
定时器控制LED闪烁
'''
from machine import Timer,Pin
import utime


def led_toggle(led_pin):
    '''
    LED状态翻转
    '''
    status = led_pin.value()
    status = (status + 1) % 2
    led_pin.value(status)


def led_blink_timed(timer, led_pin, freq=10):
    '''
    led 按照特定的频率进行闪烁
    LED闪烁周期 = 1000ms / 频率
    状态变换间隔（period） = LED闪烁周期/ 2 
    '''
    # 计算状态变换间隔时间 ms
    period = int(0.5 * 1000 / freq)
    # 初始化定时器
    timer.init(period=period, mode=Timer.PERIODIC, callback=lambda t:led_toggle(led_pin))


# 声明引脚 D12 作为LED的引脚
led_pin = Pin(12, Pin.OUT)
timer = Timer(1)    # 创建定时器对象
led_blink_timed(timer, led_pin, freq=20)




try:
    while True:
        # do nothing 什么也不做
        pass        
except:
    # 销毁定时器
    timer.deinit()
