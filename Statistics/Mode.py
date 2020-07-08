def mode(data):
    countNum = dict()
    for num in data:
        if num not in countNum:
            countNum[num] = 1
        else:
            countNum[num] += 1
