import socket
import threading
def meth(s):
    while True:
        data = s.recv(1024)
        data = data.decode()
        print(data)
def main():
    host = '127.0.0.1'
    port = 5000
    rollnumber = input("enter your rollnumber : ")
    socketobj = socket.socket()
    socketobj.connect((host, port))
 # socketobj.send((str(rollnumber)+" had just joined").encode())
    thread = threading.Thread(target = meth, args = (socketobj, ))
    thread.start()

    while True:
        message = input()
        socketobj.send((rollnumber +" : "+message).encode())
    socketobj.close()

if __name__ == '__main__':
    main()