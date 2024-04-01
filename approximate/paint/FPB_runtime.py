import matplotlib.pyplot as plt
import matplotlib
import numpy as np
plt.rcParams['font.size']=12
plt.rcParams['lines.markersize'] = 7

# 生成示例数据
categories = ['4', '5', '6', '7','8']
# face
y1 = [35,100,190,290,700]  # FPB
y2 = [1,1.1,1.3,1.66,3.75]  # BRB
y3 = [110,900,21300,1200000,1200000]  # baseline
y4 = [2.5, 2.6, 2.6, 2.6, 2.6]  # greedyD
y5 = [0.5, 0.5, 0.5, 0.5, 0.5]  # GreedyF

# wiki
w1 = [30,90,163,220,600]  # FPB
w2 = [2,20,31,109,211]  # BRB
w3= [100,681,14288,900000,700000]  # baseline
w4 = [2, 2, 2.4, 2.4, 2.4]
w5 = [0.5, 0.5, 0.5, 0.5, 0.5]

# 创建两个子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.2))

# 绘制第一个折线图
ax1.plot(categories, y1, marker='v', label='FPB', linestyle='-',markersize=7)
ax1.plot(categories, y2, marker='^', label='BRB', linestyle='-',markersize=7)
ax1.plot(categories, y4, marker='*', label='GreedyD', linestyle='-',markersize=7)
ax1.plot(categories, y5, marker='o', label='GreedyF', linestyle='-',markersize=7)
ax1.plot(categories, y3, marker='+', label='baseline', linestyle='-',markersize=7)

# 设置第一个子图标题和标签
ax1.set_title('(a) Facebook',fontsize = 12)
ax1.set_xlabel('community size')
ax1.set_ylabel('runtime(s)')
# yticks = [10**i for i in range(1, 7)]
# print(yticks)
# ax1.set_yticks(yticks)
ax1.legend(loc='center left',bbox_to_anchor=(0.001, 0.82),fontsize = 10.5)
ax1.set_ylim(10**-1, 10 ** 5*2)
ax1.set_yscale('log')

# 绘制第二个折线图
ax2.plot(categories, w1, marker='v', label='FPB', linestyle='-',markersize=7)
ax2.plot(categories, w2, marker='^', label='BRB', linestyle='-',markersize=7)
ax2.plot(categories, w4, marker='*', label='GreedyD', linestyle='-',markersize=7)
ax2.plot(categories, w5, marker='o', label='GreedyF', linestyle='-')
ax2.plot(categories, w3, marker='+', label='baseline', linestyle='-')

# 设置第二个子图标题和标签
ax2.set_title('(b) WikiVote',fontsize = 12)
ax2.set_xlabel('community size')
ax2.set_ylabel('runtime(s)')
ax2.legend(loc='center left',bbox_to_anchor=(0.001, 0.82),fontsize = 10.5)
ax2.set_ylim(10**-1, 10 ** 5*2)
ax2.set_yscale('log')
plt.tight_layout(pad=0.5)


# 显示图表
plt.show()

