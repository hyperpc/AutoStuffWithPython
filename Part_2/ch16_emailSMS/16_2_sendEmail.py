import smtplib

# TLS加密
smtpObj = smtplib.SMTP('smtp.126.com', 25)
# SSL加密
#smtpObj = smtplib.SMTP_SSL('smtp.126.com', 25)

print(smtpObj.ehlo)

# 如果使用SSl加密，需要跳过这一步
# 因为该SSL加密已经设置好了
#tls = smtpObj.starttls()
#print(tls)

loginfo = smtpObj.login('wwwww@126.com', 'wwwww')
print(loginfo)

sending = smtpObj.sendmail('wwwww@126.com', ['wwwww@126.com'],'''Subject: Meeting minutes. 
YP, 
Plz share today's meeting minus to me, and I will one new copy of requirement to you before tomorrow 8:00AM
Thanks, YP''')
print(sending)

quit = smtpObj.quit()
print(quit)