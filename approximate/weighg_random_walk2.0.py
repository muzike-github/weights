"""
随机游走算法2.0，可以往回走，
反馈策略：访问节点时，计算节点
"""
import time

import networkx as nx
import random
from core import fileHandle
from core import function


def calculate_contributions(graph, node, query_node, partial_solution):
    """
    计算节点相对于部分解的贡献值 （度数*0.25+边权重*0.5+与start_node相连的边权值*0.25）
    :param graph:
    :param node:
    :return: 节点的贡献值
    """
    # node加入后的新图
    sub_graph = nx.subgraph(graph, list(set(partial_solution).union({node})))
    degree = sub_graph.degree(node)
    weight = 0
    good_weight = 0
    for nb in nx.neighbors(sub_graph, node):
        weight += sub_graph.get_edge_data(nb, node)['weight']
    if sub_graph.has_edge(query_node, node):
        good_weight += sub_graph.get_edge_data(query_node, node)['weight']
    return degree * 0.5 + weight * 0.5


def random_walk(graph, start_node, size, times):
    """
    完全随机游走，并在游走时为节点标记
    :param graph: 图
    :param start_node: 开始节点
    :param walk_length: 步长（当社区大小小于size时一直游走）
    :return: 游走后更新的图
    """
    for i in range(times):
        current_node = start_node
        partial_solution = [start_node]
        while len(partial_solution) < size:
            # 得到候选集并随机选取下一个节点
            candidate = list(nx.neighbors(graph, current_node))
            next_node = random.choices(candidate)[0]
            # 如果节点已经访问过，则不更新节点的贡献值
            if next_node in partial_solution:
                continue
            # 否则计算该节点的综合贡献值并更新
            partial_solution.append(next_node)
            contribution_value = calculate_contributions(graph, next_node, start_node, partial_solution)
            graph.nodes[next_node]['node_weight'] += contribution_value
    return graph


def get_result(G, start_node, size):
    """
    :param G:
    :param start_node:
    :param size: 社区大小
    :return: 结果社区
    """
    result = [start_node]
    # 初始候选节点为start_node的所有邻居节点
    candidate = list(nx.neighbors(G, start_node))
    for i in range(size):
        next_node = None
        weight = 0
        # 取对当前社区来说贡献值最大的一个邻居节点
        for nb in candidate:
            if nb in result:
                continue
            else:
                temp_weight = G.nodes[nb]['node_weight']
                if temp_weight > weight:
                    next_node = nb
                    weight = temp_weight
        if next_node is None:
            print("下一个节点为node，程序退出")
            exit(-1)
        else:
            result.append(next_node)
            candidate.remove(next_node)
        # 更新candidate
        for nb in nx.neighbors(G, next_node):
            if nb not in candidate:
                candidate.append(nb)
    return result


Glist = fileHandle.csvResolve("../dataset/wiki-vote.csv")
G = nx.Graph()
G.add_weighted_edges_from(Glist)
nodes_weights = []
# 添加点权重
for i in list(G.nodes):
    nodes_weights.append((i, {'node_weight': 0}))
G.add_nodes_from(nodes_weights)

# Glist = [(1, 2, 1), (1, 4, 4), (1, 5, 2), (1, 6, 1), (2, 3, 2),
#          (2, 4, 5), (2, 6, 2), (3, 4, 3), (3, 5, 3), (4, 5, 3), (5, 6, 4)]

size = 7
# start_node = 1489
times = 500
nodes = [133, 7, 231, 3073, 25, 1489, 1137, 6596, 813, 1166]
for i in range(len(nodes)):
    query_node = nodes[i]
    graph = random_walk(G, query_node, size, times)
    print("查询节点:", query_node)
    result = get_result(graph, query_node, size)
    fun = function.Function(graph, query_node)
    print("result:", result,
          "最小影响力：", fun.get_min_weight(result)
          , "最小度：", fun.minDegree(nx.subgraph(graph, result)))
    # function.paint(Glist, result, str(nodes[i]))
