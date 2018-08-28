'''
点位计 ADC采样
定时打印ADC采样的结果
'''
from machine import ADC,Pin
import utime


# 设置D34号引脚作为ADC采样引脚
pin_read = Pin(34,Pin.IN)
# 声明ADC对象
adc = ADC(pin_read)
# 设置衰减比 满量程3.3v
adc.atten(ADC.ATTN_11DB)
# 设置数据宽度为10bit
adc.width(ADC.WIDTH_10BIT)

while True:
    # 数据采样 数值范围0-1023
    value = adc.read()
    # 打印日志
    print("Value: %d"%value)
    # 延时500ms
    utime.sleep_ms(500)