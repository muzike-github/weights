import matplotlib.pyplot as plt
import numpy as np
import matplotlib
# 图4.16不同社区大小下算法的运行时间对比
matplotlib.rcParams.update({'font.size': 12})
# 生成示例数据
categories = ['4', '5', '6', '7', '8']
data1F = [13.70,
17.50 ,
22.10 ,
25.00 ,
28.90 ,
          ]
data2F = [5,
30,
31,
109,
298
]
data3F = [2,
2,
3,
3,
3,
 ]
data4F = [0.8,
0.8,
0.9,
0.9,
0.9,
   ]

data1W = [14,
20.8,
27.4,
34,
40

]
data2W = [30,
90,
120,
210,
500,

          ]
data3W = [2,
2,
3,
3,
3

]
data4W = [0.8,
0.8,
0.9,
0.9,
0.9
 ]

# 创建两个子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# 绘制第一个折线图
ax1.plot(categories, data1F, marker='o', label='SA_I', linestyle='-')
ax1.plot(categories, data2F, marker='^', label='BRB', linestyle='-')
ax1.plot(categories, data3F, marker='*', label='GreedyD', linestyle='-')
ax1.plot(categories, data4F, marker='+', label='GreedyF', linestyle='-')

# 设置第一个子图标题和标签
ax1.set_title('(a) WikiVote',fontsize = 12)
ax1.set_xlabel('community size')
ax1.set_ylabel('runtime(s)')
ax1.legend(fontsize = 10.5)
# 使用10的幂次方作为纵坐标
ax1.set_ylim(10**-1,10**3*4)  # 根据实际情况调整范围
ax1.set_yscale('log')
# ax1.ticklabel_format(axis='y', style='sci', scilimits=(-1, 3))

# 绘制第二个折线图
ax2.plot(categories, data1W, marker='o', label='SA_I', linestyle='-')
ax2.plot(categories, data2W, marker='^', label='BRB', linestyle='-')
ax2.plot(categories, data3W, marker='*', label='GreedyD', linestyle='-')
ax2.plot(categories, data4W, marker='+', label='GreedyF', linestyle='-')

# 设置第二个子图标题和标签
ax2.set_title('(b) DBLP',fontsize = 12)
ax2.set_xlabel('community size')
ax2.set_ylabel('runtime(s)')
ax2.legend(fontsize = 10.5)

# 使用10的幂次方作为纵坐标
ax2.set_ylim(10**-1,10**3*4)  # 根据实际情况调整范围
ax2.set_yscale('log')
# ax2.set_ylim(0,65)
# 调整子图之间的间距
plt.tight_layout()


# 显示图表
plt.show()
