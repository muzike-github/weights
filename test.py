import matplotlib.pyplot as plt

# 创建一些示例数据
x = [1, 2, 3, 4, 5]
y1 = [1, 2, 3, 4, 5]
y2 = [5, 4, 3, 2, 1]

# 绘制图形
plt.plot(x, y1, label='Line 1')
plt.plot(x, y2, label='Line 2')

# 显示图例，并设置阴影为False
plt.legend(shadow=True)

plt.show()
