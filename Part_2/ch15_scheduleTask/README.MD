# 第15章 保持时间、计划任务和启动程序

Python的time、datetime模块，可以根据计算机的始终，调度程序在特定的日期和时间运行，或定期执行  
subprocess和threading模块，可以按时启动某些程序  

## 15.1 time模块

### 15.1.1 time.time()函数

UNIX纪元是编程中经常参考的时间：1970年1月1日0点整，即协调世界时UTC  
time.time()函数返回自那一刻以来的秒数，是一个浮点值，被称为UNIX纪元时间戳  
纪元时间戳可以用来剖析代码，即测量一段代码的运行时间  
参考示例代码#15_1_time.py  
> 另一种剖析代码的方法是利用cProfile.run()函数，会提供更详细的信息  
> 请参考[cProfile.run()](https://docs.python.org/3/library/profile.html)  

### 15.1.2 time.sleep()函数

time.sleep()将阻塞(也就是说，不会返回或让程序执行其他代码)，直到传给time.sleep()的秒数流逝  
值得注意的是，IDLE中Ctrl+C不会中断time.sleep()的调用，而是在秒数流逝后，抛出KeyboardInterruptException  
一个变通方法是：当sleep的描述较长时，将它放入for循环中，变为sleep()1到3秒。这样，就无需等待所有时间的流逝，而是很快看到抛出的异常  

## 15.2 数字四舍五入

Python内置的round()函数，接收两个参数，第一个是需要舍入的数，第二个是需要传入到小数点后多少位  
如果省略第二个参数，结果将会是跟舍入数字最接近的整数  
参考示例脚本#15_1_2_round.py  

## 15.3 项目：超级秒表

程序要求：  

- 记录从按下回车键开始，每次按键的时间，每次按键都是一个新的"单圈"  
- 打印圈数、总时间和单圈时间  

代码任务：

- 程序开始时，调用time.time()得到当前时间，将其保存为一个时间戳。每个单圈开始时也一样  
- 记录圈数，每次按下回车键时+1  
- 用时间戳相减，得到计算流逝的时间  
- 捕获KeyboardInterruptException，这样用户通过Ctrl+C可以退出程序  

参考示例脚本#15_3_stopwatch.py  

### 第1步：设置程序来记录时间

### 第2步：记录并打印单圈时间

### 第3步：类似程序的想法

- 创建简单的工时表应用，输入一个工人名字，用当前时间作为这个工人进入或离开的时间  
- 位程序添加一个功能，显示自一项处理开始以来的时间，诸如利用requests模块进行的下载  
- 间歇性检查程序已运行的时间，并为用户提供一个机会，取消耗时长的任务  

## 15.4 datetime模块

datetime模块，以更易读的方式表示时间  
参考示例脚本#15_4_0_datetime.py  

### 15.4.1 timedelta数据类型

表示一段时间，而不是某一时间点  
该函数接收关键字参数weeks、days、hours、minutes、seconds、milliseconds和microseconds。  
没有month和year关键字参数，因为month和year是可变的时间，依赖于特定的年月  
timedelta对象拥有的总时间，以天、秒和微妙来表示  
将timedelta对象传入str()，会得到格式良好的字符串表示  
参考示例脚本#15_4_1_timedelta.py  

### 15.4.2 暂停直至特定日期

time.sleep()让程序暂停若干秒  
在while循环中，可以控制某个程序，直到某个特定日期再继续执行  

### 15.4.3 将datetime对象转换为字符串

strftime()方法，可以将datetime对象，格式化为可读的字符串(支持传入任何需要的斜线和冒号)  
其中的f，为format的缩写  

strftime()指令：  
|strftime指令|含义|
|:---|:---|
|%Y|带世纪的年份，如'2014'|
|%y|不带世纪的年份，'00'至'99'(表示1970至2069)|
|%m|数字表示的月份，'01'至'12'|
|%B|完整的月份，如'November'|
|%b|简写的月份，如'Nov'|
|%d|一月中的第几天，'01'至'31'|
|%j|一年中的第几天，'001'至'366'|
|%w|一周中的第几天，'0'(周日)至'6'(周六)|
|%A|完整的周几，如'Monday'|
|%a|简写的周几，如'Mon'|
|%H|小时(24小时时钟)，'00'至'23'|
|%I|小时(12小时时钟)，'01'至'12'|
|%M|分，'00'至'59'|
|%S|秒，'00'至'59'|
|%p|'AM'或'PM'|
|%%|字符'%'|

参考示例脚本#15_4_3_strftime.py  

### 15.4.4 将字符串转换成datetime对象

strptime()函数与strftime()作用相反。它将根据传入的格式字符串和日期字符串，解析出datetime对象  
函数名中的p，表示parse  
参考示例脚本#15_4_4_strptime.py  

## 15.5 回顾Python的时间函数

- UNIX纪元时间戳，1970年1月1日午夜0点(UTC)以来的秒数  
- datetime对象  
- timedelta对象  
- time.time()函数  
- time.sleep()函数  
- datetime.datetime(year, month, day, hour, minute, second)  
- datetime.datetime.now()  
- datetime.datetime.fromtimestamp(epoch)，epoch为时间戳  
- datetime.timedelta(weeks, days, hours, minutes, seconds, milliseconds, microseconds)  
- timedelta().total_seconds()  
- strftime(format)  
- strptime(time_string, format)  

## 15.6 多线程

Python提供的Threading模块，支持将耗时的模块放入一个单独的线程  
这样就不会影响其他线程的程序继续执行  
参考示例代码#15_6_0_threadingDemo.py  

### 15.6.1 向线程的目标函数传递参数

threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep':' & '})  
Thread()方法的target参数传入调用的方法名，args参数传入常规的参数列表，kwargs参数传入关键字参数字典  
参考示例脚本#15_6_1_argv.py  

### 15.6.2 并发问题

当创建的多个线程，同时运行时，如果它们读写同一个变量，可能互相干扰，导致并发问题  
为避免此类并发问题，应确保新的Thread对象的目标函数，只访问其局部变量  

## 15.7 项目：多线程XKCD下载程序

根据第11章的类似代码，更新为#15_7_multiDownloadXkcd.py  

### 第1步：修改程序以使用函数

漫画地址url: https://xkcd.com/100/ 等
downloadXkcd(startComic, endComic)方法参数支持下载某一序列号段内的漫画  
requests模块根据url下载网页  
Beautiful Soup模块，根据CSS选择器语法bs4.select('#comic img')，提取图片地址  
迭代下载图片内容，并保存到当前目录下的xkcd文件夹下  

### 第2步：创建并启动线程

multipleDownload()方法创建一个线程列表  
下载url的序列号段为1到1400，迭代步长100  
故每次迭代的数字区间为1-100，101-200，201-300等  
每次得带都调用了新创建的Thread对象的start()方法，所以i性能对象都会立刻开始下载，然后迭代继续创建新的对象  
如果下载的序列区间较大时，有可能因网络等原因，而出现异常中断  

### 第3步：等待所有线程结束

希望所有下载线程完成下载后，统一执行后面的代码逻辑  
故，遍历线程列表中的所有线程对象，主线程调用每个线程对象的join()方法，将阻塞，直至线程结束  

## 15.8 从Python启动其他程序

Python内建的Popen()函数(p为process)，可以启动计算机中的其他程序  
如果打开同一个应用的多个实例，则这些实例运行在不同的进程  
每个进程可以有多个线程。不想线程存在并发的问题，进程无法读写另一进程的变量  
Popen()函数启动了其他的应用后，就立即返回一个Popen对象，被启动的应用和启动它的Python程序不在同一个线程中运行  
返回的Popen对象有poll()和wait()方法。  
poll()方法检查启动的应用是否执行完成：返回None，表示仍在运行；返回该进程的整数退出代码，表示应用终止(0为无错终止，非零为错误导致终止)  
wait()方法将阻塞主线程，等待启动的进程终止，其返回值为进程的整数退出代码，数字意义与poll()方法相同  
参考示例脚本#15_8_0_subprocess.py  

### 15.8.1 向Popen()传递命令行参数

Popen()还支持传入一个参数列表  
第一个参数时要启动的应用的可执行文件名；所有后续字符串为该程序启动时，传递给该程序的命令行参数。它将作为sys.argv的值使用  
参考示例脚本#15_8_0_subprocess.py  

### 15.8.2 Task Scheduler、launchd和cron

Task Scheduler是Windows上内置的调度程序，launchd是OS X的和cron属于Linux系统  
如果程序只需要稍作停顿，可以调用time.sleep()；或者，不借助操作系统，代码可以循环直到特定时间，每次循环时调用time.sleep(1)即可  

### 15.8.3 用Python打开网站

webbrowser.open()函数可以从程序启动Web浏览器，打开指定网址(参考第11章)  
而subprocess.Popen()只是打开浏览器应用程序  

### 15.8.4 运行其他Python脚本

如果要运行其他的Python脚本，可以向Popen()方法传入python.exe可执行文件的完整目录，以及脚本的目录即可  

```python
subprocess.Popen(['C:\\Python310\\python.exe', '.\\another.py'])
```

### 15.8.5 用默认的应用程序打开文件

操作系统会关联某些文件的默认打开程序，subprocess.Popen()也可以实现同样的功能  
(Windows: start；OS X: open；Linux: see)  
注意Windows上调用时，需要传入参数shell=True  
参考示例脚本#15_8_0_subprocess.py  

## 15.9 项目：简单的倒计时程序

程序要求：  

- 60秒倒数  
- 倒数至0时，播放声音文件(alarm.wav)  

代码实现：  

- 在显示每个倒计时数字之间，调用time.sleep(1)暂停一秒  
- 调用subprocess.Popen()，用默认的应用后层序播放声音文件  
参考示例脚本#15_9_countdown.py  

### 第1步：倒计时

### 第2步：播放声音文件

### 第3步：类似程序的思想

- 利用time.sleep()给用户一个机会，按下Ctrl-C取消的操作，如删除文件。  打印"Pres Ctrl-C to cancel"，然后用try...except语句处理所有KeyboardInterrupt异常  
- 对于长期的倒计时，可用timedelta对象测量直到未来某个时间点的天、时、分和秒数  

## 15.10 小结

time.time()，time.sleep()，threading.Thread()，subprocess.Popen()  
round()，start/open/see  

## 15.11 习题

## 15.12 实践项目

### 15.12.1 美化的秒表

将本章的秒表程序输出的结果，进行格式化对其  
参考示例脚本#15_12_stopwatchAdv.py  

### 15.12.2 计划的web漫画下载

通过操作系统的调度程序，每天运行一次我们的程序，去漫画网站里检查。  
如果有更新的漫画，就下载到本地  
