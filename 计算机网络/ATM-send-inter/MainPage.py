# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 22:30:13 2017

@author: Administrator
"""

import tkinter as tk
import balance
import deposit
import draw
import transfer
import returncard

        
class MainPage(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        
        self.root = master
        self.pack()
        self.root.title("选择页面")
        self.root.geometry('650x500')
        self.create_widgets()
        
    def create_widgets(self):  
        self.page=tk.Frame(self)
      
        self.page.pack()
        
        self.l1=tk.Label(self.page,text="请选择所需要的服务",font='Helvetica -20 bold').grid(row=0,column=4,pady=50)
        self.btn1=tk.Button(self.page,command=self.balance,text="查询余额",font='Helvetica -20',width=15,height=1).grid(row=1,column=2,pady=20)
        self.btn2=tk.Button(self.page,command=self.deposit,text="存款",font='Helvetica -20',width=15,height=1).grid(row=1,column=5)
        
        self.btn3=tk.Button(self.page,command=self.draw,text="取款",font='Helvetica -20',width=15,height=1).grid(row=2,column=2,pady=40)
        self.btn4=tk.Button(self.page,command=self.transfer,text="转账",font='Helvetica -20',width=15,height=1).grid(row=2,column=5)
        self.btn5=tk.Button(self.page,command=self.returncard,text="退卡",font='Helvetica -20',width=15,height=1).grid(row=3,column=4,pady=25)
        
    def balance(self):
        root = tk.Tk()
        balance.balance(root)
        root.mainloop()  
       
        
    def deposit(self):
        root = tk.Tk()
        deposit.deposit(root)
        root.mainloop()  
        
    def draw(self):
        root = tk.Tk()
        draw.draw(root)
        root.mainloop()  
    
    def transfer(self):
        root = tk.Tk()
        transfer.transfer(root)
        root.mainloop()  
       
    
    def returncard(self):
        self.root.destroy()
        root = tk.Tk()
        returncard.returncard(root)
        root.mainloop() 