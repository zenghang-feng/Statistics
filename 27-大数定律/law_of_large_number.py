import numpy as np
import pandas as pd

# 模拟：一次试验投掷100枚均匀的硬币，得到正面向上的次数（1代表正面向上）
list_01 = [0] * 100 + [1] * 100

# 进行一万次采样，每次样本为50，记录每次采样的均值
trail_nums = 10000
sample_size = 2
list_sample = []
for i in range(trail_nums):
    list_tmp = []
    for j in range(sample_size):
        list_tmp.append(sum(np.random.choice(a=list_01,size=100)))
    list_sample.append(np.mean(a=list_tmp))

mean = np.mean(a=list_sample)
print("最终的均值是：", mean)
# 采样均值趋于随机变量的均值