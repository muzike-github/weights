import time

import networkx as nx
import random
from core import fileHandle
from core import function

"""
目前暂时采用该种方式
根据邻居边权重进行加权概率随机游走，通过累加节点的访问次数来计算节点的得分
两种方式
1：完全根据两个节点之间的权重作为概率（会出现查询节点只有一度的情形）
2：需要考虑该节点和查询节点是否有连接，如果当前节点和查询节点有连接，则将分数值将会相应的增大
"""


def get_next_node(graph, current_node):
    """
    计算当前节点选择下一个节点的概率分布,并选择下一个节点
    :param graph:
    :param current_node:
    :return: next_ndoe
    """
    neighbors = list(graph.neighbors(current_node))
    if not neighbors:
        return None
    # 计算总权重
    total_score = 0
    for neighbor in neighbors:
        total_score += graph[current_node][neighbor]['weight']
        # total_score += graph[current_node][neighbor]['weight'] * 0.5 + graph.degree(neighbor) * 0.5
    # 根据总得分计算概率
    probabilities = []
    for neighbor in neighbors:
        score = graph[current_node][neighbor]['weight']
        # score = graph[current_node][neighbor]['weight'] * 0.5 + graph.degree(neighbor) * 0.5
        probabilities.append(score / total_score)
    next_node = random.choices(neighbors, weights=probabilities)[0]
    return next_node


def weighted_random_walk(graph, start_node, walk_length, times):
    """
    基于邻边进行随机游走
    :param times: 游走次数
    :param graph: 母图
    :param start_node:起始节点
    :param walk_length: 步长
    :return: 更新后的图
    """
    for t in range(times):
        current_node = start_node
        walk = [current_node]
        for _ in range(walk_length - 1):
            # 根据邻边决定游走概率
            # 计算权重总和
            next_node = get_next_node(graph, current_node)
            if next_node is None:
                print("游走下一个节点为none,程序退出")
                exit("-1")
            graph.nodes[next_node]['node_weight'] += 1
            walk.append(next_node)
            current_node = next_node
    return graph


def get_result(G, start_node, size):
    """
    选择标记次数最多的几个节点
    :param G:
    :param start_node:
    :param size:
    :return: result
    """
    cur = start_node
    result = [start_node]
    # 初始化候选集为start_node的所有邻居节点
    candidate = list(nx.neighbors(G, start_node))
    for i in range(size):
        next_node = None
        weight = 0
        for nb in candidate:
            if nb in result:
                continue
            else:
                temp_weight = G.nodes[nb]['node_weight']
                if temp_weight > weight:
                    next_node = nb
                    weight = temp_weight
        if next_node is None:
            print("-1")
            exit(-1)
        else:
            result.append(next_node)
            candidate.remove(next_node)
        # 更新candidate
        for nb in nx.neighbors(G, next_node):
            if nb not in candidate:
                candidate.append(nb)
    return result


# 示例
Glist = fileHandle.csvResolve("../../dataset/wiki-vote.csv")
# Glist = [(1, 2, 1), (1, 4, 4), (1, 5, 2), (1, 6, 1), (2, 3, 2),
#          (2, 4, 5), (2, 6, 2), (3, 4, 3), (3, 5, 3), (4, 5, 3), (5, 6, 4)]
G = nx.Graph()
G.add_weighted_edges_from(Glist)
nodes_weights = []
# 添加点权重
for i in list(G.nodes):
    nodes_weights.append((i, {'node_weight': 0}))
G.add_nodes_from(nodes_weights)
size = 4-1  # 社区大小
walk_length = size * 3
# start_node = 1
times = 5000  # 随机游走次数
# facebook
# nodes = [715, 751, 430, 436, 1026, 1339, 2203, 2336, 0]
# wiki-vote
nodes = [133, 7, 231, 3073, 25, 1489, 1137, 6596, 813, 1166]
# bitcoin
# nodes = [3, 4553, 4683, 1860, 3598, 3744, 2942, 546, 1018, 905]



for i in range(len(nodes)):
    query_node = nodes[i]
    # 对每个节点进行10次重复，取最优
    min_weight = 0
    final_result = []
    fun = function.Function(G, query_node)
    print("查询节点:", query_node)
    start_time = time.time()
    # for t in range(5):
    #     graph = weighted_random_walk(G, query_node, size * 2, times)
    #     result = get_result(graph, query_node, size)
    #     print("result",result)
    #     # print(result)
    #     if fun.get_min_weight(result) >= min_weight:
    #         min_weight = fun.get_min_weight(result)
    #         final_result = result
    graph = weighted_random_walk(G, query_node, size * 4, times)
    end_time = time.time()
    final_result = get_result(graph, query_node, size)
    print("result:", final_result,
          "最小影响力：", fun.get_min_weight(final_result)
          , "最小度：", fun.minDegree(nx.subgraph(G, final_result)),
          "runtime:", round(end_time - start_time))
    # function.paint(Glist, final_result, str(nodes[i]))
