import networkx as nx

import core.function as fun
import core.fileHandle as fh

Glist = fh.csvResolve('dataset/Wiki-Vote.csv')
# fun.paint(Glist, [], "测试")
fun.paint(Glist,[5430, 5429, 68, 1549, 2237, 2565, 3352],"测试")




