from torchvision import datasets, transforms
import torch.nn as nn
import torch
from model import LeNet
import os

lr = 0.001
batch_size = 64
train_epoch = 10

def main():
    # 创建模型 #
    model = LeNet()

    # 定义数据集与dataloader
    train_set = datasets.MNIST('./data', train=True, download=True,    # 继承自torch.utils.data.Dataset类，                                                                     
                        transform = transforms.Compose([                 # 实现__len__和__getitem__方法可以
                            transforms.Resize((32, 32)),                 # 制作自己的数据集
                            transforms.ToTensor()
                        ]))

    val_set = datasets.MNIST('./data', train=False,
                        transform=transforms.Compose([                 # transform 对数据进行批量预处理
                            transforms.Resize((32, 32)),                 # 更改到统一大小，并变成Tensor数据类型
                            transforms.ToTensor()
                        ]))

    train_loader = torch.utils.data.DataLoader(train_set, batch_size=batch_size, shuffle=True) 
    val_loader = torch.utils.data.DataLoader(val_set, batch_size=batch_size, shuffle=False) # 图片，label迭代器

    # 用于打印信息和计算精度
    steps_per_epoch = len(train_loader)
    testnum = len(val_loader.dataset)

    # 定义损失函数，优化器
    criterion = nn.CrossEntropyLoss(reduce=True)    # pytorch中损失函数也继承自nn.Module，即可以将其看作一个层，
                                                      # 实现其forward方法即可自己编写损失函数。 
    # 随机梯度下降 (stochastic gradient descent) 优化器
    optimizer = torch.optim.SGD(params=model.parameters(), lr=lr, momentum=0.9)     

    # 开始训练
    print("start training!")
    for epoch in range(train_epoch):
        for i, (inputData, target) in enumerate(train_loader):          # 从data_loader取出数据
            model.zero_grad()                                           # 每轮训练将上轮梯度置0
            output = model(inputData)                                   # 将数据输入到模型
            loss = criterion(output, target)                            # 计算损失
            loss.backward()                                             # 反向传播
            optimizer.step()                                            # 迭代优化器，更新参数

            if i % 100 == 0:
                print('Epoch [{}/{}], Step [{}/{}], LR {:.1e}, Loss: {:.4f}'
                      .format(epoch, train_epoch, str(i).zfill(3), str(steps_per_epoch).zfill(3), lr, loss.item()))
        # 开始测试
        model.eval()                                                    # 主要作用在Batch Normalization和Dropout层，
        correct = 0                                                       # 进行测试时不使用相关操作
        with torch.no_grad():                                           # 不进行反向传播，不记录梯度信息
            for i, (inputData, target) in enumerate(val_loader):        # 从验证集取得数据
                output = torch.softmax(model(inputData), dim=0)         # 对输出进行softmax
                pred = output.argmax(dim=1, keepdim=True)               # 取到标签
                correct += pred.eq(target.view_as(pred)).sum().item()   # 计算标签正确的数目
        acc = 100.0 * correct / testnum
        print('\nTest set: Accuracy: {}/{} ({:.3f}%)\n'.format(correct, testnum, acc))

        try:
            torch.save(model.state_dict(), os.path.join(                # 保存最后一轮的模型
                'models/', 'LeNet.ckpt'))
        except:
            pass

        model.train()                                                   # 返回训练，启用Batch Normalization和Dropout层

if __name__ == '__main__': # 与keras相比，Pytorch中的模块更简洁，需要指定的参数更少，这是因为keras将正则、激活操作集成到了对应的网络结构中，但torch中需要自行定义这些操作。同时
    main()