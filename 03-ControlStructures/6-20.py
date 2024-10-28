dec_numb = int(input('Enter decimal number: '))
number = dec_numb
remainder = 0
binary = ''
while dec_numb!=0:
    remainder = dec_numb%2 
    dec_numb = dec_numb // 2
    binary = str(remainder) + binary

print(f'{number}(10) = {binary}(2)')
