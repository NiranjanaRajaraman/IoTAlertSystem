import json
import urllib.request
import time

mytoken = 'your token here'
chatid = 640595928

botresponse=urllib.request.urlopen('https://api.telegram.org/bot'+mytoken+'/getUpdates?offset=-1')
botanswer = json.loads(botresponse.read())

oldinmessage=botanswer
# 
# 
# outmessage="Hello it is a message"
# botresponse=urllib.request.urlopen('https://api.telegram.org/bot'+mytoken+'/sendMessage?chat_id='+str(chatid)+'&text='+urllib.parse.quote(outmessage))


#-------------------------- Here some fancy things happen--------------------------------
outmessage="please answer within 5 seconds"
botresponse=urllib.request.urlopen('https://api.telegram.org/bot'+mytoken+'/sendMessage?chat_id='+str(chatid)+'&text='+urllib.parse.quote(outmessage))

time.sleep(5)

outmessage="5 seconds are over"
botresponse=urllib.request.urlopen('https://api.telegram.org/bot'+mytoken+'/sendMessage?chat_id='+str(chatid)+'&text='+urllib.parse.quote(outmessage))


botresponse=urllib.request.urlopen('https://api.telegram.org/bot'+mytoken+'/getUpdates?offset=-1')
botanswer = json.loads(botresponse.read())

actid = botanswer['result'][0]['message']['message_id']
oldid = oldinmessage['result'][0]['message']['message_id']

if actid-oldid>0:
    outmessage="well done"
    botresponse=urllib.request.urlopen('https://api.telegram.org/bot'+mytoken+'/sendMessage?chat_id='+str(chatid)+'&text='+urllib.parse.quote(outmessage))
else:
    outmessage="too late"
    botresponse=urllib.request.urlopen('https://api.telegram.org/bot'+mytoken+'/sendMessage?chat_id='+str(chatid)+'&text='+urllib.parse.quote(outmessage))
