# GPIO输入与用户按键控制LED开关-1Z实验室


## 概要

* 读取按键的值 Value
* 按键状态打印
* 按键计数器
* 按键控制LED

## GPIO的输入模式

从`machine` 里面导入`Pin`, 创建一个名字叫做`button`的管脚对象。
设置模式为输入模式（`Pin.IN`）. 
```python
>>> from machine import Pin
# 引脚
>> button = Pin(22, Pin.IN)
```
读取电平高低的方式依然使用的是`value`函数。

```python
# 打印当前按键的电平 0 / 1
>>> button.value()
```

## 按键状态检测

这个时候，你可以尝试在按按钮的时候采集的电平，与不按按钮的时候电平。
常规的按键电路，按键按下电路导通，输入高电平，按键抬起输入低电平
在按键模块采用上拉电路的情况下，按键抬起是高电平，按下是低电平。


`BTN_DOWN`跟`BTN_UP`两个取值，可以根据你的按键模块做相应的调整。

```python
'''
打印按键的状态
'''
from machine import Pin
import utime

# 引脚
button = Pin(22, Pin.IN)

# 定义按键按下的值 （取决于按键模块的设计， 有可能相反）
BTN_DOWN = 0 # 按键按下对应的取值 
BTN_UP = 1 # 按键抬起对应的状态

while True:
    # 获取按钮状态
    btn_status = button.value()

    if btn_status == BTN_DOWN:
        print("按键状态：按下 <<<<<<<<")
    else:
        print("按键状态：抬起 ========")
    # 延时500ms
    utime.sleep_ms(100)
```

## 按键计数

按键计数就是记录按键按下的次数。
根据当前按键的状态`btn_status`与上一次按键的状态`last_btn_status`来判断按键是否按下。如果当前按键状态为`BTN_DOWN`，之前的按键状态为`BTN_UP` 则判断为产生一次键盘按下的事件，计数器`counter`就+1。

```python
'''
[功能描述]
按键计数器 每按一下，数值加1
[存在问题]
存在按键抖动的问题
'''
from machine import Pin
import utime

# 引脚
button = Pin(22, Pin.IN)

# 定义按键按下的值 （取决于按键模块的设计， 有可能相反）
BTN_DOWN = 0 # 按键按下对应的取值 
BTN_UP = 1 # 按键抬起对应的状态

# 记录上一次按键的状态
last_btn_status = BTN_UP
counter = 0 # 计数器

print("按下按键， 会计数哦")
while True:
    # 获取按钮状态
    btn_status = button.value()

    if btn_status == BTN_DOWN and last_btn_status == BTN_UP:
        print("按键按下")
        counter += 1
        print("Counter += 1 ; Counter = %d"%(counter))

    last_btn_status = btn_status
    # 延时200ms 消抖用
    utime.sleep_ms(200)
```

## 按键抖动与消抖
在上面的演示实例运行的过程中，我们会发现有时候按下一次，计数器会增加好几个数值。这个是因为按键**抖动 Bouncing**的问题，当机械触点断开、闭合时，由于机械触点的弹性作用，一个按键开关在闭合时不会马上稳定地接通，在断开时也不会一下子断开。

![button-bouncing.png](./image/button-bouncing.png)

从而产生噪声，干扰对按键状态的判断，为了克服这个问题，产生了**消抖**技术。

消抖又分为两种，一种是软件消抖，一种是硬件消抖。硬件消抖的方式就是在按键两端加上一个电容。

软件消抖又有延时消抖，定时轮巡，还有时间戳+状态机（适用于外部中断）的方法。

上面的按键计数中的：
```python
# 延时100ms 消抖用
utime.sleep_ms(200)
```
就是较为简单的延时消抖，延时时间短了效果不稳定，抖动还是比较明显。如果延时时间长了，一来反应速度慢，而来阻塞式延时，比较消耗资源。

软件消抖的算法，在后续的课程里再深入讲解，这里大家需要知道有这么一会儿事。

> TODO 编写软件消抖的教程。

## 按键控制LED亮灭

**关于接线**
GPIO22接按键， GPIO12接LED模块
> TODO 接线配图

用按键来切换LED的状态，在0 - 1之间进行切换。
LED状态转换核心代码：
```python
led.value((led.value()+1)%2)
```
需要思考一会儿才能领悟其中的真谛。


```python
'''
按键控制LED亮灭
状态转换
'''

from machine import Pin
import utime

# 按键
button = Pin(22, Pin.IN)
led = Pin(12, Pin.OUT)


# 定义按键按下的值 （取决于按键模块的设计， 有可能相反）
BTN_DOWN = 0 # 按键按下对应的取值 
BTN_UP = 1 # 按键抬起对应的状态
last_btn_status = None

while True:
    # 获取按钮状态
    btn_status = button.value()

    if btn_status == BTN_DOWN and last_btn_status == BTN_UP:
        led.value((led.value()+1)%2)
        print("按键按下,LED状态转换 LED: {}".format(led.value()))
    last_btn_status = btn_status
    # 延时500ms
    utime.sleep_ms(150)

```