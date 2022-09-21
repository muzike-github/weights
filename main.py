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
    # 如果C满足个数且最小权重更大,更新H和最小权重
    if len(C) == h and fun.get_min_weight(C) > weight_max:
        H = C[:]
        weight_max = fun.get_min_weight(C)
        print("更新社区:", H, "最小权重为：", weight_max)
    # 剪枝1，对候选集R进行剪枝
    R = fun.reduce1(C, R, h, weight_max)
    # 剪枝2，对部分解C进行剪枝
    weight_upperbound1 = fun.get_weight_upperbound(C, R, h)
    weight_upperbound2 = fun.neighbor_reconstruct_weight(C, R, h)
    upperbound = min(weight_upperbound2, weight_upperbound1)
    # 如果C的节点数小于h并且候选集R不为空，且当前部分解的理想最小权重大于weight
    if len(C) < h and len(R) != 0 and upperbound > weight_max:
        # 从候选集R中选一个节点生成两个分支
        # 此节点不应当随意选取(采用节点选择策略可降低计算时间)
        scoreDict = fun.weight_score(C, R)
        score_max_node = max(scoreDict, key=scoreDict.get)
        # v = R[0]
        v = score_max_node
        CAndV = list(set(C).union({v}))
        RExcludeV = list(set(R).difference({v}))
        Recursion(CAndV, RExcludeV, h)
        RExcludeV2 = list(set(R).difference({v}))
        Recursion(C, RExcludeV2, h)


# 主算法
def WBS(G, q, h):
    global H
    global weight_max
    fun = fc.Function(G, q)
    H = fun.WSHeuristic(q, h)  # 调用WSHeuristic算法计算一个可行社区H
    weight_max = fun.get_min_weight(H)  # 计算初始社区的最小权重,是为最优社区的下界
    # 开始递归,初始R为所有节点
    R = list(G.nodes)
    R.remove(q)
    Recursion([q], R, h)  # 初始最优社区就是SCheu算出的可行社区H
    return H


if __name__ == '__main__':
    start_time = time.time()
    Glist = fh.csvResolve("dataset/wiki-vote.csv")
    G = nx.Graph()
    G.add_weighted_edges_from(Glist)
    q = 7  # 查询节点和社区大小
    size = 8
    fun = fc.Function(G, q)
    print("数据的节点数量", len(G.nodes))
    print("数据的边数量", len(G.edges))
    global H
    global weight_max
    result = WBS(G, q, size)
    print("社区的最小权重", fun.get_min_weight(H),
          "最小度", fun.minDegree(nx.subgraph(G, H)))
    end_time = time.time()
    print("耗时", end_time - start_time)
    fc.paint(Glist, result, "weightOnly")
