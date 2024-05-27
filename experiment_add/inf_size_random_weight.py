import matplotlib.pyplot as plt
import numpy as np
import matplotlib

'''
将边的权重设置为随机值，观察不同算法的搜索表现
'''
# # 设置全局字体
plt.rcParams['font.family'] = 'Times New Roman'
matplotlib.rcParams.update({'font.size': 14})
# # 设置全局label标签的大小
# plt.rcParams['axes.labelsize'] = 18
# plt.rcParams['axes.titlesize'] = 18
# 更改配色
# colors = [(142 / 255, 207 / 255, 201 / 255),
#           (255 / 255, 190 / 255, 122 / 255),
#           (250 / 255, 127 / 255, 111 / 255),
#           (130 / 255, 176 / 255, 210 / 255)]

# 三种算法影响力对比
# 生成示例数据
categories = ['4', '5', '6', '7', '8']
FPB1 = [2.11, 2.59, 3.09, 3.5, 3.91]
BRB1 = [0.88, 1.16, 1.66, 2.15, 2.11]
greedyD1 = [0.68, 0.82, 1.23, 1.52, 1.73]
greedyF1 = [0.35, 0.40, 0.72, 0.77, 1]

FPB2 = [1.79, 2.08, 2.23, 2.49, 2.76]
BRB2 = [0.64, 1.35, 1.09, 1.55, 1.42]
greedyD2 = [0.52, 0.68, 0.72, 0.85, 1]
greedyF2 = [0.25, 0.4, 0.3, 0.6, 0.74]
# 设置柱状图宽度
bar_width = 0.2  # 柱子宽度

# 生成柱状图位置
index = np.arange(len(categories))

# 创建两个子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))

# 绘制第一个柱状图
ax1.bar(index - bar_width, FPB1, bar_width, label='FPB', )
ax1.bar(index, BRB1, bar_width, label='BRB', )
ax1.bar(index + bar_width, greedyD1, bar_width, label='GreedyD', )
ax1.bar(index + bar_width * 2, greedyF1, bar_width, label='GreedyF', )

# 设置第一个子图标题和标签
ax1.set_title('(a) Facebook')
ax1.set_xlabel('Community size')
ax1.set_ylabel('min_influence')
ax1.set_xticks(index + bar_width / 2)
ax1.set_xticklabels(categories)
# ax1.legend(loc='upper left')
ax1.set_ylim(0, 4)
# 绘制第二个柱状图
ax2.bar(index - bar_width, FPB2, bar_width, label='FPB', )
ax2.bar(index, BRB2, bar_width, label='BRB', )
ax2.bar(index + bar_width, greedyD2, bar_width, label='GreedyD', )
ax2.bar(index + bar_width * 2, greedyF2, bar_width, label='GreedyF', )

# 设置第二个子图标题和标签
ax2.set_title('(b) WikiVote')
ax2.set_xlabel('Community size')
ax2.set_ylabel('min_influence')
ax2.set_xticks(index + bar_width / 2)
ax2.set_xticklabels(categories)
# ax2.legend(loc='upper left')
ax2.set_ylim(0, 3.5)
# 调整子图之间的间距
plt.tight_layout()
# plt.subplots_adjust(wspace=0.3, left=0.1, right=0.9, bottom=0.1, top=0.9)
# 调整图例位置，两个图共用一个图例
# 设置图例,bbox_to_anchor参数的意思是离左边和上边的距离
ax1.legend(loc='upper center', bbox_to_anchor=(1.1, 1.22), fancybox=True, shadow=False, ncol=4,frameon=False)
plt.subplots_adjust(top=0.85,hspace=0.5)
# 显示图表
plt.savefig("algorithm_inf_random.svg")
plt.show()
