

'''
可用的DAC口， PIN25  PIN26
STATIC const mdac_obj_t mdac_obj[] = {
    {{&machine_dac_type}, GPIO_NUM_25, DAC_CHANNEL_1},
    {{&machine_dac_type}, GPIO_NUM_26, DAC_CHANNEL_2},
};
'''

from machine import DAC,Pin
import math
import Timer

# 创建一个缓冲数组，用于存放一个sin波形
buf = bytearray(100)
for i in range(len(buf)):
    buf[i] = 128 + int(127 * math.sin(2*math.pi * i/len(buf)))


dac = DAC(Pin(25), bits=12) # bits可选 8/12



def write_sin_wave():
    # 设定频率为400HZ
    dac.write(buf, 400*len(buf), mode=DAC.CIRCULAR)

