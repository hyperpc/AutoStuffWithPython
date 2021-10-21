# 第5章 字典和结构化数据

## 5.1 字典数据类型

字典，键-值对的集合。键即字典的索引，可使用多种不同的数据类型，也可以使用整数，不一定从0开始  
字典的集合由一堆花括号{}包括  

```python
>>> myCat = {'size':'fat', 'color':'gray', 'disposition':'loud'}
>>> myCat
{'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
>>> myCat['size']
'fat'
>>> 'My cat has ' + myCat['color'] + ' fur.'
'My cat has gray fur.'
>>> spam = {12345:'Luggage Combination', 42:'The Answer'}
>>> spam
{12345: 'Luggage Combination', 42: 'The Answer'}
```

### 5.1.1 字典与列表

列表可以通过有序的下标访问其中的表项；
字典中的键值对则没有顺序，只能通过键来访问某个项  
字典因此也不支持切片，但如果访问不存在的键值时，会导致KeyError，类似列表的越界错误IndexError  

```python
>>> spam = ['cats', 'dogs', 'moose']
>>> bacon = ['dogs', 'moose', 'cats']
>>> spam == bacon
False
>>> eggs = {'name':'Zophie', 'species':'cat', 'age':'8'}
>>> ham = {'species':'cat', 'age':'8', 'name':'Zophie'}
>>> eggs == ham
True
>>> eggs['color']
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    eggs['color']
KeyError: 'color'
```

参考示例脚本#5_2_birthday.py  

### 5.1.2 keys()、values()和items()

keys()、values()和items()分别返回字典的键、值和键值对  
他们的返回值不是列表，不能修改和append()，但是支持for循环  

```python
>>> spam = {'color':'red', 'age':42}
>>> for v in spam.values():
>>>     print(v)

red
42
>>> for k in spam.keys():
>>>     print(k)

color
age
>>> for i in spam.items():
>>>     print(i)

('color', 'red')
('age', 42)
>>> spam.keys()
dict_keys(['color', 'age'])
>>> list(spam.keys())
['color', 'age']
>>> for k,v in spam.items():
>>>     print('Key: ' + k +' Value: '+ str(v))

Key: color Value: red
Key: age Value: 42
```

### 5.1.3 检查字典中是否存在键或值

使用in或not in操作符检查字典中的键  

```python
>>> spam = {'name':'Zophie', 'age':42}
>>> 'name' in spam.keys()
True
>>> 'Zophie' in spam.values()
True
>>> 'color' in spam.keys()
False
>>> 'color' not in spam.keys()
True
>>> 'color' in spam
False
```

### 5.1.4 get()方法

两个参数：要取得其值的键，及如果该键不存在时，返回的备用值  
如果不用get()方法，直接通过键取一个不存在的值，会报错KeyError  

```python
>>> picnicItems = {'apples':5, 'cups':2}
>>> 'I am bring ' + str(picnicItems.get('cups', 0)) + ' cups.'
'I am bring 2 cups.'
>>> 'I am bring ' + str(picnicItems.get('eggs', 0)) + ' eggs.'
'I am bring 0 eggs.'
>>> 'I am bring ' + str(picnicItems['cups']) + ' cups.'
'I am bring 2 cups.'
>>> 'I am bring ' + str(picnicItems['eggs']) + ' cups.'
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    'I am bring ' + str(picnicItems['eggs']) + ' cups.'
KeyError: 'eggs'
```

### 5.1.5 setdefault()方法

两个参数：第一个是要检查的键；另一个是在该键不存在时，要设置的值。如果存在，方法返回键对应的值  
针对同一个键，setdefault()方法只会在第一次调用时生效  

```python
spam = {'name':'Pooka', 'age':5}
spam.setdefault('color', 'black')
'black'
spam
{'name': 'Pooka', 'age': 5, 'color': 'black'}
spam.setdefault('color', 'white')
'black'
spam
{'name': 'Pooka', 'age': 5, 'color': 'black'}
```

参考示例脚本#5_1_5_charCount.py  

## 5.2 漂亮打印

参考示例脚本#5_2_prettyCharCount.py  

## 5.3 使用数据结构对真实世界建模

将程序中的值，组织成数据结构，可以创建真实世界事物的模型  

### 5.3.1 井字棋

定义井字形棋盘的九个空格名字， 如top-L, top-M, top-R, mid-L, mid-M, mid-R, low-L, low-M, low-R  
空格内可以填写三种值，如'X'，'O'和''空字符  

参考示例代码#5_3_1_ticTacToe.py，是一个不完整的井字棋游戏，因为没有判断输赢  
完整版示例请参考[源码](http://nostarch.com/automatestuff/)  

### 5.3.2 嵌套的字典和列表

参考示例脚本#5_3_2_guestsFood.py，统计所有人带的所有食物的数量  

## 5.4 小结

字典和列表，嵌套，键值对，数据建模，pprint模块，pprint.pprint()，setdefault()  
Python基础知识结束  

## 5.5 习题

## 5.6 实践项目

### 5.6.1 好玩游戏的物品清单

### 5.6.2 列表到字典的函数，针对好玩游戏物品清单

参考示例脚本#5_6_Inventory.py  
