from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.faker import Faker
import csv
#单个城市职业月薪数据分解及处理
jobname="Python"
place_list=["shenzhen","beijing","shanghai","hangzhou","chengdu","wuhan","changsha","xiamen","suzhou","taiyuan","shenyang","changchun","haerbin","hefei","jinan","zhengzhou","haikou","guiyang","kunming","xian","lanzhou"]
place_list_cn=["广东","北京","上海","浙江","四川","湖北","湖南","福建","江苏","山西","辽宁","吉林","黑龙江","安徽","山东","河南","海南","贵州","云南","陕西","甘肃"]
placeaver=[]
for placename,placenamecn in zip(place_list,place_list_cn):
    sum = 0
    count = 0
    with open('data\\'+placename+'-'+jobname+'.csv','r') as f:
        read = csv.reader(f)
        for i in read:
            try:
                if i[2]=="月薪":
                    continue
                result=i[2].split('-')
                result[0]=int(result[0][0:result[0].index("k")])
                result[1] = int(result[1][0:result[1].index("k")])
                count = count +1
                sum = sum + (result[0]+result[1])/2
            except:
                pass
    end = sum/count
    salaryaver=[placenamecn,int(end)]
    placeaver.append(salaryaver)


c = (
    Geo()
    .add_schema(maptype="china")
    .add("月薪", [list(z) for z in placeaver])
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(is_piecewise=True),
        title_opts=opts.TitleOpts(title="全国"+jobname+"月薪分布"),
    )
    .render("全国"+jobname+"月薪图.html")
)