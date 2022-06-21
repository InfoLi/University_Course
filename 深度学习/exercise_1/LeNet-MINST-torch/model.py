import torch.nn as nn


class LeNet(nn.Module):
    def __init__(self):
        super(LeNet, self).__init__()
        self.block1 = nn.Sequential(        # 创建一个有顺序的容器，神经网络模块按照在传入构造器的顺序依次被添加到计算图中
            nn.Conv2d(1, 6, (5, 5)),        # 第一层 卷积层 N*1*32*32 -> N*6*28*28 ((32-5+0)/1+1, padding=0, stride=1)
            nn.ReLU(),                      # 激活
            nn.MaxPool2d(2)                 # 第二层 pooling层 N*6*28*28 -> N*6*14*14 (28/2, size(2*2), stride=kernel_size)
        )
        self.block2 = nn.Sequential(
            nn.Conv2d(6, 16, (5, 5)),       # 第三层 卷积层：N*6*14*14 -> N*16*10*10
            nn.ReLU(),                      # 激活
            nn.MaxPool2d(2)                 # 第四层 pooling层：N*16*10*10 -> N*16*5*5
        )
        self.block3 = nn.Sequential(
            nn.Conv2d(16, 120, (5, 5)),     # 第五层 卷积层：N*16*5*5 -> N*120*1*1
            nn.ReLU()
        )
        self.feature = nn.Sequential(       # 打包上述层，上述层作用是特征提取
            self.block1,
            self.block2,
            self.block3
        )
        self.classify = nn.Sequential(      # 分类层，使用全连接层进行分类
            nn.Flatten(),                    # 展平：N*120*1*1 -> N*120, Flatten不影响batch size(第一维度)
            nn.Linear(120,90),
            nn.Linear(90,120),
            nn.Linear(120, 84),             # 第六层 全连接层：N*120 -> N*84
            nn.Dropout(p=0.1),              # 每次迭代以概率p 随机丢弃一些连接 -> 减少过拟合
            nn.Linear(84, 10)               # 第七层 全连接层：N*84 -> N*10
        )

    # pytorch
    def forward(self, x):
        x = self.feature(x)
        # print(x.shape)
        x = self.classify(x)
        return x

