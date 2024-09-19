```
import numpy as np
import matplotlib.pyplot as plt


############################################################
# 定义标准正态分布的概率密度函数（pdf）
############################################################
# 也可直接调用用 scipy.stats.norm.pdf，和以下函数定义的内容相同
# mean = 0
# std = 1
def norm_distribute(x, mean, std):
    """
    :param x: 随机变量取值，是一个标量数值
    :return: 概率密度函数对应的取值，是一个标量数值
    """
    return (1 / (np.power(2 * np.pi, 0.5) * std)) * np.power(np.e, -(np.power(x - mean, 2)) / (2 * np.power(std, 2)))


############################################################
# 生成离散的自变量采样序列，并计算对应的pdf取值，绘制图像
############################################################
list_x = np.linspace(start=-20, stop=20, num=1000)
list_y = []
for x in list_x:
    list_y.append(norm_distribute(x=x, mean=0, std=4))

# 绘制pdf的图像
fig, ax = plt.subplots()
ax.grid(True)  # 设置图像背景中的网格
ax.plot(list_x, list_y)
plt.show()
```
