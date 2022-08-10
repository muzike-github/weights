import networkx as nx

import core.function as fun
import core.fileHandle as fh

Glist = fh.csvResolve('dataset/wiki-vote.csv')
# fun.paint(Glist, [], "测试")
# fun.paint(Glist,[35, 259, 2565, 6, 7, 20, 28, 271],"测试")

graph=nx.Graph()
c=[]
graph.add_weighted_edges_from(Glist)
for i in nx.connected_components(graph):
    c=list(i)[:]
    print(c)
    print()


