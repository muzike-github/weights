import networkx as nx
import core.fileHandle as fh
import core.function as fc
import time


def get_next_node(P, C):
    # c_graph = nx.subgraph(G, C)
    nbs = []  # P的所有邻居节点
    for pi in P:
        for nb in nx.neighbors(G, pi):
            if nb not in P:
                nbs.append(nb)
    p_graph = nx.subgraph(G, P)
    # 求部分解P中的影响力值
    sum_influence = 0
    for i in P:
        sum_influence += fc.get_weight(p_graph, i)
    # 计算候选节点的得分
    node = C[0]
    score = 0
    for ci in nbs:
        ci_p_graph = nx.subgraph(G, list(set(P).union({ci})))
        temp_score = 0
        for pi in P:
            # 如果两个节点不连通，则分数不增加
            if ci not in nx.neighbors(ci_p_graph, pi):
                temp_score += 0
            else:
                temp_score += (sum_influence / fc.get_weight(p_graph, pi)) * (
                    ci_p_graph.get_edge_data(pi, ci)['weight'])
        if temp_score > score:
            score = temp_score
            node = ci
    return node


# 选取第二个节点
def get_second_node(q):
    second_node = None
    second_node_degree = 0
    for i in nx.neighbors(G, q):
        if G.degree(i) > second_node_degree:
            second_node_degree = G.degree(i)
            second_node = i
    return second_node


def run_pagerank(size):
    for i in range(len(query_nodes)):
        query_node = query_nodes[i]
        if query_node == -1:
            break
        H = [query_node]
        pagerank_list = nx.pagerank(G, alpha=0.85)
        cur = query_node
        pagerank_list.pop(cur)
        for i in range(size):
            next_node = None
            next_rank = 0
            for nb in nx.neighbors(G, cur):
                if nb in H:
                    continue
                else:
                    if pagerank_list[nb] > next_rank:
                        next_node = nb
                        next_rank = pagerank_list[nb]
            H.append(next_node)
        fun = fc.Function(G, query_node)
        print("H:", H, "最小影响力值", fun.get_min_weight(H), "最小度:", fun.minDegree(nx.subgraph(G, H)))
    # fc.paint(Glist, H, "测试")


filename = "../dataset/facebook.csv"
Glist = fh.csvResolve(filename)
G = nx.Graph()
G.add_weighted_edges_from(Glist)

# facebook
query_nodes = [715, 751, 430, 436, 1026, 1339, 2203, 2336, 2244, 0]
# wiki-vote
# query_nodes = [133, 7, 231, 3073, 25, 1489, 1137, 6596, 813, 1166]
# bitcoin
# query_nodes = [3, 4553, 4683, 1860, 3598, 3744, 2942, 546, 1018, 905]
start_time = time.time()
end_time = time.time()
run_pagerank(4 - 1)
print("算法运行时间:", round(end_time - start_time, 2))
