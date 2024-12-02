arr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]] 

i=0
rowN = 0
newRow = []
for row in arr:
    i +=1
    y=1
    for item in row:
        item= i*y
        y=y+1
        newRow.append(item)
    arr[rowN]=newRow
    rowN +=1
    newRow = []

for row in arr:
    for item in row:
        print(item,end=' ')
    print()

