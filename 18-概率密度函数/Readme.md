```
import numpy as np
import scipy.stats
from matplotlib import pyplot as plt
from scipy import integrate


############################################################
# 定义标准正态分布的概率密度函数（pdf）
############################################################
# 也可直接调用用 scipy.stats.norm.pdf，和以下函数定义的内容相同
# mean = 0
# std = 1
def s_norm_distribute(x):
    """
    :param x: 随机变量取值，是一个标量数值
    :return: 概率密度函数对应的取值，是一个标量数值
    """
    return (1 / (np.power(2 * np.pi, 0.5) * 1)) * np.power(np.e, -(np.power(x - 0, 2)) / (2 * np.power(1, 2)))


############################################################
# 生成离散的自变量采样序列，并计算对应的pdf取值，绘制图像
############################################################
list_x = np.linspace(-10, 10, 1000)
list_y = []
for x in list_x:
    list_y.append(s_norm_distribute(x))

# 绘制pdf的图像
fig, ax = plt.subplots()
ax.grid(True)  # 设置图像背景中的网格
ax.plot(list_x, list_y)
plt.show()

############################################################
# 参考定义的pdf，通过计算pdf的积分值，确定随机变量积分区间内对应的概率值
############################################################
prob, err = integrate.quad(func=s_norm_distribute, a=-1, b=1)
print("正负一个标准差区间内的概率是：", prob)
# 标准正态分布，正负一个标准差区间内的概率约为0.68
```

标准正态分布的概率密度函数图像如下：  
![image](https://github.com/zenghang-feng/khanacademy_statistics/blob/main/18-概率密度函数/pic1.png)
