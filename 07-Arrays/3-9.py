arr = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

longest = arr[1]

for item in arr:
    if len(item) > len(longest):
        longest = item

print("Names: ",arr)
print("Longest name: ", longest)

