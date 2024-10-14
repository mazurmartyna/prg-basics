## Enter price: 24.72
## Enter discount %: 15
## Price with discount: 21.01
## Reduction: 3.71

price = input('Enter price: ')
price = float(price)
discount = input('Enter discount %: ')
discount = int(discount)
pricedisc = price - price * discount / 100
pricedisc = round(pricedisc, 2)
reduction = price - pricedisc
reduction = round(reduction,2)
print(f'Price with discount: {pricedisc}')
print(f'Reduction: {reduction}')