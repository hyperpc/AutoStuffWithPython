from twilio.rest import Client as twClient

twSID = 'AC98f32.....3454238b2'
twAuth = '08795e8.....243523a4c1'
myTwNum = '+1 7.. ... ...5'
myhpNum = '+861.........0'
twCli = twClient(twSID, twAuth)
message = twCli.messages.create(messaging_service_sid='MG01e74123.....34gd9f7fcf1', body='Mr. Hou - Come here - I want to see you.', from_=myTwNum, to=myhpNum)
print(message.to)
print(message.from_)
print(message.body)
print(message.status)
print(message.date_created)
print(message.date_sent == None)
print(message.sid)
updateMsg = twCli.messages.get(message.sid)
#print(updateMsg.status)
#print(updateMsg.date_status)
