from Calculator.Calculator import Calculator
from Statistics.Mean import mean

class Statistics(Calculator):

    def mean(self):
        self.result = mean(self.data)
        return self.result