from tkinter import *
import tkinter.messagebox
import time
import requests
import json
from bs4 import BeautifulSoup
import bs4
from minus import *
flag = 0
def talk(s):
# 对话
  global flag
  flag = 0
  sign = 1;
  while (sign):
    if '1' in s:
      flag = 1
      return ("请输入城市：(guangzhou,beijing,shanghai,shenzhen,hangzhou\n"
                  "chengdu,wuhan,changsha,xiamen,suzhou,taiyuan,shenyang,changchun,haerbin\n"
                  "nanjing,hefei,fuzhou,jinan,zhengzhou,haikou,guiyang,kunming,xian,lanzhou\n")
    if '2' in s:
      flag = 2
      return ("请输入城市：(guangzhou,beijing,shanghai,shenzhen,hangzhou\n"
                  "chengdu,wuhan,changsha,xiamen,suzhou,taiyuan,shenyang,changchun,haerbin\n"
                  "nanjing,hefei,fuzhou,jinan,zhengzhou,haikou,guiyang,kunming,xian,lanzhou\n"
              "职业:(C%23,C++,Java,JavaScript,MySQL,PHP,Python,VB)\n")
    if '3' in s:
      flag = 3
      return ("想要了解的词云zhiwei:[职位],fuli:[公司福利],guanjianci:[职位关键词]\n"
              "输入城市：guangzhou,beijing,shanghai,shenzhen,hangzhou\n"
              "chengdu,wuhan,changsha,xiamen,suzhou,taiyuan,shenyang,changchun,haerbin\n"
              "nanjing,hefei,fuzhou,jinan,zhengzhou,haikou,guiyang,kunming,xian,lanzhou\n"
              "输入职业:C%23,C++,Java,JavaScript,MySQL,PHP,Python,VB)\n")
    if '4' in s:
      flag = 4
      return("请输入职业:(C%23,C++,Java,JavaScript,MySQL,PHP,Python,VB)\n")
    if '5' in s:
      flag = 5
      return ("请输入城市：(guangzhou,beijing,shanghai,shenzhen,hangzhou\n"
                  "chengdu,wuhan,changsha,xiamen,suzhou,taiyuan,shenyang,changchun,haerbin\n"
                  "nanjing,hefei,fuzhou,jinan,zhengzhou,haikou,guiyang,kunming,xian,lanzhou\n"
              "职业:(C%23,C++,Java,JavaScript,MySQL,PHP,Python,VB)\n")
    else:
      return "功能菜单：1.城市各项职业平均月薪对比展示\n2.城市某项职业应聘需求展示\n3.词云\n4.全国各地平均月薪比较\n5.单城市单职业月薪分布\n"
      #调用图灵机器人
      # try:
      #   key = 'fa72382d2ace4913841df4ca3c5451ba'
      #   info = s
      #   url = 'http://www.tuling123.com/openapi/api?key=' + key + '&info=' + info
      #   res = requests.get(url)
      #   res.encoding = 'utf-8'
      #   data = json.loads(res.text)
      #   return(data['text']+'\n')
      # except:
      #   return('机器人过期了or没接网线')

def main():
  def start():
    strMsg = '小冰:' + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + '\n'
    txtMsgList.insert(END, strMsg, 'redcolor')
    txtMsgList.insert(END, '功能菜单：'+'\n'
                           '1.城市各项职业平均月薪对比展示'+'\n'
                           '2.城市某项职业应聘需求展示'+'\n'
                           '3.词云'+'\n'
                           '4.全国各地平均月薪比较'+'\n'
                           '5.单城市单职业月薪分布'+'\n')


  def sendMsg():  # 发送消息
    global flag
    t = txtMsg.get('0.0', END)
    if flag == 1:
      t = t.replace('\r','').replace('\n','').replace('\t','')
      getcityalljobsalary(t)
    if flag == 2:
      t = t.replace('\r', '').replace('\n', '').replace('\t', '')
      list = t.split()
      getwordcloudbar(list[0],list[1])
    if flag == 3:
      t = t.replace('\r', '').replace('\n', '').replace('\t', '')
      list = t.split()
      getwordcloud(list[0],list[1],list[2])
    if flag == 4:
      t = t.replace('\r', '').replace('\n', '').replace('\t', '')
      getmap(t)
    if flag == 5:
      t = t.replace('\r', '').replace('\n', '').replace('\t', '')
      list = t.split()
      getonecitysalary(list[0],list[1])

    txtMsg.delete('0.0', END)
    strMsg = '我:' + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + '\n'
    for i in range(int(txtMsgList.index(END).split(".")[0]) - int(txtMsgList.index(END).split(".")[0]) + 1):
      txtMsgList.insert(END, '\n')
    txtMsgList.insert(END, strMsg, 'greencolor')
    txtMsgList.insert(END, t,'yellowcolor')
    txtMsgList.see(END)
    strMsg = '小冰:' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n'
    for i in range(int(txtMsgList.index(END).split(".")[0]) - int(txtMsgList.index(END).split(".")[0]) + 1):
      txtMsgList.insert(END, '\n')
    txtMsgList.insert(END, strMsg, 'redcolor')
    txtMsgList.insert(END, talk(t))
    txtMsgList.see(END)

  def cancelMsg():  #取消消息
    txtMsg.delete('0.0', END)

  def sendMsgEvent(event):  # 发送消息事件
    sendMsg()


#框架
  t = Tk()
  t.title('招聘助手')
#分区
  frm01 = Frame(t,width=300, height=187, bg='red')
  # frm02 = Frame(t, width=300, height=150, bg='pink')
  frm00 = Frame(t,width=500, height=500, bg='green')
  frm10 = Frame(t,width=500, height=500, bg='yellow')
  frm20 = Frame(t,width=500, height=30, bg='black')

  frm01.grid(row=0,column=2)
  # frm02.grid(row=1, column=2)
  frm00.grid(row=0,column=0)
  frm10.grid(row=1,column=0)
  frm20.grid(row=2,column=0)


#文本
  txtMsgList = Text(frm00)
  txtMsg = Text(frm10,height=10)
  txtMsgList.tag_config('yellowcolor', background='yellow')  # 创建tag
  txtMsgList.tag_config('greencolor', foreground='green')
  txtMsgList.tag_config('redcolor', foreground='red')

  txtMsgList.pack()
  txtMsg.pack()
  start()

#按钮
  btnSend = Button(frm20, text='发送(F12)', width=8, command=sendMsg, bg='#E88384', bd=0)
  btnSend.grid(row=0, column=0)
  btnCancel = Button(frm20, text='取消', width=8, command=cancelMsg, bg='#F3ADA0', bd=0)
  btnCancel.grid(row=0, column=1)

  txtMsg.bind('<F12>',sendMsgEvent)

#滑轮
  scollor=Scrollbar(bg='white')
  scollor.config(command=txtMsgList.yview)
  txtMsgList.config(yscrollcommand=scollor.set)
  scollor.grid(row=0,column=1,sticky=N+S)

#图片
  imgInfo = PhotoImage(file="headshot.gif")
  lblImage = Label(frm01, image=imgInfo)
  lblImage.image = imgInfo
  lblImage.pack()

  t.mainloop()
if __name__ == '__main__':
    main()
