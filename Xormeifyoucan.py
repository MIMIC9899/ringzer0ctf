import base64
import requests
from lxml import html
import webbrowser

cookie = {'PHPSESSID':'id'}

page = requests.get('http://challenges.ringzer0team.com:10016/', cookies=cookie)
tree = html.fromstring(page.content)

xor = tree.xpath('/html/body/main/div/text()')[1].strip()
message = tree.xpath('/html/body/main/div/text()')[5].strip()
message = base64.b64decode(message)
for i in range(len(xor) - 10):
    key = xor[i:i+10].encode()
    res = []
    
    for index, char in enumerate(message):
        #print(char)
        res.append(chr(char ^ key[index % 10]))
    
    res = ''.join(res)
    if res.isalnum():
        print(res)
        break

answer = res
answerUrl = 'http://challenges.ringzer0team.com:10016/?r=' + answer
webbrowser.open(answerUrl)
