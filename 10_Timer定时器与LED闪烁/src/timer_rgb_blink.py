'''
利用定时器让RGB彩灯按照不同的频率闪烁
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


# 声明引脚 D32 作为LED的引脚
red_pin = Pin(12, Pin.OUT) # 定义红色LED引脚
red_timer = Timer(1)    # 创建定时器对象
led_blink_timed(red_timer, red_pin, freq=10)

green_pin = Pin(14, Pin.OUT) # 定义绿色LED引脚
green_timer = Timer(2)
led_blink_timed(green_timer, green_pin, freq=15)

blue_pin = Pin(27, Pin.OUT) # 定义蓝色LED引脚
blue_timer = Timer(3)
led_blink_timed(blue_timer, blue_pin, freq=20)



try:
    while True:
        # do nothing 什么也不做
        pass        
except:
    # 销毁定时器
    red_timer.deinit()
    green_timer.deinit()
    blue_timer.deinit()
