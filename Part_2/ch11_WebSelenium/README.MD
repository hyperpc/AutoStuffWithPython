# 第11章 从Web抓取信息

Web抓取，是一个术语，即利用程序下载并处理来自Web的内容  

- webbrowser：是Python自带的，打开浏览器获取指定页面  
- requests：从internet上下载文件和网页  
- Beautiful Soup：解析HTML，即网页编写的格式  
- selenium：启动并控制一个Web浏览器。selenium能够填写表单，并模拟鼠标在这个浏览器中点击  

## 11.1 项目：利用webbrowser模块的mapIt.py

webbrowser模块的open()函数，可以启动一个浏览器  
新建脚本mapIt.py  

### 第1步：弄清楚URL

通过命令行参数，传递url参数；而不是通过剪贴板  

### 第2步：处理命令行参数

通过sys模块的argv变量，获取程序文件名和命令行参数列表  
> mapIt 870 Valencia st, San Francisco, CA 94110  

### 第3步：处理剪贴板内容，加载浏览器

通过pyperclip模块操作剪贴板内容  

### 第4步：类似程序的想法

- 在独立浏览器标签，打开一个页面的所有链接  
- 用浏览器打开本地天气的URL  
- 打开你经常查看的几个网站  

参考示例脚本#11_1_webbrowser.py  

## 11.2 用requests模块从Web下载文件

requests模块不是Python自带的，但比自带的urllib2方便使用
> pip install requests  

### 11.2.1 用requests.get()函数下载一个网页

requests.get()函数接受一个要下载的URL字符串做参数  

### 11.2.2 检查错误

在Response对象上调用raise_for_status()方法，可以检查调用是否成功，以确定是否继续执行  
当下载文件出错时，这个方法会报异常。建议用try和except语句包裹，防止程序崩溃  

```python
>>> import requests
>>> res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
>>> type(res)
<class 'requests.models.Response'>
>>> res.status_code == requests.codes.ok
True
>>> len(res.text)
179380
>>> print(res.text[:250])
﻿The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare





*******************************************************************

THIS EBOOK WAS ONE OF PROJECT GUTENBERG'S EARLY FILES PRODUCED AT A

TIME WHEN PROOFING METHODS AND TOO
>>> res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
>>> res.raise_for_status()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    res.raise_for_status()
  File "C:\Users\LENOVO\AppData\Roaming\Python\Python310\site-packages\requests\models.py", line 953, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 404 Client Error: Not Found for url: http://inventwithpython.com/page_that_does_not_exist
>>> try:
>>>     res.raise_for_status()
>>> except Exception as exc:
>>>     print('There was a problem: %s' % (exc))

There was a problem: 404 Client Error: Not Found for url: http://inventwithpython.com/page_that_does_not_exist
```

## 11.3 将下载的文件保存到硬盘

将web页面保存到硬盘中的一个文件：  

- 以“写二进制”模式('wb')打开硬盘中的文件  
- 迭代Response对象的iter_content()方法，返回一段bytes类型的内容，指定字节大小  

参考示例脚本#11_3_downloadFile.py  

## 11.4 HTML

### 11.4.1 学习HTML的资源

只针对HTML初学者：  

- [HTML Beginner Tutorial](http://htmldog.com/guides/html/beginner/)  
- [Codecademy](http://www.codecademy.com/tracks/web/)  
- [MDN Web Docs - en](https://developer.mozilla.org/en-US/learn/html/)  
- [MDN Web Docs - cn](https://developer.mozilla.org/zh-CN/docs/Learn/HTML)

### 11.4.2 快速学习

HTML的加粗标签：&lt;strong&gt;和&lt;b&gt;  
首先，从语义上来说&lt;b&gt;是UI层面上的‘加粗’，而&lt;strong&gt;是语气上的强调。  
其次，官方解释：根据 HTML5 规范，在没有其他合适标签更合适时，才<b style='color:red'>应该把&lt;b&gt;标签作为最后的选项</b>。HTML5 规范声明：应该使用&lt;h1&gt;-&lt;h6&gt;来表示标题，使用 &lt;em&gt;标签来表示强调的文本，应该使用&lt;strong&gt;标签来表示重要文本，应该使用 &lt;mark&gt;标签来表示标注的/突出显示的文本。提示：您也能够使用 CSS "font-weight" 属性来设置粗体文本。  

### 11.4.3 查看网页的HTML源代码

网页上点击鼠标右键，选择View Soure  

### 11.4.4 打开浏览器的开发者工具

快捷键F12  
View -> Developer -> Developer Tools
注意，不要用正则表达式解析HTML源码。因为不同浏览器对HTML解析不一致，且HTML对语法的解释是非常宽容的，所以正则表达式难以做到面面俱到  

### 11.4.5 使用开发者工具来寻找HTML元素

在页面的右键菜单中，有类似‘Inspect Element’或‘检查’的菜单，可以打开开发者工具，并定位到相应部分的HTML源码  

## 11.5 用BeatifulSoup模块解析HTML

安装BeatifulSoup模块(名称是bs4，指第4版)：  
> pip install beautifulsoup4  

准备一个HTML文件：example.html  

### 11.5.1 从HTML创建一个BeautifulSoup对象

bs4.BeautifulSoup()函数接收一个字符串(requests.get(url)返回的text属性，或一个已知File对象)  

```python
>>> import requests, bs4
>>> #res = requests.get('https://nostarch.com')
>>> res = requests.get('https://www.baidu.com/')
>>> res.raise_for_status()
>>> noStarchSoup = bs4.BeautifulSoup(res.text)
>>> type(noStarchSoup)
<class 'bs4.BeautifulSoup'>
```

### 11.5.2 使用select()方法寻找元素

select(选择器)返回Tag对象列表，每个Tag对象包含一段HTML标签，以及可操作这些标签的方法  

|select()方法的选择器|将匹配...|
|:---|:---|
|soup.select('div')|所有名为&lt;div&gt;的元素|
|soup.select('#author')|带有id属性值为author的元素|
|soup.select('.notice')|所有使用CSS class属性名为notice的元素|
|soup.select('div span')|所有在&lt;div&gt;元素内的&lt;span&gt;元素|
|soup.select('div>span')|所有直接在&lt;div&gt;元素内的&lt;span&gt;元素，中间无其他元素|
|soup.select('input[name]')|所有&lt;input&gt;，并有name属性，无论何值的元素|
|soup.select('input[type="button"]')|所有&lt;input&gt;，并有type属性，值为button的元素|

### 11.5.3 通过元素的属性获取数据

Tag对象的get()方法，可以从元素中获取属性值

参考示例代码#11_5_example.py  

## 11.6 项目：“I'm Feeling Lucky”Google查找

程序目标：  

- 从命令行参数中获取查询关键字  
- 取得查询结果页面  
- 为每个结果打开一个浏览器选项卡  

代码实现：  

- 从sys.argv中读取命令行参数  
- 用requests模块取得查询结果页面  
- 找到每个查询结果的链接  
- 调用webbrowser.open()函数打开Web浏览器  

参考示例脚本#11_6_lucky.py  

### 第1步：获取命令行参数，并请求查找页面

明确查找结果页面的URL结构  

### 第2步：找到所有结果

从浏览器的开发者工具中，根据元素&lt;h3 class="r"&gt;找到需要的链接  

### 第3步：针对每个结果打开Web浏览器

使用webbrowser模块，在新选项卡中打开排名靠前的几个搜索结果  
可以在命令行运行以下命令：  
> lucky python programming tutorials  

### 第4步：类似程序的想法

- 查找电商网站的某商品，打开所有的查找结果  
- 打开针对某产品的所有评论链接  
- 查找Flickr或Imgur这样的图片网站后，打开查找结果中所有照片链接  

## 11.7 项目：下载所有XKCD漫画

[XKCD](https://xkcd.com/)是一个流行的极客漫画网站  
程序目标：  

- 加载主页  
- 保存该页的漫画图片  
- 转入前一张漫画的链接  
- 重复直到第一张漫画  

代码逻辑：  

- 利用requests模块下载页面  
- 利用BeautifulSoup找到页面中漫画图像的URL  
- 利用iter_content()下载漫画图像，并保存到硬盘  
- 找到前一张漫画的链接URL，然后重复  

参考示例脚本#11_7_downloadXkcd.py  
在示例脚本中，控制了下载漫画的张数为前10张  

### 第1步：设计程序

### 第2步：下载网页

### 第3步：寻找和下载漫画图像

### 第4步：保存图像，找到前一张漫画

### 第5步：类似程序的想法

- 顺着网站的所有链接，备份整个网站  
- 拷贝一个论坛的所有信息  
- 复制一个在线商店中所有商品的目录  

## 11.8 用selenium模块控制浏览器

安装第三方模块selenium：  

> pip install selenium  

selenium模块会启动Web浏览器，模拟人类的一些交互行为，比Requests和BeautifulSoup模块更高级，但速度会更慢，难以在后台运行  
惨开示例脚本#11_8_selenium.py  
注意，如果未打开，或打开后无法跳转指定网址，请先下载跟Edge版本对应的[Microsoft Edge Driver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)  

### 11.8.1 启动selenium控制的浏览器

导入selenium模块有些特殊，使用如下方式：  

> from selenium import webdriver  

### 11.8.2 在页面中寻找元素

find_element_*方法返回页面中匹配查询的第一个WebElement对象  
find_elements_*方法返回页面中所有匹配查询的WebElement对象列表  

|方法名|返回的WebElement对象/列表|
|:---|:---|
|browser.find_element_by_class_name(name)|返回CSS类name的第一个元素|
|browser.find_elements_by_class_name(name)|返回CSS类name的元素列表|
|browser.find_element_by_css_selector(selector)|匹配CSS selector的第一个元素|
|browser.find_element_by_css_selector(selector)|匹配CSS selector的元素列表|
|browser.find_element_by_id(id)|匹配id属性值的第一个元素|
|browser.find_elements_by_id(id)|匹配id属性值的元素列表|
|browser.find_element_by_link_text(text)|完全匹配提供的text的第一个&lt;a&gt;元素|
|browser.find_elements_by_link_text(text)|完全匹配提供的text的&lt;a&gt;元素列表|
|browser.find_element_by_partial_link_text(text)|包含提供的text的第一个&lt;a&gt;元素|
|browser.find_elements_by_partial_link_text(text)|包含提供的text的&lt;a&gt;元素列表|
|browser.find_element_by_name(name)|匹配name属性值的第一个元素|
|browser.find_elements_by_name(name)|匹配name属性值的元素列表|
|browser.find_element_by_tag_name(name)|匹配标签name的第一个元素(大小写无关，&lt;a&gt;元素匹配'a'和'A')|
|browser.find_elements_by_tag_name(name)|匹配标签name的元素列表(大小写无关，&lt;a&gt;元素匹配'a'和'A')|

以上表格中，除了*_by_tag_name(name)方法，其余的方法参数都是区分大小写的  
如果未找到元素，selenium模块会报出NoSuchElement异常  

|属性或方法|描述|
|:---|:---|
|tag_name|标签名，例如'a'表示&lt;a&gt;元素|
|get_attribute(name)|该元素name属性的值|
|text|该元素内的文本，例如&lt;span&gt;hello&lt;/a&gt;中的'hello'|
|clear()|对于文本字段或文本区域元素，清除其中输入的文本|
|is_displayed()|如果该元素可见，返回True，否则返回False|
|is_enabled()|对于输入元素，如果该元素启用，返回True，否则返回False|
|is_selected()|对于复选框或单选框元素，如果该元素被选中，返回True，否则返回False|
|location|一个字典，包含键'x'和'y'，表示该元素在页面上的位置|

### 11.8.3 点击页面

调用find_element_\*和find_elements_\*返回WebElement对象的click()方法，模拟鼠标点击该元素的效果  

### 11.8.4 填写并提交表单

找到页面文本字段所属的&lt;input&gt;或&lt;textarea&gt;，然后调用send_keys()方法  
在表单内的任何元素上调用submit()方法，等同于表单的Submit按钮  

### 11.8.5 发送特殊按钮

selenium有一个模块，针对不能用字符串值输入的键盘左键击键  
selenium.webdriver.common.keys  
如果向如下方式导入，可以直接通过Keys调用：  

> from selenium.webdriver.common.keys import Keys  

|属性|含义|
|:---|:---|
|Keys.DOWN，Keys.UP，Keys.LEFT，Keys.RIGHT|键盘箭头键|
|Keys.ENTER，Keys.RETURN|回车和换行键|
|Keys.HOME，Keys.END，Keys.PAGE_UP，Keys.PAGE_DOWN|Home键，End键，PageUp键，PageDown键|
|Keys.ESCAPE，Keys.BACK_SPACE，Keys.DELETE|Esc，Backspace和删除键|
|Keys.F1，Keys.F2，...，Keys.F12|键盘顶部的F1到F12键|
|Keys.TAB|Tab键|

调用find_element_by_tag_name('html')是向一般Web页面发送按键的好地方。当滚到页面底部，新内容就会加载  

### 11.8.6 点击浏览器按钮

selenium可以模拟点击各种浏览器按钮：  

- browser.back() 点击返回按钮  
- browser.forward() 点击前进按钮  
- browser.refresh() 点击刷新按钮  
- browser.quit() 点击关闭窗口按钮  

### 11.8.7 关于selenium的更多信息

可以修改浏览器的cookie，截取页面快照，运行定制的JavaScript  
[更多](https://selenium-python.readthedocs.io/)  

## 11.9 小结

webbrowser打开浏览器，可指定特定网址  
requests下载文件和网页，BeatifulSoup解析网页，selenium可以自动化操作网页  

## 11.10 习题

## 11.11 实践项目

### 11.11.1 命令行邮件程序

利用selenium登录到某个邮件账号，参考示例脚本#11_11_emailLogon.py  
<b style="color:red;">本实例演示未通过</b>

### 11.11.2 图像网站下载

通过程序脚本，访问任何一个有查找功能的图片网站，搜索某一类型的图片，并下载前10个搜索到的图片  

### 11.11.3 2048

通过程序脚本，访问[2048](https://gabrielecirulli.github.io/2048/)，不断发送上、右、下、左按键，自动玩游戏，得高分  

### 11.11.4 链接验证

通过程序脚本，下载某特定页面的所有链接页面，找到并下载所有具有404"Not Found"状态码的坏链页面  
