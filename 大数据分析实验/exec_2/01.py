import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules


def loaddata():
    data = {'001': '牛奶,面包', '002': '面包,尿布,啤酒,橙汁',
            '003': '牛奶,尿布,啤酒,鸡翅', '004': '面包,牛奶,尿布,啤酒',
            '005': '面包,牛奶,尿布,鸡翅'}
    data_set = []
    for key in data:
        item = data[key].split(',')
        data_set.append(item)
    return data_set
dataset = loaddata()
te = TransactionEncoder()
#进行 one-hot 编码
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)
#利用 Apriori 找出频繁项集
freq = apriori(df, min_support=0.3, use_colnames=True)
print(freq)
ass_rule = association_rules(freq, metric='confidence',min_threshold=0.7)
ass_rule.sort_values(by='leverage', ascending=False, inplace=True)
print(ass_rule)