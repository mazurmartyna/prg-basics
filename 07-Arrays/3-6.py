arr= [ -15, 8, -31, 47, -2, 19]

smallest = arr[0]

largest = arr[1]

for item in arr:
    if item <= smallest:
        smallest = item
    elif item >= largest:
        largest = item

print(f"Minimum: {smallest}, Maximum: {largest}")