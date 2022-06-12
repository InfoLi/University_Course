# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 17:27:15 2017

@author: Administrator
"""

import tkinter as tk
import sqlite3
import TCPClient as tcp
class balance(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.root = master
        self.pack()
        self.root.title("查询页面")
        self.root.geometry('650x500')
       
        self.create_widgets()
        
        
       
        
    def create_widgets(self):
        self.page=tk.Frame(self)
        self.page.pack()
        
        
        # with open(r'.\ATM.txt', 'r') as f:
        #     for s in f.readlines():
        #          print(s)
        #          username=s
        #
        # conn=sqlite3.connect(r'.\atm.db')
        # cursor = conn.cursor()
        #
        # sql="select cash from money where id={}".format(username)
        # cursor.execute(sql)
        # cash=cursor.fetchone()
        # conn.commit()
        cash=tcp.myTCP(['chaxun'])
        self.l1=tk.Label(self.page,text="查询余额服务",font='Helvetica -20 bold').grid(row=0,column=2,pady=50)
        
        self.l2=tk.Label(self.page,text='您当前的余额为：',font='Helvetica -20').grid(row=1,column=1,pady=50)
        self.l3=tk.Label(self.page,text=cash,font='Helvetica -20').grid(row=1,column=3)
        self.btn1=tk.Button(self.page,command=self.mainpage,text="返回",font='Helvetica -20',width=8,height=1).grid(row=2,column=2,pady=40)
        #print(username)
        print(cash)
    
    def mainpage(self):
        self.root.destroy()