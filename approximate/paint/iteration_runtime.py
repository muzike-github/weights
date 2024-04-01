import matplotlib.pyplot as plt
import numpy as np
import matplotlib
# 4.8不同迭代次数对运行时间的影响
# 设置全局字体
# plt.rcParams['font.family'] = 'Times New Roman'
matplotlib.rcParams.update({'font.size': 12})
# 设置全局label标签的大小
# plt.rcParams['axes.labelsize'] = 12
# plt.rcParams['axes.titlesize'] = 12
# 生成示例数据
categories = ['10', '50', '100', '200', '500', '1000', '1500', '2000']
data1F = [2.1, 2.92, 4, 6, 12, 23, 34, 44]
data1W = [3, 4.54, 6, 10, 22, 41, 60, 79]

# 设置柱状图宽度
bar_width = 0.4  # 柱子宽度

# 生成柱状图位置
index = np.arange(len(categories))

# 创建两个子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 3))

# 绘制第一个柱状图
ax1.bar(index + bar_width / 2, data1F, bar_width,color = 'skyblue')
ax1.plot(index + bar_width / 2, data1F, marker='o', linestyle='-', label='Line',markersize=3)
# 设置第一个子图标题和标签
ax1.set_title('(a) Facebook',fontsize = 12)
ax1.set_xlabel('iterations')
ax1.set_ylabel('runtime(s)')
ax1.set_xticks(index + bar_width / 2)
ax1.set_xticklabels(categories)
# ax1.legend()
ax1.set_ylim(0, 90)
# 绘制第二个柱状图
ax2.bar(index + bar_width / 2, data1W, bar_width,color = 'skyblue')
ax2.plot(index + bar_width / 2, data1W, marker='o', linestyle='-', label='Line',markersize=3)
# 设置第二个子图标题和标签
ax2.set_title('(b) WikiVote',fontsize = 12)
ax2.set_xlabel('iterations')
ax2.set_ylabel('runtime(s)')
ax2.set_xticks(index + bar_width / 2)
ax2.set_xticklabels(categories)
# ax2.legend()
ax2.set_ylim(0, 90)
# 调整子图之间的间距
plt.tight_layout()
# plt.subplots_adjust(wspace=0.3, left=0.1, right=0.9, bottom=0.1, top=0.9)
# 显示图表
plt.show()
