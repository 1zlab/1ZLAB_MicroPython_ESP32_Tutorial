# ESP32的REPL使用方法与文件同步-1Z实验室



## 导引

本文主要讲解如何给ESP32-MicroPython编写程序，程序如何执行， 本文主要讲的是REPL交互式终端。

## 推广

**1Z实验室出品**
**1zlab: make things easy** 致力于在机器人+计算机视觉+人工智能的重叠区域, 制作小白友好的教程.

![img](https://upload-images.jianshu.io/upload_images/1199728-589a80ff77f380d8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000)


## 安装picocom

picocom是linux下的串口（终端）调试工具， 最简单易用。


https://developer.ridgerun.com/wiki/index.php/Setting_up_Picocom_-_Ubuntu

```bash
$ sudo apt-get install picocom
```


### 通过picocom连接ESP32终端

REPL的全称是`Read读入`+ `Evaluate执行` + `Print打印` + `Loop循环`。

连接MicroPython开发板的中断，直接输入就是输入一句，执行一句，并且将结果打印到终端上面。

**规约：在教程里如果代码是输入到`REPL`的话，都会添加`>>>`标志**
例如如下代码：
```python
>>> print('HelloWorld')
```
就代表是在`REPL`里面输入了`print('HelloWorld')`， **注意,` >>>` 不需要输入。**


首先需要通过串口链接MicroPython的终端： 

```bash
$ sudo picocom -b 115200 /dev/ttyUSB0
```

`-b` 是制定波特率`boundrate` 为115200

`/dev/ttyUSB0` 是设备端口号



**日志**

连接上窗口的时候，会打印一些ESP32开发板的信息：

```bash
$ sudo picocom -b 115200 /dev/ttyUSB0
[sudo] password for scorpion: 
picocom v2.2

port is        : /dev/ttyUSB0
flowcontrol    : none
baudrate is    : 115200
parity is      : none
databits are   : 8
stopbits are   : 1
escape is      : C-a
local echo is  : no
noinit is      : no
noreset is     : no
nolock is      : no
send_cmd is    : sz -vv
receive_cmd is : rz -vv -E
imap is        : 
omap is        : 
emap is        : crcrlf,delbs,

Type [C-a] [C-h] to see available commands

Terminal ready
```



如果没出出现如下标识，说明正在执行其他程序， 你需要先将程序中断。

```
>>> 
```

`CTRL+C` 中断程序，接下来你就可以在终端里面敲入Python的指令。

首先导入`machine` 模块

```python
>>> import machine
```

然后写入`machine.`  按下`Tab`按键

```python
>>> machine.
```

温馨提示： `TAB` 可以补全代码.

然后我们就可以看到machine下都有哪些子模块。

```python
>>> machine.
__name__        mem8            mem16           mem32
freq            reset           unique_id       idle
disable_irq     enable_irq      time_pulse_us   Timer
WDT             Pin             Signal          TouchPad
ADC             DAC             I2C             PWM
SPI             UART
```

声明一个管脚，GPIO编号为13, 模式为输出模式
```python
>>> pinR = machine.Pin(13, machine.Pin.OUT)
```
管脚写入高点平
```python
>>> pinR.value(1)
```



> PS: 如果你手里有LED模块的话， 可以将LED模块与ESP32的`13`号引脚相连接， 你也可以随意指定引脚编号。
>
> **PyESPCar小车底板 第13号引脚就是上拉的LED不需要外接,  高点平灭， 低电平亮。 使用的时候需要接入外接电源， 打开电源开关**
>
> NodeMCU32s开发板上的P2也是LED， 蓝色的， 高电平亮， 低电平灭。



### REPL快捷键(控制指令)

MicroPython终端交互里面有一些控制指令的快捷键。

- `CTRL + C` 中断程序
- `CTRL + D` 软重启
- `CTRL + E`  进入代码片段粘贴模式



```
  CTRL-A        -- on a blank line, enter raw REPL mode
  CTRL-B        -- on a blank line, enter normal REPL mode
  CTRL-C        -- interrupt a running program
  CTRL-D        -- on a blank line, do a soft reset of the board
  CTRL-E        -- on a blank line, enter paste mode
```



### 粘贴整段代码

如果你觉得一行一行的代码敲起来比较麻烦，你可以整段整段copy。

MicroPython有一个粘贴模式。

你可以先copy下面的代码片段： 

```python
'''
功能介绍： LED闪烁例程
'''
import utime
import machine

# 声明一个引脚 例如 D13 作为LED的引脚
led_pin = machine.Pin(13, machine.Pin.OUT)

while True:
    # 点亮LED -> 高电平
    led_pin.value(1)
    # 延时 500ms
    utime.sleep_ms(500)
    # 关闭LED -> 低电平
    led_pin.value(0)
    # 延时500ms
    utime.sleep_ms(500)
```



然后在picocom的REPL里面按`CTRL+E`进入粘贴模式， 右键粘贴刚才的代码片段。

**注意：粘贴好代码后，不要尝试修改粘贴好的代码，或者追加**

```python
>>> 
paste mode; Ctrl-C to cancel, Ctrl-D to finish
=== 
```

然后中端会提示你`Ctrl + C` 撤销刚才粘贴的代码， 就当啥也没发生过。

你可以按`Ctrl+D` 执行你刚才粘贴的代码。



**注意： 如果代码片段长了之后，可能会出现粘贴不全的问题， 这类情况，建议直接上传文件。**



### 断开REPL的连接

退出picocom， 断开与ESP32开发板的连接

`Ctrl + A` 是转义键

重要的事情，需要多重复几遍：

* 按 `Ctrl + A ` 然后按`Ctrl + Q` 就能够退出终端。
* 按 `Ctrl + A ` 然后按`Ctrl + Q` 就能够退出终端。
* 按 `Ctrl + A ` 然后按`Ctrl + Q` 就能够退出终端。
* 按 `Ctrl + A ` 然后按`Ctrl + Q` 就能够退出终端。

如果直接关闭掉`Terminal`左上角的`X`叉叉也是可以的。

## ESP32开发板的局限

**首先是ESP32没有板载LED, 板子上的LED只是 POWER LIGHT**


所以我们需要外接LED,去测试基本的I/O

MicroPython的官网也没找到ESP32的文档. 



**其此插入ESP32不会显示文件系统, 也就是不可以通过在文件系统中放置boot.py main.py的方式进行编程**

唯一的方法就是 terminal 终端交互式编程.



## 参考文章



Getting Started with MicroPython on ESP32 – Hello World, GPIO, and WiFi

https://www.cnx-software.com/2017/10/16/esp32-micropython-tutorials/



## 推广

**1Z实验室出品**
**1zlab: make things easy** 致力于在机器人+计算机视觉+人工智能的重叠区域, 制作小白友好的教程.

![img](https://upload-images.jianshu.io/upload_images/1199728-589a80ff77f380d8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000)

