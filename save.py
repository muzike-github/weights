import datetime
import time


def save_txt(dataset, influential, time_consume, degree):
    time_record = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
    with open("D:/experiment.txt", "a", encoding="utf-8") as f:
        f.write("======="+time_record+"========")
        f.write('\n')
        f.write("dataset:" + dataset)
        f.write('\n')
        f.write("min_influential:" + str(influential) )
        f.write('\n')
        f.write("time_consume:" + str(time_consume) )
        f.write('\n')
        f.write("min_degree:" + str(degree))
        f.write('\n')
