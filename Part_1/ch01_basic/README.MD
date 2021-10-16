# 第1章 Python基础

## 1.1 在交互式环境中输入表达式

|操作符|操作|例子|求值为|优先级|
|:---|:---|:---|:---|:---|
|**|指数|2**3|8|1|
|%|取模/取余数|22%8|6|2|
|//|整除/商数取整|22//8|2|2|
|/|除法|22/8|2.75|2|
|*|乘法|3*5|15|2|
|-|减法|5-2|3|3|
|+|加法|2+2|4|3|

> 括号()优先级最高  

## 1.2 整型、浮点型和字符串数据类型

常见数据类型
|数据类型|取值范围|例子|
|:---|:---|:---|
|整型int|32bit: -2\**31～2\**31-1; 64bit: -2\**63～2\**63-1|-2, -1, 0, 1, 2|
|浮点型float|sys.float_info.min（2.2250738585072014e-308）~sys.float_info.max（1.7976931348623157e+308）|-1.25, -1.0, --0.05, 0.0, 1.0, 1.25|
|字符串string|-|'', 'abc', '123 cde'|

## 1.3 字符串连接和复制

```python
'Alice' + 'Bob'  // Alice Bob  
'Alice' * 5      // AliceAliceAliceAliceAlice  
'Alice' + 1      // TypeError: Can't covert 'int' object to str implicity  
'Alice' * 'Bob'  // TypeError: Can't multiply sequence by non-int of type 'str'  
'Alice' * 5.0    // TypeError: Can't multiply sequence by non-int of type 'float'  
```

## 1.4 在变量中保存值

### 1.4.1 赋值语句

```python
spam = 40  
spam                     // 40  
eggs = 2  
eggs                     // 2  
spam + eggs              // 42  
spam = spam + eggs  
spam                     // 42  
spam = 'Hi'  
spam                     // Hi  
spam = 'Bye'  
spam                     // Bye  
```

### 1.4.2 变量名

变量命名建议：

- 只能是一个词  
- 只能包含字母、数字和下划线  
- 不能以数字开头  
- 区分大小写，小写字母开头是Python惯例  
- 建议驼峰命名，lookLikeThis  
- 取一个符合程序上下文，有意义的变量名  

## 1.5 第一个程序

```python
# This program says hi and asks for my name
print('hi')
print('What is your name?')
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge)+1) +' in a year.')
```

在Visual Studio Code中运行的结果为：

```cmd
D:\Workspace\PythonDemo> cmd /C ""C:\Program Files\Python310\python.exe" c:\Users\mypc\.vscode\extensions\ms-python.python-2021.10.1336267007\pythonFiles\lib\python\debugpy\launcher 52588 -- d:\Workspace\PythonDemo\Part_1\ch01_basic\hello.py "
hi
What is your name?
Bob
It is good to meet you, Bob
The length of your name is:
3
What is your age?
18
You will be 19 in a year.

D:\Workspace\PythonDemo>
```

也可以在IDLE 3中打开上述源文件，Run> Run Module或F5，就可以得到运行结果  

## 1.6 程序剖析

### 1.6.1 注释

单行注释：行开头输入#  

### 1.6.2 print()函数

将单引号中的字符串打印到屏幕  

### 1.6.3 input()函数

接收用户输入的一些文本，并以回车键结束输入  

### 1.6.4 打印用户的名字

将被赋值用户名的变量打印到屏幕  

### 1.6.5 len()函数

参数是一个字符串或包含字符串的变量，返回一个整数，表示字符的个数  

### 1.6.6 str()、int()和float()函数

str()将传入的参数转换为字符串  
int()将传入的参数转换为整数  
float()将传入的参数转换为浮点数  

```python
str(0)               // '0'  
str(-3.14)           // '-3.14'  
int('42')            // 42  
int('-99')           // -99  
int(1.25)            // 1  
int(1.99)            // 1  
float('3.14')        // 3.14  
float(10)            // 10.0  
spam=input()  
spam                 // '101'  
spam=int(spam)  
spam                 // 101  
spam * 10 / 5        // 202.0  
int(99.99)           // ValueError: invalid literal for int() with base 10: '99.99'  
int('twelve')        // ValueError: invalid literal for int() with base 10: 'twelve'  

42 == '42'           // False  
42 == 42.0           // True  
42.0 == 0042.000     // True  
```

## 1.7 小结

操作符，数据类型，常用函数  

## 1.8 习题
