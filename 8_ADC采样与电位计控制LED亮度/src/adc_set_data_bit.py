'''
设定ADC采样对应的二进制数值的比特数
'''

from machine import ADC,Pin
import utime


# 设置D34号引脚作为ADC采样引脚
pin_read = Pin(34, bit=0)
# 声明ADC对象
adc = ADC(pin_read)


while True:
    # 数据采样 模拟信号 -> 数字信号
    value = adc.read()
    # 打印日志
    print("Value: %d"%value)
    utime.sleep_ms(1000)