'''
利用定时器周期的打印HelloWorld
'''
from machine import Timer

timer_id = 10000 # TODO 这里timer id好像可以是任何值 -1会报错
timer = Timer(timer_id)    # 创建定时器对象

def hello_world(t):
    print("Hello World")

# 初始化定时器
timer.init(period=1000, mode=Timer.PERIODIC , callback=hello_world) 


try:
    while True:
        # do nothing 什么也不做
        pass        
except:
    # 销毁定时器
    timer.deinit()
