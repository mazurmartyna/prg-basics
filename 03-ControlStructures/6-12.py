number_of_products = int(input('Number of products purchased: '))
product_price = int(input('Product price: '))
amount=0
if number_of_products > 2:
    amount = (product_price - product_price*25/100) *number_of_products
else:
    amount = number_of_products * product_price

print(f'Amount to pay: {amount}')