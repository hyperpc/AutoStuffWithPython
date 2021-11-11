# 第13章 处理PDF和Word文档

## 13.1 PDF文档

PDF: Portable Document Format, *.pdf  
PyPDF2模块，模块名区分大小写  
> pip install PyPDF2  

### 13.1.1 从PDF提取文本

PyPDF2模块无法从PDF文档中提取图像、图表或其他媒体，但可以提取文本，并返回为Python字符串  
注意，模块打开PDF文档时，使用读二进制模式('rb')打开文件  
参考示例脚本#13_1_1_readPDF.py  

### 13.1.2 解密PDF

针对加密过的PDF文档，使用上述方式读取文档会产生异常  
判断PdfFileReader对象的isEncrypted属性，为True时，应使用decrypt()，将口令字符串作为参数传入  
参考示例脚本#13_1_2_readEncryptedPDF.py  

### 13.1.3 创建PDF

PyPDF2通过PdfFileWriter对象，创建一个新pdf文件  
其写入能力，但仅限于从其他pdf中拷贝页面、旋转页面、重叠页面和加密文件  
模块不允许直接编辑pdf文件  
一般创建步骤如下：  

- 打开一个或已有PDF(源PDF)，得到PdfFileReader对象  
- 创建一个新的PdfFileWriter对象  
- 将页面从PdfFileReader对象拷贝到PdfFileWriter对象中  
- 最后，利用PdfFileWriter对象，写入输出的PDF  

通过Python的open()函数，以写二进制模式('wb')打开一个将要创建的pdf文件  
然后调用PdfFileWriter对象的write()方法，将open()得到的File对象作为参数传入  
此时才会真正创建一个新的pdf物理对象  

### 13.1.4 拷贝页面

PyPDF2模块不能再PdfFileWriter对象中间插入页面，addPage()方法智能在末尾添加页面  
参考示例脚本#13_1_4_copy.py  

### 13.1.5 旋转页面

利用rotateClockWise()和rotateCounterClockWise()方法，PDF文档的页面可以旋转90度的整数倍  
参考示例脚本#13_1_5_rotate.py  

### 13.1.6 叠加页面

PyPDF2模块可以将多个页面叠加在一起，以实现类似公司标志、时间戳或水印的效果  
通过Python，可以方便的为多个指定的页面添加水印  
参考示例脚本#13_1_6_watermarkedCover.py  

### 13.1.7 加密PDF

调用writer()方法之前，通过encrypt()方法加密。传入两个参数。
第一个参数为用户口令，允许查看文件  
第二个参数为拥有者口令，允许设置打印、注释、提取文本和其他功能  
如果只传入一个口令，则会用作两个相同的口令使用  
参考示例脚本#13_1_7_encrypt.py  

## 13.2 项目：从多个PDF中合并选择的页面

程序期望：  

- 找到当前目录下的所有pdf文件  
- 按文件名排序，可以有序添加文件  
- 除了第一页封面外，每个pdf的所有页面写入输出的文件  

代码任务：  

- os.listdir()找到当前目录的所有文件，去除非PDF文件  
- Python的sort()方法，对文件名按字母排序  
- 为输出的PDF文件创建PdfFileWriter对象  
- 循环遍历每个PDF文件，并创建各自的PdfFileReader对象  
- 依次循环遍历每一个PDF文件的每一页，第一页除外  
- 将页面添加到输出的PDF  
- 将输出的PDF写入一个文件allminutes.pdf

参考示例代码#13_2_combinedPdfs.py  

### 第1步：找到所有的PDF文件

```python
import PyPDF2, sys, os

def combinedPdfs():
    currentPath = os.path.dirname(sys.argv[0])
    # Get all the pdf filename
    pdfFiles = []
    #for filename in os.listdir('.\\Part_2\\ch13_pdfWord\\13_2\\'):
    for filename in os.listdir(os.path.join(currentPath, '13_2')):
        if filename.endswith('.pdf'):
            pdfFiles.append(filename)
    pdfFiles.sort(key=str.lower)
    writer = PyPDF2.PdfFileWriter()
```

### 第2步：打开每个PDF文件

```python
    #loop through all the pdfs
    for filename in pdfFiles:
        pdfFileObj = open(os.path.join(currentPath, filename), 'rb')
        reader = PyPDF2.PdfFileReader(pdfFileObj)
```

### 第3步：添加每一页

```python
        # loop through all the pages(except the first) and add them
        for pageNum in range(1, reader.numPages):
            pageObj = reader.getPage(pageNum)
            writer.addPage(pageObj)
```

### 第4步：保存结果

```python
    # save the resulting pdf to a file
    pdfOutput = open(os.path.join(currentPath, '13_2', 'allminutes.pdf'), 'wb')      
    writer.write(pdfOutput)
    pdfOutput.close()  
```

### 第5步：类似程序的想法

- 从PDF文件中截取特定的页面  
- 重新调整PDF文件中页面的次序  
- 创建一个PDF文件，只包含那些具有特定文本的页面。文本由extractText()来确定  

## 13.3 Word文档

Python利用python-docx模块创建和修改扩展名为.docx的Word文档  
> pip install python-docx  

模块名称是[python-docx](https://python-docx.readthedocs.io/)，(docx是其他的已有的模块名)  
程序中引入python-docx使用import docx，而不是import python-docx  
python-docx将.docx文档结构解析成三种类型对象：  

- Document，表示整个文档  
- Paragraph，包含在Document对象中，表示文档中的一个段落  
- Run，每个Paragraph对象包含一个Run对象的列表  

Word文档中除了文本，还有相关的字体，大小和颜色等信息。样式是这些属性的集合  
一个Run对象就是相同样式文本的延续。文本样式发生变化时，就需要一个新Run对象  
参考示例脚本#13_3_0_demo.py  

### 13.3.1 读取Word文档

docx.Document(os.path.join(currentPath, 'demo.docx'))  
doc.paragraphs
doc.paragraphs[0].text
doc.paragraphs[1].runs
doc.paragraphs[1].runs[0].text

### 13.3.2 从.docx文件中取得完整的文本

for...in循环doc.paragraphs读取，并打印  
中间可以设置文本的格式  

### 13.3.3 设置Paragraph和Run对象的样式

Word文档的3种样式：段落样式(Paragraph对象)、字符样式(Run对象)和链接样式(Paragraph对象和Run对象)  
当前版本的python-docx模块，只支持Word的默认样式，和打开文档中的已有样式，不能创建新样式。  
通过Paragraph对象或Run对象的style属性，赋值为一个样式字符串(中间不能有空格)  
如果赋值为None，则没有样式与此对象关联  
默认的Word样式字符串：  
|||||
|:---|:---|:---|:---|
|Normal|Heading5|ListBullet|ListParagraph|
|BodyText|Heading6|ListBullet2|MacroText|
|BodyText2|Heading7|ListBullet3|NoSpacing|
|BodyText3|Heading8|ListContinue|Quote|
|Caption|Heading9|ListContinue2|Subtitle|
|Heading1|IntenseQuote|ListContinue3|ToCHeading|
|Heading2|List|ListBullet|Title|
|Heading3|List2|ListNumber2|-|
|Heading4|List3|ListNumber3|-|
||||

设置链接样式：  
paragraphObj.style = 'Quote'  
runObj.style = 'QuoteChar'  

### 13.3.4 创建带有非默认样式的Word文档

打开一个空白Word文档，点击样式窗口底部的New Style按钮，  
在打开的"Create New Style from Formatting"对话框，在此输入新样式。  
然后，返回交互式环境，用docx.Document()打开这个空白Word文档，利用它作为Word文档的基础。  
现在，新样式的名称就可以被python-docx模块使用了  

### 13.3.5 Run属性

除了style属性，还可以利用Run对象的text属性，继续设置需要的样式  

Run对象的text属性：  
|属性|描述|
|:---|:---|
|bold|粗体|
|italic|斜体|
|underline|下划线|
|strike|删除线|
|double_strike|双删除线|
|all_caps|首字母大写|
|small_caps|首字母大写，小写字母小两磅|
|shadow|阴影|
|outline|空心轮廓线|
|rtl|从右至左书写|
|imprint|刻入页面|
|emboss|凸出页面|

上表中的每个属性值都有3种值可选：  

- True：总是启用，不论其他样式是否应用到该Run对象  
- False：总是禁用  
- None：默认使用该Run对象被设置的任何属性

### 13.3.6 写入Word文档

通过docx.Document()创建新的Word文档对象doc，然后doc.add_paragraph('text')在文档末尾添加一个新的Paragraph对象，并返回该Paragraph对象  
同样地，add_run('text')，在对应的Paragraph对象末尾添加新的Run对象，并返回该Run对象  
参考示例脚本#13_3_6_multipleparagraphs.py  

### 13.3.7 添加标题

doc.add_paragraph('heading', 0)可以在文档中添加标题  
第一个参数是标题内容，第二个参数是标题样式，0到4  
参考示例脚本#13_3_7_headings.py  

### 13.3.8 添加换行符和换页符

doc.add_break(docx.text.WD_BREAK.PAGE)会在调用它的Run对象后插入分页符，强制后面的段落出现在新页面中  
在新版本python-docx模块中，添加分页符的方式为：doc.add_page_break()  
参考示例脚本#13_3_8_newpage.py  

### 13.3.9 添加图像

doc.add_picture('', )可以在文档末尾添加一个图像  
第一个参数指定图像位置  
第二和第三个参数设置图像的宽度和高度，单位支持英制和公制，而且两个参数的单位互不影响，如英寸和厘米  
参考示例脚本#13_3_9_image.py  

## 13.4 小结

## 13.5 习题

## 13.6 实践项目

### 13.6.1 PDF偏执狂

在当前目录(包含子文件夹)遍历所有pdf文件，用命令行提供的口令解密这些文件，并保存为新的文件名(原文件名加上_encrypted.pdf后缀)  
再遍历加密的pdf文件(包括子文件夹)，利用已有的口令，创建解密的拷贝。  
如果口令不对，打印处相应信息；然后继续处理下一个pdf文件  
参考示例脚本#13_6_1_encrypt_decrypt.py  

### 13.6.2 定制邀请函，保存为Word文档

为guests.txt中列出的客人名单，每人制作一份邀请函  

- 利用空白Word文档新建需要的样式  
- python-docs模块打开该文件  
- 生成Word邀请函  
- 每份邀请函占一页，所以在每页最后通过add_break()，添加分页符  
- 每行文本居中显示，注意每行的样式并不完全相同  
参考示例脚本#13_6_2_invitation.py  

### 13.6.3 暴力PDF口令破解程序

如果某一加密的PDF的口令为某一个英文单词，但不知具体是什么单词  
暴力口令攻击，以破解加密的PDF。
循环读取dictionary.txt中的每一行，依次使用每行的单词尝试解密  
如果decrypt()方法返回0，表示口令错误，继续尝试下一行的单词  
如果decrypt()方法返回1，循环应该终止，并打印出找到的破解口令  
注意，文本中的单词都是大写形式，应该大小写形式都尝试依次  
参考示例脚本#13_6_3_brute_force_pdf.py  
