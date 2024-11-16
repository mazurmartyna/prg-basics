arr = [34,7,19,4,21,8]

total = 0

i=0
while arr[i] != arr[-1] :
    if arr[i] %2 == 0:
        total = total + arr[i]
    i += 1
else:
    if arr[i] %2 == 0:
        total = total + arr[i]
    print(total)
