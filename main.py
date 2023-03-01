import networkx as nx
import core.function as fc
import core.fileHandle as fh
import time
import matplotlib.pyplot as plt
import save as save


def paint(G):
    # 生成节点位置序列（）
    pos = nx.spring_layout(G)
    # 重新获取权重序列
    weights = nx.get_edge_attributes(G, "weight")
    # 画节点图
    nx.draw_networkx(G, pos, with_labels=True)
    # 画权重图
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title(str)
    plt.show()


# 递归函数,weight是当前以求得的最优社区的最小权重
def Recursion(C, R, h):
    global H
    global weight_max
    # 求出最大边值，开始递归
    max_edge = get_max_edge(G, C, R)
    fun = fc.Function(G, q, h)
    # 如果C满足个数且最小权重更大,更新H和最小权重
    if len(C) == h and fun.get_min_weight(C) > weight_max:
        H = C[:]
        weight_max = fun.get_min_weight(C)
        print("更新社区:", H, "最小权重为：", weight_max)

    # 剪枝1，对候选集R进行剪枝
    R = fun.reduce1(C, R, weight_max, max_edge)
    # 剪枝2，对部分解C进行剪枝
    weight_upperbound1 = fun.get_weight_upperbound(C, R, max_edge)
    weight_upperbound2 = fun.neighbor_reconstruct_weight(C, R, max_edge)
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


# 求出针对当前C和R的最大边
def get_max_edge(G, P, C):
    value = 0
    P_and_C = list(set(P).union(C))
    P_and_C_graph = nx.subgraph(G, P_and_C)
    for v in P:
        for i in nx.neighbors(P_and_C_graph, v):
            temp_value = P_and_C_graph.get_edge_data(v, i)['weight']
            if temp_value > value:
                value = temp_value
    return value


# 主算法
def WBS(G, q, h):
    global H
    global weight_max
    function = fc.Function(G, q, h)
    H = function.WSHeuristic(q, h)  # 调用WSHeuristic算法计算一个可行社区H
    weight_max = function.get_min_weight(H)  # 计算初始社区的最小权重,是为最优社区的下界
    # 开始递归,初始R为所有节点
    R = list(G.nodes)
    R.remove(q)
    Recursion([q], R, h)  # 初始最优社区就是SCheu算出的可行社区H
    return H


'''
数据集的查询结点：
wiki-vote:7
bitcoin:1
email-weight:256
dblp:247
dblp:354
lastfm:81
'''
if __name__ == '__main__':
    filename = "dataset/bitcoinJa.csv"
    Glist = fh.csvResolve(filename)
    G = nx.Graph()
    G.add_weighted_edges_from(Glist)

    q = 1  # 查询节点和社区大小
    size = 7

    print("数据的节点数量", len(G.nodes))
    print("数据的边数量", len(G.edges))
    global H
    global weight_max
    function = fc.Function(G, q, size)
    start_time = time.time()
    result = WBS(G, q, size)
    end_time = time.time()
    # 最小影响力

    min_influential = function.get_min_weight(H)
    # 最小度
    min_degree = function.minDegree(nx.subgraph(G, H))
    print("耗时", end_time - start_time)
    print("社区的最小权重", min_influential,
          "最小度", min_degree)
    save.save_txt(filename, q, min_influential, end_time - start_time, min_degree)
    fc.paint(Glist, result, "weightOnly")
