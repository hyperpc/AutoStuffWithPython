#! python
from twilio.rest import Client

twSID = 'AC98f32.....3454238b2'
twAuth = '08795e8.....243523a4c1'
myTwNum = '+1 7.. ... ...5'
myhpNum = '+861.........0'

def textMyself(msg):
    twCli = Client(twSID, twAuth)
    twCli.messages.create(body=msg, from_=myTwNum, to=myhpNum)

textMyself('The boring task i finished.')