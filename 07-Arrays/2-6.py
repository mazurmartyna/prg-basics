array = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]

i=0
y=0

for row in array:
    array[y][i] = 1
    i += 1
    y += 1

for row in array:
    for item in row:
        print(item, end=' ')
    print()