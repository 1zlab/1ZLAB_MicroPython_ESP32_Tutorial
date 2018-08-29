'''
利用ADC 自制电压表

数字的数值范围 ，0-4095
测量范围 0v - 3.3v  注意： 不能越界
'''
from machine import ADC,Pin
import utime

# 设置D34号引脚作为ADC采样引脚
pin_read = Pin(34,Pin.IN)
# 声明ADC对象
adc = ADC(pin_read)


def digtal2volt(digital_value):
    '''
    数字信号转换为实际的电压值
    '''
    volt = (digital_value / 4095) * 3.3
    return volt


while True:
    # 数据采样 模拟信号 -> 数字信号
    value = adc.read()
    # 打印日志
    print("Value: %d -> Volt: %.2fv"%(value, digtal2volt(value)))
    # 延时1s
    utime.sleep_ms(1000)
