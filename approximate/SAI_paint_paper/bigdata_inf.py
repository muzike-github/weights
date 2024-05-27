import matplotlib.pyplot as plt
import numpy as np
import matplotlib

plt.rcParams['font.size']=16
plt.rcParams['lines.markersize'] = 9
# 图4.15不同数据集下各算法返回社区的质量
# 三种算法影响力对比
# 生成示例数据
categories = ['Email','SSBO', 'Facebook', 'WikiVote', 'Deezer', 'DBLP','Amazon']
# 更改配色
colors = [(142 / 255, 207 / 255, 201 / 255),
          (255 / 255, 190 / 255, 122 / 255),
          (250 / 255, 127 / 255, 111 / 255),
          (130 / 255, 176 / 255, 210 / 255)]
data1F = [2.4,0.7268,2.67,0.79,0.8536,1.5424,0.835,  ]
data2F = [2.05,0.36,1.5,0.4172,0.5158,0.9338,0.5306]
data3F = [1.35,0.3,1.25,0.35,0.4,0.7,0.4,]
data4F = [0.89,0.2,0.6,0.3,0.2,0.5,0.3   ]



# 设置柱状图宽度
bar_width = 0.15  # 柱子宽度

# 生成柱状图位置
index = np.arange(len(categories))

# 创建两个子图
fig, (ax1) = plt.subplots(1, figsize=(8.5, 4.1))

# 绘制第一个柱状图
ax1.bar(index - bar_width, data1F, bar_width, label='SAI',color=colors[0],hatch ='//')
ax1.bar(index, data2F, bar_width, label='BRB',color=colors[1],hatch ='xx')
ax1.bar(index + bar_width, data3F, bar_width, label='GreedyD',color=colors[2],hatch ='\\\\')
ax1.bar(index + bar_width * 2, data4F, bar_width, label='GreedyF',color=colors[3],hatch ='..')

# 设置第一个子图标题和标签
ax1.set_title('')
ax1.set_xlabel('dataset')
ax1.set_ylabel('min_influence')
ax1.set_xticks(index + bar_width / 2)
ax1.set_xticklabels(categories)
ax1.legend()
ax1.set_ylim(0, 3)
plt.tight_layout()
plt.savefig("4.15.jpg",dpi=600)
# 显示图表
plt.show()
