import hashlib
import requests
from lxml import html
import webbrowser

cookie = {"PHPSESSID" : "id"}

page = requests.get("http://challenges.ringzer0team.com:10056", cookies=cookie)
tree = html.fromstring(page.content)
message = tree.xpath('/html/body/main/div/text()')[1].strip()

for i in range(10000):
    if hashlib.sha1(str(i).encode()).hexdigest() == message:
        answer = str(i)
print(answer)
answerUrl = 'http://challenges.ringzer0team.com:10056/?r=' + answer
webbrowser.open(answerUrl)
