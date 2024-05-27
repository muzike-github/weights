import matplotlib.pyplot as plt
import numpy as np
import matplotlib
# 4.13各算法返回社区的质量对比
plt.rcParams['font.size']=16
# 更改配色
colors = [(142 / 255, 207 / 255, 201 / 255),
          (255 / 255, 190 / 255, 122 / 255),
          (250 / 255, 127 / 255, 111 / 255),
          (130 / 255, 176 / 255, 210 / 255)]
# 三种算法影响力对比
# 生成示例数据
categories = ['4', '5', '6', '7', '8']
data1F = [1.40 ,1.76 ,2.17 ,2.70 ,2.90 , ]
data2F = [1.33 ,1.76 ,2.16 ,2.67 ,2.88 , ]
data3F = [1.08,1.44 ,1.68 ,2.19 ,2.18 ]
data4F = [0.52 ,0.73 ,0.95 ,1.08 ,1.35 , ]


data1W = [0.55 ,0.64 ,0.75 ,0.86 ,1.20 , ]
data2W = [0.52 ,0.63 ,0.74 ,0.79 ,0.92 , ]
data3W = [0.08 ,0.10 ,0.16 ,0.18 ,0.19]
data4W = [0.26,0.34 ,0.41 ,0.44 ,0.49 ]

# 设置柱状图宽度
bar_width = 0.2  # 柱子宽度

# 生成柱状图位置
index = np.arange(len(categories))

# 创建两个子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.5, 4))

# 绘制第一个柱状图
ax1.bar(index - bar_width, data1F, bar_width, label='FPB',color=colors[0],hatch ='//')
ax1.bar(index, data2F, bar_width, label='SAI',color=colors[1],hatch ='xx')
ax1.bar(index + bar_width, data3F, bar_width, label='RWI',color=colors[2],hatch ='\\\\')
ax1.bar(index + bar_width * 2, data4F, bar_width, label='PRI',color=colors[3],hatch ='..')

# 设置第一个子图标题和标签
ax1.set_title('(a) Facebook',fontsize = 12)
ax1.set_xlabel('community size')
ax1.set_ylabel('min_influence')
ax1.set_xticks(index + bar_width / 2)
ax1.set_xticklabels(categories)
ax1.legend()
ax1.set_ylim(0, 3.5)
# 绘制第二个柱状图
ax2.bar(index - bar_width, data1W, bar_width, label='FPB',color=colors[0],hatch ='//')
ax2.bar(index, data2W, bar_width, label='SAI',color=colors[1],hatch ='xx')
ax2.bar(index + bar_width, data3W, bar_width, label='RWI',color=colors[2],hatch ='\\\\')
ax2.bar(index + bar_width * 2, data4W, bar_width, label='PRI',color=colors[3],hatch ='..')

# 设置第二个子图标题和标签
ax2.set_title('(b) WikiVote',fontsize = 12)
ax2.set_xlabel('community size')
ax2.set_ylabel('min_influence')
ax2.set_xticks(index + bar_width / 2)
ax2.set_xticklabels(categories)
ax2.legend()
ax2.set_ylim(0, 1.4)
# 调整子图之间的间距
plt.tight_layout()
# plt.subplots_adjust(wspace=0.3, left=0.1, right=0.9, bottom=0.1, top=0.9)
# plt.savefig("4.13.jpg",dpi=600)
# 显示图表
plt.show()
