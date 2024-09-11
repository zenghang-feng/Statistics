# 对0-1分布进行采样，采样的信息如下
sample_nums = 250
pos_nums = 142
nag_nums = sample_nums - pos_nums

# 计算样本的均值和标准差
mean_sample = (1 * pos_nums + 0 * nag_nums) / sample_nums
var_sample = (pos_nums * ((1-mean_sample)**2) + nag_nums * ((0-mean_sample)**2)) / (sample_nums - 1)
std_sample = var_sample ** 0.5

# 用样本的标准差作为总体标准差的无偏估计，并用总体标准差计算抽样分布的标准差
std_sample_population = std_sample
std_sample_dis = std_sample_population / (sample_nums**0.5)

# 构建99%的置信区间：通过查表获取Z分数(约为2.58)，然后计算区间的上下限
z_score = 2.58
mean_population_low = mean_sample - z_score * std_sample_dis
mean_population_up = mean_sample + z_score * std_sample_dis

# 如果要估计的结果更准确，可以增加采样的样本容量，那么抽样分布的标准差会变小，构造的区间相应也会更小

