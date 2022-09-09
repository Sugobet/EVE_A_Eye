# EVE A Eye

A Eye基于python、open-cv、pywin32等类库

主要用于搭建eve手游预警机系统，支持多模拟器，支持监测多星系，支持发送游戏指定频道预警、微信预警

### 安装说明：
>1.安装python,安装包放在脚本主目录，也可自行百度教程

>2.请将脚本目录路径添加到环境变量Path，<u>不会可忽视</u>

>3.双击主目录下的 '运行一次即可.bat' , 等待安装完成即可

### 微信设置:
>1.若要使用微信预警，请自行下载安装登录电脑微信客户端，并在脚本中修改wx_groupName参数为指定群聊或人

>2.将指定微信群聊或人的聊天窗口设置为独立窗口中打开，这一步至关重要，且不要最小化该窗口，否则将会导致微信预警失败

### 模拟器设置:
>1.目前已知支持的模拟器有雷电、夜神模拟器，<u>原理上，只要支持adb的模拟器均可，可自行百度自己使用的模拟器是否支持adb</u>

>2.请将模拟器分辨率调整为 手机版->540×960，请务必是这个分辨率

### 游戏设置:
>1.预警机请安放至外太空，建议配合隐身安放至星门附近

>2.请确保  游戏 总览->高级设置->显示分类标签   为勾选

>3.总览中 请任意选择一个标签，将舰船、建筑、天体、信号、其他、诱导   <u>全部取消勾选</u>, 声望 勾选罪犯-全部、中立-全部、敌对-全部  保存，并切换至该标签

>4.请将'本地人数列表'移动至游戏右下角，确保是最右下角，不能有一点偏差！

### 脚本设置 & 注意事项:
>1.devices参数设置, ,,有多个模拟器预警机可直接复制以下然后粘贴

    '星系名': [        # 星系名        请勿出现中文或中文字符以及特殊字符
        '127.0.0.1:62001',      # cmd输入adb devices查看模拟器地址
        False       # 没卵用，但不能少也不能改
    ],

>在确保预警机的模拟器处于运行状态中时，打开cmd  输入adb devices

    C:\Users\sugob\Desktop\evescript\adb_version>adb devices
    List of devices attached
    * daemon not running. starting it now on port 5037 *
    * daemon started successfully *
    127.0.0.1:62001 device

>请复制如 <u>127.0.0.1:62001</u>  的字符串到脚本中对应星系的devices参数中

#### 开启顺序：微信 or 模拟器 后，进入游戏设置好（安放外太空，打开总览，将本地人数列表移动至最右下角），后，双击 ‘点我运行脚本.bat’即可运行脚本
/

/


作者: Sugobet

QQ: 321355478

脚本开源免费，使用前请先查阅readme.md文档



### 感谢使用，觉得好用的话，希望能给个Star


### 捐赠名单 (按时间排序)
<img src="http://a1.qpic.cn/psc?/V12Xu6Mm26x6GL/ruAMsa53pVQWN7FLK88i5jVNuhzjJnHl7ojd6hbq*UE8G0jQ1BzCueV*99qhA275MB5ITIwGAHZqYabkfICXe*lcOd9b*VwaMnJB0Soa3FQ!/c&ek=1&kp=1&pt=0&bo=2gScBtoEnAYDEDU!&tl=1&vuin=1749445382&tm=1660014000&dis_t=1660016830&dis_k=0377483ea5dd3499d7266097d58fe6b3&sce=60-2-2&rf=0-0" width="30%">
<img src="http://a1.qpic.cn/psc?/V12Xu6Mm26x6GL/ruAMsa53pVQWN7FLK88i5jVNuhzjJnHl7ojd6hbq*UHSftihZRfU4QSDMTikpSgT6q9ISwYS*B09oSw*06s7NE0sJdK3DBFo4kowDq5YA4A!/c&ek=1&kp=1&pt=0&bo=OASQBjgEkAYWECA!&t=5&tl=3&vuin=1749445382&tm=1660014000&dis_t=1660016830&dis_k=fd8d61a70b1e3bba2b1a241a0c664653&sce=60-2-2&rf=0-0" width="30%">

>感谢各位老板的捐赠与支持

>1.天空 -> 14亿isk ---2022.8.8

>2.匿名用户1 -> 300 RMB ---2022.8.16

>3.匿名用户2 -> 30 RMB ---2022.8.30

>4.匿名用户3 -> 30 RMB ---2022.8.30
