import matplotlib.pyplot as plt
import numpy as np
import matplotlib
# 设置全局字体
# plt.rcParams['font.family'] = 'Times New Roman'
matplotlib.rcParams.update({'font.size': 12})
# # 设置全局label标签的大小
# plt.rcParams['axes.labelsize'] = 12
# plt.rcParams['axes.titlesize'] = 12
# 生成示例数据
categories = ['10','50', '100','200', '500', '1000', '1500', '2000']
data1F = [2.5343, 2.6133, 2.6258, 2.6592, 2.6726, 2.6742, 2.6816, 2.6871]
data1W = [0.6052, 0.7561, 0.8162, 0.8122, 0.8355, 0.8339, 0.8484, 0.8538]

# 设置柱状图宽度
bar_width = 0.5  # 柱子宽度

# 生成柱状图位置
index = np.arange(len(categories))

# 创建两个子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 3))

# 绘制第一个柱状图
ax1.bar(index + bar_width / 2, data1F, bar_width,color = 'skyblue')

# 设置第一个子图标题和标签
ax1.set_title('(a) Facebook',fontsize = 12)
ax1.set_xlabel('iterations')
ax1.set_ylabel('min_influence')
ax1.set_xticks(index + bar_width / 2)
ax1.set_xticklabels(categories)
# ax1.legend()
ax1.set_ylim(2.5, 2.7)
ax1.plot(index + bar_width / 2, data1F, marker='o', linestyle='-', label='Line',markersize=3)


# 绘制第二个柱状图
ax2.bar(index + bar_width / 2, data1W, bar_width,color = 'skyblue')
# 设置第二个子图标题和标签
ax2.set_title('(b) WikiVote',fontsize = 12)
ax2.set_xlabel('iterations')
ax2.set_ylabel('min_influence')
ax2.set_xticks(index + bar_width / 2)
ax2.set_xticklabels(categories)
# ax2.legend()
ax2.set_ylim(0.5, 1)
ax2.plot(index + bar_width / 2, data1W, marker='o', linestyle='-', label='Line',markersize=3)
# 调整子图之间的间距
plt.tight_layout()
# plt.subplots_adjust(wspace=0.3, left=0.1, right=0.9, bottom=0.1, top=0.9)
# 显示图表
plt.show()
