import heapq
import time

import function as fc
import networkx as nx
import matplotlib.pyplot as plt
import fileHandle as fh


def get_distance(G, q, v):
    dis = nx.shortest_path_length(G, v, q)
    dis = pow(dis, 2)
    return dis


def greedy_F(G, q):
    # 预处理，取距离查询节点最近的k个节点
    # node_list=list(G.nodes())
    # node_list.remove(q)
    dic = {}
    print(list(nx.neighbors(G,q)))
    for u in nx.neighbors(G, q):
        dic[u] = get_distance(G, q, u)
    largest_dic = heapq.nlargest(size-1, dic)
    return list(largest_dic)


filename = "../dataset/facebook.csv"
Glist = fh.csvResolve(filename)
G = nx.Graph()
G.add_weighted_edges_from(Glist)
q = 436
size = 7
start_time=time.time()
H = greedy_F(G, q)
end_time=time.time()
fun=fc.Function(G,q)
total_influence = fun.get_total_weight(nx.subgraph(G,H))
H.append(q)
# 最小影响力
min_influential = fun.get_min_weight(H)
# 最小度
min_degree = fun.minDegree(nx.subgraph(G, H))
print("社区的最小权重", min_influential,
          "最小度", min_degree,
      "总影响力值",total_influence,
      "耗时",end_time-start_time)
print(H)

