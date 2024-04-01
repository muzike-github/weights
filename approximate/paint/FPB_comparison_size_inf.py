import matplotlib.pyplot as plt
import numpy as np
import matplotlib
# # 设置全局字体
# plt.rcParams['font.family'] = 'Times New Roman'
# matplotlib.rcParams.update({'font.size': 12})
# # 设置全局label标签的大小
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 12
# 更改配色
colors = [(142 / 255, 207 / 255, 201 / 255),
          (255 / 255, 190 / 255, 122 / 255),
          (250 / 255, 127 / 255, 111 / 255),
          (130 / 255, 176 / 255, 210 / 255)]

# 三种算法影响力对比
# 生成示例数据
categories = ['4', '5', '6', '7', '8']
FPB1 = [1.39,1.76,2.165,2.7,2.88]
BRB1 = [0.66,0.86,1.21,1.35,1.6]
greedyD1 = [0.52,0.75,1.06,1.12,1.3]
greedyF1 = [0.34,0.48,0.8,0.85,1.0]


FPB2 = [0.95,0.86,0.7,0.64,0.54]
BRB2 = [0.5152,0.40,0.33,0.27,0.23]
greedyD2 = [0.4,0.29,0.22,0.19,0.16]
greedyF2 = [0.3,0.2,0.18,0.15,0.1]
# 设置柱状图宽度
bar_width = 0.2  # 柱子宽度

# 生成柱状图位置
index = np.arange(len(categories))

# 创建两个子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 3.7))

# 绘制第一个柱状图
ax1.bar(index - bar_width, FPB1, bar_width, label='FPB',color=colors[0],hatch ='//')
ax1.bar(index, BRB1, bar_width, label='BRB',color=colors[1],hatch ='xx')
ax1.bar(index + bar_width, greedyD1, bar_width, label='GreedyD',color=colors[2],hatch ='\\\\')
ax1.bar(index + bar_width * 2, greedyF1, bar_width, label='GreedyF',color=colors[3],hatch ='..')

# 设置第一个子图标题和标签
ax1.set_title('(a) Facebook')
ax1.set_xlabel('community size')
ax1.set_ylabel('min_influence')
ax1.set_xticks(index + bar_width / 2)
ax1.set_xticklabels(categories)
ax1.legend(loc='upper left')
ax1.set_ylim(0, 3.2)
# 绘制第二个柱状图
ax2.bar(index - bar_width, FPB2, bar_width, label='FPB',color=colors[0],hatch ='//')
ax2.bar(index, BRB2, bar_width, label='BRB',color=colors[1],hatch ='xx')
ax2.bar(index + bar_width, greedyD2, bar_width, label='GreedyD',color=colors[2],hatch ='\\\\')
ax2.bar(index + bar_width * 2, greedyF2, bar_width, label='GreedyF',color=colors[3],hatch ='..')

# 设置第二个子图标题和标签
ax2.set_title('(b) WikiVote')
ax2.set_xlabel('community size')
ax2.set_ylabel('min_influence')
ax2.set_xticks(index + bar_width / 2)
ax2.set_xticklabels(categories)
ax2.legend()
ax2.set_ylim(0, 1.2)
# 调整子图之间的间距
plt.tight_layout()
# plt.subplots_adjust(wspace=0.3, left=0.1, right=0.9, bottom=0.1, top=0.9)
# 显示图表
plt.savefig("3.5.jpg",dpi=600)
plt.show()
