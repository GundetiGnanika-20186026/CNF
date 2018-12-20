import socket
def main():
    host  = '127.0.0.1'
    port = 5000
    s = socket.socket()
    s.connect((host,port))
    initial = s.recv(1024)
    print('received from server : '+ initial.decode())
    message = input("Enter your guess : ")
    while message != 'q':
        s.send(message.encode())
        data = s.recv(1024)
        print('received from server : ' + data.decode())
        if(data.decode() == 'correct!'):
            print("Done with Game!!!!!!")
            print("connection will be closed")
            s.close()
            break
        message = input("client1 Enter your guess : ")
    s.close()

if __name__ == "__main__":
    main()
# import socket

# def main():
#     host = '127.0.0.1'
#     port = 5000

#     s = socket.socket()
#     s.connect((host,port))

#     message = input("Guess the number : ")
#     while message != 'q':
#         s.send(message.encode())
#         data = s.recv(1024)
#         print("Received from Server: " + str(data.decode()))
#         check = str(data.decode()).split(" ")
#         if(check[0] == "correct,"):
#             print("Game Done! Connection Close")
#             s.close()
#             return
#         message = input("-->")
#     s.close()

# if __name__ == "__main__":
#     main()