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
            soreDict = self.weight_score(H, R)
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
            RGraph = nx.subgraph(self.G, R)  # 图R
            # 首先要看该节点是否与部分解C连通（注意此处是CAndRGraph）
            # connected = False
            # for t in C:
            #     if nx.has_path(CAndRGraph, i, t):
            #         connected = True
            # # 如果该节点与C中每一个节点都不连通，删除之
            # if not connected:
            #     R.remove(i)
            #     continue
            # max_node_count表示该节点最多可能再和h - len(C) - 1个节点相连
            max_node_count = h - len(C) - 1
            # 列表存储节点i的邻居边
            neighbor_weight_list = []
            # 计算i在图C∪{i}中的权值（再加上几条最大的邻居边）
            weight = get_weight(CAndIGraph, i)
            # 遍历i在图R中的所有邻居
            for j in nx.neighbors(RGraph, i):
                neighbor_weight_list.append(RGraph.get_edge_data(i, j)['weight'])
            # 排序后取最大的前max_node_count个,或者不够就将剩下的都加上
            neighbor_weight_list.sort(reverse=True)
            for t in range(0, min(max_node_count, len(neighbor_weight_list))):
                weight += neighbor_weight_list[t]
            # 如果小于就删去
            if weight < min_weight:
                R.remove(i)
        return R

    # 计算部分解C的权重上界
    def get_weight_upperbound(self, C, R, h):
        # 存放C中所有节点的理想最小权重
        node_weight_list = []
        CGraph = nx.subgraph(self.G, C)
        # 遍历C中每个节点，计算每个节点的理想最大权重
        for i in C:
            RAndI = list(set(R).union({i}))
            RAndIGraph = nx.subgraph(self.G, RAndI)
            # 计算i在图C中的权值，再加上几条最大的邻居边
            weight = get_weight(CGraph, i)
            # 存放每个节点在R中的邻居边
            neighbor_weight_list = []
            for j in nx.neighbors(RAndIGraph, i):
                neighbor_weight_list.append(RAndIGraph.get_edge_data(i, j)['weight'])
            # 排序后取h-len(C)条边
            neighbor_weight_list.sort(reverse=True)
            for t in range(0, min(h - len(C), len(neighbor_weight_list))):
                weight += neighbor_weight_list[t]
            node_weight_list.append(weight)
        upper_weight = min(node_weight_list)
        # 计算整个部分解C中最小权重上界
        return upper_weight

    # 基于邻域重构
    # 　基于度的上界在考虑的时候认为R可以无限大的满足C中节点的要求，但是其实R也是有限制的
    def neighbor_reconstruct(self, C, R, h):
        C_graph = nx.subgraph(self.G, C)
        C_and_R_graph = nx.subgraph(self.G, list(set(C).union(set(R))))
        # 从R中取h-|C|个在C中有最多邻居数的节点记为R'
        max_node_count = h - len(C)
        neighbor_count_dict = {}
        # 遍历R，记录每个节点在C∪{r}中的邻居数
        # 先判断该节点是否与C连通
        for r in R:
            r_and_C_graph = nx.subgraph(C_and_R_graph, list(set(C).union({r})))
            neighbor_count_dict[r] = len(list(nx.neighbors(r_and_C_graph, r)))
        # 排序，取出前h-|C|个有最多邻居数的,并对字典按照降序排列
        neighbor_count_dict = dict(heapq.nlargest(max_node_count, neighbor_count_dict.items(), key=lambda x: x[1]))
        print("前n个为", neighbor_count_dict)
        # 记录u(u∈C)在C中的度
        degree_u_in_c = {}
        for u in C:
            degree_u_in_c[u] = C_graph.degree(u)
        # 记录u(u∈C)在C中的权重(后面会对节点进行权重加法)
        weight_u_in_c = {}
        for u in C:
            weight_u_in_c[u] = get_weight(C_graph, u)
        # 遍历neighbor_dict,从C中选取neighbor_dict[v]个节点，
        # 将v的neighbor_dict[v]条边按照大权边连接小权重点的原则进行连接
        for v in neighbor_count_dict:
            edge_list = []  # 存储节点v最大的neighbor_count_dict[v]条边
            v_and_C_graph = nx.subgraph(C_and_R_graph, list(set(C).union({v})))
            for t in nx.neighbors(v_and_C_graph, v):
                edge_list.append(v_and_C_graph.get_edge_data(v, t)['weight'])
            edge_list.sort(reverse=True)  # 降序排列，与下面C中节点刚好相反
            # print(edge_list)
            # C中取权重最小的neighbor_count_dict[v]个节点，
            temp_dict = dict(heapq.nsmallest(neighbor_count_dict[v], weight_u_in_c.items(), key=lambda x: x[1]))
            # print(temp_dict)
            # 计算出节点的权重,开始加边(此处C中节点是从小到大排列)
            count = 0  # 用作记录当前节点要加上edge_list的哪一条边
            for key in temp_dict.keys():
                weight_u_in_c[key] += edge_list[count]
                count = count + 1
        upper_weight = min(weight_u_in_c.values())
        # print(upper_weight)
        return upper_weight

    def neighbor_reconstruct_weight(self, C, R, h):
        C_graph = nx.subgraph(self.G, C)
        C_and_R_graph = nx.subgraph(self.G, list(set(C).union(set(R))))
        # 从R中取h-|C|个在C中有最多邻居数的节点记为R'
        max_node_count = h - len(C)
        neighbor_count_dict = {}
        r_in_C_weight_dict={}
        # 遍历R，记录每个节点在C∪{r}中的权重,以及度数
        for r in R:
            r_and_C_graph = nx.subgraph(C_and_R_graph, list(set(C).union({r})))
            # 记录R中节点的在r_and_C_graph中的度数
            neighbor_count_dict[r] = len(list(nx.neighbors(r_and_C_graph, r)))
            # 记录R中节点的在r_and_C_graph中的权重
            r_in_C_weight_dict[r] = 0
            for e in nx.neighbors(r_and_C_graph, r):
                r_in_C_weight_dict[r] += r_and_C_graph.get_edge_data(e, r)['weight']
        # print(neighbor_count_dict)
        # print(r_in_C_weight_dict)
        # 排序，取出前h-|C|个有最多邻居数的,并对字典按照降序排列
        r_in_C_weight_dict = dict(heapq.nlargest(max_node_count, r_in_C_weight_dict.items(), key=lambda x: x[1]))
        # print("R中前n个权重最大的为", r_in_C_weight_dict)
        # 记录u(u∈C)在C中的权重(后面会对节点进行权重加法)
        weight_u_in_c = {}
        for u in C:
            weight_u_in_c[u] = get_weight(C_graph, u)
        # 遍历neighbor_dict,从C中选取neighbor_dict[v]个节点，
        # 将v的neighbor_dict[v]条边按照大权边连接小权重点的原则进行连接
        for v in r_in_C_weight_dict.keys():
            edge_list = []  # 存储节点v最大的neighbor_count_dict[v]条边
            v_and_C_graph = nx.subgraph(C_and_R_graph, list(set(C).union({v})))
            for t in nx.neighbors(v_and_C_graph, v):
                edge_list.append(v_and_C_graph.get_edge_data(v, t)['weight'])
            edge_list.sort(reverse=True)  # 降序排列，与下面C中节点刚好相反
            # print(edge_list)
            # C中取权重最小的neighbor_count_dict[v]个节点，
            temp_dict = dict(heapq.nsmallest(neighbor_count_dict[v], weight_u_in_c.items(), key=lambda x: x[1]))
            # print("C中权重最小的",neighbor_count_dict[v],"n个节点为",temp_dict)
            # 计算出节点的权重,开始加边(此处C中节点是从小到大排列)
            count = 0  # 用作记录当前节点要加上edge_list的哪一条边
            for key in temp_dict.keys():
                weight_u_in_c[key] += edge_list[count]
                count = count + 1
        upper_weight = min(weight_u_in_c.values())
        # print(upper_weight)
        return upper_weight
