```
import numpy as np

# 需要计算的数据列表
############################################################
list_nums = [2, 2, 3, 3]
mean = np.mean(list_nums)

############################################################
# 计算样本方差：简单的实现方式
############################################################
sample_variance = np.var(list_nums, ddof=1)                     # 除以样本数量-1
print("样本方差是：", sample_variance)

############################################################
# 计算样本方差：基础的实现方式
############################################################
dif_sqrt = 0
count_num = 0
for num in list_nums:
    dif_sqrt = dif_sqrt + (num-mean)**2
    count_num = count_num + 1
sample_variance = dif_sqrt / (count_num-1)                      # 除以样本数量-1

print("样本方差是：", sample_variance)
```
