import matplotlib.pyplot as plt
import numpy as np
import matplotlib
# 4.14社区不同规模下近似算法运行时间
plt.rcParams['font.size']=12
plt.rcParams['lines.markersize'] = 7
# 生成示例数据
categories = ['4', '5', '6', '7', '8']
data1F = [20.00, 40.00,
          120.00,
          200.00,
          500.00,
          ]
data2F = [7.90,
          8.75,
          11.63,
          15.25,
          16.75,
          ]
data3F = [4.38,
          5.75,
          7.38,
          9.13,
          10.63,
          ]
data4F = [1.00,
          1.00,
          1.2,
          1.3,
          1.5,
          ]

data1W = [30.00,
          50.30,
          150.70,
          260.00,
          600.00,
          ]
data2W = [13.70,
          17.50,
          22.10,
          25.00,
          28.90,
          ]
data3W = [7.50,
          10.90,
          13.50,
          16.70,
          20.30,
          ]
data4W = [1.00,
          1.00,
          1.200,
          1.3,
          1.5,
          ]

# 创建两个子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.2, 4))

# 绘制第一个折线图
ax1.plot(categories, data1F, marker='+', label='FPB', linestyle='-')
ax1.plot(categories, data2F, marker='^', label='SA_I', linestyle='-')
ax1.plot(categories, data3F, marker='*', label='RW_I', linestyle='-')
ax1.plot(categories, data4F, marker='o', label='PR_I', linestyle='-')

# 设置第一个子图标题和标签
ax1.set_title('(a) Facebook',fontsize = 12)
ax1.set_xlabel('community size')
ax1.set_ylabel('runtime(s)')
ax1.legend()
# 使用10的幂次方作为纵坐标
ax1.set_ylim(10**-1,10**4)  # 根据实际情况调整范围
ax1.set_yscale('log')
# ax1.ticklabel_format(axis='y', style='sci', scilimits=(-1, 3))

# 绘制第二个折线图
ax2.plot(categories, data1W, marker='+', label='FPB', linestyle='-')
ax2.plot(categories, data2W, marker='^', label='SA_I', linestyle='-')
ax2.plot(categories, data3W, marker='*', label='RW_I', linestyle='-')
ax2.plot(categories, data4W, marker='o', label='PR_I', linestyle='-')

# 设置第二个子图标题和标签
ax2.set_title('(b) WikiVote',fontsize = 12)
ax2.set_xlabel('community size')
ax2.set_ylabel('runtime(s)')
ax2.legend()

# 使用10的幂次方作为纵坐标
ax2.set_ylim(10**-1,10**4)  # 根据实际情况调整范围
ax2.set_yscale('log')
# ax2.set_ylim(0,65)
# 调整子图之间的间距
plt.tight_layout()


# 显示图表
plt.show()
