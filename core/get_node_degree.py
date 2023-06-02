# 求出图中各个节点的度数，方便后序实验中固定查询节点
import networkx as nx
import core.fileHandle as fh

'''
nodes:图中节点和边的三元组集合
'''


def get_nodes_degree(filename):
    nodes = fh.csvResolve(filename)
    G = nx.Graph()
    G.add_weighted_edges_from(nodes)
    print("the count of nodes:",len(G.nodes()))
    print("the count of edges:",len(G.edges()))
    dic = {}
    for i in G.nodes:
        dic[i] = nx.degree(G, i)
    sort_list=sorted(dic.items(),key=lambda x:x[1],reverse=True)
    return sort_list


filename = "../dataset/facebook.csv"
node_dic=get_nodes_degree(filename)
print(node_dic)
print(len(node_dic))
