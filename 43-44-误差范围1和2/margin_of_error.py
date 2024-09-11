# 假设有0-1分布，取值为1的概率等于p，取值为0的概率等于1-p
# 对上述0-1分布进行采样，样本容量为100，取值为0的数量为57，取值为1的数量为43
mean_sample = (57 * 0 + 43 * 1) / 100
var_sample = (57 * ((0-mean_sample)**2) + 43 * ((1-mean_sample)**2)) / (100 - 1)
std_sample = var_sample ** 0.5

# 用样本的标准差作为总体标准差的无偏估计，并用总体标准差计算抽样分布的标准差
std_population = std_sample
std_sample_dis = std_population / (100 ** 0.5)

# 样本均值位于抽样分布均值左右2个标准差的概率等于95.4%，等价于抽样分布均值距离样本均值左右2个标准差的概率等于95.4%
# 同时，抽样分布的均值等于总体均值，所以可以构造95%的置信区间如下：0.43±(2*std_sample_dis)
mean_population_low = 0.43 - 2*std_sample_dis
mean_population_up = 0.43 + 2*std_sample_dis

# 如果要估计的结果更准确，可以增加采样的样本容量，那么抽样分布的标准差会变小，构造的区间相应也会更小



