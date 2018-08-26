'''
ADC采样demo 

复杂一些的样例：支持自定义衰减比，跟二进制数据宽度
'''

from machine import ADC,Pin
import utime


# 设置D34号引脚作为ADC采样引脚
pin_read = Pin(34)
# 声明ADC对象
adc = ADC(pin_read)

'''
设定衰减比 （即满量程的电压，比如A TTN_11DB 满量程时电压为3.3V）。
衰减比取值
  ATTN_0DB    -- 0    --       # 满量程：1.2v
  ATTN_2_5DB  -- 1    --       # 满量程：1.5v
  ATTN_6DB    -- 2    --       # 满量程：2.0v
  ATTN_11DB   -- 3    --       # 满量程：3.3v
'''
adc.atten(ADC.ATTN_11DB)
# 也可以直接传入数值
# adc.atten(3)

 
'''
设定数据宽度 （二进制数据位数）
  WIDTH_9BIT  -- 0    --       # 9位数据宽度， 即：满量程0x1ff(511) 
  WIDTH_10BIT -- 1    --       # 10位数据宽度，即：满量程0x3ff(1023)
  WIDTH_11BIT -- 2    --       # 11位数据宽度，即：满量程0x7ff(2047)
  WIDTH_12BIT -- 3    --       # 12位数据宽度，即：满量程0xfff(4095)
'''
adc.width(ADC.WIDTH_12BIT)


while True:
    # 数据采样 模拟信号 -> 数字信号
    value = adc.read()
    # 打印日志
    print("Value: %d"%value)
    utime.sleep_ms(1000)


'''
ADC采样举例： 光敏电阻模块

？TODO 光敏电阻模块的简化电路图 ？


这是由于光照产生的载流子都参与导电，在外加电场的作用下作漂移运动，电子奔向电源的正极，
空穴奔向电源的负极，从而使光敏电阻器的阻值迅速下降。



光照增强 -> 电阻下降 -> 电压分压变小
'''