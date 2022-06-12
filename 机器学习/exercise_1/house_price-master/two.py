import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

np.random.seed(777)  # 随机数种子


class LogisticRegression:
    def __init__(self, max_iter=100, use_matrix=True):
        self.beta = None  # 权重
        self.n_features = None  # 特征数量
        self.max_iter = max_iter  # 迭代次数
        self.use_Hessian = use_matrix
        """
        是否使用 Hessian 矩阵,若为True则为使用Hessian 矩阵，     
        采用牛顿法求解时需要计算hessian矩阵，
        而用拟牛顿法时，每一步使用梯度向量更新hessian矩阵的近似，就可以不使用hessian矩阵 
        """

    def fit(self, X, y):
        n_samples = X.shape[0]
        self.n_features = X.shape[1]
        extra = np.ones((n_samples,))
        X = np.c_[X, extra]
        self.beta = np.random.random((X.shape[1],))
        for i in range(self.max_iter):  # 迭代 max_iter 次进行权重更新
            if self.use_Hessian is not True:
                dldbeta = self._dldbeta(X, y, self.beta)
                dldldbetadbeta = self._dldldbetadbeta(X, self.beta)
                self.beta -= (1. / dldldbetadbeta * dldbeta)
            else:
                dldbeta = self._dldbeta(X, y, self.beta)
                dldldbetadbeta = self._dldldbetadbeta_matrix(X, self.beta)
                self.beta -= (np.linalg.inv(dldldbetadbeta).dot(dldbeta))

    @staticmethod
    def _dldbeta(X, y, beta):
        # 《机器学习》公式 3.30
        m = X.shape[0]
        sum = np.zeros(X.shape[1], ).T
        for i in range(m):
            sum += X[i] * (y[i] - np.exp(X[i].dot(beta)) / (1 + np.exp(X[i].dot(beta))))
        return -sum

    @staticmethod
    def _dldldbetadbeta_matrix(X, beta):
        m = X.shape[0]
        Hessian = np.zeros((X.shape[1], X.shape[1]))  # 生成一个n阶Hessian矩阵，此处为3阶
        for i in range(m):
            p1 = np.exp(X[i].dot(beta)) / (1 + np.exp(X[i].dot(beta)))
            tmp = X[i].reshape((-1, 1))
            Hessian += tmp.dot(tmp.T) * p1 * (1 - p1)
        return Hessian

    @staticmethod
    def _dldldbetadbeta(X, beta):
        # 《机器学习》公式 3.31
        m = X.shape[0]
        sum = 0.
        for i in range(m):
            p1 = np.exp(X[i].dot(beta)) / (1 + np.exp(X[i].dot(beta)))
            sum += X[i].dot(X[i].T) * p1 * (1 - p1)
        return sum

    def predict_proba(self, X):
        n_samples = X.shape[0]
        extra = np.ones((n_samples,))
        X = np.c_[X, extra]
        if self.beta is None:
            raise RuntimeError('cant predict before fit')
        p1 = np.exp(X.dot(self.beta)) / (1 + np.exp(X.dot(self.beta)))
        p0 = 1 - p1
        return np.c_[p0, p1]

    def predict(self, X):
        p = self.predict_proba(X)
        res = np.argmax(p, axis=1)  # 返回 p 的第二维中最大值的索引，即预测的标签
        return res


if __name__ == '__main__':
    breast_data = load_breast_cancer()  # 乳腺癌诊断数据集
    # print(breast_data.DESCR)  # 打印数据集的具体信息
    """
   此处每个样本取前2个特征（便于可视化）以及对应的标签
   同学们可在数据集的30个特征里自行选择特征
   """
X, y = breast_data.data[:, 2:6], breast_data.target
# print(X.shape)  # (569, 2)

X = MinMaxScaler().fit_transform(X)  # 归一化
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)  # 取30%作为测试集

logisticreg = LogisticRegression(max_iter=100, use_matrix=True)
logisticreg.fit(X_train, y_train)  # 训练模型

lda_prob = logisticreg.predict_proba(X_test)  # 模型在测试集上对两种类别预测的概率，两种概率的和为1
lda_pred = logisticreg.predict(X_test)  # 模型在测试集上的预测结果，即取概率最大的作为预测结果
# print('logistic_prob:', lda_prob)
# print('logistic_pred:', lda_pred)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)  # 取30%作为测试集
logisticreg = LogisticRegression(max_iter=100,use_matrix=True)

logisticreg.fit(X_train,y_train)    #训练模型

lda_prob = logisticreg.predict_proba(X_test)  # 模型在测试集上对两种类别预测的概率，两种概率的和为1
lda_pred = logisticreg.predict(X_test)  # 模型在测试集上的预测结果，即取概率最大的作为预测结果



print('accuracy:', len(y_test[y_test == lda_pred]) * 1. / len(y_test))  # 计算准确率

# 可视化
x_ponits = np.array([0.1, 0.8])
y_ = -(logisticreg.beta[0] * x_ponits + logisticreg.beta[2]) / logisticreg.beta[1]
# 设置图名属性
plt.title("LogisticRegression", fontsize='large', fontweight='bold', color='b')

# 设置坐标轴属性
font = {'family': 'Times New Roman', 'weight': 'normal', 'size': 12}
plt.xlabel(breast_data.feature_names[2], font)  # x轴标签
plt.ylabel(breast_data.feature_names[3], font)  # y轴标签

plt.plot(x_ponits, y_)
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()