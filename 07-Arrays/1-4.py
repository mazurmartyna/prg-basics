arr = [2,3,7,5,4]

print(arr)

print('Number of elements: ', len(arr))
print('First value: ', arr[0])
print('Second value: ', arr[1])
print('Last value: ', arr[-1])
print('Last value again :) :', arr[len(arr)-1])
print('Sum of the first and last value: ', arr[0]+arr[len(arr)-1])
print('Middle value: ', arr[(len(arr)-1)//2])

for element in arr:
    print(element, end=' ')

print('')

for i in range(len(arr)):
    print(arr[i], end=' ')
    arr[i]= arr[i]-1