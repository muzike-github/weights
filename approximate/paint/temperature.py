import matplotlib.pyplot as plt
import numpy as np
import matplotlib
# 4.6不同温度对社区质量的影响力
plt.rcParams['font.size']=12
plt.rcParams['lines.markersize'] = 7

# 生成示例数据
categories = ['50', '100', '500', '1000', '5000', '10000']
data1F = [2.612, 2.6145, 2.632, 2.6337, 2.6388, 2.6389]

data1W = [0.7948, 0.8018, 0.8146, 0.8228, 0.8244, 0.8257]

# 设置柱状图宽度
bar_width = 0.4  # 柱子宽度

# 生成柱状图位置
index = np.arange(len(categories))

# 创建两个子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 3))

# 绘制第一个柱状图
ax1.bar(index + bar_width / 2, data1F, bar_width,color = 'lightblue')
# 设置第一个子图标题和标签
ax1.set_title('(a) Facebook',fontsize = 12)
ax1.set_xlabel('temperature')
ax1.set_ylabel('min_influence')
ax1.set_xticks(index + bar_width / 2)
ax1.set_xticklabels(categories)
# ax1.legend()
ax1.set_ylim(2.59, 2.65)
# 折线连起来
# 在两组柱状图的中间位置绘制连接线，设置连接点的大小
ax1.plot(index + bar_width / 2, data1F, marker='o', linestyle='-', label='Line', markersize=3)


# 绘制第二个柱状图
ax2.bar(index + bar_width / 2, data1W, bar_width,color = 'skyblue')
# 设置第二个子图标题和标签
ax2.set_title('(b) WikiVote',fontsize = 12)
ax2.set_xlabel('temperature')
ax2.set_ylabel('min_influence')
ax2.set_xticks(index + bar_width / 2)
ax2.set_xticklabels(categories)
# ax2.legend()
ax2.set_ylim(0.78, 0.83)
# 调整子图之间的间距
plt.tight_layout()
ax2.plot(index + bar_width / 2, data1W, marker='o', linestyle='-',color = '#1F77B4', label='Line', markersize=3)
# plt.subplots_adjust(wspace=0.3, left=0.1, right=0.9, bottom=0.1, top=0.9)
# 显示图表
plt.show()
