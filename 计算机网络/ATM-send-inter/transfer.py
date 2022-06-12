# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 17:10:16 2017

@author: Administrator
"""

import tkinter as tk
import sqlite3
import tkinter.messagebox as me
import TCPClient as tcp
class transfer(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.root = master
        self.pack()
        self.root.title("转账页面")
        self.root.geometry('650x500')
        self.username=tk.IntVar(self.root)
        self.cash=tk.IntVar(self.root)
        self.create_widgets()
        
    def create_widgets(self):  
        self.page=tk.Frame(self)
        self.page.pack()
        
        self.l1=tk.Label(self.page,text="转帐服务",font='Helvetica -20 bold').grid(row=0,column=2,pady=50)
        
        self.l2=tk.Label(self.page,text='转入的帐号：',font='Helvetica -20').grid(row=1,column=1,pady=50)
        
        self.en2=tk.Entry(self.page,textvariable=self.username).grid(row=1,column=3)
       
        self.l3=tk.Label(self.page,text='转入的金额：',font='Helvetica -20').grid(row=2,column=1,pady=20)
        
        self.en2=tk.Entry(self.page,textvariable=self.cash).grid(row=2,column=3)
        
        self.btn1=tk.Button(self.page,text="确定",command=self.transfer,font='Helvetica -20',width=8,height=1).grid(row=3,column=1,pady=40)
        self.btn1=tk.Button(self.page,command=self.mainpage,text="返回",font='Helvetica -20',width=8,height=1).grid(row=3,column=3)
        
        
    def mainpage(self):
        self.root.destroy()
    
    def transfer(self):
        self.money=self.cash.get()
        self.name=self.username.get()
        
        # with open(r'.\ATM.txt', 'r') as f:
        #     for s in f.readlines():
        #          #print(s)
        #          username=s
        # conn=sqlite3.connect(r'.\atm.db')
        # cursor = conn.cursor()
        #
        # sql="select cash from money where id={}".format(username)
        # cursor.execute(sql)
        # cash=cursor.fetchone()
        # conn.commit()
        # print(username)
        # print(self.money)
        # print(cash)
        hhh=tcp.myTCP(["zhuanzhang",str(self.money),str(self.name)])
        # m=cash[0]-self.money
        
        if hhh=="shibai":
            me.showinfo(title="错误", message="转账失败")
            self.root.destroy()
        else:
            me.showinfo(title="成功",message="转账成功")
            self.root.destroy()