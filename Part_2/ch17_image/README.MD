# 第17章 操作图像

Pillow是一个第三方Python模块，它包含的一些函数，可以容易地裁剪图像，调整图像大小，以及编辑图像的内容  
[完整文档](https://pillow.readthedocs.io/en/stable/)  

## 17.1 计算机图像基础

参考示例脚本#17_1_rgba.py  

### 17.1.1 颜色和RGBA值

Pillow中，RGBA值表示为四个整数值的元组，使用了HTML的标准颜色名称和值  
红色：(255, 0, 0, 255)  
绿色：(0, 255, 0, 255)  
蓝色：(0, 0, 255, 255)  
红色：(255, 0, 0, 255)  
白色：(255, 255, 255, 255)  
黑色：：(0, 0, 0, 255)  
以上颜色的alpha值为255，即不透明；如果为0，则为全透明，那么前面的rgb色值就失去了意义，无法表现出来  

### 17.1.2 坐标和Box元组

图像的坐标：
原点在左上角，坐标为(0,0)。
第一个0为x轴的原点，从左向右增加；第二个0为y轴的原点，从上到下增加  

> 减色模型：混合红、黄、蓝三种颜色，可以得到其他颜色  
> 适用于染料，油墨和颜料。如CYMK墨盒:青色(蓝色)，品红色(红色)，黄色和黑色墨水  
> 加色模型：利用光的物理现象，组合红、绿和蓝色可组合形成其他颜色。如RGB：红，绿和蓝  

矩形元组，表示一个矩形区域的颜色块。  
如(3,1,9,6)，表示包括左上顶点为(3,1)，直到但不包括右下坐标(9,6)的矩形区域  

## 17.2 用Pillow操作图像

参考示例脚本#17_2_pillowImg.py  

### 17.2.1 处理Image数据类型

### 17.2.2 裁剪图片

crop()

### 17.2.3 复制和粘贴图像到其他图像

copy(), paste()  

### 17.2.4 调整图像大小

resize(int, int)  

### 17.2.5 旋转和反转图像

rotate(deg), rotate(deg, expand=True)  

### 17.2.6 更改单个像素

getpixel(), putpixel(), ImageColor.getColor()  

## 17.3 项目：添加徽标

程序要求：  

- 载入徽标图像  
- 循环遍历工作目标中的所有.png和.jpg文件  
- 检查图片是否宽于或高于300像素  
- 如果是，将宽、高中较大的一个减小300像素，并按比例缩小另一维度  
- 在角上粘贴徽标图像
- 将改变的图像存入另一个文件夹  

代码实现：  

- 打开catlogo.png文件作为Image对象  
- 循环遍历os.listdir('.')返回的字符串  
- 通过size属性取得图像的宽度和高度  
- 计算调整后的图像的新高度和宽度  
- 通过resize()方法调整图像大小  
- 通过paste()方法来粘贴徽标  
- 调用save()方法保存更改，使用原来的文件名

参考示例脚本#17_3_resizeAndAddLogo.py  

### 第1步：打开徽标图像

如果不想要丢失png图像的透明属性，需要按照以下方式打开图片：  
> logoImg = Image.open(os.path.join(imgPath, LOGO_FILENAME)).convert('RGBA')

### 第2步：遍历所有文件并打开图像

### 第3步：调整图像大小

### 第4步：添加徽标，并保存更改

### 第5步：类似程序的想法

- 为图像添加文字或网站URL  
- 为图像添加时间戳  
- 根据图像大小，将图像复制或移动到不同的文件夹中  
- 为图像添加一个几乎透明的水印，防止他人复制  

## 17.4 在图像上绘画

Pillow的ImageDraw模块  

### 17.4.1 绘制形状

|形状|方法|参数说明|
|:---|:---|:---|
|点|point(xy, fill)|xy是要画的点的列表，格式为[(x1,y1),(x2,y2)...]或[x1,y1,x2,y2...]；fill是点的颜色，可选，可以是一个RGBA元组，或颜色名称|
|线|line(xy, fill, width)|xy是要画的线上的点的列表，格式为[(x1,y1),(x2,y2)...]或[x1,y1,x2,y2...]；fill是线的颜色，可选，可以是一个RGBA元组，或颜色名称；width是线的宽度，可选，默认值为1|
|矩形|rectangle(xy, fill, outline)|xy是矩形元组(left,top,right,bottom)，分别代表矩形左上角和右下角的坐标；fill是填充矩形的颜色；outline是矩形轮廓颜色。如果矩形的宽高一样，则是正方形|
|椭圆|ellipse(xy, fill, outline)|xy是矩形元组(left,top,right,bottom)，分别代表刚好包含椭圆的矩形左上角和右下角的坐标；fill是填充椭圆的颜色；outline是椭圆轮廓颜色。如果椭圆的宽高一样，则是圆形|
|多边形|polygon(xy, fill, outline)|xy是各条边的连接点坐标，一个元组[(x1,y1),(x2,y2)...]或[x1,y1,x2,y2...]，最后一对坐标自动连接回第一对坐标；fill是填充多边形内部的颜色；outline是多边形轮廓颜色|

参数fill和outline是可选的，如果未指定，默认为白色  
参考示例脚本#17_4_1_draw.py  

### 17.4.2 绘制文本

|形状|方法|参数说明|
|:---|:---|:---|
|文本|text(xy, text, fill, font)|xy是两个整数的元组，是文本区域左上角坐标；text是想写入的文本字符串；fill是文本的颜色，可选；font是ImageFont对象，可选，用于设置文本字体和大小|
|文本|textsize(text,font)|text是想写入的文本字符串；font是ImageFont对象；返回两个整数的元组，表示文本区域的宽高，以用来计算文本在图像的合适位置|

参考示例脚本#17_4_2_font.py  

## 17.5 小结

Pillow模块：  
Image模块：crop()、copy()、paste()、resize()、rotate()和transpose()，save()  
ImageDraw模块：point()、line()、rectangle()、ellipse()和polygon()；text()和textsize()  
ImageFont对象

## 17.6 习题

## 17.7 实践项目

### 17.7.1 扩展和修正本章项目的程序

扩展示例脚本#17_3_resizeAndAddLogo.py，也支持处理GIF和BMP；并且文件扩展名不区分大小写。  
并且检查图像大小，必须是徽标高度和宽度的两倍，才允许粘贴徽标  

### 17.7.2 在硬盘上识别照片文件夹

首先，文件夹内文件扩展名为.png和.jpg；高度和宽度必须大于500像素  
程序代码框架：  

```python
#! python3

for foldername, subfolders, filenames in os.walk('C:\\'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        # check if file extension isnt .png or .jpg
        if TODO:
            numNonPhotoFiles += 1
            continue   # skip to next filename
        # open image file using pillow

        # check if width & height are larger than 500
        if TODO:
            # image is large enough to be considered a photo
            numPhotoFiles += 1
        else:
            # image is too small to be a photo
            numNonPhotoFiles += 1
        # if more than half of files were photos,
        # print the absolute path of the folder
        if TODO:
            print(TODO)
```

程序运行时，打印出照片文件夹的绝对路径

### 17.7.3 定制的座位卡

客户名单guests.txt，为每个客人生成带有客人名字和鲜花装饰的图像文件。  
生成的png文件每英寸72像素，4x5英寸的卡片需要288x360像素的图像  
在图像边缘添加一个黑色矩形，以方便沿线裁剪。  
