'''
电位计采样，控制LED的亮度
'''
from machine import ADC,Pin,PWM
import utime

# 2号引脚作为led引脚
led_pin = Pin(2, Pin.OUT)
led_pwm = PWM(led_pin)
led_pwm.duty(0)
led_pwm.freq(1000)

# 设置D34号引脚作为ADC采样引脚
pin_read = Pin(34,Pin.IN)
# 声明ADC对象
adc = ADC(pin_read)
# 设置衰减比 满量程3.3v
adc.atten(ADC.ATTN_11DB)
# 设置数据宽度为10bit
adc.width(ADC.WIDTH_10BIT)

def mean_filter(adc, sample_times = 10):
    # 做一个简单的均值滤波
    value_sum = 0
    for i in range(sample_times):
        value_sum += adc.read()
    # 计算ADC采样的均值
    value_mean =  value_sum / sample_times
    return value_mean

last_value = 0
while True:
    try:
        value_mean = mean_filter(adc)
        # 判断是否发生了变化
        if abs(last_value-value_mean) > 2:
            # 打印日志
            print("电位计采样: %d"%value_mean)
            # 根据adc采样 设定LED的duty
            # ADC采样与PWM占空比的范围都设定的是0-1023
            led_pwm.duty(int(value_mean))
        # 更新last value
        last_value = value_mean
        # 延时100ms
        utime.sleep_ms(100)
    except:
        # 释放PWM资源
        led_pwm.deinit()