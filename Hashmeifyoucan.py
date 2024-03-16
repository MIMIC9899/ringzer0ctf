# Hash me if you can 

from lxml import html
import webbrowser
import requests
import hashlib
import codecs

cookie = {'PHPSESSID':'id'}

page = requests.get('http://challenges.ringzer0team.com:10013/', cookies=cookie)
tree = html.fromstring(page.content)

message = tree.xpath('/html/body/main/div/text()')[1].strip()

print('Message:', message)

# message = message.encode('utf8')
hashedMessage = hashlib.sha512(message).hexdigest()

print('Hashed: ', hashedMessage)
answerUrl = 'http://challenges.ringzer0team.com:10013/?r=' + hashedMessage
webbrowser.open(answerUrl)