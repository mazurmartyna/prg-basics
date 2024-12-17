arr =[]

for i in range(1,21):
    arr.append(i)

divisable = lambda x: (x%2 ==0) or (x%3 == 0)

arr_div = list(filter(divisable, arr))

print(arr)
print(arr_div)