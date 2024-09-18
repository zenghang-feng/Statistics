```
import numpy as np

# 需要计算的数据列表
############################################################
list_nums = [2, 2, 3, 3]
mean = np.mean(list_nums)

############################################################
# 计算总体方差：诸方差公式
############################################################
dif_sqrt = 0
count_num = 0
for num in list_nums:
    dif_sqrt = dif_sqrt + num**2
    count_num = count_num + 1
population_variance = (dif_sqrt / count_num) - (mean ** 2)

print("总体方差是：", population_variance)
```
