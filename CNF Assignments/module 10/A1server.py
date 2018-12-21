import socket
import threading
clients = list()

def method(client):
    while True:
        data = client.recv(1024).decode()
        if not data:
            break;
        for cl in clients:
            if cl != client:
                cl.send(str(data).encode())


def main():
    num = int(input('please enter the number of clients : '))
    host = '127.0.0.1'
    port = 5000
    socketobj = socket.socket()
    socketobj.bind((host, port))
    socketobj.listen(num)
    for i in range(0,num):
           client, addr = socketobj.accept()
           print('connection established with : '+str(addr))
           clients.append(client)
           thread= threading.Thread(target=method, args=(clients[i],))
           thread.start()
    socketobj.close()

if __name__ == '__main__':
    main()

