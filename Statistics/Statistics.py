from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.SampleMean import sample_mean
from Statistics.Median import median
from Statistics.StandardDeviation import standard_deviation
from Statistics.Zscore import z_score
from Statistics.Mode import mode

class Statistics(Calculator):

    def mean(self):
        self.result = mean(self.data)
        return self.result

    def sample_mean(self, sample_size):
        self.result = sample_mean(self.data, sample_size)
        return self.result

    def median(self):
        self.result = median(self.data)
        return self.result
    
    def mode(self):
        self.result = mode(self.data)
        return self.result

    def standard_deviation(self):
        self.result = standard_deviation(self.data)
        return self.result

    def z_score(self, score):
        self.result = z_score( score, self.data)
        return self.result

