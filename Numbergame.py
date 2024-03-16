#  Number game 

import paramiko 

host = 'challenges.ringzer0team.com'
user = 'number'
secret = 'Z7IwIMRC2dc764L'
port = 10130

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, password=secret, port=port)
ssh = client.invoke_shell()
s = ssh.recv(3000)
print(s)
s = ssh.recv(3000)
print(s)
numb = 5000
difference = [2200,600,170,50,15,4,1]
i = 0
fSmall = 0
fBig = 0
while(True):
    if b"win" in s:
        i=0
        numb = 5000
        print(s)
    q = ssh.send(f"{numb}\n")
    s = ssh.recv(1000)
    if b"small" in s:
        numb += difference[i]
        fSmall = 1
        if fSmall == 0:
            i+=1
        fBig = 0
    elif b"big" in s:
        numb = difference[i]
        fSmall = 0
        if fBig == 0:
            i+=1
        fBig = 1
    if b"10 on 10" in s:
        break
print(ssh.recv(1000))