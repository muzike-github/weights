import random

import networkx as nx

import core.function as fun
import core.fileHandle as fh
import matplotlib.pyplot as plt
import random

i = 1
rate = 0.01
count = 0
while i > 0.1:
    print(i)
    i = i * (1-rate)
    count += 1
print(count)
