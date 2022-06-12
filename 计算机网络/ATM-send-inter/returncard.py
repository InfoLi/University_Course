# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 18:44:02 2017

@author: Administrator
"""

import tkinter as tk
        
class returncard(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.root = master
        self.pack()
        self.root.title("退卡页面")
        self.root.geometry('650x500')
        #self.username=tk.StringVar()
        #self.password=tk.StringVar()
        self.create_widgets()
        
    def create_widgets(self):  
        self.page=tk.Frame(self)
      
        self.page.pack()
        
        self.l1=tk.Label(self.page,text="请取出您的磁卡",font='Helvetica -40 bold').grid(row=0,column=2,pady=60)
        
        self.l2=tk.Label(self.page,text='感谢您的使用，欢迎下次光临',font='Helvetica -20').grid(row=1,column=2,pady=50)
        
        self.btn1=tk.Button(self.page,text="退出",font='Helvetica -20',width=8,height=1,command=self.root.destroy).grid(row=2,column=2,pady=40)       

'''       
root = tk.Tk()
returncard(root)
root.mainloop()
'''        