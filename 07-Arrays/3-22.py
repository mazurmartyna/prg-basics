arr= [7,9,2,4,5,6]
even=[]
odd = []
i=0
for item in arr:
    if item %2 == 0:
        even.append(item)
    else:
        odd.append(item)

arr = even+odd

print(arr)