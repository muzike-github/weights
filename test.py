import random
import os
import networkx as nx
import pandas as pd
import openpyxl
import core.function as fun
import core.fileHandle as fh
import matplotlib.pyplot as plt
import random

temperature = 100
count = 0
while temperature > 1:
    print(temperature)
    count += 1
    temperature *= 0.95
print(count)
print("github test")
