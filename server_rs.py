import socket
i=""
ser=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ser.bind(('localhost',9596))
ser.listen(5)
cli,add=ser.accept()
cli_message="summa"
while cli_message != 'bye':
    cli_message=cli.recv(4096).decode()
    print(cli_message)
    i=input("enter the message:")+'/'+input("enter the command:")
    cli.send(i.encode())
    print(cli.recv(4096).decode())
i="have a great day"
cli.send(i.encode())
ser.close()
