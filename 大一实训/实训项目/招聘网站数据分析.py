import csv
import time
import jieba
import requests
import json
import random
import numpy as np
import pandas as pd
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def get_list_json(list_url):
    """
    根据url获取网站列表页的JSON格式数据
    :param list_url:
    :return:
    """
    header = {
        "Host": "search.51job.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br"
    }
    try:
        response = requests.get(list_url, headers=header)
        # 设置编码方式
        response.encoding = 'gbk'
    except Exception as e:
        print("请求页异常：url={},error={}".format(list_url, e))
        return None
    else:
        return response.text


def parser_list_json(list_json):
    """
    解析列表页JSON数据
    :param list_json:
    :return:
    """
    # 将字符串的形式转换为dict
    list_data = json.loads(list_json)
    # 目标数据
    result = list_data['engine_search_result']
    print(result)
    for data in result:
        # 获取职位名称
        jobName = data['job_name'].strip()
        # 获取公司名称
        companyName = data['company_name'].strip()
        # 获取公司性质
        companyType = data['companytype_text'].strip()
        # 获取工作地点
        workArea = data['workarea_text'].strip()
        # 获取薪资范围
        salary = data['providesalary_text'].strip()
        # 获取福利待遇
        jobWelf = data['jobwelf'].strip()
        # 加入到列表中
        dataList.append([jobName, companyName, companyType, workArea, salary, jobWelf])


dataList = []


def save_to_csv():
    """
    保存数据到 csv文件
    :return:
    """
    with open('51job.csv', 'w', newline="") as csvfile:
        writer = csv.writer(csvfile)
        # 写标题
        writer.writerow(['职位名称', '公司名称', '公司性质', '工作地点', '薪资', '福利待遇'])
        writer.writerows(dataList)


def main(keywords, pages):
    for index in range(1, pages + 1):
        url = "https://search.51job.com/list/060000,000000,0000,00,9,99,{},2,{}.html".format(keywords, str(index))
        print("正在爬取第" + str(index) + "页数据")
        # 获取JSON
        list_json = get_list_json(url)
        # 解析数据
        parser_list_json(list_json)
        # 线程休眠
        time.sleep(random.randrange(1, 4))


if __name__ == '__main__':
    # 爬取数据
    # main('python', 1)
    # 保存文件
    # save_to_csv()

    # 读csv文件 usecols=[0]表示只读第一列数据
    jobName = pd.read_csv('51job.csv', usecols=[0])
    # 获取重复最高的职位名称
    # job = pd.concat([jobName.drop_duplicates(), jobName.drop_duplicates(keep=False)]).drop_duplicates(keep=False)
    job = jobName
    # 将数据拼接成字符串
    job = job['职位名称'].sum()
    print(job)
    job_list = jieba.cut(job)
    word = " ".join(job_list)

    # 打开目标图像
    alice_mask = np.array(Image.open("alice_color.png"))

    wc = WordCloud(mask=alice_mask,
                   font_path="/System/Library/Fonts/PingFang.ttc",  # 字体以路径的方式加载
                   background_color="white",
                   contour_width=3,
                   contour_color='steelblue',
                   max_words=2000
                   )

    # 文本给词云
    wc.generate_from_text(word)
    # 保存词云文件
    wc.to_file('alice_color2.png')

    plt.imshow(wc)
    plt.axis("off")
    plt.show()
