import requests
import csv
import time
import random
from bs4 import BeautifulSoup
place_list=["guangzhou","beijing","shanghai","shenzhen","hangzhou","chengdu","wuhan","changsha","xiamen","suzhou"]
newplace_list=["taiyuan","shenyang","changchun","haerbin","nanjing","hefei","fuzhou","jinan","zhengzhou","haikou","guiyang","kunming","xian","lanzhou",]
job_list=["C%23","C++","Java","JavaScript","MySQL","PHP","Python","VB"]
for job in job_list:
    for place in newplace_list:
        # 创建csv
        n = ["公司", "职位", "月薪", "公司介绍", "应聘要求", "福利", "职位关键词", "上班地点"]  # 文件标头
        with open(place+"-"+job+".csv", 'w', newline='') as t:  # w 覆盖 a+ 续写
            writer = csv.writer(t)  # 创建写入器
            writer.writerow(n)  # 续写时记得注释标头！！！！！！！
            # 换页面爬数据
            for i in range(1,30):   #更改页面
                urls=[#"https://www.lagou.com/guangzhou-zhaopin/Python/1/?filterOption=3&sid=fe4d72b4591b4d83a7c433ffdf012f25",
                    "https://www.lagou.com/"+place+"-zhaopin/"+job+"/" + str(i) + "/?filterOption=3&sid=fe4d72b4591b4d83a7c433ffdf012f25"
                        ] #url
                time.sleep(random.randrange(2,5)) #反爬
                for url in urls:
                    try:
                        response = requests.get(url)
                        response = response.content.decode('utf-8')
                        soup = BeautifulSoup(response, 'lxml') #页面解析
                        divdate=soup.find("div",id="s_position_list")
                        each_finders=divdate.find_all("li",class_="con_list_item default_list")
                        for each_finder in each_finders:
                            try:
                                # 获取取每个公司的招聘数据
                                datacompany = each_finder["data-company"]
                                datapositionname = each_finder["data-positionname"]
                                datasalary = each_finder["data-salary"]
                                introductiondatalist = each_finder.find("div",class_="industry").string.split()
                                dataintroduction=introductiondatalist[0]+' '+introductiondatalist[2]+' '+introductiondatalist[4]   #对数据进行缝合
                                keywordlist = each_finder.find("div",class_="li_b_l").text.split()
                                datademand = keywordlist[1]+' '+keywordlist[3]
                                keyfinder = each_finder.find("div",class_="list_item_bot")
                                keyword = keyfinder.find("div",class_="li_b_l").text.split()
                                # 缝合关键字
                                lenth = len(keyword)
                                datakeyword=""
                                for j in range(lenth):
                                    datakeyword=datakeyword+keyword[j]+' '
                                advertising = keyfinder.find("div",class_="li_b_r").text
                                placefinder = each_finder.find("span",class_="add").text
                                # print('公司:{},职位:{},月薪:{},公司介绍:{},应聘要求:{},关键词:{},福利:{}'.format(datacompany,datapositionname,datasalary,dataintroduction,datademand,datakeyword,advertising))
                                list=[datacompany,datapositionname,datasalary,dataintroduction,datademand,advertising,datakeyword,placefinder]
                                writer.writerow(list)
                            except:
                                pass
                    except:
                        pass
            print("finish " + job + place)
t.close()





