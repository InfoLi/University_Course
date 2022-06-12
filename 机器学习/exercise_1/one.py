import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time

# np.random.seed(777)  # 随机数种子


class LinearRegression:
    def __init__(self):
        self.w = None
        self.n_features = None

    def fit1(self, X, y):
        # 《机器学习》公式3.7,3.8
        # assert isinstance(X, np.ndarray) and isinstance(y, np.ndarray)
        assert X.ndim == 2 and y.ndim == 1
        assert y.shape[0] == X.shape[0]
        assert X.shape[1] <= 1
        X = X.squeeze()
        x_mean = np.mean(X)
        y_mean = np.mean(y)
        xy_mean = np.mean(X * y)
        xx_mean = np.mean(X * X)
        w = ((x_mean * y_mean) - xy_mean) / (x_mean ** 2 - xx_mean)
        b = y_mean - w * x_mean
        self.w = [w, b]

    def fit2(self, X, y):
        # 《机器学习》公式3.11
        # assert isinstance(X, np.ndarray) and isinstance(y, np.ndarray)
        assert X.ndim == 2 and y.ndim == 1
        assert y.shape[0] == X.shape[0]
        n_samples = X.shape[0]
        self.n_features = X.shape[1]
        extra = np.ones((n_samples,))
        X = np.c_[X, extra]
        if self.n_features < n_samples:
            self.w = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
        else:
            raise ValueError('dont have enough samples')

    def predict(self, X):
        n_samples = X.shape[0]
        extra = np.ones((n_samples,))
        X = np.c_[X, extra]
        if self.w is None:
            raise RuntimeError('cant predict before fit')
        y_ = X.dot(self.w)
        return y_

    def func(self):
        print('func start')
        time.sleep(1)
        print('func end')


if __name__ == '__main__':

    t = time.time()
    # 提取数据
    file = pd.read_csv('train.csv')
    # x = np.arange(999)
    x = np.array(file['year'][1:1000])
    x = x.reshape(999,1)
    y = file['buildingSize'][1:1000]

    # X = 2 * np.random.rand(100, 1)
    # y = (4 + 3 * X + np.random.randn(100, 1)).squeeze()  # 为了模拟真实存在误差的场景，我们对 y 加上一个[0,1)范围内的误差
    lr = LinearRegression()
    lr.func()   #计时函数
    lr.fit1(x,y)  # 公式一训练模型
    # lr.fit2(x,y)  # 公式二训练模型
    X_new = np.array([[1900], [2030]])  # 我们画出模型在 0 到 2 区间内的值
    y_predict = lr.predict(X_new)  # 预测的端点值
    plt.scatter(x,y)
    plt.plot(X_new, y_predict, "r-")  # 画出模型拟合的结果
    print(f'coast:{time.time() - t:.4f}s')
    plt.show()
