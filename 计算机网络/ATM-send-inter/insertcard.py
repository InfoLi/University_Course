# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 18:53:16 2017
@author: Administrator
"""
import tkinter as tk
import LoginPage
       
class returncard(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.pack()
        self.root = master
        self.root.title("插卡页面")
        self.root.geometry('650x500')
        self.create_widgets()

        
    def create_widgets(self):  
        self.page=tk.Frame(self.root)

        self.page.pack()
        self.l1=tk.Label(self.page,text="请插入您的磁卡",font='Helvetica -40 bold').grid(row=0,column=2,pady=60)
        
        self.l2=tk.Label(self.page,text='欢迎使用ATM机系统',font='Helvetica -20').grid(row=1,column=2,pady=50)
        
        self.btn1=tk.Button(self.page,command=self.loginpage,text="插入",font='Helvetica -20',width=8,height=1).grid(row=2,column=2,pady=40)
        
        
    def loginpage(self):
        self.root.destroy()
        root = tk.Tk()
        LoginPage.LoginPage(root)
        root.mainloop()


root = tk.Tk()
returncard(root)
root.mainloop()