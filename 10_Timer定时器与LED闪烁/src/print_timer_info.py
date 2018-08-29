'''
定时器演示实例， 打印定时器，讲解定时器的属性。
'''

from machine import Timer
import utime


timer=Timer(1)


def timer_print(timer):
    # 打印当前的计数
    print("Timer InteruptCount , counter= %d"%(timer.value()))
    print(timer)


'''
定时器　模式：
Timer.ONE_SHOT --- 0                             --         # 执行一次
Timer.PERIODIC --- 1                             --         # 循环执行
'''
# timer.init(period=3000, mode=Timer.PERIODIC , callback=timer_print) #这里直接在回调函数中打印tim状态信息
timer.init(period=1000, mode=Timer.PERIODIC , callback=lambda t: print("Counter: %d"%(t.value()))) 


try:
    while True:
        print("do something..., counter = %d"%(timer.value()))
        utime.sleep_ms(100)    
except:
    # 必须要有这个try except ,要不然 键盘中段不能让定时器停止
    # 禁用此定时器
    timer.deinit()

'''
样例打印： 
Timer(3ffe67a0; alarm_en=1, auto_reload=1, counter_en=1)
Timer(3ffe67a0; alarm_en=1, auto_reload=1, counter_en=1)
。。。

3ffe67a0：创建定时器分配的内存空间首地址
alarm_en : alarm_en：ONE_SHOT模式下，回调函数调用完成之后alarm_en=0，否则alarm_en=1；PERIODIC模式下，alarm_en=1。
auto_reload: alarm_en：ONE_SHOT模式下，回调函数调用完成之后alarm_en=0，否则alarm_en=1；PERIODIC模式下，alarm_en=1。
counter_en：参数为0时表示计数器没在计数（没有初始化之前或者调用deinit()之后），参数为1时表示计数器正在计数
'''