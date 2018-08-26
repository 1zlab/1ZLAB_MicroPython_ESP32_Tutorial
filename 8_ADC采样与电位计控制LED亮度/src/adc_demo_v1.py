'''
ADC采样demo 

复杂一些的样例：支持自定义衰减比，跟二进制数据宽度
'''

from machine import ADC,Pin
import utime

'''
ADC管脚在固件中的定义： !!! 有效引脚编号　32->37 !!!
STATIC const madc_obj_t madc_obj[] = {
    {{&machine_adc_type}, GPIO_NUM_36, ADC1_CHANNEL_0},
    {{&machine_adc_type}, GPIO_NUM_37, ADC1_CHANNEL_1},
    {{&machine_adc_type}, GPIO_NUM_38, ADC1_CHANNEL_2},
    {{&machine_adc_type}, GPIO_NUM_39, ADC1_CHANNEL_3},
    {{&machine_adc_type}, GPIO_NUM_32, ADC1_CHANNEL_4},
    {{&machine_adc_type}, GPIO_NUM_33, ADC1_CHANNEL_5},
    {{&machine_adc_type}, GPIO_NUM_34, ADC1_CHANNEL_6},
    {{&machine_adc_type}, GPIO_NUM_35, ADC1_CHANNEL_7},
};
'''
# 设置D32号引脚作为ADC采样引脚
pin_read = Pin(32)
# 声明ADC对象
adc = ADC(pin_read)

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