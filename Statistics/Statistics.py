from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.SampleMean import sample_mean
from Statistics.Median import median

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