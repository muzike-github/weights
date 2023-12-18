import datetime
import time


def save_txt(dataset, nodes,edges,queryNode,influential, time_consume, degree):
    time_record = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
    with open("result/result_log.txt", "a", encoding="utf-8") as f:
        f.write("======="+time_record+"========")
        f.write('\n')
        f.write("dataset:" + dataset)
        f.write('\n')
        f.write("nodes:" + str(nodes)+"\t edges:"+str(edges)+"\t queryNode:"+str(queryNode))
        f.write('\n')
        f.write("min_influential:" + str(influential) )
        f.write('\n')
        f.write("time_consume:" + str(time_consume) )
        f.write('\n')
        f.write("min_degree:" + str(degree))
        f.write('\n')
