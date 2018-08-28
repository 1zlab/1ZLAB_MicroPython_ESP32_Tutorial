'''
检测ADC采样值是否发生变化，如果发生变化就打印出来
采用均值滤波
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

last_value = 0
sample_times = 10
while True:
    # 做一个简单的均值滤波
    value_sum = 0
    for i in range(sample_times):
        value_sum += adc.read()
    # 计算ADC采样的均值
    value_mean =  value_sum / sample_times
    # 判断是否发生了变化
    if abs(last_value-value_mean) > 2:
        # 打印日志
        print("电位计采样: %d"%value_mean)
    # 更新last value
    last_value = value_mean
    # 延时100ms
    utime.sleep_ms(100)