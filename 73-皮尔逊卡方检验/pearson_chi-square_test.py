from scipy import stats

############################################################
# 样本数据
############################################################
sample_1 = [10, 10, 15, 20, 30, 15]
sample_2 = [30, 14, 34, 45, 57, 20]

############################################################
# 假设检验：显著性水平为5%
############################################################
# 原假设：两次采样的数据符合同一个分布
# 备择假设：两次采样的数据不符合同一个分布
sample_1_sum = sum(sample_1)
sample_2_sum = sum(sample_2)
sample_nums = len(sample_1)
expected = [sample_2_sum * sample_1[i] / sample_1_sum for i in range(sample_nums)]

# 用卡方分布进行近似计算
chi_square = sum([(sample_2[i] - expected[i]) ** 2 / expected[i] for i in range(sample_nums)])
dof = sample_nums - 1           # 自由度为5
# 查表可得在自由度为5，显著性水平为5%的情况下，卡方统计量的临界值为11.07
# 计算得到的卡方统计量为11.44，11.44 > 11.07，所以拒绝原假设


############################################################
# 假设检验：显著性水平为5%(简单实现)
############################################################
res = stats.chisquare(f_obs=sample_2, f_exp=expected, ddof=dof)
# https://docs.scipy.org.cn/doc/scipy/reference/generated/scipy.stats.chisquare.html#scipy.stats.chisquare