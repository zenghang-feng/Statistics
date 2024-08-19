import numpy as np
from scipy import stats


# 需要计算的数据列表
############################################################
list_nums = [23, 29, 20, 32, 23, 21, 33, 25]

############################################################
# 计算均值、中位数、众数：简单的实现方式
############################################################
mean = np.mean(list_nums)
median = np.median(list_nums)
mode = stats.mode(list_nums)[0]

# print("均值是：", mean)
# print("中位数是：", median)
# print("众数是：", mode)
############################################################
# 计算均值、中位数、众数：基本的实现方式
############################################################
# 计算均值 ==================================================
total = 0
count_nums = 0
for num in list_nums:
    total += num
    count_nums += 1
if count_nums > 0:
    mean = total / count_nums
else:
    mean = 0

# 计算中位数 ================================================
def quick_sort(list_nums):
    """
    :param list_nums: 需要排序的数据列表
    :return: 排序后的数据列表
    """
    length = len(list_nums)
    if length <= 1:
        return list_nums
    else:
        piv = list_nums[0]
        left_nums = [num for num in list_nums[1:] if num <= piv]
        right_nums = [num for num in list_nums[1:] if num > piv]
        return quick_sort(left_nums) + [piv] + quick_sort(right_nums)

list_nums_sort = quick_sort(list_nums)
length = len(list_nums_sort)
mid_idx = int(length / 2)
if length % 2 == 1:
    median = list_nums_sort[mid_idx]
else:
    median = (list_nums_sort[mid_idx] + list_nums_sort[mid_idx-1]) / 2

# 计算众数 ===================================================
count_dit = {}
count_max = 0
mode = 0
for num in list_nums:
    if num in count_dit:
        count_dit[num] = count_dit[num] + 1
    else:
        count_dit[num] = 1
    if count_dit[num] > count_max:
        count_max = count_dit[num]
        mode = num

# 打印计算得到的均值、中位数、众数
print("均值是：", mean)
print("中位数是：", median)
print("众数是：", mode)