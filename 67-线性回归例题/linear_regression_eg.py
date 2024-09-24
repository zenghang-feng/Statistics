import numpy as np

# 样本数据如下：
list_samples = [(1, 2), (2, 1), (4, 3)]
list_x = [s[0] for s in list_samples]
list_y = [s[1] for s in list_samples]
list_xx = [s[0] ** 2 for s in list_samples]
list_xy = [s[0] * s[1] for s in list_samples]

# 计算样本统计量
x_mean = np.mean(list_x)
y_mean = np.mean(list_y)
xx_mean = np.mean(list_xx)
xy_mean = np.mean(list_xy)

# 计算参数m、b
m = (xy_mean - x_mean * y_mean) / (xx_mean - x_mean ** 2)
b = y_mean - m * x_mean

# 可得最佳拟合曲线为：y = 0.43 * x + 1
