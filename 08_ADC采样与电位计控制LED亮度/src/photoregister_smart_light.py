'''
Smart LED 基于光敏电阻的智能照明
如果光照强度小于某个阈值，就开灯。
'''


from machine import ADC,Pin
import utime

led_pin = Pin(2, Pin.OUT)
# 设置D33号引脚作为ADC采样引脚
pin_read = Pin(33, Pin.IN)

# 声明ADC对象
adc = ADC(pin_read)
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_12BIT)

# 设定阈值
boudary = 2000

while True:
    # 数据采样 模拟信号 -> 数字信号
    # 读取光照强度 illumination intensity
    intensity = adc.read()
    
    is_dark = intensity > boudary
    if is_dark:
        led_pin.value(1)
    else:
        led_pin.value(0)
        # 如果光照强度
    
    # 打印日志
    print("is Too Dark: {}".format(is_dark))
    utime.sleep_ms(1000)

