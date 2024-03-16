#  I hate mathematics 

from lxml import html
import webbrowser
import requests
import hashlib
import codecs

cookie = {'PHPSESSID':'id'}

page = requests.get('http://challenges.ringzer0team.com:10032/', cookies=cookie)
tree = html.fromstring(page.content)

message = tree.xpath('/html/body/main/div/text()')[2].strip()

print('Message:', message)

lenm = len(message)
i = 0
n1 = 0
n2 = n3 = ''
for i in range(lenm):
    if message[i] in '0123456789':
        n1 = n1 * 10 + int(message[i])
    else: 
        last = i + 3
        break
for i in range(last, lenm):
    if message[i] in '0123456789xabcdef':
        n2 += message[i]
    else:
        n2 = int(n2, 16)
        last = i + 3
        break
for i in range(last, lenm):
    if message[i] in '01':
        n3 += message[i]
    else:
        n3 = int(n3, 2) 
        break
calcedMessage = n1 + n2 - n3

print(calcedMessage)

answerUrl = 'http://challenges.ringzer0team.com:10032/?r=' + str(calcedMessage)
webbrowser.open(answerUrl)
