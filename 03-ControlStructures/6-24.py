pattern = ''
for i in range(1,10):
    if i<=5:
        pattern = pattern + ' ' + '*'
        print(pattern)
    else:
        if pattern[-1] == ' ':
            pattern = ' ' + pattern[1:-2]
        else: 
            pattern = ' ' + pattern[1:-1]
        print(pattern) 