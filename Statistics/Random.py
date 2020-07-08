def random(start, end, seed):
    random_number = seed.generate_seed()
    random_number = random_number % 1
    random_number = str(random_number)

    if random_number.find('.') != -1:
        random_number = random_number.split('.')[1]

    random_number = int(random_number)
    random_number = random_number % end

    if random_number < start:
        random_number = random_number + start

    return random_number
