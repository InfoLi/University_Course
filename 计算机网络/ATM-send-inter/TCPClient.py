# from socket import *
# serverName="10.234.109.70"
# serverPort=12000
# clientSocket=socket(AF_INET,SOCK_STREAM)
# clientSocket.connect((serverName,serverPort))
# # print("zhuce,1001,123456,'李四',2000")
# # print("cunqian,1001,200")
# # print("quqian,1001,200")
# # print("chaxun,1001")
# sentence=input("Input lowercase sentence:")
# clientSocket.send(sentence.encode())
# modifiedSentence=clientSocket.recv(1024)
# print("From Server: ",modifiedSentence.decode())
# clientSocket.close()

from socket import *


def myTCP(a=[]):
    #serverName = "10.234.109.70"
    serverName = "127.0.0.1"
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    # print("zhuce,1001,123456,'李四',2000")
    # print("cunqian,1001,200")
    # print("quqian,1001,200")
    # print("chaxun,1001")
    # 发送信息

    # sentence=input("Input lowercase sentence:")
    sentence = ','.join(a)
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    # 接受到的信息
    # print("From Server: ", modifiedSentence.decode())
    clientSocket.close()
    return modifiedSentence.decode()