import matplotlib.pyplot as plt
import numpy as np

# 示例数据
categories = ['A', 'B', 'C', 'D']
values = [3, 5, 2, 7]

# 生成柱状图位置
index = np.arange(len(categories))

# 创建图表和子图
fig, ax = plt.subplots()

# 绘制柱状图，并指定hatch参数填充柱子
bars = ax.bar(index, values, hatch='///', color='lightblue', label='Data')

# 添加数值标签
for i, v in enumerate(values):
    ax.text(i, v + 0.2, str(v), ha='center')

# 设置标签和标题
ax.set_xlabel('Categories')
ax.set_ylabel('Values')
ax.set_title('Bar Chart with Hatch Filling')

# 设置 x 轴刻度和标签
ax.set_xticks(index)
ax.set_xticklabels(categories)

# 添加图例，并设置填充样式


# 显示图表
plt.show()
