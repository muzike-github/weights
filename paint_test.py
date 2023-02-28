import networkx as nx

import core.function as fun
import core.fileHandle as fh

Glist = fh.csvResolve('dataset/bitcoinJa.csv')
fun.paint(Glist, [], "测试")
# fun.paint(Glist,[35, 259, 2565, 6, 7, 20, 28, 271],"测试")




