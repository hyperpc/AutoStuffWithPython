from operator import delitem
import imapclient
import pprint, imaplib

import pyzmail

# 16.4.1
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
print(imapObj)
# 16.4.2
loginfo = imapObj.login('email@ddr.com', 'password')
print(loginfo)
# 16.4.3
# 16.4.4
folders = imapObj.list_folders()
pprint.pprint(folders)
# 16.4.5
imapObj.select_folder('INBOX', readonly=True)
UIDs = imapObj.search(['SINCE 05-Jul-2015'])
print(UIDs)
# 16.4.6
#imaplib._MAXLINE=10000000
# 16.4.7
rawMsgs = imapObj.fetch(UIDs, ['BODY[]'])
pprint.pprint(rawMsgs)

# 16.4.8
message = pyzmail.PyzMessage.factory(rawMsgs[40041]['BODY[]'])
subject = message.get_subject()
print(subject)
from_addr = message.get_addresses('from')
print(from_addr)
to_addr = message.get_addresses('to')
print(to_addr)
cc_addr = message.get_addresses('cc')
print(cc_addr)
bcc_addr = message.get_addresses('bcc')
print(bcc_addr)
# 16.4.9
print(message.text_part != None)
text = message.text_part.get_payload().decode(message.text_part.charset)
print(text)
print(message.html_part != None)
html = message.html_part.get_payload().decode(message.html_part.charset)
# 16.4.10
delInfo = imapObj.delete_messages(UIDs)
print(delInfo)
imapObj.expunge() # 真正从服务器永久删除邮件
# 16.4.11
imapObj.logout()