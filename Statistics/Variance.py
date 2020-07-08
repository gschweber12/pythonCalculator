from Statistics.Mean import mean

def _ss(data, c=None):
    if c is None:
        c = mean(data)
    total = total2 = 0
    for x in data:
        total += (x - c)**2
        total2 += (x - c)
    total -= total2**2/len(data)
    return total


def variance(data, xbar=None):
    if iter(data) is data:
        data = list(data)
    return _ss(data, xbar)/(len(data) - 1)
