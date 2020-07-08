from Statistics.Mean import mean
from Calculator.Addition import addition
from Calculator.Squared import squared
from Calculator.Subtraction import subtraction
from Calculator.Squareroot import squarerooted
from Calculator.Division import division

def standard_deviation(data):
    avg = mean(data)
    num_values = len(data)
    sd1 = 0
    for num in data:
        sd1 = addition(sd1, squared(subtraction(mean, num)))
    return squarerooted(division(num_values, sd1))

