# 第8章 读写文件

## 8.1 文件与文件路径

系统路径(Windows用反斜杠\，而OS X和Linux用正斜杠做路径分隔符)：

> C:\Windows\System32  # Windows path  
> /usr/bin             # OSX、Linux path  

挂载驱动器：

> D:\                  # Windows DVD Driver  
> /Volumnes            # OSX DVD Driver  
> /mnt                 # Linux DVD Driver  

注意，Windows和OS X的路径是不区分大小写的  
但是，Linux系统的路径区分大小写  

### 8.1.1 Windows上的倒斜杠以及OS X和Linux上的正斜杠

下的输出，是在Windows环境的结果。如果在OS X或Linux环境，输出为'usr/bin/spam'  

```python
>>> import os
>>> os.path.join('usr','bin', 'spam')
'usr\\bin\\spam'

>>> myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
>>> for filename in myFiles:
>>>     print(os.path.join('D:\\pyAuto', filename))
D:\pyAuto\accounts.txt
D:\pyAuto\details.csv
D:\pyAuto\invite.docx
```

### 8.1.2 当前工作目录

```python
>>> import os
>>> os.getcwd()
'C:\\Program Files\\Python310'
>>> os.chdir('D:\\pyAuto')
>>> os.getcwd()
'D:\\pyAuto'
>>> os.chdir('NotExistsFolder')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    os.chdir('NotExistsFolder')
FileNotFoundError: [WinError 2] 系统找不到指定的文件。: 'NotExistsFolder'
```

### 8.1.3 绝对路径与相对路径

绝对路径，是从系统盘的根文件夹开始的  
相对路径，是相对于程序的当前工作目录  
点(.)，是当前工作目录  
点点(..)，是父文件夹目录

相对路径的.\是可选的  

### 8.1.4 用os.makedirs()创建新文件夹

```python
>>> import os
>>> os.makedirs('D:\\pyAuto\\walnut\\waffles')
```

检查系统目录D:\\pyAuto\\walnut\\waffles，多层目录都创建了新的文件夹  

### 8.1.5 os.path()模块

[os.path模块的完整文档](https://docs.python.org/3/library/os.path.html)  

### 8.1.6 处理绝对路径和相对路径

os.path模块包含了处理绝对路径和相对路径的一些函数  
因为Windows系统和OS X、Linux系统的路径分隔符不同，故封装在os.path.sep变量  

```python
>>> import os
>>> os.path.abspath('.')
'D:\\pyAuto'
>>> os.path.abspath('.\\Scripts')
'D:\\pyAuto\\Scripts'
>>> os.path.abspath('.\\walnut')
'D:\\pyAuto\\walnut'
>>> os.path.isabs('.')
False
>>> os.path.isabs(os.path.abspath('.'))
True

>>> os.path.relpath('D:\\pyAuto', 'D:\\')
'pyAuto'
>>> os.path.relpath('D:\\pyAuto', 'D:\\test')
'..\\pyAuto'
>>> os.getcwd()
'D:\\pyAuto'

>>> path = 'C:\\Windows\\System32\\calc.exe'
>>> os.path.basename(path)
'calc.exe'
>>> os.path.dirname(path)
'C:\\Windows\\System32'
>>> os.path.split(path)
('C:\\Windows\\System32', 'calc.exe')
>>> path.split(os.path.sep)
['C:', 'Windows', 'System32', 'calc.exe']
```

如果是OS X和Linux系统：

```python
>>> import os
>>> '/usr/bin'.split(os.path.sep)
['', 'usr', 'bin']
```

### 8.1.7 查看文件大小和文件夹内容

```python
>>> import os
>>> os.path.getsize('C:\\Windows\\System32\\calc.exe')
27648
>>> os.listdir(os.getcwd())
['6_3_pw.py', '6_4_bulletPointAdder.py', 'pw.bat', 'test.py', 'walnut']

>>> for filename in os.listdir(os.getcwd()):
>>>     totalSize = totalSize + os.path.getsize(os.path.join(os.getcwd(), filename))
>>> totalSize
8642235
```

### 8.1.8 检查路径有效性

```python
>>> os.path.exists('D:\\pyAuto')
True
>>> os.path.exists('D:\\pyAuto_fake')
False
>>> os.path.isdir('D:\\pyAuto_fake')
False
>>> os.path.isdir('D:\\pyAuto')
True
>>> os.path.isdir('D:\\pyAuto\\test.py')
False
>>> os.path.isfile('D:\\pyAuto\\test.py')
False
>>> os.path.isfile('D:\\pyAuto')
False
>>> os.path.exists('H:\\')
False
```

## 8.2 文件读写过程

Python读写文件的3个步骤：

- 调用open()函数，返回一个File对象  
- 调用File对象的read()或write()方法  
- 调用File对象的close()方法，关闭文件  

open()函数第一个参数是文件完整目录，包括文件名；还有一个可选参数，是打开文件的模式('r'-只读；'w'-写；'a'-末位附加)  
如果是以'w'写模式打开一个已经存在的文件，则文件原有内容会被删除并完全覆写  

read()方法将文件全部内容作为一个字符串返回；readlines()返回一个字符串列表，其中每个字符串是文件内容中的一行  

### 8.2.1 用open()函数打开文件

### 8.2.2 读取文件内容

### 8.2.3 写入文件

如果文件不存在，Python会创建一个新的空文件  
读取或写入文件后，调用close()方法后，才能再次打开该文件进行读写  

```python
>>> helloFile = open('D:\\pyAuto\\hello.txt')
>>> helloContent = helloFile.read()
>>> helloContent
'Hello world!'
>>> linesFile = open('D:\\pyAuto\\lines.txt')
>>> linesFile.read()
''
>>> linesFile.readlines()
["When, in disgrace with fortune and men's eyes,\n", 'I all alone beweep my outcase state,\n', 'And trouble deaf heaven with my bootless cries,\n', 'And look upon myself and curse my fate,\n', '... ...']
>>> baconFile = open('bacon.txt', 'w')
>>> baconFile.write('This is a file that Python created!!!\n')
37
>>> baconFile.close()
>>> baconFile = open('bacon.txt', 'a')
>>> baconFile.write('Bacon is not a vegetable.')
25
>>> baconFile.close()
>>> baconFile = open('bacon.txt')
>>> baconContent = baconFile.read()
>>> baconFile.close()
>>> baconContent
'This is a file that Python created!!!\nBacon is not a vegetable.'
>>> print(baconContent)
This is a file that Python created!!!
Bacon is not a vegetable.
```

## 8.3 用shelve模块保存变量

利用shelve模块，可以将Python程序中的变量保存到二进制的shelf文件中  

```python
>>> import shelve
>>> shelfFile = shelve.open('mydata')
>>> cats = ['Zophie', 'Pooka', 'Simon']
>>> shelfFile['cats'] = cats
>>> shelfFile.close()
```

如果'mydata'文件不存在，shelve模块会创建新文件  
Windows系统下，会创建三个文件：'mydata.bak', 'mydata.dat', 'mydata.dir'  
OS X系统下，指挥创建一个文件：'mydata.db'  

```python
>>> shelfFile = shelve.open('mydata')
>>> type(shelfFile)
<class 'shelve.DbfilenameShelf'>
>>> shelfFile['cats']
['Zophie', 'Pooka', 'Simon']
>>> shelfFile.close()
```

shelf值有keys()和values()方法，返回的值类似列表的值，但不是真正的列表  
将返回的值传给list()函数，得到列表形式的值  

```python
>>> shelfFile = shelve.open('mydata')
>>> list(shelfFile.keys())
['cats']
>>> list(shelfFile.values())
[['Zophie', 'Pooka', 'Simon']]
>>> shelfFile.close()
```

## 8.4 用pprint.pformat()函数保存变量

```python
>>> import os
>>> os.getcwd()
'C:\\Program Files\\Python310'
>>> os.chdir('D:\\pyAuto')
>>> os.getcwd()
'D:\\pyAuto'
>>> import pprint
>>> cats = [{'name':'Zophie', 'desc':'chubby'}, {'name':'Pooka', 'desc':'fluffy'}]
>>> pprint.pformat(cats)
"[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]"
>>> fileObj = open('myCats.py','w')
>>> fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
83
>>> fileObj.close()
```

刚才保存的*.py脚本文件，支持导入其他脚本文件

```python
>>> import myCats
>>> myCats.cats
[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]
>>> myCats.cats[0]
{'desc': 'chubby', 'name': 'Zophie'}
>>> myCats.cats[1]
{'desc': 'fluffy', 'name': 'Pooka'}
>>> myCats.cats[0]['name']
'Zophie'
```

## 8.5 项目：生成随机的测验试卷文件

### 第1步：将测验数据保存在一个字典中

### 第2步：创建测验文件，并打乱问题的顺序

### 第3步：创建答案选项

### 第4步：将内容写入测验试卷和答案文件

参考脚本文件#8_5_randomQuizGenerator.py  

## 8.6 项目：多重剪贴板

### 第1步：注释和shelf设置

### 第2步：用一个关键字保存剪贴板内容

### 第3步：列出关键字和加载关键字的内容

参考示例脚本#8_6_mcb.pyw  
仿照第6章的批处理配置，  
将文件6_3_pw.py和pw.bat放入目录D:\pyAuto下  
输入py mcb.pyw &lt;argv[1]&gt; &lt;argv[2]&gt;：  

> py mcb.pyw save spam # 剪贴板中当前内容用关键字spam保存  
> py mcb.pyw spam      # 将关键字spam对应文本重新加载到剪贴板中  
> py mcb.pyw list      # 将所有关键字的列表复制到剪贴板中  

如果将脚本所在目录，配置在环境变量中，可以在“运行”对话框输入以下命令：  

> mcb spam save  
> mcb spam  
> mcb list  

检查是否指定的目录下，是否生成了命名的二进制文件mcbdata  
如果只制定了二进制文件名，而没有指定具体目录，则默认会将二进制数据文件生成到系统默认的个人文件夹下  
建议指定具体的生成目录，如shelve.open('D:\\pyAuto\\mcbdata')  

## 8.7 小结

os，sys，shelve，pyperclip模块，os.path，read()，readlines()

## 8.8 习题

## 8.9 实践项目

### 8.9.1 扩展多重剪贴板

参考示例脚本#8_9_mcbAdv.pyw  
支持delete和delete &lt;keyword&gt;，可以删除shelf中保存的关键字  

首先，向二进制文件添加多个关键字及粘贴的内容  

> mcbAdv save spam1  
> mcbAdv save spam2  
> mcbAdv save spam3  

然后，删除一个关键字  

> mcbAdv delete spam2  

可以通过IDLE环境检查关键字是否删除  
最后，删除所有关键字  

> mcbAdv delete  

### 8.9.2 疯狂填词

参考示例脚本#8_9_madLibs.py

### 8.9.3 正则表达式查找

参考示例脚本#8_9_searchPath.py， 输入'C#'，脚本以此为正则表达式，匹配当前目录下的文本内容  
