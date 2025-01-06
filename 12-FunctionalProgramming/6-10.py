temps = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

arr1 = list(map(lambda x: x, temps))

arr2 = list(map(lambda x: temps[x], temps))

x=0
print("Temperatures Recorded in Cities")
print("-------------------------------")
print("Cities")
for item in arr2:
    city = arr1[x]
    print(f"{city:10} | ", end='') 
    x=x+1
    if item > 0:
        print('      ',end='=')
        for i in range(item):
            print('===', end='')
        print('')
    elif item == -1:
        print('   ===')
    else:
        print('======')

print(f"{' ':10} | -2 -1 0  1  2  3  4  5  6  7  8")
print(f'{'Temperatures in ^C':>44}')