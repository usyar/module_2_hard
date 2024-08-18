import random

result = ''


def random_number():
    number = range(3, 21)
    random_ = random.choice(number)
    return random_


random_ = random_number()
for i in range(1, random_):
    for j in range(i + 1, random_):
        if random_ % (i + j) == 0:
            result += f'{i}{j}'
print(f'{random_} - {result}')
