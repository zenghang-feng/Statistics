# 1. 问题描述
有2种预防流感的药物，为了检验2种药物预防流感的效果，设置了3组实验，第一组服用药物1，第二组服用药物2，第3组服用安慰剂， 

3组实验的数据如下：  

----	   药物1	   药物2	   安慰剂  

--患病	     20	            30	           30  

未患病       100	           110	           90  

请检验2种药物对于预防流感是否有效果？（显著性水平为10%）

# 2. 程序实现
```
import numpy as np
from scipy import stats

############################################################
# 样本数据
############################################################
samples = [(20, 100), (30, 110), (30, 90)]

############################################################
# 假设检验：显著性水平为5%
############################################################
# 原假设：药物没有效果
# 备择假设：药物有效果
sicks = [s[0] for s in samples]
not_sicks = [s[1] for s in samples]
totals = [s[0] + s[1] for s in samples]
sick_sum = sum(sicks)
not_sick_sum = sum(not_sicks)
total_sum = sum(totals)
p_sick = sick_sum / total_sum
p_not_sick = not_sick_sum / total_sum

sample_nums = len(sicks)
sicks_exp = [s * p_sick for s in totals]
not_sicks_exp = [totals[i] - sicks_exp[i] for i in range(sample_nums)]

# 用卡方分布近似来做假设检验，计算卡方统计量
chi_square = sum([(sicks[i] - sicks_exp[i]) ** 2 / sicks_exp[i] + (not_sicks[i] - not_sicks_exp[i]) ** 2 / not_sicks_exp[i] for i in range(sample_nums)])
dof = (sample_nums - 1) * (2 - 1)
# # 查表可得在自由度为2，显著性水平为10%的情况下，卡方统计量的临界值为4.6
# 计算得到的卡方统计量为2.53，2.53 < 4.6，所以不能拒绝原假设

############################################################
# 假设检验：显著性水平为5%(简单实现)
############################################################
res = stats.chi2_contingency(np.array([sicks, not_sicks]))
# p值为0.28，所以不能拒绝原假设
# https://docs.scipy.org.cn/doc/scipy/reference/generated/scipy.stats.chi2_contingency.html#scipy.stats.chi2_contingency
```
