"""
数据处理
    将有向图或是无向图转换为加权图,权值为jaccard系数值
"""
import networkx as nx
import csv


# 处理无权重txt格式数据集，转化为csv格式
def txt_trans_csv(filename, output_filename):
    f = open(filename)
    line = f.readline()
    Glist = []
    t = 0
    while line:
        line = line.strip('\n')  # 处理换行
        node = line.split('\t')  # 数据之间以换行隔开
        # node = line.split(' ')  # 数据之间以空格隔开
        nodeturple = tuple(node)
        Glist.append(nodeturple)
        line = f.readline()
    f.close()
    # 将结果先处理为图，便于计算邻居
    G = nx.Graph()
    G.add_edges_from(Glist)
    nodes_weight_list = []
    # 处理每条边，利用jaccard系数代表两个节点之间的关系
    for e in Glist:
        nbs1 = list(nx.neighbors(G, e[0]))
        nbs2 = list(nx.neighbors(G, e[1]))
        common_neighbors = len(list(set(nbs1) & set(nbs2)))
        jaccard = common_neighbors / (len(nbs2) + len(nbs1) - common_neighbors)
        jaccard = round(jaccard, 3)
        nodes_weight_list.append((e[0], e[1], jaccard))
    # 写入csv文件
    csv_path = 'dataset/' + output_filename
    csv_file = open(csv_path, 'w', encoding='utf-8', newline='')
    csv_write = csv.writer(csv_file)
    # 　开始写入
    for i in nodes_weight_list:
        # print(list(i))
        csv_write.writerow(list(i))

    return nodes_weight_list


# txt_no_weight_trans("dataset/Brightkite_edges.txt", "Brightkite.csv")


# 将带有权重的txt数据集直接转化为csv格式
def txt_weight_trans_csv(filename, output_filename):
    f = open(filename)
    line = f.readline()
    Glist = []
    t = 0
    while line:
        line = line.strip('\n')  # 处理换行
        node = line.split(' ')  # 数据之间以空格隔开
        node_tuple = tuple(node)
        Glist.append(node_tuple)
        line = f.readline()
        # t = t + 1
        # if t > 1000:
        #     break
    f.close()

    # 写入csv文件
    csv_path = 'dataset/' + output_filename
    csv_file = open(csv_path, 'w', encoding='utf-8', newline='')
    csv_write = csv.writer(csv_file)
    # 　开始写入
    for i in Glist:
        csv_write.writerow(list(i))

    return Glist


#  将csv格式数据集的权重转化为jaccard系数
def csv_trans(filename, output_filename):
    Glist = []
    with open(filename) as f:
        render = csv.reader(f)
        header_row = next(render)  # 取表头
        for row in render:
            node1 = int(row[0])
            node2 = int(row[1])
            Glist.append((node1, node2))
        f.close()
    # 将结果先处理为图，便于计算邻居
    G = nx.Graph()
    G.add_edges_from(Glist)
    nodes_weight_list = []
    # 处理每条边，利用jaccard系数代表两个节点之间的关系
    for e in Glist:
        nbs1 = list(nx.neighbors(G, e[0]))
        nbs2 = list(nx.neighbors(G, e[1]))
        common_neighbors = len(list(set(nbs1) & set(nbs2)))
        jaccard = common_neighbors / (len(nbs2) + len(nbs1) - common_neighbors)
        jaccard = round(jaccard, 3)
        # if jaccard==0:
        #     print(len(nbs1),len(nbs2),common_neighbors)
        # jaccard = str(jaccard)
        nodes_weight_list.append((e[0], e[1], jaccard))
    # 写入csv文件
    csv_path = 'dataset/' + output_filename
    csv_file = open(csv_path, 'w', encoding='utf-8', newline='')
    csv_write = csv.writer(csv_file)
    # 　开始写入
    for i in nodes_weight_list:
        # print(list(i))
        csv_write.writerow(list(i))
    return nodes_weight_list


# 将无权图处理为加权图
# txt_no_weight_trans("dataset/facebook.txt", "facebook.csv")
# 将加权图直接处理为csv格式
# txt_weight_trans("dataset/bitcoin2.csv", "bitcoin.csv")
# csv_trans("dataset/bitcoin2.csv", "bitcoin.csv")
# csv_trans("dataset/emailWeight.csv", "emailWeightJa.csv")
# csv_trans("dataset/HR_edges.csv", "HR_edges_ja.csv")
txt_trans_csv("dataset/Brightkite_edges.txt", "Brightkite.csv")
