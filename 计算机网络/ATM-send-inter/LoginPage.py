# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 19:53:50 2017
@author: Administrator
"""
import tkinter as tk
import tkinter.messagebox as me
import MainPage
import sqlite3
import TCPClient as tcp
        
class LoginPage(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.root = master
        self.pack()
        self.root.title("登录页面")
        self.root.geometry('650x500')
        self.username=tk.StringVar(self.root)
        self.password=tk.StringVar(self.root)
        self.create_widgets()
        
    def create_widgets(self):  
        self.page=tk.Frame(self)
        self.page.pack()
        
        self.p1=tk.PanedWindow(self.page)
        self.p2=tk.PanedWindow(self.page)
        self.p3=tk.PanedWindow(self.page)
    
        self.p1.pack()
        self.p2.pack() 
        self.p3.pack()
        
        
        self.label_1=tk.Label(self.p1,text="用户名: ")
        self.entry_1=tk.Entry(self.p1,textvariable=self.username)
        
        self.label_2=tk.Label(self.p2,text="密码:    ")
        self.entry_2=tk.Entry(self.p2,textvariable=self.password,show="*")
    
        
        self.btn1 = tk.Button(self.p3,width=5)
        self.btn2 = tk.Button(self.p3,width=5)
        
        self.label_1.pack(side="left",padx=30,pady=50)
        self.entry_1.pack(side="left")
        
        self.label_2.pack(side="left",padx=30,pady=50)
        self.entry_2.pack(side="left")

        self.btn1.pack(padx=30,pady=50,side="left")
        self.btn2.pack(padx=30,pady=50,side='left')
        
        self.btn1["text"]="提交"
        self.btn2["text"]="退出"
        
        self.btn1["command"]=self.loginCheck
        self.btn2["command"]=self.root.destroy
        
   
    def loginCheck(self): 
        self.name=self.username.get()
        self.passw=self.password.get()
        print(self.name)
        row=tcp.myTCP(['zhuce',self.name,self.passw])

        # conn=sqlite3.connect(r'.\atm.db')
        # cursor=conn.cursor()
        # sql="select * from user where id={} and password={}".format(self.name,self.passw)
        # cursor.execute(sql)
        # row=cursor.fetchone()
        # conn.commit()
        # #print(sql)
        # #uname=self.name
        # with open(r'.\ATM.txt', 'w') as f:
        #     f.write(self.name)
        if row =='chenggong' :
            self.root.destroy()
            root = tk.Tk()
            MainPage.MainPage(root)
            root.mainloop()
        else:
            me.showinfo(title="错误",message="用户名或密码错误！")