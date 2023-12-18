import networkx as nx
import random

def calculate_neighbor_weights(graph, current_node, community):
    neighbor_weights = {}
    for neighbor in graph.neighbors(current_node):
        if neighbor in community:
            total_weight = sum(graph[current_node][neighbor].get('weight', 0) for neighbor in community)
            neighbor_weights[neighbor] = total_weight
    return neighbor_weights

def state_dependent_random_walk(graph, start_node, n, iterations):
    current_node = start_node
    marked_nodes = set()

    # 节点贡献值的初始化
    node_contributions = {node: 0 for node in graph.nodes}

    for _ in range(iterations):
        community = set()
        for _ in range(n):
            neighbors = list(graph.neighbors(current_node))
            if not neighbors:
                break

            # 计算每个邻居节点在当前社区中的邻边总权重
            contribution_values = calculate_neighbor_weights(graph, current_node, community)

            # 更新节点贡献值
            for node, weight in contribution_values.items():
                node_contributions[node] += weight

            # 根据贡献值设置选择概率
            probabilities = [node_contributions.get(node, 0) for node in neighbors]
            total_probability = sum(probabilities)
            probabilities = [prob / total_probability for prob in probabilities]

            # 选择下一个节点
            next_node = random.choices(neighbors, weights=probabilities)[0]

            community.add(next_node)
            current_node = next_node

        marked_nodes.update(community)

    return marked_nodes

# 示例图和参数设置
G = nx.Graph()
G.add_edges_from([(1, 2, {'weight': 3}), (1, 3, {'weight': 2}), (2, 4, {'weight': 1}),
                  (3, 4, {'weight': 4}), (3, 5, {'weight': 2}), (4, 5, {'weight': 1})])
start_node = 1
n = 3
iterations = 5

marked_nodes = state_dependent_random_walk(G, start_node, n, iterations)
print("Marked Nodes:", marked_nodes)
