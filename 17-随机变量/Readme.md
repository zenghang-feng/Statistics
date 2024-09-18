```
import numpy as np

# 模拟投掷骰子，可以改变列表中的数字模拟是否均匀的骰子
population = [1, 2, 3, 4, 5, 6]

# list_count记录每次采样得到的数字的出现次数
list_count = [0] * 6

# 采样1200次：每次从总体中随机取1个元素
sample_frequency = 120000
for i in range(sample_frequency):
    sample = np.random.choice(population, 1)
    num = sample[0]
    list_count[num-1] = list_count[num-1] + 1

# 打印随机变量各个取值出现的频率
list_rate = [freq / sample_frequency for freq in list_count]
for i, r in enumerate(list_rate):
    print(i+1 , "出现的频率是", r)

# 均匀骰子上每个数字采样得到的频率大概是六分之一
```
