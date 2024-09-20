############################################################
# 样本信息：
############################################################
sample_nums = 1000
pos_1 = 642
pos_2 = 591

############################################################
# 计算样本均值和方差：
############################################################
p1_sample_sample = pos_1 / sample_nums
p2_sample_sample = pos_2 / sample_nums
# 用抽样分布样本的方差作为抽样分布总体方差的无偏估计
var1_sample_sample = p1_sample_sample * (1-p1_sample_sample) / sample_nums
var2_sample_sample = p2_sample_sample * (1-p2_sample_sample) / sample_nums

############################################################
# 构建置信水平为95的置信区间
############################################################
# 计算均值之差的抽样分布的均值和方差
dif_p = p1_sample_sample - p2_sample_sample
dif_var = var1_sample_sample + var1_sample_sample
# 对于均值之差的抽样分布：用样本方差作为总体方差的无偏估计,可得标准差
dif_std = dif_var ** 0.5
# 查表可得95%的概率对应的Z值为1.96
z_score = 1.96
ci_low = dif_p - z_score * dif_std
ci_up = dif_p + z_score * dif_std
# 可得95%的置信区间为 （0.009， 0.093）
