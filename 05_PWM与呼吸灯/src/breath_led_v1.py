'''
呼吸灯测试程序
v1
'''
import machine
import utime, math

# 初始化一个PWM对象叫做 led_pwm
led_pwm = machine.PWM(machine.Pin(12), freq=1000)

def pulse(led_pwm, delay):
    # 呼吸灯核心代码
    # 借用sin正弦函数，将PWM范围控制在 0 - 1000范围内
    for i in range(20):
        led_pwm.duty(int(math.sin(i / 10 * math.pi) * 500 + 500))
        # 延时delay个ms
        utime.sleep_ms(delay)
try:
    while True:
        pulse(led_pwm, 50)
except:
    # 销毁PWM对象
    led_pwm.deinit()