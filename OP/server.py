import socket

def server_prog():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host,port))
    server_socket.listen(2)
    connection,address = server_socket.accept()
    print("Connection from: "+ str(address))
    while True:
        data = connection.recv(1024).decode()
        if not data:
            break
        print("From Connected User: "+str(data))
        data = "Message Recieved.."
        connection.send(data.encode())
    connection.close()

if __name__=='__main__':
    server_prog()
