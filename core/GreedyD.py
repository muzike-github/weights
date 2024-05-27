import time

import networkx as nx
import matplotlib.pyplot as plt
import fileHandle as fh
import function as fc

'''
Greedy算法
每一步删除当前图中度数最小的节点，当结点数满足大小限制时返回社区
直到该节点属于查询节点集或查询节点集合不再连通
'''


# Glist = [(0, 1, 7), (0, 2, 4), (0, 3, 2), (0, 4, 6), (0, 5, 9),
#          (1, 4, 8), (2, 3, 5), (2, 5, 8), (3, 4, 10),
#          (4, 5, 8), (4, 6, 9), (4, 9, 10),
#          (5, 6, 10), (5, 7, 8), (5, 8, 7),
#          (6, 7, 7), (6, 8, 10), (7, 8, 9), (8, 9, 7)]


# 预处理，只保留与查询节点距离不超过h-1的节点
def pre_byDistance(G, Q, h):
    delete_list = []
    for v in G.nodes:
        if not nx.has_path(G, v, Q) or nx.shortest_path_length(G, v, Q) > h:
            delete_list.append(v)
    for i in delete_list:
        G.remove_node(i)
    return G


# 找到包含查询结点的连通分量
def find_connected_component(graph, query_node):
    connected_components = nx.connected_components(graph)  # 这里假设是无向图
    for component in connected_components:
        if query_node in component:
            return component
    return None


def Greedy(Gx, q, h):
    # graph = pre_byDistance(Gx, q, h)
    graph = Gx
    nodes = list(nx.nodes(graph))  # 获取图的所有节点
    nodes.remove(q)
    #print(nodes)
    print("开始根据距离迭代删除")
    for node in nodes[:]:
        if not nx.has_path(graph, node, q):
            graph.remove_node(node)
            nodes.remove(node)
        elif nx.shortest_path_length(graph, node, q) > 2:
            # print(node,"与结点距离:",nx.shortest_path_length(graph, node, q))
            graph.remove_node(node)
            nodes.remove(node)
            # print("是否还在列表",2625 in nodes)
    print("删除后节点数",len(nodes))
    if 2625 in nodes:
        print("true")
    print("开始根据度数迭代删除")
    # 根据社区大小来进行迭代删除
    while len(nodes) >= h:
        min_degree_node = nodes[0]
        min_degree = nx.degree(graph, min_degree_node)
        # 计算度数最小的结点
        for node in nodes:
            temp_degree = nx.degree(graph, node)
            if temp_degree < min_degree:
                min_degree = temp_degree
                min_degree_node = node
        # 删除度数最小的结点
        graph.remove_node(min_degree_node)
        nodes.remove(min_degree_node)
        # 判断

    return graph.nodes()


def paint_by_graph(G):
    # 生成节点位置序列（）
    pos = nx.circular_layout(G)
    # 重新获取权重序列
    weights = nx.get_edge_attributes(G, "weight")
    # 画节点图
    nx.draw_networkx(G, pos, with_labels=True)
    # 画权重图
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.show()


filename = "../dataset/wiki-vote_random.csv"
Glist = fh.csvResolve(filename)
# facebook
# nodelist = [715, 751, 430, 436, 1026, 1339, 2203, 2336, 2244, 0]
nodelist = [715, 751]
# wikivote
# nodelist = [133, 7, 231, 3073, 25, 1489, 1137, 6596, 813, 1166]
# nodelist = [133, 7, 231, 3073]

for querynode in nodelist:
    G = nx.Graph()
    G.add_weighted_edges_from(Glist)
    print(querynode)
    # paint_by_graph(G)
    start_time = time.time()
    # q = 1339
    result = Greedy(G, querynode, 8)
    end_time = time.time()
    print(result)
    print("runtime:", end_time - start_time)
    fun = fc.Function(G, querynode)
    min_weight = fun.get_min_weight(result)
    min_degree = fun.minDegree(nx.subgraph(G,result))
    print("min_weight", min_weight)
    print("min_degree", min_degree)

    # paint_by_graph(nx.subgraph(G, result))
