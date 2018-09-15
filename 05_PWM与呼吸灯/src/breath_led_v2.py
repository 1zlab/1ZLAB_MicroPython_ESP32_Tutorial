'''
呼吸灯测试程序
v2 使用led.py
'''
import machine
import utime, math
from led import LED

# 初始化一个PWM对象叫做 led_pwm
led = LED(0)

def pulse(led, delay):
    # 呼吸灯核心代码
    # 借用sin正弦函数，将PWM范围控制在 0 - 1000范围内
    for i in range(20):
        value = int(math.sin(i / 10 * math.pi) * 500 + 500)
        # 设置LED的亮度
        led.intensity(value)
        # 延时delay个ms
        utime.sleep_ms(delay)
try:
    while True:
        pulse(led, 50)
except:
    # 销毁PWM对象
    led.deinit()