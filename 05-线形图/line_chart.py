import matplotlib.pyplot as plt

# 需要可视化的数据
months = ["July", "August", "September", "October", "November", "December", "January", "February", "March", "April", "May", "June" ]
prices = [10.2, 11.2, 10.3, 12.1, 12.8, 12.2, 13.3, 13.5, 16.8, 15.2, 15.88, 16.7]

# 创建折线图
fig, ax = plt.subplots()
ax.set_ylim(0, 18)                              # 设置坐标轴范围
ax.grid(True)                                   # 设置图像背景中的网格
ax.plot(months, prices, "bs-")

# 添加标题、坐标轴等信息
plt.xlabel("Month")
plt.ylabel("Pricec($)")
plt.title("Price of Stock Share, July 2010-June 2011")

# 显示图像
plt.show()

# 参考：https://geek-docs.com/matplotlib/matplotlib-top-tutorials/1006100_matplotlib_simple_plot.html#google_vignette