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
def pre_byDistance(G, query_node):
    # 如果图有多个连通分量，则筛选只包含查询结点的那个
    print("删减前：", len(G.nodes))
    components = [c for c in nx.connected_components(G) if query_node in c]
    nodes = list(components[0])
    filter_graph = nx.Graph(nx.subgraph(G, nodes))
    print("删减后", len(filter_graph.nodes))
    print("删减后连通分量", len(list(nx.connected_components(filter_graph))))
    # 根据距离进一步筛选
    delete_list = []
    for v in filter_graph.nodes:
        if not nx.has_path(G, v, query_node) or nx.shortest_path_length(G, v, query_node) > int(size / 2):
            delete_list.append(v)
    for i in delete_list:
        filter_graph.remove_node(i)
    return filter_graph


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
# email结点
# nodes=[176,256,238,25,135,7]
# wiki
# nodes = [133, 7, 231, 3073, 25, 1489, 1137, 6596, 813, 1166]
# facebook
nodes = [715,751,430,436,1026,1339,2203,2336,2244,0]
if __name__ == '__main__':
    for node in nodes:
        # q = eval(input("查询节点:"))  # 查询节点和社区大小
        size = 4
        query_node = node
        H = []
        weight_min = 0
        filename = "dataset/facebook.csv"
        Glist = fh.csvResolve(filename)
        # Glist = node_list
        G = nx.Graph()
        G.add_weighted_edges_from(Glist)
        # 预处理
        # G = pre_byDistance(G, query_node)
        # print("connect",len(list(nx.connected_components(G))))

        start_time = time.time()
        fun = fc.Function(G, query_node)
        print("数据的节点数量", len(G.nodes))
        print("数据的边数量", len(G.edges))

        result = WBS(G, query_node, size)
        end_time = time.time()
        # 最小影响力
        min_influential = fun.get_min_weight(H)
        # 最小度
        min_degree = fun.minDegree(nx.subgraph(G, H))
        print("社区大小", size)
        print("耗时", end_time - start_time)
        print("社区的最小权重", min_influential,
              "最小度", min_degree)
        save.save_txt(filename, len(G.nodes), len(G.edges), query_node, min_influential, end_time - start_time,
                      min_degree)
        # fc.paint(Glist, result, "weightOnly")
