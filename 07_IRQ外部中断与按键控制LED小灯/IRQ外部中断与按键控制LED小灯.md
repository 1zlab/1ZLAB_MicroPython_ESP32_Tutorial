# IRQ外部中断与按键控制LED小灯



## 中断是个啥

中断是个什么呢？ 中断就是在做一个事情的时候，有另外一件事情**打断/打扰**你，等待你去处理。

假如你正在写代码，这个时候有人“梆～梆～梆～”敲门， 这个时候如果你放下手中的工作，站起身来马上去开门，那这个就叫做 **抢占式中断**。 如果你觉得这个事情不是很着急，神情自若的完成了手头的开发，同时顺便还写了一个单元测试，单元测试还给跑通了，然后去冲个咖啡提提神。 这个时候突然想起来，刚才有人在敲门，这才去走到门前，把门开开， 这个就叫做 **非抢占式中断**。 
不同事物的优先级 **Priority** 是不一样的，如果在一个时刻有多个中断产生，这个时候就按照它们的优先级进行排队，依次进行解决。

另外，站在单片机的角度，中断又分为 **内部中断** 与 **外部中断**。 **内部中断** 是单片机内部产生的，例如 **定时器中断** 每隔一段时间就执行特定的任务。 **外部中断** 是外界（单片机的外部）产生的中断，例如输入管脚电平的变化，从高电平到低电平（**下降沿中断， Falling**）或者从低电平变化到高电平(**上升沿中断, Rising**).


> 思考： 如果中断频次太高了会怎么样？


## IRQ的API介绍
IRQ的英文全称是 Interrupt Request， 中断请求的意思。Pin内置的IRQ其实是 **外部中断**，根据输入电平的变化作出相应。

**注意：ESP32的任何管脚都可以配置成IRQ外部中断。**

**初始化irq**， 首先要创建一个管脚对象
```python
from machine import Pin
button = Pin(22, Pin.IN) # 按键
```
这里用的是22号管脚，引脚配置为输入模式。

接下来使用Pin的`irq`方法，给管脚配置外部中断。
irq有两个参数，一个是`trigger`触发器，判断电平发生什么样的事件的时候触发。trigger有四种取值：

1. `0` 发生什么变化都不触发
2. `1`，`Pin.IRQ_FALLING` 下降沿触发
3. `2`， `Pin.IRQ_RISING` 上升沿触发
4. `3`, `Pin.IRQ_FALLING | Pin.IRQ_RISING` 双边触发（下降沿或上升沿的时候都触发）

 另外一个是`handler` 指定当发生中断的时候，哪个函数来处理这件事情。如果`handler = None`的话，就是产生中断的时候什么也不做。

```python
# 下降沿触发
button.irq(trigger=Pin.IRQ_FALLING, handler=button_irq_handle)
```
回调函数`button_irq_handle`的第一个参数是产生中断的这个Pin对象，你可以在回调函数里面调用其方法，读取`pin`的电平

```python
def button_irq_handle(pin):
    '''
    外部中断处理函数
    回调函数传入的参数为产生中断的Pin管脚对象
    '''
    print('当前管脚电平 ： {}'.format(pin.value()))
```

**释放引脚的irq资源**
经常释放资源是一个好习惯，如果你在repl里面创建了一个button的Pin对象并配置了`irq`， 如果你不释放资源的话，下次你重新创建`Pin(22)`的`irq`就不好使了。
```python
# 下降沿触发
button.irq(trigger=0, handler=None)
```

习惯上我们在粘贴模式粘贴代码的时候，都会带一个`try-except`语句，这样`CTRL + C`中断程序的时候，会自动释放`irq`资源。
```python
try:
    while True:
        pass
except:
    # 释放按键的IRQ资源
    button.irq(trigger=0, handler=None)
```

## 按键IRQ计数

`button_irq.py`

```python
'''
[功能描述]
按键外部中断 记录中断的次数

[备注]
按键模块 未按下的电平是1, 按下电平是0, 所以要检测是电平的下降沿 IRQ_FALLING

[存在问题]
按下一次，但是计数器增加多个，这个是因为按键在按下的时候产生了 抖动
所以我们需要做消抖操作！！！
'''
from machine import Pin

button = Pin(22, Pin.IN) # 按键
counter = 0 # 中断计数器
def button_irq_handle(pin):
    '''
    外部中断处理函数
    回调函数传入的参数为产生中断的Pin管脚对象
    '''
    global counter
    print('外部中断 下降沿触发， 中断计数:{}'.format(counter))
    print('当前管脚电平 ： {}'.format(pin.value()))
    counter += 1

# 下降沿触发
button.irq(trigger=Pin.IRQ_FALLING, handler=button_irq_handle)


try:
    while True:
        pass
except:
    # 释放按键的IRQ资源
    button.irq(trigger=0, handler=None)
```


## IRQ按键控制LED小灯
通过按键的IRQ 外部中断，来切换LED开关灯的状态.
这里添加了延时滤波，比上面的效果要好很多。

`button_irq_ctl_led.py`

```python
'''
按键中断控制LED的开关
'''
from machine import Pin
import utime

led_pin = Pin(12, Pin.OUT) # LED按键
button = Pin(22, Pin.IN) # 按键
led_status = False # LED的开关状态

# 定义按键按下的值 （取决于按键模块的设计， 有可能相反）
BTN_DOWN = 0 # 按键按下对应的取值 
BTN_UP = 1 # 按键抬起对应的状态


def button_irq_handle(pin):
    '''
    外部中断处理函数
    回调函数传入的参数为产生中断的Pin管脚对象
    '''
    global led_status
    global BTN_DOWN

    # 延时消抖
    utime.sleep_ms(150)

    if pin.value() == BTN_DOWN:
        # 状态取反
        led_status = not led_status
        led_pin.value(led_status)


# 下降沿触发
button.irq(trigger=Pin.IRQ_FALLING, handler=button_irq_handle)

try:
    while True:
        pass
except:
    # 释放按键的IRQ资源
    button.irq(trigger=0, handler=None)
```

## 工程经验

外部中断的回调函数里面， 尽量使用全局变量，另外尽量不要print。
如果要响应高频的中断的话，例如AB相编码器计数，在repl里面打印字符是非常消耗资源的。