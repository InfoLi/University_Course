import csv
import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType

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
    min=[0,0,0,0,0,0,0,0,0]
    max=[0,0,0,0,0,0,0,0,0]
    aver=[0,0,0,0,0,0,0,0,0]
    bins=[-1,5,10,15,20,25,30,35,40,300]    #分组范围
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
#三柱(min,max,salary)柱状图
def onecitysalary(min,max,aver,jobname,placename):
    name_list = ["1k-5k","5k-10k","10k-15K","15K-20K","20k-25K","25K-30K","30K-35K","35K-40K","more than 40K"]
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(xaxis_data=name_list)
        .add_yaxis("最低工资分布", [min[0], min[1], min[2], min[3], min[4], min[5],min[6],min[7],min[8]])
        .add_yaxis("最高工资分布", [max[0], max[1], max[2], max[3], max[4], max[5],max[6],max[7],max[8]])
        .add_yaxis("平均工资分布", [aver[0], aver[1], aver[2], aver[3], aver[4], aver[5],aver[6],aver[7],aver[8]])
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),  #解决x轴文字显示不全的问题
            title_opts=opts.TitleOpts(title=jobname+"工程师月薪统计表", subtitle="地区："+placename)
        )
        .render(placename+jobname+"salary.html")
    )
def main():
    placename = input("请输入城市：(guangzhou,beijing,shanghai,shenzhen,hangzhou,chengdu,wuhan,changsha,xiamen,suzhou,taiyuan,shenyang,changchun,haerbin,nanjing,hefei,fuzhou,jinan,zhengzhou,haikou,guiyang,kunming,xian,lanzhou\n")
    jobname = input("请输入职业:(C%23,C++,Java,JavaScript,MySQL,PHP,Python,VB)\n")
    a,b,c=salary(placename,jobname)
    onecitysalary(a,b,c,jobname,placename)






main()








