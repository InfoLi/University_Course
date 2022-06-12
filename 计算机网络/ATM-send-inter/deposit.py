# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:38:53 2017

@author: Administrator
"""
import tkinter as tk
import sqlite3
import tkinter.messagebox as me
import TCPClient as tcp
class deposit(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.root = master
        self.pack()
        self.root.title("存款页面")
        self.root.geometry('650x500')
        self.save=tk.IntVar(self.root)
        self.create_widgets()
        
    def create_widgets(self):  
        self.page=tk.Frame(self)
      
        self.page.pack()
        
        self.l1=tk.Label(self.page,text="存款服务",font='Helvetica -20 bold').grid(row=0,column=2,pady=50)
        
        self.l2=tk.Label(self.page,text='请输入存款数值：',font='Helvetica -20').grid(row=1,column=1,pady=50)
        
        self.en1=tk.Entry(self.page,textvariable=self.save).grid(row=1,column=3)
        
        self.btn1=tk.Button(self.page,command=self.save1,text="存款",font='Helvetica -20',width=8,height=1).grid(row=2,column=1,pady=40)
        self.btn1=tk.Button(self.page,command=self.mainpage,text="返回",font='Helvetica -20',width=8,height=1).grid(row=2,column=3)
        
        
    def mainpage(self):
        self.root.destroy()
        
    def save1(self):
        self.savemoney=self.save.get()
       
        print(self.savemoney)
        
        
        # with open(r'.\ATM.txt', 'r') as f:
        #     for s in f.readlines():
        #          #print(s)
        #          username=s
        #
        # conn=sqlite3.connect(r'.\atm.db')
        # cursor = conn.cursor()
        #
        # sql="select cash from money where id={}".format(username)
        # cursor.execute(sql)
        # cash=cursor.fetchone()
        # conn.commit()
        # print(cash)
        cash=tcp.myTCP(["cunqian",str(self.savemoney)])
        # m=cash+self.savemoney
        
        
        # a=("update money set cash={} where id={}".format(m, username))
        # cursor.execute(a)
        # conn.commit()
        me.showinfo(title="成功",message="存款成功")
        # print(m)
        self.root.destroy()
        #print(cash)
