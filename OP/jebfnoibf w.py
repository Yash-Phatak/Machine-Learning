import socket

s=socket.socket()
ip='127.0.0.1'
port=1222
s.connect((ip, port))
while True:
    try:
        msg=s.recv(1024)
        if msg:
            print("\n recv: ", msg.decode())
    except:
        continue
    msg1=input("Send:")
    s.send(msg1.encode())