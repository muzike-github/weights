import time

import networkx as nx
import matplotlib.pyplot as plt
import fileHandle as fh
import function as fc

'''
Greedy算法
每一步删除当前图中度数最小的节点，
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


def Greedy(Gx, Q, h):
    nbs = list(nx.neighbors(Gx, Q))
    # print(nbs)
    Gx = pre_byDistance(Gx, Q, h)
    nodes = list(Gx.nodes)  # 获取图的所有节点
    while True:
        if not nx.is_connected(Gx):
            # 获取包含查询节点的连通分量，
            nodes_new = nx.node_connected_component(Gx, Q)
            #print(len(nodes_new))
            freeze_graph = nx.subgraph(Gx, nodes_new)
            # 生成新的图（此时图属于冻结图，需要解冻后才可以进行修改）
            Gx = nx.Graph(freeze_graph)
            nodes = list(Gx.nodes)  # 更新节点集合nodes
            if Gx is None:
                print("error")
                return None
        if len(Gx.nodes) <= h:
            result = nodes[:]
            return result
        # 遍历所有节点，找出度数最小的
        else:
            v = nodes[len(nodes) - 1]
            if v == Q:
                v = nodes[len(nodes) - 2]
            for i in range(1, len(nodes)):
                if nodes[i] == Q:
                    return nodes
                if Gx.degree(nodes[i]) < Gx.degree(v):
                    v = nodes[i]
            nodes.remove(v)
            Gx.remove_node(v)


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


filename = "../dataset/Wiki-Vote.csv"
Glist = fh.csvResolve(filename)
G = nx.Graph()
G.add_weighted_edges_from(Glist)
# paint_by_graph(G)
start_time = time.time()
Q = 25
result = Greedy(G, Q, 7)
end_time = time.time()
print(result)
print("runtime:", end_time - start_time)
fun = fc.Function(G, Q)
min_weight = fun.get_min_weight(result)
print("min_weight", min_weight)
# paint_by_graph(nx.subgraph(G, result))
