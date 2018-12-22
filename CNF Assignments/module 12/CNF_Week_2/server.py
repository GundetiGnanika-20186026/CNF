import socket
import threading
clients = list()
eachline = dict()
# # total1 = 0

def method(client,):
    # global total1
    while True:
        data = client.recv(1024).decode()
        string1 = data.split(" ")
        secret = 'SECRETQUESTION-'
        notpresent = 'ROLLNUMBER-NOTFOUND'
        present = 'ATTENDANCE SUCCESS '
        notcorrect = 'ATTENDANCE FAILUE'

        if not data:
            break;

        for cl1 in clients:

            if (string1[0] not in eachline):
                cl1.send(str(notpresent).encode())

            else :
                # token = dictionary[cl1].split('?')
                if (string1[2] == 'MARK-ATTENDANCE') :
                    token =eachline[string1[0]]
                # print(token[0])
                    cl1.send(str(secret+token[0]).encode())
                else:
                    token = eachline[string1[0]]
                    # if (string1[2] == token[1].substring(0,len(token[1]-2))):
                    #        cl1.send(str(present).encode())
                    if(token[1].find(string1[2])):
                          cl1.send(str(present).encode())
                    else :
                        cl1.send(str(notcorrect+" "+secret+token[0]).encode())


              #  total1 = total1 + int(string1[2])
              # for cl in clients:

              #     cl.send(str(string1).encode())




def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''




    with open(filename, 'r') as givenfile:
        for line in givenfile:
              # print(line)
              # new = list()
              new = (line.split(",",1))
              eachline[new[0]] = new[1].split('?')




def main():
    extra = load_stopwords("data.Csv")
    # print(eachline)
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

