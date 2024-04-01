import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
import matplotlib
# 4.11不同温度下迭代次数对社区质量的影响
# 设置全局字体
# plt.rcParams['font.family'] = 'Times New Roman'
matplotlib.rcParams.update({'font.size': 12})
# 设置全局label标签的大小
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 12
# 生成示例数据
categories = ['10','30','50','100','150','200','300','500']
dataF_100 = [0.0773,0.0463,0.0459,0.0384,0.0409,0.0316,0.0236,0.0219,]
dataF_300 = [0.0786,0.0516,0.0378,0.0273,0.0313,0.0306,0.0255,0.0227,]
dataF_500 = [0.0747,0.0445,0.0379,0.0308,0.0310,0.0248,0.0184,0.0182,]
dataF_1000 = [0.0839,0.0463,0.0311,0.0355,0.0275,0.0210,0.0202,0.0176,]
dataF_2000 = [0.0730,0.0449,0.0328,0.0331,0.0266,0.0206,0.0196 ,0.0161 ,]

dataW_100 = [0.1929,0.1151,0.0820,0.1236,0.0711,0.0505,0.0779,0.0690,]
dataW_300 = [0.1487,0.1315,0.1069,0.0812,0.0863,0.0750,0.0731,0.0650,]
dataW_500 = [0.2051,0.1256,0.0990,0.1008,0.0761,0.0742,0.0638,0.0600,]
dataW_1000 = [0.1499,0.0954,0.0677,0.0761,0.0716,0.0705,0.0603,0.0580,]
dataW_2000 = [0.1508,0.1000,0.0714,0.0767,0.0653,0.0638,0.0508,0.0550,]

# 创建两个子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# 绘制第一个折线图
ax1.plot(categories, dataF_100, marker='+', label='100', linestyle='-')
ax1.plot(categories, dataF_300, marker='^', label='300', linestyle='-')
ax1.plot(categories, dataF_500, marker='*', label='500', linestyle='-')
ax1.plot(categories, dataF_1000, marker='o', label='1000', linestyle='-')
ax1.plot(categories, dataF_2000, marker='v', label='2000', linestyle='-')

# 设置第一个子图标题和标签
ax1.set_title('(a) Facebook',fontsize = 12)
ax1.set_xlabel('iterations')
ax1.set_ylabel('relative error')
ax1.legend()
ax1.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y*100:.1f}%'))
# 绘制第二个折线图
ax2.plot(categories, dataW_100, marker='+', label='100', linestyle='-')
ax2.plot(categories, dataW_300, marker='^', label='300', linestyle='-')
ax2.plot(categories, dataW_500, marker='*', label='500', linestyle='-')
ax2.plot(categories, dataW_1000, marker='o', label='1000', linestyle='-')
ax2.plot(categories, dataW_2000, marker='v', label='2000', linestyle='-')

# 设置第二个子图标题和标签
ax2.set_title('(b) WikiVote',fontsize = 12)
ax2.set_xlabel('iterations')
ax2.set_ylabel('relative error')
ax2.legend()
ax2.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y*100:.1f}%'))
# 调整子图之间的间距
plt.tight_layout()

# 显示图表
plt.show()
