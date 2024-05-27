import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# 设置全局字体
plt.rcParams['font.family'] = 'Times New Roman'
matplotlib.rcParams.update({'font.size': 16})
# # 设置全局label标签的大小
# plt.rcParams['axes.labelsize'] = 12
# plt.rcParams['axes.titlesize'] = 12
# 更改配色
# colors = [(142 / 255, 207 / 255, 201 / 255),
#           (255 / 255, 190 / 255, 122 / 255),
#           (250 / 255, 127 / 255, 111 / 255),
#           (130 / 255, 176 / 255, 210 / 255)]
# 生成示例数据
categories = ['Email', 'SSBO', 'Facebook', 'WikiVote', 'Deezer']
# 影响力值
y1 = [2.56, 0.69, 2.7, 0.69, 0.665]  # FPB算法
y2 = [2.05, 0.332, 1.5, 0.45, 0.411]  # BRB算法
y3 = [1.35, 0.2, 1.25, 0.32, 0.2]  # GreedyD算法
y4 = [0.89, 0.15, 0.6, 0.2, 0.18]  # GreedyF算法
# 最小度
d1 = [6, 5.3, 5.6, 5.55, 3.6]  # FPB算法
d2 = [6, 5.8, 6, 6, 5.2]  # BRB算法
d3 = [3.2, 3, 4.2, 2.6, 2.8]  # GreedyD
d4 = [2.1, 2.0, 2.5, 1.7, 1.8]  # GreedyF

# 设置柱状图宽度
bar_width = 0.2  # 柱子宽度

# 生成柱状图位置
index = np.arange(len(categories))

# 创建两个子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))
# fig, (ax1, ax2) = plt.subplots(1, 2)

# 绘制第一个柱状图
ax1.bar(index - bar_width, y1, bar_width, label='FPB',)
ax1.bar(index, y2, bar_width, label='BRB', )
ax1.bar(index + bar_width, y3, bar_width, label='GreedyD', )
ax1.bar(index + bar_width * 2, y4, bar_width, label='GreedyF', )

# 设置第一个子图标题和标签
ax1.set_title('(a) Minimum Influence Comparison')
# ax1.set_xlabel('dataset')
ax1.set_ylabel('min_influence')
ax1.set_xticks(index + bar_width / 2)
ax1.set_xticklabels(categories)
# ax1.legend(fontsize=10.5)
# ax1.set_ylim(2.5, 2.7)

# 绘制第二个柱状图
ax2.bar(index - bar_width, d1, bar_width, label='FPB',)
ax2.bar(index, d2, bar_width, label='BRB', )
ax2.bar(index + bar_width, d3, bar_width, )
ax2.bar(index + bar_width * 2, d4, bar_width, )

# 设置第二个子图标题和标签
ax2.set_title('(b) Minimum Degree Comparison')
# ax2.set_xlabel('dataset')
ax2.set_ylabel('min_degree')
ax2.set_xticks(index + bar_width / 2)
ax2.set_xticklabels(categories)
# ax2.legend(fontsize=10.5)
# ax2.set_ylim(0, 7)
# 调整子图之间的间距
plt.tight_layout()
# 调整图例位置，两个图共用一个图例
# 设置图例
ax1.legend(loc='upper center', bbox_to_anchor=(1.1, 1.23), fancybox=True, shadow=False, ncol=4,frameon=False)
plt.subplots_adjust(top=0.85,hspace=0.5)
# 添加图例，并设置填充样式
plt.savefig("algorithm_quality_comparison.eps")
# 显示图表
plt.show()
