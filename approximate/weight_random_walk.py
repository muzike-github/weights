import time

import networkx as nx
import random
from core import fileHandle
from core import function

"""
算法的核心思想：计算节点对查询节点的贡献值，并在新选择一个节点后，更新贡献值，
多次游走，最终将所有节点标记，最后选择权重大的节点
"""


def weighted_random_walk(graph, start_node, walk_length):
    """
    基于邻边进行随机游走
    :param graph: 母图
    :param start_node:起始节点
    :param walk_length: 步长
    :return: 游走序列
    """
    current_node = start_node
    walk = [current_node]
    for _ in range(walk_length - 1):
        neighbors = list(graph.neighbors(current_node))
        if not neighbors:
            break  # 没有相邻节点可选,跳出
        # 根据邻边决定游走概率
        # 计算权重总和
        total_weight = sum(graph[current_node][neighbor]['weight'] for neighbor in neighbors)
        # 根据权重随机选择下一个节点
        probabilities = [graph[current_node][neighbor]['weight'] / total_weight for neighbor in neighbors]
        next_node = random.choices(neighbors, weights=probabilities)[0]
        walk.append(next_node)
        current_node = next_node
    return walk


def calculate_contribution(graph, community):
    """
    计算community中所有节点的邻居节点对community的贡献值（类似于连接分数）
    :param graph: 母图
    :param community: 需要计算的社区的节点集
    :return:以字典形式返回节点的贡献值
    """
    contributions_values = {node: 0 for node in community}
    current_graph = nx.subgraph(graph, community)
    for node in community:
        total_weight = sum(current_graph[node][neighbor].get('weight', 0) for neighbor in current_graph.neighbors(node))
        contributions_values[node] = total_weight
    print(contributions_values)
    return contributions_values


def update_contributions(graph, partial_solution):
    """
    在新加入节点后，更新邻居节点的贡献值,每增加一个节点，都需要更新所有节点的贡献值
    :param node_contributions: 节点贡献值
    :param graph:
    :param partial_solution:
    :return: 更新后的节点贡献值字典
    """
    # 找出需要更新的节点集合
    update_nodes = set()
    for u in partial_solution:
        for nb in nx.neighbors(graph, u):
            update_nodes.add(nb)
    print(update_nodes)
    # 开始更新
    for node in update_nodes:
        print(node, "更新前：", graph.nodes[node]['node_weight'])
        for u in partial_solution:
            if node != u and graph.has_edge(node, u):
                graph.nodes[node]['node_weight'] += graph.get_edge_data(node, u)['weight']
        print(node,"更新后：", graph.nodes[node]['node_weight'])
    return graph


def random_walk_status_dep(graph, start_node, walk_length, times):
    """
    状态依赖随机游走：每一次游走会对之前已经游走过的节点进行更新，每次游走
    :param graph:图
    :param start_node:开始节点
    :param walk_length:步长
    :param times:游走次数
    :return: n次游走后的图
    """
    current_node = start_node
    community = []
    # 初始化所有节点的贡献值
    node_contributions = {node: 0 for node in graph.nodes}
    for t in range(times):
        current_node = start_node
        community.append(start_node)
        for i in range(walk_length):
            # todo 此处为先更新节点的贡献值，再选择节点
            # 更新节点贡献值（只用更新当前节点的所有邻居节点即可）
            graph = update_contributions(graph, community)

            # 根据邻居节点贡献度值选择节点
            neighbors = list(graph.neighbors(current_node))
            probability = [graph.nodes[node]['node_weight'] for node in neighbors]
            total_probability = sum(probability)
            probability = [pro / total_probability for pro in probability]

            # 选择下一个节点
            next_node = random.choices(neighbors, weights=probability)[0]

            # 更新所选择的节点的贡献值
            print("next-node:", next_node)
            community.append(next_node)
            current_node = next_node


def run(G, start_node, size):
    cur = start_node
    result = [start_node]
    for i in range(size):
        next_node = None
        weight = 0
        for nb in nx.neighbors(G, cur):
            if nb in result:
                continue
            else:
                temp_weight = G.nodes[nb]['node_weight'] * G.get_edge_data(cur, nb)['weight']
                if temp_weight > weight:
                    next_node = nb
                    weight = temp_weight
        if next_node is None:
            print("-1")
            exit(-1)
        else:
            cur = next_node
        result.append(next_node)
    return result


# 示例
# Glist = fileHandle.csvResolve("../dataset/wiki-vote.csv")
Glist = [(1, 2, 1), (1, 4, 4), (1, 5, 2), (1, 6, 1), (2, 3, 2),
         (2, 4, 5), (2, 6, 2), (3, 4, 3), (3, 5, 3), (4, 5, 3), (5, 6, 4)]
G = nx.Graph()
G.add_weighted_edges_from(Glist)
nodes_weights = []
# 添加点权重
for i in list(G.nodes):
    nodes_weights.append((i, {'node_weight': 0}))
G.add_nodes_from(nodes_weights)
size = 7
start_node = 1
random_walk_status_dep(G, 1, 4, 1)
# function.paint(Glist, "", "ceshi")
# while True:
#     start_node = int(input("query_node:"))
#     if start_node == -1:
#         break
#     start_time = time.time()
#     # 随机游走（步数为size-1），并对节点进行标记
#     G_modify = train_and_mark(G, start_node, size - 1, 1000)
#     # 根据节点权重选取下一个待选节点
#     # for i in range(10):
#     #     H = run(G_modify, start_node, size)
#     #     print(H)
#     H = run(G_modify, start_node, size - 1)
#     end_time = time.time()
#     fun = function.Function(G, start_node)
#     print("H:", H)
#     print("运算耗时", end_time - start_time)
#     print("社区的最小影响力值", fun.get_min_weight(H),
#           "最小度", fun.minDegree(nx.subgraph(G, H)))
