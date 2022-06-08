from sklearn.linear_model import LinearRegression as LR
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error as MSE
from sklearn.metrics import mean_absolute_error as MAE
from sklearn.metrics import r2_score
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

houseData = pd.read_csv(r'F:\python\大数据分析实验课\exec_1\data\boston.csv')

# 填充空值
for i in houseData.columns:
    houseData.loc[:, i] = houseData[i].fillna(0)

# 特征选择
y = houseData['MEDV']
# 相关性分析
r = houseData.corr()
# 绘制热力图
# sns.heatmap(r, annot=True)
# plt.savefig("./r.png")
# plt.show()

rMEDV = r.loc['MEDV']
rMEDV.drop('MEDV', axis=0, inplace=True)
for i in rMEDV:
    # 删除次要特征
    if -0.5 < i < 0.5:
        row = rMEDV.loc[rMEDV == i]
        houseData.drop(row.index[0], axis=1, inplace=True)
houseData.drop('MEDV', axis=1, inplace=True)

# 绘制散点图
for i in houseData.columns:
    x = houseData[i]
#     plt.figure()
#     plt.scatter(x, y)
# plt.show()

# 数据归一化
for i in houseData.columns:
    houseData[i] = (houseData[i] - houseData[i].min()) / (houseData[i].max() - houseData[i].min())

# 训练
Xtrain, Xtest, Ytrain, Ytest = train_test_split(houseData, y, test_size=0.3)
reg = LR().fit(Xtrain, Ytrain) #
# 预测
print('-'*20+'线性回归'+'-'*20)
yhat1 = reg.predict(Xtest)
print(f'线性回归MSE={MSE(yhat1, Ytest)}')
print(f'线性回归MAE={MAE(yhat1, Ytest)}')
print(f'线性回归R2={r2_score(yhat1, Ytest)}')
plt.figure('线性回归')
plt.scatter(yhat1, Ytest)
plt.plot(list(range(40)),list(range(40)))

print('-'*20+'岭回归'+'-'*20)
ridge =Ridge().fit(Xtrain,Ytrain)
yhat2 = ridge.predict(Xtest)
print(f'岭回归MSE={MSE(yhat2, Ytest)}')
print(f'岭回归MAE={MAE(yhat2, Ytest)}')
print(f'岭回归R2={r2_score(yhat2, Ytest)}')
plt.figure('岭回归')
plt.scatter(yhat2, Ytest)
plt.plot(list(range(40)),list(range(40)))


# 套索回归
print('-'*20+'套索回归'+'-'*20)
lasso=Lasso().fit(Xtrain,Ytrain)
yhat3 = ridge.predict(Xtest)
print(f'套索回归MSE={MSE(yhat3, Ytest)}')
print(f'套索回归MAE={MAE(yhat3, Ytest)}')
print(f'套索回归R2={r2_score(yhat3, Ytest)}')
plt.figure('套索回归')
plt.scatter(yhat3, Ytest)
plt.plot(list(range(40)),list(range(40)))

plt.figure('汇总比较')
plt.plot(list(range(len(yhat3))), yhat1 - Ytest)
plt.plot(list(range(len(yhat3))), yhat2 - Ytest)
plt.plot(list(range(len(yhat3))), yhat3 - Ytest)
plt.legend(['线性回归', '岭回归', '套索回归'])

plt.show()
