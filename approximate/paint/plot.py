import matplotlib.pyplot as plt
import numpy as np

# 生成示例数据
categories = ['50', '100', '500', '1000','5000','10000']
data1F = [2.612, 2.6145, 2.632, 2.6337, 2.6388, 2.6378]
data2F = [2.2179, 2.2353, 2.2471, 2.2349, 2.2521, 2.2371]
data3F = [1.833, 1.8279, 1.8382, 1.8352, 1.8396, 1.8264]
data4F = [1.3869, 1.3962, 1.3989, 1.4061, 1.3948, 1.3923]
data1W = [0.7948, 0.8018, 0.8046, 0.8228, 0.8244, 0.8227]
data2W = [0.7053, 0.7217, 0.7263, 0.7091, 0.7138, 0.7342]
data3W = [0.6142, 0.6137, 0.6166, 0.624, 0.6338, 0.6266]
data4W = [0.5062, 0.5179, 0.5183, 0.5226, 0.5047, 0.5056]

# 设置柱状图宽度
bar_width = 0.2  # 柱子宽度

# 生成柱状图位置
index = np.arange(len(categories))

# 创建两个子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

# 绘制第一个柱状图
ax1.bar(index - bar_width, data1F, bar_width, label='Data Set 1', color='green')
ax1.bar(index, data2F, bar_width, label='Data Set 2', color='cyan')
ax1.bar(index + bar_width, data3F, bar_width, label='Additional Data 1', color='orange')
ax1.bar(index + 2*bar_width, data4F, bar_width, label='Additional Data 2', color='pink')

# 设置第一个子图标题和标签
ax1.set_title('Data Sets with Additional Bars')
ax1.set_xlabel('Categories')
ax1.set_ylabel('Values')
ax1.set_xticks(index + bar_width / 2)
ax1.set_xticklabels(categories)
ax1.legend()

# 绘制第二个柱状图
ax2.bar(index - bar_width, data1W, bar_width, label='Additional Data 3', color='green')
ax2.bar(index, data2W, bar_width, label='Additional Data 4', color='cyan')
ax2.bar(index + bar_width,data3W, bar_width, label='Data Set 2', color='orange')
ax2.bar(index + 2*bar_width, data4W, bar_width, label='Additional Data 5', color='pink')

# 设置第二个子图标题和标签
ax2.set_title('Additional Data Sets with Data Set 2')
ax2.set_xlabel('Categories')
ax2.set_ylabel('Values')
ax2.set_xticks(index + bar_width / 2)
ax2.set_xticklabels(categories)
ax2.legend()

# 调整子图之间的间距
plt.tight_layout()

# 显示图表
plt.show()
