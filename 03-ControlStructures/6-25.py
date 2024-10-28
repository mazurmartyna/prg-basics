pattern = ''
for i in range(1,10):
    for a in range(i):
        pattern = pattern + str(i)
    print(pattern)
    pattern = ''