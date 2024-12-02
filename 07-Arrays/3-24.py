import random

def rand_elem(array):
    i = random.randint(0, len(array)-1)
    return array[i]


arr=[1,2,3,4,5,"LOL","Amazing!",9821893,21]
print(rand_elem(arr))
print(len(arr))