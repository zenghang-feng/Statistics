import numpy as np
import matplotlib.pyplot as plt

############################################################
# 5均匀的硬币同时抛出，随机变量X为正面向上的硬币数量
############################################################
# 用从列表中随机取值模拟抛硬币，0代表反面，1代正面
list_01 = [0, 1]

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
# 随机变量X的概率分布函数
############################################################
# f = np.math.factorial(6)
# list_x 存储的是随机变量X取值为0-5的理论概率
list_x = [(factorial(5)/factorial(i)/factorial(5-i)) * np.power(0.5, i) * np.power(0.5, 5-i) for i in range(6)]                             # 存储随机变量X的不同取值

############################################################
# 进行10000次模拟，观测X的取值情况
############################################################
# list_xt 存储的是在10000次随机实验中，随机变量X取值为0-5的实际频数
list_xt = [0] * 6
trail = 10000
for i in range(trail):
    tmp = 0
    for j in range(5):
        tmp = tmp + np.random.choice(list_01, 1)[0]
    list_xt[tmp] += 1
list_xtr = [xt/trail for xt in list_xt]
print("----------计算结束----------")
# 结论：随机实验的结果和理论结果的取值比较接近

############################################################
# 绘制二项分布的概率分布
############################################################
fig, ax = plt.subplots()
ax.grid(True)  # 设置图像背景中的网格
ax.plot(range(6), list_x)
plt.show()
#  当前示例下的二项分布的概率分布类似正态分布的钟形曲线