arr1= [1,2,3,5]

arr2= [2,3,4,5,6,7,1]
result = True

for item in arr1:
    if not(item in arr2):
        result = False
        break
    

if result == False:
    print("no")
else:
    print("yes")
