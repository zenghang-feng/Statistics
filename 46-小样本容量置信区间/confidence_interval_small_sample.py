import numpy as np

# 采样结果如下：
samples = [1.5, 2.9, 0.9, 3.9, 3.2, 2.1, 1.9]
sample_nums = len(samples)

# 计算样本的均值和标准差
mean_sample = np.mean(samples)
std_sample = np.std(samples, ddof=1)

# 由于样本容量为7，小于30，此时抽样分布是t分布
# 用样本的标准差作为总体标准差的无偏估计，并用总体标准差计算抽样分布的标准差
std_sample_population = std_sample
std_sample_dis = std_sample_population / (sample_nums**0.5)

# 查询t分布对应的Z分数表格，自由度为7-1=6，95%的置信区间对应得到Z分数如下
z_score = 2.447
mean_population_low = mean_sample - z_score * std_sample_dis
mean_population_up = mean_sample + z_score * std_sample_dis
