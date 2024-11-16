import random

arr1 = [3,7,1,0,4]

for item in arr1:
    print(item, end=' ')
print()
print()

arr2 = [
    [2,3],
    [7,1],
    [0,4]
    ]

for row in arr2:
    for item in row:
        print(item, end= ' ')
    print()
print()

arr3 = [7 for i in range(5)]

for item in arr3:
    print(item, end=' ')
print()

print()

arr4 = [i for i in range(1,10)]

for item in arr4:
    print(item, end= ' ')
print()
print()

arr5 = [i*2 for i in range(1,10)]

for item in arr5:
    print(item, end= ' ')
print(), print()

arr6 = [random.randint(1,20) for i in range(10)]
for item in arr6:
    print(item, end= ' ')
print(), print()

arr7 = [[] for i in range(5)]
for item in arr7:
    print(item, end= ' ')
print(), print()

arr8 = [[1 for i in range(2)] for j in range(4)]
for row in arr8:
    for item in row:
        print(item, end= ' ')
    print()
print(), print()

arr9 = [[random.randint(1,20) for i in range(3)] for j in range(5)]
for row in arr9:
    for item in row:
        print(item, end= ' ')
    print()
print(), print()

arr10 = [4,0,3]

for item in arr10:
    print(item, end=' ')
print(), print()

arr11 = [0 for i in range(15)]

for item in arr11:
    print(item, end=' ')
print(), print()

arr12= [random.randint(1,30) for i in range(10)]
for item in arr12:
    print(item, end=' ')
print(), print()

arr13 = [random.randint(0,1) for i in range(20)]
for item in arr13:
    print(item, end=' ')
print(), print()

arr14 = [[False for i in range(2)] for j in range(5)]
for row in arr14:
    for item in row:
        print(item, end= ' ')
    print()
print(), print()



