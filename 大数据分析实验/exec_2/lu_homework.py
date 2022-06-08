import copy
import csv
import matplotlib.pyplot as plt
import matplotlib as mpl
from datetime import datetime


mpl.rcParams['font.sans-serif'] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

min_sup = 0.05
min_conf = 0.5
# 最大 K 项集
K = 3


def load_simple_data():
    # 事务ID 购买商品
    data = {'001': '牛奶,面包', '002': '面包,尿布,啤酒,橙汁',
            '003': '牛奶,尿布,啤酒,鸡翅', '004': '面包,牛奶,尿布,啤酒',
            '005': '面包,牛奶,尿布,鸡翅'}
    data_set = []
    for key in data:
        item = data[key].split(',')
        data_set.append(item)
    return data_set


def load_data(path):
    data = []
    with open(path) as f:
        csv_data = csv.reader(f)
        header = next(csv_data)
        for row in csv_data:
            if len(row) <= 3:  # 去除缺失值
                continue
            data.append(row)

    return data


def construct_by_tranid(data):
    # 通过交易id重新构建交易
    id = []
    for row in data:
        id.append(row[2])

    id = list(set(id))
    # print(id)

    newdata = {}
    for row in data:
        # row[2] 位置
        if row[2] in newdata:
            # newdata[row[2]][3].append(row[3])
            newdata[row[2]].append(row[3])
        else:
            # newdata[row[2]] = [row[0], row[1], row[2], [row[3]]]
            newdata[row[2]] = [row[3]]
    for i in newdata:  # 去除重复值
        newdata[i] = list(set(newdata[i]))
    return newdata


# 构建 1-项集
def create_C1(data_set):
    C1 = set()
    for t in data_set:
        for item in t:
            item_set = frozenset([item])
            C1.add(item_set)
    return C1


# 计算给定数据每项及其支持数，第一次
def count_itemset1(data_set, C1):
    item_count = {}
    for data in data_set:
        for item in C1:
            if item.issubset(data):  # 保证对应项集存在
                if item in item_count:
                    item_count[item] += 1
                else:
                    item_count[item] = 1
    return item_count


# 生成剪枝后的 L1
def generate_L1(length, item_count):
    L1 = {}
    for i in item_count:
        if item_count[i] / length >= min_sup:
            L1[i] = item_count[i]
            # print(item_count[i] / length)
    return L1


# 判断是否该剪枝
def is_apriori(Ck_item, Lk_copy):
    for item in Ck_item:
        sub_Ck = Ck_item - frozenset([item])
        if sub_Ck not in Lk_copy:
            return False
    return True


# 生成 k 项商品集，连接操作
def create_Ck(Lk_copy, k):
    Ck = set()
    len_Lk_copy = len(Lk_copy)
    list_Lk_copy = list(Lk_copy)
    for i in range(len_Lk_copy):
        for j in range(1, len_Lk_copy):
            l1 = list(list_Lk_copy[i])
            l2 = list(list_Lk_copy[j])
            l1.sort()
            l2.sort()
            if l1[0:k - 2] == l2[0:k - 2]:
                Ck_item = list_Lk_copy[i] | list_Lk_copy[j]
                # 扫描前一个项集，剪枝
                if is_apriori(Ck_item, Lk_copy):
                    Ck.add(Ck_item)
    return Ck


# 生成剪枝后的 Lk
def generate_Lk_by_Ck(Ck, data_set):
    item_count = {}
    for data in data_set:
        for item in Ck:
            if item.issubset(data):
                if item in item_count:
                    item_count[item] += 1
                else:
                    item_count[item] = 1
    Lk2 = {}
    for i in item_count:
        if item_count[i] / len(data_set) >= min_sup:
            Lk2[i] = item_count[i]
    return Lk2


# 产生强关联规则
def generate_strong_rules(L, support_data, data_set):
    strong_rule_list = []
    sub_set_list = []
    # print(L)
    for i in range(0, len(L)):
        for freq_set in L[i]:
            for sub_set in sub_set_list:
                if sub_set.issubset(freq_set):
                    # 计算包含 X 的交易数
                    sub_set_num = 0
                    for item in data_set:
                        if (freq_set - sub_set).issubset(item):
                            sub_set_num += 1
                    conf = support_data[freq_set] / sub_set_num
                    strong_rule = (freq_set - sub_set, sub_set, conf, conf / (support_data[sub_set] / len(data_set)))
                    if conf >= min_conf and strong_rule not in strong_rule_list:
                        # print(list(freq_set-sub_set), " => ", list(sub_set), "conf: ", conf)
                        strong_rule_list.append(strong_rule)
            sub_set_list.append(freq_set)
    return strong_rule_list


def apriori(data_set):
    # 1.读入数据
    # 2.计算每项的支持数
    C1 = create_C1(data_set)
    item_count = count_itemset1(data_set, C1)
    # 3.剪枝，去掉支持数小于最小支持度数的项
    L1 = generate_L1(len(data_set), item_count)
    # print(L1)
    # 4.连接
    # 5.扫描前一个项集，剪枝
    # 6.计数，剪枝
    # 7.重复4-6，直到得到最终的 K 项频繁项集
    Lk_copy = L1.copy()
    L = []
    L.append(Lk_copy)
    for i in range(2, K + 1):
        Ci = create_Ck(Lk_copy, i)
        Li = generate_Lk_by_Ck(Ci, data_set)
        Lk_copy = Li.copy()
        L.append(Lk_copy)
    # 8.输出频繁项集及其支持度数
    print('频繁项集\t支持度')
    support_data = {}
    # L.sort(key=lambda result: result[2], reverse=True)
    L_sort = []
    for item in L:
        for i in item:
            # if item[i] / len(data_set) >= min_sup:
            #     print(list(i), '\t', item[i] / len(data_set))
            L_sort.append([list(i), item[i] / len(data_set)])
            # print(list(i), '\t', item[i] / len(data_set))
            support_data[i] = item[i]
    L_sort.sort(key=lambda result: result[1], reverse=True)
    for row in L_sort:
        print(row[0], '\t', row[1])
    # print(L_sort[0][1])
    # 9.对每个关联规则计算置信度，保留大于最小置信度的频繁项为 强关联规则
    strong_rules_list = generate_strong_rules(L, support_data, data_set)
    strong_rules_list.sort(key=lambda result: result[2], reverse=True)
    print("\nStrong association rule\nX\t\t\tY\t\tconf\t\tproval")
    for item in strong_rules_list:
        print(list(item[0]), "\t", list(item[1]), "\t", item[2], "\t", item[3])


def hot_commodity(data_set):
    count_item = count_itemset1(data_set, create_C1(data_set))
    L1 = generate_L1(len(data_set), count_item)
    # print(count_item)

    x = []
    y = []
    for key in L1:
        x.append(list(key)[0])
        y.append(count_item[key])

    plt.bar(x, y)
    plt.title("支持度大于0.05的热销商品")
    plt.show()


def string_toDatetime(st):
    return datetime.strptime(st, "%Y-%m-%d")


def week_analyse(csv_data):
    week_list = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    newdata = {}
    for row in csv_data:
        # row[2] 位置
        if row[2] in newdata:
            newdata[row[2]][3].append(row[3])
            # newdata[row[3]].append(row[3])
        else:
            newdata[row[2]] = [row[0], row[1], row[2], [row[3]]]
    for key in newdata:  # 去除重复值
        newdata[key][3] = list(set(newdata[key][3]))

    for key in newdata:
        newdata[key][0] = week_list[datetime.date(string_toDatetime(newdata[key][0])).weekday()]

    # 绘制商品交易总量
    total_tran_week = {}
    for key in newdata:
        if newdata[key][0] in total_tran_week:
            total_tran_week[newdata[key][0]] += len(newdata[key][3])
        else:
            total_tran_week[newdata[key][0]] = len(newdata[key][3])

    print(total_tran_week)
    x = copy.deepcopy(week_list)
    # print(x)
    y = []
    for i in x:
        y.append(total_tran_week[i])

    plt.bar(x, y)
    plt.ylabel("销售总量")
    plt.title("星期一至星期日商品交易情况")
    plt.show()

csv_data = load_data("./data/BreadBasket_DMS.csv")
trans_by_id = construct_by_tranid(csv_data)

data = []
for key in trans_by_id:
    data.append(trans_by_id[key])

# hot_commodity(data)
week_analyse(csv_data)
# apriori(data)

# apriori(load_simple_data())
