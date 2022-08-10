import copy

import networkx as nx
import core.function as fc
import core.fileHandle as fh
import time
import sys


# 递归函数,weight是当前以求得的最优社区的最小权重
def Recursion(C, R, h):
    global H
    global weight_max
    # 如果C满足个数且最小权重更大
    if len(C) == h and fun.get_min_weight(C) > weight_max:
        # 更新H和最小权重
        H = C[:]
        weight_max = fun.get_min_weight(C)
        print("更新社区:", H, "最小权重为：", weight_max)
    # 剪枝1，对候选集R进行剪枝
    # R = fun.reduce1(C, R, h, weight_max)
    # 剪枝2，对部分解C进行剪枝
    weight_upperbound = fun.get_weight_upperbound(C, R, h)
    # 如果C的节点数小于h并且候选集R不为空，且当前部分解的理想最小权重大于weight
    if len(C) < h and len(R) != 0 and weight_upperbound > weight_max:
        # 从候选集R中选一个节点生成两个分支
        v = R[0]
        CAndV = list(set(C).union({v}))
        RExcludeV = list(set(R).difference({v}))
        Recursion(CAndV, RExcludeV, h)
        Recursion(C, RExcludeV, h)
# 递归函数
# def Recursion(C, R, h, weight):
#     # 如果C满足个数且最小权重更大
#     if len(C) == h and fun.get_min_weight(C) > weight:
#         print("更新社区:", "凝聚分数为", weight)
#         return C,fun.get_min_weight(C)
#     R = fun.reduce1(C, R, h, weight)
#     weight_bound = fun.get_weight_upperbound(C, R, h)
#     # print("C的分数上界：",Upperbound,"score:",score)
#     # 如果C的节点数小于h并且候选集R不为空
#     if len(C) < h and len(R) != 0 and weight_bound > weight:
#         # 从候选集R中选一个节点生成两个分支
#         v = R[0]
#         CAndV = list(set(C).union({v}))
#         RExcludeV = list(set(R).difference({v}))
#         H1, weight1 = Recursion(CAndV, RExcludeV, h, weight)
#         H2, weight2 = Recursion(C, RExcludeV,h, weight)
#         if weight1 >= weight2:
#             return H1, weight1
#         else:
#             return H2,weight2
#
#     return None, -1


# 主算法
def WBS(G, q, h):
    global H
    global weight_max
    fun = fc.Function(G, q)
    H = fun.WSHeuristic(q, h)  # 调用WSHeuristic算法计算一个可行社区H
    weight_max = fun.get_min_weight(H)  # 计算初始社区的最小权重,是为最优社区的下界
    # scoreUpper = 2  # 上界为最理想情况,社区每个点达到最大值，最小权值也达到最大值
    print("scoreLower:", weight_max)
    # 开始递归,初始R为所有节点
    R = list(G.nodes)
    R.remove(q)
    # 将初始可行社区H作为递归参数，
    Recursion([q], R, h)  # 初始最优社区就是SCheu算出的可行社区H
    return H


if __name__ == '__main__':
    # Glist = [(0, 1, 5), (0, 2, 10), (0, 3, 10), (0, 4, 4), (0, 5, 8), (1, 4, 7),
    #          (2, 3, 1), (2, 5, 10),(2, 7, 8), (3, 4, 1), (4, 5, 7), (4, 6, 6),
    #          (4, 9, 8), (5, 6, 4), (5, 7, 10),(5, 8, 8), (6, 7, 9), (6, 8, 5), (7, 8, 2), (8, 9, 9)]
    #
    # sys.setrecursionlimit(10000)
    start_time = time.time()
    Glist = fh.csvResolve("dataset/emailWeight.csv")
    G = nx.Graph()
    G.add_weighted_edges_from(Glist)
    q = 256  # 查询节点和社区大小
    size = 6
    fun = fc.Function(G, q)
    print("数据的节点数量", len(G.nodes))
    print("数据的边数量", len(G.edges))
    global H
    global weight_max
    result = WBS(G, q, size)
    # wiki-vote数据集，查询节点7
    # bitcoin数据集，查询节点1
    # email-weight数据集，查询节点256
    # result = WBS(G, q, size)
    print("社区的最小权重", fun.get_min_weight(H),
          "最小度", fun.minDegree(nx.subgraph(G, H)))
    end_time = time.time()
    print("耗时", end_time - start_time)
    fc.paint(Glist, result, "weightOnly")
