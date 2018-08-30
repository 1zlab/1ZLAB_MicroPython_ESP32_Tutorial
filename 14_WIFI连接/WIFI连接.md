
# ESP32Wifi连接-STA模式

## 概述
ESP32可以连接WIFI热点，此模式称之为STA模式。
ESP32也可以当作热点，别的设备连接ESP32，此模式为AP模式。
本节课主要讲的是


## WIFI连接

如果你想ESP32上电就连接ESP32的话，可以把这个脚本放在main.py里面。初次连接网络需要连接REPL，在终端中输入WIFI热点的SSID还有密码，这些信息会保存在`wifi_config.json`文件里，下次reboot之后会自动连接。

`main.py`
```python
def do_connect():
    import json
    import network
    # 尝试读取配置文件wifi_confi.json,这里我们以json的方式来存储WIFI配置
    # wifi_config.json在根目录下
    
    # 若不是初次运行,则将文件中的内容读取并加载到字典变量 config
    try:
        with open('wifi_config.json','r') as f:
            config = json.loads(f.read())
    # 若初次运行,则将进入excpet,执行配置文件的创建        
    except:
        essid = input('wifi name:') # 输入essid
        password = input('wifi passwrod:') # 输入password
        config = dict(essid=essid, password=password) # 创建字典
        with open('wifi_config.json','w') as f:
            f.write(json.dumps(config)) # 将字典序列化为json字符串,存入wifi_config.json
            
    #以下为正常的WIFI连接流程        
    wifi = network.WLAN(network.STA_IF)  
    if not wifi.isconnected(): 
        print('connecting to network...')
        wifi.active(True) 
        wifi.connect(config['essid'], config['password']) 
        import time
        time.sleep(5) #一般睡个5-10秒,应该绰绰有余
        
        if not wifi.isconnected():
            wifi.active(False) #关掉连接,免得repl死循环输出
            print('wifi connection error, please reconnect')
            import os
            # 连续输错essid和password会导致wifi_config.json不存在
            try:
                os.remove('wifi_config.json') # 删除配置文件
            except:
                pass
            do_connect() # 重新连接
        else:
            print('network config:', wifi.ifconfig()) 

if __name__ == '__main__':
    do_connect()
```

## 工程经验

关于在连接WIFI上遇到的一些坑，以及为什么代码要这么写，参见文章：
[MicroPython-ESP32之更合理的建立wifi连接-1Z实验室](https://www.jianshu.com/p/0613f3f3f4ba)