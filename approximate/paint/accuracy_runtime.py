import matplotlib.pyplot as plt
import numpy as np
import matplotlib
# 4.12不同温度下迭代次数对算法运行时间影响
# 设置全局字体
# plt.rcParams['font.family'] = 'Times New Roman'
matplotlib.rcParams.update({'font.size':12})
# 设置全局label标签的大小
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 12
# 生成示例数据
categories = ['10','30','50','100','150','200','300','500']
dataF_100 = [2.5 ,3.3 ,4.4 ,6.5 ,8.8 ,11.1 ,15.5 ,24.0]
dataF_300 = [2.5,3.4 ,4.8 ,8.0 ,11.5 ,13.7 ,19.2 ,29.4 ,]
dataF_500 = [2.5 ,3.6 ,4.9 ,8.1 ,10.8 ,14.1 ,19.9 ,32.0 ,]
dataF_1000 = [2.5 ,3.6 ,4.9 ,8.3 ,11.7 ,14.8 ,20.5 ,33.4 ,]
dataF_2000 = [2.5 ,3.9 ,5.1 ,8.7 ,12.2 ,15.4 ,22.0 ,35.5 ,]

dataW_100 = [3.6,5.1,6.7,10.8,14.9 ,19.0 ,26.8 ,43.3 ,]
dataW_300 = [3.9 ,6.0 ,7.7 ,13.0 ,18.0 ,23.1 ,32.6 ,51.8 ,]
dataW_500 = [3.9 ,5.8 ,8.0 ,13.8 ,19.1 ,24.3 ,34.7 ,56.5 ,]
dataW_1000 = [3.9,6.2 ,8.6 ,14.0 ,19.8 ,25.2 ,35.6 ,57.6 ,]
dataW_2000 = [3.9 ,6.3 ,8.7 ,14.6 ,20.6 ,26.4 ,37.5 ,60.5 ,]



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
ax1.set_ylabel('runtime(s)')
ax1.legend()
ax1.set_ylim(0,65)

# 绘制第二个折线图
ax2.plot(categories, dataW_100, marker='+', label='100', linestyle='-')
ax2.plot(categories, dataW_300, marker='^', label='300', linestyle='-')
ax2.plot(categories, dataW_500, marker='*', label='500', linestyle='-')
ax2.plot(categories, dataW_1000, marker='o', label='1000', linestyle='-')
ax2.plot(categories, dataW_2000, marker='v', label='2000', linestyle='-')

# 设置第二个子图标题和标签
ax2.set_title('(b) WikiVote',fontsize = 12)
ax2.set_xlabel('iterations')
ax2.set_ylabel('runtime(s)')
ax2.legend()
ax2.set_ylim(0,65)
# 调整子图之间的间距
plt.tight_layout()

# 显示图表
plt.show()
