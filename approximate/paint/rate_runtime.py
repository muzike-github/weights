import matplotlib.pyplot as plt
import numpy as np
import matplotlib
# 4.9降温速率对算法运行时间的影响
# 设置全局字体
# plt.rcParams['font.family'] = 'Times New Roman'
matplotlib.rcParams.update({'font.size': 12})
# 设置全局label标签的大小
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 12
# 生成示例数据
categories = ['0.5', '0.7', '0.8', '0.85', '0.9', '0.95', '0.97']
data1F = [3.5, 4.7, 6.48, 8.54, 12, 22, 36]
data1W = [5.58, 8.1, 11, 14, 21, 40, 65]

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
ax1.set_xlabel('cooling rate')
ax1.set_ylabel('runtime(s)')
ax1.set_xticks(index + bar_width / 2)
ax1.set_xticklabels(categories)
# ax1.legend()
ax1.set_ylim(0, 70)


# 绘制第二个柱状图
ax2.bar(index + bar_width / 2, data1W, bar_width,color = 'skyblue')
ax2.plot(index + bar_width / 2, data1W, marker='o', linestyle='-', label='Line',markersize=3)
# 设置第二个子图标题和标签
ax2.set_title('(b) WikiVote',fontsize = 12)
ax2.set_xlabel('cooling rate')
ax2.set_ylabel('runtime(s)')
ax2.set_xticks(index + bar_width / 2)
ax2.set_xticklabels(categories)
# ax2.legend()
ax2.set_ylim(0, 70)
# 调整子图之间的间距
plt.tight_layout()
# plt.subplots_adjust(wspace=0.3, left=0.1, right=0.9, bottom=0.1, top=0.9)
# 显示图表
plt.show()
