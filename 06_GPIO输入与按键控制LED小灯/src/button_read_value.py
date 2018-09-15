from machine import Pin

# 用户按键GPIO
# PyESPCar上自带的用户按键在39号管脚
USER_BTN = 39
# 按键引脚对象
button = Pin(USER_BTN, Pin.IN)

# 打印当前按键的电平 0 / 1
button.value()