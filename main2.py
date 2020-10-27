import random
def list_maker(size):
    array = []
    for _ in range(size):
        random_num = random.randint(0, 100)
        array.append(random_num)
    return array
print(list_maker(10))