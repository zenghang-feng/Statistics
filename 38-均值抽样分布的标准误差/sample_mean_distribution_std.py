import numpy as np
import matplotlib.pyplot as plt

############################################################
# 数据准备：准备一个随机分布的数据总体，绘制图像
############################################################
list_population = []
range_upper = 32
for i in range(range_upper):
    list_population = list_population + [i] * np.random.randint(low=0, high=100)

fig, ax = plt.subplots(nrows=3, ncols=1)
ax[0].hist(list_population, bins=range_upper, linewidth=0.5, edgecolor="white")
print("list_population mean =", np.mean(list_population))
print("list_population median =", np.median(list_population))
print("list_population std =", np.std(list_population))
print("---------------------------------------------------")


############################################################
# 对数据进行采样，获取多次采样的均值的抽样分布
############################################################
def sample_fun(sample_times, sample_nums):
    """
    :param sample_times: 采样次数，是一个正整数
    :param sample_nums: 每次采样的样本容量，是一个正整数
    :return: 存放均值抽样的数据，是一个列表
    """
    list_sample_mean = []  # 存放均值抽样的数据
    for i in range(sample_times):
        sample_tmp = []
        for j in range(sample_nums):
            sample_tmp.append(np.random.choice(a=list_population, size=1)[0])
        mean_tmp = np.mean(sample_tmp)
        list_sample_mean.append(mean_tmp)
    return list_sample_mean


# 第1个抽样分布 =============================================
sample_times = 1000  # 采样次数
sample_nums = 5  # 每次采样的样本容量(可以调整样本容量大小，样本容量越大，采样均值的分布越接近正态分布)
sample_1 = sample_fun(sample_times, sample_nums)
print("sample_1 mean =", np.mean(sample_1))
print("sample_1 median =", np.median(sample_1))
print("sample_1 std =", np.std(sample_1))
# 样本均值抽样分布的标准差
print("sample_1 std theory = ", np.std(list_population) / np.power(sample_nums, 0.5))
print("---------------------------------------------------")

# 第2个抽样分布 =============================================
sample_times = 1000  # 采样次数
sample_nums = 25  # 每次采样的样本容量(可以调整样本容量大小，样本容量越大，采样均值的分布越接近正态分布)
sample_2 = sample_fun(sample_times, sample_nums)
print("sample_2 mean =", np.mean(sample_2))
print("sample_2 median =", np.median(sample_2))
print("sample_2 std =", np.std(sample_2))
# 样本均值抽样分布的标准差
print("sample_2 std theory = ", np.std(list_population) / np.power(sample_nums, 0.5))


# 均值抽样分布的标准误差 = 原分布的标准误差 / sqrt(样本容量)
# 样本容量越大，样本均值的抽样分布的标准误差越小