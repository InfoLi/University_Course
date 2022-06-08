import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import mean_squared_error, f1_score, recall_score, roc_curve
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn import metrics



data = pd.read_csv(r'./audit_risk.csv')
# 缺失值处理-零值补充
# print(data.isnull().sum())
data = data.fillna(0)
# 异常值处理（描述性变量转换为数值）
cols = data.columns.tolist()
for col in cols:
    if data[col].dtype == 'object':
        for i in range(len(data[col])):
            if isinstance(data[col][i],str):
                data[col][i] = 0

# 数据划分
x = data.iloc[:,:26]
y = data.iloc[:,26]
train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.2)

# 数据标准化
ss = preprocessing.StandardScaler()
ss_train_x = ss.fit_transform(train_x)
ss_test_x = ss.fit_transform(test_x)

def evaluate(test_y, predict_y):
    f1 = f1_score(test_y, predict_y, average='micro')
    acc = accuracy_score(test_y, predict_y)
    recall = recall_score(test_y, predict_y, average='macro')
    con_matr = confusion_matrix(test_y, predict_y)
    tn, fp, fn, tp = con_matr.ravel()
    print(f"准确率={acc},f1均值={f1},召回率={recall}")
    print(f"混淆矩阵=\n{con_matr}")
    print(f"真阳率(TPR)={tp / (tp + fn)},假阳率(FPR)={tn / (tn + fp)}")

    plt.figure()
    fpr, tpr, thresholds = roc_curve(test_y, test_y)
    plt.plot(fpr, tpr, label='ROC')
    plt.show()


# 分类决策树模型
dtc = DecisionTreeClassifier()
dtc.fit(ss_train_x, train_y)
predict_y = dtc.predict(ss_test_x)
# 评分
print("mean_squared_error:", mean_squared_error(test_y, predict_y))
evaluate(test_y, predict_y)
# 混淆矩阵
CM = confusion_matrix(test_y, predict_y)
print(CM)





# SVM分类模型
svc = SVC()
svc.fit(ss_train_x, train_y)
predict_y = svc.predict(ss_test_x)
# 评分
print("mean_squared_error:", mean_squared_error(test_y, predict_y))
evaluate(test_y, predict_y)
# 混淆矩阵
CM = confusion_matrix(test_y, predict_y)
print(CM)




# KNN分类模型
knn = KNeighborsClassifier()
knn.fit(ss_train_x, train_y)
predict_y = knn.predict(ss_test_x)
# 评分
print("mean_squared_error:", mean_squared_error(test_y, predict_y))
evaluate(test_y, predict_y)
# 混淆矩阵
CM = confusion_matrix(test_y, predict_y)
print(CM)


