# 第3章 函数

## 3.1 def语句与函数

定义的函数名，括号里面的变元，就是参数。  

```python
def hello(name):
    print('Hello ' + name)
```

## 3.2 返回值和return语句

一般来说，函数调用求值的结果，称为函数的返回值  
return语句可以指定函数返回的值或表达式  

## 3.3 None值

None表示没有值，是NoneType数据类型的唯一值，首字母大写  
类似其他编程语言中的null、nil或undefined

所有函数调用都需要一个返回值，但像print()这样，没有返回值的函数，或以空的return语句结尾，Python会在末尾return None  
类似地，while或for循环，都是隐式地以continue语句结尾  

```python
>>> spam = print('Hi')
Hi
>>> spam == None
True
```

## 3.4 关键字参数和print()

关键字参数是函数调用时加在他们前面的关键字来识别的，常用于可选参数  
如print()函数的end和sep  

- print()函数默认在传入的字符串结尾，添加换行符，如#1  
- print()函数的可选参数end赋值为空字符串，替代换行符，end=''可以避免当前字符串末尾换行，如#2  
- print()函数接收多个字符串参数，默认以空格分隔，如#3  
- print()函数的可选参数sep赋值为某值，将替换默认的空格分隔符，如#4  

```python
# 1
print('Hello'); print('World')
Hello
World

# 2
print('Hello', end=''); print('World')
HelloWorld

# 3
print('cats', 'dogs', 'mice')
cats dogs mice

# 3
print('cats', 'dogs', 'mice', sep=',')
cats,dogs,mice
```

## 3.5 局部和全局作用域

声明一个变量，根据声明的位置，分为局部变量和全局变量  
尽量使用局部变量，方便定位程序缺陷或错误  

### 3.5.1 局部变量不能在全局作用域内使用

一旦程序从局部作用域返回，局部作用域中声明的局部变量就会被销毁，不能再被使用  

### 3.5.2 局部作用域不能使用其他局部作用域内的变量

不同局部作用域内的局部变量，是分割开的，互不影响  

### 3.5.3 全局变量可以在局部作用域中读取

全局变量再全局作用域有效，包括局部作用域内  

### 3.5.4 名称相同的局部变量和全局变量

虽然Python允许存在同名的局部变量和全局变量，但还是应尽量避免同名情况的出现  
这样，可以避免在追踪代码时，出现混淆  

## 3.6 global语句

如果需要在局部作用域(如函数)中，修改全局变量，则需要在局部作用内，这个全局变量名的前面添加global关键字，并避免用同样的名字声明局部变量。函数没有办法先使用同名的局部变量，稍后又在同一作用域使用同名的全局变量  

区分局部变量和全局变量：

- 如果变量在全局作用域中使用(即在所用函数之外)，它就是全局变量  
- 如果在一个函数中，有针对该变量的global语句，它就是全局变量  
- 否则，如果该变量用于函数中的赋值语句，它就是局部变量  
- 但是，如果该变量没有用在赋值语句，它就是全局变量  

```python
def spam():
    global eggs
    eggs = 'spam'  # this is the global

def bacon():
    eggs = 'bacon' # this is a local

def ham():
    print(eggs)    # this is the global

eggs = 42          # this is the global
spam()
print(eggs)        # spam
bacon()
print(eggs)        # spam

def spam2():
    print(eggs2)   # UnboundLocalError: local variable 'eggs2' referenced before assignment
    eggs2 = 'spam2 local'

eggs2 = 'global'
spam2()
```

## 3.7 异常处理

try...except...语句用来捕获try包裹的代码块中出现的异常，并终止当前代码块的执行，跳到except语句块继续执行  

```python
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')
```

## 3.8 一个小程序：猜数字

参考源码#3_8_guessNum.py，注意最后if...else...语句块的缩进，它在for循环的外部  

## 3.9 小结

函数，是将代码逻辑分组的主要方式。局部变量和全局变量，try...except语句

## 3.10 习题

## 3.11 实践项目

### 3.11.1 Collatz序列

编写一个函数Collatz()，接收一个参数，名为number。  
如果参数为偶数，则打印并返回number//2，然后递归调用Collatz()；  
如果参数为奇数，则打印并返回3*number+1，然后递归调用Collatz()  

> 输出结果如下：
> Enter number:  
> 3  
> 10  
> 5  
> 16  
> 8  
> 4  
> 2  
> 1  

### 3.11.2 输入验证

在函数Collatz()中添加try...except语句，以处理用户输入非整数的字符串，避免ValueError，如invalid literal for int() with base 10: 'puppy'

参考脚本#3_11_Collatz.py
