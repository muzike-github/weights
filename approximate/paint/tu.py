import matplotlib.pyplot as plt

# 第一张子图的数据
file_sizes = list(range(10, 110, 10))
temperature_100 = [0.07733, 0.04634, 0.04889, 0.03807, 0.03838, 0.04093, 0.022622222]
temperature_300 = [0.07863, 0.05158, 0.03781, 0.04263, 0.03129, 0.03128, 0.01959]
temperature_500 = [0.07468, 0.04448, 0.03794, 0.04244, 0.03081, 0.02895, 0.03378]
temperature_700 = [0.08386, 0.04626, 0.02606, 0.05007, 0.03554, 0.02748, 0.02796]
temperature_1000 = [0.07304, 0.04488, 0.03978, 0.04063, 0.03312, 0.0376, 0.02562]

# 第二张子图的数据
temperature_100_w = [0.19292,
                     0.11508,
                     0.082,
                     0.12364,
                     0.0711,
                     0.05047,
                     0.07792
                     ]
temperature_300_w = [0.14867,
                     0.1315,
                     0.10686,
                     0.08119,
                     0.08626,
                     0.07497,
                     0.07306
                     ]
temperature_500_w = [0.20506,
                     0.12559,
                     0.09895,
                     0.10075,
                     0.07614,
                     0.07417,
                     0.06381
                     ]
temperature_700_w = [0.14991,
                     0.09535,
                     0.06768,
                     0.07607,
                     0.07157,
                     0.0705,
                     0.06031
                     ]
temperature_1000_w = [0.15077,
                      0.10004,
                      0.09136,
                      0.07667,
                      0.09328,
                      0.06377,
                      0.04082
                      ]

# 绘制6张子图
plt.figure(figsize=(12, 8))

# 第一个子图
plt.subplot(1, 2, 1)
plt.plot( temperature_100, marker='o', label='100')
plt.plot(temperature_300, marker='s', label='300')
plt.plot( temperature_500, marker='^', label='500')
plt.plot( temperature_700, marker='D', label='700')
plt.plot(temperature_1000, marker='*', label='1000')
plt.title('(a)Symmetric Algorithm Layer 1')
plt.xlabel('File Size (MB)')
plt.ylabel('Runtime (Seconds)')
plt.grid(True)
plt.legend()

# 第二个子图
plt.subplot(1, 2, 2)
plt.plot(temperature_100_w, marker='o', label='100')
plt.plot(temperature_300_w, marker='s', label='300')
plt.plot(temperature_500_w, marker='^', label='500')
plt.plot(temperature_700_w, marker='^', label='700')
plt.plot(temperature_1000_w, marker='^', label='1000')
plt.title('(b)Symmetric Algorithm Layer 2')
plt.xlabel('File Size (MB)')
plt.ylabel('Runtime (Seconds)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
