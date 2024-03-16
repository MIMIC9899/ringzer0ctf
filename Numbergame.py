import paramiko 
import time

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
low = 0
high = 10000
while (True):
    if b'win' in s:
        low = 0
        high = 10000
        print(s)
    numb = (low + high)//2
    q = ssh.send(str(numb) + "\n")
    time.sleep(0.2)
    s = ssh.recv(1000)
    #print(low, high, s)
    if b"small" in s:
        low = numb
    if b"big" in s:
        high = numb
