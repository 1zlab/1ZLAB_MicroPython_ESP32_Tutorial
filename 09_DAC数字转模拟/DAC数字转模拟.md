# DAC数字转模拟


## 什么是DAC
**首先声明，ESP32的DAC不好用， 有纹波。**
DAC 英文全称为Digital Analog Converter，将数字信号输出为模拟信号。
这里主要对比DAC与PWM，DAC输出的是模拟信号，PWM输出的是数字信号。
DAC也可以控制LED亮度，而且亮度范围更精细，因为DAC的输出电压是连续可变的，DAC控制LED也不存在PWM控制LED亮度那样的频闪问题，DAC可以实现比PWM更高精度的控制。另外PWM可以通过滤波器实现低精度的DAC功能。

## DAC的API文档
> TODO 添加时序DAC部分
### DAC硬件资源
**DAC在专用引脚上可用，可用的DAC引脚只有两个。 可用引脚有：GPIO25, GPIO26，输出的电压模拟值范围为0~3.3V**


### 导入DAC类
**导入DAC类与Pin类**
```python
from machine import DAC,Pin
```
### DAC构造器
**创建一个DAC的管脚Pin对象（声明为输出），然后传入到DAC的构造器里面**
```python
dac_pin = Pin(26, Pin.OUT)
dac = DAC(dac_pin)
```
另外你也可以指定DAC输出的分辨率`bits`， `bits`可选的值为`8， 12`。
```python
dac = DAC(Pin(26), bits=12) # bits可选 8/12
```
默认`bits=8`
如果`bits=8` 则dac的数值范围为`0-255`
如果`bits=12` 则dac的数值范围为`0-4095`

实际输出电压值为`0-3.3v`，数值范围映射到电压范围上。

### DAC输出

DAC输出使用`write`函数。
根据`bits`的不同，写入`value`值的范围也不同。
```python
dac.write(value)
```

### DAC资源的释放

```python
dac.deinit()
```

## DAC输出正弦波
DAC的演示实例-DAC输出正弦波， 可以用示波器进行观察。

```python
from machine import DAC,Pin
import math

# 创建一个缓冲数组，用于存放一个sin波形
buf = bytearray(100)
for i in range(len(buf)):
    buf[i] = 128 + int(127 * math.sin(2*math.pi * i/len(buf)))


dac = DAC(Pin(25), bits=12) # bits可选 8/12



def write_sin_wave():
    # 设定频率为400HZ
    dac.write(buf, 400*len(buf), mode=DAC.CIRCULAR)

```
> TODO DAC控制扬声器
## 思考题
大家可以把DAC与ADC的管脚用一根杜邦线连接在一起，然后DAC发送模拟量，通过ADC对其进行采样，观察ESP32的DAC纹波效应。