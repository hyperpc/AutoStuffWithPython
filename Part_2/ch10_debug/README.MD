# 第10章 调试

首先，查看日志和断言。越早发现缺陷，越容易修复  
其次，使用调试器。  

## 10.1 抛出异常

抛出异常使用raise语句：

- raise关键字  
- 对Exception函数的调用  
- 传递给Exception函数的字符串，包含有用的出错信息  

使用try和except语句，可以优雅地处理错误，而不是让整个程序崩溃  
参考示例脚本#10_1_raise.py  

## 10.2 取得反向跟踪的字符串

反向跟踪，包含了出错信息、导致该错误的代码行号，及导致该错误的函数调用的序列。这个序列就是“调用栈”  
参考示例脚本#10_2_Exception.py  

使用traceback.format_exc()，可以优雅地处理该异常，不会是程序崩溃，甚至可以将反向跟踪信息写入日志文件  
参考示例代码#10_2_errLog.py  

## 10.3 断言

assert语句：

- assert关键字  
- 条件表达式，结果为True或False  
- 逗号  
- 条件结果为False时显示的字符串  

```python
>>> podBayDoorStatus = 'open'
>>> assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
>>> podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
>>> assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
AssertionError: The pod bay doors need to be "open".
```

断言针对的时程序员的错误，而非用户错误。对于那些可恢复的错误(如文件未找到，或用户输入的数据无效等)，请抛出异常，而不是用assert语句检测  

### 10.3.1 在交通灯模拟中使用断言

```python
>>> market_2nd = {'ns':'green', 'ew':'red'}
>>> mission_16th = {'ns':'red', 'ew':'green'}
>>> def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
>>> switchLights(market_2nd)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    switchLights(market_2nd)
  File "<pyshell#13>", line 9, in switchLights
    assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
AssertionError: Neither light is red! {'ns': 'yellow', 'ew': 'green'}
```

两个方向都没有红灯，意味着两个方向的车都可以走。这是不符合程序预期的  

### 10.3.2 禁用断言

在运行Python时，传入-O选项，可禁用断言  

## 10.4 日志

日志模块logging  

### 10.4.1 使用日志模块

```python
>>> import logging
>>> logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
```

### 10.4.2 不要用print()调试

print()知识和在开发过程中，程序员临时调试用的，且代码中过多的print()不易删除  
logging模块使得显示和隐藏日志信息之间的切换变容易  

### 10.4.3 日志级别

|级别|日志函数|描述|
|:---|:---|:---|
|DEBUG|logging.debug()|最低级别。用于小细节。通常只在诊断问题时，才会关心这些信息|
|INFO|logging.info()|用于记录程序中一般事件的信息，或确认一切工作正常|
|WARNING|logging.warning()|用于表示可能的问题，它不会阻止程序的工作，但将来可能会|
|ERROR|logging.error()|用于记录错误，它导致程序做某事失败|
|CRITICAL|logging.critical()|最高级别。用于表示致命错误，它导致或将要导致程序完全停止工作|

```python
>>> import logging
>>> logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
>>> logging.debug('Start of program')
 2021-10-30 22:24:08,264 - DEBUG - Start of program
>>> def factorial(n):
    logging.debug('Start of factorial(%s%%)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is '+ str(total))
    logging.debug('End of factorial(%s%%)' % (n))
    return total

>>> print(factorial(5))
 2021-10-30 22:28:26,824 - DEBUG - Start of factorial(5%)
 2021-10-30 22:28:26,895 - DEBUG - i is 1, total is 1
 2021-10-30 22:28:26,911 - DEBUG - i is 2, total is 2
 2021-10-30 22:28:26,929 - DEBUG - i is 3, total is 6
 2021-10-30 22:28:26,946 - DEBUG - i is 4, total is 24
 2021-10-30 22:28:26,962 - DEBUG - i is 5, total is 120
 2021-10-30 22:28:26,977 - DEBUG - End of factorial(5%)
120
>>> logging.debug('End of program')
 2021-10-30 22:29:01,427 - DEBUG - End of program
```

### 10.4.4 禁用日志

disable()函数传入一个日志级别，就会禁止该级别和更低级别的所有日志消息  

```python
>>> logging.disable(logging.CRITICAL)
```

### 10.4.5 将日志记录到文件

```python
>>> logging.basicConfig(filename='myProgLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
>>> logging.disable(logging.CRITICAL)
```

## 10.5 IDLE的调试器

在IDLE窗口菜单，点击Debug->Debugger，打开调试器窗口  
勾选4个复选框：Stack、Locals、Source和Globals，窗口将显示全部调试信息  

### 10.5.1 GO

GO按钮是让程序从当前处继续执行  

### 10.5.2 Step

Step按钮是让调试器执行下一行代码，然后再次暂停  
如果下一行代码是调用某一个函数，将会跳入下一个函数的第一行暂停  

### 10.5.3 Over

Over按钮是让调试器执行下一行代码，然后再次暂停  
如果下一行代码是调用某一个函数，不会跳入下一个函数内暂停，而是拿到函数的返回值后暂停  

### 10.5.4 Out

Out按钮是继续执行，直到当前函数退出到外层调用代码处暂停  

### 10.5.5 Quit

Quit按钮不会继续执行剩余程序，终止程序  

### 10.5.6 调试一个数字相加的程序

- 启动调试窗口，然后在IDLE窗口打开脚本#10_5_6_buggyAddingProggram.py  
- 按下F5或选择Run -> Run Module(Debug -> Debugger，选中调试窗口的4个复选框)
- 程序启动后，会在第一行暂停  
- 对于print()函数，点击Over按钮，而不是Step按钮  
- 按步骤调试，尝试发现任何异常的代码  

### 10.5.7 断点

在新的文本编辑器窗口，可以在需要的代码处，设置断点  
参考示例脚本#10_5_6_coinFlip.py，并在第7行设置断点  

## 10.6 小结

断言、异常、日志和调试器。try和except语句，logging模块  

## 10.7 习题

## 10.8 实践项目

### 调试硬币抛掷

参考示例脚本#10_8_coinGame.py  

issue on sample code:

- have no exit condition in while loop  
- int not equals with string  
