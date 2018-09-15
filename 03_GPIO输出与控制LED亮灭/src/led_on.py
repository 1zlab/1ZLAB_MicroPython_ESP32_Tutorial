from machine import Pin
# 创建一个Pin的对象，传入GPIO的编号
led_pin = Pin(3, Pin.OUT)
# Pin13 输出高电平 打开LED
LED_ON = 0 # LED亮的时候的电平
LED_OFF = 1 # LED灭的时候的电平

# 小灯灭
# led_pin.value(LED_OFF)

# 小灯亮
led_pin.value(LED_ON)