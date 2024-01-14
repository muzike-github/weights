import networkx as nx
import core.function as fc
import core.fileHandle as fh
import time
import matplotlib.pyplot as plt
import save as save

node_list = [(0, 1, 7), (0, 2, 4), (0, 3, 2), (0, 4, 6), (0, 5, 9),
             (1, 4, 8), (2, 3, 5), (2, 5, 8), (3, 4, 10),
             (4, 5, 8), (4, 6, 9), (4, 9, 10),
             (5, 6, 10), (5, 7, 8), (5, 8, 7),
             (6, 7, 7), (6, 8, 10), (7, 8, 9), (8, 9, 7)]


# 根据距离对R进行预处理
def pre_byDistance(G):
    delete_list = []
    for v in G.nodes:
        if not nx.has_path(G, v, q) or nx.shortest_path_length(G, v, q) > int(size / 2):
            delete_list.append(v)
    for i in delete_list:
        G.remove_node(i)
    return G


# 递归函数,weight是当前以求得的最优社区的最小权重
def Recursion(C, R, h):
    global H
    global weight_min
    # 如果C满足个数且最小权重更大,更新H和最小权重
    if len(C) == h and fun.get_min_weight(C) > weight_min:
        H = C[:]
        weight_min = fun.get_min_weight(C)
        print("更新社区:", H, "最小权重为：", weight_min, "runtime:", time.time() - start_time)
    # 剪枝1，对候选集R进行剪枝
    R = fun.reduce1(C, R, h, weight_min)
    # 剪枝2，对部分解C进行剪枝
    weight_upperbound1 = fun.get_weight_upperbound(C, R, h)
    weight_upperbound2 = fun.neighbor_reconstruct_weight(C, R, h)
    upperbound = min(weight_upperbound2, weight_upperbound1)
    # 如果C的节点数小于h并且候选集R不为空，且当前部分解的理想最小权重大于weight
    if len(C) < h and len(R) != 0 and upperbound > weight_min:
        # 从候选集R中选一个节点生成两个分支
        # 此节点不应当随意选取(采用节点选择策略可降低计算时间)
        # scoreDict = fun.weight_score(C, R)
        # score_max_node = max(scoreDict, key=scoreDict.get)
        v = choose_by_score(C, R)
        # v = choose_random(R)
        # v = choose_by_weight(C, R)
        CAndV = list(set(C).union({v}))
        RExcludeV = list(set(R).difference({v}))
        RExcludeV2 = list(set(R).difference({v}))
        #  此处判断节点v是否和C相连（莫名提高了算法效率）
        if fun.has_path(v, C):
            Recursion(CAndV, RExcludeV, h)
        Recursion(C, RExcludeV2, h)


# 节点选择策略：
# 从R中取权重最大的（与社区C相连）
def choose_by_weight(C, R):
    C_and_R = list(set(C).union(set(R)))
    C_and_R_graph = nx.subgraph(G, C_and_R)
    candidate = {}
    for r in R:
        candidate[r] = (fc.get_weight(C_and_R_graph, r))
    return max(candidate, key=candidate.get)


# 随机选取
def choose_random(R):
    return R[0]


# 连接分数选取：
def choose_by_score(C, R):
    scoreDict = fun.weight_score(C, R)
    score_max_node = max(scoreDict, key=scoreDict.get)
    return score_max_node


# 主算法
def WBS(G, q, h):
    global H
    global weight_min
    H = fun.WSHeuristic(q, h)  # 调用WSHeuristic算法计算一个可行社区H
    weight_min = fun.get_min_weight(H)  # 计算初始社区的最小权重,是为最优社区的下界
    # 开始递归,初始R为所有节点
    R = list(G.nodes)
    R.remove(q)
    Recursion([q], R, h)  # 初始最优社区就是SCheu算出的可行社区H
    return H


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
    q = eval(input("查询节点:"))  # 查询节点和社区大小
    size = 7
    H = []
    weight_min = 0
    filename = "dataset/Brightkite.csv"
    Glist = fh.csvResolve(filename)
    # Glist = node_list
    G = nx.Graph()
    G.add_weighted_edges_from(Glist)
    print(len(G.nodes))
    print(len(G.edges))
    # 预处理
    G = pre_byDistance(G)
    start_time = time.time()
    fun = fc.Function(G, q)
    print("数据的节点数量", len(G.nodes))
    print("数据的边数量", len(G.edges))

    result = WBS(G, q, size)
    end_time = time.time()
    # 最小影响力
    min_influential = fun.get_min_weight(H)
    # 最小度
    min_degree = fun.minDegree(nx.subgraph(G, H))
    print("耗时", end_time - start_time)
    print("社区的最小权重", min_influential,
          "最小度", min_degree)
    save.save_txt(filename, len(G.nodes), len(G.edges), q, min_influential, end_time - start_time, min_degree)
    fc.paint(Glist, result, "weightOnly")
