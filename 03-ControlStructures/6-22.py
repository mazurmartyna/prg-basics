numbers = ''

for i in range(1,31):
    if i%3 == 0:
        if i%5==0:
            number = 'BINGO'
        else:
            number = 'THREE'
    elif i%5 == 0:
        number = 'FIVE'
    else:
        number = str(i)
    numbers = numbers +' '+ number

print(numbers)
