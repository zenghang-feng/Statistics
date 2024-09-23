import numpy as np

############################################################
# 样本数据如下：
############################################################
list_samples = [(-2, -3), (-1, -1), (1, 2), (4, 3)]
list_x = [s[0] for s in list_samples]
list_y = [s[1] for s in list_samples]
list_xx = [s[0] ** 2 for s in list_samples]
list_xy = [s[0] * s[1] for s in list_samples]

############################################################
# 拟合线性回归曲线
############################################################
# 计算样本统计量
x_mean = np.mean(list_x)
y_mean = np.mean(list_y)
xx_mean = np.mean(list_xx)
xy_mean = np.mean(list_xy)

# 计算参数m、b
m = (x_mean * y_mean - xy_mean) / (x_mean ** 2 - xx_mean)
b = y_mean - m * x_mean

# 可得最佳拟合曲线为：y = 0.976 * x - 0.238

############################################################
# 线性回归拟合情况评估
############################################################
# 计算R方
se_line_sub= [(m * s[0] + b - s[1]) ** 2 for s in list_samples]
se_ymean_sub = [(s[1] - y_mean) ** 2 for s in list_samples]

se_line = sum(se_line_sub)
se_ymean = sum(se_ymean_sub)

r_sqr = 1 - (se_line / se_ymean)