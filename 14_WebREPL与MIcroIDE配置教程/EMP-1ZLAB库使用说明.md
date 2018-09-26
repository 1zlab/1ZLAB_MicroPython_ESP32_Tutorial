# EMP

EMP (Easy MicroPython) is a upy module to make things Easy on MicroPython.



## 当前版本为0.1.11, 包含以下几个模块:

- emp_boot.py  一句代码用于设置MicroPython的boot启动模式
- emp_wifi.py  一句代码搞定WIFI连接
- emp_utils.py 工具模块,包含了emp_boot.py 和emp_wifi.py模块的一些依赖
- emp_dev.py 原microide.py,封装了一些文件操作的接口,供microide所调用的,现在已放置当前项目维护

当前版本主要包含的功能是为用户提供便捷的WIFI连接,通过emp_wifi.py





## 通过EMP来设置MicroPython开机WIFI连接和WebREPL

### 第一步,让你的MicroPython设备连接到网络

(如果已经连接请忽略,直接执行第二步)

连接wifi的代码如下:

```python
>>> import network
>>> wifi = network.WLAN(network.STA_IF)  
>>> wifi.active(True) 
>>> wifi.connect('<essid>', '<password>') #essid为WIFI名
>>> I (62825) wifi: n:1 1, o:1 0, ap:255 255, sta:1 1, prof:1
I (63395) wifi: state: init -> auth (b0)
I (63405) wifi: state: auth -> assoc (0)
I (63465) wifi: state: assoc -> run (10)
I (63515) wifi: connected with 你的WIFI名字, channel 1
I (63515) wifi: pm start, type: 1

I (63515) network: CONNECTED
I (64385) event: sta ip: 192.168.0.115, mask: 255.255.255.0, gw: 192.168.0.1
I (64385) network: GOT_IP
# 至此,可能你需要回车一下,才能出现下一 提示符 >>>
>>>

```



### 第二步,安装`emp-1zlab`库

```python
>>> import upip
I (240305) modsocket: Initializing
>>> upip.install('emp-1zlab')
Installing to: /lib/
Warning: pypi.org SSL certificate is not validated
Installing emp-1zlab 0.1.11 from https://files.pythonhosted.org/packages/59/95/b9e425d00c195c9beb2e77c0b02020676115c42762a32d61047650e3884b/emp-1zlab-0.1.11.tar.gz
>>> 
```



### 第三步,设置启动模式

```python
>>> from emp_boot import set_boot_mode
>>> set_boot_mode()
[0]   Boot with nothing
      attention: this option will clear up boot.py, careful!
[1]   Boot with wifi startup
      this mode will auto start wifi connect program.
[2]   Easy to develop
      this mode is for developers.In this mode you can develop much easier via EMP-IDE(emp.1zlab.com)
Please input your choice [0-2]: 


```



简单说明以下,第0项为启动脚本为空,这个会清除boot.py中的所有内容

第1项为开机时启动WIFI连接

第2项为开机启动WIFI连接的同时启动WebRepl,配合我们的IDE一起使用



### 第四步,按照提示进行开机引导

在此我们以第二项 Easy to develop为例:当你按下2回车后,你的设备将会重启:

```python
# 以上省略若干行日志,以下会罗列出 你当前的可用WIFI
created config/wifi_cfg.json # 初次运行会创建配置文件
I (3675) network: event 1
[0]    How_Router_Home                          -79     dBm
[1]    CMCC-iEPD                                -83     dBm
No record available # 如果你有已经登陆过的wifi,那么将会尝试自动连接
scaning networks...
I (6205) network: event 1
[0]    How_Router_Home                          -80     dBm
[1]    CMCC-iEPD                                -84     dBm
Which one do you want to access? [0-1]

```

在此选择你想要连接的WIFI,我的WIFI是第0个:

```python
scaning networks...
I (6205) network: event 1
[0]    How_Router_Home                          -80     dBm
[1]    CMCC-iEPD                                -84     dBm
Which one do you want to access? [0-1]0
Password for How_Router_Home: # 输入你的WIFI密码,回车

```

初次运行设置WebRepl

```python
# 省略若干行日志
I (369455) network: CONNECTED
I (370225) event: sta ip: 192.168.0.115, mask: 255.255.255.0, gw: 192.168.0.1
I (370225) network: GOT_IP
You are connected to How_Router_Home
IP: 192.168.0.115     # 你的内网 IP
Netmask: 255.255.255.0 # 掩码
Gateway: 192.168.0.1 # 网关
Added record: How_Router_Home
WebREPL daemon auto-start status: enabled

Would you like to (E)nable or (D)isable it running on boot?
(Empty line to quit)
> E                # E 为开启
To enable WebREPL, you must set password for it
New password (4-9 chars): 1zlab # 输入你的密码
Confirm password: 1zlab # 再次输入
No further action required


```



### 至此已成功的设置完成 你的MicroPython启动模式至 Easy develop模式,请访问我们的 网站[emp.1zlab.com](http://emp.1zlab.com)进行webrepl的高效开发吧!



### 可能你有如下的疑问:

- 自动连接wifi的话,我如何控制在多个网络下的连接?比如我有家两个路由器,分别为A,B,我都进行过连接,我该如何保证我想要连接到A而不是B呢?

  ```python
  >>> Wifi.set_default('<essid>')
  ```

- 如何删除一条记录呢? 忘记WIFI?

  ```python
  >>> Wifi.del_record('<essid>')
  ```

- 查看ip的接口?

  ```python
  >>> Wifi.ifconfig()
  You are connected to How_Router_Home
  IP: 192.168.0.115
  Netmask: 255.255.255.0
  Gateway: 192.168.0.1
  
  ```

- 断开当前的WIFI

  ```python
  >>> Wifi.disconnect()
  I (601244) wifi: state: run -> init (0)
  I (601244) wifi: pm stop, total sleep time: 565609183 us / 597113853 us
  
  I (601244) wifi: n:1 0, o:1 1, ap:255 255, sta:1 1, prof:1
  I (601264) wifi: flush txq
  I (601264) wifi: stop sw txq
  I (601264) wifi: lmac stop hw txq
  I (601264) wifi: STA_DISCONNECTED, reason:8
  E (601264) wifi: esp_wifi_connect 935 wifi not start
  I (601264) wifi: error attempting to reconnect: 0x3002
  I (601274) network: event 3
  WIFI connection has been disconnected
  
  ```

- 重新连接到其他WIFI?

  ```python
  # TODO em,有点小bug,待修复 ...
  ```


