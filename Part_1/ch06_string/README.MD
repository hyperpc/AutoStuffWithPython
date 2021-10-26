# 第6章 字符串操作

## 6.1 处理字符串

### 6.1.1 字符串字面量

以单引号(')开始和结束  

### 6.1.2 双引号

如果字符串中含有单引号(')，则可以选择用双引号(")开始和结束  

### 6.1.3 转义字符

如果字符串中含有单引号(')，则可以选择用转义字符\\'替换字符串中的'  

|转义字符|转义为|
|:---|:---|
|\\' |单引号|
|\\" |双引号|
|\\t |横向制表符|
|\\n |换行符|
|\\\ |反斜杠|
|\\ (在行尾) |续行符|
|\\a |响铃|
|\\b |退格|
|\\000 |空|
|\\v |纵向制表符|
|\\r |回车，将 \r 后面的内容移到字符串开头，并逐一替换开头部分的字符，直至将 \r 后面的内容完全替换完成|
|\\\f|换页|
|\\yyy|八进制，如\012 代表换行|
|\\xyy|十六进制数，如\x0a 代表换行|
|\\other|其它的字符以普通格式输出|

### 6.1.4 原始字符串

在字符串开始的引号之前添加r，使其成为原始字符串(忽略其中的转义字符和到斜杠等特殊字符)，原样输出  

```python
>>> 'This is Alice'
'This is Alice'
>>> "This is Alice's cat."
"This is Alice's cat."
>>> 'This is Alice\'s cat.'
"This is Alice's cat."
>>> print(r'That is Carol\'s cat.')
That is Carol\'s cat.
```

### 6.1.5 用三重引号的多行字符串

三个单引号或三个双引号包裹一个字符串，其中的所有引号、制表符或换行等特殊字符，都会被原样输出  

```python
>>> print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')
Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob
```

### 6.1.6 多行注释

单行注释#  
多行注释"""(与三重双引号相同)  

```python
"""This is a test Python program.
Written by blahblah...

This program was designed for Python 3, not Python 2.
"""

def spam():
    """multiline comment 1
    multiline comment 2"""
    print('Hello!')
```

### 6.1.7 字符串下标和切片

切片并不会改变原来的字符串

```python
>>> spam = 'Hello world!'
>>> spam[0]
'H'
>>> spam[4]
'o'
>>> spam[-1]
'!'
>>> spam[0:5]
'Hello'
>>> spam[:5]
'Hello'
>>> spam[6:]
'world!'
>>> spam[3:7]
'lo w'
```

### 6.1.8 字符串的in和not in操作符

精确匹配，区分大小写

```python
>>> 'Hello' in 'Hello'
True
>>> spam = 'Hello World'
>>> 'Hello' in spam
True
>>> 'HELLO' in spam
False
>>> ' ' in spam
True
>>> 'cats' not in 'cats and dogs'
False
```

## 6.2 有用的字符串方法

### 6.2.1 upper()、lower()和islower()

```python
>>> spam = 'Hello world!'
>>> spam = spam.upper()
>>> spam
'HELLO WORLD!'
>>> spam = spam.lower()
>>> spam
'hello world!'
>>> spam.islower()
True

>>> spam = 'Hello world!'
>>> spam.islower()
False
>>> spam.isupper()
False
>>> 'abc12345'.islower()
True
>>> '12345'.islower()
False
>>> '12345'.isupper()
False
>>> 'Hello'.upper()
'HELLO'
>>> 'Hello'.upper().lower()
'hello'
>>> 'Hello'.upper().lower().upper()
'HELLO'
>>> 'HELLO'.lower()
'hello'
>>> 'HELLO'.lower().islower()
True
```

### 6.2.2 isX字符串方法

|isX方法名|返回值|返回True的条件|
|:---|:---|:---|
|isalpha()|布尔值|如果字符串只包含字母，并且非空|
|isalnum()|布尔值|如果字符串只包含字母和数字，并且非空|
|isdecimal()|布尔值|如果字符串只包含数字字符，并且非空|
|isspace()|布尔值|如果字符串只包含空格、制表符和换行，并且非空|
|istitle()|布尔值|如果字符串仅包含以大写字母开头、后面都是小写字母的单词|

```python
>>> 'hello'.isalpha()
True
>>> 'hello123'.isalpha()
False
>>> 'hello123'.isalnum()
True
>>> 'hello'.isalnum()
True
>>> '123'.isalnum()
True
>>> '123'.isdecimal()
True
>>> ' '.isspace()
True
>>> 'This Is Title Case'.istitle()
True
>>> 'This Is Title Case 123'.istitle()
True
>>> 'This Is not Title Case'.istitle()
False
>>> 'This Is NOT Title Case'.istitle()
False
>>> 'This Is A Title Case'.istitle()
True
>>> while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')
while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Password can only have letters and numbers')
    
Enter your age:
>>> eighteen
Please enter a number for your age.
Enter your age:
>>> 18
Select a new password (letters and numbers only):
>>> secr3t!
Password can only have letters and numbers
Select a new password (letters and numbers only):
>>> secr3t
```

### 6.2.3 startswith()和endswith()

```python
>>> spam = 'Hello world!'
>>> spam.startswith('Hello')
True
>>> spam.endswith('world!')
True
>>> spam = 'abc123'
>>> spam.startswith('abcdef')
False
>>> spam.endswith('12')
False
>>> spam.startswith(spam)
True
>>> spam.endswith(spam)
True
>>> spam.startswith('c', 2)
True
>>> spam.endswith('c', 0, 2)
False
>>> spam.endswith('c', 0, 3)
True
```

### 6.2.4 join()和split()

值得注意的是，split()方法在不指定分隔字符时，以空格分割的  

```python
>>> ','.join(['cats', 'rats', 'bats'])
'cats,rats,bats'
>>> ', '.join(['cats', 'rats', 'bats'])
'cats, rats, bats'
>>> ' '.join(['My', 'name', 'is', 'Simon'])
'My name is Simon'
>>> 'ABC'.join(['My', 'name', 'is', 'Simon'])
'MyABCnameABCisABCSimon'

>>> 'My name is Simon'.split()
['My', 'name', 'is', 'Simon']
>>> 'MyABCnameABCisABCSimon'.split('ABC')
['My', 'name', 'is', 'Simon']
>>> 'My name is Simon'.split('m')
['My na', 'e is Si', 'on']
>>> spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".

Please do not drink it.
Sincerely,
Bob'''
>>> spam.split('\n')
['Dear Alice,', 'How have you been? I am fine.', 'There is a container in the fridge', 'that is labeled "Milk Experiment".', '', 'Please do not drink it.', 'Sincerely,', 'Bob']
```

### 6.2.5 rjust()、ljust()和center()对齐文本

```python
>>> 'Hello'.rjust(10)
'     Hello'
>>> 'Hello'.rjust(20)
'               Hello'
>>> 'Hello World'.rjust(20)
'         Hello World'
>>> 'Hello'.ljust(10)
'Hello     '
>>> 'Hello'.rjust(20,'*')
'***************Hello'
>>> 'Hello'.ljust(20,'-')
'Hello---------------'
>>> 'Hello'.center(20)
'       Hello        '
>>> 'Hello'.center(20,'=')
'=======Hello========'
```

下面示例脚本#6_2_5_picnicTable.py，演示了如何打印表格式数据  

### 6.2.6 strip()、rstrip()和lstrip()删除空白字符

```python
>>> spam = ' Hello World '
>>> spam.strip()
'Hello World'
>>> spam.lstrip()
'Hello World '
>>> spam.rstrip()
' Hello World'
>>> spam = 'SpamSpamBaconSpamEggsSpamSpam'
>>> spam.strip('ampS')
'BaconSpamEggs'
>>> spam.strip('Samp')
'BaconSpamEggs'
>>> spam.strip('SmapS')
'BaconSpamEggs'
```

strip()传入的参数里的字符顺序不重要  

### 6.2.7 用pyperclip模块拷贝粘贴字符串

pyperclip模块是第三方模块，需要另外安装  

> pip工具是Python安装第三方模块的工具  
> 在Windows和OS X上，pip会随Python一块安装  
> 在Linux上，需要单独安装  
> Ubuntu/Debian: get install python3-pip  
> Fedora: install python3-pip  
> 升级pip：  
> 进入Python安装目录，找到python.exe所在目录  
> 升级pip命令：python.exe -m pip install --upgrade pip
> 安装pyperclip模块：pip install pyperclip  
> 升级pyperclip模块：pip install -U pyperclip  
> OS X和Linux上安装命令：  
> sudo pip3 install pyperclip  
> pip3 install -U pyperclip  

```python
>>> import pyperclip
>>> pyperclip.copy('Hello World!')
>>> pyperclip.paste()
'Hello World!'

## 在程序之外，复制一段文字带剪贴板，然后执行paste()
>>> pyperclip.paste()
'Join us virtually on Oct. 27 and 28 (PDT). Check out sessions across Security, DevOps, Developer Productivity, and Communities. Register to start building your customized Universe schedule.'
```

> 在IDLE和IDE之外运行Python程序  
> 保证Python脚本的第一行必须是：#! python3  
> linux系统则是：#! /usr/bin/python3  
> os x系统则是：#! /usr/bin/env python3  
> 在Python解释程序的目录下，或配置好的目录下，执行脚本的完整目录  
> 使用-O开关，可以关闭脚本中的Python断言  

## 6.3 项目：口令保管箱

### 第1步：程序设计和数据结构

首行输入 ‘#! python3’  

### 第2步：处理命令行参数

命令行参数，都存储在sys.argv变量中  

> py pw.py [account] - copy account password  

### 第3步：复制正确的口令

参考示例脚本#6_3_pw.py  
在Windows上创建一个批处理文件pw.bat：  

```batch
@py.exe D:\pyAuto\6_3_pw.py %*
@pause
```

将文件6_3_pw.py和pw.bat放入目录D:\pyAuto下  
然后添加该目录到PATH环境变量中  
之后，按快捷键Win+R，输入pw &lt;account_name&gt;，如pw email  

## 6.4 项目：在Wiki标记中添加无序列表

### 第1步：从剪贴板中复制和粘贴

pyperclip.copy()，pyperclip.paste()  

### 第2步：分离文本中的行，并添加星号

### 第3步：链接修改过的行

pyperclip.copy()方法只接收一个字符串参数

参考示例脚本#6_4_bulletPointAdder.py  
注意，在运行脚本前，一定要先复制下列文本到剪贴板：  

Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars

## 6.5 小结

操作文本，剪贴板  

## 6.6 习题

## 6.7 实践项目

### 表格打印

总体思路和第4章最后的实践项目类似，但是需要字符对齐(需要考虑每列的最大宽度，存入列表或字典)，参考示例脚本#6_7_printTable.py  
