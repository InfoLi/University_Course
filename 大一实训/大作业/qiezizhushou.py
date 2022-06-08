from tkinter import *
import tkinter.messagebox
import time
import requests
import json
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url, timeout=30):
  try:
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text
  except:
    return '产生异常'

def get_data(html):
  final_list = []
  soup = BeautifulSoup(html, 'html.parser')
  body = soup.body
  data = body.find('div', {'id': '7d'})
  ul = data.find('ul')
  lis = ul.find_all('li')
  for day in lis:
    temp_list = []
    date = day.find('h1').string  # 找到日期
    temp_list.append(date)
    info = day.find_all('p')  # 找到所有的p标签
    temp_list.append(info[0].string)
    if info[1].find('span') is None:  # 找到p标签中的第二个值'span'标签——最高温度
      temperature_highest = ' '  # 用一个判断是否有最高温度
    else:
      temperature_highest = info[1].find('span').string
      temperature_highest = temperature_highest.replace('°', ' ')
    if info[1].find('i') is None:  # 找到p标签中的第二个值'i'标签——最低温度
      temperature_lowest = ' '  # 用一个判断是否有最低温度
    else:
      temperature_lowest = info[1].find('i').string
      temperature_lowest = temperature_lowest.replace('°', ' ')
    temp_list.append(temperature_highest)  # 将最高气温添加到temp_list中
    temp_list.append(temperature_lowest)  # 将最低气温添加到temp_list中
    final_list.append('\n')
    final_list.append(temp_list)  # 将temp_list列表添加到final_list列表中
  return final_list

# 抓取天气网站的信息
def getWeather():
  url = 'http://www.weather.com.cn/weather/101040100.shtml'
  html = getHTMLText(url)
  list = get_data(html)
  return list

#对话
def talk(s):
  sign = 1;
  while (sign):
    if '草' in s or '日' in s:
      return 'wdnmd\n'
    elif '垃圾' in s or '傻逼' in s:
      return '我起了，一枪秒了，有什么好说的。\n'
    elif '？' in s:
      return '给我发把狙，这把拿下给你看\n'
    elif '行吧' in s:
      return '我操了都\n'
    elif '天气查询' in s:
      return getWeather()
    else:   #调用图灵机器人
      try:
        key = 'fa72382d2ace4913841df4ca3c5451ba'
        info = s
        url = 'http://www.tuling123.com/openapi/api?key=' + key + '&info=' + info
        res = requests.get(url)
        res.encoding = 'utf-8'
        data = json.loads(res.text)
        return(data['text']+'\n')
      except:
        return('机器人过期了or没接网线')

def main():
  def start():
    strMsg = '茄子:' + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + '\n'
    txtMsgList.insert(END, strMsg, 'redcolor')
    txtMsgList.insert(END, 'A1高闪来一个好吗,秋梨膏'+'\n')

  def sendMsg():  # 发送消息
    t = txtMsg.get('0.0', END)
    txtMsg.delete('0.0', END)
    strMsg = '我:' + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + '\n'
    for i in range(int(txtMsgList.index(END).split(".")[0]) - int(txtMsgList.index(END).split(".")[0]) + 1):
      txtMsgList.insert(END, '\n')
    txtMsgList.insert(END, strMsg, 'greencolor')
    txtMsgList.insert(END, t,'yellowcolor')
    txtMsgList.see(END)
    strMsg = '茄子:' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n'
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
  t.title('茄子助手')
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

# 菜单
  def message1():
    tkinter.messagebox.showinfo(title='功能菜单', message="""
  1.素质聊天
  2.天气查询（重庆）
  """)
  menubar = Menu(t)
  filemenu = Menu(menubar, tearoff=0)
  menubar.add_cascade(label='Menu', menu=filemenu)
  filemenu.add_command(label='specification', command=message1)
  t.config(menu=menubar)

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
