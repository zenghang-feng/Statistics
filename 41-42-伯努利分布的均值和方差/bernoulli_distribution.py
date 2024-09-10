# 伯努利分布的示例：取值为0的概率等于0.4，取值为一的概率等于0.6
mean = 0.4 * 0 + 0.6 * 1
var = 0.4 * ((0-mean)**2) + 0.6 * ((1-mean)**2)
print("均值：", mean)
print("方差：", var)

# 伯努利分布的均值和方差的一般情况：取值为0的概率等于1-p，取值为一的概率等于p
p = 0.6
mean_theory = (1-p) * 0 + p * 1
# 化简后 mean_theory = p

var_theory = (1-p) * ((0-p)**2) + p * ((1-p)**2)
# 化简后 var_theory = pq
