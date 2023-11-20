import networkx as nx

import core.function as fun
import core.fileHandle as fh
import core.function as fc
Glist = fh.csvResolve('dataset/bitcoinJa.csv')
# fun.paint(Glist, [], "测试")
# 计算
fun.paint(Glist,[4733, 4704, 4688, 4686, 4684, 4682, 4683],"测试")




