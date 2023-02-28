import networkx as nx
import core.function as fun

Glist = [(1, 2), (1, 3), (1, 7), (1, 8), (2, 3), (2, 7), (2, 8),(2,9),
         (3, 4), (3, 5),(3,6),(3,8),(3,9),
         (4, 5), (4, 6),(4,9),
         (5,6), (5, 7), (7, 8),(7,9),(8,9)]
G = nx.Graph()
G.add_edges_from(Glist)
Glist_weight = []
for e in Glist:
    nbs1 = list(nx.neighbors(G, e[0]))
    nbs2 = list(nx.neighbors(G, e[1]))
    common_neighbors = len(list(set(nbs1) & set(nbs2)))
    jaccard = common_neighbors / (len(nbs2) + len(nbs1) - common_neighbors)
    jaccard = round(jaccard, 3)
    print(e[0],e[1],jaccard)
    Glist_weight.append((e[0], e[1], jaccard))

if __name__ == '__main__':
    fun.paint(Glist_weight, [], "实例1")
