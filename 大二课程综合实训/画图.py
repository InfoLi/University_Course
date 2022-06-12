from pyecharts.charts import Bar,Line
from pyecharts import options as opts
# 导入输出图片工具
from pyecharts.render import make_snapshot
# 使用snapshot-selenium 渲染图片
from snapshot_selenium import snapshot
import numpy as np
import pandas as pd
import csv
placelist = ["bj","cd","sh","cq","gz","sa","xa","xm","lj","hz","qd","dl","wh","nj","shenzhen","cs","sz","tj","km","bh"]

def drawviewpoint():
    for placename in placelist:
        #读取文件
        viewpoint = pd.read_csv('data\\'+placename+'.csv',usecols=[2],encoding = "gb18030")
        viewpoint_list = list(viewpoint['地利'])
        result = pd.value_counts(viewpoint_list)
        viewpoint_dict = dict(result)
        # print(list(viewpoint_dict.keys()))
        # print(list(viewpoint_dict.values()))
        value = list(viewpoint_dict.values())[0:10]
        for i in range(len(value)):
            value[i] = int(value[i])
        #画图
        bar = (
            Bar()
            .add_xaxis(xaxis_data=list(viewpoint_dict.keys())[0:10])
            .add_yaxis("地理位置",value)
            .set_global_opts(
                xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),  #解决x轴文字显示不全的问题
                title_opts=opts.TitleOpts(title="民宿中地理位置一览", subtitle="数量：")
            )
        )
        make_snapshot(snapshot,bar.render("F:\python\Grade2_training\pyecharts\\"+placename+"_viewpoint.html"),"F:\python\Grade2_training\Hotel\static\img\viewpoint\\"+placename+"_viewpoint.png")
        # make_snapshot(snapshot,bar.render("XXX.html"),"XXX.png")



def drawprice():
    for placename in placelist:
        price_standard = ['<100','100+','200+','300+','400+','500+','600+','700+','800+','900+']
        price = pd.read_csv('data\\'+placename+'.csv',usecols=[1],encoding = "gb18030")
        price_list = list(price['价格'])
        aver = int(np.mean(price_list))
        price_count = [0,0,0,0,0,0,0,0,0,0]
        for i in price_list:
            if (i < 100):
                price_count[0] = price_count[0]+1
            elif (i < 200):
                price_count[1] = price_count[1]+1
            elif (i < 300):
                price_count[2] = price_count[2]+1
            elif (i < 400):
                price_count[3] = price_count[3]+1
            elif (i < 500):
                price_count[4] = price_count[4]+1
            elif (i < 600):
                price_count[5] = price_count[5]+1
            elif (i < 700):
                price_count[6] = price_count[6]+1
            elif (i < 800):
                price_count[7] = price_count[7]+1
            elif (i < 900):
                price_count[8] = price_count[8]+1
            else:
                price_count[9] = price_count[9]+1
        line = (
            Line()
            .add_xaxis(xaxis_data=price_standard)
            .add_yaxis(
                series_name = "房价分布图",
                y_axis = price_count,
                symbol="emptyCircle",
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="民宿价格分布一览", subtitle="数量：")
            )
        )
        # line.render()
        make_snapshot(snapshot,line.render("F:\python\Grade2_training\pyecharts\\"+placename+"_price.html"),"F:\python\Grade2_training\Hotel\static\img\price\\"+placename+"_price.png")
        


# def recommended():
#     placelist = ["bj","cd","sh","cq","gz","sa","xa","xm","lj","hz","qd","dl","wh","nj","shenzhen","cs","sz","tj","km","bh"]
#     placename = "cq"
#     comment = pd.read_csv('data\\'+placename+'.csv',usecols=[3],encoding = "gb18030")
#     comment_list = list(comment['评论数'])
#     for i in range(len(comment_list)):
#         if(comment_list[i]!='None'):
#             comment_list[i] = int(comment_list[i])
#         else:
#             comment_list[i] = -1
#     sort_comment = sorted(comment_list,reverse=True)[0:10]
#     print(sort_comment)

#     data = pd.read_csv('data\\'+placename+'.csv',encoding = "gb18030")
#     a = np.array(data)
#     namelist = []
#     datalist = []
#     for comment in sort_comment:
#         for item in a:
#             try:
#                 item_price = int(item[3])
#             except:
#                 pass
#             if((item_price) == comment):
#                 if(item[0] not in namelist):
#                     namelist.append(item[0])
#                     datalist.append(item)
#     print(datalist)

    





recommended()