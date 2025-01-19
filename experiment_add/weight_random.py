"""
增加一部分实验，一是为无权图随机赋予权值，
将facebook和wikivote两个数据集的权值改为随机赋予
"""
import random

import networkx as nx
import csv


def csv_trans(filename, output_filename):
    Glist = []
    with open(filename) as f:
        render = csv.reader(f)
        header_row = next(render)  # 取表头
        for row in render:
            node1 = int(row[0])
            node2 = int(row[1])
            # 为结点之间的边随机分配权重
            edge_weight = round(random.random(), 3)
            Glist.append((node1, node2, edge_weight))
        f.close()

    # 写入csv文件
    csv_path = '../dataset/' + output_filename
    csv_file = open(csv_path, 'w', encoding='utf-8', newline='')
    csv_write = csv.writer(csv_file)
    # 　开始写入
    for i in Glist:
        # print(list(i))
        csv_write.writerow(list(i))
    return Glist


# 开始转换
input_filename = '../dataset/wiki-vote.csv'
output_filename = 'wiki-vote_random.csv'
csv_trans(input_filename, output_filename)
