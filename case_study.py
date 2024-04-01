import networkx as nx

import core.function as fun
import core.fileHandle as fh
import matplotlib.pyplot as plt
import igraph as ig
# 两个case study 的示例图
Glist = fh.csvResolve('dataset/facebook.csv')
G = nx.Graph()
G.add_weighted_edges_from(Glist)


def paint_case1_BRB(H):
    g1 = nx.subgraph(G, H)
    # 生成节点位置序列（）
    pos = nx.circular_layout(g1)
    # 重新获取权重序列
    weights = nx.get_edge_attributes(g1, "weight")

    # 自定义节点颜色
    nodelist = {
        'r': [414],
        'g': [436],
        '#237ab5': [683, 370, 373, 376, 395, 412, 423, 428]
    }
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 将边删除
    g2 = nx.Graph(g1)  # 解冻,g2只包含节点
    g2.remove_edges_from(Glist)
    print(g2.edges)
    # 画节点图
    for node_color, nodelist in nodelist.items():
        nx.draw_networkx_nodes(g2, pos, nodelist=nodelist,
                               node_size=600,
                               node_color=node_color, label=True)

    # 画边
    nx.draw_networkx_edges(g2, pos, edgelist=weights.keys(), width=0.5, alpha=1)
    weights = filter(weights, 414)
    # # # 画边权重
    nx.draw_networkx_edge_labels(g1, pos, edge_labels=weights)
    nx.draw_networkx_labels(g1, pos, font_color='black')
    plt.box(False)
    #plt.savefig("case1_BRB.svg", dpi=600, bbox_inches='tight')
    plt.show()


def paint_case1_FPB(H):
    g1 = nx.subgraph(G, H)
    print(g1.edges())
    # 生成节点位置序列（）
    pos = nx.circular_layout(g1)
    # 重新获取权重序列
    weights = nx.get_edge_attributes(g1, "weight")
    # 自定义节点颜色
    nodelist = {
        'r': [506],  # 最小影响力节点
        'g': [436],  # 查询节点
        '#237ab5': [513, 524, 461, 559, 400, 561, 373, 438]
    }
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 将边删除
    g2 = nx.Graph(g1)  # 解冻,g2只包含节点
    g2.remove_edges_from(Glist)
    # # 画节点图
    for node_color, nodelist in nodelist.items():
        nx.draw_networkx_nodes(g1, pos, nodelist=nodelist,
                               node_size=400,
                               node_color=node_color, label=True)

    # # 画边
    nx.draw_networkx_edges(g1, pos, edgelist=list(weights.keys()), width=0.3, alpha=1)
    weights = filter(weights, 506)
    # 画边权重
    nx.draw_networkx_edge_labels(g1, pos, edge_labels=weights)
    nx.draw_networkx_labels(g1, pos, font_color='black')
    plt.box(False)
    # plt.savefig("case1_FPB.svg", dpi=600, bbox_inches='tight')
    plt.show()


def get_min_weight(G, H):
    graph = nx.subgraph(G, H)
    weights = []
    dic = {}
    for i in graph:
        weight = 0
        for j in nx.neighbors(graph, i):  # 遍历节点的所有邻居
            weight += G.get_edge_data(i, j)['weight']
        weights.append(weight)
        dic[i] = weight
    sorted(dic.items(), key=lambda x: x[0], reverse=False)
    return dic


def filter(weights, node):
    del_list = []
    for w in weights.keys():
        if node not in w:
            del_list.append(w)
    for l in del_list:
        del weights[l]
    return weights


BRB = [436, 683, 370, 373, 376, 395, 412, 414, 423, 428]
FPB = [513, 524, 461, 559, 400, 561, 436, 373, 438, 506]
# dic = get_min_weight(G, H1)
# dic2 = get_min_weight(G, H2)
#
# print(dic)
# print(dic2)

# fun.paint(Glist, [], "测试")
# fun.paint(Glist,[513, 524, 461, 559, 400, 561, 436, 373, 438, 506],"case1_FPB")
# fun.paint(Glist, [436, 683, 370, 373, 376, 395, 412, 414, 423, 428], "case1_BRB")
paint_case1_BRB(BRB)
paint_case1_FPB(FPB)
