import numpy as np
from scipy import stats


# 需要计算的数据列表
############################################################
list_nums = [3, 3, 3, 3, 3, 100]

############################################################
# 计算均值、中位数、众数：简单的实现方式
############################################################
mean = np.mean(list_nums)
median = np.median(list_nums)
mode = stats.mode(list_nums)[0]

print("均值是：", mean)
print("中位数是：", median)
print("众数是：", mode)

# 一些情况下样本均值不能较好地反映出数据的集中趋势