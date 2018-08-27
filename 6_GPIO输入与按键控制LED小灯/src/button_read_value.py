from machine import Pin

# 引脚
button = Pin(22, Pin.IN)
# 打印当前按键的电平 0 / 1
button.value()