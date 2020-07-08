def mode(data):
    count_num = dict()
    for num in data:
        if num not in count_num:
            count_num[num] = 1
        else:
            count_num[num] += 1
