# 第14章 处理CSV文件和JSON数据

CSV：Comma-Separated Values逗号分隔的值  
JSON：JavaScript Object Notation  

## 14.1 CSV模块

CSV文件，缺少Excel电子表格的很多功能：  

- 值没有类型，所有的值都是字符串  
- 没有字体大小和颜色设置  
- 没有多个工作表  
- 不能指定单元格的宽度和高度  
- 不能合并单元格  
- 不能嵌入图像或图表  

但CSV文件最大的优势就是简单：它就是一个文本文件，具有逗号分隔的值  
但是，不能简单的用split(',')方法处理每个单元格的值  
因为CSV有自己的转义符，如果单元格的值包含逗号(',')或其它关键字符，有可能就会出错  
这时，使用csv模块就变得很必要  

### 14.1.1 Reader对象

csv模块是Python自带的模块，可以直接导入  
通过open()方法生成一个File对象，然后把File对象传给csv.reader(fileObj)方法，返回一个Reader对象  
可以讲Reader对象转化为list(reader)，以方便操作数据  
比如list(reader)[0][0]就可以读取到第一行第一列的单元格的值  
参考示例代码#14_1_1_reader.py  

### 14.1.2 在for循环中，从Reader对象读取数据

当读取较大的CSV文件时，可以用for循环遍历Reader对象，以避免一次性讲整个文件装入内存  
Reader对象只支持向前一次性读取，故需要再次读取CSV文件，须再次生成新的File对象并用csv.reader(fileObj)方法调用  
参考示例代码#14_1_1_reader.py  

### 14.1.3 Writer对象

通过open()方法的写('w')模式打开将要写入的文件，这会得到一个File对象  
> 在Windows系统中，还需要为open()传入一个参数newline，值为空字符串。否则生成的csv文件会有两倍空行间距  

然后，将File对象传递给csv.writer(fileObj)，得到一个Writer对象  
Writer对象的writerow()接收一个列表参数，列表的每一项，将作为字符串，依次填入单元格，其返回值，为写入的字符数  
如果某一项内容包含逗号，请将整个字符串用引号包裹，csv模块会自动处理  

### 14.1.4 delimiter和lineterminator关键字参数

CSV文件的分隔符delimiter是逗号(',')，行终止符lineterminator是换行符('\n')  
我们可以通过这两个关键字，替换成想要的格式：  
在csv.writer()打开文件的时候，用新的符号替换掉即可  
参考示例脚本#14_1_4_tsv.py，生成一个制表符分隔的值的文件，扩展名为.tsv  

## 14.2 项目：从CSV文件中删除表头

在程序执行操作前，记得备份好原数据  
程序要求：  

- 找到当前目录的所有CSV文件  
- 读取每个文件的全部内容  
- 跳过第一行，将内容写入新的csv文件  
  
代码实现：  

- 循环遍历从os.listdir()得到的文件列表，跳过非CSV文件  
- 创建一个CSV Reader对象，读取文件内容，利用line_num确定要跳过的行  
- 创建一个CSV Writer对象，将读入的数据写入新文件  

参考实例代码#14_2_removeCsvHeader.py  

### 第1步：循环遍历每个CSV文件

### 第2步：读入CSV文件

### 第3步：写入CSV文件，没有第一行

### 第4步：类似程序的思想

- 在一个CSV文件的不同行，或多个CSV文件之间比较数据  
- 从CSV文件拷贝特定的数据到Excel文件，或反过来  
- 检查CSV文件中无效的数据或格式错误，并向用户提醒这些错误  
- 从CSV文件读取数据，作为Python的输入  

## 14.3 JSON和API

利用API可以编程完成以下任务：

- 从网站抓取原始数据(访问API通常比下载网页并用Beautiful Soup解析HTML更方便)  
- 自动从一个社交网络账户下载新的帖子，并发布到另一个账户。如，可以把tumblr的帖子上传到Facebook  
- 从Imdb。Rotten Tomatoes和维基百科提取数据，放到计算机的一个文本文件中，为个人电影收藏创建一个"电影百科全书"  

## 14.4 Json模块

JSON格式只能包含以下的Python数据类型：字符串、整型、浮点型、布尔型、列表、字典和NoneType  
JSON也无法表示Python特有的对象：File对象、CSV Reader或Writer对象、Regex对象或Selenium WebElement对象  
Python自带的json模块通过loads()函数和dumps()函数操作JSON格式的字符串，函数名中的's'就是'string'的缩写  
参考示例脚本#14_4_json.py  

### 14.4.1 用loads()函数读取JSON

JSON字符串总是用双引号，且json模块处理后，会返回一个字典，包含原有的json数据，但是顺序可能不同  

### 14.4.2 用dumps()函数写出JSON

该函数将Python值转为JSO格式的数据，且该值只能是以下数据类型之一：  
字典、列表、整型、浮点型、字符串、布尔型或None  

## 14.5 项目：取得当前的天气数据

程序要求：  

- 从命令行读取请求位置  
- 从OpenWeatherMap.org下载JSON天气数据(默认是JSON格式，也支持XML格式)  
- 将JSON数据字符串转换成Python数据结构  
- 打印今天和未来两天的天气  

代码实现：  

- 连接sys.argv中的字符串，得到位置  
- 调用request.get()下载天气数据  
- 调用json.loads()将JSON数据转换为Python数据结构  
- 打印天气预报  

注意，现在OpenWeatherMap.org需要注册之后才能使用它提供的API  
具体操作请参考网站的最新介绍  

参考示例脚本#14_5_quickWeather.py  

### 第1步：从命令行参数获取位置  

> 14_5_quickWeather my_api_id San Francisco  
运行上述命令后，sys.argv会保存为['14_5_quickWeather', 'my_api_id', 'San', 'Francisco']  
程序会将appid后面的几个参数连接成一个字符串，作为传入的位置数据  

### 第2步：下载JSON数据  

利用位置参数和需要预告的天数构造请求的url  
利用requests.get(url)得到Response对象  
具体的天气数据，可以从response.text属性获取  

### 第3步：加载JSON数据并打印天气  

关于返回的JSON数据结构，可以从https://openweathermap.org/ 查找相关文档说明  

### 第4步：类似程序的思想

- 收集几个露营地点，或远足路线的天气预报，看一下哪天天气最好  
- 如需要将植物移到室内，安排一个程序检查天气预报，并发送霜冻警报  
- 从多个站点获得气象数据，同时显示。或计算并显示多个天气预报的平均值  

## 14.6 小结

csv模块和json模块是Python自带的模块，方便我们处理CSV文件和JSON格式的数据  

## 14.7 习题

## 14.8 实践项目

### Excel到CSV的转换程序

参考示例脚本#14_8_excelTocsv.py  
