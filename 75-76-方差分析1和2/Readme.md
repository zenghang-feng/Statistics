# 1. 问题描述
有3组数据分别如下： 

![i](https://github.com/zenghang-feng/khanacademy_statistics/blob/main/75-76-方差分析1和2/pic1.png)

可以计算上述数据总的波动，组间波动，组内波动：  

# 2. 程序实现
```
import numpy as np

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
```
