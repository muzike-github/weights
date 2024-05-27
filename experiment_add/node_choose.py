import matplotlib.pyplot as plt
import matplotlib
import numpy as np
plt.rcParams['font.family'] = 'Times New Roman'
matplotlib.rcParams.update({'font.size': 16})

# 生成示例数据
categories = ['4', '5', '6', '7','8']
# face
y1 = [2.7, 6.6, 46, 68, 237]  # score
y2 = [1.1, 9, 164, 269, 4756]  # random
y3 = [0.2, 0.3, 113, 116, 535]  # weight


# wiki
w1 = [15, 23, 50, 121, 189]  # score
w2 = [11, 44, 309, 1360, 9756]  # random
w3 = [15, 55, 172, 759, 2248]  # weight

# 创建两个子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))

# 绘制第一个折线图
ax1.plot(categories, y1, marker='v', label='score', linestyle='-',markersize=7)
ax1.plot(categories, y2, marker='^', label='random', linestyle='-',markersize=7)
ax1.plot(categories, y3, marker='+', label='weight', linestyle='-',markersize=7)

# 设置第一个子图标题和标签
ax1.set_title('(a) Facebook')
ax1.set_xlabel('Community size')
ax1.set_ylabel('runtime(s)')
# yticks = [10**i for i in range(1, 7)]
# print(yticks)
# ax1.set_yticks(yticks)
ax1.legend(frameon=False)
ax1.set_ylim(10**-1, 10 ** 4)
ax1.set_yscale('log')

# 绘制第二个折线图
ax2.plot(categories, w1, marker='v', label='score', linestyle='-')
ax2.plot(categories, w2, marker='^', label='random', linestyle='-')
ax2.plot(categories, w3, marker='+', label='weight', linestyle='-')

# 设置第二个子图标题和标签
ax2.set_title('(b) WikiVote')
ax2.set_xlabel('Community size')
ax2.set_ylabel('runtime(s)')
ax2.legend(frameon=False)
ax2.set_ylim(10**0, 10 ** 4)
ax2.set_yscale('log')
plt.tight_layout(pad=0.5)
plt.savefig("node_choose_strategy.eps")

# 显示图表
plt.show()

