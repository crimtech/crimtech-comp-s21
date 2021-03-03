import random

arr = []
while(True):
    rand_int = random.randint(1, 10)
    arr.append(rand_int)
    if rand_int == 7:
        break
print(arr)
