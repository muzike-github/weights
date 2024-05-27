import matplotlib.pyplot as plt
import matplotlib
import numpy as np
plt.rcParams['font.family'] = 'Times New Roman'
matplotlib.rcParams.update({'font.size': 16})
plt.rcParams['lines.markersize'] = 7
# 生成示例数据
categories = ['4', '5', '6', '7','8']
y1 = [2.7, 6.6, 59, 68, 252]  # FPB
y2 = [19, 40, 349, 467, 1955]  # FPB\F
y3 = [1.46, 14, 431, 2364, 25000]  # FPB\P
y4 = [1.53, 4.5, 176, 312, 758]  # FPB\B

w1 = [15, 23, 50, 121, 189]  # FPB
w2 = [215, 432, 4593, 15000, 25000]  # FPB\F
w3 = [11, 32, 191, 4421, 25000]  # FPB\P
w4 = [12, 46, 320, 976, 10000]  # FPB\B

# 创建两个子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))

# 绘制第一个折线图
ax1.plot(categories, y1, marker='v', label='FPB', linestyle='-')
ax1.plot(categories, y2, marker='^', label='FPB\F', linestyle='-')
ax1.plot(categories, y3, marker='*', label='FPB\P', linestyle='-')
ax1.plot(categories, y4, marker='o', label='FPB\B', linestyle='-')

# 设置第一个子图标题和标签
ax1.set_title('(a) Facebook')
ax1.set_xlabel('Community size')
ax1.set_ylabel('runtime(s)')
# yticks = [10**i for i in range(1, 7)]
# print(yticks)
# ax1.set_yticks(yticks)
ax1.legend(frameon=False)
ax1.set_ylim(10**0, 10 ** 4*2)
ax1.set_yscale('log')
# 绘制第二个折线图
ax2.plot(categories, w1, marker='v', label='FPB', linestyle='-')
ax2.plot(categories, w2, marker='^', label='FPB\F', linestyle='-')
ax2.plot(categories, w3, marker='*', label='FPB\P', linestyle='-')
ax2.plot(categories, w4, marker='o', label='FPB\B', linestyle='-')

# 设置第二个子图标题和标签
ax2.set_title('(b) WikiVote')
ax2.set_xlabel('Community size')
ax2.set_ylabel('runtime(s)')
ax2.legend(frameon=False)
ax2.set_ylim(10**0, 10 ** 4*2)
ax2.set_yscale('log')
plt.tight_layout(pad=0.5)

plt.savefig("different_strategy.eps")
# 显示图表
plt.show()
