amount = int(input('Enter the amount in PLN: '))
PLN = amount

five_coin= amount//5
amount= amount%5
two_coin = amount//2
amount = amount%2

print(f'The amount of PLN {PLN} in coins:')
print('5 PLN coins: ', five_coin)
print('2 PLN coins: ', two_coin)
print('1 PLN coins: ', amount)