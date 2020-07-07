from Statistics.Mean import mean
from Calculator.Division import division

def median(data):
    num_values = len(data)
    data.sort()

    if num_values %2 == 0:
        median1 = data[division(2, num_values)]
        median2 = data[division(2, num_values)-1]
        medianList = [median1, median2]
        return mean(medianList)

    else:
        median = int(data[division(2, num_values)])
        return median

