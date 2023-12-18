import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

'''
数据可视化
'''


# FPB算法和BRB算法 算法质量比对
def algorithm_quality():
    x_list = ['ssbo', 'FaceBook', 'WikiVote', 'HR_edges']  # 横坐标，代表数据集
    y1 = [0.377, 1.233, 0.365, 0.665]  # FPB算法
    y2 = [0.232, 1, 0.317, 0.311]  # BRB算法
    y3 = []
    width = 0.35
    x = np.arange(len(x_list))
    plt.bar(x, y1, width=width, label="FPB", )
    plt.bar(x + width, y2, width=width, label="BRB")
    plt.xticks(x + width / 2, x_list)
    plt.xlabel('dataset')
    plt.ylabel('min_influence')
    plt.legend()  # 显示标签
    plt.show()


# wiki-vote数据集算法效率对比
def wiki_vote_efficiency():
    # 建立坐标系
    x_list = ['4', '5', '6', '7', '8']  # 横坐标，社区大小
    y1 = [15, 23, 50, 121, 189]  # FPB
    y2 = [1, 227, 240, 125, 128]  # BRB
    y3 = [2286, 8000, 10000, 10000, 10000]  # baseline
    y_tick = [pow(10, i) for i in range(0, 5)]
    y_label = [pow(10, i) for i in range(0, 4)]
    y_label.append('inf')
    plt.semilogy(x_list, y1, 's-', alpha=0.5, linewidth=1, label='FPB')
    plt.semilogy(x_list, y2, 'o-', alpha=0.5, linewidth=1, label='BRB')
    plt.semilogy(x_list, y3, '^-', alpha=0.5, linewidth=1, label='baseline')
    plt.legend()
    plt.xlabel('size')
    plt.ylabel('runtime(s)')
    plt.yticks(y_tick, y_label)
    plt.show()


# facebook数据集算法效率对比
def facebook_efficiency():
    x_list = ['4', '5', '6', '7', '8']  # 横坐标，社区大小
    y1 = [2.7, 6.6, 59, 68, 252]  # FPB
    y2 = [0.9, 1.1, 1.4, 1.7, 1.5]  # BRB
    y3 = [5286, 9000, 10000, 10000, 10000]  # baseline
    y_tick = [pow(10, i) for i in range(0, 5)]
    y_label = [pow(10, i) for i in range(0, 4)]
    y_label.append('inf')
    plt.semilogy(x_list, y1, 's-', alpha=0.5, linewidth=1, label='FPB')
    plt.semilogy(x_list, y2, 'o-', alpha=0.5, linewidth=1, label='BRB')
    plt.semilogy(x_list, y3, '^-', alpha=0.5, linewidth=1, label='baseline')
    plt.legend()
    plt.xlabel('size')
    plt.ylabel('runtime(s)')
    plt.yticks(y_tick, y_label)
    plt.show()


# 去除某种剪枝操作对算法效率的影响
# FaceBook
def facebook_different_strategy():
    x_list = ['4', '5', '6', '7', '8']  # 横坐标，社区大小
    y1 = [2.7, 6.6, 59, 68, 252]  # FPB
    y2 = [19, 40, 349, 467, 1955]  # FPB\F
    y3 = [1.46, 14, 431, 2364, 9456]  # FPB\P
    y4 = [1.53, 4.5, 176, 312, 758]  # FPB\B
    y_tick = [pow(10, i) for i in range(0, 5)]
    # y_label = [pow(10, i) for i in range(0, 4)]
    # y_label.append('inf')
    plt.semilogy(x_list, y1, '*-', alpha=0.5, linewidth=1, label='FPB')
    plt.semilogy(x_list, y2, '^-', alpha=0.5, linewidth=1, label='FPB\F')
    plt.semilogy(x_list, y3, '+-', alpha=0.5, linewidth=1, label='FPB\P')
    plt.semilogy(x_list, y4, 'v-', alpha=0.5, linewidth=1, label='FPB\B')
    plt.legend()
    plt.xlabel('size')
    plt.ylabel('runtime(s)')
    plt.yticks(y_tick)
    plt.title("facebook")
    plt.show()


# wiki-vote

def wiki_vote_different_strategy():
    x_list = ['4', '5', '6', '7', '8']  # 横坐标，社区大小
    y1 = [15, 23, 50, 121, 189]  # FPB
    y2 = [215, 432, 4593, 20000, 20000]  # FPB\F
    y3 = [11, 32, 191, 4421, 20000]  # FPB\P
    y4 = [12, 46, 320, 976, 10000]  # FPB\B
    y_tick = [pow(10, i) for i in range(0, 5)]
    # y_label = [pow(10, i) for i in range(0, 4)]
    # y_label.append('inf')
    plt.semilogy(x_list, y1, '*-', alpha=0.5, linewidth=1, label='FPB')
    plt.semilogy(x_list, y2, '^-', alpha=0.5, linewidth=1, label='FPB\F')
    plt.semilogy(x_list, y3, '+-', alpha=0.5, linewidth=1, label='FPB\P')
    plt.semilogy(x_list, y4, 'v-', alpha=0.5, linewidth=1, label='FPB\B')
    plt.legend()
    plt.xlabel('size')
    plt.ylabel('runtime(s)')
    plt.yticks(y_tick)
    plt.title("wiki-vote")
    plt.show()





def facebook_nodeChoose_strategy():
    x_list = ['4', '5', '6', '7', '8']  # 横坐标，社区大小
    y1 = [2.7, 6.6, 46, 68, 237]  # score
    y2 = [1.1, 9, 164, 269, 4756]  # random
    y3 = [0.2, 0.3, 113, 116, 535]  # weight
    y_tick = [pow(10, i) for i in range(0, 5)]
    # y_label = [pow(10, i) for i in range(0, 4)]
    # y_label.append('inf')
    plt.semilogy(x_list, y1, '*-', alpha=0.5, linewidth=1, label='score')
    plt.semilogy(x_list, y2, '^-', alpha=0.5, linewidth=1, label='random')
    plt.semilogy(x_list, y3, '+-', alpha=0.5, linewidth=1, label='weight')
    plt.legend()
    plt.xlabel('size')
    plt.ylabel('runtime(s)')
    plt.yticks(y_tick)
    plt.title("facebook")
    plt.show()


def wiki_vote_nodeChoose_strategy():
    x_list = ['4', '5', '6', '7', '8']  # 横坐标，社区大小
    y1 = [15, 23, 50, 121, 189]  # score
    y2 = [11, 44, 309, 1360, 9756]  # random
    y3 = [15, 55, 172, 759, 2248]  # weight
    y_tick = [pow(10, i) for i in range(0, 5)]
    # y_label = [pow(10, i) for i in range(0, 4)]
    # y_label.append('inf')
    plt.semilogy(x_list, y1, '*-', alpha=0.5, linewidth=1, label='score')
    plt.semilogy(x_list, y2, '^-', alpha=0.5, linewidth=1, label='random')
    plt.semilogy(x_list, y3, '+-', alpha=0.5, linewidth=1, label='weight')
    plt.legend()
    plt.yticks(y_tick)
    plt.xlabel('size')
    plt.ylabel('runtime(s)')
    plt.title("wiki_vote")
    plt.show()


# facebook_nodeChoose_strategy()
# wiki_vote_nodeChoose_strategy()
facebook_different_strategy()
wiki_vote_different_strategy()