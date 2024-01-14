import time
import os
import networkx as nx
import random
import math
from core import function
from core import fileHandle
import pandas as pd
import openpyxl


def get_weight_score(G, C, R):
    copy_c = C.copy()  # 用copyC 代替C的所有操作,否则求完连接分数后C会改变
    score_dict = {}  # 字典保存R中每个节点的连接分数
    for v in R:
        graph_c = nx.subgraph(G, copy_c)  # 得到图C
        copy_c.append(v)
        graph_c_and_v = nx.subgraph(G, copy_c)  # 得到节点集C∪{v}的在G中的子图
        score = 0
        # 此处判断v是否在C∪{v}中是否有邻居，没有邻居，分数为0
        if len(list(nx.neighbors(graph_c_and_v, v))) != 0:
            # 有邻居但邻居在C中度为0，则设置score为0
            for i in nx.neighbors(graph_c_and_v, v):  # 得到v(v∈R)在C∪{v}所有的邻居节点
                if graph_c.degree(i) != 0:
                    score += (1 / graph_c.degree(i))
                    score = round(score, 2)
                else:
                    score = 0
        # 如果v没有邻居，则直接分数为0
        else:
            score = 0
        score_dict[v] = score  # 将对应节点的连接分数存储
        copy_c.remove(v)  # 节点v测试完毕，移除
    # scoreMaxNode = max(score_dict, key=score_dict.get)
    return score_dict


def initial_solution(graph, query_node, size):
    """
    初始化一个包含种子节点的社区,(使用连接分数算法)
    :param graph:
    :param query_node:
    :param size:
    :return: 初始解
    """
    partial_solution = [query_node]
    # 候选节点，每次加入新节点，都把所有的邻居节点加入进去（去重）
    candidate = list(nx.neighbors(graph, query_node))
    # 取第二个节点（query_node邻居节点中度数最大的那个）
    degree = 0
    second_node = None
    # print(len(list(nx.neighbors(graph, query_node))))
    for i in nx.neighbors(graph, query_node):
        if graph.degree(i) > degree:
            degree = graph.degree(i)
            second_node = i
    if second_node is None:
        print("第二个节点为空，有问题")
        exit(-1)
    partial_solution.append(second_node)
    # print("第二个节点:", second_node)
    # print("partial", partial_solution)
    # print(partial_solution)
    # print("candidate:", candidate)
    # 开始选取剩下的节点
    while len(partial_solution) < size:
        # 找出G\partial_solution中连接分数最大的节点V*
        candidate = list(set(graph.nodes).difference(set(partial_solution)))
        score_dict = get_weight_score(graph, partial_solution, candidate)
        next_node = max(score_dict, key=score_dict.get)
        partial_solution.append(next_node)
    print("初始解：", partial_solution)
    return partial_solution


'''
graph:母图
community：需要计算最小影响力的社区的节点集合
'''


def calculate_community_weight(graph, community):
    # 计算社区内边的权重之和
    community_graph = nx.subgraph(graph, community)
    weights = []
    dic = {}
    for i in community_graph:
        weight = 0
        for j in nx.neighbors(community_graph, i):  # 遍历节点的所有邻居
            weight += G.get_edge_data(i, j)['weight']
        weights.append(weight)
        dic[i] = weight
    sorted(dic.items(), key=lambda x: x[0], reverse=False)
    return min(weights)


def get_node_weight(graph, community, node):
    '''
    得到node在community中的权重
    :param graph:
    :param community:
    :param node:
    :return: 权重
    '''
    graph_part = nx.subgraph(graph, community)
    weight = 0
    for u in nx.neighbors(graph_part, node):
        weight += G.get_edge_data(u, node)['weight']
    return weight


def get_min_node(graph, community):
    '''
    移除当前社区中影响力最小的节点
    :param graph:
    :param community:
    :return: 返回最小的节点
    '''
    node = community[0]
    min_weight = float("inf")
    for u in community:
        temp_weight = get_node_weight(graph, community, u)
        if temp_weight < min_weight:
            min_weight = temp_weight
            node = u
    return node


def simulated_annealing(graph, query_node, size, initial_temperature, min_temperature, cooling_rate, iterations):
    current_solution = initial_solution(graph, query_node, size)
    current_weight = calculate_community_weight(graph, current_solution)
    best_solution = current_solution.copy()
    best_weight = current_weight

    print("初始解最小影响力值:", fun.get_min_weight(current_solution), "最小度",
          fun.minDegree(nx.subgraph(G, best_solution)))

    temperature = initial_temperature
    while temperature > min_temperature:
        # 对每次温度进行迭代
        for _ in range(iterations):
            new_solution = current_solution.copy()
            # 对当前解进行进行随机扰动得到新解，这里从社区中随机选择一个节点移除，并随机选择一个新节点加入社区
            # todo 此处以何种方式来移除节点和新加入节点？（先使用完全随机）
            # 移除节点（随机移除）
            # remove_node = random.choice(list(set(new_solution).difference({query_node})))
            # 移除影响力最小的节点
            remove_node = get_min_node(graph, new_solution)
            if remove_node == query_node:
                # continue
                remove_node = random.choice(list(set(new_solution).difference({query_node})))
            new_solution.remove(remove_node)
            # 增加节点
            candidate_neighbors = []
            for v in new_solution:
                for nb in nx.neighbors(graph, v):
                    if nb not in new_solution:
                        candidate_neighbors.append(nb)
            append_node = random.choice(list(candidate_neighbors))
            # print(append_node)
            new_solution.append(append_node)

            new_weight = calculate_community_weight(graph, new_solution)
            # 根据接受概率决定是否接受新解,
            dE = new_weight - current_weight

            # 如果产生更优结果，则接受新解，
            if dE > 0:
                current_solution = new_solution
                current_weight = new_weight
                # 如果新解优于最优结果，则更新最优值
                if current_weight > best_weight:
                    best_solution = current_solution.copy()
                    best_weight = current_weight
                    print("更新社区，影响力为：", best_weight)
            # 否则，根据概率选择是否接受新解
            else:
                # print("接受概率：", math.exp(dE / temperature), "random:", random.random())
                if random.random() < math.exp(dE / temperature):
                    # print("接受较差解", math.exp(dE / temperature))
                    current_solution = new_solution
                    current_weight = new_weight
            # 降低温度
        temperature *= cooling_rate  # 线性降温
        # temperature = temperature * cooling_rate  # 指数降温
        # print("temperature:",temperature)

    return best_solution, best_weight


def log(query_node, result_community, weight, degree):
    with open("result/log_simulated_annealing.txt", "a", encoding="utf-8") as f:
        f.writelines("==================参数==================")
        f.writelines("初始上限：" + str(initial_temperature))
        f.writelines("温度下限：" + str(min_temperature))
        f.writelines("冷却速率：" + str(cooling_rate))
        f.writelines("每个温度的迭代次数：" + str(iterations))
        f.writelines("社区大小：" + str(size))
        f.writelines("查询节点：" + str(query_node))
        f.writelines("结果社区：" + str(result_community))
        f.writelines("最小影响力值:" + str(weight))
        f.writelines("最小度：" + str(degree))


def write_to_excel(record_filename, algorithm_parameters, weights, degrees,
                   compare_weights, compare_degrees, initial_temperature, runtime_one_node):
    # 判断文件是否存在，文件不存在则创建(使用openpyxl)
    if not os.path.exists(record_filename):
        wb = openpyxl.Workbook()
        wb.save(record_filename)

    # 读取原文件内容
    df = pd.read_excel(record_filename, index_col=0, engine="openpyxl")
    # 增加头部(模拟退火的参数)
    head = algorithm_parameters
    df = df._append(head)
    # 增加数据
    data = pd.DataFrame([compare_weights, weights, compare_degrees, degrees, runtime_one_node],
                        index=['FPB_w', 'sa_w' + str(initial_temperature), 'FPB_d', 'sa_d', 'runtime'])
    df = df._append(data, ignore_index=False)
    # 写入
    df.to_excel(record_filename, sheet_name="Sheet2", index=True, engine="openpyxl")
    # 写入空行


def run(query_nodes):
    weights = []
    degrees = []
    runtime_node = []
    for i in range(len(query_nodes)):
        # query_node = int(input("查询节点:"))
        query_node = query_nodes[i]
        print("查询节点：", query_node, "度数为：", nx.degree(G, query_node))
        if query_node == -1:
            break
        start_time = time.time()
        best_community, best_weight = simulated_annealing(G, query_node, size, initial_temperature, min_temperature,
                                                          cooling_rate, iterations)
        best_degree = fun.minDegree(nx.subgraph(G, best_community))
        end_time = time.time()
        print("Best Community:", best_community, "w:", best_weight, "d:", best_degree)
        print("耗时：", end_time - start_time)
        weights.append(best_weight)
        degrees.append(best_degree)
        runtime_node.append(round(end_time - start_time, 0))
        # paint
        function.paint(Glist, best_community, str(runtime_node[i]))
    return weights, degrees, runtime_node


# 数据预处理，移除距离大于size-1的节点
def pre_byDistance(G, q, size):
    delete_list = []
    for v in G.nodes:
        if not nx.has_path(G, v, q) or nx.shortest_path_length(G, v, q) > int(size / 2):
            delete_list.append(v)
    for i in delete_list:
        G.remove_node(i)
    return G


# 创建一个简单的图
G = nx.Graph()

# filename = "bitcoin.csv"
# record_filename = "bitcoin.xlsx"

filename = "Brightkite.csv"
record_filename = "./result/Brightkite_100.xls"
Glist = fileHandle.csvResolve("../dataset/" + filename)
G.add_weighted_edges_from(Glist)

# 写入文件参数

# facebook
# query_nodes = [715, 751, 430, 436, 1026, 1339, 2203, 2336, 2244, 0]
# wiki-vote
# query_nodes = [133, 7, 231, 3073, 25, 1489, 1137, 6596, 813, 1166]
# bitcoin
# query_nodes = [3, 4553, 4683, 1860, 3598, 3744, 2942, 546, 1018, 905]
query_nodes = [1, 2, 3]

# 温度为[100,300,600,1000,1500,2000,3000]

# temperatures = [100, 300, 600, 1000, 1500, 2000, 3000]
temperatures = [100]
for i in range(len(temperatures)):
    # 设置退火算法参数
    initial_temperature = temperatures[i]
    print("当前温度", initial_temperature)
    min_temperature = 1
    cooling_rate = 0.95
    iterations = 100
    cool_type = "非线性"
    size = 7

    # 初始化类
    print("原始节点数：", len(G.nodes()))
    fun = function.Function(G, -1)
    G = pre_byDistance(G, i, size)
    print("修剪后节点数：", len(G.nodes()))

    start_time = time.time()
    weights, degrees, runtime_node = run(query_nodes)
    end_time = time.time()
    runtime = end_time - start_time
    # 算法参数
    algorithm_parameter = pd.DataFrame(
        [['initial_temperature', 'min_temperature', 'cooling_rate', 'iterations', 'size', 'filename', 'cool-type',
          'runtime'],
         [initial_temperature, min_temperature, cooling_rate, iterations, size, filename, cool_type, runtime]],
        index=['parameter', 'value'])
    # 增加单个节点的计算时间

    # 精确解（facebook）
    # compare_weights = [1.233, 1.211, 2.118, 2.91, 2.27, 3.154, 3.386, 4.215, 5.299, 1.236]
    # compare_degrees = [4, 4, 6, 6, 6, 6, 6, 6, 6, 6]
    # # 精确解（wiki-vote）
    # compare_weights = [0.083, 0.377, 0.497, 0.71, 1.069, 1.162, 0.869, 1.13, 1.214, 1.527]
    # compare_degrees = [3, 4, 5, 5, 6, 6, 5, 6, 6, 6]
    # 精确解（bitcoin）
    compare_weights = [0.365, 0.662, 3.774, 0.588, 0.659, 0.96, 0.844, 0.618, 0.72, 0.84]
    compare_degrees = [4, 6, 6, 6, 5, 6, 6, 5, 6, 6]
    write_to_excel(record_filename, algorithm_parameter, weights, degrees, compare_weights, compare_degrees,
                   initial_temperature, runtime_node)

