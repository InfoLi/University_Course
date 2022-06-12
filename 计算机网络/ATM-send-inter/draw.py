# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 17:05:20 2017

@author: Administrator
"""

import tkinter as tk
import sqlite3
import tkinter.messagebox as me
import TCPClient as tcp
class draw(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.pack()
        self.root = master   
        self.root.title("取款页面")
        self.root.geometry('650x500')
        self.drawcash=tk.IntVar(self.root)  
        self.create_widgets()
        
    def create_widgets(self):  
        self.page=tk.Frame(self)
        self.page.pack()
        self.l1=tk.Label(self.page,text="取款服务",font='Helvetica -20 bold').grid(row=0,column=2,pady=50)
        self.l2=tk.Label(self.page,text='请输入取款数值：',font='Helvetica -20').grid(row=1,column=1,pady=50)
        self.en1=tk.Entry(self.page,textvariable=self.drawcash).grid(row=1,column=3)
        self.btn1=tk.Button(self.page,command=self.draw,text="取款",font='Helvetica -20',width=8,height=1).grid(row=2,column=1,pady=40)
        self.btn1=tk.Button(self.page,command=self.mainpage,text="返回",font='Helvetica -20',width=8,height=1).grid(row=2,column=3)
        
    def mainpage(self):
        self.root.destroy()
        
    def draw(self):
        self.drawmoney=self.drawcash.get()
        print(self.drawmoney)
        # with open(r'.\ATM.txt', 'r') as f:
        #     for s in f.readlines():
        #          #print(s)
        #          username=s
        # conn=sqlite3.connect(r'.\atm.db')
        # cursor = conn.cursor()
        # sql="select cash from money where id={}".format(username)
        # cursor.execute(sql)
        # cash=cursor.fetchone()
        # conn.commit()
        hhh=tcp.myTCP(["quqian",str(self.drawmoney)])
        # print(cash)
        # m=cash[0]-self.drawmoney
        if hhh=="chenggong":
            # a=("update money set cash={} where id={}".format(m, username))
            # cursor.execute(a)
            # conn.commit()
            me.showinfo(title="成功",message="取款成功")
            self.root.destroy()
        else:
            me.showinfo(title="错误",message="取款失败")
            self.root.destroy()
        # print(m)