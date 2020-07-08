from Calculator.Subtraction import subtraction
from Statistics.Mean import mean
from Calculator.Division import division
from Statistics.StandardDeviation import standard_deviation


def z_score(test_score, data):
    x = subtraction(mean(data), test_score)
    return division(standard_deviation(data), x)
