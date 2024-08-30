import numpy as np
import matplotlib.pyplot as plt

# 假设有离散随机变量，P(X=1)=1/3;P(X=3)=1/6;P(X=4)=1/6;P(X=6)=1/3.
# 随机变量X的均值如下：
mean = 1*(1/3) + 3*(1/6) + 4*(1/6) + 6*(1/3)
print("随机变量X的均值是：", mean)

# 对上述随机变量X进行采样，采样100000次，每次采样的样本容量为10
list_x = [1, 1, 3, 4, 6, 6]
list_sample_mean = []
sample_times = 100000                   # 采样次数
sample_nums = 10                        # 每次采样的样本容量(可以调整样本容量大小，样本容量越大，采样均值的分布越接近正态分布)
for i in range(sample_times):
    sample_tmp = []
    for j in range(sample_nums):
        sample_tmp.append(np.random.choice(a=list_x, size=1)[0])
    mean_tmp = np.mean(sample_tmp)
    list_sample_mean.append(mean_tmp)

# 绘制样本均值的分布图象
fig, ax = plt.subplots()
ax.hist(list_sample_mean, bins=8, linewidth=0.5, edgecolor="white")
plt.show()

# 中心极限定理：样本容量足够大时(n>30），样本均值(样本求和)的分布接近正态分布