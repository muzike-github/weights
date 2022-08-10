"""
各种功能函数
"""
import copy
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


# 计算节点u在图C中的权重,参数C的类型为networkx的图
def get_weight(G, u):
    weight = 0
    for i in nx.neighbors(G, u):
        weight += G.get_edge_data(u, i)['weight']
    return weight


class Function:
    def __init__(self, G, q):
        self.G = G
        self.q = q

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
    def weight_score(self, C,R):
        copyC = C.copy()  # 用copyC 代替C的所有操作,否则求完连接分数后C会改变
        scoreDict = {}  # 字典保存R中每个节点的连接分数
        # R = []  # todo: 候选集，此处可以优化
        # for v in C:  # 候选集应该是C中所有节点的所有邻居
        #     for i in nx.neighbors(self.G, v):
        #         if i not in C:
        #             R.append(i)
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
        # print("查询节点", q, "的度为：", self.G.degree(q))
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
            soreDict = self.weight_score(H,R)
            # print(soreDict)
            scoreMaxNode = max(soreDict, key=soreDict.get)
            H.append(scoreMaxNode)  # S=S∪{V*}
        if len(H) == 0:
            H = [q]
        print("权重分数启发式算法得到的可行社区为:", H, "最小权重：", self.get_min_weight(H))
        print("启发式算法结束")
        return H

    # 缩减规则1（对R中节点进行修剪）
    def reduce1(self, C, R, h, min_weight):
        RCopy = R.copy()  # 利用copy数组循环，去改变
        for i in RCopy:
            CAndI = list(set(C).union({i}))
            CAndIGraph = nx.subgraph(self.G, CAndI)  # 图C∪{i}
            CAndRGraph = nx.subgraph(self.G, list(set(C).union(set(R))))  # 图C∪R
            RGraph = nx.subgraph(self.G, R)  # 图R
            # 首先要看该节点是否与部分解C连通（）
            connected = False
            for t in C:
                if nx.has_path(CAndIGraph, i, t):
                    connected = True
            # 如果该节点与C中每一个节点都不连通，删除之
            if not connected:
                R.remove(i)
                continue
            # max_node_count表示该节点最多可能再和h - len(C) - 1个节点相连
            max_node_count = h - len(C) - 1
            # 列表存储节点i的邻居边
            neighbor_weight_list = []
            # 计算i在图C∪R中的最大权值
            weight1 = get_weight(CAndRGraph, i)
            # 计算i在图C∪{i}中的权值（再加上几条最大的邻居边）
            weight2 = get_weight(CAndIGraph, i)
            # 遍历i在图R中的所有邻居
            for j in nx.neighbors(RGraph, i):
                neighbor_weight_list.append(RGraph.get_edge_data(i, j)['weight'])
            # 排序后取最大的前max_node_count个,或者不够就将剩下的都加上
            sorted(neighbor_weight_list, reverse=True)
            for t in range(0, min(max_node_count, len(neighbor_weight_list))):
                weight2 += neighbor_weight_list[t]
            # 取二者最小值和当前社区最小值比较，如果小于就删去
            if min(weight1, weight2) < min_weight:
                R.remove(i)
        return R

    # 计算部分解C的权重上界
    def get_weight_upperbound(self, C, R, h):
        # 存放C中所有节点的理想最小权重
        node_weight_list = []
        CAndR = list(set(C).union(set(R)))
        CAndRGraph = nx.subgraph(self.G, CAndR)
        CGraph = nx.subgraph(self.G, C)
        length_C = len(C)
        # 遍历C
        for i in C:
            RAndI = list(set(R).union({i}))
            RAndIGraph = nx.subgraph(self.G, RAndI)
            # 计算i在图C∪R中的最大权值
            weight1 = get_weight(CAndRGraph, i)
            # 计算i在图C中的权值，再加上几条最大的邻居边
            weight2 = get_weight(CGraph, i)
            # 存放每个节点在R中的邻居边
            neighbor_weight_list = []
            for j in nx.neighbors(RAndIGraph, i):
                neighbor_weight_list.append(RAndIGraph.get_edge_data(i, j)['weight'])
            # 排序后取h-len(C)条边
            sorted(neighbor_weight_list, reverse=True)
            for t in range(0, min(h - length_C, len(neighbor_weight_list))):
                weight2 += neighbor_weight_list[t]
            # 取较小值作为节点的理想最大权重
            node_weight_list.append(min(weight1, weight2))
        upper_weight = min(node_weight_list)
        # 计算整个部分解C中最小权重上界
        return upper_weight
