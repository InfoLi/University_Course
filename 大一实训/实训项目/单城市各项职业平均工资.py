import pyecharts.options as opts
from pyecharts.charts import Bar3D
import csv
import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Bar
job_list=["C%23","C++","Java","JavaScript","MySQL","PHP","Python"]
def salary(placename,jobname):
    #单个城市职业月薪数据分解及处理
    with open('data\\'+placename+'-'+jobname+'.csv','r') as f:
        read = csv.reader(f)
        minsalary=[]
        maxsalary=[]
        averagesalary=[]
        for i in read:
            try:
                if i[2]=="月薪":
                    continue
                result=i[2].split('-')
                result[0]=int(result[0][0:result[0].index("k")])
                result[1] = int(result[1][0:result[1].index("k")])
                minsalary.append(result[0])
                maxsalary.append(result[1])
                averagesalary.append((result[0]+result[1])/2)
            except:
                pass
    # print(minsalary)
    # print(maxsalary)
    # print(averagesalary)
    min=[0,0,0,0,0,0,0,0,0,0,0,0]
    max=[0,0,0,0,0,0,0,0,0,0,0,0]
    aver=[0,0,0,0,0,0,0,0,0,0,0,0]
    bins=[-1,5,10,15,17,20,23,25,28,30,35,40,300]    #分组范围
    mincount=list(pd.cut(minsalary,bins,labels=False))      #min分组
    maxcount=list(pd.cut(maxsalary,bins,labels=False))
    avercount=list(pd.cut(averagesalary,bins,labels=False))
    # print(mincount)

    for i in mincount:
        min[i]=min[i]+1       #分组结果统计
    for i in maxcount:
        max[i]=max[i]+1
    for i in avercount:
        aver[i]=aver[i]+1
    return(min,max,aver)

def var3d(list,job_list,place):
    valuelist = ["5k", "10k", "15K","17K","19K","21K","23K","25K","27K","29K","30K","35K" "40K", "more than 40K"]
    var=(
        Bar3D(init_opts=opts.InitOpts(width="1600px", height="800px"))
        .add(
            series_name="",
            data=list,
            xaxis3d_opts=opts.Axis3DOpts(type_="category", data=valuelist),
            yaxis3d_opts=opts.Axis3DOpts(type_="category", data=job_list),
            zaxis3d_opts=opts.Axis3DOpts(type_="value"),
        )
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_=200,
                                              range_color=[
                                                  "#313695",
                                                  "#4575b4",
                                                  "#74add1",
                                                  "#abd9e9",
                                                  "#e0f3f8",
                                                  "#ffffbf",
                                                  "#fee090",
                                                  "#fdae61",
                                                  "#f46d43",
                                                  "#d73027",
                                                  "#a50026",
                                              ],
                                              ),
            title_opts=opts.TitleOpts(title= "各项职业平均月薪对比", subtitle="地区:"+place)
        )
        .render("why.html")
    )
def main():
    place = "beijing"
    list=[]
    i=0
    for job in job_list:
        a,b,c = salary(place,job)
        list1=[[0,i,c[0]],[1,i,c[1]],[2,i,c[2]],[3,i,c[3]],[4,i,c[4]],[5,i,c[5]],[6,i,c[6]]
            ,[7,i,c[7]],[8,i,c[8]],[9,i,c[9]],[10,i,c[10]],[11,i,c[11]]]
        list = list+list1
        i=i+1
        c.clear()
    var3d(list,job_list,place)








main()
