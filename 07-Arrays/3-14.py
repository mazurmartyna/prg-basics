arr = [2,3,2,5,8,1,9,8]

element_count = {}
count = 0

for item in arr:
    for word in arr:
        if item == word:
            count += 1
    element_count[item] = count
    count =0

print("Array: ", arr)
print("Unique elements:", end=' ')
for key, value in element_count.items():
    if value <2:
        print(key, end=' ')