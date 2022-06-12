from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

import pandas as pd
import numpy as np

city = None
citylist = {
    "北京":'bj',
    "成都":'cd',
    "上海":'sh',
    "重庆":'cq',
    "广州":'gz',
    "三亚":"sa",
    "西安":"xa",
    "厦门":"xm",
    "丽江":"lj",
    "杭州":"hz",
    "青岛":"qd",
    "大理":"dl",
    "武汉":"wh",
    "南京":"nj",
    "深圳":"shenzhen",
    "长沙":"cs",
    "苏州":"sz",
    "天津":"tj",
    "昆明":"km",
    "北海":"bh",
    # "澳门":"aomeny397",
    "长春":"changchun189",
    "桂林":"guilin32",
    "哈尔滨":"haerbin64",
    "合肥":"hefei50",
}

def index_view(request):
    if request.method == 'GET':
        return render(request,"index.html")
    if request.method == 'POST':
        global city
        city = request.POST['city']
        if(city not in list(citylist.keys())):  
            messages.error(request,'无当前城市的信息')
            return render(request,"index.html")
        else:
            dict = {
                'city0':city,
                'img':'/static/img/viewpoint/'+citylist[city]+'_viewpoint.png'
            }
            return render(request,"mainpage.html",dict)

def mainpage(request):
    dict = {
        'city0':city,
        'img':'/static/img/viewpoint/'+citylist[city]+'_viewpoint.png'
    }
    return render(request,"mainpage.html",dict)

def pricepage(request):
    dict = {
        'city0':city,
        'img':'/static/img/price/'+citylist[city]+'_price.png'
    }
    return render(request,"pricepage.html",dict)

def recommendedpage(request):
    city0 = city

    # 读取数据并处理
    placename = citylist[city]
    comment = pd.read_csv('F:\python\Grade2_training\data\\'+placename+'.csv',usecols=[3],encoding = "gb18030")
    comment_list = list(comment['评论数'])
    for i in range(len(comment_list)):
        if(comment_list[i]!='None'):
            comment_list[i] = int(comment_list[i])
        else:
            comment_list[i] = -1
    sort_comment = sorted(comment_list,reverse=True)[0:20]
    print(sort_comment)

    data = pd.read_csv('F:\python\Grade2_training\data\\'+placename+'.csv',encoding = "gb18030")
    a = np.array(data)
    namelist = []
    datalist = []
    for comment in sort_comment:
        for item in a:
            try:
                item_price = int(item[3])
            except:
                pass
            if((item_price) == comment):
                if(item[0] not in namelist):
                    namelist.append(item[0])
                    datalist.append(item)
    
    return render(request,"recommendedpage.html",locals())
