# 1. 问题描述
有3组数据分别如下：  

![i](https://github.com/zenghang-feng/khanacademy_statistics/blob/main/75-76-方差分析1和2/pic1.png)

检验3组数据的均值是否相同？（显著性水平为10%）

# 2. 程序实现
```
import numpy as np
from scipy import stats

############################################################
# 样本数据如下
############################################################
list_1 = [3, 2, 1]
list_2 = [5, 3, 4]
list_3 = [5, 6, 7]

############################################################
# 计算样本统计量
############################################################
# 一共有3个样本组(m=3)，每个样本组的样本数为3(n=3)
m = 3
n = len(list_1)
mean_1 = np.mean(list_1)
mean_2 = np.mean(list_2)
mean_3 = np.mean(list_3)
mean_of_mean = (mean_1 + mean_2 + mean_3) / m

############################################################
# 计算总波动、组内波动、组间波动
############################################################
# 总波动及对应的自由度
sst = sum([(list_1[i] - mean_of_mean)**2 + (list_2[i] - mean_of_mean)**2 + (list_3[i] - mean_of_mean)**2 for i in range(n)])
dof_t = m * n - 1
# 组内波动及对应的自由度
ssw = sum([(list_1[i] - mean_1)**2 + (list_2[i] - mean_2)**2 + (list_3[i] - mean_3)**2 for i in range(n)])
dof_w = m * (n - 1)
# 组间波动及对应的自由度
ssb = n * ((mean_1 - mean_of_mean)**2 + (mean_2 - mean_of_mean)**2 + (mean_3 - mean_of_mean)**2)
dof_b = m - 1

############################################################
# 进行假设检验，显著性水平为10%
############################################################
# 原假设：3组数据的均值没有差异
# 备择假设，3组数据的均值存在差异
f = (ssb / dof_b) / (ssw / dof_w)
# 显著性水平为0.1，分子自由度为2，分母自由度为6，查表可得f统计量的取值为3.46
# 计算得到的f统计量为12，12 > 3.46，所以拒绝原假设

############################################################
# 进行假设检验，显著性水平为10%（简单实现单因素方差分析）
############################################################
res = stats.f_oneway(list_1, list_2, list_3)
# p值为0.008，所以拒绝原假设
# https://docs.scipy.org.cn/doc/scipy/reference/generated/scipy.stats.f_oneway.html#scipy.stats.f_oneway
```

# 3. 参考：显著性水平为0.1的F表
![i](https://github.com/zenghang-feng/khanacademy_statistics/blob/main/77-方差分析F统计量假设检验/pic_f_分布.png)
