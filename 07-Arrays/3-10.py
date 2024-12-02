arr = [2, 6, 4, 9, 7]

def star(n):
    result = ''
    for i in range(n):
        result += '*'
    return result

for item in arr:
    print(f"{item}: {star(item)}")
