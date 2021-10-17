# 第2章 控制流

## 2.1 布尔值

Boolean首字母大写。它只有两种值：True和False，且首字母大写。  

```python
>>> spam=True
>>> spam
True
>>> true
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> True = 2 + 2
SyntaxError: cannot assign to True
```

## 2.2 比较操作符

|操作符|含义|使用范围|
|:---|:---|:---|
|==|等于|所有数据类型|
|!=|不等于|所有数据类型|
|<|小于|整型和浮点型|
|>|大于|整型和浮点型|
|<=|小于等于|整型和浮点型|
|>=|大于等于|整型和浮点型|

```python
>>> spam=True
>>> spam
True
>>> true
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> True = 2 + 2
SyntaxError: cannot assign to True
>>> 42 == 42
True
>>> 42 == 99
False
>>> 2 != 3
True
>>> 2 != 2
False
>>> 'Hi' == 'Hi'
True
>>> 'Hi' != 'Hi'
False
>>> 'Dog' != 'Cat'
True
>>> True == True
True
>>> True != False
True
>>> 42 == 42.0
True
>>> 42 = '42'
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> 42 == '42'
False
>>> 42 < 100
True
>>> 42 <= 100
True
>>> 42 > 100
False
>>> 42 >= 42
True
>>> 42 < 42
False
>>> eggCnt = 42
>>> eggCnt <= 42
True
>>> myAge = 29
>>> myAge >= 10
True
```

## 2.3 布尔操作符

布尔操作符，分为二元布尔操作符(and, or)和一元布尔操作符(not)  

### 2.3.1 二元布尔操作符

### 2.3.2 not操作符

真值表
|操作符|表达式|值|
|:---|:---|:---|
|and|True and True|True|
|and|True and False|False|
|and|False and True|False|
|and|False and False|False|
|or|True or True|True|
|or|True or False|True|
|or|False or True|True|
|or|False or False|False|
|not|not True|False|
|not|not False|True|

```python
#多重否定
>>> not not not not True
True
```

## 2.4 混合布尔和比较操作符

布尔操作符有操作顺序：  
在所有算数和比较操作符求值后，Python先求值not，然后是and，最后是or。  

```python
>>> (4 < 5) and (5 < 6)
True
>>> (4 < 5) and (9 < 6)
False
>>> (1 == 2) or (2 == 2)
True
>>> 2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2
True
```

## 2.5 控制流的元素

### 2.5.1 条件

条件总是求值为一个布尔值：True或False。几乎所有的控制流语句都使用条件  

### 2.5.2 代码块

3条规则：

- 缩进增加时，代码块开始  
- 代码块支持嵌套  
- 缩进减少为零，或减少到外层包围代码块的缩进，则代码块结束  

```python
print('Plz input your name:')
name = input()
if name == 'Mary':
    print('Hello Mary')
    print('Plz input your password:')
    password = input()
    if password == 'swordfish':
        print('Access granted.')
    else:
        print('Wrong password.')
else:
    print('Wrong name.')
```

## 2.6 程序执行

程序都是由程序入口开始，一条接一条，顺序执行。控制流语句可以改变程序执行的顺序  

## 2.7 控制流语句

所有控制流语句都以冒号结尾  

### 2.7.1 if语句

### 2.7.2 else语句

### 2.7.3 elif语句

如果有一系列elif语句，但仅有一条或零条会被执行，所以elif语句的顺序很重要  

```python
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')
else:
    print('You are neither Alice nor a little kid.')
```

### 2.7.4 while循环语句

### 2.7.5 恼人的循环

### 2.7.6 break语句

中断整个循环块，只用于while循环和for循环  

### 2.7.7 continue语句

中断当前这一次循环，只用于while循环和for循环  

> IDLE环境下，如何中断无限循环(infinite loop)？  
> 1. Ctrl-C;  
> 2. Shell > Restart Shell  

### 2.7.8 for循环和range()函数

'类真'和'类假'的值  
在用于条件时，0、0.0和''(空字符串)被认为时False，其他值被认为True。  

```python
print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')
```

### 2.7.9 等价的while循环

```python
print('My name is')
i = 0
while i < 5:
    print('Jimmy Five Times (' + str(i) + ')')
    i = i + 1
```

### 2.7.10 range()的开始、停止和步长参数

range()有三个参数：  

- 第一个参数：for循环变量开始的值  
- 第二个参数：for循环变量终止的上限，但不包含这个值  
- 第三个参数：for循环每次迭代结束增加的值  

```python
for i in range(12, 16):
    print(i)

for i in range(0, 10, 2):
    print(i)

for i in range(5, -1, -1):
    print(i)
```

## 2.8 导入模块

Python可以调用一些"内建函数"，如print()、input()和len()函数。  
Python也包括一组模块，即"标准库"，如math模块(数学运算相关的函数库)，random模块(随机数相关的函数库)等。  

```python
#导入一个模块
import random
for i in range(5):
    print(random.randint(1,10))

##导入多个模块
import random, sys, os, math
```

### from import语句

使用from import语句，可以在程序中省略库名，直接调用其中的函数名。  
**但不推荐使用**  

```python
from random import *
for i in range(5):
    print(randint(1,10))
```

## 2.9 用sys.exit()提前结束程序

```python
import sys

while True:
    print('Type exit to exit.')
    response = input()
    if(response == 'exit'):
        sys.exit()
    print('You typed' + response + '.')
```

## 2.10 小结

条件表达式，循环，break，continue，range(), import, sys.exit()  

## 2.11 习题

round(), abs()  
