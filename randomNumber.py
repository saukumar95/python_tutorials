import random

print(random.randint(100, 500))

if random.randint(100, 500) == random.randint(100, 500):
    print('Random numbers are same.')
else:
    print('Not same.')