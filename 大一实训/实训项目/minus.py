import csv
import jieba
import pandas as pd
import numpy as np
from wordcloud import WordCloud
from pyecharts.charts import WordCloud
import pyecharts.options as opts
from pyecharts.charts import Bar3D
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Geo
from pyecharts.faker import Faker
import webbrowser
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
                result[0]=int(result[0][0:result[0].index("k")])  #处理月薪数据中的无用数据
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
def onecitysalary(min,max,aver,jobname,placename):
#单城市单职业柱状图构建
    name_list = ["5k", "10k", "15K","17K","19K","21K","23K","25K","27K","29K","30K","35K" "40K", "more than 40K"]
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(xaxis_data=name_list)
        .add_yaxis("最低工资分布", [min[0], min[1], min[2], min[3], min[4], min[5],min[6],min[7],min[8],min[9],min[10],min[11]])
        .add_yaxis("最高工资分布", [max[0], max[1], max[2], max[3], max[4], max[5],max[6],max[7],max[8],max[9],max[10],max[11]])
        .add_yaxis("平均工资分布", [aver[0], aver[1], aver[2], aver[3], aver[4], aver[5],aver[6],aver[7],aver[8],aver[9],aver[10],aver[11]])
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),  #解决x轴文字显示不全的问题
            title_opts=opts.TitleOpts(title=jobname+"工程师月薪统计表", subtitle="地区："+placename)
        )
        .render(placename+jobname+"salary.html")
    )
    webbrowser.open(placename+jobname+"salary.html")

def getonecitysalary(placename,jobname):
# 单城市单职业柱状图的主函数
    a,b,c=salary(placename, jobname)
    onecitysalary(a, b, c, jobname, placename)

def var3d(list,job_list,place):
# 3d图构建
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
        .render(place+"各项职业平均月薪对比.html")
    )
    webbrowser.open(place+"各项职业平均月薪对比.html")
def getcityalljobsalary(place):
# 3d图单城市各项职业平均工资的主函数
    job_list = ["C%23", "C++", "Java", "JavaScript", "MySQL", "PHP", "Python"]
    # place = input("请输入城市：(guangzhou,beijing,shanghai,shenzhen,hangzhou\n"
    #               "chengdu,wuhan,changsha,xiamen,suzhou,taiyuan,shenyang,changchun,haerbin\n"
    #               "nanjing,hefei,fuzhou,jinan,zhengzhou,haikou,guiyang,kunming,xian,lanzhou\n")
    list=[]
    i=0
    for job in job_list:
        a,b,c = salary(place,job)
        list1=[[0,i,c[0]],[1,i,c[1]],[2,i,c[2]],[3,i,c[3]],[4,i,c[4]],[5,i,c[5]],[6,i,c[6]]
            ,[7,i,c[7]],[8,i,c[8]],[9,i,c[9]],[10,i,c[10]],[11,i,c[11]]]
        list = list+list1
        i=i+1
        c.clear()

    var3d(list, job_list, place)

def wordcloud(numlist,wordlist,place,job,num):
# 词云构建
    title_list={"zhiwei":"[职位]","fuli":"[公司福利]","guanjianci":"[职位关键词]"}
    list = []
    for i, j in zip(wordlist, numlist):
        a = [i, j]
        list.append(a)
    (
        WordCloud()
            .add(series_name="词云", data_pair=list, word_size_range=[16, 100])
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title=place+job+title_list[num]+"词云", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
            .render(place+job+title_list[num]+"词云.html")
    )
    webbrowser.open(place+job+title_list[num]+"词云.html")
def getwordcloudbar(place,job):
# 工程师应聘要求柱状图构建
    jobneed = pd.read_csv('data\\'+place+'-'+job+'.csv',usecols=[4],encoding = "gbk")
    numlist = jobneed.value_counts().tolist()
    wordlist = jobneed.value_counts().index.tolist()
    name = wordlist[0:9]
    bar = (
        Bar()
            .add_xaxis(xaxis_data=name)
            .add_yaxis("应聘要求分布",
                       [numlist[0], numlist[1], numlist[2], numlist[3], numlist[4], numlist[5], numlist[6], numlist[7],
                        numlist[8]])
            .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),  # 解决x轴文字显示不全的问题
            title_opts=opts.TitleOpts(title="应聘要求统计表", subtitle="地区："+place)
        )
            .render(place+job+"应聘要求统计表.html")
    )
    webbrowser.open(place+job+"应聘要求统计表.html")

def getwordcloud(num,place,job):
# 词云main函数
    # num = input("想要了解的词云(输入数字):1[职位],5[公司福利],6[职位关键词]\n")
    # place = input("请输入城市：(guangzhou,beijing,shanghai,shenzhen,hangzhou\n"
    #               "chengdu,wuhan,changsha,xiamen,suzhou,taiyuan,shenyang,changchun,haerbin\n"
    #               "nanjing,hefei,fuzhou,jinan,zhengzhou,haikou,guiyang,kunming,xian,lanzhou\n")
    # job = input("请输入职业:(C%23,C++,Java,JavaScript,MySQL,PHP,Python,VB)\n")
    find ={"zhiwei":1,"fuli":5,"guanjianci":6}
    jobneed = pd.read_csv('data\\'+place+'-'+job+'.csv',usecols=[int(find[num])],encoding = "gbk")
    numlist = jobneed.value_counts().tolist()
    wordlist = jobneed.value_counts().index.tolist()
    wordcloud(numlist,wordlist,place,job,num)

def getmap(jobname):
# jobname = input("请输入职业:(C%23,C++,Java,JavaScript,MySQL,PHP,Python,VB)\n")
    place_list = ["shenzhen", "beijing", "shanghai", "hangzhou", "chengdu", "wuhan", "changsha", "xiamen", "suzhou",
                  "taiyuan", "shenyang", "changchun", "haerbin", "hefei", "jinan", "zhengzhou", "haikou", "guiyang",
                  "kunming", "xian", "lanzhou"]
    place_list_cn = ["广东", "北京", "上海", "浙江", "四川", "湖北", "湖南", "福建", "江苏", "山西", "辽宁", "吉林", "黑龙江", "安徽", "山东", "河南",
                     "海南", "贵州", "云南", "陕西", "甘肃"]
    placeaver = []
    for placename, placenamecn in zip(place_list, place_list_cn):
        sum = 0
        count = 0
        with open('data\\' + placename + '-' + jobname + '.csv', 'r') as f:
            read = csv.reader(f)
            for i in read:
                try:
                    if i[2] == "月薪":
                        continue
                    result = i[2].split('-')
                    result[0] = int(result[0][0:result[0].index("k")])
                    result[1] = int(result[1][0:result[1].index("k")])
                    count = count + 1
                    sum = sum + (result[0] + result[1]) / 2
                except:
                    pass
        end = sum / count
        salaryaver = [placenamecn, int(end)]
        placeaver.append(salaryaver)

    c = (
        Geo()
            .add_schema(maptype="china")
            .add("月薪", [list(z) for z in placeaver])
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(is_piecewise=True),
            title_opts=opts.TitleOpts(title="全国" + jobname + "月薪分布"),
        )
            .render("全国" + jobname + "月薪图.html")
    )
    webbrowser.open("全国" + jobname + "月薪图.html")



