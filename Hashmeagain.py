#  Hash me again 

from lxml import html
import webbrowser
import requests
import hashlib
import codecs

cookie = {'PHPSESSID':'id'}

page = requests.get('http://challenges.ringzer0team.com:10014/', cookies=cookie)
tree = html.fromstring(page.content)

message = tree.xpath('/html/body/main/div/text()')[1].strip()

print('Message: ', message)

line = message
message2 = []
line = [line[i:i+8] for i in range(0, len(line), 8)]
for i in range(len(line)):
    message2.append(int(line[i], 2))
message=''
for i in range(len(message2)):
    message += chr(message2[i])

lines = [message[i:i+8] for i in range(0, len(message), 8)]

output = str()

for line in lines:
    output += chr(int(line, 2))

message = output
print(message)

# message=message.encode('utf8')
hashedMessage = hashlib.sha512(message).hexdigest()

print('Hashed: ', hashedMessage)
answerUrl = 'http://challenges.ringzer0team.com:10014/?r=' + hashedMessage
print(answerUrl)
webbrowser.open(answerUrl)