import time

import networkx as nx
import random
from core import fileHandle
from core import function


def calculate_contribution(graph, partial_solution, candidates):
    """
    计算community中所有节点的邻居节点对community的贡献值（类似于连接分数）
    :param candidates: 下一步的候选节点集
    :param graph: 母图
    :param community: 当前的部分游走序列（看作一个社区）
    :return:以字典形式返回节点的贡献值
    """

    # 计算贡献值
    contributions_values = {node: 0.01 for node in candidates}
    for node in candidates:
        for u in partial_solution:
            if graph.has_edge(node, u):
                contributions_values[node] += graph.get_edge_data(node, u)['weight']
    # print(contributions_values)
    return contributions_values


def update_contributions(graph, partial_solution, join_node):
    """
    加入节点后更新已访问节点的贡献值
    :param graph:
    :param partial_solution:
    :param join_node: 新加入的节点
    :return:
    """
    for u in partial_solution:
        if graph.has_edge(u, join_node):
            # 计算新节点的贡献值
            graph.nodes[u]['node_weight'] += graph.get_edge_data(u, join_node)['weight']
            # 如果部分解中节点有与新节点相连的节点，则更新该节点的贡献值
            graph.nodes[join_node]['node_weight'] += graph.get_edge_data(u, join_node)['weight']
    return graph


def weighted_random_walk(graph, start_node, walk_length, times):
    """
    一次概率随机游走，每次根据候选节点对当前社区的总贡献值来进行概率选择
    :param times: 游走次数
    :param graph:母图
    :param start_node:开始节点
    :param walk_length: 步长
    :return: 一次游走后的序列
    """
    current_node = start_node
    community = []
    # 初始化所有节点的贡献值
    node_contributions = {node: 0 for node in graph.nodes}
    for t in range(times):
        current_node = start_node
        community.append(start_node)
        # 游走步长为设置的社区大小
        for i in range(walk_length*2):
            # 计算邻居节点的贡献值
            # todo 此处邻居节点的选择决定了是否可以回头走，如果选择了当前节点的所有邻居节点，则表示可以回头走
            neighbors = list(graph.neighbors(current_node))
            neighbors = list(set(neighbors).difference(set(community)))
            if not neighbors:
                continue
            candidate_contribution_dic = calculate_contribution(graph, community, neighbors)

            # 根据邻居节点贡献度值选择节点
            probability = list(candidate_contribution_dic.values())
            # 选择下一个节点
            # next_node = random.choices(neighbors, weights=probability)[0]
            next_node = random.choices(neighbors)[0]
            # 更新所选择的节点的贡献值()只更新部分解中节点的贡献值
            graph = update_contributions(graph, community, next_node)
            # 加入节点
            community.append(next_node)
            current_node = next_node
    return graph


def run(G, start_node, size):
    """
    根据游走后的结果选择size-1个节点，每次从部分解的所有邻居节点中中选择一个贡献值最大的节点
    :param G:
    :param start_node:
    :param size:
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
    graph = weighted_random_walk(G, query_node, size, times)
    print("查询节点:", query_node)
    result = run(graph, query_node, size)
    fun = function.Function(graph, query_node)
    print("result:", result,
          "最小影响力：", fun.get_min_weight(result)
          , "最小度：", fun.minDegree(nx.subgraph(graph, result)))
    function.paint(Glist, result, str(nodes[i]))
