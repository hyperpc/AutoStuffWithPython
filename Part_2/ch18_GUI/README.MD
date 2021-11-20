# 第18章 用GUI自动化控制键盘和鼠标

pyautogui模块包含一些函数，可以模拟鼠标移动、按键和滚动鼠标滚轮。  
这里只介绍一些功能子集，其他请参考[完整文档](https://pyautogui.readthedocs.io/)  

## 18.1 安装pyautogui模块

在安装pyautogui模块之前，需要线安装它的一些依赖模块：

- Windows环境：无依赖模块  
- OS X环境：sudo pip3 install pyobjc-framework-Quartz, sudo pip3 install pyobjc-core, sudo pip3 install pyobj  
- Linux环境：sudo pip3 install python3-xlib, sudo apt-get install scrot, sudo apt-get install python3-tk, sudo apt-get install python3-dev  

最后，再安装pyautogui模块：pip install pyautogui  

## 18.2 走对路

为防止模块自动化执行太快，导致其他程序跟不上反应，需要以下几种方式来防止或回复GUI自动化问题  

### 18.2.1 通过注销关闭所有程序

通过操作系统的注销，会丢失所有未保存的工作，但至少不需要等计算机完全重启  

### 18.2.2 暂停和自动防故障装置

pyautogui.PAUSE = 1.5可以在函数调用之后，暂停1.5秒。非pyautogui指令不会停顿  
将鼠标移动至屏幕左上角，将导致pyautogui.FailSafeException异常。自动防故障功能将停止程序  
设置pyautogui.FAILSAFE=False，禁止这项功能；True为启动自动防故障功能  

## 18.3 控制鼠标移动

pyautogui的鼠标函数使用x、y坐标，屏幕左上角为坐标原点  
x坐标水平向右增加，y坐标竖直向下增加。所有坐标都是正整数，没有负数坐标  
分辨率是屏幕的宽、高有多少像素。  
分辨率1920x1080对应的左上角坐标为(0,0)，右下角坐标为(1919,1079)  

ptautogui.size()返回屏幕的分辨率：  

```python
>>> import pyautogui
>>> pyautogui.size()
Size(width=1920, height=1080)
>>> width,height=pyautogui.size()
>>> print(width, height)
1920 1080
```

参考示例脚本#18_3_mouse_position.py  

### 18.3.1 移动鼠标

pyautogui.moveTo(x, y, duration)函数，将鼠标立即移动到指定位置(x,y)，可选的duration是整数或浮点数，指移动需要的时间，默认为0。  
pyautogui.moveRel(x, y, duration)函数，将鼠标相对于当前位置坐标移动，x为水平移动像素数，y为数值移动像素数；正数为自左向右或自上而下移动，负数为自右向左或自下而上移动；可选的duration整数或浮点数，指移动需要的时间，默认为0。  

### 18.3.2 获取鼠标位置

pyautogui.position()返回函数调用时，鼠标当前的位置坐标x,y组成的元组  

## 18.4 项目：“现在鼠标在哪里？”

程序要求：  

- 获得鼠标当前的xy坐标  
- 鼠标移动时，更新xy坐标  

代码实现：  

- 调用函数，获得当前坐标
- 在屏幕上打印回退字符。删除以前打印的坐标  
- 处理异常。让用户能按键退出
参考示例脚本#18_4_mouseNow.py  

### 第1步：导入模块

### 第2步：编写退出代码和无限循环

捕获KeyboardInterrupt异常，调用推出函数  

### 第3步：获取并打印鼠标坐标

坐标值最高在4位数，所以可以rjust(4)美化打印输出  
使用\\b退格字符，结合flush，屏幕才会刷新  

## 18.5 控制鼠标交互

### 18.5.1 点击鼠标

pyautogui.click(x, y, button)函数，(x,y)为发生点击鼠标的坐标，可选参数button，值为"left"，"right"或"middle"  
pyautogui.click()是对pyautogui.mouseDown()和pyautogui.mouseUp()的封装
pyautogui.doubleClick()、pyautogui.rightClick()、pyautogui.middleClick()

```python
pyautogui.click(10,5)
```

### 18.5.2 拖动鼠标

pyautogui.dragTo(x, y, duration)、pyautogui.dragRel(x, y, duration)  
建议总是提供duration参数，以防止拖动过快，导致拖动失效  

参考示例脚本#18_5_2_spiralDraw.py  
通过画图程序，选中画笔，演示鼠标移动轨迹  

### 18.5.3 滚动鼠标

pyautogui.scroll(int)，向上或向下滚动多少单位。  
针对不同的系统或应用，单位的意义并不相同  
参数为正数，向上滚动；负数为向下滚动  
参考示例脚本#18_5_3_mouseScroll.py  

## 18.6 处理屏幕

Linux系统中，需要安装scrot模块，才能使用pyautogui的屏幕快照的功能  
Windows和OS X系统已经支持该功能  
参考示例脚本#18_6_screenshot.py  

### 18.6.1 获取屏幕快照

屏幕快照的图像是完全不透明的，所以imgObj.getpixel((x,y))返回的像素颜色值是没有alpha值得  

### 18.6.2 分析屏幕快照

pyautogui.pixelMatchesColor(x, y, (r, g, b))将比较(x,y)坐标的颜色和传入的RGB颜色值，如果完全一致，将返回True；否则返回False  

## 18.7 项目：扩展mouseNew程序

扩展18.4节的程序：在输出信息中添加坐标处的颜色值  
如果配合pixelMatchesColor()函数，使得给GUI自动化脚本添加颜色检查更容易  
参考示例脚本#18_7_mouseNowColor.py  

## 18.8 图像识别

pyautogui.locateOnScreen(buttonFilePath)返回第一个匹配的图片左上角位置所在屏幕的坐标，以及宽、高的值  
> Box(left=14, top=49, width=28, height=35)  
pyautogui.locateAllOnScreen(buttonFilePath)返回一个Generator，转换成list()，包含所有匹配的图片左上角位置所在屏幕的坐标，以及宽、高的值  
pyautogui.center((x, y, width, height))返回给定区域的中心点坐标  

## 18.9 控制键盘

### 18.9.1 通过键盘发送一个字符串

pyautogui.typewrite('Hello world!', 0.25)向计算机发送虚拟按键。  
这些按键产生的效果，取决于当前的焦点窗口和文本输入框。  
第一个参数是传递的按键，大写的字母键，会自动模拟shift按下的效果  
第二个参数是第一个参数传入的所有击键之间的间隔时间  

pyautogui.typewrite('\r\n', 0.25)表示换行

### 18.9.2 键名

通过pyautogui.KEYBOARD_KEYS列表，查看模块接受的所有可能的键字符串  
|键盘键字符串|含义|
|:---|:---|
|'a','b','c','A','B','C','1','2','3','!','@','#'等|单个字符的键|
|'enter' or 'return' or '\n'|回车键|
|'esc'|Esc键|
|'shiftleft','shiftright'|左、右shift键|
|'altleft','altright'|左、右alt键|
|'ctrlleft','ctrlright'|左、右ctrl键|
|'tab' or '\t'|Tab键|
|'backspace','delete'|Baclspace和Delete键|
|'pageup','pagedown'|Page Up和Page Down键|
|'home','end'|Home和End键|
|'up','down','left','right'|上、下、左、右箭头键|
|'f1','f2','f3',等|F1至F12功能键|
|'volumemute','volumedown','volumeup'|静音、减小音量、增大音量|
|'pause'|Pause键|
|'capslock','numlock','scrolllock'|CapsLock，NumLock和ScrollLock|
|'insert'|Ins或Insert键|
|'printscreen'|PrtSc或Print Screen键|
|'winleft','winright'|左、右Windows徽标键(Windows系统)|
|'command'|Command键(OS X系统)|
|'option'|Option键(OS X系统)|

### 18.9.3 按下和释放键盘

pyautogui.keyUp(key)，pyautogui.keyDown(key)以及封装的函数pyautogui.press(key)
pyautogui.press(key)适合模拟单个按键的击键动作  

### 18.9.4 热键组合

热键或组合键是按键组合。  
组合按键Ctrl-c：

```python
# 1
pyautogui.keyDown('ctrl')
pyautogui.keyDown('c')
pyautogui.keyUp('c')
pyautogui.keyUp('ctrl')
# 2
pyautogui.hotkey('ctrlleft', 'c')
```

IDLE环境的快捷键：  

```python
>>> import pyautogui, time
>>> def commentAfterDelay():
>>>     pyautogui.click(600,600)
>>>     time.sleep(5)
>>>     pyautogui.typewrite('In IDLE, Alt-3 comments out a line.')
>>>     time.sleep(2)
>>>     pyautogui.hotkey('alt', '3')
>>> commentAfterDelay()
```

## 18.10 复习PyAutoGUUI的函数

moveTo(x,y)将鼠标移动到指定到x、y坐标  
moveRel(xOffset,yOffset)相对于当前位置移动坐标  
dragTo(x,y)按下左键移动鼠标  
dragRel(xOffset,yOffset)按下左键，相对于当前位置移动坐标  
click(x,y,button)模拟点击(默认左键)  
rightClick()模拟右键点击  
middleClick()模拟中键点击  
doubleClick()模拟左键双击  
mouseDown(x,y,button)模拟在x、y处按下指定鼠标按键  
mouseUp(x,y,button)模拟在x、y处释放指定键  
scroll(units)模拟滚动鼠标滚轮。正数表示向上滚动，负数向下滚动  
typewrite(message)键入给定消息字符串中的字符  
typewrite([key1, key2, key3])键入给定键字符串  
press(key)按下并释放给定键  
keyDown(key)模拟按下给定键  
keyUp(key)模拟释放给定键  
hotkey([key1, key2, key3])模拟按顺序按下给定键字符串，然后以相反顺序释放  
screenshot()返回屏幕快照的Image对象  

## 18.11 项目：自动填表程序

程序要求：  

- 点击表单的第一个文本字段  
- 遍历表单，在每一个输入栏键入信息  
- 点击Submit按钮  
- 用下一组数据重复这个过程  

代码实现：  

- 调用pyautogui.click()函数，点击表单和Submit按钮  
- 调用pyautogui.typewrite()函数，在输入栏输入文本  
- 处理KeyboardInterrupt异常，这样用户按下Ctrl-C组合键退出  
参考示例脚本#18_11_formFiller.py  

### 第1步：弄清楚步骤

### 第2步：建立坐标

### 第3步：开始键入数据

### 第4步：处理选择列表和单选按钮

### 第5步：提交表单并等待

## 18.12 小结

## 18.13 习题

## 18.14 实践项目

### 18.14.1 看起来很忙

编写一段脚本，每隔10秒稍微动一下鼠标，以防止屏幕锁屏。
参考示例脚本#18_14_1_mouseMove.py  

### 18.14.2 即时通信机器人

打开Google Talk、Skype、Yahoo Messenger、AIM或其他即时通信应用。  
在联系人列表搜索某个测试联系人，并发送一条通知消息。  
程序可以处理异常情况，如好友离线，聊天窗口的不同位置，或确认对话框打断输入信息。  
必须使用屏幕快照，指导GUI交互，并在发送虚拟按键前采用各种检测方式  

### 18.14.3 玩游戏机器人指南

创建一个Python GUI自动化程序，玩'Sushi Go Round'游戏。  
程序模拟点击正确的成分按钮，填写客户的寿司订单。填写无错订单越快，得分越高。  
这样利用GUI自动化作弊得高分。  
这会涉及本章的很多主题，也涉及PyAutoGUI的基本图像识别功能  
