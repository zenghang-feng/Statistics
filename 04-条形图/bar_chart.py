import numpy as np
import matplotlib.pyplot as plt

# 需要可视化的数据
student = ["Jasmine", "Jeff", "Nevin", "Alejandra", "Marta"]
score_mid = [73, 87, 83, 82, 96]
score_fin = [88, 85, 88, 94, 91]

# 配置条形图的参数
x = np.arange(len(student))  # the label locations
width = 0.35  # the width of the bars

# 创建双条形图
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, score_mid, width, label="Midterm Exam")
rects2 = ax.bar(x + width/2, score_fin, width, label="Final Exam")

# 添加标题、坐标轴、图例等信息
ax.set_ylabel("Score")
ax.set_xlabel("Student")
ax.set_title("Scores on Midterm and Final Exams")
ax.set_xticks(x)
ax.set_xticklabels(student)
ax.legend(labels=('tv', 'Smartphone'), loc=0)

# 显示图像
plt.show()

# 参考：https://geek-docs.com/matplotlib/matplotlib-top-tutorials/1019100_matplotlib_bar_plot.html