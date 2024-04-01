# 精确算法运行时间对比
import matplotlib.pyplot as plt
import numpy as np

# 生成示例数据
categories = ['4','5','6','7','8']
# facebook数据
f1 = [2.7, 6.6, 59, 68, 252]  # FPB
f2 = [0.9, 1.1, 1.4, 1.7, 1.5]  # BRB
f3 = [1050, 2000, 8800, 13000, 15000]  # baseline
f4 = [1, 1.2, 1.5, 2, 2]  # greedyD
f5 = [1, 1, 1, 1, 1]  # GreedyF
# wiki数据
w1 = [15, 23, 50, 121, 300]  # FPB
w2 = [1, 20, 60, 150, 200]  # BRB
w3 = [1100, 1500, 7000, 11000, 15000]  # baseline
w4 = [1, 1.2, 1.5, 2, 2]
w5 = [1, 1, 1, 1, 1]
# 创建两个子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.set_yscale('log')
ax2.set_yscale('log')
# 绘制第一个折线图
ax1.plot(categories, f1, marker='+', label='FPB', linestyle='-')
ax1.plot(categories, f2, marker='^', label='BRB', linestyle='-')
ax1.plot(categories, f3, marker='*', label='baseline', linestyle='-')
ax1.plot(categories, f4, marker='o', label='GreedyD', linestyle='-')
ax1.plot(categories, f5, marker='v', label='GreedyF', linestyle='-')

# 设置第一个子图标题和标签
ax1.set_title('Facebook')
ax1.set_xlabel('community size')
ax1.set_ylabel('runtime(s)')
ax1.legend()
ax1.set_ylim(0, 10**4)

# ax1.spines['top'].set_visible(False) # 去掉上边框
# ax1.spines['right'].set_visible(False)
# 绘制第二个折线图
ax2.plot(categories, w1, marker='+', label='FPB', linestyle='-')
ax2.plot(categories, w2, marker='^', label='BRB', linestyle='-')
ax2.plot(categories, w3, marker='*', label='baseline', linestyle='-')
ax2.plot(categories, w4, marker='o', label='GreedyD', linestyle='-')
ax2.plot(categories, w5, marker='v', label='GreedyF', linestyle='-')

# 设置第二个子图标题和标签
ax2.set_title('wiki-vote')
ax2.set_xlabel('community size')
ax2.set_ylabel('runtime(s)')
ax2.legend()
ax2.set_ylim(0, 10**4)
# 调整子图之间的间距
plt.tight_layout()

# 显示图表
plt.show()
