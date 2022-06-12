from socket import *

import sqlite3

# def loginCheck(self):
#     conn = sqlite3.connect(r'.\atm.db')
#     cursor = conn.cursor()
#     sql = "select * from user where id={} and password={}".format(self.name, self.passw)
#     cursor.execute(sql)
#     row = cursor.fetchone()
#     conn.commit()
#     # print(sql)
#     # uname=self.name
#     with open(r'.\ATM.txt', 'w') as f:
#         f.write(self.name)


serverPort=12000
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
while True:
    connectionSocket,addr=serverSocket.accept()
    sentence=connectionSocket.recv(1024).decode()
    # capitalizedSentence=sentence.upper()
    myresult = sentence.split(',')
    if myresult[0]=='zhuce':
        conn = sqlite3.connect(r'.\atm.db')
        cursor = conn.cursor()
        sql = "select * from user where id={} and password={}".format(myresult[1], myresult[2])
        cursor.execute(sql)
        row = cursor.fetchone()
        conn.commit()
        # print(sql)
        # uname=self.name
        with open(r'.\ATM.txt', 'w') as f:
            f.write(myresult[1])

        if row != None:
            myresult[0]="chenggong"
        else:
            myresult[0]="shibai"
        # login(myresult[1],myresult[2],myresult[3],myresult[4])
    elif myresult[0]=='cunqian':
        for i in myresult:
           print(i)
        with open(r'.\ATM.txt', 'r') as f:
            for s in f.readlines():
                # print(s)
                username = s

        conn = sqlite3.connect(r'.\atm.db')
        cursor = conn.cursor()

        sql = "select cash from money where id={}".format(username)
        cursor.execute(sql)
        cash = cursor.fetchone()
        conn.commit()
        myresult[0] = str(cash[0])
        print(myresult[0])
        m=int(myresult[1])+int(myresult[0])
        a = ("update money set cash={} where id={}".format(m, username))
        cursor.execute(a)
        conn.commit()
        # save(myresult[1],myresult[2])
    elif myresult[0]=='quqian':
        with open(r'.\ATM.txt', 'r') as f:
            for s in f.readlines():
                # print(s)
                username = s
        conn = sqlite3.connect(r'.\atm.db')
        cursor = conn.cursor()
        sql = "select cash from money where id={}".format(username)
        cursor.execute(sql)
        cash = cursor.fetchone()
        conn.commit()
        myresult[0] = str(cash[0])
        m = int(myresult[0]) - int(myresult[1])
        if m > 0:
            a = ("update money set cash={} where id={}".format(m, username))
            cursor.execute(a)
            conn.commit()
            myresult[0] = "chenggong"
        else:
            myresult[0] = "shibai"

        # getmoney(myresult[1],myresult[2])
    elif myresult[0]=='zhuanzhang':
        with open(r'.\ATM.txt', 'r') as f:
            for s in f.readlines():
                # print(s)
                username = s
        conn = sqlite3.connect(r'.\atm.db')
        cursor = conn.cursor()

        sql = "select cash from money where id={}".format(username)
        cursor.execute(sql)
        cash = cursor.fetchone()
        conn.commit()
        m = cash[0] - int(myresult[1])
        if m > 0:
            a = ("update money set cash={} where id={}".format(m, username))
            cursor.execute(a)
            conn.commit()
        else:
            myresult[0]="shibai"
        if m > 0:
            sql = "select cash from money where id={}".format(myresult[2])
            cursor.execute(sql)
            cash = cursor.fetchone()
            conn.commit()

            m = cash[0] + int(myresult[1])

            a = ("update money set cash={} where id={}".format(m, myresult[2]))
            cursor.execute(a)
            conn.commit()
            myresult[0] = "chenggong"
    elif myresult[0]=='chaxun':

        with open(r'.\ATM.txt', 'r') as f:
            for s in f.readlines():
                print(s)
                username = s

        conn = sqlite3.connect(r'.\atm.db')
        cursor = conn.cursor()

        sql = "select cash from money where id={}".format(username)
        cursor.execute(sql)
        cash = cursor.fetchone()
        conn.commit()

        myresult[0] =str(cash[0])
        print(myresult[0])
        # inquire(myresult[1])
    else:
        print("错误操作")
        myresult[0] = "caozuoshibai"
    # connectionSocket.send(capitalizedSentence.encode())

    connectionSocket.send(myresult[0].encode())
    connectionSocket.close()