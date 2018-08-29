

# Timer定时器与LED闪烁


## 什么是定时器？

定时器你可以理解是一个闹钟，你可以设定特定时间之后执行某件事情，也可以周期的执行某件事情,比如每隔1s钟变换一下LED的亮灯状态. 那它与`utime.sleep_ms`最大区别在于，定时器是**非阻塞**的（等待下一个时刻到来之前，可以做其他的事情），而延时函数是阻塞的（延时的时候不可以做其他的事情）。
定时器每个周期都会产生一次中断，然后调用特定的 **回调函数callback**, 定时器中断属于内部中断.

## 定时器Timer的API文档

第一步从`machine`模块里面导入`Timer`类。
```python
from machine import Timer
```
实例化一个`Timer`对象，传入一个任意正整数。
> TODO ESP32最多设置多少个定时器？

例如：
```python
timer = Timer(1)
```

然后需要 **初始化定时器**:
```python
timer.init(period=1000, mode=Timer.PERIODIC , callback=callback)
```

* `period`: 定时器执行的周期，单位是`ms`， 隔period ms 执行一次。
    period取值范围： `0 < period <= 3435973836`
* `mode`： 定时器的执行模式
    * `Timer.PERIODIC` 周期执行
    * `Timer.ONE_SHOT` 只执行一个，执行完了定时器就结束
* `callback`： 定时器的回调函数，传入的一个参数是`timer`


如果你想在callback函数里面传入其他参数，可以参照下方 **定时器控制LED闪烁** 中的 **Lambda表达式** 的方法。
```python
timer.init(period=period, mode=Timer.PERIODIC, callback=lambda t:led_toggle(led_pin))
```

最后，定时器使用完了记得要释放定时器资源，键盘中断并不会销毁定时器，定时器会一直产生回调函数。
```python
timer.deinit()
```
一般都是要在主循环里面，监听键盘中断，然后捕获异常执行`deinit`
```python
try:
    while True:
        # do nothing 这里做一些其他的事情。
        pass        
except:
    # 销毁定时器
    timer.deinit()
```

## 定时器样例
更多演示样例见`src`
### 定时器周期Print
如果你在运行这个程序的时候遇到了问题，可以参照下面的 **工程经验**。

设置定时器周期的打印`HelloWorld`

`print_hello_world_period.py`
```python
'''
利用定时器周期的打印HelloWorld
'''
from machine import Timer

timer_id = 10000 # TODO 这里timer id好像可以是任何值 -1会报错
timer = Timer(timer_id)    # 创建定时器对象

def hello_world(t):
    print("1ZLAB：Hello World")

# 初始化定时器
timer.init(period=1000, mode=Timer.PERIODIC , callback=hello_world) 


try:
    while True:
        # do nothing 什么也不做
        pass        
except:
    # 销毁定时器
    timer.deinit()

```

### 定时器控制LED闪烁


定时器控制LED闪烁
`timer_led_blink.py`
```python
from machine import Timer,Pin
import utime


def led_toggle(led_pin):
    '''
    LED状态反转
    '''
    status = led_pin.value()
    status = (status + 1) % 2
    led_pin.value(status)


def led_blink_timed(timer, led_pin, freq=10):
    '''
    led 按照特定的频率进行闪烁
    LED闪烁周期 = 1000ms / 频率
    状态变换间隔（period） = LED闪烁周期/ 2 
    '''
    # 计算状态变换间隔时间 ms
    period = int(0.5 * 1000 / freq)
    # 初始化定时器
    # 这里回调是使用了lambada表达式，因为回调函数需要传入led_pin
    timer.init(period=period, mode=Timer.PERIODIC, callback=lambda t:led_toggle(led_pin))


# 声明引脚 D12 作为LED的引脚
led_pin = Pin(12, Pin.OUT)
timer = Timer(1)    # 创建定时器对象
led_blink_timed(timer, led_pin, freq=20)

try:
    while True:
        # do nothing 什么也不做
        pass        
except:
    # 销毁定时器
    timer.deinit()

```

## 工程经验

注意，**不要在定时器函数里面创建变量**，可以使用 **全局变量 global**，因为定时器每次都创建变量比较消耗内存。
另外定时器函数里面，**不要在终端里面Print**，在终端Print打印会干扰Timer回调函数执行频率。而且定时器在产生按键中断`CTRL+C`的时候 **并不会注销**，如果定时器回调函数一直在打印，它会一直打印 **占用REPL资源**，导致 **无法通过REPL（AMPY）上传文件**，更蛋疼的是，如果你把这个带有定时打印的定时器函数写在了`main.py`的话, 每次上电都重新执行，你一直都修改不了`main.py`里面的内容，而且 **重新烧录固件并不会修改文件系统**， 你需要使用`esptool.py erase_flash` 擦除整个Flash

所以要养成一个良好的习惯，在程序里面写`timer.deinit`函数 

```python
try:
    while True:
        pass
except:
    # 注销Timer资源
    timer.deinit()
```

如果你想周期的打印一些东西，可以考虑设置一个全局的标志位`flag`， 定时器中断可以定期修改flag的值。 在`while True`主循环里面判断标志位的状态`flag`进行打印。

```python
flag = False # 标志位

def callback(timer):
    # 回调函数
    global flag
    
    if not flag:
        flag = True

# 初始化定时器
timer.init(period=1000, mode=Timer.PERIODIC , callback=callback)

try:
    while True:
        if flag:
            print('Flag is True')
            # flag == True，做相应的处理
            do_something()
        else:
            pass
except:
    # 注销Timer资源
    timer.deinit()
```

