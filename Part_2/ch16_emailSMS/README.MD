# 第16章 发送电子邮件和短信

## 16.1 SMTP

Simple Mail Transfer Protocol  
简单邮件传输协议，负责向别人发送电子邮件  
Python的smtplib模块，将发送邮件的细节简化为几个函数  

## 16.2 发送电子邮件

参考示例脚本#16_2_sendEmail.py  

### 16.2.1 连接到SMTP服务器

常见电子邮件提供商及SMTP服务器
|服务商|SMTP服务器域名|端口|
|:---|:---|:---|
|Gmail|smtp.gmail.com|587|
|Outlook/Hotmail|smtp-mail.outlook.com|587|
|Yahoo|smtp.mail.yahoo.com|587|
|AT&T|smtp.mail.att.net|465|
|Comcast|smtp.comcast.net|587|
|Verizon|smtp.verizon.net|465|
|126|smtp.126.com|25|

国际上的SMTP服务器一般使用支持TLS加密标准的端口587，也有使用SSL加密标准的465端口的  
国内的一般使用25端口，如126，163等  

### 16.2.2 发送SMTP的'Hello'消息

得到SMTP对象后，第一步就是调用古怪的ehlo()方法，否则，后面的调用会失败  
在该调用的返回的元组中，有一个整数250，表示成功  

### 16.2.3 开始TLS加密

SMTP对象的starttls()方法，让连接处于TLS模式，返回220，说明服务器准备就绪  

### 16.2.4 登录到SMTP服务器

调用login()方法，传入邮箱的用户名和密码，即可登录  
返回值235，表示认证成功  

### 16.2.5 发送电子邮件

sendmail()方法需要三个参数：  

- from  
- to (收件人邮件字符串，或收件人邮件字符串列表)  
- 邮件正文  

返回值是一个字典。每个发送失败的收件人，字典就有一个对应的键值对。空字典意味着所有收件人都发送成功  

### 16.2.6 从SMTP服务器断开

quit()方法会断开SMTP服务器的连接  
返回值221表示会话结束  

## 16.3 IMAP

Python的imaplib模块可以从邮件服务器取回邮箱里的邮件  
建议使用更易用的第三方模块imapclient  
imapclient模块的[完整文档](https://imapclient.readthedocs.io/)  
模块pyzmail可以将格式复杂的email邮件内容解析成简单的字符串  
pyzmail模块的[完整文档](https://pyzmail.readthedocs.io/en/latest/)  
目前Python3.7以上的版本，已无法安装模块pyzmail

## 16.4 用IMAP获取和删除电子邮件

参考示例脚本#16_4_receiveEmail.py  

### 16.4.1 连接到IMAP服务器

常见电子邮件提供商及IMAP服务器
|服务商|SMTP服务器域名|
|:---|:---|
|Gmail|imap.gmail.com|
|Outlook/Hotmail|imap-mail.outlook.com|
|Yahoo|imap.mail.yahoo.com|
|AT&T|imap.mail.att.net|
|Comcast|imap.comcast.net|
|Verizon|incoming.verizon.net|
|126|imap.126.com|
大多数邮件服务提供商要求SSL加密  

### 16.4.2 登录到IMAP服务器

### 16.4.3 搜索电子邮件

imapObj.list_folders()列出邮件账号下的所有文件夹  
返回的列表的每一项是每一层文件夹的目录组成的元组，共分成三项：  
文件夹标志的元组，分隔符和文件夹名字  

### 16.4.4 选择文件夹

imapObj.select_folder('INBOX', readonly=True)总是将readonly设置为True，以防止误删邮件  

### 16.4.5 执行搜索

UIDs = imapObj.search(['SINCE 05-Jul-2015', 'BEFORE 01-Feb-2015', 'UNSEEN'])  
search()支持各种搜索键：  
ALL，  
BEFORE date, ON date, SINCE date,  
SUBJECT string, BODY string, TEXT string,  
FROM string, TO string, CC string, BCC string,  
SEEN, UNSEEN,  
ANSWERED, UNANSWERED,  
DELETED, UNDELETED,  
DRAFT, UNDRAFT,  
FLAGGED, UNFLAGGED,  
LARGER n, SMALLER n,  
NOT search-key, OR search-key1 search-key2  

### 16.4.6 大小限制

如果搜索到的匹配邮件太多，会导致Python异常，这是Python防止内存消耗过大的一种限制  
可以通过模块imaplib将限制调大：imaplib._MAXLINE=10000000

### 16.4.7 取邮件并标记为已读

如果需要将邮件设为已读，需要再调用一次select_folder()，并将readonly参数置为True  

### 16.4.8 从原始消息中获取电子邮件地址

这里就要开始使用pyzmail模块了  

### 16.4.9 从原始消息中获取正文

当邮件是纯文本内容，PyzMessage对象会将html_part属性设为None  
当邮件是HTMl内容，PyzMessage对象会将text_part属性设为None  

### 16.4.10 删除电子邮件

### 16.4.11 从IMAP服务器断开

## 16.5 项目：向会员发送会费提醒电子邮件

程序要求：  

- 从Excel电子表格中读取数据  
- 找出上月未交费用的所有会员  
- 找到他们的电子邮件，向他们发送针对个人的提醒  

代码实现：  

- 用openpyxl模块打开并读取Excel文档的单元格
- 创建一个字典，包含会费超期的会员
- 调用smtplib.SMTP()、ehlo()、starttls()和login()，登录SMTP服务器  
- 针对会员超期的所有会员，调用sendmail()方法，发送针对个人的电子邮件提醒  

参考示例脚本#16_5_sendDuesReminders.py  

### 第1步：打开Excel文件

### 第2步：查找所有未付成员

### 第3步：发送定制的电子邮件提醒

## 16.6 用Twilio发送短信

Twilio会提供有限的免费发送短信的服务，且没有使用期限  
Python的twilio模块可以连接这个服务  
注意，Twilio服务现在在中国是不能使用的

### 16.6.1 注册Twilio账号

从[Twilio](https://www.twilio.com/)注册一个账户，通过手机验证后，可以得到一个试用账户  
从dashboard页面得到账户SID和AUTH(认证)标志  

### 16.6.2 发送短信

参考示例代码#16_6_twilio.py  

## 16.7 项目："只给我发短信"模块

## 16.8 小结

## 16.9 习题

## 16.10 实践项目

### 16.10.1 随机分配家务活的电子邮件程序

部分实例代码：  

```python
import random
chores = ['dished', 'bathroom', 'vacuum', 'walk dog']
randomChore = random.choice(chores)
print(randomChore)
chores.remove(randomChore)
```

### 16.10.2 伞提醒程序

通过request模块从http://weather.gov 抓取数据。如果有雨，就短信通知出门前带伞

### 16.10.3 自动退订

编程扫描邮箱账户，找到所有退订链接，并自动在浏览器中打开  
程序登录邮箱的IMAP服务器，下载所有邮件。用BeautifulSoup模块找到unsubscribe的HTML链接标签  
得到的URL列表，通过webbrowser.open()打开。然后可以手动点击一个确认链接，以退订

### 16.10.4 通过电子邮件控制你的电脑

参考示例脚本#torrentStarter.py  
