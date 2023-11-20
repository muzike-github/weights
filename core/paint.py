import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

'''
数据可视化
'''

plt.rcParams['figure.figsize'] = (4, 3)
plt.rcParams['xtick.labelsize'] = 18
plt.rcParams['ytick.labelsize'] = 18
plt.rcParams['lines.markersize'] = 8
# FPB算法和BRB算法 算法质量比对
def algorithm_quality():
    x_list = ['ssbo', 'FaceBook', 'Wiki-Vote', 'HR-edges']  # 横坐标，代表数据集
    # x_list = ['SSBO', 'FB', 'WV', 'HR']  # 横坐标，代表数据集
    y1 = [0.844, 1.211, 1.069, 0.665]  # FPB算法
    y2 = [0.587, 0.951, 0.731, 0.475]  # BRB算法
    y3 = [0.1, 0.986, 0.031, 0.1]  # GreedyF
    width = 0.2  # 柱状图的宽度
    x = np.arange(len(x_list))
    plt.bar(x, y1, width=width, label="FPB", )
    plt.bar(x + width, y2, width=width, label="BRB")
    plt.bar(x + width * 2, y3, width=width, label="GreedyF")
    plt.xticks(x + width / 2, x_list, fontsize=12)
    plt.yticks(fontsize=12)
    plt.xlabel('dataset', fontsize=12)
    plt.ylabel('min_influence', fontsize=12)
    plt.legend(fontsize=10)  # 显示标签
    plt.savefig("algorithm_quality_influence.eps", dpi=300, bbox_inches='tight')
    plt.show()


# algorithm_quality()


# FPB算法和BRB算法 算法质量比对(最小度)
def algorithm_quality_degree():
    x_list = ['ssbo', 'FaceBook', 'Wiki-Vote', 'HR-edges']  # 横坐标，代表数据集
    # y1 = [6, 4, 6, 3]  # FPB算法
    # y2 = [6, 6, 6, 4]  # BRB算法
    # y3 = [1, 3, 1, 1]  # GreedyF
    y1 = [4.3, 4.5, 4.8, 2.8]  # FPB算法
    y2 = [5.5, 5.8, 5.3, 3.5]  # BRB算法
    y3 = [0.9, 2.5, 0.6, 0.5]  # GreedyF
    width = 0.2  # 柱状图的宽度
    x = np.arange(len(x_list))
    plt.bar(x, y1, width=width, label="FPB", )
    plt.bar(x + width, y2, width=width, label="BRB")
    plt.bar(x + width * 2, y3, width=width, label="GreedyF")
    plt.xticks(x + width / 2, x_list, fontsize=12)
    plt.xlabel('dataset', fontsize=12)
    plt.ylabel('min_degree', fontsize=12)
    plt.legend(fontsize=10)  # 显示标签
    plt.savefig("algorithm_quality_degree.eps", dpi=300, bbox_inches='tight')
    plt.show()


# algorithm_quality_degree()


# wiki-vote数据集算法效率对比
def wiki_vote_efficiency():
    # 建立坐标系
    x_list = ['4', '5', '6', '7', '8']  # 横坐标，社区大小
    y1 = [15, 23, 50, 121, 189]  # FPB
    y2 = [1, 227, 240, 125, 128]  # BRB
    y3 = [2286, 8000, 10000, 10000, 10000]  # baseline
    y4 = [0.2, 0.2, 0.2, 0.2, 0.2]
    y_tick = [pow(10, i) for i in range(0, 5)]
    plt.semilogy(x_list, y1, 's-', alpha=0.5, linewidth=1, label='FPB', markersize='8')
    plt.semilogy(x_list, y2, 'o-', alpha=0.5, linewidth=1, label='BRB', markersize='8')
    plt.semilogy(x_list, y3, '^-', alpha=0.5, linewidth=1, label='baseline', markersize='8')
    plt.semilogy(x_list, y4, '*-', alpha=0.5, linewidth=1, label='GreedyF', markersize='8')
    plt.legend(facecolor='none', markerscale=0.5, fontsize=12)
    plt.xticks(x_list, fontsize=18)
    plt.xlabel('size', fontsize=18)
    plt.ylabel('runtime(s)', fontsize=18)
    plt.yticks(y_tick, fontsize=18)
    plt.savefig("wiki_vote_efficiency.eps", dpi=300, bbox_inches='tight')
    plt.show()


# wiki_vote_efficiency()

# facebook数据集算法效率对比
def facebook_efficiency():
    x_list = ['4', '5', '6', '7', '8']  # 横坐标，社区大小
    y1 = [2.7, 6.6, 59, 68, 252]  # FPB
    y2 = [0.9, 1.1, 1.4, 1.7, 1.5]  # BRB
    y3 = [5286, 9000, 15000, 15000, 15000]  # baseline
    y4 = [0.2, 0.2, 0.2, 0.2, 0.2]
    y_tick = [pow(10, i) for i in range(0, 5)]
    plt.semilogy(x_list, y1, 's-', alpha=0.5, linewidth=1, label='FPB', markersize='8')
    plt.semilogy(x_list, y2, 'o-', alpha=0.5, linewidth=1, label='BRB', markersize='8')
    plt.semilogy(x_list, y3, '^-', alpha=0.5, linewidth=1, label='baseline', markersize='8')
    plt.semilogy(x_list, y4, '*-', alpha=0.5, linewidth=1, label='GreedyF', markersize='8')
    plt.legend(facecolor='none', markerscale=0.5, fontsize=11, bbox_to_anchor=(0.42, 0.4))
    plt.xticks(x_list, fontsize=18)
    plt.xlabel('size', fontsize=18)
    plt.ylabel('runtime(s)', fontsize=18)
    plt.yticks(y_tick, fontsize=18)
    plt.savefig("facebook_efficiency.eps", dpi=300, bbox_inches='tight')
    plt.show()


# facebook_efficiency()


def facebook_nodeChoose_strategy():
    x_list = ['4', '5', '6', '7', '8']  # 横坐标，社区大小
    y1 = [2.7, 6.6, 46, 68, 237]  # score
    y2 = [1.1, 9, 164, 269, 4756]  # random
    y3 = [0.2, 0.3, 113, 116, 535]  # weight
    y_tick = [pow(10, i) for i in range(0, 5)]
    # y_label = [pow(10, i) for i in range(0, 4)]
    # y_label.append('inf')
    plt.semilogy(x_list, y1, '*-', alpha=0.5, linewidth=1, label='score', markersize='8')
    plt.semilogy(x_list, y2, '^-', alpha=0.5, linewidth=1, label='random', markersize='8')
    plt.semilogy(x_list, y3, '+-', alpha=0.5, linewidth=1, label='weight', markersize='8')
    plt.legend(facecolor='none', markerscale=0.5, fontsize=14)
    plt.xlabel('size', fontsize=18)
    plt.ylabel('runtime(s)', fontsize=18)
    plt.xticks(x_list, fontsize=18)
    plt.yticks(y_tick, fontsize=18)
    plt.title("Facebook", fontsize=18)
    plt.savefig("facebook_nodeChoose_strategy.eps", dpi=300, bbox_inches='tight')
    plt.show()


# facebook_nodeChoose_strategy()

def wiki_vote_nodeChoose_strategy():
    x_list = ['4', '5', '6', '7', '8']  # 横坐标，社区大小
    y1 = [15, 23, 50, 121, 189]  # score
    y2 = [11, 44, 309, 1360, 9756]  # random
    y3 = [15, 55, 172, 759, 2248]  # weight
    y_tick = [pow(10, i) for i in range(0, 5)]
    # y_label = [pow(10, i) for i in range(0, 4)]
    # y_label.append('inf')
    plt.semilogy(x_list, y1, '*-', alpha=0.5, linewidth=1, label='score', markersize='8')
    plt.semilogy(x_list, y2, '^-', alpha=0.5, linewidth=1, label='random', markersize='8')
    plt.semilogy(x_list, y3, '+-', alpha=0.5, linewidth=1, label='weight', markersize='8')
    plt.legend(facecolor='none', markerscale=0.5, fontsize=14, loc='upper left')
    plt.xticks(x_list, fontsize=18)
    plt.yticks(y_tick, fontsize=18)
    plt.xlabel('size', fontsize=18)
    plt.ylabel('runtime(s)', fontsize=18)
    plt.title("wiki-vote", fontsize=18)
    plt.savefig("wiki_vote_nodeChoose_strategy.eps", dpi=300, bbox_inches='tight')
    plt.show()


# wiki_vote_nodeChoose_strategy()
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
    plt.semilogy(x_list, y1, '*-', alpha=0.5, linewidth=1, label='FPB', markersize='8')
    plt.semilogy(x_list, y2, '^-', alpha=0.5, linewidth=1, label='FPB\F', markersize='8')
    plt.semilogy(x_list, y3, '+-', alpha=0.5, linewidth=1, label='FPB\P', markersize='8')
    plt.semilogy(x_list, y4, 'v-', alpha=0.5, linewidth=1, label='FPB\B', markersize='8')
    plt.legend(facecolor='none', markerscale=0.5, fontsize=11, loc='upper left')
    plt.xlabel('size',fontsize=18)
    plt.ylabel('runtime(s)',fontsize=18)
    plt.xticks(fontsize=18)
    plt.yticks(y_tick,fontsize=18)
    plt.title('facebook',fontsize=18)
    plt.savefig("facebook_different_strategy.eps", dpi=300, bbox_inches='tight')
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
    plt.semilogy(x_list, y1, '*-', alpha=0.5, linewidth=1, label='FPB', markersize='8')
    plt.semilogy(x_list, y2, '^-', alpha=0.5, linewidth=1, label='FPB\F', markersize='8')
    plt.semilogy(x_list, y3, '+-', alpha=0.5, linewidth=1, label='FPB\P', markersize='8')
    plt.semilogy(x_list, y4, 'v-', alpha=0.5, linewidth=1, label='FPB\B', markersize='8')
    plt.legend(facecolor='none', markerscale=0.5, fontsize=11, loc='lower right')
    plt.xlabel('size',fontsize = 18)
    plt.ylabel('runtime(s)',fontsize = 18)
    plt.yticks(y_tick)
    plt.title('wiki-vote',fontsize = 18)
    plt.savefig("wiki_vote_different_strategy.eps", dpi=300, bbox_inches='tight')
    plt.show()

# algorithm_quality()
# facebook_efficiency()
# wiki_vote_efficiency()
# facebook_nodeChoose_strategy()
# wiki_vote_nodeChoose_strategy()
# facebook_different_strategy()
# wiki_vote_different_strategy()
algorithm_quality_degree()
algorithm_quality()