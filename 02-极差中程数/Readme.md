```
import numpy as np

# 需要计算的数据列表
list_nums = [65, 81, 73, 85, 94, 79, 67, 83, 82]

############################################################
# 计算极差、中程数：简单实现
############################################################
# range = np.ptp(list_nums)
num_max = max(list_nums)
num_min = min(list_nums)
range = num_max - num_min
mid_range = (num_max+num_min) / 2

# 打印计算得到的极差、中程数
print("极差是：", range)
print("中程数是：", mid_range)

############################################################
# 计算极差、中程数：基本实现
############################################################
num_max = list_nums[0]
num_min = list_nums[0]
for num in list_nums:
    if num > num_max:
        num_max = num
    if num < num_min:
        num_min = num
range = num_max - num_min
mid_range = (num_max+num_min) / 2


# 打印计算得到的极差、中程数
print("极差是：", range)
print("中程数是：", mid_range)
```
