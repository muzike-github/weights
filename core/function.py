"""
各种功能函数
"""
import copy
import heapq

import networkx as nx
import matplotlib.pyplot as plt


# 画图函数
def paint(GList, H, str):
    # 添加加权边
    G = nx.Graph()
    G.add_weighted_edges_from(GList)
    if len(H) != 0:
        G = nx.subgraph(G, H)
    # 生成节点位置序列（）
    pos = nx.circular_layout(G)
    # 重新获取权重序列
    weights = nx.get_edge_attributes(G, "weight")
    # 画节点图
    nx.draw_networkx(G, pos, with_labels=True)
    # 画权重图
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title(str)
    plt.show()


# 计算节点u在图G中的权重,参数C的类型为networkx的图
def get_weight(G, u):
    weight = 0
    for i in nx.neighbors(G, u):
        weight += G.get_edge_data(u, i)['weight']
    return weight


class Function:
    def __init__(self, G, q, h):
        self.G = G
        self.q = q
        self.h = h

    def minDegree(self, G):
        degrees = []
        for i in G:
            degrees.append(G.degree(i))
        return min(degrees)

    # 求由社区H组成的子图的的最小权重（）
    def get_min_weight(self, H):
        graph = nx.subgraph(self.G, H)
        weights = []
        for i in graph:
            weight = 0
            for j in nx.neighbors(graph, i):  # 遍历节点的所有邻居
                weight += self.G.get_edge_data(i, j)['weight']
            weights.append(weight)
        return min(weights)

        # 计算权重分数用以启发式算法中选取节点

    def weight_score(self, C, R):
        copyC = C.copy()  # 用copyC 代替C的所有操作,否则求完连接分数后C会改变
        scoreDict = {}  # 字典保存R中每个节点的连接分数
        for v in R:
            graphC = nx.subgraph(self.G, copyC)  # 得到图C
            copyC.append(v)
            graphCAndV = nx.subgraph(self.G, copyC)  # 得到节点集C∪{v}的在G中的子图
            score = 0
            # 此处判断v是否在C∪{v}中是否有邻居，没有邻居，分数为0
            if len(list(nx.neighbors(graphCAndV, v))) != 0:
                # 有邻居但邻居在C中度为0，则设置score为0
                for i in nx.neighbors(graphCAndV, v):  # 得到v(v∈R)在C∪{v}所有的邻居节点
                    if graphC.degree(i) != 0:
                        score += (1 / graphC.degree(i))
                        score = round(score, 2)
                    else:
                        score = 0
            # 如果v没有邻居，则直接分数为0
            else:
                score = 0
            scoreDict[v] = score  # 将对应节点的连接分数存储
            copyC.remove(v)  # 节点v测试完毕，移除
        scoreMaxNode = max(scoreDict, key=scoreDict.get)
        return scoreDict

    # 启发式算法计算初始可行社区
    def WSHeuristic(self, q, h):
        print("===========权重分数启发式算法开始=============")
        print("查询节点", q, "的度为：", self.G.degree(q))
        H = [q]  # 初始为查询节点
        # 如果只有一个节点，选取所有邻居中度数最大的节点
        if len(H) == 1:
            degree = 0
            node = None
            for i in nx.neighbors(self.G, H[0]):
                if self.G.degree(i) > degree:
                    node = i
            if node is None:
                print("第二个节点为空，有问题")
                exit(-1)
            H.append(node)
        print("第二个节点是", H)
        while len(H) < h:
            # 找出G\H中连接分数最大的节点V*
            R = list(set(self.G.nodes).difference(set(H)))
            soreDict = self.weight_score(H, R)
            # print(soreDict)
            scoreMaxNode = max(soreDict, key=soreDict.get)
            H.append(scoreMaxNode)  # S=S∪{V*}
        if len(H) == 0:
            H = [q]
        print("权重分数启发式算法得到的可行社区为:", H, "最小权重：", self.get_min_weight(H))
        print("启发式算法结束")
        return H

    # 　距离缩减
    # todo 是否采取距离缩减公式
    # 缩减规则1（删除R中影响力较低的节点）
    def reduce1(self, P, C, min_weight,max_edge_value):
        # 需要删除的元素
        delete = []
        for v in C:
            P_and_C = list(set(P).union(C))
            P_and_C_graph = nx.subgraph(self.G, P_and_C)
            # 计算节点v在P∪C中的权重
            w1 = get_weight(P_and_C_graph, v)
            # 计算节点v在P∪{v}中的权重并加上（h-|P|-1）*W_max
            P_and_v = list(set(P).union({v}))
            P_and_v_graph = nx.subgraph(self.G, P_and_v)
            w2 = get_weight(P_and_v_graph, v)
            w2 += max_edge_value * (self.h - len(P) - 1)
            if min(w1, w2) < min_weight:
                delete.append(v)
        # 删除节点
        for i in delete:
            C.remove(i)
        return C

    # 计算部分解C的权重上界
    def get_weight_upperbound(self, P, C, max_edge_value):
        # 存放部分解P中所有节点的最小权重(计算后)
        nodes_weight = []
        C_graph = nx.subgraph(self.G, P)
        # 遍历C中每个节点，计算每个节点的理想最大权重
        for u in P:
            P_and_u = list(set(C).union({u}))
            P_and_u_graph = nx.subgraph(self.G, P_and_u)
            # 计算u在P∪C中的权重
            w1 = get_weight(P_and_u_graph, u)
            # 计算u在图C中的权值，再加上（h-|P|）*w_max
            w2 = get_weight(C_graph, u)
            w2 += max_edge_value * (self.h - len(P))
            upperbound = min(w1, w2)
            nodes_weight.append(upperbound)
        upper_bound = min(nodes_weight)
        return upper_bound

    # 基于邻域重构
    # 　基于度的上界在考虑的时候认为R可以无限大的满足C中节点的要求，但是其实R也是有限制的
    def neighbor_reconstruct_weight(self, P, C, max_edge_value):
        P_graph = nx.subgraph(self.G, P)
        P_and_C_graph = nx.subgraph(self.G, list(set(P).union(set(C))))
        # 从R中取h-|C|个在C中有最多邻居数的节点记为R'
        # todo 此处是取度数最大的还是影响力最大的
        max_node_count = self.h - len(P)
        # 记录
        neighbor_count_dict = {}
        u_in_P_weight_dict = {}
        # 遍历P，记录P中各个节点的权重
        for u in P:
            u_in_P_weight_dict[u] = 0
            u_in_P_weight_dict[u] += get_weight(P_graph, u)
        # 遍历C，记录候选集中每个节点在C∪{v}中的权重,以及度数取出前max_count个节点
        for v in C:
            C_and_v_graph = nx.subgraph(self.G, list(set(C).union({v})))
            # 记录节点对应的度数
            neighbor_count_dict[v] = len(list(nx.neighbors(C_and_v_graph, v)))
        # 求出前n个具有最大邻居数的
        top_n = dict(heapq.nlargest(max_node_count, neighbor_count_dict.items(), key=lambda x: x[1]))

        # 遍历neighbor_dict,从P中选取影响力值最小的neighbor_dict[v]个节点，加上最大值
        for v in top_n.keys():
            v_and_C_graph = nx.subgraph(P_and_C_graph, list(set(P).union({v})))
            # C中取权重最小的neighbor_count_dict[v]个节点，加上最大边
            smallest_n_dict = dict(
                heapq.nsmallest(neighbor_count_dict[v], u_in_P_weight_dict.items(), key=lambda x: x[1]))
            for node in smallest_n_dict.keys():
                u_in_P_weight_dict[node] += max_edge_value
        upper_weight = min(u_in_P_weight_dict.values())
        # print(upper_weight)
        return upper_weight
