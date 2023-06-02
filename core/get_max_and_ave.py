import networkx as nx
import core.fileHandle as fh


def get_max_and_ave(filename):
    nodes = fh.csvResolve(filename)
    G = nx.Graph()
    G.add_weighted_edges_from(nodes)
    degree_list = []
    sum_degree = 0
    for i in G.nodes:
        degree_i = nx.degree(G, i)
        sum_degree += degree_i
        degree_list.append(degree_i)
    print("max:", max(degree_list))
    print("ave:", sum_degree / len(G.nodes))


get_max_and_ave("../dataset/HR_edges_ja.csv")
