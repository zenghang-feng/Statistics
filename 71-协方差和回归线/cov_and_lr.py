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
m = (xy_mean - x_mean * y_mean) / (xx_mean - x_mean ** 2)
b = y_mean - m * x_mean

# 可得最佳拟合曲线为：y = 0.976 * x - 0.238

############################################################
# 计算样本数据中x，y的协方差
############################################################
def cov_2d(l1, l2, ddof):
    """
    :param l1: 1维数组或者列表
    :param l2: 1维数组或者列表
    :param ddof: 自由度数值，是一个正整数
    :return: 协方差数值
    """
    mean_1 = np.mean(l1)
    mean_2 = np.mean(l2)
    length = len(l1)
    s = 0
    for i in range(length):
        s = s + (l1[i] - mean_1)*(l2[i]-mean_2)

    cov = s / (length - ddof)
    return cov

cov_xy = cov_2d(l1=list_x, l2=list_y, ddof=0)
numerator = (xy_mean - x_mean * y_mean)

cov_xx = cov_2d(l1=list_x, l2=list_x, ddof=0)
denominator = (xx_mean - x_mean ** 2)