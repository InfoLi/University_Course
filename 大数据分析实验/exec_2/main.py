import numpy as np
import pandas as pd

def loaddata():
    data = {'001': '牛奶,面包', '002': '面包,尿布,啤酒,橙汁',
            '003': '牛奶,尿布,啤酒,鸡翅', '004': '面包,牛奶,尿布,啤酒',
            '005': '面包,牛奶,尿布,鸡翅'}
    data_set = []
    for key in data:
        item = data[key].split(',')
        data_set.append(item)
    return data_set

def createC1(d):
    C1 = []
    for row in d:
        for item in row:
            if[item] not in C1:
                C1.append([item])
    C1.sort()
    return list(map(frozenset, C1))

def calSupport(D, C, minSupport):
    """
    计算1项候选集的支持度,剔除小于最小支持度的项集，
    :param D: 数据集
    :param C1: 候选集
    :param minSupport: 最小支持度
    :return: 返回1项频繁集及其支持度
    """
    dict_sup = {}  # 中间储存变量，用于计数
    # 迭代每一条数据，对项集中的每一项进行计数
    for i in D:
        for j in C:
            # 集合j是否是集合i的子集，如果是返回True，否则返回False
            if j.issubset(i):
                # 再判断之前有没有统计过，没有统计过的话为1
                if j not in dict_sup:
                    dict_sup[j] = 1
                else:
                    dict_sup[j] += 1
    # 事务总数
    sumCount = float(len(D))
    # 计算支持度，支持度 = 项集的计数/事务总数
    supportData = {}  # 用于存储频繁集的支持度
    relist = []  # 用于存储频繁集
    for i in dict_sup:
        temp_sup = dict_sup[i] / sumCount
        # 将剔除后的频繁项集及其对应支持度保存起来
        if temp_sup > minSupport:
            relist.append(i)
            supportData[i] = temp_sup
    # 返回1项频繁项集及其对应支持度
    return relist, supportData


def aprioriGen(Lk, k):
    """
    改良了剪枝步，原来的Ck是由L1与L(k-1)来连接产生的，这里采用了新的连接方式
    使用剪枝算法，减少了候选集空间，找到k项候选集
    :param Lk: k-1项频繁集
    :param k: 第k项
    :return: 第k项候选集
    """
    reList = []  # 用来存储第k项候选集
    lenLk = len(Lk)  # 第k-1项频繁集的长度
    # 两两组合遍历
    for i in range(lenLk):
        for j in range(i + 1, lenLk):
            L1 = list(Lk[i])[:k - 2]
            L2 = list(Lk[j])[:k - 2]
            L1.sort()
            L2.sort()
            # 前k-1项相等，则可相乘，这样可以防止重复项出现
            if L1 == L2:
                a = Lk[i] | Lk[j]  # a为frozenset集合
                # 进行剪枝
                a1 = list(a)  # a1为k项集中的一个元素
                b = []  # b为它的所有k-1项子集
                # 构造b:遍历取出每一个元素，转换为set，依次从a1中剔除该元素，并加入到b中
                for q in range(len(a1)):
                    t = [a1[q]]
                    tt = frozenset(set(a1) - set(t))
                    b.append(tt)

                # 当b都是频繁集时，则保留a1,否则，删除
                t = 0
                for w in b:
                    # 如果为True，说明是属于候选集，否则不属于候选集
                    if w in Lk:
                        t += 1
                # 如果它的子集都为频繁集，则a1是候选集
                if len(b) == t:
                    reList.append(b[0] | b[1])

    return reList

def scanD(D, Ck, minSupport):
    """
    计算候选k项集的支持度，剔除小于最小支持度的候选集，得到频繁k项集及其支持度
    :param D: 数据集
    :param Ck: 候选k项集
    :param minSupport: 最小支持度
    :return: 返回频繁k项集及其支持度
    """
    sscnt = {}  # 存储支持度
    for tid in D:  # 遍历数据集
        for can in Ck:  # 遍历候选项
            if can.issubset(tid):  # 判断数据集中是否含有候选集各项
                if can not in sscnt:
                    sscnt[can] = 1
                else:
                    sscnt[can] += 1

    # 计算支持度
    numItem = len(D)  # 事务总数
    reList = []  # 存储k项频繁集
    supportData = {}  # 存储频繁集对应支持度
    for key in sscnt:
        support = sscnt[key] / numItem
        if support > minSupport:
            reList.insert(0, key)  # 满足条件的加入Lk中
            supportData[key] = support
    return reList, supportData

def apriori(dataset,minSupport):
    C1 = createC1(dataset)
    D = list(map(set, dataset))
    L1, supportData = calSupport(D, C1, minSupport)
    L = [L1]
    k = 2
    # 跳出循环的条件是没有候选集
    while len(L[k - 2]) > 0:
        # 产生k项候选集Ck
        Ck = aprioriGen(L[k - 2], k)
        # 计算候选k项集的支持度，剔除小于最小支持度的候选集，得到频繁k项集及其支持度
        Lk, supK = scanD(D, Ck, minSupport)
        # 将supK中的键值对添加到supportData
        supportData.update(supK)
        # 将第k项的频繁集添加到L中
        L.append(Lk)  # L的最后一个值为空值
        k += 1
    del L[-1]
    # 返回频繁集及其对应的支持度；L为频繁项集，是一个列表，1,2，3项集分别为一个元素
    return L, supportData




if __name__ == '__main__':
    minSupport = 0.3
    minConf = 0.7
    dataset = loaddata()
    L, supportData = apriori(dataset, minSupport)
    print(supportData)