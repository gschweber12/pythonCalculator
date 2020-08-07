from Statistics.Mean import mean
from Calculator.Division import division
import math


def median(data):
    num_values = len(data)
    data.sort()

    if num_values % 2 == 0:
        median1 = data[math.floor(division(2, num_values))]
        median2 = data[math.floor(division(2, num_values))-1]
        median_list = [median1, median2]
        return mean(median_list)

    else:
        median = int(data[math.floor(division(2, num_values))])
        return median
