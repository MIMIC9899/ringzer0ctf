#  Ascii art 

from lxml import html
import webbrowser
import requests
import hashlib
import codecs

cookie = {'PHPSESSID':'id'}

page = requests.get('http://challenges.ringzer0team.com:10119/', cookies=cookie)
tree = html.fromstring(page.content)

message = tree.xpath('/html/body/main/div/text()')[2:2]

decodedMessage = ''
i = 0
while i<len(message):
    print(message[i])
    i+=1
i = 0
while i<len(message)1:
    if message[i]=='\xa0xx\xa0\xa0':
        decodedMessage += '1'
        if i+4<len(message):
            i+=4
        else: break
    elif message[i]=='\xa0xxx\xa0':
        if message[i+4]=='xxxxx':
            decodedMessage += '2'
        elif message[i+2]=='\xa0\xa0xx\xa0':
            decodedMessage += '3'
        else: decodedMessage += '0'
        if i+4<len(message):
            i+=4
        else: break
    elif message[i]=='xxxxx':
        decodedMessage += '5'
        if i+4<len(message):
            i+=4
        else: break
    elif message[i]=='\xa0x\xa0\xa0\xa0x':
        decodedMessage += '4'
        if i+4<len(message):
            i+=4
        else: break
    i+=1

print('Message:', message)
print(decodedMessage)

answerUrl = 'http://challenges.ringzer0team.com:10119/?r=' + decodedMessage
webbrowser.open(answerUrl)