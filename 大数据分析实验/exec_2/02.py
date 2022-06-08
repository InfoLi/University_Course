import pandas as pd
import csv
import matplotlib.pyplot as plt
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
from datetime import datetime
import copy

# 读取数据
def load_data(path):
    data = []
    with open(path) as f:
        csv_data = csv.reader(f)
        header = next(csv_data)
        for row in csv_data:
            if len(row) <= 3:  # 去除缺失值
                continue
            if row[3] == "NONE": # 删除无效值
                continue
            data.append(row)
    return data

# 画热销物品图
def draw_hot(df):
    hot_good = df[3].value_counts()[1:10]
    hot_good.plot.bar(rot=0)
    print(hot_good)
    plt.show()

# 数据重构
def clean_data(data):
    newdata = {}
    for row in csv_data:
        if row[2] in newdata:
            newdata[row[2]][3].append(row[3])
        else:
            newdata[row[2]] = [row[0], row[1], row[2], [row[3]]]
    for key in newdata:  # 去除重复值
        newdata[key][3] = list(set(newdata[key][3]))

    return newdata

def string_toDatetime(st):
    return datetime.strptime(st, "%Y-%m-%d")

# 画周销量图
def draw_week(d):
    week_list = ["Mon", "Tue", "Wed", "Thr", "Fri", "Sat", "Sun"]
    for key in d:
        d[key][0] = week_list[datetime.date(string_toDatetime(d[key][0])).weekday()]

    # 绘制商品交易总量
    total_tran_week = {}
    for key in d:
        if d[key][0] in total_tran_week:
            total_tran_week[d[key][0]] += len(d[key][3])
        else:
            total_tran_week[d[key][0]] = len(d[key][3])

    print(total_tran_week)
    x = copy.deepcopy(week_list)
    y = []
    for i in x:
        y.append(total_tran_week[i])
    plt.bar(x, y)
    plt.ylabel("total")
    plt.title("Merchandise trading from Monday to Sunday")
    plt.show()

def Apriori(newdata):
    df01 = pd.DataFrame(new_data)
    dataset = list(df01.iloc[3])

    te = TransactionEncoder()
    # 进行 one-hot 编码
    te_ary = te.fit(dataset).transform(dataset)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    # 利用 Apriori 找出频繁项集
    freq = apriori(df, min_support=0.05, use_colnames=True).sort_values(by='support', ascending=False)
    # print(freq)
    ass_rule = association_rules(freq, metric='confidence', min_threshold=0.5).sort_values(by='leverage', ascending=False)
    print(ass_rule)


if __name__ == '__main__':
    csv_data = load_data("./data/BreadBasket_DMS.csv")
    df = pd.DataFrame(csv_data)
    # draw_hot(df)
    new_data = clean_data(csv_data)
    # draw_week(new_data)
    Apriori(new_data)


