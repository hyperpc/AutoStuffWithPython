# 第9章 组织文件

## 9.1 shutil模块

shutil(shell工具)模块

### 9.1.1 复制文件和文件夹

shutil.copy(source, destination)，将路径source处的文件复制到路径destination出的文件夹。如果destination包含文件名，则将它作为被赋值后的新的文件名。该函数返回复制后的文件路径  
shutil.copytree(source, destination)，将复制整个文件夹，包括它包含的子文件夹和文件。函数返回复制后的文件路径  

```python
>>> import shutil, os
>>> os.chdir('C:\\')
>>> shutil.copy('C:\\spam.txt', 'C:\\delicious')
'C:\\delicious\\spam.txt'
>>> shutil.copy('eggs.txt', 'C:\\delicious\\eggs2.txt')
'C:\\delicious\\eggs2.txt'

>>> shutil.copytree('C:\\bacon', 'C:\\bacon_backup')
'C:\\bacon_backup'
```

### 9.1.2 文件和文件夹的移动与改名

shutil.move(source, destination)，将路径source处的文件夹移动到路径destination，并返回新位置的绝对路径  
如果destination指向一个文件夹，文件会被移动到该文件夹下，并保持原来的文件名  
如果要移动的文件，在destination处已经存在同名的文件，则已经存在的文件会被覆写  
如果source指向一个文件，destination指向一个新文件，则移动后的文件以destination指定的名字命名  
如果destination指向一个文件夹，但该文件夹不存在，Python会认为他是一个新文件名，被移动的文件会以此作为新文件名  
如果destination路径的中间某一层文件夹不存在，则程序会报错FileNotFoundError  

```python
>>> import shutil
>>> shutil.move('C:\\bacon.txt', 'C:\\eggs')
'C:\\eggs\\bacon.txt'
>>> shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt')
'C:\\eggs\\new_bacon.txt'

>>> shutil.move('spam.txt', 'C:\\does_not_exist\\eggs\\ham')
```

### 9.1.3 永久删除文件和文件夹

- os.unlink(path) 删除path处的文件  
- os.rmdir(path) 删除path处的文件夹。该文件夹必须为空，不包含任何文件和文件夹  
- shutil.rmtree(path) 删除path处的文件夹，其包含的所有子文件夹和文件都会被删除  

建议在执行删除程序时，先将删除语句注释掉，只打印要删除的路径，以确认是否操作正确  
确认无误后再取消注释  

```python
>>> import os
>>> for filename in os.listdir():
>>>     if filename.endswith('.rxt'):
>>>         # os.unlink(filename)
>>>         print(filename)
```

### 9.1.4 用send2trash模块安全地删除

shutil.rmtree()函数是不可恢复地删除文件和文件夹  
第三方模块send2trash可以将文件和文件夹删除到回收站，以方便找回  

> pip install send2trash  

```python
>>> import send2trash
>>> baconFile = open('bacon.txt', 'a') # creates the file
>>> baconFile.write('Bacon is not a vegetable.')
25
>>> baconFile.close()
>>> send2trash.send2trash('bacon.txt')
```

## 9.2 遍历目录树

os.walk(path)返回传入文件夹包含的文件及各级子文件夹组成的类似列表  
循环迭代返回的类似列表数据，返回3个值  

- 当前文件夹名称的字符串  
- 当前文件夹中子文件夹的字符串列表  
- 当前文件夹中文件的字符串列表  

```python
>>> import os
>>> for foldername, subfolders, filenames in os.walk('D:\\pyAuto'):
>>>     print('The current folder is ' + foldername)
>>>     for subfolder in subfolders:
>>>         print('SUBFOLDER OF ' + foldername + ': ' + subfolder)
>>>     for filename in filenames:
>>>         print('FILE INSIDE ' + foldername + ': ' + filename)
```

## 9.3 用zipfile模块压缩文件

### 9.3.1 读取ZIP文件

zipfile模块，首先创建ZipFile函数对象。该对象支持的操作和File对象类似  
zipfile.ZipFile(filename, open_mode)，openmode支持'r'读，'w'写，'a'添加  

```python
>>> import zipfile, os
>>> os.chdir('C:\\') # move to the folder with example.zip
>>> exampleZip = zipfile.ZipFile('example.zip')
>>> exampleZip.namelist()
['spam.txt', 'cats/', 'cats/catnames.txt' 'cats/zophie.jpg']
>>> spamInfo = exampleZip.getinfo('spam.txt')
>>> spamInfo.file_size
13908
>>> spamInfo.compress_size
3828
>>> 'Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2))
'Compressed file is 3.63x smaller!'
>>> exampleZip.close()
```

### 9.3.2 从ZIP文件中解压缩

ZipFile对象的extractall()方法从ZIP文件中解压缩所有的文件和文件夹，放到当前工作目录下  
extract(filename[, path])方法从ZIP文件中解压缩指定的filename文件，放到指定的path目录，默认是当前目录  

```python
>>> import zipfile, os
>>> os.chdir('C:\\') # move to the folder with example.zip
>>> exampleZip = zipfile.ZipFile('example.zip')
>>> exampleZip.extractall()
>>> exampleZip.close()
```

### 9.3.3 创建和添加到ZIP文件

创建ZipFile对象时，需要指定‘写模式’打开该对象  
write()方法传入的第一个参数是要添加到压缩文件的文件名，第二个参数是压缩类型(一般为zipfile.ZIP_DEFLATED)  

```python
>>> import zipfile
>>> newZip = zipfile.ZipFile('new.zip', 'w')
>>> newZip.write('spam.txt', compress_type = zipfile.ZIP_DEFLATED)
>>> newZip.close()
```

## 9.4 项目：将带有美国风格日期的文件改名为欧洲风格日期

### 第1步：为美国风格的日期创建一个正则表达式

### 第2步：识别文件名中的日期部分

### 第3步：构成新文件名，并对文件改名

### 第4步：类似程序的想法

参考示例脚本#9_4_renameDates.py  

## 9.5 项目：将一个文件夹备份到一个ZIP文件

### 第1步：弄清楚ZIP文件的名称

### 第2步：创建新ZIP文件

### 第3步：遍历目录树并添加到ZIP文件

### 第4步：类似程序的想法

参考示例脚本#9_5_backupToZip.py  

## 9.6 小结

os和shutil模块的复制、移动、改名和删除文件，send2trash模块，os.walk()遍历文件夹，zipfile模块

## 9.7 习题

## 9.8 实践项目

### 9.8.1 选择性拷贝

参考示例代码#9_8_copyFile.py，将某文件夹下所有的\*.py，\*.pyw和\*.bat文件备份到一个专门的文件夹下  

### 9.8.2 删除不需要的文件

参考示例代码#9_8_delBigFile.py

### 9.8.3 清除缺失的编号

参考示例代码#9_8_fillMissNum.py  
