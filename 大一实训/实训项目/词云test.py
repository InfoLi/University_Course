import csv
import jieba
import numpy as np
import pandas as pd
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pyecharts.options as opts
from pyecharts.charts import WordCloud
from pyecharts.charts import Bar

# #职位词云
# jobName = pd.read_csv('data\\guangzhou-Python.csv',usecols=[1],encoding = "gbk")
# job = jobName
# # 将数据拼接成字符串
# job = job['职位'].sum()
# # print(job)
# job_list = jieba.cut(job)
# word = " ".join(job_list)
# # 打开目标图像
# alice_mask = np.array(Image.open("02.png"))
#
# wc = WordCloud(mask=alice_mask,
#                 font_path="STSONG.TTF",            # 字体以路径的方式加载
#                 background_color="white",
#                 contour_width=3,
#                 contour_color='steelblue',
#                 max_words=500
#                 )
#
# # 文本给词云
# wc.generate_from_text(word)
# # 保存词云文件
# wc.to_file('shut.png')
#
# plt.imshow(wc)
# plt.axis("off")
# plt.show()

#通用词云生成
jobneed = pd.read_csv('data\\guangzhou-Python.csv',usecols=[5],encoding = "gbk")
print(jobneed)
numlist=jobneed.value_counts().tolist()
wordlist=jobneed.value_counts().index.tolist()
name=wordlist[0:9]
"""
bar = (
        Bar()
        .add_xaxis(xaxis_data=name)
        .add_yaxis("最低工资分布", [numlist[0], numlist[1], numlist[2], numlist[3], numlist[4], numlist[5],numlist[6],numlist[7],numlist[8]])
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),  #解决x轴文字显示不全的问题
            title_opts=opts.TitleOpts(title="工程师月薪统计表", subtitle="地区：")
        )
        .render("sy.html")
    )
"""
list=[]
for i,j in zip(wordlist,numlist):
    a=[i,j]
    list.append(a)
(
    WordCloud()
    .add(series_name="应聘需求", data_pair=list, word_size_range=[16, 100])
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="应聘需求", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
    .render("应聘需求.html")
)
