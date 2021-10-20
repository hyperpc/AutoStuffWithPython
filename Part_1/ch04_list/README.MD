# 第4章 列表

## 4.1 列表数据类型

列表，包含多个值构成的一个序列，序列的值由逗号分隔  
列表值，指列表本身，由中括号[]包裹，而不是指列表序列内的值  
列表支持嵌套  

### 4.1.1 用下标取得列表中的单个值

下标从0开始，一次递增+1  
超出下标范围，Python会报错IndexError  
下标只能是整数，否则会报错TypeError  
嵌套列表可通过多重下标访问  

### 4.1.2 负数下表

下标如果是-1，则表示序列中的最后一个元素；-2是倒数第二个下标  

### 4.1.3 利用切片取得子列表

切片，是从列表中截取一段子序列，得到一个新的序列。  
中括号中，冒号前面的数字，指切片开始的下标；冒号后面的数字，是切片结束的下标，但不包括改下表对应的值  
如果省略冒号前的下标，则表示从0下标开始；省略冒号后的下标，则表示使用列表的长度，即取到列表末尾，包括最后一个下标的值  

### 4.1.4 用len()取得列表的长度

### 4.1.5 用下标改变列表中的值

### 4.1.6 列表链接和列表复制

+操作符，链接两个列表，得到一个新列表  
*操作符，复制一个列表，得到一个新列表  

### 4.1.7 用del语句从列表中删除值

del删除列表中的某个值后，该值后面的所有值，都将向前移动一个下标。  
另外，del语句也可用于删除某简单变量，类似于取消赋值。  
删除后，再引用该变量，就会报错NameError，因为变量已不存在  
实际应用中，得了很少用于删除变量，而多用于删除列表中的值  

```python
# 4.1
>>> [1,2,3]
[1, 2, 3]
>>> ['cat','bat','rat','elephant']
['cat', 'bat', 'rat', 'elephant']
>>> ['hello',3.1415, True, None, 42]
['hello', 3.1415, True, None, 42]
>>> spam = []
>>> spam
[]
>>> spam = ['cat','bat','rat','elephant']
>>> spam
['cat', 'bat', 'rat', 'elephant']

# 4.1.1
>>> spam[0]
'cat'
>>> spam[3]
'elephant'
'Hicat'
>>> 'Hi ' + spam[0]
'Hi cat'
>>> 'The ' + spam[1] + ' ate the ' + spam[0]
'The bat ate the cat'
>>> spam[99]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    spam[99]
IndexError: list index out of range
>>> spam[1.0]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    spam[1.0]
TypeError: list indices must be integers or slices, not float
>>> spam[int(1.0)]
'bat'
>>> spam2 = [['cat','bat'],[10,20,30,40,50]]
>>> spam2[0]
['cat', 'bat']
>>> spam2[0][1]
'bat'
>>> spam2[1][4]
50
>>> spam[0][1]
'a'

# 4.1.2
>>> spam[-1]
'elephant'
>>> spam[-2]
'rat'
>>> 'The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.'
'The elephant is afraid of the bat.'

# 4.1.3
>>> spam[0:4]
['cat', 'bat', 'rat', 'elephant']
>>> spam[1:3]
['bat', 'rat']
>>> spam[0:-1]
['cat', 'bat', 'rat']
>>> spam[:2]
['cat', 'bat']
>>> spam[1:]
['bat', 'rat', 'elephant']
>>> spam[:]
['cat', 'bat', 'rat', 'elephant']

# 4.1.4
>>> len(spam)
4

# 4.1.5
>>> spam[1] = 'aardvark'
>>> spam
['cat', 'aardvark', 'rat', 'elephant']
>>> spam[2] = spam[1]
>>> spam
['cat', 'aardvark', 'aardvark', 'elephant']
>>> spam[-1] = 12345
>>> spam
['cat', 'aardvark', 'aardvark', 12345]

# 4.1.6
>>> [1,2,3] + ['A', 'B', 'C']
[1, 2, 3, 'A', 'B', 'C']
>>> ['X', 'Y', 'Z'] * 3
['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']
>>> spam3 = [1, 2, 3]
>>> spam3 = spam3 + ['A', 'B', 'C']
>>> spam3
[1, 2, 3, 'A', 'B', 'C']

# 4.1.7
>>> del spam[2]
>>> spam
['cat', 'aardvark', 12345]
>>> del spam[2]
>>> spam
['cat', 'aardvark']
```

## 4.2 使用列表

参考示例脚本 #4_2_myCats.py

### 4.2.1 列表用于循环

range(4)的返回值是类似列表的值，即[0,1,2,3]。如下示例中的两个for循环，输出结果相同  

```python
for i in range(4):
  print(i)

for i in [0, 1, 2, 3]:
  print(i)
```

Python常用range(len(someList))，迭代列表的每个下标  

```python
>>> supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
>>> for i in range(len(supplies)):
>>>     print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

Index 0 in supplies is: pens
Index 1 in supplies is: staplers
Index 2 in supplies is: flame-throwers
Index 3 in supplies is: binders
```

### 4.2.2 in和not in操作符

in和not in链接两个值：要查找的值，和待查找的列表  
表达式返回一个布尔值，以表示是否在列表中找到该值  

```python
>>> 'howdy' in ['hello', 'hi', 'howdy', 'heyas']
True
>>> spam = ['hello', 'hi', 'howdy', 'heyas']
>>> 'cat' in spam
False
>>> 'howdy' not in spam
False
>>> 'cat' not in spam
True
```

参考示例脚本#4_2_myPets.py  

### 4.2.3 多重赋值技巧

即用列表中的值，为多个变量赋值  
要求变量数目和列表长度必须严格相等  

```python
>>> cat = ['fat', 'black', 'loud']
>>> size,color = cat
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    size,color = cat
ValueError: too many values to unpack (expected 2)
>>> size, color, disposition, name = cat
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    size,color,disposition,name = cat
ValueError: not enough values to unpack (expected 4, got 3)
>>> size,color,disposition = cat
>>> size
'fat'
>>> disposition
'loud'
>>> color
'black'
```

## 4.3 增强的赋值操作

|增强的赋值语句|等价的赋值语句|适用范围|
|:---|:---|:---|
|spam += 1|spam = spam + 1|数字，字符串|
|spam -= 1|spam = spam - 1|数字|
|spam *= 1|spam = spam * 1|数字，字符串|
|spam /= 1|spam = spam / 1|数字|
|spam %= 1|spam = spam % 1|数字|

```python
>>> spam = 42
>>> spam = spam + 1
>>> spam
43
>>> spam += 1
>>> spam
44
>>> spam = 'Hello'
>>> spam += ' world!'
>>> spam
'Hello world!'
>>> bacon = ['Zophie']
>>> bacon *= 3
>>> bacon
['Zophie', 'Zophie', 'Zophie']
```

## 4.4 方法

每种数据类型都有自己的一组方法，通过变量名后边加点号(.)调用  

### 4.4.1 用index()方法在列表中查找值

调用列表的index()方法，index()方法参数是要查找的值，返回值是列表中查找到的第一个值的下标  
如果未找到，Python会报错ValueError  

```python
>>> spam = ['hello', 'hi', 'howdy', 'heyas']
>>> spam.index('hello')
0
>>> spam.index('heyas')
3
>>> spam.index('howdy howdy howdy')
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    spam.index('howdy howdy howdy')
ValueError: 'howdy howdy howdy' is not in list
>>> spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
>>> spam.index('Pooka')
1
```

### 4.4.2 用append()和insert()方法在列表中添加值

append()和insert()是列表方法，返回值为None，是不能用于字符串和整型的  

```python
>>> eggs = 'hello'
>>> eggs.append('world')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    eggs.append('world')
AttributeError: 'str' object has no attribute 'append'
>>> bacon = 42
>>> bacon.insert(1, 'world')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    bacon.insert(1, 'world')
AttributeError: 'int' object has no attribute 'insert'
>>> spam = ['cat', 'dog', 'bat']
>>> spam.append('moose')
>>> spam
['cat', 'dog', 'bat', 'moose']
>>> spam = ['cat', 'dog', 'bat']
>>> spam.insert(1, 'chicken')
>>> spam
['cat', 'chicken', 'dog', 'bat']
```

注意，insert()方法的第一个参数是新值的下标，第二个参数是插入的新值  

### 4.4.3 用remove()方法从列表中删除值

remove()方法参数是要删除的值，且只删除列表中找到的第一个值；  
如果该值不存在，会导致ValueError错误  
如果不知道值，知道其在列表中的下标，可用del语句删除  

```python
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam.remove('bat')
>>> spam
['cat', 'rat', 'elephant']
>>> spam.remove('chicken')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    spam.remove('chicken')
ValueError: list.remove(x): x not in list
>>> spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
>>> spam.remove('cat')
>>> spam
['bat', 'rat', 'cat', 'hat', 'cat']
>>> del spam[2]
>>> spam
['bat', 'rat', 'hat', 'cat']
```

### 4.4.4 用sort()方法将列表中的值排序

sort()方法对数字或字符串列表，默认是按照“ASCII字符顺序”，而非实际的字典顺序。即大写字母Z会排在小写字母a的前面  
设置reverse=True，可以逆序排序；设置key=str.lower，可以按照字典顺序排序(表项都当成小写)，且不会改变列表中的值  
值得注意的是，列表中不能同时混合有数字和字符串，不然，会导致TypeError错误  

```python
>>> spam = [2, 5, 3.14, 1, -7]
>>> spam.sort()
>>> spam
[-7, 1, 2, 3.14, 5]
>>> spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
>>> spam.sort()
>>> spam
['ants', 'badgers', 'cats', 'dogs', 'elephants']
>>> spam.sort(reverse=True)
>>> spam
['elephants', 'dogs', 'cats', 'badgers', 'ants']
>>> spam = [1, 3, 2, 4, 'Alice', 'Bob']
>>> spam.sort()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    spam.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
>>> spam.sort()
>>> spam
['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']
>>> spam.sort(key=str.lower)
>>> spam
['Alice', 'ants', 'badgers', 'Bob', 'Carol', 'cats']
```

## 4.5 例子程序：神奇8球和列表

参考示例脚本#4_5_magic8Ball.py，是上一章的脚本#3_2_return.py的改进版本  
注意下面代码中，列表messages的值没有遵守Python的缩进规则，是因为没有检测到结束方括号，列表就还没结束，缩进规则不起作用  
当一行文本太长，需要在代码中换行，可以使用续行符号(\)结尾，以支持一条指令跨越多行  

```python
>>> messages = [
    'It is certain'
    ,'It is decidedly so'
    ,'Yes definitely'
]
>>> messages
['It is certain', 'It is decidedly so', 'Yes definitely']
>>> print('Four score and seven ' + \
  'years ago...')
Four score and seven years ago...
```

## 4.6 类似列表的类型：字符串和元组

可以将非空字符串看作是单个文本字符的列表，针对列表的许多操作，都适用于字符串  

```python
>>> name = 'Zophie'
>>> name[0]
'Z'
>>> name[-2]
'i'
>>> name[0:4]
'Zoph'
>>> 'Zo' in name
True
>>> 'z' in name
False
>>> 'p' not in name
False
>>> for i in name:
>>>     print('* * * ' + i + ' * * *')

* * * Z * * *
* * * o * * *
* * * p * * *
* * * h * * *
* * * i * * *
* * * e * * *
```

### 4.6.1 可变和不可变数据类型

列表是“可变的”数据类型，而字符串是“不可变的”，不能被更改。如果对字符串中的一个字符重新赋值，将导致TypeError错误  
可以通过切片和连接，构造“新的”字符串  

```python
>>> name = 'Zophie a cat'
>>> name[7]
'a'
>>> name[7] = 'the'
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    name[7] = 'the'
TypeError: 'str' object does not support item assignment
>>> newName = name[0:7] + 'the' + name[8:12]
>>> name
'Zophie a cat'
>>> newName
'Zophie the cat'
```

针对可变列表值，要区分覆写原来的列表值(传递引用)和修改原来的列表(通过del()和append())

```python
# 覆写
>>> eggs = [1, 2, 3]
>>> eggs = [4, 5, 6]
>>> eggs
[4, 5, 6]
# 修改
>>> eggs = [1, 2, 3]
>>> del eggs[2]
>>> del eggs[1]
>>> del eggs[0]
>>> eggs
[]
>>> eggs.append(4)
>>> eggs.append(5)
>>> eggs.append(6)
>>> eggs
[4, 5, 6]
```

### 4.6.2 元组数据类型

元组数据类型，是列表数据类型的不可变形式  
元组的特征：

- 输入时用圆括号()，而不是[]  
- 元组像字符串一样，是不可变的  
- 如果元组只有一个值，要在括号内该值后面加上逗号(,)，可以用type()函数检查其类型  

建议能用元组的地方，尽量不要用列表  
因为Python针对元组做了优化，使其比列表的速度块  

```python
>>> eggs = ('hello', 42, 0.5)
>>> eggs[0]
'hello'
>>> eggs[1:3]
(42, 0.5)
>>> len(eggs)
3
>>> eggs[1] = 99
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    eggs[1] = 99
TypeError: 'tuple' object does not support item assignment
>>> type(('hello'))
<class 'str'>
>>> type(('hello',))
<class 'tuple'>
```

### 4.6.3 用list()和tuple()函数来转换类型

当需要元组值的一个可变版本，可以通过list()将元组转换为列表  

```python
>>> tuple(['cat', 'dog', 5])
('cat', 'dog', 5)
>>> list(('cat', 'dog', 5))
['cat', 'dog', 5]
>>> list('hello')
['h', 'e', 'l', 'l', 'o']
```

## 4.7 引用

对于不可变数据类型(字符串、整型或元组等)，变量赋值，是直接改变存储在变量中的值  
对于可变数据类型(列表或字典等)，变量赋值，是将值的“引用”赋值给了变量，而非值本身  

```python
>>> spam = 42
>>> cheese = spam
>>> spam = 100
>>> spam
100
>>> cheese
42
>>> spam = [0, 1, 2, 3, 4, 5]
>>> cheese = spam
>>> cheese[1] = 'Hello!'
>>> spam
[0, 'Hello!', 2, 3, 4, 5]
>>> cheese
[0, 'Hello!', 2, 3, 4, 5]
```

### 4.7.1 传递引用

参考示例脚本#4_7_passingReference.py，其中的两个变量spam和myParam，他们的值是同一个引用，指向相同的列表。  
故，任何一个变量的修改，都会影响到另一个变量  

### 4.7.2 copy模块的copy()和deepcopy()函数

导入copy模块后，使用copy.copy()方法，可以复制列表或字典这样的可变值，而非复制引用  
如果要同时复制列表中的列表，就使用copy.deepcopy()方法  

```python
>>> import copy
>>> spam = ['A', 'B', 'C', ['abc', ['d', 1, 'ef']], 'D', 'E']
>>> cheese = copy.copy(spam)
>>> cheese[1] = 42
>>> spam
['A', 'B', 'C', ['abc', ['d', 1, 'ef']], 'D', 'E']
>>> cheese
['A', 42, 'C', ['abc', ['d', 1, 'ef']], 'D', 'E']
>>> cheese2 = copy.deepcopy(spam)
>>> cheese2
['A', 'B', 'C', ['abc', ['d', 1, 'ef']], 'D', 'E']
```

在当前版本中，没有发现copy()和deepcopy()函数的使用区别  

## 4.8 小结

可变数据类型(列表，字典)和不可斌数据类型(元组，字符串)，切片，append()，remove()，覆写，引用，copy()和deepcopy()  

## 4.9 习题

第3题的解答脚本：

```python
>>> spam = ['a', 'b', 'c', 'd']
>>> spam[int(int('3'*2)/11)]
'd'
```

## 4.10 实践项目

### 4.10.1 逗号代码

初始数据为：
> spam = ['apple', 'bananas', 'tofu', 'cats']  

输出结果为：
> apple, bananas, tofu, and cats  

参考示例脚本#4_10_1_test.py  

### 4.10.2 字符图网格

初始数据为：  
> grid =[  
    ['.', '.', '.', '.', '.', '.']  
    ,['.', 'o', 'o', '.', '.', '.']  
    ,['o', 'o', 'o', 'o', '.', '.']  
    ,['o', 'o', 'o', 'o', 'o', '.']  
    ,['.', 'o', 'o', 'o', 'o', 'o']  
    ,['o', 'o', 'o', 'o', 'o', '.']  
    ,['o', 'o', 'o', 'o', '.', '.']  
    ,['.', 'o', 'o', '.', '.', '.']  
    ,['.', '.', '.', '.', '.', '.']  
    ]  

输出点阵为：  
> ..oo.oo..  
.ooooooo.  
.ooooooo.  
..ooooo..  
...ooo...  
....o....  

参考示例脚本#4_10_2_test.py  
