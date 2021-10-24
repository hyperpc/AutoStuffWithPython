# 第7章 模式匹配和正则表达式

## 7.1 不用正则表达式来查找文本模式

参考示例脚本#7_1_isPhoneNum_1.py  

## 7.2 用正则表达式查找文本模式

正则表达式，简称regex，是文本模式的描述方法。  

### 7.2.1 创建正则表达式对象

正则表达式的所有函数都在re模块中。  
compile()函数参数就是正则表达式，注意参数使用原始字符串r，否则正则表达式中的很多的(\)都要加转义字符  

```python
>>> import re
>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
```

### 7.2.2 匹配Regex对象

Regex对象的search()方法查找传入的字符串，寻找该正则表达式的所有匹配  
如果未找到，则返回None；找到了，就返回一个Match对象，其group()方法，返回查找到的第一次匹配到的文本

```python
>>> mo = phoneNumRegex.search('My number is 415-555-4242.')
>>> print('Phone number found: ' + mo.group())
Phone number found: 415-555-4242
```

### 7.2.3 正则表达式匹配复习

使用步骤：

> 1. 用import re导入正则表达式模块  
> 2. 用re.compile()函数创建一个Regex对象(使用原始字符串)  
> 3. 向Regex对象的search()方法传入想查找的字符串；返回一个Match对象  
> 4. 调用Match对象的group()方法，返回实际匹配文本的字符串  

在线测试正则表达式的网址：
[https://www.regexpal.com/](https://www.regexpal.com/)  

## 7.3 用正则表达式匹配更多模式

### 7.3.1 利用括号分组

括号将正则表达式分成几个不同的组，每组匹配的值，通过group()传入组的序号获得  
groups()返回多个值的元组，故可使用多重赋值获得匹配结果  
如果要匹配的文本中本来就存在括号，就通过转义符表示普通括号  

```python
>>> import re
>>> phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
>>> mo = phoneNumRegex.search('My number is 415-555-4242.')
>>> mo.group(1)
'415'
>>> mo.group(2)
'555-4242'
>>> mo.group(0)
'415-555-4242'
>>> mo.group()
'415-555-4242'
>>> mo.groups()
('415', '555-4242')
>>> areaCode, mainNum = mo.groups()
>>> print(areaCode)
415
>>> print(mainNum)
555-4242
>>> areaCode
'415'
>>> mainNum
'555-4242'
>>> phoneNumRegex = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
>>> mo = phoneNumRegex.search('My number is (415)-555-4242.')
>>> mo.group(1)
'(415)'
>>> mo.group(2)
'555-4242'
```

### 7.3.2 用管道匹配多个分组

字符|称为管道，在正则表达式中表示，希望匹配多个表达式中的任何一个  
如果被搜索的文本，可以匹配多个管道的表达式，只返回第一个匹配的Match对象  
如果是匹配以某个固定字符组合开头的字符串，可通过括号实现  

```python
>>> heroRegex = re.compile(r'Batman|Tina Fey')
>>> mo1 = heroRegex.search('Batman and Tina Fey.')
>>> mo1.group()
'Batman'
>>> mo2 = heroRegex.search('Tina Fey and Batman')
>>> mo2.group()
'Tina Fey'
>>> batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
>>> mo = batRegex.search('Batmobile lost a wheel')
>>> mo.group()
'Batmobile'
>>> mo.group(1)
'mobile'
>>> mo.group(2)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    mo.group(2)
IndexError: no such group
```

### 7.3.3 用问号实现可选匹配

?表示问号前面一组文本是可选的(匹配零次或一次)  

```python
>>> batRegex = re.compile(r'Bat(wo)?man')
>>> mo1 = batRegex.search('The Adventure of Batman')
>>> mo1.group()
'Batman'
>>> mo2 = batRegex.search('The Adventure of Batwoman')
>>> mo2.group()
'Batwoman'

>>> phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
>>> mo1 = phoneRegex.search('My number is 415-555-4242')
>>> mo1.group()
'415-555-4242'
>>> mo2 = phoneRegex.search('My number is 555-4242')
>>> mo2.group()
'555-4242'
```

### 7.3.4 用星号匹配零次或多次

星号*表示匹配零次或多次星号之前的分组文本  

```python
>>> batRegex = re.compile(r'Bat(wo)*man')
>>> mo1 = batRegex.search('The Adventure of Batman')
>>> mo1.group()
'Batman'

>>> mo2 = batRegex.search('The Adventure of Batwoman')
>>> mo2.group()
'Batwoman'

>>> mo3 = batRegex.search('The Adventure of Batwowowowoman')
>>> mo3.group()
'Batwowowowoman'
```

### 7.3.5 用加号匹配一次或多次

加号+表示至少匹配一次加号之前的分组文本  

```python
>>> batRegex = re.compile(r'Bat(wo)+man')
>>> mo1 = batRegex.search('The Adventure of Batman')
>>> mo1 == None
True

>>> mo2 = batRegex.search('The Adventure of Batwoman')
>>> mo2.group()
'Batwoman'

>>> mo3 = batRegex.search('The Adventure of Batwowowowoman')
>>> mo3.group()
'Batwowowowoman'
```

### 7.3.6 用花括号匹配特定次数

{n}表示匹配前面的分组文本n次  
{m}表示匹配前面的分组文本m次  
{n,m}表示匹配前面的分组文本n到m次  
{n,}表示匹配前面的分组文本至少n次  
{,m}表示匹配前面的分组文本最多m次  

```python
>>> haRegex = re.compile(r'(Ha){3}')
>>> mo1 = haRegex.search('HaHaHa')
>>> mo1.group()
'HaHaHa'
>>> mo2 = haRegex.search('Ha')
>>> mo2 == None
True
```

## 7.4 贪心和非贪心匹配

Python的正则表达式，默认是贪心匹配的  
'HaHaHaHaHa'通过正则表达式'(Ha){3,5}'匹配，结果是'HaHaHaHaHa'，而非'HaHaHa'  
如果想要使用非贪心匹配，返回'HaHaHa'，则使用正则表达式'(Ha){3,5}?'  

```python
>>> greedyRegex = re.compile(r'(Ha){3,5}')
>>> mo1 = greedyRegex.search('HaHaHaHaHa')
>>> mo1.group()
'HaHaHaHaHa'
>>> nonGreedyRegex = re.compile(r'(Ha){3,5}?')
>>> mo2 = nonGreedyRegex.search('HaHaHaHaHa')
>>> mo2.group()
'HaHaHa'
```

注意，花括号后面的?表示使用非贪心匹配；其余位置的?表示可选匹配；\?表示普通问号文本  

## 7.5 findall()方法

findall()方法返回一组字符串，包含被查找文本中的所有匹配  

- 如果调用在未分组的正则表达式上，findall()返回一个包含所有匹配字符串的列表  
- 如果调用在分组的正则表达式上，findall()返回字符串的元组的列表  

```python
>>> import re
>>> phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
>>> phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
['415-555-9999', '212-555-0000']
>>> phoneNumRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
>>> phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
[('415', '555', '9999'), ('212', '555', '0000')]
```

## 7.6 字符分类

常用字符分类的缩写代码
|缩写字符|含义|
|:---|:---|
|\d|匹配一个数字字符。等价于 [0-9]|
|\D|匹配一个非数字字符。等价于 [^0-9]|
|\w|匹配包括下划线的任何单词字符。等价于[A-Za-z0-9_]|
|\W|匹配任何非单词字符。等价于[^A-Za-z0-9_]|
|\s|匹配任何空白字符，包括空格、制表符、换页符等等。等价于[\f\n\r\t\v]|
|\S|匹配任何非空白字符。等价于 [^\f\n\r\t\v]|

```python
>>> xmasRegex = re.compile(r'\d+\s\w+')
>>> xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']
```

## 7.7 建立自己的字符分类

中括号内可以定义自己的字符分类，而且任何特殊符号(如*，?，+，.等)都会被作为普通字符处理  
如果要对中括号内的字符分类，进行取反，只需要在左中括号紧跟插入符号^  

```python
>>> vowelRegex = re.compile(r'[.aeiouAEIOU]')
>>> vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', '.', 'A', 'O', 'O', '.']
>>> consonantRegex = re.compile(r'[^aeiouAEIOU]')
>>> consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']
```

## 7.8 插入字符和美元字符

正则表达式开始处使用插入符号^，表示匹配必须发生在被查找文本的开始处  
正则表达式结束处使用美元符号$，表示该字符串必须以这个正则表达式的模式结束  
如果同时使用^和$，表明整个字符串必须匹配该模式，而不是匹配某个子集  

```python
>>> beginWithHello = re.compile(r'^Hello')
>>> beginWithHello.search('Hello world!')
<re.Match object; span=(0, 5), match='Hello'>
>>> beginWithHello.search('He said hello.') == None
True
>>> endsWithNum = re.compile(r'\d$')
>>> endsWithNum.search('Your number is 42')
<re.Match object; span=(16, 17), match='2'>
>>> endsWithNum.search('Your number is forty two') == None
True
>>> wholeStrIsNum = re.compile(r'^\d+$')
>>> wholeStrIsNum.search('1234567890')
<re.Match object; span=(0, 10), match='1234567890'>
>>> wholeStrIsNum.search('12345xyz67890') == None
True
>>> wholeStrIsNum.search('12345 67890') == None
True
```

## 7.9 通配字符

句点.字符是通配符，匹配除换行符之外的任何一个字符  

```python
>>> atRegex = re.compile(r'.at')
>>> atRegex.search('The cat in the hat sat on the flat mat.')
<re.Match object; span=(4, 7), match='cat'>
>>> atRegex.findall('The cat in the hat sat on the flat mat.')
['cat', 'hat', 'sat', 'lat', 'mat']
```

### 7.9.1 用点-星(.*)匹配所有字符

(.*)默认是贪心匹配模式  

```python
>>> nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
>>> mo = nameRegex.search('First Name: Al Last Name: Sweigart')
>>> mo.group(1)
'Al'
>>> mo.group(2)
'Sweigart'
>>> nonGreedyRegex = re.compile(r'<.*?>')
>>> mo = nonGreedyRegex.search('<To serve man> for dinner.>')
>>> mo.group()
'<To serve man>'
>>> greedyRegex = re.compile(r'<.*>')
>>> mo = greedyRegex.search('<To serve man> for dinner.>')
>>> mo.group()
'<To serve man> for dinner.>'
```

### 7.9.2 用句点字符匹配换行

compile()传入第二个参数re.DOTALL，表示句点符号可以匹配包含换行符的所有字符  

```python
>>> noNewLineRegex = re.compile('.*')
>>> noNewLineRegex.search('Serve the public trust.\n Protect the innocent.\n Uphold the low.')
<re.Match object; span=(0, 23), match='Serve the public trust.'>
>>> noNewLineRegex.search('Serve the public trust.\n Protect the innocent.\n Uphold the low.').group()
'Serve the public trust.'
>>> newLineRegex = re.compile('.*', re.DOTALL)
>>> newLineRegex.search('Serve the public trust.\n Protect the innocent.\n Uphold the low.')
<re.Match object; span=(0, 63), match='Serve the public trust.\n Protect the innocent.\n>
>>> newLineRegex.search('Serve the public trust.\n Protect the innocent.\n Uphold the low.').group()
'Serve the public trust.\n Protect the innocent.\n Uphold the low.'
```

## 7.10 正则表达式符号复习

\ 将下一个字符标记为一个特殊字符、或一个原义字符、或一个后向引用、或一个八进制转义符。  
^ 匹配输入字符串的开始位置。如果设置了 RegExp 对象的Multiline 属性，^ 也匹配 ’\n’ 或 ’\r’ 之后的位置。  
\$ 匹配输入字符串的结束位置。如果设置了 RegExp 对象的Multiline 属性，$ 也匹配 ’\n’ 或 ’\r’ 之前的位置。  
\* 匹配前面的子表达式零次或多次。  
\+ 匹配前面的子表达式一次或多次。+ 等价于 {1,}。  
? 匹配前面的子表达式零次或一次。? 等价于 {0,1}。  
{n} n 是一个非负整数，匹配确定的n 次。  
{n,} n 是一个非负整数，至少匹配n 次。  
{n,m} m 和 n 均为非负整数，其中n <= m。最少匹配 n 次且最多匹配 m 次。在逗号和两个数之间不能有空格。  
? 当该字符紧跟在任何一个其他限制符 (*, +, ?, {n}, {n,}, {n,m}) 后面时，匹配模式是非贪婪的。非贪婪模式尽可能少的匹配所搜索的字符串，而默认的贪婪模式则尽可能多的匹配所搜索的字符串。  
. 匹配除 "\n" 之外的任何单个字符。要匹配包括 ’\n’ 在内的任何字符，请使用象 ’[.\n]’ 的模式。  
(pattern) 匹配pattern 并获取这一匹配。 (?:pattern) 匹配pattern 但不获取匹配结果，也就是说这是一个非获取匹配，不进行存储供以后使用。 (?=pattern) 正向预查，在任何匹配 pattern 的字符串开始处匹配查找字符串。这是一个非获取匹配，也就是说，该匹配不需要获取供以后使用。 (?!pattern) 负向预查，与(?=pattern)作用相反 x|y 匹配 x 或 y。  
[xyz] 字符集合。  
[^xyz] 负值字符集合。  
[a-z] 字符范围，匹配指定范围内的任意字符。  
[^a-z] 负值字符范围，匹配任何不在指定范围内的任意字符。  
\b 匹配一个单词边界，也就是指单词和空格间的位置。  
\B 匹配非单词边界。  
\cx 匹配由x指明的控制字符。  
\d 匹配一个数字字符。等价于 [0-9]。  
\D 匹配一个非数字字符。等价于 [^0-9]。  
 \f 匹配一个换页符。等价于 \x0c 和 \cL。  
\n 匹配一个换行符。等价于 \x0a 和 \cJ。  
\r 匹配一个回车符。等价于 \x0d 和 \cM。  
\s 匹配任何空白字符，包括空格、制表符、换页符等等。等价于[ \f\n\r\t\v]。  
\S 匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。  
\t 匹配一个制表符。等价于 \x09 和 \cI。  
\v 匹配一个垂直制表符。等价于 \x0b 和 \cK。  
\w 匹配包括下划线的任何单词字符。等价于’[A-Za-z0-9_]’。  
\W 匹配任何非单词字符。等价于 ’[^A-Za-z0-9_]’。  
\xn 匹配 n，其中 n 为十六进制转义值。十六进制转义值必须为确定的两个数字长。  
\num 匹配 num，其中num是一个正整数。对所获取的匹配的引用。  
\n 标识一个八进制转义值或一个后向引用。如果 \n 之前至少 n 个获取的子表达式，则 n 为后向引用。否则，如果 n 为八进制数字 (0-7)，则 n 为一个八进制转义值。  
\nm 标识一个八进制转义值或一个后向引用。如果 \nm 之前至少有is preceded by at least nm 个获取得子表达式，则 nm 为后向引用。如果 \nm 之前至少有 n 个获取，则 n 为一个后跟文字 m 的后向引用。如果前面的条件都不满足，若 n 和 m 均为八进制数字 (0-7)，则 \nm 将匹配八进制转义值 nm。 \nml 如果 n 为八进制数字 (0-3)，且 m 和 l 均为八进制数字 (0-7)，则匹配八.  

## 7.11 不区分大小写的匹配

正则表达式默认是区分大小写的  
如果想要忽略大小再匹配，可以在compile()方法的第二个参数传入re.IGNORECASE或re.I  

```python
>>> robocop = re.compile(r'robocop', re.I)
>>> robocop.search('Robocop is part man, part machine, all cop.').group()
'Robocop'
>>> robocop.search('ROBOCOP protects the innocent.').group()
'ROBOCOP'
>>> robocop.search('Al, why does your programming book talk about robocop so much?').group()
'robocop'
```

## 7.12 用sub()方法替换字符串

sub()支持传入两个参数  
第一个参数是即将取代被匹配的字符串的新字符串  
第二个参数是正则表达式要去匹配的原字符串  

```python
>>> namesRegex = re.compile(r'Agent \w+')
>>> namesRegex.search('Agent Alice gave the secret documents to Agent Bob.')
<re.Match object; span=(0, 11), match='Agent Alice'>
>>> namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')
['Agent Alice', 'Agent Bob']
>>> namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
'CENSORED gave the secret documents to CENSORED.'
>>> agentNamesRegex = re.compile(r'Agent (\w)\w*')
>>> agentNamesRegex.findall('Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
['A', 'C', 'E', 'B']
>>> agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
'A**** told C**** that E**** knew B**** was a double agent.'
```

## 7.13 管理复杂的正则表达式

对于复杂难懂的正则表达式，如：

> phoneRegex = re.compile(r'((\d{3}|\\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')  

可以在compile()的第二个参数输入re.VERBOSE，并将正则表达式放入三重引号中，分成多行，添加注释，以#开头  

> phoneRegex = re.compile(r'''(  
> (\d{3}|\\(\d{3}\))?            # area code  
> (\s|-|\.)?                    # separator  
> \d{3}                         # first 3 digits  
> (\s|-|\.)                     # separator
> \d{4}                         # last 4 digits
> (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
> )''', re.VERBOSE)  

## 7.14 组合使用re.IGNORECASE、re.DOTALL和re.VERBOSE

re.IGNORECASE、re.DOTALL和re.VERBOSE利用管道符号|组合成compile()的第二个参数  
可以同时支持三种效果  

> someRegexValue = re.compile('foo', re.IGNORECASE|re.DOTALL|re.VERBOSE)  

此语法是在早期的Python版本引入的  
参考信息[https://nostarch.com/automatestuff](https://nostarch.com/automatestuff)  

## 7.15 项目：电话号码和E-mail地址提取程序

任务：

- 从剪贴板取得文本  
- 找出文本中的电话号码和E-mail地址  
- 将它们粘贴到剪贴板  

代码构思：

- 使用pyperclip模块复制和粘贴字符串  
- 创建两个正则表达式，分别匹配电话号码和E-mail地址  
- 找到两个正则表达式的所有匹配结果，而非第一次匹配  
- 整理匹配的字符串格式，放入一个字符串中，用于粘贴  
- 如果未找到匹配，显示某种消息  

参考示例脚本#7_15_phoneAndEmail.py  

### 第1步：为电话号码创建一个正则表达式

### 第2步：为E-mail创建一个正则表达式

### 第3步：在剪贴板文本中找到所有匹配

### 第4步：所有匹配连接成一个字符串，复制到剪贴板

### 第5步：运行程序

打开网址[https://nostarch.com/contactus.html](https://nostarch.com/contactus.html)或[https://www.csdn.net/company/index.html#about](https://www.csdn.net/company/index.html#about)或[https://www.qcc.com/?utm_source=baidu&utm_medium=cpc&utm_term=%E8%81%94%E7%B3%BB%E6%96%B9%E5%BC%8F](https://www.qcc.com/?utm_source=baidu&utm_medium=cpc&utm_term=%E8%81%94%E7%B3%BB%E6%96%B9%E5%BC%8F)，Ctrl+A，Ctrl+C，然后运行程序  

### 第6步：类似程序的构想

识别文本的模式(并可能用sub()方法替换他们)由许多不同潜在的应用  

- 寻找网站的URL，它们以http:// 或https:// 开始  
- 整理不同日期格式的日期，替换成唯一的标准格式  
- 删除敏感信息，诸如社会保险号码或信用卡号  
- 寻找常见打字错误，诸如单词键的多个空格、重复的单词，或多余的标点符号!!!  

## 7.16 小结

查找替换功能，re模块，re.compile()，re.search()，re.findall()，re.sub()  
更多相关的正则资源：  
[https://docs.python.org/3/library/re.html](https://docs.python.org/3/library/re.html)  
[https://www.regular-expressions.info/](https://www.regular-expressions.info/)  

## 7.17 习题

## 7.18 实践项目

### 7.18.1 强口令检测

强口令定义:  

- 长度不少于8个字符  
- 同时包含大写和小写字符  
- 至少有一位数字  

参考示例脚本#7_18_1_strongPwd.py  

### 7.18.2 strip()的正则表达式版本

自定义一个strip()方法，接收两个参数  
第一个参数，是要被操作的字符串  
第二个参数，是要被去除的字符。它是可选的  
如果未传第二个参数，则去除第一个参数的首尾空白字符串；  
如果传了第二个参数，则将第二个参数传入的字符串，从第一个参数中去除  

参考示例脚本#7_18_2_strip.py  
