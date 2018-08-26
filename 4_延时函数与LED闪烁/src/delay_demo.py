
'''
演示延时功能
每隔1s(1000 ms) 打印一个hello_world
'''

import utime


while True:
    print('Hello World!!!')
    utime.sleep_ms(1000)
