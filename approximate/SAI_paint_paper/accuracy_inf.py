import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
import matplotlib

# 模拟退火论文，将两个图合并为一个
# 设置全局字体
# plt.rcParams['font.family'] = 'Times New Roman'
matplotlib.rcParams.update({'font.size': 16})
# 设置全局label标签的大小
# plt.rcParams['axes.labelsize'] = 12
# plt.rcParams['axes.titlesize'] = 12
# 生成示例数据
# 影响力值
categories = ['10', '30', '50', '100', '150', '200', '300', '500']
dataF_100 = [0.0773, 0.0463, 0.0459, 0.0384, 0.0409, 0.0316, 0.0236, 0.0219, ]
dataF_300 = [0.0786, 0.0516, 0.0378, 0.0273, 0.0313, 0.0306, 0.0255, 0.0227, ]
dataF_500 = [0.0747, 0.0445, 0.0379, 0.0308, 0.0310, 0.0248, 0.0184, 0.0182, ]
dataF_1000 = [0.0839, 0.0463, 0.0311, 0.0355, 0.0275, 0.0210, 0.0202, 0.0176, ]
dataF_2000 = [0.0730, 0.0449, 0.0328, 0.0331, 0.0266, 0.0206, 0.0196, 0.0161, ]

dataW_100 = [0.1929, 0.1151, 0.0820, 0.1236, 0.0711, 0.0505, 0.0779, 0.0690, ]
dataW_300 = [0.1487, 0.1315, 0.1069, 0.0812, 0.0863, 0.0750, 0.0731, 0.0650, ]
dataW_500 = [0.2051, 0.1256, 0.0990, 0.1008, 0.0761, 0.0742, 0.0638, 0.0600, ]
dataW_1000 = [0.1499, 0.0954, 0.0677, 0.0761, 0.0716, 0.0705, 0.0603, 0.0580, ]
dataW_2000 = [0.1508, 0.1000, 0.0714, 0.0767, 0.0653, 0.0638, 0.0508, 0.0550, ]
# 运行时间
dataFQ_100 = [2.5, 3.3, 4.4, 6.5, 8.8, 11.1, 15.5, 24.0]
dataFQ_300 = [2.5, 3.4, 4.8, 8.0, 11.5, 13.7, 19.2, 29.4, ]
dataFQ_500 = [2.5, 3.6, 4.9, 8.1, 10.8, 14.1, 19.9, 32.0, ]
dataFQ_1000 = [2.5, 3.6, 4.9, 8.3, 11.7, 14.8, 20.5, 33.4, ]
dataFQ_2000 = [2.5, 3.9, 5.1, 8.7, 12.2, 15.4, 22.0, 35.5, ]

dataWQ_100 = [3.6, 5.1, 6.7, 10.8, 14.9, 19.0, 26.8, 43.3, ]
dataWQ_300 = [3.9, 6.0, 7.7, 13.0, 18.0, 23.1, 32.6, 51.8, ]
dataWQ_500 = [3.9, 5.8, 8.0, 13.8, 19.1, 24.3, 34.7, 56.5, ]
dataWQ_1000 = [3.9, 6.2, 8.6, 14.0, 19.8, 25.2, 35.6, 57.6, ]
dataWQ_2000 = [3.9, 6.3, 8.7, 14.6, 20.6, 26.4, 37.5, 60.5, ]

# 创建两个子图
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 7))

# 绘制第一个折线图
ax1.plot(categories, dataF_100, marker='+', label='100', linestyle='-')
ax1.plot(categories, dataF_300, marker='^', label='300', linestyle='-')
ax1.plot(categories, dataF_500, marker='*', label='500', linestyle='-')
ax1.plot(categories, dataF_1000, marker='o', label='1000', linestyle='-')
ax1.plot(categories, dataF_2000, marker='v', label='2000', linestyle='-')

# 设置第一个子图标题和标签
ax1.set_title('(a) Facebook')
ax1.set_xlabel('iterations')
ax1.set_ylabel('relative error')
ax1.legend()
ax1.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y * 100:.1f}%'))
# 绘制第二个折线图
ax2.plot(categories, dataW_100, marker='+', label='100', linestyle='-')
ax2.plot(categories, dataW_300, marker='^', label='300', linestyle='-')
ax2.plot(categories, dataW_500, marker='*', label='500', linestyle='-')
ax2.plot(categories, dataW_1000, marker='o', label='1000', linestyle='-')
ax2.plot(categories, dataW_2000, marker='v', label='2000', linestyle='-')

# 设置第二个子图标题和标签
ax2.set_title('(b) WikiVote')
ax2.set_xlabel('iterations')
ax2.set_ylabel('relative error')
ax2.legend()

# 绘制第3个折线图
ax3.plot(categories, dataFQ_100, marker='+', label='100', linestyle='-')
ax3.plot(categories, dataFQ_300, marker='^', label='300', linestyle='-')
ax3.plot(categories, dataFQ_500, marker='*', label='500', linestyle='-')
ax3.plot(categories, dataFQ_1000, marker='o', label='1000', linestyle='-')
ax3.plot(categories, dataFQ_2000, marker='v', label='2000', linestyle='-')

# 设置第3个子图标题和标签
ax3.set_title('(a) Facebook')
ax3.set_xlabel('iterations')
ax3.set_ylabel('runtime')
ax3.legend()

# 绘制第4个折线图
ax4.plot(categories, dataWQ_100, marker='+', label='100', linestyle='-')
ax4.plot(categories, dataWQ_300, marker='^', label='300', linestyle='-')
ax4.plot(categories, dataWQ_500, marker='*', label='500', linestyle='-')
ax4.plot(categories, dataWQ_1000, marker='o', label='1000', linestyle='-')
ax4.plot(categories, dataWQ_2000, marker='v', label='2000', linestyle='-')

# 设置第4个子图标题和标签
ax4.set_title('(b) WikiVote')
ax4.set_xlabel('iterations')
ax4.set_ylabel('runtime')
ax4.legend()

# 调整子图之间的间距
plt.tight_layout()

# 显示图表
plt.show()
