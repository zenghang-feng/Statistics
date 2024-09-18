```
import numpy as np

# 每次试验成功的概率为p，进行n次重复试验，计算均值（假设试验成功随机变量取值为1）
n = 1000000
p = 0.6
bn = np.random.binomial(n=n, p=p)
mean = round(bn / n, 1)
# 二项分布的均值为 n*p，实验值和理论值基本一致（后续补充公式推导）
```
