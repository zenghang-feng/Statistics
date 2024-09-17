```
import matplotlib.pyplot as plt

# 需要可视化的数据
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
sells = [18, 10, 7, 5, 5, 3, 3, 9, 7, 8, 13, 12]

# 创建折线图
fig, ax = plt.subplots()
ax.pie(sells, labels=months, autopct="%1.0f%%", counterclock=False, startangle=90, labeldistance=1.1)

# 显示图像
plt.show()

# 保存图表
# plt.savefig()

# 参考：https://www.cnblogs.com/biyoulin/p/9565350.html
```
