from machine import Pin
# 创建一个Pin的对象，传入GPIO的编号
led_pin = Pin(12, Pin.OUT)
# Pin12 输出高电平 打开LED
led_pin.value(1)