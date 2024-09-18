```
import numpy as np
import matplotlib.pyplot as plt

############################################################
# 定义一个求阶乘的函数
############################################################
def factorial(n):
    """
    :param n: 大于等于0的整数
    :return: 是输入参数n的阶乘，一个正整数
    """
    res = 1
    if n == 0:
        return res
    else:
        for i in range(1, n+1):
            res = res * i
        return res

############################################################
# 构建函数模拟二项分布
############################################################
def binomial_distribution(n, p):
    """
    :param n: 实验次数，是一个正整数
    :param p: 每一次实验成功的概率，取值为0-1之间的小数
    :return: 存储实验成功次数对应的概率的列表（成功次数为列表的各个索引）
    """
    list_x = [(factorial(n) / factorial(i) / factorial(n-i)) * np.power(p, i) * np.power(1-p, n-i) for i in
              range(n+1)]
    return list_x

############################################################
# 绘制二项分布的概率分布图
############################################################
list_x = binomial_distribution(6, 0.5)
# 可以设置不同的n和p进行测试
fig, ax = plt.subplots()
rects1 = ax.bar(range(len(list_x)), list_x)
plt.show()

############################################################
# 随机变量的期望值
############################################################
mean = 0
for i, r in enumerate(list_x):
    mean = mean + i * r
print("二项分布的均值是：", mean)

```
