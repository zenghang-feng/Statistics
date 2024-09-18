```
import numpy as np

import numpy as np

# 需要计算的数据列表
############################################################
list_nums = [1, 2, 3, 8, 7]
mean = np.mean(list_nums)

############################################################
# 计算总体标准差：简单的实现方式
############################################################
standard_deviation = np.std(list_nums)
print("总体标准差是：", standard_deviation)

############################################################
# 计算总体标准差：基础的实现方式
############################################################
dif_sqrt = 0
count_num = 0
for num in list_nums:
    dif_sqrt = dif_sqrt + (num-mean)**2
    count_num = count_num + 1
standard_deviation = (dif_sqrt / count_num) ** 0.5

print("总体标准差是：", standard_deviation)
# 样本的标准差等于样本方差开平方
```
