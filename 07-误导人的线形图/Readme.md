```
import matplotlib.pyplot as plt

# 需要可视化的数据
years = [2006, 2007, 2008, 2009, 2010, 2011]
precent_1 = [0.8, 0.76, 0.77, 0.73, 0.73, 0.68]
precent_2 = [0.12, 0.19, 0.19, 0.20, 0.21, 0.25]

# 创建折线图
fig, ax = plt.subplots(1,2)
ax[0].set_ylim(0.5, 1)                                  # 设置坐标轴范围
ax[0].grid(True)                                        # 设置图像背景中的网格
ax[0].plot(years, precent_1, "bs-")
ax[1].set_ylim(0, 0.3)
ax[1].grid(True)
ax[1].plot(years, precent_2, "gs-")

# 添加标题、坐标轴等信息
ax[0].set_title("Percentage of Peple Who Prefer Yummy Cola")
ax[1].set_title("Percentage of Peple Who Prefer Thrill Soda")

# 显示图像
plt.show()
```
