import heapq

import networkx as nx
import matplotlib.pyplot as plt
import fileHandle as fh
import function as fc


def get_distance(G, q, v):
    dis = nx.shortest_path_length(G, v, q)
    dis = pow(dis, 2)
    return dis


def greedy_F(G, q):
    # 预处理，取距离查询节点最近的k个节点
    # node_list=list(G.nodes())
    # node_list.remove(q)
    dic = {}
    # print(list(nx.neighbors(G,q)))
    for u in nx.neighbors(G, q):
        dic[u] = get_distance(G, q, u)
    largest_dic = heapq.nlargest(size - 1, dic)
    return list(largest_dic)


filename = "../dataset/facebook.csv"
Glist = fh.csvResolve(filename)
G = nx.Graph()
G.add_weighted_edges_from(Glist)
q = 436
size = 8
H = greedy_F(G, q)
fun = fc.Function(G, q)
print(fun.get_min_weight(H))
print(H)
