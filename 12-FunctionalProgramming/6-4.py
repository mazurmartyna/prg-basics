arr =[]

for i in range(1,21):
    arr.append(i)

arr_3 = list(map(lambda x: x*x*x, arr))

print(arr_3)