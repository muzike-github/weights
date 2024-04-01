import networkx as nx

import core.function as fun
import core.fileHandle as fh
import matplotlib.pyplot as plt
import igraph as ig
from matplotlib.font_manager import FontProperties

# 两个case study 的示例图
Glist = fh.csvResolve('../../dataset/facebook.csv')
G = nx.Graph()
G.add_weighted_edges_from(Glist)
BRB = [436, 683, 370, 373, 376, 395, 412, 414, 423, 428]
FPB = [513, 524, 461, 559, 400, 561, 436, 373, 438, 506]

# 创建两个子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))


# 结点过滤
def filter(weights, node):
    del_list = []
    for w in weights.keys():
        if node not in w:
            del_list.append(w)
    for l in del_list:
        del weights[l]
    return weights


# g1_b只画边
g1_B = nx.subgraph(G, BRB)
# 生成节点位置序列（）
pos = nx.circular_layout(g1_B)
# 重新获取权重序列
weights = nx.get_edge_attributes(g1_B, "weight")

# 自定义节点颜色
nodelist = {
    'orange': [414],
    'g': [436],
    '#237ab5': [683, 370, 373, 376, 395, 412, 423, 428]
}
plt.rcParams['font.sans-serif'] = ['SimHei']
# 将边删除
graph1 = nx.Graph(g1_B)  # 解冻,g2只包含节点
graph1.remove_edges_from(Glist)
print(graph1.edges)
# 画节点图
for node_color, nodelist in nodelist.items():
    nx.draw_networkx_nodes(graph1, pos, nodelist=nodelist,
                           node_size=400,
                           node_color=node_color, label=True, ax=ax1)

# 画边
nx.draw_networkx_edges(graph1, pos, edgelist=weights.keys(), width=0.3, alpha=1, ax=ax1)
weights = filter(weights, 414)
# # # 画边权重
nx.draw_networkx_edge_labels(g1_B, pos, edge_labels=weights, ax=ax1)
nx.draw_networkx_labels(g1_B, pos, font_color='black', ax=ax1)
plt.box(False)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.spines['left'].set_visible(False)
# ax1.set_title('(a) community returned by BRB(h=10)', y=-0.1)
# plt.savefig("case1_BRB.svg", dpi=600, bbox_inches='tight')
# g2只画边
g2 = nx.subgraph(G, FPB)
print(g2.edges())
# 生成节点位置序列（）
pos = nx.circular_layout(g2)
# 重新获取权重序列
weights = nx.get_edge_attributes(g2, "weight")
# 自定义节点颜色
nodelist = {
    'orange': [506],  # 最小影响力节点
    'g': [436],  # 查询节点
    '#237ab5': [513, 524, 461, 559, 400, 561, 373, 438]
}
plt.rcParams['font.sans-serif'] = ['Times New Roman']
# 将边删除
graph2 = nx.Graph(g2)  # 解冻,g2只包含节点
graph2.remove_edges_from(Glist)
# # 画节点图
for node_color, nodelist in nodelist.items():
    nx.draw_networkx_nodes(graph2, pos, nodelist=nodelist,
                           node_size=400,
                           node_color=node_color, label=True, ax=ax2)

# # 画边
nx.draw_networkx_edges(graph2, pos, edgelist=list(weights.keys()), width=0.5, alpha=1, ax=ax2)
weights = filter(weights, 506)
# 画边权重
nx.draw_networkx_edge_labels(g2, pos, edge_labels=weights, ax=ax2)
nx.draw_networkx_labels(g2, pos, font_color='black', ax=ax2)
# plt.savefig("case1_FPB.svg", dpi=600, bbox_inches='tight')
# ax2.set_title('(b) community returned by FPB(h=10)', y=-0.1)
plt.box(False)
# 填充空白
plt.tight_layout(pad=0)
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
