# 第12章 处理Excel电子表格

## 12.1 Excel文档

Windows系统下的Office Excel文档，扩展名.xslx  
另外，[LibreOffice Calc](https://www.libreoffice.org/)和[OpenOffice Calc](http://www.openoffice.org/)也可以处理Excel文档  
openpyxl模板可以处理这些Excel电子表格  
读取当前目录下的电子表格：  

```python
>>> import sys, os
>>> currentPath = os.path.dirname(sys.argv[0])
>>> excelPath = os.path.join(currentPath, "example.xlsx")
```

## 12.2 安装openpyxl模块

[OpenPyXL](http://openpyxl.readthedocs.org/)完整文档  
安装命令：  
> pip install openpyxl  

导入该模块：

```python
>>> from openpyxl import load_workbook
>>> from openpyxl import Workbook as Wb
```

## 12.3 读取Excel文档

准备电子表格example.xslx，放入指定文件夹  
鉴于新版本的openpyxl模块API有所更新，书中代码示例已不适用，请参考示例代码#12_3_loadWorkbook.py  

### 12.3.1 用openpyxl模块打开Excel文档

### 12.3.2 从工作簿中取得工作表

### 12.3.3 从表中取得单元格

### 12.3.4 列字母和数字之间的转换

openpyxl.cell.column_index_from_string('M')
openpyxl.cell.get_column_letter(14)

### 12.3.5 从表中取得行和列

cell.row，cell.column  

### 12.3.6 工作簿、工作表、单元格

## 12.4 项目：从电子表格中读取数据

程序期望：  

- 从Excel电子表格中读取数据  
- 计算每个县中普查区的数目  
- 计算每个县的总人口  
- 打印结果  

代码任务：  

- 用openpyxl模块打开Excel文档并读取单元格  
- 计算所有普查区和人口数据，将它保存到一个数据结构中  
- 利用pprint模块，将数据结构写入一个扩展名为.py的文本文件  

### 第1步：读取电子表格数据

### 第2步：填充数据结构

### 第3步：将结果写入文件

### 第4步：类似程序的思想

- 比较一个电子表格中多行的数据  
- 打开多个Excel文件，跨电子表格比较数据  
- 检查电子表格是否有空行或无效数据，如果有就警告  
- 从电子表格中读取数据，将它作为Python程序的输入  

## 12.5 写入Excel文档

### 12.5.1 创建并保存Excel文档

workbook的save()方法，传入一个文件路径，就可以保存到相应路径下  

### 12.5.2 创建和删除工作表

wb.create_sheet()，wb.create_sheet(index=2, title='Middle Sheet')，  
wb.remove(wb['Sheet'])

### 12.5.3 将值写入单元格

activeSheet.cell(1, 1, 'Hello world!')
wb.save(excelPath)
注意，在写入完成后，一定要调用save()方法，这样数据才会保存到物理文件  

## 12.6 项目：更新一个电子表格

程序期望：  

- 循环遍历所有行  
- 如果该行是Garlic、Celery或Lemons，更新价格  

代码任务：  

- 打开电子表格  
- 针对每一行，检查列A的值是不是Garlic、Celery或Lemons  
- 如果是，更新列B中的价格  
- 将该电子表格保存为一个新文件(这样就不会丢失原来的电子表格)  

### 第1步：利用更新信息建立数据结构

将更新的数据存在一个字典数据类型的变量中  

### 第2步：检查所有行，更新不正确的价格

更新价格后，调用save(newfilepath)，保存为一个新的文件  

### 第3步：类似程序的思想

- 从一个电子表格读取数据，写入另一个电子表格的某些部分  
- 从网站、文本文件或剪贴板读取数据，将它写入电子表格  
- 自动清理电子表格中的数据。例如，通过正则表达式，将各种格式的电话号码，更新为统一的标准格式  

## 12.7 设置单元格的字体风格

导入openpyxl模块的Font()和Style()函数  
参考示例脚本#12_7_styled.py  

## 12.8 Font对象

参考示例脚本#12_8_styles.py  

|关键字参数|数据类型|描述|
|:---|:---|:---|
|name|字符串|字体名称|
|size|整型|大小点数|
|bold|布尔型|True表示粗体|
|italic|布尔型|True表示斜体|

## 12.9 公式

openpyxl模块的load_workbook()函数的参数data_only=True，会读取单元格上设置的公式生成的结果，而不是公示本身  
参考示例脚本#12_9_formula.py  
<b style="color:red;">此实例有一个bug，想要输出公示的结果时，却得到了None？</b>  
首先，在执行相应的data_only=True代码前(设置断点)，先手动打开电子表格并保存、关闭。
然后，再继续运行断点处代码，将会得到公式计算出的结果  
如果是读取一个已经存在的电子表格，且设置data_only=True之前，没有被程序打开过，则不会有此bug  

## 12.10 调整行和列

### 12.10.1 设置行高和列宽

```python
activeSheet.row_dimensions[1].height = 70
activeSheet.column_dimensions['B'].width = 20
```

行高可以设置为0~499之间的整数或浮点值，表示高度的点数  
一个点数等于1/72英寸。默认行高为12.75  
列宽为0~255之间的整数或浮点数，表示使用默认字体大小(11点)时，单元格可显示的字符  
默认列宽8.43个字符  
列宽或行高为0时，将隐藏单元格  
参考示例脚本#12_10_1_dimension.py  

### 12.10.2 合并和拆分单元格

合并：merge_cells('C5:D5')  
拆分：unmerge_cells('A1:D3')  
参考示例脚本#12_10_2_merged.py  

### 12.10.3 冻结窗格

WorkSheet对象的freeze_panes属性，可以设置为一个Cell对象或一个单元格坐标的字符串。  
它会冻结指定单元格上边的所有行，和左边的所有列，但自己所在行和列不会冻结  
freeze_panes设置为'None'或'A1'，会解冻所有单元格  

|freeze_panes设置|冻结的行和列|
|:---|:---|
|sheet.freeze_panes = 'A2'|行1|
|sheet.freeze_panes = 'B1'|列A|
|sheet.freeze_panes = 'C1'|列A和列B|
|sheet.freeze_panes = 'C2'|行1和列A和列B|
|sheet.freeze_panes = 'None' 或 sheet.freeze_panes = 'A1'|未冻结窗格|

参考示例代码#12_10_3_freeze.py  

### 12.10.4 图表

openpyxl模块可以利用电子表格中的数据，创建条形图、折线图、柱状图和饼图  
创建图表的步骤：  

- 从一个矩形区域选择的单元格，创建一个Reference对象  
- 通过传入Reference对象，创建一个Series对象  
- 创建一个Chart对象  
- 将Series对象添加到Chart对象  
- 可选地设置Chart对象的drawing.top、drawing.left、drawing.width和drawing.height  
- 将Chart对象添加到Worksheet对象  

Reference对象通过调用openpyxl.charts.Reference()函数并传入3个参数创建的：  

- 包含图表数据的Worksheet对象  
- 两个整数元组，代表矩形选择区域的左上角单元格，该区域包含图表数据：  
  元组中第一个整数是行，第二个整数是列。第一行是1，不是0  
- 两个整数元组，代表矩形选择区域的右下角单元格，该区域包含图表数据：  
  元组中第一个整数是行，第二个整数是列。第一行是1，不是0  

openpyxl.charts.BarChart()条形图  
openpyxl.charts.LineChart()折线图  
openpyxl.charts.ScatterChart()散点图  
openpyxl.charts.PieChart()饼图  

openpyxl的2.1.4版本中，load_workbook()不会加载Excel文件中的图表(即使文件包含图表)  
如果加载一个Workbook对象，然后马上保存到同一个.xlsx文件名中，实际上就会删除其中的图表  

最新的openpyxl版本改动比较大，绘制图表的方式有了很大变化，而且文件中已经存在的图表，也可以读取了  
参考示例脚本#12_10_4_chart.py  

## 12.11 小结

openpyxl模块支持创建.xlsx文档，读写Excel文档，甚至将其他格式的文件(文本文件或PDF)转换为电子表格  

## 12.12 习题

## 12.13 实践项目

### 12.13.1 乘法表

通过命令行输入一个正整数参数，然后在电子表格中创建一个N*N的乘法表  
行1和列A应该用作标签，使用粗体  
参考示例脚本#12_13_1_multiplicationTable.py  

### 12.13.2 空行插入程序

思路：  
1 如果使用最新版本的openpyxl模块，可以新的便捷方法实现(Worksheet.insert_rows(), Worksheet.insert_cols(), Worksheet.delete_rows(), Worksheet.delete_cols())，这些新的方法会同时操作单元格上的样式和数据格式  
2 读入电子表格内容，然后写入新表格时，利用for循环拷贝前n行，对于剩下的行，行号加上M，写入新的电子表格  
  此种方式，会丢失单元格的样式和数据格式等  
参考示例脚本#12_13_2_blankRowInsert.py  
> cd .\Part_2\ch12_excel  
> py 12_13_2_blankRowInsert.py 3 2 myProduce.xlsx  

前两个参数是整数。第一个整数表示从第3行开始插入空行，第二个参数表示插入2行空行  
第三个参数是生成新的电子表格的文件名  

### 12.13.3 电子表格单元格反转程序

翻转电子表格中行和列的单元格。可以新建一个Worksheet，将翻转的单元格写入新建的Worksheet中  
通过嵌套for循环，将表格数据读入一个列表的列表。这个数据结构用sheetData[x][y]表示列x和行y处的单元格。然后，写入新单元格时，将sheetData[y][x]写入列x和行y处的单元格  
参考示例脚本#12_13_3_reverseRowColData.py  

### 12.13.4 文本文件到电子表格

读取已有的几个文本文件的内容，然后写入电子表格  
第一个文本文件的内容写入列A的单元格，第一行写入A1单元格，第2行写入A2单元格...  
第二个文本文件的内容写入列B的单元格，第一行写入B1单元格，第2行写入B2单元格...  
利用File对象的readlines获得一个字符串列表，每个字符串对应文件中的一行。  
参考示例脚本#12_13_4_txtToExcel.py  

### 12.13.5 电子表格到文件

将### 12.13.4得到的电子表格文件里的数据，反向生成类似之前的文本文件，并将数据写入  
列A的单元格数据写入第一个文件，A1写入第一行，A2写入第二行...  
列B的单元格数据写入第二个文件，B1写入第一行，B2写入第二行...  
参考示例脚本#12_13_5_excelToTxt.py  
