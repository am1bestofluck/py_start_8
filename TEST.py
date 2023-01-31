import random
from literals import NAMES
collection = open(NAMES).read().split('\n')
names = []
for i in range(10):
    names.append(
    random.choice(collection).split()[0]
    + ' '
    + random.choice(collection).split()[1])

print(names)