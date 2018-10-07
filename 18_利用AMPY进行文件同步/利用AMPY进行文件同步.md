# 利用AMPY进行文件同步-1Z实验室



## 概要

本文主要讲的是如何使用AMPY工具对文件进行同步，把文件上传到ESP32上面。



## 推广

**1Z实验室出品**
**1zlab: make things easy** 致力于在机器人+计算机视觉+人工智能的重叠区域, 制作小白友好的教程.

![img](https://upload-images.jianshu.io/upload_images/1199728-589a80ff77f380d8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000)

## Ampy简介

不同与其他的MicroPython开发板， ESP32连接到电脑上，并不会出现其文件系统，需要借助其他工具实现文件上传与下载。

Ampy是Adafruit公司推出的用于对ESP32文件系统进行管理的工具， 可以用于将本地的`.py`文件同步到ESP32的文件系统中。

Ampy的原理就是进入REPL，在REPL中完成文件的同步。所以在使用Ampy之前，需要先**中断原来picocom的连接**.

另外如果原来的程序在一直`print` 打印输出，则ampy也无法正常使用，在使用前需要先在Picocom的REPL里面中断掉原有的循环语句。



## 安装Ampy



通过`pip` 安装`ampy`

```bash
$ sudo pip install adafruit-ampy --upgrade
```

安装成功, 查看ampy的版本号：

```bash
$ ampy --version
ampy, version 1.0.3
```



## 调试执行-run

首先打开文本编辑器， 创建一个文件叫做`led.py`

然后，粘贴如下内容：

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



接下来在终端执行代码：

```bash
$ sudo ampy --port /dev/ttyUSB0 run led.py 
```

然后ESP32开发板就会执行`led.py` 里面的内容。 这个效果跟REPL里面的**Paste 粘贴模式** 效果是一样的。



## 上传文件-put

文件上传使用`put`指令，把之前写好的`led.py` 上传到ESP32的文件系统里面。

```bash
$ sudo ampy --port /dev/ttyUSB0 put led.py
```

通过终端重新链接, 查看刚刚存入的.py文件.

```python
>>> import os
>>> os.listdir()
['boot.py', 'led.py']
```



**如果你希望你写的代码可以上电执行的话，需要把代码写在main.py里面。**

首先需要创建一个`main.py`  我们直接将之前的 `led.py` 重命名为`main.py`

```bash
$ cp led.py main.py
```

然后将`main.py`上传到板子上

```bash
$ sudo ampy --port /dev/ttyUSB0 put main.py 
```

接下来, 按硬件上的**复位 Reset**按钮， 硬件开始执行LED小灯的程序.



## 删除文件-rm

删除文件使用`rm` 指令。

```bash
$ ampy --port /dev/ttyUSB0 rm led.py 
```



## 推广

**1Z实验室出品**
**1zlab: make things easy** 致力于在机器人+计算机视觉+人工智能的重叠区域, 制作小白友好的教程.

![img](https://upload-images.jianshu.io/upload_images/1199728-589a80ff77f380d8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000)

